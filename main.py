import re
import os

def extract_text_from_srt(file_path, output_text_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        srt_content = file.read()

    # 正则表达式匹配字幕内容
    subtitle_blocks = re.findall(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})\n(.*?)\n\n', srt_content, re.DOTALL)
    
    subtitles = [block[2].replace('\n', ' ') for block in subtitle_blocks]
    
    with open(output_text_path, 'w', encoding='utf-8') as text_file:
        for subtitle in subtitles:
            text_file.write(subtitle + '\n')
    
    return subtitle_blocks

def create_translated_srt_from_text(original_blocks, translated_text_path, output_srt_path):
    with open(translated_text_path, 'r', encoding='utf-8') as text_file:
        translated_texts = [line.strip() for line in text_file.readlines()]

    with open(output_srt_path, 'w', encoding='utf-8') as srt_file:
        for i, block in enumerate(original_blocks):
            index = block[0]
            timecode = block[1]
            original_text = block[2]
            translated_text = translated_texts[i] if i < len(translated_texts) else original_text
            srt_file.write(f"{index}\n{timecode}\n{translated_text}\n\n")

# 获取当前脚本所在的目录
current_directory = os.path.dirname(os.path.abspath(__file__))

# SRT 文件路径
srt_file_path = os.path.join(current_directory, '1.srt')

# 提取字幕文本的输出文件路径
output_text_file_path = os.path.join(current_directory, 'extracted_text.txt')

# 翻译后的文本文件路径（假设你翻译后将文本保存到这个文件）
translated_text_file_path = os.path.join(current_directory, 'translated_text.txt')

# 翻译后的 SRT 文件路径
output_srt_file_path = os.path.join(current_directory, 'translated_1.srt')

# 提取字幕文字并保存到文本文件
subtitle_blocks = extract_text_from_srt(srt_file_path, output_text_file_path)
print(f"字幕已提取并保存到 {output_text_file_path}")

# 创建翻译后的 SRT 文件
create_translated_srt_from_text(subtitle_blocks, translated_text_file_path, output_srt_file_path)
print(f"翻译后的 SRT 文件已生成并保存到 {output_srt_file_path}")
