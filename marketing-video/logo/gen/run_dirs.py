import base64, json, sys, concurrent.futures as cf
from PIL import Image
from gen import gen
# reference: white mark on black, square
ic = Image.open('../export2/icon-white-transparent.png').convert('RGBA')
bg = Image.new('RGBA', ic.size, (0, 0, 0, 255)); bg.alpha_composite(ic); bg.convert('RGB').save('ref.png')
ref = 'data:image/png;base64,' + base64.b64encode(open('ref.png', 'rb').read()).decode()
base = ' Keep the exact silhouette, proportions and details of the logo in the reference image: the bold rounded letter E wallet with the strap and button hole, and the tilted card peeking out of the top. Single object, perfectly centered, front view with a very slight 3D tilt, generous empty margin around it, square composition, no text, no extra letters, no watermark. Ultra high-end brand identity render, studio lighting, razor sharp.'
dirs = {
 'A_glass': 'Render this logo as a premium 3D object made of thick frosted glass with polished edges, internal glow and a magenta to violet to electric blue gradient, subtle refraction and soft rim light, floating on a deep black-violet background with a faint purple glow behind it.',
 'B_chrome': 'Render this logo as a premium 3D object made of liquid mirror chrome with iridescent holographic reflections in pink, violet and cyan, on a pure black background with a soft glossy floor reflection.',
 'C_gold': 'Render this logo as a luxury 3D emblem made of polished and brushed 24k gold with fine bevels, on a matte black textured background, dramatic soft top light, elegant and expensive.',
 'D_soft': 'Render this logo as a soft inflated matte white 3D shape with smooth rounded edges and gentle shadows, the card in translucent frosted glass, on a vivid smooth magenta to violet to blue gradient background.',
 'E_neon': 'Render this logo as a glowing neon glass tube sign in magenta and electric blue, with realistic glow and reflections, on a very dark navy black wall.',
 'F_enamel': 'Render this logo as a glossy deep enamel and glass 3D app icon: the logo in luminous white glass embossed on a rounded-square tile with a rich magenta to violet to blue gradient, glossy highlights, on a dark background.',
}
def job(k):
    gen('fal-ai/nano-banana/edit', k, {'prompt': dirs[k] + base, 'image_urls': [ref], 'num_images': 2})
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(job, dirs))
