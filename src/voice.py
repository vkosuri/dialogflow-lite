
from .agent import ApiAi
import speech_recognition
import subprocess


class Voice(ApiAi):
    def speech_recognizer(self):
        # Start jack control
        self.attempt_jack_control_start()

        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        recognizer_function = getattr(recognizer, self.recognizer_function)

        try:
            result = recognizer_function(audio)
            return result
        except speech_recognition.UnknownValueError:
            return 'I am sorry, I could not understand that.'
        except speech_recognition.RequestError as e:
            m = 'My speech recognition service has failed. {0}'
            return m.format(e)

    def attempt_jack_control_start(self):
        """
        Jack is a program that can be used to get audio
        input from your system. This command will try
        to start it when your program runs.
        """
        import warnings

        try:
            subprocess.call(['jack_control', 'start'])
        except Exception:
            # Note: jack_control is not a valid command in Windows
            warnings.warn(
                'Unable to start jack control.',
                RuntimeWarning
            )
