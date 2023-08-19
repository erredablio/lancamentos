from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from fluxo.models import Categoria, Ator, Lancamento

def home(request):
    pass
    return render (request, './fluxo/home.html')

def select_categoria(request):
    s_categoria = Categoria.objects.all()
    context = {'categorias':s_categoria}
    return render (request, './fluxo/select_categoria.html', context)

def insert_categoria(request):
    if request.method=='POST':
        post=Categoria()
        post.nome=request.POST['nomecategoria']
        post.save()
        return redirect('select_categoria')
    else:
        return redirect('select_categoria')    

def update_categoria(request, id):
    s_categoria = get_object_or_404(Categoria, pk=id)
    context = {'categorias':s_categoria}
    if request.method=='POST':        
        s_categoria.nome=request.POST['nomecategoria']
        s_categoria.save()
        return redirect('select_categoria')    
    return render(request, './fluxo/update_categoria.html', context)

def delete_categoria(request, id):
    s_categoria = get_object_or_404(Categoria, pk=id)
    s_categoria.delete()
    return redirect('select_categoria')

def select_ator(request):
    s_ator = Ator.objects.all()
    s_categoria = Categoria.objects.all()
    context = {'atores':s_ator, 'categorias':s_categoria}
    return render (request, './fluxo/select_ator.html', context)

def insert_ator(request):
    s_categoria = Categoria.objects.all()
    context = {'categorias':s_categoria}
    if request.method=='POST':
        post=Ator()
        post.categoria=get_object_or_404(Categoria, id=int(request.POST['selectcategoria']))
        post.nome=request.POST['nomeator']
        if 'checkboxstatus' in request.POST:
            post.status=True
        else:
            post.status=False        
        if 'checkboxcredor' in request.POST:
            post.credor=True
        else: 
            post.credor=False        
        if 'checkboxresponsavelconta' in request.POST:
            post.responsavel_pagamento=True
        else:
            post.responsavel_pagamento=False
        if 'responsavelpagamento' in request.POST:
            post.responsavel_conta=True
        else:
            post.responsavel_conta=False
        post.save()
        # return render(request, './fluxo/insert_ator.html', context)
        return redirect('select_ator')
    else:
        # return render(request, './fluxo/insert_ator.html', context)
        return redirect('select_ator')
    
def update_ator(request, id):
    s_ator = get_object_or_404(Ator, pk=id)
    context = {'atores':s_ator}
    if request.method=='POST':
        s_ator.categoria=get_object_or_404(Categoria, id=int(request.POST['selectcategoria']))
        s_ator.nome=request.POST['nomeator']
        if 'checkboxstatus' in request.POST:
            s_ator.status=True
        else:
            s_ator.status=False

        if 'checkboxcredor' in request.POST:
            s_ator.credor=True
        else: 
            s_ator.credor=False 
                   
        if 'checkboxresponsavelconta' in request.POST:
            s_ator.responsavel_pagamento=True
        else:
            s_ator.responsavel_pagamento=False

        if 'responsavelpagamento' in request.POST:
            s_ator.responsavel_conta=True
        else:
            s_ator.responsavel_conta=False
        s_ator.save()
        return redirect('select_ator')
    return render(request, './fluxo/update_ator.html', context)

def delete_ator(request, id):
    s_ator = get_object_or_404(Ator, pk=id)
    s_ator.delete()
    return redirect('select_ator')


def insert_lancamento(request):
    s_responsavel_conta = Ator.objects.filter(responsavel_conta=True)
    s_responsavel_pagamento = Ator.objects.filter(responsavel_pagamento=True)
    s_credor = Ator.objects.filter(credor=True)
    context = {'credores':s_credor, 'responsaveis_pagamentos':s_responsavel_pagamento, 'responsaveis_contas':s_responsavel_conta}
    if request.method=='POST':
        post=Lancamento()
        post.data_vencimento=datetime.strptime(request.POST['dtvencimento'], '%d/%m/%Y')
        post.categoria=Categoria.objects.get(fk_categoria=int(request.POST['lancamentocredor']))
        post.credor=Ator.objects.get(id=int(request.POST['lancamentocredor']))
        post.responsavel_pagamento=Ator.objects.get(id=int(request.POST['lancamentoresponsavelpagamento']))
        post.responsavel_conta=Ator.objects.get(id=int(request.POST['lancamentoresponsavelconta']))
        post.descricao=request.POST['observacao']
        post.parcelas=1
        post.valor_devido=request.POST['vlrdevido']
        post.tipo=request.POST['lancamentotipo']
        post.status='A'  
        post.save()      
        return render(request, './fluxo/insert_lancamento.html', context)
    else:
        return render(request, './fluxo/insert_lancamento.html', context)
