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
    
    print("\nLOS REGISTROS EN LA BASE DE DATOS SON:")
    c = conn.cursor()
    c.execute('SELECT * FROM "Cliente"')
    
    clientesData = c.fetchall()
    for row in clientesData:
        print(row)
    
    unconnection(conn)

def buscarClientePorId():
    conn = getConnection()
    if not conn: return
    
    print("\nBUSCAR CLIENTE POR ID")
    id_cliente = input("\nDigite el ID del cliente: ")

    c = conn.cursor()
    query = 'SELECT * FROM "Cliente" WHERE id_cliente = %s'
    val = (id_cliente,)
    
    c.execute(query, val)
    print(c.fetchone())
    
    unconnection(conn)

def crearCliente():
    conn = getConnection()
    if not conn: return
    print("\nCREAR CLIENTE")

    while True:
        id_cliente = input("\nDigite el ID del cliente: ")
        cedula = input("Digite la cédula: ")
        nombre = input("Digite el nombre: ")
        apellido = input("Digite el apellido: ")
        c = conn.cursor()
        query = 'INSERT INTO "Cliente" (id_cliente, cedula, nombre, apellido) VALUES (%s, %s, %s, %s)'
        val = (id_cliente, cedula, nombre, apellido)
    
        c.execute(query, val)
        conn.commit()
        print(c.rowcount, "Registro insertado exitosamente.")

        print("\n¿Desea agregar otro cliente?\n1. Sí \n2. No")
        var = int(input())

        if var != 1:
            break
    unconnection(conn)

def actualizarCliente():
    conn = getConnection()
    if not conn: return
    
    print("\nACTUALIZAR CLIENTE")
    
    while True:
        id_cliente = input("\nIngrese el Id del cliente a actualizar: ")

        while True: 
            print("¿Qué infromación desea actualizar? \nOpción 1: Cédula \nOpción 2: Nombre \nOpción 3: Apellido")
            upd = input()

            if upd == "1":
                cedula = input("Ingrese la nueva cédula: ")
                c = conn.cursor()
                query = 'UPDATE "Cliente" SET cedula = %s WHERE id_cliente = %s'
                val = (cedula, id_cliente)
                c.execute(query, val)
                conn.commit()
                print(c.rowcount, "Registro actualizado exitosamente.")

        
            if upd == "2":
                nombre = input("Ingrese el nuevo nombre: ")
                c = conn.cursor()
                query = 'UPDATE "Cliente" SET nombre = %s WHERE id_cliente = %s'
                val = (nombre, id_cliente)
                c.execute(query, val)
                conn.commit()
                print(c.rowcount, "Registro actualizado exitosamente.")
    

            if upd == "3":
                apellido = input("Ingrese el nuevo apellido: ")
                c = conn.cursor()
                query = 'UPDATE "Cliente" SET apellido = %s WHERE id_cliente = %s'
                val = (apellido, id_cliente)
                c.execute(query, val)
                conn.commit()
                print(c.rowcount, "Registro actualizado exitosamente.")

            print("\n¿Desea actualizar otro dato del cliente?\n1. Sí \n2. No")
            var = int(input())
            if var != 1:
                break

        print("\n¿Desea actualizar otro cliente?\n1. Sí \n2. No")
        var = int(input())
        if var != 1:
            break
        
    unconnection(conn)
      
    
def eliminarCliente():
    conn = getConnection()
    if not conn: return
    
    print("\nELIMINAR CLIENTE")
    
    while True: 
        id_cliente = input("Digite el ID del cliente a eliminar: ")

        c = conn.cursor()
        query = 'DELETE FROM "Cliente" WHERE id_cliente = %s'
        val = (id_cliente,)
        c.execute(query, val)
        conn.commit()
        
        print(c.rowcount, "registro eliminado.")

        print("\n¿Desea eliminar otro cliente?\n1. Sí \n2. No")
        var = input()

        if var != "1":
            break
    
    unconnection(conn)
