#!/usr/bin/env python3
"""Independent scalar/FLINT audit of all actual frontier rows.
Author: Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro.
No mathematical arrays are written; all inputs remain temporary.
"""
from pathlib import Path
import gzip, hashlib, json, resource, signal, struct, time
from flint import nmod_mat

ROOT = Path('/tmp/r150-normal-789f-20261116-1040/original-mean-first-frontier127')
OUT = Path('/tmp/isp-root-mean-frontier-full-product-audit-receipt.json')
T0 = time.monotonic()
resource.setrlimit(resource.RLIMIT_AS, (1536 * 1024**2, 1536 * 1024**2))
signal.alarm(150)

def need(value, message):
    if not value:
        raise AssertionError(message)

def h(data):
    return hashlib.sha256(data).hexdigest()

def checked(desc, base=ROOT):
    raw = (base / desc['path']).read_bytes()
    need(len(raw) == desc['bytes'] and h(raw) == desc['sha256'], 'whole physical descriptor')
    if 'logicalSha256' in desc:
        logical = gzip.decompress(raw)
        need(len(logical) == desc['logicalBytes'] and h(logical) == desc['logicalSha256'], 'whole logical descriptor')
        json.loads(logical)
    return raw

raw = (ROOT / 'original-mean-frontier-receipt.json').read_bytes()
need(len(raw) == 25766 and h(raw) == '20405495e04e812ddd06366e1edd300f4cf7d612ccc959eeadb836a9323594ea', 'exact actual raw')
receipt = json.loads(raw)
need(receipt['status'] == 'completed', 'actual completed frontier')
params = receipt['parameters']
manifest_raw = checked(params['manifest'])
need(h(manifest_raw) == '2b2011f80201661ab7b9680aeb86f8f11414244b4adbf21a6fb2728babfa72c9', 'exact complete manifest')
manifest = json.loads(manifest_raw)
for desc in manifest['phases'].values():
    checked(desc)
need(len(manifest['phases']) == 61, 'all source phases')
native = params['nativeWholePrefix']
for key in ('dictionary', 'input', 'checkpoint', 'result', 'receipt', 'log'):
    checked(native[key], ROOT / 'complete-weight7')
data = checked(native['input'], ROOT / 'complete-weight7')
state = checked(native['checkpoint'], ROOT / 'complete-weight7')
need(data[:8] == b'R15PCI01' and state[:8] == b'R15PCS01', 'independent input and state protocols')
version, no, ni, first, prime = struct.unpack_from('<5I', data, 8)
need((version, no, ni, first, prime) == (1, 7754, 312, 282, 127), 'complete original dimensions')
binding = data[28:92]
need(binding.decode() == native['binding'], 'complete native binding')
need(len(data) == 92 + no * ni and all(x < prime for x in data[92:]), 'all original scalar input coefficients')
sv, sno, sni, sf, done, rank, dependent = struct.unpack_from('<7I', state, 8)
need((sv, sno, sni, sf, done, rank, dependent) == (1, no, ni, first, ni, ni, 0), 'all original rows completed, exact rank')
need(state[36:100] == binding, 'same entire state binding')
nw = (no + ni + 31) // 32
stride = 8 + 7 * nw * 4
need(len(state) == 116 + ni * stride, 'whole checkpoint bytes')
qvalues, rvalues, pivots, sources = [], [], [], []
for k in range(ni):
    offset = 116 + k * stride
    pivot, source = struct.unpack_from('<2I', state, offset)
    words = struct.unpack_from('<' + str(7 * nw) + 'I', state, offset + 8)
    values = [sum(((words[b * nw + j // 32] >> (j % 32)) & 1) << b for b in range(7)) for j in range(32 * nw)]
    need(all(v < prime for v in values) and not any(values[no + ni:]), 'canonical complete scalar state and all padding')
    need(pivot < no and source < ni and values[pivot] == 1 and not any(values[:pivot]), 'actual normalized leading coordinate')
    need(values[no + source] != 0 and not any(values[no + source + 1:no + ni]), 'exact original triangular source recipe')
    pivots.append(pivot)
    sources.append(source)
    rvalues.extend(values[:no])
    qvalues.extend(values[no:no + ni])
need(len(set(pivots)) == ni and sorted(sources) == list(range(ni)), 'all distinct actual original unit rows')
X = nmod_mat(ni, no, list(data[92:]), prime)
Q = nmod_mat(ni, ni, qvalues, prime)
R = nmod_mat(ni, no, rvalues, prime)
need(Q * X == R, 'all original source products independently equal every normalized output coordinate')
out = {'format': 'isp-independent-complete-original-mean-frontier-product-audit-v1',
       'author': 'Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro',
       'status': 'completed', 'actualRank': rank, 'originalRows': ni, 'allOutputCoordinates': no,
       'completeOriginalCoordinateProducts': ni * no, 'all61PhysicalAndLogicalPhasesVerified': True,
       'allNativeDescriptorHashesVerified': True, 'allOriginalScalarSourceProductsVerified': True,
       'allUniqueNormalizedPivotsVerified': True, 'nativeBinding': native['binding'],
       'producerBinding': receipt['binding'], 'producerRawSHA256': h(raw),
       'elapsedSeconds': time.monotonic() - T0,
       'peakRssKiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
       'mathematicalArraysWritten': False, 'scope': 'complete finite weight-seven prefix only; no full B-module independence or unit claim'}
OUT.write_text(json.dumps(out, sort_keys=True, separators=(',', ':')) + '\n')
print(json.dumps(out, sort_keys=True))
print(json.dumps({'receiptBytes': OUT.stat().st_size, 'receiptSHA256': h(OUT.read_bytes())}))
