# 导入os模块，用于执行系统命令
import os

# 定义输入和输出文件的名称
wav_file = "./output/output.wav"
mp4_file = "./input/old.mp4"
output_file = "./output/new.mp4"

# 构造ffmpeg命令，使用-c:v copy和-map选项
ffmpeg_command = f"ffmpeg -i {mp4_file} -i {wav_file} -c:v copy -map 0:v:0 -map 1:a:0 {output_file}"

# 执行ffmpeg命令，并获取返回值
return_code = os.system(ffmpeg_command)

# 判断返回值是否为0，如果是0，表示执行成功，否则表示执行失败
if return_code == 0:
    print("替换音频成功！")
else:
    print("替换音频失败！")