git:
	git add \.
	git commit -m "$m"
	git push -u origin master

run: manage.py
	python manage.py runserver

migrate:
	python manage.py $m