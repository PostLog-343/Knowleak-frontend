from accounts.models import User
import logging

# Class of authentication back-end
class MyAuthBackend(object):
    #Function of authenticate for login case.
    def authenticate(username, password):    
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None 
        except User.DoesNotExist:
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None
    
    # Function of find user:
    def get_user(self, user_id):
        try:
            user = User.objects.get(sys_id=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None
