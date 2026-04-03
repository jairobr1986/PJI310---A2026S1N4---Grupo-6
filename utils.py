def classificar_risco(temp, fc, pa, fr, ox):
    # Regras simplificadas inspiradas no Protocolo Manchester
    if ox < 90 or fc > 140 or fr > 30 or temp > 39:
        return "Vermelho - Emergência"
    elif ox < 94 or fc > 120 or fr > 24 or temp > 38:
        return "Amarelo - Urgente"
    elif fc > 100 or fr > 20 or temp > 37.5:
        return "Verde - Pouco Urgente"
    else:
        return "Azul - Não Urgente"
