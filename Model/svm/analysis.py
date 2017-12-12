hit = [[0., 0.], [0., 0.]]
cnt = [0., 0.]
with open('result.txt') as fi:
	for l in fi:
		l = map(lambda x: int(x), l.strip().split(' '))
		cnt[l[0]] += 1
		hit[l[0]][l[1]] += 1

print cnt
print hit

print 

print '0: recall: %f; precision: %f'%(hit[0][0]/cnt[0], hit[0][0]/(hit[0][0] + hit[1][0]))
print '1: recall: %f; precision: %f'%(hit[1][1]/cnt[1], hit[1][1]/(hit[1][1] + hit[0][1]))
