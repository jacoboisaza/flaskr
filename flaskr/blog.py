"""Blog Module."""
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for
)
from flaskr.models.post import PostModel
from werkzeug.exceptions import abort

from flaskr.auth import login_required

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    return render_template(
        "blog/index.html",
        posts=[post.dump() for post in PostModel.query.all()]
    )


def get_post(post_id, check_author=True):
    """
    Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post_model = PostModel.query.get(post_id)
    if post_model is None:
        abort(404, f"Post id {post_id} doesn't exist.")
    elif check_author and post_model.author_id != g.user["id"]:
        abort(403, f"you are not the author of the post with id {post_id}.")
    return post_model


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            PostModel.add(
                title=title,
                body=body
            )
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:post_id>/update", methods=("GET", "POST"))
@login_required
def update(post_id):
    """Update a post if the current user is the author."""
    post_model = get_post(post_id)

    if request.method == "POST":
        post_model.update(
            title=request.form["title"],
            body=request.form["body"]
        )
        return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post_model.dump())


@bp.route("/<int:post_id>/delete", methods=("POST",))
@login_required
def delete(post_id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(post_id).delete()
    return redirect(url_for("blog.index"))
