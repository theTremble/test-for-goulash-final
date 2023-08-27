#РЕШЕНИЕ
#Генерация inventory из папки ansible/generate (предварительно заменить IP серверов в файле config.toml на нужные)
python3 inv_generator.py

#Подготовка серверов из папки ansible
ansible-playbook playbook_prep.yml

#Создание БД из папки ansible
ansible-playbook --extra-vars "db_name=dev db_user=dev db_pass=testpartner_db" mysql.yml

#Подключение к БД с сервера MySQL
mysql --host=localhost --user=dev --password=testpartner_db dev

#Комментарии к решению
1) Скорее всего, парсинг файла config.toml можно организовать более универсально, но всё зависит от того, насколько разнится наполнение таких файлов в реальной работе. Если файлы-источники обычно однотипны, то проблем не будет. Если нет - логику парсинга придется каждый раз корректировать;
2) В задании не шло речи про настройку кластера между серверами MySQL, поэтому в решении этот этап отсутствует. Кластер можно организовать с помощью (MySQL Cluster - https://dev.mysql.com/downloads/cluster/);
3) Если будут дополнительные задания, либо замечания - готов взять на доработку.
