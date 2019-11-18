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
def plot_ROOT_style():
		
	path = "pp_HppHmm_xml_data"
	import array 
	import glob
	SinAlpha_200 = []
	xsec_200 = []

      
        gStyle.SetPaintTextFormat("1.4f");
        gROOT.LoadMacro("/atlas/haxu/dchwwana/RootUtils/AtlasStyle.C")
        SetAtlasStyle()
	
	mass_ = []
	xsec_ = []
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
		
	c1 = TCanvas("c1","c1",800,600)
	g1 = TGraph(len(arr_SinAlpha_200),arr_SinAlpha_200,arr_xsec_200)

	g1.Draw("ap")
	g1.GetXaxis().SetTitle("SinAlpha")
	g1.GetYaxis().SetTitle("xsec")
	c1.Print("SinAlphaxsec_200.pdf")
	
	g2 = TGraph(len(arr_mass_),arr_mass_,arr_sec_)

        g2.Draw("ap")
        g2.GetXaxis().SetTitle("mass_hpp")
        g2.GetYaxis().SetTitle("xsec")
	c1.Print("mass_hppxsec.pdf")
                
                
def plot_matplotlib_style():
	
	import numpy
	#import matplotlib
	import matplotlib.pyplot as plt
       
	mass_ = []
        xsec_ = []
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

	plt.scatter(arr_SinAlpha_200, arr_xsec_200, alpha=0.6)
	plt.savefig('./SinAlphaxsec_200.jpg')	
	
		
	 
if __name__ in '__main__':
		
#	analysis_example()                
#	plot_ROOT_style()
	plot_matplotlib_style()
