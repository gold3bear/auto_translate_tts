# 导入所需的库
import pydub
import librosa
import numpy as np

# 定义一个MP4文件的路径
mp4_file = "./input/test.mp4"

# 使用pydub库，将MP4文件转换为WAV文件
audio = pydub.AudioSegment.from_file(mp4_file)
audio.export("./output/audio.wav", format="wav")

# 使用librosa库，对WAV文件进行短时傅里叶变换（STFT），得到一个复数矩阵
y, sr = librosa.load("./output/audio.wav")
S = librosa.stft(y)

# 使用librosa库，对STFT矩阵进行分解，得到两个矩阵，一个表示前景信号（人声），一个表示背景信号（音乐）
S_foreground, S_background = librosa.decompose.hpss(S)

# 使用librosa库，对前景信号矩阵进行逆STFT，得到一个一维数组，表示去除背景音乐后的音频信号
y_foreground = librosa.istft(S_foreground)

# 使用pydub库，将去除背景音乐后的音频信号保存为一个新的WAV文件
new_audio = pydub.AudioSegment(y_foreground.tobytes(), frame_rate=sr, sample_width=y_foreground.dtype.itemsize, channels=1)
new_audio.export("./output/audio_without_music.wav", format="wav")

# 使用librosa库，对背景信号矩阵进行逆STFT，得到一个一维数组，表示背景音乐的音频信号
y_background = librosa.istft(S_background)

# 对背景音乐的音频信号进行绝对值处理，避免负值造成的噪声或失真
y_background = np.abs(y_background)


# 使用pydub库，将背景音乐的音频信号保存为一个新的WAV文件
new_bgm = pydub.AudioSegment(y_background.tobytes(), frame_rate=sr, sample_width=y_background.dtype.itemsize, channels=1)
new_bgm.export("./output/bgm.wav", format="wav")