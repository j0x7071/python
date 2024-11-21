from campeonato import campeonato

PARTIDOS_GANADOS=0
PARTIDOS_EMPATADOS=1
PARTIDOS_PERDIDOS=2
GOLES_A_FAVOR=3
GOLES_EN_CONTRA=4

def salio_campeon(campeonato):
    puntos=0
    nuevos_puntos=0
    campeon=""
    
    for i in campeonato:
        puntos+=campeonato[i][PARTIDOS_GANADOS]*3
        puntos+=campeonato[i][PARTIDOS_EMPATADOS]
        if puntos > nuevos_puntos:
            campeon=i
            nuevos_puntos=puntos       
        puntos=0
        
    return campeon
    
def desciende(campeonato):
    puntos=999
    nuevos_puntos=999
    desciende=""
    
    for i in campeonato:
        puntos+=campeonato[i][PARTIDOS_GANADOS]*3
        puntos+=campeonato[i][PARTIDOS_EMPATADOS]
        if puntos < nuevos_puntos:
            desciende=i
            nuevos_puntos=puntos       
        puntos=0
        
    return desciende

def empato_mas(campeonato):
    partidos=0
    nueva_cantidad_partidos=0
    mas_empato=""
    for i in campeonato:
        partidos=campeonato[i][PARTIDOS_EMPATADOS]
        if partidos > nueva_cantidad_partidos:
            mas_empato=i
            nueva_cantidad_partidos=partidos      
        puntos=0
    return mas_empato    

def goleador(campeonato):
    
    ratio_goles=0
    nuevo_ratio_goles=0
    goleador=""
    
    for i in campeonato:
        ratio_goles=campeonato[i][GOLES_A_FAVOR]/campeonato[i][GOLES_EN_CONTRA]
        
        if ratio_goles > nuevo_ratio_goles:
            goleador=i
            nuevo_ratio_goles=ratio_goles       
        puntos=0
        
    return goleador


def mani():
    
    print(salio_campeon(campeonato))
    print(desciende(campeonato))
    print(empato_mas(campeonato))
    print(goleador(campeonato))
        
    
    
mani()