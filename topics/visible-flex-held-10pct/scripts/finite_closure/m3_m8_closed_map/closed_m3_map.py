#!/usr/bin/env python3
"""Queryable finite C2 closed m3 map in explicit prefix/tail/pole charts.

The phase acts on physical material angle, not the computational warp angle.
The upper and lower pieces share one reflected Cartesian core, two identical
full cut functions, exact inner collar jets and ordinary Cartesian pole charts.
The reference rotational primitives are evaluated numerically by the original
factory. Their mathematical definition and continuous bounds are separate.

With marker_strength=0 the phase images are rigid rotations, hence delta_E=0.
A nonzero fixed compact cap marker is available as a separate fixed cap metric;
this module does not by itself certify the marker's strict noncongruence gate.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,math,subprocess,sys
import numpy as np
from m3_shared_prefix import load_prefix,M3SharedPrefix,M3CartesianPrefix,TailCutTarget,CartesianCutLift,circle
from phase_angle_chart import PhaseAngleChart

class Background:
    def __init__(self,source,checkpoint):
        cmd=['node',str(Path(__file__).with_name('background_query.mjs')),str(source),str(checkpoint)]
        self.process=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
        line=self.process.stdout.readline()
        if not line:raise RuntimeError('Background evaluator failed to initialize')
        self.info=json.loads(line);self.cache={}
        if not self.info.get('ready'):raise RuntimeError(self.info)
    def sample(self,R):
        R=float(R)
        if R not in self.cache:
            self.process.stdin.write(json.dumps({'radii':[R]})+'\n');self.process.stdin.flush()
            line=self.process.stdout.readline()
            if not line:raise RuntimeError('Background evaluator ended')
            result=json.loads(line)
            if 'error'in result:raise RuntimeError(result['error'])
            self.cache[R]=result['rows'][0]
        return self.cache[R]
    def close(self):
        if self.process.poll()is None:
            self.process.stdin.close();self.process.wait(timeout=10)

def rotation(v,phase):
    v=np.asarray(v);c,s=math.cos(phase),math.sin(phase)
    return np.stack([c*v[...,0]-s*v[...,1],s*v[...,0]+c*v[...,1],v[...,2]],axis=-1)

class ClosedM3Map:
    def __init__(self,source_topic,short_bridge,prefix_checkpoint,tail_checkpoint,port,
                 tail_manifest,tail_reader,cap_source,angular=512,marker_strength=0.):
        self.record,obj,flow,sol,_=load_prefix(source_topic,short_bridge,prefix_checkpoint,port,angular)
        base=M3SharedPrefix(obj,flow,sol,.04);self.prefix=M3CartesianPrefix(base,32)
        spec=importlib.util.spec_from_file_location('closed_m3_cap',cap_source);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        self.cap=mod.FiniteClosedTail(tail_manifest,tail_reader)
        self.target=TailCutTarget(self.prefix,self.cap)
        self.prefix.end_lift=CartesianCutLift(self.prefix,self.target,.04)
        self.phase_chart=PhaseAngleChart(self.prefix)
        self.background=Background(source_topic,tail_checkpoint)
        self.end=flow.end;self.a=float(self.cap.a);self.Rcut=self.target.R
        self.Zcap=self.target.zcut+self.target.mean+self.background.sample(self.a)['heightFromRToCut']
        self.marker_strength=float(marker_strength);self.marker_eta=.5;self.marker_radius=self.a/2
        if self.marker_strength<0:raise ValueError('Nonnegative fixed marker required')

    def prefix_jets(self,s,theta,phase=0.):
        """X,Xs,Xss,Xtheta,Xthetatheta,Xstheta; signed s crosses the core."""
        if abs(s)>self.end:raise ValueError('Outside prefix')
        sign=1 if s>=0 else-1;u=abs(float(s))
        psi=float(self.phase_chart.inverse(u,float(theta)-phase))
        X,Xs,Xss,Xp,Xpp,Xsp=self.prefix.point(u,psi)
        _,rho,rhop,ts,tss,rhos=self.phase_chart.angular(u,psi)
        v=ts/rho;vp=(rhos*rho-ts*rhop)/rho**2;vs=(tss*rho-ts*rhos)/rho**2
        Fs=Xs-v*Xp;Ft=Xp/rho
        Fss=Xss-2*v*Xsp+v*v*Xpp+(v*vp-vs)*Xp
        Ftt=Xpp/rho**2-Xp*rhop/rho**3;Fst=(Xsp-vp*Xp-v*Xpp)/rho
        jets=[X,Fs,Fss,Ft,Ftt,Fst];flip=np.array([1,1,sign])
        for j in range(6):jets[j]=rotation(jets[j],phase)*flip*(sign if j in [1,5] else 1)
        return tuple(jets)

    def marker(self,x,y):
        r2=x*x+y*y;rc2=self.marker_radius**2;eps=self.marker_strength;eta=self.marker_eta
        if r2>=rc2 or eps==0:return 0.,np.zeros(2),np.zeros((2,2))
        p=1-r2/rc2;b=(1+eta)*x*x+(1-eta)*y*y
        gp=-2*np.array([x,y])/rc2;Hp=-2*np.eye(2)/rc2
        gb=2*np.array([(1+eta)*x,(1-eta)*y]);Hb=2*np.diag([1+eta,1-eta])
        value=eps*p**3*b;grad=eps*(3*p*p*b*gp+p**3*gb)
        Hess=eps*(6*p*b*np.outer(gp,gp)+3*p*p*b*Hp+3*p*p*(np.outer(gp,gb)+np.outer(gb,gp))+p**3*Hb)
        return value,grad,Hess

    def disk_jets(self,x,y,side=1):
        """Regular Cartesian pole chart X,DX,D2X; fixed at every phase."""
        if side not in [-1,1]or x*x+y*y>self.a*self.a:raise ValueError('Outside a cap disk')
        z,g,H=self.marker(float(x),float(y))
        X=np.array([x,y,side*(self.Zcap+z)])
        J=np.array([[1,0],[0,1],[side*g[0],side*g[1]]])
        Q=np.zeros((3,2,2));Q[2]=side*H
        return X,J,Q

    def tail_jets(self,R,theta,side=1,phase=0.):
        """X,XR,XRR,Xtheta,Xthetatheta,XRtheta on tail/collar/disk polar charts."""
        R=float(R);theta=float(theta)
        if side not in [-1,1]or R<0 or R>self.Rcut:raise ValueError('Outside closed tail')
        if R<=self.a:
            er=circle(theta);et=circle(theta,1);x,y=R*er[:2];f,g,H=self.marker(x,y)
            jets=[np.array([x,y,self.Zcap+f]),er.copy(),np.zeros(3),R*et,-R*er,et.copy()]
            jets[1][2]=g@er[:2];jets[2][2]=er[:2]@H@er[:2]
            jets[3][2]=R*(g@et[:2]);jets[4][2]=R*R*(et[:2]@H@et[:2])-R*(g@er[:2])
            jets[5][2]=R*(er[:2]@H@et[:2])+g@et[:2]
            return tuple(z*np.array([1,1,side])for z in jets)
        phi=theta-phase;bg=self.background.sample(R)
        rr,r1,r2=self.target.perturbation_radius(R)
        if R==self.Rcut:
            A=self.target.A
            V,Vr,Vrr=[self.target.fourier(c,[phi],0)[0]for c in A]
            Vt,Vtt=[self.target.fourier(A[0],[phi],j)[0]for j in [1,2]]
            Vrt=self.target.fourier(A[1],[phi],1)[0]
        else:
            V,Vr,Vt,Vrr,Vrt,Vtt=self.cap.perturbation_jets(rr,phi)
        d1=Vr*r1;d2=Vrr*r1*r1+Vr*r2;dt=Vrt*r1
        flip=np.array([1,1,-1.]);er=circle(phi);et=circle(phi,1)
        X=R*er+V*flip;X[2]+=self.target.zcut+self.target.mean+bg['heightFromRToCut']
        XR=er+d1*flip;XR[2]-=bg['w']
        XRR=d2*flip;XRR[2]-=bg['wr']
        Xt=R*et+Vt*flip;Xtt=-R*er+Vtt*flip;XRt=et+dt*flip
        return tuple(rotation(x,phase)*np.array([1,1,side])for x in [X,XR,XRR,Xt,Xtt,XRt])

    def close(self):self.background.close()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ['source-topic','short-bridge','prefix-checkpoint','tail-checkpoint','port','tail-manifest','tail-reader','cap-source','out']:p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--marker-strength',type=float,default=0.)
    a=p.parse_args();model=ClosedM3Map(a.source_topic,a.short_bridge,a.prefix_checkpoint,a.tail_checkpoint,a.port,a.tail_manifest,a.tail_reader,a.cap_source,marker_strength=a.marker_strength)
    maximum=np.zeros(6);rows=[];prefix_queries=0
    try:
        for phase in [0.,.17,math.pi/3]:
            for side in [-1,1]:
                for theta in [0.,.123,1.1,2.4,4.7]:
                    P=model.prefix_jets(side*model.end,theta,phase);T=model.tail_jets(model.Rcut,theta,side,phase)
                    ap,app=model.target.ap,model.target.app
                    common=[T[0],T[1]*side*ap,T[2]*ap*ap+T[1]*app,T[3],T[4],T[5]*side*ap]
                    maximum=np.maximum(maximum,[np.linalg.norm(p-t)for p,t in zip(P,common)])
                for s in [0.,.02,.3,model.end]:
                    jets=model.prefix_jets(side*s,.34,phase)
                    if not all(np.all(np.isfinite(z))for z in jets):raise ValueError('Nonfinite prefix query')
                    prefix_queries+=1
                for R in [model.Rcut,.2,.08,float(model.cap.b),(model.a+float(model.cap.b))/2,model.a,0.]:
                    jets=model.tail_jets(R,.34,side,phase)
                    if not all(np.all(np.isfinite(z))for z in jets):raise ValueError('Nonfinite tail query')
                    rows.append(dict(phase=phase,side=side,radius=R,point=np.asarray(jets[0],float).tolist()))
        maximum=np.asarray(maximum,dtype=float)
        pole=model.disk_jets(0,0,1)[0]
        report=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            inputs={str(q.resolve()):hashlib.sha256(q.read_bytes()).hexdigest()for q in [a.prefix_checkpoint,a.tail_checkpoint,a.port,a.tail_manifest]},
            phases=[0.,.17,math.pi/3],shared_cut_six_jet_numeric_errors=maximum.tolist(),
            numeric_cap_height=model.Zcap,pole=pole.tolist(),marker_strength=a.marker_strength,
            tail_point_query_count=len(rows),prefix_point_query_count=prefix_queries,finite_queries_all_successful=True,
            background_evaluation=model.background.info,
            explicit_c2_phase_chart=model.phase_chart.report(),
            exact_map_definition='Frozen finite shared Hermite/Fourier functions; literal core/end Hermite lifts; exact fixed-background real integrals; upper whole-z reflection plus one vertical translation; lower full-z mirror; physical-angle phase; Cartesian disks.',
            delta_E_asserted=False,continuous_geometry_is_separate_certificate=True)
        a.out.write_text(json.dumps(report,indent=2)+'\n')
        # These sample coordinates are scratch-only diagnostic outputs.
        a.out.with_name(a.out.stem+'-points.json').write_text(json.dumps(rows,indent=2)+'\n')
        print(json.dumps({'shared_cut_six_jet_errors':maximum.tolist(),'cap_height_approx':model.Zcap,'all_queries':len(rows),'marker':a.marker_strength}))
    finally:model.close()

if __name__=='__main__':main()
