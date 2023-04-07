from pytube import YouTube
import ffmpeg


temp_folder = "./output"
download_folder = "./download"

def Download(link):
  youtubeObject = YouTube(link)
  print(youtubeObject,youtubeObject.video_id)
  title = youtubeObject.video_id
  # print(youtubeObject.streams)
  # try:
  #   title = str(youtubeObject.video_id)
  # finally:
  #   title = ''.join(random.sample(string.ascii_letters + string.digits, 16))
  # 筛选出1080p的视频文件
  video = youtubeObject.streams.filter(res="720p").first()
  # 筛选出最高质量的音频文件
  audio = youtubeObject.streams.get_audio_only()
  try:
    # 指定保存路径为当前文件夹下的Download子文件夹
    video_file = f"{temp_folder}/_video.mp4"
    audio_file= f"{temp_folder}/_audio.mp3"
    output_file = f"{download_folder}/{title}.mp4"
    video.download(filename=video_file)
    audio.download(filename=audio_file)
    print("Output file is created successfully")
    # 使用FFmpeg合并视频和音频文件
    video_stream = ffmpeg.input(video_file)
    audio_stream = ffmpeg.input(audio_file)
    output = ffmpeg.output(video_stream, audio_stream, output_file)

    # 执行合并操作
    output.run()
    print("Download is completed successfully")
  except Exception as e:
    print("An error has occurred",e)

link = input("Enter the YouTube video URL: ")
Download(link)