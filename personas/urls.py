from django.urls import path
from .views import (
    PersonaListView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
)

urlpatterns = [
    path('', PersonaListView.as_view(), name='lista_personas'),
    path('nueva/', PersonaCreateView.as_view(), name='crear_persona'),
    path('editar/<int:pk>/', PersonaUpdateView.as_view(), name='editar_persona'),
    path('eliminar/<int:pk>/', PersonaDeleteView.as_view(), name='eliminar_persona'),
]