FROM python:3.9.5-slim-buster
RUN useradd -ms /bin/bash gunicorn
WORKDIR /webapp
RUN chown -R gunicorn: .
USER gunicorn
ENV PATH = "${PATH}:/home/gunicorn/.local/bin/"
RUN pip3 install pipenv
RUN mkdir .venv
COPY Pipfile* /webapp/
RUN pipenv install
COPY . /webapp/
USER gunicorn
CMD pipenv run gunicorn -b 0.0.0.0:5000 -w 2 --threads 2 --access-logfile - wsgi:app
