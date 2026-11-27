#!/usr/bin/env python3
"""Actual full47 third-kind values by bounded RR and short local Cartier.

The old836 cusp API is not enlarged.  A single original Gaussian length4513
torsion grid supplies73 genuine rational local charts and ALL requested
meromorphic numerators.  All mathematics is restricted to public Actions.
"""
import hashlib
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REPO="Rogerhu12/math-research-public"
REQUEST=ROOT/(PRE+"notes/full-p47-short-Cartier-third-kind-request.json")
WORKER=PRE+"scripts/full_p47_Cartier_support.py"
GRADED=PRE+"scripts/full_p47_graded_RR_source.py"
RR_REQUEST=PRE+"notes/full-p47-graded-RR-source-request.json"
HODGE_REQUEST=PRE+"notes/full-p47-CM-height-move-request.json"
GAUSSIAN=PRE+"scripts/full_p47_Gaussian_CM_log.py"
P,Q,PREC=47,4513,836
IDS=[0,76,77,100,108,141,196,220]
START=time.monotonic()
DEADLINE=None
SOURCE=None
REQUEST_HASH=None
STAGE="preflight"
COMPLETED=[]
PREPARED=[]
FAILURES=[]
SHARED=None

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,Cartier_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def ci_only():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Mathematics is restricted to the original public Actions.")

def check():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("The declared original Cartier reserve was reached.")

def stop(signum,frame):
    raise TimeoutError("The declared original Cartier reserve was reached.")

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def integral_rows(M):
    return [[int(a) for a in row] for row in M.rows()]

def row_hash(M):
    return digest(integral_rows(M))

class ResidueRR:
    def __init__(self,graded,data,req):
        from sage.all import matrix,vector,PolynomialRing,GF
        self.matrix,self.vector=matrix,vector
        self.K=graded["source"]["K"]
        self.ring=graded["ring"]
        self.M=graded["matrices"]
        self.pairs=graded["product_pairs"]
        self.cusp=graded["cusp_values"]
        self.kernel=graded["source"]["kernel"]
        self.cusp_kernel3=graded["cusp_vanishing_kernels"][3]
        self.descriptors=graded["source"]["descriptors"]
        self.data=data
        if (data["protocol"]!="full-p47-short-Cartier-support-v1" or
            data["prime"]!=P or data["coefficient_prime"]!=Q or
            data["descriptor_sha256"]!=digest(self.descriptors)):
            raise ArithmeticError("The actual residue packet belongs to another source.")
        if vector(self.K,list(self.cusp[1].row(0)))!=vector(
                self.K,list(self.M[1].column(0))):
            raise ArithmeticError("The declared cusp0 differs from the standard836 jet.")
        self.cols5=list(self.M[5].pivots())
        if len(self.cols5)!=763:
            raise ArithmeticError("The original V5 injection lost rank.")
        self.points={}
        self.fields={}
        for row in data["fields"]:
            fid=str(row["id"])
            degree=int(row["degree"])
            if degree==1:
                field=self.K
            else:
                pr=PolynomialRing(self.K,"z")
                modulus=pr([int(a)%Q for a in row["modulus"]])
                if modulus.degree()!=degree or not modulus.is_monic() or not modulus.is_irreducible():
                    raise ArithmeticError("The original closed-field modulus changed.")
                field=GF(Q**degree,name="z_"+fid,modulus=modulus)
            self.fields[fid]=(field,degree)
        for row in data["points"]:
            field,d=self.fields[str(row["field_id"])]
            f=int(row["degree"])
            if not 1<=f<=159 or d%f:
                raise ArithmeticError("The actual closed support degree is invalid.")
            def decode(coeff):
                if d==1:
                    if any(int(a)%Q for a in coeff[1:]):
                        raise ArithmeticError("An input prime-field value is not constant.")
                    return field(int(coeff[0])%Q if coeff else 0)
                return field([int(a)%Q for a in coeff])
            v=[decode(a) for a in row["values95"]]
            dv=[decode(a) for a in row["derivatives95"]]
            frame=decode(row["differential_frame"])
            pivot=int(row["projective_pivot"])
            e=int(row["effective_stabilizer"])
            if (len(v)!=95 or len(dv)!=95 or not 0<=pivot<95 or
                v[pivot]!=1 or dv[pivot] or not frame or
                e not in (1,2,3) or row["power_series_order"]!=2*e-1 or
                row["uniformizer"]!=("heat_u" if e==1 else "j-j_support")):
                raise ArithmeticError("The actual projective residue jet is incomplete.")
            if any(x**(Q**f)!=x for x in v):
                raise ArithmeticError("Actual point ratios failed closed-field descent.")
            value,derivative=self.product_values(field,v,dv)
            self.add_point(str(row["id"]),{"field":field,"ambient_degree":d,
                "degree":f,"values":value,"derivatives":derivative,"frame":frame,
                "is_cusp":False,"effective_stabilizer":e})
        # All23 actual cusp frames, including the width47.  Only length2 is read.
        engine=graded["source"]["engine"]
        cusp_receipts=[]
        for b in range(1,24):
            jets=engine.jets(self.descriptors,length=2,root=pow(2,b,Q))
            v=list(jets.column(0))
            dv=list(jets.column(1))
            if vector(self.K,v)!=self.cusp[1].row(b-1):
                raise ArithmeticError("A cusp first jet changed its original constant.")
            value,derivative=self.product_values(self.K,v,dv)
            self.add_point("cusp_%d"%(b-1),{"field":self.K,"ambient_degree":1,
                "degree":1,"values":value,"derivatives":derivative,"frame":None,
                "is_cusp":True,"effective_stabilizer":1})
            cusp_receipts.append({"cusp":b-1,"first95_sha256":digest(
                [[int(v[i]),int(dv[i])] for i in range(95)])})
        self.cusp_first_receipt=cusp_receipts
        self.center_ids=[int(r["candidate_id"]) for r in data["centers"]]
        if self.center_ids!=IDS:
            raise ArithmeticError("The eight original target order changed.")
        self.target_values={1:[] ,2:[],3:[]}
        self.target_frames=[]
        coarse_rows=[]
        for row in data["centers"]:
            v=[self.K(a) for a in row["ratio_values"]]
            dv=[self.K(a) for a in row["ratio_dz"]]
            coarse=[self.K(a) for a in row["coarse_values95"]]
            frame=self.K(row["differential_frame"])
            pivot=int(row["denominator_index"])
            if (row["coarse_parameter"]!="j-j_CM" or len(v)!=95 or len(dv)!=95 or
                len(coarse)!=95 or not frame or v[pivot]!=1 or dv[pivot] or
                [frame*x for x in v]!=coarse or
                digest([int(x) for x in coarse])!=req[
                    "certified_CM_tangent95_sha256"][str(row["candidate_id"])]):
                raise ArithmeticError("An original target frame changed its normalized tangent.")
            value,_=self.product_values(self.K,v,dv)
            for n in (1,2,3):
                self.target_values[n].append(value[n])
            self.target_frames.append(frame)
            coarse_rows.append(coarse)
        self.TV={n:matrix(self.K,self.target_values[n]).transpose() for n in (1,2,3)}
        self.target_Hodge=matrix(self.K,coarse_rows)*self.kernel.transpose()
        self.cases=self.build_cases(data,req)
        self.select_probes(data)
        self.input_receipt={"descriptor_sha256":digest(self.descriptors),
            "support_packet_sha256":digest(data),
            "all_cusp_first_jets_sha256":digest(cusp_receipts),
            "target_Hodge_values_sha256":row_hash(self.target_Hodge),
            "probe_receipt":self.probe_receipt,
            "cases":[r["id"] for r in self.cases]}

    def add_point(self,pid,row):
        if pid in self.points:
            raise ArithmeticError("An actual support identifier is repeated.")
        self.points[pid]=row

    def product_values(self,field,values,derivatives):
        if len(values)!=95 or len(derivatives)!=95:
            raise ArithmeticError("An original section jet has the wrong size.")
        vv={1:self.vector(field,values)}
        dd={1:self.vector(field,derivatives)}
        for n in (2,3):
            vv[n]=self.vector(field,[
                vv[n-1][a]*vv[1][b] for a,b in self.pairs[n]])
            dd[n]=self.vector(field,[
                dd[n-1][a]*vv[1][b]+vv[n-1][a]*dd[1][b]
                for a,b in self.pairs[n]])
        return vv,dd

    def build_cases(self,data,req):
        def image(cm,c):
            rows=data["angle_images"]["%d:%d"%(cm,c)]
            out={str(pid):int(m) for pid,m in rows}
            if len(out)!=len(rows) or any(m<=0 for m in out.values()):
                raise ArithmeticError("An original angle cycle is invalid.")
            if sum(self.points[pid]["degree"]*m for pid,m in out.items())!=(24 if c==0 else 48):
                raise ArithmeticError("An original raw angle degree changed.")
            return out
        def combine(terms):
            result={}
            for c,divisor in terms:
                for pid,m in divisor.items():
                    result[pid]=result.get(pid,0)+c*m
            return {pid:m for pid,m in result.items() if m}
        cusp={"cusp_%d"%b:1 for b in range(23)}
        allcases={}
        for cm in IDS:
            za=combine([(39,image(141,20)),(12,image(141,5)),(52,image(0,4)),
                        (48,cusp),(-156,image(cm,0)),(-48,image(cm,2))])
            zb=combine([(-21,image(141,20)),(8,image(0,12)),(-28,image(0,4)),
                        (48,cusp),(-24,image(cm,4)),(84,image(cm,0))])
            for name,weights in (("ZA",za),("ZB",zb)):
                if sum(self.points[pid]["degree"]*m for pid,m in weights.items()):
                    raise ArithmeticError("An original cleared divisor has nonzero degree.")
                if any(weights.get("cusp_%d"%b)!=48 for b in range(23)):
                    raise ArithmeticError("The complete cusp coefficient was lost.")
                key="%d-%s"%(cm,name)
                allcases[key]={"id":key,"candidate_id":cm,"angle":name,
                    "weights":weights,"clearing_denominator":6}
        wanted=req["cases"]
        consumed=req.get("already_completed_case_ids",[])
        active=req.get("other_active_case_ids",[])
        if (len(set(wanted))!=len(wanted) or not wanted or
            any(k not in allcases for k in wanted) or
            any(k not in allcases for k in consumed+active) or
            set(wanted)&(set(consumed)|set(active))):
            raise RuntimeError("The requested new case set is invalid or repeats completed values.")
        return [allcases[k] for k in wanted]

    def select_probes(self,data):
        rows=data["gaussian_free"]
        model=data["gaussian_model"]
        if (model["A"]!=343 or model["B"]!=0 or model["P"]!=[653,525] or
            model["Q"]!=[3860,232] or model["i"]!=95 or model["weil_root"]!=2 or
            model["free_coarse_count"]!=528 or len(rows)<312 or
            model["retained_common_sha256"]!=digest(rows)):
            raise ArithmeticError("The shared Gaussian probe source changed.")
        self.k0=self.K(-3)/(self.K(4)*self.K(343)**2)
        all_values=self.matrix(self.K,[r["values95"] for r in rows])
        all_E=self.k0*all_values*self.kernel.transpose()
        pivots=list(all_E.transpose().pivots())
        if len(pivots)!=73:
            raise ArithmeticError("The proven Gaussian Hodge evaluation supply lost rank73.")
        self.probes=[rows[i] for i in pivots]
        self.E=all_E.matrix_from_rows(pivots)
        if not self.E.det():
            raise ArithmeticError("The selected original Cartier evaluation matrix is singular.")
        self.E_inverse=self.E.inverse()
        self.PV={1:all_values.matrix_from_rows(pivots).transpose()}
        for n in (2,3):
            self.PV[n]=self.matrix(self.K,len(self.pairs[n]),73,lambda i,j:
                self.PV[n-1][self.pairs[n][i][0],j]*self.PV[1][self.pairs[n][i][1],j])
        self.probe_receipt={"retained_candidates":len(rows),"selected_rows":pivots,
            "selected_Cartans":[r["Cartan"] for r in self.probes],
            "selected_frames_sha256":digest([r["frame"] for r in self.probes]),
            "selected95_values_sha256":row_hash(self.PV[1]),
            "Hodge_evaluation_sha256":row_hash(self.E),
            "Hodge_evaluation_determinant":int(self.E.det()),
            "physical_parameter":"B","KS_constant":int(self.k0)}

    def coordinates(self,value,field,degree):
        if degree==1:
            return [self.K(value)]
        polynomial=field(value).polynomial()
        return [self.K(polynomial[i]) for i in range(degree)]

    def prime_value(self,value,field,degree):
        coeff=self.coordinates(value,field,degree)
        if any(coeff[1:]):
            return None
        return int(coeff[0])

    def multiplication(self,M,poly):
        check()
        rows=[]
        for row in M.rows():
            out=self.ring(list(row))._mul_trunc_(poly,PREC)
            rows.append([out[k] for k in range(PREC)])
        return self.matrix(self.K,rows)

    def choose_f(self,WS,support,case_id):
        """Deterministic avoidance of fewer than q proper linear conditions."""
        conditions=[]
        for pid in support:
            point=self.points[pid]
            field=point["field"]
            values=WS.change_ring(field)*point["derivatives"][2]
            conditions.append((pid,field,point["ambient_degree"],values))
        for j in range(8):
            conditions.append(("center_%d"%IDS[j],self.K,1,WS*self.TV[2].column(j)))
        for j in range(73):
            conditions.append(("probe_%d"%j,self.K,1,WS*self.PV[2].column(j)))
        if len(conditions)>=Q or len(conditions)>240:
            raise ArithmeticError("The proved deterministic section bound changed.")
        if any(not any(values) for _,_,_,values in conditions):
            raise ArithmeticError("A supposedly proper nonzero section condition is identically zero.")
        coeff=self.vector(self.K,[0]*WS.nrows())
        evaluations=[field.zero() for _,field,_,_ in conditions]
        adjustments=[]
        for j,(label,field,degree,values) in enumerate(conditions):
            check()
            if evaluations[j]:
                continue
            index=next(i for i,a in enumerate(values) if a)
            forbidden={0}
            for k in range(j):
                _,fk,dk,vk=conditions[k]
                if vk[index]:
                    candidate=self.prime_value(-evaluations[k]/vk[index],fk,dk)
                    if candidate is not None:
                        forbidden.add(candidate)
            c=next(c for c in range(len(conditions)+1) if c not in forbidden)
            coeff[index]+=self.K(c)
            for k,(_,fk,_,vk) in enumerate(conditions):
                evaluations[k]+=fk(c)*vk[index]
            if any(not evaluations[k] for k in range(j+1)):
                raise ArithmeticError("Deterministic section adjustment lost an earlier condition.")
            adjustments.append([j,index,c])
        f=coeff*WS
        if not any(f) or any(not x for x in evaluations):
            raise ArithmeticError("The deterministic original f was not completed.")
        for pid in support:
            point=self.points[pid]
            if self.vector(point["field"],list(f))*point["values"][2]:
                raise ArithmeticError("The chosen f failed its exact support vanishing.")
        return f,{"nonzero_conditions":len(conditions),
                  "adjustments_sha256":digest(adjustments),
                  "chosen_f_sha256":digest([int(x) for x in f])}

    def prepare_case(self,case):
        check()
        support=sorted(case["weights"])
        s=sum(self.points[pid]["degree"] for pid in support)
        bound=159 if case["angle"]=="ZA" else 151
        if not 0<s<=bound:
            raise ArithmeticError("The original reduced support exceeds its proved bound.")
        rows=[]
        for pid in support:
            point=self.points[pid]
            field,d=point["field"],point["ambient_degree"]
            vals=point["values"][2]
            coords=[self.coordinates(x,field,d) for x in vals]
            rows.extend([[coords[j][i] for j in range(262)] for i in range(d)])
        constraints=self.matrix(self.K,rows)
        if constraints.rank()!=s:
            raise ArithmeticError("The full reduced support evaluation has the wrong degree.")
        WS=constraints.right_kernel().basis_matrix()
        if WS.nrows()!=262-s:
            raise ArithmeticError("The actual support ideal has the wrong RR dimension.")
        f,selection=self.choose_f(WS,support,case["id"])
        fpoly=self.ring(list(f*self.M[2]))
        denominator=self.multiplication(self.M[3],fpoly).matrix_from_columns(self.cols5)
        if denominator.rank()!=429:
            raise ArithmeticError("Multiplication by the original f lost injectivity.")
        annihilator=denominator.right_kernel().basis_matrix().transpose()
        if annihilator.ncols()!=334:
            raise ArithmeticError("The V5 quotient has the wrong dimension.")
        numerator_space=self.cusp_kernel3
        target=72+s
        used=0
        for w in WS.rows():
            check()
            if numerator_space.nrows()==target:
                break
            wp=self.ring(list(w*self.M[2]))
            images=self.multiplication(numerator_space*self.M[3],wp)
            condition=images.matrix_from_columns(self.cols5)*annihilator
            coefficient_kernel=condition.left_kernel().basis_matrix()
            numerator_space=(coefficient_kernel*numerator_space).row_space().basis_matrix()
            used+=1
            if numerator_space.nrows()<target:
                raise ArithmeticError("The complete meromorphic colon fell below RR.")
            emit("Cartier_colon_progress",id=case["id"],constraints_used=used,
                 dimension=int(numerator_space.nrows()),target=target)
        if numerator_space.nrows()!=target:
            raise ArithmeticError("The complete WS colon did not reach the exact RR dimension.")
        residue_rows=[]
        residue_target=[]
        for pid in support:
            point=self.points[pid]
            field,d=point["field"],point["ambient_degree"]
            ff=self.vector(field,list(f))*point["derivatives"][2]
            if not ff:
                raise ArithmeticError("The original f is not simple at a support point.")
            if point["is_cusp"]:
                rr=(numerator_space.change_ring(field)*point["derivatives"][3])*(field(47)/ff)
            else:
                rr=(numerator_space.change_ring(field)*point["values"][3])*(point["frame"]/ff)
            if any(x**(Q**point["degree"])!=x for x in rr):
                raise ArithmeticError("Actual residues failed their complete closed-point descent.")
            values=[self.coordinates(x,field,d) for x in rr]
            target_values=self.coordinates(field(case["weights"][pid]),field,d)
            residue_rows.extend([[values[j][i] for j in range(target)] for i in range(d)])
            residue_target.extend(target_values)
        R=self.matrix(self.K,residue_rows)
        rhs=self.vector(self.K,residue_target)
        if R.rank()!=s-1 or R.right_kernel().dimension()!=73:
            raise ArithmeticError("The full residue map did not have its exact RR rank.")
        coefficients=R.solve_right(rhs)
        if R*coefficients!=rhs:
            raise ArithmeticError("The specified integer residues were not exactly solved.")
        h=coefficients*numerator_space
        target_f=f*self.TV[2]
        target_h=h*self.TV[3]
        probe_f=f*self.PV[2]
        probe_h=h*self.PV[3]
        if any(not a for a in target_f) or any(not a for a in probe_f):
            raise ArithmeticError("The chosen meromorphic denominator met a reading point.")
        target_rho=[self.target_frames[j]*target_h[j]/target_f[j] for j in range(8)]
        probe_rho=[self.k0*probe_h[j]/probe_f[j] for j in range(73)]
        certificate={"id":case["id"],"reduced_support_degree":s,
            "original_cleared_divisor_sha256":digest(case["weights"]),
            "support_ideal_dimension":int(WS.nrows()),"support_ideal_sha256":row_hash(WS),
            "section_selection":selection,"colon_constraints_used":used,
            "numerator_dimension":int(numerator_space.nrows()),
            "numerator_space_sha256":row_hash(numerator_space),
            "residue_rank":int(R.rank()),"residue_matrix_sha256":row_hash(R),
            "all_original_cusps_included":True,
            "h_coefficients_sha256":digest([int(x) for x in h]),
            "target_rho_sha256":digest([int(x) for x in target_rho])}
        emit("actual_meromorphic_RR_input",**certificate)
        return {"case":case,"f":[int(x) for x in f],"h":[int(x) for x in h],
            "target_rho":[int(x) for x in target_rho],
            "probe_f":[int(x) for x in probe_f],
            "probe_h":[int(x) for x in probe_h],
            "probe_rho":[int(x) for x in probe_rho],
            "certificate":certificate}

def original_reynolds_series(S,values,descriptors,frame):
    """Exact two phases on an arbitrary free Gaussian necklace."""
    a,b,c,d=frame
    transformed={key:values[((a*key[0]+b*key[1])%P,
                             (c*key[0]+d*key[1])%P)] for key in values}
    grouped={}
    for index,(phase,rc,rd) in enumerate(descriptors):
        grouped.setdefault((int(rc),int(rd)),[]).append((index,int(phase)))
    norms={h:[] for h in range(1,P)}
    for x,y in sorted(values):
        if (x,y)<((-x)%P,(-y)%P):
            norms[(x*x+y*y)%P].append((x,y))
    if any(len(v)!=24 for v in norms.values()):
        raise ArithmeticError("The full original norm half-fibre changed.")
    zeta=[S.field(pow(2,h,Q)) for h in range(P)]
    result=[None]*95
    for rc,rd in grouped:
        check()
        first={}
        second={}
        for h,labels in norms.items():
            left_sum=S.zero
            right_sum=S.zero
            for x,y in labels:
                v=transformed[x,y]
                right=transformed[((rd*x-rc*y)%P,(rc*x+rd*y)%P)]
                left_sum+=2*S.mul(v,right)
                if rc and rd:
                    conjugate=transformed[((rd*x+rc*y)%P,(-rc*x+rd*y)%P)]
                    right_sum+=2*S.mul(v,conjugate)
            first[h]=left_sum
            # These are identities of the full odd G1 source, NOT a deletion
            # of pure-imaginary descriptors or of their second phase.
            second[h]=(left_sum if not rc else (-left_sum if not rd else right_sum))
        for index,phase in grouped[rc,rd]:
            value=S.zero
            for h in range(1,P):
                value+=zeta[phase*h%P]*first[h]+zeta[-phase*h%P]*second[h]
            result[index]=value.truncate(Q)
    if any(f is None for f in result):
        raise ArithmeticError("The complete original95 free-frame source is missing.")
    return result

def frame_worker(index):
    """Only the Sage parent is forked; no wheel FLINT exists in this process."""
    check()
    from sage.all import vector
    state=SHARED
    S=state["series"]
    probe=state["probes"][index]
    forms=original_reynolds_series(S,state["grid"],state["descriptors"],probe["frame"])
    constants=[int(f[0]) for f in forms]
    if constants!=probe["values95"]:
        raise ArithmeticError("The long original frame differs from its actual finite value.")
    high=[int(S.mul(state["KS"],f)[Q-1]) for f in forms]
    hodge_high=state["kernel"]*vector(S.field,high)
    p2=[S.mul(forms[a],forms[b]) for a,b in state["pairs"][2]]
    p3=[S.mul(p2[a],forms[b]) for a,b in state["pairs"][3]]
    def combination(coefficients,polynomials):
        result=S.zero
        for a,poly in zip(coefficients,polynomials):
            if a:
                result+=S.field(a)*poly
        return result.truncate(Q)
    case_rows=[]
    for prepared in state["prepared"]:
        check()
        f=combination(prepared["f"],p2)
        h=combination(prepared["h"],p3)
        if (int(f[0])!=prepared["probe_f"][index] or
            int(h[0])!=prepared["probe_h"][index] or not f[0]):
            raise ArithmeticError("A global meromorphic numerator changed at a probe.")
        rho=S.mul(state["KS"],S.div(h,f))
        if int(rho[0])!=prepared["probe_rho"][index]:
            raise ArithmeticError("The actual KS meromorphic constant changed.")
        case_rows.append({"id":prepared["case"]["id"],
            "Cartier_difference_value":int(rho[Q-1]-rho[0]),
            "rho_constant":int(rho[0]),"rho_top":int(rho[Q-1])})
    payload={"index":index,"Cartan":probe["Cartan"],
        "frame":probe["frame"],"source_constants_sha256":digest(constants),
        "Hodge_Cartier_values":[int(x) for x in hodge_high],"cases":case_rows}
    emit("actual_short_Cartier_frame",index=index,Cartan=probe["Cartan"],
         case_count=len(case_rows),frame_values_sha256=digest(payload))
    return payload

def main():
    global SOURCE,REQUEST_HASH,DEADLINE,STAGE,SHARED
    ci_only()
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The new Cartier request pin changed.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-short-Cartier-third-kind-v1" or
        req["prime"]!=P or req["coefficient_prime"]!=Q or
        req["sage_version"]!="10.6" or req["python_flint_version"]!="0.9.0" or
        req["jet_length"]!=PREC or req["local_length"]!=Q or
        req["maximum_workers"] not in (1,2,3,4)):
        raise RuntimeError("Unexpected original bounded Cartier request.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("A pinned original source changed: "+path)
    required={WORKER,GRADED,RR_REQUEST,HODGE_REQUEST,GAUSSIAN,
        PRE+"scripts/full_p47_short_Cartier_third_kind.py",
        PRE+"scripts/full_p47_Miller_support.py",
        PRE+"scripts/full_p47_eight_CM_tangents.py",
        PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py",
        PRE+"scripts/original_p47_cuspidal_disks.py",
        PRE+"scripts/full_p47_weight_one_Hodge_certificate.py",
        PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json",
        PRE+"results/R1118-original-short-Cartier-reading-for-CM-third-kind-values.md",
        PRE+"notes/2026-11-27-full-p47-short-Cartier-third-kind-method.md",
        "README.md",PRE+"README.md"}
    if not required.issubset(req["source_sha256"]):
        raise RuntimeError("An original Cartier dependency is not pinned.")
    total=int(req["total_seconds"])
    reserve=int(req["reserve_seconds"])
    if not 120<=total<=18000 or not 30<=reserve<total:
        raise RuntimeError("The declared finite budget is invalid.")
    DEADLINE=START+total-reserve
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    source_module=load("Cartier_source_head",PRE+"scripts/full_p47_weight_one_Hodge_certificate.py")
    SOURCE=source_module.source_head()
    scratch=Path(os.environ.get("RUNNER_TEMP","/tmp"))/(
        "original-p47-Cartier-"+os.environ.get("GITHUB_RUN_ID","unknown"))
    scratch.mkdir(parents=True,exist_ok=True)
    support_path=scratch/"actual-Cartier-support.json"
    STAGE="original_residue_support_fresh_process"
    command=[sys.executable,str(ROOT/WORKER),"--request",str(REQUEST),
             "--output",str(support_path),"--seconds",
             str(min(int(req["field_worker_seconds"]),
                     max(1,int(DEADLINE-time.monotonic()))))]
    completed=subprocess.run(command,check=False,timeout=max(1,DEADLINE-time.monotonic()))
    if completed.returncode:
        raise RuntimeError("The isolated original residue worker did not complete.")
    data=json.loads(support_path.read_text())
    emit("actual_Cartier_support_input",source=SOURCE,request_sha256=REQUEST_HASH,
         input_sha256=digest(data),family_receipts=data["family_receipts"],
         target_jet_receipt=data["target_jet_receipt"],gaussian_model=data["gaussian_model"])
    # The pure FLINT subprocess has exited.  Only now is Sage imported.
    from sage.all import matrix,vector,PolynomialRing,proof,identity_matrix
    from sage.env import SAGE_VERSION
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong pinned Sage release.")
    proof.all(True)
    STAGE="consume_original_graded_source"
    rr=load("Cartier_original_graded_ring",GRADED)
    rr.DEADLINE=DEADLINE
    graded=rr.build_graded_source(json.loads((ROOT/RR_REQUEST).read_text()),
                                  expected_certificate=req["graded_certificate"])
    arithmetic=ResidueRR(graded,data,req)
    emit("original_Cartier_inputs_ready",source=SOURCE,request_sha256=REQUEST_HASH,
         input_receipt=arithmetic.input_receipt,
         graded_certificate_sha256=digest(graded["certificate"]),
         scope="New third-kind values only; completed Miller cases are excluded.")
    STAGE="new_original_meromorphic_RR"
    for case in arithmetic.cases:
        try:
            PREPARED.append(arithmetic.prepare_case(case))
        except TimeoutError:
            raise
        except Exception as exc:
            failure={"id":case["id"],"stage":"meromorphic_RR",
                     "exception_type":type(exc).__name__,"message":str(exc)}
            FAILURES.append(failure)
            emit("incomplete_meromorphic_case",**failure)
            traceback.print_exc()
    if not PREPARED:
        raise ArithmeticError("No requested original meromorphic case was completed.")
    STAGE="consume_shared_Gaussian_length4513_grid"
    gaussian=load("Cartier_original_Gaussian_grid",GAUSSIAN)
    gaussian.DEADLINE=DEADLINE
    base_p,base_q,i=gaussian.original_base()
    if base_p!=(653,525) or base_q!=(3860,232) or i!=95:
        raise ArithmeticError("The long Gaussian source changed its original physical basis.")
    ring=PolynomialRing(arithmetic.K,"B")
    S,grid=gaussian.torsion_eisenstein_grid(ring,base_p,base_q,i)
    grid_receipt=gaussian.COMPLETED["original_grid"]
    if (grid_receipt["points"]!=2208 or grid_receipt["precision"]!=Q or
        grid_receipt["weil_root"]!=2 or grid_receipt["grid_sha256"]!=
            req["certified_Gaussian_grid_sha256"]):
        raise ArithmeticError("The regenerated original long grid changed its consumed receipt.")
    KS=-3*343*S.inv(ring(4*343**3+27*S.z*S.z))
    if KS[0]!=arithmetic.k0:
        raise ArithmeticError("The original KS constant changed.")
    SHARED={"series":S,"grid":grid,"KS":KS,"descriptors":arithmetic.descriptors,
        "probes":arithmetic.probes,"kernel":arithmetic.kernel,
        "pairs":arithmetic.pairs,"prepared":PREPARED}
    STAGE="new_shared_short_Cartier_frames"
    frame_results={}
    if req["maximum_workers"]==1:
        for index in range(73):
            result=frame_worker(index)
            frame_results[index]=result
    else:
        context=multiprocessing.get_context("fork")
        with context.Pool(processes=int(req["maximum_workers"])) as pool:
            for result in pool.imap_unordered(frame_worker,range(73),chunksize=1):
                index=int(result["index"])
                if index in frame_results:
                    raise ArithmeticError("A short Cartier frame was repeated.")
                frame_results[index]=result
                emit("short_Cartier_progress",complete_frames=len(frame_results),total_frames=73)
    if sorted(frame_results)!=list(range(73)):
        raise ArithmeticError("The complete original Cartier frame set is missing.")
    ordered=[frame_results[i] for i in range(73)]
    EC=matrix(arithmetic.K,[r["Hodge_Cartier_values"] for r in ordered])
    C=arithmetic.E_inverse*EC
    I=identity_matrix(arithmetic.K,73)
    if (I-C).det()!=arithmetic.K(551):
        raise ArithmeticError("The actual Cartier matrix disagrees with the original q-unit order.")
    inverse=(I-C).inverse()
    cartier_receipt={"dimension":73,"convention":"columns; original Hecke row is transpose",
        "Cartier_column_matrix_sha256":row_hash(C),
        "Cartier_row_matrix_sha256":row_hash(C.transpose()),
        "Cartier_characteristic_polynomial":[int(x) for x in C.charpoly().list()],
        "one_minus_C_determinant":int((I-C).det()),
        "all73_frame_values_sha256":digest(ordered),
        "probe_receipt":arithmetic.probe_receipt,"consumed_Gaussian_grid":grid_receipt}
    emit("actual_Cartier_matrix_certificate",**cartier_receipt)
    STAGE="new_original_normalized_third_kind_values"
    for prepared in PREPARED:
        case=prepared["case"]
        values=[]
        for row in ordered:
            matches=[r for r in row["cases"] if r["id"]==case["id"]]
            if len(matches)!=1:
                raise ArithmeticError("A frame omitted an actual meromorphic numerator.")
            values.append(matches[0]["Cartier_difference_value"])
        delta=arithmetic.E_inverse*vector(arithmetic.K,values)
        correction=inverse*delta
        if (C-I)*correction+delta:
            raise ArithmeticError("The actual Cartier-fixed correction has the wrong sign.")
        alpha=(vector(arithmetic.K,prepared["target_rho"])+
               arithmetic.target_Hodge*correction)/arithmetic.K(6)
        target=arithmetic.center_ids.index(case["candidate_id"])
        result={"id":case["id"],"candidate_id":case["candidate_id"],"angle":case["angle"],
            "coarse_parameter":"j-j_CM","alpha":int(alpha[target]),
            "all_eight_log_derivatives":[int(x) for x in alpha],
            "clearing_denominator":6,"order_mod_q":551,
            "method":"R1118-short-Cartier",
            "exact_initial_divisor_sha256":digest(case["weights"]),
            "meromorphic_RR_certificate":prepared["certificate"],
            "Cartier_difference_coordinates_sha256":digest([int(x) for x in delta]),
            "holomorphic_correction_sha256":digest([int(x) for x in correction]),
            "Cartier_matrix_certificate_sha256":digest(cartier_receipt)}
        COMPLETED.append(result)
        emit("actual_third_kind_value",**result)
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="completed" if not FAILURES else "partially_completed"
    ordered_values=sorted(COMPLETED,key=lambda r:r["id"])
    complete=(not FAILURES and {r["id"] for r in COMPLETED}=={r["id"] for r in arithmetic.cases})
    emit("receipt",status="complete" if complete else "incomplete",
         source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),request_sha256=REQUEST_HASH,
         completed=ordered_values,failed_cases=FAILURES,result_sha256=digest(ordered_values),
         Cartier_matrix_certificate=cartier_receipt,
         scope="Actual normalized third-kind values only; no uncomputed QC rank or exclusion.")
    support_path.unlink(missing_ok=True)
    if not complete:
        sys.exit(1)

if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        if isinstance(exc,SystemExit) and exc.code==1 and STAGE=="partially_completed":
            raise
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,
             run=os.environ.get("GITHUB_RUN_ID"),request_sha256=REQUEST_HASH,
             stage=STAGE,completed=COMPLETED,failed_cases=FAILURES,
             prepared_cases=[r["case"]["id"] for r in PREPARED],
             exception_type=type(exc).__name__,message=str(exc),
             scope="Only individually completed original third-kind values are retained.")
        traceback.print_exc()
        sys.exit(1)
