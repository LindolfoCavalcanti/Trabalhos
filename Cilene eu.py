total = int(input('Quantos verbos?'))
quant_eu = int(input('Quantos eu?'))
quant_tu = int(input('Quantos tu?'))
quant_ele = int(input('Quantos ele?'))
quant_nos = int(input('Quantos nos?'))
quant_vos = int(input('Quantos vos?'))
quant_eles = int(input('Quantos eles?'))

percentual_eu = (quant_eu / total) * 100
print('{:.2f}'.format(percentual_eu))
