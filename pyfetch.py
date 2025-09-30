import psutil
import platform
import socket

tux_art = [
    "        .--.",
    "       |o_o |",
    "       |:_/ |",
    "      //   \\ \\",
    "     (|     | )",
    "    /'\\_   _/`\\",
    "    \\___)=(___/"
]

info_lines = [
    f"Ядро: {platform.system()} {platform.release()}",
    f"Имя хоста: {socket.gethostname()}",
    f"Физических ядер: {psutil.cpu_count(logical=False)}",
    f"Логических ядер: {psutil.cpu_count(logical=True)}",
    f"Оперативная память: {round(psutil.virtual_memory().total / (1024**3), 2)} GB"
]

art_width = max(len(line) for line in tux_art) + 4

for i in range(max(len(tux_art), len(info_lines))):
    art = tux_art[i] if i < len(tux_art) else ""
    info = info_lines[i] if i < len(info_lines) else ""
    print(art.ljust(art_width) + info)
