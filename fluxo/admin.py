from django.contrib import admin
from fluxo.models import Categoria, Ator, Lancamento

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nome')

admin.site.register(Categoria, CategoriaAdmin)

class AtorAdmin(admin.ModelAdmin):


    list_display = ('id', 'nome', 'status', 'categoria', 'credor', 'responsavel_pagamento', 'responsavel_conta')

admin.site.register(Ator, AtorAdmin)


class LancamentoAdmin(admin.ModelAdmin):

    list_display = ('id', 'data_vencimento', 'data_pagamento', 'categoria', 'credor', 'responsavel_pagamento', 'responsavel_conta', 'descricao', 'parcelas', 'valor_devido', 'valor_pago', 'tipo', 'status')

admin.site.register(Lancamento, LancamentoAdmin)
