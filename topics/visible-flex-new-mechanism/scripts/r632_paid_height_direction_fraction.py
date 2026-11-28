"""Exact endpoint feasibility of a new affine height direction from a paid strictly interior curve."""
from fractions import Fraction as F
from math import comb
import numpy as np
import sympy as sp
from r632_exact_pending_polynomial_frontier import FrontierBoxes, binary_rational, source_arrays, floored_fraction


class PaidHeightDirectionBoxes(FrontierBoxes):
    def height_fraction(self,graph,q,direction,maximum=1.,safety=.95):
        # The outer solver passes its accepted physical object; rejected candidate
        # evaluations cannot replace this original zero-endpoint certificate.
        accepted=self.accepted_curve
        if (not np.array_equal(accepted["shape_parameters"],q)
                or not accepted["physical_attainers"]["all_polynomial_hull_fields_in_original_box"]):
            return super().height_fraction(graph,q,direction,maximum,safety)
        if safety!=.95 or maximum!=1.:
            raise ValueError("The original .95 fraction and unit maximum are required")
        receipt={"state":"testing_new_affine_endpoints","current_q":np.asarray(q,float).tolist(),
                 "direction":np.asarray(direction,float).tolist(),"tested":[],"saved_strict_zero_endpoint_reused":True}
        self.fraction_receipts.append(receipt)
        basis,offset=source_arrays(graph,"h")
        low,high=F(4,5),F(3)
        x=sp.Symbol("t")
        cache={}
        def coefficients(cell):
            if cell not in cache:
                c,v=[],[]
                for i in range(basis.shape[0]):
                    a=F(0) if offset is None else binary_rational(offset[i,cell])
                    d=F(0)
                    for k in np.flatnonzero(basis[i,cell]):
                        factor=binary_rational(basis[i,cell,k])
                        a+=factor*binary_rational(q[k])
                        d+=factor*binary_rational(direction[k])
                    c.append(a)
                    v.append(d)
                cache[cell]=c,v
            return cache[cell]
        def test(exponent):
            step=F(1,2**exponent)
            trial={"power_of_two":-exponent,"Bernstein_cells":0,"Sturm_tests":0}
            receipt["tested"].append(trial)
            for cell in range(basis.shape[1]):
                graph.clock.check("before_new_exact_affine_height_endpoint_cell")
                c,v=coefficients(cell)
                h=[a+step*b for a,b in zip(c,v)]
                if min(h)>low and max(h)<high:
                    trial["Bernstein_cells"]+=1
                    continue
                if min(h[0],h[-1])<=low or max(h[0],h[-1])>=high:
                    trial.update(failed_cell=cell,failed_test="exact_endpoint")
                    return False
                n=len(h)-1
                powers=[sum(h[i]*comb(n,i)*comb(n-i,j-i)*(-1)**(j-i) for i in range(j+1))
                        for j in range(n+1)]
                polynomial=sp.Poly.from_list(powers[::-1],gens=x,domain=sp.QQ)
                for bound in (sp.Rational(4,5),sp.Integer(3)):
                    trial["Sturm_tests"]+=1
                    if (polynomial-bound).count_roots(0,1):
                        trial.update(failed_cell=cell,failed_test="exact_contact_or_crossing")
                        return False
            trial["strict_entire_height"]=True
            return True
        lo,hi=-1,0
        while not test(hi):
            lo=hi
            if hi==1074:
                if np.array_equal(np.asarray(q,float),np.asarray(q,float)+2.**-1074*np.asarray(direction,float)):
                    receipt.update(state="no_representable_trial_at_minimum_binary64_fraction",fraction=0.)
                    return 0.
                raise FloatingPointError("The minimum binary64 fraction still moves and has an unqualified height")
            hi=min(1074,max(1,2*hi))
        while hi-lo>1:
            mid=(lo+hi)//2
            if test(mid):hi=mid
            else:lo=mid
        answer=floored_fraction(2.**-hi)
        receipt.update(state="strict_trial_endpoint_and_convex_segment_certified",largest_tested_safe_power=-hi,
                       fraction=answer,all_rounded_trials_still_undergo_original_complete_boxes=True)
        return answer

