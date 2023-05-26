FROM python:3.7-slim

WORKDIR /backend/backend

COPY requirements.txt backend/backend/


RUN python -m pip install --upgrade pip
RUN pip3 install -r backend/backend/requirements.txt --no-cache-dir

COPY . /backend/backend

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]
