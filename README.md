# Scripting

To maintain Python and Shell scripts 


**Best work so far:**

  1.RunAnyProgram.py 

  *Purpose*: To check for source file and run any program if the source file is found. 
   
  *Usage*: Run it with a config file as an argument. 
   
  *Config file*: A .ini file which contains following details- 
   
                source folder : full path to the directory of input file. 
                
                Source file : name of the source file. Wildcards accepted ( ex *Ad_Campaigns*.csv)
                
                script : Can be used to run any script. In case of SSIS package, use DTEXEC which is a utility to run ssis package from command line.
                
                script_args: any arguments to the above mentioned scripts. In case of ssis, full path to the .dtsx file. For multiple arguments, write them comma seperated (no space allowed).
             
  *Logs* : Logs are generated in the LOGS subdirectory at the same directory as the python script, log file name will be scriptname_date.log
