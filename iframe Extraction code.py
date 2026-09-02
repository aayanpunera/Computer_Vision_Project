import subprocess
import os

video_path = r"C:\Users\Aayan Punera\Downloads\12.mp4"
output_folder = r"F:\Project Computer Vision\iframes5"

os.makedirs(output_folder, exist_ok=True)

output_pattern = os.path.join(output_folder, "iframe_%04d.jpg")

command = [
    "ffmpeg",
    "-i", video_path,
    "-vf", "select=eq(pict_type\\,I)",
    "-fps_mode", "vfr",
    output_pattern
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

print("Return code:", result.returncode)

if result.returncode == 0:
    print("I-frames extracted successfully.")
else:
    print("FFmpeg error:")
    print(result.stderr)
