from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('cadastrar_medico/', views.cadastrar_medico, name='cadastrar_medico'),
    path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('listar_pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('listar_medicos/', views.listar_medicos, name='listar_medicos'),
    path('listar_consultas/', views.listar_consultas, name='listar_consultas'),
    path('detalhes_consulta/<int:id>/', views.detalhes_consultas, name='detalhes_consultas'),
]
