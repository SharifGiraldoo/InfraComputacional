
SALARIO_BASE = 2000000
DIAS_LABORADOS = 300


prima = (SALARIO_BASE * DIAS_LABORADOS) / 360
cesantias = (SALARIO_BASE * DIAS_LABORADOS) / 360
vacaciones = (SALARIO_BASE * DIAS_LABORADOS) / 720
intereses_cesantias = ((cesantias * 0.12) * (DIAS_LABORADOS)) / 360
total = prima+cesantias+vacaciones+intereses_cesantias
print(round(total,0))