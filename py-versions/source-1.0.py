import os
import shutil
import sys
import time

def main():
    print("=== fflag injector ===\n")
    time.sleep(2)

    roblox_versions_path = os.path.join(os.getenv("LOCALAPPDATA"), "Roblox", "Versions")
    if not os.path.isdir(roblox_versions_path):
        print(f"[ERROR] Roblox Versions folder not found: {roblox_versions_path}")
        sys.exit(1)
    time.sleep(2)

    try:
        latest_folder = max(
            (os.path.join(roblox_versions_path, d) for d in os.listdir(roblox_versions_path) if os.path.isdir(os.path.join(roblox_versions_path, d))),
            key=os.path.getmtime
        )
        print(f"[INFO] Latest Roblox version detected: {latest_folder}")
    except ValueError:
        print("[ERROR] No Roblox version folders found.")
        sys.exit(1)
    time.sleep(2)

    json_file = input("JSON FFlag file: ").strip('"').strip()
    if not os.path.isfile(json_file):
        print(f"[ERROR] Invalid file: {json_file}")
        sys.exit(1)
    if not json_file.lower().endswith(".json"):
        print(f"[ERROR] Not a JSON file: {json_file}")
        sys.exit(1)
    time.sleep(2)

    target_settings_folder = os.path.join(latest_folder, "ClientSettings")

    try:
        if not os.path.exists(target_settings_folder):
            os.makedirs(target_settings_folder, exist_ok=True)
            print(f"[INFO] Folder created: {target_settings_folder}")
        else:
            print("[INFO] Folder already exists, skipping")
    except Exception as e:
        print(f"[ERROR] Failed to create folder: {e}")
        sys.exit(1)
    time.sleep(2)

    destination_file = os.path.join(target_settings_folder, "ClientAppSettings.json")

    try:
        shutil.copy2(json_file, destination_file)
        print(f"[SUCCESS] {os.path.basename(json_file)} copied and renamed to ClientAppSettings.json in {target_settings_folder}")
    except Exception as e:
        print(f"[ERROR] Failed to copy file: {e}")
        sys.exit(1)
    time.sleep(2)

    print("[DONE] Injection complete")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
