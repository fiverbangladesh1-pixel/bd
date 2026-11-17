import concurrent.futures as cf
from gen import gen
tail = ' Professional brand identity logo design by a world-class logo designer, flat vector style, perfectly geometric, clean crisp edges, balanced negative space, timeless and memorable like a top global fintech brand. Logo mark centered on top, and below it the wordmark text "E-WALLET" in a bold modern geometric sans-serif typeface, correctly spelled. Plain solid background, lots of empty space, no mockup, no extra text, no watermark.'
D = {
 '1': 'A clever monogram logo: the letter E formed by three stacked horizontal rounded bars that look like three payment cards, the middle one shorter with a small circle, electric blue on a deep navy background, white wordmark.',
 '2': 'A logo mark: a bold letter E whose three arms become forward-pointing arrows suggesting fast money transfer, vivid emerald green on a near-black background, white wordmark.',
 '3': 'A logo mark: a rounded-square wallet silhouette with the letter E cut out in negative space and a small coin dot, bright orange on a warm off-white background, dark charcoal wordmark.',
 '4': 'A luxury logo mark: a hexagonal shield outline containing a refined geometric letter E, thin elegant lines, metallic gold on a pure black background, gold wordmark.',
 '5': 'A dynamic logo mark: the letter E made from a single continuous folded ribbon like origami, with a gradient from red to orange, on a white background, black wordmark.',
 '6': 'A logo mark: a circle coin with the letter E inside formed by three horizontal slots, with a small orbit ring around it suggesting digital payments, teal and lime green on a dark teal background, white wordmark.',
 '7': 'A bold minimal logo mark: a solid rounded square app icon with a thick white letter E where the middle arm ends in a check mark, royal blue icon on a white background, royal blue wordmark.',
 '8': 'A modern logo mark: the letter E built from three horizontal speed lines of decreasing length with a lightning bolt cut, yellow on a black background, white wordmark.',
}
def job(k): gen('fal-ai/ideogram/v3', 'o' + k, {'prompt': D[k] + tail, 'image_size': 'square_hd', 'rendering_speed': 'QUALITY', 'style': 'DESIGN', 'expand_prompt': False})
with cf.ThreadPoolExecutor(8) as ex: list(ex.map(job, D))
from PIL import Image
S = 600; sh = Image.new('RGB', (S*4, S*2))
for i in range(8):
    try: sh.paste(Image.open(f'o{i+1}_0.png').convert('RGB').resize((S, S)), ((i % 4)*S, (i//4)*S))
    except Exception as e: print(i+1, e)
sh.save('sheet.jpg', quality=88)
