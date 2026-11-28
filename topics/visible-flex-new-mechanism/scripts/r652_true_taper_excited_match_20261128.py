#!/usr/bin/env python3
"""Finite Morse-to-flat-tail preparation, only in public Actions.

The taper-end lines are the proven limits of actual flat suffixes. Nothing
in this script equates the limiting profile or its sampled geometry to a
finite smooth suffix, a completed nonlinear branch, or a reach certificate.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import Polynomial
from scipy.integrate import solve_ivp
from scipy.optimize import root
from scipy.special import eval_genlaguerre


def emit(kind, **fields):
    print(json.dumps(dict(kind=kind, **fields), sort_keys=True, allow_nan=False), flush=True)


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"
            or not os.environ.get("GITHUB_RUN_ID", "").isdigit()):
        raise SystemExit("Scientific evaluation requires public math-research-public Actions.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-seconds", type=float, default=780)
    args = parser.parse_args()
    start = time.perf_counter()
    count = Counter()

    def guard():
        if time.perf_counter() - start >= args.max_seconds:
            raise RuntimeError("Finite-input scientific wall budget reached.")

    v = math.sqrt(55)
    s = (684+95*v)/632
    eta2 = (12*s-19)/20
    eta = math.sqrt(eta2)
    bm = (5*s-8)*(s-2)/20
    smaller_t = (2*bm/s**2)/(1+math.sqrt(1-4*bm/s**2))
    xl, xr = -math.log1p(-smaller_t), -math.log(smaller_t)
    h0 = 1/8
    xpoly = Polynomial([0., 1.])

    def rho(x):
        t = np.exp(-x)
        return s*s*t*(1-t)-bm

    def exact_finite_gap():
        # Exclude levels only by exact comparisons with rational enclosing
        # endpoints for sqrt(55).  A wider finite list is harmless.
        scale = 10**30
        floor_v = math.isqrt(55*scale*scale)
        floor_s_num = 684*scale + 95*floor_v
        ceil_s_num = floor_s_num+95
        den = 632*scale
        best = None
        levels = 0
        skips = []
        for j in range(1, 256):
            for n in range(1, (ceil_s_num*j)//den+1, 2):
                if floor_s_num*j <= n*den:
                    raise ArithmeticError("Algebraic rounding could not decide the discrete index.")
                a = 12-18*j*j+10*j*n
                c = 16*j*j-5*n*n-19
                if not a and not c:
                    skips.append([j,n])
                    continue
                lo, hi = sorted([a*floor_s_num+c*den, a*ceil_s_num+c*den])
                if lo <= 0 <= hi:
                    raise ArithmeticError("Algebraic rounding could not separate finite level.")
                lower = min(abs(lo),abs(hi))
                levels += 1
                if best is None or lower < best[0]:
                    best = lower, j, n
        if skips != [[2,3],[3,5]]:
            raise ArithmeticError("Unexpected designated levels.")
        numerator, j, n = best
        count["finite_nonzero_integer_levels"] = levels
        return dict(lower_numerator=str(numerator),lower_denominator=str(20*den),
                    attainer_indices=[j,n], finite_nonzero_levels=levels,
                    designated_zeros=skips, infinite_j_ge_256_lower="1/3072")

    # Analytic limiting unit-normalized line (value, log-radius derivative).
    # e^z cancels. Jet D(e^z L_n(-z))=e^z[L_n(-z)+L^(1)_(n-1)(-z)].
    def line(j,z):
        n = j*j-1
        val = float(eval_genlaguerre(n,0,-z))
        der = val+float(eval_genlaguerre(n-1,1,-z))
        norm = math.hypot(val,der)
        return val/norm, der/norm

    def transfer(right,left):
        def ode(x,y):
            count["transfer_rhs"] += 1
            matrices = y.reshape(4,2,2)
            out = np.empty_like(matrices)
            out[:,0,:] = matrices[:,1,:]
            out[:,1,:] = (eta2-np.arange(4)**2*rho(x))[:,None]*matrices[:,0,:]
            return out.ravel()
        initials = np.tile(np.eye(2),(4,1,1)).ravel()
        sol = solve_ivp(ode,(right,left), initials, method="DOP853",
                        rtol=2e-12,atol=3e-14,max_step=.1,dense_output=True)
        count["transfer_solves"] += 1
        if not sol.success:
            raise ArithmeticError(sol.message)
        def sample(x):
            count["transfer_readouts"] += 1
            return sol.sol(x).reshape((4,2,2)+np.shape(x))
        return sample

    def cross_rows(mats, lines_l, lines_r):
        # Construct the two residuals as polynomials in c=psi'_1(B).
        # Each coefficient is a polynomial in a=sigma'(B).
        sig = [Polynomial(row) for row in mats[0]]
        psi = mats[1]
        result = []
        for j,(gl,dl),(gr,dr) in zip((2,3),lines_l,lines_r):
            v0, v1 = mats[j][:,0]*gr,mats[j][:,1]
            y = [Polynomial([v0[i],v1[i]*(gr-dr)]) for i in range(2)]
            yd = v1*dr
            # log-derivative boundary condition, cleared of sig*psi.
            h = [gl*y[1]*sig[0]-(gl-dl)*y[0]*sig[1],
                 gl*yd[1]*sig[0]-(gl-dl)*yd[0]*sig[1]]
            d = [-dl*y[0]*sig[0],-dl*yd[0]*sig[0]]
            coeff = [h[0]*psi[0,0]+d[0]*psi[1,0],
                     h[0]*psi[0,1]+h[1]*psi[0,0]+d[0]*psi[1,1]+d[1]*psi[1,0],
                     h[1]*psi[0,1]+d[1]*psi[1,1]]
            size = max(np.max(abs(p.coef)) for p in coeff)
            result.append([p/size for p in coeff])
        return result

    def ratios(rows, x):
        return np.array([[p(x) for p in row] for row in rows])

    def residual(rows,a,c):
        cf = ratios(rows,a)
        return cf[:,0]+c*(cf[:,1]+c*cf[:,2])

    def jacobian(rows,a,c):
        da = np.array([[p.deriv()(a) for p in row] for row in rows])
        cf = ratios(rows,a)
        return np.column_stack((da[:,0]+c*(da[:,1]+c*da[:,2]),cf[:,1]+2*c*cf[:,2]))

    def solve_rows(rows):
        c,b,a = rows[0]
        h,e,d = rows[1]
        resultant = (a*h-d*c)**2-(a*e-d*b)*(b*h-e*c)
        count["finite_resultants"] += 1
        candidates = []
        for ap in resultant.roots():
            if abs(ap.imag) > 1e-5*(1+abs(ap.real)):
                continue
            u = float(ap.real)
            if abs(u)>200:
                continue
            co = ratios(rows,u)
            ci = max(co,key=lambda row: np.linalg.norm(row))
            for cp in np.polynomial.polynomial.polyroots(ci):
                if abs(cp.imag)>2e-4*(1+abs(cp.real)):
                    continue
                c0 = float(cp.real)
                if abs(c0)>201:
                    continue
                count["newton_refinements"] += 1
                def fun(y):
                    count["matching_residual"] += 1
                    return residual(rows,*y)
                def jac(y):
                    count["matching_jacobian"] += 1
                    return jacobian(rows,*y)
                sol = root(fun,[u,c0],jac=jac,tol=1e-11)
                av,cv = (float(t) for t in sol.x)
                if not np.all(np.isfinite(sol.x)) or abs(av)>200 or abs(cv)>201:
                    continue
                if np.linalg.norm(fun(sol.x), np.inf)>1e-10:
                    continue
                if any(np.linalg.norm(np.array(old)-sol.x)<2e-6*(1+np.linalg.norm(sol.x))
                       for old in candidates):
                    continue
                candidates.append((av,cv))
        count["distinct_numeric_roots"] += len(candidates)
        return candidates

    def radial(x,mat,a,c):
        sigma = mat[0,0,0]+a*mat[0,0,1]
        sx = mat[0,1,0]+a*mat[0,1,1]
        psi = mat[1,0,0]+c*mat[1,0,1]
        px = mat[1,1,0]+c*mat[1,1,1]
        w = sigma*px-sx*psi
        return sigma,psi,w

    def transfer_residual(mat,a,c,ll,rr):
        # Direct unexpanded normalized line determinants, independent of
        # the resultant coefficient basis. No finite suffix evaluated.
        sig,psi,w = radial(None,mat,a,c)
        nu = w/(sig*psi)
        al = (mat[0,1,0]+a*mat[0,1,1])/sig
        res = []
        for j,(lg,ld),(rg,rd) in zip((2,3),ll,rr):
            y,yx = mat[j]@np.array([rg,a*rg+(c-a)*rd])
            fl = np.array([y,(yx-al*y)/nu])
            res.append(float((fl[0]*ld-fl[1]*lg)/np.linalg.norm(fl)))
        return res

    def geometry(x,mat,left,right,a,c,ell_l,ell_r):
        sig,psi,wr = radial(x,mat,a,c)
        radius = psi/sig
        rx = wr/sig**2
        core = (xl<=x)&(x<=xr)
        raw_h = np.trapezoid(wr[core]*rx[core],x[core])
        if raw_h<=0 or np.min(rx)<=0:
            return None
        scale = h0/raw_h
        w = scale*wr
        r = radius
        kr = -scale*rho(x)*sig*psi/(rx*(1+w*w)**1.5)
        kt = w/(r*np.sqrt(1+w*w))
        tip_l,tip_r = float(r[0]*math.exp(-ell_l)), math.exp(ell_r)
        ys = 129
        def cap(z0,z1,tip,wcut,length):
            z = np.linspace(z0,z1,ys)
            rad = tip*np.exp(z)
            ww = wcut*abs(z)/length
            kz = np.sign(z0+z1)*wcut/(length*rad*(1+ww*ww)**1.5)
            kc = ww/(rad*np.sqrt(1+ww*ww))
            return np.max(abs(kz)),np.max(abs(kc)),float(np.trapezoid(ww*rad,z))
        kl,tl,hl = cap(0,ell_l,tip_l,w[0],ell_l)
        kr2,tr,hr = cap(-ell_r,0,tip_r,w[-1],ell_r)
        height = float(hl+hr+np.trapezoid(w*rx,x))
        dia_upper = math.hypot(2*tip_r,height)
        peak = float(max(np.max(abs(kr)),np.max(kt),kl,tl,kr2,tr))
        count["sampled_radial_points"] += len(x)+2*ys
        return dict(a_B=a,psi1_log_slope_B=c,nu_B=c-a,core_X=[left,right],
                    taper_lengths=[ell_l,ell_r],height_scale=float(scale),
                    cut_radius=[float(r[0]),float(r[-1])],cut_w=[float(w[0]),float(w[-1])],
                    cap_radii=[tip_l,tip_r],sampled_total_height=height,
                    sampled_axisymmetric_diameter_estimate=dia_upper,
                    sampled_cap_only_displacement_ceiling_estimate=tip_l/tip_r,
                    sampled_cap_diameter_over_axisymmetric_diameter_estimate=2*tip_l/dia_upper,
                    sampled_max_abs_meridional_curvature=float(max(np.max(abs(kr)),kl,kr2)),
                    sampled_max_abs_azimuthal_curvature=float(max(np.max(kt),tl,tr)),
                    sampled_curvature_times_diameter_estimate=peak*dia_upper,
                    true_closed_whole_image_displacement=None,actual_finite_suffix_N=None)

    left_offsets = [1/32,1/8,1/4,1/2,3/4]
    right_offsets = [1/32,1/8,1/4,1/2,1.,2.]
    left_lengths = [1/32,1/8,1/4,1/2]
    # Each right limiting negative-component travel is pi times sqrt(2)/d.
    right_denominators = [12,8,6,4,3]
    best = {}
    def retain(label,value,row):
        if label not in best or value>best[label][0]:
            best[label] = (float(value),row)
    emit("provenance",run_id=os.environ["GITHUB_RUN_ID"],
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         s=s,eta_squared=eta2,B=bm,core_height= h0,
         finite_gap=exact_finite_gap(),scientific_wall_limit=args.max_seconds,
         intended_cells=len(left_offsets)*len(right_offsets)*len(left_lengths)*len(right_denominators),
         nonlinear_solved=False)
    try:
        for bo in right_offsets:
            right = xr+bo
            matrices = transfer(right,xl-max(left_offsets))
            at_xr = matrices(xr)
            for ao in left_offsets:
                guard()
                left = xl-ao
                ml = matrices(left)
                x = np.unique(np.r_[np.linspace(left,right,513),xl,xr])
                grid = matrices(x)
                for ell_l in left_lengths:
                    ll = [line(j,ell_l) for j in (2,3)]
                    for div in right_denominators:
                        guard()
                        ell_r = math.pi**2/(2*div**2)
                        rr = [line(j,-ell_r) for j in (2,3)]
                        rows = cross_rows(ml,ll,rr)
                        count["matched_geometries_tested"] += 1
                        for a,c in solve_rows(rows):
                            if c<=a:
                                continue
                            sig,psi,wa = radial(left,ml,a,c)
                            _,_,wr = radial(xr,at_xr,a,c)
                            if min(sig,psi,wa,wr)<=1e-9:
                                continue
                            res = transfer_residual(ml,a,c,ll,rr)
                            if max(abs(y) for y in res)>1e-6:
                                continue
                            count["positive_directly_matched_candidates"] += 1
                            row = geometry(x,grid,left,right,a,c,ell_l,ell_r)
                            if row is None:
                                continue
                            row.update(left_offset=ao,right_offset=bo,
                                       right_travel_sqrt2_denominator=div,
                                       normalized_line_residual=res,
                                       scaled_polynomial_jacobian_singular_values=np.linalg.svd(
                                           jacobian(rows,a,c),compute_uv=False).tolist(),
                                       actual_positivity_margins=dict(sigma_A=float(sig),
                                           psi1_A=float(psi),W_A=float(wa),W_XR=float(wr)))
                            capacity = row["sampled_cap_only_displacement_ceiling_estimate"]
                            kD = row["sampled_curvature_times_diameter_estimate"]
                            retain("widest_cap",capacity,row)
                            retain("smallest_curvature",-kD,row)
                            if kD<100/3:
                                retain("widest_cap_under_sampled_curvature",capacity,row)
                            retain("geometry_tradeoff",min(capacity/.3,(100/3)/kD),row)
            emit("progress",right_offset=bo,counts=dict(count),
                 best_tradeoff=best.get("geometry_tradeoff",(None,))[0],
                 elapsed_seconds=time.perf_counter()-start)
        emit("terminal",choices={k:{"score":v[0],"candidate":v[1]} for k,v in best.items()},
             counts=dict(count),elapsed_seconds=time.perf_counter()-start,
             true_tail_values_are_limits=True,finite_N_complete=False,nonlinear_solved=False,
             README_completion_claim=False)
    except Exception as exc:
        emit("incomplete",reason=str(exc),counts=dict(count),elapsed_seconds=time.perf_counter()-start,
             partial_choices={k:{"score":v[0],"candidate":v[1]} for k,v in best.items()})
        raise


if __name__ == "__main__":
    main()
