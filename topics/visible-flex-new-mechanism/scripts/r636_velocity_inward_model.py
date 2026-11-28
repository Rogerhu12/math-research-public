"""Use a strictly inward actual velocity derivative when the tangent model retains its descent."""
import numpy as np
from r632_extremum_physical_faces import ExtremeCone


class StrictInteriorCone(ExtremeCone):
    def __init__(self,graph,current,args,retained,iteration,enforce_ends):
        super().__init__(graph,current,args,retained,iteration,enforce_ends)
        self.enforce_ends=enforce_ends
        self.field="upsilon" if args.family=="r636" else "h"

    def solve(self,penalty):
        d,report=super().solve(penalty)
        v=next((r for r in self.rows if r["field"]==self.field and r["coordinate"] is None),None)
        if v is None or not np.any(d):
            return d,report
        n=len(d)
        # Leave every coordinate face exact, including center height. Preserve all
        # other dense normals and every already qualified original end tangent.
        fixed={r["coordinate"] for r in self.rows if r["coordinate"] is not None}
        keep=[j for j in range(n) if j not in fixed]
        rows=[r["row"][keep] for r in self.rows if r is not v and r["coordinate"] is None]
        if self.enforce_ends:
            rows.extend(self.current["jacobian"][:3,keep])
        nv=v["row"][keep]
        if rows:
            matrix=np.asarray(rows)
            coeff=np.linalg.lstsq(matrix.T,nv,rcond=None)[0]
            nv=nv-matrix.T@coeff
        inward=np.zeros(n)
        inward[keep]=nv
        pairing=float(v["row"]@inward)
        signed=float(v["row"]@d)
        r,J=self.current["residual"],self.current["jacobian"]
        jd=J@d
        baseline=float(-r@jd-(jd@jd+penalty*(d@d))/2)
        rec=report["strict_inward_extremum_model"]={"field":self.field,"baseline":baseline,"base_signed_derivative":signed,"candidates":[]}
        if not pairing>0 or not baseline>0:
            return d,report
        target=min(.01,.01*np.linalg.norm(d)*np.linalg.norm(nv))
        for shrink in (1.,.1,.01,.001):
            desired=shrink*target
            if signed>=desired:
                return d,report
            candidate=d+(desired-signed)/pairing*inward
            jv=J@candidate
            gain=float(-r@jv-(jv@jv+penalty*(candidate@candidate))/2)
            actual=float(v["row"]@candidate)
            other=[float(row["row"]@candidate) for row in self.rows if row is not v]
            base_other=[float(row["row"]@d) for row in self.rows if row is not v]
            fine=all(z>=min(0.,z0)-64*np.finfo(float).eps*np.linalg.norm(row["row"])*np.linalg.norm(candidate)
                     for row,z,z0 in zip([k for k in self.rows if k is not v],other,base_other))
            rec["candidates"].append({"target":desired,"actual":actual,"Euclidean_model_decrease":gain,
                "other_original_face_derivatives":other})
            if actual>0 and gain>=.99*baseline and fine:
                rec["selected"]=len(rec["candidates"])-1
                return candidate,report
        return d,report
