function validateForm() {
            var fileInput = document.getElementById('picture1');
            var errorMessage = document.getElementById('error-message');
            if (fileInput.files.length === 0) {
                errorMessage.textContent = 'No pictures uploaded';
                return false;
            }

            var fileInput2 = document.getElementById('picture2');
            if (fileInput2.files.length === 0) {
                errorMessage.textContent = 'No pictures uploaded';
                return false;
                }
            errorMessage.textContent = '';
            return true;
        }