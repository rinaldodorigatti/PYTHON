import tarfile
import getopt
import sys
import re
import hashlib
import psycopg2
import magic
import os
import shutil

wanted_mime = ['application/x-executable', 'application/x-object', 'application/x-sharedlib']


def get_priority(f, mime):
    filename = f.name[1:]
    perm = f.mode

    if filename == '/bin/busybox':
        return 0

    score = 0
    score += mime_exam(mime)
    score += permission_exam(perm)
    score += filename_exam(filename)
    return score


def mime_exam(mime):
    for x in wanted_mime:
        if x in mime:
            return 50
    return 0


def filename_exam(filename):
    score = 0

    if filename.endswith('.a'):
        score += 10

    if filename.startswith('/home/'):
        score += 10
    elif filename.startswith('/lib/'):
        score += 20
    elif filename.startswith('/usr/bin/'):
        score += 20
    elif filename.startswith('/usr/local/bin/'):
        score += 20

    return score


def permission_exam(perm):
    if perm & 73:
        return 10
    else:
        return 0


def get_type(t, f):
    path = '/tmp/tar2db_evaluate'
    if not os.path.isdir(path):
        os.makedirs(path)
    t.extract(f, path)

    m = magic.open(magic.MAGIC_MIME)
    m.load()
    return m.file(path + f.name[1:])


def getfilehashes(infile):
    t = tarfile.open(infile)
    files = list()
    links = list()
    for f in t.getmembers():
        if f.isfile():
            mime = get_type(t, f)
            # we use f.name[1:] to get rid of the . at the beginning of the path
            files.append((f.name[1:], hashlib.md5(t.extractfile(f).read()).hexdigest(),
                          f.uid, f.gid, f.mode, mime, get_priority(f, mime)))
        elif f.issym():
            links.append((f.name[1:], f.linkpath))
    shutil.rmtree('/tmp/tar2db_evaluate')
    return files, links


def getoids(objs, cur):
    # hashes ... all the hashes in the tar file
    hashes = [x[1] for x in objs]
    hashes_str = ",".join(["""'%s'""" % x for x in hashes])
    query = """SELECT id,hash FROM object WHERE hash IN (%s)"""
    cur.execute(query % hashes_str)
    res = [(int(x), y) for (x, y) in cur.fetchall()]

    existinghashes = [x[1] for x in res]
    missinghashes = set(hashes).difference(set(existinghashes))
    newobjs = createobjects(missinghashes, cur)

    res += newobjs

    result = dict([(y, x) for (x, y) in res])
    return result


def createobjects(hashes, cur):
    query = """INSERT INTO object (hash) VALUES (%(hash)s) RETURNING id"""
    res = list()
    for h in set(hashes):
        cur.execute(query, {'hash': h})
        oid = int(cur.fetchone()[0])
        res.append((oid, h))
    return res


def insertobjecttoimage(iid, files2oids, links, cur):
    query = """INSERT INTO object_to_image (iid, oid, filename, regular_file, uid, gid, permissions, mime, score) 
    VALUES (%(iid)s, %(oid)s, %(filename)s, %(regular_file)s, %(uid)s, %(gid)s, %(mode)s, %(mime)s, %(score)s)"""

    cur.executemany(query, [{'iid': iid, 'oid': x[1], 'filename': x[0][0],
                             'regular_file': True, 'uid': x[0][1],
                             'gid': x[0][2], 'mode': x[0][3], 'mime': x[0][4],
                             'score': x[0][5]} for x in files2oids])
    cur.executemany(query, [{'iid': iid, 'oid': 1, 'filename': x[0],
                             'regular_file': False, 'uid': None,
                             'gid': None, 'mode': None, 'mime': None, 'score': 0} for x in links])


def process(iid, infile):
    dbh = psycopg2.connect(database="firmware", user="firmadyne",
                           password="firmadyne", host="127.0.0.1")
    cur = dbh.cursor()

    (files, links) = getfilehashes(infile)
    oids = getoids(files, cur)
    fdict = dict([(h, (filename, uid, gid, mode, mime, score)) for (filename, h, uid, gid, mode, mime, score) in files])

    file2oid = [(fdict[h], oid) for (h, oid) in oids.items()]
    insertobjecttoimage(iid, file2oid, links, cur)

    dbh.commit()
    dbh.close()


def getarch(infile):
    if os.path.isfile('../scripts/getArch.sh'):
        os.system('../scripts/getArch.sh {0}'.format(infile))
    elif os.path.isfile('./scripts/getArch.sh'):
        os.system('./scripts/getArch.sh {0}'.format(infile))
    else:
        print('cannot find getArch.sh')
        sys.exit(1)


def main():
    infile = iid = None
    opts, argv = getopt.getopt(sys.argv[1:], "f:i:")
    for k, v in opts:
        if k == '-i':
            iid = int(v)
        if k == '-f':
            infile = v

    if infile and not iid:
        m = re.match(r"(\d+)\.tar\.gz", infile)
        if m:
            iid = int(m.groups(1))

    getarch(infile)
    process(iid, infile)


if __name__ == "__main__":
    main()
