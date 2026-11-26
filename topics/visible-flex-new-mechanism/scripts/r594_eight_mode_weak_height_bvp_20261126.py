#!/usr/bin/env python3
"""Complete weak angular BVP about the whole paid R576 height.

This is a finite radial collocation of the exact R594 weak equations,
with genuine mode-specific flat ends and the R597 finite core trace.
It preserves the paid pre-tanh field and the paid post-tanh forced term.
No pointwise division by the possibly sign-changing acceleration
coefficient is performed. Science belongs only to the declared public job.
"""
import argparse
from dataclasses import replace
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
PAID_FILE = "r576_body_forced_j4_height_20261126.py"
PAID_SHA = "5ae3884c3a877a87a933b82a66aeb2e4d861a3883a9b4bf31f67bc48bb49908c"
SCHEMA = "r594-paid-full-height-eight-mode-weak-BVP-v1"
SOURCE_COMMIT = "f96716859c81870ba1e6466018d3c436f9f9efad"
SOURCE_RUN, SOURCE_JOB = 45813421528, 139886872647
SOURCE_LOG_SHA = "7bf33880b3071344907b4dfc7629444aef92bb1a2088957637c3c1ef49b20d8c"
SOURCE_FINAL_SHA = "4235164d7bf44d9bc42986beb81ba73bee80450048fbe1bffb6ec5a985fd5fdd"
SOURCE_Q_SHA = "242afcd609b5a9f3ff9480689d296dfdc3171c51f46d1c35f6b1875c9959cab6"
SOURCE_KNOT_SHA = "9e3ce07c7d55f46135c31b86f45bddec557495c2f6648ef4b723b53637fb3e15"
RAW_Q_JSON = r"""[0.5188907586810884,-1.2881449262822639e-05,-9.121551964035835e-07,6.502943823871695e-08,2877834239.4424744,-410350855.4329968,692447.9358298166,-90707.30941907236,5711.353653937934,1211.1202638806574,1770.1288174223082,1602.277738108328,709.6622631109315,1305.8198466042195,381.73869429328045,146.57918623367001,23.817626366372405,3.6436589912880817,1.2600945270514343,0.6147991760970372,0.4276732406236924,0.33288059206117354,0.27534588362938056,0.20524933211442145,0.08099621054264197,-0.24469755354602465,-0.7096770309000233,-1.3027540318708977,-1.8957887023359,-2.473158845637858,-2.8742017656211805,-3.0055535747078097,-2.867584746813288,-2.6396171884292365,-2.248970263582652,0.05469574073442159,0.0009941710399716981,-0.0005402843124594985,-0.00034782046929962665,-0.00035466719868199764,-0.0003201488320993073,-0.00030113889996304094,-0.00029192483935023417,-0.0002846081636373043,-0.0002522522988108859,-0.00022693188623538668,-0.00018942820636842124,-0.00013944026187978235,-9.643269186729401e-05,-6.779632467134631e-05,-4.7223699280218635e-05,-5.761048943627423e-05,-0.0001177818667464418,-0.00016854890228991252,-0.00010201551098870566,-3.755239943009007e-05,-4.166636546168967e-05,-3.6502631840380564e-05,-3.973488376665437e-05,-5.63546038455176e-05,-0.00010426964817546943,-7.966673132117874e-05,-0.0004915256380529084,-0.0005122068617741788,-0.0017751993021087667,5.584092420780231e-05,7.63442451161477e-06,-7.681352922513381e-05,-0.00010066587121019775,10518103.002637949,-1743900.4484142791,20182.76255741579,-3851.203974985702,1477.7361766900867,-688.7852227693439,-79.99235429278976,-744.3845670503862,-20.515494417162166,-11.62083216583909,4.509101500845025,-13.501924130142148,20.41133276546094,5.42517423688504,2.4213770984303418,1.5298168297650023,1.2816438817428977,1.1433981549101566,0.9848410761004389,0.6629141814798075,0.10372261494336961,-0.515316601790395,-0.9985627729599749,-1.414099048658918,-1.744671292777742,-2.0070405117627708,-2.207578510503326,-2.365845681799487,-2.477725102394402,-2.571410844181445,-2.462673212381347,-1.4677958195169711,-0.005479192609159849,0.010165383700499289,0.020200639344797544,0.03485642991898092,0.03741368907363001,0.03796576581598383,0.03520864989263178,0.029970526006759556,0.021319088040760194,0.016961773020248132,0.01310572844824422,0.009496370137578796,0.006533305937359982,0.004502743540938239,0.002760817366400422,0.002338264970284871,0.0035394272242943335,0.00558389227683302,0.006066420111675243,0.006301574472794279,0.007141579986031576,0.008325102068469961,0.010609837805266737,0.02402784297003923,0.052158703840765326,0.12298406770298777,0.14844694711206388,0.691129813387368,1.8444088928189326,-0.00045758934235969555,-0.00021906478050571696,0.000617461466860847,0.0004808679905259708,2726427957.4294333,261094779.14126205,-695037.8061323231,70995.12253274885,-14907.579909534476,6641.109749363057,5247.59613385063,10252.785064260053,2385.760506921928,182.77065411486242,140.78060819185018,-27.828287145319333,-9.55597723418611,-2.3060861938105193,-1.3798530598155903,-1.021961406460463,-1.0411422671548503,-0.9797629601941595,-0.642554367676464,0.17893829166211758,1.4686691796328375,2.786297073207378,3.7620378464898026,4.540259983295785,5.1094004901049255,5.559683750507976,5.771893695620013,5.721527340153783,5.446444962247946,5.062804937420855,4.721948470081997,2.9211948834836265,0.00084284572537257,0.0006559425948800731,-0.00015052186785555042,-1.7883397881264575e-05,-7.26453363576379e-05,-6.437999506618508e-05,-5.40104089026196e-05,-1.569716826470345e-05,7.403271958340043e-05,0.00012065733423232634,0.00029269497840226884,0.0005606498085082961,0.0007611089794277466,0.0008701011549649134,0.0009113916428525996,0.0008093556110146979,0.0006121290053111708,0.0005161664192979598,0.0006053301118149016,0.0007387067845922152,0.0007936758091169348,0.0008960430269177788,0.0010501630294727537,0.0018503334171570776,0.0030069338966879264,0.005877118399936972,0.004686780442262653,0.025813559222539195,0.06888736437743012,8.375788951395893e-05,4.539739092442028e-05,-9.010995458120888e-05,-0.00015294255106294467,-95898.10532367068,-1109092.82494946,51790.40970655839,-11044.004909793419,4390.416455235756,-1983.1410615299324,-133.215047328689,714.3888636504415,148.42974204880906,21.338271740029,22.27128611478109,63.311476830430564,-0.8457043954273652,-0.19469576253250898,-0.43951708823321056,-0.41363092993065154,-0.568737865786813,-0.5740625129789672,-0.23261957279855244,0.5310187312081359,1.4756820918773446,2.426173810324784,3.2813084934758905,4.074473737523852,4.7515167105048866,5.351284440000824,5.747807071704172,5.925873006464915,5.958455822353402,5.889876424334979,5.723483619001392,4.41823231402537,-0.014914364886371117,0.0054763662222372346,-0.0017071216246122725,0.0009088408820692475,0.0007315956282099057,0.0009966835719917775,0.0005649785948311489,-5.804840845472811e-05,-0.0008380464066540732,-0.001154013876226718,-0.0015118665087791173,-0.0018430250815476017,-0.0019962440463952963,-0.002015891353646461,-0.0019037031845388034,-0.0016211117281353814,-0.0012904281881122995,-0.0010658752098678759,-0.0008293021826979509,-0.0006099340077724712,-0.0006160205854780929,-0.000627586109609773,-0.0006818719014923615,-0.0009694764722986866,-0.0011743616077107809,-0.001758832902160301,-0.0010126649452062212,-0.005664380552166852,-0.014549889581569627,0.00023503383863568504,0.0001863878131048909,-0.00018550411394451538,-3.6832417715604804e-05,6605.961649956228]"""
RAW_KNOT_JSON = r"""[0.22,0.22,0.22,0.22,0.22,0.22,0.235,0.239375,0.24375,0.24812499999999998,0.2503125,0.2525,0.25468749999999996,0.25687499999999996,0.26125,0.27,0.28750000000000003,0.29625,0.30500000000000005,0.30937500000000007,0.31375000000000003,0.318125,0.3225,0.3246875,0.326875,0.32796875000000003,0.32906250000000004,0.33015625000000004,0.33125000000000004,0.33234375000000005,0.33343750000000005,0.33453125000000006,0.33562500000000006,0.33781250000000007,0.3389062500000001,0.34,0.375,0.41000000000000003,0.48,0.4975,0.515,0.55,0.555,0.56,0.565,0.57,0.5725,0.57375,0.575,0.5774999999999999,0.58,0.585,0.59,0.6,0.61,0.62,0.63,0.635,0.64,0.65,0.78,0.85,0.85,0.85,0.85,0.85,0.85]"""
PAID_FORCE_NORMALIZATION = 16533.1541790287
PAID_ACTIVE_ETA = 3.042718636745052e-7
MODES = np.arange(2, 17, 2, dtype=int)
BULK_LEFT, BULK_RIGHT = .23, .24
COUNTS = {"weak_evaluations": 0, "analytic_jacobians": 0,
          "analytic_columns": 0, "core_evaluations": 0,
          "new_inner_RHS": 0, "new_outer_RHS": 0,
          "svd_factorizations": 0, "model_directions": 0,
          "line_search_trials": 0, "accepted_steps": 0,
          "rejected_steps": 0, "mass_eigenvalue_observations": 0}
REJECTIONS = {}

def import_paid():
    path = HERE/PAID_FILE
    if hashlib.sha256(path.read_bytes()).hexdigest() != PAID_SHA:
        raise RuntimeError("paid forced-height source changed")
    spec = importlib.util.spec_from_file_location("r594_paid_forced_height", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

paid = import_paid()
base, knot, parent = paid.base, paid.knot, paid.parent
emit = base.emit

class ScientificBudget(Exception):
    pass

def check(deadline):
    if time.monotonic() >= deadline:
        raise ScientificBudget("declared weak-BVP scientific clock")

def identity(q):
    return knot.q_identity(np.asarray(q, dtype=float))

def restore_paid(args, deadline):
    if hashlib.sha256(RAW_Q_JSON.encode()).hexdigest() != SOURCE_Q_SHA:
        raise RuntimeError("actual 265-q input changed")
    if hashlib.sha256(RAW_KNOT_JSON.encode()).hexdigest() != SOURCE_KNOT_SHA:
        raise RuntimeError("complete actual knot vector changed")
    q = np.asarray(json.loads(RAW_Q_JSON), dtype=float)
    knots = np.asarray(json.loads(RAW_KNOT_JSON), dtype=float)
    old, oldq, flats = paid.restore_paid_model(args)
    if q.size != 265 or not np.array_equal(knots, old.bs.t):
        raise RuntimeError("actual input dimension or original basis changed")
    # This is the force's ORIGINAL frozen W, not the terminal q[0].
    force_profile = replace(old.par, gain_height=float(oldq[0]))
    force = paid.BodyForcedFour(flats[1], old.modes[0], force_profile, args, deadline)
    force.scale = PAID_FORCE_NORMALIZATION
    model = paid.ForcedHeightDesign.__new__(paid.ForcedHeightDesign)
    model.__dict__.update(old.__dict__)
    model.cache = {}
    model.forced, model.original_nq, model.nq = force, old.nq, old.nq+1
    emit("WEAK_BVP_PAID_DEFINITION_REBUILT", {
        "same_265_q": identity(q), "same_67_knots": True,
        "original_force_frozen_H": float(oldq[0]),
        "terminal_background_H": float(q[0]),
        "force_normalization_reused": force.scale,
        "force_rebuilt_scalar_identity": {"raw_core_A":force.Acore,
            "raw_combined_C":force.raw_Ccore_after_combination,
            "tail_multiplier":force.tail_multiplier,
            "backward_switch_A_C_difference":force.backward_switch_difference},
        "old_inner_Riccati_repeated": False,
        "old_gain_shooting_repeated": False})
    return model, q, flats

def new_modes(old, flats, args, deadline):
    modes = list(old.modes)
    for j in (10, 12, 14, 16):
        check(deadline)
        before = base.COUNTS["seed_RHS"]
        flat = base.FlatSeed(j, args)
        inner_cost = int(flat.inner["nfev_inner"])
        total_cost = base.COUNTS["seed_RHS"]-before
        COUNTS["new_inner_RHS"] += inner_cost
        COUNTS["new_outer_RHS"] += total_cost-inner_cost
        check(deadline)
        mode = base.AdmissibleMode(flat, old.par, args)
        modes.append(mode)
        emit("WEAK_BVP_NEW_TRUE_MODE", {
            "mode": j, "proof": "R596, finite modes through 16",
            "finite_inner_data": flat.finite_inner_data,
            "balanced_alpha17_slope": flat.inner["z_at_alpha_first"],
            "rho18": flat.inner["rho_first_plus_one"],
            "terminal_index": args.M+1,
            "terminal_condition": "rho_(M+1)=0; y(alpha_(M+1))=0",
            "inner_RHS": inner_cost, "outer_RHS": total_cost-inner_cost,
            "core_and_explicit_match": mode.receipt(),
            "exact_DtN_bound_is_not_floating_ODE_error": True})
    return modes

class WeakHeight:
    geometry = base.HeightDesign.geometry

    def __init__(self, old, paidq, modes, args, deadline):
        self.old, self.paidq = old, paidq.copy()
        self.modes, self.par, self.args = modes, old.par, args
        self.deadline, self.bs = deadline, old.bs
        self.nb = len(self.bs.t)-self.bs.k-1
        self.nq = 1+7+8*self.nb
        self.minimum = max(m.flat.minimum_radius for m in modes)
        self.cache = {}
        self.bulk_power = self.par.alpha+2
        self.bulk_scale = (self.par.R-.30)**self.bulk_power
        self.column_modes = np.r_[MODES[1:], np.repeat(MODES, self.nb)]
        self.core_B = self.bs(self.par.R)
        self.core_k = self.par.core_scale*((self.par.R-self.par.core_start)/2)**self.par.alpha
        self.core_forced_source = self.old.forced.source_x(0.)/self.old.forced.scale
        self.actual_checkpoint = None
        self.analytic_observation_paid = False

    def prepare(self, r, ntheta):
        check(self.deadline)
        r = np.asarray(r, dtype=float)
        key = (r.tobytes(), int(ntheta))
        if key in self.cache:
            return self.cache[key]
        data = dict(self.old.prepare(r, ntheta))
        fields = np.concatenate([data["fields"],
            np.stack([m.evaluate(r) for m in self.modes[4:]], axis=1)], axis=1)
        chi, chir, chirr = base.step2((r-BULK_LEFT)/(BULK_RIGHT-BULK_LEFT))
        chir /= BULK_RIGHT-BULK_LEFT
        chirr /= (BULK_RIGHT-BULK_LEFT)**2
        delta, power = self.par.R-r, self.bulk_power
        v = chi*delta**power/self.bulk_scale
        vr = (chir*delta**power-chi*power*delta**(power-1))/self.bulk_scale
        vrr = (chirr*delta**power-2*chir*power*delta**(power-1)
               +chi*power*(power-1)*delta**(power-2))/self.bulk_scale
        B, Br, Brr = [self.bs(r, nu=k) for k in range(3)]
        bulk = np.stack([v[:,None]*B, vr[:,None]*B+v[:,None]*Br,
                         vrr[:,None]*B+2*vr[:,None]*Br+v[:,None]*Brr], axis=2)
        data["new_columns"] = np.concatenate([fields[:,1:,:],
                                              np.tile(bulk,(1,8,1))], axis=1)
        theta = data["theta"]
        data["column_cos"] = np.cos(self.column_modes[:,None]*theta)
        data["column_sin"] = np.sin(self.column_modes[:,None]*theta)
        data["weak_cos"] = np.cos(MODES[:,None]*theta)
        data["weak_sin"] = np.sin(MODES[:,None]*theta)
        # Fixed radial quadrature and angular row units, never changed in a trial.
        dr = np.empty_like(r)
        dr[0], dr[-1] = (r[1]-r[0])/2, (r[-1]-r[-2])/2
        dr[1:-1] = (r[2:]-r[:-2])/2
        data["weak_row_units"] = np.sqrt(dr/dr.sum())[:,None]/(MODES[None,:]**2)
        data["paid_height_cache"] = {}
        self.cache[key] = data
        return data

    def delta_jets(self, direction, amplitude, data):
        coefficients = amplitude*np.asarray(direction)[1:]
        fields = data["new_columns"]
        c, s, j = data["column_cos"], data["column_sin"], self.column_modes
        d0, d1, d2 = [fields[:,:,k]*coefficients[None,:] for k in range(3)]
        return (d0@c, d1@c, d2@c,
                -(d0*j)@s, -(d0*j*j)@c, -(d1*j)@s)

    def height_jets(self, q, amplitude, data):
        cache = data["paid_height_cache"]
        key = float(amplitude)
        if key not in cache:
            cache[key] = self.old.height_jets(self.paidq, amplitude, data)
        add = self.delta_jets(q, amplitude, data)
        return tuple(a+b for a,b in zip(cache[key],add))

    def core_state(self, q, amplitude, theta):
        COUNTS["core_evaluations"] += 1
        co, si = np.cos(MODES[:,None]*theta), np.sin(MODES[:,None]*theta)
        coeff = np.zeros(8, dtype=np.result_type(q, float))
        coeff[:4] = amplitude*np.r_[1., self.paidq[1:4]]
        coeff[1:] += amplitude*q[1:8]
        nu = MODES**2-1
        pc = -nu/self.par.R*coeff
        # The retained post-tanh force is part of the core as well as the body.
        old_force_coefficient = amplitude**2*self.paidq[-1]
        pc[1] += old_force_coefficient*(-15*self.old.forced.Acore/
                                       (self.par.R*self.old.forced.scale))
        P, Pt, Ptt = pc@co, -(pc*MODES)@si, -(pc*MODES**2)@co
        reference = float(np.max(np.real(-2*P)))
        left, right = 0., 2.
        for _ in range(56):
            mid = (left+right)/2
            value = np.mean(1/np.sqrt(mid+reference+2*np.real(P)))
            if value>1:
                left = mid
            else:
                right = mid
        e = complex((left+right)/2+reference) if np.iscomplexobj(q) else (left+right)/2+reference
        for _ in range(3):
            u = np.sqrt(e+2*P)
            e += 2*(np.mean(1/u)-1)/np.mean(u**-3)
        u = np.sqrt(e+2*P)
        if np.min(np.real(u*u))<=1e-12:
            raise base.DomainError("core turning root lost its positive margin")
        b = q[8:].reshape(8,self.nb)@self.core_B
        Pr_bulk = amplitude*self.core_k*(self.par.alpha+2)/self.bulk_scale*b
        source_core = self.core_forced_source
        linear = -self.par.R*(Pr_bulk@co)-old_force_coefficient*source_core*co[1]
        al = self.par.alpha/(1+self.par.alpha)
        At = linear+al*(e-1+2*P)*Ptt-Pt*Pt
        # The full finite radial flux derivative, including the old force.
        Pr = al/self.par.R*Ptt+Pr_bulk@co
        Pr += old_force_coefficient*source_core/self.par.R*co[1]
        er = -2*(np.mean(Pr/u**3)+np.mean(Ptt/u)/(self.par.R*(1+self.par.alpha)))/np.mean(u**-3)
        D = At-er*self.par.R/2
        weak = At@co.T/(len(theta)*self.par.R)
        return {"P":P,"Pt":Pt,"Ptt":Ptt,"e":e,"u":u,"At":At,
                "Pr":Pr,"er":er,"D":D,"weak":weak,"pc":pc,
                "turning_error":np.mean(1/u)-1,"co":co,"si":si}

    def evaluate(self, q, amplitude, data):
        check(self.deadline)
        COUNTS["weak_evaluations"] += 1
        g = self.geometry(q, amplitude, data, details=True)
        if np.min(np.real(g["Z"]))<=0:
            raise base.DomainError("reflected halves lost positive sampled height")
        r = data["r"][:,None]
        f,fr,frr,ft,ftt,frt = self.height_jets(q,amplitude,data)
        dh = q[0]-self.par.gain_height
        w = (data["w0"]+dh*data["gain_w"])[:,None]
        wr = (data["wr0"]+dh*data["gain_wr"])[:,None]
        E,e,p,b,N,u = [g[k] for k in ("E","e","p","b","N","u")]
        M = b**3*N/(r*r)
        B = frt-ft/r
        At = (-r*w*frr-r*wr*fr-e*wr*ftt
              +E*frr*ftt-w*wr*fr*ftt-E*B*B+r*fr*frr+w*wr*ft*ft/r)
        weak = (At/M)@data["weak_cos"].T/len(data["theta"])
        core = self.core_state(q,amplitude,data["theta"])
        vector = np.r_[(weak*data["weak_row_units"]/amplitude).ravel(),
                        .1*core["weak"]/(amplitude*MODES**2)]
        if not np.all(np.isfinite(vector)):
            raise base.DomainError("nonfinite complete weak BVP residual")
        return {"q":q.copy(),"g":g,"f":f,"fr":fr,"frr":frr,
                "ft":ft,"ftt":ftt,"frt":frt,"w":w,"wr":wr,
                "M":M,"B":B,"At":At,"weak":weak,"core":core,"residual":vector}

    def jacobian(self, q, amplitude, data, state):
        check(self.deadline)
        COUNTS["analytic_jacobians"] += 1
        nr,nt = len(data["r"]),len(data["theta"])
        J = np.empty((nr*8+8,self.nq))
        r = data["r"][:,None,None]
        g = state["g"]
        p,b,N,u,E,e = [g[k][:,:,None] for k in ("p","b","N","u","E","e")]
        w,wr,fr,frr,ft,ftt,B,M,At = [state[k][:,:,None] for k in
            ("w","wr","fr","frr","ft","ftt","B","M","At")]
        den = np.mean(N/u**3,axis=1,keepdims=True)
        co = data["weak_cos"]
        core = state["core"]
        al = self.par.alpha/(1+self.par.alpha)
        for first in range(0,self.nq,16):
            check(self.deadline)
            indices = np.arange(first,min(self.nq,first+16))
            nc = len(indices)
            jets = [np.zeros((nr,nt,nc)) for _ in range(6)]
            dw, dwr = np.zeros((nr,1,nc)),np.zeros((nr,1,nc))
            dpc = np.zeros((8,nc))
            dpr = np.zeros((8,nc))
            for local,index in enumerate(indices):
                if index == 0:
                    dw[:,0,local],dwr[:,0,local] = data["gain_w"],data["gain_wr"]
                    continue
                col = index-1
                fields = amplitude*data["new_columns"][:,col,:]
                c,s,j = data["column_cos"][col],data["column_sin"][col],self.column_modes[col]
                values = (fields[:,0,None]*c,fields[:,1,None]*c,
                          fields[:,2,None]*c,-j*fields[:,0,None]*s,
                          -j*j*fields[:,0,None]*c,-j*fields[:,1,None]*s)
                for target,value in zip(jets,values):
                    target[:,:,local] = value
                if index<8:
                    dpc[index,local] = -(MODES[index]**2-1)/self.par.R*amplitude
                else:
                    mode,bsindex = divmod(index-8,self.nb)
                    dpr[mode,local] = amplitude*self.core_k*(self.par.alpha+2)/self.bulk_scale*self.core_B[bsindex]
            _,dfr,dfrr,dft,dftt,dfrt = jets
            dp = -dw+dfr
            dN = (r*ft*dft/b**3+r*r*(ftt*dp+p*dftt)/b**3
                  +3*r*r*p*ftt*ft*dft/b**5)
            dshift = (-2*dw*fr-2*w*dfr+2*fr*dfr
                      +2*p*dp*ft*ft/b**2+2*p*p*ft*dft/b**2
                      +2*p*p*ft**3*dft/b**4)
            de = (2*np.mean(dN/u,axis=1,keepdims=True)
                  +np.mean(N*dshift/u**3,axis=1,keepdims=True))/den
            dE = 2*w*dw+de
            dM = ftt*dp+p*dftt-2*ft*dft/r
            dB = dfrt-dft/r
            dAt = (-r*(dw*frr+w*dfrr)-r*(dwr*fr+wr*dfr)
                   -de*wr*ftt-e*dwr*ftt-e*wr*dftt
                   +dE*frr*ftt+E*dfrr*ftt+E*frr*dftt
                   -(dw*wr+w*dwr)*fr*ftt-w*wr*dfr*ftt-w*wr*fr*dftt
                   -dE*B*B-2*E*B*dB+r*(dfr*frr+fr*dfrr)
                   +(dw*wr+w*dwr)*ft*ft/r+2*w*wr*ft*dft/r)
            dweak = np.einsum("rtp,jt->rjp",dAt/M-At*dM/M**2,co)/nt
            J[:-8,indices] = (dweak*data["weak_row_units"][:,:,None]/amplitude).reshape(-1,nc)
            dP,dPt,dPtt = core["co"].T@dpc,-core["si"].T@(MODES[:,None]*dpc),-core["co"].T@(MODES[:,None]**2*dpc)
            deR = -2*np.mean(dP/core["u"][:,None]**3,axis=0)/np.mean(core["u"]**-3)
            dAtR = (-self.par.R*(core["co"].T@dpr)
                    +al*(deR[None,:]*core["Ptt"][:,None]
                         +(core["e"]-1+2*core["P"])[:,None]*dPtt
                         +2*dP*core["Ptt"][:,None])
                    -2*core["Pt"][:,None]*dPt)
            dcore = core["co"]@dAtR/(nt*self.par.R)
            J[-8:,indices] = .1*dcore/(amplitude*MODES[:,None]**2)
            COUNTS["analytic_columns"] += nc
        if not np.all(np.isfinite(J)):
            raise ArithmeticError("nonfinite analytic complete weak Jacobian")
        return J

def mass_report(model,state,data):
    COUNTS["mass_eigenvalue_observations"] += 1
    r = data["r"][:,None]
    g = state["g"]
    aa = g["E"]*state["ftt"]+r*g["p"]
    coefficient = aa/state["M"]
    co = data["weak_cos"]
    mass = np.einsum("rt,it,jt->rij",coefficient,co,co)/len(data["theta"])
    eig = np.linalg.eigvalsh(mass)
    abs_eig = abs(eig)
    relative = np.min(abs_eig,axis=1)/np.maximum(np.max(abs_eig,axis=1),1e-300)
    where = np.unravel_index(int(np.argmax(aa)),aa.shape)
    worst = int(np.argmin(relative))
    return {"pointwise_a_min":float(np.min(aa)),"pointwise_a_max":float(np.max(aa)),
            "a_max_attainer":[float(data["r"][where[0]]),float(data["theta"][where[1]])],
            "nonnegative_a_node_count":int(np.sum(aa>=0)),
            "actual_weak_mass_smallest_relative_singular_value":float(relative[worst]),
            "weak_mass_worst_radius":float(data["r"][worst]),
            "weak_mass_worst_eigenvalues":eig[worst].tolist(),
            "sampled_weak_mass_rank_min_at_relative_1e_12":int(np.min(np.sum(
                abs_eig>1e-12*np.max(abs_eig,axis=1,keepdims=True),axis=1))),
            "pointwise_a_not_divided":True,"continuous_sign_or_rank_certificate":False}

def core_report(state,theta):
    c = state["core"]
    out = []
    for j in range(0,35,2):
        z = np.mean(c["D"]*np.cos(j*theta))*(1 if j==0 else 2)
        out.append({"mode":j,"D_coefficient":float(z)})
    return {"P_cosine_coefficients":c["pc"].tolist(),"eR":float(c["e"]),
            "erR":float(c["er"]),"uR_min":float(np.min(c["u"])),
            "complete_core_D_max":float(np.max(abs(c["D"]))),
            "complete_core_D_harmonics":out,
            "core_weak_rows":c["weak"].tolist(),
            "turning_error":float(c["turning_error"]),
            "mean_weighted_D":float(np.mean(c["D"]/c["u"]**3)),
            "finite_formula_not_R_minus_epsilon":True}

def checkpoint(model,q,amplitude,data,state,iteration,status):
    model.actual_checkpoint = {"q":q.copy(),"amplitude":float(amplitude),
                               "iteration":iteration,"status":status}
    report = knot.compact_report(q,amplitude,data,state["g"])
    report.update({"iteration":iteration,"status":status,"q_identity":identity(q),
                   "actual_correction_q":q.tolist(),
                   "weak_merit":float(np.dot(state["residual"],state["residual"])/2),
                   "body_weak_max_by_mode":np.max(abs(state["weak"]),axis=0).tolist(),
                   "mass":mass_report(model,state,data),
                   "core":core_report(state,data["theta"])})
    emit("WEAK_BVP_COMPLETE_ACCEPTED_STATE",report)
    return report

def reject(reason):
    COUNTS["rejected_steps"] += 1
    REJECTIONS[reason] = REJECTIONS.get(reason,0)+1

def solve_stage(model,initial,amplitude,data,args,deadline):
    q = initial.copy()
    state = model.evaluate(q,amplitude,data)
    report = checkpoint(model,q,amplitude,data,state,0,"initial_actual_state")
    damping,status = 1e-5,"declared_iteration_limit"
    for iteration in range(args.iterations):
        check(deadline)
        if report["eta_max"]<=args.target_eta:
            status = "active_metric_target_requires_fine_readout"
            break
        residual = state["residual"]
        objective = .5*float(residual@residual)
        J = model.jacobian(q,amplitude,data,state)
        scales = np.maximum(np.linalg.norm(J,axis=0),1e-12)
        if not model.analytic_observation_paid:
            direction = .001*np.cos(np.arange(model.nq)*.713)
            h = 1e-25
            complex_state = model.evaluate(q.astype(complex)+1j*h*direction,amplitude,data)
            actual = np.imag(complex_state["residual"])/h
            predicted = J@direction
            rel = np.linalg.norm(actual-predicted)/max(1e-100,np.linalg.norm(actual))
            emit("WEAK_BVP_ANALYTIC_DIRECTION",{
                "relative_l2_difference":float(rel),
                "absolute_max_difference":float(np.max(abs(actual-predicted))),
                "same_full_paid_field_and_core_rows":True,
                "nonzero_current_residual_not_discarded":True})
            if not rel<3e-5:
                raise ArithmeticError("new analytic weak Jacobian failed its declared directional observation")
            model.analytic_observation_paid = True
        Js = J/scales
        U,s,Vt = np.linalg.svd(Js,full_matrices=False)
        COUNTS["svd_factorizations"] += 1
        threshold = max(Js.shape)*np.finfo(float).eps*s[0]
        spectrum = {"singular_max":float(s[0]),"singular_min":float(s[-1]),
                    "reported_rank":int(np.sum(s>threshold)),"rank_threshold":float(threshold),
                    "column_norm_min":float(np.min(np.linalg.norm(J,axis=0))),
                    "column_norm_max":float(np.max(np.linalg.norm(J,axis=0))),
                    "columns_below_scale_floor":int(np.sum(np.linalg.norm(J,axis=0)<1e-12)),
                    "scaled_gradient_inf":float(np.max(abs(Js.T@residual))),
                    "all_singular_directions_retained":True,"normal_equations_not_formed":True}
        ur = U.T@residual
        accepted=False
        for trial in range(8):
            check(deadline)
            lam=damping*10.**trial
            direction=-(Vt.T@(s/(s*s+lam)*ur))/scales
            COUNTS["model_directions"]+=1
            factor,measures=parent.function_trial_limit(model,q,direction,amplitude,data,state["g"])
            direction*=factor
            linear=J@direction
            for cut in range(9):
                check(deadline)
                fraction=2.**(-cut)
                predicted=objective-.5*float((residual+fraction*linear)@(residual+fraction*linear))
                COUNTS["line_search_trials"]+=1
                try:
                    candidate_q=q+fraction*direction
                    candidate=model.evaluate(candidate_q,amplitude,data)
                    actual=objective-.5*float(candidate["residual"]@candidate["residual"])
                    threshold_drop=max(32*np.finfo(float).eps*objective,1e-30)
                    ratio=actual/predicted if predicted>0 else -np.inf
                    okay=actual>threshold_drop and predicted>0 and ratio>.01
                    reason="no_resolvable_complete_weak_decrease"
                except base.DomainError as exc:
                    okay=False
                    reason="domain:"+str(exc)
                if okay:
                    q,state=candidate_q,candidate
                    damping=max(1e-14,lam/3)
                    COUNTS["accepted_steps"]+=1
                    emit("WEAK_BVP_ACCEPTANCE",{
                        "iteration":iteration,"amplitude":amplitude,"trial":trial,
                        "fraction":fraction,"function_factor":factor,
                        "function_measures":measures,"actual_decrease":float(actual),
                        "predicted_decrease":float(predicted),"actual_over_predicted":float(ratio),
                        "spectrum":spectrum})
                    report=checkpoint(model,q,amplitude,data,state,iteration+1,"actual_complete_weak_decrease")
                    accepted=True
                    break
                reject(reason)
            if accepted:
                break
        if not accepted:
            status="no_resolvable_step_in_declared_radial_weak_space"
            emit("WEAK_BVP_STALL",{"iteration":iteration,"q_identity":identity(q),
                                  "spectrum":spectrum,"actual_retained_q":q.tolist()})
            break
    return q,state,{"status":status,"last_report":report}

def fine_readout(model,q,amplitude,args):
    r=knot.radial_grid(model,2)
    data=model.prepare(r,2*args.theta_nodes)
    st=model.evaluate(q,amplitude,data)
    report=knot.compact_report(q,amplitude,data,st["g"])
    report["mass"]=mass_report(model,st,data)
    report["core"]=core_report(st,data["theta"])
    report["body_weak_max_by_mode"]=np.max(abs(st["weak"]),axis=0).tolist()
    weight=data["r"][:,None]**2/(st["g"]["u"]**3*st["g"]["b"]**3)
    D=st["g"]["R"]/weight
    harmonics=[]
    for j in range(0,41,2):
        v=(1 if j==0 else 2)*np.mean(D*np.cos(j*data["theta"])[None,:],axis=1)
        at=int(np.argmax(abs(v)))
        harmonics.append({"mode":j,"maximum_absolute_D_coefficient":float(abs(v[at])),
                          "signed_coefficient":float(v[at]),"radius":float(r[at])})
    report["complete_D_harmonics"]=harmonics
    direct1=base.actual_curvature_observation(model,q,amplitude,r,2*args.theta_nodes)
    direct2=base.actual_curvature_observation(model,q,amplitude,r,2*args.theta_nodes,factor=.5)
    okay=(report["eta_max"]<=args.target_eta and report["sampled_height_min"]>0
          and direct1["direct_position_outward_ratio_min"]>0
          and direct2["direct_position_outward_ratio_min"]>0
          and direct1["direct_reconstructed_metric_eta"]<=args.target_eta
          and direct2["direct_reconstructed_metric_eta"]<=args.target_eta)
    return {"same_actual_q":identity(q),"fine":report,"direct_step":direct1,
            "direct_half_step":direct2,"fine_metric_observation_passed":bool(okay),
            "continuous_tail_or_reach_certificate":False}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--maximum-seconds",type=float,default=2400.)
    ap.add_argument("--M",type=int,choices=[25],default=25)
    ap.add_argument("--rtol",type=float,default=2e-11)
    ap.add_argument("--atol",type=float,default=2e-13)
    ap.add_argument("--iterations",type=int,default=60)
    ap.add_argument("--theta-nodes",type=int,choices=[128],default=128)
    ap.add_argument("--target-eta",type=float,default=2e-9)
    ap.add_argument("--height-saturation",type=float,choices=[.15],default=.15)
    args=ap.parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true"
        or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("science executes only in the declared public job")
    if not 60<args.maximum_seconds<=2400 or not 1<=args.iterations<=60:
        raise ValueError("outside declared eight-mode BVP scope")
    started=time.monotonic()
    deadline=started+args.maximum_seconds
    model,q,amplitude=None,None,1e-5
    stages,status=[],"not_started"
    emit("WEAK_BVP_DEFINITION",{
        "schema":SCHEMA,"arguments":vars(args),"modes":MODES.tolist(),
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "paid_run":SOURCE_RUN,"paid_job":SOURCE_JOB,"paid_commit":SOURCE_COMMIT,
        "paid_stdout_sha256":SOURCE_LOG_SHA,"paid_FINAL_sha256":SOURCE_FINAL_SHA,
        "paid_q_sha256":SOURCE_Q_SHA,"paid_knots_sha256":SOURCE_KNOT_SHA,
        "whole_paid_field_preserved_not_fourier_projected":True,
        "new_bulk_start_interval":[BULK_LEFT,BULK_RIGHT],
        "new_bulk_core_power":2.55,"old_inner_Riccati_calls":0,
        "new_inner_modes":[10,12,14,16],
        "finite_angular_weak_BVP_not_full_infinite_solution":True,
        "same_fixed_metric_or_README_completion_claim":False})
    try:
        old,paidq,flats=restore_paid(args,deadline)
        # The zero affine increment preserves the bound paid field algebraically.
        # Do not rerun its completed 64-angle observation as a new gate.
        # First evaluate the actual new eight-mode problem on its declared grid.
        modes=new_modes(old,flats,args,deadline)
        model=WeakHeight(old,paidq,modes,args,deadline)
        q=np.zeros(model.nq)
        q[0]=paidq[0]
        emit("WEAK_BVP_AFFINE_INPUT",{
            "correction_parameters":model.nq,"radial_basis_count":model.nb,
            "original_265q_retained_verbatim":True,
            "all_new_height_coefficients_exactly_zero":bool(np.all(q[1:]==0)),
            "primary_core_increment_fixed_zero":True,
            "new_higher_core_fluxes_free":True,
            "core_bulk_scale":model.bulk_scale,"core_W_leading_k":model.core_k,
            "same_source_normalizations_preserved":True})
        r=knot.radial_grid(model,1)
        data=model.prepare(r,args.theta_nodes)
        for amplitude in (1e-5,3e-5,1e-4,3e-4,.001,.003,.01,.03,.1,.2):
            check(deadline)
            q,state,summary=solve_stage(model,q,amplitude,data,args,deadline)
            readout=fine_readout(model,q,amplitude,args)
            record={"amplitude":amplitude,"summary":summary,"readout":readout,
                    "actual_correction_q":q.tolist(),"actual_q_identity":identity(q)}
            stages.append(record)
            emit("WEAK_BVP_STAGE",record)
            status=summary["status"]
            if not readout["fine_metric_observation_passed"]:
                break
    except (ScientificBudget,paid.ScientificBudget) as exc:
        status="declared_scientific_budget"
        emit("WEAK_BVP_CLOCK",{"message":str(exc),
             "complete_checkpoint_available":model is not None and model.actual_checkpoint is not None,
             "actual_checkpoint_will_be_restored_in_FINAL":True})
    except (base.DomainError,ArithmeticError,ValueError,FloatingPointError,np.linalg.LinAlgError) as exc:
        status="declared_model_or_numerical_failure"
        emit("WEAK_BVP_FAILURE",{"type":type(exc).__name__,"message":str(exc),
             "last_returned_q_retained":q is not None})
    entered_amplitude=amplitude
    checkpoint_identity=None
    if model is not None and model.actual_checkpoint is not None:
        retained=model.actual_checkpoint
        q=retained["q"].copy()
        amplitude=retained["amplitude"]
        checkpoint_identity={k:v for k,v in retained.items() if k!="q"}
    final={"schema":SCHEMA,"status":status,"elapsed_seconds":time.monotonic()-started,
           "last_entered_amplitude":entered_amplitude,
           "actual_retained_amplitude":amplitude,
           "actual_retained_correction_q":None if q is None else q.tolist(),
           "actual_retained_q_identity":None if q is None else identity(q),
           "actual_retained_checkpoint":checkpoint_identity,
           "actual_265q_source_sha256":SOURCE_Q_SHA,
           "actual_67knot_source_sha256":SOURCE_KNOT_SHA,
           "actual_checkpoint_recovered_even_if_inner_solver_interrupted":True,
           "stages":stages,"new_counts":COUNTS,"base_counts":base.COUNTS,
           "forced_counts":paid.NEW_COUNTS,"function_counts":parent.EXTRA,
           "gain_counts":base.gain.COUNTS,"rejections":REJECTIONS,
           "exact_infinite_tail_nonlinearity_or_ODE_error_certificate":False,
           "continuous_sign_rank_curvature_reach_or_fixed_g_claim":False,
           "raw_arrays_artifacts_releases_or_git_writes":False}
    raw=json.dumps(final,sort_keys=True,separators=(",",":"),allow_nan=False)
    print("WEAK_BVP_FINAL "+raw,flush=True)
    emit("WEAK_BVP_FINAL_IDENTITY",{"JSON_bytes":len(raw.encode()),
         "sha256":hashlib.sha256(raw.encode()).hexdigest()})

if __name__=="__main__":
    main()

