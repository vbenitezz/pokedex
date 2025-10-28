import os, random, socket, boto3
from flask import Blueprint, jsonify, render_template_string
from dotenv import load_dotenv
from .pokeneas import pokeneas

load_dotenv()

pokenea_bp = Blueprint("pokenea", __name__)

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

S3_BUCKET = os.getenv("S3_BUCKET")

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
    image = p["image"]
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": S3_BUCKET, "Key": image},
        ExpiresIn=3600
    )
    return render_template_string("""
        <img src="{{url}}" width="250"><br>
        <p><i>{{p.quote}}</i></p>
        <p><b>Contenedor: </b>{{container_id}}</p>                          
    """, p=p, url=url, container_id=container_id)



