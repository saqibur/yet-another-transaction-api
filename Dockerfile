FROM python:3.11.5-slim

RUN mkdir /yata

# set work directory
WORKDIR /yata

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements ./requirements
RUN pip install -r requirements/local.txt

# copy project
COPY . .
RUN chmod +x ./entrypoint.sh


# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
