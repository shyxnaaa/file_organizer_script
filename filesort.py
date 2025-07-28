import os
import shutil

def auto_sort_files():
    # Step 1: Ask the user to enter folder path
    folder_path = input("Enter the full path of the folder to sort: ").strip()

    # Step 2: Check if the folder exists
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path! Please check and try again.")
        return

    # Step 3: Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Step 4: Get the file extension
        _, extension = os.path.splitext(filename)
        ext = extension[1:].lower()  # Remove dot and convert to lowercase

        if ext == "":
            ext = "no_extension"

        # Step 5: Create a folder for the extension
        target_folder = os.path.join(folder_path, ext)
        os.makedirs(target_folder, exist_ok=True)

        # Step 6: Move the file to the new folder
        target_path = os.path.join(target_folder, filename)
        shutil.move(file_path, target_path)

        print(f"✅ Moved: {filename} → /{ext}/")

    print("\n🎉 Done! All files sorted.")

# Run the function
auto_sort_files()
