from flask_admin.contrib.sqla import ModelView

from .roles import RoleMixin


class UserView(RoleMixin, ModelView):
    can_delete = False
    page_size = 100
