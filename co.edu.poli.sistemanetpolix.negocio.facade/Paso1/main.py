import ClienteDAO as p  
import VideoDAO as q

def main():
    try:
    
        #p.crearCliente()
        #p.buscarClientePorId()
        #p.actualizarCliente()
        #p.eliminarCliente()
        #p.findAll() 

        q.crearVideo()
        q.buscarVideoPorIsan()
        q.actualizarVideo()
        q.eliminarVideo()

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()