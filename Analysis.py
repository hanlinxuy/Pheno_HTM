import Analysis_Helper 
def analysis_example(path = "pp_HppHmm_xml_data"):

        import glob
        list_of_xml = glob.glob(path+"/*.xml")
        for xml in list_of_xml:
			print "=============file:"+xml+"==================================="
			tmp = Analysis_Helper.XML_single_data(xml_file = xml)
			print "process_info",tmp.get_process_info()
			print "xsec",tmp.get_xsec()
			print "parameter mu:",tmp.get_parameter("mu")
			print "parameter h++ mass:",tmp.get_parameter("mHpp")#,"h+ mass:",tmp.get_parameter("mHp")
			print "decay width",tmp.get_width("H++")
			print "decay branch ratio H++ > ta+ mu+",tmp.get_branch_ratio("H++",decay_par_1="ta+",decay_par_2="mu+")
try: 	
	from ROOT import *	
except:
	print "no ROOT installed"
     
                
def plot_matplotlib_style(path='pp_HppHmm_xml_data'):

	import numpy
	import matplotlib as mpl
	mpl.use('Agg')
	import matplotlib.pyplot as plt

	mass_ = []
	xsec_ = []
	SinAlpha_200 = []
	xsec_200 = []
	import glob
	import array
	list_of_xml = glob.glob(path+"/*.xml")
	for xml in list_of_xml:
		tmp = Analysis_Helper.XML_single_data(xml_file = xml)
		mass_.append(float(tmp.get_parameter("mHpp")))
		xsec_.append(float(tmp.get_xsec()))
		if abs(float(tmp.get_parameter("mHpp"))-200.)  < 2:
			SinAlpha_200.append(float(tmp.get_parameter("sinalpha")))
			xsec_200.append(float(tmp.get_xsec()))

	arr_SinAlpha_200 = array.array("f",SinAlpha_200)
	arr_xsec_200 =  array.array("f",xsec_200)

	arr_mass_ = array.array("f",mass_)
	arr_sec_  = array.array("f",xsec_)

	plt.scatter(arr_mass_, arr_sec_, alpha=0.6)
	plt.savefig('./SinAlphaxsec_200.png')	
	
		
class Analysis_interface(object):

	input_path = ''
	list_of_infile = []
	list_comp = []
	list_xaxis = []
	list_yaxis = []
	x_title = ''
	y_title = ''

	def __init__(self,input_path = 'pp_HppHmm_xml_data'):

		self.input_path = input_path
		import glob 
		self.list_of_infile = glob.glob(input_path+'/*.xml')

	def set_title(self,x,y):

		self.x_title = x
		self.y_title = y

	def loop_all_files(self,debug = False):

		for infile in self.list_of_infile:
			tmp_reader = Analysis_Helper.XML_single_data(xml_file = infile)
			if self.selection_criteria(tmp_reader):
				x,y = self.read_one_point(tmp_reader)
				if debug:
					print "loop_all_files debug",tmp_reader.get_parameter("mHpp")
				self.list_xaxis.append(x)
				self.list_yaxis.append(y)
				
	def read_one_point(self,reader):
		
		x = float(reader.get_parameter("mHpp"))
		y = float(reader.get_xsec())
		return x,y

	def selection_criteria(self,reader):

		PASS = bool( abs(float(reader.get_parameter("mHpp"))-200.)<2. )
		return PASS

	def get_chain(self):

		return [self.list_xaxis,self.list_yaxis]
	
	def plot_root(self,prefix = '' ,suffix = '',format_ = 'png'):

		import array 
		xarr = array.array("f",self.list_xaxis) 
		yarr =  array.array("f",self.list_yaxis)

		c1 = TCanvas('c1','c1',800,600)
		g1 = TGraph(len(xarr),xarr,yarr)
		g1.Draw("ap*")
		#g1.SetMarkerSize(10)
		g1.GetXaxis().SetTitle(self.x_title)
		g1.GetYaxis().SetTitle(self.y_title)
		c1.Print(prefix+self.x_title+'_vs_'+self.y_title+suffix+'.'+format_)

	def plot_matplotlib(self,prefix = '' ,suffix = '',format_ = 'png'):

		import array 
		import matplotlib as mpl
		mpl.use('Agg')
		import matplotlib.pyplot as plt
		xarr = array.array("f",self.list_xaxis) 
		yarr =  array.array("f",self.list_yaxis)
		plt.scatter(xarr, yarr, alpha=0.6)
		plt.xlabel(self.x_title)
		plt.ylabel(self.y_title)
		plt.savefig(prefix+self.x_title+'_vs_'+self.y_title+suffix+'.'+format_)	

class MultiCurve(object):

	x_title = ''
	y_title = ''
	list_comp = []
	dict_list_xaxis = {}
	dict_list_yaxis = {}
	dict_list_color = {}
	out_name = ''
	auto_range = False
	mini = 10e10
	maxi = -10e10

	lengend_config = {'x1':0.60,'y1':0.60,'x2':0.80,'y2':0.80}	

	def __init__(self,out_name = None):
		print 'init MultiCurve'
		self.out_name = out_name 

	def set_title(self,x,y):

		self.x_title = x
		self.y_title = y

	def SetRange(self,mini=None,maxi=None):

		if mini == None or maxi == None:
			self.auto_range = True
		else:
			self.mini = mini
			self.maxi = maxi

	def add_comp(self, name , list_x_axis, list_y_axis , color):

		if name not in self.list_comp:
			self.list_comp.append(name)
			self.dict_list_xaxis[name] = list_x_axis
			self.dict_list_yaxis[name] = list_y_axis
			self.dict_list_color[name] = color
	
	def set_legend_placement(self,lengend_config):

		self.lengend_config = lengend_config

	def plot_root(self,format_='png',debug=False):

		import array
		c1 = TCanvas('c1','c1',800,600)
		mg = TMultiGraph()
		gr = {}

		leg = TLegend(self.lengend_config['x1'],self.lengend_config['y1'],self.lengend_config['x2'],self.lengend_config['y2'])

		for comp in self.list_comp:
			x_arr = array.array("f",self.dict_list_xaxis[comp])
			y_arr = array.array("f",self.dict_list_yaxis[comp])
		
			if debug :
				print comp
				print x_arr
				print y_arr
			if self.auto_range:
				self.mini = min(y_arr,self.mini)
				self.maxi = min(y_arr,self.maxi)
			gr[comp] = TGraph(len(x_arr),x_arr,y_arr)
			gr[comp].SetLineColor(self.dict_list_color[comp])
			gr[comp].SetMarkerColor(self.dict_list_color[comp])
			leg.AddEntry(gr[comp],comp,'apl')
			mg.Add(gr[comp])
		mg.GetXaxis().SetTitle(self.x_title)
		mg.GetYaxis().SetTitle(self.y_title)
		mg.GetYaxis().SetTitleOffset(1)
		if not self.auto_range:
			mg.GetYaxis().SetRangeUser(self.mini, self.maxi)
		elif self.mini == None or self.maxi == None:
			print "range no change"
		elif self.auto_range:
			mg.GetYaxis().SetRangeUser(0.9* self.mini, 1.1*self.maxi)


		c1.SetLeftMargin(15)
		mg.Draw('ap*')
		leg.Draw('same')

		if not self.out_name == None:
			c1.Print(self.out_name+'.'+format_)
		else:
			c1.Print(self.x_title+'_vs_'+self.y_title+'.'+format_)


if __name__ in '__main__':
		
#	analysis_example()                
#	plot_ROOT_style()\
	test_multi = MultiCurve()
	test = Analysis_interface()
	test.loop_all_files()
	test.set_title('mass','xsec')
	test.plot_matplotlib()
