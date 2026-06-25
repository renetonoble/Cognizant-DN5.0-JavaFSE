#!/usr/bin/env python3
"""
Generate styled screenshots for Java exercises using ImageMagick.
Creates both CODE screenshots and OUTPUT screenshots.
"""
import subprocess
import os
import sys

# Color theme: Dark terminal-style
BG_COLOR        = "#1E1E2E"   # dark navy
HEADER_COLOR    = "#313244"   # slightly lighter header
BORDER_COLOR    = "#89B4FA"   # blue accent
CODE_FG         = "#CDD6F4"   # light lavender text
KEYWORD_COLOR   = "#CBA6F7"   # purple for keywords
OUTPUT_FG       = "#A6E3A1"   # green for output text
TITLE_COLOR     = "#89B4FA"   # blue title

FONT = "DejaVu-Sans-Mono"
FONT_SIZE = 18
LINE_HEIGHT = 26
PADDING = 40
HEADER_H = 60
IMG_WIDTH = 1100


def wrap_lines(text, max_chars=100):
    """Wrap long lines."""
    lines = []
    for line in text.split('\n'):
        if len(line) <= max_chars:
            lines.append(line)
        else:
            while len(line) > max_chars:
                lines.append(line[:max_chars])
                line = '    ' + line[max_chars:]
            lines.append(line)
    return lines


def escape(s):
    """Escape special characters for ImageMagick."""
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('"', '\\"').replace('%', '%%').replace('@', '\\@').replace('<', '\\<').replace('>', '\\>').replace('&', '\\&')


def make_screenshot(title, subtitle, content, output_path, is_output=False):
    """Generate a styled screenshot image."""
    lines = wrap_lines(content)
    
    # Calculate image height
    content_h = len(lines) * LINE_HEIGHT + PADDING * 2
    img_height = HEADER_H + content_h + 20
    
    fg_color = OUTPUT_FG if is_output else CODE_FG
    header_icon = "▶  OUTPUT" if is_output else "</>  CODE"
    
    # Build the ImageMagick command
    cmd = ['convert']
    
    # Background
    cmd += ['-size', f'{IMG_WIDTH}x{img_height}', f'xc:{BG_COLOR}']
    
    # Header bar
    cmd += ['-fill', HEADER_COLOR,
            '-draw', f'rectangle 0,0 {IMG_WIDTH},{HEADER_H}']
    
    # Top border line
    cmd += ['-fill', BORDER_COLOR,
            '-draw', f'rectangle 0,0 {IMG_WIDTH},4']
    
    # Left accent bar
    cmd += ['-fill', BORDER_COLOR,
            '-draw', f'rectangle 0,{HEADER_H} 4,{img_height}']
    
    # Traffic lights (decorative dots)
    cmd += ['-fill', '#F38BA8',  # red dot
            '-draw', 'circle 24,30 34,30']
    cmd += ['-fill', '#F9E2AF',  # yellow dot
            '-draw', 'circle 52,30 62,30']
    cmd += ['-fill', '#A6E3A1',  # green dot
            '-draw', 'circle 80,30 90,30']
    
    # Title text
    cmd += ['-font', FONT, '-pointsize', '16',
            '-fill', TITLE_COLOR,
            '-annotate', f'+110+{HEADER_H//2 + 6}', escape(f'{header_icon}  |  {title}')]
    
    # Subtitle
    cmd += ['-fill', '#585B70',
            '-pointsize', '13',
            '-annotate', f'+{IMG_WIDTH - 320}+{HEADER_H//2 + 6}', escape(subtitle)]
    
    # Code/output lines
    cmd += ['-font', FONT, '-pointsize', str(FONT_SIZE), '-fill', fg_color]
    
    y = HEADER_H + PADDING + LINE_HEIGHT
    for line in lines:
        if line.strip():
            cmd += ['-annotate', f'+{PADDING + 10}+{y}', escape(line)]
        y += LINE_HEIGHT
    
    cmd += [output_path]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        return False
    print(f"✔ Created: {output_path}")
    return True


# ─── Exercise definitions ────────────────────────────────────────────────────

BASE = "/home/godofthunder/Desktop/Cognizant-DN5.0-JavaFSE/Week 1"
DP_SHOTS  = f"{BASE}/Design Patterns/screenshots"
ALG_SHOTS = f"{BASE}/Algorithms_Data Structures/screenshots"

exercises = [
    # ── Design Patterns ─────────────────────────────────────────────────────
    {
        "title": "Exercise 1 - Singleton Pattern | Logger.java",
        "subtitle": "Cognizant DN5.0 | Design Patterns",
        "code_file": f"{BASE}/Design Patterns/Exercise1_SingletonPattern/Logger.java",
        "test_file": f"{BASE}/Design Patterns/Exercise1_SingletonPattern/SingletonTest.java",
        "compile_dir": f"{BASE}/Design Patterns/Exercise1_SingletonPattern",
        "compile_cmd": "javac Logger.java SingletonTest.java",
        "run_cmd": "java SingletonTest",
        "code_out": f"{DP_SHOTS}/ex1_singleton_code.png",
        "run_out":  f"{DP_SHOTS}/ex1_singleton_output.png",
    },
    {
        "title": "Exercise 2 - Factory Method Pattern | FactoryMethodTest.java",
        "subtitle": "Cognizant DN5.0 | Design Patterns",
        "code_file": f"{BASE}/Design Patterns/Exercise2_FactoryMethodPattern/FactoryMethodTest.java",
        "compile_dir": f"{BASE}/Design Patterns/Exercise2_FactoryMethodPattern",
        "compile_cmd": "javac *.java",
        "run_cmd": "java FactoryMethodTest",
        "code_out": f"{DP_SHOTS}/ex2_factory_code.png",
        "run_out":  f"{DP_SHOTS}/ex2_factory_output.png",
    },
    # ── Algorithms ──────────────────────────────────────────────────────────
    {
        "title": "Algo Ex 2 - E-commerce Search | SearchTest.java",
        "subtitle": "Cognizant DN5.0 | Algorithms & Data Structures",
        "code_file": f"{BASE}/Algorithms_Data Structures/Exercise2_EcommerceSearch/SearchTest.java",
        "compile_dir": f"{BASE}/Algorithms_Data Structures/Exercise2_EcommerceSearch",
        "compile_cmd": "javac Product.java SearchTest.java",
        "run_cmd": "java SearchTest",
        "code_out": f"{ALG_SHOTS}/ex2_search_code.png",
        "run_out":  f"{ALG_SHOTS}/ex2_search_output.png",
    },
    {
        "title": "Algo Ex 7 - Financial Forecasting | FinancialForecasting.java",
        "subtitle": "Cognizant DN5.0 | Algorithms & Data Structures",
        "code_file": f"{BASE}/Algorithms_Data Structures/Exercise7_FinancialForecasting/FinancialForecasting.java",
        "compile_dir": f"{BASE}/Algorithms_Data Structures/Exercise7_FinancialForecasting",
        "compile_cmd": "javac FinancialForecasting.java",
        "run_cmd": "java FinancialForecasting",
        "code_out": f"{ALG_SHOTS}/ex7_forecasting_code.png",
        "run_out":  f"{ALG_SHOTS}/ex7_forecasting_output.png",
    },
]

# ─── Process each exercise ───────────────────────────────────────────────────
for ex in exercises:
    print(f"\n{'='*60}")
    print(f"Processing: {ex['title']}")
    print('='*60)

    # Read main code file
    with open(ex['code_file'], 'r') as f:
        code_content = f.read()

    # Generate CODE screenshot
    make_screenshot(
        title=ex['title'],
        subtitle=ex['subtitle'],
        content=code_content,
        output_path=ex['code_out'],
        is_output=False
    )

    # Compile
    result = subprocess.run(
        ex['compile_cmd'], shell=True,
        cwd=ex['compile_dir'], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"COMPILE ERROR: {result.stderr}")
        continue

    # Run and capture output
    result = subprocess.run(
        ex['run_cmd'], shell=True,
        cwd=ex['compile_dir'], capture_output=True, text=True
    )
    output_content = result.stdout
    if result.returncode != 0:
        output_content += f"\nSTDERR: {result.stderr}"

    # Generate OUTPUT screenshot
    make_screenshot(
        title=ex['title'],
        subtitle=ex['subtitle'],
        content=output_content,
        output_path=ex['run_out'],
        is_output=True
    )

print("\n\n✔ All screenshots generated successfully!")
