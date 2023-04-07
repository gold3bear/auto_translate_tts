import ffmpeg
# 指定音频文件的路径
audio_path = "./Download/audio.mp3"
# 尝试获取音频文件的元数据
try:
  # 调用probe方法，返回一个字典
  metadata = ffmpeg.probe(audio_path)
  print("Audio file is valid")
  # 打印音频文件的格式和编码信息
  print(metadata["format"])
  print(metadata["streams"][0])
except ffmpeg.Error as e:
  # 捕获ffmpeg.Error异常，打印异常信息
  print("Audio file is invalid")
  print(e.stderr)