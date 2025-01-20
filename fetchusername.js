let users = Array.from(document.querySelectorAll('a.user-name-badge'))
    .map(user => user.textContent.trim());

console.log(users);

copy(users.join("\n"));