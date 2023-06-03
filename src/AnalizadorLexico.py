import ply.lex as lex
import sys
import warnings

warnings.filterwarnings("ignore")

tokens = ("INICIO", "TEXTO", "VIDIMALINK", "URI", "TAG", "CLINK", "DOCTYPE", "AARTICLE", "CARTICLE", "ATITLE", "CTITLE", "AINFO", "CINFO",
          "AABSTRACT", "CABSTRACT", "AAUTHOR", "CAUTHOR", "APERSONNAME", "CPERSONNAME", "AFIRSTNAME", "CFIRSTNAME", "ASURNAME", "CSURNAME",
          "ADATE", "CDATE", "AYEAR", "CYEAR", "ACOPYRIGHT", "CCOPYRIGHT", "AADDRESS", "CADDRESS", "ACITY", "CCITY", "ASTATE", "CSTATE",
          "APOSTCODE", "CPOSTCODE", "ASTREET", "CSTREET", "AEMAIL", "CEMAIL", "APHONE", "CPHONE", "ASECTION", "CSECTION", "ASIMPLESECT",
          "CSIMPLESECT", "AITEMIZEDLIST", "CITEMIZEDLIST", "ALISTITEM", "CLISTITEM", "AEMPHASIS", "CEMPHASIS", "APARA", "CPARA", "ASIMPARA",
          "CSIMPARA", "ACOMMENT", "CCOMMENT", "AIMPORTANT", "CIMPORTANT", "AINFORMALTABLE", "CINFORMALTABLE", "ATGROUP", "CTGROUP", "ATHEAD",
          "CTHEAD", "ATFOOT", "CTFOOT", "ATBODY", "CTBODY", "AROW", "CROW", "AENTRY", "CENTRY", "AENTRYTBL", "CENTRYTBL", "AHOLDER", "CHOLDER",
          "AMEDIAOBJECT", "CMEDIAOBJECT", "AVIDEOOBJECT", "CVIDEOOBJECT", "AIMAGEOBJECT", "CIMAGEOBJECT", "ASECT1", "CSECT1")

# Mensaje por defecto para mostrar en la salida
def imprimirMensaje(t):
    print("*Etiqueta reconocida: " + t.value + " [Linea:" , t.lineno,"]")

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Espacios, salto de linea y tabulacion
# No se devuelve este token porque no afecta al leer
def t_blank(t):
    r'(\s)+'

def t_URI(t):
    '(http|ftp)(s)?://[^<>&]*([[^<>&]+:[^<>&]+?]?[[\\[^<>&]]+?[#[^<>&]+]?])?'
    print("*Reconocido URL: " + t.value + " [Linea:" , t.lineno,"]")

def t_VIDIMALINK(t):
    r'<(?:imagedata|videodata|link)\s+(fileref|xlink:href)\s*=\s*"((http|ftp)(s)?://)?[^<>&]*([[^<>&]+:[^<>&]+?]?[[\\[^<>&]]+?[#[^<>&]+]?])?"[/]?>'
    print("*Reconocido URL: " + t.value + " [Linea:" , t.lineno,"]")
    # protocolo://dominio:puerto/ruta#fragmento
    # <link xlink:href = “URI”>ETICOM4</link>

def t_APARA(t):
    r'<para>'
    imprimirMensaje(t)

def t_CPARA(t):
    r'</para>'
    imprimirMensaje(t)

def t_ASECT1(t):
    r'<sect1>'
    imprimirMensaje(t)

def t_CSECT1(t):
    r'</sect1>'
    imprimirMensaje(t)

def t_ASIMPARA(t):
    r'<simpara>'
    imprimirMensaje(t)

def t_CSIMPARA(t):
    r'</simpara>'
    imprimirMensaje(t)

def t_AARTICLE(t):
    r'<article>'
    imprimirMensaje(t)

def t_CARTICLE(t):
    r'</article>'
    imprimirMensaje(t)

def t_AINFO(t):
    r'<info>'
    imprimirMensaje(t)

def t_CINFO(t):
    r'</info>'
    imprimirMensaje(t)

def t_ATITLE(t):
    r'<title>'
    imprimirMensaje(t)

def t_CTITLE(t):
    r'</title>'
    imprimirMensaje(t)

def t_AABSTRACT(t):
    r'<abstract>'
    imprimirMensaje(t)

def t_CABSTRACT(t):
    r'</abstract>'
    imprimirMensaje(t)

def t_AAUTHOR(t):
    r'<author>'
    imprimirMensaje(t)

def t_CAUTHOR(t):
    r'</author>'
    imprimirMensaje(t)

def t_APERSONNAME(t):
    r'<personname>'
    imprimirMensaje(t)

def t_CPERSONNAME(t):
    r'</personname>'
    imprimirMensaje(t)

def t_AFIRSTNAME(t):
    r'<firstname>'
    imprimirMensaje(t)

def t_CFIRSTNAME(t):
    r'</firstname>'
    imprimirMensaje(t)

def t_ASURNAME(t):
    r'<surname>'
    imprimirMensaje(t)

def t_CSURNAME(t):
    r'</surname>'
    imprimirMensaje(t)

def t_ADATE(t):
    r'<date>'
    imprimirMensaje(t)

def t_CDATE(t):
    r'</date>'
    imprimirMensaje(t)

def t_AYEAR(t):
    r'<year>'
    imprimirMensaje(t)

def t_CYEAR(t):
    r'</year>'
    imprimirMensaje(t)

def t_ACOPYRIGHT(t):
    r'<copyright>'
    imprimirMensaje(t)

def t_CCOPYRIGHT(t):
    r'</copyright>'
    imprimirMensaje(t)

def t_AADDRESS(t):
    r'<address>'
    imprimirMensaje(t)

def t_CADDRESS(t):
    r'</address>'
    imprimirMensaje(t)

def t_ACITY(t):
    r'<city>'
    imprimirMensaje(t)

def t_CCITY(t):
    r'</city>'
    imprimirMensaje(t)

def t_ASTATE(t):
    r'<state>'
    imprimirMensaje(t)

def t_CSTATE(t):
    r'</state>'
    imprimirMensaje(t)

def t_APOSTCODE(t):
    r'<postcode>'
    imprimirMensaje(t)

def t_CPOSTCODE(t):
    r'</postcode>'
    imprimirMensaje(t)

def t_ASTREET(t):
    r'<street>'
    imprimirMensaje(t)

def t_CSTREET(t):
    r'</street>'
    imprimirMensaje(t)

def t_AEMAIL(t):
    r'<email>'
    imprimirMensaje(t)

def t_CEMAIL(t):
    r'</email>'
    imprimirMensaje(t)

def t_APHONE(t):
    r'<phone>'
    imprimirMensaje(t)

def t_CPHONE(t):
    r'</phone>'
    imprimirMensaje(t)

def t_ASECTION(t):
    r'<section>'
    imprimirMensaje(t)

def t_CSECTION(t):
    r'</section>'
    imprimirMensaje(t)

def t_ASIMPLESECTION(t):
    r'<simplesection>'
    imprimirMensaje(t)

def t_CSIMPLESECTION(t):
    r'</simplesection>'
    imprimirMensaje(t)

def t_AITEMIZEDLIST(t):
    r'<itemizedlist>'
    imprimirMensaje(t)

def t_CITEMIZEDLIST(t):
    r'</itemizedlist>'
    imprimirMensaje(t)

def t_ALISTITEM(t):
    r'<listitem>'
    imprimirMensaje(t)

def t_CLISTITEM(t):
    r'</listitem>'
    imprimirMensaje(t)

def t_AEMPHASIS(t):
    r'<emphasis>'
    imprimirMensaje(t)

def t_CEMPHASIS(t):
    r'</emphasis>'
    imprimirMensaje(t)

def t_ACOMMENT(t):
    r'<comment>'
    imprimirMensaje(t)

def t_CCOMMENT(t):
    r'</comment>'
    imprimirMensaje(t)

def t_AIMPORTANT(t):
    r'<important>'
    imprimirMensaje(t)

def t_CIMPORTANT(t):
    r'</important>'
    imprimirMensaje(t)

def t_AINFORMALTABLE(t):
    r'<informaltable>'
    imprimirMensaje(t)

def t_CINFORMALTABLE(t):
    r'</informaltable>'
    imprimirMensaje(t)

def t_ATGROUP(t):
    r'<tgroup>'
    imprimirMensaje(t)

def t_CTGROUP(t):
    r'</tgroup>'
    imprimirMensaje(t)

def t_ATHEAD(t):
    r'<thead>'
    imprimirMensaje(t)

def t_CTHEAD(t):
    r'</thead>'
    imprimirMensaje(t)

def t_ATFOOT(t):
    r'<tfoot>'
    imprimirMensaje(t)

def t_CTFOOT(t):
    r'</tfoot>'
    imprimirMensaje(t)

def t_ATBODY(t):
    r'<tbody>'
    imprimirMensaje(t)

def t_CTBODY(t):
    r'</tbody>'
    imprimirMensaje(t)

def t_AROW(t):
    r'<row>'
    imprimirMensaje(t)

def t_CROW(t):
    r'</row>'
    imprimirMensaje(t)

def t_AENTRY(t):
    r'<entry>'
    imprimirMensaje(t)

def t_CENTRY(t):
    r'</entry>'
    imprimirMensaje(t)

def t_AENTRYBL(t):
    r'<entrybl>'
    imprimirMensaje(t)

def t_CENTRYBL(t):
    r'</entrybl>'
    imprimirMensaje(t)

def t_AHOLDER(t):
    r'<holder>'
    imprimirMensaje(t)

def t_CHOLDER(t):
    r'</holder>'
    imprimirMensaje(t)

def t_AMEDIAOBJECT(t):
    r'<mediaobject>'
    imprimirMensaje(t)

def t_CMEDIAOBJECT(t):
    r'</mediaobject>'
    imprimirMensaje(t)

def t_AVIDEOOBJECT(t):
    r'<videoobject>'
    imprimirMensaje(t)

def t_CVIDEOOBJECT(t):
    r'</videoobject>'
    imprimirMensaje(t)

def T_AIMAGEOBJECT(t):
    r'<imageobject>'
    imprimirMensaje(t)

def T_CIMAGEOBJECT(t):
    r'</imageobject>'
    imprimirMensaje(t)

def t_DOCTYPE(t):
    r'<\!DOCTYPE[\s]+ (article|book|chapter)[\s]*>'
    imprimirMensaje(t)

def t_INICIO(t):
    r'<\?xml[\ ]+(version[\ ]*=[\ ]*\"\d.\d\" [\ ]+)?(encoding[\ ]*=[\ ]*\" [\S]+ \"[\ ]*)? \?>'
    imprimirMensaje(t)

def t_TEXTO(t):
    r'[^<>&]+'
    print("*Reconocido texto: " + t.value + " [Linea:" , t.lineno,"]")

def t_CLINK(t):
    r'</link>'
    imprimirMensaje(t)

notrecognized = list()

def t_error(t):
    # print("Se encontró el siguiente token no reconocible ", t.value[0])
    print("Token no reconocido: ", t.value + " [Linea:" , t.lineno,"]")
    t.lexer.skip(1)

lexer = lex.lex(debug=0)  # debug=1 si queremos ver q hace internamente

if __name__ == '__main__':
    # si empieza en espacios vacios es invalido el docbook
    # si encuentra los siguientes caracteres es invalido: & < >1
    entradaDoc = ""
    if (len(sys.argv) > 1):  # se ingreso un comando agregado con este programa
        f = open(sys.argv[1], 'r')
        entradaDoc = (f.read())
    else:
        print(
            "Ingrese 1 para ingresar un docbook por consola y 2 para ingresarlo por archivo")
        opcion = int(input())
        if opcion == 1:
            print(
                "Escriba el docbook, una vez terminado apriete CTRL+D(linux) o CTRL+Z(windows)")
            entra = ""
            while (True):
                try:  # tomamos el input asi porque el profesor quiere que termine la ejecucion cuando apretemos CTRL+D
                    entra = input()
                    entradaDoc += entra
                except EOFError:
                    break
        elif opcion == 2:
            print("Ingrese el nombre/direccion del archivo")
            entra = input()
            f = open(entra, "r")
            entradaDoc = f.read()
        else:
            print("Ingrese una opcion valida")
            quit()

    lexer.input(entradaDoc)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

    input("Presione ENTER para salir")