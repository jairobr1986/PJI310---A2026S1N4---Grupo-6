def classificar_risco(peso, altura, idade):
    """
    Classifica o risco metabólico com base no IMC e na Idade.
    Critérios: Clínica de Estética e Obesidade.
    """
    # Cálculo do IMC
    imc = peso / (altura ** 2)
    
    # 🔴 ALTA PRIORIDADE: Obesidade Grau III ou Obesidade Severa em Idosos
    if imc >= 40 or (imc >= 35 and idade >= 60):
        return "VERMELHA: ALTA PRIORIDADE"
    
    # 🟡 PRIORIDADE MÉDIA: Obesidade Grau I e II
    elif imc >= 30:
        return "AMARELO: PRIORIDADE MEDIA"
    
    # 🟢 PRIORIDADE BAIXA: Sobrepeso ou Peso Normal
    else:
        return "VERDE: PRIORIDADE BAIXA"

def formatar_imc(peso, altura):
    """Retorna o IMC arredondado para duas casas decimais."""
    return round(peso / (altura ** 2), 2)