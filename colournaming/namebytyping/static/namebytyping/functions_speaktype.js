$(window).load(function() {
  $('#speech-button').trigger('click');

  $("#help-button").click(function() {
    $("#textbox").val("Circle Invisible");
    document.getElementById('input-form').submit();
  });

  var text_input = document.getElementById ('textbox');
  text_input.focus ();
  text_input.select ();

});

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