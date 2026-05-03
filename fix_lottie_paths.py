import re
import glob

# Sub-directory pages need "../" prefix for the lottie src
subdir_files = [
    'about-us/index.html',
    'contact/index.html',
    'gallery/index.html',
    'services/index.html',
]

for file in subdir_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix the lottie src path for subdirectory pages
        new_content = content.replace(
            'src="ottie-ishmjKEnlg.lottie"',
            'src="../ottie-ishmjKEnlg.lottie"'
        )

        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed path: {file}")
        else:
            print(f"No change needed: {file}")
    except FileNotFoundError:
        print(f"Not found: {file}")

print("\nDone fixing lottie paths for subdir pages.")
