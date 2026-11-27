"""RHI complete relative parameter carriers; definitions only at import.

The public owner supplies unchanged directed Box/CBox/FFT, whole original
NP arrays and complete scalar jets. No old residual, norm or pairing is
called. All new scientific operations run inside the public child.
"""
from fractions import Fraction
from math import ceil

GRID,ORDER,RADIAL_DEGREE=2048,6,3
STRIPS=(Fraction(1,256),Fraction(1,128),Fraction(1,64))
TARGETS=('complete_same_selected_trial_relative_mean6',
    'complete_same_selected_relative_profile_error4',
    'complete_true_strict_nu_relative_mean6',
    'complete_true_strict_nu_relative_profile_error2')
ZERO_MEANS=(0,2,4)


def require(ok,message):
    if not ok:raise ValueError(message)


def full_plan(original):
    out=[]
    for index,item in enumerate(original):
        left,right=map(Fraction,item['interval'])
        count=max(1,ceil((right-left)*8192))
        for k in range(count):
            lo=left+(right-left)*k/count;hi=left+(right-left)*(k+1)/count
            out.append(dict(item,interval=[str(lo),str(hi)],original_cell=index))
    require(len(original)==2472 and len(out)<3948 and out[0]['interval'][0]=='0'
        and out[-1]['interval'][1]=='9/50'
        and all(x['interval'][1]==y['interval'][0] for x,y in zip(out,out[1:])),
        'all original2472 cells retained under exact subdivision')
    return out


class Fields:
    def __init__(self,c,core,nu):
        self.c,self.core,self.nu=c,core,nu
        self.F=core.BatchRadialFourier

    def cut(self,f):
        c=self.c;z=f.Fourier();n=min(len(f.coefficients),RADIAL_DEGREE+1)
        tail=c.wiener(z[:,n:,:]) if n<len(f.coefficients) else c.Box(0.)
        kept=z[:,:n,:]
        out=self.F(c,f.coefficients[:n],f.degree,c.wiener(kept),
            c.add_upper(f.error,tail),max(f.error_degree,f.degree if n<len(f.coefficients) else 0))
        out._fourier=kept
        return out

    def product(self,*values):
        result=values[0]
        for value in values[1:]:result=self.cut(result*value)
        return result

    def reciprocal(self,f):
        c=self.c
        require(f.degree==0,'only complete radial scalars are inverted')
        interval=f.scalar_range()
        require(c.np.all(interval.lo>0) or c.np.all(interval.hi<0),
                'whole original/selected scalar excludes zero')
        lower=min(abs(float(interval.lo[0])),abs(float(interval.hi[0])))
        cs=f.coefficients;q=[c.Box(1.)/cs[0]]
        for k in range(1,RADIAL_DEGREE+1):
            q.append(-sum((cs[j]*q[k-j] for j in range(1,min(k,len(cs)-1)+1)),
                          c.Box(c.np.zeros((1,1))))/cs[0])
        candidate=self.F.scalar(c,q)
        residual=self.cut(1-self.product(f,candidate))
        error=c.upper(c.add_upper(residual.norm,residual.error)/c.Box(lower))
        return self.F(c,candidate.coefficients,0,candidate.norm,error,0)

    def radius(self,row,left,right,read_ball):
        c=self.c;values=[]
        for jets in (row['intrinsic_midpoint_jets'],row['intrinsic_whole_third_jets']):
            a,b,b1,b2=(read_ball(jets[n]) for n in ('a','beta','beta1','beta2'))
            values.append([a,a*b,a*(b1+b*b)/2,a*(b2+3*b*b1+b*b*b)/6])
        coefficients=values[0][:3]+[values[1][3]]
        lo,hi=map(Fraction,row['interval']);middle,half=(lo+hi)/2,(hi-lo)/2
        points,error=[],c.arb(0)
        for k,value in enumerate(coefficients):
            chosen=float(value.mid());require(c.np.isfinite(chosen),'finite radius coefficient')
            difference=value-c.arb(chosen)
            error+=max(abs(difference.lower()),abs(difference.upper()))*c.exact(half)**k
            points.append(c.Box(chosen))
        cs=c.affine_polynomial(points,(left+right)/2-middle,(right-left)/2)
        return self.F.scalar(c,cs,c.arb_box(error.upper()).hi)

    def selected(self,f):
        c=self.c
        out=self.F(c,f.coefficients,96,f.norm,c.add_upper(f.error,c.box(Fraction(1,500000000))),96)
        out._fourier=f._fourier
        return out

    def make(self,base,offsets,row,item,nodes,jets,read_ball):
        c,core,nu=self.c,self.core,self.nu
        left,right=map(Fraction,item['interval'])
        scalar={name:core.scalar_taylor(c,row['intrinsic_midpoint_jets'],
            row['intrinsic_whole_third_jets'],name,*row['interval'],left,right,read_ball)
            for name in ('beta','K','gamma','s')}
        background=nu.base_background(c,core,base,offsets,item['background_piece'],left,right,scalar['s'])
        u,v=(self.selected(f) for f in background)
        scalar=core.selected_intrinsic_fees(c,scalar,row['intrinsic_whole_third_jets'],
                    Fraction(1,10000000000),left>=nu.A,read_ball)
        beta,K,gamma=(self.cut(scalar[n]) for n in ('beta','K','gamma'))
        a=self.cut(self.radius(row,left,right,read_ball))
        inva,invg=self.reciprocal(a),self.reciprocal(gamma)
        m=self.cut(v.mean());invm=self.reciprocal(m)
        index=item['trial_piece']
        cs=core.hermite_coefficients(c,[c.Box(jets[k][index,:,None]) for k in range(4)],
            [c.Box(jets[k][index+1,:,None]) for k in range(4)],c.exact(nodes[index+1]-nodes[index]))
        cs=core.restrict_trial_coefficients(c,cs,c.exact(nodes[index]),
            c.exact(nodes[index+1]-nodes[index]),left,right)
        h1,h2=(self.cut(f) for f in core.reflection_polynomial(c,cs))
        mean=self.cut(h2.mean());P=self.product
        vv=P(v,v)
        d=-P(beta,self.cut(P(u,u)+P(K,vv)).primitive())
        J=P(v,invm)
        tau=self.cut(P(d,J)-P(gamma,u))
        p=P(beta,tau,invg)
        k=P(a,self.cut(P(gamma,K,v)+P(d,u,invm)))
        t=P(a,d,invm)
        w,wp=(self.cut(f) for f in nu.control_fields(c,core,left,right))
        T=P(beta,inva,inva,invg,invg)*Fraction(1,2)
        gn=P(w,gamma)*Fraction(1,2)
        Kn=self.cut(-P(w,K)+P(T,wp))
        dd=self.cut(-2*P(beta,self.cut(P(u,h1)+P(K,v,h2)).primitive())
                    -P(beta,Kn,vv.primitive()))
        dJ=P(self.cut(h2-P(J,mean)),invm)
        dtau=self.cut(P(J,dd)+P(d,dJ)-P(gamma,h1)-P(gn,u))
        dp=self.cut(P(beta,dtau,invg)-P(beta,tau,gn,invg,invg))
        dk=P(a,self.cut(P(gamma,K,h2)+P(self.cut(P(gn,K)+P(gamma,Kn)),v)
                        +P(u,dd,invm)+P(d,h1,invm)-P(d,u,mean,invm,invm)))
        dt=P(a,self.cut(P(dd,invm)-P(d,mean,invm,invm)))
        zero=self.F.scalar(c,[0.])
        fields=[t,-k,p,P(a,gamma),P(a,tau),zero,dt,-dk,dp,P(a,gn),P(a,dtau),zero]
        fields=[self.cut(f) for f in fields]
        require(all(f.degree<=288 and f.error_degree<=288 and len(f.coefficients)<=4 for f in fields),
                'complete selected state/metric/mean support and radial remainder')
        return fields


def stack(c,values,axis=0):
    return c.Box(c.np.stack([v.lo for v in values],axis=axis),
                 c.np.stack([v.hi for v in values],axis=axis))


def mm(c,a,b):
    return stack(c,[stack(c,[sum((a[...,i,k]*b[...,k,j] for k in range(3)),c.Box(0.))
        for j in range(3)],axis=-1) for i in range(3)],axis=-2)


def mv(c,a,b):
    return stack(c,[sum((a[...,i,k]*b[...,k] for k in range(3)),c.Box(0.))
        for i in range(3)],axis=-1)


def cross(c,a,b):
    return stack(c,[a[...,1]*b[...,2]-a[...,2]*b[...,1],
        a[...,2]*b[...,0]-a[...,0]*b[...,2],a[...,0]*b[...,1]-a[...,1]*b[...,0]],axis=-1)


def skew(c,v):
    z=c.Box(c.np.zeros(v.lo.shape[:-1]))
    return stack(c,[stack(c,[z,-v[...,2],v[...,1]],-1),
        stack(c,[v[...,2],z,-v[...,0]],-1),stack(c,[-v[...,1],v[...,0],z],-1)],-2)


def maxnorm(c,value):
    absolute=c.Box(value.abs_upper());square=absolute*absolute
    while square.lo.ndim>1:square=c.reduce_box(square,axis=-1)
    upper=float(c.np.max(square.hi))
    require(c.np.isfinite(upper) and upper>=0,'finite full grid Euclidean/Frobenius norm')
    return c.arb(upper).sqrt().upper()


def convolution(a,b,op,zero):
    out=[]
    for k in range(len(a)+len(b)-1):
        result=zero()
        for i in range(max(0,k-len(b)+1),min(k,len(a)-1)+1):result=result+op(a[i],b[k-i])
        out.append(result)
    return out


def residual_integral(c,values,rhs,length):
    ds=[values[k]*k for k in range(1,len(values))]
    bound=c.arb(0)
    for k in range(max(len(ds),len(rhs))):
        value=(ds[k] if k<len(ds) else c.Box(0.))+(rhs[k] if k<len(rhs) else c.Box(0.))*c.box(length)
        bound+=maxnorm(c,value)/(k+1)
    return bound.upper()


def polynomial_bound(c,values):
    return sum((maxnorm(c,v) for v in values),c.arb(0)).upper()


def proposal(np,start,source,length):
    midpoint=source.lo/2+source.hi/2
    require(np.all(np.isfinite(midpoint)),'finite chosen source coefficients')
    source=[midpoint[k] for k in range(midpoint.shape[0])]
    m,vel,dm,dvel=([x[:,i:i+3] for x in source] for i in (0,3,6,9))
    def omega(v):
        out=np.zeros((GRID,3,3))
        out[:,0,1],out[:,0,2],out[:,1,0]=-v[:,2],v[:,1],v[:,2]
        out[:,1,2],out[:,2,0],out[:,2,1]=-v[:,0],-v[:,1],v[:,0]
        return out
    M=list(map(omega,m))
    A=[start[:,:9].reshape(GRID,3,3).copy()]
    x=[start[:,9:12].copy()];u=[start[:,12:15].copy()];y=[start[:,15:18].copy()]
    fmv=lambda a,b:np.einsum('nij,nj->ni',a,b)
    fmm=lambda a,b:np.einsum('nij,njk->nik',a,b)
    d=float(length)
    for n in range(ORDER):
        adot=np.zeros((GRID,3,3));xdot=np.zeros((GRID,3));udot=np.zeros((GRID,3));ydot=np.zeros((GRID,3))
        for i in range(n+1):
            j=n-i
            if j<len(M):adot+=fmm(A[i],M[j])
            if j<len(vel):xdot+=fmv(A[i],vel[j]);udot+=fmv(A[i],dm[j]);ydot+=fmv(A[i],dvel[j])
            for j in range(n-i+1):
                k=n-i-j
                if k<len(vel):ydot+=np.cross(u[i],fmv(A[j],vel[k]))
        A.append(-d*adot/(n+1));x.append(-d*xdot/(n+1))
        u.append(-d*udot/(n+1));y.append(-d*ydot/(n+1))
    coefficients=[np.concatenate((a.reshape(GRID,9),xx,uu,yy),axis=1) for a,xx,uu,yy in zip(A,x,u,y)]
    endpoint=np.sum(np.stack(coefficients,axis=0),axis=0)
    require(all(np.all(np.isfinite(z)) for z in coefficients) and np.all(np.isfinite(endpoint)),
            'finite whole dyadic proposal')
    return coefficients,endpoint


class Integrator:
    def __init__(self,c,core,nu,base,offsets,rows,nodes,original_plan,jets,read_ball):
        self.c,self.core,self.nu=c,core,nu
        self.base,self.offsets,self.rows,self.nodes,self.jets,self.read_ball=base,offsets,rows,nodes,jets,read_ball
        self.plan=full_plan(original_plan);self.fields=Fields(c,core,nu)
        self.state=c.np.zeros((GRID,18));self.state[:,:9]=c.np.eye(3).reshape(1,9)
        self.errors=[c.arb(0) for _ in range(4)]
        self.strip_integrals=[[c.arb(0) for _ in range(4)] for _ in STRIPS]
        self.impulses=[c.arb(0) for _ in range(4)]
        self.cells=0;self.edge=Fraction(9,50);self.maximum_support=0;self.weights=[]
        for sigma in STRIPS:
            values=[c.arb_box((4*abs(int(j))*c.exact(sigma)).exp()).hi for j in c.modes]
            self.weights.append(c.Box(c.np.asarray(values).reshape(core.GRID,1,1)))
        self.error_weights={}

    def source(self,fields):
        c=self.c;z=c.zeros((GRID,4,12));strips=[]
        for j,f in enumerate(fields):
            old=f.Fourier();n=old.real.lo.shape[1]
            z[:self.core.GRID//2,:n,j:j+1]=old[:self.core.GRID//2]
            z[-self.core.GRID//2:,:n,j:j+1]=old[self.core.GRID//2:]
        values=c.real(c.fft.fft(z,inverse=True)*GRID)
        coefficients=c.affine_polynomial([values[:,k,:] for k in range(4)],Fraction(1),Fraction(-2))
        errors=[c.arb(float(c.np.max(f.error.hi))) for f in fields]
        for index,sigma in enumerate(STRIPS):
            components=[]
            for f in fields:
                weighted=c.wiener(f.Fourier()*self.weights[index])
                key=(sigma,f.error_degree)
                if key not in self.error_weights:self.error_weights[key]=c.arb_box((4*f.error_degree*c.exact(sigma)).exp()).hi
                error=c.mul_upper(f.error,c.Box(self.error_weights[key]))
                components.append(c.arb(float(c.np.max(c.add_upper(weighted,error).hi))))
            groups=[sum((components[j]*components[j] for j in range(k,k+3)),c.arb(0)).sqrt().upper()
                    for k in (0,3,6,9)]
            groups[0]=(2*groups[0]*groups[0]).sqrt().upper();strips.append(groups)
        grouped=[sum((errors[j]*errors[j] for j in range(k,k+3)),c.arb(0)).sqrt().upper()
                 for k in (0,3,6,9)]
        return stack(c,coefficients),grouped,strips

    def step(self):
        c=self.c
        require(self.cells<len(self.plan),'only a new incomplete cell')
        item=self.plan[-1-self.cells];left,right=map(Fraction,item['interval'])
        require(right==self.edge,'one complete reverse prefix')
        fields=self.fields.make(self.base,self.offsets,self.rows[item['row']],item,self.nodes,self.jets,self.read_ball)
        self.maximum_support=max(self.maximum_support,max(f.degree for f in fields))
        source,epsilon,strips=self.source(fields)
        chosen,endpoint=proposal(c.np,self.state,source,right-left)
        chosen=[c.Box(x) for x in chosen]
        A=[x[:,:9].reshape(GRID,3,3) for x in chosen]
        x=[z[:,9:12] for z in chosen];u=[z[:,12:15] for z in chosen];y=[z[:,15:18] for z in chosen]
        m,vel,dm,dvel=([source[k,:,j:j+3] for k in range(4)] for j in (0,3,6,9))
        M=[skew(c,z) for z in m]
        zeroM=lambda:c.Box(c.np.zeros((GRID,3,3)))
        zeroV=lambda:c.Box(c.np.zeros((GRID,3)))
        AM=convolution(A,M,lambda a,b:mm(c,a,b),zeroM)
        Ac=convolution(A,vel,lambda a,b:mv(c,a,b),zeroV)
        Ad=convolution(A,dm,lambda a,b:mv(c,a,b),zeroV)
        Ae=convolution(A,dvel,lambda a,b:mv(c,a,b),zeroV)
        uxAc=convolution(u,Ac,lambda a,b:cross(c,a,b),zeroV)
        yrhs=[(uxAc[k] if k<len(uxAc) else zeroV())+(Ae[k] if k<len(Ae) else zeroV())
               for k in range(max(len(uxAc),len(Ae)))]
        residual=[residual_integral(c,v,r,right-left) for v,r in ((A,AM),(x,Ac),(u,Ad),(y,yrhs))]
        BA,Bu=polynomial_bound(c,A),polynomial_bound(c,u)
        Mc=polynomial_bound(c,vel)+epsilon[1]
        MD=polynomial_bound(c,dm)+epsilon[2]
        ME=polynomial_bound(c,dvel)+epsilon[3]
        length=c.exact(right-left);ea,ex,eu,ey=self.errors
        EA=(ea+residual[0]+length*BA*epsilon[0]).upper()
        EU=(eu+residual[2]+length*(EA*MD+BA*epsilon[2])).upper()
        EX=(ex+residual[1]+length*(EA*Mc+BA*epsilon[1])).upper()
        EY=(ey+residual[3]+length*(EU*Mc+Bu*(EA*Mc+BA*epsilon[1])+EA*ME+BA*epsilon[3])).upper()
        complete_endpoint=sum(chosen,c.Box(c.np.zeros((GRID,18))))
        jump=c.Box(endpoint)-complete_endpoint
        impulse=[maxnorm(c,jump[:,:9].reshape(GRID,3,3)),maxnorm(c,jump[:,9:12]),
                 maxnorm(c,jump[:,12:15]),maxnorm(c,jump[:,15:18])]
        self.errors=[(e+j).upper() for e,j in zip((EA,EX,EU,EY),impulse)]
        self.impulses=[(e+j).upper() for e,j in zip(self.impulses,impulse)]
        for k in range(3):
            self.strip_integrals[k]=[(old+length*value).upper()
                for old,value in zip(self.strip_integrals[k],strips[k])]
        self.state,self.edge=endpoint,left;self.cells+=1

    def prefix(self,record,receipt,plan_sha,chain):
        return {'kind':'RHI_complete_relative_ordered_cell_prefix_v1','exact_interval':[str(self.edge),'9/50'],
            'complete_cells':self.cells,'total_cells':len(self.plan),'complete_plan_sha256':plan_sha,
            'grid':GRID,'component_order':['A_rowmajor9','x3','axial_parameter3','position_parameter3'],
            'whole_private_endpoint':receipt,'whole_accepted_endpoint_chain_sha256':chain,
            'complete_uniform_grid_errors':[record(x,'upper') for x in self.errors],
            'complete_strip_integrals':[[record(x,'upper') for x in row] for row in self.strip_integrals],
            'complete_endpoint_impulse_sums':[record(x,'upper') for x in self.impulses],
            'complete_endpoint_impulse_count':self.cells,'maximum_complete_source_support':self.maximum_support,
            'all_original_seams_and_both_means_retained':True,'all_source_and_residual_monomials_retained':True,
            'relative_initial_identity_is_not_world_anchor':True,'old_scientific_targets_evaluated':0}

    def finish(self,old_error,publish):
        c=self.c
        require(self.cells==len(self.plan) and self.edge==0,'whole short carrier complete')
        profile=[[],[],[],[]];mean=[[],[],[],[]]
        for sigma,integrals in zip(STRIPS,self.strip_integrals):
            M,C,D,E=integrals;A=M.exp()
            bounds=[c.arb(3).sqrt()*A,A*C,A*D,c.arb(2).sqrt()*A*A*D*C+A*E]
            q=(-4*c.exact(sigma)).exp();qN=(-4*GRID*c.exact(sigma)).exp()
            half=(-2*GRID*c.exact(sigma)).exp()
            for k,B in enumerate(bounds):
                mean[k].append((2*B*qN/(1-qN)).upper())
                profile[k].append((4*B*half/(1-q)).upper())
        mean_fee=[min(values).upper() for values in mean]
        interpolation_fee=[min(values).upper() for values in profile]
        original_means=[];exact_centres=[]
        for j in range(12,18):
            exact=sum((Fraction.from_float(float(x)) for x in self.state[:,j]),Fraction(0))/GRID
            exact_centres.append(str(exact));original_means.append(c.exact(exact))
        trial_fees=[self.errors[2]+mean_fee[2]]*3+[self.errors[3]+mean_fee[3]]*3
        signed=[v+c.arb(0,e.upper()) for v,e in zip(original_means,trial_fees)]
        for j in ZERO_MEANS:
            require(signed[j].contains(0),'complete numerical ball respects proved reflection')
            signed[j]=c.arb(0)
        trial=publish(TARGETS[0],signed,'signed_enclosure',exact_centres)
        profiles=publish(TARGETS[1],[(e+f).upper() for e,f in zip(self.errors,interpolation_fee)],'upper')
        paid=[(c.arb(17)/16*old_error).upper(),(c.arb(36)/25*old_error).upper()]
        true=[c.arb(0) if j in ZERO_MEANS else x+c.arb(0,paid[0 if j<3 else 1]) for j,x in enumerate(trial)]
        true=publish(TARGETS[2],true,'signed_enclosure',exact_centres)
        final=publish(TARGETS[3],[(profiles[k+2]+paid[k]).upper() for k in range(2)],'upper')
        return {'all_source_strip_bounds_complete':True,'grid_mean_alias_fees':[str(x) for x in mean_fee],
            'whole_profile_interpolation_fees':[str(x) for x in interpolation_fee],
            'same_selected_full_PDE_receiver_fees':[str(x) for x in paid],
            'exact_zero_mean_indices':list(ZERO_MEANS),'signed_means_exclude_zero':[not x.contains(0) for x in true],
            'true_joint_profile_error_balls':[str(x) for x in final]}
