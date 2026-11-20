#!/usr/bin/env python3
"""New R138 two-scalar root-axis consumer; scientific execution is CI-only.

This source has not been scientifically executed. It reads the complete
accepted positive intrinsic/mean rows, all original cubic shards, and the
accepted root germ. It never imports or calls an old target/primitive/ODE
producer. Its new target is the two-scalar support propagation, using
the exact axis cosine-sum definition. No Fourier coefficient array is
published. The separate root-angle helper only materializes the original
definition for direct use inside a future angular consumer.

The exact original interfaces remain in the saved 4650-row partition.
Qrepair is received through its already proved 4e-18 full-state difference.
The whole true root interval is used; no midpoint is treated as the root.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import time

POSITIVE_SHA = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
GERM_SHA = '397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
CANDIDATE_SHA = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT_SHA = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
REPAIR_DEFINITION_SHA = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
ETA = Fraction(-7789843107295549, 4611686018427387904)
NU = Fraction(-2572625729470897, 72057594037927936)
ROOT_LO = Fraction(1191984371497, 5000000000000)
ROOT_HI = Fraction(2383968743003, 10000000000000)
BODY_LEFT = Fraction(1192029371497, 5000000000000)
RIGHT = Fraction(25, 8)
REPAIR = Fraction(4, 10**18)
WORLD_H = Fraction(4347844570122155, 4503599627370496)
KIND = 'R138_same_physical_anchor_true_root_axis_support_v1'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path, expected):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('accepted input byte identity differs: ' + str(path))
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def persist(path, doc):
    raw = (json.dumps(doc, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()
    temp = Path(str(path) + '.partial')
    temp.write_bytes(raw)
    temp.replace(path)
    if Path(path).read_bytes() != raw:
        raise OSError('new result failed exact byte readback')


def load_candidate(path):
    # Pure input restoration/identity checking, not an old numerical producer.
    import numpy as np
    doc = read(path, CANDIDATE_SHA)
    if (doc['kind'] != 'complete_lossless_radial_cubic_shards_v1'
        or doc['coefficient_shape'] != [4, 6144, 65]
        or doc['metadata']['object_sha256'] != OBJECT_SHA):
        raise ValueError('wrong complete original cubic definition')
    nodes, blocks, prior, end = [], [], None, 0
    for part in doc['parts']:
        if Path(part['file']).name != part['file']:
            raise ValueError('candidate shard is not local to the accepted index')
        p = Path(path).parent / part['file']
        raw = p.read_bytes()
        if len(raw) != part['bytes'] or hashlib.sha256(raw).hexdigest() != part['sha256']:
            raise ValueError('original cubic shard bytes differ')
        z = np.load(io.BytesIO(gzip.decompress(raw)), allow_pickle=False)
        r, c = z['radial_nodes'], z['piece_coefficients']
        if (part['first_interval'] != end or len(r) != c.shape[1] + 1
            or c.shape[0] != 4 or c.shape[2] != 65
            or not np.all(np.isfinite(c)) or np.any(np.diff(r) <= 0)):
            raise ValueError('incomplete or nonfinite original cubic shard')
        if prior is not None and r[0].view(np.uint64) != prior.view(np.uint64):
            raise ValueError('original cubic exact interface differs')
        nodes.extend(Fraction.from_float(float(x)) for x in (r if prior is None else r[1:]))
        blocks.append(c)
        prior, end = r[-1], part['last_interval_exclusive']
    cc = np.concatenate(blocks, axis=1)
    if len(nodes) != 6145 or list(cc.shape) != [4, 6144, 65] or end != 6144:
        raise ValueError('complete cubic input was not restored')
    return doc, nodes, cc


def private_root_angular_definition(germ, candidate, nodes, cc, arb):
    """Materialize the exact original definition for an in-process consumer.

    This helper is not called by the axis target. Its returned array is
    private scratch, not a new certificate, output JSON, or published data.
    The angular consumer must separately admit its same original inputs.
    """
    def rat(x):
        x = Fraction(x)
        return arb(x.numerator)/x.denominator
    def ball(rec):
        return arb(rec['lower']).lower().union(arb(rec['upper']).upper())
    alpha = Fraction(candidate['metadata']['exact_float_amplitude'])
    j = 2549
    xr = rat(ROOT_LO-nodes[j]).union(rat(ROOT_HI-nodes[j]))
    uv = []
    for component in range(65):
        value = arb(0)
        for degree in range(4):
            value = value*xr+rat(alpha*Fraction.from_float(float(cc[degree,j,component])))
        uv.append(value)
    ci = germ['complex_intrinsic_coefficients']
    mean = ball(ci['s']['real'])+uv[32]
    # Every coefficient error is bounded by the already paid full A0 repair.
    repair_ball = arb(0, rat(REPAIR))
    u_sin = [x+repair_ball for x in uv[:32]]
    v_cos = [x+repair_ball for x in [mean]+uv[33:]]
    return dict(a=ball(ci['a']['real']),
                b0=ball(ci['beta']['real'])/ball(ci['gamma']['real']),
                mean_v=v_cos[0], u_sine=u_sin, v_cosine=v_cos,
                physical_frequency_factor=4, full_modes=32)


def run(args):
    # No Arb/scientific imports occur during static source inspection.
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise RuntimeError('this new scientific consumer is for the public Actions child')
    from flint import arb, ctx
    ctx.prec = 320
    started = time.monotonic()
    if args.output.exists() and not args.resume:
        raise FileExistsError('preserve the previous new result; use its explicit unfinished resume')
    if args.resume and not args.output.exists():
        raise FileNotFoundError('the requested unfinished checkpoint is absent')
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def rat(x):
        x = Fraction(x)
        return arb(x.numerator) / x.denominator

    def ball(rec):
        return arb(rec['lower']).lower().union(arb(rec['upper']).upper())

    def saved(x):
        if not x.is_finite():
            raise ValueError('nonfinite new scalar')
        token = x.str(100)
        if not arb(token).contains(x):
            raise ValueError('published scalar failed outward readback')
        return {'ball': token}

    def unpack(rec):
        return arb(rec['ball'])

    def euclidean(*xs):
        return sum((abs(x).upper()**2 for x in xs), arb(0)).sqrt().upper()

    positive = read(args.positive, POSITIVE_SHA)
    germ = read(args.germ, GERM_SHA)
    cand, nodes, cc = load_candidate(args.candidate)
    alpha = Fraction(cand['metadata']['exact_float_amplitude'])
    if (not positive['complete'] or not positive['coefficient_cover_complete']
        or positive['failure'] is not None or len(positive['rows']) != 4650
        or positive['identity']['candidate_sha256'] != CANDIDATE_SHA
        or positive['identity']['object_sha256'] != OBJECT_SHA
        or Fraction(positive['identity']['actual_alpha']) != alpha
        or Fraction(positive['identity']['actual_nu']) != NU
        or Fraction(positive['identity']['exact_eta_center']) != ETA
        or not positive['whole_original_eta']):
        raise ValueError('accepted complete positive coefficient scope differs')
    if (not germ['complete'] or not germ['proved'] or germ['failure'] is not None
        or germ['candidate_sha256'] != CANDIDATE_SHA or germ['object_sha256'] != OBJECT_SHA
        or tuple(map(Fraction, germ['root_interval'])) != (ROOT_LO, ROOT_HI)
        or Fraction(germ['exact_amplitude']) != alpha
        or Fraction(germ['actual_fixed_nu']) != NU
        or Fraction(germ['exact_center_parameter']) != ETA
        or not germ['whole_affine_parameter_interval']
        or germ['actual_candidate_piece'] != 2549
        or not germ['compact_bump_identically_zero_on_entire_actual_germ']):
        raise ValueError('accepted true-root germ scope differs')
    radial_domain = tuple(map(Fraction, germ['complex_radial_rectangle']['real_interval']))
    scalar_domain = tuple(map(Fraction, germ['original_scalar_germ']))
    if (not nodes[2549] <= ROOT_LO < ROOT_HI < BODY_LEFT <= nodes[2550]
        or not radial_domain[0] <= ROOT_LO < BODY_LEFT <= radial_domain[1]
        or not scalar_domain[0] <= ROOT_LO < BODY_LEFT <= scalar_domain[1]):
        raise ValueError('the whole true root collar leaves an original germ')
    endpoint = BODY_LEFT
    for row in positive['rows']:
        l, r = map(Fraction, row['interval'])
        j = row['candidate_piece']
        if l != endpoint or not nodes[j] <= l < r <= nodes[j+1]:
            raise ValueError('an original closed row/interface was changed')
        endpoint = r
    if endpoint != RIGHT:
        raise ValueError('original full positive cover does not reach its true endpoint')

    identity = dict(kind=KIND, source_sha256=digest(__file__), positive=POSITIVE_SHA,
                    germ=GERM_SHA, candidate=CANDIDATE_SHA, fixed_point='(0,0,1/2)',
                    eta=str(ETA), actual_nu=str(NU),
                    repair_definition_sha256=REPAIR_DEFINITION_SHA,
                    exact_root_interval=[str(ROOT_LO), str(ROOT_HI)],
                    original_row_count=4650, arithmetic_bits=320,
                    exact_repair_C0=str(REPAIR), original_interfaces_retained=True)
    interfaces = [r['right_interface'] for r in positive['rows'] if r['right_interface'] is not None]
    identity['original_interface_count'] = len(interfaces)
    identity['original_interface_records_sha256'] = hashlib.sha256(
        json.dumps(interfaces, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    gbound = rat(Fraction(222,125) + 16*REPAIR)

    if args.resume:
        doc = json.loads(args.output.read_text())
        if doc['identity'] != identity or doc['complete'] or doc['failure'] is not None:
            raise ValueError('only the same successful incomplete prefix may resume')
        done = doc['completed_original_rows']
        q, s = unpack(doc['nominal_q']), unpack(doc['nominal_s'])
        error = unpack(doc['axis_error']).upper()
        # A coefficient is an exact definition, not a new scientific
        # target. Materialize it privately when its next row is visited.
        cached_piece, axis_poly = -1, []
    else:
        last = positive['rows'][-1]['intrinsic']
        a, beta, gamma, Cr = (ball(last[k]) for k in ('a','beta','gamma','Cref'))
        t, z = beta/gamma, -a*Cr
        if not a > 0 or not t < 0 or not z > 0:
            raise ValueError('the original real outer anchor signs are unresolved')
        hh = rat(WORLD_H-Fraction(1,2))
        qr, sr = a*t+hh*z, a*z-hh*t
        q, s = qr.mid(), sr.mid()
        error = euclidean(qr.rad(), sr.rad())
        done, cached_piece, axis_poly = 0, -1, []
        doc = dict(identity=identity, complete=False, failure=None,
                   completed_original_rows=0, axis_projection_count=0,
                   current_axis_piece=-1,
                   nominal_q=saved(q), nominal_s=saved(s), axis_error=saved(error),
                   old_target_or_primitive_calls=0, old_geometry_ODE_calls=0,
                   scope=dict(same_physical_Qrepair=True, full_root_circle_proved=False,
                              root_mean_denominator_proved=False, positive_inverse_proved=False,
                              final_topic_complete=False))
        persist(args.output, doc)

    rows = positive['rows']
    while done < len(rows):
        row = rows[len(rows)-1-done]
        left, right = map(Fraction, row['interval'])
        piece = row['candidate_piece']
        if piece != cached_piece:
            # New signed AXIS functional, not re-evaluation of 65 old fields.
            axis_poly = [alpha*sum((Fraction.from_float(float(cc[d,piece,k]))
                                   for k in range(33,65)), Fraction(0)) for d in range(4)]
            cached_piece = piece
            if doc['current_axis_piece'] != piece:
                doc['axis_projection_count'] += 1
                doc['current_axis_piece'] = piece
        dx = rat(left-nodes[piece]).union(rat(right-nodes[piece]))
        v_nonmean = arb(0)
        for coeff in axis_poly:
            v_nonmean = v_nonmean*dx+rat(coeff)
        v_axis = ball(row['bounds']['mean_v'])+v_nonmean
        zz = row['intrinsic']
        e = ball(zz['a'])*ball(zz['gamma'])
        curvature = ball(zz['K'])
        if not e > 0 or not curvature > 0 or not v_axis < 0:
            raise ValueError('new closed-row axis denominator/sign unresolved')
        w = e*curvature*v_axis
        ec, wc = e.mid(), w.mid()
        dr = rat(left-right)
        angle = wc*dr
        co, si = angle.cos(), angle.sin()
        if wc.contains(0):
            raise ValueError('body nominal rotation vanished despite the strict signed gate')
        nq = co*q+si*s+ec*si/wc
        ns = -si*q+co*s+ec*(co-1)/wc
        local = (rat(right-left)*(e.rad().upper()+gbound*w.rad().upper())).upper()
        rounding = euclidean(nq.rad(), ns.rad())
        error = (error+local+rounding).upper()
        q, s = nq.mid(), ns.mid()
        done += 1
        if done % 64 == 0 or done == len(rows):
            doc.update(completed_original_rows=done, nominal_q=saved(q),nominal_s=saved(s),
                       axis_error=saved(error), current_axis_piece=cached_piece,
                       current_left=str(left), seconds=time.monotonic()-started)
            persist(args.output, doc)
            # Consume the exact outward checkpoint after publication, before more work.
            q, s = unpack(doc['nominal_q']), unpack(doc['nominal_s'])
            error = unpack(doc['axis_error']).upper()
            print(json.dumps(dict(completed_original_rows=done,current_left=str(left))),flush=True)

    # Actual unknown root is inside the full saved interval, never its midpoint.
    ci = germ['complex_intrinsic_coefficients']
    aa, gg = ball(ci['a']['real']), ball(ci['gamma']['real'])
    if not aa > 0 or not gg > 0:
        raise ValueError('true-root metric positivity was lost')
    emax = (aa.upper()*gg.upper()).upper()
    vmax = ball(germ['moving_v_derivative_Astrip'][0]).upper()
    kmax = abs(ball(ci['K']['real'])).upper()
    collar = (rat(BODY_LEFT-ROOT_LO)*(emax+gbound*emax*kmax*vmax)).upper()
    repair = rat(16*REPAIR)
    total_error = (error+collar+repair).upper()
    q_root = (q-total_error).lower().union((q+total_error).upper())
    s_root = (s-total_error).lower().union((s+total_error).upper())

    doc.update(complete=True, proved=True, completed_original_rows=4650,
               true_root_support_coordinates=dict(q=saved(q_root),s=saved(s_root)),
               complete_axis_error=saved(total_error), root_collar_fee=saved(collar),
               original_root_collar_K_bound=saved(kmax),
               exact_repair_fee=saved(repair),
               same_global_fixed_support_lower='2/5',
               root_axis_q_negative=bool(q_root<0), root_axis_s_positive=bool(s_root>0),
               seconds=time.monotonic()-started)
    persist(args.output,doc)
    print(json.dumps(dict(complete=True,q=q_root.str(20),s=s_root.str(20),
                          axis_error=total_error.str(20),output=str(args.output))),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--positive',type=Path,required=True)
    parser.add_argument('--germ',type=Path,required=True)
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--resume',action='store_true')
    args=parser.parse_args()
    try:
        run(args)
    except Exception as exc:
        if args.output.exists():
            doc=json.loads(args.output.read_text())
            if not doc.get('complete'):
                doc['failure']=dict(type=type(exc).__name__,message=str(exc))
                persist(args.output,doc)
        raise


if __name__=='__main__':
    main()
