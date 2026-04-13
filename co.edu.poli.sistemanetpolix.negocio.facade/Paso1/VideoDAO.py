import psycopg2
import os

def getConnection():
    try:
        conn = psycopg2.connect(
            host="aws-1-us-east-1.pooler.supabase.com",
            port="6543",
            database="postgres",
            user="postgres.himzzqbqzmxrckedqapx",
            password="Politecnico123*",
            sslmode="require"
        )
        return conn
    except Exception as e:
        print(f"No se puede conectar a la base de datos: {e}")
        return None

def unconnection(conn):
    if conn:
        conn.close()

def findAll():
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    c.execute('SELECT * FROM "Video"')
    
    clientesData = c.fetchall()
    for row in clientesData:
        print(row)
    
    unconnection(conn)

def buscarVideoPorTitulo():
    conn = getConnection()
    if not conn: return

    print("\nBusca el video por título: ")
    titulo = input("Ingrese el título del video: ")

    c = conn.cursor()
    query = 'SELECT * FROM "Video" WHERE titulo ILIKE %s'
    val = (f"%{titulo}%",)
    
    c.execute(query, val)
    for row in c.fetchall():
        print(row)
    
    unconnection(conn)

def buscarVideoPorIsan():
    conn = getConnection()
    if not conn: return
    
    print("\nBusca el video por ISAN")
    isan_video = input("Ingrese el isan del video: ")

    c = conn.cursor()
    query = 'SELECT * FROM "Video" WHERE isan_video = %s'
    val = (isan_video,)
    
    c.execute(query, val)
    print(c.fetchone())
    
    unconnection(conn)

def crearVideo():
    conn = getConnection()
    if not conn: return

    print("\nCREAR VIDEO")

    while True:
        isan_video = input("\nDigite el ISAN del video: ")
        titulo = input("Digite el título: ")
        año = input("Digite el año de lanzamiento: ")
        duracion_minutos = input("Digite la duracion en minutos: ")

        c = conn.cursor()
        query = 'INSERT INTO "Video" (isan_video, titulo, año, duracion_minutos) VALUES (%s, %s, %s, %s)'
        val = (isan_video, titulo, año, duracion_minutos)
        
        c.execute(query, val)
        conn.commit()
        print(c.rowcount, "registro insertado.")

        print("\n¿Desea agregar otro video?\n1. Sí \n2. No")
        var = input()

        if var != "1":
            break
    unconnection(conn)

def actualizarVideo():
    conn = getConnection()
    if not conn: return
    print("\nACTUALIZAR VIDEO")

    while True:
         isan_video = input("\nIngrese el ISAN del video a actualizar: ")
         
         while True:
            print("¿Qué infromación desea actualizar? \nOpción 1: Título \nOpción 2: Año \nOpción 3: Duración")
            upd = input()
            
            if upd == "1":
                titulo = input("Ingrese el nuevo título: ")
                c = conn.cursor()
                query = 'UPDATE "Video" SET titulo = %s WHERE isan_video = %s'
                val = (titulo, isan_video)
                c.execute(query, val)
                conn.commit()
                print(c.rowcount, "Registro actualizado exitosamente.")

            if upd == "2":
                año = input("Ingrese el nuevo año: ")
                c = conn.cursor()
                query = 'UPDATE "Video" SET año = %s WHERE isan_video = %s'
                val = (año, isan_video)
                c.execute(query, val)
                conn.commit()
                print(c.rowcount, "Registro actualizado exitosamente.")

            if upd == "3":
                duracion_minutos = input("Ingrese la nueva duración: ")
                c = conn.cursor()
                query = 'UPDATE "Video" SET duracion_minutos = %s WHERE isan_video = %s'
                val = (duracion_minutos, isan_video)
                c.execute(query, val)
                conn.commit()
                print(c.rowcount, "Registro actualizado exitosamente.")
            
            print("\n¿Desea actualizar otro dato del video?\n1. Sí \n2. No")
            var = input()
            if var != "1":
                break
            
         print("\n¿Desea actualizar otro video?\n1. Sí \n2. No")
         var = input()
         if var != "1":
            break
 
    unconnection(conn)

def eliminarVideo():
    conn = getConnection()
    if not conn: return

    print("\nELIMINAR VIDEO")

    while True:
        isan_video = input("Digite el ISAN del video a eliminar: ")
        c = conn.cursor()
        query = 'DELETE FROM "Video" WHERE isan_video = %s'
        val = (isan_video,)
        c.execute(query, val)
        conn.commit()

        print(c.rowcount, "registro eliminado.")

        print("\n¿Desea eliminar otro cliente?\n1. Sí \n2. No")
        var = input()

        if var != "1":
            break

    unconnection(conn)

