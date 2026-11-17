import base64, concurrent.futures as cf
from gen import gen
picks = {'glass': 'A_glass_1', 'chrome': 'B_chrome_0', 'gold': 'C_gold_0', 'soft': 'D_soft_0', 'neon': 'E_neon_1', 'enamel': 'F_enamel_0'}
def job(k):
    uri = 'data:image/png;base64,' + base64.b64encode(open(picks[k] + '.png', 'rb').read()).decode()
    gen('fal-ai/esrgan', 'up_' + k, {'image_url': uri, 'scale': 2})
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(job, picks))
