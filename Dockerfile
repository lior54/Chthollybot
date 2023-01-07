FROM python:3.10.5
WORKDIR /bot
COPY requirements.txt /bot/
RUN source ./.vnev/bin/activate
RUN pip install -r requirements.txt
COPY . /bot/
CMD python main.py