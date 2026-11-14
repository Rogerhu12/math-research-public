#!/usr/bin/env python3
"""Exact Fourier padding and Bernstein degree elevation of an INITIAL GUESS.
New binary controls are rounded representatives of stored exact rational
degree elevation. This is not a new solve or evidence of metric convergence.
"""
import argparse,json,math
from fractions import Fraction
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz,save_npz,identity

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--modes',type=int,required=True)
    a=ap.parse_args();data=load_npz(a.input)
    y,p=data['corrections'],data['parameters']
    old=(y.shape[1]-2)//3;new=a.modes
    if y.shape[1]!=3*old+2 or len(p)!=2*old+2 or new<=old:
        raise ValueError('Expected a strictly larger raw Fourier mode count')
    if str(data.get('tail_kind',''))!='positive_bernstein':
        raise ValueError('Explicit positive Bernstein family identity is required')
    z=np.zeros((len(y),3*new+2))
    z[:,:old+1]=y[:,:old+1]
    z[:,new+1:new+1+old]=y[:,old+1:2*old+1]
    z[:,2*new+1:2*new+old+2]=y[:,2*old+1:]
    q=np.zeros(2*new+2);q[:old]=p[:old];q[-1]=p[-1]
    controls=[Fraction.from_float(float(x)) for x in p[old:-1]]
    exact=[];errors=[]
    for k in range(new+1):
        value=sum((controls[j]*math.comb(old,j)*math.comb(new-old,k-j)
                   for j in range(max(0,k-new+old),min(old,k)+1)),Fraction())/math.comb(new,k)
        q[new+k]=float(value)
        exact.append([str(value.numerator),str(value.denominator)])
        errors.append(abs(Fraction.from_float(float(value))-value))
    bound=float(max(errors))
    definition=dict(source=identity(__file__),input=identity(a.input),
        old_modes=old,new_modes=new,exact_control_rationals=exact,
        Fourier_correction_preserved_exactly=True,
        maximum_control_rounding_error=bound,tail_angle_rounding_bound=bound,
        tail_curvature_rounding_bound=bound*630/(256*.46),
        physical_T_unchanged=True,initializer_only=True,new_nonlinear_solve=False)
    mesh=data['mesh'] if 'mesh' in data else data['x']
    arrays=dict(mesh=mesh,corrections=z,parameters=q,modes=np.array(new),
        elevation_definition=np.array(json.dumps(definition,sort_keys=True)))
    for key in ('profile_kind','tail_kind','base_kind','candidate_sha256'):
        if key in data:arrays[key]=data[key]
    definition['output']=save_npz(a.output,**arrays)
    a.output.with_name(a.output.name+'-report.json').write_text(json.dumps(definition,indent=2)+'\n')
    print(json.dumps({k:definition[k] for k in ('old_modes','new_modes','maximum_control_rounding_error','output')}))
if __name__=='__main__':main()
