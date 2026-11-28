"""Full-J Euclidean LM on the actual near-bound height/velocity/length faces."""
from itertools import product
from math import comb
import numpy as np
import r632_true_hermite_bvp as solver
from r632_exact_pending_polynomial_frontier import source_arrays


def bernstein(n,t):
    return np.asarray([comb(n,j)*t**j*(1-t)**(n-j) for j in range(n+1)])


def near_bound(graph,curve,field,tolerance):
    q=curve["shape_parameters"]
    basis,offset=source_arrays(graph,field)
    values=np.einsum("ijk,k->ij",basis,np.asarray(q,dtype=solver.LD))
    if offset is not None:
        values+=offset
    L,alpha=curve["length"],curve["alpha"]
    lower,upper=(.8,3.) if field=="h" else (-6.,6.)
    best=None
    for cell in range(values.shape[1]):
        c=np.asarray(values[:,cell],float)
        width=float(graph.knots[cell+1]-graph.knots[cell])
        if field=="upsilon":
            c=(len(c)-1)*np.diff(c)/width*float(alpha.value/L.value)
        # A convex-hull screen affects the direction model only.
        if min(np.min(c)-lower,upper-np.max(c))>tolerance:
            continue
        n=len(c)-1
        ascending=[sum(c[j]*comb(n,j)*comb(n-j,k-j)*(-1)**(k-j)
                       for j in range(k+1)) for k in range(n+1)]
        roots=np.polynomial.Polynomial(ascending).deriv().roots()
        points=[0.,1.]+[float(z.real) for z in roots if abs(z.imag)<1.e-9 and 0<z.real<1]
        for point in points:
            bweights=bernstein(n,point)
            value=float(bweights@c)
            gap,sign=min((value-lower,1.),(upper-value,-1.))
            if gap>tolerance or (best is not None and gap>=best["gap"]):
                continue
            center=bool(field=="h" and cell==0 and point==0.)
            if field=="h":
                row=bweights@np.asarray(basis[:,cell],float)
            else:
                coeff=basis[:,cell]
                base_slope_row=(coeff.shape[0]-1)/width*(bweights@np.asarray(np.diff(coeff,axis=0),float))
                unscaled=(len(values[:,cell])-1)/width*(bweights@np.diff(np.asarray(values[:,cell],float)))
                row=(float(alpha.value/L.value)*base_slope_row
                     +unscaled/float(L.value)*np.asarray(alpha.derivative,float)
                     -value/float(L.value)*np.asarray(L.derivative,float))
            best={"field":field,"gap":gap,"inward_sign":sign,"coordinate":0 if center else None,
                "cell":cell,"reference_point":point,"physical_x":float(graph.knots[cell])+point*width,
                "value":value,"row":sign*row}
    return best


class ExtremeCone:
    def __init__(self,graph,current,args,retained,iteration,enforce_ends):
        self.current,self.clock=current,graph.clock
        curve=current["data"]["curve"]
        self.rows=[]
        for field in ("h","upsilon"):
            record=near_bound(graph,curve,field,args.extremum_distance)
            if record is not None:
                self.rows.append(record)
        L=curve["length"]
        for bound,sign in ((2.1,1.),(7.9,-1.)):
            gap=sign*(float(L.value)-bound)
            if gap<1.e-9:
                self.rows.append({"field":"L","gap":gap,"inward_sign":sign,
                    "coordinate":graph.dimension-1,"row":sign*np.asarray(L.derivative,float)})
        self.faces=[]
        self.record=retained["latest_extremum_cone"]={"iteration":iteration,"state":"building",
            "normals":[{k:v for k,v in r.items() if k!="row"} for r in self.rows],
            "original_qualified_end_rows":3 if enforce_ends else 0,"faces":[],"solves":[]}
        for mask in product((False,True),repeat=len(self.rows)):
            graph.clock.check("before_extremum_complete_face_factor")
            active=[r for r,on in zip(self.rows,mask) if on]
            fixed=[r["coordinate"] for r in active if r["coordinate"] is not None]
            keep=[j for j in range(graph.dimension) if j not in fixed]
            rows=list(current["jacobian"][:3,keep]) if enforce_ends else []
            rows.extend(r["row"][keep] for r in active if r["coordinate"] is None)
            if rows:
                Q,R=np.linalg.qr(np.asarray(rows).T,mode="complete")
                if np.any(np.diag(R[:len(rows)])==0):
                    raise np.linalg.LinAlgError("Exact-zero equality pivot on a complete physical face")
                reduced=Q[:,len(rows):]
            else:
                reduced=np.eye(len(keep))
            tangent=np.zeros((graph.dimension,reduced.shape[1]))
            tangent[keep]=reduced
            label="physical_extremum_"+str(iteration)+"_"+"".join(str(int(v)) for v in mask)
            face={"mask":list(mask),"fixed_coordinates":fixed,"state":"pending"}
            self.record["faces"].append(face)
            factor=solver.EuclideanCompleteRowFactor(current["jacobian"]@tangent,
                -current["residual"],graph.clock,solver.COUNTS,label)
            self.faces.append((mask,tangent,factor))
            face.update(state="completed",factor_id=factor.receipt["factor_id"])
        self.record["state"]="completed"

    def solve(self,penalty):
        r,J=self.current["residual"],self.current["jacobian"]
        best=0.
        winner=np.zeros(J.shape[1])
        report={"lambda":penalty,"candidates":[],"selected":{"face":[],"linear_report":None}}
        self.record["solves"].append(report)
        for mask,tangent,factor in self.faces:
            self.clock.check("before_extremum_complete_model_solve")
            restricted,linear=factor.solve(penalty)
            d=tangent@restricted
            vals=[]
            feasible=bool(np.all(np.isfinite(d)))
            for row,active in zip(self.rows,mask):
                index=row["coordinate"]
                sign=float(row["inward_sign"]*d[index]) if index is not None else float(row["row"]@d)
                tol=32*len(d)*np.finfo(float).eps*np.linalg.norm(row["row"])*np.linalg.norm(d)
                good=(sign==0 if index is not None else abs(sign)<=tol) if active else sign>=0
                feasible=feasible and good
                vals.append(sign)
            item={"mask":list(mask),"actual_signed_derivatives":vals,"feasible":bool(feasible),
                  "linear_report":linear}
            if feasible:
                jd=J@d
                gain=float(-r@jd-(jd@jd+penalty*(d@d))/2)
                item["model_decrease"]=gain
                if np.isfinite(gain) and gain>best:
                    best,winner=gain,d
                    report["selected"]={"face":[row["field"] for row,on in zip(self.rows,mask) if on],
                        "linear_report":linear,"model_decrease":gain}
            report["candidates"].append(item)
        return winner,report
