python = python3
pip = pip3


backend-server-start:
	$(python) -u manage.py runserver back-localhost:8050


install:
	$(pip) install -r requirements.txt 
