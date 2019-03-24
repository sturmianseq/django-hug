from django.urls import path

from . import views

urlpatterns = list(views.routes.urls())

urlpatterns += [
    path('3/', views.index3),
    path('4/', views.index4)
]
