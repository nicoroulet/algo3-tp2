from sys import argv
import subprocess
from numpy import mean , log2
import matplotlib.pyplot as plt       

def f(x):
	return x[1]
def fn(x):
	return x[1]/x[0]
def fnlogn(x):
	return x[1]/(x[0]*log2(x[0]))
def fn2(x):
	return x[1]/(x[0]**2)

ej=int(argv[1])

if (ej==3):
	
	subprocess.call(['sh', '-c', 'mkdir -p ../graficos'])
	l=[[float(i) for i in x.strip().split()] for x in open("../tests/stats/ej3.stats", 'r')]
	l2 = [(i[0], mean(sorted([j[1] for j in l if j[0]==i[0]])[2:-2])) for i in l] ## saco 2 outliers de cada lado
	l3 = [l2[i] for i in range(len(l2)) if not l2[i] in l2[:i-1]] # a esta altura, l3 son tuplas (n, promedio de tiempos de tests de tamanio n)
	xs = [i[0] for i in l3]
	ys = [f(i) for i in l3]
	plt.xlabel("Cantidad de pozos")
	plt.ylabel("Tiempo de ejecucion (s)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej3.png")
	plt.show()
	
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	
	ys = [fn(i) for i in l3]
	plt.xlabel("Cantidad de pozos")
	plt.ylabel("Tiempo de ejecucion / n (s)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej3_sobre_n.png")
	plt.show()
		
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	
	ys = [fnlogn(i) for i in l3]
	plt.xlabel("Cantidad de pozos")
	plt.ylabel("Tiempo de ejecucion / (n*log(n)) (s)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej3_sobre_nlogn.png")
	plt.show()
	
	ys = [fn2(i) for i in l3]
	plt.xlabel("Cantidad de pozos")
	plt.ylabel("Tiempo de ejecucion / n^2 (s)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej3_sobre_n2.png")
	plt.show()