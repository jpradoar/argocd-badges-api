import os
import requests
from flask import Flask, render_template   

app = Flask(__name__)

ARGOCD_SERVER = os.getenv("ARGOCD_SERVER") # o svc interno de kubernetes ;) 
ARGOCD_TOKEN = os.getenv("ARGOCD_TOKEN")

def get_apps():
    headers = {"Authorization": f"Bearer {ARGOCD_TOKEN}"}
    url = f"{ARGOCD_SERVER}/api/v1/applications"
    resp = requests.get(url, headers=headers, verify=False) # verify=False Solo para dev, no para prod
    resp.raise_for_status()
    data = resp.json()
    return data.get("items", [])

@app.route("/", methods=['GET'])
def index():
    apps = get_apps()
    return render_template("index.html", apps=apps, argocd_server=ARGOCD_SERVER)

@app.route("/detailed", methods=['GET'])
def detailed():
    apps = get_apps()
    return render_template("detailed.html", apps=apps, argocd_server=ARGOCD_SERVER)

@app.route("/health", methods=['GET'])
def health():
    return {"status": "ok"}, 200

# Si ArgoCD no me responde con un json valido, claramente es que hay un problema
# entonces prefiero dejar la api como "NO ready" para que kubernetes no la levante 
# y quede como falsamente funcional
@app.route("/readiness", methods=['GET'])
def readiness():
    try:
        # solo un request rápido, no necesariamente todo el payload
        headers = {"Authorization": f"Bearer {ARGOCD_TOKEN}"}
        url = f"{ARGOCD_SERVER}/api/v1/applications?fieldsOnly=true"  # filtra para hacerlo más liviano
        resp = requests.get(url, headers=headers, verify=False, timeout=3)
        resp.raise_for_status()
        return {"status": "ready"}, 200
    except Exception as e:
        return {"status": "error", "detail": str(e)}, 500

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
