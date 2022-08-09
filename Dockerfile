FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8080



RUN mkdir /Teamwork
WORKDIR /Teamwork

RUN python -m pip install --upgrade pip
COPY . /Teamwork
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8080"]
