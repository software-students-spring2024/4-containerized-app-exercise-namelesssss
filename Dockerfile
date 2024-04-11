FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m pip install "pymongo[srv]"

COPY . .

ENV OPENAI_API_KEY=insert_api_key_here
ENV MONGODB_URI=mongodb+srv://<username>:<ljh020527>@nameless.wun5lpq.mongodb.net/?retryWrites=true&w=majority&appName=Nameless

EXPOSE 5000
EXPOSE 8000

CMD ["python", "app.py"]