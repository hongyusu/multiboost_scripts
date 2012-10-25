
import sys
feaNum=eval(sys.argv[1])
labNum=eval(sys.argv[2])
infile=sys.argv[3]
outfile=sys.argv[4]

fout=open(outfile,'w')
fout.write('@relation numerical\n')
for i in range(feaNum):
    fout.write('@attribute t%d real\n' % i)
fout.write('@attribute class {')
for i in range(labNum):
    fout.write('%d' % i)
    if i<(labNum)-1:
        fout.write(',')
    else:
        fout.write('}\n')
fout.write('@data\n')
fin=open(infile)
for line in fin:
    i=0
    words=line.strip().split(',')
    for word in words:
        if i-feaNum<0:
            fout.write('%s' % word)
        else:
            fout.write('%d %s' % (i-feaNum,word))
        if i==len(words)-1:
            fout.write('}\n')
        elif i<feaNum:
            fout.write(',')
        else:
            fout.write(' ')
        if i==feaNum-1:
            fout.write('{')
        i=i+1
fin.close()
fout.close()

