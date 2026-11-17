import json, time, urllib.request, base64, sys, os
H = {'Authorization': 'Key dummy', 'Content-Type': 'application/json'}
def call(url, data=None, method=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None, headers=H, method=method)
    try: return json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e: return {'_err': e.code, '_body': e.read()[:500].decode('utf8', 'ignore')}
    except Exception as e: return {'_err': str(e)}
def submit(model, payload): return call('https://queue.fal.run/' + model, payload)
def uri(path, mime='image/png'): return f'data:{mime};base64,' + base64.b64encode(open(path, 'rb').read()).decode()
def wait(sub, name, tmax=900):
    if '_err' in sub: print(name, 'SUBMIT ERR', sub); return None
    t0 = time.time()
    while time.time() - t0 < tmax:
        st = call(sub['status_url'])
        s = st.get('status')
        if s == 'COMPLETED': break
        if '_err' in st: print(name, 'status err', st); return None
        time.sleep(6)
    else: print(name, 'timeout'); return None
    r = call(sub['response_url'])
    if '_err' in r: print(name, 'RESULT ERR', r); return None
    v = (r.get('video') or {}).get('url') or (r.get('videos') or [{}])[0].get('url')
    if not v: print(name, 'no video', str(r)[:300]); return None
    fn = f'raw/{name}.mp4'
    try: open(fn, 'wb').write(urllib.request.urlopen(v, timeout=300).read()); print('saved', fn, os.path.getsize(fn))
    except Exception as e: print(name, 'DOWNLOAD FAIL', v, e)
    return fn
