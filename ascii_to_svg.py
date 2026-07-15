import sys
import os
try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Creating default placeholder ASCII art.")
    Image = None

def generate_svg(image_path, out_dark="dark.svg", out_light="light.svg"):
    chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    ascii_lines = []
    
    if Image and os.path.exists(image_path):
        try:
            img = Image.open(image_path).convert('L')
            width = 40
            aspect_ratio = img.height / img.width
            new_height = int(aspect_ratio * width * 0.5)
            img = img.resize((width, new_height))
            pixels = list(img.getdata())
            
            for i in range(0, len(pixels), width):
                row = pixels[i:i+width]
                # Map dark to space, bright to @
                line_str = "".join([chars[int(p / 256 * len(chars))] for p in row])
                ascii_lines.append(line_str)
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")

    if not ascii_lines:
        # Default placeholder ASCII (Anonymous/Hacker silhouette)
        ascii_lines = [
            "         .::::.         ",
            "       .::::::::.       ",
            "      ::::::::::::      ",
            "      ::::::::::::      ",
            "       ::::::::::       ",
            "         ::::::         ",
            "         ::::::         ",
            "      .::::::::::.      ",
            "    .::::::::::::::.    ",
            "  .::::::::::::::::::.  ",
            " :::::::::::::::::::::: ",
            " :::::::::::::::::::::: "
        ]

    system_info = [
        "gowtham@devos —",
        ". Subject: ....................... Karri Gowtham Venkata Reddy",
        ". Role: ................. Final-Year CSE Student · Software Developer",
        ". Origin: ........................... Andhra Pradesh, India",
        ". Education: ................. B.Tech CSE, KL University, CGPA/91%",
        ". Status: .......... Building Anti-Gravity AI · Job Hunting · Learning",
        ". ToolChain: ..................... VS Code, Git, GitHub",
        "",
        ". Core.Lang: ................ Java, Python, C, JavaScript",
        ". Core.Frontend: ................. React.js, HTML5, CSS3",
        ". Core.Backend: ................. Node.js, Firebase",
        ". Core.Database: ..................... MongoDB",
        ". Core.Infra: .............. UiPath (RPA), AWS, Oracle Cloud",
        "",
        "- Contact ————————————",
        ". Grid.Mail: ............... 2300032792cseird@gmail.com",
        ". Grid.Portfolio: ............... YOUR_PORTFOLIO_URL",
        ". Grid.LinkedIn: ................ YOUR_LINKEDIN_HANDLE",
        ". Grid.Github: ................... gowtham786786",
        "",
        "- Live Stats ————————————",
        "  See live GitHub stats badges below in README ↓"
    ]

    def make_svg(bg_color, text_color, highlight_color, stroke_color, filename):
        svg_width = 950
        svg_height = max(len(ascii_lines) * 16, len(system_info) * 20) + 120
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
  <style>
    .terminal-text {{ font-family: ui-monospace, "Cascadia Code", "Fira Code", monospace; }}
    @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    .blinking {{ animation: blink 2s step-end infinite; }}
  </style>
  <rect width="100%" height="100%" rx="10" fill="{bg_color}" stroke="{stroke_color}" stroke-width="2"/>
  
  <!-- Window Chrome -->
  <circle cx="25" cy="25" r="6" fill="#ff5f56" />
  <circle cx="45" cy="25" r="6" fill="#ffbd2e" />
  <circle cx="65" cy="25" r="6" fill="#27c93f" />
  <text x="{svg_width/2}" y="30" class="terminal-text" font-size="14" fill="{text_color}" text-anchor="middle">gowtham@devos ~ % ./profile.sh --live</text>
  <text x="{svg_width - 25}" y="30" class="terminal-text blinking" font-size="14" font-weight="bold" fill="{highlight_color}" text-anchor="end">● SCANNING</text>
  <line x1="0" y1="50" x2="{svg_width}" y2="50" stroke="{stroke_color}" stroke-width="1"/>
  
  <!-- VISUAL.MAP Header -->
  <text x="40" y="85" class="terminal-text" font-size="14" font-weight="bold" fill="{highlight_color}">VISUAL.MAP</text>
  '''
        
        # Ascii Art
        y_offset = 120
        for line in ascii_lines:
            safe_line = line.replace(' ', '&#160;').replace('<', '&lt;').replace('>', '&gt;')
            svg += f'  <text x="40" y="{y_offset}" class="terminal-text" font-size="12" fill="{text_color}">{safe_line}</text>\n'
            y_offset += 16
            
        # SYSTEM.INFO Header
        svg += f'  <text x="400" y="85" class="terminal-text" font-size="14" font-weight="bold" fill="{highlight_color}">SYSTEM.INFO</text>\n'
        
        y_offset = 120
        for line in system_info:
            safe_line = line.replace(' ', '&#160;').replace('<', '&lt;').replace('>', '&gt;')
            svg += f'  <text x="400" y="{y_offset}" class="terminal-text" font-size="14" fill="{text_color}">{safe_line}</text>\n'
            y_offset += 20
            
        svg += '</svg>'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(svg)
            
    # Dark Mode
    make_svg('#0D1117', '#c9d1d9', '#00b4d8', '#30363d', out_dark)
    # Light Mode
    make_svg('#ffffff', '#24292f', '#0077b6', '#d0d7de', out_light)

if __name__ == '__main__':
    image_path = 'photo.jpg' if len(sys.argv) < 2 else sys.argv[1]
    generate_svg(image_path)
    print(f"Generated SVG banners (Dark & Light).")
