#!/usr/bin/env python3
"""Keep all eleven old high Green windows before the already paid maximum.

The frozen R50 adapter executes the frozen R33 propagation arithmetic.
This collector adds storage only: no ODE, quadrature, source evaluation,
new frequency window, far-radius change, or nonlinear existence claim.
The exact old maximum, complete pure source, and far columns are checked
by the original R50 finalizer before this certificate can be completed.

Author: geometry_audit (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import sys
import time

from flint import arb, ctx

INPUT_MANIFEST_SHA256 = '5526ca91c916e851b22d9f24cbf8fcdacc0ac9e160836f8099a396d72dc19ef7'
CELLS = tuple(range(12, 225))
PAIR_COUNT = len(CELLS) * (len(CELLS) + 1) // 2
S = Fraction(257, 256)
OLD_WINDOWS = ((94,96),(98,104),(106,112),(114,128),(130,192),
               (194,256),(258,512),(514,1024),(1026,2048),
               (2050,4096),(4098,8190))
REQUESTED_WINDOWS = ((94,94),(96,96),(98,104),(106,112),(114,128),
                     (130,184),(186,192),(194,256),(258,512),
                     (514,1024),(1026,2048),(2050,4096),(4098,8190))
WINDOW_MAP = (0,0,1,2,3,4,4,5,6,7,8,9,10)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for data in iter(lambda: f.read(1048576), b''):
            h.update(data)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with gzip.open(path, 'rt') if path.suffix == '.gz' else path.open() as f:
        return json.load(f)


def exact_envelope(record):
    if record['lower'] != record['upper']:
        raise ValueError('The defined physical envelope must be an exact dyadic')
    p = record['upper']
    value, exponent = Fraction(int(p['mantissa'])), int(p['binary_exponent'])
    return value * (2**exponent if exponent >= 0 else Fraction(1, 2**-exponent))


def write_json(path, doc):
    if path.exists():
        raise FileExistsError(path)
    raw = (json.dumps(doc, indent=2) + '\n').encode()
    if len(raw) >= 1_000_000:
        raise ValueError('Small certificate unexpectedly exceeds one MB')
    path.write_bytes(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frozen', type=Path, required=True)
    parser.add_argument('--input-manifest', type=Path, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--rss-limit-mib', type=int, default=96)
    args = parser.parse_args()
    start = time.monotonic()
    args.frozen = args.frozen.resolve()
    args.out_dir = args.out_dir.resolve()
    if sha(args.input_manifest) != INPUT_MANIFEST_SHA256:
        raise ValueError('Frozen input manifest changed')
    manifest = read(args.input_manifest)
    for path, expected in manifest['inputs'].items():
        if sha(args.frozen/path) != expected:
            raise ValueError('Scientific input changed: '+path)
    for name, expected in manifest['sources'].items():
        if sha(args.frozen/'computations'/name) != expected:
            raise ValueError('Frozen original source changed: '+name)
    if (args.out_dir/'certificate.json').exists():
        raise FileExistsError('Use a fresh output directory')
    args.out_dir.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(args.frozen/'computations'))
    module_path = args.frozen/'computations/tail_middle_frequency_split.py'
    spec = importlib.util.spec_from_file_location('frozen_R50_window_replay', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    from closure_real_head_source_enclosure import exact_q
    from closure_real_head_green_enclosure import ball

    ctx.prec = 192
    qpath = 'notes/2026-11-12-tail-r33-plateau2-density-window.json.gz'
    spath = 'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz'
    qd, sd = read(args.frozen/qpath), read(args.frozen/spath)
    if not all(qd['gates'].values()) or not all(sd['gates'].values()):
        raise ValueError('Unpaid original density or same-strip gate')
    origin = sd['continuous_strip_origin']
    if origin['sha256'] != manifest['inputs'][qpath] or not origin['do_not_renormalize_using_new_strong_density']:
        raise ValueError('Need the identical complete original q strip')
    qr, sr = ({r['cell']:r for r in d['rows']} for d in (qd,sd))
    if tuple(sorted(qr)) != CELLS or tuple(sorted(sr)) != CELLS:
        raise ValueError('Need every original physical cell')
    fields = ('B','Q_coefficient','mu_lower','mu_upper','w_lower',
              'normalized_width_upper','TV_log_w_upper','beta_integral_upper',
              'eta_integral_upper','tau_inner','tau_outer','certified_reference_tau',
              'reference_tau','minimum_strip_buffer')
    identity_gates = 0
    for n in CELLS:
        for key in fields:
            if any(qr[n][key][endpoint] != sr[n][key][endpoint] for endpoint in ('lower','upper')):
                raise ValueError(f'Changed source geometry/strip: {n}/{key}')
            identity_gates += 1
    sigma = {n:exact_envelope(sr[n]['canonical_total_envelope'])/
               exact_envelope(qr[n]['canonical_total_envelope']) for n in CELLS}
    if any(v <= 0 for v in sigma.values()):
        raise ValueError('Positive defined rescaling required')
    del qd, sd, qr, sr

    files = []
    sample_edges = {}
    counts = {'stored_positive_entries':0, 'upward_rounding':0,
              'complete_band_triangles':0, 'saved_array_readback':0}
    Base = module.SplitCollector

    class KeepWindows(Base):
        def __init__(self, bands):
            super().__init__(bands)
            self.band = None
            self.count = 0
            self.output = self.raw_output = None
            self.seen = set()

        def close_band(self):
            if self.output is None:
                return
            self.output.write(b']}\n')
            self.output.close()
            self.raw_output.close()
            if self.count != PAIR_COUNT or len(self.seen) != PAIR_COUNT:
                raise ValueError('Incomplete original causal triangle')
            path = args.out_dir/f'window-{self.band:02d}.json.gz'
            if path.stat().st_size >= 5_000_000:
                raise ValueError('Single-file size limit')
            files.append(dict(index=self.band, first_mode=OLD_WINDOWS[self.band][0],
                              last_mode=OLD_WINDOWS[self.band][1], path=path.name,
                              bytes=path.stat().st_size, sha256=sha(path), entries=self.count))
            counts['complete_band_triangles'] += 1
            self.output = self.raw_output = None
            self.seen.clear()

        def start_band(self, band):
            self.close_band()
            if band != len(files):
                raise ValueError('Original comparison-window order changed')
            path = args.out_dir/f'window-{band:02d}.json.gz'
            if path.exists():
                raise FileExistsError(path)
            self.band, self.count = band, 0
            self.raw_output = path.open('wb')
            self.output = gzip.GzipFile(filename='', fileobj=self.raw_output, mode='wb', mtime=0)
            header = dict(schema='original-inner-single-comparison-window-Gamma-v1',
                          index=band, comparison_window=list(OLD_WINDOWS[band]),
                          columns=['output_cell','source_cell','upper_mantissa','binary_exponent'],
                          norm='Vprime=S*Vstrong, original continuous tau_q, strong Fourier mass',
                          scale='S*sigma_source^2/sigma_output', S=[257,256],
                          upper_significand_bits=64, input_manifest_sha256=INPUT_MANIFEST_SHA256)
            self.output.write(json.dumps(header,separators=(',',':'))[:-1].encode()+b',"entries":[')

        def record(self, n, j, band, value):
            super().record(n,j,band,value)
            if band != self.band:
                self.start_band(band)
            if not 12 <= n <= j <= 224 or (n,j) in self.seen:
                raise ValueError('Wrong or repeated causal source/target')
            self.seen.add((n,j))
            # The scale is exact rational, then enclosed once by Arb.
            factor = S*sigma[j]**2/sigma[n]
            v = (exact_q(factor)*value).upper()
            stored = module.compact_upper(v,bits=64)
            if not value > 0 or not v > 0 or not ball(stored) >= v:
                raise ArithmeticError('Positive kernel or upward rounding failed')
            p = stored['upper']
            entry = [n,j,p['mantissa'],p['binary_exponent']]
            if self.count:
                self.output.write(b',')
            self.output.write(json.dumps(entry,separators=(',',':')).encode())
            self.count += 1
            counts['stored_positive_entries'] += 1
            counts['upward_rounding'] += 1
            if (n,j) in ((12,12),(12,13),(12,14),(12,15),(13,13),(13,14)):
                sample_edges[f'{band}:{n}:{j}'] = entry[2:]
            if self.count % 2048 == 0:
                module.resource_check('retain-window-entries',band=band,entries=self.count)

        def finish(self, replay_args, hashes, densityhash, original_gamma, original_far,
                   started, base_source_hash):
            self.close_band()
            # Unchanged old routine: exact identity for all 22,791 maxima,
            # all complete far columns, and all complete pure-source cells.
            super().finish(replay_args,hashes,densityhash,original_gamma,original_far,
                           started,base_source_hash)

    module.SplitCollector = KeepWindows
    original_cwd = Path.cwd()
    original_argv = sys.argv
    names = {
      'density':qpath,
      'positive':'notes/2026-11-12-closure-positive-highband-38.json.gz',
      'subhead':'notes/2026-11-12-closure-middle-high-subhead24.json.gz',
      'local':'notes/2026-11-12-tail-r33-plateau2-middle-local-homogeneous.json.gz',
      'hybrid':'notes/2026-11-12-tail-r33-plateau2-middle-hybrid-density.json.gz',
      'ready':'notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json',
      'extra-positive':'notes/2026-11-12-closure-middle-high-subhead16to23.json.gz',
      'wide-low':'notes/2026-11-12-tail-r33-plateau2-middle-wide-low-density.json.gz',
      'original-middle':'notes/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz',
      'reference-high':'notes/2026-11-12-tail-r33-plateau2-quadratic-high-recovered-r1.json',
    }
    replay_out = args.out_dir/'original-split-replay.json.gz'
    sys.argv = [str(module_path)]
    for name,path in names.items():
        sys.argv += ['--'+name,path]
    sys.argv += ['--out',str(replay_out),'--resource-out',str(args.out_dir/'original-replay-resource.json'),
                 '--rss-limit-mib',str(args.rss_limit_mib),'--z-log2','-2200']
    try:
        os.chdir(args.frozen)
        module.main()
    finally:
        os.chdir(original_cwd)
        sys.argv = original_argv

    old = module.metadata_without_array(replay_out,'gamma_rows')
    if not old['original_kernel_identity_bitwise'] or not old['original_far_and_pure_identity_bitwise']:
        raise ValueError('The original exact identity was not paid')
    if old['original_kernel_identity_count'] != PAIR_COUNT or len(files) != 11:
        raise ValueError('Incomplete original replay')
    for info in files:
        path = args.out_dir/info['path']
        if sha(path) != info['sha256']:
            raise ValueError('Saved kernel drift')
        seen = set()
        for n,j,m,e in module.iter_array(path,'entries'):
            if not 12 <= n <= j <= 224 or (n,j) in seen or int(m) <= 0 or int(m).bit_length() > 64:
                raise ValueError('Invalid saved positive causal row')
            seen.add((n,j))
            counts['saved_array_readback'] += 1
        if len(seen) != PAIR_COUNT:
            raise ValueError('Saved coverage lost a source/target')
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if peak > args.rss_limit_mib*1024:
        raise MemoryError('Resource gate exceeded')
    cert = dict(schema='original-inner-eleven-window-Gamma-replay-v1',
        status='All original maxima reproduced, all eleven positive comparison kernels retained',
        original_kernel_identity_count=PAIR_COUNT,original_maximum_bitwise_identity=True,
        original_complete_far_and_pure_identity=True,new_ODE_integrations=0,
        new_source_integrations=0,new_radial_quadratures=0, original_continuous_strip_unchanged=True,
        source_g_does_not_change=True, complete_mean_inverse_and_far_not_removed=True,
        nonlinear_existence_or_joint_contraction_claimed=False,
        matrix_convention='Only source>=target is nonzero for this initial-value high Green map',
        input_material='Common weak Fourier source dprime=Vprime^2/(r*w)+abs(w_r/w)*Vprime^2/w',
        output_norm='sum_m (1+m) sup_cell exp(m*tau_q(r))*(B*abs(p_m)+abs(kappa_m))/Vprime',
        coefficient_already_included='Original factor 2 for separated component radial sup; no DQ/source polynomial coefficient',
        Vprime_scale=[257,256], original_nu='m^2*(m^2-1)/12', original_mu_interface='rho=2^(11/4)',
        defined_sigma=[dict(cell=n,numerator=str(sigma[n].numerator),denominator=str(sigma[n].denominator))for n in CELLS],
        files=files, requested_window_restrictions=[dict(window=list(w),saved_window_index=i,
            rule='Restrict the unchanged original comparison window; no single-mode recomputation')
            for w,i in zip(REQUESTED_WINDOWS,WINDOW_MAP)],
        counts=counts, geometry_and_strip_identity_gates=identity_gates,
        sample_edges=sample_edges,input_manifest_sha256=INPUT_MANIFEST_SHA256,
        inputs=manifest['inputs'],frozen_sources=manifest['sources'],source_sha256=sha(Path(__file__)),
        original_replay_sha256=sha(replay_out),elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=peak,
        storage='The eleven inexpensive derived window files stay in scratch; source, pins, exact schema and SHA values reproduce them.')
    write_json(args.out_dir/'certificate.json',cert)
    print(json.dumps(dict(status='complete',certificate=str(args.out_dir/'certificate.json'),
        sha256=sha(args.out_dir/'certificate.json'),original_maximum_identity_count=PAIR_COUNT,
        entries=counts['stored_positive_entries'],elapsed_seconds=cert['elapsed_seconds'],peak_RSS_KiB=peak)),flush=True)


if __name__ == '__main__':
    main()
