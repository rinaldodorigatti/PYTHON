from datetime import datetime as dt


def main():
    """
    Type    Meaning
    d       Decimal integer
    c       Corresponding Unicode character
    b       Binary format
    o       Octal format
    x       Hexadecimal format (lower case)
    X       Hexadecimal format (upper case)
    n       Same as 'd'. Except it uses current locale setting for number separator
    e       Exponential notation. (lowercase e)
    E       Exponential notation (uppercase E)
    f       Displays fixed point number (Default: 6)
    F       Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
    g       General format. Rounds number to p significant digits. (Default precision: 6)
    G       Same as 'g'. Except switches to 'E' if the number is large.
    %       Percentage. Multiples by 100 and puts % at the end.
    """

    numero = 45
    numero_format_b = format(numero, 'b')
    numero_format_f = format(numero, 'f')
    numero_format_p = format(numero, '%')
    numero_format_o = format(numero, 'o')
    numero_format_x = format(numero, 'x')
    numero_format_c = format(numero, 'c')
    print(f'Binary : {numero_format_b}')
    print(f'Float  : {numero_format_f}')
    print(f'Perce  : {numero_format_p}')
    print(f'Octal  : {numero_format_o}')
    print(f'Hexa   : {numero_format_x}')
    print(f'Char   : {numero_format_c}')

    txt = "For only {price:.2f} dollars"
    print(txt.format(price = 44.55))

    txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
    txt2 = "My name is {0}, I'm {1}".format("John",36)
    txt3 = "My name is {}, I'm {}".format("John",36)
    txt4 = "My name is {0:>20} and my surname id {1:>20}".format("Rinaldo", "Rickyd")
    txt5 = "My name is {0:_<15} and my surname id {1:,<15}".format("Rinaldo", "Rickyd")
    txt6 = "My name is {0:_^16}".format("Rinaldo")
    txt7 = "My PI   is {:06.2f}".format(3.141592653589793)
    print(txt1), print(txt2), print(txt3), print(txt4), print(txt5), print(txt6)
    print(txt7)

    data = {'first': 'un', 'last': 'ten'}
    print("F => {first} L => {last}".format(**data))
    print("F => %(first)s L => %(last)s" % data)

    person = {'Ville': 'Renens', 'Adresse': 'Rue de Lausanne'}
    print("Ville = {p[Ville]} Adresse = {p[Adresse]}".format(p=person))
    print("Ville = {p[Ville]:_>20} \nAdresse = {p[Adresse]:_>30}".format(p=person))

    data2 = [2, 4, 6, 8, 10]
    print("d0 = {d[0]} d2 = {d[2]}".format(d=data2))

    data3 = [2.25, 4.45, 6.65, 8.85, 1.15]
    print("d0 = {d[0]} d2 = {d[2]}".format(d=data3))

    datet = '{:%Y-%m-%d %H:%M}'.format(dt(2001, 2, 3, 4, 5))
    print(datet)

    precision = '{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
    print(precision)

    dtt = dt(2001, 2, 3, 4, 5)
    print('{:{dfmt} {tfmt}}'.format(dtt, dfmt='%Y-%m-%d', tfmt='%H:%M'))


if __name__ == '__main__':
    main()
