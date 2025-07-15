document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())  // JSON形式に変換
    .then(data => {
      document.getElementById('hello').textContent = data.hello;  // 文字を表示！
    })
    .catch(error => {
      console.error('error:', error);
    });
});

