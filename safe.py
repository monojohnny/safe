from subprocess import Popen, PIPE
import pickle
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
		data=f.read()
		plain_data=decrypt(data)
		record=pickle.loads(plain_data)
		return record
	
def savefile(filename, record):
	print "save"
	plain_file=StringIO.StringIO()
	pickle.dump(record, plain_file)
	cypher=encrypt(plain_file.getvalue())
	with open(filename, "wb") as f:
		f.write(cypher)


class record:
	def __init__(	self,
		 	name, 
			acc_num,
			valid_from,
			expire,
			 card_num):
		self.name=name
		self.acc_num=acc_num
		self.valid_from=valid_from
		self.expire=expire
		self.card_num=card_num

if __name__=='__main__':
	r=record("Barclloyds", '123456', '01/01/1950', '01/01/2050','123456789012345')
	savefile('test.db', r)
	del r
	r2=loadfile('test.db')
	print r2.name
