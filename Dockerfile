FROM jordanirabor/python3.7-pip-pipenv
MAINTAINER Annie

COPY ptt_crawler.py ./

Run pip install --upgrade pip
Run pip install pandas
Run pip install requests
Run pip install beautifulsoup4
RUN python ptt_crawler.py