FROM python:alpine
WORKDIR /app
RUN pip install Flask

#Pythonファイルの実行
CMD ["python", "main.py"]