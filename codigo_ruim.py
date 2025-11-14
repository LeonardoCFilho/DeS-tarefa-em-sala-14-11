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

# Função gigante com múltiplas responsabilidades
def processar_internacao(request):
    if request.method == 'GET' or request.method == 'POST' or request.method == 'PUT':
        try:
            # SQL Injection - VULNERABILIDADE CRÍTICA
            paciente_id = request.GET.get('id')
            query = "SELECT * FROM pacientes WHERE id = " + paciente_id
            
            # Código duplicado
            if request.user.is_authenticated:
                if request.user.is_staff:
                    if request.user.has_perm('view_paciente'):
                        if request.user.groups.filter(name='Auditores').exists():
                            # Complexidade ciclomática muito alta
                            dados = []
                            for i in range(100):
                                for j in range(100):
                                    if i > 50:
                                        if j > 50:
                                            if i + j > 150:
                                                dados.append(i * j)
                                            else:
                                                dados.append(i + j)
                                        else:
                                            dados.append(i - j)
                                    else:
                                        dados.append(i)
            
            # Variáveis não utilizadas
            x = 10
            y = 20
            z = 30
            nome_completo = "João da Silva"
            endereco = "Rua ABC, 123"
            telefone = "11999999999"
            
            # Código morto (nunca executado)
            if False:
                print("Isso nunca vai executar")
                resultado = processar_dados_especiais()
            
            # Magic numbers sem contexto
            if len(dados) > 42:
                resultado = dados[0] * 3.14159
                valor_final = resultado / 2.71828
            
            # Exceções genéricas demais
        except:
            pass
        
        # Sem validação de entrada
        paciente_nome = request.POST.get('nome')
        paciente_cpf = request.POST.get('cpf')
        
        # Concatenação de strings em loop (ineficiente)
        relatorio = ""
        for item in range(1000):
            relatorio = relatorio + "Item: " + str(item) + "\n"
        
        # Código duplicado novamente
        if request.user.is_authenticated:
            if request.user.is_staff:
                if request.user.has_perm('view_paciente'):
                    if request.user.groups.filter(name='Auditores').exists():
                        print("Usuário autorizado")
        
        # Retorno sem tratamento
        return HttpResponse("OK")


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


# Função com path traversal - VULNERABILIDADE
def ler_arquivo(request):
    filename = request.GET.get('file')
    # Permite ler qualquer arquivo do sistema!
    with open('/var/www/' + filename) as f:
        content = f.read()
    return HttpResponse(content)


# Uso de eval - VULNERABILIDADE CRÍTICA
def calcular_expressao(request):
    expressao = request.GET.get('expr')
    resultado = eval(expressao)  # Permite execução arbitrária de código!
    return HttpResponse(str(resultado))


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
