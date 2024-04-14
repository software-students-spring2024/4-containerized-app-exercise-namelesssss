FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m pip install "pymongo[srv]"
RUN python -m pip install openai==0.28

COPY . .

ENV OPENAI_API_KEY=
ENV MONGODB_URI=mongodb+srv://nameless.wun5lpq.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Nameless

EXPOSE 5050
EXPOSE 8000

CMD ["python", "machine-learning-client/app.py"]