"""Actual two-ended R745 shooting, every valley derivative, and retained physical beta integrals."""
import hashlib
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import expit
from r745_three_broad_valleys import CUT,CENTER,H,slopes,pieces,physical_slope_prime
from r738_negative_tail_and_macro_source import native_dense_at,mode_at,FIRST,RATIO


def tag(eta):
    return hashlib.sha256(np.ascontiguousarray(eta,dtype='<f8').tobytes()).hexdigest()[:24]


def raw_side(book,ports,s,j,eta,ray,tol,counts):
    rr=CUT[s];k=j*j;lam=k*(k-1);f0,f1=ports[s,j]['f_0_1_2'][:2]
    if [float(z) for z in f0]!=[1.,1.]:raise ValueError('Wrong bound original negative port.')
    x0,x1=np.nextafter(float(f1[0]),-np.inf),np.nextafter(float(f1[1]),np.inf)
    d=(x0,(x0+x1)/2,x1)[ray]
    w0,_=slopes(rr,eta)
    state=np.zeros((2,3));state[:,0]=[1.,w0*(rr*d-k)]
    knots=pieces(s);sections=[]
    for ix,(lo,hi) in enumerate(zip(knots,knots[1:])):
        scale=slopes(np.sqrt(lo*hi),eta)[0];start=state.copy();start[1]/=scale
        key=f'r745_side_{s}_{j}_{tag(eta)}_{ray}_{float(tol).hex()}_{ix}'.replace('.','p').replace('+','u')
        def integrate():
            def rhs(x,y):
                r=np.exp(x);w,dw=slopes(r,eta);b=y.reshape(2,3)
                A=np.array([[k,scale/w],[-lam*w/scale,1-k]])
                out=A@b
                out[0,1:]-=scale*dw/w**2*b[1,0]
                out[1,1:]-=lam*dw/scale*b[0,0]
                return out.ravel()
            sol=solve_ivp(rhs,(np.log(lo),np.log(hi)),start.ravel(),method='DOP853',rtol=tol,atol=tol*1.e-5,dense_output=True)
            counts['actual_R745_RHS_evaluations']+=int(sol.nfev)
            if not sol.success or not np.isfinite(sol.y).all():raise ArithmeticError('True broad-shoulder propagation failed.')
            seg=sol.sol.interpolants;end=sol.y[:,-1].reshape(2,3).copy();end[1]*=scale
            return dict(start=np.array([q.t_old for q in seg]),width=np.array([q.h for q in seg]),
                 old=np.stack([q.y_old for q in seg]),coeff=np.stack([q.F for q in seg]),end=end,scale=scale,
                 steps=len(seg),rhs=int(sol.nfev))
        v=book.once(key,'segment',integrate)
        state=v['end'];sections.append(v)
    return state,sections


def matching(book,ports,eta,ray,tol,counts,keep=False):
    eta=np.asarray(eta)
    rows=[];jac=[];ratios=[];states={};sections={}
    for j in (2,3):
        end=[]
        for s in (-1,1):
            b,pp=raw_side(book,ports,s,j,eta,ray,tol,counts)
            q=b.copy();q[1]/=H/np.sqrt(1-H*H);end.append(q);states[s,j]=q
            if keep:sections[s,j]=pp
        l,r=end;V=l[:,0];U=r[:,0];n=np.linalg.norm(V)*np.linalg.norm(U)
        if not np.isfinite(n) or n<=0:raise ArithmeticError('Zero or nonfinite physical terminal ray.')
        det=lambda a,b:a[0]*b[1]-a[1]*b[0]
        d=det(V,U)/n;rows.append(d);ratios.append(V@U/(U@U))
        jac.append([(det(l[:,i],U)+det(V,r[:,i]))/n-d*(V@l[:,i]/(V@V)+U@r[:,i]/(U@U)) for i in (1,2)])
    return np.asarray(rows),np.asarray(jac),ratios,states,sections


def at_bulk(sections,s,j,eta,r):
    knots=np.asarray(pieces(s));z=r if s==-1 else -r
    i=np.searchsorted(knots if s==-1 else -knots,z,side='right')-1
    seg=sections[s,j][max(0,min(i,len(knots)-2))]
    x=np.log(r)
    if s==-1:
        val=native_dense_at(seg,x).reshape(2,3)[:,0]
    else:
        # DOP853 uses signed h for reverse propagation; search in monotone -x.
        n=max(0,min(len(seg['start'])-1,np.searchsorted(-seg['start'],-x,side='right')-1))
        u=(x-seg['start'][n])/seg['width'][n];v=np.zeros_like(seg['old'][n])
        for l,coef in enumerate(reversed(seg['coeff'][n])):v+=coef;v*=u if l%2==0 else 1-u
        val=(v+seg['old'][n]).reshape(2,3)[:,0]
    f=val[0];w=slopes(r,eta)[0]
    return f,(j*j*f+seg['scale']*val[1]/w)/r


def beta_and_cost(book,ports,native,eta,tol,count,order):
    res,J,ratio,ends,secs=matching(book,ports,eta,1,tol,count,True)
    nodes,weights=np.polynomial.legendre.leggauss(order);total={};budget={}
    from r738_negative_tail_and_macro_source import w_actual
    def weight(r,w,f,g,fp,gp):
        return -(r*fp*gp-9*fp*g-4*f*gp+12*f*g/r)/(2*w*r*r)
    for ix,s in enumerate((-1,1)):
        mul=np.ones(2) if s==-1 else np.array(ratio)
        out=np.zeros(2);peak=np.zeros((2,6));knees=pieces(s);deep=[]
        for n in range(FIRST[s],0):
            cuts=native[s,2][n][0]
            L=np.ldexp(1/512,-n)
            deep.extend(RATIO[s]*(.22-s*L*cuts))
        def evaluate(r,bulk):
            if bulk:
                vals=np.array([at_bulk(secs,s,j,eta,r) for j in (2,3)])
                w=slopes(r,eta)[0]
                wp=physical_slope_prime(r,eta)
            else:
                vals=[]
                for j in (2,3):
                    _,e=mode_at(native[s,j],j,s,r)
                    # e=-j f/r and e_r=-j(f_r/r-f/r^2) at the **actual physical radius**.
                    f=-r*e[0,1]/j;fp=-e[0,1]/j-r*e[1,1]/j
                    vals.append([f,fp])
                vals=np.asarray(vals)
                w,wp=w_actual(s,abs(r/RATIO[s]-.22));wp/=RATIO[s]
            vals*=mul[:,None];f,g=vals
            K=np.array([4.,9.]);j=np.array([2.,3.]);F=vals[:,0];Fr=vals[:,1];E=1+w*w
            pp=-(wp/w)*(Fr-K*F/r)
            costs=np.column_stack((F,Fr,j*F/r,pp/np.sqrt(E),-j*(Fr-F/r)/r,np.sqrt(E)*(Fr/r-K*F/r**2)))
            return weight(r,w,f[0],g[0],f[1],g[1]),costs
        for ii,br in enumerate((knees,np.unique(deep))):
            br=sorted(set(br))
            for a,b in zip(br,br[1:]):
                for x,wg in zip(nodes,weights):
                    r=(a+b)/2+(b-a)*x/2;v,fields=evaluate(r,ii==0)
                    out[ii]+=wg*(b-a)*v/2
                    peak=np.maximum(peak,abs(fields))
        label='inner' if s==-1 else 'outer'
        total[label]=dict(bulk=float(out[0]),new_negative_cells=float(out[1]))
        budget[label]=dict(sampled_f_fp_jf_over_r_delta_brr_brphi_bphiphi_absolute_maximum=peak.tolist(),real_cut_multipliers=mul.tolist(),
                            cuts=CUT[s],original_true_line_input_ray='enclosure_midpoint')
    return dict(signed_finite_parts=total,physical_derivative_costs=budget,midpoint_normalized_wronskians=res.tolist(),
                full_valley_derivative=J.tolist(),right_cut_true_multipliers=list(ratio),
                finite_signed_sum=sum(x['bulk']+x['new_negative_cells'] for x in total.values()),
                quadrature_nodes_per_interval=order,continuous_total_beta_certified=False)
