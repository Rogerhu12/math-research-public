#!/usr/bin/env python3
"""Actual quintic B-spline collocation for fourfold finite-body exploration.

Floating arithmetic only. All geometric jets and the Newton equations use the
same actual splines. Neither a full-frequency existence proof nor a closed-cap
construction follows from a converged finite collocation problem.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import BSpline, make_interp_spline
from scipy.sparse import coo_matrix, csc_matrix, eye
from scipy.sparse.linalg import splu
from scipy.optimize import brentq
import poschl_teller_fourfold_series as ps


def parity_matrix(knots, degree, x, derivative, odd=False):
    """Map the positive control points to actual parity-spline derivatives."""
    t = np.asarray(knots)
    count = len(t)-degree-1
    transform = eye(count, format='csc')
    current_count, k = count, degree
    for _ in range(derivative):
        denominator = t[np.arange(current_count-1)+k+1]-t[np.arange(current_count-1)+1]
        coefficient = k/denominator
        row = np.repeat(np.arange(current_count-1), 2)
        col = np.column_stack([np.arange(current_count-1), np.arange(1, current_count)]).ravel()
        data = np.column_stack([-coefficient, coefficient]).ravel()
        d = coo_matrix((data, (row, col)), shape=(current_count-1, current_count)).tocsc()
        transform = d@transform
        t, current_count, k = t[1:-1], current_count-1, k-1
    full = BSpline.design_matrix(x, t, k).tocsc()@transform
    n = count//2
    rows = np.arange(count)
    cols = np.r_[np.arange(n-1, -1, -1), np.arange(n)]
    data = np.r_[np.full(n, -1. if odd else 1.), np.ones(n)]
    reflection = coo_matrix((data, (rows, cols)), shape=(count, n)).tocsc()
    return csc_matrix(full@reflection)


class WeightedMode:
    def __init__(self, solver, coefficient):
        self.solver = solver
        full = np.concatenate([coefficient[:, ::-1], coefficient], axis=1).T
        full[:solver.points, 2] *= -1
        self.spline = BSpline(solver.knots, full, 5)

    def __call__(self, x, nu=0):
        x = np.asarray(x)
        a, ap, app = (self.solver.base_spline(x, nu=j)[..., 0] for j in range(3))
        powers = np.array([4,4,3])
        weight = a[..., None]**powers
        w1 = powers*a[..., None]**(powers-1)*ap[..., None]
        w2 = (powers*(powers-1)*a[..., None]**(powers-2)*ap[..., None]**2+
              powers*a[..., None]**(powers-1)*app[..., None])
        c = self.spline(x)
        if nu == 0:
            return weight*c
        d = self.spline(x, nu=1)
        if nu == 1:
            return weight*d+w1*c
        if nu == 2:
            return weight*self.spline(x, nu=2)+2*w1*d+w2*c
        raise ValueError('only geometric jets through order two are supported')


class CombinedMean:
    def __init__(self, solver, alpha):
        self.solver, self.alpha = solver, alpha

    def __call__(self, x, nu=0):
        out = self.solver.base_spline(x, nu=nu).copy()
        for alpha, spline in zip(self.alpha, self.solver.mean_splines):
            out += alpha*spline(x, nu=nu)
        return out


class SplineNewton:
    def __init__(self, modes=16, points=301, length=3., mu_scale=4.,
                 means=3, gauge='radius', profile_points=1201, mesh='uniform'):
        self.modes, self.points, self.length = modes, points, length
        self.mean_count, self.mean_gauge = means, gauge
        self.mu = 2**.5*mu_scale
        self.profile_points = profile_points
        self.mesh = mesh
        if mesh == 'uniform':
            breaks = np.linspace(-length, length, 2*points-4)
        elif mesh == 'graded':
            parameter = np.linspace(-1., 1., 2*points-4)
            breaks = length*np.sinh(3*parameter)/np.sinh(3.)
        else:
            raise ValueError('mesh must be uniform or graded')
        self.knots = np.r_[np.full(6, -length), breaks[1:-1], np.full(6, length)]
        greville = np.array([np.mean(self.knots[i+1:i+6]) for i in range(2*points)])
        self.x = greville[points:]
        self.even = [parity_matrix(self.knots,5,self.x,j,False) for j in range(3)]
        self.odd = [parity_matrix(self.knots,5,self.x,j,True) for j in range(3)]
        base = ps.build_series(order=3, points=profile_points, length=length, mu_scale=mu_scale)
        self.base_series = base
        self.base_spline = ps.make_candidate(base, 0., 1)['splines'][0]
        alpha2 = next(r['mean_previous'] for r in base['recursion'] if r['order']==3)
        field = tuple(a/alpha2 for a in base['fields'][2][0])
        self.mean_splines = [self.field_spline(base['x'], *field)]
        for radius in [.25,.5,.8,1.2][:means-1]:
            a = 1/base['h']
            ph, php = ps.bump(base['x'],radius)
            c = np.stack([-a*ph, np.zeros_like(a), np.zeros_like(a)])
            cd = np.stack([a*base['v']/base['h']*ph-a*php,
                           np.zeros_like(a), -2*a*a*ph])
            self.mean_splines.append(self.field_spline(base['x'],c,cd))
        if len(self.mean_splines) != means:
            raise ValueError('means must be 1 through 5')
        self.a = self.base_spline(self.x)[:,0]
        self.ap = self.base_spline(self.x,nu=1)[:,0]
        self.gamma = self.a**3
        self.mode = 4*np.arange(1,modes+1)
        self.angles = 4*modes+8
        self.phi = 2*np.pi*np.arange(self.angles)/self.angles
        self.cos = np.cos(np.arange(1,modes+1)[:,None]*self.phi)
        self.sin = np.sin(np.arange(1,modes+1)[:,None]*self.phi)
        self.base_x = np.broadcast_to(self.base_spline(self.x,nu=1)[:,None,:],
                                      (points,self.angles,3)).copy()
        self.base_t = np.zeros_like(self.base_x)
        self.base_t[:,:,1] = self.a[:,None]
        self.means_c = np.stack([s(self.x).T for s in self.mean_splines])
        self.means_d = np.stack([s(self.x,nu=1).T for s in self.mean_splines])
        # Integrate amplitude in the actual spline coordinates, rather than
        # assigning a second unrelated finite-difference quadrature grid.
        boundaries = np.r_[0., breaks[breaks>0]]
        q, qw = leggauss(8)
        lo,hi=boundaries[:-1,None],boundaries[1:,None]
        qx=((lo+hi)/2+(hi-lo)/2*q).ravel()
        qweight=((hi-lo)/2*qw).ravel()
        y=np.cosh(qx)**(-4*self.mu)
        qa=self.base_spline(qx)[:,0]
        qe=parity_matrix(self.knots,5,qx,0,False)
        self.amplitude_row=np.asarray((qweight*y*qa**3)@qe).ravel()
        self.kernel_norm=float(qweight@(y*y))
        self.value_lu=[splu(self.even[0]),splu(self.odd[0])]
        self.history=[]
        self.reference_action=self.action(np.zeros(self.mean_count))[0]

    def action(self,alpha,quadrature=128):
        """Actual positive Sturm action of the current mean curve, and gradient.

        Uses J = 2 integral sqrt((a'' z' - a' z'')/(a z')) dx over its
        positive intervals. Floating quadrature is diagnostic, never a bound.
        The turning-point endpoint term is zero; sin-squared coordinates
        regularize the integrable derivative singularity at a simple root.
        """
        curve=CombinedMean(self,alpha)
        def data(x):
            c=curve(x);d=curve(x,nu=1);d2=curve(x,nu=2)
            a,ap,app=c[...,0],d[...,0],d2[...,0]
            b,bp=d[...,2],d2[...,2]
            return a,ap,app,b,bp
        grid=np.linspace(0.,self.length,2001)
        a,ap,app,b,bp=data(grid)
        if np.min(a)<=0 or np.min(b)<=0:
            raise ValueError('mean profile lost positive radius or height slope')
        n=app*b-ap*bp
        def numerator(x):
            a,ap,app,b,bp=data(np.array([x]))
            return float((app*b-ap*bp)[0])
        roots=[]
        for i in np.nonzero(n[:-1]*n[1:]<0)[0]:
            roots.append(brentq(numerator,grid[i],grid[i+1],xtol=2e-14))
        cuts=[0.]+roots+[self.length]
        q,w=leggauss(quadrature)
        theta=(q+1)*np.pi/4
        sin,cos=np.sin(theta),np.cos(theta)
        total=0.;grad=np.zeros(self.mean_count);intervals=[]
        for lo,hi in zip(cuts[:-1],cuts[1:]):
            if numerator((lo+hi)/2)<=0:continue
            x=lo+(hi-lo)*sin*sin
            weights=w*(np.pi/4)*2*(hi-lo)*sin*cos
            a,ap,app,b,bp=data(x)
            num=app*b-ap*bp;den=a*b
            if np.min(num)<=0:raise ValueError('unresolved mean-action turning point')
            sq=np.sqrt(num/den)
            total+=2*float(weights@sq)
            for j,spline in enumerate(self.mean_splines):
                c=spline(x);d=spline(x,nu=1);d2=spline(x,nu=2)
                da,dap,dapp=c[:,0],d[:,0],d2[:,0]
                db,dbp=d[:,2],d2[:,2]
                dnum=dapp*b+app*db-dap*bp-ap*dbp
                dden=da*b+a*db
                grad[j]+=float(weights@(sq*(dnum/num-dden/den)))
            intervals.append([float(lo),float(hi)])
        return total,grad,intervals

    @staticmethod
    def field_spline(x,c,cd):
        full_x=np.r_[-x[:0:-1],x]
        reflected=c[:,:0:-1].copy()
        reflected[2]*=-1
        component=make_interp_spline(full_x,np.concatenate([reflected,c],axis=1).T,k=5)
        slope=np.r_[cd[2,:0:-1],cd[2]]
        return ps.IntegratedMeanHeight(component,make_interp_spline(full_x,slope,k=5))

    def pack(self,coeff,alpha):
        return np.r_[np.asarray(coeff).ravel(),np.broadcast_to(alpha,(self.mean_count,))]

    def unpack(self,vector):
        return vector[:-self.mean_count].reshape(self.modes,3,self.points),vector[-self.mean_count:]

    def jets(self,vector):
        coeff,alpha=self.unpack(vector)
        dx=np.zeros_like(self.base_x)
        dt=np.zeros_like(dx)
        for k,m in enumerate(self.mode):
            val=np.stack([self.even[0]@coeff[k,0], self.even[0]@coeff[k,1], self.odd[0]@coeff[k,2]])
            deriv=np.stack([self.even[1]@coeff[k,0], self.even[1]@coeff[k,1], self.odd[1]@coeff[k,2]])
            p=np.array([4,4,3])[:,None]
            c=val*self.a[None,:]**p
            cd=(deriv+p*self.ap[None,:]/self.a[None,:]*val)*self.a[None,:]**p
            co,si=self.cos[k],self.sin[k]
            dx[:,:,0]+=cd[0,:,None]*co
            dx[:,:,1]+=cd[1,:,None]*si
            dx[:,:,2]+=cd[2,:,None]*co
            dt[:,:,0]-=(m*c[0]+c[1])[:,None]*si
            dt[:,:,1]+=(c[0]+m*c[1])[:,None]*co
            dt[:,:,2]-=m*c[2,:,None]*si
        dx+=np.tensordot(alpha,self.means_d,axes=(0,0)).T[:,None,:]
        dt[:,:,1]+=np.tensordot(alpha,self.means_c,axes=(0,0))[0,:,None]
        return dx,dt

    def extract(self,xx,xt,tt):
        fft=[np.fft.rfft(v,axis=1)/self.angles for v in [tt,xt,xx]]
        return np.stack([np.stack([2*fft[0][:,k].real,-2*fft[1][:,k].imag,
                                  2*fft[2][:,k].real]) for k in range(1,self.modes+1)])

    def cross(self,ax,at,bx,bt):
        return self.extract(2*np.sum(ax*bx,axis=2),np.sum(ax*bt+bx*at,axis=2),
                            2*np.sum(at*bt,axis=2))

    def residual(self,vector,epsilon):
        coeff,alpha=self.unpack(vector)
        vx,vt=self.jets(self.pack(coeff,np.zeros(self.mean_count)))
        ax=self.base_x+np.tensordot(alpha,self.means_d,axes=(0,0)).T[:,None,:]
        at=self.base_t.copy()
        at[:,:,1]+=np.tensordot(alpha,self.means_c,axes=(0,0))[0,:,None]
        dxx=2*np.sum(ax*vx,axis=2)+np.sum(vx*vx,axis=2)
        dxt=np.sum(ax*vt+vx*at+vx*vt,axis=2)
        dtt=2*np.sum(at*vt,axis=2)+np.sum(vt*vt,axis=2)
        residual=self.extract(dxx,dxt,dtt)
        ex=np.sum(ax[:,0]**2,axis=1)+dxx.mean(axis=1)
        et=np.sum(at[:,0]**2,axis=1)+dtt.mean(axis=1)
        scales=np.stack([et,np.sqrt(ex*et),ex])
        low=abs(residual)/scales[None,:,:]
        weighted=low/self.gamma[None,None,:]
        weighted[:,2,-1]=0
        boundary=[]
        for k,m in enumerate(self.mode):
            rate=m*self.mu+3*self.ap[-1]/self.a[-1]
            boundary.append(float((self.even[1].getrow(self.points-1)@coeff[k,0])[0]+
                                  rate*(self.even[0].getrow(self.points-1)@coeff[k,0])[0]))
        amp=float(self.amplitude_row@coeff[0,0]/self.kernel_norm-epsilon)
        ea=(dxx-dxx.mean(axis=1)[:,None])/ex[:,None]
        eb=dxt/np.sqrt(ex*et)[:,None]
        ec=(dtt-dtt.mean(axis=1)[:,None])/et[:,None]
        cen=(ea+ec)/2
        rad=np.sqrt(((ea-ec)/2)**2+eb*eb)
        full=np.maximum(abs(cen-rad),abs(cen+rad))
        peak=np.unravel_index(np.argmax(full),full.shape)
        stats=dict(retained_weighted_robin_residual=max(float(weighted.max()),max(map(abs,boundary)),abs(amp)),
                   retained_metric_coefficient=float(low.max()), full_metric_collocation_sample=float(full.max()),
                   peak_x=float(self.x[peak[0]]),peak_theta=float(self.phi[peak[1]]/4),
                   outer_xx_coefficient=float(low[:,2,-1].max()),
                   robin_residual=max(map(abs,boundary)),amplitude_error=amp,alpha=alpha.tolist())
        if self.mean_gauge in ['action','action_radius']:
            action,gradient,intervals=self.action(alpha)
            stats['mean_action']=action
            stats['action_error']=action-self.reference_action
            stats['retained_weighted_robin_residual']=max(
                stats['retained_weighted_robin_residual'],abs(stats['action_error']))
        return residual,stats,ax+vx,at+vt,np.array(boundary)

    def direct_step(self,vector,epsilon,residual,fx,ft,boundary):
        n,ksize=self.points,3*self.modes
        aa=np.zeros((n,ksize,ksize)); bb=np.zeros_like(aa)
        for j in range(ksize):
            k,c=divmod(j,3)
            m,co,si=self.mode[k],self.cos[k],self.sin[k]
            dxv=np.zeros_like(fx);dxd=np.zeros_like(fx);dtv=np.zeros_like(ft)
            p=4 if c<2 else 3
            weight=self.a**p
            derivative=p*self.ap/self.a*weight
            trig=si if c==1 else co
            dxv[:,:,c]=derivative[:,None]*trig
            dxd[:,:,c]=weight[:,None]*trig
            if c==0:
                dtv[:,:,0]=-m*weight[:,None]*si
                dtv[:,:,1]=weight[:,None]*co
            elif c==1:
                dtv[:,:,0]=-weight[:,None]*si
                dtv[:,:,1]=m*weight[:,None]*co
            else:
                dtv[:,:,2]=-m*weight[:,None]*si
            aa[:,:,j]=self.cross(fx,ft,dxv,dtv).transpose(2,0,1).reshape(n,ksize)
            bb[:,:,j]=self.cross(fx,ft,dxd,np.zeros_like(ft)).transpose(2,0,1).reshape(n,ksize)
        sx=np.linalg.norm(self.base_x[:,0],axis=1)
        scale=np.tile(np.stack([self.a*self.a,sx*self.a,sx*sx],axis=1),(1,self.modes))
        scale*=self.gamma[:,None]
        aa/=scale[:,:,None];bb/=scale[:,:,None]
        br=np.arange(2,ksize,3)
        aa[-1,br,:]=0.;bb[-1,br,:]=0.
        rows=[];cols=[];vals=[]
        eqs=np.arange(ksize,dtype=np.int32)
        for j in range(ksize):
            basis=self.odd if j%3==2 else self.even
            for dense,mat in [(aa,basis[0]),(bb,basis[1])]:
                matrix=mat.tocoo();rr=matrix.row.astype(np.int32);cc=matrix.col.astype(np.int32)
                values=dense[rr,:,j]*matrix.data[:,None]
                rows.append((rr[:,None]*ksize+eqs).ravel())
                cols.append(np.broadcast_to(cc[:,None]*ksize+j,values.shape).ravel())
                vals.append(values.ravel())
        rvec=(residual.transpose(2,0,1).reshape(n,ksize)/scale).ravel()
        coeff,alpha=self.unpack(vector)
        nonmean_x,nonmean_t=self.jets(self.pack(coeff,np.zeros(self.mean_count)))
        mcols=[]
        for i in range(self.mean_count):
            al=np.zeros(self.mean_count);al[i]=1.
            dx,dt=self.jets(self.pack(np.zeros_like(coeff),al))
            mcols.append((self.cross(nonmean_x,nonmean_t,dx,dt).transpose(2,0,1).reshape(n,ksize)/scale).ravel())
        mcols=np.stack(mcols,axis=1)
        for k,m in enumerate(self.mode):
            row=(n-1)*ksize+3*k+2
            rate=m*self.mu+3*self.ap[-1]/self.a[-1]
            end=(self.even[1].getrow(n-1)+rate*self.even[0].getrow(n-1)).tocoo()
            rows.append(np.full(end.nnz,row,dtype=np.int32))
            cols.append(end.col.astype(np.int32)*ksize+3*k)
            vals.append(end.data)
            rvec[row]=boundary[k];mcols[row,:]=0.
        matrix=coo_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),
                          shape=(n*ksize,n*ksize)).tocsc()
        matrix.eliminate_zeros()
        lu=splu(matrix)
        answers=lu.solve(np.column_stack([-rvec,mcols]))
        av=self.amplitude_row@answers[0::ksize,0]
        au=self.amplitude_row@answers[0::ksize,1:]
        amplitude_error=self.amplitude_row@coeff[0,0]-epsilon*self.kernel_norm
        constraints=[au];targets=[av+amplitude_error]
        if self.mean_gauge in ['radius','action_radius'] and self.mean_count>1:
            candidate=self.candidate(vector,epsilon)
            values=ps.evaluate_candidate(candidate,self.x,self.phi/4,False)[0]
            squared=np.sum(values*values,axis=2)
            ip,jp=np.unravel_index(np.argmax(squared),squared.shape)
            unit=values[ip,jp]/np.sqrt(squared[ip,jp])
            direction=np.zeros((n,ksize))
            for kk in range(self.modes):
                for c in range(3):
                    basis=self.odd[0] if c==2 else self.even[0]
                    p=3 if c==2 else 4
                    trig=self.sin[kk,jp] if c==1 else self.cos[kk,jp]
                    direction[:,3*kk+c]=basis.getrow(ip).toarray().ravel()*self.a[ip]**p*unit[c]*trig
            point=direction.ravel()@answers
            pointmean=self.means_c[:,:,ip]@unit
            constraints.append(point[1:]-pointmean);targets.append(point[0])
        elif self.mean_gauge=='waist' and self.mean_count>1:
            row=np.array([s(np.array([0.]))[0,0] for s in self.mean_splines])
            constraints.append(row);targets.append(-row@alpha)
        if self.mean_gauge in ['action','action_radius']:
            action,gradient,intervals=self.action(alpha)
            constraints.append(gradient);targets.append(self.reference_action-action)
        constraints=np.asarray(constraints);targets=np.asarray(targets)
        particular=np.linalg.lstsq(constraints,targets,rcond=1e-12)[0]
        _,sing,vh=np.linalg.svd(constraints,full_matrices=True)
        rank=np.sum(sing>sing[0]*1e-12)
        null=vh[rank:].T
        if null.shape[1]:
            shaped=answers.reshape(n,ksize,1+self.mean_count)
            physical=np.tile(np.stack([self.a**4,self.a**4,self.a**3],axis=1),(1,self.modes))
            angular=np.repeat(1+self.mode*self.mode,3)
            weighted=shaped*(physical*angular[None,:])[:,:,None]
            costs=[weighted.reshape(-1,1+self.mean_count)]
            # Actual derivative costs only choose free means; they do not
            # replace the governing metric equations or their diagnostics.
            second=np.zeros_like(shaped)
            for j in range(ksize):
                basis=self.odd if j%3==2 else self.even
                second[:,j,:]=basis[2]@shaped[:,j,:]
            second*=physical[:,:,None]
            costs.append(second.reshape(-1,1+self.mean_count))
            cost=np.concatenate(costs,axis=0)
            b,A=cost[:,0],cost[:,1:]
            reg=np.eye(self.mean_count)*1e-4
            reduced=np.vstack([A@null,reg@null])
            rhs=np.r_[b-A@particular,-reg@particular]
            free=np.linalg.lstsq(reduced,rhs,rcond=1e-12)[0]
            dalpha=particular+null@free
        else:
            dalpha=particular
        dc=answers[:,0]-answers[:,1:]@dalpha
        discrepancy=matrix@dc+mcols@dalpha+rvec
        delta=self.pack(dc.reshape(n,self.modes,3).transpose(1,2,0),dalpha)
        return delta,dict(linear_residual=float(abs(discrepancy).max()),jacobian_nnz=int(matrix.nnz),
                          mean_schur=au.tolist(),mean_constraint_singular_values=sing.tolist())

    def from_old(self,saved):
        candidate=ps.make_candidate(saved,1.,1)
        coeff=np.zeros((self.modes,3,self.points))
        for k,m in enumerate(self.mode):
            if int(m) not in candidate['splines']:
                continue
            val=candidate['splines'][int(m)](self.x).T
            for c in range(3):
                p=4 if c<2 else 3
                coeff[k,c]=self.value_lu[int(c==2)].solve(val[c]/self.a**p)
        alpha=np.r_[saved['parameters'].get('mean_parameters',[0.]),
                    np.zeros(max(0,self.mean_count-len(saved['parameters'].get('mean_parameters',[0.]))))]
        if alpha.size!=self.mean_count:
            raise ValueError('input has incompatible mean count')
        return self.pack(coeff,alpha)

    def seed(self,epsilon):
        base=self.base_series
        c,d=base['fields'][1][4]
        source=ps.make_candidate(base,epsilon,3)
        coeff=np.zeros((self.modes,3,self.points))
        for k,m in enumerate(self.mode):
            if int(m) not in source['splines']:continue
            val=source['splines'][int(m)](self.x).T
            for j in range(3):
                coeff[k,j]=self.value_lu[int(j==2)].solve(val[j]/self.a**(3 if j==2 else 4))
        alpha=np.zeros(self.mean_count)
        alpha[0]=epsilon**2*next(r['mean_previous'] for r in base['recursion'] if r['order']==3)
        return self.pack(coeff,alpha)

    def change_amplitude(self,vector,increment):
        coeff,alpha=self.unpack(vector)
        coeff=coeff.copy()
        c=self.base_series['fields'][1][4][0]
        # Analytic linear seed in the same actual interpolation baseline.
        base=ps.make_candidate(self.base_series,1.,1)
        val=base['splines'][4](self.x).T
        for j in range(3):
            coeff[0,j]+=increment*self.value_lu[int(j==2)].solve(val[j]/self.a**(3 if j==2 else 4))
        return self.pack(coeff,alpha)

    def candidate(self,vector,epsilon):
        coeff,alpha=self.unpack(vector)
        return dict(splines={0:CombinedMean(self,alpha)}|
                    {int(m):WeightedMode(self,c) for m,c in zip(self.mode,coeff)},
                    epsilon=epsilon,order=1,length=self.length)

    def diagnostic(self,vector,epsilon,samples=1201,angles=None):
        if angles is None:angles=max(192,16*self.modes+8)
        candidate=self.candidate(vector,epsilon)
        x=np.unique(np.r_[np.linspace(0,self.length,samples),self.x])
        theta=2*np.pi*np.arange(angles)/angles
        peak=0.;at=None;radius=0.;kmax=0.;support=float('inf');low_peak=0.;high_peak=0.;low_at=None;high_at=None;waist_type={}
        for start in range(0,len(x),64):
            xx=x[start:start+64]
            f,fx,ft,fxx,fxt,ftt=ps.evaluate_candidate(candidate,xx,theta,False)
            gxx=np.sum(fx*fx,axis=2);gxt=np.sum(fx*ft,axis=2);gtt=np.sum(ft*ft,axis=2)
            ex=gxx.mean(axis=1)[:,None];et=gtt.mean(axis=1)[:,None]
            aa=(gxx-ex)/ex;bb=gxt/np.sqrt(ex*et);cc=(gtt-et)/et
            fc=np.stack([2*np.fft.rfft(zz,axis=1).real/angles for zz in [cc,aa]])
            fq=-2*np.fft.rfft(bb,axis=1).imag/angles
            for k in range(1,2*self.modes+1):
                frequency=4*k
                if frequency>=fc.shape[-1]:continue
                vals=np.stack([fc[0,:,frequency],fq[:,frequency],fc[1,:,frequency]])
                ii=np.unravel_index(np.argmax(abs(vals)),vals.shape)
                value=float(abs(vals[ii]))
                if k<=self.modes and value>low_peak:
                    low_peak=value;low_at=dict(mode=frequency,component=['tt','xt','xx'][ii[0]],x=float(xx[ii[1]]))
                if k>self.modes and value>high_peak:
                    high_peak=value;high_at=dict(mode=frequency,component=['tt','xt','xx'][ii[0]],x=float(xx[ii[1]]))
            center=(aa+cc)/2;rad=np.sqrt(((aa-cc)/2)**2+bb*bb)
            norm=np.maximum(abs(center-rad),abs(center+rad))
            index=np.unravel_index(np.argmax(norm),norm.shape)
            if norm[index]>peak:peak=float(norm[index]);at=(float(xx[index[0]]),float(theta[index[1]]))
            radius=max(radius,float(np.linalg.norm(f,axis=2).max()))
            cross=np.cross(ft,fx);jac=np.linalg.norm(cross,axis=2);normal=cross/jac[:,:,None]
            bx=np.sum(normal*fxx,axis=2);bt=np.sum(normal*ftt,axis=2);bxt=np.sum(normal*fxt,axis=2)
            trace=(bx*gtt-2*bxt*gxt+bt*gxx)/(jac*jac)
            detii=bx*bt-bxt*bxt
            gauss=detii/(jac*jac)
            for iz in np.nonzero(xx==0.)[0]:
                waist_type=dict(detII_min=float(detii[iz].min()),detII_max=float(detii[iz].max()),
                                N_min=float(bt[iz].min()),N_max=float(bt[iz].max()),
                                gauss_min=float(gauss[iz].min()),gauss_max=float(gauss[iz].max()))
            root=np.sqrt(np.maximum(0,trace*trace-4*gauss))
            kmax=max(kmax,float(np.maximum(abs((trace+root)/2),abs((trace-root)/2)).max()))
            support=min(support,float(np.sum(f*normal,axis=2).min()))
        f=ps.evaluate_candidate(candidate,[0.],[0.,np.pi/4],False)[0]
        gap=float(f[0,0,0]-f[0,1,0])
        return dict(kind='floating_actual_spline_samples_not_bounds',samples=int(len(x)),angles=angles,
                    metric_operator_norm_sample=peak,at_x=at[0],at_theta=at[1],
                    twice_sampled_radius=2*radius,waist_radial_gap=gap,gap_ratio_sample=gap/(2*radius),
                    max_abs_principal_curvature_sample=kmax,minimum_support_sample=support,
                    retained_metric_coefficient_sample=low_peak,retained_peak=low_at,
                    unretained_metric_coefficient_sample=high_peak,unretained_peak=high_at,
                    waist_second_form_samples=waist_type)

    def solve(self,epsilon,initial=None,iterations=12,tolerance=1e-10):
        vector=self.seed(epsilon) if initial is None else initial.copy()
        for it in range(iterations):
            residual,stats,fx,ft,boundary=self.residual(vector,epsilon)
            record=dict(epsilon=epsilon,iteration=it,**stats)
            self.history.append(record)
            print(json.dumps(record),flush=True)
            if stats['retained_weighted_robin_residual']<tolerance:return vector,True
            delta,info=self.direct_step(vector,epsilon,residual,fx,ft,boundary)
            record.update(info);record['maximum_step']=float(abs(delta).max())
            accepted=False
            for j in range(16):
                damping=2.**(-j)
                trial=vector+damping*delta
                try:
                    _,st,*_=self.residual(trial,epsilon)
                except ValueError:
                    continue
                if st['retained_weighted_robin_residual']<stats['retained_weighted_robin_residual']:
                    vector=trial;record['damping']=damping;accepted=True;break
            print(json.dumps(dict(step=record)),flush=True)
            if not accepted:return vector,False
        return vector,False

    def save(self,vector,path,epsilon):
        metadata=dict(kind='floating_actual_spline_finite_body_candidate_not_proof',
                      parameters=dict(modes=self.modes,points=self.points,length=self.length,
                                      mu_scale=self.mu/2**.5,means=self.mean_count,gauge=self.mean_gauge,
                                      profile_points=self.profile_points,mesh=self.mesh),epsilon=epsilon,
                      limitations=['Finite angular equations','Finite Robin endpoint','No exact caps',
                                   'No interval error or global reach certificate'])
        np.savez_compressed(path,vector=vector,metadata=np.array(json.dumps(metadata)))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--modes',type=int,default=16)
    ap.add_argument('--points',type=int,default=301)
    ap.add_argument('--length',type=float,default=3.)
    ap.add_argument('--mu-scale',type=float,default=4.)
    ap.add_argument('--means',type=int,default=3)
    ap.add_argument('--gauge',choices=['none','radius','waist','action','action_radius'],default='radius')
    ap.add_argument('--profile-points',type=int,default=1201)
    ap.add_argument('--mesh',choices=['uniform','graded'],default='uniform')
    ap.add_argument('--epsilons',nargs='+',type=float,default=[.06])
    ap.add_argument('--iterations',type=int,default=12)
    ap.add_argument('--start-old',type=Path)
    ap.add_argument('--start-cache',type=Path)
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    solver=SplineNewton(args.modes,args.points,args.length,args.mu_scale,args.means,args.gauge,args.profile_points,args.mesh)
    previous=None;last=None
    if args.start_old:
        saved=ps.load_series(args.start_old);previous=solver.from_old(saved);last=saved['parameters']['actual_epsilon']
    if args.start_cache:
        with np.load(args.start_cache,allow_pickle=False) as s:
            metadata=json.loads(str(s['metadata']));previous=s['vector'];last=metadata['epsilon']
            if metadata['parameters']['points']!=args.points or metadata['parameters']['modes']!=args.modes or metadata['parameters'].get('mesh','uniform')!=args.mesh:
                old=SplineNewton(**metadata['parameters'])
                oldcandidate=old.candidate(previous,last)
                oldcoeff,alpha=old.unpack(previous)
                coeff=np.zeros((solver.modes,3,solver.points))
                for k,m in enumerate(solver.mode):
                    if int(m) not in oldcandidate['splines']:continue
                    val=oldcandidate['splines'][int(m)](solver.x).T
                    for j in range(3):
                        coeff[k,j]=solver.value_lu[int(j==2)].solve(val[j]/solver.a**(3 if j==2 else 4))
                previous=solver.pack(coeff,alpha)
    report=dict(kind='floating_spline_newton_not_proof',parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},runs=[])
    for eps in args.epsilons:
        if previous is not None and eps!=last:previous=solver.change_amplitude(previous,eps-last)
        vector,success=solver.solve(eps,previous,args.iterations)
        diag=solver.diagnostic(vector,eps)
        report['runs'].append(dict(epsilon=eps,success=success,diagnostic=diag))
        report['history']=solver.history
        args.cache.parent.mkdir(parents=True,exist_ok=True)
        solver.save(vector,args.cache,eps)
        report['cache_sha256']=hashlib.sha256(args.cache.read_bytes()).hexdigest()
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report['runs'][-1]),flush=True)
        if not success:break
        previous,last=vector,eps


if __name__=='__main__':main()
