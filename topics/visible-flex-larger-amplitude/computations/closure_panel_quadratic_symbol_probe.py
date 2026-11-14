#!/usr/bin/env python3
"""True one-cell quadratic derivative columns with two radial materials.

The reference Fourier centre and input/output frequencies are explicit.
This is a diagnostic column of the exact quadratic principal part, not a
claim about the full mean/denominator remainder or a complete contraction.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_green_enclosure import load_json, ball, maximum
from closure_real_head_source_enclosure import ball_record
from closure_weighted_panel_low_green_v3 import physical_caps


def sha(raw): return hashlib.sha256(raw).hexdigest()


def rec(x):
    d = ball_record(x)
    return {k: d[k] for k in ('lower', 'upper')}


def integrate_ordered(parents, ph, ps, phi, psi, weights, mu_ratio):
    iphi = [(q[0]*v).upper() for q, v in zip(phi, weights)]
    ipsi = [(q[0]*v).upper() for q, v in zip(psi, weights)]
    suffix = [arb(0)]*(len(parents)+1)
    for j in range(len(parents)-1, -1, -1): suffix[j] = (suffix[j+1]+ipsi[j]).upper()
    prefix = arb(0); pmax = arb(0); kmax = arb(0)
    for j in range(len(parents)):
        prefix = (prefix+iphi[j]).upper()
        pmax = maximum(pmax, ph[j][0]*suffix[j]+ps[j][0]*prefix)
        kmax = maximum(kmax, ph[j][1]*suffix[j]+ps[j][1]*prefix)
    return dict(diagonal=rec((mu_ratio*(pmax+kmax)).upper()),
        weighted_phi_source=rec(prefix), weighted_psi_source=rec(suffix[0]))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('mode-packet', 'centre-packet', 'material', 'density', 'columns', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    args = p.parse_args(); ctx.prec = 192; started = time.monotonic()
    docs = {}; hashes = {}
    for name in ('mode_packet', 'centre_packet', 'material', 'density', 'columns'):
        path = getattr(args, name); docs[name], raw = load_json(path); hashes[str(path)] = sha(raw)
    D = docs['mode_packet']; C = docs['centre_packet']; P = docs['material']; N = docs['density']
    if len(D['rows']) != 1 or len(C['rows']) != 1: raise ValueError('A one-mode panel export is required')
    if D['cell'] != C['cell'] or D['cell'] != P['cell']: raise ValueError('Cells differ')
    for packet in (D, C):
        if hashes[str(args.material)] not in packet['input_hashes'].values():
            raise ValueError('Panel source package changed')
        if hashes[str(args.density)] not in packet['input_hashes'].values():
            raise ValueError('Physical envelope differs')
    row = D['rows'][0]; centre = C['rows'][0]; m = row['mode']; a = centre['mode']
    pp = row['panel_export']; cp = centre['panel_export']
    if not pp or len(pp) != len(cp) or len(pp) != len(P['panels']):
        raise ValueError('The source panel order is incomplete')
    density = next(r for r in N['rows'] if r['cell'] == D['cell'])
    X = ball(density['canonical_total_envelope']); B = ball(density['B'])
    qcoef = ball(density['Q_coefficient']); mu = ball(density['mu_lower']).union(ball(density['mu_upper']))
    mu_bar = ball(density['mu_upper']); root = arb(12).sqrt()
    qcut = abs(ball(next(r for r in docs['columns']['endpoint_rows'] if r['mode'] == a)['reference_Q'])).upper()
    parents = []; phi = []; psi = []; ph = []; ps = []; symbols = []
    for i, (mrow, crow, raw) in enumerate(zip(pp, cp, P['panels'])):
        if (mrow['segment'],mrow['x_left'],mrow['x_right']) != (crow['segment'],crow['x_left'],crow['x_right']):
            raise ValueError('Fundamental columns have different panel orders')
        parent = dict(radius=ball(mrow['radius']), w=ball(mrow['w']), tau=ball(mrow['tau']))
        if ball(mrow['tau']).lower() != ball(crow['tau']).lower() or ball(mrow['tau']).upper() != ball(crow['tau']).upper():
            raise ValueError('Mode and centre strips differ')
        parents.append(parent)
        phi.append((ball(mrow['phi_Q']), ball(mrow['phi_Xi'])))
        psi.append((ball(mrow['psi_Q']), ball(mrow['psi_Xi'])))
        ph.append(physical_caps(parent, *phi[-1], m, X, B, qcoef, mu, mu_bar))
        ps.append(physical_caps(parent, *psi[-1], m, X, B, qcoef, mu, mu_bar))
        r = parent['radius']; w = parent['w']; V = ball(raw['V'])
        fQ = r.upper()**3/V.lower()
        fXi = root*mu.upper()/(r.lower()**4*w.lower()*V.lower())
        Q = ball(crow['phi_Q'])*qcut; Xi = ball(crow['phi_Xi'])*qcut
        # These are full cosine/sine amplitudes.  Each signed complex
        # centre coefficient is one half.  Its half cancels the factor2
        # in D(quadratic), separately for each shift m=b +/- a.
        U2 = (a*a*fQ*Q+fXi*Xi).upper()
        S = (a*a*fQ*Q).upper(); T = (a*fQ*Q).upper()
        A = (a*((a*a-1)*fQ*Q+fXi*Xi)).upper()
        # Exact identity C=u2+partial_theta u1/B=fXi*Xi: do not
        # introduce an artificial Q contribution by a triangle bound.
        Cc = (fXi*Xi).upper()
        material_factor = (r.upper()**4*V.upper()**2/(root*mu.lower())).upper()
        Jrad = (material_factor*ball(raw['radial_log_increment']).upper()).upper()
        Jlog = (material_factor*ball(raw['log_w_variation']).upper()).upper()
        symbols.append(dict(U2=U2,S=S,T=T,A=A,C=Cc,Jrad=Jrad,Jlog=Jlog,
            E=(1+w.upper()**2).upper(), w2=(w.upper()**2).upper()))
    output = []
    for b in sorted(set([m-a,m+a])):
        if b <= 0: continue
        for component in (0,1):
            rad=[]; log=[]; w2=[]
            for parent,s in zip(parents,symbols):
                weight=(-b*parent['tau'].lower()).exp().upper()/arb(1+b)
                rad.append((weight*s['Jrad']*s['E']*s['A']*(1/B.lower() if component==0 else arb(b))).upper())
                log.append((weight*s['Jlog']*s['C']*(arb(b)/B.lower() if component==0 else arb(1))).upper())
                extra=((s['U2']+s['S'])*b/B.lower()+s['T']/B.lower()) if component==0 else s['S']
                w2.append((weight*s['Jlog']*s['w2']*extra).upper())
            total=[(x+y+z).upper() for x,y,z in zip(rad,log,w2)]
            result=integrate_ordered(parents,ph,ps,phi,psi,total,ball(row['mu_ratio']))
            result.update(input_mode=b,input_component='Bp/V' if component==0 else 'kappa/V',
                radial=integrate_ordered(parents,ph,ps,phi,psi,rad,ball(row['mu_ratio'])),
                logarithmic=integrate_ordered(parents,ph,ps,phi,psi,log,ball(row['mu_ratio'])),
                w_squared=integrate_ordered(parents,ph,ps,phi,psi,w2,ball(row['mu_ratio'])))
            output.append(result)
    result=dict(status='Certified one-cell derivative columns of the exact quadratic principal part only',
        cell=D['cell'],output_mode=m,centre_mode=a,centre_plain_cosine_Q=rec(qcut),rows=output,
        exact_identity='C_a=u2_a+partial_theta(u1_a/B)=sqrt(12)*mu*Xi_a/(r^4*w*V)',
        source_materials=['d1=V^2/(r*w)','dlambda=abs(w_r/w)*V^2/w'],
        angular_weights='Output (1+m) is already in physical Green caps; each input column divides only by1+b. Its source exponential is exp(-b*tau_source).',
        scope=['Only the specified true linear centre mode is included.',
            'The auxiliary centre correction, other centre modes, full mean/inverse remainder, and other source/target cells remain separate inputs.',
            'Each row is one frequency shift and one physical input component, not the norm of the full coupled derivative.'],
        input_hashes=hashes,source_hashes={Path(__file__).name:sha(Path(__file__).read_bytes()),
            'closure_weighted_panel_low_green_v3.py':sha(Path(__file__).with_name('closure_weighted_panel_low_green_v3.py').read_bytes())},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    args.out.write_bytes(payload)
    print(json.dumps(dict(event='done',output=str(args.out),
        columns=[dict(input_mode=r['input_mode'],component=r['input_component'],bound=str(ball(r['diagonal']))) for r in output],
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
