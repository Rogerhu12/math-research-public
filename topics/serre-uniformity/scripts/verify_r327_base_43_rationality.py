#!/usr/bin/env python3
"""Exact local-unit certificate for R327; Python standard library only.

All computations take place either in the two given degree-44 rational fields,
in the fixed q residue field, or in F_43[X]/(X^43).  No class-number software,
floating-point logarithm, infinite p-adic tail, or uncomputed upper Norm is used.
"""
import argparse
import hashlib
import importlib.util
import json
import sys
from math import lcm
from pathlib import Path

sys.dont_write_bytecode = True
P = 43
MINOR_ROWS = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,31]
INPUTS = ['r171_principal_norm_selflocal_certificate.json',
          'r185_p_local_kummer_certificate.json',
          'small_robert_norm_target_certificate.json',
          'r243_h_unit_norm_kernel_certificate.json']


def load_module(path):
    spec = importlib.util.spec_from_file_location('r327_exact_field', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Truncated:
    """F_43[X]/X^43; all polynomial vectors have exactly 43 entries."""
    def __init__(self):
        self.zero = [0] * P
        self.one = [1] + [0] * (P-1)

    def add(self, a, b):
        return [(x+y) % P for x,y in zip(a,b)]

    def sub(self, a, b):
        return [(x-y) % P for x,y in zip(a,b)]

    def scale(self, a, c):
        return [x*c % P for x in a]

    def mul(self, a, b):
        c = [0] * P
        for i,x in enumerate(a):
            if not x:
                continue
            for j in range(P-i):
                c[i+j] += x*b[j]
        return [x % P for x in c]

    def shift(self, a, n):
        return [0]*n + a[:P-n]

    def inv(self, a):
        c = [0] * P
        c[0] = pow(a[0], -1, P)
        for n in range(1, P):
            c[n] = -c[0]*sum(a[j]*c[n-j] for j in range(1,n+1)) % P
        assert self.mul(a,c) == self.one
        return c

    def evaluate(self, coeffs, x):
        a = self.zero[:]
        for c in reversed(coeffs):
            a = self.mul(a,x)
            a[0] = (a[0]+c) % P
        return a

    def log(self, a):
        b = self.sub(self.scale(a,pow(a[0],-1,P)),self.one)
        assert b[0] == 0
        out, power = self.zero[:], self.one[:]
        for n in range(1,P):
            power = self.mul(power,b)
            out = self.add(out,self.scale(power,(-1 if n%2==0 else 1)*pow(n,-1,P)))
        # A second computation, by g'/g, checks all 42 coefficients independently.
        derivative = [(j*a[j]) % P for j in range(1,P)] + [0]
        quotient = self.mul(derivative,self.inv(a))
        assert all(out[j] == quotient[j-1]*pow(j,-1,P) % P for j in range(1,P))
        return out


def determinant(a):
    a = [[x % P for x in row] for row in a]
    d = 1
    for c in range(len(a)):
        k = next((j for j in range(c,len(a)) if a[j][c]),None)
        if k is None:
            return 0
        if k != c:
            a[c],a[k] = a[k],a[c]
            d = -d
        d = d*a[c][c] % P
        inverse = pow(a[c][c],-1,P)
        for j in range(c+1,len(a)):
            s = a[j][c]*inverse % P
            a[j] = [(x-s*y) % P for x,y in zip(a[j],a[c])]
    return d % P


def canonical_y(ring, original):
    poly = list(reversed(original['P']))
    assert len(poly)==45 and poly[-1]==1
    assert all(x % P==0 for x in poly[:-1]) and poly[0] % (P*P)
    C = -poly[0]//P
    coeffs = [(poly[j]//P)*pow(C,-1,P) % P for j in range(44)]
    def equation(u):
        powers = [ring.one]
        for _ in range(44):
            powers.append(ring.mul(powers[-1],u))
        f = ring.sub(powers[44],ring.one)
        d = ring.scale(powers[43],44)
        for j in range(1,P):
            if coeffs[j]:
                f = ring.add(f,ring.scale(ring.shift(powers[j],j),coeffs[j]))
                d = ring.add(d,ring.scale(ring.shift(powers[j-1],j),j*coeffs[j]))
        return f,d
    u = ring.one[:]
    for _ in range(6):
        f,d = equation(u)
        u = ring.sub(u,ring.mul(f,ring.inv(d)))
    assert equation(u)[0] == ring.zero
    assert u[0] == 1
    return C,ring.shift(u,1)


def run(notes, progress=False):
    raw = {name:(notes/name).read_bytes() for name in INPUTS}
    original,extra,small,units = [json.loads(raw[name]) for name in INPUTS]
    exact = load_module(notes.parent/'scripts/verify_o6_single_real_norm_target.py')
    fz = [int(x) for x in small['factors'][0]['coefficients']]
    h = extra['h_coefficients_ascending']
    assert len(h)==44 and all(int(d)%P for _,d in h)
    # Exact global map, distinct from the original Eisenstein generator y.
    field_y = exact.Field44(list(reversed(original['P'])))
    D = lcm(*(2*int(d) for _,d in h))
    z_in_y = field_y.normalize([(int(a)*(D//(2*int(d))),0) for a,d in h],D)
    assert field_y.evaluate(fz,z_in_y) == field_y.zero
    if progress:
        print('PASS exact f_z(h(y)/2)=0',flush=True)
    # Same q, same marked four-torsion, same original real 43-torsion.
    q = int(small['q'])
    assert q == int(original['q'])
    finite = exact.Fp2(q)
    curve = exact.EC(finite,(q-1,0),finite.zero)
    Pq = tuple(tuple(map(int,a)) for a in small['P'])
    P4 = (finite.i,(1,q-1))
    assert curve.on(Pq) and curve.mult(Pq,P) is None
    _,phi = curve.velu43(Pq)
    e0 = phi((finite.zero,finite.zero))[0]
    f = finite.sub(phi(((q-1,0),finite.zero))[0],e0)
    r = finite.sub(phi(P4)[0],e0)
    zq = finite.div(finite.mul((0,q-1),r),f)
    yq = -pow(int(original['b']),-1,q) % q
    hq = 0
    for a,d in reversed(h):
        hq = (hq*yq+int(a)*pow(int(d),-1,q)) % q
    assert zq == (hq*pow(2,-1,q) % q,0)
    # Ordinary unit status is checked again by all 22 exact integer identities.
    field_z = exact.Field44(fz)
    rows = units['ordinary_units']
    assert [row['index'] for row in rows] == list(range(22))
    for row in rows:
        element = row['element']
        denominator = int(element['common_denominator'])
        assert denominator % P
        unit = field_z.normalize([(int(x),0) for x in element['numerators_ascending']],denominator)
        ann = list(map(int,row['integral_annihilator_ascending']))
        assert ann[-1]==1 and abs(ann[0])==1
        assert field_z.evaluate(ann,unit)==field_z.zero
    if progress:
        print('PASS all 22 monic integer unit identities and fixed q label',flush=True)
    ring = Truncated()
    C,y = canonical_y(ring,original)
    z = ring.evaluate([int(a)*pow(2*int(d),-1,P) % P for a,d in h],y)
    assert z[0] == 1
    records = []
    for row in rows:
        element = row['element']
        denominator = int(element['common_denominator'])
        g = ring.evaluate([int(x)*pow(denominator,-1,P) % P for x in element['numerators_ascending']],z)
        assert g[0]
        log = ring.log(g)
        records.append({'unit_index':row['index'],'residue':g[0],
                        'normalized_unit_coefficients':[x*pow(g[0],-1,P) % P for x in g],
                        'truncated_log_coefficients_degrees_1_to_42':log[1:]})
    matrix = [[row['truncated_log_coefficients_degrees_1_to_42'][j] for row in records] for j in range(42)]
    minor = [matrix[j-1] for j in MINOR_ROWS]
    det = determinant(minor)
    assert det == 10
    # In the same positive Artin normalization sigma(pi)=omega^(-1)*pi.
    def multiply_gaussian(a,b):
        return ((a[0]*b[0]-a[1]*b[1]) % P,(a[0]*b[1]+a[1]*b[0]) % P)
    omega = (8,25)
    omega_powers = [(1,0)]
    for _ in range(44):
        omega_powers.append(multiply_gaussian(omega_powers[-1],omega))
    assert omega_powers[44]==(1,0) and omega_powers[22]==(P-1,0)
    assert len(set(omega_powers[:44]))==44
    sigma_columns = [j for j in range(22) if j!=8]
    F_minor = []
    F_rows = []
    for j in MINOR_ROWS:
        re,im = omega_powers[(-j)%44]
        F_minor.append(matrix[j-1]+[matrix[j-1][k]*re % P for k in sigma_columns])
        F_rows.append([j,'real'])
    for j in MINOR_ROWS:
        if j==22:
            continue
        re,im = omega_powers[(-j)%44]
        F_minor.append([0]*22+[matrix[j-1][k]*im % P for k in sigma_columns])
        F_rows.append([j,'imaginary'])
    F_det = determinant(F_minor)
    assert F_det==30
    if progress:
        print('PASS H rank22/minor det10; F rank43/minor det30 modulo43',flush=True)
    return {'schema':'R327-base-43-rationality-v1','p':P,
            'input_sha256':{name:hashlib.sha256(raw[name]).hexdigest() for name in INPUTS},
            'same_global_map_z_equals_h_over_2':True,'same_marked_q_embedding':True,
            'ordinary_unit_integer_identities_checked':22,
            'local_parameter_relation':'pi^44=C*43; original y=pi*u(pi); u(0)=1',
            'C':C,'y_coefficients_mod43_through_degree42':y,
            'z_coefficients_mod43_through_degree42':z,
            'units':records,'truncated_log_matrix_42_by_22':matrix,
            'minor_row_degrees':MINOR_ROWS,'minor_determinant_mod43':det,
            'rank':22,
            'F_unit_columns':[['identity',j] for j in range(22)]+[['sigma',j] for j in sigma_columns],
            'F_minor_row_labels':F_rows,'F_minor_matrix_43_by_43':F_minor,
            'F_minor_determinant_mod43':F_det,'F_local_unit_rank':43,
            'H_signature':[2,21],'F_signature':[0,44],
            'H_maximal_43_ramified_pro43_group_free_rank':22,
            'F_maximal_43_ramified_pro43_group_free_rank':45,
            'class_group_input':'R264 full Cl_F[43]=0; norm gives Cl_H[43]=0',
            'used_GRH':False,'actual_norm_preimage_computed':False,'actual_L_computed':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('notes_dir',type=Path)
    parser.add_argument('--certificate',type=Path,required=True)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--progress',action='store_true')
    args = parser.parse_args()
    data = run(args.notes_dir,args.progress)
    if args.write:
        args.certificate.write_text(json.dumps(data,indent=2)+'\n')
    else:
        assert data == json.loads(args.certificate.read_text())
    print('PASS R327: exact marked field map; 22 ordinary units; H/F local minors det10/30; no upper Norm/L value.',flush=True)


if __name__ == '__main__':
    main()
