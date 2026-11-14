#!/usr/bin/env python3
"""Finite nonlinear Frenet-flow diagnostic for an exact elliptic inlet.

This is an initial-value screen for a NEW metric, not a boundary-value solve,
not a certified continuum computation, and not a closed flexible surface.
Its termination event reports loss of the chosen positive-binormal chart or
loss of numerical metric accuracy; either can require a BVP or another chart.
It never transfers a linear tail condition to a nonlinear endpoint.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
_sp = importlib.util.spec_from_file_location('fd2d_short_core', HERE / 'fd2d_short_core_screen.py')
short = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(short)


class Meridian:
    def __init__(self, segments, a0):
        self.segments = []
        self.end = 0.
        aa = float(a0)
        for original in segments:
            if original['L'] <= 1e-14:
                continue
            seg = dict(original, s0=self.end, a0=aa)
            self.end += seg['L']
            seg['s1'] = self.end
            aa += seg['dr']
            self.segments.append(seg)

    @staticmethod
    def partial(seg, u):
        result = 0.
        cuts = [0., .08, .92, 1.] if seg['kind'] == 'turn' else [0., 1.]
        for lo, hi in zip(cuts[:-1], cuts[1:]):
            width = np.clip(u - lo, 0., hi - lo)
            phi = short.phase(seg, lo + width * short.G)
            result += width * np.dot(np.sin(phi), short.W)
        return float(result)

    def jet(self, s):
        seg = next((x for x in self.segments if s < x['s1'] - 1e-14), self.segments[-1])
        u = np.clip((s - seg['s0']) / seg['L'], 0., 1.)
        phi = float(short.phase(seg, u))
        if seg['kind'] == 'turn':
            dp = np.sign(seg['p1'] - seg['p0']) * seg['K'] * float(short.ramp(u)[0])
        elif seg['kind'] == 'brake':
            dp = 2 * (seg['p1'] - seg['p0']) * u / seg['L']
        else:
            dp = 0.
        return (seg['a0'] + seg['L'] * self.partial(seg, u),
                math.sin(phi), math.cos(phi) * dp)


class Flow:
    def __init__(self, meridian, nodes, A, B, a0, max_calls):
        self.meridian = meridian
        self.nodes = nodes
        self.a0 = a0
        self.max_calls = max_calls
        self.calls = 0
        self.k = np.fft.fftfreq(nodes, 1 / nodes)
        theta = np.arange(nodes) * (2 * np.pi / nodes)
        self.initial = np.column_stack((A * np.cos(theta), B * np.sin(theta), np.zeros(nodes)))
        self.initial_speed = np.sqrt(A * A * np.sin(theta)**2 + B * B * np.cos(theta)**2)

    def derivative(self, x, order=1):
        return np.fft.ifft(np.fft.fft(x, axis=0) * ((1j * self.k)**order)[:, None], axis=0).real

    def frame(self, s, flat):
        X = np.asarray(flat).reshape(self.nodes, 3)
        xp, xpp = self.derivative(X), self.derivative(X, 2)
        ell = np.linalg.norm(xp, axis=1)
        T = xp / ell[:, None]
        c = xpp - np.sum(xpp * T, axis=1)[:, None] * T
        clen = np.linalg.norm(c, axis=1)
        kappa = clen / ell**2
        N = c / clen[:, None]
        B = np.cross(T, N)
        aa, vv, acc = self.meridian.jet(s)
        alpha = -vv / (aa * kappa)
        chart = 1 - alpha**2
        beta = np.sqrt(np.maximum(chart, 1e-14))
        V = alpha[:, None] * N + beta[:, None] * B
        return dict(X=X, xp=xp, xpp=xpp, ell=ell, T=T, N=N, B=B, kappa=kappa,
                    aa=aa, vv=vv, acc=acc, alpha=alpha, beta=beta, chart=chart, V=V)

    def rhs(self, s, y):
        self.calls += 1
        if self.calls > self.max_calls:
            raise RuntimeError('Finite diagnostic RHS-call limit reached; no endpoint result.')
        return self.frame(s, y)['V'].ravel()

    def metric_error(self, s, y):
        fr = self.frame(s, y)
        target = fr['aa'] / self.a0 * self.initial_speed
        return float(np.max(abs(fr['ell']**2 / target**2 - 1)))

    def acceleration(self, frame, curvature_s):
        return frame['acc']

    def diagnostics(self, s, y):
        f = self.frame(s, y)
        X, xp, xpp, ell, T, N, B = (f[k] for k in ('X','xp','xpp','ell','T','N','B'))
        V, alpha, beta, kappa = (f[k] for k in ('V','alpha','beta','kappa'))
        vp, vpp = self.derivative(V), self.derivative(V, 2)
        ell_s = np.sum(T * vp, axis=1)
        Ts = (vp - ell_s[:, None] * T) / ell[:, None]
        xt = np.sum(xpp * T, axis=1)
        cs = vpp - (np.sum(vpp*T,axis=1)+np.sum(xpp*Ts,axis=1))[:,None]*T - xt[:,None]*Ts
        ksvec = cs / ell[:, None]**2 - 2 * (ell_s / ell)[:, None] * (kappa[:, None] * N)
        ks = np.sum(N * ksvec, axis=1)
        Ns = (ksvec - ks[:,None]*N) / kappa[:,None]
        Bs = np.cross(Ts,N)+np.cross(T,Ns)
        acc = self.acceleration(f,ks)
        alphas = -acc/(f['aa']*kappa) - alpha*(f['vv']/f['aa']+ks/kappa)
        betas = -alpha*alphas/beta
        Xss = alphas[:,None]*N + alpha[:,None]*Ns + betas[:,None]*B + beta[:,None]*Bs
        normal = np.cross(xp,V)
        normal /= np.linalg.norm(normal,axis=1)[:,None]
        EE=np.sum(V*V,axis=1);FF=np.sum(V*xp,axis=1);GG=ell**2
        LL=np.sum(normal*Xss,axis=1);MM=np.sum(normal*vp,axis=1);NN=np.sum(normal*xpp,axis=1)
        detI=EE*GG-FF*FF
        trace=(GG*LL-2*FF*MM+EE*NN)/detI
        det=(LL*NN-MM*MM)/detI
        maxk=abs(trace)/2+np.sqrt(np.maximum(trace*trace/4-det,0))
        return dict(s=float(s), radius=f['aa'], radial_speed=f['vv'],
                    minimum_chart=float(f['chart'].min()),
                    metric_angular_error=self.metric_error(s,y),
                    sampled_curvature_max=float(maxk.max()),
                    sampled_support_min=float(np.sum(X*normal,axis=1).min()),
                    maximum_radius=float(np.linalg.norm(X,axis=1).max()),
                    maximum_abs_z=float(abs(X[:,2]).max()),maximum_abs_y=float(abs(X[:,1]).max()),
                    held_witness_min_distance=float(np.linalg.norm(X-np.array([0.,1.4,0.]),axis=1).min()))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--index',type=int,default=0)
    p.add_argument('--nodes',type=int,default=48)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--A',type=float,default=1.4)
    p.add_argument('--B',type=float,default=.45)
    p.add_argument('--a0',type=float,default=.9870588543320401)
    p.add_argument('--max-calls',type=int,default=12000)
    args=p.parse_args()
    data=json.loads(args.candidate.read_text())
    rows=data['rows'] if isinstance(data,dict) else data
    candidate=rows[args.index]
    meridian=Meridian(candidate['segments'],args.a0)
    flow=Flow(meridian,args.nodes,args.A,args.B,args.a0,args.max_calls)
    def chart_event(s,y):return float(flow.frame(s,y)['chart'].min())-1e-5
    def metric_event(s,y):return 2e-5-flow.metric_error(s,y)
    chart_event.terminal=metric_event.terminal=True
    chart_event.direction=metric_event.direction=-1
    report=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                candidate_sha256=hashlib.sha256(args.candidate.read_bytes()).hexdigest(),
                index=args.index,nodes=args.nodes,A=args.A,B=args.B,a0=args.a0,
                complete_prefix=False,closed_surface=False,segments=[])
    y=flow.initial.ravel()
    report['initial']=flow.diagnostics(0.,y)
    try:
        for j,seg in enumerate(meridian.segments):
            times=np.linspace(seg['s0'],seg['s1'],33)
            sol=solve_ivp(flow.rhs,(seg['s0'],seg['s1']),y,method='DOP853',
                          rtol=2e-10,atol=2e-12,max_step=min(.002,seg['L']/16),
                          t_eval=times,events=[chart_event,metric_event])
            records=[flow.diagnostics(s,flat) for s,flat in zip(sol.t,sol.y.T)]
            if sol.status == 1:
                for event_times,event_states in zip(sol.t_events,sol.y_events):
                    if len(event_times):
                        records.append(flow.diagnostics(event_times[-1],event_states[-1]))
            row=dict(index=j,status=sol.status,message=sol.message,
                     chart_events=sol.t_events[0].tolist(),metric_events=sol.t_events[1].tolist(),
                     last=records[-1] if records else None,
                     sampled_extrema={key:(min(r[key] for r in records) if 'min' in key else max(r[key] for r in records))
                      for key in ('minimum_chart','metric_angular_error','sampled_curvature_max',
                                  'sampled_support_min','maximum_radius','maximum_abs_z','maximum_abs_y',
                                  'held_witness_min_distance')})
            report['segments'].append(row)
            args.out.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(row),flush=True)
            if sol.status!=0:break
            y=sol.y[:,-1]
        else:report['complete_prefix']=True
    except Exception as exc:
        report['failure']=str(exc)
    report['rhs_calls']=flow.calls
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='complete',complete_prefix=report['complete_prefix'],
                         rhs_calls=flow.calls,failure=report.get('failure'))))


if __name__=='__main__':main()
