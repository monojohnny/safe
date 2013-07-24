from Tkinter import *
from subprocess import Popen, PIPE
import StringIO
import hashlib

dbfile="test.db"
db=None
sha1=None
values=None
current=0

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

def loadfile():
	global dbfile
	global db
	global sha1
	with open(dbfile) as f:
		data=f.read()
		db=eval(decrypt(data))
		del data
		sha1=hashlib.sha1()
		sha1.update( str(db) )
		print sha1.hexdigest() 
	
def savefile():
	global dbfile
	global db
	print t.get()
	with open(dbfile, "wb") as f:
		plain_file=StringIO.StringIO()
		plain_file.write(db)
		cypher=encrypt(plain_file.getvalue())
		f.write(cypher)
		plain_file.close()
		del plain_file
		del cypher

def prev():
	global db
	global current
	if current>0:
		current-=1
		print "prev"

def next():
	global db
	global current
	if current<len(db):
		current+=1
		print "next"


if __name__=='__main__':
	loadfile()
	root = Tk()
	menubar = Menu(root)
	root.config(menu=menubar)
	fileMenu=Menu(menubar)
	fileMenu.add_command(label='Save', command= savefile) 
	menubar.add_cascade(label="File",  menu=fileMenu)
	# Data
	values=[]
	for i, key in enumerate( db[current].keys() ):
 		Label(root, text=key,  borderwidth=1 ).grid(row=i,column=1)
		values.append( StringVar() )
		values[i].set(db[current][key])
 		Entry(root, text=db[current][key],  borderwidth=1, textvariable=values[i] ).grid(row=i,column=2)
	# Buttons
	Button(root, text="prev", command=prev).grid( row=len( db[current] ) , column=1 ) 
	Button(root, text="next", command=prev).grid( row=len( db[current] ), column=2 ) 
	
	root.mainloop()
