/*global webkitSpeechRecognition */

(function() {
	'use strict';

	if (! ('webkitSpeechRecognition' in window) ) return;

	var talkMsg = 'Speak or Type to Answer...';
	var patience = 60;

	var two_line = /\n\n/g;
	var one_line = /\n/g;
	function linebreak(s) {
  	return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
	}

	function capitalize(str) {
		return str.length ? str[0].toUpperCase() + str.slice(1) : str;
	}

	var speechInputWrappers = document.getElementsByClassName('si-wrapper');

	[].forEach.call(speechInputWrappers, function(speechInputWrapper) {
		// find elements
		var inputEl = speechInputWrapper.querySelector('.si-input');
		var micBtn = speechInputWrapper.querySelector('.si-btn');

		// size and position them
		var inputHeight = inputEl.offsetHeight;
		var inputRightBorder = parseInt(getComputedStyle(inputEl).borderRightWidth, 10);
		var buttonSize = 0.8 * inputHeight;
		micBtn.style.top = 0.1 * inputHeight + 'px';
		micBtn.style.height = micBtn.style.width = buttonSize + 'px';
		inputEl.style.paddingRight = buttonSize - inputRightBorder + 'px';
		speechInputWrapper.appendChild(micBtn);

		// setup recognition
		var finalTranscript = '';
		var recognizing = false;
		var timeout;
		var oldPlaceholder = null;
		var recognition = new webkitSpeechRecognition();
		recognition.continuous = true;
		recognition.interimResults = true;

		function restartTimer() {
			timeout = setTimeout(function() {
				recognition.stop();
			}, patience * 1000);
		}

		recognition.onstart = function() {
			oldPlaceholder = inputEl.placeholder;
			inputEl.placeholder = talkMsg;
			recognizing = true;
			micBtn.classList.add('listening');
			restartTimer();
			$("#listening-mic").css("display", "inline-block");
			$("#stopped-mic").css("display", "none");
			$("#restart-recognition").css('display', 'none');
			var text_input = document.getElementById ('textbox');
		  text_input.focus ();
		  text_input.select ();
			$(".mic-container").click(function() {
				event.preventDefault();
				if (recognizing) {
					recognition.stop();
					var text_input = document.getElementById ('textbox');
				  text_input.focus ();
				  text_input.select ();
					return;
				}
			});
		};

		recognition.onend = function() {
			recognizing = false;
			clearTimeout(timeout);
			micBtn.classList.remove('listening');
			if (oldPlaceholder !== null) {
				inputEl.placeholder = oldPlaceholder;
				$("#restart-recognition").css('display', 'flex');
				$("#listening-mic").css("display", "none");
				$("#stopped-mic").css("display", "inline-block");
				$("#restart-recognition").click(function() {
					$("#listen-text").html("Listening...");
					$("#restart-recognition").css('display', 'none');
					recognition.start();
				});
			}

			$(".mic-container").click(function() {
				event.preventDefault();
				if (!recognizing) {
					recognition.start();
					return;
				}
			});
		};

		recognition.onresult = function(event) {
			clearTimeout(timeout);

			var interim_transcript = '';

			for (var i = event.resultIndex; i < event.results.length; ++i) {
				if (event.results[i].isFinal) {
					finalTranscript += event.results[i][0].transcript;
				} else {
        	interim_transcript += event.results[i][0].transcript;
      	}
			}
			interim_transcript = linebreak(interim_transcript);
			inputEl.placeholder = interim_transcript;
			finalTranscript = capitalize(finalTranscript);
			inputEl.value = finalTranscript;
			restartTimer();

			if (finalTranscript) {
				$("#textbox").css("background-color", "#b2d8b2");
				setTimeout(function() {
					document.getElementById('input-form').submit();
				}, 500);
			}
		};

		micBtn.addEventListener('click', function(event) {
			event.preventDefault();
			if (recognizing) {
				recognition.stop();
				return;
			}
			inputEl.value = finalTranscript = '';
			recognition.start();
		}, false);

	});
})();
