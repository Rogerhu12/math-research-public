#!/usr/bin/env python3
"""Paid R576 knot state plus a genuine body-forced j4 direction.

Scientific execution only in the declared public Actions run. The new source
is explicitly cut off on r<=.30; its omitted quadratic tail stays in the full
nonlinear residual. No new inner Riccati or background shooting is performed.
"""
import argparse
from dataclasses import asdict, replace
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import BSpline

HERE = Path(__file__).resolve().parent
KNOT_FILE = "r576_exact_knot_height_continuation_20261126.py"
KNOT_SHA = "28ab4e379e1a1dddb6dd10ee64b795bb9810c1cc72a9b39b092ae6f142d923d3"
SOURCE_RUN, SOURCE_JOB = 45804732428, 139856848406
SOURCE_COMMIT = "a76c263734cdfb02ce66c9b92f46527e68f914ae"
SOURCE_LOG_SHA = "aa07a9a98ca2c28e309ba94ab1b203c7382f4c8b1da95b8a0038ae1ff20aa885"
SOURCE_FINAL_SHA = "3e9dbcd41d52e269f875bf45baedf57bf6f7d380e39037b4e999274aa447e1e4"
SOURCE_Q_SHA = "7d6c399a8a025432e0e5781e0a6699430f69702c4aead41ed2c9eba5c0e47647"
PAID_ACTIVE_ETA = 2.746802948926504e-7
PAID_FINE_ETA = 2.7468029489506276e-7
SCHEMA = "r576-paid-knot-body-forced-j4-v1"
RAW_Q_JSON = "[0.5188895813736972,-2.2075995237180782e-05,-1.5267712604885981e-06,5.789317579121834e-08,2748669733.8110266,-409573509.3377591,694822.8136088056,-91473.89971539752,5945.911445604788,1227.4953273733563,1823.051202246067,1602.6802607546654,713.9711016200372,1300.7157487154632,388.4964900996658,162.31373501213616,25.709123252155262,3.8915441719883614,1.3414963528852724,0.6520496350594263,0.45281313373845034,0.3515508738574568,0.2893111684869183,0.21236270649728897,0.07699473320510393,-0.2585715821030442,-0.7294360825543696,-1.326368978706162,-1.921462829851927,-2.498688253245305,-2.9000676612053287,-3.03794464601775,-2.9106649005547753,-2.68209825678446,-2.3054695020848848,0.2832994774257502,0.0017850464787336295,-0.0004743821207915702,-0.00034799544649875987,-0.00036983007114096294,-0.0003470089804089119,-0.0003298030680119044,-0.0003230089772229521,-0.00031740710503546483,-0.0002916580733912041,-0.00026971063405645664,-0.00023603057710193701,-0.00018686264689580557,-0.00014056722922494027,-0.00010718065483439611,-7.89237355911439e-05,-8.00735640554197e-05,-0.00013255442447802305,-0.00017996339281724387,-0.00011181372386362711,-4.726037479759882e-05,-5.1976817528432956e-05,-4.838447967502625e-05,-5.496527011971741e-05,-9.240976132972656e-05,-0.00018945598362532463,-0.0003024576367563503,-0.000788817342631924,-0.0018516575377102201,-0.00515618102613538,5.674808995901768e-05,6.873416525799587e-06,-7.767573262085307e-05,-9.904852207079505e-05,8901093.765861537,-841933.1435818012,16434.14101264771,-3327.7073680381645,1305.6234540553794,-601.3024582862369,-38.23971458142047,-655.5431859472415,-3.3531111054684866,-6.747316042498436,8.315389554456486,-20.333039166094,44.725092688427225,11.292662680857509,5.0037638767475245,3.131798158405744,2.615327835243938,2.3238195276950897,1.9862672905001229,1.298564902618202,0.09338543407714277,-1.3441155172750696,-2.5189526737534162,-3.518779352367397,-4.2581351046459535,-4.779059796238803,-5.061611799626869,-5.160108255409763,-5.110739412473352,-5.01765015074295,-4.7689951160970265,-2.6951628312681564,-0.011250275027720042,0.017325071368077257,0.03353730146280509,0.05805965897531008,0.06230365877656969,0.06323275350607092,0.05863862123522939,0.049918518902220405,0.03550913718419967,0.0282518500129671,0.021834969413025578,0.015833262753086066,0.010905967048224661,0.0075286005092915905,0.004629937695261924,0.0039242186360539414,0.005920300411141057,0.009326105934383582,0.010136550774504172,0.010537157716932245,0.011944849952535232,0.01392670075359353,0.017747891594575165,0.04017870818947615,0.08720840276611333,0.205560675209069,0.24822541502059495,1.1551297556409352,3.0828139026614916,-0.0007587732962437023,-0.00035687662922427365,0.0010235273463705906,0.0008050075206578072,2611074633.474756,258422453.1718903,-696338.3793292533,72048.33765065573,-15293.403397524236,6646.831689402931,5102.101088136854,10214.871263408155,2384.7084821003964,190.2554963594744,137.4509937453445,-39.65661985039456,-9.402883585691175,-2.2226117305265016,-1.321886885783493,-0.9771307543904945,-0.9947201219916219,-0.9355053518632068,-0.6123264353633703,0.1738451039328784,1.4081954868749795,2.6656225851304938,3.5940285165675125,4.329324628510337,4.864759167542252,5.281567790729141,5.454706091959394,5.363727362834284,5.039219766430859,4.607267059393232,4.212111928335905,2.1897884312371794,0.0026878475773706753,-0.0001003378243004179,3.5745118591227066e-05,-4.972052967137671e-05,-5.9271957940455084e-05,-6.901997971181802e-05,-4.916290574212199e-05,-2.2346374231156994e-05,8.498827960145442e-05,0.00013864480745325768,0.00039067861708506674,0.0008075552056763159,0.0011375019908459382,0.001331588340544883,0.0014362215910173474,0.0013331225970174756,0.001095104107105713,0.0009867458848868541,0.0010750862218981809,0.0012133620756228044,0.0013189003882719571,0.0014855288258520333,0.0017415379066857935,0.003059742411066688,0.004998520375963684,0.009558829574119633,0.008109253087065735,0.04196789437204105,0.11295797514077703,4.3938382494726225e-05,1.153647593509551e-05,-7.15046599209909e-05,-0.00015117383308462383,-53579.22244608366,-1964388.060232356,50705.30043717558,-10698.89240456403,4277.887317710267,-1991.625641974053,-58.2090581918435,648.6784658163111,142.22685558086192,16.966719113368814,36.28324494313461,60.27632183523643,-0.6869959879748275,-0.18694180205360195,-0.42711757073709133,-0.40574405290498133,-0.5591258274016148,-0.5657065354510606,-0.23179898589888598,0.5162049314029821,1.4500506773917834,2.3931662918203975,3.246731399216654,4.037334962742768,4.714787316200676,5.313256592667463,5.704929406541211,5.879293698889139,5.908757004338406,5.828752138238745,5.66116856944301,4.189076017785426,-0.012956422868179048,0.0047764758092213614,-0.001482237641342587,0.0007862236627886894,0.0006319960471057537,0.0008619332460282083,0.0004886005745736289,-4.95177241430405e-05,-0.0007249045656599642,-0.0009984711443110097,-0.001310766239206371,-0.0016029735925966939,-0.001740746829020699,-0.0017612940793670976,-0.0016670012224107396,-0.0014225558038768857,-0.001134227992079295,-0.0009380312579612286,-0.0007318533423342059,-0.0005409053785157145,-0.0005462961065140688,-0.0005567965887292561,-0.0006049881957387309,-0.0008601173086586092,-0.0010413976015693398,-0.0015602935471732754,-0.0008983691735493488,-0.005022899447507673,-0.012903971135146908,0.00020459435066340044,0.0001618441519947218,-0.00016143265573337936,-3.1796907156823894e-05]"
RAW_KNOT_JSON = "[0.22,0.22,0.22,0.22,0.22,0.22,0.235,0.239375,0.24375,0.24812499999999998,0.2503125,0.2525,0.25468749999999996,0.25687499999999996,0.26125,0.27,0.28750000000000003,0.29625,0.30500000000000005,0.30937500000000007,0.31375000000000003,0.318125,0.3225,0.3246875,0.326875,0.32796875000000003,0.32906250000000004,0.33015625000000004,0.33125000000000004,0.33234375000000005,0.33343750000000005,0.33453125000000006,0.33562500000000006,0.33781250000000007,0.3389062500000001,0.34,0.375,0.41000000000000003,0.48,0.4975,0.515,0.55,0.555,0.56,0.565,0.57,0.5725,0.57375,0.575,0.5774999999999999,0.58,0.585,0.59,0.6,0.61,0.62,0.63,0.635,0.64,0.65,0.78,0.85,0.85,0.85,0.85,0.85,0.85]"

def import_knot():
    path = HERE / KNOT_FILE
    if hashlib.sha256(path.read_bytes()).hexdigest() != KNOT_SHA:
        raise RuntimeError("paid knot source binding changed")
    spec = importlib.util.spec_from_file_location("r576_forced_paid_knot", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

knot = import_knot()
parent, base = knot.parent, knot.base
emit = base.emit
NEW_COUNTS = {"forced_source_values": 0, "forced_connector_RHS": 0,
              "forced_core_RHS": 0, "forced_basis_points": 0}

class ScientificBudget(Exception):
    pass

class BodyForcedFour:
    """L_4 G=chi*S4, with the paid flat j4 tail and a zero C core trace.

    A=(16 W G-r W G')/15. With D=A-WG,
    A'=(A-16D)/r-S/15, D'=-(W'/W)(A-D)-S/15.
    The two columns are the paid homogeneous field and the zero-mouth
    particular field. The actual C_core coefficient solves the boundary row.
    """
    def __init__(self, flat4, Fmode, profile, args, deadline):
        self.flat, self.Fmode, self.par = flat4, Fmode, profile
        self.args, self.deadline = args, deadline
        self.mu = 16
        self.cut_left, self.cut_right = .55, .65
        self.source_left, self.source_right = .30, .31
        self.scale = 1.
        w0 = float(base.radial_slope(profile, base.R0)[0])
        A0, C0 = flat4.outer[4], flat4.outer[0]

        def rhs(r, y):
            self.check()
            NEW_COUNTS["forced_connector_RHS"] += 1
            w, wr = (float(v) for v in base.radial_slope(profile, r))
            A, D = y.reshape(2, 2)
            forcing = np.array([0., self.source_r(float(r)) / (self.mu-1)])
            return np.r_[(A-self.mu*D)/r-forcing,
                         -wr/w*(A-D)-forcing]

        initial = np.array([A0, 0., A0-w0*C0, 0.])
        self.forward = solve_ivp(rhs, (base.R0, profile.switch_radius), initial,
            method="DOP853", rtol=args.rtol, atol=args.atol,
            max_step=.0015, dense_output=True)
        if not self.forward.success:
            raise ArithmeticError(self.forward.message)
        self.xsw = float(profile.x_of_r(profile.switch_radius))
        wsw = float(base.radial_slope(profile, profile.switch_radius)[0])
        Asw, Dsw = self.forward.y[:, -1].reshape(2, 2)
        core_initial = np.r_[Asw, (Asw-Dsw)/wsw]

        def rhs_x_columns(x, y):
            self.check()
            NEW_COUNTS["forced_core_RHS"] += 1
            a, ax, _, zx, _ = (float(v) for v in base.spatial_jets(profile, x))
            A, C = y.reshape(2, 2)
            source = np.array([0., self.source_x(float(x))])
            unforced_Ax = -(self.mu-1)*ax/a*A-self.mu*zx/a*C
            Ax = unforced_Ax-source*ax/(self.mu-1)
            Cx = -ax/zx*unforced_Ax
            return np.r_[Ax, Cx]

        self.raw_core = solve_ivp(rhs_x_columns, (self.xsw, 0.), core_initial,
            method="DOP853", rtol=args.rtol, atol=args.atol,
            max_step=.004, dense_output=True)
        if not self.raw_core.success:
            raise ArithmeticError(self.raw_core.message)
        Ac, Cc = self.raw_core.y[:, -1].reshape(2, 2)
        self.raw_core_A, self.raw_core_C = Ac.copy(), Cc.copy()
        if abs(Cc[0]) <= 1e-10 * max(1e-100, np.hypot(Ac[0], Cc[0])):
            raise ArithmeticError("paid-mouth j4 core nonresonance too small in this declared numerical input")
        self.tail_multiplier = float(-Cc[1]/Cc[0])
        self.Acore = float(Ac[1]+self.tail_multiplier*Ac[0])
        self.raw_Ccore_after_combination = float(Cc[1]+self.tail_multiplier*Cc[0])

        def rhs_x_back(x, y):
            self.check()
            NEW_COUNTS["forced_core_RHS"] += 1
            a, ax, _, zx, _ = (float(v) for v in base.spatial_jets(profile, x))
            A, C = y
            unforced_Ax = -(self.mu-1)*ax/a*A-self.mu*zx/a*C
            return [unforced_Ax-self.source_x(float(x))*ax/(self.mu-1),
                    -ax/zx*unforced_Ax]

        self.core_back = solve_ivp(rhs_x_back, (0., float(profile.x_of_r(self.cut_left))),
            [self.Acore, 0.], method="DOP853", rtol=args.rtol, atol=args.atol,
            max_step=.003, dense_output=True)
        if not self.core_back.success:
            raise ArithmeticError(self.core_back.message)
        actual_switch = np.array([Asw[1]+self.tail_multiplier*Asw[0],
            (Asw[1]-Dsw[1]+self.tail_multiplier*(Asw[0]-Dsw[0]))/wsw])
        self.backward_switch_difference = (self.core_back.sol(self.xsw)-actual_switch).tolist()

    def check(self):
        if time.monotonic() >= self.deadline:
            raise ScientificBudget("forced j4 construction reached its declared scientific clock")

    def _source(self, r, F, Fr, Frr, w, wr):
        mu = 4.
        e0 = 1+w*w
        qc = (r*Fr-mu*e0*F)*Frr+mu*w*wr*F*Fr
        qs = -mu*e0*(Fr-F/r)**2+mu*w*wr*F*F/r
        return float((qc-qs)/2)

    def source_r(self, r):
        NEW_COUNTS["forced_source_values"] += 1
        if r <= self.source_left:
            return 0.
        if r >= self.cut_right:
            return self.source_x(float(self.par.x_of_r(r)))
        F, Fr, Frr = self.Fmode.evaluate(np.array([r]))[0]
        w, wr = (float(v) for v in base.radial_slope(self.par, r))
        chi = float(base.step2(np.asarray((r-self.source_left)/
                            (self.source_right-self.source_left)))[0])
        return chi*self._source(r, F, Fr, Frr, w, wr)

    def source_x(self, x):
        # The reference mode and the new frozen W have identical core geometry
        # on r>=.65. Evaluate via regular x to avoid rounding r to R in W.
        NEW_COUNTS["forced_source_values"] += 1
        if x == 0:
            mu, alpha, radius = 4., self.par.alpha, self.par.R
            return mu*(mu-1)**2*(1-alpha)/(2*radius*radius*(1+alpha))
        r, rx, rxx, zx, zxx = (float(v) for v in base.spatial_jets(self.par, x))
        if r < self.cut_right:
            return self.source_r(r)
        pair = self.Fmode.core_pair.sol(x).reshape(2, 2)
        A, F = float(pair[0, 0]), float(pair[1, 0])
        w = -zx/rx
        wr = (-zxx*rx+zx*rxx)/(rx**3)
        Fr = 4*F/r-3*A/(r*w)
        Frr = 3*wr*A/(r*w*w)
        return self._source(r, F, Fr, Frr, w, wr)

    def AC_jets(self, r, A, C):
        w, wr = base.radial_slope(self.par, r)
        source = np.array([self.source_r(float(t)) for t in r])
        Cr = self.mu*C/r-(self.mu-1)*A/(r*w)
        Crr = (self.mu-1)*wr*A/(r*w*w)+source/(r*w)
        return np.stack([C, Cr, Crr], axis=1)

    def evaluate(self, r):
        self.check()
        r = np.asarray(r, dtype=float)
        NEW_COUNTS["forced_basis_points"] += int(r.size)
        result = np.zeros((r.size, 3))
        tail = r <= base.R0
        if np.any(tail):
            result[tail] = self.tail_multiplier*self.flat.evaluate(r[tail])
        body = (r > base.R0) & (r < self.cut_right)
        if np.any(body):
            rb = r[body]
            both = self.forward.sol(rb).reshape(2, 2, -1)
            A = both[0, 1]+self.tail_multiplier*both[0, 0]
            D = both[1, 1]+self.tail_multiplier*both[1, 0]
            w = base.radial_slope(self.par, rb)[0]
            C = (A-D)/w
            values = self.AC_jets(rb, A, C)
            active = rb > self.cut_left
            if np.any(active):
                ra = rb[active]
                Ab, Cb = self.core_back.sol(self.par.x_of_r(ra))
                admissible = self.AC_jets(ra, Ab, Cb)
                raw = values[active].copy()
                chi, chir, chirr = base.step2((ra-self.cut_left)/(self.cut_right-self.cut_left))
                chir /= self.cut_right-self.cut_left
                chirr /= (self.cut_right-self.cut_left)**2
                delta = admissible-raw
                values[active, 0] += chi*delta[:, 0]
                values[active, 1] += chi*delta[:, 1]+chir*delta[:, 0]
                values[active, 2] += chi*delta[:, 2]+2*chir*delta[:, 1]+chirr*delta[:, 0]
            result[body] = values
        core = r >= self.cut_right
        if np.any(core):
            rr = r[core]
            A, C = self.core_back.sol(self.par.x_of_r(rr))
            result[core] = self.AC_jets(rr, A, C)
        return result/self.scale

    def receipt(self, r):
        fields = self.evaluate(r)
        w, _ = base.radial_slope(self.par, r)
        e0 = 1+w*w
        quantities = np.stack([abs(fields[:, 0]), abs(fields[:, 1])/np.sqrt(e0),
            abs(fields[:, 2])/e0, 4*abs(fields[:, 0])/r,
            16*abs(fields[:, 0])/(r*r),
            4*abs(fields[:, 1])/(r*np.sqrt(e0))], axis=1)
        peaks = []
        for j in range(6):
            i = int(np.argmax(quantities[:, j]))
            peaks.append({"maximum": float(quantities[i, j]), "r": float(r[i])})
        return {"mode": 4, "mu": 16, "frozen_force_background_H": self.par.gain_height,
            "source_cutoff": [self.source_left, self.source_right],
            "source_equation": "r*(W*G')'-16*W'*G=chi*(Qc-Qs)/2",
            "unforced_tail_is_the_paid_true_flat_j4_kernel": True,
            "omitted_tail_source_stays_in_complete_nonlinear_residual": True,
            "raw_homogeneous_and_particular_core_A": self.raw_core_A.tolist(),
            "raw_homogeneous_and_particular_core_C": self.raw_core_C.tolist(),
            "tail_multiplier_before_height_normalization": self.tail_multiplier,
            "core_A": self.Acore, "raw_combined_C_core": self.raw_Ccore_after_combination,
            "backward_switch_A_C_difference": self.backward_switch_difference,
            "explicit_two_jet_matching_support": [self.cut_left, self.cut_right],
            "core_C_after_explicit_matching": 0.,
            "core_W_G_r": -15*self.Acore/self.par.R/self.scale,
            "positive_height_normalization": self.scale,
            "height_and_scaled_C2_peaks": peaks,
            "finite_ODE_error_or_exact_core_root_certificate": False}

class ForcedHeightDesign(parent.LocalHeightDesign):
    def prepare(self, r, ntheta):
        data = super().prepare(r, ntheta)
        if "forced_j4" not in data:
            data["forced_j4"] = self.forced.evaluate(data["r"])
            data["forced_cos4"] = np.cos(4*data["theta"])
            data["forced_sin4"] = np.sin(4*data["theta"])
        return data

    def height_jets(self, q, amplitude, data):
        old = super().height_jets(q[:self.original_nq], amplitude, data)
        c = amplitude*amplitude*q[self.original_nq]
        G, Gr, Grr = data["forced_j4"].T
        co, si = data["forced_cos4"], data["forced_sin4"]
        add = (G[:, None]*co, Gr[:, None]*co, Grr[:, None]*co,
               -4*G[:, None]*si, -16*G[:, None]*co, -4*Gr[:, None]*si)
        return tuple(a+c*b for a, b in zip(old, add))

def restore_paid_model(args):
    if hashlib.sha256(RAW_Q_JSON.encode()).hexdigest() != SOURCE_Q_SHA:
        raise RuntimeError("actual paid 264-q payload changed")
    q = np.asarray(json.loads(RAW_Q_JSON), dtype=float)
    knots = np.asarray(json.loads(RAW_KNOT_JSON), dtype=float)
    if q.size != 264 or knots.size != 67:
        raise RuntimeError("actual paid q/knot dimension changed")
    profile = base.gain.Profile(R=.85, log_suppression=6., core_scale=.5,
                                gain_height=parent.PAID_REFERENCE_H)
    flats = [parent.PaidFlatSeed(j, args) for j in base.MODES]
    modes = [base.AdmissibleMode(f, profile, args) for f in flats]
    original = base.HeightDesign(profile, modes, knots[6:-6], args)
    model, _ = parent.enrich_same_state(original, np.zeros(original.nq))
    if model.nq != q.size or not np.array_equal(model.bs.t, knots):
        raise RuntimeError("actual paid basis reconstruction changed")
    return model, q, flats

def residual_harmonics(model, q, amplitude, data):
    g = model.geometry(q, amplitude, data, details=True)
    r = data["r"][:, None]
    # R=weight*D; use the actual nonlinear Darboux numerator D.
    weight = r*r/(g["u"]**3*g["b"]**3)
    D = g["R"]/weight
    output = []
    for j in (0, 2, 4, 6, 8, 10, 12, 16):
        coefficient = np.mean(D*np.cos(j*data["theta"])[None, :], axis=1)*(1 if j==0 else 2)
        at = int(np.argmax(abs(coefficient)))
        output.append({"mode": j, "maximum_absolute_D_coefficient": float(abs(coefficient[at])),
                       "signed_coefficient_at_attainer": float(coefficient[at]),
                       "r": float(data["r"][at])})
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-seconds", type=float, default=2400.)
    parser.add_argument("--M", type=int, choices=[25], default=25)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--iterations", type=int, default=90)
    parser.add_argument("--theta-nodes", type=int, choices=[64], default=64)
    parser.add_argument("--target-eta", type=float, default=2e-9)
    parser.add_argument("--height-saturation", type=float, choices=[.15], default=.15)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("new science executes only in the declared public Actions run")
    if not 60 < args.maximum_seconds <= 2400 or args.iterations < 1:
        raise ValueError("outside declared forced-height scope")
    started = time.monotonic()
    deadline = started+args.maximum_seconds
    stages, final_status = [], "not_started"
    model = None
    q = None
    active_amplitude = 1e-5
    emit("HEIGHT_FORCED_DEFINITION", {"schema": SCHEMA, "arguments": vars(args),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "paid_run": SOURCE_RUN, "paid_job": SOURCE_JOB, "paid_commit": SOURCE_COMMIT,
        "paid_log_sha256": SOURCE_LOG_SHA, "paid_final_sha256": SOURCE_FINAL_SHA,
        "paid_q_sha256": SOURCE_Q_SHA, "paid_knot_count": 67,
        "new_direction": "post-tanh body-forced j4 with exactly zero initial coefficient",
        "source_tail_cutoff": [.30, .31], "old_inner_Riccati_repeated": False,
        "old_H_shooting_repeated": False, "same_metric_refinement_claim": False})
    try:
        old, oldq, flats = restore_paid_model(args)
        model, q = old, oldq
        r = knot.radial_grid(old, 1)
        data = old.prepare(r, args.theta_nodes)
        baseline = knot.compact_report(oldq, 1e-5, data, old.geometry(oldq, 1e-5, data, details=True))
        baseline["actual_q"] = knot.q_identity(oldq)
        baseline["eta_difference"] = baseline["eta_max"]-PAID_ACTIVE_ETA
        emit("HEIGHT_FORCED_PAID_BASELINE", baseline)
        if abs(baseline["eta_difference"]) > max(1e-11, 1e-5*PAID_ACTIVE_ETA):
            raise ArithmeticError("paid 264-q height identity changed")
        emit("HEIGHT_FORCED_PAID_HARMONICS", residual_harmonics(old, oldq, 1e-5, data))
        force_profile = replace(old.par, gain_height=float(oldq[0]))
        forced = BodyForcedFour(flats[1], old.modes[0], force_profile, args, deadline)
        raw_values = forced.evaluate(r)
        forced.scale = max(1., float(np.max(abs(raw_values[:, 0]))))
        model = ForcedHeightDesign.__new__(ForcedHeightDesign)
        model.__dict__.update(old.__dict__)
        model.cache = {}
        model.forced = forced
        model.original_nq = old.nq
        model.nq = old.nq+1
        q = np.r_[oldq, 0.]
        knot.mapping_observation(old, oldq, model, q, 1e-5, r, args.theta_nodes)
        emit("HEIGHT_FORCED_BASIS", forced.receipt(r))
        density, angular = 1, args.theta_nodes
        data = model.prepare(r, angular)
        amplitudes = [1e-5, 3e-5, 1e-4, 3e-4, .001, .003, .01, .03, .1, .2]
        final_status = "declared_amplitude_list_complete"
        for amplitude in amplitudes:
            active_amplitude = amplitude
            exchanges = []
            while True:
                q, status, history = knot.solve_stage(model, q, amplitude, data, args, deadline)
                observation, fine_data, _ = knot.assess(model, q, amplitude, data, density, args)
                exchange = {"status": status, "iterations": len(history),
                            "actual_q_identity": knot.q_identity(q), **observation}
                exchanges.append(exchange)
                emit("HEIGHT_FORCED_EXCHANGE", exchange)
                if status == "sampled_metric_target" and observation["fine_observation_passed"]:
                    break
                if status == "sampled_metric_target" and density < 2:
                    density *= 2
                    angular *= 2
                    data = fine_data
                    emit("HEIGHT_FORCED_GRID_PROMOTION", {"density": density,
                        "theta_nodes": angular, "same_q": knot.q_identity(q)})
                    continue
                break
            stage = {"amplitude": amplitude, "status": status,
                "actual_retained_q": q.tolist(), "actual_q_identity": knot.q_identity(q),
                "metric_observation_accepted_at_this_amplitude":
                    status == "sampled_metric_target" and observation["fine_observation_passed"],
                "actual_spline_knot_vector": model.bs.t.tolist(),
                "actual_local_extra_count": 4, "actual_forced_directions": 1,
                "actual_effective_flat_j4_multiplier": float(
                    amplitude*amplitude*q[model.original_nq]*forced.tail_multiplier/forced.scale),
                "actual_residual_harmonics": residual_harmonics(model, q, amplitude, data),
                "exchanges": exchanges}
            stages.append(stage)
            emit("HEIGHT_FORCED_STAGE", stage)
            if not stage["metric_observation_accepted_at_this_amplitude"]:
                final_status = status
                break
    except Exception as error:
        final_status = "construction_or_actual_domain_failure"
        emit("HEIGHT_FORCED_FAILURE", {"type": type(error).__name__, "message": str(error),
            "actual_amplitude": active_amplitude,
            "actual_retained_q": None if q is None else q.tolist(),
            "actual_q_identity": None if q is None else knot.q_identity(q),
            "actual_knot_vector": None if model is None else model.bs.t.tolist()})
    final = {"schema": SCHEMA, "status": final_status, "stages": stages,
        "actual_amplitude": active_amplitude,
        "actual_retained_q": None if q is None else q.tolist(),
        "actual_q_identity": None if q is None else knot.q_identity(q),
        "actual_knot_vector": None if model is None else model.bs.t.tolist(),
        "elapsed_seconds": time.monotonic()-started, "new_counts": NEW_COUNTS,
        "solver_counts": knot.COUNTS, "rejection_reasons": knot.REJECTIONS,
        "base_counts": dict(base.COUNTS), "function_trial_counts": dict(parent.EXTRA),
        "gain_import_counts": dict(base.gain.COUNTS),
        "old_inner_Riccati_repeated": False, "old_gain_shooting_repeated": False,
        "accurate_infinite_forced_tail_claim": False,
        "source_cutoff_residual_was_omitted": False,
        "finite_ODE_error_certificate": False,
        "same_metric_refinement_or_README_completion_claim": False,
        "raw_arrays_tables_artifacts_releases_or_git_writes": False}
    emit("HEIGHT_FORCED_FINAL", final)
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("HEIGHT_FORCED_FINAL_IDENTITY", {"JSON_bytes": len(raw),
                                        "sha256": hashlib.sha256(raw).hexdigest()})

if __name__ == "__main__":
    main()
