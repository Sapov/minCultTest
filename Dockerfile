FROM python:3.10.4

LABEL authors="sasha"

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc gettext cron openssh-client locales vim

RUN useradd -rms /bin/bash django && chmod 777 /opt /run

WORKDIR /django
RUN mkdir /django/static
RUN chown -R django:django /django && chmod 755 /django

COPY --chown=django:django . .

RUN pip install -r requirements.txt

USER django
RUN chmod 777 cinemas/management/commands/parser.py
RUN python cinemas/management/commands/parser.py

CMD ["gunicorn","-b","0.0.0.0:8000","mysite.wsgi:application"]
