FROM python:3-slim

LABEL version=""
LABEL authors="Marek Sirovy"
LABEL contact="msirovy@gmail.com"

# Copy application source to image
copy ./apigw/ /opt/apigw

# Set application's home as workdir
WORKDIR /opt/apigw

# Install deps
RUN pip3 install -r requirements.txt

# Set ENV
ENV PORT=5000
ENV THREAD_COUNT=4

# Expose port
EXPOSE ${PORT}


# Entrypoint
#ENTRYPOINT ["/bin/bash"]
CMD ["/opt/apigw/entrypoint.sh"]

