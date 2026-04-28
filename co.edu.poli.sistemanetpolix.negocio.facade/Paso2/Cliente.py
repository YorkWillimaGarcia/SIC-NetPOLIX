# ============================================================
# Cliente.py
# ============================================================

import ClienteDAO as cdao
import VideoDAO as vdao
from models import SessionLocal

session   = SessionLocal()
miDaoC    = cdao.ClienteDAO(session)
miDaoV    = vdao.VideoDao(session)


def mostrar_clientes(clientes):
    if not clientes:
        print("No hay registros.")
    else:
        for c in clientes:
            print(f"ID: {c.id_cliente} | Cédula: {c.cedula} | Nombre: {c.nombre} | Apellido: {c.apellido}")


def mostrar_videos(videos):
    if not videos:
        print("No hay registros.")
    else:
        for v in videos:
            print(f"ISAN: {v.isan_video} | Título: {v.titulo} | Año: {v.año} | Duración: {v.duracion_minutos} min")


def menu_principal():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Gestionar Clientes")
    print("2. Gestionar Videos")
    print("3. Salir")
    print("=====================================")


def menu_clientes():
    print("\n========== MENÚ CLIENTES ==========")
    print("1. Ver todos los clientes")
    print("2. Buscar cliente por ID")
    print("3. Crear cliente")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("6. Volver")
    print("====================================")


def menu_videos():
    print("\n========== MENÚ VIDEOS ==========")
    print("1. Ver todos los videos")
    print("2. Buscar video por ISAN")
    print("3. Buscar video por título")
    print("4. Crear video")
    print("5. Actualizar video")
    print("6. Eliminar video")
    print("7. Volver")
    print("==================================")


def run_clientes():
    while True:
        menu_clientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_clientes(miDaoC.obtener_todos())

        elif opcion == "2":
            miDaoC.obtener_por_id()

        elif opcion == "3":
            miDaoC.crear()
            print("\nClientes actualizados:")
            mostrar_clientes(miDaoC.obtener_todos())

        elif opcion == "4":
            miDaoC.actualizar()
            print("\nClientes actualizados:")
            mostrar_clientes(miDaoC.obtener_todos())

        elif opcion == "5":
            miDaoC.eliminar()
            print("\nClientes actualizados:")
            mostrar_clientes(miDaoC.obtener_todos())

        elif opcion == "6":
            break

        else:
            print("Opción no válida. Intente de nuevo.")


def run_videos():
    while True:
        menu_videos()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_videos(miDaoV.obtener_todos())

        elif opcion == "2":
            miDaoV.obtener_por_isan()

        elif opcion == "3":
            miDaoV.obtener_por_titulo()

        elif opcion == "4":
            miDaoV.crear()
            print("\nVideos actualizados:")
            mostrar_videos(miDaoV.obtener_todos())

        elif opcion == "5":
            miDaoV.actualizar()
            print("\nVideos actualizados:")
            mostrar_videos(miDaoV.obtener_todos())

        elif opcion == "6":
            miDaoV.eliminar()
            print("\nVideos actualizados:")
            mostrar_videos(miDaoV.obtener_todos())

        elif opcion == "7":
            break

        else:
            print("Opción no válida. Intente de nuevo.")


def run():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            run_clientes()

        elif opcion == "2":
            run_videos()

        elif opcion == "3":
            print("Saliendo...")
            session.close()
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()