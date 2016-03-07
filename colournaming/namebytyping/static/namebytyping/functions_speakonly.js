$(window).load(function() {

  $("#help-button").click(function() {
    $("#textbox").val("SPEECH-BROKEN");
    this.parentNode.submit();
  });

  $("#skip-button").click(function() {
    $("#textbox").val("Circle Invisible");
    this.parentNode.submit();
  });
  //var text_input = document.getElementById ('textbox');
  //text_input.focus ();
  //text_input.select ();
});

window.onload = function(){
  $('#speech-button').trigger('click');
}
