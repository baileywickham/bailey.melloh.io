mg="python mysite/manage.py makemigrations && python mysite/manage.py migrate"
echo $mg | sudo docker run -i djangoproject_web cat -
# do not use this script, it is unreliable at best.
