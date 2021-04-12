FROM  ubuntu:20.10
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip curl

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV MYSQL_ROOT_PASSWORD Cizoo123*

COPY . /usr/src/app
COPY requirements.txt /usr/src/app

RUN pip3 install -r requirements.txt
RUN apt-get install -y mysql-client
RUN apt-get install -y mysql-server
RUN apt-get install -y nginx

RUN apt-get update

RUN  usermod -d /var/lib/mysql/ mysql
RUN service mysql restart

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 3308 8181
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

