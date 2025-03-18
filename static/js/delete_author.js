document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const authorId = this.getAttribute('data-author-id');
            const authorName = this.getAttribute('data-author-name');
            const authorPhotoUrl = this.getAttribute('data-author-photo-url');

            document.getElementById('deleteAuthorId').value = authorId;
            document.getElementById('deleteAuthorName').textContent = authorName;
            document.getElementById('deleteAuthorPhoto').src = authorPhotoUrl;

            const deleteModal = new bootstrap.Modal(document.getElementById('deleteAuthorModal'));
            deleteModal.show();
        });
    });
});