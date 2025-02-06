<template>
    <div>
      <h1>テック記事一覧</h1>
  
      <div v-if="loading">記事を取得中...</div>
      <div v-else-if="error">{{ error }}</div>
      <ul v-else>
        <li v-for="(article, index) in articles" :key="index">
          <h2>{{ article.title }}</h2>
          <p>著者: {{ article.user.name }}</p>
          <a :href="article.url" target="_blank">記事を読む</a>
        </li>
      </ul>
  
      <button @click="fetchArticles">記事を再取得</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        articles: [],  // 取得した記事のリスト
        loading: false, // 読み込み中フラグ
        error: null     // エラー情報
      };
    },
    methods: {
      async fetchArticles() {
        this.loading = true;
        this.error = null;
        try {
          const response = await fetch('https://qiita.com/api/v2/items?page=1&per_page=10');
          if (!response.ok) {
            throw new Error("APIの取得に失敗しました");
          }
          this.articles = await response.json();
        } catch (err) {
          this.error = err.message;
        } finally {
          this.loading = false;
        }
      }
    },
    mounted() {
      this.fetchArticles();
    }
  };
  </script>
  
  <style scoped>
  h1 {
    color: #42b983;
    text-align: center;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    background: #f9f9f9;
    margin: 10px 0;
    padding: 15px;
    border-left: 5px solid #42b983;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  }
  h2 {
    font-size: 1.2em;
    margin: 0 0 5px;
  }
  p {
    margin: 0 0 10px;
    font-size: 0.9em;
    color: #555;
  }
  a {
    color: #007bff;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #42b983;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
  }
  button:hover {
    background-color: #369b7e;
  }
  </style>
  