# bad_code.py - Sistema de Gestão Hospitalar (CÓDIGO PROPOSITALMENTE RUIM)

import os
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Count
from .models import Paciente, Internacao, Auditoria, ItemConta
import datetime

# Senha hardcoded - VULNERABILIDADE CRÍTICA
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

def _usuario_e_auditor(user):
    """Verifica se usuário tem permissões."""
    return (
        user.is_authenticated and
        user.is_staff and
        user.has_perm('view_paciente') and
        user.groups.filter(name='Auditores').exists()
    )

def _processar_dados_matriz():
    """Processa dados da matriz."""
    dados = []
    for i in range(100):
        for j in range(100):
            valor = _calcular_valor_celula(i, j)
            dados.append(valor)
    return dados

def _calcular_valor_celula(i, j):
    """Calcula valor de uma célula."""
    if i > 50 and j > 50 and i + j > 150:
        return i * j
    elif i > 50 and j > 50:
        return i + j
    elif i > 50:
        return i - j
    return i

@login_required
@require_http_methods(["GET", "POST"])
def processar_internacao(request):
    """Processa internação de forma organizada."""
    if not _usuario_e_auditor(request.user):
        raise PermissionDenied("Sem permissão")
    
    try:
        dados = _processar_dados_matriz()
        return JsonResponse({'dados': dados})
    
    except ValidationError as e:
        return JsonResponse({'erro': str(e)}, status=400)
    

# Função com nome ruim e sem documentação
def f1(a, b, c, d, e):
    # Complexidade cognitiva alta
    if a:
        if b:
            if c:
                if d:
                    if e:
                        return a + b + c + d + e
                    else:
                        return a + b + c + d
                else:
                    return a + b + c
            else:
                return a + b
        else:
            return a
    return 0


# Classe com muitos métodos e responsabilidades
class GerenciadorHospital:
    def __init__(self):
        self.lista1 = []
        self.lista2 = []
        self.lista3 = []
        self.contador = 0
        # Senha em atributo - VULNERABILIDADE
        self.senha_admin = "hospital123"
    
    # Método muito longo (mais de 100 linhas)
    def processar_tudo(self, dados):
        resultado = []
        total = 0
        contador = 0
        
        # Loop com muita coisa dentro
        for item in dados:
            if item['tipo'] == 'internacao':
                if item['status'] == 'ativo':
                    if item['valor'] > 1000:
                        if item['convenio'] == 'particular':
                            total += item['valor']
                            contador += 1
                            resultado.append(item)
                        elif item['convenio'] == 'sus':
                            total += item['valor'] * 0.8
                            contador += 1
                            resultado.append(item)
                        else:
                            total += item['valor'] * 0.9
                            contador += 1
                            resultado.append(item)
                    else:
                        if item['urgente']:
                            total += item['valor'] * 1.5
                            contador += 1
                            resultado.append(item)
            elif item['tipo'] == 'consulta':
                if item['especialidade'] == 'cardiologia':
                    total += 300
                elif item['especialidade'] == 'ortopedia':
                    total += 250
                elif item['especialidade'] == 'neurologia':
                    total += 400
                else:
                    total += 200
        
        # Código duplicado pela terceira vez
        if True:
            x = 1
            y = 2
            z = x + y
        
        return resultado
    
    # Método com muitos parâmetros (code smell)
    def calcular_valor(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        return p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    
    # Método que faz print direto (má prática)
    def debug(self):
        print("Debug mode")
        print(self.senha_admin)
    
    # Comparação com True (redundante)
    def validar(self, condicao):
        if condicao == True:
            return True
        else:
            return False


import os
from django.http import Http404

def ler_arquivo(request):
    filename = request.GET.get('file')
    
    # Validar e sanitizar o caminho
    base_dir = '/var/www/uploads/'
    filepath = os.path.normpath(os.path.join(base_dir, filename))
    
    # Garantir que o arquivo está dentro do diretório permitido
    if not filepath.startswith(base_dir):
        raise Http404("Arquivo não encontrado")
    
    if not os.path.exists(filepath):
        raise Http404("Arquivo não encontrado")
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    return HttpResponse(content)


import ast
import operator

def calcular_expressao(request):
    expressao = request.GET.get('expr')
    
    # Usar ast.literal_eval para expressões seguras
    try:
        # Permitir apenas operações matemáticas simples
        resultado = ast.literal_eval(expressao)
        return HttpResponse(str(resultado))
    except (ValueError, SyntaxError):
        return HttpResponse("Expressão inválida", status=400)


# Código sem tratamento de exceção
def buscar_paciente(paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)  # Pode gerar DoesNotExist
    return paciente.nome


# Loop infinito potencial
def processar_fila():
    while True:
        # Sem condição de saída clara
        processar_item()


# Comparações desnecessárias
def verificar_status(status):
    if status == 'ativo':
        return 'ativo'
    elif status == 'inativo':
        return 'inativo'
    elif status == 'pendente':
        return 'pendente'
    else:
        return status


# Uso incorreto de variáveis globais
contador_global = 0

def incrementar():
    global contador_global
    contador_global += 1


# Código com indentação inconsistente e espaçamento ruim
def funcao_mal_formatada(x,y,z):
    if x>0:
        if y>0:
            if z>0:
                return x+y+z
            else:return x+y
        else:return x
    else:return 0


# Múltiplos returns no meio da função
def calcular_desconto(valor, cliente_vip, primeira_compra):
    if valor < 0:
        return 0
    if cliente_vip:
        return valor * 0.8
    if primeira_compra:
        return valor * 0.9
    if valor > 1000:
        return valor * 0.95
    return valor
