from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text
from django.shortcuts import redirect

class AlreadyAuthenticated(AccessMixin):
    """Redirect To Home/Profile or Next If User is Authenticated"""

    def dispatch(self, request, *args, **kwargs):
        """Run this method to verify the authenication status"""
        if request.user.is_authenticated:
            if request.GET.get('next'):
                return HttpResponseRedirect(force_text(request.GET.get('next')))
            else:
                return redirect('login:menu')    
        return super().dispatch(request, *args, **kwargs)