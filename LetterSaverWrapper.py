from XMLwrapper import XMLwrapper
import os
from datetime import datetime
from PySide import QtGui
def onOpenClick(self,key):
	par=XMLwrapper("data/letters.xml")
	itms=par.getLettersByKey(key)
	for i in self.listWidget.count():
		self.listWidget.takeItem(self.listWidget.currentRow())
	for i in itms:
		self.listWidget.addItem(i.strip())

def onDelClick(self,key):
	itm=self.listWidget.currentItem()
	par=XMLwrapper("data/letters.xml")
	os.remove("data/ltt/"+itm.text()+".ltt")
	par.delLetterByName(itm.text())
	self.listWidget.takeItem(self.listWidget.currentRow())

def onSaveClick(self,key,letter):
	par=XMLwrapper("data/letters.xml")
	arr_keys=key.split(",")
	now=datetime.now()
	now=str(now.day)+"."+str(now.month)+"."+str(now.year)+"  "+str(now.hour)+":"+str(now.minute)
	for i in arr_keys:
		if (par.putLetterByKey(i,now+"  "+key)==0):
			par.addKey(i)
			par.putLetterByKey(i,now+"  "+key)
	f=open("data/ltt/"+now+"  "+key+".ltt","w")
	print letter
	f.write(letter)
	f.close

def onItemChange(self):
	itm=self.listWidget.currentItem()
	linestring = open("data/ltt/"+itm.text()+".ltt", 'r').read()
	self.plainTextEditLetter.clear()
	self.plainTextEditLetter.setPlainText(linestring)

def onCopyClick(self,name,letter):
	letter=letter.replace("*",name)
	clipboard = QtGui.QApplication.clipboard()
	clipboard.setText(letter)

def onAllClick(self):
	par=XMLwrapper("data/letters.xml")
	itms=par.getAllLetters()
	for i in itms:
		self.listWidget.addItem(i.strip())