"""Mixed BVP on one actual finite-tail cell with the recorded physical BC.

Scalar height jets below differentiate the nodal L interpolant. They are
reported as an additional audit, not as an automatic C2 Cartesian certificate.
"""
import argparse, gzip, hashlib, json, time
from pathlib import Path
import numpy as np
from mu_free_fields import MuFreeFields
from mixed_bvp import MixedBVP


def height_jets(fields, Y, Lr, r, w, wr, flow):
    d = fields.d
    v = Y[:d]
    L = Y[2*d:]
    vr = -flow[:d]
    P, Pt, Lv = v@fields.dphi, v@fields.ddphi, L@fields.Phi
    K = Lv-Pt
    U = (L[1:]+(fields.freq**2-1)*v)@fields.dphi
    E = 1+w*w
    D = 1-w*w*(2*K+K*K+E*P*P)
    A = 1+K+E*Pt
    h = r*w*(v@fields.phi)
    hr = w*(1+K)
    ht = r*w*P
    hrr = wr*(1+K)+w*(Lr@fields.Phi-vr@fields.ddphi)
    hrt = w*(U+P)
    htt = r*w*Pt
    aa = (hrr-w*wr/E*hr)/(np.sqrt(E*D))
    bb = w*U/(r*np.sqrt(D))
    cc = w*A/(r*np.sqrt(E*D))
    Kg = w*wr/(r*E*E)
    gauss = aa*cc-bb*bb-Kg
    curvature = .5*(abs(aa+cc)+np.hypot(aa-cc, 2*bb))
    return np.stack([h, hr, ht, hrr, hrt, htt], axis=1), dict(
        formal_gauss_defect=float(np.max(abs(gauss))),
        height_darboux_defect=float(np.max(abs(D/E*gauss))),
        formal_curvature=float(np.max(curvature)), target_gauss=Kg)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--max-iterations', type=int, default=20)
    a = p.parse_args()
    data = json.loads(gzip.decompress(a.input.read_bytes()))
    nodes, param = data['nodes'], data['parameters']
    x = np.array([n['x'] for n in nodes])
    r = np.array([n['r'] for n in nodes])
    w = np.array([n['w'] for n in nodes])
    wr = np.array([n['wr'] for n in nodes])
    reference = np.array([n['Y'] for n in nodes])
    f = MuFreeFields(param['M'], param['spacing'], param['N'], False, param['mixedProjectionFloor'])
    def profile(points):
        if not np.array_equal(points, x):
            raise ValueError('Use only the exact physical-factory profile nodes')
        return dict(r=r, w=w, rx=-1., ell=-wr/w)
    bvp = MixedBVP(f, x, profile, reference[0,:f.d], reference[-1,f.d:2*f.d])
    started = time.monotonic()
    result = bvp.solve(reference, max_iterations=a.max_iterations,
                       callback=lambda row:print(json.dumps(dict(event='mixed_iteration', **row)), flush=True))
    Y, final = result['Y'], result['final']
    a.out.parent.mkdir(parents=True, exist_ok=True)
    checkpoint = a.out.with_suffix('.npz')
    np.savez_compressed(checkpoint, x=x, Y=Y, reference=reference)
    fY = final['fields']['flow']
    intervals = []
    previous_right_Lr = None
    for j in range(bvp.k):
        ids = [2*j, 2*j+1, 2*j+2]
        l,m,rr = ids
        h = x[rr]-x[l]
        L = Y[ids, 2*f.d:]
        Lx = np.stack([-3*L[0]+4*L[1]-L[2], L[2]-L[0], L[0]-4*L[1]+3*L[2]])/h
        item = dict(interval=j, stage=int(nodes[m]['stage']), raw_segment=int(nodes[m]['raw_segment']),
                    x_left=float(x[l]), x_right=float(x[rr]),
                    Lr_jump_left=0. if previous_right_Lr is None else float(np.max(abs(-Lx[0]-previous_right_Lr))),
                    height_jet_reference_errors=[0.]*6, Lr_reference_error=0.,
                    formal_gauss_defect=0., height_darboux_defect=0., formal_curvature=0.,
                    reference_formal_gauss_defect=0.)
        for k,n in enumerate(ids):
            hj, audit = height_jets(f, Y[n], -Lx[k], r[n], w[n], wr[n], fY[n])
            original_jets = np.asarray(nodes[n]['height_jets'])
            errors = np.max(abs(hj-original_jets), axis=0)
            item['height_jet_reference_errors'] = np.maximum(item['height_jet_reference_errors'], errors).tolist()
            item['Lr_reference_error'] = max(item['Lr_reference_error'], float(np.max(abs(-Lx[k]-nodes[n]['Lr']))))
            for name in ('formal_gauss_defect', 'height_darboux_defect', 'formal_curvature'):
                item[name] = max(item[name], audit[name])
            ref_flow = f.evaluate(reference[n], r[n], w[n], -1., -wr[n]/w[n])['flow'][0]
            _, ref_audit = height_jets(f, reference[n], np.asarray(nodes[n]['Lr']), r[n], w[n], wr[n], ref_flow)
            item['reference_formal_gauss_defect'] = max(item['reference_formal_gauss_defect'], ref_audit['formal_gauss_defect'])
        previous_right_Lr = -Lx[2]
        intervals.append(item)
    eig = np.linalg.eigvalsh(final['fields']['gram'])
    report = dict(scope=__doc__, input=dict(path=str(a.input), sha256=hashlib.sha256(a.input.read_bytes()).hexdigest()),
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
            [Path(__file__),Path(__file__).with_name('mixed_bvp.py'),Path(__file__).with_name('mu_free_fields.py')]},
        parameters=param, success=result['success'], stop_reason=result['stop_reason'],
        root_relative=final['root_relative'], ode_residual=final['ode_residual'], boundary_residual=final['boundary_residual'],
        minD=final['fields']['minD'], minS=final['fields']['minS'], minA=final['fields']['minA'],
        minimum_abs_gram_eigenvalue=float(np.min(abs(eig))), minimum_gram_eigenvalue=float(np.min(eig)),
        reference_state_error=float(np.max(abs(Y-reference))), history=result['history'],
        maximum_height_jet_reference_errors=np.max([v['height_jet_reference_errors'] for v in intervals],axis=0).tolist(),
        maximum_Lr_join_jump=max(v['Lr_jump_left']for v in intervals),
        maximum_formal_gauss_defect=max(v['formal_gauss_defect']for v in intervals),
        maximum_height_darboux_defect=max(v['height_darboux_defect']for v in intervals),
        maximum_reference_gauss_defect=max(v['reference_formal_gauss_defect']for v in intervals),
        maximum_formal_curvature=max(v['formal_curvature']for v in intervals), intervals=intervals,
        checkpoint=dict(path=str(checkpoint),sha256=hashlib.sha256(checkpoint.read_bytes()).hexdigest()),
        elapsed_seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ('intervals','history')}),flush=True)


if __name__ == '__main__':
    main()
