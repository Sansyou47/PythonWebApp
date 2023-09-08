FROM python:alpine
WORKDIR /app
RUN pip install Flask && \
    pip install Flask-SQLAlchemy

#Pythonファイルの実行
CMD ["python", "main.py"]