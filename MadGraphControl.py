import os
from optparse import OptionParser
usage="show something usefull -- for example: how to use this program"
parser = OptionParser(usage)
parser.add_option("-c","--GenConf" ,dest="GenConf"   ,help="Generate single conf from " ,action = "store", type=str,default = "cmd-240718-highvt-PPscan.dat")
parser.add_option("-p","--Prefix"  ,dest="Prefix"    ,help="process prefix            " ,action = "store", type=str,default = "pp_HppHmm")
parser.add_option("--Process"      ,dest="process"   ,help=" process  todo                " ,action = "store", type=str,default = "p p > H++ H-- " )
parser.add_option("--EXCL"         ,dest="EXCL"      ,help="exclsion              "      ,action = "store", type=str,default = "define EXCL = H ha h" )

parser.add_option("-g","--Do_GenConf" ,dest="do_GenConf" ,help="Generate conf  " ,action = "store_true", default = False)
parser.add_option("-r","--do_running" ,dest="do_running" ,help="run command  "   ,action = "store_true", default = False)

parser.add_option("-m","--mg5_exe_path" ,dest="mg5_exe_path" ,help="mg5_exe_path  " ,action = "store",type=str, default = os.environ['madgraph_path'])
parser.add_option("--mul" ,dest="do_multicores" ,help="do_multicores  " ,action = "store_true", default = False)
parser.add_option("--cmd" ,dest="command" ,action = "store", type=str)
parser.add_option("--debug_mode" ,dest="debug_mode" ,action = "store_true", default = False)
parser.add_option("--time_limit" ,dest="time_limit" ,action = "store", type=float,default = 10e10)
<<<<<<< HEAD
parser.add_option("--mad_spin" ,dest="mad_spin" ,action = "store_true",default = False)
=======
parser.add_option("--mad_spin" ,dest="mad_spin" ,action = "store_true",default = True)
>>>>>>> 071ccbccf2b82db148544cbf3d34ac0409c0bbff

(options,args)=parser.parse_args()

def global_start(suffix=""):
	out_str =  "import model Type-II_seesaw_mix_UFO\n"
	if not options.EXCL == "":
		out_str+=options.EXCL+"\n"
		out_str+="define Hpp = H++ H-- \n"
		out_str+="define Hp = H+ H- \n"
		out_str+="generate "+options.process+"/EXCL\n"
	else:
		out_str+="generate "+options.process+"\n"
		out_str+="define Hpp = H++ H-- \n"
		out_str+="define Hp = H+ H- \n"
		out_str+="output "+options.Prefix+suffix+"\n"
	return out_str


#================#======================================
global_setting = "4\n\
0\n\
set LHC 13\n\
set bwcutoff 1000\n\
set cut_decays F\n\
set pdfwgt F\n\
set use_syst F\n\
set fixed_ren_scale F\n\
set fixed_fac_scale F\n"


class ParaM(object):

	title  = ""
	cmd = ""
	process = ""
	excl = ""
	paraM = {}
	__paraM = [#"wh__2",
			#"wha",
			#"whp",
			#"whpp",
			"mHpp",
			"mHp",
			"mha",
			"mh__2",
			"mh",
			"vt",
			"sinalpha",
			"mu",
			"lam1",
			"lam2",
			"lam3",
			"lam4"]

	xsec_cen = -1
	xsec_err = -1
	dict_br = {}
	def __init__(self,title,cmd):

		self.title  = title
		self.cmd    = cmd	
		self.__translate_cmd()

	def __translate_cmd(self):

		for para in self.__paraM:
			if not para in ["mHpp","mHp","mh__2","mha"]:
				for i in self.cmd:
					if i.find(para)>-1:
						self.paraM[para] = i.split(" ")[-1].replace("\n","")
						break
			elif para in ["mHpp"]:
				if i.find(para)>-1:
					self.paraM[para] = i.split(" ")[-1].replace("\n","")
                                        break
			elif para in ["mHp"]:
				if i.find(para)>-1 and i.find("mHpp")==-1:
                                        self.paraM[para] = i.split(" ")[-1].replace("\n","")
                                        break
			elif para in ["mh__2"]:
                                if i.find(para)>-1:
                                        self.paraM[para] = i.split(" ")[-1].replace("\n","")
                                        break
			elif para in ["mha"]:
                                if i.find(para)>-1:
                                        self.paraM[para] = i.split(" ")[-1].replace("\n","")
                                        break
			elif para in ["mh"]:
				#mh should be always 125
				self.paraM[para] = "125.0"

		for i in self.cmd:
			if i.find("generate") > -1:
				self.process = i.replace("\n","")
			elif i.find("define") > -1:
				self.excl = i.replace("\n","")
	
	def set_xsec(self,cs_str):
		self.xsec_cen =  cs_str.split(" ")[cs_str.split(" ").index("+-")-1]
		self.xsec_err = cs_str.split(" ")[cs_str.split(" ").index("+-")+1]

<<<<<<< HEAD
	def set_br(self,br_list):

=======
	def set_br(self,br_list,debug=False):
		
		
>>>>>>> 071ccbccf2b82db148544cbf3d34ac0409c0bbff
		self.dict_br[br_list[0]] = {}
		self.dict_br[br_list[0]]["particle"] = br_list[0]
		self.dict_br[br_list[0]]["width"]    = br_list[1]
		if debug:
			print "debug set_br"
			print br_list
		for elem in br_list:
			if debug:
				print "debug set_br elem",elem
			if br_list.index(elem)>1 and not elem == "":
				fs = []
				br = ""
				for detail in elem.split(" "):
					if not detail == "":
						if detail.find(".")>-1:
							br = detail	
						else:
							fs.append(detail)
				
				fs_str = "decay: "+fs[0]+"_"+fs[1]
<<<<<<< HEAD
		self.dict_br[br_list[0]][fs_str] = br
=======
				if debug:
                		        print "debug set_br fs_str"
		                        print fs_str
				self.dict_br[br_list[0]][fs_str] = br
>>>>>>> 071ccbccf2b82db148544cbf3d34ac0409c0bbff
			
	def AsStr(self):
		print self.paraM
		print self.xsec_cen,self.xsec_err
		print self.dict_br	
	
	def to_xml(self):
		import xml.dom.minidom
		doc = xml.dom.minidom.Document() 
		root = doc.createElement('single_run') 
		root.setAttribute('excl',    self.excl)
		root.setAttribute('process', self.process)
		doc.appendChild(root) 
		#save parameters
		nodepara = doc.createElement("parameters")
		for para in self.__paraM:
			node_detail = doc.createElement("parameter")
			node_detail.setAttribute( "name",para )
			node_detail.setAttribute( "value",str(self.paraM[para]) )
			#node_detail.appendChild(doc.createTextNode( str(self.paraM[para]) ))
			nodepara.appendChild(node_detail)
		root.appendChild(nodepara)
		#save cross_section
		nodecs = doc.createElement("cross_section")	
		node_cscen = doc.createElement("xsec_central_value")
		node_cscen.setAttribute( "value",str(self.xsec_cen) )
		nodecs.appendChild(node_cscen)
		node_cserr = doc.createElement("xsec_central_error")
                node_cserr.setAttribute( "value",str(self.xsec_err) )
		nodecs.appendChild(node_cserr)
		root.appendChild(nodecs)

		if options.mad_spin:
			#save branch ratio
			node_decay_all = doc.createElement("DECAY")
			
			for particle in self.dict_br:
				node_decay = doc.createElement("BSM_HIGGS")
				node_decay.setAttribute( "particle" ,self.dict_br[particle]["particle"] )
				node_decay.setAttribute( "width" ,self.dict_br[particle]["width"] )
		
				for comp in self.dict_br[particle]:
					if comp.find("decay") > -1:
<<<<<<< HEAD
=======
						#print "DDDBUUGGG:",comp
>>>>>>> 071ccbccf2b82db148544cbf3d34ac0409c0bbff
						node_br = doc.createElement("decay")
						node_br.setAttribute( "final_state"  ,comp.replace("decay: ","") )
						node_br.setAttribute( "branch_ratio" ,self.dict_br[particle][comp] )
						node_decay.appendChild(node_br)
				node_decay_all.appendChild(node_decay)
			root.appendChild(node_decay_all)


		fp = open(self.title.replace("dat","xml"), 'w')
		doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")		
		

def multi_run():
	import os
	cores = int(os.environ['defined_cores'])
	import glob
	config_files = glob.glob('pp_HppHmm_config/*.dat')
	dict_process = {}
	for i in range(0,len(config_files),cores):
		dict_process[i] =  config_files[i:i+cores]
		#print dict_process[i]
	#print len(config_files),len(dict_process)
	for i in dict_process:
		import multiprocessing
		pool = multiprocessing.Pool(processes=cores)
		pool.map(gen_raw_data_conf, dict_process[i])
		os.system('killall check')
		os.system('killall f951')
		os.system('killall make')
		os.system('killall gfortran')
		os.system('rm -f ME5_debug')
		os.system('rm py.py')
		os.system('rm nsqso_born.inc')
		import time 
		time.sleep(30)
		for dir_ in dict_process[i]:
			direc = dir_.split('.')[0]
			path_to_rm = direc.split('/')[1]
			try:
				os.system('rm -rf '+path_to_rm)
				os.system('rm -rf tmp*')
			except:
				continue
		os.system('mv *.xml pp_HppHmm_xml_data/')
		print "finished",i

def gen_raw_data_conf(command_dat):

	import os
	mg5_exe_path = os.environ['madgraph_path']
	return gen_raw_data(command_dat ,mg5_exe_path)

def gen_raw_data(command_dat ,mg5_exe_path, print_log = False , time_limit = 10e10 ):

	print "before import"
	import shlex,subprocess
        print "finish import"
	command_line  = mg5_exe_path+" "+command_dat
	args = shlex.split(command_line)
	print "args: ",args 
	p = subprocess.Popen(args, stdout=subprocess.PIPE ,stderr=subprocess.STDOUT)
	import time
	start_time = time.time()
        print "start time:",start_time
	print_branch_bit = False
	cross_section = ""
	decay_info = {}
	list_tag = []
	decay_tag = ""
	while True:
		line = p.stdout.readline()
		line = line.strip()
		if print_log and not line == "":
			print "debug",line 
		if line == "":
			time.sleep(5)
		is_time_to_kill  = time.time() - start_time
		if line.find("generating the production square matrix element") > -1 or is_time_to_kill > time_limit:
                        print "SUBPROCESS KILLED, time usage: ",is_time_to_kill ,"second"
                        p.terminate()
			if is_time_to_kill > time_limit:
				f = open("time_limit_"+command_dat.split("/")[-1],"w")
				return
                        break

		if line.find("Cross-section") > -1:
			#	print "result",line
			cross_section = line
		if line.find(" W E L C O M E  to  M A D S P I N ") > -1:
			print_branch_bit = True
		if print_branch_bit:
			#if line.find("INFO:") > -1:
			#		print "result",line
			if line.find("decay channels for")> -1:	
				decay_tag = line.split(" ")[4]
				if print_log:
					print "decay_tag,",decay_tag	
				list_tag.append(decay_tag)
				decay_info[decay_tag] = [line.split(" ")[4],line.split(" ")[9]]
				
			elif not decay_tag == "":
				#if print_log:
                                #        print "decay_debug",line
				if not line.find("BR") > 0:
					if print_log:
						print "decay_debug",line
					decay_info[decay_tag].append(line.replace("INFO:",""))
	f = open(command_dat)
	info = ParaM(command_dat.split("/")[-1],f.readlines())
	info.set_xsec(cross_section)
	for tag in list_tag:
		info.set_br(decay_info[tag])
	if print_log:
		info.AsStr()
	info.to_xml()
	import os
	os.system('killall check')
	return 

def Reader(file_name):
	
	f = open(file_name,"r")
	set_info = {}
	set_tag  = 0
	while True:
		line = f.readline()
		if line == "\n":
			continue
		if line == "":
		#	print "fin"
			break
		elif line.find("launch")>-1:
			set_tag +=1
			set_info[set_tag] = []
		elif not line.find("launch")>-1:
			set_info[set_tag].append(line.replace("\n",""))
	return set_tag,set_info

def gen_conf(tag,info):

	f = open(options.Prefix+"_"+str(tag)+".dat","w")	
	f.write(global_start("_"+str(tag)))
	f.write("launch--name="+options.Prefix+"_"+str(tag)+"\n")
	f.write(global_setting)
	f.write("set vt 0.1 \n")
	for i in range(0,len(info)):
		f.write( info[i]+"\n" )
	f.write( "0\n" )

def script_single(tag,info):
	f = open(options.Prefix+"_"+str(tag)+".sh","w")
	f.write("echo run_"+options.Prefix+"_"+str(tag)+"\n")
	f.write("rm -rf run_"+options.Prefix+"_"+str(tag)+"\n")
	f.write("mkdir run_"+options.Prefix+"_"+str(tag)+"\n")
#	f.write("rm -rf "+options.Prefix+"_"+str(tag)+"\n")	
	f.write("cd run_"+options.Prefix+"_"+str(tag)+"\n")
        f.write("echo  cp_"+options.Prefix+"_"+str(tag)+"\n")
	f.write("cp "+os.environ['phenoHTM_code_path']+"/*.py . \n")
        f.write("echo python_"+options.Prefix+"_"+str(tag)+"\n")
<<<<<<< HEAD
	f.write("python HelloWorld.py ")
=======

>>>>>>> 071ccbccf2b82db148544cbf3d34ac0409c0bbff
	f.write("python MadGraphControl.py -r -m "+options.mg5_exe_path+" --cmd "+os.environ['phenoHTM_code_path']+"/"+options.Prefix+"_config/"+options.Prefix+"_"+str(tag)+".dat --debug_mode \n")
	f.write("echo python_"+options.Prefix+"_"+str(tag)+"\n")
	f.write("cp *.xml "+os.environ['phenoHTM_code_path']+"/"+options.Prefix+"_xml_data/"+" \n")
	#if not options.debug_mode:
		#f.write("cd ..\n")
		#f.write("rm -rf run_"+options.Prefix+"_"+str(tag)+"\n")

if __name__=='__main__':
	print "hello world"	
	if options.do_GenConf:

		os.system("rm -rf "+options.Prefix+"_config")
		os.system("mkdir  "+options.Prefix+"_config")
		set_tag,set_info = Reader(options.GenConf)
		for i in range(1,set_tag+1):
			gen_conf(i,set_info[i])
		os.system("mv "+options.Prefix+"*.dat "+options.Prefix+"_config")
		os.system("rm -rf "+options.Prefix+"_script")
		os.system("mkdir  "+options.Prefix+"_script")
		for i in range(1,set_tag+1):
                       script_single(i,set_info[i])
		os.system("mv "+options.Prefix+"*.sh "+options.Prefix+"_script")

	if options.do_running:

		print "do_running in py"
		gen_raw_data(command_dat = options.command ,mg5_exe_path=options.mg5_exe_path, print_log = options.debug_mode , time_limit = options.time_limit )	
	
	if options.do_multicores:

		multi_run()
		

	##test_datreader
	
	
	
	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
	
#	
		
