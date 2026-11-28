#!/usr/bin/env python3
"""R657 high adjacent modes and actual rigid-cap geometric requirements, only in public Actions.

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

from flint import arb, ctx
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


    ctx.prec = 192
    mode = None
    eta2 = None
    s = None
    bm = None

    def rho(x):
        t = np.exp(-x)
        return s*s*t*(1-t)-bm

    def neck_ball(sb,etab,bb):
        """Four new rigorous endpoint values, no prior numerical ODE replay."""
        disc = (1-4*bb/sb**2).sqrt()
        tl,tr = (1+disc)/2, (2*bb/sb**2)/(1+disc)
        beta,d = (etab+bb).sqrt(),(sb-1)/2
        def solutions(t):
            z = 2*sb*t
            def kummer(alpha,bparam):
                # For n>=128 the term ratio has absolute value <1/16 here.
                # Guard this directly at 128 using |alpha|, |b|, |z|.
                if not ((128+abs(alpha))*abs(z)*16 < (128-abs(bparam))*129):
                    raise ArithmeticError("Cannot enclose entire hypergeometric tail.")
                term = arb(1)
                total = arb(1)
                for n in range(128):
                    term = term*(alpha+n)*z/((bparam+n)*(n+1))
                    total += term
                first = term*(alpha+128)*z/((bparam+128)*129)
                count["ball_kummer_series"] += 1
                return total+arb(0,1)*(16*abs(first)/15)
            return [(-z/2).exp()*z**b*kummer(b-d,1+2*b) for b in (beta,-beta)]
        la,lb = solutions(tl)
        ra,rb = solutions(tr)
        d1 = (la*rb-lb*ra)/(2*beta)
        eta = etab.sqrt()
        d0 = (eta*(tl/tr).log()).sinh()/eta
        g = d1/d0
        if not g.is_finite() or not (g>0 and g<1):
            raise ArithmeticError("No rigorous positive finite neck upper bound.")
        lo,hi = g.lower().fmpq(),g.upper().fmpq()
        return dict(ball=g.str(24),dyadic_lower=str(lo),dyadic_upper=str(hi),
                    R655_strictly_impossible=bool(22*hi<7),permits_R655_neck=bool(22*lo>7))

    def algebraic_model(m):
        if m is None:
            sb = (684+95*arb(55).sqrt())/632
            return sb,(12*sb-19)/20,(5*sb-8)*(sb-2)/20
        h = 2*m+1
        d = arb(h)/(2*arb(2).sqrt()*(h+arb(2).sqrt()))
        return 2+d,arb(1)/4+(m*(m+1)*d)/(2*h),d**2/4+d/(2*h)

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
            out[:,1,:] = (eta2-np.asarray([0,1,mode,mode+1])**2*rho(x))[:,None]*matrices[:,0,:]
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

    def geometry(x,mat,left,right,a,c,ell_l,ell_r,rr):
        sig,psi,wr = radial(x,mat,a,c)
        rx = wr/sig**2
        r = psi/sig
        if min(np.min(rx),np.min(r),np.min(sig))<=0:
            return None
        tip_l = float(r[0]*math.exp(-ell_l))
        tip_r = math.exp(ell_r)
        physical_scale = .22/tip_r
        # Three exact chart pieces integrated on their own intervals.
        zl = np.linspace(0,ell_l,129)
        zr = np.linspace(-ell_r,0,129)
        rl,rrad = tip_l*np.exp(zl),tip_r*np.exp(zr)
        wlu,wru = wr[0]*zl/ell_l,-wr[-1]*zr/ell_r
        def integral(lval,cval,rval):
            return float(np.trapezoid(lval*rl,zl)+np.trapezoid(cval*rx,x)
                         +np.trapezoid(rval*rrad,zr))
        def arclength(scale):
            count["sampled_complete_meridian_quadratures"] += 1
            return integral(np.hypot(1,scale*wlu),np.hypot(1,scale*wr),np.hypot(1,scale*wru))
        min_cos=math.sqrt(1-(9/25)**2)
        chord=math.sqrt((tip_r-tip_l)**2+2*tip_r*tip_l*(1-min_cos))
        # The limiting derivative at the linear taper tip is w_cut/(r_tip*d).
        cap_scale=(physical_scale/.03)*min(tip_l*ell_l/wr[0],tip_r*ell_r/wr[-1])
        at_cap=arclength(cap_scale)
        # One physical vertical scale per root, solving the best-case chord
        # requirement with a 1% reserve in the required arclength excess.
        target=(tip_r-tip_l)+1.01*(chord-(tip_r-tip_l))
        low,high=0.,cap_scale
        for _ in range(64):
            if arclength(high)>=target:
                break
            high *= 2
        else:
            return None
        for _ in range(48):
            mid=(low+high)/2
            if arclength(mid)<target:
                low=mid
            else:
                high=mid
        scale=high
        w = scale*wr
        krc = -scale*rho(x)*sig*psi/(rx*(1+w*w)**1.5)
        ktc = w/(r*np.hypot(1,w))
        kl = w[0]/(ell_l*rl*(1+(scale*wlu)**2)**1.5)
        kr = -w[-1]/(ell_r*rrad*(1+(scale*wru)**2)**1.5)
        ktl = scale*wlu/(rl*np.hypot(1,scale*wlu))
        ktr = scale*wru/(rrad*np.hypot(1,scale*wru))
        kmax=float(max(abs(krc).max(),ktc.max(),kl.max(),abs(kr).max(),ktl.max(),ktr.max()))
        gauss_charts = [(name, radii, vals/(physical_scale**2)) for name,radii,vals in
                        (("left_taper",rl,kl*ktl),("center",r,krc*ktc),
                         ("right_taper",rrad,kr*ktr))]
        gauss_hits = []
        for name,radii,vals in gauss_charts:
            index = int(np.argmax(abs(vals)))
            gauss_hits.append((float(abs(vals[index])),name,float(radii[index]*physical_scale),
                               float(vals[index])))
        gauss_abs,gauss_chart,gauss_radius,gauss_signed = max(gauss_hits)
        # Monotone-r Clairaut paths are actual intrinsic paths; no
        # minimizing-geodesic claim is required by the chord test.
        chart_states=((rl,scale*wlu),(r,w),(rrad,scale*wru))
        chords = []
        for fraction in (0.,.5,.75):
            angular_momentum = fraction*tip_l
            lengths = [rad*np.hypot(1,ww)/np.sqrt(rad**2-angular_momentum**2)
                       for rad,ww in chart_states]
            angles = [angular_momentum*length/(rad**2)
                      for length,(rad,_) in zip(lengths,chart_states)]
            path_length=integral(*lengths)
            angle=integral(*angles)
            rhs=(tip_r-tip_l)**2+2*tip_l*tip_r*(1-math.cos(angle))
            rhs+=tip_l*tip_r*(1-min_cos)*(1+math.cos(angle))
            chords.append(dict(momentum_over_inner_radius=fraction,material_azimuth=angle,
                               physical_path_length=physical_scale*path_length,
                               sampled_squared_margin=(path_length**2-rhs)*physical_scale**2))
        count["sampled_oblique_path_quadratures"] += 2*len(chords)
        e=1+w*w
        sx=mat[0,1,0]+a*mat[0,1,1]
        fields=[]
        for index,j,ends in zip((2,3),(mode,mode+1),rr):
            gf,df=ends
            input_line=np.array([gf,a*gf+(c-a)*df])
            y,yx=np.einsum("ikx,k->ix",mat[index],input_line)
            f=y/sig
            fr=(yx-sx*f)/(sig*rx)
            normf=float(np.max(abs(f)))
            if not np.isfinite(normf) or normf==0:
                return None
            fields.append((f/normf,fr/normf,normf))
        (f,fr,nf),(g,gr,ng)=fields
        m,n=mode,mode+1
        qden=abs(fr-m*m*e*f/r)+abs(gr-n*n*e*g/r)
        rad=abs(fr)+abs(gr)
        ang=m*abs(f)+n*abs(g)
        qd=.5/(w*rad+np.sqrt((w*rad)**2+.5*(rad**2+e*(ang/r)**2)))
        qq=np.divide(w,2*qden,out=np.full_like(w,np.inf),where=qden>0)
        qseed=float(np.min(np.minimum(qq,qd)))
        j0=(r*fr*gr-n*n*fr*g-m*m*f*gr+2*m*n*f*g/r)/2
        boundary=w*(n*n*fr*g/(m*r)-m*m*f*gr/(n*r)-m*n*f*g/r**2)
        beta_c=float(-np.trapezoid(j0*rx/(w*r**2),x)-(boundary[-1]-boundary[0])/2)
        count["sampled_core_and_taper_points"] += len(x)+len(zl)+len(zr)
        return dict(a_B=float(a),psi1_log_slope_B=float(c),nu_B=float(c-a),
                    core_X=[left,right],core_cut_radii=[float(r[0]),float(r[-1])],
                    taper_lengths=[ell_l,ell_r],cap_radii=[tip_l,tip_r],
                    width_over_outer_radius=tip_l/tip_r,physical_scale_to_b_point22=physical_scale,
                    physical_R655_a=physical_scale*tip_l,R655_required_a=.07,
                    selected_vertical_scale=scale,taper_tip_curvature_scale_ceiling=cap_scale,
                    sampled_arclength_at_tip_curvature_ceiling=at_cap,
                    necessary_chord_at_sin_9_over_25=chord,sampled_arclength_at_selected_scale=arclength(scale),
                    sampled_physical_total_height=physical_scale*integral(scale*wlu,w,scale*wru),
                    sampled_physical_max_abs_curvature=kmax/physical_scale,
                    sampled_physical_curvature_ratio_to_100_over_3=.03*kmax/physical_scale,
                    sampled_intrinsic_gauss_ratio_to_reach_limit=.03**2*gauss_abs,
                    sampled_gauss_curvature_attainer=dict(chart=gauss_chart,
                        physical_radius=gauss_radius,signed_physical_Gaussian_curvature=gauss_signed),
                    sampled_intrinsic_reach_ceiling=1/math.sqrt(gauss_abs) if gauss_abs else None,
                    sampled_oblique_chord_margins=chords,
                    sampled_core_linear_QD_amplitude=qseed,core_mode_height_normalizations=[nf,ng],
                    sampled_core_own_adjacent_port_with_boundary=beta_c,
                    sampled_own_core_port_times_qseed_squared=beta_c*qseed*qseed,
                    actual_full_port=None,actual_nonlinear_angle=None,actual_finite_suffix_N=None)

    fixed_choices=[4,8,16,32,64]
    matches={}
    def retain(store,label,value,row):
        if label not in store or value>store[label][0]:
            store[label]=(float(value),row)
    def summarize():
        return {str(m):{k:{"score":w[0],"root":w[1]} for k,w in b.items()} for m,b in matches.items()}
    emit("provenance",run_id=os.environ["GITHUB_RUN_ID"],
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         previous_run_preserved=46132827514,previous_ODE_replay=False,
         scientific_wall_limit=args.max_seconds,ball_precision=ctx.prec)
    try:
        eligible=[]
        for number in [None,*fixed_choices]:
            sb,eb,bb=algebraic_model(number)
            report=neck_ball(sb,eb,bb)
            emit("sharp_neck",model="R652" if number is None else "R657",
                 m=2 if number is None else number,**report)
            if number is not None and report["permits_R655_neck"]:
                eligible.append(number)
        selected = eligible[:3]
        emit("selected",eligible=eligible,modes=selected,
             criterion="First up to three distinct adjacent pairs with rigorously G>7/22.")
        for mode in selected:
            before=dict(count)
            sb,eb,bb=algebraic_model(mode)
            s,eta2,bm=(float(t.mid().fmpq()) for t in (sb,eb,bb))
            eta=math.sqrt(eta2)
            tsmall=(2*bm/s**2)/(1+math.sqrt(1-4*bm/s**2))
            xl,xr=-math.log1p(-tsmall),-math.log(tsmall)
            best=matches[mode]={}
            for buff_right in (1/64,1/8):
                right=xr+buff_right/eta
                matrices=transfer(right,xl-1/(16*eta))
                at_xr=matrices(xr)
                for buff_left in (1/64,1/16):
                    left=xl-buff_left/eta
                    ml=matrices(left)
                    x=np.unique(np.r_[np.linspace(left,right,1025),xl,xr])
                    grid=matrices(x)
                    for ell_l in (1/8,1/4,1/2):
                        ll=[line(j,ell_l) for j in (mode,mode+1)]
                        for den in (4,8,12):
                            guard()
                            ell_r=math.pi**2/(2*den**2)
                            rr=[line(j,-ell_r) for j in (mode,mode+1)]
                            rows=cross_rows(ml,ll,rr)
                            count["geometries"]+=1
                            for a,c in solve_rows(rows):
                                if c<=a:
                                    continue
                                sig,psi,wa=radial(None,ml,a,c)
                                _,_,wb=radial(None,at_xr,a,c)
                                if min(sig,psi,wa,wb)<=1e-9:
                                    continue
                                res=transfer_residual(ml,a,c,ll,rr)
                                if max(abs(t) for t in res)>1e-6:
                                    continue
                                count["positive_projective_roots"]+=1
                                row=geometry(x,grid,left,right,a,c,ell_l,ell_r,rr)
                                if row is None:
                                    continue
                                row.update(mode_pair=[mode,mode+1],left_buffer_eta_units=buff_left,
                                           right_buffer_eta_units=buff_right,right_travel_sqrt2_denominator=den,
                                           Cauchy_determinant_residuals=res,
                                           radial_positivity_margins=list(map(float,(sig,psi,wa,wb))),
                                           jacobian_singular_values=np.linalg.svd(jacobian(rows,a,c),
                                                                                compute_uv=False).tolist())
                                width=row["width_over_outer_radius"]
                                curvature=row["sampled_physical_curvature_ratio_to_100_over_3"]
                                chord_ratio=row["sampled_arclength_at_tip_curvature_ceiling"]/row[
                                    "necessary_chord_at_sin_9_over_25"]
                                retain(best,"widest",width,row)
                                retain(best,"joint",min(width/(7/22),1/curvature,chord_ratio),row)
                                if width>7/22:
                                    retain(best,"lowest_curvature_above_neck",-curvature,row)
                                    if (row["sampled_intrinsic_gauss_ratio_to_reach_limit"]<=1 and
                                        min(t["sampled_squared_margin"] for t in
                                            row["sampled_oblique_chord_margins"])>=0):
                                        retain(best,"surviving_intrinsic_and_chord",-curvature,row)
            emit("mode_finished",mode=mode,
                 costs={k:v-before.get(k,0) for k,v in count.items() if v!=before.get(k,0)},
                 best={k:{"score":v[0],"root":v[1]} for k,v in best.items()},
                 elapsed_seconds=time.perf_counter()-start)
        emit("terminal",selected=selected,choices=summarize(),counts=dict(count),
             elapsed_seconds=time.perf_counter()-start,actual_angles_solved=False,
             actual_full_tail_root_certified=False,README_completion_claim=False)
    except Exception as exc:
        emit("incomplete",reason=str(exc),choices=summarize(),counts=dict(count),
             elapsed_seconds=time.perf_counter()-start)
        raise


if __name__=="__main__":
    main()
