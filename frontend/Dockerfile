# ベースイメージ
FROM node:16

# 作業ディレクトリを設定
WORKDIR /app

# パッケージマネージャー用のファイルをコピー
COPY ./frontend/package*.json ./


# 必要な依存関係をインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# 開発サーバーを起動
CMD ["npm", "run", "serve"]
