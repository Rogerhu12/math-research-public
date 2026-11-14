#!/usr/bin/env python3
"""Fourier assembly of the real fixed-g adaptive Frenet Jacobian.

The local JVP is linear in its two Cartesian arguments. Six calls recover
its 3 by 3 coefficient fields. Sparse Fourier products then implement the
same finite trapezoidal projection. The RHS, metric, BC, tolerance, and
mean reconstruction are unchanged. Floating point summation is reordered;
this is not a byte-identical implementation or a derivative certificate.
"""
import numpy as np
from scipy.sparse import coo_matrix


def add_term(target, component, frequency, value):
    key=(component,frequency)
    target[key]=target.get(key,0j)+value


def cylindrical_fourier_coefficients(modes, frequencies):
    er={(0,1):.5,(0,-1):.5,(1,1):-.5j,(1,-1):.5j}
    et={(0,1):.5j,(0,-1):-.5j,(1,1):.5,(1,-1):.5}
    result=[{} for _ in range(3*modes+1)]
    result[0]=er.copy()
    for j,frequency in enumerate(frequencies):
        k=int(frequency)
        for (component,f),value in er.items():
            add_term(result[j+1],component,f+k,value/2)
            add_term(result[j+1],component,f-k,value/2)
        for (component,f),value in et.items():
            add_term(result[modes+j+1],component,f+k,-.5j*value)
            add_term(result[modes+j+1],component,f-k,.5j*value)
        add_term(result[2*modes+j+1],2,k,.5)
        add_term(result[2*modes+j+1],2,-k,.5)
    return [{key:value for key,value in row.items() if value} for row in result]


def build_tables(flow):
    n,M=flow.n,flow.M
    N=flow.B.shape[1]
    if n!=3*M+1 or flow.B.shape!=(n,N,3):
        raise ValueError('The complete cylindrical basis is required')
    if len(flow.even)!=M or min(flow.even)<2:
        raise ValueError('Unsupported physical Fourier frequencies')
    coefficients=cylindrical_fourier_coefficients(M,flow.even)
    norms=np.sum(flow.B*flow.B,axis=(1,2))/N
    rows=[]; columns=[]; first=[]; second=[]
    for i,output in enumerate(coefficients):
        for j,input_basis in enumerate(coefficients):
            row=i*n+j
            for (a,p),left in output.items():
                for (b,q),right in input_basis.items():
                    common=left*right/norms[i]
                    rows.append(row)
                    columns.append((3*a+b)*N+((-p-q)%N))
                    first.append(common*(1j*q))
                    second.append(common*(-q*q))
    shape=(n*n,9*N)
    A=coo_matrix((np.asarray(first),(rows,columns)),shape=shape).tocsr()
    B=coo_matrix((np.asarray(second),(rows,columns)),shape=shape).tocsr()
    A.sum_duplicates();B.sum_duplicates();A.eliminate_zeros();B.eliminate_zeros()
    return dict(n=n,M=M,N=N,first=A,second=B,
                source='analytic complete cylindrical Fourier basis',
                imaginary_max=0.,evaluated_points=0,calls=0)


def adapt_fun_jac(flow,s,y,p):
    s=np.asarray(s)
    y=np.asarray(y)
    if np.iscomplexobj(y) or y.shape!=(flow.n,len(s)):
        raise ValueError('Real fixed-g states with the original shape are required')
    cached=getattr(flow,'_fourier_jacobian_tables',None)
    if cached is None:
        cached=build_tables(flow)
        flow._fourier_jacobian_tables=cached
    n,N=flow.n,flow.B.shape[1]
    if (cached['n'],cached['N'])!=(n,N):
        raise ValueError('Flow basis changed after assembly')
    out=np.empty((n,n,len(s)))
    zero=np.zeros((1,1,3))
    for start in range(0,len(s),64):
        part=slice(start,start+64)
        fr=flow.frame(s[part],flow.q*y[:,part])
        count=len(s[part])
        L=np.empty((count,N,3,3))
        K=np.empty_like(L)
        for component in range(3):
            unit=np.zeros((1,1,3));unit[0,0,component]=1.
            L[:,:,:,component]=(flow.frame_jvp(fr,unit,zero)
                +fr['geo']['v'][:,:,None]*unit)
            K[:,:,:,component]=flow.frame_jvp(fr,zero,unit)
        Lhat=(np.fft.fft(L,axis=1)/N).transpose(2,3,1,0).reshape(9*N,count)
        Khat=(np.fft.fft(K,axis=1)/N).transpose(2,3,1,0).reshape(9*N,count)
        packed=cached['first']@Lhat+cached['second']@Khat
        cached['imaginary_max']=max(cached['imaginary_max'],float(np.max(np.abs(packed.imag))))
        out[:,:,part]=packed.real.reshape(n,n,count)
    cached['calls']+=1;cached['evaluated_points']+=len(s)
    return out,np.zeros((n,flow.M,len(s)))


def install(adaptive):
    """Select the backend for subsequent classes; return the old builder."""
    original=adaptive.build_classes
    def selected(chart):
        Flow,BVP=original(chart)
        Flow.adapt_fun_jac=adapt_fun_jac
        return Flow,BVP
    adaptive.build_classes=selected
    return original
