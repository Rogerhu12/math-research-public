#!/usr/bin/env python3
"""Independent literal scalar audit of seven completed original F127 targets.
Author: Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro.
Read-only mathematical inputs; no source or residual arrays are written.
"""
from pathlib import Path
import hashlib, json, resource, signal, struct, time
from flint import nmod_mat

started = time.monotonic()
resource.setrlimit(resource.RLIMIT_AS, (1536 * 1024**2,) * 2)
signal.alarm(180)
ROOT = Path('/tmp/literature_bell_rank4_789f/original-rank-four-bounded-rhs127')
PARENT = Path('/tmp/r150-normal-789f-20261116-1040')
OUT = Path('/tmp/isp-root-bounded-rhs-full-product-audit-receipt.json')

def need(b, s):
    if not b:
        raise AssertionError(s)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def checked(p, d):
    b = p.read_bytes()
    need(len(b) == d['bytes'] and sha(b) == d['sha256'], 'whole literal file: ' + p.name)
    return b

raw = (ROOT / 'rank-four-bounded-rhs-receipt.json').read_bytes()
need(len(raw) == 6587 and sha(raw) == '48fcfcbf7b2f482c11c82927eef843d1c219805c1f564294fecef179637863ed', 'entire actual receipt')
actual = json.loads(raw)
need(actual['status'] == 'completed-diagnostic', 'actual complete diagnostic')
manifest = json.loads(checked(ROOT / actual['parameters']['manifest']['path'], actual['parameters']['manifest']))
canon = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('ascii')
need(sha(canon(manifest['semantic'])) == actual['binding'] == manifest['binding'], 'whole semantic binding')
counts, products = {}, 0
for degree, folder, no, ni, nrank, nt in [
    (7, 'original-mean-first-frontier127', 7754, 312, 312, 1),
    (8, 'original-complete-weight8-frontier127', 17674, 1386, 1312, 6),
]:
    spec = manifest['semantic']['completeParentStates'][str(degree)]
    pd = PARENT / folder / ('complete-weight' + str(degree))
    inp = checked(pd / 'all-original-row-input.bin', spec['input'])
    original = checked(pd / 'complete-row-result.bin', spec['result'])
    checked(pd / 'complete-row-state.bin', spec['checkpoint'])
    checked(pd / 'complete-original-dictionaries.json', spec['dictionary'])
    need(inp[:8] == b'R15PCI01' and struct.unpack_from('<5I', inp, 8) == (1, no, ni, spec['first'], 127), 'exact original input protocol')
    need(len(inp) == 92 + no * ni and all(v < 127 for v in inp[92:]), 'all canonical original scalars')
    need(original[:8] == b'R15PCR01', 'original rank-result protocol')
    need(struct.unpack_from('<7I', original, 8)[:6] == (1, no, ni, spec['first'], ni, nrank), 'complete original source classification')
    pivots = [struct.unpack_from('<2I', original, 116 + 8 * i)[0] for i in range(nrank)]
    need(len(set(pivots)) == nrank, 'all distinct actual pivots')
    nd = ROOT / ('weight' + str(degree) + '-rhs')
    d = manifest['native'][str(degree)]
    ti = checked(nd / d['input']['path'], d['input'])
    ro = checked(nd / d['result']['path'], d['result'])
    need(ti[:8] == b'R15RHI01' and ro[:8] == b'R15RHO01', 'independent RHS protocols')
    need(struct.unpack_from('<6I', ti, 8) == struct.unpack_from('<6I', ro, 8) == (1, no, ni, nt, 127, nrank), 'all literal dimensions')
    need(ti[32:96].decode() == ro[32:96].decode() == spec['nativeBinding'], 'whole parent binding')
    need(ti[96:160].decode() == ro[96:160].decode() == actual['binding'], 'whole target binding')
    need(len(ti) == 160 + nt * no, 'literal RHS EOF')
    targets, residuals, coefficients, nzs = [], [], [], []
    off = 160
    for k in range(nt):
        nz = struct.unpack_from('<I', ro, off)[0]
        off += 4
        residual = list(ro[off:off + no]); off += no
        coeff = list(ro[off:off + ni]); off += ni
        target = list(ti[160 + k * no:160 + (k + 1) * no])
        need(len(residual) == len(target) == no and len(coeff) == ni, 'all source and output coordinates')
        need(all(v < 127 for v in residual + coeff + target), 'all canonical field coefficients')
        need(sum(v != 0 for v in residual) == nz and nz > 0, 'actual nonzero full residual')
        need(all(residual[p] == 0 for p in pivots), 'all actual pivot residuals vanish')
        targets.extend(target); residuals.extend(residual); coefficients.extend(coeff); nzs.append(nz)
    need(off == len(ro), 'full result exact EOF')
    X = nmod_mat(ni, no, list(inp[92:]), 127)
    Q = nmod_mat(nt, ni, coefficients, 127)
    R = nmod_mat(nt, no, residuals, 127)
    T = nmod_mat(nt, no, targets, 127)
    need(Q * X + R == T, 'every original scalar target = source + residual product')
    counts[str(degree)] = nzs
    products += nt * no
    del X, Q, R, T, inp
need(products == 113798, 'all seven original target products')
out = {'format': 'r150-independent-bounded-original-rhs-full-product-audit-v1',
       'author': 'Astra-ISP-789f / root; AI-assisted GPT-6 Astra Pro',
       'status': 'completed', 'allOriginalCoordinateProducts': products,
       'allOriginalPivotResidualsZero': True, 'residualNonzeroCounts': counts,
       'producerBinding': actual['binding'], 'producerRawSHA256': sha(raw),
       'elapsedSeconds': time.monotonic() - started,
       'peakRssKiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
       'mathematicalArraysWritten': False,
       'scope': 'Only the two specified complete finite source spaces; no full-ideal nonmembership.'}
OUT.write_bytes(canon(out) + b'\n')
print(json.dumps(out, sort_keys=True))
print(json.dumps({'receiptBytes': OUT.stat().st_size, 'receiptSHA256': sha(OUT.read_bytes())}))
