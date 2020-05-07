"""
Tratamento de exceções
"""

try:
    with open("teste.txt",'r') as f:
        print(f.readline())
except Exception as e:
    print("Erro %s"%e)