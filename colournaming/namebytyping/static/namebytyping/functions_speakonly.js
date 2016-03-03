$(window).load(function() {
  var img = document.getElementById('shown-image');
  var width = img.clientWidth;
  var height = img.clientHeight;
  $('#overlay').css('height', height);
  $('#overlay').css('width', width);

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
