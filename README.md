## GENERAL USAGE NOTES:

1. This file contains instructions about installing softwares and running the programs in Windows Environment.
1. The instructions in the file may not match the installation procedures in other operating systems like Mac OS, Ubuntu OS etc.
1. However, the programs are independent of any operating systems and will run successfully in all platforms once the initial installation has been done. 



## INSTALLATION GUIDE:

1. Download python 3.6.x from https://www.python.org/downloads/release/python-360/ - automatic!
1. From Windows Home go to Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables and add two new variables in 'PATH' -> [Home directory of Python]; [Home directory of Python]\Scripts
1. Check python version using the following command: python --version
1. Install django using: pip install Django==1.10.3


## INSTRUCTIONS TO RUN THE PROGRAM:

1. Open Windows PowerShell
1. Navigate to the directory having the folder, i.e. navigate inside TravelMate which has manage.py file
1. Now Perform the following steps: 
	 1. Type in command in the command line: python manage.py runserver
	 1. Open a browser and type in or copy paste the following URL: http://127.0.0.1:8000/ - automatic!