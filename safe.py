from subprocess import Popen, PIPE
from csv import reader, writer
import StringIO


def encrypt(plain):
	p=Popen(["gpg", "-a", "-c"], stdout=PIPE, stdin=PIPE)
	p.stdin.write(plain)
	cypher=p.communicate()[0]
	p.stdin.close()
	return cypher

def decrypt(cypher):
	p=Popen(["gpg", "-a",  "-d"], stdout=PIPE, stdin=PIPE)
	p.stdin.write(cypher)
	plain=p.communicate()[0]
	p.stdin.close()
	return plain

def loadfile(filename):
	with open(filename) as f:
		cypher=f.read()
		plain_file=decrypt(cypher)
		spamreader=reader(plain_file.splitlines())
		for row in spamreader:
			print ', '.join(row)

def savefile(filename):
	plain_file=StringIO.StringIO()
    	spamwriter = writer(plain_file)
    	spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    	spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
	cypher=encrypt(plain_file.getvalue())
	with open(filename,"wb") as f:
		f.write(cypher)
	plain_file.close()
	
if __name__=='__main__':
	savefile('test.db')
	loadfile('test.db')
	
