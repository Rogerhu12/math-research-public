"""Transfer the genuine stored closed-spinor height and its two fixed-material radial derivatives."""
import numpy as np
from r726_closed_spinor_fourier import public,ClosedSpinor
from r728_full_spinor_geometry import state


def projected(layout,old_parameters,r,old_N,target_K,source_reference):
    public()
    # All derivatives are components of the same paid native F at fixed MATERIAL phi.
    # psi is only the integration coordinate. The measure is J dpsi.
    core=ClosedSpinor(layout.K,old_N)
    st,c,sh=state(layout,core,np.asarray(old_parameters),np.asarray(r),source_reference)
    phi=st['material_angle'];J=st['J']
    if np.min(st['ordinary_angular_J_lower'])<=0:raise FloatingPointError('The source material angle inverse is not even separated on this lattice.')
    v=np.stack([sh[0][i][...,2] for i in (0,1,3)])
    k=np.arange(target_K+1);C=np.cos(phi[:,:,None]*k);S=np.sin(phi[:,:,None]*k)
    cc=np.einsum('drn,rn,rnk->drk',v,J,C)/old_N
    sc=np.einsum('drn,rn,rnk->drk',v,J,S)/old_N
    cc[:,:,1:]*=2;sc[:,:,1:]*=2;sc[:,:,0]=0.
    fitted=np.einsum('drk,rnk->drn',cc,C)+np.einsum('drk,rnk->drn',sc,S)
    native=np.stack([sh[1][i][...,2] for i in (0,1,3)])
    return dict(cos=cc,sin=sc,J_mean_error=float(abs(J.mean(axis=1)-1).max()),
          material_three_native_source_error=[float(abs(a-b).max()) for a,b in zip(v,native)],
          material_three_projection_error=[float(abs(a-b).max()) for a,b in zip(v,fitted)],
          reflection_sin_absolute_by_order=[float(abs(v).max()) for v in sc],
          source_angles=old_N,degree=target_K,r=np.array(r),all_errors_are_ordinary=True)


class QuinticHeight:
    """One material Fourier field, with value and both true r derivatives fixed at every declared knot."""
    def __init__(self,knots,cos,sin,declared_reflection=False):
        public()
        self.knots=np.asarray(knots);self.cosine=np.asarray(cos);self.sine=np.asarray(sin)
        if self.cosine.ndim!=3 or self.cosine.shape!=self.sine.shape or self.cosine.shape[:2]!=(3,len(self.knots)):
            raise ValueError('The same three radial jets of each material Fourier coefficient are required.')
        if np.any(np.diff(self.knots)<=0) or np.any(self.sine[:,:,0]!=0):raise ValueError('Wrong height-space knots or zero mode.')
        self.input_sin=[float(abs(q).max()) for q in self.sine]
        if declared_reflection:
            # This is a named projection. The original sine magnitudes stay visible as a source-fit cost.
            self.sine=np.zeros_like(self.sine)
    def coefficient_jets(self,r):
        r=np.asarray(r)
        if not len(r) or min(r)<self.knots[0] or max(r)>self.knots[-1]:
            raise ValueError('No extension across a missing deep material interval is implied.')
        ix=np.clip(np.searchsorted(self.knots,r,side='right')-1,0,len(self.knots)-2)
        h=(self.knots[ix+1]-self.knots[ix])[:,None];t=(r[:,None]-self.knots[ix,None])/h
        def piece(v):
            a=v[0,ix];b=h*v[1,ix];c=h*h*v[2,ix]/2
            A=v[0,ix+1]-a-b-c;B=h*v[1,ix+1]-b-2*c;D=h*h*v[2,ix+1]-2*c
            p=10*A-4*B+D/2;q=-15*A+7*B-D;l=6*A-3*B+D/2
            value=a+t*(b+t*(c+t*(p+t*(q+t*l))))
            first=(b+t*(2*c+t*(3*p+t*(4*q+5*t*l))))/h
            second=(2*c+t*(6*p+t*(12*q+20*t*l)))/(h*h)
            # Evaluation at the exact native knots uses the supplied C2 jets without cancellation.
            at=np.searchsorted(self.knots,r)
            valid=(at<len(self.knots));valid[valid]=self.knots[at[valid]]==r[valid]
            for data,original in zip((value,first,second),v):data[valid]=original[at[valid]]
            return np.stack((value,first,second))
        return piece(self.cosine),piece(self.sine)


def original_fixed_reference(base,r):
    """R738's single declared E evaluator and its derivative on the smooth physical pieces."""
    from r738_negative_tail_and_macro_source import bump,A0,B0
    public()
    r=np.asarray(r);v=base.paid(r);k,dk=bump(r);p=-base.M*k;dp=-base.M*dk
    ca,sa=np.cos(v['omega']),np.sin(v['omega'])
    axis=np.column_stack((sa,np.zeros_like(sa),ca))
    on=(r<A0+.01)|(r>B0-.01)
    dr=np.sum(v['center'][:,1]*axis,axis=1);dd=np.sum(v['center'][:,2]*axis,axis=1)
    Eprime=2*2.01**2*p*dp+np.where(on,2*dr*dd,0.)
    return v['reference_E'],Eprime
