# PARIS-PASSEPORT-RDV
Python script that autamatically finds an appointement for you in the city hall (Paris, France). This script uses GOOGLE CHROME 102.0.5005.63 (64 bits) on Win 10 and PYTHON 3.10.4 + dependancies.

- INSTALLATION
- 1 - Change values there :
    data = {
        "nombre"        : "4",    #number of persons
        "time_in_secs"  : 9       #time interval between requests
    }
- 2 - Install dependancues :
	pip install playsound==1.2.2
	pip install selenium
- or run  
	pip install -r requirements.txt


- 3 - if it doesnt works, verify and replace the chromedriver path bay your's :
	default path = '.\chromedriver.exe'
