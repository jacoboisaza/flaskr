"""Blog Module."""
from flask import (
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for
)
from werkzeug.exceptions import abort
import json

from app.models.family_leader import FamilyLeaderModel
from app.schemas.family_leader import FamilyLeaderSchema
from app.models.family import FamilyModel
from app.schemas.family import FamilySchema
from app.models.position import PositionModel
from app.schemas.position import PositionSchema
from app.models.post import PostModel
from app.schemas.post import PostSchema
from app.models.user import UserModel
from app.schemas.user import UserSchema
from app.models.bookmark import BookmarkModel
from app.schemas.bookmark import BookmarkSchema
from app.ctrl.auth import login_required
from app import bp


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    family_leaders = FamilyLeaderSchema(many=True).dump(
        FamilyLeaderModel.query.all()
    )
    families = FamilySchema(many=True).dump(
        FamilyModel.query.all()
    )
    positions = PositionSchema(many=True).dump(
        PositionModel.query.all()
    )
    posts = PostSchema(many=True).dump(
        PostModel.query.all()
    )
    users = UserSchema(many=True).dump(
        UserModel.query.all()
    )
    bookmarks = BookmarkSchema(many=True).dump(
        BookmarkModel.query.all()
    )
    return render_template(
        "blog/index.html",
        family_leaders=json.dumps(family_leaders, indent=4),
        families=json.dumps(families, indent=4),
        positions=json.dumps(positions, indent=4),
        posts=json.dumps(posts, indent=4),
        users=json.dumps(users, indent=4),
        bookmarks=json.dumps(bookmarks, indent=4)
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
            return redirect(url_for("app.index"))

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
        return redirect(url_for("app.index"))

    post = PostSchema().dump(post_model)
    return render_template("blog/update.html", post=post)


@bp.route("/<int:post_id>/delete", methods=("POST",))
@login_required
def delete(post_id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(post_id).delete()
    return redirect(url_for("app.index"))
