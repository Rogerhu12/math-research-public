"""Finite raw/full residual locations, kept separate from a posterior bound."""
import numpy as np


def residual_locations(problem, vector, data, complement=None, curvature_cap=7.2):
    theta = np.asarray(problem.chart.theta, float)
    cod = data['codazzi_cells']
    out = dict(continuous_certificate=False)
    for label, block, frequencies in (
        ('raw_codazzi_n', cod[:, :problem.e], 2*np.arange(problem.e)),
        ('raw_codazzi_m', cod[:, problem.e:], 2*np.arange(1, problem.K+1))):
        j, k = np.unravel_index(np.argmax(abs(block)), block.shape)
        out[label] = dict(maximum=float(abs(block[j, k])), signed_value=float(block[j, k]),
            cell=int(j), mode=int(frequencies[k]), coefficient=int(k),
            endpoints=problem.x[j:j+2].tolist(), cell_length=float(problem.h[j]))
    def angular_peak(values):
        i, j = np.unravel_index(np.argmax(abs(values)), values.shape)
        return dict(maximum=float(abs(values[i, j])), signed_value=float(values[i, j]),
            angular_index=int(i), node=int(j), s=float(problem.x[j]), xi=float(theta[i]),
            material_u=float(problem.coords['u'][i, j]),
            n_m_l=data['fields'][i, j].tolist(), target_K=float(data['profile_jet']['K'][j]))
    out['full_gauss'] = angular_peak(data['full_gauss'])
    n, m, l = (data['fields'][:, :, k] for k in range(3))
    disc = np.hypot(l-n, 2*m)
    curvature = .5*np.maximum(abs(l+n+disc), abs(l+n-disc))
    out['formal_curvature'] = angular_peak(curvature)
    active = curvature > curvature_cap
    out['formal_curvature'].update(cap=float(curvature_cap), active_points=int(active.sum()))
    if np.any(active):
        jj = np.nonzero(active)[1]
        out['formal_curvature']['active_s_range'] = [float(problem.x[jj.min()]), float(problem.x[jj.max()])]
    if complement is not None:
        low = np.stack((problem.E@cod[:, :problem.e].T,
                        problem.O@cod[:, problem.e:].T), axis=-1)
        omitted = complement['omitted_codazzi_cells']
        for label, array in (('full_angular_codazzi', low+omitted), ('omitted_angular_codazzi', omitted)):
            out[label] = {}
            for k, name in enumerate(('n', 'm')):
                v = array[:, :, k]
                i, j = np.unravel_index(np.argmax(abs(v)), v.shape)
                out[label][name] = dict(maximum=float(abs(v[i, j])), signed_value=float(v[i, j]),
                    angular_index=int(i), xi=float(theta[i]), cell=int(j),
                    endpoints=problem.x[j:j+2].tolist(), cell_length=float(problem.h[j]),
                    material_u_endpoints=problem.coords['u'][i, j:j+2].tolist())
    return out
