# ベースイメージ
FROM python:3.10-slim-buster

# 出力をバッファリングしないように設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを設定
WORKDIR /app

# システムパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# pipを最新バージョンにアップグレード
RUN pip install --upgrade pip

# 必要なパッケージをインストール
COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# ポートを公開
EXPOSE 8000

# サーバーを起動するコマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
