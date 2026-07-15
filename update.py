import os
import sys

def main():
    print("Updating SVG banners...")
    image_arg = sys.argv[1] if len(sys.argv) > 1 else "photo.jpg"
    os.system(f"python ascii_to_svg.py {image_arg}")
    print("Update complete.")

if __name__ == "__main__":
    main()
