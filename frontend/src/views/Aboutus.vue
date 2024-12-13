<template>
    <div class="about-us">
      <h1>このサイトの説明</h1>
      <p>
        これは仮の "About Us" ページです。ここに会社の情報や
        その他の説明を追加できます。
      </p>
      <p>
        このページは Vue.js のルーター設定に従って表示されます。
      </p>
      <button @click="goHome">Go to Home Page</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Aboutus',
    methods: {
      goHome() {
        this.$router.push({ name: 'Home' });  // ホームページにリダイレクト
      }
    }
  };
  </script>
  
  <style scoped>
  .about-us {
    padding: 20px;
    text-align: center;
  }
  
  h1 {
    color: #333;
  }
  
  button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>
  