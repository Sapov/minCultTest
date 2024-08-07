FROM python:3.10.4

LABEL authors="sasha"

ENTRYPOINT ["top", "-b"]


SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc gettext cron openssh-client locales vim

RUN useradd -rms /bin/bash django && chmod 777 /opt /run

WORKDIR /django
RUN chown -R django:django /django && chmod 755 /django

COPY --chown=django:django . .

RUN pip install -r requirements.txt

USER django
CMD ["gunicorn","-b","0.0.0.0:8000","mysite.wsgi:application"]