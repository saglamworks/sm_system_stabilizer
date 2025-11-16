import os
import psutil
import shutil
import time

KILL_LIST_FILE = "kill_list.txt"


# ----------------------------------------------------
#  SYSTEM STATUS CHECK
# ----------------------------------------------------
def check_system_status():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return {
        "cpu": cpu,
        "ram": ram,
        "disk": disk
    }


# ----------------------------------------------------
#  CLEAN TEMP FILES
# ----------------------------------------------------
def clean_temp_files():
    temp_path = os.getenv("TEMP")
    if not temp_path:
        return "TEMP klasörü bulunamadı."

    deleted = 0

    for root, dirs, files in os.walk(temp_path):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
                deleted += 1
            except:
                pass

    return f"{deleted} geçici dosya silindi."


# ----------------------------------------------------
#  KILL PROCESSES FROM kill_list.txt
# ----------------------------------------------------
def kill_processes():
    if not os.path.exists(KILL_LIST_FILE):
        return "[!] kill_list.txt bulunamadı. Lütfen kapanacak uygulamaları buraya yaz."

    # Dosyadaki uygulama listesini oku
    with open(KILL_LIST_FILE, "r", encoding="utf-8") as f:
        targets = [line.strip() for line in f.readlines() if line.strip()]

    if not targets:
        return "[!] kill_list.txt boş. Kapatılacak uygulama yok."

    killed = []
    running = 0

    # Çalışan processleri tarayıp listedekileri kapat
    for proc in psutil.process_iter(['pid', 'name']):
        running += 1
        try:
            if proc.info["name"] in targets:
                proc.terminate()
                killed.append(proc.info["name"])
        except:
            pass

    if not killed:
        return "Listede olan hiçbir uygulama çalışmıyor."

    return f"Kapatılan uygulamalar: {', '.join(killed)}"


# ----------------------------------------------------
#  GENERATE REPORT
# ----------------------------------------------------
def generate_report():
    status = check_system_status()
    report = (
        f"=== SM System Stabilizer Report ===\n"
        f"CPU Usage: {status['cpu']}%\n"
        f"RAM Usage: {status['ram']}%\n"
        f"Disk Usage: {status['disk']}%\n"
        f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    )

    with open("system_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    return "Rapor oluşturuldu: system_report.txt"
