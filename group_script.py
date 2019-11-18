import glob
import sys


def group_script(argv):
	if len(argv)<3:
		print "python group_script.py [path] [n_core] [username]"
		return
	path = argv[0]
	n_core = argv[1]
	USERNAME = argv[2]
	list_ = glob.glob(path+"/*.sh")	
	
	nscripts = int(round(len(list_)/ (float(n_core)) ))
	print nscripts	
	
	list_of_shell = []
	f0 = open("all_shell.sh","w")
	for i in range(0,nscripts):
		f = open("part_shell_"+str(i)+".sh","w")
		for j in range(0,int(n_core)):
			if not (j*int(n_core)+i) >= len(list_):
				f.write("sh "+list_[i+j*int(n_core)]+" & \n")
			else:
				print "end"
				break
		f.write("sleep 400 \n")
                f.write("echo 400s gone. Kill all job   \n")
                f.write("ps -ef | grep "+USERNAME+" | grep -v grep | grep -v sh | grep -v bash | grep -v sshd | grep -v tcsh | awk '{print $2}' | xargs kill -9")

		f0.write("sh part_shell_"+str(i)+".sh \n")
		
			

if __name__ == '__main__':
		
	group_script(sys.argv[1:])
