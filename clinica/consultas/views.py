from django.shortcuts import render, redirect
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Medico, Paciente, Consulta

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'consultas/cadastrar_paciente.html', {'form': form})

def cadastrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm()
    return render(request, 'consultas/cadastrar_medico.html', {'form': form})

def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'consultas/agendar_consulta.html', {'form': form})

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'consultas/listar_medicos.html', {'medicos': medicos})

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'consultas/listar_pacientes.html', {'pacientes': pacientes})

def listar_consultas(request):
    consultas = Consulta.objects.all()

    # Obter parâmetros de filtragem da requisição GET
    medico_id = request.GET.get('medico')
    paciente_id = request.GET.get('paciente')
    data_consulta = request.GET.get('data_consulta')
    hora_consulta = request.GET.get('hora_consulta')

    # Aplicar filtros conforme os parâmetros
    if medico_id:
        consultas = consultas.filter(medico_id=medico_id)
    if paciente_id:
        consultas = consultas.filter(paciente_id=paciente_id)
    if data_consulta:
        consultas = consultas.filter(data_consulta=data_consulta)  # Assumindo que há um campo de data
    if hora_consulta:
        consultas = consultas.filter(hora_consulta=hora_consulta)

    # Passar médicos e pacientes para popular o filtro no template
    medicos = Medico.objects.all()
    pacientes = Paciente.objects.all()

    return render(request, 'consultas/listar_consultas.html', {
        'consultas': consultas,
        'medicos': medicos,
        'pacientes': pacientes
    })

def detalhes_consultas(request, id):
    consultas = Consulta.objects.filter(medico_id = id).order_by('data_consulta')

    return render(request, 'consultas/detalhes_consultas.html', {
        'consultas': consultas
    })