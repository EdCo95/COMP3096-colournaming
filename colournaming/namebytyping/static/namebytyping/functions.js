$(window).load(function() {
  $('#speech-button').trigger('click');

  var text_input = document.getElementById ('textbox');
  text_input.focus ();
  text_input.select ();

  $("#unable-to-speak").click(function() {
    $("#able-to-speak-box").val("UNABLE")
    document.getElementById('input-form').submit();
  });

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
