$(window).load(function() {
  $('#speech-button').trigger('click');

  $("#help-button").click(function() {
    $("#textbox").val("Circle Invisible");
    document.getElementById('input-form').submit();
  });

  $("#submitbutton").click(function() {
    var submitted = $("#submitted").val();
    if (submitted !== "True") {
      $("#submitted").val("True");
      document.getElementById('input-form').submit();
    }
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

  var submitted = $("#submitted").val();

  if (keycode == 13 && submitted !== "True") {
    $("#submitted").val("True");
    myfield.form.submit();
    return false;
  } else {
    return true;
  }
}
