from flask import Flask, request, render_template

app = Flask(__name__)

# 🔐 hidden secret in file
with open("config.txt", "w") as f:
    f.write("admin_key=SUPER_SECRET_KEY_777")

FLAG = "ZYR{ultimate_chain_exploit_07}"

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= PROFILE =================
@app.route("/profile")
def profile():
    user = request.args.get("user", "guest")

    return f"<h2>Welcome {user}</h2>"


# ================= VIEW FILE =================
@app.route("/view")
def view():
    file = request.args.get("file")

    try:
        # ❌ LFI vulnerability
        with open(file, "r") as f:
            return f.read()
    except:
        return "File not found"


# ================= ADMIN =================
@app.route("/admin")
def admin():
    key = request.args.get("key")

    # ❌ weak auth logic
    if key == "SUPER_SECRET_KEY_777":
        return f"<h2>Admin Panel</h2><p>{FLAG}</p>"

    return "Access Denied"


if __name__ == "__main__":
    app.run(debug=True)