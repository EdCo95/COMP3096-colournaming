window.onload = function (){
  if (! ('webkitSpeechRecognition' in window) ) {
    $('#speech-recog-test').val("False");
  } else {
    $('#speech-recog-test').val("True");
  }
}
