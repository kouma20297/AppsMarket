<template>
    <div>
      <!-- Header コンポーネントを使用 -->
      <Header />
  
      <!-- Introduction Section -->
      <section class="intro">
        <p class="intro-text">
          「<strong>mediba’s CREDO</strong>」はmedibaで働くすべての人が共有すべき価値観です。<br>
          CREDOが私たちの向かうベクトルを示し、社員一人ひとりの成長を促します。
        </p>
        <a href="#" class="btn">mediba's CREDOを見る</a>
      </section>
  
      <!-- Business Section -->
      <section class="business">
        <h2 class="section-title">Our Business</h2>
        <h3 class="business-title">事業紹介</h3>
        <p class="business-text">
          5つのケイパビリティを活用し、事業のあらゆるフェーズをサポートいたします。<br>
          多くのユーザーを抱える大規模サービスのトータル支援から、専門家集団による課題解決まで、medibaが携わる事業をご紹介します。
        </p>
        <a href="#" class="btn">medibaのケイパビリティを見る</a>
      </section>
    </div>
  </template>
  
  <script>
  import Header from "@/components/Header.vue";
  
  export default {
    name: "Home",
    components: {
      Header,
    },
  };
  </script>
  
  <style scoped>
  .intro {
    padding: 20px;
    text-align: center;
  }
  
  .intro-text {
    font-size: 18px;
    line-height: 1.6;
  }
  
  .btn {
    display: inline-block;
    margin-top: 10px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
  }
  
  .business {
    padding: 20px;
    text-align: center;
  }
  
  .section-title {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .business-title {
    font-size: 20px;
    margin-bottom: 5px;
  }
  
  .business-text {
    font-size: 16px;
    line-height: 1.6;
  }
  </style>
  