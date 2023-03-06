FROM python:slim
ENV TOKEN='your token'
COPY . . 
RUN pip install -r requirement.txt
CMD python bot.py
