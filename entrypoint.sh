#!/bin/sh

# DBの準備ができるまで待機
echo "Waiting for postgres..."
while ! nc -z postgres_db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# マイグレーションの実行
python manage.py migrate

# サーバーを起動
exec "$@"
