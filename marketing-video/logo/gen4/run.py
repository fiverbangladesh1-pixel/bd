import concurrent.futures as cf
from gen import gen
tail = ' The emblem fills most of the frame and is perfectly centered, symmetrical front view, designed as a round profile picture that stays bold and readable at tiny size. Hyper-realistic luxury product render, ray-traced reflections, studio lighting, macro detail, 8k, flawless. The only letter is a single clear capital E. No other text, no watermark.'
D = {
 'a': 'A breathtaking 3D emblem: a thick bold capital letter E sculpted from mirror-polished liquid gold with warm glowing edges, floating in front of a deep royal sapphire blue glossy glass disc with a thin glowing gold rim, intense orange-gold rim light against rich blue, complementary colors, luminous.',
 'b': 'A breathtaking 3D emblem: a chunky glossy white ceramic capital letter E with soft gold bevels and a small gold coin set into its middle arm, on a full-bleed vivid sunrise gradient background from bright golden yellow through hot orange to magenta red, radiant, joyful, extremely eye-catching.',
 'c': 'A breathtaking 3D emblem: a bold capital letter E carved from glowing emerald green crystal glass with internal light and sparkling facets, encircled by a polished gold ring, on a deep black background with soft green glow.',
 'd': 'A breathtaking 3D emblem: a glossy royal blue glass sphere button with bright cyan inner glow and a bold embossed polished gold capital letter E in the center, thin gold ring bezel, crisp specular highlights, on a dark navy background.',
 'e': 'A breathtaking 3D emblem: a bold capital letter E made of electric cyan to lime green glowing glass with liquid light flowing inside, chrome edges, hovering over a deep midnight blue glossy disc, vivid neon reflections.',
 'f': 'A breathtaking 3D emblem: a luxurious round coin medallion in rich glossy red enamel with a wide polished gold rim and a bold raised polished gold capital letter E in the center, tiny diamond sparkle highlights, on a dark red velvet background.',
 'g': 'A breathtaking 3D emblem: a bold capital letter E in brilliant polished gold with a diamond-encrusted edge, set on a glossy black onyx disc with a thin bright gold ring, dramatic spotlight, ultimate luxury.',
 'h': 'A breathtaking 3D emblem: a bold glossy capital letter E with a vivid gradient from hot pink through orange to golden yellow, glass and chrome material with strong highlights, on a full-bleed deep turquoise to navy gradient background, bold complementary colors, radiant glow.',
}
def job(k): gen('fal-ai/flux-pro/v1.1-ultra', k, {'prompt': D[k] + tail, 'aspect_ratio': '1:1'})
with cf.ThreadPoolExecutor(8) as ex: list(ex.map(job, D))
from PIL import Image
S = 600; sh = Image.new('RGB', (S*4, S*2))
for i, k in enumerate(D):
    try: sh.paste(Image.open(f'{k}_0.png').convert('RGB').resize((S, S)), ((i % 4)*S, (i//4)*S))
    except Exception as e: print(k, e)
sh.save('sheet.jpg', quality=88)
