FROM python:3.8.2
ENV FLASK_APP "/app.py"
RUN pip install Flask
ADD app.py app.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]