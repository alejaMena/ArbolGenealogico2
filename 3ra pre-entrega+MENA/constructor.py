class mujer:
    rol="familia"
    def __init__(self, nombre, tuvo_hijos, tuvo_hermanos):
        self.nombre=nombre
        self.tuvo_hijos=tuvo_hijos
        self.tuvo_hermanos=tuvo_hermanos
        #print(f"nombra la primera mujer de tu familia: {nombre},  tuvo hijos s/n: {tuvo_hijos} y tuvo hermanos s/n: {tuvo_hermanos}")

    def madre(self, cantidad_hijos):
        tuvo_hijos=input("tiene hijos? s/n: ")
        if tuvo_hijos=="s":
            print(f"{mujer.nombre}, es madre")
            print(f"cuantos hijos tuvo: {cantidad_hijos}")
        else:
            print(f"{mujer.nombre}, no es madre")

    def hija(self, cantidad_hermanos):
        tuvo_hermanos=input("tiene hermanos? s/n: ")
        if cantidad_hermanos=="s":
            print(f"{mujer.nombre}, es hija")
            print(f"cuantos hermanos tuvo: {cantidad_hermanos}")
        else:
            print(f"{mujer.nombre}, es hija unica")
        
abuela=mujer("ana", "s", "s")
abuela.madre("s")
#abuela.hija('s')