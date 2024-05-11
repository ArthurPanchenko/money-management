FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY req.txt .
RUN pip3 install -r req.txt
COPY . .
EXPOSE 8000
CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
    && python manage.py runserver 0.0.0.0:8000

