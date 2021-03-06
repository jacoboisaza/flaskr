"""Authentication Module."""
import functools
from flask import (
    flash,
    url_for,
    redirect,
    render_template,
    g,
    request,
    session,
    current_app as app
)
from sqlalchemy.exc import (
    IntegrityError
)

from app.models.user import UserModel
from app.schemas.user import UserSchema


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("login"))

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    """
    Request intercerptor to load user data from session to Flask Global.

    If a user id is stored in the session, load the user object from
    the database into ``g.user``.
    """
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = UserSchema().dump(
            UserModel.query.get(user_id)
        )


@app.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        try:
            UserModel.add(
                username=request.form["username"],
                password=request.form["password"]
            )
        except IntegrityError:
            import traceback
            traceback.print_exc()
            # The username was already taken, which caused the
            # commit to fail. Show a validation error.
            error = f"User {request.form['username']} is already registered."
        else:
            # Success, go to the login page.
            return redirect(url_for("login"))

        flash(error)

    return render_template("auth/register.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        error = None
        user_model = UserModel.query.filter_by(
            username=request.form["username"]
        ).first()
        if user_model is None:
            error = "Incorrect username."
        elif not user_model.verify_password(
            request.form["password"]
        ):
            error = "Incorrect password."
        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user_model.id
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@app.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))
