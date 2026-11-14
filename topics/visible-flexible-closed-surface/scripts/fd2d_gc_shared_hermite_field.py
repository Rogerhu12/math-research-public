#!/usr/bin/env python3
"""Thin actual C1 Hermite/Fourier definition for R119 residual consumers.

Defining binary64 arrays are shared node values and FIRST radial jets, not
independently rounded per-span power coefficients. Exact cubic Hermite
formulas make the mathematical field C1. The finite numerical evaluator
below is a screening interface; continuous interval bounds are separate.
Chart metadata may describe a fixed or a moving computational angle.
"""
from __future__ import annotations
import gzip
import hashlib
import io
import json
from fractions import Fraction
from pathlib import Path
import numpy as np

LD = np.longdouble
SCHEMA = 'fd2d-gc-shared-c1-hermite-field-v1'


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def write_field(directory, nodes, values, first_s, *, chart, target, provenance,
                complete_target_prefix=False, derivative_source, source_coefficients=None):
    """Save one actual finite field; provenance does not assert a solved BVP."""
    directory = Path(directory)
    if directory.exists():
        raise FileExistsError('Use a new field directory')
    nodes, values, first_s = (np.asarray(x, dtype=np.float64) for x in (nodes, values, first_s))
    if nodes.ndim != 1 or len(nodes)<2 or np.any(np.diff(nodes)<=0):
        raise ValueError('Strictly increasing radial nodes are required')
    if values.ndim!=2 or first_s.shape!=values.shape or values.shape[0]!=len(nodes) or values.shape[1]%2!=1:
        raise ValueError('Expected (nodes,2K+1) shared values and first jets')
    if not all(np.all(np.isfinite(x)) for x in (nodes,values,first_s)):
        raise ValueError('All defining binary data must be finite')
    dimension = values.shape[1]
    K = (dimension-1)//2
    directory.mkdir(parents=True)
    per = min(128,max(2,750000//(8*(2*dimension+1))))
    shards=[]
    for left in range(0,len(nodes)-1,per-1):
        right=min(left+per,len(nodes))
        buffer=io.BytesIO()
        np.savez(buffer,nodes=nodes[left:right],values=values[left:right],first_s=first_s[left:right])
        payload=gzip.compress(buffer.getvalue(),compresslevel=6,mtime=0)
        if len(payload)>5_000_000:
            raise ValueError('A field shard exceeds the repository file limit')
        path=directory/f'nodes-{left:06d}-{right:06d}.npz.gz'
        path.write_bytes(payload)
        shards.append(dict(file=path.name,sha256=hashlib.sha256(payload).hexdigest(),bytes=len(payload),
                           first_node=left,stop_node=right))
    manifest=dict(schema=SCHEMA,definition='exact cubic Hermite of shared binary64 values and first-s jets',
        dtype='little-endian float64 stored by numpy',node_count=len(nodes),dimension=dimension,
        n_modes=list(range(0,2*K+1,2)),m_modes=list(range(2,2*K+1,2)),
        state_order='[n_0,n_2,...,n_(2K),m_2,...,m_(2K)] real cos/sin amplitudes; no sqrt(2)',
        radial_domain_exact=[str(Fraction(float(nodes[0]))),str(Fraction(float(nodes[-1])))],
        chart=chart,target=target,provenance=provenance,derivative_source=derivative_source,
        source_coefficients=source_coefficients,shards=shards,
        source=identity(__file__),complete_target_prefix=bool(complete_target_prefix),
        exact_C1_definition=True,continuous_residual_bounded_here=False,closed_surface=False)
    path=directory/'field.json'
    path.write_text(json.dumps(manifest,indent=2,allow_nan=False)+'\n')
    return path


class SharedHermiteGCField:
    def __init__(self,path):
        self.path=Path(path);self.meta=json.loads(self.path.read_text())
        if self.meta['schema']!=SCHEMA:
            raise ValueError('Unsupported actual field definition')
        pieces=[];previous=None;last_stop=0
        for row in self.meta['shards']:
            payload=(self.path.parent/row['file']).read_bytes()
            if hashlib.sha256(payload).hexdigest()!=row['sha256']:
                raise ValueError('A defining field shard changed')
            with np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False) as raw:
                block={key:raw[key].copy() for key in ('nodes','values','first_s')}
            if not all(x.dtype==np.float64 and np.all(np.isfinite(x)) for x in block.values()):
                raise ValueError('The defining shard has an unexpected dtype or a nonfinite value')
            if len(block['nodes'])!=row['stop_node']-row['first_node']:
                raise ValueError('Shard node range disagrees with its arrays')
            if previous is None:
                if row['first_node']!=0:raise ValueError('The first radial node is missing')
                pieces.append(block)
            else:
                if row['first_node']!=last_stop-1:raise ValueError('Radial shard coverage is not contiguous')
                if not all(np.array_equal(previous[key][-1],block[key][0]) for key in block):
                    raise ValueError('Shared value/first jet differs between shards')
                pieces.append({key:value[1:] for key,value in block.items()})
            previous,last_stop=block,row['stop_node']
        arrays={key:np.concatenate([p[key] for p in pieces],axis=0) for key in ('nodes','values','first_s')}
        self.nodes,self.values,self.first_s=(arrays[key] for key in ('nodes','values','first_s'))
        if len(self.nodes)!=self.meta['node_count'] or np.any(np.diff(self.nodes)<=0):
            raise ValueError('The radial field coverage is inconsistent')
        self.dimension=self.meta['dimension'];self.K=(self.dimension-1)//2
        if self.values.shape!=(len(self.nodes),self.dimension) or self.first_s.shape!=self.values.shape:
            raise ValueError('The field arrays have incompatible dimensions')
        if self.meta['n_modes']!=list(range(0,2*self.K+1,2)) or self.meta['m_modes']!=list(range(2,2*self.K+1,2)):
            raise ValueError('Unexpected angular basis')
        self.frequencies=2*np.arange(1,self.K+1,dtype=LD)

    def normalized_power(self,index):
        """Floating representative of the exact rational Hermite formula.

        A strict interval consumer must evaluate this formula with outward
        arithmetic on the stored binary endpoints and the EXACT node gap.
        It must not promote the rounded result here to an exact input.
        """
        h=LD(self.nodes[index+1])-LD(self.nodes[index])
        y0,y1=(np.asarray(x,dtype=LD) for x in self.values[index:index+2])
        d0,d1=(np.asarray(x,dtype=LD) for x in self.first_s[index:index+2])
        c0,c1=y0,h*d0
        delta=y1-y0
        c2=3*delta-h*(2*d0+d1)
        c3=-2*delta+h*(d0+d1)
        return np.stack((c0,c1,c2,c3)),h

    def state(self,s,radial_order=0):
        s=np.atleast_1d(np.asarray(s,dtype=LD))
        if np.any(s<LD(self.nodes[0])) or np.any(s>LD(self.nodes[-1])):
            raise ValueError('Outside the actual radial field interval')
        ids=np.clip(np.searchsorted(self.nodes,s,side='right')-1,0,len(self.nodes)-2)
        out=np.empty((len(s),self.dimension),dtype=LD)
        for index in np.unique(ids):
            mask=ids==index;power,h=self.normalized_power(int(index));t=(s[mask]-LD(self.nodes[index]))/h
            if radial_order==0:
                out[mask]=power[0]+t[:,None]*(power[1]+t[:,None]*(power[2]+t[:,None]*power[3]))
            elif radial_order==1:
                out[mask]=(power[1]+t[:,None]*(2*power[2]+3*t[:,None]*power[3]))/h
            else:raise ValueError('Only the required value and first radial derivative are supplied')
        return out

    def evaluate(self,s,angle):
        angle=np.atleast_1d(np.asarray(angle,dtype=LD))
        y,ys=self.state(s),self.state(s,1)
        phase=self.frequencies[:,None]*angle[None,:]
        co,si=np.cos(phase),np.sin(phase);k=self.frequencies[:,None]
        n0,n,m=y[:,0:1],y[:,1:self.K+1],y[:,self.K+1:]
        ns0,ns,ms=ys[:,0:1],ys[:,1:self.K+1],ys[:,self.K+1:]
        return dict(n=n0+n@co,m=m@si,ns=ns0+ns@co,ms=ms@si,
            nxi=n@(-k*si),mxi=m@(k*co),
            nxixi=n@(-k*k*co),mxixi=m@(-k*k*si),
            nsxi=ns@(-k*si),msxi=ms@(k*co))


def codazzi_numerators(a,ap,app,q,U_s,n,m,ns,ms,nxi,mxi):
    """Coefficient-first residuals: q=U_xi>0, w=U_s/q, g fixed.

    This formula uses only +,-,* and so also accepts the existing strict
    polynomial/Fourier interval types. Denominators are enclosed afterward.
    The ns/ms inputs are derivatives at fixed COMPUTATIONAL angle xi.
    """
    aa,nn=a*a,n*n
    Pn=q*(aa*n*ns-a*ap*(m*m-nn)+ap*app)-aa*U_s*n*nxi-a*n*mxi
    Pm=q*(aa*nn*ms+2*a*ap*m*nn)-aa*U_s*nn*mxi-2*a*m*n*mxi+a*m*m*nxi-app*nxi
    return dict(Pn=Pn,Pm=Pm,Dn=aa*q*n,Dm=aa*q*nn)


def codazzi_sample_residual(fields,a,ap,app,q,U_s=0):
    """Low-cost numerical screen; never a continuous residual certificate."""
    a,ap,app=(np.atleast_1d(np.asarray(x,dtype=LD))[:,None] for x in (a,ap,app))
    q,U_s=np.asarray(q,dtype=LD),np.asarray(U_s,dtype=LD)
    if np.any(a<=0) or np.any(q<=0) or np.any(fields['n']<=0):
        raise ArithmeticError('Positive a, U_xi and n are required by this chart')
    n,m=fields['n'],fields['m'];c,K=ap/a,-app/a
    l=(m*m+K)/n
    lxi=(2*m*fields['mxi']-l*fields['nxi'])/n
    Rn=fields['ns']-(U_s/q)*fields['nxi']-fields['mxi']/(a*q)-c*(l-n)
    Rm=fields['ms']-(U_s/q)*fields['mxi']-lxi/(a*q)+2*c*m
    polynomials=codazzi_numerators(a,ap,app,q,U_s,n,m,fields['ns'],fields['ms'],fields['nxi'],fields['mxi'])
    return dict(Rn=Rn,Rm=Rm,l=l,K=K,
                numerator_Rn=polynomials['Pn']/polynomials['Dn'],
                numerator_Rm=polynomials['Pm']/polynomials['Dm'],
                **polynomials)
