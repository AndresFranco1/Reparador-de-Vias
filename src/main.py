import os

def cargar_y_filtrar_archivos( ruta_archivo, filtros):
    """
    Guarda las lineas de texto que contengan los filtros (holistor/via/usuario)  buscados
    """
    resultados_filtrados = []#array vacío que luego va a contener las lineas concidentes a los filtros
    
    try:
        with open(ruta_archivo, 'r') as file:
            for line in file:
                line_lower = line.lower() #pone todo la linea en minúscula para evitar errores en las comparaciones
                if any(filtro.lower() in line_lower for filtro in filtros):
                    # recorre el array filtros, si algún filtro se enccuentra en alguna linea del array lines_lower retorna un true (entra al if)
                    resultados_filtrados.append(line.strip())#strip elimina de la linea el caracter que esté dentro del paréntesis 
        return resultados_filtrados
    except FileNotFoundError:
        print( f"Error: El archivo {ruta_archivo} no se encuentra")
        return []
    except Exception as e:
        print (f"Erro inesperado : {e}")
        return []
    
if __name__ == "__main__":
    """ las funciones dentro del if van a correr solo y solo si el archivo es jectuado directamente, es decir, desde la terminal de comando, y no importandolo desde otro módulo o programa. Esto permite asegurarnos que solo sean ejecutadas en esas circunstancias y también importar las funciones dentro de ella
    """
    ruta_simulada = os.path.join("data","dispositivos.txt")#une las rutas de manera personalizada en funnción del sistema operativo en el que se esté ejecutando
    
    filtros = ["holistorwsociedades", "etorreano", "remonda"]
    
    resultados = cargar_y_filtrar_archivos(ruta_simulada, filtros)
    
    print(f'Palabras filtro: {filtros}')
    print ("Resultados Filtrados")
    for resultado in resultados:
        print(resultado)