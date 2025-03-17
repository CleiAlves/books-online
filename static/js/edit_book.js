document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.btn-edit-book');
    const editCoverInput = document.getElementById('editCover');
    const bookCover = document.getElementById('bookCover');
    const deleteCoverButton = document.getElementById('deleteCoverButton');
    const cameraIcon = document.querySelector('.fa-camera');
    const coverClearCheckbox = document.getElementById('cover_image-clear');

    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const bookId = this.dataset.bookId;
            const bookTitle = this.dataset.bookTitle;
            const bookAuthor = this.dataset.bookAuthor;
            const bookYear = this.dataset.bookYear;
            const bookGenre = this.dataset.bookGenre;
            const bookSynopsis = this.dataset.bookSynopsis;
            const bookCoverUrl = this.dataset.bookCoverUrl;

            document.getElementById('editTitle').value = bookTitle;
            document.getElementById('editAuthor').value = bookAuthor;
            document.getElementById('editYear').value = bookYear;
            document.getElementById('editGenre').value = bookGenre;
            document.getElementById('editSynopsis').value = bookSynopsis;
            bookCover.src = bookCoverUrl;

            const form = document.getElementById('editBookForm');
            form.action = `/book_edit/${bookId}/`;

            const editBookModal = new bootstrap.Modal(document.getElementById('editBookModal'));
            editBookModal.show();
        });
    });

    bookCover.addEventListener('click', function() {
        editCoverInput.click();
    });

    cameraIcon.addEventListener('click', function() {
        editCoverInput.click();
    });

    editCoverInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                bookCover.src = e.target.result;
            }
            reader.readAsDataURL(file);
        }
    });

    deleteCoverButton.addEventListener('click', function() {
        bookCover.src = 'https://dummyimage.com/150x200/9e9e9e/030303.png&text=+SEM+CAPA';
        editCoverInput.value = '';
        coverClearCheckbox.checked = true;
    });
});