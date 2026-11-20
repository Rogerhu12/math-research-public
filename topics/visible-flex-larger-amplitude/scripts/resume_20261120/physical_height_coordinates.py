#!/usr/bin/env python3
"""Invertible physical-height change of complete free direction coordinates.

A=I+vq e_H^T, with e_H^T vq=0, so A^-1=I-vq e_H^T.
Only the step norm changes. No original field or equation is changed.
"""
import numpy as np


def height_scale(length):
    """b=10u^3-15u^4+6u^5 has integral b_ss^2=120/(7*S^3)."""
    length=float(length)
    if not np.isfinite(length) or length<=0:
        raise ValueError('Need a positive actual radial length')
    return np.sqrt(7*length**3/120)


class PhysicalHeight:
    def __init__(self, coordinates, basis):
        self.coordinates=coordinates
        selector=np.zeros(basis.dimension);selector[-1]=1.
        column=basis.free_direction(selector)
        if column[-1]!=1.:
            raise ValueError('The declared final physical coarse column must change H by one')
        self.compensation=column.copy();self.compensation[-1]=0.
        self.size=coordinates.size

    def forward_free(self, v):
        v=np.asarray(v)
        return v+v[-1]*self.compensation

    def inverse_free(self, v):
        v=np.asarray(v)
        return v-v[-1]*self.compensation

    def transpose_free(self, g):
        result=np.array(g,copy=True)
        result[-1]+=self.compensation@g
        return result

    def lift(self, z):
        return self.forward_free(self.coordinates.lift(z))

    def pullback(self, g):
        return self.coordinates.pullback(self.transpose_free(g))

    def metadata(self):
        S=self.coordinates.problem.S
        return dict(map='A=I+vq e_H^T',inverse='I-vq e_H^T',
            transpose='A^T g=g+e_H(vq^T g)',
            vq_height_slot=float(self.compensation[-1]),
            vq_norm=float(np.linalg.norm(self.compensation)),
            length=S,height_scale=float(self.coordinates.scale[-1]),
            ideal_height_bending_energy=120/(7*S**3),
            ideal_smooth_height='b(s)=10(s/S)^3-15(s/S)^4+6(s/S)^5',
            actual_column='The existing literal nodal B_H=(q_Z=b-chi,H=1), evaluated by the unchanged quintic/lift model',
            complete_free_space_preserved=True,step_norm_changed=True,
            physical_equations_changed=False,
            scope='A positive invertible direction coordinate change; not an isometry, continuous geometry or reach claim')


def new_map_checks(problem,x,lift,transpose,size,point_module,geometry_module,
                   observed_module,witness,seed=2026112003):
    """One complete-map adjoint and one new arbitrary-point complex step."""
    rng=np.random.default_rng(seed)
    z=rng.standard_normal(size);z/=np.linalg.norm(z)
    g=rng.standard_normal(problem.free_size);g/=np.linalg.norm(g)
    dz=lift(z)
    left=float(dz@g);right=float(z@transpose(g))
    adjoint=abs(left-right)/max(1e-30,abs(left),abs(right))
    p=problem.prepare(x)
    cell,u,phi=int(witness['cell']),float(witness['u']),float(witness['phi'])
    fields=point_module.fields_at(problem,p,cell,u,phi,observed_module)
    values=[geometry_module.curvature_cotangent(fields,j)for j in (0,1)]
    branch=int(np.argmax([abs(item[0])for item in values]))
    k,cot,meta=values[branch]
    row=point_module.pullback_at(problem,p,cell,u,phi,cot,observed_module)
    predicted=float(z@transpose(row))
    epsilon=1e-30
    pc=problem.prepare(x+1j*epsilon*dz)
    complex_fields=point_module.fields_at(problem,pc,cell,u,phi,observed_module)
    actual=float(np.imag(geometry_module.analytic_kappa(complex_fields,branch))/epsilon)
    complex_error=abs(predicted-actual)/max(1e-30,abs(predicted),abs(actual))
    if max(adjoint,complex_error)>2e-9:
        raise ValueError('New physical-height/continuous-point map failed its necessary derivative check')
    return dict(seed=seed,adjoint_left=left,adjoint_right=right,adjoint_relative_difference=adjoint,
        complex_step=epsilon,curvature_derivative_predicted=predicted,
        curvature_derivative_complex_step=actual,complex_step_relative_difference=complex_error,
        witness=dict(cell=cell,u=u,phi=phi,branch=branch,current_kappa=k),
        principal_metadata=meta,
        scope='New complete height map plus new arbitrary-point transpose only; no repeated whole-Gram solve or continuous certificate')
