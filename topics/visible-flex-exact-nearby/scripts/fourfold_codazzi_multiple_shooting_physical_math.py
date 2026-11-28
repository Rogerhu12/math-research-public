"""Global bidirectional multiple shooting on the authentic original physical BVP.

The preconditioner is a finite dyadic proposal. The proof is one global
induced block-norm test on the original 1424 ordered transfers and both
physical boundaries. No directional Grassmann denominator is assumed.
"""
from hashlib import sha256
import json
from pathlib import Path
import struct


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def save_weights(e,ws,path):
    """Read back the entire private dyadic definition before the norm test."""
    raw=b"R149-MSS-weights-v1\0"+struct.pack("<Q",len(ws[0]))+b"".join(
        struct.pack("<d",float(x)) for side in ws for x in side)
    path.write_bytes(raw)
    check=path.read_bytes()
    require(check==raw,"complete private positive weight bytes")
    offset=len(b"R149-MSS-weights-v1\0")+8
    flat=[e.exact_float(x[0]) for x in struct.iter_unpack("<d",check[offset:])]
    n=len(ws[0])
    require(len(flat)==2*n and flat[:n]==ws[0] and flat[n:]==ws[1],"same exact dyadics on readback")
    return (flat[:n],flat[n:]),dict(bytes=len(raw),sha256=sha256(raw).hexdigest(),nodes=n)


class Model:
    def __init__(self,*,e,np,method,env,math_module,pool,store,context,progress,budget):
        self.e,self.np,self.method,self.env=e,np,method,env
        self.math,self.pool,self.store=math_module,pool,store
        self.context,self.progress,self.budget=context,progress,budget
        self.n=len(context.domain.cells)
        self.rows=[]
        self.p,self.q=97,96
        require(self.n==1424 and context.qualifications["same_WVC_reference"],"the actual whole physical WVC family")
        self.R=env.OrderedProducts(False)
        self.S=env.OrderedProducts(True)
        self.spatial=(range(97),range(97,193))
        self.private_model_token=object()

    def point(self,values):
        e=self.e
        require(self.np.all(self.np.isfinite(values)),"finite whole dyadic proposal")
        h,w=values.shape
        return self.math.MatrixBall(e,e.km.Matrix(h,w,[[e.exact_float(float(x)) for x in row] for row in values]),e.api.zero)

    def floats(self,M):
        return self.np.array([[float(v) for v in row] for row in M.c.values],dtype=float)

    def native(self,M):
        return self.e.api.arb_mat(M.c.values)

    def sub(self,M,rows,cols):
        return self.e.api.arb_mat([[M[i,j] for j in cols] for i in rows])

    def norm(self,v):
        return self.method.Factor(self.e,self.np,v,v.nrows(),v.ncols()).norm()

    def columns(self):
        """Exact dyadic definition chosen by two independent floating bases; no transversality assumed."""
        e,np,n=self.e,self.np,self.n
        U=np.vstack((np.eye(97),np.zeros((96,97))))
        self.store.put(("U",0),self.point(U))
        for i in range(n):
            f=self.pool(i,"left")
            require(f["panel"]==i and f["all193_coordinates_retained"] and not f["actual_S_changed"],
                    "whole original family on each physical cell")
            U=np.linalg.qr(self.floats(f["forward"])@U,mode="reduced")[0]
            self.store.put(("U",i+1),self.point(U))
            self.progress("new_complete_nominal_left_basis",dict(cells=i+1))
            self.budget()
        self.pool.close()
        V=np.vstack((-13/80*np.eye(96),np.zeros((1,96)),np.eye(96)))
        self.store.put(("V",n),self.point(V))
        for i in range(n-1,-1,-1):
            V=np.linalg.qr(self.floats(self.pool(i,"right")["backward"])@V,mode="reduced")[0]
            self.store.put(("V",i),self.point(V))
            self.progress("new_complete_nominal_right_basis",dict(cells=n-i))
            self.budget()

    def local(self,i):
        e,np=self.e,self.np
        U,V,Un,Vn=(self.store.get((name,j)) for name,j in (("U",i),("V",i),("U",i+1),("V",i+1)))
        T=self.pool(i,"left")["forward"]
        U0,V0,U1,V1,T0=map(self.native,(U,V,Un,Vn,T))
        F,G,L,H=self.floats(U),self.floats(V),self.floats(Un),self.floats(Vn)
        Tm=self.floats(T)
        proposal=np.linalg.solve(np.column_stack((Tm@F,-H)),np.eye(193))
        P=self.point(proposal)
        self.store.put(("P",i),P)
        P0=self.native(P)
        D0=e.api.arb_mat(e.km.eye(e.api,193).values)
        # Keep the same joint error of T in both temporal orientations.
        PU=P0*(T0*U0)
        PV=P0*V1
        QU=P0*U1
        QV=P0*(T0*V0)
        approximate=np.column_stack((L,-Tm@G))
        diag=proposal@approximate
        R=self.point(diag[:97,:97])
        S=self.point(diag[97:,97:])
        self.store.put(("R",i),R)
        self.store.put(("S",i),S)
        RF=self.method.Factor.from_centre(e,np,R)
        SF=self.method.Factor.from_centre(e,np,S)
        self.R.append(RF)
        self.S.append(SF)
        un,vn=self.norm(U0),self.norm(V0)
        result=[]
        for k,rs in enumerate(self.spatial):
            pfee=self.norm(self.sub(P0,rs,range(193)))*T.r
            t1=self.sub(D0,rs,self.spatial[0])-self.sub(PU,rs,range(97))
            t2=self.sub(D0,rs,self.spatial[1])+self.sub(PV,rs,range(96))
            t3=self.sub(QU,rs,range(97))
            t4=-self.sub(QV,rs,range(96))
            if k==0:
                t3=t3-RF.mat
            else:
                t4=t4-SF.mat
            result.append([(self.norm(t1)+pfee*un).upper(),self.norm(t2),
                           self.norm(t3),(self.norm(t4)+pfee*vn).upper()])
        self.rows.append(result)
        self.progress("new_all_original_scattering_defect_blocks",dict(cell=i,complete_eight_induced_norms=result))
        self.budget()

    def boundaries(self):
        e,np=self.e,self.np
        U0,V0,Un,Vn=(self.store.get((name,i)) for name,i in (("U",0),("V",0),("U",self.n),("V",self.n)))
        # root residual is the original independent even96. The terminal uses actual 13/80 plus its independent mean.
        au=e.rows(U0,range(97,193));av=e.rows(V0,range(97,193))
        def physical(M):
            native=self.native(M)
            upper=self.sub(native,range(96),range(M.cols))
            lower=self.sub(native,range(97,193),range(M.cols))
            top=upper+lower*e.api.rational(13,80)
            return e.api.arb_mat([[top[i,j] if i<96 else native[96,j] for j in range(M.cols)] for i in range(97)])
        bu,bv=physical(Un),physical(Vn)
        def inverse_proposal(A):
            mid=np.array([[float(A[i,j].mid()) for j in range(A.ncols())] for i in range(A.nrows())])
            return self.point(np.linalg.solve(mid,np.eye(A.nrows())))
        PA,PB=inverse_proposal(self.native(av)),inverse_proposal(bu)
        self.store.put(("root_preconditioner",),PA)
        self.store.put(("outer_preconditioner",),PB)
        pa,pb=self.native(PA),self.native(PB)
        self.root=(self.norm(pa*self.native(au)),self.norm(self.native(e.eye(96))-pa*self.native(av)))
        self.outer=(self.norm(self.native(e.eye(97))-pb*bu),self.norm(pb*bv))
        self.progress("new_exact_two_physical_boundary_defects",dict(root=self.root,outer=self.outer))

    def certify(self,directory,finish_blocks):
        self.columns()
        for i in range(self.n):
            self.local(i)
        self.R.seal()
        self.S.seal()
        self.boundaries()
        args=dict(e=self.e,rows=self.rows,root=self.root,outer=self.outer,R=self.R.norms,S=self.S.norms)
        # Save the entire binary interval row evidence privately, including the ordered signed free products.
        def ball(v):
            m,r,p=v.mid_rad_10exp(56)
            return [str(int(m)),str(int(r)),int(p)]
        records=dict(local=[[[ball(v) for v in side] for side in row] for row in self.rows],
            root=[ball(v) for v in self.root],outer=[ball(v) for v in self.outer],
            reverse=[[i,h,ball(v)] for (i,h),v in sorted(self.R.norms.items())],
            forward=[[i,h,ball(v)] for (i,h),v in sorted(self.S.norms.items())])
        raw=(json.dumps(records,sort_keys=True,separators=(",",":"))+"\n").encode()
        path=Path(directory)/"all-original-shooting-rows.private"
        path.write_bytes(raw)
        require(path.read_bytes()==raw,"complete directed original scattering records and free products")
        finish_blocks(dict(original_cells=self.n,original_nodes=self.n+1,all_local_angular_block_bounds=8*self.n,
            original_boundary_block_bounds=4,diagonal_signed_product_counts=[len(self.R.norms),len(self.S.norms)],
            complete_private_row_bytes=len(raw),complete_private_row_sha256=sha256(raw).hexdigest(),
            complete_dyadic_definition=self.store.receipt()))
        proposal=self.env.positive_weights(**args)
        self.weights,self.weights_receipt=save_weights(self.e,proposal,Path(directory)/"whole-dyadic-weights.private")
        self.gap=self.env.verify(**args,weights=self.weights,report=self.progress)
        self.true_hybrid_BVP_verified=True
        return dict(complete_true_inverse=True,dimension=193*(self.n+1),original_cells=self.n,
            complete_left_and_right_weights=self.weights_receipt,strict_contraction_margin=self.gap,
            exact_original_boundary_dimensions=[96,97],independent_physical_mean_retained=True,
            true_ordinary_lengths=True,whole_signed_free_product_bounds=[len(self.R.norms),len(self.S.norms)])

    def hs_source_maps(self):
        """All physical body and atoms as actual Hilbert-Schmidt maps including both within-cell orientations."""
        e,api,n=self.e,self.e.api,self.n
        require(self.true_hybrid_BVP_verified and self.gap>0,"actual full inverse before source observations")
        roles=self.math.ROLES
        z=api.zero
        local={a:{r:[[],[]] for r in roles} for a in ("HS","op")}
        triangles={a:{r:z for r in roles} for a in ("HS","op")}
        wc,wd=self.weights
        homogeneous=z
        def opnorm(M):
            return min(M.norm(),(self.norm(self.native(M))+M.r).upper())
        def trace(M):
            return (sum((M.c.values[i][i] for i in range(M.rows)),z)+M.rows*M.r).upper()
        for i in range(n):
            packet=self.pool(i,"maps")
            moments=packet["true_moments"]
            T=self.pool(i,"left")["forward"]
            U,V,P=(self.store.get((a,i)) for a in ("U","V","P"))
            X=e.as_ball(moments["output"])
            PT=e.multiply(P,T)
            arcs=[e.rows(PT,r) for r in self.spatial]
            homogeneous+=(api.sqrt(opnorm(e.quadratic(X,U)))*wc[i]+api.sqrt(opnorm(e.quadratic(X,V)))*wd[i])**2
            for role in roles:
                J=e.as_ball(moments["inputs"][role])
                for k,G in enumerate(arcs):
                    gram=e.quadratic(J,e.transpose(G))
                    val=trace(gram)
                    require(val>=0,"whole local true projected Hilbert-Schmidt square")
                    local["HS"][role][k].append(val)
                    local["op"][role][k].append(min(val,opnorm(gram)))
                tri=e.trace_product_upper(X,J)
                triangles["HS"][role]+=tri
                triangles["op"][role]=max(triangles["op"][role],tri)
            self.progress("new_whole_four_source_injections",dict(cells=i+1))
            self.budget()
        U0,V0,Un,Vn=(self.store.get((a,b)) for a,b in (("U",0),("V",0),("U",n),("V",n)))
        theta=e.from_interval(e.km.Matrix(96,96,[[self.context.reference_thetas[j+1] if j==k else z
                                    for k in range(96)] for j in range(96)]))
        obs_root=opnorm(e.rows(U0,range(97)))*wc[0]+opnorm(e.rows(V0,range(97)))*wd[0]
        obs_outer=sum((opnorm(e.multiply(theta,e.rows(m,range(97,193))))*v for m,v in ((Un,wc[-1]),(Vn,wd[-1]))),z)
        out={}
        for role in roles:
            values={}
            for mode in ("HS","op"):
                a,b=local[mode][role]
                c=self.env.all_observations(injections=a,endpoint=z,products=self.R.norms,reverse=True,quadratic=True)
                d=self.env.all_observations(injections=b,endpoint=z,products=self.S.norms,reverse=False,quadratic=True)
                seed=api.sqrt(max(max((v/w**2).upper() for v,w in zip(c,wc)),max((v/w**2).upper() for v,w in zip(d,wd))))
                gain=(seed/self.gap).upper()
                body=(api.sqrt(homogeneous)*gain+api.sqrt(triangles[mode][role])).upper()
                root,terminal=(obs_root*gain).upper(),(obs_outer*gain).upper()
                values[mode]=(body,root,terminal)
            hbody,hroot,hterm=values["HS"]
            body,root,terminal=(min(a,b) for a,b in zip(values["op"],values["HS"]))
            atoms=api.sqrt(root**2+terminal**2).upper()
            rec=dict(kind="R149_actual_multiple_shooting_four_source_map_v1",source_role=role,
                complete_true_cells=n,source_columns=128 if role==roles[3] else 193,ordinary_dr=True,
                body_HS2_upper=(hbody**2).upper(),root97_HS2_upper=(hroot**2).upper(),outer96_HS2_upper=(hterm**2).upper(),
                root97_operator_upper=root,outer96_operator_upper=terminal,
                body_norm_upper=body,atoms193_norm_upper=atoms,complete_norm_upper=api.sqrt(body**2+atoms**2).upper(),
                all193_original_mean_and_boundary_observations_retained=True,actual_low_BVP_proved=True,
                same_cell_triangles_charged_via_positive_whole_X_J=True,full_CFB_or_positive_family_inverse_inferred=False)
            for x,y in (("body_norm_upper","actual_body_norm_upper"),("atoms193_norm_upper","actual_atoms193_norm_upper"),
                        ("complete_norm_upper","actual_complete_source_norm_upper")):
                rec[y]=rec[x]
            if role==roles[2]:
                rec.update(actual_low_second_kind_inverse_upper=((api.sqrt((2+body)**2+atoms**2)+api.sqrt(body**2+atoms**2))/2).upper(),
                           all193_independent_atom_inputs_keep_their_identity=True)
            out[role]=rec
        return out
