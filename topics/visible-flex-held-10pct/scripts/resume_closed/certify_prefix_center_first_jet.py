#!/usr/bin/env python3
"""Fourth-order angular Taylor bounds for the unchanged analytic core lift.

R28's second-order Taylor boxes suffice for geometry, but their interval
cancellation losses need not suffice for a 1e-6 metric claim.  This computes
the new first-jet bound, preserving the identical analytic core and lift.
"""
from pathlib import Path
import argparse,hashlib,json,math,sys,time
import numpy as np
import mpmath as mp
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'finite_closure/m3_m8_closed_map'))
from m3_interval_center import CoreLiftIntervals,lower,upper
from prefix_true_profile import sincos
from certify_background_sharp import Jet,interval,absmax


class FourthOrder(CoreLiftIntervals):
    def jet_delta(self,psi,phi):
        iv=self.iv;n=4
        angle=Jet.variable(psi,n)
        sp,cp=sincos(angle*3)
        theta_prime=1-cp*iv.mpf(self.E0)
        phi_coeff=[phi]+[iv.mpf(0)]*n
        # phi'=theta_psi/rho_core(phi); this recurrence determines every
        # Taylor coefficient without differentiating a numerical root.
        for j in range(n):
            pj=Jet(phi_coeff[:j+1]);rho=Jet.constant(1,j)
            for c,m in zip(self.coeff,self.freq):
                _,co=sincos(pj*m)
                rho=rho+co*(iv.mpf(c)*(1-m*m))
            assert lower(rho.c[0])>0
            rhs=Jet(theta_prime.c[:j+1])/rho
            phi_coeff[j+1]=rhs.c[j]/(j+1)
        pp=Jet(phi_coeff);sn,cs=sincos(pp)
        h=Jet.constant(1,n);hp=Jet.constant(0,n)
        for c,m in zip(self.coeff,self.freq):
            si,co=sincos(pp*m)
            h=h+co*iv.mpf(c);hp=hp-si*(m*iv.mpf(c))
        zero=Jet.constant(0,n);one=Jet.constant(1,n)
        gamma=[h*cs-hp*sn,h*sn+hp*cs,zero]
        b=sp*(-iv.mpf(self.Epp))/3
        target=[gamma,[zero,zero,one],[-b*sn,b*cs,zero]]
        trig={}
        for k in set(self.odd+self.even):trig[k]=sincos(angle*k)
        before=[]
        for row in self.jets:
            X=Jet.constant(0,n);Y=Jet.constant(0,n);Z=Jet.constant(iv.mpf(row[self.iz]),n)
            for j,k in enumerate(self.odd):
                si,co=trig[k]
                X=X+co*iv.mpf(row[j])
                Y=Y+si*iv.mpf(row[len(self.odd)+j])
            for j,k in enumerate(self.even):Z=Z+trig[k][1]*iv.mpf(row[self.iz+1+j])
            before.append([X,Y,Z])
        return [[x-y for x,y in zip(t,b)]for t,b in zip(target,before)]

    def all_first_bounds(self):
        iv=self.iv;N=self.N
        bounds=[[[mp.mpf(0)for _ in range(3)]for _ in range(3)]for _ in range(2)]
        point_max=np.zeros((4,3));fourth_max=np.zeros(3)
        left_phi=self.phi_point(iv.mpf(0))
        for j in range(N):
            pl=2*iv.pi*j/N;pr=2*iv.pi*(j+1)/N;pc=iv.pi*(2*j+1)/N
            right_phi=self.phi_point(pr);center_phi=self.phi_point(pc)
            whole_psi=iv.mpf([lower(pl),upper(pr)])
            whole_phi=iv.mpf([lower(left_phi),upper(right_phi)])
            center=self.jet_delta(pc,center_phi)
            whole=self.jet_delta(whole_psi,whole_phi)
            width=iv.mpf(upper((pr-pl)/2))
            for radial in range(3):
                for axis in range(3):
                    c=center[radial][axis].c
                    rem=absmax(whole[radial][axis].c[4])
                    val=sum((iv.mpf(absmax(c[k]))*width**k for k in range(4)),iv.mpf(0))+iv.mpf(rem)*width**4
                    first=sum((k*iv.mpf(absmax(c[k]))*width**(k-1)for k in range(1,4)),iv.mpf(0))+4*iv.mpf(rem)*width**3
                    for d,v in enumerate([val,first]):bounds[d][radial][axis]=max(bounds[d][radial][axis],upper(v))
                    for k in range(4):point_max[k,radial]=max(point_max[k,radial],float(absmax(c[k])*math.factorial(k)))
                    fourth_max[radial]=max(fourth_max[radial],float(rem*24))
            left_phi=right_phi
            if j%32==0:print(json.dumps({'event':'fourth_order_center','done':j+1,'total':N}),flush=True)
        norm=[]
        for row in bounds:
            norm.append([math.nextafter(float(upper(iv.sqrt(sum((iv.mpf(x)**2 for x in v),iv.mpf(0))))),math.inf)for v in row])
        return dict(angular_boxes=N,validated_inverse_brackets=self.bracket_checks,
            uniform_delta_norm_angular_then_radial=norm,
            component_bounds_angular_radial_axis=[[[math.nextafter(float(v),math.inf)for v in row]for row in order]for order in bounds],
            point_delta_derivative_abs_max_display=point_max.tolist(),
            whole_box_fourth_derivative_abs_max_display=fourth_max.tolist(),
            maximum_taylor_order=4,full_circle=True,angular_sampling_used_as_proof=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=512)
    a=p.parse_args();started=time.monotonic();raw=np.load(a.data)
    pm,hm=raw['planar_modes'],raw['height_modes'];P=len(pm)
    odd=np.sort(abs(pm));index={int(k):j for j,k in enumerate(odd)}
    J=np.zeros((3,2*len(odd)+len(hm),len(raw['knots'])))
    for j,k in enumerate(pm):
        i=index[abs(int(k))]
        J[:,i]=raw['jets'][:,j]
        J[:,len(odd)+i]=(1 if k>0 else -1)*raw['jets'][:,j]
    J[:,2*len(odd):]=raw['jets'][:,P:]
    data=dict(odd=odd,even=hm[1:],jets=J,core_coefficients=raw['core_coefficients'],
        core_frequencies=raw['core_frequencies'],chart_E0=raw['phase_jets'][0,0,0],chart_Epp=raw['phase_jets'][2,0,0])
    result=FourthOrder(data,a.angular).all_first_bounds()
    result.update(scope=__doc__,command=sys.argv,input_sha256=hashlib.sha256(a.data.read_bytes()).hexdigest(),
        sources_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),
            Path(__file__).with_name('prefix_true_profile.py'),Path(__file__).with_name('certify_background_sharp.py'),
            Path(__file__).resolve().parents[1]/'finite_closure/m3_m8_closed_map/m3_interval_center.py']},
        seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)


if __name__=='__main__':main()
