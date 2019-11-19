########################################

For Madgraph control

  First you need to do source prepare to set up environment.
  
  You can set your own madgraph path and the core you plan to use with your machine.
  
  Then run
  
  python MadGraphControl.py -g [optional -c [command file] --Process [process you want to see] --EXCL [exclusion you want to add]]
  
  to generate config and script for each subprocess.
  
  For example, python MadGraphControl.py -g  -c cmd-240718-highvt-PPscan.dat --Process 'p p > H++ H-- ' --EXCL 'define EXCL = H ha h'
  
  Then for running, the main part I suggest you to use 
  
  python MadGraphControl.py --mul
  
  For job reach the time limit(300s), you can rerun the script stored in pp_HppHmm_script folder. You can also use these script to submit condor but I am not supporting condor env setting.
  
########################################

For plot analysis.

  The main intereface is written in Analysis_Helper.py and Analysis.py.
  
  If you don't want to do to complex thing, you can try the style in Example_analysis.py
  
  I suggest you for each of you analysis target, write differenct script.
  
  
  
