from campeonato import campeonato

PARTIDOS_GANADOS=0
PARTIDOS_EMPATADOS=1
PARTIDOS_PERDIDOS=2
GOLES_A_FAVOR=3
GOLES_EN_CONTRA=4

def salio_campeon(campeonato):
    puntos=0
    nuevos_max_puntos=0
    nuevos_menos_puntos=999
    empates=0
    mas_empates=0
    
    campeon=""
    desciende=""
    mas_empato=""
    
    
    for i in campeonato:
        
        puntos+=campeonato[i][PARTIDOS_GANADOS]*3
        puntos+=campeonato[i][PARTIDOS_EMPATADOS]
        
        empates=campeonato[i][PARTIDOS_EMPATADOS]
        
        if puntos > nuevos_max_puntos:
            campeon=i
            nuevos_max_puntos=puntos       

        if puntos < nuevos_menos_puntos:
            desciende=i
            nuevos_menos_puntos=puntos       
        
        if empates > mas_empates:
            mas_empato=i
            mas_empates=empates
            
        puntos=0
    
    lista=[campeon,mas_empato,desciende]
    
    print("El equipo campeon es",lista[0],"con",nuevos_max_puntos,"puntos.")
    print("El equipo que desciende es",lista[2],"con",nuevos_menos_puntos,"puntos.")
    print("El equipo que mas partidos empato es",lista[1],"con",mas_empates,"partidos.")
        
    return lista

def goleador(campeonato):
    
    ratio_goles=0
    nuevo_ratio_goles=0
    goleador=""
    
    for i in campeonato:
        ratio_goles=campeonato[i][GOLES_A_FAVOR]/campeonato[i][GOLES_EN_CONTRA]
        
        if ratio_goles > nuevo_ratio_goles:
            goleador=i
            nuevo_ratio_goles=ratio_goles   
            nuevo_ratio_goles=round(nuevo_ratio_goles,3)
        puntos=0
    
    print("El equipo con mejor proporcion goleadora es",goleador,"con",nuevo_ratio_goles)
    return goleador


def mani():
    
    salio_campeon(campeonato)
    goleador(campeonato)
    
mani()
