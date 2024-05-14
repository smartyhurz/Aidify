document.getElementById('fileInput').addEventListener('change', function(event) {
    var file = event.target.files[0];
    var imageHolder = document.getElementById('imageHolder');
    var placeholderText = document.getElementById('placeholderText');
    var uploadedImage = document.getElementById('uploadedImage');
  
    if (file) {
      var reader = new FileReader();
      reader.onload = function() {
        uploadedImage.src = reader.result;
        placeholderText.style.display = 'none';
      }
      reader.readAsDataURL(file);
    } else {
      uploadedImage.src = '#';
      placeholderText.style.display = 'block';
    }
  });