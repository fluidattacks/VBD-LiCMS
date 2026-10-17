from flask_admin.contrib.sqla import ModelView

from .roles import RoleMixin


class UserView(ModelView, RoleMixin):
    can_delete = False
    page_size = 100
