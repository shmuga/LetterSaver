import xml.dom.minidom
from xml.dom.minidom import parse,parseString
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree
from BeautifulSoup import BeautifulStoneSoup

class XMLwrapper:
	def __init__(self,fil):
		self.file_name = fil;
		self.xml_file = parse(fil)

	def getLettersByKey(self,key):
		try:
			arr = self.xml_file.getElementsByTagName("key")
			for i in arr:
				if i.getAttribute("name") == key:
					letters = i
			let = []
			for i in letters.getElementsByTagName("letter"):
				let.append(i.firstChild.data)
			return let
		except:
			return 0

	def getAllLetters(self):
		try:
			let = []
			arr = self.xml_file.getElementsByTagName("key")
			for i in arr:
				letters = i
				for j in letters.getElementsByTagName("letter"):
					let.append(j.firstChild.data)
			return let
		except:
			return 0

	def putLetterByKey(self,_key,letter_in):
		try:
			tree = ElementTree()
			tree = ET.parse(self.file_name)
			root = tree.getroot()
			flag=1
			for i in root.findall("key"):
				root.remove(i)
				if i.get("name") == _key:
					let="<letter>"+letter_in+"</letter>"
					mini=ET.fromstring(let)
					i.append(mini)
					flag=0
				root.append(i)
			if flag==1:
				return 0
	   		res=open(self.file_name,"r+")
	   		res.write(BeautifulStoneSoup(ET.tostring(root)).prettify())
	   		res.close()
	   	except:
	   		return 0

   	def delLetterByName(self,name):
   		try:
	   		tree = ElementTree()
			tree = ET.parse(self.file_name)
			root = tree.getroot()
			for i in root.findall("key"):
				root.remove(i)
				for j in i:
					if j.text.strip()!=name:
						print j.text.strip()
					else:
						i.remove(j)
				root.append(i)
	   		res=open(self.file_name,"w")
	   		res.write(BeautifulStoneSoup(ET.tostring(root)).prettify())
	   		res.close()
		except:
			return 0;

	def addKey(self,key):
		tree = ElementTree()
		tree = ET.parse(self.file_name)
		root = tree.getroot()
		flag=0
		for i in root.findall("key"):
			if i.get("name")==key:
				flag=1
		if flag==0:
			mini=ET.fromstring("<key name=\""+key+"\"></key>")
			root.append(mini)
		res=open(self.file_name,"w")
	   	res.write(BeautifulStoneSoup(ET.tostring(root)).prettify())
	   	res.close()
	
	def delKey(self,key):
		tree = ElementTree()
		tree = ET.parse(self.file_name)
		root = tree.getroot()
		flag=0
		for i in root.iter("key"):
			if i.get("name")==key:
				root.remove(i)	
		res=open(self.file_name,"w")
		print ET.tostring(root)
	   	res.write(BeautifulStoneSoup(ET.tostring(root)).prettify())
	   	res.close()

 
