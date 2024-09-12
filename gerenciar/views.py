from django.shortcuts import render, redirect, get_object_or_404
from .forms import SalaForm  # Certifique-se de ter criado um formulário SalaForm no forms.py
from .models import Sala, Reserva
from .forms import ReservaForm
from .models import Sala 
from django.contrib.auth.decorators import login_required



@login_required
def listar_salas(request):
    # Lógica para listar as salas
    pass



def home(request):
 return render(request, 'home.html')


def criar_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a nova sala no banco de dados
            return redirect('listar_salas')  # Redireciona para a lista de salas após salvar
    else:
        form = SalaForm()  # Cria um formulário vazio se o método não for POST
    return render(request, 'salas/form.html', {'form': form})  # Renderiza o template form.html com o formulário



# Listar Salas
def listar_salas(request):
    salas = Sala.objects.all()
    return render(request, 'salas/listar.html', {'salas': salas})

# Listar Reservas
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar.html', {'reservas': reservas})

# Criar Reserva
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/form.html', {'form': form})

# Editar Reserva
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/form.html', {'form': form})

# Cancelar Reserva
def cancelar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar_reservas')

def editar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)  # Busca a sala pelo ID ou retorna um erro 404 se não encontrada
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('listar_salas')  # Redireciona para a lista de salas após salvar
    else:
        form = SalaForm(instance=sala)  # Preenche o formulário com os dados da sala existente
    return render(request, 'salas/form.html', {'form': form})

# @login_required
# def profile(request):
#     return render(request, 'profile.html')  # Cria um template profile.html para essa página











