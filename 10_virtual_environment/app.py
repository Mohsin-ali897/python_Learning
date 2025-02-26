
#! Virtual environment
#? A Python virtual environment (venv) is simply a directory with a particular file structure. It has a bin subdirectory that includes links to a Python interpreter as well as subdirectories that hold packages installed in the specific venv.
# python -m venv myennv 
#? for CMD
#* myenv\Scripts\activate
#? for power shell
#* myenv\Scripts\Activate.ps1
#? for deactivate
#* deactivate
import pandas as pd    
print(pd.__version__())


#? pip freeze is used to list all python packages is used in current project
#* command to install all packages founded in requriment.txt pip install -r requriment.txt