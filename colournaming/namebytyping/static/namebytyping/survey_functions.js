window.onload = function(){
  $("#begin-button").click(function() {
    var n_checked = $("input:checked").length;
    if (n_checked > 1) {
      var age = $("#age-input").val();
      var nationality = $("#nationality-input").val();
      if (age == "") {
        $("#age-input").val("-");
      }
      if (nationality == "") {
        $("#nationality-input").val("-");
      }
      this.parentNode.submit();
    } else {
      alert("Please select a gender and your preference for using speech recognition");
    }
  });

  if (! ('webkitSpeechRecognition' in window) ) {
    $('#speech-recog-test').val("False");
  } else {
    $('#speech-recog-test').val("True");
  }

}
