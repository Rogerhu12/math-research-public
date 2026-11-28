"""Complete only unpaid Bernstein paths, using the exact represented coefficients."""
from fractions import Fraction as F
from math import comb
import numpy as np
import sympy as sp
import r632_adaptive_polynomial_boxes as adaptive

LD=adaptive.LD


def binary_rational(value):
    numerator,denominator=LD(value).as_integer_ratio()
    return F(int(numerator),int(denominator))


def source_arrays(graph,field):
    height=field in ("h","gamma")
    basis=(graph.h_coeff if height else graph.k_coeff)[0]
    if hasattr(graph,"background_h_coeff"):
        offset=(graph.background_h_coeff if height else graph.background_k_coeff)[0]
    else:
        offset=None if height else graph.k_coeff_offset[0]
    return basis,offset


def exact_field_cell(graph,q,alpha,length,field,cell):
    basis,offset=source_arrays(graph,field)
    c=[]
    for i in range(basis.shape[0]):
        v=F(0) if offset is None else binary_rational(offset[i,cell])
        for factor,parameter in zip(basis[i,cell],q):
            if factor!=0 and parameter!=0:
                v+=binary_rational(factor)*binary_rational(parameter)
        c.append(v)
    if field in ("gamma","upsilon"):
        width=binary_rational(graph.knots[cell+1])-binary_rational(graph.knots[cell])
        c=[(len(c)-1)*(b-a)/width for a,b in zip(c,c[1:])]
    scale=F(1)
    if field in ("k","upsilon"):
        scale*=binary_rational(alpha)
    if field in ("gamma","upsilon"):
        scale/=binary_rational(length)
    c=[v*scale for v in c]
    n=len(c)-1
    # Convert the exact Bernstein coefficients to ascending powers.
    return [sum(c[i]*comb(n,i)*comb(n-i,j-i)*(-1)**(j-i) for i in range(j+1))
            for j in range(n+1)]


def floored_fraction(cap,maximum=1.):
    """The original .95 safety factor and directed binary64 conversion."""
    fraction=min(LD(maximum),adaptive.down(LD(.95)*LD(cap)))
    answer=float(fraction)
    if LD(answer)>fraction:
        answer=float(np.nextafter(answer,-np.inf))
    return max(0.,answer)


class FrontierBoxes:
    def __init__(self,ordinary,accepted_q,accepted_alpha,accepted_length,accepted_qualification):
        self.ordinary=ordinary
        self.cache={self.key(accepted_q,accepted_alpha,accepted_length):accepted_qualification}
        self.latest=None
        self.receipts=[]
        self.fraction_receipts=[]

    def __getattr__(self,name):
        return getattr(self.ordinary,name)

    @staticmethod
    def key(q,alpha,length):
        return (np.asarray(q,float).tobytes(),adaptive.ld_text(alpha),adaptive.ld_text(length))

    @property
    def latest_record(self):
        return self.latest

    def close(self,graph,q,alpha,length,source):
        """Original closed paths/fields remain paid. Exact tests only on remaining paths."""
        self.latest=record={**source,"fields":dict(source["fields"])}
        inflight=source["inflight_polynomial_field"]
        field=inflight["field"]
        limits={"h":(F(4,5),F(3)),"k":(F(-2),F(2)),"gamma":(F(-6),F(6)),"upsilon":(F(-6),F(6))}
        lower,upper=limits[field]
        leaves=inflight["unresolved_frontier"]
        receipt={"field":field,"previous_closed_leaves":inflight["certified_leaves"],
            "previous_processed_nodes":inflight["processed_nodes"],"previous_frontier_size":len(leaves),
            "new_exact_path_results":[],"state":"pending","next_frontier_index":0}
        self.receipts.append(receipt)
        record["exact_remaining_frontier"]=receipt
        cache={}
        x=sp.Symbol("t")
        def rr(v):
            return sp.Rational(v.numerator,v.denominator)
        for index,leaf in enumerate(leaves):
            graph.clock.check("before_exact_represented_pending_path")
            cell,depth,path=(leaf[k] for k in ("cell","depth","path"))
            receipt["next_frontier_index"]=index
            if cell not in cache:
                coeffs=exact_field_cell(graph,q,alpha,length,field,cell)
                poly=sp.Poly.from_list([rr(v) for v in coeffs[::-1]],gens=x,domain=sp.QQ)
                cache[cell]=(poly-rr(lower),-poly+rr(upper))
            left,right=sp.Rational(path,2**depth),sp.Rational(path+1,2**depth)
            item={"cell":cell,"depth":depth,"path":path,"tests":[]}
            receipt["new_exact_path_results"].append(item)
            for bound,Q in zip(("lower","upper"),cache[cell]):
                for point in (left,right):
                    value=Q.eval(point)
                    if value<=0:
                        item["witness"]={"bound":bound,"local_rational":str(point),"signed_value":str(value)}
                        break
                if "witness" in item:
                    break
                roots=int(Q.count_roots(left,right))
                item["tests"].append({"bound":bound,"endpoints_strictly_positive":True,
                                      "exact_real_root_count":roots})
                if roots:
                    item["witness"]={"bound":bound,"point_with_boundary_equality_exists_in":[str(left),str(right)]}
                    break
            if "witness" in item:
                receipt.update(state="actual_point_violation",next_frontier_index=index+1)
                record["fields"][field]={**inflight,"state":"actual_point_violation","exact_witness":item}
                record["state"]="actual_point_violation"
                return record
            item["strict_on_entire_path"]=True
        receipt.update(state="all_remaining_paths_strict",next_frontier_index=len(leaves))
        record["fields"][field]={**inflight,"state":"certified_represented_polynomial",
            "certified_leaves":inflight["certified_leaves"]+len(leaves),"exact_frontier_result":receipt,
            "original_pending_partition_retained":True}
        missing=source.get("unevaluated_fields",[])
        if missing:
            coefficients=self.ordinary.physical_coefficients(graph,q,alpha,length)
            for name in missing:
                qualification,_=self.ordinary.certify_field(name,coefficients[name])
                record["fields"][name]=qualification
                if qualification["state"]=="pending":
                    partial={**record,"inflight_polynomial_field":qualification,
                             "unevaluated_fields":missing[missing.index(name)+1:],"state":"pending"}
                    return self.close(graph,q,alpha,length,partial)
                if qualification["state"]!="certified_represented_polynomial":
                    record["state"]=qualification["state"]
                    return record
        record.update(state="all_four_represented_polynomial_fields_certified",unevaluated_fields=[])
        return record

    def certify(self,graph,q,alpha,length):
        key=self.key(q,alpha,length)
        if key in self.cache:
            self.latest=self.cache[key]
            return self.latest
        source=self.ordinary.certify(graph,q,alpha,length)
        self.latest=source if source["state"]!="pending" else self.close(graph,q,alpha,length,source)
        return self.latest

    def height_fraction(self,graph,q,direction,maximum=1.,safety=.95):
        try:
            return self.ordinary.height_fraction(graph,q,direction,maximum,safety)
        except adaptive.PolynomialPhysicalPending as exc:
            rec=exc.record
            value=rec.get("safe_cap_LD_decimal")
            if rec.get("reason")!="affine_height_fraction_refinement_budget" or value is None or LD(value)<=0:
                raise
            answer=floored_fraction(value,maximum)
            self.fraction_receipts.append({"source_safe_cap":value,"source_possible_cap":rec.get("possible_cap_LD_decimal"),
                "processed_nodes":rec.get("processed_nodes"),"reached_depth":rec.get("reached_depth"),
                "previous_queue_size":len(rec.get("unresolved_frontier",[])),"fraction":answer,
                "used_proven_safe_cap_without_a_99_percent_maximality_requirement":True})
            return answer
