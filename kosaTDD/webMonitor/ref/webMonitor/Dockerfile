FROM python:3.11.4
LABEL maintainer="kimcj020828@gmail.com"

ENV TZ=Asia/Seoul

RUN mkdir -p /app/webMonitor

WORKDIR /app/webMonitor
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pytest -s ./tests

RUN rm -rf _envMonitor
RUN rm -rf .pytest_cache
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD pytest -s ./tests && python main.py