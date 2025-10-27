import os, random, socket
from flask import Blueprint, jsonify, render_template_string
from .pokeneas import pokeneas

pokenea_bp = Blueprint("pokenea", __name__)

# Ruta 1
@pokenea_bp.route("/json")
def pokenea_json():
    p = random.choice(pokeneas)
    container_id = socket.gethostname()
    return jsonify({
        "id": p["id"],
        "name": p["name"],
        "height": p["height"],
        "ability": p["ability"],
        "container_id": container_id
    })

# Ruta 2
@pokenea_bp.route("/img_quote")
def pokenea_img_quote():
    p = random.choice(pokeneas)
    container_id = socket.gethostname()
    return render_template_string("""
        <img src="{{p.image}}" width="250"><br>
        <p>{{p.quote}}</p>
        <p><b>Contenedor: </b>{{container_id}}</p>                          
    """, p=p, container_id=container_id)



