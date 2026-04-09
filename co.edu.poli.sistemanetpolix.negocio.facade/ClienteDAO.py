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
    c.execute('SELECT * FROM "Cliente"')
    
    clientesData = c.fetchall()
    for row in clientesData:
        print(row)
    
    unconnection(conn)

def buscarPersonaPorNombre(nombre):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'SELECT * FROM "Cliente" WHERE nombre ILIKE %s'
    val = (f"%{nombre}%",)
    
    c.execute(query, val)
    for row in c.fetchall():
        print(row)
    
    unconnection(conn)

def buscarPersonaPorId(id_cliente):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'SELECT * FROM "Cliente" WHERE id_cliente = %s'
    val = (id_cliente,)
    
    c.execute(query, val)
    print(c.fetchone())
    
    unconnection(conn)

def crearPersona(id_cliente, cedula, nombre, apellido):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'INSERT INTO "Cliente" (id_cliente, cedula, nombre, apellido) VALUES (%s, %s, %s, %s)'
    val = (id_cliente, cedula, nombre, apellido)
    
    c.execute(query, val)
    conn.commit()
    print(c.rowcount, "registro insertado.")
    unconnection(conn)

def editarPersona(cedula, nombre, apellido, id_cliente):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'UPDATE "Cliente" SET cedula = %s, nombre = %s, apellido = %s WHERE id_cliente = %s'
    val = (cedula, nombre, apellido, id_cliente)
    
    c.execute(query, val)
    conn.commit()
    print(c.rowcount, "registro actualizado.")
    unconnection(conn)

def eliminarPersona(id_cliente):
    conn = getConnection()
    if not conn: return
    
    c = conn.cursor()
    query = 'DELETE FROM "Cliente" WHERE id_cliente = %s'
    val = (id_cliente,)
    
    c.execute(query, val)
    conn.commit()
    print(c.rowcount, "registro eliminado.")
    unconnection(conn)

if __name__ == "__main__":
    print("Probando consulta de todos los clientes:")
    findAll()   