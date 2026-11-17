import base64, concurrent.futures as cf
from gen import gen
def up(k, src):
    uri = 'data:image/png;base64,' + base64.b64encode(open(src, 'rb').read()).decode()
    gen('fal-ai/esrgan', 'up_' + k, {'image_url': uri, 'scale': 2})
BG = {
 'teal': 'Abstract premium background for a fintech brand banner: smooth flowing translucent glass ribbons and soft 3D waves in teal, turquoise and aqua with a few thin warm gold light lines, along the left and right edges and bottom corners, deep dark teal empty calm space in the center, subtle glow, elegant, luxurious, ultra clean studio render, no text, no logos, no objects in the center',
 'green': 'Abstract luxury background for a fintech brand banner: smooth flowing dark emerald green silk waves with thin elegant polished gold lines and soft gold bokeh sparkles, along the left and right edges and bottom corners, deep dark green empty calm space in the center, subtle glow, rich, expensive, ultra clean studio render, no text, no logos, no objects in the center',
}
jobs = [lambda: up('teal', '4_teal_wallet_0.png'), lambda: up('green', '6_green_wallet_0.png')]
for k in BG:
    for i in range(2): jobs.append(lambda k=k, i=i: gen('fal-ai/flux-pro/v1.1-ultra', f'bg_{k}{i}', {'prompt': BG[k], 'aspect_ratio': '16:9', 'seed': 7 + i}))
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(lambda f: f(), jobs))
from PIL import Image
sh = Image.new('RGB', (3200, 450))
for n, f in enumerate(['bg_teal0', 'bg_teal1', 'bg_green0', 'bg_green1']): sh.paste(Image.open(f + '_0.png').convert('RGB').resize((800, 450)), (800*n, 0))
sh.save('bg_sheet.jpg', quality=85)
