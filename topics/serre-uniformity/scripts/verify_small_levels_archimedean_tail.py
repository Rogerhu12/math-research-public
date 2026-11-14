#!/usr/bin/env python3
"""Check the R101 tail certificate independently of its coordinate search.

The previously verified exact cusp data are read from their published hash.
Logarithms and the inverse matrix are rebuilt at higher precision with a
different trigonometric entry point.  Saved coordinates only select a test;
every possible integer and every reported surviving interval is checked.
"""
import argparse
import hashlib
import json
from pathlib import Path
from flint import arb, arb_mat, fmpq, ctx


def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--precision',type=int,default=384)
    pa.add_argument('--initial',type=Path,default=Path(__file__).with_name('data')/'small_levels_archimedean_reduction.json')
    pa.add_argument('--certificate',type=Path,default=Path(__file__).with_name('data')/'small_levels_archimedean_tail.json')
    args=pa.parse_args();ctx.prec=args.precision
    raw=args.certificate.read_bytes();cert=json.loads(raw)
    initial_raw=args.initial.read_bytes();initial=json.loads(initial_raw)
    assert cert['version']==1 and cert['contraction_passes']==3
    assert hashlib.sha256(initial_raw).hexdigest()==cert['initial_sha256']=='0b4d761752b07f3410a18d2e16eeb7f6bde98add4214bf889c0188fd410ba159'
    assert args.precision>cert['precision_bits']>=256
    scale=2**cert['endpoint_bits'];assert cert['endpoint_bits']==64
    dyadic=lambda n:arb(fmpq(n,scale))
    lowint=lambda x:int(x.lower().ceil().unique_fmpz())
    highint=lambda x:int(x.upper().floor().unique_fmpz())
    assert [r['p'] for r in cert['levels']]==[41,47,59,83]
    for saved,old in zip(cert['levels'],initial['levels']):
        p=old['p'];assert saved['p']==p
        d=(p-1)//2;g=old['g'];xi=old['xi']
        logs=[None]+[(2*(arb.pi()*a/p).sin()).log() for a in range(1,p)]
        E=arb_mat([[2*logs[pow(g,k,p)]]+[logs[(j*pow(g,k,p))%p]-logs[pow(g,k,p)] for j in range(2,d+1)] for k in range(d)])
        A=E.inv()
        kappa=arb(fmpq(saved['kappa_upper_numerator'],2**64))
        assert all(sum(abs(A[i,j]) for j in range(d))<=kappa for i in range(d))
        def epsilon(s):
            z=(-s/p).exp()
            q=(-s).exp()
            return 16*kappa*(z/((1-z)*(1-z)*(1-q))+q/((1-q)*(1-q)))
        lower=saved['lower'];assert lower==6*p
        total=kept=0;largest=lower
        assert len(saved['cusps'])==len(old['cusps'])==d
        for c,src in zip(saved['cusps'],old['cusps']):
            assert c['s']==src['s']
            u,b,v,w=src['matrix']
            assert (u*w-b*v)%p==1 and (xi*v*v-u*u)%p==(-c['s'])%p!=0
            # Nonzero y^2 coefficient proves at most four y for each x.
            delta=A*arb_mat([[arb(fmpq(*z))] for z in src['v']])
            theta=A*arb_mat([[2*sum(n*logs[a] for a,n in row)] for row in src['gamma']])
            i=c['coordinate'];assert 0<i<d and abs(delta[i,0])>0
            upper=src['S_final']
            image=delta[i,0]*arb(lower).union(upper)+theta[i,0]+arb(0,epsilon(arb(lower)).upper())
            first,last=c['n_first'],c['n_last']
            assert first<=lowint(image) and last>=highint(image)
            assert len(c['exclusion_coordinates'])==last-first+1
            bands={int(n):(int(a),int(b)) for n,a,b in c['surviving_bands']}
            assert len(bands)==len(c['surviving_bands'])
            for n,j in zip(range(first,last+1),c['exclusion_coordinates']):
                lo,hi=lower*scale,upper*scale
                midpoint=(n-theta[i,0])/delta[i,0]
                for _ in range(cert['contraction_passes']):
                    radius=(epsilon(dyadic(lo))/abs(delta[i,0])).upper()
                    interval=midpoint+arb(0,radius)
                    lo=max(lo,int((interval.lower()*scale).floor().unique_fmpz()))
                    hi=min(hi,int((interval.upper()*scale).ceil().unique_fmpz()))
                    if lo>hi:break
                total+=1
                if j==-1:
                    assert lo>hi and n not in bands;continue
                assert lo<=hi
                if j==0:
                    aa,bb=bands.pop(n)
                    assert aa<=lo<=hi<=bb
                    kept+=1;largest=max(largest,(bb+scale-1)//scale)
                    continue
                assert 0<j<d and j!=i and n not in bands
                val=delta[j,0]*dyadic(lo).union(dyadic(hi))+theta[j,0]+arb(0,epsilon(dyadic(lo)).upper())
                assert lowint(val)>highint(val)
            assert not bands
        assert (total,kept,largest)==(saved['integers_checked'],saved['bands_surviving'],saved['S_uniform'])
        print(f'p={p}: verified all {total} integers, {kept} possible bands; s <= {largest}.',flush=True)
    print('SHA256',hashlib.sha256(raw).hexdigest())
    print('Surviving bands are necessary enclosures, not constructed integral points.')


if __name__=='__main__':main()
