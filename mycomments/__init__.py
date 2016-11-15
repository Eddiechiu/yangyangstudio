__version__ = "1.0"


def get_model():
    from mycomments.models import MyCommentsModel
    return MyCommentsModel


def get_form():
    from mycomments.forms import MyCommentsForm
    return MyCommentsForm