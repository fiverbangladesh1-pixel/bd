import concurrent.futures as cf
from gen import gen
tail = ' Logo icon for a digital wallet brand, single emblem perfectly centered with generous margin, front view, designed to be cropped into a circle profile picture, ultra premium brand identity, photorealistic 3D studio render, razor sharp, the letter E must be a clear readable capital E, no other text, no watermark.'
D = {
 '1_emerald_gold': 'A round medallion logo in deep emerald green glossy enamel with a thin polished gold rim, in the center a bold elegant capital letter E in polished gold with soft bevels, dark green background.',
 '3_black_gold': 'A bold thick sans-serif capital letter E in polished brushed gold metal with crisp bevels, the middle arm of the E ends in a small round gold coin, inside a thin gold circle ring, on a matte black background with soft top spotlight.',
 '5_crimson_gold': 'A glossy deep crimson red rounded-square app icon tile with a bold capital letter E in polished gold, subtle glass highlight on top, thin gold edge, on a dark wine red background.',
 '6_green_wallet': 'A premium 3D leather wallet icon in rich deep green with fine stitching and a round red snap button on the strap, a bold white capital letter E embossed on the front, a gold card peeking out of the top, on a dark green background with soft vignette.',
}
def job(k): gen('fal-ai/nano-banana', k, {'prompt': D[k] + tail, 'num_images': 1})
with cf.ThreadPoolExecutor(4) as ex: list(ex.map(job, D))
from PIL import Image
ks = ['1_emerald_gold','2_sapphire_silver','3_black_gold','4_teal_wallet','5_crimson_gold','6_green_wallet','7_diamond','8_white_navy']; S = 600; sh = Image.new('RGB', (S*4, S*2))
for i, k in enumerate(ks):
    try: sh.paste(Image.open(k + '_0.png').convert('RGB').resize((S, S)), ((i % 4)*S, (i//4)*S))
    except Exception as e: print(k, e)
sh.save('sheet.jpg', quality=88)
