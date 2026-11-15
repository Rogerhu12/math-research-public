#!/usr/bin/env python3
"""Same-field continuous active-sheet balls for the R248/R281 boundary.

Interpret the actual complete shared-B bundle as the exact shared-node real
Hermite / full FFT normal form already declared by R249, R258 and R279.
Differentiate that expression, not the floating renderer's labelled jets.
This entry does not manufacture an accepted parent, alter g, run a new BVP,
or turn a sampled mesh into a C2/reach certificate.  Scientific arithmetic
and the original loader run only in the named public repository's Actions.

Every upper and reflected lower closed parameter cell is exported.  Resource
or interval failures remain explicit unresolved cells.  Temporary outputs are
recomputable; repository rule 15 permits only sources/parameters/run/hashes
and compact conclusions to be retained, not these complete cell payloads.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import OrderedDict
from fractions import Fraction as F
import gzip
import hashlib
import importlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "same-shared-field-complete-active-interval-balls-v1"
CELL_SCHEMA = "same-shared-field-closed-active-cell-six-jets-v1"
EXPRESSION = "R249-R258-R279-exact-shared-nodes-full-FFT-shared-B-complete-material-cut-v1"
SOURCE_PINS = {
    "geometry_20261114_shared_background_closed_assembly.py": "ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb",
    "geometry_20261114_shared_background_normal_form.py": "da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9",
    "geometry_20261114_large_core_saved_prefix.py": "51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0",
    "geometry_20261114_large_core_closed_assembly.py": "e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0",
    "geometry_20261114_inlet_parity_normal_form.py": "ce5f287c1de870b6bf71d1650d6942e23fd2bdd23a25af72ec5b637599a97410",
    "geometry_20261114_full_state_continuous_cover.py": "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "exact_20261114_refined_tail_adapter.py": "6b06db6c7c96078b9fabe403a0b3ade14f8b30b07a78b565ed299c77f840d937",
    "exact_20261114_refined_closed_assembly.py": "1fec55a9d9f6c2a9211e64036226496bb4e4ae42c641c842e863e8c4f34fcccc",
    "root_mixed_phase_normal_balls.py": "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6",
}
JET_NAMES = ("value", "u", "q", "uu", "uq", "qq")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Run scientific arithmetic only in the named public Actions repository")


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)+"\n").encode()


def canonical_sha(value):
    return sha_bytes(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode())


def receipt(path):
    digest = hashlib.sha256()
    size = 0
    with Path(path).open("rb") as stream:
        for raw in iter(lambda:stream.read(1048576),b""):
            size += len(raw)
            digest.update(raw)
    return dict(file=Path(path).name, bytes=size, sha256=digest.hexdigest())


def exact(value):
    if isinstance(value, F):
        return value
    if isinstance(value, bool):
        raise ValueError("A Boolean is not a scientific coefficient")
    if isinstance(value, int) or isinstance(value, np.integer):
        return F(int(value))
    n, d = value.as_integer_ratio()
    return F(int(n), int(d))


def initialise_runtime(code_directory):
    require_actions()
    root = Path(code_directory).resolve()
    sources = {}
    for name, expected in SOURCE_PINS.items():
        raw = (root/name).read_bytes()
        if sha_bytes(raw) != expected:
            raise ValueError("A frozen defining source changed: "+name)
        sources[name] = dict(bytes=len(raw), sha256=expected)
    sys.path.insert(0, str(root))
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[key] = "1"
    global np, arb, ctx, fmpq
    import numpy as np
    from flint import arb, ctx, fmpq
    geometry = importlib.import_module("geometry_20261114_shared_background_closed_assembly")
    background = importlib.import_module("geometry_20261114_shared_background_normal_form")
    spec = importlib.util.spec_from_file_location("_active_ball_r62", root/"root_mixed_phase_normal_balls.py")
    kernel = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(kernel)
    return geometry, background, kernel, sources


def ball(value):
    q = exact(value)
    return arb(fmpq(q.numerator, q.denominator))


def interval(a, b):
    """Exact rational endpoints -> outward Arb ball; no decimal float input."""
    a, b = exact(a), exact(b)
    if a > b:
        raise ValueError("Reversed exact parameter interval")
    # The constructor rounds the radius upward and accounts for midpoint
    # rounding; rational strings are documented exact inputs, not floats.
    return arb(str((a+b)/2), str((b-a)/2))


def bounds(value):
    if not value.is_finite():
        raise ArithmeticError("Nonfinite interval enclosure")
    return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))


def encode_interval(value):
    a, b = bounds(value)
    return dict(lower=str(a), upper=str(b))


class Jet2:
    """Actual derivatives (not factorial-scaled) in (u,q), through order 2."""
    __slots__ = ("d",)

    def __init__(self, values):
        self.d = tuple(values)
        if len(self.d) != 6:
            raise ValueError("All six derivative slots are required")

    @classmethod
    def constant(cls, value):
        v = value if isinstance(value, arb) else ball(value)
        return cls((v, arb(0), arb(0), arb(0), arb(0), arb(0)))

    @classmethod
    def variable(cls, a, b, coordinate):
        values = [interval(a, b), arb(0), arb(0), arb(0), arb(0), arb(0)]
        values[1 if coordinate == 0 else 2] = arb(1)
        return cls(values)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Jet2) else Jet2.constant(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Jet2(tuple(a+b for a, b in zip(self.d, other.d)))

    __radd__ = __add__

    def __neg__(self):
        return Jet2(tuple(-a for a in self.d))

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other = self.coerce(other)
        a, au, aq, auu, auq, aqq = self.d
        b, bu, bq, buu, buq, bqq = other.d
        return Jet2((a*b, au*b+a*bu, aq*b+a*bq,
                     auu*b+2*au*bu+a*buu,
                     auq*b+au*bq+aq*bu+a*buq,
                     aqq*b+2*aq*bq+a*bqq))

    __rmul__ = __mul__

    def __truediv__(self, other):
        # Every denominator in this finite expression is a fixed nonzero
        # rational width or cut-chart coefficient, never a sampled field.
        q = exact(other)
        if not q:
            raise ZeroDivisionError("A declared finite-coordinate denominator vanished")
        return self*(1/q)

    def compose(self, value, first, second):
        _, u, q, uu, uq, qq = self.d
        return Jet2((value, first*u, first*q, second*u*u+first*uu,
                     second*u*q+first*uq, second*q*q+first*qq))

    def sin(self):
        s, c = self.d[0].sin(), self.d[0].cos()
        return self.compose(s, c, -s)

    def cos(self):
        s, c = self.d[0].sin(), self.d[0].cos()
        return self.compose(c, -s, -c)


def polynomial(coefficients, argument):
    value = Jet2.constant(0)
    for coefficient in reversed(coefficients):
        value = value*argument+coefficient
    return value


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), arb(0))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def array_identity(value, dtype):
    binary = np.asarray(value, dtype=dtype, order="C")
    if not np.all(np.isfinite(binary)):
        raise ValueError("Nonfinite defining nodal data")
    raw = binary.tobytes(order="C")
    return dict(dtype=dtype, shape=list(binary.shape), bytes=len(raw),
                raw_sha256=sha_bytes(raw),
                shape_and_raw_sha256=sha_bytes(str(binary.shape).encode()+b"\0"+raw))


class ExactFiniteField:
    """Only the bound finite expressions; no call to renderer jets below."""
    def __init__(self, bundle, background):
        self.paths, self.plan, self.assembly, self.table, self.saved, self.A, self.binding = bundle
        self.background = background
        self.B = self.A.shared_background
        self.M = int(self.saved.M)
        self.x = tuple(exact(x) for x in self.saved.quintic.x)
        self.nodal = tuple(np.asarray(value) for value in self.saved.quintic.nodal)
        if (len(self.x) < 2 or any(a >= b for a,b in zip(self.x,self.x[1:]))
                or any(v.shape != (len(self.x), 3*self.M+2) for v in self.nodal)
                or any(v.dtype.kind != "f" or v.dtype.itemsize != 8 for v in self.nodal)):
            raise ValueError("Retain the complete current shared binary64 prefix nodes")
        if self.x[0] != 0 or self.x[-1] != exact(self.A.L):
            raise ValueError("The original complete prefix endpoint/radial chart differs")
        self.core = tuple(exact(x) for x in self.saved.core)
        self.density = tuple((1-4*m*m)*x for m,x in enumerate(self.core, 1))
        self.rho_lower = exact(self.saved.rho_lower_exact)
        if self.rho_lower <= 0:
            raise ValueError("The actual loader's full material-circle certificate is required")
        self.registration = self.saved.registration
        expected_phase_rule = ("For all real alpha, moving F_alpha(s,theta)=R_alpha F_0(s,theta-alpha); "
                               "fixed caps are unchanged. alpha=pi*t/2 on t in [0,1].")
        if (self.plan.get("phase_rule") != expected_phase_rule
                or self.assembly["mean_gauge"]["whole_lower_sheet_reflected"] is not True
                or self.assembly["core_and_hold_gauge"]["native_cap_rotation_axis_xy"] != [0.,0.]):
            raise ValueError("The actual source family/axis/reflection is not the bound R248 family")
        self.beta = exact(self.registration["rotation_angle"])
        self.translation = tuple(exact(x) for x in self.registration["prefix_translation_to_subtract"])
        self.cuff, self.inner, self.cut, self.width = map(exact, (self.A.cuff,self.A.inner,self.A.cut,self.A.W))
        self.cut_start = self.cut-self.width
        self.v, self.acceleration = exact(self.A.ap), exact(self.A.app)
        if not (0 < self.cuff < self.inner < self.cut_start < self.cut and self.v < 0):
            raise ValueError("The original positive radii/collar/cut-chart conditions differ")
        self.radii = tuple(exact(x) for x in self.A.tail.r)
        if (self.radii[0] != self.inner or self.radii[-1] != self.cut
                or any(a >= b for a,b in zip(self.radii,self.radii[1:]))):
            raise ValueError("All actual native radial nodes must be retained")
        if (self.B.radii[0] != self.cuff or self.B.radii[-1] != self.cut
                or exact(self.A.sigma) != -1):
            raise ValueError("The shared scalar or upper-tail reflection changed")
        self.frequency_count = self.A.tail.N//2+1
        self.node_cache, self.prefix_cache, self.tail_cache = OrderedDict(), OrderedDict(), OrderedDict()
        self.node_records = {}
        self.pieces = self.make_pieces()

    def remember(self, cache, key, value, capacity):
        cache[key] = value
        cache.move_to_end(key)
        while len(cache) > capacity:
            cache.popitem(last=False)
        return value

    def make_pieces(self):
        pieces = [dict(kind="prefix", index=i, left=a, right=b,
                       prefix_span=i) for i,(a,b) in enumerate(zip(self.x,self.x[1:]))]
        breaks = sorted(set((self.cuff,self.inner,self.cut_start,self.cut)+self.radii+self.B.radii))
        for i,(a,b) in enumerate(zip(breaks,breaks[1:])):
            middle = (a+b)/2
            ti = -1 if middle < self.inner else min(len(self.radii)-2,bisect_right(self.radii,middle)-1)
            bi = min(len(self.B.radii)-2,bisect_right(self.B.radii,middle)-1)
            pieces.append(dict(kind="collar" if ti < 0 else "native", index=i,
                               left=a,right=b,tail_span=ti,background_span=bi,
                               cut_patch=(a >= self.cut_start)))
        return pieces

    def node(self, index):
        if index in self.node_cache:
            self.node_cache.move_to_end(index)
            return self.node_cache[index]
        generated = np.asarray(self.A.tail.node_coefficients(index))
        shape = (3,self.frequency_count,3)
        if generated.shape != shape or not np.all(np.isfinite(generated)):
            raise ValueError("The actual node lost a mode, coordinate or derivative")
        binary = np.asarray(generated,dtype="<c16",order="C")
        if not np.array_equal(binary.astype(np.clongdouble),generated):
            raise ValueError("The FFT node needs a new explicit non-binary64 encoding")
        record = array_identity(binary,"<c16")
        original = self.A.tail.rows[index]
        record.update(index=index,exact_radius=str(self.radii[index]),
                      original_node_file=original["file"],
                      original_compressed_sha256=original["sha256"],
                      original_raw_sha256=original["rawSha256"],
                      actual_dtype=str(generated.dtype),complex128_roundtrip_exact=True)
        if index in self.node_records and self.node_records[index] != record:
            raise ValueError("Re-evaluation changed an already bound complete FFT node")
        self.node_records[index] = record
        data = tuple(tuple(tuple((exact(z.real),exact(z.imag)) for z in row) for row in derivative)
                     for derivative in generated)
        return self.remember(self.node_cache,index,data,4)

    def prefix_coefficients(self, index):
        if index in self.prefix_cache:
            self.prefix_cache.move_to_end(index)
            return self.prefix_cache[index]
        width = self.x[index+1]-self.x[index]
        result = tuple(self.background.hermite(
            tuple(exact(v[index,column]) for v in self.nodal),
            tuple(exact(v[index+1,column]) for v in self.nodal),width)
            for column in range(3*self.M+2))
        return self.remember(self.prefix_cache,index,result,2)

    def tail_coefficients(self, index):
        if index in self.tail_cache:
            self.tail_cache.move_to_end(index)
            return self.tail_cache[index]
        if index < 0:
            width = self.inner-self.cuff
            right = self.node(0)
            left = None
        else:
            width = self.radii[index+1]-self.radii[index]
            left,right = self.node(index),self.node(index+1)
        result = tuple(tuple(tuple(self.background.hermite(
            (F(0),F(0),F(0)) if left is None else tuple(left[d][k][j][part] for d in range(3)),
            tuple(right[d][k][j][part] for d in range(3)),width)
            for part in range(2)) for j in range(3)) for k in range(self.frequency_count))
        return self.remember(self.tail_cache,index,result,2)

    def registered_world(self, state, phi, *, translate):
        zero = Jet2.constant(0)
        R,T,Z = zero,zero,zero
        for m in range(self.M+1):
            cosine = (2*m*phi).cos()
            R += state[m]*cosine
            Z += state[2*self.M+1+m]*cosine
            if m:
                T += state[self.M+m]*(2*m*phi).sin()
        co,si = phi.cos(),phi.sin()
        x,y = R*co-T*si,R*si+T*co
        if translate:
            x,y = x-self.translation[0],y-self.translation[1]
        beta = ball(self.beta)
        cb,sb = Jet2.constant(beta.cos()),Jet2.constant(beta.sin())
        # Original row-vector SE2: (p-c) @ [[cos,-sin],[sin,cos]].
        return (cb*x+sb*y,-sb*x+cb*y,Z)

    def prefix(self, piece, u, phi):
        i = piece["prefix_span"]
        unit = (u-self.x[i])/(self.x[i+1]-self.x[i])
        states = tuple(polynomial(c,unit) for c in self.prefix_coefficients(i))
        return self.registered_world(states,phi,translate=True)

    def material_angle(self, phi):
        theta = phi
        for m,density in enumerate(self.density,1):
            theta += density/(2*m)*(2*m*phi).sin()
        return theta

    def cut_targets(self, phi):
        worlds = [self.registered_world(tuple(Jet2.constant(exact(value[-1,j]))
                    for j in range(3*self.M+2)),phi,translate=(d == 0))
                  for d,value in enumerate(self.nodal)]
        return (worlds[0],tuple(v/self.v for v in worlds[1]),
                tuple(worlds[2][j]/(self.v*self.v)
                      -self.acceleration*worlds[1][j]/(self.v**3) for j in range(3)))

    def native_cut(self, theta):
        node = self.node(len(self.radii)-1)
        co,si = theta.cos(),theta.sin()
        result = [[Jet2.constant(0) for _ in range(3)] for _ in range(3)]
        for k in range(self.frequency_count):
            ck,sk = (k*theta).cos(),(k*theta).sin()
            for d in range(3):
                for j in range(3):
                    re,im = node[d][k][j]
                    result[d][j] += (1 if j < 2 else -1)*(re*ck-im*sk)
        for d,radius in enumerate((self.cut,F(1),F(0))):
            result[d][0] += radius*co
            result[d][1] += radius*si
            result[d][2] += self.B.evaluate_exact(self.cut,d)
        return result

    def tail(self, piece, u, phi):
        i = piece["tail_span"]
        left,right = ((self.cuff,self.inner) if i < 0 else (self.radii[i],self.radii[i+1]))
        unit = (u-left)/(right-left)
        theta = self.material_angle(phi)
        result = [Jet2.constant(0) for _ in range(3)]
        for k,coordinates in enumerate(self.tail_coefficients(i)):
            co,si = (k*theta).cos(),(k*theta).sin()
            for j,(real,imag) in enumerate(coordinates):
                result[j] += (1 if j < 2 else -1)*(polynomial(real,unit)*co-polynomial(imag,unit)*si)
        result[0] += u*theta.cos()
        result[1] += u*theta.sin()
        b = piece["background_span"]
        bu = (u-self.B.radii[b])/(self.B.radii[b+1]-self.B.radii[b])
        result[2] += polynomial(self.B.coefficients[b],bu)
        if piece["cut_patch"]:
            target,native = self.cut_targets(phi),self.native_cut(theta)
            t = (u-self.cut_start)/self.width
            W = self.width
            weights = (polynomial((0,0,0,10,-15,6),t),
                       polynomial((0,0,0,-4*W,7*W,-3*W),t),
                       polynomial((0,0,0,W*W/2,-W*W,W*W/2),t))
            for j in range(3):
                result[j] += sum((weights[d]*(target[d][j]-native[d][j]) for d in range(3)),Jet2.constant(0))
        return tuple(result)

    def evaluate(self, piece, radial, angular, lower):
        u = Jet2.variable(*radial,coordinate=0)
        q = Jet2.variable(*angular,coordinate=1)
        phi = Jet2.constant(2*arb.pi())*q
        values = self.prefix(piece,u,phi) if piece["kind"] == "prefix" else self.tail(piece,u,phi)
        if lower:
            values = (values[0],values[1],-values[2])
        return values

    def expression_identity(self):
        return dict(schema=EXPRESSION,
            prefix_node_coordinate_identity=array_identity(self.saved.quintic.x,"<f8"),
            prefix_complete_nodal_identities=[array_identity(v,"<f8") for v in self.nodal],
            prefix_field_modes=self.M,material_core_modes=len(self.core),
            exact_core_coefficients=[str(v) for v in self.core],
            complete_material_density_lower=str(self.rho_lower),
            material_map="Phi(phi)=phi+sum((1-4*m*m)*c_m*sin(2*m*phi)/(2*m)); exact real expression",
            recorded_registration=self.registration,exact_rotation_angle=str(self.beta),
            exact_translation_to_subtract=[str(v) for v in self.translation],
            cut_chart=dict(cut=str(self.cut),prefix_end=str(self.x[-1]),
                supplied_r_s=str(self.v),supplied_r_ss=str(self.acceleration),
                coefficients_role="Declared finite seam coordinate jets, not a claim that a finite Gauss profile differentiates to its returned ap",
                exact_patch_start=str(self.cut_start),exact_width=str(self.width)),
            native_full_mode_count=self.frequency_count,
            native_complete_FFT_nodes=[self.node_records[i] for i in sorted(self.node_records)],
            all_native_nodes_evaluated_and_bound=len(self.node_records) == len(self.radii),
            shared_background_payload_sha256=self.A.shared_background_geometry["exact_background_payload_sha256"],
            original_target_metric_background_sha256=self.A.shared_background_geometry["original_target_metric_background_sha256"],
            literal_reflection_trace_conditions=dict(
                prefix_z_at_zero_all_zero=all(exact(v)==0 for v in self.nodal[0][0,2*self.M+1:]),
                prefix_radial_xy_at_zero_all_zero=all(exact(v)==0 for v in self.nodal[1][0,:2*self.M+1]),
                prefix_second_radial_z_at_zero_all_zero=all(exact(v)==0 for v in self.nodal[2][0,2*self.M+1:]),
                role="Actual exact nodal conditions for R248.6; recorded, never substituted by a residual tolerance"),
            radial_pieces=[{k: str(v) if isinstance(v,F) else v for k,v in row.items()} for row in self.pieces],
            radial_order="Prefix ascending s; collar/native ascending r; both closed reflected sheets",
            normalized_physical_angle="q in [0,1], phi=2*pi*q; material Phi is a full circle diffeomorphism",
            complete_cut_correction_represented_without_theta_Fourier_projection=True,
            derivatives_are_of_this_exact_expression=True,
            floating_renderer_jet_labels_used_as_derivatives=False,
            sampled_renderer_error_envelope_certified=False,
            original_g_replaced_by_Bprime=False)


def vector_ball(vector, sqrt_upper, bits):
    intervals = [bounds(x) for x in vector]
    center = [(a+b)/2 for a,b in intervals]
    squared = sum((((b-a)/2)**2 for a,b in intervals),F(0))
    return list(map(str,center)), str(sqrt_upper(squared,bits)), [dict(lower=str(a),upper=str(b)) for a,b in intervals]


def certify_cell(field, piece, radial, angular, lower, sqrt_upper, bits, K):
    result = field.evaluate(piece,radial,angular,lower)
    jets = tuple(tuple(value.d[i] for value in result) for i in range(6))
    p, X, Y, XX, XY, YY = jets
    N = cross(X,Y)
    delta = dot(N,N)
    dlo,dhi = bounds(delta)
    record = dict(six_jets={name:[encode_interval(v) for v in value] for name,value in zip(JET_NAMES,jets)},
                  normal_numerator=[encode_interval(v) for v in N],
                  squared_cross_lower=str(dlo),squared_cross_upper=str(dhi),
                  normal_ball_certified=False,curvature_requested=K is not None)
    position,radius,position_box = vector_ball(p,sqrt_upper,bits)
    record.update(moving_position=position,moving_position_radius=radius,
                  position_interval_box=position_box)
    if dlo <= 0:
        record.update(reason="interval_cross_lower_not_positive_no_normal_ball_claimed")
        return record
    length = delta.sqrt()
    normal = tuple(v/length for v in N)
    center,eta,normal_box = vector_ball(normal,sqrt_upper,bits)
    record.update(normal_ball_certified=True,moving_normal_centre=center,moving_normal_radius=eta,
                  unit_normal_interval_box=normal_box,
                  normal_length_interval=encode_interval(length),
                  normal_orientation="Own parameter cross; R281 is invariant under its global sign",
                  center_is_not_required_to_be_unit=True,
                  reason="complete_unit_normal_normalization_enclosed_on_the_entire_closed_cell")
    if K is not None:
        E,B,C = dot(X,X),dot(X,Y),dot(Y,Y)
        h11,h12,h22 = dot(N,XX),dot(N,XY),dot(N,YY)
        T,D = C*h11-2*B*h12+E*h22,h11*h22-h12*h12
        kb = ball(K)
        ak = 2*kb*kb*delta**3-T*T+2*delta*D
        bk = kb**4*delta**4-kb*kb*delta*T*T+2*kb*kb*delta*delta*D+D*D
        al,_ = bounds(ak)
        bl,_ = bounds(bk)
        record["R279"] = dict(K=str(K),Gram={"E":encode_interval(E),"B":encode_interval(B),"C":encode_interval(C)},
            unnormalized_second_form=[encode_interval(v) for v in (h11,h12,h22)],
            T=encode_interval(T),D=encode_interval(D),A_K=encode_interval(ak),B_K=encode_interval(bk),
            strict_curvature_bound=(al > 0 and bl > 0),
            nonpositive_lower_bound_means_actual_curvature_failure=False)
    return record


def cell_specs(field, depth):
    division = 2**depth
    for lower in (False,True):
        for piece_index,piece in enumerate(field.pieces):
            a,b = piece["left"],piece["right"]
            for i in range(division):
                radial = (a+(b-a)*F(i,division),a+(b-a)*F(i+1,division))
                for j in range(division):
                    angular = (F(j,division),F(j+1,division))
                    yield dict(cell_id=f"{'lower' if lower else 'upper'}/{piece_index}/{i}/{j}",
                               lower=lower,piece_index=piece_index,radial_index=i,angular_index=j,
                               radial=radial,angular=angular,piece=piece)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("directory","source-directory","descriptor","checkpoint","port","config",
                 "tail-response","complete","source-topic","out"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--basename",default="surface")
    parser.add_argument("--source-basename",default="surface")
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--depth",type=int,required=True)
    parser.add_argument("--precision-bits",type=int,default=192)
    parser.add_argument("--sqrt-bits",type=int,default=128)
    parser.add_argument("--max-cells",type=int,default=1000000)
    parser.add_argument("--budget-seconds",type=int,default=3600)
    parser.add_argument("--curvature-upper",default=None)
    args = parser.parse_args()
    require_actions()
    if args.out.exists():
        raise FileExistsError("Preserve all earlier outputs")
    if not (0 <= args.depth <= 30 and 64 <= args.precision_bits <= 8192
            and 16 <= args.sqrt_bits <= 4096 and args.max_cells > 0 and args.budget_seconds > 0):
        raise ValueError("Invalid explicit resource parameters")
    K = None if args.curvature_upper is None else F(args.curvature_upper)
    if K is not None and K <= 0:
        raise ValueError("R279 requires the original proposed K to be positive")
    geometry,background,kernel,sources = initialise_runtime(args.code_directory)
    started = time.monotonic()
    old_precision = ctx.prec
    args.out.mkdir(parents=True)
    try:
        ctx.prec = args.precision_bits+args.depth
        bundle = geometry.load_shared_bundle(args)
        field = ExactFiniteField(bundle,background)
        planned = 2*len(field.pieces)*4**args.depth
        binding = dict(complete_field_binding=field.binding,
            shared_background_geometry=field.A.shared_background_geometry,
            shared_plan=receipt(field.paths["plan"]),shared_assembly=receipt(field.paths["assembly"]),
            original_input_receipts={name:receipt(getattr(args,name)) for name in
                ("descriptor","checkpoint","port","config","tail_response","complete")},
            source_pins=sources, source_sha256=sha_bytes(Path(__file__).read_bytes()),
            expression_schema=EXPRESSION,
            actual_accepted_parent_required_by_original_loader=True,
            global_family_definition="R248: R_alpha F_active(s,theta-alpha), with both marked graph caps pointwise fixed",
            image_family_definition="R_alpha A union C; one common original z axis; active-active pairs rotate together",
            common_rotation_axis_xy=["0","0"],
            no_rigid_rotation_of_one_end_of_an_old_static_base_pair=True,
            no_new_fit_or_target_metric_or_native_acceptance=True)
        (args.out/"input-binding.json").write_bytes(canonical(binding))
        stream_path = args.out/"active-cells.jsonl.gz"
        count = normals = curvatures = 0
        failure = None
        with stream_path.open("xb") as raw_stream:
            with gzip.GzipFile(filename="",mode="wb",fileobj=raw_stream,mtime=0) as stream:
                for spec in cell_specs(field,args.depth):
                    if count >= args.max_cells or time.monotonic()-started >= args.budget_seconds:
                        failure = "cell_or_time_resource_budget_before_next_complete_cell"
                        break
                    row = dict(schema=CELL_SCHEMA,cell_id=spec["cell_id"],ordinal=count,
                        sheet="lower" if spec["lower"] else "upper",phase_motion="active_R248_image_rotation",
                        piece_index=spec["piece_index"],piece_kind=spec["piece"]["kind"],
                        radial_subdivision=spec["radial_index"],angular_subdivision=spec["angular_index"],
                        closed_radial_interval=list(map(str,spec["radial"])),
                        closed_normalized_physical_angle_interval=list(map(str,spec["angular"])),
                        normal_ball_certified=False,ball_evaluation_exception=None)
                    try:
                        row.update(certify_cell(field,spec["piece"],spec["radial"],spec["angular"],
                            spec["lower"],kernel.sqrt_upper,args.sqrt_bits+args.depth,K))
                    except (ArithmeticError,ValueError) as error:
                        row["ball_evaluation_exception"] = dict(type=type(error).__name__,message=str(error))
                    normals += int(row["normal_ball_certified"])
                    curvatures += int(row.get("R279",{}).get("strict_curvature_bound",False))
                    stream.write(canonical(row))
                    count += 1
        expression = field.expression_identity()
        (args.out/"exact-field-expression.json").write_bytes(canonical(expression))
        completed = count == planned
        result = dict(schema=SCHEMA,completed=completed,source_sha256=binding["source_sha256"],
            input_binding=receipt(args.out/"input-binding.json"),
            expression=receipt(args.out/"exact-field-expression.json"),
            active_cells=receipt(stream_path),
            parameters=dict(depth=args.depth,precision_bits=args.precision_bits,
                effective_precision_bits=args.precision_bits+args.depth,sqrt_bits=args.sqrt_bits,
                effective_sqrt_bits=args.sqrt_bits+args.depth,max_cells=args.max_cells,
                budget_seconds=args.budget_seconds,curvature_upper=None if K is None else str(K)),
            complete_partition_rule="Both sheets x every exact radial piece x all closed dyadic radial and normalized-physical-angle cells",
            planned_closed_cells=planned,exported_closed_cells=count,
            normal_ball_certified_cells=normals,normal_ball_unresolved_cells=count-normals,
            unvisited_cell_ordinals=None if completed else [count,planned],
            complete_active_position_and_unit_normal_balls=(completed and normals == planned),
            R279_strict_curvature_certified_for_active_cells=(K is not None and completed and curvatures == planned),
            full_surface_curvature_certified=False,
            all_radial_interfaces_and_angle_endpoints_included=True,
            shared_boundaries_deliberately_covered_more_than_once=True,
            resource_failure=failure,elapsed_seconds=time.monotonic()-started,
            original_R241_R24_route_unchanged=True,
            seam_C2_responsibility="R249 and shared-node/collar/cut normal-form identities; not numerical mesh coincidence",
            seam_local_pair_responsibility_paid=False,
            marked_mixed_pairs_evaluated=False,full_surface_certified=False,actual_reach_certified=False,
            same_g_refinement_or_metric_error_certified=False,held_or_delta_E_certified=False,
            task_completed=False)
        raw = canonical(result)
        (args.out/"result.json").write_bytes(raw)
        print(json.dumps(dict(event="actual_shared_active_interval_ball_component",
            completed=completed,exported_closed_cells=count,planned_closed_cells=planned,
            normal_ball_certified_cells=normals,result_sha256=sha_bytes(raw),result_bytes=len(raw),
            source_sha256=result["source_sha256"],full_surface_certified=False,actual_reach_certified=False),
            sort_keys=True,separators=(",",":")),flush=True)
    finally:
        ctx.prec = old_precision


if __name__ == "__main__":
    main()
