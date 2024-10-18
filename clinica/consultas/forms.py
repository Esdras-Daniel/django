from django import forms
from .models import Paciente, Medico, Consulta
from datetime import datetime, timedelta

def retorna_horarios_validos(medico, hora_consulta=None):
    horarios_disponiveis = []
    format = '%H:%M'
    hora_inicial = medico.hora_inicio
    hora_final = medico.hora_final

    while hora_inicial < hora_final:
        print(hora_inicial)

        horarios_disponiveis.append(hora_inicial.strftime(format))
        hora_inicial = (datetime.combine(datetime.today(), hora_inicial) + timedelta(hours=1)).time()
    
    return horarios_disponiveis


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'telefone', 'data_nascimento', 'endereco']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'especialidade', 'hora_inicio', 'hora_final']
        widgets = {
            'hora_inicio': forms.TimeInput(format='%H:%M'),
            'hora_final': forms.TimeInput(format='%H:%M')
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_final = cleaned_data.get('hora_final')

        if hora_final < hora_inicio:
            raise forms.ValidationError("O horário final deve ser maior que o horário de início!")
        
        return cleaned_data

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data_consulta', 'hora_consulta']

    def clean(self):
        clean_data = super().clean()
        medico = clean_data.get('medico')
        data_consulta = clean_data.get('data_consulta')
        hora_consulta = clean_data.get('hora_consulta')

        if medico.hora_final < hora_consulta:
            horarios_validos = retorna_horarios_validos(medico=medico)

            raise forms.ValidationError(f'O médico não atende neste horário. Horários do médico {medico.hora_inicio} - {medico.hora_final}')

        if Consulta.objects.filter(medico=medico, data_consulta=data_consulta, hora_consulta=hora_consulta).exists():

            raise forms.ValidationError(f"O médico {medico.nome} já tem horário agendado")
