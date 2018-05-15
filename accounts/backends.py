from django.contrib.auth.models import User

class EmailAuth:
    """Auth an user by email"""
    
    def authenticate(self, username=None, password=None):
        """Get instance of user"""
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """Used bu the django auth system to retrieve an user"""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None