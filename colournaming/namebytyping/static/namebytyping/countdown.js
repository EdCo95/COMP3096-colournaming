



// Credit to http://stackoverflow.com/questions/2400227/jquery-timer-implementation
// for this countdown code

var elapsed = parseInt($('#time-start').val(), 10);
var interval;
var total = 60 * 3;

function showElapsedTime()
{
  if (elapsed < total) {
    elapsed += 1;
    time = total - elapsed;
    var minutes = Math.floor(time/60);
    var seconds = time - minutes * 60;
    var final_time = str_pad_left(minutes,'0',2)+':'+str_pad_left(seconds,'0',2);
    $('#timer').html(final_time);
    $('#time-tracker-box').val(elapsed);
  } else {
    clearInterval(interval);
    $('#time-tracker-box').val(-1);
    this.parentNode.submit();
  }
}

$(function() {
  interval = setInterval(showElapsedTime, 1000);
});

function str_pad_left(string,pad,length) {
    return (new Array(length+1).join(pad)+string).slice(-length);
}
