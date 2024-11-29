#!/bin/bash

PAGE_NAME=$1

if [ -z "$PAGE_NAME" ]; then
  echo "ページ名を指定してください。"
  echo "使用方法: ./create_page.sh [ページ名]"
  exit 1
fi

PAGE_DIR="./src/pages/$PAGE_NAME"
mkdir -p "$PAGE_DIR"

cat <<EOT > "$PAGE_DIR/$PAGE_NAME.html"
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${PAGE_NAME^} Page</title>
  <link href="../../dist/output.css" rel="stylesheet">
</head>
<body>
  <h1>Welcome to the $PAGE_NAME page</h1>
  <script src="./$PAGE_NAME.ts"></script>
</body>
</html>
EOT

cat <<EOT > "$PAGE_DIR/$PAGE_NAME.ts"
console.log("This is the $PAGE_NAME page.");
EOT

cat <<EOT > "$PAGE_DIR/$PAGE_NAME.css"
EOT

echo "$PAGE_NAME ページのディレクトリとファイルが作成されました。"
