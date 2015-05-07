from sys import argv,maxint
import subprocess
from numpy import mean , log2
import matplotlib.pyplot as plt       

# input: primera linea, tamano maximo, cant de tests de cada tamano
# cada linea adicional tiene tamano de entrada, numero de test (de ese tamano) y tiempo de ejecucion
def read_input(path):
	f=open(path, 'r')
	n, t = [int(i) for i in f.readline().strip().split()]
	
	d = dict()
	for i in f:
		i=i.strip().split()
		i=[int(i[0]), int(i[1]), float(i[2])]
		if not i[0] in d:
			d[i[0]] = [maxint]*t
		d[i[0]][i[1]] = min(d[i[0]][i[1]], i[2])
	''' 
	mat = [[maxint]*t]*n
	l=[[float(i) for i in x.strip().split()] for x in f]
	for i in l:
		mat[int(i[0])-1][int(i[1])-1] = min(mat[int(i[0])-1][int(i[1])-1], i[2])
	'''
	l = [(i[0], mean(i[1])) for i in d.items()]
	return l

def f(x):
	return x[1]
def fn(x):
	return x[1]/x[0]
def fnlogn(x):
	return x[1]/(x[0]*log2(x[0]))
def fn2(x):
	return x[1]/(x[0]**2)
def fn2logn(x):
	return x[1]/(x[0]**2*log2(x[0]))

ej=int(argv[1])

if (ej==1):
	subprocess.call(['sh', '-c', 'mkdir -p ../graficos'])
	l = read_input("../tests/stats/ej1_n.stats")
	xs = [i[0] for i in l]
	ys = [f(i) for i in l]
	plt.xlabel("Cantidad de etapas (n)")
	plt.ylabel("Tiempo de ejecucion (seg)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej1_n.png")
	plt.show()
	
	l = read_input("../tests/stats/ej1_km.stats")
	xs = [i[0] for i in l]
	ys = [f(i) for i in l]
	plt.xlabel("Cantidad de motos (k_m)")
	plt.ylabel("Tiempo de ejecucion (seg)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej1_km.png")
	plt.show()
	
	l = read_input("../tests/stats/ej1_kb.stats")
	xs = [i[0] for i in l]
	ys = [f(i) for i in l]
	plt.xlabel("Cantidad de buggys (k_b)")
	plt.ylabel("Tiempo de ejecucion (seg)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej1_kb.png")
	plt.show()

if (ej==2):
	subprocess.call(['sh', '-c', 'mkdir -p ../graficos'])
	'''
	l=[[float(i) for i in x.strip().split()] for x in open("../tests/stats/ej2_nm.stats", 'r')]
	l2 = [(i[0], mean([j[2] for j in l if j[1]==i[1] and j[0]==i[0]])) for i in l]
	l3 = [l2[i] for i in range(len(l2)) if not l2[i] in l2[:i-1]] # a esta altura, l3 son tuplas (n, promedio de tiempos de tests de tamanio n)
	'''
	l=read_input("../tests/stats/ej2_nm.stats")
	xs = [i[0] for i in l]
	ys = [f(i) for i in l]
	plt.xlabel("Dimension de la ciudad (n y m)")
	plt.ylabel("Tiempo de ejecucion (seg)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej2_nm.png")
	plt.show()
	
	ys = [fn(i) for i in l]
	plt.xlabel("Dimension de la ciudad (n y m)")
	plt.ylabel("Tiempo de ejecucion / n (seg)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej2_nm_sobre_n.png")
	plt.show()
	
	'''l=[[float(i) for i in x.strip().split()] for x in open("../tests/stats/ej2_s.stats", 'r')]
	l2 = [(i[0], mean([j[2] for j in l if j[1]==i[1] and j[0]==i[0]])) for i in l] ## saco 2 outliers de cada lado
	l3 = [l2[i] for i in range(len(l2)) if not l2[i] in l2[:i-1]] # a esta altura, l3 son tuplas (n, promedio de tiempos de tests de tamanio n)
	'''
	l=read_input("../tests/stats/ej2_s.stats")
	xs = [i[0] for i in l]
	ys = [f(i) for i in l]
	plt.xlabel("Cantidad de soldados iniciales")
	plt.ylabel("Tiempo de ejecucion (seg)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej2_s.png")
	plt.show()
	
if (ej==3):
	
	subprocess.call(['sh', '-c', 'mkdir -p ../graficos'])
	'''l=[[float(i) for i in x.strip().split()] for x in open("../tests/stats/ej3.stats", 'r')]
	l2 = [(i[0], mean(sorted([j[2] for j in l if j[1]==i[1] and j[0]==i[0]])[2:-2])) for i in l] ## saco 2 outliers de cada lado
	l3 = [l2[i] for i in range(len(l2)) if not l2[i] in l2[:i-1]] # a esta altura, l3 son tuplas (n, promedio de tiempos de tests de tamanio n)
	'''
	l3 = read_input("../tests/stats/ej3.stats")
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
	
	ys = [fn2logn(i) for i in l3]
	plt.xlabel("Cantidad de pozos")
	plt.ylabel("Tiempo de ejecucion / n^2*log(n) (s)")
	plt.plot(xs, ys, 'o')
	plt.savefig("../graficos/ej3_sobre_n2logn.png")
	plt.show()	