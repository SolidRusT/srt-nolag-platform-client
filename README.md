# nolag-client
Client for consuming the files place in s3 by `s3_oxide_ext_discord` and `s3_oxide_ext_linux`.

Requires `python3` and `virtualenv`. Some distributions you can install `python-is-python3` if there is still a legacy python 2 installed, otherwise you can replace the below `python` with `python3` if the command is not working. The same with `pip` for `pip3`.

I also like to use [pyenv](https://github.com/pyenv/pyenv) and `virtualenv`. These are not required, but are just better to use, so that we have more control over the python environment here.

## Download, Configure, Install and Run.

git clone https://github.com/SolidRusT/srt-nolag-platform-client.git

example SQL. Configure this before adding to your DB.

```sql
CREATE DATABASE IF NOT EXISTS oxide;
USE oxide;
CREATE TABLE config_values (
  id INT NOT NULL AUTO_INCREMENT,
  server_name VARCHAR(50) NOT NULL,
  key_name VARCHAR(50) NOT NULL,
  value VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE USER 'oxide_client'@'%' IDENTIFIED BY 'SomePassword123';
GRANT ALL PRIVILEGES ON *.* TO 'oxide_client'@'%';
FLUSH PRIVILEGES;
```

cd srt-nolag-platform-client

Copy the `config.ini.example` to `config.ini`.

Customize the `config.ini`.

Install the client dependencies with `./install.sh`

Run the updater with `./run.sh`
