#!/usr/bin/env python3
"""Build a local, vendorable release; never deploys or edits consumers."""
from pathlib import Path
import hashlib,json,tarfile,zipfile
root=Path(__file__).resolve().parents[1]
version=(root/'VERSION').read_text().strip()
name=f'uvy-design-v{version}'
out=root/'dist';out.mkdir(exist_ok=True)
paths=[]
for directory in ['assets','icons','vendor','docs']:
 paths += [p for p in (root/directory).rglob('*') if p.is_file()]
paths += [root/p for p in ['VERSION','LICENSE','THIRD_PARTY_NOTICES.txt']]
paths=sorted(paths)
manifest={'version':version,'source':'https://github.com/UnitVectorY-Labs/uvy-design','files':[{'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}
manifest_data=(json.dumps(manifest,indent=2)+'\n').encode()
(out/'asset-manifest.json').write_bytes(manifest_data)
with tarfile.open(out/f'{name}.tar.gz','w:gz') as archive:
 for p in paths:archive.add(p,arcname=f'{name}/{p.relative_to(root)}')
 archive.add(out/'asset-manifest.json',arcname=f'{name}/asset-manifest.json')
with zipfile.ZipFile(out/f'{name}.zip','w',zipfile.ZIP_DEFLATED) as archive:
 for p in paths:archive.write(p,arcname=f'{name}/{p.relative_to(root)}')
 archive.writestr(f'{name}/asset-manifest.json',manifest_data)
sums=[]
for p in [out/f'{name}.tar.gz',out/f'{name}.zip',out/'asset-manifest.json']:
 sums.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}')
(out/'SHA256SUMS').write_text('\n'.join(sums)+'\n')
print(f'Packaged {len(paths)} files for v{version}')
