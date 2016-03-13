window.onload = function() {

  $("#able-to-speak").val("");

  if (! ('webkitSpeechRecognition' in window) ) {
    $('#speech-recog-test').val("False");
    document.getElementById('input-form').submit();
  } else {
    $('#speech-recog-test').val("True");
  }

  $("#yes-button").click(function() {
    document.getElementById('input-form').submit();
  });

  $("#no-button").click(function() {
    $("#able-to-speak").val("No");
    document.getElementById('input-form').submit();
  });
}
