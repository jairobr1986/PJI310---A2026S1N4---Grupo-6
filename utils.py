def classificar_risco(peso, altura, idade):
    """Retorna: (Status Visual, Nível de Prioridade, Classificação de Peso)"""
    imc = peso / (altura ** 2)
    
    if imc >= 40:
        status, nivel, desc = "🔴 Alta ++", (1 if idade > 60 else 2), "Obesidade Grau III (Mórbida)"
    elif imc >= 35:
        status, nivel, desc = "🔴 Alta", (3 if idade > 60 else 4), "Obesidade Grau II (Severa)"
    elif imc >= 30:
        status, nivel, desc = "🔴 Alta", (3 if idade > 60 else 4), "Obesidade Grau I"
    elif imc >= 25:
        status, nivel, desc = "🟡 Média", 5, "Sobrepeso"
    elif imc < 18.5:
        status, nivel, desc = "🟡 Média", 5, "Abaixo do Peso"
    else:
        status, nivel, desc = "🟢 Baixa", 6, "Peso Ideal"

    if idade > 60 and imc >= 30: 
        status += " (Idoso)"
        
    return status, nivel, desc

def formatar_imc(peso, altura):
    return round(peso / (altura ** 2), 2)