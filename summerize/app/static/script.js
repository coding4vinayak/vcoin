// static/script.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const button = document.querySelector('button');

    form.addEventListener('submit', function () {
        button.innerText = 'Summarizing...';
        button.disabled = true;
    });
});
