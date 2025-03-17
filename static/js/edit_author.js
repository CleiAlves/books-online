document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.btn-edit');
    const editPhotoInput = document.getElementById('editPhoto');
    const authorPhoto = document.getElementById('authorPhoto');
    const deletePhotoButton = document.getElementById('deletePhotoButton');

    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const authorId = this.dataset.authorId;
            const authorFirstName = this.dataset.authorFirstName;
            const authorLastName = this.dataset.authorLastName;
            const authorPhotoUrl = this.dataset.authorPhotoUrl;

            document.getElementById('editFirstName').value = authorFirstName;
            document.getElementById('editLastName').value = authorLastName;
            authorPhoto.src = authorPhotoUrl;

            const form = document.getElementById('editAuthorForm');
            form.action = `/authors/edit/${authorId}/`;

            const editAuthorModal = new bootstrap.Modal(document.getElementById('editAuthorModal'));
            editAuthorModal.show();
        });
    });

    // Input de foto acionado pelo clique no label
    editPhotoInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                authorPhoto.src = e.target.result;
            }
            reader.readAsDataURL(file);
        }
    });

    // Botão de deletar foto
    deletePhotoButton.addEventListener('click', function() {
        authorPhoto.src = 'https://dummyimage.com/150x150/9e9e9e/030303.png&text=+SEM+FOTO';
        editPhotoInput.value = '';
    });
});