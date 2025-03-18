document.addEventListener('DOMContentLoaded', function () {
    const searchTitleInput = document.getElementById('searchTitle');
    const searchAuthorSelect = document.getElementById('searchAuthor');
    const bookCards = document.querySelectorAll('.book-card');

    function filterBooks() {
        const titleQuery = searchTitleInput.value.toLowerCase();
        const authorQuery = searchAuthorSelect.value;

        bookCards.forEach(card => {
            const bookTitle = card.getAttribute('data-title');
            const bookAuthor = card.getAttribute('data-author');

            const matchesTitle = bookTitle.includes(titleQuery);
            const matchesAuthor = !authorQuery || bookAuthor === authorQuery;

            if (matchesTitle && matchesAuthor) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    searchTitleInput.addEventListener('input', filterBooks);
    searchAuthorSelect.addEventListener('change', filterBooks);
});