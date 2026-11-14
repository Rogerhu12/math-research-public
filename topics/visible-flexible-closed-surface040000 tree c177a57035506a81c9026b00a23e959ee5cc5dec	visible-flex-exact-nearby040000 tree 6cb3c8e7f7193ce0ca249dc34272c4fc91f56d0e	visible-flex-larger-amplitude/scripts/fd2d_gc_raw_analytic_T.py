"""Analytic physical-coast T column for the independent three-field raw DAE.

This is a new provider subclass. The original provider remains unchanged.
The angular chart, computational nodes, Fourier corrections, lifting weights,
central coefficients and tail controls are fixed while T is differentiated.
All scalar-profile T jets are supplied by the selected profile's actual jet().
No evaluation outside the physical T domain, or subtraction of nearby T values,
is used by this column.

The subclass otherwise assembles the same finite equations and all the same
state/tail/central columns. Its full continuous residual and actual geometry
remain unpaid until their separate consumers are run.
"""
from __future__ import annotations
import numpy as np
from scipy import sparse
from fd2d_gc_raw_lifted_dae import RawLiftedDAE as BaseRawLiftedDAE,step5
from fd2d_gc_raw_native_field import curvature_second_y


class AnalyticTRawLiftedDAE(BaseRawLiftedDAE):
    def analytic_T(self,vector,*,data=None):
        """Return the full raw residual derivative and the actual field_T.

        All entries have the same floating evaluation status as the original
        finite provider. The formulas are analytic; this is not an interval
        enclosure of their floating evaluation.
        """
        y,p=self.unpack(vector)
        T=float(p[-1])
        self.profile.set_parameter(T)
        if data is None:
            _,data=super().evaluate(vector,jacobian=False)
        ops=self.operators(T)
        jet=ops['jet']
        needed=('a','a_s','c','K','radial_scale','a_T','a_s_T','c_T','K_T','radial_scale_T')
        missing=[key for key in needed if key not in jet]
        if missing:
            raise ValueError('Selected actual profile lacks analytic T jets: '+','.join(missing))
        a,ap,c,J,aT,apT,cT,KT,JT=[
            np.asarray(jet[key],float) for key in
            ('a','a_s','c','radial_scale','a_T','a_s_T','c_T','K_T','radial_scale_T')]
        inv=np.asarray(ops['inv'],float)
        adv=np.asarray(ops['adv'],float)
        scale_inv=J[None,:]*inv
        scale_inv_T=(JT-J*aT/a)[None,:]*inv
        reaction=J*c
        reaction_T=JT*c+J*cT
        op_T=np.zeros_like(ops['op'])
        eye_e=np.eye(self.e);eye_K=np.eye(self.K)
        for j in range(self.N):
            op_T[j,:self.e,:self.e]=-reaction_T[j]*eye_e
            op_T[j,:self.e,self.e:self.d]=self.PE@(scale_inv_T[:,j,None]*self.Ox)
            op_T[j,:self.e,self.d:]=reaction_T[j]*eye_e
            op_T[j,self.e:,self.e:self.d]=-2*reaction_T[j]*eye_K
            op_T[j,self.e:,self.d:]=self.PO@(scale_inv_T[:,j,None]*self.Ex)
        lift=data['lift']
        U,Ux,Uxi=[np.asarray(self.coords[key],float) for key in ('u','u_s','u_xi')]
        sn,cs=np.sin(U),np.cos(U)
        height=a[None,:]*sn
        height_T=aT[None,:]*sn
        ax=ap*J
        axT=apT*J+ap*JT
        height_x=ax[None,:]*sn+a[None,:]*cs*Ux
        height_x_T=axT[None,:]*sn+aT[None,:]*cs*Ux
        height_xi=a[None,:]*cs*Uxi
        height_xi_T=aT[None,:]*cs*Uxi
        family=lift['tail']
        curve=family.angle_jets(height)
        ky=np.asarray(curve['kappa_y'],float)
        kyy=np.asarray(curvature_second_y(family,height,self.tail_kind),float)
        V=np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
        Vu=np.stack((-2*sn*cs,sn*sn-cs*cs,2*sn*cs),axis=-1)
        mul=lambda coefficient,vector:coefficient[...,None]*vector
        raw_T=mul(ky*height_T,V)
        raw_x_T=(mul(kyy*height_T*height_x+ky*height_x_T,V)
                 +mul(ky*height_T*Ux,Vu))
        raw_xi_T=(mul(kyy*height_T*height_xi+ky*height_xi_T,V)
                  +mul(ky*height_T*Uxi,Vu))
        length=.58*self.profile.end
        weight,weight_q=step5((self.x-.42*self.profile.end)/length)
        weight_x=weight_q/length
        field_T=weight[None,:,None]*raw_T
        lift_x_T=weight_x[None,:,None]*raw_T+weight[None,:,None]*raw_x_T
        lift_xi_T=weight[None,:,None]*raw_xi_T
        values=np.asarray(lift['values'],float)
        derivatives=np.asarray(lift['xi'],float)
        fn_T=(scale_inv_T*derivatives[:,:,1]+scale_inv*lift_xi_T[:,:,1]
            +reaction_T[None,:]*(values[:,:,2]-values[:,:,0])
            +reaction[None,:]*(field_T[:,:,2]-field_T[:,:,0])
            +adv*lift_xi_T[:,:,0]-lift_x_T[:,:,0])
        fm_T=(scale_inv_T*derivatives[:,:,2]+scale_inv*lift_xi_T[:,:,2]
            -2*reaction_T[None,:]*values[:,:,1]-2*reaction[None,:]*field_T[:,:,1]
            +adv*lift_xi_T[:,:,1]-lift_x_T[:,:,1])
        forcing_T=np.concatenate(((self.PE@fn_T).T,(self.PO@fm_T).T),axis=1)
        velocity_T=np.einsum('ndq,nq->nd',op_T,y)+forcing_T
        fields=np.asarray(data['fields'],float)
        n,m,l=fields[:,:,0],fields[:,:,1],fields[:,:,2]
        gauss_T=l*field_T[:,:,0]+n*field_T[:,:,2]-2*m*field_T[:,:,1]-KT[None,:]
        codazzi_T=-.5*(velocity_T[1:]+velocity_T[:-1])
        projected_gauss_T=(self.PE@gauss_T[:,:-1]).T
        raw_F_T=np.r_[codazzi_T.ravel(),projected_gauss_T.ravel(),
                       np.zeros(self.e+2*self.d+1)]
        if raw_F_T.shape!=(self.size,):
            raise ValueError('Raw residual layout changed; this explicit analytic assembly must be updated')
        for key,value in dict(op_T=op_T,field_T=field_T,lift_x_T=lift_x_T,
            lift_xi_T=lift_xi_T,forcing_T=forcing_T,raw_F_T=raw_F_T).items():
            if not np.all(np.isfinite(value)):
                raise FloatingPointError('Nonfinite analytic T evaluation: '+key)
        return dict(op_T=op_T,field_T=field_T,lift_x_T=lift_x_T,lift_xi_T=lift_xi_T,
            forcing_T=forcing_T,velocity_T=velocity_T,gauss_T=gauss_T,K_T=KT,
            raw_F_T=raw_F_T,
            definition=dict(kind='analytic fixed-computational-coordinate physical-coast derivative',
                physical_T=T,profile_kind=self.profile_kind,tail_kind=self.tail_kind,
                finite_difference_used=False,out_of_domain_T_evaluations=0,
                chart_and_lifting_weights_T_derivative_zero=True,
                auxiliary_l_remains_independent=True,continuous_certificate=False))

    def evaluate(self,vector,*,jacobian=False):
        residual,data=super().evaluate(vector,jacobian=False)
        if not jacobian:
            return residual,data
        y,p=self.unpack(vector)
        ops=self.operators(float(p[-1]))
        lift=data['lift'];fields=np.asarray(data['fields'])
        n,m,l=fields[:,:,0],fields[:,:,1],fields[:,:,2]
        derivative=self.analytic_T(vector,data=data)
        rr,cc,vv=[],[],[]
        def block(row,col,values):
            values=np.atleast_2d(np.asarray(values,float))
            ii,jj=np.nonzero(values)
            rr.append(ii+row);cc.append(jj+col);vv.append(values[ii,jj])
        pcol=self.N*self.q
        for j in range(self.N-1):
            row=j*self.d
            block(row,j*self.q,-self.select/self.h[j]-.5*ops['op'][j])
            block(row,(j+1)*self.q,self.select/self.h[j]-.5*ops['op'][j+1])
            block(row,pcol+self.K,-.5*(lift['forcing_parameters'][j]+lift['forcing_parameters'][j+1]))
        row0=(self.N-1)*self.d
        gp=lift['parameters']
        for j in range(self.N-1):
            row=row0+j*self.e
            state=np.concatenate((self.PE@(l[:,j,None]*self.E),
                self.PE@(-2*m[:,j,None]*self.O),self.PE@(n[:,j,None]*self.E)),axis=1)
            block(row,j*self.q,state)
            tail=l[:,j,None]*gp[:,j,0]+n[:,j,None]*gp[:,j,2]-2*m[:,j,None]*gp[:,j,1]
            block(row,pcol+self.K,self.PE@tail)
        row=row0+(self.N-1)*self.e
        block(row,(self.N-1)*self.q+self.d,np.eye(self.e));row+=self.e
        block(row,0,self.select)
        central=np.zeros((self.d,self.K));central[:self.e]=-self.core_coefficients
        block(row,pcol,central);row+=self.d
        block(row,(self.N-1)*self.q,self.select);row+=self.d
        block(row,pcol,np.asarray(data['axes']['gap_jacobian'],float)[None,:]/self.gap)
        block(0,self.size-1,derivative['raw_F_T'][:,None])
        matrix=sparse.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),
            shape=(self.size,self.size)).tocsc()
        data['analytic_T']=derivative
        data['field_T']=derivative['field_T']
        data['fields_T']=derivative['field_T']
        data['K_T']=derivative['K_T']
        return residual,matrix,data


# Explicit import replacement in a NEW driver; the frozen base source is untouched.
RawLiftedDAE=AnalyticTRawLiftedDAE

