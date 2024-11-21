jugadores={}

jugadores['juga']= {'puntos':4,'turnos':3}
jugadores['jokra']= {'puntos':2,'turnos':40}
jugadores['jienia']= {'puntos':8,'turnos':70}
       
registro_jugadores={}
def registrar_partida(jugadores, registro_jugadores):
    
    for key in jugadores:
        
        if key in registro_jugadores:
            registro_jugadores[key]['puntos'] = registro_jugadores[key]['puntos'] + jugadores[key]['puntos']  
            registro_jugadores[key]['turnos'] = registro_jugadores[key]['turnos'] + jugadores[key]['turnos']  

        else:
            
            registro_jugadores[key]={'puntos':0,'turnos':0}
            registro_jugadores[key]['turnos'] = jugadores[key]['turnos']  
            registro_jugadores[key]['puntos'] = jugadores[key]['puntos']  

    return registro_jugadores
    

print(registrar_partida(jugadores, registro_jugadores))