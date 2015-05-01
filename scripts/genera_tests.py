from sys import argv
import subprocess
from random import randrange

usage="""Usage: python genera_tests.py <ej> <tamanio maximo> <cantidad de cada tamanio> <otros params>
"""
if len(argv) < 4:
	print usage
else:
	ej, max_size, cant = [int(i) for i in argv[1:4]]
	subprocess.call(['sh', '-c', 'mkdir -p ../tests'])
	subprocess.call(['sh', '-c', ('mkdir -p ../tests/ej%d' % ej)])
	subprocess.call(['sh', '-c', ('rm -f ../tests/ej%d/*' % ej)])
	if (ej==3):
		for n in range(max_size/25, max_size+1, max_size/50):
			for i in range(cant):
				m=randrange(n*(n-1)/2)
				C=randrange(1,n)
				f=open("../tests/ej3/%d_%d.in" % (n,i), 'w')
				f.write("%d %d %d\n" %(n,m,C))
				s=set()
				while len(s) < m:
					t1, t2=(randrange(n), randrange(n))
					if not ((t1, t2) in s or (t2,t1) in s): s.add((t1,t2))
				for (t1,t2) in s:
					f.write("%d %d %d\n" %(t1,t2,randrange(2*C)))
				f.close()

"""
	if ej==1:
		usage2="otros params: max_km max_kb"
		if len(argv) < 6:
			print usage
			print usage2
		else:
			max_km, max_kb = argv[4:6]
			dir_n, dir_km, dir_kb = "../tests/ej1/n", "../tests/ej1/km", "../tests/ej1/kb"
			subprocess.call(['sh', '-c', 'mkdir -p ../tests/ej1/n'])
			subprocess.call(['sh', '-c', 'mkdir -p ../tests/ej1/km'])
			subprocess.call(['sh', '-c', 'mkdir -p ../tests/ej1/kb'])
			for n in range(gran, max_size, gran):
				for k_m in range(k_m)
				for i in range(cant):
					f=open("%d_%03d.in" % (n,i),'w')
					km = randrange(0,)
					f.write()"""
