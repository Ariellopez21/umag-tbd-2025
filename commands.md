# Comandos
Para usar en terminal y que no se me olviden :c

## Instalar
Para instalar **uv**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Para instalar **Postgresql**

### Paso 1
```
sudo apt install postgresql -y
sudo systemctl status postgresql
sudo su - postgres 
createuser -s admin
createdb -O admin admin
psql
\password admin
```

### Paso 2
```
createuser -s -h localhost -U admin [username]

createdb -O [username] [username]
```

## UV
```
uv tool install harlequin
uv tool install pgcli
uv tool install 'harlequin[postgres]'

uv add colorama
```

## Para problemas u otras cosas
```
harlequin -a postgres "postgresql:///library"
psql library < library_db.sql

source ~/.bashrc
sudo nvim /etc/postgresql/16/main/pg_hba.conf # local | all | postgres | peer
sudo systemctl restart postgresql

pgcli -h localhost -U ariel
```