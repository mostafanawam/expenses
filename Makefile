python = python3
pip = pip3


backend-server-start:
	$(python) -u manage.py runserver localhost:8050


install:
	$(pip) install -r requirements.txt 



setup:
	$(python) manage.py makemigrations && $(python) manage.py migrate
