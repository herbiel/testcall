FROM python:3.9
COPY . /app
WORKDIR /app
RUN wget http://ftp.br.debian.org/debian/pool/main/s/swig/swig3.0_3.0.12-2_amd64.deb \
    && dpkg -i swig3.0_3.0.12-2_amd64.deb \
    && ln -s /usr/bin/swig3.0 /usr/bin/swig \
    && pip install -r requirements.txt
EXPOSE 8000
CMD ["/usr/local/bin/python", "app.py"]

