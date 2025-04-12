import os

def rename_files(folder_path, prefix="", suffix="", numbering=False):
    try:
        files = os.listdir(folder_path)
        files.sort()  # Ensuring order in renaming

        count = 1
        for file_name in files:
            old_path = os.path.join(folder_path, file_name)
            
            if os.path.isfile(old_path):  # Ignore folders
                file_ext = os.path.splitext(file_name)[1]  # Get file extension
                new_name = f"{prefix}{count if numbering else ''}{suffix}{file_ext}"
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                print(f"✅ Renamed: {file_name} ➝ {new_name}")

                count += 1

        print("\n🎉 Bulk renaming completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Main function
def main():
    print("📂 Bulk File Renamer\n")
    
    folder_path = input("📌 Enter folder path: ").strip()
    prefix = input("🔤 Enter prefix (optional): ").strip()
    suffix = input("🔤 Enter suffix (optional): ").strip()
    numbering = input("🔢 Add numbering? (yes/no): ").strip().lower() == "yes"

    rename_files(folder_path, prefix, suffix, numbering)

# Run the program
if __name__ == "__main__":
    main()