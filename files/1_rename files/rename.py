import os
import re

def main():
    lines = []
    with open("SQL and PostgreSQL The Complete Developer's Guide.txt") as file:
        lines = file.readlines()
        lines = [re.sub(r"[<>:/\|\"?*]", '', line.rstrip()) for line in lines]

    end_count = 280

    for i in range(end_count):
        try:
            os.replace(f"lesson{i+1}.mp4", f"{i+1}_{lines[i]}.mp4")
            os.replace(f"lesson{i+1}.srt", f"{i+1}_{lines[i]}.srt")
        except Exception:
            print(f"lesson{i+1} не существует")
            continue

main()