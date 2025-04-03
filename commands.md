# Comandos
Para usar en terminal y que no se me olviden :c

## Instalar
Para instalar **uv**

´´´
curl -LsSf https://astral.sh/uv/install.sh | sh
´´´

Para instalar **Postgresql**

´´´
 sudo apt install postgresql -y
 sudo systemctl status postgresql
 sudo su - postgres 
createuser -s admin
createdb -O admin admin
psql
\password admin
´´´

´´´
createuser -s -h localhost -U admin [username]

createdb -O [username] [username]
´´´

## UV
 1983  uv tool install harlequin
 1995  uv tool install pgcli
 1996  uv tool install 'harlequin[postgres]'
 1997  harlequin -a postgres "postgresql:///library"
 1998  hpsql library < library_db.sql
 2013  uv add colorama
 2014  source ~/.bashrc
 2047  sudo nvim /etc/postgresql/16/main/pg_hba.conf # local | all | postgres | peer
 2048  sudo systemctl restart postgresql

 2055  pgcli -h localhost -U ariel
