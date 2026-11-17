#!/usr/bin/env python3
"""A fixed finite-speed arclength normalization of the actual C2 prefix.

At each s, q_N is the real trigonometric interpolant of |F_phi| on a fixed
construction grid. Let b=mean(q_N), lambda=a/b, c=(0,0,z_mean), and define
psi by integral_0^psi q_N = b*integral_0^phi rho. The new map is
c+lambda*(F(s,psi)-c). Its g_phiphi error is retained as |F_phi|^2/q_N^2-1.
Audit angles vary without changing the construction grid or parent quintic.
Curvature is computed on G=c+lambda*(F-c), which has the same image before
angular reparameterization. All radial jets come from that same quintic.
"""
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
import parallel_20261117_inward_profile as scalar

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def opnorm(er,gr,fr):return (abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2

def main(a):
 start=time.perf_counter();raw=a.input.read_bytes();data=json.loads(gzip.decompress(raw))
 if not data['success']or sha(scalar.__file__)!=data['inward_profile_sha256']:raise ValueError('Accepted inward source required')
 M=data['M'];N=a.construction_angles or data['N'];Q=a.angles
 if Q<N or Q%2:raise ValueError('Audit grid must be even and at least construction grid')
 qc=Frenet(M,N);qa=Frenet(M,Q);old=Frenet(M,data['N']);v=data['inward_scalar_profile']
 profile=scalar.InwardProfile(data['fixed_scalar_profile']['geometry'],data['analytic_extension_origin'],v['cut'],v['curvature'],v['ramp_in'],v['ramp_out'],v['quadrature'])
 x=np.array(data['mesh']);Y=np.array(data['states']);D=np.array(data['rhs']);DD=[]
 for s,y,dy in zip(x,Y,D):
  r,ap,app=profile(s);k=ap/r;DD.append(old.jvp(y,k,dy,dk=app/r-k*k))
 DD=np.array(DD);rho=1+np.cos(qa.angle[:,None]*qa.freq[None,1:])@((1-qa.freq[1:]**2)*Y[0,1:M+1])
 freqs=np.arange(N//2+1);minima=dict(qN=np.inf,angle_positive_lower_at_sampled_s=np.inf,scaled_image_gram_determinant=np.inf)
 maxima=dict(scale_minus_one=0.,scale_s=0.,scale_ss=0.,psi_s=0.,qN_speed_relative=0.,position_change=0.,velocity_change=0.,rr=0.,angular=0.,mixed=0.)
 worst=dict(value=0.);old_worst=dict(value=0.);curve=dict(value=0.);core=None;samples=0
 def fourier(values,power=0):
  spec=np.fft.rfft(values)/N;spec[-1]*=.5
  if power:
   spec[0]=0.;spec[1:] *= (1j*freqs[1:])**power
  padded=np.zeros(Q//2+1,complex);padded[:len(spec)]=spec
  if Q==N:padded[-1]*=2
  result=np.fft.irfft(Q*padded,n=Q)
  if power<0:result-=result[0]
  return result,spec
 for i,h in enumerate(np.diff(x)):
  c0=Y[i];c1=h*D[i];c2=h*h*DD[i]/2;aa=Y[i+1]-c0-c1-c2;bb=h*D[i+1]-c1-2*c2;cc=h*h*DD[i+1]-2*c2
  co=np.array([c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2])
  for j in range(a.radial_subdivisions+1):
   if i and j==0:continue
   u=j/a.radial_subdivisions;s=x[i]+u*h
   if j==0:y,dy,ddy=Y[i],D[i],DD[i]
   elif j==a.radial_subdivisions:y,dy,ddy=Y[i+1],D[i+1],DD[i+1]
   else:
    y=np.polynomial.polynomial.polyval(u,co);dy=np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*co[1:])/h
    ddy=np.polynomial.polynomial.polyval(u,(np.arange(2,6)*np.arange(1,5))[:,None]*co[2:])/(h*h)
   _,tc,_=qc.jet(y);_,tcs,_=qc.jet(dy);_,tcss,_=qc.jet(ddy)
   speed=np.linalg.norm(tc,axis=1);speed_s=np.sum(tc*tcs,axis=1)/speed
   speed_ss=(np.sum(tcs*tcs+tc*tcss,axis=1)-speed_s**2)/speed
   b=speed.mean();bs=speed_s.mean();bss=speed_ss.mean();rate=bs/b;r,ap,app=profile(s);k=ap/r
   lam=r/b;lam_s=lam*(k-rate);lam_ss=lam*(app/r-bss/b-2*k*rate+2*rate*rate)
   qn,spec=fourier(speed);primitive,_=fourier(speed_s-rate*speed,-1);psi_s=-primitive/qn
   lower=float(qn.min()-np.pi/Q*2*np.sum(freqs*abs(spec)))
   minima['qN']=min(minima['qN'],float(qn.min()));minima['angle_positive_lower_at_sampled_s']=min(minima['angle_positive_lower_at_sampled_s'],lower)
   if qn.min()<=0:raise ValueError('The declared finite arclength coordinate is not positive on audit samples')
   F,t,e=qa.jet(y);V,t_s,_=qa.jet(dy);Acc,_,_=qa.jet(ddy)
   center=np.array([0.,0.,y[2*M+1]]);center_s=np.array([0.,0.,dy[2*M+1]]);center_ss=np.array([0.,0.,ddy[2*M+1]])
   Gs=lam*V+(1-lam)*center_s+lam_s*(F-center)
   Gss=lam*Acc+(1-lam)*center_ss+2*lam_s*(V-center_s)+lam_ss*(F-center)
   Gphi=lam*t;Gsphi=lam*t_s+lam_s*t;Gphiphi=lam*e
   newV=Gs+Gphi*psi_s[:,None];er=np.sum(newV*newV,axis=1)-1;gr=np.sum(t*t,axis=1)/(qn*qn)-1;fr=np.sum(newV*t,axis=1)/qn
   err=opnorm(er,gr,fr);jmax=int(np.argmax(err));location=dict(s=float(s),parent_angle=float(qa.angle[jmax]),cell=i,u=float(u))
   if err[jmax]>worst['value']:worst=dict(value=float(err[jmax]),**location,rr=float(er[jmax]),angular=float(gr[jmax]),mixed=float(fr[jmax]))
   target=(r*rho)**2;older=opnorm(np.sum(V*V,axis=1)-1,np.sum(t*t,axis=1)/target-1,np.sum(V*t,axis=1)/np.sqrt(target));jo=int(np.argmax(older))
   if older[jo]>old_worst['value']:old_worst=dict(value=float(older[jo]),s=float(s),parent_angle=float(qa.angle[jo]))
   E=np.sum(Gs*Gs,axis=1);mix=np.sum(Gs*Gphi,axis=1);G=np.sum(Gphi*Gphi,axis=1);det=E*G-mix*mix
   minima['scaled_image_gram_determinant']=min(minima['scaled_image_gram_determinant'],float(det.min()))
   normal=np.cross(Gs,Gphi);normal/=np.linalg.norm(normal,axis=1)[:,None]
   e2=np.sum(Gss*normal,axis=1);f2=np.sum(Gsphi*normal,axis=1);g2=np.sum(Gphiphi*normal,axis=1)
   trace=(e2*G+g2*E-2*f2*mix)/det;gauss=(e2*g2-f2*f2)/det;kap=(abs(trace)+np.sqrt(np.maximum(0,trace*trace-4*gauss)))/2;jk=int(np.argmax(kap))
   if kap[jk]>curve['value']:curve=dict(value=float(kap[jk]),s=float(s),parent_angle=float(qa.angle[jk]))
   values=dict(scale_minus_one=abs(lam-1),scale_s=abs(lam_s),scale_ss=abs(lam_ss),psi_s=max(abs(psi_s)),qN_speed_relative=max(abs(gr)),
    position_change=max(abs(lam-1)*np.linalg.norm(F-center,axis=1)),velocity_change=max(np.linalg.norm(newV-V,axis=1)),rr=max(abs(er)),angular=max(abs(gr)),mixed=max(abs(fr)))
   for key,value in values.items():maxima[key]=max(maxima[key],float(value))
   if core is None:
    qns,_=fourier(speed_s);qnphi,_=fourier(speed,1);C,_=fourier(speed_ss-bss/b*speed,-1);psi_ss=-(C+2*qns*psi_s+qnphi*psi_s*psi_s)/qn
    newAcc=Gss+2*Gsphi*psi_s[:,None]+Gphiphi*(psi_s*psi_s)[:,None]+Gphi*psi_ss[:,None]
    core=dict(value_change=float(max(abs(lam-1)*np.linalg.norm(F-center,axis=1))),first_jet_change=float(max(np.linalg.norm(newV-V,axis=1))),second_jet_change=float(max(np.linalg.norm(newAcc-Acc,axis=1))),psi_s=float(max(abs(psi_s))),psi_ss=float(max(abs(psi_ss))))
   samples+=Q
 report=dict(scope=__doc__,input_sha256=sha(a.input),source_sha256=sha(__file__),M=M,construction_angles=N,audit_angles=Q,radial_subdivisions=a.radial_subdivisions,
  quintic_cells=len(x)-1,sample_points=samples,new_gram=worst,parent_gram_same_samples=old_worst,new_principal_curvature=curve,maxima=maxima,minima=minima,core_common_jets=core,
  core_rho_sample_min=float(rho.min()),seconds=time.perf_counter()-start,
  limitations='Open prefix only. All radial extrema are sampled; angular positivity lower bounds apply only at sampled s. No global reach, closed completion, or mesh/frequency/t convergence is claimed.')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('input','out'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--construction-angles',type=int);p.add_argument('--angles',type=int,default=4096);p.add_argument('--radial-subdivisions',type=int,default=4)
 main(p.parse_args())
