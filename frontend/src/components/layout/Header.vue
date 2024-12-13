<template>
    <header class="header">
      <div class="header-container">
        <img src="logo.png" alt="ロゴ" class="logo">
        <div class="header-title">
          <h1>学生と企業をつなぐ</h1>
        </div>
        <div class="header-icons">
          <button class="login-btn">ログイン</button>
          <button class="register-btn">会員登録</button>
        </div>
      </div>
      <nav class="navbar">
        <ul>
          <router-link to="/">ホーム</router-link> <!-- 追加されたリンク -->
          <li><a href="#">記事</a></li>
          <li><a href="#">クリエイター</a></li>
          <li><a href="#">作品</a></li>
          <router-link to="/aboutus">サイトについて</router-link> <!-- 追加されたリンク -->
          <li><a href="#">採用情報</a></li>
          <li><a href="#">求人</a></li>
        </ul>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: "Header",
  };
  </script>
  
  <style scoped>
  .header {
    background-color: #f8f9fa;
    padding: 10px 20px;
  }
  
  .header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .logo {
    height: 50px;
  }
  
  .header-title {
    text-align: center;
  }
  
  .header-title h1 {
    font-size: 24px;
    margin: 0;
  }
  
  .header-icons button {
    margin-left: 10px;
    padding: 5px 10px;
  }
  
  .navbar {
    margin-top: 10px;
  }
  
  .navbar ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
  }
  
  .navbar li {
    margin: 0 10px;
  }
  
  .navbar a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
  }
  </style>
  