import csv

import sys

def grafico(x1,x2,y1,y2,cor):

	return f' <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="2" /> '

def nome(a):

	return f' <text x="530" y="40" font-size="25" font-weight = "bold"> Covid-19: {a}</text>'

def eixo_x(data, i, x1, dias):

	if i == 0:

		return f' <text x="{x1-30}" y="560" font-size="16">{data[0]}</text>'

	elif i == (dias - 2):

		return f' <text x="{x1-30}" y="560" font-size="16">{data[dias-1]}</text>'

	elif dias%2 == 0 and i == dias/2:

		return f' <text x="{x1-30}" y="560" font-size="16">{data[i]}</text>'

	elif dias%2 != 0 and i == (dias-1)/2:

		return f' <text x="{x1-30}" y="560" font-size="16">{data[i-1]}</text>'

	else:
		
		return ""

def eixo_y_casos(lista_casos,i, y1, dias):

	if i == 0:

		return f' <text x="50" y="{y1+5}" font-size="16">{lista_casos[i]}</text>'
	
	elif i == (dias - 2):
		
		return f' <text x="1070" y="{y1+5}" font-size="16">{lista_casos[dias-2]}</text>'

	else:

		return ""

def eixo_y_mortes(lista_mortes,i, y3, dias):

	if i == 0:

		return f' <text x="50" y="{y3+5}" font-size="14">{lista_mortes[i]}</text>'
	
	elif i == (dias - 2):
		
		return f' <text x="1070" y="{y3}" font-size="14">{lista_mortes[dias-2]}</text>'

	else:

		return ""

def eixo_y_recuperados(lista_recuperados,i, y5, dias):

	if i == 0:

		return f' <text x="50" y="{y5+5}" font-size="16">{lista_recuperados[i]}</text>'
	
	elif i == (dias - 2):
		
		return f' <text x="1070" y="{y5+5}" font-size="16">{lista_recuperados[dias-2]}</text>'

	else:

		return ""
	

with open(sys.argv[1] + '.csv', 'r') as csv_file:
	
	csv_reader = csv.reader(csv_file, delimiter=' ')

	lista_casos = []
	
	lista_mortes = []

	lista_recuperados = []
	
	data = []

	a = sys.argv[1]

	for line in csv_reader:
	
		lista_casos.append(line[0])

		lista_mortes.append(line[2])

		lista_recuperados.append(line[4])

		data.append(line[5])

	dias = len(data)

	for i in lista_casos:
	
		s = i.replace(",", "")
	
		lista_casos[lista_casos.index(i)] = int(s)

	for i in lista_mortes:

		s = i.replace(",", "")

		lista_mortes[lista_mortes.index(i)] = int(s)

	for i in lista_recuperados:

		s = i.replace(",", "")

		lista_recuperados[lista_recuperados.index(i)] = int(s)

with open('grafico.svg', 'w') as svg:
	
	svg.write('<svg width="1200" height="700">')

	svg.write('<rect fill="white" width="100%" height="100%"/>')

	svg.write('<line x1="110" y1="70" x2="110" y2="535" stroke="black" stroke-width="3" />')

	svg.write('<line x1="110" y1="535" x2="1060" y2="535" stroke="black" stroke-width="3" />')

	svg.write('<text x="20" y="55" font-size="16" font-weight = "bold" font-family = "serif">Quantidade de pessoas</text>')

	svg.write('<text x="1070" y="540" font-size="16" font-weight = "bold" font-family = "serif">Tempo</text>')

	svg.write('<text x="530" y="600" font-size="16" fill="blue">Casos Confirmados</text>')	

	svg.write('<text x="530" y="630" font-size="16" fill="green">Recuperados</text>')

	svg.write('<text x="530" y="660" font-size="16" fill="red">Mortos</text>')

	svg.write(nome(a))

	i = 0

	x = 950/dias

	while i < (dias - 1):

		x1 = 110 + x*i

		x2 = x1 + x

		y1 = ((lista_casos[i] - lista_mortes[0])/(lista_casos[dias-1]-lista_mortes[0])) * -465 + 535

		y2 = ((lista_casos[i + 1] - lista_mortes[0])/(lista_casos[dias-1]-lista_mortes[0])) * -465 + 535

		y3 = ((lista_mortes[i] - lista_mortes[0])/(lista_casos[dias-1]-lista_mortes[0])) * -465 + 535

		y4 = ((lista_mortes[i + 1] - lista_mortes[0])/(lista_casos[dias-1]-lista_mortes[0])) * -465 + 535
				
		y5 = ((lista_recuperados[i] - lista_mortes[0])/(lista_casos[dias-1]-lista_mortes[0])) * -465 + 535

		y6 = ((lista_recuperados[i + 1] - lista_mortes[0])/(lista_casos[dias-1]-lista_mortes[0])) * -465 + 535

		svg.write(grafico(x1,x2,y1,y2,'blue'))
		svg.write(grafico(x1,x2,y3,y4,'red'))
		svg.write(grafico(x1,x2,y5,y6,'green'))

		svg.write(eixo_y_casos(lista_casos,i, y1, dias))

		svg.write(eixo_y_mortes(lista_mortes,i, y3, dias))

		svg.write(eixo_y_recuperados(lista_recuperados,i, y5, dias))

		svg.write(eixo_x(data, i, x1, dias))

		i = i + 1

	svg.write('</svg>')
