# General commands
exec:
	docker-compose exec app bash

perms:
	sudo chown -hR imply:imply .

killpos:
	sudo /etc/init.d/postgresql stop

# Django Commands
gettext:
	apt-get update
	apt-get install gettext

pretrans:
	django-admin makemessages -l "en"

trans:
	django-admin compilemessages

migrate:
	django-admin makemigrations
	django-admin migrate