from Jugador import *
from Arbitro import *
from Equipo import *
from Partido import *

if __name__ == "__main__":
    # Jugadores de la Seleccion Argentina
    molinas = Jugador("Nahuel", "Molinas", 4)
    mac_alister = Jugador("Alexis", "Mac Alister", 20)
    messi = Jugador("Lionel", "Messi", 10)
    alvarez = Jugador("Julian", "Alvarez", 9)
    di_maria = Jugador("Angel", "Di Maria", 11)
    
    # Jugadores de la Seleccion Francesa
    tchouameni = Jugador("Aurelien", "Tchouameni", 1)
    kolo_muani = Jugador("Radal", "Kolo Muani", 2)
    varane = Jugador("Raphael", "Varane", 3)
    camavinga = Jugador("Eduardo", "Camavinga", 4)
    lloris = Jugador("Hugo", "Lloris", 5)

    # Tipos de Arbitros: El árbitro principal, los árbitros asistentes, el cuarto árbitro, los árbitros asistentes adicionales y el árbitro asistente de reserva
    arbitro = Arbitro("Szymon", "Marciniak", "Principal")

    # Selecciones
    argentina = Equipo("Selección Argentina")
    francia = Equipo("Selección francesa")

    # Cargado de jugadores a las selecciones
    argentina.agregar_jugador(molinas)
    argentina.agregar_jugador(mac_alister)
    argentina.agregar_jugador(messi)
    argentina.agregar_jugador(alvarez)
    argentina.agregar_jugador(di_maria)

    francia.agregar_jugador(tchouameni)
    francia.agregar_jugador(kolo_muani)
    francia.agregar_jugador(varane)
    francia.agregar_jugador(camavinga)
    francia.agregar_jugador(lloris)

    partido = Partido(argentina, francia, arbitro)
    print("Llamado a los datos del arbitro desde el objeto de la clase Partido: ", partido.get_arbitro())
    print("")
    print("Llamado a los datos del arbitro desde el objeto de la clase Arbitro: ", arbitro)
    print("")

    partido.iniciar_partido()

    messi.hizo_gol()

    arbitro.convalido_gol()

    partido.incrementar_marcador_local()
    print(partido)

    print("\n=====El gol más lindo de la final=====")

    molinas.dar_pase(mac_alister)
    mac_alister.dar_pase(messi)
    messi.dar_pase(alvarez)
    alvarez.dar_pase(mac_alister)
    mac_alister.dar_pase(di_maria)
    di_maria.hizo_gol()
    arbitro.convalido_gol()
    partido.incrementar_marcador_local()

    print(partido)

    print("HACER: Realizar los demás goles y mostrar el resultado final del partido...", "\n")

    partido.finalizar_partido()
    