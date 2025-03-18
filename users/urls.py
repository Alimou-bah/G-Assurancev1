from .views import profile_update
from django.urls import path
from users.views import CustomLoginView
from users.views import ActivationUserView
from users.views import LogoutView, ProfileUserView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('accounts/activation/<uid>/<token>', ActivationUserView.as_view(), name='confirm_user_activation'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('profile/update/', profile_update, name='profile_update'),
    path('profile/user', ProfileUserView.as_view(), name='profile_user'),

]
