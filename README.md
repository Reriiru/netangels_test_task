## To run:
1. Create db and user, put in password. (Uses maria/mysql, settings is test/_task//test/_task/settings.py)
2. pip install -r requirements.txt
3. python ./test_task/manage.py makemigration test\_task\_app
4. python ./test_task/manage.py migrate
5. python ./test_task/manage.py populate\_db
6. python ./test_task/manage.py runserver

Look at it go!