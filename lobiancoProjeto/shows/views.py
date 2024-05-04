from django.shortcuts import redirect, render

from shows.models import Show

def INDEX(request):
    shows = Show.objects.all()
    context = {
        'shows':shows,
    }
    return render(request,'index.html',context)

def ADD(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        tipo = request.POST.get('tipo')
        assentos = request.POST.get('assentos')
        elenco = request.POST.get('elenco')
        secoes = request.POST.get('secoes')
        data = request.POST.get('data')
        horarios = request.POST.get('horarios')
  

        shows = Show(
            nome = nome,
            descricao = descricao,
            preco = preco,
            tipo = tipo,
            assentos = assentos,
            elenco = elenco,
            secoes = secoes,
            data = data,
            horarios = horarios
        )
        shows.save()
        return redirect('shows')
    
    return render(request,'index.html')

def EDIT(request, id):  # Adicione o argumento 'id' aqui
    show = Show.objects.get(id=id)
    context = {'show': show}
    return render(request, 'index.html', context)



def UPDATE(request, id):
    if request.method == "POST":
        shows = Show.objects.get(id=id) 
        shows.nome = request.POST.get('nome')
        shows.descricao = request.POST.get('descricao')
        shows.preco = request.POST.get('preco')
        shows.tipo = request.POST.get('tipo')
        shows.assentos = request.POST.get('assentos')
        shows.elenco = request.POST.get('elenco')
        shows.secoes = request.POST.get('secoes')
        shows.data = request.POST.get('data')
        shows.horarios = request.POST.get('horarios')
  
        shows.save()
        return redirect('shows')
    else:
        fun = Show.objects.all()
        context = {'shows':shows}
        return render(request, 'index.html', context)

def DELETE(request, id):
    Show.objects.filter(id=id).delete()
    return redirect('shows')
