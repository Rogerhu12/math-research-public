#!/usr/bin/env python3
"""Fixed physical-angle tail operator and a declared finite weak deep boundary.

rho is frozen by the accepted core.  The state is (Ptilde= rho*P, Kbar, c),
retaining physical Fourier modes.  The mean and its derivative use the full
literal Q_N(rho*...) chain, including nonzero weighted means of Kbar and T.
The deep angular boundary is a finite generalized-eigenvalue model, not a
claim that material diagonal rows are diagonal in physical angle.
"""
import numpy as np
from scipy.linalg import eigh
from parallel_20261117_dynamic_tail import DynamicMean


class WeightedMean(DynamicMean):
    def __init__(self,M,N,rho_coefficients):
        super().__init__(M,N);self.rho_coefficients=np.array(rho_coefficients)
        f=2*np.arange(1,len(self.rho_coefficients)+1)
        self.rho=1+np.cos(self.angle[:,None]*f[None,:])@self.rho_coefficients
        self.rhop=-np.sin(self.angle[:,None]*f[None,:])@(f*self.rho_coefficients)
        if np.min(self.rho)<=0:raise ValueError('Fixed angular metric must remain positive')
        self.R=self.rho[:,None];self.Rp=self.rhop[:,None]

    def fields(self,y):
        p,k,c=y[:self.M],y[self.M:2*self.M],y[-1]
        pt=self.S@p;ptp=self.C@(self.freq[:,None]*p);K=self.C@k+c;kp=-self.S@(self.freq[:,None]*k)
        return pt/self.R,ptp/self.R**2-pt*self.Rp/self.R**3,K,kp/self.R

    def evaluate(self,y,s,ell,z,details=False):
        y=np.atleast_2d(y);P,T,K,V=self.fields(y);E=1+z;A=2*K+K*K+E*P*P
        D=1-z*A;S=1-z*P*P;Q=np.sqrt(D);yy=1+K;L=yy+E*T;N=1+z*yy*T/S
        if any(np.any(v.real<=0) for v in (D,S,L,N)) or (self.require_positive_height_slope and np.any(yy.real<=0)):raise FloatingPointError('Weighted tail branch exited')
        rawpt=self.R*(s*V-(s+ell)*P)
        rawk=-ell*(2*K+T)+(E*s*(V-P)**2+ell*((K+T)**2+z*(2*K*T+T*T-P*P)))/L
        fp=(2/self.N)*(self.S.T@rawpt);fk=(2/self.N)*(self.C.T@rawk)
        ppt=self.S@fp;pp=ppt/self.R;tp=(self.C@(self.freq[:,None]*fp))/self.R**2-ppt*self.Rp/self.R**3
        kk=self.C@fk
        B=A/(Q*(1+Q))+yy*T/(S*Q)
        BP=E*P*N/Q**3+2*z*yy*T*P/(S*S*Q);BK=L/Q**3;BT=yy/(S*Q)
        Bz=P*P/(Q*(1+Q))+A*(A+z*P*P)*(1+2*Q)/(2*Q**3*(1+Q)**2)+yy*T*((A+z*P*P)/(2*S*Q**3)+P*P/(S*S*Q))
        mean=np.mean(self.R*B,axis=0);mu=np.mean(self.R*BK,axis=0)
        cc=-(2*ell*z*np.mean(self.R*Bz,axis=0)+np.mean(self.R*(BP*pp+BK*kk+BT*tp),axis=0))/mu
        result=np.vstack((fp,fk,cc))
        if not details:return result
        fullk=kk+cc;chain=2*ell*z*np.mean(self.R*Bz,axis=0)+np.mean(self.R*(BP*pp+BK*fullk+BT*tp),axis=0)
        return result,dict(mean=mean,mu=mu,eta=cc-np.mean(rawk,axis=0),chain=chain,D=D,S=S,L=L,y=yy,N=N,
                           P=P,T=T,K=K,V=V,Ptilde=self.R*P,projected_k=fullk,raw_k=rawk,
                           pde_k_residual=fullk-rawk,pde_p_residual=ppt-rawpt)


def ideal_graph(frequency,R,a):
    nu=frequency*frequency*(frequency*frequency-1)/12
    if abs(nu-1)<1e-12:return 0.
    alpha=1+1/R;port=2**a;a00=1-alpha*nu*R
    a10=(-nu*(1+R)+alpha*nu*nu*R)/port;a11=(1-alpha*nu)/port
    trace=a00+a11;disc=trace*trace-4/port
    if disc<=0:raise ValueError('Deep generalized angular eigenvalue has no real stable graph')
    large=(trace-np.sqrt(disc))/2
    return a10/(large-a11)


def weak_deep_boundary(q,background,columns=None):
    """Use exact weighted cosine Gram and sampled weak angular energy.

    Subtracting the weighted mean from every cosine gives a square M-space
    exactly orthogonal to constants.  Its generalized angular eigenvalues
    remain real frequencies; they are not rounded to material even integers.
    """
    M=q.M;rho=q.rho_coefficients
    def coefficient(j):return rho[j-1] if 0<j<=len(rho) else 0.
    g0=np.array([coefficient(j)/2 for j in range(1,M+1)])
    G=np.empty((M,M))
    for i in range(1,M+1):
        for j in range(1,M+1):G[i-1,j-1]=(.5 if i==j else coefficient(abs(i-j))/4)+coefficient(i+j)/4
    G-=np.outer(g0,g0)
    derivative=-q.S*q.freq[None,:]
    A=(derivative.T@(derivative/q.rho[:,None]))/q.N
    eigen,U=eigh(A,G);frequency=np.sqrt(eigen);projection=U.T@G
    data=background.data;deep=data['inner'];r=deep['r'];logw=deep['logw'];mu=data['boundary'][0]['mu']
    parameters=data['parameters'];orientation=parameters['orientation'];R=parameters.get('R',64);a=parameters.get('a',2.75)
    if columns is None:
        u=np.ones(M);momentum=orientation*np.array([ideal_graph(m,R,a) for m in frequency]);boundary_kind='ideal finite design graph'
    else:
        if columns['input_sha256']!=background.sha256:raise ValueError('Actual deep columns belong to another background input')
        rows=columns['final']['modes']
        if len(rows)!=M:raise ValueError('Need one actual homogeneous column for every generalized mode')
        for j,row in enumerate(rows):
            if abs(row['mode']-frequency[j])>5e-11*max(1,frequency[j]):raise ValueError('Generalized frequency does not match the propagated column')
            d=row['deepBoundary']
            if max(abs(d['r']-r),abs(d['logw']-logw),abs(d['mu']-mu))>1e-11:raise ValueError('Actual column endpoint or mu differs')
        u=np.array([row['deepColumn'][0] for row in rows]);momentum=np.array([row['deepColumn'][1] for row in rows]);boundary_kind='actual same-source finite far columns'
    multiplier=eigen*u+np.sqrt(12)*np.exp(np.log(mu)-7*np.log(r)-logw)*momentum
    BK=u[:,None]*projection;BP=multiplier[:,None]*projection/q.freq[None,:]
    scale=np.sqrt(np.sum(BK*BK+BP*BP,axis=1));BK/=scale[:,None];BP/=scale[:,None]
    return BP,BK,dict(definition='finite G-orthogonal physical-angle generalized angular eigenproblem plus same ideal material-frequency graph function',
                     eigenvalues=eigen.tolist(),frequencies=frequency.tolist(),gram_min_eigenvalue=float(np.linalg.eigvalsh(G)[0]),
                     constant_weighted_mean=g0.tolist(),angular_samples=q.N,orientation=orientation,boundary_kind=boundary_kind,
                     scope='Finite linear design boundary. No nonlinear infinite DN, no assertion of equivalence to diagonal physical-frequency rows.')
