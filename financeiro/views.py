from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from .models import Honorario
from .forms import HonorarioForm

@login_required
def lista_honorarios(request):
    honorarios = Honorario.objects.all().order_by('data_vencimento')
    return render(request, 'financeiro/lista_honorarios.html', {'honorarios': honorarios})

@login_required
def novo_honorario(request):
    form = HonorarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_honorarios')
    return render(request, 'financeiro/form_honorario.html', {'form': form})

# --- NOVA FUNÇÃO PARA EDITAR/BAIXAR ---
@login_required
def editar_honorario(request, id):
    honorario = get_object_or_404(Honorario, id=id)
    form = HonorarioForm(request.POST or None, instance=honorario)
    
    if form.is_valid():
        form.save()
        return redirect('lista_honorarios')
        
    return render(request, 'financeiro/form_honorario.html', {'form': form})