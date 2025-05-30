from rest_framework import viewsets
from .models import Veiculo
from .serializers import VeiculoSerializer
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .forms import VeiculoForm
import plotly.graph_objs as go
from collections import Counter


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

def home(request):
    # Lista fixa e completa de marcas para o filtro
    marcas = ['Audi', 'BMW', 'BYD', 'Caoa Chery', 'Chevrolet', 'Citroen', 'Dodge', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'JAC', 'Jeep', 'KIA', 'Land Hover', 'Mercedes Benz', 'Mitsubichi', 'Nissan', 'Pegeout', 'Renault', 'Suzuki', 'Toyota', 'Volkswagen', 'Volvo',]

    marca_filtrada = request.GET.get('marca')
    modelo_filtrado = request.GET.get('modelo')

    veiculos = Veiculo.objects.all()

    if marca_filtrada:
        veiculos = veiculos.filter(marca=marca_filtrada)
        modelos = Veiculo.objects.filter(marca=marca_filtrada).values_list('modelo', flat=True).distinct()
    else:
        modelos = Veiculo.objects.values_list('modelo', flat=True).distinct()

    if modelo_filtrado:
        veiculos = veiculos.filter(modelo=modelo_filtrado)

    mensagem = None
    if (marca_filtrada or modelo_filtrado) and not veiculos.exists():
        mensagem = "Nenhum veículo encontrado para o filtro selecionado."

    return render(request, 'home.html', {
        'marcas': marcas,
        'modelos': modelos,
        'veiculos': veiculos,
        'mensagem': mensagem,
        'marca_filtrada': marca_filtrada,
        'modelo_filtrado': modelo_filtrado,
    })

def editar_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)

    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VeiculoForm(instance=veiculo)

    return render(request, 'veiculos/form_veiculo.html', {'form': form, 'veiculo': veiculo})


def deletar_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('/')

    return render(request, 'veiculos/confirma_delete.html', {'veiculo': veiculo})

def grafico_veiculos_por_marca(request):
    veiculos = Veiculo.objects.all()
    marcas = [v.marca for v in veiculos]
    contagem = Counter(marcas)

    # Dados do gráfico
    data = [go.Bar(x=list(contagem.keys()), y=list(contagem.values()))]
    layout = go.Layout(title='Quantidade de Veículos por Marca')
    fig = go.Figure(data=data, layout=layout)

    # Gerar gráfico em HTML
    grafico_html = fig.to_html(full_html=False)

    return render(request, 'veiculos/grafico.html', {'grafico_html': grafico_html})