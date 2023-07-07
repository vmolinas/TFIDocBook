import sys
import ply.lex as lex
import warnings
import os
warnings.filterwarnings("ignore")

tokens = ("INICIO", "TEXTO","VIDIMALINK", "DOCTYPE", "AARTICLE", "CARTICLE", "ATITLE", "CTITLE", "AINFO", "CINFO",
          "AABSTRACT", "CABSTRACT", "AAUTHOR", "CAUTHOR", "AFIRSTNAME", "CFIRSTNAME", "ASURNAME", "CSURNAME",
          "ADATE", "CDATE", "AYEAR", "CYEAR", "ACOPYRIGHT", "CCOPYRIGHT", "AADDRESS", "CADDRESS", "ACITY", "CCITY", "ASTATE", "CSTATE",
          "ASTREET", "CSTREET", "AEMAIL", "CEMAIL", "APHONE", "CPHONE", "ASECTION", "CSECTION", "ASIMPLESECT",
          "CSIMPLESECT", "AITEMIZEDLIST", "CITEMIZEDLIST", "ALISTITEM", "CLISTITEM", "AEMPHASIS", "CEMPHASIS", "APARA", "CPARA", "ASIMPARA",
          "CSIMPARA", "ACOMMENT", "CCOMMENT", "AIMPORTANT", "CIMPORTANT", "AINFORMALTABLE", "CINFORMALTABLE", "ATGROUP", "CTGROUP", "ATHEAD",
          "CTHEAD", "ATFOOT", "CTFOOT", "ATBODY", "CTBODY", "AROW", "CROW", "AENTRY", "CENTRY", "AENTRYTBL", "CENTRYTBL", "AHOLDER", "CHOLDER",
          "AMEDIAOBJECT", "CMEDIAOBJECT", "AVIDEOOBJECT", "CVIDEOOBJECT", "AIMAGEOBJECT", "CIMAGEOBJECT")

entradaDoc = ""
entra = ""
salida = "out.html"

def search_files(folder, extension):
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(dirpath, filename))
    return files

if len(sys.argv) > 1:  # se ingresó un comando al ejecutar el programa
    entra = sys.argv[1]
    f = open(entra, 'r')
    salida = entra.split('.')[0] + '.html'
    entradaDoc = f.read()
else:
    print("Ingrese 1 para ingresar un docbook por consola y 2 para ingresarlo por archivo")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese el código por teclado.")
        print("Para terminar, presione Ctrl+Z en Windows o Ctrl+D en sistemas UNIX/Linux")
        while True:
            try:
                entra = input('> ')
                entradaDoc += entra + '\n'
            except EOFError:
                break
    elif opcion == 2:
        while True:
            print("Ingrese el nombre/dirección de la carpeta:")
            folder = input()
            files = search_files(folder, ".xml")
            if len(files) == 0:
                print("No se encontraron archivos en la carpeta especificada.")
                continue
            print("Archivos encontrados:")
            for i, f in enumerate(files):
                print(f"{i+1}. {f}")
            print("Ingrese el número del archivo que desea seleccionar:")
            file_num = int(input())
            if file_num < 1 or file_num > len(files):
                print("Número de archivo inválido.")
                continue
            entra = files[file_num - 1]
            f = open(entra, "r", encoding="utf-8")
            salida = entra.split('.')[0] + '.html'
            entradaDoc = f.read()
            break
    else:
        print("Ingrese una opción válida.")
        quit()

file = open(salida, 'w')
validoA = True
validoC = True

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_blank(t):
    r'(\s)+'

def t_VIDIMALINK(t):
    r'<(?:imagedata|videodata|link)\s+(fileref|xlink:href)\s*=\s*"((http|ftp)(s)?://)?[^<>&]*([[^<>&]+:[^<>&]+?]?[[\\[^<>&]]+?[#[^<>&]+]?])?"\s*[/]?>'
    if t.value.split('=')[0]  == '<imagedata fileref':
        file.write("<img src = "+t.value.split('=')[1] + '</img>')
    else:
        file.write("<a href = "+t.value.split('=')[1])
    return(t)

def t_APARA(t):
    r'<para>'
    file.write("<p>")
    return (t)

def t_CPARA(t):
    r'</para>'
    file.write("</a></p>")
    return (t)

def t_ASIMPARA(t):
    r'<simpara>'
    file.write("<p>")
    return (t)

def t_CSIMPARA(t):
    r'</simpara>'
    file.write("</p>")
    return (t)

def t_AARTICLE(t):
    r'<article>'
    file.write('<p>')
    return (t)

def t_CARTICLE(t):
    r'</article>'
    file.write("</p></body></html>")
    return (t)

def t_AINFO(t):
    r'<info>'
    file.write('<div style="background-color: green; color: white; font-size: 8pt;"><p>')
    return (t)

def t_CINFO(t):
    r'</info>'
    file.write('</p></div>')
    return (t)

def t_ATITLE(t):
    r'<title>'
    global validoA
    if validoA:
        file.write("<h1>")
        validoA = False
    else:
        file.write("<h2>")
    return (t)

def t_CTITLE(t):
    r'</title>'
    global validoC
    if validoC:
        file.write("</h1>")
        validoC = False
    else:
        file.write("</h2>")
    return (t)

def t_AABSTRACT(t):
    r'<abstract>'
    return (t)

def t_CABSTRACT(t):
    r'</abstract>'
    return (t)

def t_AAUTHOR(t):
    r'<author>'
    return (t)

def t_CAUTHOR(t):
    r'</author>'
    return (t)

def t_AFIRSTNAME(t):
    r'<firstname>'
    file.write(' ')
    return (t)

def t_CFIRSTNAME(t):
    r'</firstname>'
    return (t)

def t_ASURNAME(t):
    r'<surname>'
    file.write(' ')
    return (t)

def t_CSURNAME(t):
    r'</surname>'
    return (t)

def t_ADATE(t):
    r'<date>'
    file.write(' ')
    return (t)

def t_CDATE(t):
    r'</date>'
    return (t)

def t_AYEAR(t):
    r'<year>'
    file.write(' ')
    return (t)

def t_CYEAR(t):
    r'</year>'
    return (t)

def t_ACOPYRIGHT(t):
    r'<copyright>'
    file.write(' ')
    return (t)

def t_CCOPYRIGHT(t):
    r'</copyright>'
    return (t)

def t_AADDRESS(t):
    r'<address>'
    file.write(' ')
    return (t)

def t_CADDRESS(t):
    r'</address>'
    return (t)

def t_ACITY(t):
    r'<city>'
    file.write(' ')
    return (t)

def t_CCITY(t):
    r'</city>'
    return (t)

def t_ASTATE(t):
    r'<state>'
    file.write(' ')
    return (t)

def t_CSTATE(t):
    r'</state>'
    return (t)

def t_ASTREET(t):
    r'<street>'
    file.write(' ')
    return (t)

def t_CSTREET(t):
    r'</street>'
    return (t)

def t_AEMAIL(t):
    r'<email>'
    file.write(' ')
    return (t)

def t_CEMAIL(t):
    r'</email>'
    return (t)

def t_APHONE(t):
    r'<phone>'
    file.write(' ')
    return (t)

def t_CPHONE(t):
    r'</phone>'
    return (t)

def t_ASECTION(t):
    r'<section>'
    file.write('<p>')
    return (t)

def t_CSECTION(t):
    r'</section>'
    file.write('<p>')
    return (t)

def t_ASIMPLESECTION(t):
    r'<simplesection>'
    return (t)

def t_CSIMPLESECTION(t):
    r'</simplesection>'
    return (t)

def t_AITEMIZEDLIST(t):
    r'<itemizedlist>'
    file.write('<ul>')
    return (t)

def t_CITEMIZEDLIST(t):
    r'</itemizedlist>'
    file.write('</ul>')
    return (t)

def t_ALISTITEM(t):
    r'<listitem>'
    file.write('<li>')
    return (t)

def t_CLISTITEM(t):
    r'</listitem>'
    file.write('</li>')
    return (t)

def t_AEMPHASIS(t):
    r'<emphasis>'
    return (t)

def t_CEMPHASIS(t):
    r'</emphasis>'
    return (t)

def t_ACOMMENT(t):
    r'<comment>'
    return (t)

def t_CCOMMENT(t):
    r'</comment>'
    return (t)

def t_AIMPORTANT(t):
    r'<important>'
    file.write('<div style="background-color: red; color: white;">')
    return (t)

def t_CIMPORTANT(t):
    r'</important>'
    file.write('</div>')
    return (t)

def t_AINFORMALTABLE(t):
    r'<informaltable>'
    file.write('<table style="border:1xp solid black">')
    return (t)

def t_CINFORMALTABLE(t):
    r'</informaltable>'
    file.write('</table>')
    return (t)

def t_ATGROUP(t):
    r'<tgroup>'
    return (t)

def t_CTGROUP(t):
    r'</tgroup>'
    return (t)

def t_ATHEAD(t):
    r'<thead>'
    file.write('<thead>')
    return (t)

def t_CTHEAD(t):
    r'</thead>'
    file.write('</thead>')
    return (t)

def t_ATFOOT(t):
    r'<tfoot>'
    return (t)

def t_CTFOOT(t):
    r'</tfoot>'
    return (t)

def t_ATBODY(t):
    r'<tbody>'
    file.write('<tbody>')
    return (t)

def t_CTBODY(t):
    r'</tbody>'
    file.write('</tbody>')
    return (t)

def t_AROW(t):
    r'<row>'
    file.write('<tr>')
    return (t)

def t_CROW(t):
    r'</row>'
    file.write('</tr>')
    return (t)

def t_AENTRY(t):
    r'<entry>'
    file.write('<td>')
    return (t)

def t_CENTRY(t):
    r'</entry>'
    file.write('</td>')
    return (t)

def t_AENTRYBL(t):
    r'<entrybl>'
    file.write('<th>')
    return (t)

def t_CENTRYBL(t):
    r'</entrybl>'
    file.write('</th>')
    return (t)

def t_AHOLDER(t):
    r'<holder>'
    return (t)

def t_CHOLDER(t):
    r'</holder>'
    return (t)

def t_AMEDIAOBJECT(t):
    r'<mediaobject>'
    return (t)

def t_CMEDIAOBJECT(t):
    r'</mediaobject>'
    return (t)

def t_AVIDEOOBJECT(t):
    r'<videoobject>'
    return (t)

def t_CVIDEOOBJECT(t):
    r'</videoobject>'
    return (t)

def t_AIMAGEOBJECT(t):
    r'<imageobject>'
    return (t)

def t_CIMAGEOBJECT(t):
    r'</imageobject>'
    return (t)

def t_DOCTYPE(t):
    r'<\!DOCTYPE[\s]+ (article|book|chapter)[\s]*>'
    file.write("<!DOCTYPE html><html><head></head><body>")
    return (t)

def t_INICIO(t):
    r'<\?xml[\ ]+(version[\ ]*=[\ ]*\"\d.\d\" [\ ]+)?(encoding[\ ]*=[\ ]*\" [\S]+ \"[\ ]*)? \?>'
    return (t)

def t_TEXTO(t):
    r'[^<>&]+'
    file.write(t.value)
    return(t)
notrecognized = list()

def t_error(t):
    print("Token no reconocido: ", t.value + " [Linea:", t.lineno, "]")
    t.lexer.skip(1)

lexer = lex.lex(debug=0)  # debug=1 si queremos ver q hace internamente