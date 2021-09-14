from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "polls"
urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('<int:question_id>/', views.details, name="details")
]