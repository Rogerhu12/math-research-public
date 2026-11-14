#!/usr/bin/env python3
"""Directed complete 193-state moving generator on an actual cut cell.

The reference is a NEW exact degree-three polynomial: its physical
background and scalar target coefficients are explicitly recorded dyadics.
All operations below mean exact finite Fourier / radial polynomial algebra,
with radial terms above degree three paid as uniform operator errors.
Directed boxes and Arb matrices enclose that exact reference; they do not
redefine it through an unstored floating BLAS calculation.  Both mean
terms, the entire 128-mode primitive intermediate and Rprime/R are kept.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb
import numpy as np
from flint import arb,arb_mat,acb
from fourfold_phase_beta_bulk_box import Box,CBox,zeros,DirectedFFT,arb_box
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_codazzi_reciprocal_continuous_residual_v3 import wiener_upper

ORDER=3
GRID=512
MODES=96
DIM=193
INTERMEDIATE=128


def q(value):return exact_arb(Fraction(value))
def ab(value):return abs(arb(value)).upper()
def record(value):
    value=arb(value)
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))
def box_scalar(value):
    lo,hi=float(value.lo),float(value.hi)
    return arb(lo) if lo==hi else arb(lo).union(arb(hi))


def clean(coefficient,degree,parity):
    """Only mathematically exact finite-support / reflection zeros vanish."""
    z=coefficient
    indices=np.arange(GRID);indices=np.where(indices<GRID//2,indices,indices-GRID)
    outside=np.abs(indices)>degree
    for a in (z.real,z.imag):
        if np.any(a.lo[outside]>0) or np.any(a.hi[outside]<0):
            raise ArithmeticError('an exact absent full Fourier coefficient lost zero')
    z[outside]=0
    absent=z.real if parity else z.imag
    if np.any(absent.lo>0) or np.any(absent.hi<0):
        raise ArithmeticError('a complete exact reflection coefficient lost zero')
    if parity:z.real=Box(np.zeros_like(z.real.lo))
    else:z.imag=Box(np.zeros_like(z.imag.lo))
    return z


class Field:
    """Exact finite reference polynomial plus a full uniform Wiener error."""
    def __init__(self,c,degree,parity,fft,error=arb(0)):
        if c.real.lo.shape!=(GRID,ORDER+1) or 2*degree>=GRID:
            raise ValueError('the complete unaliased reference support changed')
        self.c=clean(c,int(degree),int(parity));self.degree=int(degree)
        self.parity=int(parity);self.fft=fft;self.error=arb(error).upper()
        if self.error<0:raise ValueError('negative intrinsic field error')
        self.coefficient_norms=[wiener_upper(self.c[:,j]) for j in range(ORDER+1)]
        self.norm=sum(self.coefficient_norms,arb(0)).upper();self._samples=None

    @classmethod
    def scalar(cls,values,fft,error=arb(0)):
        if len(values)>ORDER+1:raise ValueError('the exact reference radial order changed')
        c=zeros((GRID,ORDER+1))
        for j,value in enumerate(values):c[0,j]=CBox.from_acb(acb(q(value)))
        return cls(c,0,0,fft,error)

    def coerce(self,value):
        if isinstance(value,Field):
            if value.fft is not self.fft:raise ValueError('incompatible exact Fourier contexts')
            return value
        return self.scalar([Fraction(value)],self.fft)

    def __add__(self,other):
        other=self.coerce(other)
        if self.parity!=other.parity:
            if self.norm==0 and self.error==0:return other
            if other.norm==0 and other.error==0:return self
            raise ValueError('this exact moving field sum has incompatible reflection')
        return Field(self.c+other.c,max(self.degree,other.degree),self.parity,self.fft,self.error+other.error)
    __radd__=__add__
    def __neg__(self):return Field(-self.c,self.degree,self.parity,self.fft,self.error)
    def __sub__(self,other):return self+-self.coerce(other)
    def __rsub__(self,other):return self.coerce(other)+-self

    def samples(self):
        if self._samples is None:
            samples=self.fft.fft(self.c,inverse=True)*GRID
            if np.any(samples.imag.lo>0) or np.any(samples.imag.hi<0):
                raise ArithmeticError('an exact real reference field lost reality')
            self._samples=samples.real
        return self._samples

    def __mul__(self,other):
        other=self.coerce(other);degree=self.degree+other.degree
        if 2*degree>=GRID:raise ValueError('an exact full Fourier product would alias')
        full=zeros((GRID,2*ORDER+1))
        if self.degree==0 or other.degree==0:
            scalar,field=(self,other) if self.degree==0 else (other,self)
            for k in range(2*ORDER+1):
                for i in range(max(0,k-ORDER),min(ORDER,k)+1):
                    full[:,k]=full[:,k]+scalar.c[0,i]*field.c[:,k-i]
        else:
            a,b=self.samples(),other.samples();values=zeros((GRID,2*ORDER+1))
            for k in range(2*ORDER+1):
                term=Box(np.zeros(GRID))
                for i in range(max(0,k-ORDER),min(ORDER,k)+1):term=term+a[:,i]*b[:,k-i]
                values[:,k]=CBox(term)
            full=self.fft.fft(values)/GRID
        full=clean(full,degree,(self.parity+other.parity)%2)
        discarded=sum((wiener_upper(full[:,j]) for j in range(ORDER+1,2*ORDER+1)),arb(0))
        error=self.norm*other.error+other.norm*self.error+self.error*other.error+discarded
        return Field(full[:,:ORDER+1],degree,(self.parity+other.parity)%2,self.fft,error)
    __rmul__=__mul__
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError('only nonnegative exact powers')
        result=self.coerce(1)
        for _ in range(n):result=result*self
        return result

    def derivative(self):
        if not self.degree:return self.coerce(0)
        j=np.arange(GRID);j=np.where(j<GRID//2,j,j-GRID)
        c=self.c*CBox(0.,Box((4*j)[:,None]))
        return Field(c,self.degree,1-self.parity,self.fft,4*self.degree*self.error)

    def primitive(self):
        if not self.degree:return self.coerce(0)
        c=zeros((GRID,ORDER+1))
        for j in range(-self.degree,self.degree+1):
            if j:c[j%GRID]=self.c[j%GRID]*CBox.from_acb(acb(0,-arb(1)/(4*j)))
        return Field(c,self.degree,1-self.parity,self.fft,self.error/4)

    def mean(self):
        if self.parity:return self.coerce(0)
        c=zeros((GRID,ORDER+1));c[0]=self.c[0]
        return Field(c,0,0,self.fft,self.error)


def matrix_norm(matrix):
    """Complete induced Euclidean upper bound, never a sampled SVD."""
    n,m=matrix.nrows(),matrix.ncols();rows=[arb(0) for _ in range(n)]
    cols=[arb(0) for _ in range(m)];squares=arb(0)
    for i in range(n):
        for j in range(m):
            value=ab(matrix[i,j]);rows[i]+=value;cols[j]+=value;squares+=value*value
    if not rows or not cols:return arb(0)
    rowmax=max(value.upper() for value in rows);colmax=max(value.upper() for value in cols)
    return min((rowmax*colmax).sqrt().upper(),squares.sqrt().upper()).upper()


def matrix_from_box(value):
    lo,hi=value.lo,value.hi;zero=arb(0)
    return arb_mat([[zero if lo[i,j]==hi[i,j]==0 else
                     arb(float(lo[i,j])) if lo[i,j]==hi[i,j] else
                     arb(float(lo[i,j])).union(arb(float(hi[i,j])))
                     for j in range(lo.shape[1])] for i in range(lo.shape[0])])


def rectangle(field,k,out_odd,in_odd,out_modes=MODES,in_modes=MODES):
    """Every exact Toeplitz/Hankel coefficient and the independent mean."""
    rows=np.arange(1 if out_odd else 0,out_modes+1)[:,None]
    cols=np.arange(1 if in_odd else 0,in_modes+1)[None,:]
    coefficients=field.c.real[:,k] if out_odd==in_odd else field.c.imag[:,k]
    value=coefficients[(rows-cols)%GRID]+(-1 if in_odd else 1)*coefficients[(rows+cols)%GRID]
    if out_odd and not in_odd:value=-value
    if not out_odd:
        halfrow=value[0]*.5
        value.lo[0]=halfrow.lo;value.hi[0]=halfrow.hi
    if not np.isfinite(value.lo).all() or not np.isfinite(value.hi).all():
        raise ArithmeticError('nonfinite complete multiplication matrix')
    return value


def orthonormal(matrix,out_odd,in_odd):
    """Only mean versus nonmean introduces a nontrivial Gram factor."""
    root2=arb(2).sqrt()
    if not out_odd:
        for j in range(matrix.ncols()):matrix[0,j]*=root2
    if not in_odd:
        for i in range(matrix.nrows()):matrix[i,0]/=root2
    return matrix


def joint2(a,b):return (a*a+b*b).sqrt().upper()


def physical_reference(cube,knot,left,right,alpha,offset,fft):
    """A new recorded exact dyadic reference to the full repaired cubic."""
    step=left-right;shift=right-knot;coefficients=[];errors=[Fraction(0),Fraction(0)]
    for k in range(ORDER+1):
        row=[]
        for column in range(65):
            value=sum((Fraction(comb(power,k))*Fraction(float(cube[3-power,column]))
                *shift**(power-k)*step**k for power in range(k,4)),Fraction(0))*alpha
            if k==0:value+=offset[column]
            selected=float(value);error=abs(value-Fraction(selected));row.append(selected)
            errors[0 if column<32 else 1]+=error
        coefficients.append(row)
    uc=zeros((GRID,ORDER+1));vc=zeros((GRID,ORDER+1))
    for k,row in enumerate(coefficients):
        vc[0,k]=CBox(row[32])
        for j in range(1,33):
            ub=Fraction(row[j-1])/2;vb=Fraction(row[32+j])/2
            uc[j,k]=CBox.from_acb(acb(0,-q(ub)));uc[-j,k]=CBox.from_acb(acb(0,q(ub)))
            vc[j,k]=vc[-j,k]=CBox.from_acb(acb(q(vb)))
    definition=dict(physical_repaired_cubic_power_s_binary64_hex=[[x.hex() for x in row] for row in coefficients],
        s='(r-right)/(left-right), 0<=s<=1',
        full_original_state_order='all32 odd u, even v mean and all32 nonmean v',
        original_exact_offsets_and_alpha_used_before_reference_rounding=True)
    return Field(uc,32,1,fft,q(errors[0])),Field(vc,32,0,fft,q(errors[1])),definition


def target_reference(target,left,right,nu,fft):
    mid=(left+right)/2;half=(right-left)/2
    point,point_germ=target.coefficients(mid,mid,nu)
    whole,germ=target.coefficients(left,right,nu)
    fields={};definition={};fees={}
    for name in ('beta','gamma','K','s'):
        a=[point[name],q(half)*point[name+'1'],q(half*half)*point[name+'2']/2,
           q(half**3)*whole[name+'3']/6]
        chosen=[Fraction(float(value.mid())) for value in a]
        error=sum((ab(value-q(selected)) for value,selected in zip(a,chosen)),arb(0))
        coefficients=[sum((Fraction(comb(j,i)*(-2)**i)*chosen[j]
            for j in range(i,ORDER+1)),Fraction(0)) for i in range(ORDER+1)]
        fields[name]=Field.scalar(coefficients,fft,error)
        definition[name]=[float(value).hex() for value in chosen]
        fees[name]=record(error)
    return fields,dict(exact_original_scalar_germ=list(map(str,germ)),
        exact_midpoint_scalar_germ=list(map(str,point_germ)),
        scalar_target_power_t_binary64_hex=definition,t='2*(r-midpoint)/(right-left)=1-2*s',
        whole_original_third_jet_and_intrinsic_primitive_errors_retained=True,
        scalar_uniform_Wiener_errors=fees)


def raw_generator(u,v,a):
    beta,gamma,K=(a[name] for name in ('beta','gamma','K'))
    m=v.mean();up=u.derivative();vp=v.derivative()
    d=-beta*(u*u+K*v*v).primitive()
    a12=gamma*m*K;a21=-gamma*m
    L11=-beta*(1+3*u*u+K*v*v);L12=-2*beta*K*u*v
    L21=-2*beta*u*v;L22=beta*(1-u*u-3*K*v*v)
    tu=-2*beta*up;tv=-2*beta*vp;su=u;sv=K*v
    rank_u=gamma*K*vp;rank_v=-gamma*up
    matrices=[];Ts=[];Ds=[];frequency=Box(4*np.arange(1,MODES+1)[None,:])
    for k in range(ORDER+1):
        uu=rectangle(L11,k,True,True)+rectangle(d,k,True,False)[:,1:]*frequency
        uv=rectangle(L12,k,True,False)
        derivative=rectangle(a12,k,True,True)*frequency
        uv=Box(np.concatenate((uv.lo[:,:1],(uv[:,1:]-derivative).lo),axis=1),
               np.concatenate((uv.hi[:,:1],(uv[:,1:]-derivative).hi),axis=1))
        vu=rectangle(L21,k,False,True)+rectangle(a21,k,False,False)[:,1:]*frequency
        vv=rectangle(L22,k,False,False);derivative=rectangle(d,k,False,True)*frequency
        vv=Box(np.concatenate((vv.lo[:,:1],(vv[:,1:]-derivative).lo),axis=1),
               np.concatenate((vv.hi[:,:1],(vv[:,1:]-derivative).hi),axis=1))
        raw=matrix_from_box(Box(np.block([[uu.lo,uv.lo],[vu.lo,vv.lo]]),
                                  np.block([[uu.hi,uv.hi],[vu.hi,vv.hi]])))
        root2=arb(2).sqrt()
        for j in range(DIM):raw[MODES,j]*=root2
        for i in range(DIM):raw[i,MODES]/=root2
        # Complete independent even-mean rank-one column.
        for j in range(1,MODES+1):
            raw[j-1,MODES]+=-root2*box_scalar(rank_u.c.imag[j,k])
            raw[MODES+j,MODES]+=root2*box_scalar(rank_v.c.real[j,k])
        raw[MODES,MODES]+=box_scalar(rank_v.c.real[0,k])
        matrices.append(raw)
        top=rectangle(tu,k,True,True,MODES,INTERMEDIATE)
        bottom=rectangle(tv,k,False,True,MODES,INTERMEDIATE)
        T=matrix_from_box(Box(np.concatenate((top.lo,bottom.lo),axis=0),
                              np.concatenate((top.hi,bottom.hi),axis=0)))
        for j in range(INTERMEDIATE):T[MODES,j]*=root2
        leftpart=rectangle(su,k,False,True,INTERMEDIATE,MODES)[1:]
        rightpart=rectangle(sv,k,False,False,INTERMEDIATE,MODES)[1:]
        D=matrix_from_box(Box(np.concatenate((leftpart.lo,rightpart.lo),axis=1),
                              np.concatenate((leftpart.hi,rightpart.hi),axis=1)))
        for i in range(INTERMEDIATE):
            D[i,MODES]/=root2
            for j in range(DIM):D[i,j]/=4*(i+1)
        Ts.append(T);Ds.append(D)
    for k in range(ORDER+1):
        for i in range(k+1):matrices[k]+=Ts[i]*Ds[k-i]
    Tnorm=joint2(tu.norm,tv.norm);Dnorm=joint2(su.norm,sv.norm)/4
    Terror=joint2(tu.error,tv.error);Derror=joint2(su.error,sv.error)/4
    nonlocal_error=Tnorm*Derror+Terror*Dnorm+Terror*Derror
    for i in range(ORDER+1):
        ti=joint2(tu.coefficient_norms[i],tv.coefficient_norms[i])
        for j in range(ORDER+1):
            if i+j>ORDER:
                dj=joint2(su.coefficient_norms[j],sv.coefficient_norms[j])/4
                nonlocal_error+=ti*dj
    local_error=sum((field.error**2 for field in (L11,L12,L21,L22)),arb(0)).sqrt()
    error=(384*(d.error+max(a12.error,a21.error))+local_error+nonlocal_error
           +joint2(rank_u.error,rank_v.error)).upper()
    return matrices,error,dict(complete_primitive_intermediate_modes=INTERMEDIATE,
        complete_odd_head_modes=MODES,complete_even_head_modes_with_independent_mean=MODES+1,
        complete_raw_generator_uniform_error=record(error),
        both_nonlocal_mean_and_primitive_terms_retained=True,
        physical_full_Gram_used=True)


def block(matrix,row_start,row_end,col_start,col_end):
    return arb_mat([[matrix[i,j] for j in range(col_start,col_end)] for i in range(row_start,row_end)])


def weighted_generator(raw,raw_error,left,right,rho_left,rho_right):
    step=left-right;rho=[rho_right,rho_left-rho_right];ratio=rho[1]/rho[0]
    if min(rho_left,rho_right)<=0 or abs(ratio)>=1:
        raise ValueError('this exact positive radial weight cell needs refinement')
    inverse=[(-ratio)**j/rho_right for j in range(ORDER+1)]
    inverse_error=q(abs(ratio)**(ORDER+1)/(rho_right*(1-abs(ratio))))
    derivative=(rho_left-rho_right)/step
    out=[arb_mat(DIM,DIM) for _ in range(ORDER+1)]
    oe=[block(matrix,0,MODES,MODES,DIM) for matrix in raw]
    eo=[block(matrix,MODES,DIM,0,MODES) for matrix in raw]
    oe_norm=[matrix_norm(matrix) for matrix in oe];eo_norm=[matrix_norm(matrix) for matrix in eo]
    discarded=arb(0)
    for k in range(ORDER+1):
        for i in range(DIM):
            for j in range(DIM):
                if (i<MODES)==(j<MODES):out[k][i,j]=raw[k][i,j]
        for i in range(k+1):
            for row in range(MODES):
                for col in range(MODES,DIM):out[k][row,col]+=q(inverse[k-i])*raw[i][row,col]
            if k-i<len(rho):
                for row in range(MODES,DIM):
                    for col in range(MODES):out[k][row,col]+=q(rho[k-i])*raw[i][row,col]
        for row in range(MODES,DIM):out[k][row,row]+=q(derivative*inverse[k])
    for i in range(ORDER+1):
        for j in range(ORDER+1):
            if i+j>ORDER:discarded+=oe_norm[i]*q(abs(inverse[j]))
        for j in range(len(rho)):
            if i+j>ORDER:discarded+=eo_norm[i]*q(abs(rho[j]))
    condition=q(max(Fraction(1),rho_left,rho_right)/min(Fraction(1),rho_left,rho_right))
    error=(condition*raw_error+(sum(oe_norm,arb(0))+q(abs(derivative)))*inverse_error+discarded).upper()
    return out,error,dict(exact_rho_left=str(rho_left),exact_rho_right=str(rho_right),
        exact_rho_derivative=str(derivative),radial_weight_condition_upper=record(condition),
        exact_reference_inverse_rho_coefficients=list(map(str,inverse)),
        inverse_rho_uniform_remainder=record(inverse_error),
        complete_weighted_generator_uniform_error=record(error),
        exact_even_diagonal_Rprime_over_R_retained=True,
        new_reference_radial_order=ORDER,
        omitted_radial_polynomial_products_paid=record(discarded))


def complete_cell_model(cube,knot,left,right,alpha,nu,offset,target,rho_left,rho_right,fft):
    u,V,physical_definition=physical_reference(cube,knot,left,right,alpha,offset,fft)
    a,target_definition=target_reference(target,left,right,nu,fft);v=V+a['s']
    raw,error,raw_record=raw_generator(u,v,a)
    weighted,error,weight_record=weighted_generator(raw,error,left,right,rho_left,rho_right)
    definition=dict(kind='new_exact_full_weighted_degree3_generator_reference_from_recorded_dyadics',
        physical_background=physical_definition,scalar_target=target_definition,
        exact_weight=weight_record,raw_complete_operator=raw_record,
        reference_rule='exact reflection Fourier algebra and degree3 radial truncation at every operation; all discarded terms are included in the displayed uniform error',
        no_unstored_original_proposal_matrix_is_assumed_identical=True,
        all_mean_and_primitive_columns_retained=True)
    return weighted,error,definition
