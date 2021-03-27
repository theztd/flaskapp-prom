FROM python:3-slim

LABEL version=""
LABEL authors="Marek Sirovy"
LABEL contact="msirovy@gmail.com"

# Copy application source to image
copy ./src/ /opt/flaskapp

# Set application's home as workdir
WORKDIR /opt/flaskapp

# Install deps
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 5000

# Entrypoint
ENTRYPOINT ["waitress-serve"]
CMD ["main:app", "--port 5000"]

