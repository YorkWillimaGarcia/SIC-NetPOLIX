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

def buscarVideoPorTitulo(titulo):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'SELECT * FROM "Video" WHERE titulo ILIKE %s'
    val = (f"%{titulo}%",)
    
    c.execute(query, val)
    for row in c.fetchall():
        print(row)
    
    unconnection(conn)

def buscarVideoPorIsan(isan_video):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'SELECT * FROM "Video" WHERE isan_video = %s'
    val = (isan_video,)
    
    c.execute(query, val)
    print(c.fetchone())
    
    unconnection(conn)

def crearVideo(isan_video, titulo, año, duracion_minutos):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'INSERT INTO "Video" (isan_video, titulo, año, duracion_minutos) VALUES (%s, %s, %s, %s)'
    val = (isan_video, titulo, año, duracion_minutos)
    
    c.execute(query, val)
    conn.commit()
    print(c.rowcount, "registro insertado.")
    unconnection(conn)

def editarVideo(isan_video, titulo, año, duracion_minutos):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'UPDATE "Video" SET titulo = %s, año = %s, duracion_minutos = %s WHERE isan_video = %s'
    val = (isan_video, titulo, año, duracion_minutos)
    
    c.execute(query, val)
    conn.commit()
    print(c.rowcount, "registro actualizado.")
    unconnection(conn)

def eliminarVideo(isan_video):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'DELETE FROM "Video" WHERE isan_video = %s'
    val = (isan_video,)
    
    c.execute(query, val)
    conn.commit()
    print(c.rowcount, "registro eliminado.")
    unconnection(conn)

if __name__ == "__main__":
    print("Probando consulta de todos los videos:")
    findAll()   