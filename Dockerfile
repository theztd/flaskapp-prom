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

# Set ENV
ENV PORT=5000
    THREAD_COUNT=4

# Expose port
EXPOSE ${PORT}


# Entrypoint
ENTRYPOINT ["/opt/flaskapp/entrypoint.sh"]

