async function loadHeader() {
    const headerContainer = document.getElementById('header'); // 正しく`id`で取得
    try {
        // header.htmlを取得
        // const response = await fetch('./component.html/header.html'); // パスを指定
        const response = await fetch('/frontend/src/component.html/header.html');

        if (!response.ok) throw new Error('Failed to load header.html');
        const headerHtml = await response.text(); // HTML内容をテキストとして取得
        headerContainer.innerHTML = headerHtml; // 取得したHTMLを挿入
    } catch (error) {
        console.error('Error loading header:', error);
    }
}

// ページが読み込まれたらヘッダーを読み込む
document.addEventListener('DOMContentLoaded', loadHeader);
