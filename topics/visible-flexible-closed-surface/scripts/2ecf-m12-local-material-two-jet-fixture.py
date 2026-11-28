#!/usr/bin/env python3
"""Nonzero two-piece check against independent direct material derivatives."""
import argparse,gzip,hashlib,importlib.util,io,json,time
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import BSpline

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser()
    for k in ('scripts','data','out'):ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    new=load('new_material_two_jet',Path(__file__).with_name('2ecf-m12-local-material-two-jet-budget.py'))
    old=load('old_local_first_jet',args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py')
    cert=load('old_integer_interval',args.scripts/'6a65-m12-r137-continuous-domain.py')
    with np.load(io.BytesIO(gzip.decompress(args.data.read_bytes())),allow_pickle=False) as f:
        source=f['jets'][0,0]
    M=(len(source)-2)//3;pm=np.arange(-M,M+1)*3+1;zm=np.arange(M+1)*3
    planar={1:Q.from_float(float(source[0]))}
    for k in range(1,M+1):
        a,b=Q.from_float(float(source[k])),Q.from_float(float(source[M+k]))
        planar[1+3*k]=(a+b)/2;planar[1-3*k]=(a-b)/2
    amp=Q(1,10**7)
    row=[amp*planar.get(int(k),Q(0)) for k in pm]+[Q(0)]*len(zm)
    knots=[Q(0)]*6+[Q(1,2)]+[Q(1)]*6
    pieces=old.extract_bezier(knots,[row])
    # This artificial field deliberately uses a=1, radial coordinate z and
    # target radius 1. It is not a new production M12 candidate.
    metric=SimpleNamespace(Jmin=Q(1,10),ahi=Q(1),Tlo=Q(1),Thi=Q(1),Slo=Q(2),scales=lambda a,b:(Q(1),Q(1),Q(0)))
    bounder=new.Bounds(old,cert,metric,new.central_laurent(args.data),64,8)
    cc={k:Q(0) for k in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]}
    bound=[]
    for a,b,c in pieces:
        v,r=bounder.piece(c,a,b,pm,zm,cc,Q(0),Q(0));bound.append(v)
    full=np.zeros((7,len(row)));full[3]=[float(x) for x in row]
    spline=BSpline(np.asarray(knots,float),full,5)
    P=new.central_laurent(args.data)
    peak=np.zeros(3);max_numerator_discrepancy=0.
    for z in np.linspace(0,1,65):
        C,Cz,Czz=[spline(z,d) for d in (0,1,2)]
        for theta in np.linspace(0,2*np.pi,193,endpoint=False):
            exp=np.exp(1j*pm*theta)
            W=np.dot(C[:len(pm)],exp);Wz=np.dot(Cz[:len(pm)],exp);Wzz=np.dot(Czz[:len(pm)],exp)
            Wt=np.dot(C[:len(pm)]*(1j*pm),exp);Wzt=np.dot(Cz[:len(pm)]*(1j*pm),exp);Wtt=np.dot(-C[:len(pm)]*pm**2,exp)
            speed=sum(float(v)*np.exp(1j*k*theta) for k,v in P.items()).real
            speedprime=sum(1j*k*float(v)*np.exp(1j*k*theta) for k,v in P.items()).real
            J=np.sqrt(speed);Jt=speedprime/(2*J)
            # Direct chain rule, separate from the single Fourier numerator.
            Wuu=Wtt/J**2-Wt*Jt/J**3
            vectors,errors,exact=new.round_vector([Q.from_float(float(v)) for v in C],pm,zm)
            if z in (0.,.5,1.):
                num,ne=bounder.numerator(vectors,errors,exact)
                Nv=sum(v*np.exp(1j*k*theta) for k,v in num[0].items())/(2*new.S**2)
                max_numerator_discrepancy=max(max_numerator_discrepancy,abs(Nv/speed**2-Wuu))
            vals=[abs(W),np.sqrt(abs(Wz)**2+abs(Wt/J)**2),abs(Wzz)+2*abs(Wzt/J)+abs(Wuu)]
            peak=np.maximum(peak,vals)
            i=0 if z<=.5 else 1
            if any(v>float(bound[i][j])*(1+2e-13)+1e-18 for j,v in enumerate(vals)):
                raise ArithmeticError('Independent material derivative escaped the continuous bound')
    out={'schema':'2ecf-local-material-two-jet-nonzero-fixture-v1','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(new.__file__).read_bytes()).hexdigest(),'nonzero_radial_free_rows':1,
        'angular_columns':len(row),'basis_spans':2,'direct_evaluation_points':65*193,
        'material_coordinate_definition':'a=1, s=z, f=1; exact original central J; artificial nonzero C2 correction, no production geometry claim',
        'strict_bounds':[[str(x) for x in v] for v in bound],
        'independent_direct_sample_maxima':peak.tolist(),'direct_chain_vs_Fourier_numerator_maximum_difference':max_numerator_discrepancy,
        'every_sample_inside_exact_continuous_bounds':True,'production_field_consumed':False,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
