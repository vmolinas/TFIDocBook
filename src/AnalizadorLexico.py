import ply.lex as lex
import sys
import warnings

warnings.filterwarnings("ignore")

tokens = ("INICIO", "TEXTO", "VIDIMALINK", "URL", "TAG", "ALINK", "CLINK", "DOCTYPE", "AARTICLE", "CARTICLE", "ATITLE", "CTITLE", "AINFO", "CINFO", "AABSTRACT", "CABSTRACT", "AAUTHOR", "CAUTHOR", "APERSONNAME", "CPERSONNAME", "AFIRSTNAME", "CFIRSTNAME", "ASURNAME", "CSURNAME", "ADATE", "CDATE", "AYEAR", "CYEAR", "ACOPYRIGHT", "CCOPYRIGHT", "AADDRESS", "CADDRESS", "ACITY", "CCITY", "ASTATE", "CSTATE", "APOSTCODE", "CPOSTCODE", "ASTREET", "CSTREET", "AEMAIL", "CEMAIL", "APHONE", "CPHONE", "ASECTION", "CSECTION",
          "ASIMPLESECT", "CSIMPLESECT", "AITEMIZEDLIST", "CITEMIZEDLIST", "ALISTITEM", "CLISTITEM", "AEMPHASIS", "CEMPHASIS", "APARA", "CPARA", "ASIMPARA", "CSIMPARA", "ACOMMENT", "CCOMMENT", "AIMPORTANT", "CIMPORTANT", "AINFORMALTABLE", "CINFORMALTABLE", "ATGROUP", "CTGROUP", "ATHEAD", "CTHEAD", "ATFOOT", "CTFOOT", "ATBODY", "CTBODY", "AROW", "CROW", "AENTRY", "CENTRY", "AENTRYTBL", "CENTRYTBL", "AHOLDER", "CHOLDER", "AMEDIAOBJECT", "CMEDIAOBJECT", "AVIDEOOBJECT", "CVIDEOOBJECT", "AIMAGEOBJECT", "CIMAGEOBJECT")
# <para>|<title>|<info>|<abstract>|<author>|<personname>|<firstname>|<surname>|<date>|<year>|<copyright>|<address>|<city>|<state>|<postcode>|<street>|<email>|<phone>|<section>|<simplesect>|<itemizedlist>|<listitem>|<emphasis>|<para>|<simpara>|<comment>|<important>|<informaltable>|<tgroup>|<thead>|<tfoot>|<tbody>|<row>|<entry>|<entrytbl>|<holder>|<mediaobject>|<videoObject>|<ImageObject>'

# def t_TAG(t):
#     r'<([a-z]+)( [a-z]+="[^"]*")*>|<\/[a-z]+>'
#     return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_blank(t):
    r'(\s)+'
    # Espacios, salto de linea y tabulacion
    # No se devuelve este token porque no afecta al leer


def t_URL(t):
    r'(http|ftp)(s)?://[^<>&\s]+' 
    return t


def t_VIDIMALINK(t):
    r'<(?:imagedata|videodata|link)\s+(fileref|xlink:href)\s*=\s*"((http|ftp)(s)?://)?[^<>&]*([[^<>&]+:[^<>&]+?]?[[\\[^<>&]]+?[#[^<>&]+]?])?"[/]?>'
    return t
#      <link xlink:href = “URI”>ETICOM4<link>


def t_APARA(t):
    r'<para>'
    return t


def t_CPARA(t):
    r'</para>'
    return t


def t_ASIMPARA(t):
    r'<simpara>'
    return t


def t_CSIMPARA(t):
    r'</simpara>'
    return t


def t_AARTICLE(t):
    r'<article>'
    return t


def t_CARTICLE(t):
    r'</article>'
    return t


def t_AINFO(t):
    r'<info>'
    return t


def t_CINFO(t):
    r'</info>'
    return t


def t_ATITLE(t):
    r'<title>'
    return t


def t_CTITLE(t):
    r'</title>'
    return t


def t_AABSTRACT(t):
    r'<abstract>'
    return t


def t_CABSTRACT(t):
    r'</abstract>'
    return t


def t_AAUTHOR(t):
    r'<author>'
    return t


def t_CAUTHOR(t):
    r'</author>'
    return t


def t_APERSONNAME(t):
    r'<personname>'
    return t


def t_CPERSONNAME(t):
    r'</personname>'
    return t


def t_AFIRSTNAME(t):
    r'<firstname>'
    return t


def t_CFIRSTNAME(t):
    r'</firstname>'
    return t


def t_ASURNAME(t):
    r'<surname>'
    return t


def t_CSURNAME(t):
    r'</surname>'
    return t


def t_ADATE(t):
    r'<date>'
    return t


def t_CDATE(t):
    r'</date>'


def t_AYEAR(t):
    r'<year>'
    return t


def t_CYEAR(t):
    r'</year>'
    return t


def t_ACOPYRIGHT(t):
    r'<copyright>'
    return t


def t_CCOPYRIGHT(t):
    r'</copyright>'
    return t


def t_AADDRESS(t):
    r'<address>'
    return t


def t_CADDRESS(t):
    r'</address>'
    return t


def t_ACITY(t):
    r'<city>'
    return t


def t_CCITY(t):
    r'</city>'
    return t


def t_ASTATE(t):
    r'<state>'
    return t


def t_CSTATE(t):
    r'</state>'
    return t


def t_APOSTCODE(t):
    r'<postcode>'
    return t


def t_CPOSTCODE(t):
    r'</postcode>'
    return t


def t_ASTREET(t):
    r'<street>'
    return t


def t_CSTREET(t):
    r'</street>'
    return t


def t_AEMAIL(t):
    r'<email>'
    return t


def t_CEMAIL(t):
    r'</email>'
    return t


def t_APHONE(t):
    r'<phone>'
    return t


def t_CPHONE(t):
    r'</phone>'
    return t


def t_ASECTION(t):
    r'<section>'
    return t


def t_CSECTION(t):
    r'</section>'
    return t


def t_ASIMPLESECTION(t):
    r'<simplesection>'
    return t


def t_CSIMPLESECTION(t):
    r'</simplesection>'
    return t


def t_AITEMIZEDLIST(t):
    r'<itemizedlist>'
    return t


def t_CITEMIZEDLIST(t):
    r'</itemizedlist>'
    return t


def t_ALISTITEM(t):
    r'<listitem>'
    return t


def t_CLISTITEM(t):
    r'</listitem>'
    return t


def t_AEMPHASIS(t):
    r'<emphasis>'
    return t


def t_CEMPHASIS(t):
    r'</emphasis>'
    return t


def t_ACOMMENT(t):
    r'<comment>'
    return t


def t_CCOMMENT(t):
    r'</comment>'
    return t


def t_AIMPORTANT(t):
    r'<important>'
    return t


def t_CIMPORTANT(t):
    r'</important>'
    return t


def t_AINFORMALTABLE(t):
    r'<informaltable>'
    return t


def t_CINFORMALTABLE(t):
    r'</informaltable>'
    return t


def t_ATGROUP(t):
    r'<tgroup>'
    return t


def t_CTGROUP(t):
    r'</tgroup>'
    return t


def t_ATHEAD(t):
    r'<thead>'
    return t


def t_CTHEAD(t):
    r'</thead>'
    return t


def t_ATFOOT(t):
    r'<tfoot>'
    return t


def t_CTFOOT(t):
    r'</tfoot>'
    return t


def t_ATBODY(t):
    r'<tbody>'
    return t


def t_CTBODY(t):
    r'</tbody>'
    return t


def t_AROW(t):
    r'<row>'
    return t


def t_CROW(t):
    r'</row>'
    return t


def t_AENTRY(t):
    r'<entry>'
    return t


def t_CENTRY(t):
    r'</entry>'
    return t


def t_AENTRYBL(t):
    r'<entrybl>'
    return t


def t_CENTRYBL(t):
    r'</entrybl>'
    return t


def t_AHOLDER(t):
    r'<holder>'
    return t


def t_CHOLDER(t):
    r'</holder>'
    return t


def t_AMEDIAOBJECT(t):
    r'<mediaobject>'
    return t


def t_CMEDIAOBJECT(t):
    r'</mediaobject>'
    return t


def t_AVIDEOOBJECT(t):
    r'<videoObject>'
    return t


def t_CVIDEOOBJECT(t):
    r'</videoObject>'
    return t


def T_AIMAGEOBJECT(t):
    r'<ImageObject>'
    return t


def T_CIMAGEOBJECT(t):
    r'</ImageObject>'
    return t


def t_DOCTYPE(t):
    r'<\!DOCTYPE[\s]+ (article|book|chapter)[\s]*>'
    return t


def t_INICIO(t):
    r'<\?xml[\ ]+(version[\ ]*=[\ ]*\"\d.\d\" [\ ]+)?(encoding[\ ]*=[\ ]*\" [\S]+ \"[\ ]*)? \?>'
    return t


def t_TEXTO(t):
    r'[^<>&]+'
    # EL TEXTO ENCUENTRA TODO SALVO ESTOS "< >" CARACTERES QUE SON INVALIDOS PARA CUALQUIER TEXTO Y URL
    return t


# def t_ALINK(t):
#     r'<link xlink:href\s*=\s*[/]?>?'
#     return t


def t_CLINK(t):
    r'</link>'
    return t


notrecognized = list()


def t_error(t):
    print("se encontró el siguiente token no reconocible ", t.value[0])
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
            print("ingrese el nombre del archivo")
            entra = input()
            f = open(entra, "r")
            entradaDoc = f.read()
        else:
            print("ingrese una opcion valida")
            quit()

    lexer.input(entradaDoc)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

    input("presione enter para salir")
