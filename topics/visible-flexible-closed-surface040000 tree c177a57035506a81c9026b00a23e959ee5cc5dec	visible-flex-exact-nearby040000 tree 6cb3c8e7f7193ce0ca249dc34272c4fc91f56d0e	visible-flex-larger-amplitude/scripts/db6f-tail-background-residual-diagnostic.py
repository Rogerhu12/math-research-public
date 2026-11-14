#!/usr/bin/env python3
"""Locate loose phase bounds without asserting a new continuous certificate."""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import numpy as np
from db6f_tail_integrated import IntegratedTail

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('residual_packet',HERE/'db6f-tail-background-packet-totalwidth.py')
supplier=importlib.util.module_from_spec(sp);sp.loader.exec_module(supplier)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--packet',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--width',type=float,default=1e-9)
    args=ap.parse_args();data=json.loads(args.packet.read_text())
    bg=supplier.Background(data['primitive_file'],data['settings']['calibrations'])
    tail=IntegratedTail(data['finite_tail_manifest']);nodes=supplier.exact_nodes(tail)
    path=args.packet.parent/data['data_file'];raw=path.read_bytes()
    assert sha(path)==data['data_sha256']
    z=np.load(io.BytesIO(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw))
    uncertainty=z['w_remainder']+np.sum(z['w_hi']-z['w_lo'],axis=1)
    rows=[]
    for k in np.flatnonzero(uncertainty>args.width):
        span=int(z['span_index'][k]);ul,ur=map(Q,map(float,[z['u_left'][k],z['u_right'][k]]))
        L=nodes[span+1]-nodes[span];rl,rr=nodes[span]+L*ul,nodes[span]+L*ur
        profile=bg.proposal_profile((rl+rr)/2)
        xp,x0,x1=bg.inverse_polynomial(profile,rl,rr)
        first,last=profile.leaf_index(x0),profile.leaf_index(x1)
        points=[]
        for tau in [0.,.25,.5,.75,1.]:
            coeff=[(float(q.lo)+float(q.hi))/2 for q in xp]
            x=float(np.polynomial.polynomial.polyval(tau,coeff));x=min(x1,max(x0,x))
            radius=profile.point(x);target=rl+(rr-rl)*Q(tau)
            points.append({'tau':tau,'source_x':x,
                           'point_radius_width':float(radius.hi-radius.lo),
                           'center_phase_error':float((Q(float(radius.lo))+Q(float(radius.hi)))/2-target),
                           'point_error_upper':float(supplier.qbounds(max(abs(Q(float(radius.lo))-target),abs(Q(float(radius.hi))-target))).hi)})
        rows.append({'row':int(k),'span':span,'u_left':float(ul),'u_right':float(ur),
                     'physical_width':float(rr-rl),'source_cell':profile.n,'source_segment':profile.j,
                     'source_x0':x0,'source_x1':x1,'intersected_leaves':last-first+1,
                     'used_many_leaf_monotone_fallback':last-first>64,
                     'saved_radial_residual':float(z['radial_residual'][k]),'samples':points})
    report={'status':'phase-bound-localization-not-a-new-certificate','input':str(args.packet),
            'input_sha256':sha(args.packet),'script_sha256':sha(__file__),'rows':rows}
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'rows':len(rows),'many_leaf_fallbacks':sum(x['used_many_leaf_monotone_fallback'] for x in rows),
                      'maximum_leaf_count':max(x['intersected_leaves'] for x in rows),
                      'maximum_point_radius_width':max(x['point_radius_width'] for row in rows for x in row['samples']),
                      'maximum_sampled_phase_center_error':max(abs(x['center_phase_error']) for row in rows for x in row['samples'])}))


if __name__=='__main__':main()
