import base64, concurrent.futures as cf
from PIL import Image
from gen import gen
Image.open('flat.png').convert('RGB').resize((1024, 1024), Image.LANCZOS).save('ref.png')
ref = 'data:image/png;base64,' + base64.b64encode(open('ref.png', 'rb').read()).decode()
keep = ' Keep the logo exactly as in the reference image: the same white rounded E symbol with two slots, the same bold white text WALLET and the smaller spaced text SUPPORT below it, the same blue to cyan gradient colors, same proportions and spelling. Do not add any other text. Photorealistic, premium, sharp.'
D = {
 'glossy': 'Turn this flat logo into a premium glossy 3D version: the square becomes a thick glossy glass tile with softly rounded corners, the white symbol and letters are slightly raised glossy white enamel with soft shadows, bright specular highlights and a subtle light sweep across the surface, soft studio lighting, on a clean dark navy background.',
 'wall': 'A photorealistic mockup: this logo as an illuminated 3D sign mounted on a modern office reception wall of dark blue textured panels, the symbol and letters are white glowing acrylic with a soft blue halo, elegant interior, shallow depth of field.',
 'phone': 'A photorealistic mockup: a modern smartphone standing on a glossy dark surface showing this logo full-screen as an app splash screen, soft blue reflections on the surface, studio lighting, blurred dark blue background.',
 'card': 'A photorealistic mockup: a stack of premium business cards on a dark slate surface, the top card is deep blue with this logo printed in glossy white spot-UV finish, soft directional light, shallow depth of field.',
}
def job(k): gen('fal-ai/nano-banana/edit', k, {'prompt': D[k] + keep, 'image_urls': [ref], 'num_images': 1})
with cf.ThreadPoolExecutor(4) as ex: list(ex.map(job, D))
S = 700; sh = Image.new('RGB', (S*4, S))
for i, k in enumerate(D):
    try: sh.paste(Image.open(k + '_0.png').convert('RGB').resize((S, S)), (i*S, 0))
    except Exception as e: print(k, e)
sh.save('sheet.jpg', quality=88)
