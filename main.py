from classes import Simulador

def main():
    """
        Crea una instancia de Simulador el cual
        simula programas, intérpretes y traductores como 
        los diagramas de T 

        Dependiendo del input del usuario el programa
        interactua con el simulador
    """

    # Booleano que representa si hay que seguir ejecutando el simulador
    seguir_ejecutandose : bool = True
    simulador : Simulador = Simulador()

    while (seguir_ejecutandose):
        
        # Pedimos el input del usuario
        input_usuario_str : str = input()

        if input_usuario_str == "":
            print("Se necesita una accion")
            continue
        
        input_usuario_list : list[str] = input_usuario_str.split(" ")

        if input_usuario_list[0] == "DEFINIR":

            if len(input_usuario_list) < 2:
                print("Faltan argumentos")
                continue

            if input_usuario_list[1] == "PROGRAMA":

                if len(input_usuario_list) < 4:
                    print("Faltan argumentos")
                    continue
                if len(input_usuario_list) > 4:
                    print("Demasiados argumentos pasados")
                    continue
   
                nombre = input_usuario_list[2]
                lenguaje = input_usuario_list[3]

                try:
                    simulador.definir_programa(nombre, lenguaje)
                    print(f"Se definió el programa '{nombre}', ejecutable en '{lenguaje}'")
                except:
                    print("Ya existe un programa con ese nombre")
                    continue

            elif input_usuario_list[1] == "INTERPRETE":

                if len(input_usuario_list) < 4:
                    print("Faltan argumentos")
                    continue
                if len(input_usuario_list) > 4:
                    print("Demasiados argumentos pasados")
                    continue

                lenguaje_base_nombre = input_usuario_list[2]
                lenguaje_nombre = input_usuario_list[3]

                simulador.definir_interprete(lenguaje_base_nombre, lenguaje_nombre)

                print(f"Se definió un intérprete para '{lenguaje_nombre}', escrito en '{lenguaje_base_nombre}'")

            elif input_usuario_list[1] == "TRADUCTOR":
                
                if len(input_usuario_list) < 5:
                    print("Faltan argumentos")
                    continue
                if len(input_usuario_list) > 5:
                    print("Demasiados argumentos")
                    continue

                lenguaje_base_nombre = input_usuario_list[2]
                lenguaje_origen_nombre = input_usuario_list[3]
                lenguaje_destino_nombre = input_usuario_list[4]

                simulador.definir_traductor(lenguaje_base_nombre, lenguaje_origen_nombre, lenguaje_destino_nombre)

                print(f"Se definió un traductor de '{lenguaje_origen_nombre}' hacia '{lenguaje_destino_nombre}', escrito en '{lenguaje_base_nombre}'")

            else:

                print("\033[31m Tipo a definir no reconocido \033[0m")
                
        elif input_usuario_list[0] == "EJECUTABLE":

            if len(input_usuario_list) < 2:
                print("Faltan argumentos")
                continue

            if len(input_usuario_list) > 2:
                print("Demasiados argumentos")
                continue

            programa_nombre = input_usuario_list[1]

            try: 
                if (simulador.ejecutable(programa_nombre)):

                    print(f"Si, es posible ejecutar el programa '{programa_nombre}'")

                else:
                    print(f"No es posible ejecutar el programa '{programa_nombre}'")

            except:
                print("No existe el programa {programa_nombre}")

        elif input_usuario_list[0] == "SALIR":

            seguir_ejecutandose = False

        else:
            print("Accion no reconocida")

main()