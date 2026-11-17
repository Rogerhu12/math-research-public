#!/usr/bin/env python3
"""Same finite N angle-value operator through FFT synthesis/transposes.

This changes the implementation of finite trig matrices, not the full
analytic circle lift or the angle-value objective.  Real/imaginary input
parts are transformed separately, preserving complex-step continuation.
No continuous-spectrum alias/completeness statement is made.

Optional base cache stores the actual V,d at every evaluation point.  It
is used only for an exactly identical real free vector.  No nonlinear
solver, warm construction, or scientific probe is launched on import.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys
import numpy as np

DENSE_SHA = 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d'


class TrigMatrix:
    """The same sampled cosine/sine matrix, or its ordinary transpose.

    C columns have frequencies 0,2,...,2M; S columns have 2,...,2M.
    C[:,1:] is supported.  Products are one-dimensional vector products.
    The transpose is the finite Euclidean transpose (no 1/N factor).
    """

    def __init__(self,N,M,kind,*,constant=True,transposed=False,sign=1):
        self.N,self.M,self.kind = int(N),int(M),kind
        self.constant = bool(constant and kind=='cos')
        self.transposed = bool(transposed)
        self.sign = int(sign)
        if self.sign not in (-1,1):raise ValueError('Only exact signed trig views are supported')
        if self.N%2 or self.N<=4*self.M or self.M<1 or kind not in ('cos','sin'):
            raise ValueError('This finite trig implementation requires even N>4M')
        self.freq=2*np.arange(1,self.M+1)
        self.columns=self.M+int(self.constant)

    @property
    def shape(self):
        return (self.columns,self.N) if self.transposed else (self.N,self.columns)

    @property
    def T(self):
        return TrigMatrix(self.N,self.M,self.kind,constant=self.constant,transposed=not self.transposed,sign=self.sign)

    def __getitem__(self,key):
        if (self.transposed or self.kind!='cos' or not self.constant
            or not isinstance(key,tuple) or len(key)!=2
            or key[0]!=slice(None) or key[1]!=slice(1,None)):
            raise IndexError('Only the actual C[:,1:] view is implemented')
        return TrigMatrix(self.N,self.M,'cos',constant=False,sign=self.sign)

    def __neg__(self):
        return TrigMatrix(self.N,self.M,self.kind,constant=self.constant,transposed=self.transposed,sign=-self.sign)

    def _real_product(self,x):
        if self.transposed:
            z=np.fft.rfft(x)
            if self.kind=='sin':
                return -z[self.freq].imag
            v=z[self.freq].real
            return np.concatenate(([z[0].real],v)) if self.constant else v
        z=np.zeros(self.N//2+1,dtype=complex)
        if self.kind=='sin':
            z[self.freq]=-0.5j*self.N*x
        else:
            if self.constant:
                z[0]=self.N*x[0]
                x=x[1:]
            z[self.freq]=0.5*self.N*x
        return np.fft.irfft(z,n=self.N)

    def __matmul__(self,x):
        x=np.asarray(x)
        if x.ndim!=1 or x.shape[0]!=self.shape[1]:
            raise ValueError('Wrong finite trigonometric matrix-vector shape')
        if np.iscomplexobj(x):
            return self.sign*(self._real_product(x.real)+1j*self._real_product(x.imag))
        return self.sign*self._real_product(x)


class FFTMixin:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.cos=TrigMatrix(self.N,self.M,'cos')
        self.sin=TrigMatrix(self.N,self.M,'sin')
        self._base_x=None
        self._base_p=None
        self._base_first=None
        self.cache_builds=0
        self.cache_hits=0

    def prepare(self,x):
        x=np.asarray(x)
        if (self._base_x is not None and x.dtype==self._base_x.dtype
                and x.shape==self._base_x.shape and np.array_equal(x,self._base_x)):
            self.cache_hits+=1
            return self._base_p
        return super().prepare(x)

    def _first(self,p,stage):
        if p is self._base_p and self._base_first is not None:
            return self._base_first[0,stage],self._base_first[1,stage]
        return super()._first(p,stage)

    def set_base(self,x):
        """Build once per actual real linearization point, never implicitly."""
        x=np.asarray(x)
        if np.iscomplexobj(x) or x.dtype!=np.dtype(float) or x.shape!=(self.free_size,):
            raise ValueError('Cache requires the actual float64 real free vector')
        p=super().prepare(x)
        values=np.empty((2,self.P,self.N,3),dtype=float)
        for j in range(self.P):
            values[0,j],values[1,j]=super()._first(p,j)
        values.setflags(write=False)
        frozen=x.copy();frozen.setflags(write=False)
        self._base_x=frozen
        self._base_p=p
        self._base_first=values
        self.cache_builds+=1
        return dict(first_derivative_cache_bytes=int(values.nbytes),base_vector_bytes=int(frozen.nbytes),
                    full_stages=self.P,all_angles=self.N,cache_builds=self.cache_builds,
                    same_angle_value_model=True,continuous_geometry_certified=False)

    def clear_base(self):
        self._base_x=None
        self._base_p=None
        self._base_first=None


def create(dense_source,*args,**kwargs):
    """Create an FFT implementation of the exact SHA-bound dense class."""
    dense_source=Path(dense_source)
    if hashlib.sha256(dense_source.read_bytes()).hexdigest()!=DENSE_SHA:
        raise ValueError('The audited dense operator source changed')
    name='fullclosed_dense_'+DENSE_SHA[:16]
    if name in sys.modules:
        dense=sys.modules[name]
    else:
        spec=importlib.util.spec_from_file_location(name,dense_source)
        dense=importlib.util.module_from_spec(spec);sys.modules[name]=dense
        spec.loader.exec_module(dense)
    class FFTClosedGram(FFTMixin,dense.ClosedGram):
        pass
    return FFTClosedGram(*args,**kwargs)


if __name__=='__main__':
    raise SystemExit('Import-only FFT implementation: requires the same actual input and saved unique dense probe for comparison; no solve is launched.')
