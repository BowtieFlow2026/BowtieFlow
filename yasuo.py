import os
import subprocess

# 目标文件夹
root_dir = "/Users/caiminghong/Desktop/Canvas/assets_new"

# 支持的视频扩展名
video_exts = (".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv")

def compress_video(input_path):
    # 临时输出文件
    temp_path = input_path + ".compressed.mp4"
    
    # 使用 H.265 压缩 (比 H.264 更高效)，CRF 设置为 28（通常能压缩到原大小的 1/3 左右）
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vcodec", "libx265", "-crf", "28",  # 控制压缩率（28≈原大小1/3）
        "-acodec", "aac", "-b:a", "128k",    # 音频压缩
        "-y", temp_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        # 替换原文件
        os.replace(temp_path, input_path)
        print(f"✅ 压缩完成: {input_path}")
    except Exception as e:
        print(f"❌ 压缩失败: {input_path}, 错误: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)

def walk_and_compress(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.lower().endswith(video_exts):
                full_path = os.path.join(dirpath, filename)
                compress_video(full_path)

if __name__ == "__main__":
    walk_and_compress(root_dir)