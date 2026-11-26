#!/usr/bin/env python3
"""Small new-design Cartesian solve on the actual R137-to-R205 connector.

This is not the previous 1025-column strong-field objective. The metric uses
all E/F/G entries, while every trial retains complete endpoint two jets.
The scalar radius is still a design variable; no same-g refinement is claimed.
Curvature is observed from the actual position, not silently constrained by a
reference-frame proxy. All raw states/reports must remain outside the repo.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial,Legendre

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('connector',HERE/'6a65-geometry-r137-two-connectors.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)


class Model:
    def __init__(self,raw,angles=64,radials=20,radial_modes=6,angular_max=8,metric_tau=.1,L=.75,Z=.56,coast_length=.35,
                 curvature_weight=0.,geometry_weight=10.,profile_weight=1.):
        self.raw=raw;self.angles=angles;self.radials=radials;self.metric_tau=metric_tau;self.L=L;self.Z=Z;self.coast_length=coast_length
        self.curvature_weight=curvature_weight;self.geometry_weight=geometry_weight;self.profile_weight=profile_weight
        self.radial_modes=radial_modes;self.angular_max=angular_max
        self.u=2*np.pi*np.arange(angles)/angles
        self.aq=raw['inheritedGapLengthDesign']['centralSeed']['actualCentralA']
        curve=c.core.Curve([p['X'] for p in raw['points']],96,planar=True)
        self.left=c.ruling_port(curve,.003,coast_length,self.u)
        self.right=c.r205_port(raw['tailAmplitude'],Z,self.u)
        nodes,weights=np.polynomial.legendre.leggauss(radials);self.t=(nodes+1)/2
        self.weight=np.repeat(weights/2,angles)/angles
        self.base={k:[] for k in ['X','Xs','Xu','Xss','Xsu','Xuu','f','fs','fss']}
        for t in self.t:
            packet=c.connector_at(float(t),L,self.left,self.right)
            for k in self.base:
                self.base[k].append(packet[k] if k.startswith('X') else np.full(angles,packet[k]))
        self.base={k:np.concatenate(v) for k,v in self.base.items()}
        self.radial=[]
        bubble=64*Polynomial([0,0,0,1,-3,3,-1])
        for j in range(radial_modes):
            polynomial=bubble*Legendre.basis(j).convert(kind=Polynomial)(Polynomial([-1,2]))
            self.radial.append([polynomial(self.t),polynomial.deriv()(self.t)/L,polynomial.deriv(2)(self.t)/L**2])
        columns=[]
        for component in range(3):
            modes=list(range(1,angular_max,2)) if component<2 else list(range(0,angular_max+1,2))
            for j in range(radial_modes):
                for mode in modes:columns.append((component,j,mode))
        self.columns=columns;self.position_columns=len(columns);self.n=self.position_columns+4
        count=angles*radials
        self.J={key:np.zeros((count,self.n,3)) for key in ['X','Xs','Xu','Xss','Xsu','Xuu']}
        self.Jf=np.zeros((count,self.n));self.Jfs=np.zeros_like(self.Jf);self.Jfss=np.zeros_like(self.Jf)
        for index,(component,j,mode) in enumerate(columns):
            if component==1:phi=np.sin(mode*self.u);phiu=mode*np.cos(mode*self.u)
            else:phi=np.cos(mode*self.u);phiu=-mode*np.sin(mode*self.u)
            phiuu=-mode*mode*phi;b,bs,bss=self.radial[j]
            for key,pair in [('X',(b,phi)),('Xs',(bs,phi)),('Xu',(b,phiu)),('Xss',(bss,phi)),('Xsu',(bs,phiu)),('Xuu',(b,phiuu))]:
                self.J[key][:,index,component]=(pair[0][:,None]*pair[1]).ravel()
        for j in range(4):
            self.Jf[:,self.position_columns+j]=np.repeat(self.radial[j][0],angles)
            self.Jfs[:,self.position_columns+j]=np.repeat(self.radial[j][1],angles)
            self.Jfss[:,self.position_columns+j]=np.repeat(self.radial[j][2],angles)

    def jets(self,z):
        out={key:self.base[key]+np.einsum('nji,j->ni',jac,z) for key,jac in self.J.items()}
        out.update(f=self.base['f']+self.Jf@z,fs=self.base['fs']+self.Jfs@z,fss=self.base['fss']+self.Jfss@z)
        return out

    def evaluate(self,z,normal=False):
        p=self.jets(z);X,S,U=p['X'],p['Xs'],p['Xu'];f=p['f'];count=len(f)
        if np.min(f)<=.1:raise ValueError('Radius design became nonpositive')
        E=np.sum(S*S,axis=1);F=np.sum(S*U,axis=1);G=np.sum(U*U,axis=1)
        e=E-1;ff=F/f;g=G/f**2-1;q=e*e+2*ff*ff+g*g;h=np.sqrt(1+q/self.metric_tau**2)
        w=np.sqrt(self.weight);res=[w*h*e,w*np.sqrt(2)*h*ff,w*h*g];jac=[]
        if normal:
            dE=2*np.einsum('ni,nji->nj',S,self.J['Xs']);dF=np.einsum('ni,nji->nj',U,self.J['Xs'])+np.einsum('ni,nji->nj',S,self.J['Xu'])
            dG=2*np.einsum('ni,nji->nj',U,self.J['Xu']);de=dE;dff=dF/f[:,None]-F[:,None]*self.Jf/f[:,None]**2
            dg=dG/f[:,None]**2-2*G[:,None]*self.Jf/f[:,None]**3
            dq=2*e[:,None]*de+4*ff[:,None]*dff+2*g[:,None]*dg;dh=dq/(2*self.metric_tau**2*h[:,None])
            jac=[w[:,None]*(h[:,None]*de+e[:,None]*dh),np.sqrt(2)*w[:,None]*(h[:,None]*dff+ff[:,None]*dh),w[:,None]*(h[:,None]*dg+g[:,None]*dh)]
        def add_hinge(value,derivative=None,scale=None):
            if scale is None:scale=self.geometry_weight
            active=value>0;res.append(w*scale*np.maximum(value,0))
            if normal:jac.append(w[:,None]*scale*active[:,None]*derivative)
        radius=np.linalg.norm(X,axis=1);width=np.abs(X[:,1]);rxy=np.linalg.norm(X[:,:2],axis=1)
        d_radius=np.einsum('ni,nji->nj',X,self.J['X'])/radius[:,None] if normal else None
        d_width=np.sign(X[:,1,None])*self.J['X'][:,:,1] if normal else None
        add_hinge(radius-1.59,d_radius);add_hinge(width-.885,d_width)
        qh=np.clip((rxy-.52)/.02,0,1);allowance=.0195*(10*qh**3-15*qh**4+6*qh**5)
        if normal:
            d_rxy=np.einsum('ni,nji->nj',X[:,:2],self.J['X'][:,:,:2])/np.maximum(rxy[:,None],1e-12)
            slope=.0195/.02*30*qh**2*(1-qh)**2
            d_height=self.J['X'][:,:,2]-slope[:,None]*d_rxy
        else:d_height=None
        add_hinge(X[:,2]-self.Z-allowance,d_height)
        held_values=[]
        for sign in [-1,1]:
            delta=X-np.array([0,sign*self.aq,0]);distance=np.linalg.norm(delta,axis=1);held_values.append(distance)
            dd=-np.einsum('ni,nji->nj',delta,self.J['X'])/distance[:,None] if normal else None
            add_hinge(.65-distance,dd)
        add_hinge(.7-f,-self.Jf if normal else None,scale=10.)
        add_hinge(np.abs(p['fs'])-1,np.sign(p['fs'])[:,None]*self.Jfs if normal else None,scale=self.profile_weight)
        area_vector=np.cross(S,U);area=np.linalg.norm(area_vector,axis=1)
        if np.min(area)<=1e-10:raise ValueError('Cartesian trial contains a sampled nonimmersion')
        own=area_vector/area[:,None];bss=np.sum(own*p['Xss'],axis=1);bsu=np.sum(own*p['Xsu'],axis=1);buu=np.sum(own*p['Xuu'],axis=1)
        det=E*G-F*F;trace=(G*bss-2*F*bsu+E*buu)/det;gauss=(bss*buu-bsu**2)/det
        curvature=np.abs(trace)/2+np.sqrt(np.maximum(0,trace**2/4-gauss))
        if self.curvature_weight>0:
            if normal:
                darea=np.cross(self.J['Xs'],U[:,None,:])+np.cross(S[:,None,:],self.J['Xu'])
                dn=(darea-own[:,None,:]*np.einsum('ni,nji->nj',own,darea)[:,:,None])/area[:,None,None]
                dbss=np.einsum('nji,ni->nj',dn,p['Xss'])+np.einsum('ni,nji->nj',own,self.J['Xss'])
                dbsu=np.einsum('nji,ni->nj',dn,p['Xsu'])+np.einsum('ni,nji->nj',own,self.J['Xsu'])
                dbuu=np.einsum('nji,ni->nj',dn,p['Xuu'])+np.einsum('ni,nji->nj',own,self.J['Xuu'])
                ddet=G[:,None]*dE+E[:,None]*dG-2*F[:,None]*dF
                dtrace=(bss[:,None]*dG+G[:,None]*dbss-2*bsu[:,None]*dF-2*F[:,None]*dbsu+buu[:,None]*dE+E[:,None]*dbuu-trace[:,None]*ddet)/det[:,None]
                dgauss=(buu[:,None]*dbss+bss[:,None]*dbuu-2*bsu[:,None]*dbsu-gauss[:,None]*ddet)/det[:,None]
                disc=np.sqrt(np.maximum(0,trace**2/4-gauss))
                dcurvature=.5*np.sign(trace)[:,None]*dtrace+(trace[:,None]*dtrace/2-dgauss)/(2*np.maximum(disc[:,None],1e-12))
            else:dcurvature=None
            add_hinge(curvature-9.5,dcurvature,scale=self.curvature_weight)
        metric=np.abs(e+g)/2+np.sqrt(((e-g)/2)**2+ff*ff)
        r=np.concatenate(res);cost=float(r@r)
        report=dict(R2=cost,metricIntegral=float(self.weight@q),maximumRelativeMetric=float(np.max(metric)),maximumOwnCurvature=float(np.max(curvature)),
            maximumAbsEError=float(np.max(np.abs(e))),maximumAbsNormalizedF=float(np.max(np.abs(ff))),maximumAbsGError=float(np.max(np.abs(g))),
            minimumArea=float(np.min(area)),minimumHeld=float(np.min(held_values)),maximumRadius=float(np.max(radius)),maximumAbsY=float(np.max(width)),
            maximumHeightExcess=float(np.max(X[:,2]-self.Z-allowance)),maximumZ=float(np.max(X[:,2])),minimumZ=float(np.min(X[:,2])),
            minimumRadiusProfile=float(np.min(f)),maximumRadiusProfile=float(np.max(f)),maximumAbsProfileSlope=float(np.max(np.abs(p['fs']))))
        if normal:
            J=np.concatenate(jac);report.update(residual=r,jacobian=J,gradient=J.T@r,normal=J.T@J)
        return report


def plain(x):return {k:v for k,v in x.items() if not isinstance(v,np.ndarray)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source_samples');ap.add_argument('output_prefix');ap.add_argument('--steps',type=int,default=6)
    ap.add_argument('--input-state');ap.add_argument('--direction-check',action='store_true')
    ap.add_argument('--curvature-weight',type=float,default=0.);ap.add_argument('--geometry-weight',type=float,default=10.)
    ap.add_argument('--profile-weight',type=float,default=1.);ap.add_argument('--coast-length',type=float,default=.35)
    ap.add_argument('--right-length',type=float,default=.75);ap.add_argument('--cut-height',type=float,default=.56)
    ap.add_argument('--radial-modes',type=int,default=6);ap.add_argument('--angular-max',type=int,default=8)
    ap.add_argument('--angles',type=int,default=64);ap.add_argument('--radials',type=int,default=20)
    args=ap.parse_args();start=time.time();prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output required')
    raw=json.loads(Path(args.source_samples).read_text());model=Model(raw,curvature_weight=args.curvature_weight,
        geometry_weight=args.geometry_weight,profile_weight=args.profile_weight,coast_length=args.coast_length,L=args.right_length,Z=args.cut_height);z=np.zeros(model.n)
    if args.radial_modes!=6 or args.angular_max!=8 or args.angles!=64 or args.radials!=20:
        model=Model(raw,curvature_weight=args.curvature_weight,geometry_weight=args.geometry_weight,profile_weight=args.profile_weight,
            coast_length=args.coast_length,L=args.right_length,Z=args.cut_height,radial_modes=args.radial_modes,angular_max=args.angular_max,
            angles=args.angles,radials=args.radials);z=np.zeros(model.n)
    if args.input_state:
        old=json.loads(Path(args.input_state).read_text());oz=np.asarray(old['z']);om=old['model'];old_columns=[]
        for component in range(3):
            modes=list(range(1,om.get('angularMax',8),2)) if component<2 else list(range(0,om.get('angularMax',8)+1,2))
            for j in range(om.get('radialModes',6)):
                for mode in modes:old_columns.append((component,j,mode))
        index={entry:j for j,entry in enumerate(model.columns)}
        for j,entry in enumerate(old_columns):
            if entry not in index and oz[j]!=0:raise ValueError('Cannot discard a nonzero old Cartesian column')
            if entry in index:z[index[entry]]=oz[j]
        z[model.position_columns:]=oz[len(old_columns):]
    initial=model.evaluate(z);history=[];check=None;damping=.001
    if args.direction_check:
        p=model.evaluate(z,True);rng=np.random.default_rng(671203);direction=rng.normal(size=model.n);direction/=np.linalg.norm(direction);eps=1e-7
        plus=model.evaluate(z+eps*direction,True);minus=model.evaluate(z-eps*direction,True)
        fd=(plus['residual']-minus['residual'])/(2*eps);an=p['jacobian']@direction
        check={'epsilon':eps,'relativeResidualDirectionError':float(np.linalg.norm(fd-an)/max(1,np.linalg.norm(fd))),
               'gradientDirectionalIdentity':float(abs(float(p['gradient']@direction)-float(p['residual']@an))/max(1,abs(float(p['gradient']@direction))))}
    for step in range(args.steps):
        packet=model.evaluate(z,True);normal,gradient=packet['normal'],packet['gradient'];diag=np.maximum(np.diag(normal),1e-10)
        trials=[];accepted=False
        for attempt in range(6):
            dz=np.linalg.solve(normal+damping*np.diag(diag),-gradient)
            for alpha in [1.,.5,.25,.125,.0625,.03125]:
                trial_z=z+alpha*dz
                try:trial=model.evaluate(trial_z);record=dict(alpha=alpha,damping=damping,R2=trial['R2'])
                except (ValueError,FloatingPointError) as exc:trials.append(dict(alpha=alpha,damping=damping,error=str(exc)));continue
                trials.append(record)
                if trial['R2']<packet['R2']:
                    z=trial_z;accepted=True;damping=max(1e-8,damping/3);break
            if accepted:break
            damping*=10
        item=dict(step=step+1,accepted=accepted,before=plain(packet),after=plain(model.evaluate(z)),trials=trials)
        history.append(item)
        state=dict(schema='6a65-new-Cartesian-R137-connector-design-state-v1',z=z.tolist(),model=dict(angles=model.angles,radials=model.radials,
            columns=model.n,positionColumns=model.position_columns,radiusDesignColumns=4,metricTau=model.metric_tau,rightLength=model.L,trueCutHeight=model.Z,
            curvatureWeight=model.curvature_weight,geometryWeight=model.geometry_weight,profileWeight=model.profile_weight,coastLength=model.coast_length,
            radialModes=model.radial_modes,angularMax=model.angular_max),
            acceptedSteps=sum(x['accepted'] for x in history),last=item['after'],continuousCertificate=False,curvatureOnlyObserved=model.curvature_weight==0)
        Path(str(prefix)+f'-step{step+1}-state.json').write_text(json.dumps(state)+'\n')
        print(json.dumps(dict(step=step+1,accepted=accepted,**item['after'])),flush=True)
        if not accepted:break
    report=dict(schema='6a65-new-R137-Cartesian-connector-metric-LM-v1',initial=initial,directionCheck=check,history=history,
        final=plain(model.evaluate(z)),columns=model.n,positionColumns=model.position_columns,radiusDesignColumns=4,
        sourceSHA256=hashlib.sha256(Path(args.source_samples).read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        curvatureConstraintInObjective=model.curvature_weight>0,curvatureOnlyObserved=model.curvature_weight==0,completeMetricUsesAllThreeComponents=True,
        fixedEndpointTwoJets=True,newMetricDesignNotSameGRefinement=True,seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(exitSummary=report['final'],seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
