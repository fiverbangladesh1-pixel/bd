import concurrent.futures as cf
from gen import gen
tail = ' Logo icon for a digital wallet brand, single emblem perfectly centered with generous margin, front view, designed to be cropped into a circle profile picture, ultra premium brand identity, crafted by a senior logo designer, photorealistic 3D studio render, razor sharp, no words, no text other than the single letter E, no watermark.'
D = {
 '1_emerald_gold': 'A luxurious emblem: a bold elegant capital letter E in polished gold, set on a deep emerald green enamel round medallion with a fine gold rim, subtle guilloche engraving pattern, rich dark green background.',
 '2_sapphire_silver': 'A modern shield-shaped badge in deep sapphire blue glossy glass with a bold capital letter E in brushed silver chrome, thin silver bevel edge, cool blue rim light, dark navy background.',
 '3_black_gold': 'An ultra minimal luxury monogram: a refined geometric capital letter E made of three clean gold bars with a small gold coin circle, inside a thin gold ring, on matte black stone background with soft spotlight.',
 '4_teal_wallet': 'A friendly modern 3D wallet icon in glossy teal and turquoise gradient with rounded corners, a white bold capital letter E embossed on the front and a gold coin peeking out of the top, on a clean bright aqua to deep teal gradient background.',
 '5_sunrise_coin': 'A bold 3D gold coin standing upright with an embossed capital letter E, glowing warm orange and red sunrise gradient background, glossy highlights, energetic and warm.',
 '6_green_red': 'A bold capital letter E built from three thick rounded bars in rich bottle green glossy enamel with a bright red circular button at the end of the middle bar, thin gold outline, on a deep dark green background with soft vignette.',
 '7_diamond': 'A capital letter E carved from a brilliant faceted diamond crystal, icy white and blue refractions with sparkles, floating on a dark midnight navy background with a soft blue glow.',
 '8_white_navy': 'A clean premium app icon: a rounded square tile in deep navy blue with a subtle gradient, a bold white capital letter E whose middle bar ends in a small gold dot, soft shadow, on a pure white background.',
}
def job(k): gen('fal-ai/nano-banana', k, {'prompt': D[k] + tail, 'num_images': 1})
with cf.ThreadPoolExecutor(8) as ex: list(ex.map(job, D))
from PIL import Image
ks = list(D); S = 600; sh = Image.new('RGB', (S*4, S*2))
for i, k in enumerate(ks):
    try: sh.paste(Image.open(k + '_0.png').convert('RGB').resize((S, S)), ((i % 4)*S, (i//4)*S))
    except Exception as e: print(k, e)
sh.save('sheet.jpg', quality=88)
