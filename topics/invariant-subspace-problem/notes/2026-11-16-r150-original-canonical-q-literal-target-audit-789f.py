#!/usr/bin/env python3
"""Independent original pencil normalization and four literal finite nonmemberships.
Author: Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro.
Uses ordinary Python arithmetic, no producer or native functions and no new elimination.
"""
from pathlib import Path
import gzip, hashlib, json, resource, signal, struct, time

started = time.monotonic()
signal.alarm(60)
ROOT = Path('/tmp/literature_bell_rank4_789f/original-canonical-mean-quadrics-bounded-rhs127')
PARENT = Path('/tmp/r150-normal-789f-20261116-1040')
OUT = Path('/tmp/isp-root-canonical-q-literal-target-audit-receipt.json')

def need(b, s):
    if not b:
        raise AssertionError(s)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def checked(p, d):
    b = p.read_bytes()
    need(len(b) == d['bytes'] and sha(b) == d['sha256'], 'complete original bytes: ' + p.name)
    return b

def phase(folder, d):
    b = gzip.decompress(checked(folder / d['path'], d))
    need(len(b) == d['logicalBytes'] and sha(b) == d['logicalSha256'], 'complete logical phase')
    return json.loads(b)

canon = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('ascii')
raw = (ROOT / 'canonical-mean-quadrics-bounded-rhs-receipt.json').read_bytes()
need(len(raw) == 6588 and sha(raw) == '1688af057845a567db2a9fa57f3ad6fc7efd129e1634ad1f8b546eae14a0c143', 'actual complete target run')
rec = json.loads(raw)
man = json.loads(checked(ROOT / rec['parameters']['manifest']['path'], rec['parameters']['manifest']))
need(sha(canon(man['semantic'])) == man['binding'] == rec['binding'], 'semantic source binding')
model = PARENT / 'original-ten-parameter-module127-v2'
mm = json.loads(checked(model / 'original-parameter-module-manifest.json', {'bytes':30466, 'sha256':'9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2'}))
md = mm['phases']['complete-original-ten-parameter-action127']
base = phase(model, md)
need(base['binding'] == '7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4', 'literal original model')
T = base['data']['allFourOriginalMeanMatrices']
need(len(T) == 4 and all(len(t) == 6 and all(len(r) == 6 for r in t) for t in T), 'all original symmetric matrices')
need(all(T[k][i][j] == T[k][j][i] and 0 <= T[k][i][j] < 127 for k in range(4) for i in range(6) for j in range(6)), 'all original symmetric coefficients')
U = [[T[k][0][i] for k in range(4)] for i in range(4)]
A = [row[:] + [int(i == j) for j in range(4)] for i,row in enumerate(U)]
det = 1
for c in range(4):
    r = next((i for i in range(c,4) if A[i][c]), None)
    need(r is not None, 'actual fixed original unit')
    if r != c:
        A[c], A[r] = A[r], A[c]
        det = -det
    v = A[c][c]
    det = det * v % 127
    A[c] = [x * pow(v,-1,127) % 127 for x in A[c]]
    for i in range(4):
        if i != c:
            v = A[i][c]
            A[i] = [(x-v*y) % 127 for x,y in zip(A[i],A[c])]
V = [row[4:] for row in A]
need(det == 74, 'independent literal determinant')
need(all(sum(U[i][k]*V[k][j] for k in range(4)) % 127 == int(i==j) and sum(V[i][k]*U[k][j] for k in range(4)) % 127 == int(i==j) for i in range(4) for j in range(4)), 'all independent inverse products')
Tp = [[[sum(T[k][i][j]*V[k][a] for k in range(4)) % 127 for j in range(6)] for i in range(6)] for a in range(4)]
np = phase(ROOT, rec['parameters']['canonicalQuadrics'])
need(np['binding'] == rec['binding'], 'same complete normalization')
n = np['data']
need(n['unit'] == U and n['inverse'] == V and n['allFourOriginalMatrices'] == T and n['allFourCanonicalMatrices'] == Tp, 'every actual original and normalized coefficient')
quadrics = []
for a in range(4):
    q = {}
    for i in range(6):
        for j in range(6):
            e = [0]*17
            e[i] += 1; e[j] += 1
            e = tuple(e)
            q[e] = (q.get(e,0) + Tp[a][i][j]) % 127
    q = {e:c for e,c in q.items() if c}
    packed = [[list(e),c] for e,c in sorted(q.items())]
    need(packed == n['allFourCanonicalQuadrics'][a], 'entire independently normalized ordinary quadratic')
    quadrics.append(q)
nd = PARENT / 'original-complete-weight8-frontier127' / 'complete-weight8'
spec = man['semantic']['completeParentStates']['8']
dictionary = json.loads(checked(nd / 'complete-original-dictionaries.json', spec['dictionary']))
orig = checked(nd / 'complete-row-result.bin', spec['result'])
checked(nd / 'all-original-row-input.bin', spec['input'])
checked(nd / 'complete-row-state.bin', spec['checkpoint'])
need(orig[:8] == b'R15PCR01' and struct.unpack_from('<7I', orig,8) == (1,17674,1386,1286,1386,1312,74), 'paid complete rank1312 classification')
pivots = [struct.unpack_from('<2I',orig,116+8*i)[0] for i in range(1312)]
need(len(set(pivots)) == 1312, 'all paid unit-minor coordinates')
lookup = {(axis,tuple(e)):i for i,(axis,e) in enumerate(dictionary['outputs'])}
need(len(lookup) == 17674, 'complete original output dictionary')
native = man['native']['8']; run = ROOT / 'weight8-rhs'
ti = checked(run/native['input']['path'],native['input'])
ro = checked(run/native['result']['path'],native['result'])
need(ti[:8] == b'R15RHI01' and ro[:8] == b'R15RHO01', 'literal target protocols')
need(struct.unpack_from('<6I',ti,8) == struct.unpack_from('<6I',ro,8) == (1,17674,1386,4,127,1312), 'all four complete targets')
need(ti[32:96] == ro[32:96] == spec['nativeBinding'].encode() and ti[96:160] == ro[96:160] == rec['binding'].encode(), 'both exact bindings')
off = 160
counts = []
for k,q in enumerate(quadrics):
    target = {}
    for e,c in q.items():
        for i in range(6):
            for j in range(6):
                ee = list(e)
                ee[i] += 1; ee[6+i] += 1
                ee[j] += 1; ee[6+j] += 1
                ee = tuple(ee)
                target[ee] = (target.get(ee,0)+c) % 127
    vector = bytearray(17674)
    for e,c in target.items():
        if c:
            need(not any(e[12:]), 'only original parameter variables')
            vector[lookup[(0,e[:12])]] = c
    literal = ti[160+k*17674:160+(k+1)*17674]
    nz = struct.unpack_from('<I',ro,off)[0]; off += 4
    residual = ro[off:off+17674]; off += 17674
    coefficients = ro[off:off+1386]; off += 1386
    need(bytes(vector) == literal == residual, 'all literal independently rebuilt target and residual coordinates')
    need(not any(coefficients), 'all original source coefficients are actually zero')
    need(not any(vector[p] for p in pivots), 'all1312 paid original unit-minor coordinates vanish')
    need(sum(v!=0 for v in vector) == nz and nz > 0, 'actual nonzero full target')
    counts.append(nz)
need(off == len(ro) and len(ti) == 160+4*17674, 'whole target and result EOF')
out = {'format':'r150-independent-original-canonical-q-literal-target-audit-v1',
       'author':'Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro', 'status':'completed',
       'normalizationDeterminant127':det, 'allFourQuadricsRebuiltFromOriginalMatrices':True,
       'allOriginalTargetAndResidualCoordinates':70696, 'allOriginalSourceCoefficientsZero':True,
       'all1312OriginalUnitMinorCoordinatesVanishForEachTarget':True,
       'targetNonzeroCounts':counts, 'paidWholeParentRank':1312,
       'negativeReason':'The paid rank1312 original unit minor makes restriction to its1312 coordinates injective on the complete source space; each nonzero target restricts to zero.',
       'binding':rec['binding'], 'elapsedSeconds':time.monotonic()-started,
       'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
       'scope':'Fixed complete weight8 source space only; no full ideal or characteristic-zero conclusion.',
       'mathematicalArraysWritten':False}
OUT.write_bytes(canon(out)+b'\n')
print(json.dumps(out,sort_keys=True))
print(json.dumps({'receiptBytes':OUT.stat().st_size,'receiptSHA256':sha(OUT.read_bytes())}))
