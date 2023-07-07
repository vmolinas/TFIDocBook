import ply.yacc as yacc
from Lexer import tokens,salida,entra,entradaDoc
import warnings
warnings.filterwarnings("ignore")

def p_sigma(p):
    '''sigma : INICIO art
        | DOCTYPE art
        | INICIO DOCTYPE art'''
    print('EL DOCBOOK ES CORRECTO')

def p_section(p):
    '''section : ASECTION info title eticom CSECTION section
                | ASECTION info eticom CSECTION section
                | ASECTION title eticom CSECTION section
                | ASECTION eticom CSECTION section
                | ASECTION info title eticom etisec CSECTION section
                | ASECTION info eticom etisec CSECTION section
                | ASECTION title eticom  etisec CSECTION section
                | ASECTION eticom etisec CSECTION section'''

def p_section2(p):
    '''section : ASECTION info title eticom CSECTION
                | ASECTION info eticom CSECTION
                | ASECTION title eticom CSECTION
                | ASECTION eticom CSECTION
                | ASECTION info title eticom etisec CSECTION
                | ASECTION info eticom etisec CSECTION
                | ASECTION title eticom etisec CSECTION
                | ASECTION eticom etisec CSECTION'''

def p_art(p):
    '''art : AARTICLE info title eticom etisec CARTICLE
        | AARTICLE info eticom etisec CARTICLE
        | AARTICLE title eticom etisec CARTICLE
        | AARTICLE eticom etisec CARTICLE
        | AARTICLE eticom  CARTICLE'''

def p_info(p):
    '''info : AINFO etiquetainfo CINFO'''

def p_title(p):
    '''title : ATITLE TEXTO CTITLE'''

def p_title2(p):
    '''title2 : ATITLE TEXTO CTITLE'''

def p_abstract(p):
    '''abstract : AABSTRACT title etiaux CABSTRACT
        | AABSTRACT etiaux CABSTRACT'''

# Simplesection
def p_simplesection1(p):
    '''simplesection : ASIMPLESECT info CSIMPLESECT
        | ASIMPLESECT info title2 CSIMPLESECT
        | ASIMPLESECT info eticom CSIMPLESECT
        | ASIMPLESECT info title2 eticom CSIMPLESECT'''

def p_simplesection2(p):
    '''simplesection : ASIMPLESECT info CSIMPLESECT simplesection
        | ASIMPLESECT info title2 CSIMPLESECT simplesection
        | ASIMPLESECT info eticom CSIMPLESECT simplesection
        | ASIMPLESECT info title2 eticom CSIMPLESECT simplesection'''

def p_para(p):
    '''para : APARA eticomp CPARA 
        |  APARA eticomp CPARA eticom'''

def p_simpara(p):
    '''simpara : ASIMPARA eticom4 CSIMPARA'''

def p_itemlist(p):
    '''itemlist : AITEMIZEDLIST listitem CITEMIZEDLIST'''

def p_listitem(p):
    '''listitem : ALISTITEM eticom CLISTITEM listitem
        | ALISTITEM eticom CLISTITEM'''

def p_emphasis(p):
    '''emphasis : AEMPHASIS eticom4 CEMPHASIS'''

def p_comment(p):
    '''comment : ACOMMENT eticom4 CCOMMENT'''

def p_vidimalink(p):
    '''vidimalink : VIDIMALINK eticom4
        | VIDIMALINK '''

def p_important(p):
    '''important : AIMPORTANT title eticom CIMPORTANT
        | AIMPORTANT eticom CIMPORTANT'''

# Data
def p_firstname(p):
    '''firstname : AFIRSTNAME eticom3 CFIRSTNAME'''

def p_surname(p):
    '''surname : ASURNAME eticom3 CSURNAME'''

def p_street(p):
    '''street : ASTREET eticom3 CSTREET'''

def p_city(p):
    '''city : ACITY eticom3 CCITY'''

def p_state(p):
    '''state : ASTATE eticom3 CSTATE'''

def p_phone(p):
    '''phone : APHONE eticom3 CPHONE'''

def p_email(p):
    '''email : AEMAIL eticom3 CEMAIL'''

def p_date(p):
    '''date : ADATE eticom3 CDATE'''

def p_year(p):
    '''year : AYEAR eticom3 CYEAR year 
        | AYEAR eticom3 CYEAR'''

def p_holder(p):
    '''holder : AHOLDER eticom3 CHOLDER holder
        | AHOLDER eticom3 CHOLDER'''

def p_address(p):
    '''address : AADDRESS etiadd CADDRESS'''

def p_author(p):
    '''author : AAUTHOR etiaut CAUTHOR'''

def p_copyright(p):
    '''copyright : ACOPYRIGHT year holder CCOPYRIGHT
        | ACOPYRIGHT year CCOPYRIGHT'''

def p_mediaobject(p):
    '''mediaobject : AMEDIAOBJECT info object CMEDIAOBJECT
        | AMEDIAOBJECT object CMEDIAOBJECT'''

def p_videoobject(p):
    '''videoobject : AVIDEOOBJECT info vidimalink CVIDEOOBJECT
        | AVIDEOOBJECT vidimalink CVIDEOOBJECT'''

def p_imageobject(p):
    '''imageobject : AIMAGEOBJECT info vidimalink CIMAGEOBJECT
        | AIMAGEOBJECT vidimalink CIMAGEOBJECT'''

def p_obj(p):
    '''object : videoobject object  
        | imageobject object
        | videoobject  
        | imageobject'''

def p_tgroup(p):
    '''tgroup : ATGROUP thead tfoot tbody CTGROUP
        | ATGROUP thead tbody CTGROUP
        | ATGROUP tfoot tbody CTGROUP
        | ATGROUP tbody CTGROUP
        | ATGROUP thead tfoot tbody CTGROUP tgroup
        | ATGROUP thead tbody CTGROUP tgroup
        | ATGROUP tfoot tbody CTGROUP tgroup
        | ATGROUP tbody CTGROUP tgroup'''

def p_thead(p):
    '''thead : ATHEAD row CTHEAD'''

def p_tfoot(p):
    '''tfoot : ATFOOT row CTFOOT'''

def p_tbody(p):
    '''tbody : ATBODY row CTBODY'''

def p_row(p):
    '''row : AROW etirow CROW row
        | AROW etirow CROW'''

def p_etirow(p):
    '''etirow : entry etirow
        | entrytbl etirow
        | entrytbl
        | entry'''

def p_entry(p):
    '''entry : AENTRY etientry CENTRY entry
        | AENTRY etientry CENTRY'''

def p_entrytbl1(p):
    '''entrytbl : AENTRYTBL thead tbody  CENTRYTBL entrytbl
        | AENTRYTBL thead tbody CENTRYTBL 
        | AENTRYTBL tbody CENTRYTBL'''

def p_entrytbl2(p):
    '''entrytbl : AENTRYTBL tbody CENTRYTBL entrytbl'''
    
from etiquetas import *

def p_error(p):
    print("Error sintáctico en '%s'" % p.value + " [Línea: %d]" % p.lineno)

parser = yacc.yacc(debug=0,start='sigma')
result = parser.parse(entradaDoc)