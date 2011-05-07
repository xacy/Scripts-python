import httplib,urllib2,urllib,os 

"""
    Añadir que se pueda listar las imagenes y obtener el nombre para descargarlas.    

"""
 
# Descargamos la imagen. Usamos try/except por si hay algun
# error en la conexion
def main():
    dominio = 'URL_DOMINIO'
    ruta_imagen = 'RUTA_DESCARGA'
    dir_downloads = 'DIR_LOCAL'
    try:
        # conectamos con el servidor
        conn = httplib.HTTPConnection(dominio)
        #creamos el objeto para manejar la ruta
        d=os.path.dirname(dir_downloads)
        #comprobamos que existe el directorio y si no le creamosD
        print "Comprobando que existe el directorio"
        if not os.path.exists(dir_downloads):
            print "Creando..."
            os.makedirs(dir_downloads)
        else:
            print "Existe"
        # hacemos la peticion a la imagen
        for i in range(1, 24):

            ruta_imagen = ruta_imagen + str(i)+'.jpg'

            conn.request ("GET", '/' + ruta_imagen)
            r = conn.getresponse()
            imagen_local=str(i)+'.jpg'
            print "Cargando la imagen: %d" %i
            # abrimos o creamos el fichero donde vamos a guardar la imagen
            """ otro=os.path.dirname(dir_downloads+'/' + imagen_local)
            if os.path.exists(otro):
                print "el fichero existe"
            else:
                print "no existe" """
            fichero = file(dir_downloads + '/' + imagen_local, "wb")
            #guardamos la imagen en el fichero
            fichero.write(r.read())
            # y cerramos el fichero
            fichero.close()
            ruta_imagen="images/gallery/97194/"
        
        print "Finalizada la carga."

    except:
        print "No se ha podido descargar la imagen"
    
if __name__ == "__main__":
    main()
