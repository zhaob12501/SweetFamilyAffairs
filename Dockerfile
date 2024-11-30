# 使用官方 Python 3.12 镜像作为基础镜像
FROM python:3.12-slim

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt /app/

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . /app/

# 运行数据库迁移（可选）
RUN python manage.py makemigrations
RUN python manage.py migrate

# 收集静态文件（可选）
# RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 80

# 启动 Django 应用
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]