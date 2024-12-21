from django.urls import path, include
from .views import UserRegisterView, UserDetailsView, UserDestroyView, UserLogoutView, UserUpdateView
# from .views import UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('list/', UserListView.as_view(), name='list_user'),
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('login/', TokenObtainPairView.as_view(), name='token_pair_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('logout/', UserLogoutView.as_view(), name='logout_user'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    path('details/<int:pk>', UserDetailsView.as_view(), name='user_details'),
    path('delete/<int:pk>', UserDestroyView.as_view(), name='destroy_user'),

    path('todos/', include('todos.urls')),
]
