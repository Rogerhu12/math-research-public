#!/usr/bin/env python3
"""R375: actual q Frobenius classes by finite local-ring arithmetic.

Standard library only.  The ring is O_{F_43}/(pi^46), pi^44=C*43.
The complete local unit Kummer quotient is evaluated by elementary units,
without logarithmic tails or conditional class-group computations.
"""
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
sys.dont_write_bytecode = True
P = 43
MOD = P*P
LABELS = list(range(1,43))+[44,45]
INPUTS = ['r171_principal_norm_selflocal_certificate.json',
          'r185_p_local_kummer_certificate.json',
          'r243_h_unit_norm_kernel_certificate.json']


class Ring:
    """Canonical degree<44 pairs; coefficients0,1 mod p^2, others mod p."""
    def __init__(self,C):
        self.C = C
        self.cp = C*P % MOD
        self.zero = [(0,0)]*44
        self.one = [(1,0)]+[(0,0)]*43
        self.x = [(0,0),(1,0)]+[(0,0)]*42
        self.omega = self.power(self.scalar((8,25)),P*P)[0]
        self.wp = [(1,0)]
        for _ in range(44):
            self.wp.append(self.mul(self.scalar(self.wp[-1]),self.scalar(self.omega))[0])
        assert self.wp[44]==(1,0) and self.wp[22]==(MOD-1,0)
        assert len(set(self.wp[:44]))==44

    def normalize(self,a):
        return [(x%(MOD if j<2 else P),y%(MOD if j<2 else P)) for j,(x,y) in enumerate(a)]

    def add(self,a,b):
        return self.normalize([(x+z,y+w) for (x,y),(z,w) in zip(a,b)])

    def sub(self,a,b):
        return self.normalize([(x-z,y-w) for (x,y),(z,w) in zip(a,b)])

    def scale(self,a,c):
        if isinstance(c,int):
            c = (c,0)
        u,v = c
        return self.normalize([(x*u-y*v,x*v+y*u) for x,y in a])

    def mul(self,a,b):
        c = [[0,0] for _ in range(46)]
        ia = [(i,x,y) for i,(x,y) in enumerate(a) if x or y]
        ib = [(i,x,y) for i,(x,y) in enumerate(b) if x or y]
        for i,x,y in ia:
            for j,u,v in ib:
                if i+j>=46:
                    break
                c[i+j][0] += x*u-y*v
                c[i+j][1] += x*v+y*u
        for k in (0,1):
            c[k][0] += self.cp*c[k+44][0]
            c[k][1] += self.cp*c[k+44][1]
        return self.normalize(c[:44])

    def power(self,a,k):
        assert k>=0
        v = self.one
        while k:
            if k&1:
                v = self.mul(v,a)
            k//=2
            if k:
                a = self.mul(a,a)
        return v

    def scalar(self,c):
        if isinstance(c,int):
            c = (c,0)
        return self.normalize([c]+self.zero[1:])

    def gaussian_inverse(self,c):
        x,y = c
        v = pow(x*x+y*y,-1,MOD)
        return (x*v % MOD,-y*v % MOD)

    def inv(self,a):
        c = self.gaussian_inverse(a[0])
        v = self.sub(self.one,self.scale(a,c))
        assert v[0]==(0,0)
        power,result = self.one,self.one
        for _ in range(1,46):
            power = self.mul(power,v)
            result = self.add(result,power)
        result = self.scale(result,c)
        assert self.mul(a,result)==self.one
        return result

    def evaluate(self,coeff,x):
        r = self.zero
        for c in reversed(coeff):
            r = self.add(self.mul(r,x),self.scalar(c))
        return r

    def pi_power(self,k,c=1):
        if k>=46:
            return self.zero
        if isinstance(c,int):
            c = (c,0)
        a = self.zero[:]
        if k>=44:
            a[k-44] = (self.cp*c[0],self.cp*c[1])
        else:
            a[k] = c
        return self.normalize(a)

    def sigma(self,a,k):
        r = []
        for j,(x,y) in enumerate(a):
            u,v = self.wp[(-j*k)%44]
            r.append((x*u-y*v,x*v+y*u))
        return self.normalize(r)

    def canonical_y(self,original):
        f = list(reversed(original['P']))
        assert len(f)==45 and f[-1]==1
        assert all(v%P==0 for v in f[:-1]) and f[0]%(P*P)
        assert -f[0]//P==self.C
        coefficients = [(f[j]//P)*pow(self.C,-1,MOD) % MOD for j in range(44)]
        def equation(u):
            powers = [self.one]
            for _ in range(44):
                powers.append(self.mul(powers[-1],u))
            F = self.sub(powers[44],self.one)
            D = self.scale(powers[43],44)
            for j in range(1,44):
                if coefficients[j]:
                    F = self.add(F,self.scale(self.mul(self.pi_power(j),powers[j]),coefficients[j]))
                    D = self.add(D,self.scale(self.mul(self.pi_power(j),powers[j-1]),j*coefficients[j]))
            return F,D
        u = self.one
        for _ in range(6):
            f,d = equation(u)
            u = self.sub(u,self.mul(f,self.inv(d)))
        assert equation(u)[0]==self.zero
        assert tuple(v%P for v in u[0])==(1,0)
        y = self.mul(self.x,u)
        assert self.evaluate(list(reversed(original['P'])),y)==self.zero
        return u,y


class Kummer:
    def __init__(self,ring):
        self.R = R = ring
        self.minus = {}
        for r in LABELS:
            for c in (0,1):
                cc = (1,0) if c==0 else (0,1)
                for a in range(P):
                    z = R.one
                    if a:
                        cpower = (1,0)
                        for k in range(1,45//r+1):
                            cpower = R.mul(R.scalar(cpower),R.scalar(cc))[0]
                            v = (-1 if k%2 else 1)*math.comb(a+k-1,k)
                            z = R.add(z,R.pi_power(r*k,(v*cpower[0],v*cpower[1])))
                    self.minus[(r,c,a)] = z
        self.Greal = R.power(R.add(R.one,R.x),P)
        self.Gimag = R.power(R.add(R.one,R.scale(R.x,(0,1))),P)
        assert self.Greal==R.add(R.add(R.one,R.pi_power(43)),R.scale(R.x,P))
        assert self.Gimag==R.add(R.add(R.one,R.pi_power(43,(0,-1))),R.scale(R.x,(0,P)))

    def coordinates(self,g):
        R = self.R
        c = (g[0][0]%P,g[0][1]%P)
        teich = R.power(R.scalar(c),P*P)[0]
        g = R.scale(g,R.gaussian_inverse(teich))
        assert tuple(v%P for v in g[0])==(1,0)
        answer = []
        for r in range(1,43):
            a,b = (v%P for v in g[r])
            answer.append((a,b))
            if a:
                g = R.mul(g,self.minus[(r,0,a)])
            if b:
                g = R.mul(g,self.minus[(r,1,b)])
            assert all(v%P==0 for v in g[r])
        a,b = g[43]
        g = R.mul(g,R.sub(R.one,R.scale(R.sub(self.Greal,R.one),a)))
        g = R.mul(g,R.add(R.one,R.scale(R.sub(self.Gimag,R.one),b)))
        assert g[43]==(0,0)
        a = (g[0][0]-1)//P*pow(R.C,-1,P) % P
        b = g[0][1]//P*pow(R.C,-1,P) % P
        answer.append((a,b))
        for c,v in enumerate((a,b)):
            if v:
                g = R.mul(g,self.minus[(44,c,v)])
        assert g[0]==(1,0)
        a = g[1][0]//P*pow(R.C,-1,P) % P
        b = g[1][1]//P*pow(R.C,-1,P) % P
        answer.append((a,b))
        for c,v in enumerate((a,b)):
            if v:
                g = R.mul(g,self.minus[(45,c,v)])
        assert g==R.one
        return [list(v) for v in answer]


def matrix(cols):
    return [[col[j][c] for col in cols] for j in range(44) for c in (0,1)]


def rref(A):
    a = [[v%P for v in row] for row in A]
    r,pcs,prs = 0,[],[]
    labs = list(range(len(A)))
    for c in range(len(a[0])):
        k = next((j for j in range(r,len(a)) if a[j][c]),None)
        if k is None:
            continue
        a[r],a[k] = a[k],a[r]
        labs[r],labs[k] = labs[k],labs[r]
        iv = pow(a[r][c],-1,P)
        a[r] = [v*iv%P for v in a[r]]
        for j in range(len(a)):
            if j!=r:
                z = a[j][c]
                a[j] = [(x-z*y)%P for x,y in zip(a[j],a[r])]
        pcs.append(c)
        prs.append(labs[r])
        r+=1
        if r==len(a):
            break
    return a,pcs,prs


def determinant(A):
    a = [[x%P for x in row] for row in A]
    d = 1
    for c in range(len(a)):
        k = next((j for j in range(c,len(a)) if a[j][c]),None)
        if k is None:
            return 0
        if c!=k:
            a[c],a[k] = a[k],a[c]
            d = -d
        d = d*a[c][c] % P
        iv = pow(a[c][c],-1,P)
        for j in range(c+1,len(a)):
            s = a[j][c]*iv%P
            a[j] = [(x-s*y)%P for x,y in zip(a[j],a[c])]
    return d%P


def kernel(A):
    a,pcs,_ = rref(A)
    result = []
    for free in range(len(A[0])):
        if free in pcs:
            continue
        v = [0]*len(A[0])
        v[free] = 1
        for j,c in enumerate(pcs):
            v[c] = -a[j][free]%P
        result.append(v)
    return result


def run(notes,progress=False):
    raw = {name:(notes/name).read_bytes() for name in INPUTS}
    original,extra,units = [json.loads(raw[name]) for name in INPUTS]
    C = -original['P'][-1]//P
    R = Ring(C)
    u,Y = R.canonical_y(original)
    h = extra['h_coefficients_ascending']
    assert all(int(d)%P for _,d in h)
    Z = R.evaluate([int(a)*pow(2*int(d),-1,MOD)%MOD for a,d in h],Y)
    alpha = R.add(R.one,R.scale(Y,int(original['b'])))
    G = []
    for row in units['ordinary_units']:
        e = row['element']
        den = int(e['common_denominator'])
        assert den%P
        G.append(R.evaluate([int(a)*pow(den,-1,MOD)%MOD for a in e['numerators_ascending']],Z))
    assert len(G)==22
    K = Kummer(R)
    # Direct normalization of every elementary basis vector and the shallow p powers.
    for r in LABELS:
        for c in (0,1):
            a = K.coordinates(R.add(R.one,R.pi_power(r,(1,0) if c==0 else (0,1))))
            want = [[0,0] for _ in LABELS]
            want[LABELS.index(r)] = [1,0] if c==0 else [0,1]
            assert a==want
    assert K.coordinates(K.Greal)==[[0,0] for _ in LABELS]
    assert K.coordinates(K.Gimag)==[[0,0] for _ in LABELS]
    sigma_indices = [j for j in range(22) if j!=8]
    E = G+[R.sigma(G[j],1) for j in sigma_indices]
    E_labels = [['identity',j] for j in range(22)]+[['sigma',j] for j in sigma_indices]
    E_coords = [K.coordinates(g) for g in E]
    alpha_conjugates = [R.sigma(alpha,j) for j in range(44)]
    alpha_coords = [K.coordinates(g) for g in alpha_conjugates]
    # Positive arithmetic Frobenius is minus the local principal generator.
    Frob_coords = [[[(-a)%P,(-b)%P] for a,b in col] for col in alpha_coords]
    U = matrix(E_coords)
    A = matrix(E_coords+Frob_coords)
    _,pu,_ = rref(U)
    rr,pa,pr = rref(A)
    assert len(pu)==43 and len(pa)==84
    minor = [[A[r][c] for c in pa] for r in pr]
    minor_det = determinant(minor)
    assert minor_det==5
    # Three complete q relations, with explicit corrections in the fixed43 unit basis.
    omega = [(a%P,b%P) for a,b in R.wp[:44]]
    weight_vectors = [
        ('real_16',[omega[(16*j)%44][0] for j in range(44)]),
        ('imaginary_16',[omega[(16*j)%44][1] for j in range(44)]),
        ('quadratic_22',[1 if j%2==0 else P-1 for j in range(44)])]
    relations = []
    for name,weights in weight_vectors:
        target = [sum(weights[j]*alpha_coords[j][k][c] for j in range(44))%P
                  for k in range(44) for c in (0,1)]
        aug = [row+[t] for row,t in zip(U,target)]
        a,pcs,_ = rref(aug)
        assert pcs==list(range(43))
        correction = [a[j][-1] for j in range(43)]
        assert all(sum(row[j]*correction[j] for j in range(43))%P==t for row,t in zip(U,target))
        # Check the actual finite local product, not just the stored linear relation.
        lhs,rhs = R.one,R.one
        for g,v in zip(alpha_conjugates,weights):
            lhs = R.mul(lhs,R.power(g,v))
        for g,v in zip(E,correction):
            rhs = R.mul(rhs,R.power(g,v))
        ratio = R.mul(lhs,R.inv(rhs))
        assert K.coordinates(ratio)==[[0,0] for _ in LABELS]
        relations.append({'name':name,'alpha_weights':weights,
                          'ordinary_unit_correction_exponents':correction,
                          'local_ratio_mod_pi46':ratio,'local_43_power_verified':True})
    _,rp,_ = rref([v for _,v in weight_vectors])
    assert len(rp)==3
    annihilator = kernel([list(row) for row in zip(*A)])
    assert len(annihilator)==4
    for v in annihilator:
        assert all(sum(v[j]*A[j][c] for j in range(88))%P==0 for c in range(87))
    # Class field theory is equivariant: test sigma^22 directly on every
    # elementary local unit, after passing to the actual four-dimensional quotient.
    central_checks = []
    for depth in LABELS:
        for c in (0,1):
            basis = R.add(R.one,R.pi_power(depth,(1,0) if c==0 else (0,1)))
            before = K.coordinates(basis)
            after = K.coordinates(R.sigma(basis,22))
            difference = [(after[j][v]-before[j][v])%P for j in range(44) for v in (0,1)]
            values = [sum(x*y for x,y in zip(row,difference))%P for row in annihilator]
            assert values==[0,0,0,0]
            central_checks.append([depth,c,values])
    if progress:
        print('PASS sigma^22 acts trivially on the complete four-dimensional quotient.',flush=True)
        print('PASS finite O_F43/(pi^46); all88 elementary Kummer basis vectors; p-power kernel.',flush=True)
        print('PASS unit rank43, augmented rank84, q Frobenius rank41; three complete relations.',flush=True)
        print('PASS four quotient characters; rank84 minor determinant',minor_det,flush=True)
    return {'schema':'R375-q-frobenius-matrix-v1','p':P,'ring_pi_precision':46,
            'C':C,'omega_teich_mod_p2':list(R.omega),
            'input_sha256':{name:hashlib.sha256(raw[name]).hexdigest() for name in INPUTS},
            'canonical_u_mod_pi46':u,'canonical_y_mod_pi46':Y,'ordinary_z_mod_pi46':Z,
            'elementary_unit_depths':LABELS,'coefficient_basis':['1','i'],
            'ordinary_unit_columns':E_labels,'ordinary_unit_Kummer_coordinates':E_coords,
            'alpha_conjugate_Kummer_coordinates':alpha_coords,
            'arithmetic_Frobenius_sign_relative_to_alpha':-1,
            'ordinary_unit_rank':43,'augmented_rank':84,'q_Frobenius_quotient_rank':41,
            'rank84_minor_row_indices':pr,'rank84_minor_column_indices':pa,
            'rank84_minor_determinant_mod43':minor_det,
            'three_complete_q_relations':relations,
            'kernel_Delta_character_exponents':[16,28,22],
            'q_split_abelian_exponent43_quotient_dimension':4,
            'four_quotient_character_row_vectors':annihilator,
            'sigma22_quotient_basis_checks':central_checks,
            'sigma22_acts_trivially_on_q_split_Frattini_quotient':True,
            'q_split_pro43_minimal_generator_number':4,
            'q_split_pro43_relation_number_upper_bound':3,
            'q_split_pro43_tower_descends_to_F_sigma22_fixed_field':True,
            'q_split_class_field_degree_over_F':P**4,
            'used_GRH':False,'actual_norm_preimage_computed':False,
            'actual_L_computed':False,'nonabelian_q_Frobenius_computed':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('notes_dir',type=Path)
    parser.add_argument('--certificate',type=Path,required=True)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--progress',action='store_true')
    args = parser.parse_args()
    data = json.loads(json.dumps(run(args.notes_dir,args.progress)))
    if args.write:
        args.certificate.write_text(json.dumps(data,indent=2)+'\n')
    else:
        assert data==json.loads(args.certificate.read_text())
    print('PASS R375: actual abelian q Frobenius rank41; Norm/L still uncomputed.',flush=True)


if __name__=='__main__':
    main()
