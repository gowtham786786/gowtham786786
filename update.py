import os
import sys

def main():
    print("Updating SVG banners...")
    image_arg = sys.argv[1] if len(sys.argv) > 1 else "photo.jpg"
    # Ensure ascii_to_svg.py exists before running
    if not os.path.exists("ascii_to_svg.py"):
        print("Error: ascii_to_svg.py not found in current directory.")
        sys.exit(1)
        
    exit_code = os.system(f"python ascii_to_svg.py {image_arg}")
    if exit_code == 0:
        print("Update complete. SVGs regenerated.")
    else:
        print("Update failed with an error.")

if __name__ == "__main__":
    main()
