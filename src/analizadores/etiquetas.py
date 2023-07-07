# CASOS GENERALES etiquetas

# ETIQUETAS DE INFO
def p_etiquetainfo(p):
    '''etiquetainfo : author etiquetainfo
        | date etiquetainfo
        | copyright etiquetainfo
        | title etiquetainfo
        | mediaobject etiquetainfo
        | abstract etiquetainfo
        | address etiquetainfo
        | author 
        | date
        | copyright 
        | title
        | mediaobject
        | abstract
        | address'''

# ETIQUETAS COMPARTIDAS ART SECT SSEC IMPORTANT:
def p_eticom(p):
    '''eticom : para eticom
        | simpara eticom
        | comment eticom
        | inftable eticom
        | itemlist eticom
        | important eticom
        | mediaobject eticom 
        | abstract eticom
        | address eticom
        | para
        | simpara 
        | comment 
        | inftable 
        | itemlist 
        | important 
        | mediaobject 
        | abstract  
        | address'''

# ETIQUETAS COMPARTIDAS Street, City, State, Phone, Email, Date, Year, Holder
def p_eticom3(p):
    '''eticom3 : TEXTO eticom3
        | TEXTO
        | vidimalink eticom3
        | vidimalink
        | emphasis eticom3
        | emphasis
        | comment eticom3
        | comment'''

# ETIQUETAS COMPARTIDAS SimPara, Emphasis, Comment, Link
def p_eticom4(p):
    '''eticom4 : TEXTO eticom4
        | TEXTO
        | emphasis eticom4
        | emphasis
        | vidimalink eticom4
        | vidimalink
        | email eticom4
        | email
        | author eticom4
        | author
        | comment eticom4
        | comment'''

# Etiquetas compartidas extras
def p_eticomp(p):
    '''eticomp : inftable eticomp
        | itemlist eticomp
        | important eticomp
        | mediaobject eticomp 
        | abstract eticomp
        | address eticomp
        | TEXTO eticomp
        | emphasis eticomp
        | vidimalink eticomp
        | email eticomp
        | author eticomp
        | comment eticomp'''

def p_eticomp2(p):
    '''eticomp : inftable 
        | itemlist 
        | important
        | mediaobject 
        | abstract
        | address
        | TEXTO
        | emphasis
        | vidimalink
        | email
        | author
        | comment'''


def p_inftable(p):
    '''inftable : AINFORMALTABLE mediaobject CINFORMALTABLE
        | AINFORMALTABLE tgroup CINFORMALTABLE'''

# ETIQUETAS COMPARTIDAS PersonName
def p_etiaut(p):
    '''etiaut : firstname etiaut
        | firstname 
        | surname etiaut
        | surname'''

# ETIQUETAS COMPARTIDAS Address
def p_etiadd(p):
    '''etiadd : TEXTO etiadd
        | TEXTO
        | street etiadd
        | street
        | city etiadd
        | city
        | state etiadd
        | state
        | phone etiadd
        | phone
        | email etiadd
        | email'''

# ETIQUETAS COMPARTIDAS entry
def p_etientry(p):
    '''etientry : TEXTO etientry
        | TEXTO
        | itemlist etientry
        | itemlist
        | important etientry
        | important
        | para etientry
        | para
        | simpara etientry
        | simpara
        | mediaobject etientry
        | mediaobject
        | comment etientry
        | comment
        | abstract etientry
        | abstract'''

def p_etisec(p):
    '''etisec : simplesection
                | section 
    '''

def p_etiaux(p):
    '''etiaux : para etiaux
        | simpara etiaux
        | para
        | simpara'''