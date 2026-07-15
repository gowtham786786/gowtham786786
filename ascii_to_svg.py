import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Pillow not installed. Creating default placeholder ASCII art.")
    Image = None

def generate_svg(image_path, out_dark="dark.svg", out_light="light.svg"):
    chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    ascii_lines = []
    
    if Image and os.path.exists(image_path):
        try:
            img = Image.open(image_path).convert('L')
            img = ImageOps.autocontrast(img)
            width = 80
            aspect_ratio = img.height / img.width
            new_height = int(aspect_ratio * width * 0.5)
            img = img.resize((width, new_height))
            # get_flattened_data or getdata
            pixels = list(img.getdata())
            
            for i in range(0, len(pixels), width):
                row = pixels[i:i+width]
                # Invert intensity: 255 (white bg) -> index 0 (space), 0 (black) -> index 9 (@)
                line_str = "".join([chars[int((255 - p) / 256 * len(chars))] for p in row])
                ascii_lines.append(line_str)
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")

    if not ascii_lines:
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
        ". Subject: .......................... Karri Gowtham Venkata Reddy",
        ". Role: ................ Final-Year CSE Student · Software Developer",
        ". Origin: ........................... Andhra Pradesh, India",
        ". Education: ................ B.Tech CSE, KL University, CGPA 91%",
        ". Status: .......... Building Anti-Gravity AI · Job Hunting · Learning",
        ". ToolChain: ..................... VS Code, Git, GitHub, Postman",
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

    def make_svg(bg_color, text_color, highlight_color, stroke_color, filename, mode="dark"):
        svg_width = 1000
        svg_height = max(len(ascii_lines) * 9, len(system_info) * 20) + 120
        
        if mode == "dark":
            grad_c1, grad_c2 = "#00b4d8", "#90e0ef"
        else:
            grad_c1, grad_c2 = "#0077b6", "#023e8a"

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
  <style>
    .terminal-text {{ font-family: ui-monospace, "Cascadia Code", "Fira Code", monospace; }}
  </style>
  <defs>
    <!-- Animated Gradient -->
    <linearGradient id="animGrad_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{grad_c1}">
        <animate attributeName="stop-color" values="{grad_c1};{grad_c2};{grad_c1}" dur="4s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="{grad_c2}">
        <animate attributeName="stop-color" values="{grad_c2};{grad_c1};{grad_c2}" dur="4s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Reveal Mask ClipPath (slides open) -->
    <clipPath id="slideOpen_{mode}">
      <rect x="0" y="0" width="{svg_width}" height="0">
        <animate attributeName="height" from="0" to="{svg_height}" dur="1s" begin="0s" fill="freeze" />
      </rect>
    </clipPath>
'''
        
        base_delay = 1.0 
        typing_speed = 0.08
        
        # Generate clip paths for each typed line
        for i in range(len(system_info)):
            line_y = 120 + (i * 20) - 15  # 15px above the text baseline
            delay = base_delay + (i * typing_speed)
            svg += f'''    <clipPath id="typeLine_{mode}_{i}">
      <rect x="420" y="{line_y}" width="0" height="25">
        <animate attributeName="width" from="0" to="560" dur="{typing_speed}s" begin="{delay}s" fill="freeze" />
      </rect>
    </clipPath>
'''
        
        cursor_begin = base_delay + (len(system_info) * typing_speed)
        
        svg += f'''  </defs>

  <!-- Pulsing Border Rect -->
  <rect width="100%" height="100%" rx="10" fill="{bg_color}" stroke="url(#animGrad_{mode})" stroke-width="2">
    <animate attributeName="stroke-opacity" values="0.3;1;0.3" dur="3s" repeatCount="indefinite" />
  </rect>

  <g clip-path="url(#slideOpen_{mode})">
    
    <!-- Moving Scanline -->
    <rect x="0" y="-50" width="100%" height="50" fill="url(#animGrad_{mode})" opacity="0.1">
      <animateTransform attributeName="transform" type="translate" from="0 -50" to="0 {svg_height + 50}" dur="4s" repeatCount="indefinite" />
    </rect>

    <!-- Window Chrome -->
    <circle cx="25" cy="25" r="6" fill="#ff5f56" />
    <circle cx="45" cy="25" r="6" fill="#ffbd2e" />
    <circle cx="65" cy="25" r="6" fill="#27c93f" />
    <text x="{svg_width/2}" y="30" class="terminal-text" font-size="14" fill="{text_color}" text-anchor="middle">gowtham@devos ~ % ./profile.sh --live</text>
    
    <text x="{svg_width - 25}" y="30" class="terminal-text" font-size="14" font-weight="bold" fill="url(#animGrad_{mode})" text-anchor="end">● SCANNING
      <animate attributeName="opacity" values="1;0;1" dur="1.5s" repeatCount="indefinite" />
    </text>
    <line x1="0" y1="50" x2="{svg_width}" y2="50" stroke="{stroke_color}" stroke-width="1"/>
    
    <!-- VISUAL.MAP Header -->
    <text x="30" y="85" class="terminal-text" font-size="14" font-weight="bold" fill="url(#animGrad_{mode})">VISUAL.MAP</text>
'''
        
        # Ascii Art
        y_offset = 110
        for line in ascii_lines:
            safe_line = line.replace(' ', '&#160;').replace('<', '&lt;').replace('>', '&gt;')
            svg += f'    <text x="30" y="{y_offset}" class="terminal-text" font-size="7.5" fill="url(#animGrad_{mode})">{safe_line}</text>\n'
            y_offset += 9
            
        # SYSTEM.INFO Header
        svg += f'\n    <text x="420" y="85" class="terminal-text" font-size="14" font-weight="bold" fill="url(#animGrad_{mode})">SYSTEM.INFO</text>\n'
        
        y_offset = 120
        last_line_len = 0
        for i, line in enumerate(system_info):
            safe_line = line.replace(' ', '&#160;').replace('<', '&lt;').replace('>', '&gt;')
            svg += f'    <text x="420" y="{y_offset}" class="terminal-text" font-size="14" fill="{text_color}" clip-path="url(#typeLine_{mode}_{i})">{safe_line}</text>\n'
            if i == len(system_info) - 1:
                last_line_len = len(line)
            y_offset += 20
            
        # Blinking Cursor immediately after the last character of the last line
        cursor_x = 420 + (last_line_len * 8.4) + 5
        cursor_y = y_offset - 20 - 12
        svg += f'''
    <rect x="{cursor_x}" y="{cursor_y}" width="8" height="15" fill="{highlight_color}" opacity="0">
      <animate attributeName="opacity" values="0;1;0" dur="1s" begin="{cursor_begin}s" repeatCount="indefinite" />
    </rect>

  </g>
</svg>'''
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(svg)
            
    make_svg('#0D1117', '#c9d1d9', '#00b4d8', '#30363d', out_dark, "dark")
    make_svg('#ffffff', '#24292f', '#0077b6', '#d0d7de', out_light, "light")

if __name__ == '__main__':
    image_path = 'photo.jpg' if len(sys.argv) < 2 else sys.argv[1]
    generate_svg(image_path)
    print(f"Generated SVG banners (Dark & Light) with SMIL animations.")
