# FROM python:3.9-alpine
FROM seleniarm/standalone-firefox:latest

RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip

COPY ./requirements.txt /app/
RUN xargs sudo apt-get -y install < /app/requirements.txt
# RUN pip install -r /app/requirements.txt
COPY . /app/
RUN crontab /app/scrape_cron

# Create empty log (TAIL needs this)
RUN touch /tmp/out.log

# Start TAIL - as your always-on process (otherwise - container exits right after start)
CMD crond && tail -f /tmp/out.log
