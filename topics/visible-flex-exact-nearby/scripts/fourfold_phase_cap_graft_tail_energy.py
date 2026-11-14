#!/usr/bin/env python3
"""True natural-graft and infinite-tail energies of the saved physical cap trials.

The graft is the same exact natural C4 construction used in R71/R74, evaluated
at the exact affine center.  All infinite angular modes are enclosed by real
Wiener majorants.  The tail uses the actual R74 Robin intervals and their true
reciprocals; the regular mean is retained as its separate flux/trace slot.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_affine import AffineBulkTarget
from fourfold_phase_beta_bulk_box import CBox,cstack,zeros
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import (
    FiniteTrial,gauss_rule,constant_array,matrix_product,conjugate,hermitian_midpoint,sha)
from fourfold_phase_cap_wiener_box import real_wiener_form,integrate_box,real_part
from fourfold_phase_natural_exterior_graft import NaturalGraft,real_coefficient,modulus
from fourfold_phase_exterior_entry_jet import entry_germs
from fourfold_phase_finite_tail_DN import finite_tail_entries


def save(path,record):
    path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(record,indent=2)+'\n').encode()
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)
    temporary.replace(path)


class ExactGraftPoint(NaturalGraft):
    def __init__(self,object_path):
        self.target=AffineBulkTarget(object_path,128,128,arb('.003'),arb('.0025'),arb('.32'))
        self.entry=entry_germs(self.target)
        self.length=Fraction(1,8);self.ell=exact_arb(self.length)
        old,ctx.cap=ctx.cap,8
        beta,gamma,radius,_=self.target.scalars(acb(3),1)
        self.beta_normalized=[[real_coefficient(v/radius**3,j) for j in range(5)] for v in beta]
        self.gamma_normalized=[[real_coefficient(v/radius**2,j) for j in range(5)] for v in gamma]
        ctx.cap=old
        loga,c=self.entry['log_radius'],self.entry['slope_ratio']
        correction=sum((modulus(loga[j])*self.ell**j for j in range(2,5)),arb(0))
        cfee=sum((modulus(c[j])*self.ell**j for j in range(1,4)),arb(0))
        self.c_global=c[0]+arb(0,cfee.upper())
        if not self.c_global>0 or not loga[1]<0:
            raise ValueError('the same actual graft lacks decreasing radius or positive vertical slope')
        self.a_global=(loga[0]+loga[1]*real_interval(0,self.length)+arb(0,correction.upper())).exp()
        increment=(self.ell*self.a_global**2*self.c_global).upper()
        self.Z_global=self.entry['height'][0]+arb(0).union(increment)
        if not self.Z_global>0:
            raise ValueError('the actual full graft height is not positive')

    def whole_angle_values(self,left,right):
        if not Fraction(3)<=left<right<=Fraction(25,8):
            raise ValueError('the requested interval is outside this exact natural graft')
        jets=self.jets(left-3,right-3)
        a=real_part(jets['radius'][0])
        L=real_part(jets['log_radius'][1])
        Lp=2*real_part(jets['log_radius'][2])
        C=real_part(jets['slope_ratio'][0]);Cp=real_part(jets['slope_ratio'][1])
        beta=[[math.factorial(j)*real_part(v[j]) for v in jets['beta']] for j in range(3)]
        gamma=[[math.factorial(j)*real_part(v[j]) for v in jets['gamma']] for j in range(3)]
        return real_wiener_form(a,self.Z_global,L,Lp,C,Cp,beta,gamma)


def true_tail_energy(trial,tail):
    if tail['input_sha256']!=trial.cache['exact_tail_input_sha256']:
        raise ValueError('the saved trial and true infinite tail inputs differ')
    parameter=list(map(Fraction,tail['exact_parameter_interval']))
    delta=Fraction(trial.report['exact_delta_fraction'])
    if not parameter[0]<=delta<=parameter[1]:
        raise ValueError('the actual point is outside the certified tail family')
    U=constant_array(trial.V[-trial.n:])
    P=zeros((trial.n,trial.d))
    begin=(trial.nodes-1)*trial.nn
    P[trial.nonzero]=constant_array(trial.flux[begin:begin+trial.nn])
    P[trial.M]=constant_array(trial.flux[trial.nodes*trial.nn])
    gamma=zeros((trial.n,1));inverse=zeros((trial.n,1))
    for index,k in enumerate(range(-trial.M,trial.M+1)):
        if not k:continue
        value=arb(tail['entries'][abs(k)-1]['true_Robin']['ball'])
        if not value>0:
            raise ValueError('an actual nonzero-mode Robin eigenvalue is not positive')
        gamma[index,0]=CBox.from_acb(acb(value))
        inverse[index,0]=CBox.from_acb(acb(1/value))
    matrices=[matrix_product(conjugate(U).transpose(1,0),gamma*U),
              matrix_product(conjugate(P).transpose(1,0),inverse*P)]
    answer=[]
    for matrix in matrices:
        middle,error=hermitian_midpoint(matrix)
        answer.append(dict(matrix_middle=[[[float(z.real),float(z.imag)] for z in row] for row in middle],
            full_operator_error=ball_record(error),
            scope='True Robin or inverse Robin, its actual family interval, directed finite sums and dyadic selection are all included; the mean is not assigned a false Robin eigenvalue.'))
    # T(g,h)=L(j_g,h) uses only exact saved boundary coefficients.
    # No floating inverse is used and no interior energy enters this matrix.
    left=np.zeros((trial.n,trial.d),complex)
    left[trial.nonzero]=trial.flux[:trial.nn]
    left[trial.M]=trial.flux[trial.nodes*trial.nn]
    selected=trial.M-trial.B+np.arange(2*trial.B+1)
    T=np.empty((trial.d,trial.d),complex)
    T[:,:-1]=-left[selected].conj().T
    T[:,-1]=left[trial.M].conj()
    return dict(primal_energy=answer[0],dual_energy=answer[1],
        exact_boundary_T=[[[float(z.real),float(z.imag)] for z in row] for row in T],
        regular_mean_flux_retained=True,tail_input=tail)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--error-per-length',type=Fraction,default=Fraction(1,100000))
    parser.add_argument('--max-depth',type=int,default=10)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();ctx.prec,ctx.cap=args.bits,8
    wall,cpu=time.monotonic(),time.process_time()
    trial=FiniteTrial(args.trial);graft=ExactGraftPoint(trial.object_path)
    tail=finite_tail_entries(Path('notes/2026-11-12-positive-family-natural-graft.json'),
        Path('notes/2026-11-12-actual-exterior-robin-certificate.json'),
        Path('notes/2026-11-12-common-core-exterior-parameter-interval.json'),trial.M)
    original=json.loads(Path('notes/2026-11-12-positive-family-natural-graft.json').read_text())
    if (not original['complete'] or Fraction(original['graft_length'])!=graft.length
        or original['origin_inputs_sha256']!=graft.target.affine_definition['origin_inputs']['sha256']
        or original['direction_sha256']!=graft.target.affine_definition['direction']['sha256']):
        raise ValueError('the actual natural graft and R74 tail construction do not match')
    if original['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_natural_exterior_graft.py')):
        raise ValueError('the frozen actual natural graft formula changed')
    nodes,weights=gauss_rule(trial.degree+1)
    rows,failed,rejected=[],[],[]
    report=dict(kind='actual_natural_graft_and_true_tail_finite_trial_energy',complete=False,
        source_sha256=sha(__file__),trial_report_path=str(args.trial),trial_report_sha256=sha(args.trial),
        object_sha256=trial.report['object_sha256'],exact_delta_fraction=trial.report['exact_delta_fraction'],
        graft_radius_interval=['3','25/8'],actual_natural_graft_sha256=sha('notes/2026-11-12-positive-family-natural-graft.json'),
        error_density_target=str(args.error_per_length),bits=args.bits,
        actual_graft_height_enclosure=ball_record(graft.Z_global),
        intervals=rows,failed=failed,rejected=rejected,
        gauss_nodes=list(map(ball_record,nodes)),gauss_weights=list(map(ball_record,weights)),
        infinite_tail=true_tail_energy(trial,tail),full_positive_cap_complete=False,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_wiener_box.py','fourfold_phase_cap_energy_interval.py',
            'fourfold_phase_natural_exterior_graft.py','fourfold_phase_exterior_entry_jet.py',
            'fourfold_phase_finite_tail_DN.py','fourfold_phase_beta_affine.py')},
        scope='The true graft and infinite-tail energy only. The rest of the cap body and final full operator remain separate.')
    def checkpoint():
        report['CPU_seconds']=time.process_time()-cpu
        report['wall_seconds']=time.monotonic()-wall
        save(args.out,report)
    for element in range(trial.cells):
        a,b=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
        if b<=3:continue
        if not 3<=a<b<=Fraction(25,8):
            raise ValueError('a saved trial element crosses the true graft entrance or exit')
        pending=[(a,b,0)]
        while pending:
            left,right,depth=pending.pop()
            try:
                values,diagnostics=graft.whole_angle_values(left,right)
                energy=integrate_box(values,trial,element,left,right,nodes,weights)
                density=max(arb(x['full_operator_error']['ball']).upper() for x in energy)/exact_arb(right-left)
                if not density<=exact_arb(args.error_per_length):
                    raise ValueError('actual graft coefficient variation exceeds energy budget: '+density.str(16))
                rows.append(dict(finite_element=element,exact_radial_interval=[str(left),str(right)],
                    subdivision_depth=depth,true_form_and_inverse_boxes=list(map(ball_record,values)),
                    full_Wiener_diagnostics=diagnostics,primal_energy=energy[0],dual_energy=energy[1]))
            except (ValueError,ZeroDivisionError) as exc:
                item=dict(exact_radial_interval=[str(left),str(right)],depth=depth,reason=str(exc))
                if depth==args.max_depth:failed.append(item)
                else:
                    rejected.append(item);mid=(left+right)/2
                    pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
            checkpoint()
        print(json.dumps(dict(element=element,accepted=len(rows),failed=len(failed),
            CPU_seconds=report['CPU_seconds'],wall_seconds=report['wall_seconds'])),flush=True)
        if failed:break
    rows.sort(key=lambda row:Fraction(row['exact_radial_interval'][0]))
    cursor=Fraction(3)
    for row in rows:
        left,right=map(Fraction,row['exact_radial_interval'])
        if left!=cursor:break
        cursor=right
    report['complete']=not failed and cursor==Fraction(25,8)
    report['integrated_graft_operator_errors']={key:ball_record(sum((
        arb(row[key]['full_operator_error']['ball']).upper() for row in rows),arb(0)).upper())
        for key in ('primal_energy','dual_energy')}
    checkpoint();print(json.dumps(dict(complete=report['complete'],
        errors=report['integrated_graft_operator_errors'],CPU_seconds=report['CPU_seconds'],
        wall_seconds=report['wall_seconds'])),flush=True)
    if not report['complete']:raise SystemExit('the true graft energy cover remains incomplete')


if __name__=='__main__':main()
