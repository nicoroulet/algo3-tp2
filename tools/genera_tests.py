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
	
	if (ej==1):
		subprocess.call(['sh', '-c', ('mkdir -p ../tests/ej1/n')])
		subprocess.call(['sh', '-c', ('rm -f ../tests/ej1/n/*')])
		subprocess.call(['sh', '-c', ('mkdir -p ../tests/ej1/km')])
		subprocess.call(['sh', '-c', ('rm -f ../tests/ej1/km/*')])
		subprocess.call(['sh', '-c', ('mkdir -p ../tests/ej1/kb')])
		subprocess.call(['sh', '-c', ('rm -f ../tests/ej1/kb/*')])
		for n in range(max_size/10, max_size+1, max_size/20):
			km, kb = 20, 20
			for i in range(cant):
				f=open("../tests/ej1/n/%d_%d.in" % (n,i), 'w')
				f.write("%d %d %d\n" %(n,km,kb))
				for j in range(n):
					f.write("%d %d %d\n" %(randrange(20), randrange(20), randrange(20)))
				f.close()
		for km in range(max_size/10, max_size+1, max_size/20):
			n, kb = 100, 20
			for i in range(cant):
				f=open("../tests/ej1/km/%d_%d.in" % (km,i), 'w')
				f.write("%d %d %d\n" %(n,km,kb))
				for j in range(n):
					f.write("%d %d %d\n" %(randrange(20), randrange(20), randrange(20)))
				f.close()
		for kb in range(max_size/10, max_size+1, max_size/20):
			km, n = 20, 100
			for i in range(cant):
				f=open("../tests/ej1/kb/%d_%d.in" % (kb,i), 'w')
				f.write("%d %d %d\n" %(n,km,kb))
				for j in range(n):
					f.write("%d %d %d\n" %(randrange(20), randrange(20), randrange(20)))
				f.close()
		
	if (ej==2):
		subprocess.call(['sh', '-c', ('mkdir -p ../tests/ej2/nm')])
		subprocess.call(['sh', '-c', ('rm -f ../tests/ej2/nm/*')])
		subprocess.call(['sh', '-c', ('mkdir -p ../tests/ej2/s')])
		subprocess.call(['sh', '-c', ('rm -f ../tests/ej2/s/*')])
		for n in range(max_size/10, max_size+1, max_size/20):
			s=100
			for i in range(cant):
				f=open("../tests/ej2/nm/%d_%d.in" % (n,i), 'w')
				f.write("%d %d %d\n" %(n,n,s))
				f.write("%d %d %d %d\n" %(randrange(n)+1, randrange(n)+1, randrange(n)+1, randrange(n)+1))
				for fila in xrange(n-1):
					for c in xrange(n-1):
						f.write("  %d  " % randrange(120))
					f.write("\n")
					for c in xrange(n):
						f.write("%d    " % randrange(120))
					f.write("\n")
				for c in xrange(n-1):
					f.write("  %d  " % randrange(120))
				f.close()
		n=50
		for s in range(max_size/10, max_size+1, max_size/20):
			for i in range(cant):
				f=open("../tests/ej2/s/%d_%d.in" % (s,i), 'w')
				f.write("%d %d %d\n" %(n,n,s))
				f.write("%d %d %d %d\n" %(randrange(n)+1, randrange(n)+1, randrange(n)+1, randrange(n)+1))
				for fila in xrange(n-1):
					for col in xrange(n-1):
						f.write("  %d  " % randrange(120))
					f.write("\n")
					for col in xrange(n):
						f.write("%d    " % randrange(120))
					f.write("\n")
				for col in xrange(n-1):
					f.write("  %d  " % randrange(120))
				f.close()
	if (ej==3):
		subprocess.call(['sh', '-c', ('rm -f ../tests/ej3/*')])
		for n in range(2*max_size/25, max_size+1, max_size/50):
			for i in range(cant):
				m=randrange(n*(n-1)/2)
				C=randrange(1,n**2)
				f=open("../tests/ej3/%d_%d.in" % (n,i), 'w')
				f.write("%d %d %d\n" %(n,m,C))
				s=set()
				while len(s) < m:
					t1, t2=(randrange(n), randrange(n))
					if not ((t1, t2) in s or (t2,t1) in s): s.add((t1,t2))
				for (t1,t2) in s:
					f.write("%d %d %d\n" %(t1,t2,randrange(2*C)))
				f.close()

'''
	if ej==1:
		dir_n, dir_km, dir_kb = "../tests/ej1/n", "../tests/ej1/km", "../tests/ej1/kb"
		subprocess.call(['sh', '-c', 'mkdir -p ../tests/ej1/n'])
		subprocess.call(['sh', '-c', 'mkdir -p ../tests/ej1/km'])
		subprocess.call(['sh', '-c', 'mkdir -p ../tests/ej1/kb'])
		
		for n in range(max_size/25, max_size+1, max_size/50):
			#max_km = 
			for k_m in range()
			for i in range(cant):
				f=open("%d_%03d.in" % (n,i),'w')
				km = randrange(0,)
				f.write()
'''