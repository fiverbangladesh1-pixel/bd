import base64, os, concurrent.futures as cf
from gen import gen
ref = 'data:image/png;base64,' + base64.b64encode(open('raw/logo.png', 'rb').read()).decode()
S = {
 's1': 'Create a new image with NO logo and NO text: a cinematic abstract scene of swirling translucent liquid sapphire and cyan glass ribbons with glowing white light streaks and tiny light particles in a deep dark blue void, same blue and cyan colours as the reference, volumetric light, glossy, premium 3D render, square.',
 's2': 'Create a cinematic extreme close-up 3D render of only the white E symbol from this logo, made of thick glossy white glass with blue reflections, tilted at a dramatic angle and partly out of frame, shallow depth of field, dark deep-blue studio with soft cyan rim light and bokeh. No text at all.',
 's3': 'Create a new image with NO logo and NO text: hundreds of small glossy white glass fragments and glowing cyan light particles floating scattered in a dark deep-blue space, soft volumetric light beam from the top left, shallow depth of field, premium cinematic 3D render, same blue and cyan colours as the reference, square.',
}
os.chdir('raw')
with cf.ThreadPoolExecutor(3) as ex: list(ex.map(lambda k: gen('fal-ai/nano-banana/edit', k, {'prompt': S[k], 'image_urls': [ref], 'num_images': 1}), S))
from PIL import Image
sh = Image.new('RGB', (1800, 600))
for i, k in enumerate(S):
    im = Image.open(k + '_0.png').convert('RGB'); print(k, im.size); im.resize((1024, 1024), Image.LANCZOS).save(k + '.png'); sh.paste(im.resize((600, 600)), (i*600, 0))
sh.save('starts.jpg', quality=85)
