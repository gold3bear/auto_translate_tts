import azure.cognitiveservices.speech as speechsdk
from utils import getConfig

CONFIG = getConfig()

speech_key = CONFIG['SPEECH_KEY']
speech_region = CONFIG['SPEECH_REGION']

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
speech_config.speech_synthesis_language = "zh-CN"
speech_config.speech_synthesis_voice_name = "zh-CN-XiaoxiaoNeural"
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz48KBitRateMonoMp3)
file_name = "output.wav"

audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = "面朝大海，春暖花开。从明天起，和每一个亲人通信告诉他们我的幸福。"
result = speech_synthesizer.speak_text_async(text).get()
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Text to speech succeeded.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Text to speech canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))