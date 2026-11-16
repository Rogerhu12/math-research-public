#!/usr/bin/env python3
"""Independent literal minor and whole-kernel audit for the completed F127 frontier.
Author: Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro.
Temporary mathematical input is read only; no arrays are written.
"""
from pathlib import Path
import gzip, hashlib, json, resource, signal, struct, time
from flint import nmod_mat

ROOT = Path('/tmp/r150-normal-789f-20261116-1040/original-complete-weight8-frontier127')
NATIVE = ROOT / 'complete-weight8'
OUT = Path('/tmp/isp-root-weight8-full-rank-audit-receipt.json')
started = time.monotonic()
resource.setrlimit(resource.RLIMIT_AS, (1536 * 1024**2, 1536 * 1024**2))
signal.alarm(240)

def need(value, message):
    if not value:
        raise AssertionError(message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def checked(desc, root=ROOT):
    data = (root / desc['path']).read_bytes()
    need(len(data) == desc['bytes'] and digest(data) == desc['sha256'], 'whole stored descriptor')
    if 'logicalSha256' in desc:
        decoded = gzip.decompress(data)
        need(len(decoded) == desc['logicalBytes'] and digest(decoded) == desc['logicalSha256'], 'whole logical descriptor')
        json.loads(decoded)
    return data

raw = (ROOT / 'complete-weight8-frontier-receipt.json').read_bytes()
need(len(raw) == 73556 and digest(raw) == '10c6ba5e961b9b1c06e87589df34ebaadfd227486725b8d4dda0b6a29f439804', 'exact complete actual receipt')
actual = json.loads(raw)
need(actual['status'] == 'completed', 'complete actual producer')
par = actual['parameters']
manifest_bytes = checked(par['manifest'])
need(len(manifest_bytes) == 73953 and digest(manifest_bytes) == '08254a15dbbf01c44fc53ee4e88d8dfd7b5f8b815ee377dd30167547df6b68d1', 'exact full actual manifest')
manifest = json.loads(manifest_bytes)
need(manifest['binding'] == actual['binding'], 'same source binding')
need(len(manifest['phases']) == 201, 'all source and relation phases')
for desc in manifest['phases'].values():
    checked(desc)
native = par['nativeWholePrefix']
for key in ('dictionary', 'input', 'checkpoint', 'result', 'receipt', 'log'):
    checked(native[key], NATIVE)
data = checked(native['input'], NATIVE)
result = checked(native['result'], NATIVE)
need(data[:8] == b'R15PCI01' and result[:8] == b'R15PCR01', 'complete independent binary protocols')
version, no, ni, first, prime = struct.unpack_from('<5I', data, 8)
need((version, no, ni, first, prime) == (1, 17674, 1386, 1286, 127), 'all literal original dimensions')
binding = data[28:92]
need(binding.decode() == native['binding'], 'same native binding')
need(len(data) == 92 + no * ni and all(x < prime for x in data[92:]), 'all original scalar inputs canonical')
rv, rno, rni, rf, done, rank, nd = struct.unpack_from('<7I', result, 8)
need((rv, rno, rni, rf, done, rank, nd) == (1, no, ni, first, ni, 1312, 74), 'complete returned classification')
need(result[36:100] == binding, 'same full result binding')
offset = 116
pivots, sources = [], []
for k in range(rank):
    pivot, source = struct.unpack_from('<2I', result, offset)
    offset += 8
    need(pivot < no and source < ni, 'literal original row and output column')
    pivots.append(pivot)
    sources.append(source)
need(len(set(pivots)) == len(set(sources)) == rank, 'distinct original minor indices')
relations, targets = [], []
for k in range(nd):
    target = struct.unpack_from('<I', result, offset)[0]
    offset += 4
    coefficients = list(result[offset:offset + ni])
    offset += ni
    need(len(coefficients) == ni and all(x < prime for x in coefficients), 'complete canonical source relation')
    need(first <= target < ni and coefficients[target] == 1 and not any(coefficients[target + 1:]), 'unit original target and only earlier sources')
    targets.append(target)
    relations.extend(coefficients)
need(offset == len(result), 'entire result consumed')
need(len(set(targets)) == nd and set(sources).isdisjoint(targets) and sorted(sources + targets) == list(range(ni)), 'all original input rows exactly classified')
need(set(range(first)).issubset(sources), 'all 1286 original prefix rows are retained')
minor_values = [data[92 + row * no + col] for row in sources for col in pivots]
minor = nmod_mat(rank, rank, minor_values, prime)
minor_det = int(minor.det())
need(minor_det != 0, 'independent literal original rank1312 minor is a field unit')
del minor, minor_values
X = nmod_mat(ni, no, list(data[92:]), prime)
K = nmod_mat(nd, ni, relations, prime)
product = K * X
need(product == nmod_mat(nd, no, [0] * (nd * no), prime), 'all 74 complete original kernel products independently vanish')
need(K.rank() == nd, 'all 74 actual original kernel rows independent')
out = {'format': 'isp-independent-complete-original-weight8-rank-and-kernel-audit-v1',
       'author': 'Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro',
       'status': 'completed', 'actualRank': rank, 'originalInputRows': ni,
       'allOutputCoordinates': no, 'all201PhysicalAndLogicalPhasesVerified': True,
       'allNativeDescriptorHashesVerified': True, 'literalOriginalMinorSize': rank,
       'literalOriginalMinorDeterminant127': minor_det,
       'wholeIndependentKernelDimension': nd, 'completeKernelCoordinateProducts': nd * no,
       'all1286PrefixRowsIndependent': True, 'retainedNewRows': rank - first,
       'producerBinding': actual['binding'], 'nativeBinding': native['binding'],
       'producerRawSHA256': digest(raw), 'elapsedSeconds': time.monotonic() - started,
       'peakRssKiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
       'mathematicalArraysWritten': False,
       'scope': 'complete original finite weight8 space only; no full stable-module or unit claim'}
OUT.write_text(json.dumps(out, sort_keys=True, separators=(',', ':')) + '\n')
print(json.dumps(out, sort_keys=True))
print(json.dumps({'receiptBytes': OUT.stat().st_size, 'receiptSHA256': digest(OUT.read_bytes())}))
