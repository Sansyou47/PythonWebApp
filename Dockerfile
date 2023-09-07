FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y apache2 python3 python3-pip mysql-client

# FlaskおよびMySQLパッケージのインストール
RUN pip3 install Flask Flask-MySQL

COPY apache2.conf /etc/apache2/apache2.conf
COPY . /var/www/html/

EXPOSE 80

# Apache2とFlaskアプリの起動
CMD ["apache2ctl", "-D", "FOREGROUND"]
