####======================================================####
source prepare.sh
###gen conf
python MadGraphControl.py -g [optional -c [command file] --Process [process you want to see] --EXCL [exclusion you want to add]]
##
do python multicore running
python MadGraphControl.py --mul
###arragne script
python group\_script.py [script folder] [ncores] 
### analysis template, please setup ROOT or matplotlib your self
### I only provided how
python Analysis.py
