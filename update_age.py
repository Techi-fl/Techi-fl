from datetime import datetime

# Sua data de nascimento
birth_year = 2005
birth_month = 4
birth_day = 9

# Calcular idade
today = datetime.now()
age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

# Ler o README.md
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Atualizar o badge
new_content = content.replace(
    "![Idade](https://img.shields.io/badge/Idade-XX%20anos-blue)",
    f"![Idade](https://img.shields.io/badge/Idade-{age}%20anos-blue)"
)

# Salvar mudanças
with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_content)
