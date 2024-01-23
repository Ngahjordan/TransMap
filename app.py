from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management


# Mock data for demonstration
locations = [
    {"name": "Location 1", "details": "Details 1"},
    {"name": "Location 2", "details": "Details 2"},
    {"name": "Location 3", "details": "Details 3"},
]


# Route for viewing all locations and their details
@app.route("/locations")
def view_locations():
    if not session.get("is_admin"):
        return redirect(url_for("login"))

    return render_template("locations.html", locations=locations)


# Route for the login page
@app.route("/login")
def login():
    return render_template("login.html")


# Route to authenticate user credentials
@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = request.form.get("username")
    password = request.form.get("password")

    # Perform authentication logic here
    # Assume we have a user with username "admin" and password "password" as ADMIN

    if username == "admin" and password == "password":
        session["is_admin"] = True
        return redirect(url_for("view_locations"))
    else:
        return redirect(url_for("login"))


# Route to log out and clear the session
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)