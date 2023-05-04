#!/usr/bin/python3

from tqdm import tqdm
import os

def copy_with_progress(src, dst):
    size = os.path.getsize(src)
    with open(src, 'rb') as fsrc:
        with open(dst, 'wb') as fdst:
            with tqdm(total=size, unit='B', unit_scale=True, desc=f'Copying {src} to {dst}') as pbar:
                while True:
                    chunk = fsrc.read(4096)
                    if not chunk:
                        break
                    fdst.write(chunk)
                    pbar.update(len(chunk))


source = "FILES/spyder.sh"
destination = "FILES2/spyder.sh"
copy_with_progress(source, destination)