window.onload = function() {

  if (! ('webkitSpeechRecognition' in window) ) {
    $('#speech-recog-test').val("False");
    document.getElementById('input-form').submit();
  } else {
    $('#speech-recog-test').val("True");
  }

}
