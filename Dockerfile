FROM python:3.10-bookworm


COPY bashrc /root/.bashrc
RUN apt-get update
RUN apt-get -y install wget
WORKDIR /workshop
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY chunk-book.py .
COPY create-index-and-pipeline.py .

CMD ["bash"]