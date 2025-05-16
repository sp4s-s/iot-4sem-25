import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import argparse

class OLED_Display:
    def __init__(self):
        self.RST = None
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=self.RST)
        self.disp.begin()
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

    def display_text(self, text):
        self.disp.clear()
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw.text((0, 0), text, font=self.font, fill=255)
        self.disp.image(self.image)
        self.disp.display()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--str", type=str, required=True, help="Text to display")
    args = parser.parse_args()
    oled = OLED_Display()
    oled.display_text(args.str)

if __name__ == "__main__":
    main()
