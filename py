# main.py

import os, sys
from  app_functions import *
from code import InteractiveConsole

# InteractiveConsole class
# we added args to give the option to ad as many arguments as we like
class Console (InteractiveConsole):
   def __init__(self,*args):
       InteractiveConsole.__init__(self,*args)

USAGE = f"""
USAGE :
python {sys.argv[0]}

or with plugins

python {sys.argv[0]} <-p> <plugin> <plugin2> ... <plugin n>


"""

# global jobs list
# all jobs list

jobs =[]

def main():
   os.system('clear') # clear terminal (linux/mac) ,replace with cls for windows
   print(USAGE)
   plugin_option = sys.argv[1] # the -p option to load plugin/s
  
   global jobs

   keep_going =True # keep adding jobs flag
   print('starting ...')
   # reading jobs and saving them to jobs list
   while keep_going :
       job = read_job()
       save_job(job)
       more = input('continue  ? [y/n]')
       if more.lower() == 'n':
           break
   print("#" * 50)
   print(jobs)
   print("*" * 50,'\n')
  

   # check if -p option is chosen , then create console object
   # and read the content (python instructions)of the plugin file
   # and run it
   if plugin_option.lower() =='-p':
       plugins_names = sys.argv[2:]
       print('loading plugin/s : '+', '.join(plugins_names) )
      
      
       # iterate through all plugins, load them "read", and execute them one by one
       for plugin in plugins_names:
           c = Console()
           print(f'reading plugin : {plugin}')
            # open a file
           plugin_file = open(plugin,'r')
           #read valid python instructions(programs) regardless of the extension of the file
           instructions = plugin_file.read()
           # execute
           c.runcode(instructions)


if __name__ == "__main__":
   main()