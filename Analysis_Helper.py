class XML_single_data(object):
		
	xml_file = ""
	__dict_gen = {}	
	__dict_width = {}
	__dict_decay = {}
	def __init__(self,xml_file):

		self.xml_file = xml_file
		self.__dict_fill()

	def __dict_fill(self):
		from xml.dom.minidom import parse
		import xml.dom.minidom
		DOMTree = xml.dom.minidom.parse(self.xml_file)
		collection = DOMTree.documentElement
		if collection.hasAttribute("process"):
			self.__dict_gen["process"] = collection.getAttribute("process")
		if collection.hasAttribute("excl"):
			self.__dict_gen["excl"]    = collection.getAttribute("excl")
		for para_node in collection.getElementsByTagName("parameters")[0].childNodes:
			if para_node.nodeType == 1:
				self.__dict_gen[para_node.getAttribute("name")] = para_node.getAttribute("value")
		for xsec_node in  collection.getElementsByTagName("cross_section")[0].childNodes:
			if xsec_node.nodeType == 1:
				self.__dict_gen[ xsec_node.localName ] =  xsec_node.getAttribute("value")      

		for decay_node in  collection.getElementsByTagName("DECAY")[0].childNodes:
			if decay_node.nodeType == 1:
				self.__dict_width[decay_node.getAttribute("particle")] = decay_node.getAttribute("width")

			for fs_node in decay_node.childNodes:
				if fs_node.nodeType == 1:
					list_tmp = fs_node.getAttribute("final_state").split("_")
					self.__dict_decay[decay_node.getAttribute("particle"),list_tmp[0],list_tmp[1]] = fs_node.getAttribute("branch_ratio")
					self.__dict_decay[decay_node.getAttribute("particle"),list_tmp[1],list_tmp[0]] = fs_node.getAttribute("branch_ratio")

	def get_process_info(self):

		return self.__dict_gen["process"]+" "+self.__dict_gen["excl"]

	def get_xsec(self):

		return self.__dict_gen["xsec_central_value"]

	def get_xsecerr(self):
		
		return self.__dict_gen["xsec_central_error"]
	
	def get_parameter(self,para_name):

		if para_name in self.__dict_gen:
			return self.__dict_gen[para_name]
		else:
			print "check name of parameter"
			return -999

	def get_width(self,higgs_name):
		
		if higgs_name in self.__dict_width:
                        return  self.__dict_width[higgs_name]
                else:
                        print "check name of higgs"
                        return -999

	def get_branch_ratio(self,higgs_name,decay_par_1,decay_par_2):
		
		try:
		 	return self.__dict_decay[higgs_name,decay_par_1,decay_par_2]
		except:
			print "check name of higgs and final state particle"
			return 0

	def AsStr(self):	
		from xml.dom.minidom import parse
		import xml.dom.minidom
		DOMTree = xml.dom.minidom.parse(self.xml_file)
		collection = DOMTree.documentElement
		print "=================================================================="
		if collection.hasAttribute("process"):
			print "process: %s" % collection.getAttribute("process")
		if collection.hasAttribute("excl"):
	                print "excl: %s" % collection.getAttribute("excl")
		
		for para_node in collection.getElementsByTagName("parameters")[0].childNodes:
			if para_node.nodeType == 1:
				print para_node.getAttribute("name"), para_node.getAttribute("value")
			
		for xsec_node in  collection.getElementsByTagName("cross_section")[0].childNodes:
			if xsec_node.nodeType == 1:
				print xsec_node.localName, xsec_node.getAttribute("value")	
	
		for decay_node in  collection.getElementsByTagName("DECAY")[0].childNodes:
			if decay_node.nodeType == 1:
				print decay_node.getAttribute("particle"),"width:", decay_node.getAttribute("width")
			
			for fs_node in decay_node.childNodes:
				if fs_node.nodeType == 1:
					print decay_node.getAttribute("particle"),fs_node.getAttribute("final_state"),fs_node.getAttribute("branch_ratio")
	

def simple_analysis(xml_file):

	tmp = XML_single_data(xml_file = xml_file)
	print tmp.get_branch_ratio(higgs_name='H++', decay_par_1='w+',decay_par_2='w+')
	#tmp.AsStr()


def full_analysis_example(path = "pp_HppHmm_xml_data"):
		
	import glob
	list_of_xml = glob.glob(path+"/*.xml")
	for xml in list_of_xml:
		print "=============file:"+xml+"==================================="
		tmp = XML_single_data(xml_file = xml)
		print "process_info",tmp.get_process_info()
		print "xsec",tmp.get_xsec()

if  __name__ == '__main__':
	

	simple_analysis(xml_file = 'pp_HppHmm_xml_data/pp_HppHmm_1041.xml')
	#full_analysis_example()



