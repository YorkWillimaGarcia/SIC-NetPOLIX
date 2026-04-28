# ============================================================
# app.py
# API REST completa - Cliente, Video, Serie, Categoria, Idioma
# ============================================================

from flask import Flask, request, jsonify
from models import SessionLocal
from ClienteDAO import ClienteDAO
from VideoDAO import VideoDAO
from SerieDAO import SerieDAO
from CategoriaDAO import CategoriaDAO
from IdiomaDAO import IdiomaDAO

app = Flask(__name__)


# ------------------------------------------------------------
# Funciones auxiliares - DAOs
# ------------------------------------------------------------
def get_cliente_dao():
    session = SessionLocal()
    return ClienteDAO(session), session

def get_video_dao():
    session = SessionLocal()
    return VideoDAO(session), session

def get_serie_dao():
    session = SessionLocal()
    return SerieDAO(session), session

def get_categoria_dao():
    session = SessionLocal()
    return CategoriaDAO(session), session

def get_idioma_dao():
    session = SessionLocal()
    return IdiomaDAO(session), session


# ------------------------------------------------------------
# Funciones auxiliares - to_dict
# ------------------------------------------------------------
def cliente_to_dict(c):
    return {"id_cliente": c.id_cliente, "cedula": c.cedula,
            "nombre": c.nombre, "apellido": c.apellido}

def video_to_dict(v):
    return {"isan_video": v.isan_video, "titulo": v.titulo,
            "año": v.año, "duracion_minutos": v.duracion_minutos}

def serie_to_dict(s):
    return {"id_serie": s.id_serie, "nombre": s.nombre,
            "temporadas": s.temporadas}

def categoria_to_dict(c):
    return {"id_categoria": c.id_categoria, "nombre": c.nombre,
            "descripcion": c.descripcion}

def idioma_to_dict(i):
    return {"id_idioma": i.id_idioma, "nombre": i.nombre,
            "codigo": i.codigo}


# ============================================================
# ENDPOINTS CLIENTE
# ============================================================

@app.route("/clientes", methods=["POST"])
def crear_cliente():
    data = request.get_json()
    for campo in ["id_cliente", "cedula", "nombre", "apellido"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_cliente_dao()
    try:
        c = dao.crear(data["id_cliente"], data["cedula"], data["nombre"], data["apellido"])
        return jsonify(cliente_to_dict(c)), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/clientes", methods=["GET"])
def obtener_todos_clientes():
    dao, session = get_cliente_dao()
    try:
        return jsonify([cliente_to_dict(c) for c in dao.obtener_todos()]), 200
    finally:
        session.close()

@app.route("/clientes/<int:id_cliente>", methods=["GET"])
def obtener_cliente_por_id(id_cliente):
    dao, session = get_cliente_dao()
    try:
        c = dao.obtener_por_id(id_cliente)
        if not c:
            return jsonify({"error": f"No existe cliente con id={id_cliente}"}), 404
        return jsonify(cliente_to_dict(c)), 200
    finally:
        session.close()

@app.route("/clientes/<int:id_cliente>", methods=["PUT"])
def actualizar_cliente(id_cliente):
    data = request.get_json()
    for campo in ["cedula", "nombre", "apellido"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_cliente_dao()
    try:
        c = dao.actualizar(id_cliente, data["cedula"], data["nombre"], data["apellido"])
        if not c:
            return jsonify({"error": f"No existe cliente con id={id_cliente}"}), 404
        return jsonify(cliente_to_dict(c)), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/clientes/<int:id_cliente>", methods=["DELETE"])
def eliminar_cliente(id_cliente):
    dao, session = get_cliente_dao()
    try:
        if not dao.obtener_por_id(id_cliente):
            return jsonify({"error": f"No existe cliente con id={id_cliente}"}), 404
        dao.eliminar(id_cliente)
        return jsonify({"mensaje": f"Cliente id={id_cliente} eliminado correctamente"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


# ============================================================
# ENDPOINTS VIDEO
# ============================================================

@app.route("/videos", methods=["POST"])
def crear_video():
    data = request.get_json()
    for campo in ["isan_video", "titulo", "año", "duracion_minutos"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_video_dao()
    try:
        v = dao.crear(data["isan_video"], data["titulo"], data["año"], data["duracion_minutos"])
        return jsonify(video_to_dict(v)), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/videos", methods=["GET"])
def obtener_todos_videos():
    dao, session = get_video_dao()
    try:
        return jsonify([video_to_dict(v) for v in dao.obtener_todos()]), 200
    finally:
        session.close()

@app.route("/videos/titulo/<string:titulo>", methods=["GET"])
def obtener_video_por_titulo(titulo):
    dao, session = get_video_dao()
    try:
        videos = dao.obtener_por_titulo(titulo)
        if not videos:
            return jsonify({"error": f"No se encontraron videos con título '{titulo}'"}), 404
        return jsonify([video_to_dict(v) for v in videos]), 200
    finally:
        session.close()

@app.route("/videos/<string:isan_video>", methods=["GET"])
def obtener_video_por_isan(isan_video):
    dao, session = get_video_dao()
    try:
        v = dao.obtener_por_isan(isan_video)
        if not v:
            return jsonify({"error": f"No existe video con ISAN={isan_video}"}), 404
        return jsonify(video_to_dict(v)), 200
    finally:
        session.close()

@app.route("/videos/<string:isan_video>", methods=["PUT"])
def actualizar_video(isan_video):
    data = request.get_json()
    for campo in ["titulo", "año", "duracion_minutos"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_video_dao()
    try:
        v = dao.actualizar(isan_video, data["titulo"], data["año"], data["duracion_minutos"])
        if not v:
            return jsonify({"error": f"No existe video con ISAN={isan_video}"}), 404
        return jsonify(video_to_dict(v)), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/videos/<string:isan_video>", methods=["DELETE"])
def eliminar_video(isan_video):
    dao, session = get_video_dao()
    try:
        if not dao.obtener_por_isan(isan_video):
            return jsonify({"error": f"No existe video con ISAN={isan_video}"}), 404
        dao.eliminar(isan_video)
        return jsonify({"mensaje": f"Video ISAN={isan_video} eliminado correctamente"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


# ============================================================
# ENDPOINTS SERIE
# ============================================================

@app.route("/series", methods=["POST"])
def crear_serie():
    data = request.get_json()
    for campo in ["id_serie", "nombre", "temporadas"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_serie_dao()
    try:
        s = dao.crear(data["id_serie"], data["nombre"], data["temporadas"])
        return jsonify(serie_to_dict(s)), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/series", methods=["GET"])
def obtener_todas_series():
    dao, session = get_serie_dao()
    try:
        return jsonify([serie_to_dict(s) for s in dao.obtener_todos()]), 200
    finally:
        session.close()

@app.route("/series/<int:id_serie>", methods=["GET"])
def obtener_serie_por_id(id_serie):
    dao, session = get_serie_dao()
    try:
        s = dao.obtener_por_id(id_serie)
        if not s:
            return jsonify({"error": f"No existe serie con id={id_serie}"}), 404
        return jsonify(serie_to_dict(s)), 200
    finally:
        session.close()

@app.route("/series/<int:id_serie>", methods=["PUT"])
def actualizar_serie(id_serie):
    data = request.get_json()
    for campo in ["nombre", "temporadas"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_serie_dao()
    try:
        s = dao.actualizar(id_serie, data["nombre"], data["temporadas"])
        if not s:
            return jsonify({"error": f"No existe serie con id={id_serie}"}), 404
        return jsonify(serie_to_dict(s)), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/series/<int:id_serie>", methods=["DELETE"])
def eliminar_serie(id_serie):
    dao, session = get_serie_dao()
    try:
        if not dao.obtener_por_id(id_serie):
            return jsonify({"error": f"No existe serie con id={id_serie}"}), 404
        dao.eliminar(id_serie)
        return jsonify({"mensaje": f"Serie id={id_serie} eliminada correctamente"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


# ============================================================
# ENDPOINTS CATEGORIA
# ============================================================

@app.route("/categorias", methods=["POST"])
def crear_categoria():
    data = request.get_json()
    for campo in ["id_categoria", "nombre", "descripcion"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_categoria_dao()
    try:
        c = dao.crear(data["id_categoria"], data["nombre"], data["descripcion"])
        return jsonify(categoria_to_dict(c)), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/categorias", methods=["GET"])
def obtener_todas_categorias():
    dao, session = get_categoria_dao()
    try:
        return jsonify([categoria_to_dict(c) for c in dao.obtener_todos()]), 200
    finally:
        session.close()

@app.route("/categorias/<int:id_categoria>", methods=["GET"])
def obtener_categoria_por_id(id_categoria):
    dao, session = get_categoria_dao()
    try:
        c = dao.obtener_por_id(id_categoria)
        if not c:
            return jsonify({"error": f"No existe categoria con id={id_categoria}"}), 404
        return jsonify(categoria_to_dict(c)), 200
    finally:
        session.close()

@app.route("/categorias/<int:id_categoria>", methods=["PUT"])
def actualizar_categoria(id_categoria):
    data = request.get_json()
    for campo in ["nombre", "descripcion"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_categoria_dao()
    try:
        c = dao.actualizar(id_categoria, data["nombre"], data["descripcion"])
        if not c:
            return jsonify({"error": f"No existe categoria con id={id_categoria}"}), 404
        return jsonify(categoria_to_dict(c)), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/categorias/<int:id_categoria>", methods=["DELETE"])
def eliminar_categoria(id_categoria):
    dao, session = get_categoria_dao()
    try:
        if not dao.obtener_por_id(id_categoria):
            return jsonify({"error": f"No existe categoria con id={id_categoria}"}), 404
        dao.eliminar(id_categoria)
        return jsonify({"mensaje": f"Categoria id={id_categoria} eliminada correctamente"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


# ============================================================
# ENDPOINTS IDIOMA
# ============================================================

@app.route("/idiomas", methods=["POST"])
def crear_idioma():
    data = request.get_json()
    for campo in ["id_idioma", "nombre", "codigo"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_idioma_dao()
    try:
        i = dao.crear(data["id_idioma"], data["nombre"], data["codigo"])
        return jsonify(idioma_to_dict(i)), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/idiomas", methods=["GET"])
def obtener_todos_idiomas():
    dao, session = get_idioma_dao()
    try:
        return jsonify([idioma_to_dict(i) for i in dao.obtener_todos()]), 200
    finally:
        session.close()

@app.route("/idiomas/<int:id_idioma>", methods=["GET"])
def obtener_idioma_por_id(id_idioma):
    dao, session = get_idioma_dao()
    try:
        i = dao.obtener_por_id(id_idioma)
        if not i:
            return jsonify({"error": f"No existe idioma con id={id_idioma}"}), 404
        return jsonify(idioma_to_dict(i)), 200
    finally:
        session.close()

@app.route("/idiomas/<int:id_idioma>", methods=["PUT"])
def actualizar_idioma(id_idioma):
    data = request.get_json()
    for campo in ["nombre", "codigo"]:
        if campo not in data:
            return jsonify({"error": f"Campo requerido faltante: '{campo}'"}), 400
    dao, session = get_idioma_dao()
    try:
        i = dao.actualizar(id_idioma, data["nombre"], data["codigo"])
        if not i:
            return jsonify({"error": f"No existe idioma con id={id_idioma}"}), 404
        return jsonify(idioma_to_dict(i)), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route("/idiomas/<int:id_idioma>", methods=["DELETE"])
def eliminar_idioma(id_idioma):
    dao, session = get_idioma_dao()
    try:
        if not dao.obtener_por_id(id_idioma):
            return jsonify({"error": f"No existe idioma con id={id_idioma}"}), 404
        dao.eliminar(id_idioma)
        return jsonify({"mensaje": f"Idioma id={id_idioma} eliminado correctamente"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


# ------------------------------------------------------------
# Punto de entrada
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)