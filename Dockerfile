FROM python:3.11-alpine3.16
EXPOSE 5555
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN rm requirements.txt
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
ENTRYPOINT ["sh", "entrypoint.sh"]
