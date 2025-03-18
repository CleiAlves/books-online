document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const bookId = this.getAttribute('data-book-id');
            const bookName = this.getAttribute('data-book-title');
            const bookPhotoUrl = this.getAttribute('data-book-cover-url');

            document.getElementById('deleteBookId').value = bookId;
            document.getElementById('deleteBookName').textContent = bookName;
            document.getElementById('deleteBookPhoto').src = bookPhotoUrl;

            const deleteModal = new bootstrap.Modal(document.getElementById('deleteBookModal'));
            deleteModal.show();
        });
    });
});