from datetime import datetime
import re

# Sua data de nascimento
ano_nascimento = 2005
mes_nascimento = 4
dia_nascimento = 9

# Calcular idade
hoje = datetime.now()
idade = hoje.year - ano_nascimento - ((hoje.month, hoje.day) < (mes_nascimento, dia_nascimento))

# Ler o README.md
with open("README.md", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Procurar e atualizar qualquer badge de idade
novo_conteudo = re.sub(
    r'!\[Idade\]\(https://img\.shields\.io/badge/Idade-\d+%20anos-[\w\d]+\)',
    f'![Idade](https://img.shields.io/badge/Idade-{idade}%20anos-blue)',
    conteudo
)

# Salvar mudanças
with open("README.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(novo_conteudo)
