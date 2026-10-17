from flask_login import current_user


class RoleMixin:
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_administrator()
