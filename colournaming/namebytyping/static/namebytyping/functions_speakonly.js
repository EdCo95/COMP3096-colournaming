window.onload = function(){
  $('#speech-button').trigger('click');

  $("#help-button").click(function() {
    $("#textbox").val("SPEECH-BROKEN");
    document.getElementById('input-form').submit();
  });

  $("#skip-button").click(function() {
    $("#textbox").val("Circle Invisible");
    document.getElementById('input-form').submit();
  });
}
