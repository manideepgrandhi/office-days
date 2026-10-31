#!/usr/bin/env python3
"""Refresh the shared top bar (if ../manideepgrandhi.github.io is checked out) and the CSP hashes.
Usage: python3 build.py [path-to-manideepgrandhi.github.io]"""
import base64, hashlib, os, re, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__)); f = os.path.join(here, 'index.html')
site = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(here), 'manideepgrandhi.github.io')
sync = os.path.join(site, 'scripts', 'sync-mg-shared.py')
if os.path.exists(sync): subprocess.run([sys.executable, sync, f], check=True)
s = open(f, encoding='utf-8').read()
h = lambda body: "'sha256-%s'" % base64.b64encode(hashlib.sha256(body.encode()).digest()).decode()
scripts = [h(m) for m in re.findall(r'<script(?: id="[^"]*")?>(.*?)</script>', s, re.S)]
styles = [h(m) for m in re.findall(r'<style(?: id="[^"]*")?>(.*?)</style>', s, re.S)]
csp = ("default-src 'none'; script-src %s; style-src %s; img-src 'self' data:; manifest-src 'self'; "
       "connect-src https://api.github.com https://manideepgrandhi.github.io/search-index.json; base-uri 'none'; form-action 'none'") % (' '.join(scripts), ' '.join(styles))
s = re.sub(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(")', lambda m: m[1] + csp + m[2], s)
open(f, 'w', encoding='utf-8').write(s); print('CSP updated:', len(scripts), 'scripts,', len(styles), 'styles')
