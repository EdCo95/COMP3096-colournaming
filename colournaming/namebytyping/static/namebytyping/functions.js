$(window).load(function() {
  var img = document.getElementById('shown-image');
  var width = img.clientWidth;
  var height = img.clientHeight;
  $('#overlay').css('height', height);
  $('#overlay').css('width', width);
});

window.onload = function(){
  var text_input = document.getElementById ('textbox');
  text_input.focus ();
  text_input.select ();
}

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
