# 建立 python 3.12.0环境
FROM python:3.12.0

RUN apt-get clean
RUN apt-get -y update --fix-missing

# 安装netcat
RUN apt-get install netcat-traditional -y
RUN apt-get install gcc -y

# 镜像作者
MAINTAINER mrhuanghs

# 设置 python 环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 可选：设置镜像源为国内
COPY pip.conf /root/.pip/pip.conf

# 容器内创建 myblog 文件夹
ENV APP_HOME /var/www/html/server
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# copy 项目代码
ADD . $APP_HOME/

# 更新pip版本
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install uwsgi
# 安装项目依赖
RUN pip install -r requirements.txt

# 移除\r in windows
RUN sed -i 's/\r//' ./start.sh

# 给start.sh可执行权限
RUN chmod +x ./start.sh

# 数据迁移，并使用uwsgi启动服务
ENTRYPOINT /bin/bash ./start.sh
