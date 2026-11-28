"""A posteriori true Grassmann transfer using chronological signed Frechet products."""
import math


def require(ok,message):
    if not ok:
        raise ValueError(message)


class Factor:
    """Native directed matrix for an exact nominal product, with a PSD Gram norm witness."""
    def __init__(self,e,np,values,rows,cols):
        self.e,self.np,self.mat,self.rows,self.cols=e,np,values,rows,cols
        self._norm=None

    @classmethod
    def from_centre(cls,e,np,ball):
        return cls(e,np,e.api.arb_mat(ball.c.values),ball.rows,ball.cols)

    def times(self,other):
        require(self.cols==other.rows and self.e is other.e,"complete chronological signed matrix product")
        return Factor(self.e,self.np,self.mat*other.mat,self.rows,other.cols)

    def transpose(self):
        # The explicit dimensions also cover the rectangular B observation.
        v=[[self.mat[i,j] for i in range(self.rows)] for j in range(self.cols)]
        return Factor(self.e,self.np,self.e.api.arb_mat(v),self.cols,self.rows)

    def norm(self):
        if self._norm is not None:
            return self._norm
        np,api=self.np,self.e.api
        nr,nc=self.rows,self.cols
        upper=[[api.magnitude(self.mat[i,j]) for j in range(nc)] for i in range(nr)]
        limit=max(max(row) for row in upper)
        if bool(limit==0):
            self._norm=api.zero
            return self._norm
        # Rescale the proposal even on long products. The directed proof uses the same factor exactly.
        log2=limit.log()/api.rational(2).log()
        exponent=math.ceil(float(log2.mid()))
        scale=api.rational(2)**exponent
        simple=api.sqrt(max(sum(row,api.zero) for row in upper)*
                        max(sum((row[j] for row in upper),api.zero) for j in range(nc))).upper()
        M=self.mat*(api.one/scale)
        mid=np.array([[float(M[i,j].mid()) for j in range(nc)] for i in range(nr)],dtype=float)
        require(np.all(np.isfinite(mid)),"finite whole scaled proposal")
        if nr<nc:
            mid=mid.T
            M=api.arb_mat([[M[i,j] for i in range(nr)] for j in range(nc)])
        nr,nc=mid.shape
        MT=api.arb_mat([[M[i,j] for i in range(nr)] for j in range(nc)])
        gram=MT*M
        def gersh(X):
            return max(max([api.zero]+[(X[i,i].upper()+sum((api.magnitude(X[i,j]) for j in range(nc)
                                                            if j!=i),api.zero)).upper() for i in range(nc)]),api.zero)
        bound=gersh(gram)
        try:
            values,vectors=np.linalg.eigh(mid.T@mid)
            slack=np.sqrt(np.maximum(float(values[-1])-values,0.0))[:,None]*vectors.T
            if np.all(np.isfinite(slack)):
                proposal=api.arb_mat(slack.tolist())
                proposal_T=api.arb_mat(slack.T.tolist())
                # Whatever eigenvector code returned, proposal_T * proposal is positive semidefinite
                # at the single identical finite binary64 proposal.
                bound=min(bound,gersh(gram+proposal_T*proposal))
        except np.linalg.LinAlgError:
            pass
        self._norm=min(simple,(scale*api.sqrt(bound)).upper())
        return self._norm


class History:
    """A dyadic partition of the whole ordered history, including all accumulated defects."""
    def __init__(self,engine,np,initial_radius):
        self.e,self.np,self.initial=engine,np,initial_radius
        self.blocks=[]
        self.count=0

    def observe(self,L,P,previous_radius):
        # If |E|<=r is already known, both the scalar one-step observation
        # and the complete transported defect majorant are valid. Use their actual minimum.
        direct=(L.norm()*P.norm()*previous_radius).upper()
        total=self.e.api.zero
        left,right=L,P
        for block in reversed(self.blocks):
            total+=left.norm()*right.norm()*block["defect"]
            left=left.times(block["L"])
            right=block["P"].times(right)
        if self.initial.upper()>0:
            total+=left.norm()*right.norm()*self.initial
        return min(direct,total.upper())

    def append(self,L,P,defect):
        block=dict(length=1,L=L,P=P,defect=defect.upper())
        while self.blocks and self.blocks[-1]["length"]==block["length"]:
            left=self.blocks.pop()
            # E_out=L_right L_left E_in P_left P_right + transported left defects + right defects.
            block=dict(length=2*block["length"],L=block["L"].times(left["L"]),
                P=left["P"].times(block["P"]),
                defect=(block["L"].norm()*block["P"].norm()*left["defect"]+block["defect"]).upper())
        self.blocks.append(block)
        self.count+=1
        require(sum(b["length"] for b in self.blocks)==self.count,"all preceding physical cells occur exactly once")


def step(*,engine,np,math_module,transfer,graph,next_centre,history,old_pair=None,diagnostic=None):
    """Validate a new full Frechet transition and its denominator.

    The exact nominal products stay native through dyadic concatenation. The true transfer is
    the entire original matrix ball, including its old complete local-flow uncertainty.
    """
    e,api=engine,engine.api
    q,p=graph.rows,graph.cols
    require(transfer.rows==transfer.cols==p+q==193 and next_centre.shape==(q,p) and
            bool(next_centre.r==0),"original full low193 signed fraction")
    point=lambda x:math_module.MatrixBall(e,x.c,api.zero)
    fact=lambda x:Factor.from_centre(e,np,x)
    def realnorm(x):
        return min(x.norm(),(fact(x).norm()+x.r).upper())
    full=point(transfer)
    xi,yi=tuple(range(p)),tuple(range(p,p+q))
    A,B,C,D=(e.submatrix(full,i,j) for i,j in ((xi,xi),(xi,yi),(yi,xi),(yi,yi)))
    Z,Y=point(graph),next_centre
    Ac=e.add(A,e.multiply(B,Z))
    # Finite dyadic proposals are never accepted as the mathematical inverse.
    if old_pair is None:
        proposal=np.array([[float(x.mid()) for x in row] for row in Ac.c.values])
        raw=np.linalg.solve(proposal,np.eye(p))
        require(np.all(np.isfinite(raw)),"finite proposal for the full nominal denominator")
        values=e.km.Matrix(p,p,[[e.exact_float(float(v)) for v in row] for row in raw])
        P=math_module.MatrixBall(e,values,api.zero)
    else:
        oldgraph,oldinverse,oldgap=old_pair
        require(oldgraph.c.values==Y.c.values,"same centre in the qualified original 245-matrix store")
        P=point(oldinverse)
    PF=fact(P)
    k=PF.norm()
    L=e.subtract(D,e.multiply(Y,B))
    LF,BF=fact(L),fact(B)
    rz,ry=api.sqrt(api.one+fact(Z).norm()**2),api.sqrt(api.one+fact(Y).norm()**2)
    r=transfer.r
    Rc=e.subtract(e.add(C,e.multiply(D,Z)),e.multiply(Y,Ac))
    residual=(realnorm(e.multiply(Rc,P))+r*rz*ry*k).upper()
    alpha=((r*ry+L.r)*k).upper()
    denominator_defect=(realnorm(e.subtract(e.eye(p),e.multiply(Ac,P)))+r*rz*k).upper()
    R=graph.r
    linear=history.observe(LF,PF,R)
    # Apply the actual B observation to the accumulated graph *before* taking its norm.
    denom_gain=(history.observe(BF,PF,R)+r*R*k).upper()
    h=(denominator_defect+denom_gain).upper()
    gap=(api.one-h).lower()
    detail=dict(complete_previous_radius_upper=R,complete_nominal_residual_upper=residual,
        linear_transfer_upper=linear,complete_denominator_centre_defect=denominator_defect,
        full_transported_B_E_P_upper=denom_gain,complete_new_denominator_lower=gap,
        old_Grassmann_scalar_gate_recomputed=False)
    if diagnostic is not None:
        diagnostic(detail)
    if bool(gap>0):
        newrad=((residual+alpha*R+linear)/gap).upper()
        H=math_module.MatrixBall(e,P.c,(k*h/gap).upper(),(k/gap).upper())
        if old_pair is not None:
            newrad=min(newrad,oldgraph.r)
            H=math_module.MatrixBall(e,P.c,min(H.r,oldinverse.r),min(H.norm(),oldinverse.norm()))
    elif old_pair is not None:
        newrad,H=oldgraph.r,oldinverse
    else:
        raise ValueError("complete signed Frechet denominator remains nonpositive on the actual physical cell")
    detail["used_original_denominator_witness"] = not bool(gap>0)
    detail["complete_effective_denominator_lower"] = gap if bool(gap>0) else oldgap
    defect=(residual+alpha*R+h*newrad).upper()
    history.append(LF,PF,defect)
    detail.update(complete_new_graph_radius_upper=newrad,complete_additive_defect_upper=defect)
    return math_module.MatrixBall(e,Y.c,newrad),H,detail
