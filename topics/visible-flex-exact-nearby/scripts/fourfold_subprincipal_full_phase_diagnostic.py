#!/usr/bin/env python3
"""Numerical diagnostic of the complete geometric forward phase.

This is explicitly not an interval certificate. It retains every saved finite
reference Fourier coefficient, every radial reference segment, and every
regularized root polynomial coefficient, and combines the exact cut-flux
cancellation before floating-point integration. No partial trace is accepted.
The actual geometry is evaluated at the center of the same affine family.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_parameter_germ import ParameterGermFastBulkTarget
from fourfold_phase_root_fourier_fit import read, save, sha, stored, decode
from fourfold_shared_dense_reference import load


OBJECT = Path("data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json")
DESCRIPTOR = Path("data/phase_ring_continuation/step5_retargeted_reference/descriptor.json")
ROOT_SOURCE = Path("data/R106/root_regularized_center_degree80_plus/report.json")
FIELDS = ("source_even", "source_odd", "root_field")


def hashed(row):
    p = Path(row["path"])
    if sha(p) != row["sha256"]:
        raise ValueError("changed scientific input " + str(p))
    return p, read(p)


def exact_time_float(row):
    a = float(Fraction(int(row["numerator"]), int(row["denominator"])))
    if row["kind"] == "rational_multiple_of_pi":
        return a * math.pi
    if row["kind"] == "rational":
        return a
    raise ValueError("unknown exact time convention")


def fft_values(positive, nodes, derivative=0):
    """Every input coefficient contributes, including frequencies >= nodes."""
    k = np.arange(len(positive))
    out = np.zeros(nodes, dtype=np.complex128)
    np.add.at(out, k % nodes, positive * (1j * k) ** derivative)
    np.add.at(out, (-k[1:]) % nodes,
              positive[1:].conjugate() * (-1j * k[1:]) ** derivative)
    return (nodes * np.fft.ifft(out)).real


class FullForwardReference:
    def __init__(self, descriptor, nodes):
        self.path = descriptor
        self.doc = read(descriptor)
        if not self.doc.get("complete") or not all(self.doc["proof_gates"].values()):
            raise ValueError("complete symbolic reference required")
        self.base_path, self.base = hashed(self.doc["old_forward_reference"])
        self.q_path, self.q = hashed(self.doc["Q_forward"])
        if (self.base["exact_time_endpoints"] != self.q["exact_time_endpoints"]
                or self.base["segment_count"] != self.q["segment_count"]
                or self.base["time_degree"] != 7 or self.q["time_degree"] != 7
                or self.base["fields"] != ["U", "L"] or self.q["fields"] != ["Qtilde"]):
            raise ValueError("incompatible full forward time/reference conventions")
        self.nodes = nodes
        self.labels = 2 * math.pi * np.arange(nodes) / nodes
        self.times = np.array([exact_time_float(r) for r in self.base["exact_time_endpoints"]])
        if not np.all(np.diff(self.times) > 0) or self.base["trace_identity"]["sign"] != -1:
            raise ValueError("wrong forward branch or chronology")
        self.identity = {"descriptor": sha(descriptor), "base_manifest": sha(self.base_path),
                         "Q_manifest": sha(self.q_path)}
        self.checked = {}
        # Fail before creating any phase output if even one finite segment is absent.
        for path, doc in ((self.base_path, self.base), (self.q_path, self.q)):
            cursor = 0
            for shard in doc["shards"]:
                p = path.parent / shard["path"]
                if shard["start_segment"] != cursor:
                    raise ValueError("full-reference manifest segment gap")
                if not p.exists() or p.stat().st_size != shard["bytes"] or sha(p) != shard["sha256"]:
                    raise ValueError("full finite reference shard absent or changed " + str(p))
                self.checked[str(p)] = shard["sha256"]
                cursor += shard["segment_count"]
            if cursor != doc["segment_count"]:
                raise ValueError("incomplete final reference span")
        p, d = hashed(self.doc["initial_correction"])
        denominator = 2.0 ** int(d["denominator_power_of_two"])
        positive = np.array([(int(re) + 1j * int(im)) / denominator
                             for re, im in d["nonnegative_integer_coefficients"]])
        if len(positive) != d["degree"] + 1:
            raise ValueError("incomplete static initial correction")
        self.a = fft_values(positive, nodes)
        self.ax = fft_values(positive, nodes, 1)
        self.cache = {}

    def arrays(self, segment, is_q):
        path, doc = (self.q_path, self.q) if is_q else (self.base_path, self.base)
        row = next(r for r in doc["shards"]
                   if r["start_segment"] <= segment < r["start_segment"] + r["segment_count"])
        name = str(path.parent / row["path"])
        if is_q not in self.cache or self.cache[is_q][0] != name:
            data = load(Path(name))
            meta = json.loads(str(data["metadata"]))
            if (meta["start_segment"] != row["start_segment"]
                    or meta["segment_count"] != row["segment_count"]
                    or meta["exact_times"] != doc["exact_time_endpoints"][
                        row["start_segment"]:row["start_segment"] + row["segment_count"] + 1]):
                raise ValueError("finite reference shard metadata differs")
            real, imag = data["coefficient_real"], data["coefficient_imag"]
            expected = ((row["segment_count"], 8, doc["Fourier_degree"] + 1)
                        if is_q else (row["segment_count"], 8, 2, doc["Fourier_degree"] + 1))
            if real.shape != expected or imag.shape != expected or not np.all(np.isfinite(real)):
                raise ValueError("finite reference shape or values differ")
            self.cache[is_q] = name, real + 1j * imag
        values = self.cache[is_q][1][segment - row["start_segment"]]
        return values if is_q else values[:, 0, :]

    def sample(self, tau):
        j = min(max(bisect_right(self.times, tau) - 1, 0), len(self.times) - 2)
        v = (tau - self.times[j]) / (self.times[j + 1] - self.times[j])
        if not -1e-12 <= v <= 1 + 1e-12:
            raise ValueError("reference sample leaves segment")
        bernstein = np.array([math.comb(7, k) * v**k * (1-v)**(7-k) for k in range(8)])
        up = bernstein @ self.arrays(j, False)
        qp = bernstein @ self.arrays(j, True)
        U, Ux = fft_values(up, self.nodes), fft_values(up, self.nodes, 1)
        Q, Qx = fft_values(qp, self.nodes), fft_values(qp, self.nodes, 1)
        return self.labels / 4 + U + Q*self.a, .25 + Ux + Qx*self.a + Q*self.ax


def local_fourier(coefficients, frequencies, theta, grid=2048, order=14):
    """Floating evaluation of a full finite polynomial by local Taylor FFT.

    The report records this diagnostic interpolation, whose error is not
    silently upgraded into a rigorous bound.
    """
    theta = np.asarray(theta)
    x = 4*theta
    anchor = np.rint((x % (2*math.pi)) * grid/(2*math.pi)).astype(int) % grid
    delta = ((x - 2*math.pi*anchor/grid + math.pi) % (2*math.pi) - math.pi)
    z = delta * grid/(2*math.pi)
    coefficient = np.asarray(coefficients)
    frequencies = np.asarray(frequencies)
    extra = coefficient.shape[1:]
    if len(frequencies) != len(coefficient):
        raise ValueError("frequency/full coefficient dimension differs")
    factor = np.ones(len(frequencies), dtype=np.complex128)
    out = np.zeros((len(theta),) + extra, dtype=np.complex128)
    powers = np.ones(len(theta))
    derivative_factor = 1j*frequencies*(2*math.pi/grid)
    for j in range(order + 1):
        data = np.zeros((grid,) + extra, dtype=np.complex128)
        np.add.at(data, frequencies % grid,
                  coefficient * factor.reshape((-1,) + (1,)*len(extra)))
        val = grid * np.fft.ifft(data, axis=0)
        out += val[anchor] * powers.reshape((-1,) + (1,)*len(extra))
        factor *= derivative_factor/(j + 1)
        powers *= z
    return out.real


def product_jets(a, b):
    return np.array([sum(math.comb(n, j)*a[j]*b[n-j] for j in range(n+1))
                     for n in range(4)])


def trig_jets(a):
    s, c = np.sin(a[0]), np.cos(a[0])
    a1, a2, a3 = a[1:]
    return (np.array([s, c*a1, c*a2-s*a1*a1,
                      c*a3-3*s*a1*a2-c*a1*a1*a1]),
            np.array([c, -s*a1, -s*a2-c*a1*a1,
                      -s*a3-3*c*a1*a2+s*a1*a1*a1]))


class CenterGeometry:
    def __init__(self, nodes, grid, order):
        self.target = ParameterGermFastBulkTarget(OBJECT, Fraction(1,10**24),
            nodes, nodes, arb(".002"), arb(".0015"), arb(".32"))
        self.grid, self.order, self.nodes = grid, order, nodes
        self.frequency = np.asarray(self.target.frequency)
        self.k = self.frequency // 4
        self.sines = np.sin(2*math.pi*np.arange(1,self.target.modes+1)[:,None]
                           *np.arange(nodes)[None,:]/nodes)
        self.cell = None
        self.cache = {}

    def set_cell(self, lo, hi):
        cell = (Fraction.from_float(float(lo)), Fraction.from_float(float(hi)))
        if cell == self.cell:
            return
        self.cell = cell
        self.target.set_cell(*cell)
        value = self.target.scalar_poly.real
        self.scalar = (value.lo + value.hi)/2
        self.anchor = float(self.target.anchor)

    def phase(self, r, theta, cell):
        self.set_cell(*cell)
        m = self.target.modes
        delta = abs(r) - self.anchor
        jet = np.zeros((4,2*m+2))
        for n in range(20,-1,-1):
            jet = jet*delta + np.array([self.scalar[n],jet[0],2*jet[1],3*jet[2]])
        beta, gamma, radius, height = jet[:,:m],jet[:,m:2*m],jet[:,-2],jet[:,-1]
        sb, cb = trig_jets(beta @ self.sines)
        sg, cg = trig_jets(gamma @ self.sines)
        tangent = np.stack([-product_jets(cg,sb),product_jets(cg,cb),sg],axis=-1)
        cf = np.fft.fft(tangent,axis=1)/self.nodes
        n = self.frequency
        primitive = np.zeros_like(cf)
        primitive[:,:,0] = (1j*n[None,:]*cf[:,:,0]+cf[:,:,1])/(1-n*n)[None,:]
        primitive[:,:,1] = (-cf[:,:,0]+1j*n[None,:]*cf[:,:,1])/(1-n*n)[None,:]
        nz = np.flatnonzero(n)
        primitive[:,nz,2] = cf[:,nz,2]/(1j*n[nz][None,:])
        primitive[:,self.nodes//2,:] = 0
        primitive[:,0,1:] = 0
        pos = np.arange(1,self.nodes//2)
        for coordinate,parity in enumerate((1,-1,1)):
            v = (primitive[:,pos,coordinate]+parity*primitive[:,-pos,coordinate])/2
            primitive[:,pos,coordinate],primitive[:,-pos,coordinate] = v,parity*v
        primitive = product_jets(primitive,radius[:,None,None])
        primitive[:,0,2] += height
        reverse = (-np.arange(self.nodes)) % self.nodes
        dot = lambda a,b: np.sum(a*b,axis=-1)
        E0 = np.sum(dot(primitive[1],primitive[1,reverse])).real
        E1 = 2*np.sum(dot(primitive[1],primitive[2,reverse])).real
        E2 = 2*np.sum(dot(primitive[2],primitive[2,reverse])
                       +dot(primitive[1],primitive[3,reverse])).real
        a,ar,arr,arrr = radius
        K = (ar*E1-2*arr*E0)/(2*a*E0*E0)
        Kp = (ar*E2-arr*E1-2*arrr*E0)/(2*a*E0*E0)-K*(ar/a+2*E1/E0)
        if not K < 0:
            raise ValueError("diagnostic sampled curvature is not negative")
        ff = local_fourier(primitive[:3].transpose(1,0,2),self.k,theta,
                           self.grid,self.order)
        F,X,Frr = ff[:,0],ff[:,1],ff[:,2]
        angles = 4*np.arange(1,m+1)[:,None]*theta[None,:]
        s,c = np.sin(angles),np.cos(angles)
        sb,cb = trig_jets(beta @ s)
        sg,cg = trig_jets(gamma @ s)
        T = np.stack([-product_jets(cg,sb),product_jets(cg,cb),sg],axis=-1)
        bt,gt = (beta[0,:,None]*4*np.arange(1,m+1)[:,None]*c).sum(0),(
            gamma[0,:,None]*4*np.arange(1,m+1)[:,None]*c).sum(0)
        dT = np.stack([sg[0]*gt*sb[0]-cg[0]*cb[0]*bt-T[0,:,1],
                      -sg[0]*gt*cb[0]-cg[0]*sb[0]*bt+T[0,:,0],cg[0]*gt],axis=-1)
        Y,Frt,Ftt = radius[0]*T[0],radius[1]*T[0]+radius[0]*T[1],radius[0]*dT
        if r < 0:
            reflection = np.array([1.,1.,-1.])
            F,X,Frr,Y,Frt,Ftt = (F*reflection,-X*reflection,Frr*reflection,
                                 Y*reflection,-Frt*reflection,Ftt*reflection)
            Kp = -Kp
        C = np.cross(Y,X)
        Cr,Ct = np.cross(Frt,X)+np.cross(Y,Frr),np.cross(Ftt,X)+np.cross(Y,Frt)
        G,R,H = dot(C,C),dot(F,F),dot(C,F)
        l,braw,nraw = dot(C,Frr),dot(C,Frt),dot(C,Ftt)
        aa,bb,cc = -nraw/G,braw/G,-l/G
        omega,chat = ((l*nraw-braw*braw)/(G*G)-K)/aa,(bb*bb+K)/aa
        FX,FY = dot(F,X),dot(F,Y)
        d = (aa*(dot(X,X)-FX*FX/R)+2*bb*(dot(X,Y)-FX*FY/R)
             +cc*(dot(Y,Y)-FY*FY/R))/R
        zr,zt = dot(Cr,F)/H-dot(C,Cr)/G-FX/R,dot(Ct,F)/H-dot(C,Ct)/G-FY/R
        Lr,Lt = Kp/(2*K)-2*zr,-2*zt
        if r == 0:
            ell = Frt[:,2]/X[:,2]-FY/R
        else:
            ell = Y[:,2]/F[:,2]-FY/R
        sqrtK = math.sqrt(-K)
        D = (d+omega*(ell*ell+ell*Lt)
             -(aa*Lr*Lr+2*bb*Lr*Lt+chat*Lt*Lt)/4)/sqrtK
        S = omega*ell/sqrtK
        if not np.all(np.isfinite(D)) or not np.all(np.isfinite(S)):
            raise ValueError("nonfinite diagnostic phase field")
        return D,S


def full_encoded(row):
    positive = np.array([math.ldexp(float(int(v[0])),int(v[1]))
                         for v in row["positive_coefficients"]])
    if row["parity"] == "odd":
        positive = 1j*positive
    return np.concatenate([positive[:0:-1].conjugate(),positive])


def centered_sum(a,b):
    n = max(len(a),len(b))
    c = np.zeros(n,dtype=np.complex128)
    c[(n-len(a))//2:(n+len(a))//2] += a
    c[(n-len(b))//2:(n+len(b))//2] += b
    return c


class RootFields:
    def __init__(self,path,grid,order):
        self.path,self.doc = path,read(path)
        d = self.doc
        if not d["complete"] or not d["all_output_convolution_modes_retained"] or not d["no_missing_radial_rows"]:
            raise ValueError("full regularized finite root source required")
        if sha(d["input_report_path"]) != d["input_report_sha256"]:
            raise ValueError("center seven-field input changed")
        self.input = read(d["input_report_path"])
        self.rows = {name:[] for name in FIELDS}
        cursor = 0
        for row in d["shards"]:
            if row["first_row"] != cursor or sha(row["path"]) != row["sha256"]:
                raise ValueError("complete finite root coefficient gap or hash mismatch")
            block = read(row["path"])
            for rr in block["rows"]:
                if rr["radial_row"] != cursor:
                    raise ValueError("missing radial coefficient")
                for name in FIELDS:
                    value = full_encoded(rr["fields"][name]) if name in rr["fields"] else np.zeros(1)
                    self.rows[name].append(value)
                cursor += 1
        if cursor != d["finite_rows_done"]:
            raise ValueError("incomplete root radial range")
        self.scale = float(decode(d["radial_scale_dyadic"]))
        self.root = float(stored(d["root"]).mid())
        self.cut = float(Fraction(d["original_fixed_physical_cut"]))
        self.c = math.sqrt(self.root-self.cut)
        self.grid,self.order = grid,order
        # Only rows zero and one enter the exact transport polynomial.
        first = self.input["coefficient_shards"][0]
        if sha(first["path"]) != first["sha256"]:
            raise ValueError("root transport input changed")
        block = read(first["path"])
        def seven(row,name,odd=False):
            field = dict(row["fields"][name],parity="odd" if odd else "even")
            return full_encoded(field)
        G0,G1,q0 = seven(block["rows"][0],"G"),seven(block["rows"][1],"G"),seven(block["rows"][0],"q",True)
        prod = np.convolve(q0,G0)
        k = np.arange(-(len(prod)//2),len(prod)//2+1)
        self.Bm3 = -G0/3
        self.Bm1 = centered_sum(-G1/self.scale,-2j*4*k*prod/3)

    def coeff(self,name,rho):
        rows = self.rows[name]
        n = max(map(len,rows))
        result = np.zeros(n,dtype=np.complex128)
        z = rho/self.scale
        for row in reversed(rows):
            result *= z
            result[(n-len(row))//2:(n+len(row))//2] += row
        return result

    def eval(self,coeff,theta):
        return local_fourier(coeff,np.arange(-(len(coeff)//2),len(coeff)//2+1),
                             theta,self.grid,self.order)

    def source(self,s,theta,side):
        coeff = centered_sum(self.coeff("source_even",s*s),
                             side*s*self.coeff("source_odd",s*s))
        return self.eval(coeff,theta)

    def transport(self,theta):
        return self.eval(centered_sum(self.Bm3/self.c**3,self.Bm1/self.c),theta)

    def endpoint(self,theta,side):
        return side*self.eval(self.rows["root_field"][0],theta)


def diagnostics(values):
    coefficients = np.fft.fft(values)/len(values)
    centered = values-values.mean()
    K = len(values)//2
    return {"mean":float(values.mean()),"minimum":float(values.min()),
            "maximum":float(values.max()),"nonmean_sample_sup":float(np.max(np.abs(centered))),
            "sample_L2":float(np.sqrt(np.mean(values**2))),
            "sampled_Fourier_l1":float(np.abs(coefficients).sum()),
            "sampled_Fourier_nonmean_l1":float(np.abs(coefficients[1:]).sum()),
            "sampled_Fourier_upper_quarter_l1":float(np.abs(coefficients[K//2:K+K//2+1]).sum()),
            "first_32_positive_coefficients":[[float(v.real),float(v.imag)] for v in coefficients[:33]]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--labels",type=int,default=512)
    p.add_argument("--quadrature-order",type=int,default=6)
    p.add_argument("--primitive-nodes",type=int,default=512)
    p.add_argument("--evaluation-grid",type=int,default=4096)
    p.add_argument("--taylor-order",type=int,default=14)
    p.add_argument("--out",type=Path,required=True)
    a = p.parse_args()
    if a.out.exists():
        raise ValueError("preserve previous diagnostic; use a new report")
    ctx.prec,ctx.cap = 256,4
    started = time.monotonic()
    reference = FullForwardReference(DESCRIPTOR,a.labels)
    root = RootFields(ROOT_SOURCE,a.evaluation_grid,a.taylor_order)
    geometry = CenterGeometry(a.primitive_nodes,a.evaluation_grid,a.taylor_order)
    taucut = math.asin(root.cut/root.root)
    scalar_knots = sorted({abs(float(v)) for key,values in geometry.target.frozen.items()
                           if key.endswith("_knots") for v in values if 0<abs(float(v))<root.cut})
    positive_cells = [0.] + scalar_knots + [root.cut]
    knots = set(reference.times.tolist()) | {-taucut,taucut,0.}
    for r in scalar_knots:
        tau = math.asin(r/root.root)
        knots.update((-tau,tau))
    knots = sorted(knots)
    z,w = np.polynomial.legendre.leggauss(a.quadrature_order)
    primary = np.zeros(a.labels)
    angular_primitive = np.zeros(a.labels)
    regular = np.zeros(a.labels)
    root_terms = np.zeros(a.labels)
    chunks = []
    for i,(left,right) in enumerate(zip(knots,knots[1:])):
        mid,half = (left+right)/2,(right-left)/2
        in_root = abs(mid)>taucut
        for point,weight in zip(z,w):
            tau = mid+half*point
            theta,J = reference.sample(tau)
            if in_root:
                side = 1 if tau>0 else -1
                s = math.sqrt(2*root.root)*math.sin((math.pi/2-side*tau)/2)
                ds = math.sqrt(root.root/2)*math.cos((math.pi/2-side*tau)/2)
                regular += half*weight*root.source(s,theta,side)*J*ds
            else:
                r = root.root*math.sin(tau)
                j = min(bisect_right(positive_cells,abs(r))-1,len(positive_cells)-2)
                D,S = geometry.phase(r,theta,positive_cells[j:j+2])
                dr = root.root*math.cos(tau)
                primary += .5*half*weight*D*J*dr
                angular_primitive += .5*half*weight*S*dr
        if i%40==0:
            progress = {"piece":i+1,"total":len(knots)-1,
                        "seconds":time.monotonic()-started,
                        "primary_mean":float(primary.mean()),"regular_mean":float(regular.mean())}
            chunks.append(progress)
            print(progress,flush=True)
    for side in (-1,1):
        theta,J = reference.sample(side*taucut)
        root_terms += J*root.transport(theta)
        theta,J = reference.sample(side*math.pi/2)
        root_terms += J*root.endpoint(theta,side)
    freq = np.fft.fftfreq(a.labels,d=1/a.labels)
    angular = np.fft.ifft(1j*freq*np.fft.fft(angular_primitive)).real
    phase = primary+angular+regular+root_terms
    phi = (1+math.sqrt(5))/2
    dstar = math.pi*(690433168*phi+94331801)/(1251918455*phi+171045842)
    second = np.fft.ifft(np.fft.fft(phase)*np.exp(1j*freq*dstar)).real
    returned_nominal = phase+second
    report = {"kind":"R106_complete_finite_reference_phase_diagnostic",
        "complete_diagnostic":True,"rigorous_phase_certificate":False,
        "source_sha256":sha(__file__),"descriptor":str(DESCRIPTOR),
        "reference_identity":reference.identity,
        "all_reference_shards":reference.checked,
        "root_source":str(ROOT_SOURCE),"root_source_sha256":sha(ROOT_SOURCE),
        "root_center":root.root,"cut":root.cut,
        "actual_center_parameter":reference.doc["target_exact_delta_fraction"],
        "settings":vars(a)|{"out":str(a.out)},
        "quadrature_pieces":len(knots)-1,"reference_segment_count":len(reference.times)-1,
        "complete_saved_finite_modes_retained":True,"exact_cut_flux_cancellation_used":True,
        "initial_physical_label":"H5(x)/4, including the complete saved Q*a correction",
        "phase_components":{name:diagnostics(values) for name,values in
            (("strict_primary",primary),("strict_angular_divergence",angular),
             ("root_regular_source",regular),("root_transport_and_root_endpoint",root_terms))},
        "complete_forward_geometric_phase_diagnostic":diagnostics(phase),
        "nominal_two_leg_diagnostic_before_final_label_correction":diagnostics(returned_nominal),
        "finite_real_samples":phase.tolist(),
        "progress":chunks,"seconds":time.monotonic()-started,
        "limitations":[
          "Floating midpoint primitive and finite Taylor evaluation are diagnostic only.",
          "Gauss quadrature error, true-minus-reference flow error and full-family variation are not charged.",
          "The final J o Phi label transformation is omitted from the nominal two-leg diagnostic.",
          "No full R104 operator coefficient, Ai/contact remainder, R_star or high inverse is certified."]}
    save(a.out,report)
    print({"out":str(a.out),"sha256":sha(a.out),
           "forward":report["complete_forward_geometric_phase_diagnostic"],
           "nominal_two_leg":report["nominal_two_leg_diagnostic_before_final_label_correction"],
           "seconds":report["seconds"]},flush=True)


if __name__=="__main__":
    main()
