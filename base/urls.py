from django.urls import path
from. import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('',views.home, name="home"),
    path('room/<str:pk>/' , views.room, name="room"),

    path('create-room/', view.createRoom, name="create-room"),
    path('update-room/<str:pk>/', view.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', view.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', view.deleteMessage, name="delete-message"),
]