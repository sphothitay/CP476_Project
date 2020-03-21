FROM ubuntu:latest

# Set up some environment variables (prevent encoding issues)
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Run TANGO hack for python 3.6
RUN echo "tango-common tango-common/tango-host string ${TANGOSERVER}:20000" | debconf-set-selections

# Install dependencies
RUN apt-get update
RUN apt-get install -y python3.6 python3-pip mysql-server
RUN pip3 install flask mysql-connector bcrypt

# Copy and start the app
WORKDIR /app
COPY . .
RUN sed -i.bak 's/\r$//' "./setup.sh"
RUN chmod +x "./setup.sh"
ENTRYPOINT ["./setup.sh"]
