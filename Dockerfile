# 以python3.7.9为基础镜像
FROM python:3.7.9-alpine3.11

COPY requirements.txt /tmp/requirements.txt

# 执行指令
RUN set -eux; \
        pip install --upgrade pip -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com; \
        pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn; \
        rm -f /tmp/requirements.txt

# 拷贝项目目录到容器的/app目录下
COPY . /app/

# 切换工作目录
WORKDIR /app


EXPOSE 8000

# 会被docker-compose覆盖
CMD ["uwsgi", "--ini", "uwsgi.ini"]
