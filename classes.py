class Contexto():
    """
        Representa el contexto actual para los metodos 
        'es_ejecutable' de las clases Lenguaje, Interprete
        y Traductor

        Atributos:

            lenguajes_vistos : set con los nombres de los lenguajes
                               que ya se vieron en el recorrido
    """
    def __init__(self):
        self.lenguajes_vistos = set()

class Lenguaje():
    """
        Representa un lenguaje de programacion

        Atributos:

            nombre: string que representa el nombre del lenguaje

            interpretadores: lista de instancias de la clase Interprete 
                             los cuales son interpretes de la actual
                             instancia Lenguaje a un Lenguaje Base

            Traductores: lista de instancias de la clase Traductor
                         los cuales representan traductores de la 
                         actual instancia de Lenguaje a un Lenguaje
                         Destino escrito en Lenguaje Base

    """

    def __init__(self, nombre :str):
        self.nombre : str = nombre
        self.interpretadores : list[Interprete] = []
        self.traductores : list[Traductor] = []

    def es_ejecutable(self, contexto : Contexto) -> bool:
        """
            Determina si el lenguaje se puede interpretar o traducir
            de forma directa o indirecta al lenguaje 'LOCAL'. 
            De forma que los programas escritos en este lenguaje se
            puedan ejecutar.

            retorna:
                True, si el lenguaje se puede interpretar o traducir
                de forma directa o indirecta al lenguaje 'LOCAL'.

                False de lo contrario
        """

        if self.nombre == "LOCAL":
            return True
        
        contexto.lenguajes_vistos.add(self.nombre)
        
        for interprete in self.interpretadores:

            if not (interprete.lenguaje_base.nombre in contexto.lenguajes_vistos):

                se_puede_interpretar = interprete.es_ejecutable(contexto)

                if se_puede_interpretar:
                    return True
        
        for traductor in self.traductores:

            if not (traductor.lenguaje_destino.nombre in contexto.lenguajes_vistos):
                
                se_puede_traducir = traductor.es_ejecutable(contexto)

                if se_puede_traducir:
                    return True
        
        return False
            
class Programa():
    """
        Representa un programa

        atributos:
            nombre: nombre del programa
            lenguaje: lenguaje en el que esta escrito el programa
    """
    
    def __init__(self, nombre : str, lenguaje : Lenguaje ):
        self.nombre : str = nombre
        self.lenguaje = lenguaje
    
    def es_ejecutable(self) -> bool:
        """
            Determina si de forma directa o indirecta el programa se puede
            ejecutar

            retornar:
                True si el programa se puede ejecutar,
                False de lo contrario
        """
        contexto = Contexto()
        return self.lenguaje.es_ejecutable(contexto)
        

class Interprete():
    """
        Representa un Interprete

        args:
            lenguaje_base: lenguaje en el que esta escrito el interpretador
            lenguaje: lenguaje que se interpreta
    """

    def __init__(self, lenguaje_base : Lenguaje, lenguaje : Lenguaje):
        self.lenguaje_base : Lenguaje = lenguaje_base
        self.lenguaje : Lenguaje = lenguaje

    def es_ejecutable(self, contexto : Contexto):
        """
            Determina si el Interprete puede ser ejecutable en
            una maquina

            retorna:
                True si es posible ejecutarse en una maquina
        """

        return self.lenguaje_base.es_ejecutable(contexto)

class Traductor():
    """
        Representa un Traductor

        atributos:
            lenguaje_base: lenguaje en el que esta escrito el traductor
            lenguaje_origen: lenguaje desde el cual se traduce los programas
            lenguaje_destino: lenguaje al que se traduce los programas
    """

    def __init__(self, lenguaje_base : Lenguaje, lenguaje_origen : Lenguaje, lenguaje_destino : Lenguaje):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino

    def es_ejecutable(self, contexto : Contexto) -> bool:
        """
            Determina si el traductor puede ser ejecutado en una
            maquina

            retorna
                True si es posible er ejecutado en una maquina,
                False de lo contrario
        """
        
        contexto_lenguaje_base = Contexto()
        if self.lenguaje_base.es_ejecutable(contexto_lenguaje_base):
            return self.lenguaje_destino.es_ejecutable(contexto)
        
        return False
        
class Simulador():
    """
        Representa un simulador de programas, intérpretes 
        y traductores como los diagramas de T
    """
    def __init__(self):
        self.lenguajes : dict[str, Lenguaje] = {"LOCAL" : Lenguaje("LOCAL")}
        self.programas : dict[str, Programa] = {}
    
    def definir_programa(self, nombre : str, nombre_lenguaje : Lenguaje):
        if nombre in self.programas:
            raise ValueError("Ya existe un programa con ese nombre")       
        
        # Revisamos si el lenguaje ya existe, si no existe
        # le creamos una instancia 
        if not (nombre_lenguaje in self.lenguajes):
            nuevo_lenguaje = Lenguaje(nombre_lenguaje)
            self.lenguajes[nombre_lenguaje] = nuevo_lenguaje
                    
        # Creamos la instancia para el programa y lo agrgamos
        # al diccionario de programas
        nuevo_programa = Programa(nombre, self.lenguajes[nombre_lenguaje])
        self.programas[nombre] = nuevo_programa
    
    def definir_interprete(self, lenguaje_base_nombre : str, lenguaje_nombre : str): 

        # Creamos los lenguajes si hace falta
        if not (lenguaje_base_nombre in self.lenguajes):
            nuevo_lenguaje1 = Lenguaje(lenguaje_base_nombre)
            self.lenguajes[lenguaje_base_nombre] = nuevo_lenguaje1

        if not (lenguaje_nombre in self.lenguajes):
            nuevo_lenguaje2 = Lenguaje(lenguaje_nombre)
            self.lenguajes[lenguaje_nombre] = nuevo_lenguaje2
                                
        # Creamos el interpretador
        nuevo_interprete = Interprete(self.lenguajes[lenguaje_base_nombre], self.lenguajes[lenguaje_nombre])

         # Vamos a agregar al lenguaje su nuevo interpretador
        lenguaje = self.lenguajes[lenguaje_nombre]
        lenguaje.interpretadores += [nuevo_interprete]

    def definir_traductor(self, lenguaje_base_nombre: str, lenguaje_origen_nombre: str, lenguaje_destino_nombre: str ):

        # Creamos los lenguajes que nos hagan falta

        if not (lenguaje_base_nombre in self.lenguajes):
            nuevo_lenguaje1 = Lenguaje(lenguaje_base_nombre)
            self.lenguajes[lenguaje_base_nombre] = nuevo_lenguaje1

        if not (lenguaje_origen_nombre in self.lenguajes):
            nuevo_lenguaje2 = Lenguaje(lenguaje_origen_nombre)
            self.lenguajes[lenguaje_origen_nombre] = nuevo_lenguaje2

        if not (lenguaje_destino_nombre in self.lenguajes):
            nuevo_lenguaje3 = Lenguaje(lenguaje_destino_nombre)
            self.lenguajes[lenguaje_destino_nombre] = nuevo_lenguaje3
                
        # Creamos el nuevo traductor
        nuevo_traductor = Traductor(self.lenguajes[lenguaje_base_nombre], self.lenguajes[lenguaje_origen_nombre], self.lenguajes[lenguaje_destino_nombre])

        # Al lenguaje de origen le agregamos su nuevo traductor
        # en su lista de traductores
        lenguaje_origen = self.lenguajes[lenguaje_origen_nombre]
        lenguaje_origen.traductores += [nuevo_traductor]

    def ejecutable(self, nombre : str) -> bool:
        # Revisamos si existe el programa
        if not (nombre in self.programas):
            msg = f"No existe el programa {nombre}"
            raise ValueError(msg)

        programa = self.programas[nombre]

        return programa.es_ejecutable()