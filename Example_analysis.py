import os
import sys
sys.path.append(os.environ['phenoHTM_code_path'])
from Analysis import *
try: 	
	from ROOT import *	
except:
	print "no ROOT installed"

###########################################################
#support parameters from reader
#get_process_info()
#get_xsec()
#get_xsecerr()
#get_parameter(para_name)
#get_width(higgs_name)
#get_branch_ratio(higgs_name,decay_par_1,decay_par_2)
############################################################

class Analysis_interface_200(Analysis_interface):

    input_path = ''
    list_of_infile = []
    list_comp = []
    list_xaxis = []
    list_yaxis = []
    x_title = ''
    y_title = ''

    def read_one_point(self,reader):
        x = float(reader.get_parameter("lam1"))
        y = float(reader.get_xsec())
        return x,y

    def selection_criteria(self,reader):
        PASS = bool( abs(float(reader.get_parameter("mHpp"))-200.) < 2. )
        return PASS 

class Analysis_interface_450(Analysis_interface):

    input_path = ''
    list_of_infile = []
    list_comp = []
    list_xaxis = []
    list_yaxis = []
    x_title = ''
    y_title = ''

    def read_one_point(self,reader):
        x = float(reader.get_parameter("lam1"))
        y = float(reader.get_xsec())
        return x,y

    def selection_criteria(self,reader):
        PASS = bool( abs(float(reader.get_parameter("mHpp"))-450.) < 2. )
        return PASS 

class Analysis_interface_500(Analysis_interface):

    input_path = ''
    list_of_infile = []
    list_comp = []
    list_xaxis = []
    list_yaxis = []
    x_title = ''
    y_title = ''

    def read_one_point(self,reader):
        x = float(reader.get_parameter("lam1"))
        y = float(reader.get_xsec())
        return x,y

    def selection_criteria(self,reader):
        PASS = bool( abs(float(reader.get_parameter("mHpp"))-500.) < 2. )
        return PASS 

if __name__ == '__main__':

    analysis = MultiCurve('analysis_lam1_xsec')
    analysis.set_title('lam1','xsec')
    dict_comp = {}

    analysis_200 = Analysis_interface_200(input_path = os.environ['phenoHTM_code_path']+'/'+'pp_HppHmm_xml_data')
    analysis_200.loop_all_files(debug = False)
    dict_comp['Mhpp200'] = {'data':analysis_200.get_chain(),'color':'red'}

    analysis_450 = Analysis_interface_450(input_path = os.environ['phenoHTM_code_path']+'/'+'pp_HppHmm_xml_data')
    analysis_450.loop_all_files(debug = False)
    dict_comp['Mhpp450'] = {'data':analysis_450.get_chain(),'color':'blue'}  

    analysis_500 = Analysis_interface_500(input_path = os.environ['phenoHTM_code_path']+'/'+'pp_HppHmm_xml_data')
    analysis_500.loop_all_files(debug = False)
    dict_comp['Mhpp500'] = {'data':analysis_500.get_chain(),'color':'green'}  

    for comp in dict_comp:
        if len(dict_comp[comp]['data'][0])<1:
            print "not enough points"
            continue
        analysis.add_comp( name=comp , list_x_axis=dict_comp[comp]['data'][0], list_y_axis=dict_comp[comp]['data'][1] , color=dict_comp[comp]['color'])

    analysis.SetRange()
    analysis.plot_matplotlib(allow_pop=False,debug = False)
