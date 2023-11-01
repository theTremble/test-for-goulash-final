#Генерация inventory из папки ansible/generate (предварительно заменить IP серверов в файле config.toml на нужные)

python3 inv_generator.py

#Подготовка серверов из папки ansible

ansible-playbook playbook_prep.yml

#Создание БД из папки ansible

ansible-playbook --extra-vars "db_name=dev db_user=dev db_pass=testpartner_db" mysql.yml

#Подключение к БД с сервера MySQL

mysql --host=localhost --user=dev --password=testpartner_db dev
