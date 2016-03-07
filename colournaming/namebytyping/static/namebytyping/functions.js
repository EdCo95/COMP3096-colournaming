$(window).load(function() {

  $("#help-button").click(function() {
    $("#textbox").val("Circle Invisible");
    this.parentNode.submit();
  });

  var text_input = document.getElementById ('textbox');
  text_input.focus ();
  text_input.select ();

  $("#unable-to-speak").click(function() {
    $("#happy-to-speak-box").val("UNWILLING")
    this.parentNode.submit();
  });

});

window.onload = function(){
  $('#speech-button').trigger('click');
}

function submitenter(myfield,e)
{
  var keycode;
  if (window.event) {
    keycode = window.event.keyCode;
  } else if (e) {
    keycode = e.which;
  } else {
    return true;
  }

  if (keycode == 13) {
    myfield.form.submit();
    return false;
  } else {
    return true;
  }
}
