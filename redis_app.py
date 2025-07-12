from flask import Flask, request, jsonify, send_from_directory
import redis
import os

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/add", methods=["POST"])
def add_user():
    try:
        data = request.get_json(force=True)
        if not data:
            raise ValueError("No s'ha rebut cap JSON")
        username = data.get("username")
        password = data.get("password")
        role = data.get("role")
        if not all([username, password, role]):
            raise ValueError("Falten camps obligatoris")
        r.hset(f"user:{username}", mapping={"password": password, "role": role})
        print(f"[INFO] Usuari afegit: {username}")
        return jsonify({"status": "usuari afegit"}), 200
    except Exception as e:
        print("[ERROR] /add:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/list", methods=["GET"])
def list_users():
    try:
        keys = r.keys("user:*")
        users = []
        for key in keys:
            user_data = r.hgetall(key)
            user_data["username"] = key.split(":", 1)[1]
            users.append(user_data)
        return jsonify(users), 200
    except Exception as e:
        print("[ERROR] /list:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
