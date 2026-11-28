#!/usr/bin/env python3
"""Finite all-near-pair normal-ball search on actual complete released cores.

The surface is capped by its original flat disks, not by surrogate sampled
markers. A finite minimum is an obstruction candidate, never a reach lower
bound. All evaluated positions and normals come from the saved full field.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from fractions import Fraction as Q
from pathlib import Path
import sys
import time
from types import SimpleNamespace

for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[variable] = '1'
import numpy as np
from scipy.spatial import cKDTree


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def run(args):
    start = time.monotonic()
    work = args.work.resolve()
    receipt = json.loads(args.command_receipt.read_text())
    cmd = receipt['command']
    names = ('scripts', 'ramp', 'coast', 'prepared', 'independent',
             'seed-design', 'donor', 'donor-field', 'frozen')
    values = {}
    for name in names:
        value = Path(cmd[cmd.index('--' + name) + 1])
        values[name.replace('-', '_')] = value if value.is_absolute() else (work / value).resolve()
    a = SimpleNamespace(**values)
    ext_path = work / '2ecf-polar-released-developed-cut-to-actual-flat-collar.py'
    ext = load(ext_path, 'actual_released_source_for_normal_pairs')
    state = json.loads(args.state.read_text())
    assert state['entrySHA256'] == sha(ext_path)
    assert state['fieldSHA256'] == sha(args.field)
    assert state['rampSHA256'] == sha(a.ramp)
    assert state['coastSHA256'] == sha(a.coast)
    ends, ref, b, oldS, T, radius, target = ext.setup(a)
    assert state['targetSHA256'] == target['targetSHA256']
    assert state['trueNewRadius'] == str(radius)
    field = ext.base.MaterialField(args.field, ends)
    master = ends.master
    c, ramp, coast = master.c, master.ramp, master.coast
    delta = float(Q(c) + Q(ramp) + Q(coast) - Q(b))
    u = 2 * np.pi * (np.arange(args.angles) + args.angle_shift) / args.angles
    keys = ('X', 'Xs', 'Xu', 'Xss', 'Xsu', 'Xuu')
    # Same literal-coordinate short-coast map used by the actual source.
    def prefix(s):
        if s <= c + ramp:
            return np.stack([master.jet(s, u)[key] for key in keys])
        x = s - (c + ramp)
        t = x / (coast - delta)
        sigma = x + delta * t**3 * (10 + t * (-15 + 6*t))
        if s == b:
            sigma = coast
        ds = 1 + delta * 30 * t*t*(1-t)**2 / (coast-delta)
        dss = delta * 60*t*(1-t)*(1-2*t)/(coast-delta)**2
        p = ends.warm.packet_from_port(master.coast_port(sigma, u))
        p['Xss'] = p['Xss']*ds*ds + p['Xs']*dss
        p['Xs'] *= ds
        p['Xsu'] *= ds
        return np.stack([p[key] for key in keys])
    ramp_nodes = c + np.unique(np.r_[master.sx, (master.sx[:-1]+master.sx[1:])/2])
    pref_s = np.unique(np.r_[np.linspace(0,c,13), ramp_nodes, np.linspace(c+ramp,b,9)])
    pref_s = pref_s[pref_s < b]
    connector_s = np.unique(np.r_[field.knots, (field.knots[:-1]+field.knots[1:])/2])
    flat_r = np.linspace(float(radius), 0, 25)[1:-1]
    flat_s = oldS + .8 - flat_r
    nodes = np.r_[pref_s, connector_s, flat_s]
    labels = (['prefix']*len(pref_s) + ['released']*len(connector_s)
              + ['flat_disk']*len(flat_s))
    jets = []
    for s in pref_s:
        jets.append(prefix(float(s)))
    for i in range(0, len(connector_s), 12):
        jets.extend(field.position(connector_s[i:i+12],u))
    for r in flat_r:
        p = ext.flat_port(u,float(r))
        jets.append(np.stack([p[key] for key in ('P','V','Pu','A','Vu','Puu')]))
    j = np.asarray(jets)
    N = np.cross(j[:,1],j[:,2])
    area = np.linalg.norm(N,axis=-1)
    if np.min(area) <= 0:
        raise ArithmeticError('Actual sampled immersion failed')
    N /= area[...,None]
    x = j[:,0]
    polar_numerator = x[:,:,0]*j[:,2,:,1]-x[:,:,1]*j[:,2,:,0]
    rho2 = np.sum(x[:,:,:2]**2,axis=-1)
    phi_u = polar_numerator/rho2
    phi_s = (x[:,:,0]*j[:,1,:,1]-x[:,:,1]*j[:,1,:,0])/rho2
    rho_s = np.sum(x[:,:,:2]*j[:,1,:,:2],axis=-1)/np.sqrt(rho2)
    rho_u = np.sum(x[:,:,:2]*j[:,2,:,:2],axis=-1)/np.sqrt(rho2)
    radial_at_fixed_phi = rho_s-rho_u*phi_s/phi_u
    height_at_fixed_phi = j[:,1,:,2]-j[:,2,:,2]*phi_s/phi_u
    oblique = {str(k):float(np.min(height_at_fixed_phi-k*radial_at_fixed_phi))
               for k in (.15,.25,.4,.6,.8,1.,1.2)}
    upper_x = x.reshape(-1,3)
    upper_n = N.reshape(-1,3)
    meta = np.array([(float(s),float(v)) for s in nodes for v in u])
    piece = np.repeat(np.asarray(labels),len(u))
    lower_mask = meta[:,0]>0
    reflection = np.array([1.,1.,-1.])
    points = np.vstack([upper_x,upper_x[lower_mask]*reflection,
                        [[0,0,.415],[0,0,-.415]]])
    normals = np.vstack([upper_n,upper_n[lower_mask]*reflection,
                         [[0,0,1],[0,0,1]]])
    metadata = np.vstack([meta,meta[lower_mask]*np.array([-1.,1.]),
                          [[oldS+.8,0],[-oldS-.8,0]]])
    pieces = np.r_[piece,piece[lower_mask],['flat_center','flat_center']]
    tree = cKDTree(points)
    minima = {'all_near_pairs':None,'material_separated':None,
              'opposite_open_halves':None,'different_pieces':None}
    counts = {key:0 for key in minima}
    tests = 0
    def update(key, ii, jj, vals, squared, dot):
        counts[key] += len(vals)
        if not len(vals):return
        k = int(np.argmin(vals))
        if minima[key] is None or vals[k] < minima[key]['normalBallRatio']:
            i,jj0=int(ii[k]),int(jj[k])
            minima[key] = dict(normalBallRatio=float(vals[k]),distance=float(np.sqrt(squared[k])),
                maxAbsoluteNormalDot=float(dot[k]),indices=[i,jj0],
                material=[metadata[i].tolist(),metadata[jj0].tolist()],
                pieces=[str(pieces[i]),str(pieces[jj0])],
                points=[points[i].tolist(),points[jj0].tolist()],
                normals=[normals[i].tolist(),normals[jj0].tolist()])
    for begin in range(0,len(points),128):
        near = tree.query_ball_point(points[begin:begin+128],args.pair_radius,workers=1)
        ii,jj=[],[]
        for n,row in enumerate(near):
            i=begin+n
            row=[k for k in row if k>i]
            ii.extend([i]*len(row));jj.extend(row)
        if not ii:continue
        ii=np.asarray(ii,dtype=np.int64);jj=np.asarray(jj,dtype=np.int64)
        d=points[jj]-points[ii]
        d2=np.sum(d*d,axis=1)
        dot=np.maximum(np.abs(np.sum(normals[ii]*d,axis=1)),np.abs(np.sum(normals[jj]*d,axis=1)))
        use=(d2>1e-20)&(dot>1e-14)
        ii,jj,d2,dot=ii[use],jj[use],d2[use],dot[use]
        val=d2/(2*dot);tests+=len(val)
        angular = np.abs(np.angle(np.exp(1j*(metadata[ii,1]-metadata[jj,1]))))
        ds=np.abs(metadata[ii,0]-metadata[jj,0])
        groups={'all_near_pairs':np.ones(len(val),bool),
                'material_separated':(ds>.15)|(angular>.4),
                'opposite_open_halves':(metadata[ii,0]*metadata[jj,0]<0)&(ds>.15),
                'different_pieces':pieces[ii]!=pieces[jj]}
        for key,mask in groups.items():
            update(key,ii[mask],jj[mask],val[mask],d2[mask],dot[mask])
    held = min(float(np.min(np.linalg.norm(points-np.array([0,sign*master.A,0]),axis=1))) for sign in (-1,1))
    result=dict(schema='actual-released-complete-flat-disk-core-finite-normal-pairs-v1',
        entrySHA256=sha(__file__),fieldSHA256=sha(args.field),stateSHA256=sha(args.state),
        sourceEntrySHA256=sha(ext_path),targetSHA256=target['targetSHA256'],
        commandReceiptSHA256=sha(args.command_receipt),angles=args.angles,angleShift=args.angle_shift,
        radii=len(nodes),points=len(points),pairSearchRadius=args.pair_radius,
        testedPairs=tests,categoryCounts=counts,minimumPairs=minima,
        actualHalfDomain=[0.,b,oldS,T,oldS+.8],trueFlatJoinRadius=str(radius),
        sampledMinimumArea=float(area.min()),sampledMinimumPolarAngleDerivative=float(phi_u.min()),
        sampledObliqueDerivativeMinima=oblique,sampledHeld=held,
        sampledNormMaximum=float(np.linalg.norm(points,axis=1).max()),
        sampledWidth=float(np.max(np.abs(points[:,1]))),
        claims=dict(actualCompleteCore=True,trueOriginalFlatDisks=True,
                    outerFixedCapsSampled=False,finiteOnly=True,reachLowerBound=False,
                    strictObstruction=False),seconds=time.monotonic()-start)
    with args.output.open('x') as f:
        json.dump(result,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps({key:result[key] for key in ('fieldSHA256','points','testedPairs','minimumPairs',
          'sampledMinimumPolarAngleDerivative','sampledObliqueDerivativeMinima','sampledHeld','seconds')}),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    for name in ('work','command-receipt','state','field','output'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--angles',type=int,default=96)
    parser.add_argument('--angle-shift',type=float,default=.271)
    parser.add_argument('--pair-radius',type=float,default=.194)
    run(parser.parse_args())
