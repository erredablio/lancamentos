from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from fluxo.models import Categoria, Ator, Lancamento
# Create your views here.

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
    s_categoria = Categoria.objects.get(pk=id)
    context = {'categorias':s_categoria}
    if request.method=='POST':        
        s_categoria.nome=request.POST['nomecategoria']
        s_categoria.save()
        return redirect('select_categoria')    
    return render(request, './fluxo/update_categoria.html', context)

def delete_categoria(request, id):
    s_categoria = Categoria.objects.get(pk=id)
    s_categoria.delete()
    return redirect('select_categoria')

def insert_ator(request):
    s_categoria = Categoria.objects.all()
    context = {'categorias':s_categoria}
    if request.method=='POST':
        post=Ator()
        post.categoria=get_object_or_404(Categoria, id=int(request.POST['selectcategoria']))
        post.nome=request.POST['nomecredor']
        post.status=1        
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
        return render(request, './fluxo/insert_ator.html', context)
    else:
        return render(request, './fluxo/insert_ator.html', context)

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
