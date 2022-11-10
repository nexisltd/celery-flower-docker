FROM python:3.11-bullseye
EXPOSE 5555
RUN apt update && apt install iputils-ping sudo -y
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN rm requirements.txt
ENTRYPOINT ["sh", "entrypoint.sh"]
