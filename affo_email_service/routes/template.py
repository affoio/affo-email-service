import flask

template_bp = flask.Blueprint("template", __name__, url_prefix="/template")


@template_bp.route("/<template_name>/preview/")
def preview(template_name):
    return flask.render_template(f"email/{template_name}"), 200
