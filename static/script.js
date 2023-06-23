function validateForm() {
            var fileInput = document.getElementById('picture1');
            var errorMessage = document.getElementById('error-message');
            if (fileInput.files.length === 0) {
                errorMessage.textContent = 'One or both of the images is missing.';
                return false;
            }

            var fileInput2 = document.getElementById('picture2');
            if (fileInput2.files.length === 0) {
                errorMessage.textContent = 'One or both of the images is missing.';
                return false;
                }
            errorMessage.textContent = '';
            return true;
        }