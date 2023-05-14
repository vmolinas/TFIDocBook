import ply.lex as lex 
import sys 
import warnings
warnings.filterwarnings("ignore")

tokens=("INICIO","TEXTO","RUTA","URL","TAG","DOCTYPE","ATAG","CTAG","APARA","CPARA","ATITLE","CTITLE","AINFO","CINFO","AABSTRACT","CABSTRACT","AAUTHOR","CAUTHOR","APERSONNAME","CPERSONNAME","AFIRSTNAME","CFIRSTNAME","ASURNAME","CSURNAME","ADATE","CDATE","AYEAR","CYEAR","ACOPYRIGHT","CCOPYRIGHT","AADDRESS","CADDRESS","ACITY","CCITY","ASTATE","CSTATE","APOSTCODE","CPOSTCODE","ASTREET","CSTREET","AEMAIL","CEMAIL","APHONE","CPHONE","ASECTION","CSECTION","ASIMPLESECT","CSIMPLESECT","AITEMIZED")
#<para>|<title>|<info>|<abstract>|<author>|<personname>|<firstname>|<surname>|<date>|<year>|<copyright>|<address>|<city>|<state>|<postcode>|<street>|<email>|<phone>|<section>|<simplesect>|<itemizedlist>|<listitem>|<emphasis>|<para>|<simpara>|<comment>|<important>|<informaltable>|<tgroup>|<thead>|<tfoot>|<tbody>|<row>|<entry>|<entrytbl>|<holder>|<mediaobject>|<videoObject>|<ImageObject>'

# def t_TAG(t):
#     r'<([a-z]+)( [a-z]+="[^"]*")*>|<\/[a-z]+>'
#     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_blank(t):
    r'(\s)+'
    #Espacios, salto de linea y tabulacion
    #No se devuelve este token porque no afecta al leer

def t_URl(t) :
    '(http|ftp)(s)?://[^<>&]*([[^<>&]+:[^<>&]+?]?[[\\[^<>&]]+?[#[^<>&]+]?])?'
    return t

def t_APARA(t) :
    r'<para>|<title>|<info>|<abstract>|<author>|<personname>|<firstname>|<surname>|<date>|<year>|<copyright>|<address>|<city>|<state>|<postcode>|<street>|<email>|<phone>|<section>|<simplesect>|<itemizedlist>|<listitem>|<emphasis>|<para>|<simpara>|<comment>|<important>|<informaltable>|<tgroup>|<thead>|<tfoot>|<tbody>|<row>|<entry>|<entrytbl>|<holder>|<mediaobject>|<videoObject>|<ImageObject>'          
    return t

def t_CPARA(t):
    r'</para>'
    return t
    
def t_AARTICLE(t):
    r'<article>'
    return t

def t_CARTICLE(t):
    r'</article>'
    return t

def t_ATITLE(t):
    r'<title>'
    return t

def t_CTITLE(t):
    r'</title>'
    return t
    
def t_CTAG(t) :
    r'</para>|</article>|</title>|</info>|</abstract>|</author>|</personname>|</firstname>|</surname>|</date>|</year>|</copyright>|</address>|</city>|</state>|</postcode>|</street>|</email>|</phone>|</section>|</simplesect>|</itemizedlist>|</listitem>|</emphasis>|</para>|</simpara>|</comment>|</important>|</informaltable>|</tgroup>|</thead>|</tfoot>|</tbody>|</row>|</entry>|</entrytbl>|</holder>|</mediaobject>|</videoObject>|</ImageObject>'         
    return t

def t_DOCTYPE(t):
    r'<\!DOCTYPE[\s]+ (article|book|chapter)[\s]*>'
    return

def t_INICIO(t):
    r'<\?xml[\ ]+(version[\ ]*=[\ ]*\"\d.\d\" [\ ]+)?(encoding[\ ]*=[\ ]*\" [\S]+ \"[\ ]*)? \?>'
    return t

def t_TEXTO(t):
    r'[^<>&]+'
    #EL TEXTO ENCUENTRA TODO SALVO ESTOS "< >" CARACTERES QUE SON INVALIDOS PARA CUALQUIER TEXTO Y URL 
    return t 

notrecognized=list()
def t_error(t):
    print("se encontró el siguiente token no reconocible ",t.value[0])
    t.lexer.skip(1)


lexer= lex.lex(debug=0) #debug=1 si queremos ver q hace internamente
if __name__=='__main__': 
    #si empieza en espacios vacios es invalido el docbook
    #si encuentra los siguientes caracteres es invalido: & < >1

    entradaDoc=""
    if (len(sys.argv) > 1):#se ingreso un comando agregado con este programa
        f=open(sys.argv[1],'r')
        entradaDoc=(f.read())
    else:
        print("Ingrese 1 para ingresar un docbook por consola y 2 para ingresarlo por archivo")
        opcion=int(input())
        if opcion==1:
            print("Escriba el docbook, una vez terminado apriete CTRL+D(linux) o CTRL+Z(windows)")
            entra=""
            while(True):
                try:# tomamos el input asi porque el profesor quiere que termine la ejecucion cuando apretemos CTRL+D
                    entra=input()
                    entradaDoc+=entra
                except EOFError:
                    break
        elif opcion==2:
            print("ingrese el nombre del archivo")
            entra=input()
            f=open(entra,"r")
            entradaDoc=f.read()
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