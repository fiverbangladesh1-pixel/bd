import sys, json, base64, urllib.request, os, ssl
def gen(model, name, payload):
    payload = dict(payload); payload.setdefault('sync_mode', True)
    req = urllib.request.Request('https://fal.run/' + model, data=json.dumps(payload).encode(), headers={'Authorization': 'Key dummy', 'Content-Type': 'application/json'})
    try:
        r = json.loads(urllib.request.urlopen(req, timeout=240).read())
    except urllib.error.HTTPError as e:
        print(name, 'HTTP', e.code, e.read()[:300]); return
    except Exception as e:
        print(name, 'ERR', e); return
    imgs = r.get('images') or ([r['image']] if r.get('image') else [])
    for i, im in enumerate(imgs):
        u = im['url'] if isinstance(im, dict) else im
        fn = f'{name}_{i}.png'
        if u.startswith('data:'):
            open(fn, 'wb').write(base64.b64decode(u.split(',', 1)[1]))
        else:
            try: open(fn, 'wb').write(urllib.request.urlopen(u, timeout=120).read())
            except Exception as e: print(name, 'download fail', u[:80], e); continue
        print('saved', fn, os.path.getsize(fn))
    if not imgs: print(name, 'no images', str(r)[:300])
if __name__ == '__main__':
    gen(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]))
