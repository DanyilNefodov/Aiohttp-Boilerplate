testForm.onsubmit = function(e) {
  submitBtn.disabled = true;
  e.preventDefault();

  /*
        There was some mistake with ID of form it was AddUploadForm.
        But form named testForm.
        So I renamed it :)
    */
  console.log("SASAMBA");
  const formData = new FormData(testForm);
  setTimeout(function() {
    var xhr = new XMLHttpRequest();
    xhr.open(testForm.method, testForm.action, true);
    xhr.send(formData);
  }, 1000);
};
