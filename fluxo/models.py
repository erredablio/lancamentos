from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField(max_length=150)
    status = models.BooleanField(default=1)
    categoria = models.ForeignKey(Categoria, related_name='fk_categoria', on_delete=models.CASCADE)   
    credor = models.BooleanField(default=False)
    responsavel_pagamento = models.BooleanField(default=False)
    responsavel_conta = models.BooleanField(default=False)

    class Meta:
        db_table = 'Ator'

    def __str__(self):
        return self.nome
    
class Lancamento(models.Model):
    TIPO = [('E', 'Entrada'), ('S', 'Saída')]
    STATUS = [('A','Aberto'), ('P','Parcial'), ('Q','Quitado')]

    data_vencimento = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    data_pagamento = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)    
    credor = models.ForeignKey(Ator, related_name='fk_credor',on_delete=models.CASCADE, null=False, blank=False)
    responsavel_pagamento = models.ForeignKey(Ator, related_name='fk_responsavel_pagamento', on_delete=models.CASCADE, null=False, blank=False)
    responsavel_conta = models.ForeignKey(Ator, related_name='fk_responsavel_conta', on_delete=models.CASCADE, null=False, blank=False)
    descricao = models.TextField(max_length=150, null=True, blank=True)
    parcelas = models.IntegerField(default=0, null=False, blank=False)    
    valor_devido = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=False, blank=False)
    valor_pago = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=True)    
    tipo = models.CharField(default='S', max_length = 1, choices=TIPO, null=False, blank=False)
    status = models.CharField(default='A', max_length = 1, choices=STATUS, null=False, blank=False)
    
    class Meta:
        db_table = 'Lancamento'

    def __str__(self):
        return str(self.pk) + ' - Credor: ' + str(self.credor) + ' - Data Vencimento: ' + str(format(self.data_vencimento, '%d/%m/%Y')) + ' - Valor Devido: ' + str(self.valor_devido)
        
    
    
        
        
    