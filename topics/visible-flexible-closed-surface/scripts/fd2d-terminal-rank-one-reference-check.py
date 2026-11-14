#!/usr/bin/env python3
"""R157 exact rational budget and small reference-jet check; no BVP."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_terminal_rank_one_reference import terminal_rank_one_reference, terminal_rank_one_interior_jet


def identity(p):
    p = Path(p)
    return dict(path=str(p), sha256=hashlib.sha256(p.read_bytes()).hexdigest(), bytes=p.stat().st_size)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise RuntimeError('Use a new output path')
    started = time.time()
    config = json.loads(a.candidate.read_text())
    piece = config['segments'][-1]
    pd = F.from_float(-float(piece['p0']))
    length = F.from_float(float(piece['L']))
    assert piece['kind'] == 'phase_bridge'
    assert piece['ps0'] == piece['ps1'] == 0
    assert piece['exact_endpoint_phase'] == '-pi/2'
    assert pd > F(14499, 10000) and pd < F(3, 2)
    assert length > F(1, 40)
    D_upper = F(11, 7)-F(14499,10000)
    assert D_upper < F(1, 8)
    K_upper = F(3,2)*F(1,8)**2/(F(1,40)*F(4,5))
    kappa_upper = F(6,5)*F(315,128)/F(23,50)
    cap = F(33,5)
    permitted_K = cap*(cap-kappa_upper)
    strict_margin = permitted_K-K_upper
    assert K_upper == F(75,64) and kappa_upper == F(4725,736)
    assert permitted_K == F(21879,18400) and strict_margin > 0

    # A true scalar metric, independently differentiated position fields.
    s = np.linspace(.1,.8,17)[:,None]
    u = np.linspace(0.,2*np.pi,33,endpoint=False)[None,:]
    radius = 1-.1*s*s
    ap = -.2*s
    K = .2/radius
    Ks = .04*s/(radius*radius)
    k = .3+.2*np.cos(2*u)
    ku = -.4*np.sin(2*u)
    ref = terminal_rank_one_interior_jet(radius,ap,K,Ks,k,u,kappa_u=ku)
    eps = 2e-6
    def values(ss, uu):
        return terminal_rank_one_reference(.2/(1-.1*ss*ss),.3+.2*np.cos(2*uu),uu)['values']
    radial_fd = (values(s+eps,u)-values(s-eps,u))/(2*eps)
    angular_fd = (values(s,u+eps)-values(s,u-eps))/(2*eps)
    err_s = float(np.max(np.abs(ref['radial']-radial_fd)))
    err_u = float(np.max(np.abs(ref['angular']-angular_fd)))
    n,m,l = (ref['values'][...,j] for j in range(3))
    ns,ms = radial_fd[...,0],radial_fd[...,1]
    mu,lu = angular_fd[...,1],angular_fd[...,2]
    raw_cod = np.stack((ns-mu/radius-(ap/radius)*(l-n),ms-lu/radius+2*(ap/radius)*m),axis=-1)
    cod_error = float(np.max(np.abs(raw_cod-ref['codazzi'])))
    gauss_error = float(np.max(np.abs(n*l-m*m-K)))
    zero = terminal_rank_one_reference(0.,[0.,1.,0.],[0.,np.pi/2,1.],kappa_u=[0.,.2,0.])
    zero_cut = bool(np.all(zero['b'] == 0) and np.all(zero['b_u'] == 0))
    passed = max(err_s,err_u,cod_error)<1e-7 and gauss_error<1e-12 and zero_cut
    report = dict(schema='fd2d-terminal-rank-one-reference-check-v1',passed=passed,
        scope='Exact rational uniform curvature budget plus finite independent derivative/Codazzi checks; no actual14 replay, BVP or geometry-completion claim',
        source=identity(__file__),helper=identity(Path(__file__).with_name('fd2d_gc_terminal_rank_one_reference.py')),
        candidate=identity(a.candidate),
        exact_rational=dict(input_pd=str(pd),input_L=str(length),pi_upper='22/7',D_upper=str(D_upper),
            K_strict_upper=str(K_upper),kappa_upper=str(kappa_upper),curvature_strict_cap=str(cap),
            cap_allowed_K=str(permitted_K),strict_positive_margin=str(strict_margin)),
        derivative_check_points=int(n.size),difference_step=eps,
        radial_jet_max_error=err_s,angular_jet_max_error=err_u,
        codazzi_formula_max_error=cod_error,gauss_formula_max_error=gauss_error,
        exact_zero_tail_values_preserved=zero_cut,wall_seconds=time.time()-started)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
    if not passed:
        raise SystemExit(1)


if __name__=='__main__':
    main()
