#!/usr/bin/env python3
"""R117: actual worker height jets to the fixed-g Gauss--Codazzi port.

For an exact isometric immersion, Hess_g(z)=N_z II proves these formulas.
For a finite Darboux/DN output the same expressions are formal port values;
the actual Cartesian metric and seam still have to be checked.  The algebraic
JVP below is exact for its jet inputs. An upstream finite-difference DN
Jacobian remains a finite-difference input; it is not made exact by this map.
"""
from __future__ import annotations
import numpy as np

LD = np.longdouble
HEIGHT_KEYS = ('z', 'zr', 'zu', 'zrr', 'zru', 'zuu')


def height_to_gc(height, *, radius, radial_speed, radial_acceleration, normal_z_sign=-1):
    """Use material-u height derivatives and ONE fixed r,a',a'' target jet."""
    r, v, app = LD(radius), LD(radial_speed), LD(radial_acceleration)
    if r <= 0 or normal_z_sign not in (-1, 1):
        raise ValueError('A positive radius and an oriented normal branch are required')
    z = {key:np.asarray(height[key], dtype=LD) for key in HEIGHT_KEYS}
    D = 1-v*v*z['zr']**2-z['zu']**2/(r*r)
    if np.any(~np.isfinite(D)) or np.any(D <= 0):
        raise ArithmeticError('The chosen vertical-normal graph chart failed')
    Nz = normal_z_sign*np.sqrt(D)
    A_l = v*v*z['zrr']+app*z['zr']
    A_m = (v/r)*(z['zru']-z['zu']/r)
    A_n = z['zuu']/(r*r)+(v*v/r)*z['zr']
    l, m, n = A_l/Nz, A_m/Nz, A_n/Nz
    return dict(l=l, m=m, n=n, N_z=Nz, normal_projection_squared=D,
                A_l=A_l, A_m=A_m, A_n=A_n,
                radius=r, radial_speed=v, radial_acceleration=app,
                gauss_defect=l*n-m*m+app/r, height=z)


def height_to_gc_jvp(base, delta_height):
    """Differentiate at fixed target metric; no derivatives of r,v,a'' occur."""
    r, v, app = base['radius'], base['radial_speed'], base['radial_acceleration']
    z, Nz = base['height'], base['N_z']
    dz = {key:np.asarray(delta_height[key], dtype=LD) for key in HEIGHT_KEYS}
    dNz = -(v*v*z['zr']*dz['zr']+z['zu']*dz['zu']/(r*r))/Nz
    dl = (v*v*dz['zrr']+app*dz['zr'])/Nz-base['l']*dNz/Nz
    dm = (v/r)*(dz['zru']-dz['zu']/r)/Nz-base['m']*dNz/Nz
    dn = (dz['zuu']/(r*r)+(v*v/r)*dz['zr'])/Nz-base['n']*dNz/Nz
    return dict(l=dl, m=dm, n=dn, N_z=dNz,
                gauss_defect=dl*base['n']+base['l']*dn-2*base['m']*dm,
                height=dz)


class TailGCJetPort:
    """Consume createCompactTailDN's FULL height jet and its packed tangent.

    height/slope/second multiply cos(spacing*(j+1)*u), with NO sqrt(2).
    meanSlope and meanSecond already include the background.  The upper
    half uses physical z=-worker_height, v=-1/sqrt(E), and N_z<0.
    """
    def __init__(self, jets, *, spacing, height_jacobian=None, height_sign=-1,
                 normal_z_sign=-1, target_jet=None):
        self.jets = dict(jets)
        self.spacing, self.height_sign, self.normal_z_sign = int(spacing), int(height_sign), int(normal_z_sign)
        if self.spacing <= 0 or self.height_sign not in (-1, 1):
            raise ValueError('Positive Fourier spacing and a height reflection sign are required')
        self.h = np.asarray(jets['height'], dtype=LD)
        self.hr = np.asarray(jets['slope'], dtype=LD)
        self.hrr = np.asarray(jets['second'], dtype=LD)
        self.M = self.h.size
        if self.h.ndim != 1 or self.hr.shape != self.h.shape or self.hrr.shape != self.h.shape:
            raise ValueError('Height, slope and second arrays must have the same one-dimensional shape')
        self.frequencies = self.spacing*np.arange(1, self.M+1, dtype=LD)
        self.mean_r = LD(jets['meanSlope'])
        self.mean_rr = LD(jets['meanSecond'])
        r, E, Ep = LD(jets['radius']), LD(jets['E']), LD(jets['Ep'])
        own = (r, -1/np.sqrt(E), -Ep/(2*E*E))
        self.target_jet = own if target_jet is None else tuple(LD(x) for x in target_jet)
        if len(self.target_jet) != 3:
            raise ValueError('target_jet is (r,a_prime,a_second)')
        self.worker_background_jet = own
        self.background_jet_difference = np.asarray(self.target_jet)-np.asarray(own)
        if height_jacobian is None:
            self.height_jacobian = None
        else:
            matrix = np.asarray(height_jacobian, dtype=LD)
            if matrix.size != (3*self.M+2)*self.M:
                raise ValueError('Packed height Jacobian must have (3M+2)*M entries')
            self.height_jacobian = matrix.reshape(3*self.M+2, self.M)

    @classmethod
    def from_worker_record(cls, record, *, spacing=None, **kwargs):
        response = record.get('response', record)
        if spacing is None:
            config = record.get('config', response.get('parameters', {}))
            if 'spacing' not in config:
                raise ValueError('Material Fourier spacing is not recorded; supply it explicitly')
            spacing = config['spacing']
        return cls(response['jets'], spacing=spacing,
                   height_jacobian=response.get('heightJetJacobian'), **kwargs)

    def _series(self, u, height, slope, second, mean_slope, mean_second, mean_height=0):
        u = np.asarray(u, dtype=LD)
        phase = u[..., None]*self.frequencies
        co, si = np.cos(phase), np.sin(phase)
        k = self.frequencies
        sign = self.height_sign
        return dict(z=sign*(LD(mean_height)+co @ height),
                    zr=sign*(LD(mean_slope)+co @ slope),
                    zu=sign*(-si @ (k*height)),
                    zrr=sign*(LD(mean_second)+co @ second),
                    zru=sign*(-si @ (k*slope)),
                    zuu=sign*(-co @ (k*k*height)))

    def height_values(self, material_u, *, mean_height=0):
        return self._series(material_u, self.h, self.hr, self.hrr, self.mean_r, self.mean_rr, mean_height)

    def evaluate(self, material_u, *, mean_height=0):
        r, v, app = self.target_jet
        return height_to_gc(self.height_values(material_u, mean_height=mean_height),
            radius=r, radial_speed=v, radial_acceleration=app, normal_z_sign=self.normal_z_sign)

    def jet_direction_values(self, material_u, direction):
        zero = np.zeros(self.M, dtype=LD)
        h = np.asarray(direction.get('height', zero), dtype=LD)
        hr = np.asarray(direction.get('slope', zero), dtype=LD)
        hrr = np.asarray(direction.get('second', zero), dtype=LD)
        if h.shape != self.h.shape or hr.shape != self.h.shape or hrr.shape != self.h.shape:
            raise ValueError('A jet direction has the wrong Fourier shape')
        # The background is fixed, so these are also the derivatives of the
        # FULL means. Adding the background for a second time would be wrong.
        mr = direction.get('meanSlopeCorrection', direction.get('meanSlope', 0))
        mrr = direction.get('meanSecondCorrection', direction.get('meanSecond', 0))
        return self._series(material_u, h, hr, hrr, mr, mrr, direction.get('meanHeight', 0))

    def jvp_from_jet_direction(self, material_u, direction):
        base = self.evaluate(material_u)
        return height_to_gc_jvp(base, self.jet_direction_values(material_u, direction))

    def unpack_height_jvp(self, physical_cut_height_direction):
        if self.height_jacobian is None:
            raise ValueError('This worker record does not contain a DN height Jacobian')
        v = np.asarray(physical_cut_height_direction, dtype=LD)
        if v.shape != (self.M,):
            raise ValueError('The DN direction must be in the M physical cut-height coefficients')
        out = self.height_jacobian @ v
        M = self.M
        return dict(slope=out[:M], second=out[M:2*M],
                    meanSlopeCorrection=out[2*M], meanSecondCorrection=out[2*M+1],
                    height=out[2*M+2:3*M+2])

    def jvp(self, material_u, physical_cut_height_direction):
        return self.jvp_from_jet_direction(material_u, self.unpack_height_jvp(physical_cut_height_direction))

    def evaluate_in_chart(self, coordinate, material_map):
        """Scalar II components are composed with u(xi), not rescaled by u'."""
        mapped = material_map(coordinate)
        u = mapped['u'] if isinstance(mapped, dict) else mapped
        return self.evaluate(u)

    def jvp_in_chart(self, coordinate, direction, material_map):
        mapped = material_map(coordinate)
        u = mapped['u'] if isinstance(mapped, dict) else mapped
        return self.jvp(u, direction)
