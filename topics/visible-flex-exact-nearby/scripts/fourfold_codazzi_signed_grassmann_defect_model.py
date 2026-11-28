"""True 1424-cell low193 model in signed chronological derivative charts."""
from hashlib import sha256
import json
from pathlib import Path


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def canonical(x):
    return (json.dumps(x,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()


def freeze_history(history,path):
    """Define and use one outward decimal checkpoint of the *whole* remaining nominal-product state."""
    e,np=history.e,history.np
    def entry(x):
        m,r,t=x.mid_rad_10exp(55)
        return [str(int(m)),str(int(r)),int(t)]
    def ball(x):
        m,r,t=x
        a,b=int(m),int(r)
        scale=e.api.rational(10)**t
        return e.api.interval((e.api.rational(a-b)*scale).lower(),(e.api.rational(a+b)*scale).upper())
    def arr(F):
        return [[entry(F.mat[i,j]) for j in range(F.cols)] for i in range(F.rows)]
    value=dict(count=history.count,initial=entry(history.initial),blocks=[dict(length=b["length"],
        defect=entry(b["defect"]),L=arr(b["L"]),P=arr(b["P"])) for b in history.blocks])
    raw=canonical(value)
    tmp=path.with_suffix(".candidate")
    tmp.write_bytes(raw)
    require(tmp.read_bytes()==raw,"every decimal ball of the chronological history")
    tmp.replace(path)
    restored=json.loads(path.read_bytes())
    history.initial=ball(restored["initial"]).upper()
    for block,r in zip(history.blocks,restored["blocks"]):
        block["defect"]=ball(r["defect"]).upper()
        for name in ("L","P"):
            old=block[name]
            data=e.api.arb_mat([[ball(x) for x in row] for row in r[name]])
            block[name]=type(old)(e,np,data,old.rows,old.cols)
    return dict(bytes=len(raw),sha256=sha256(raw).hexdigest(),completed_chronological_cells=history.count,
                complete_blocks=[b["length"] for b in history.blocks],whole_private_filename=path.name)


def verified_inverse(e,np,graph_math,method,M):
    """Full physical transversality at an actual 96- or 97-dimensional terminal."""
    api=e.api
    vals=np.array([[float(x.mid()) for x in row] for row in M.c.values])
    raw=np.linalg.solve(vals,np.eye(M.rows))
    require(np.all(np.isfinite(raw)),"finite dyadic matrix inverse proposal")
    P=graph_math.MatrixBall(e,e.km.Matrix(M.cols,M.rows,[[e.exact_float(float(v)) for v in row] for row in raw]),api.zero)
    pn=method.Factor.from_centre(e,np,P).norm()
    M0=graph_math.MatrixBall(e,M.c,api.zero)
    resid=e.subtract(e.eye(M.rows),e.multiply(M0,P))
    d=(method.Factor.from_centre(e,np,resid).norm()+resid.r+M.r*pn).upper()
    gap=(api.one-d).lower()
    require(gap>0,"true joint physical terminal/node inverse including every original coordinate")
    return graph_math.MatrixBall(e,P.c,(pn*d/gap).upper(),(pn/gap).upper())


def complete(*,np,e,context,pool,store,oldstore,failed_frame,method,graph_math,
             checkpoint_dir,old_gap_powers,finish82,progress,budget):
    api=e.api
    checkpoint_dir=Path(checkpoint_dir)
    checkpoint_dir.mkdir()
    n=len(context.domain.cells)
    require(n==1424 and len(oldstore.data)==245 and len(pool.frame_records)==82,
            "complete actual original old input state before genuinely new derivative enclosures")
    p,q=97,96
    point=lambda a:graph_math.MatrixBall(e,a.c,api.zero)
    frame=oldstore.get(("frame",0))
    Z=oldstore.get(("Z",0))
    store.put(("frame",0),frame)
    store.put(("Z",0),Z)
    H=method.History(e,np,Z.r)
    require(context.qualifications["same_WVC_reference"] is True and len(old_gap_powers)==81,
            "whole original physical problem and all authenticated scalar exponents")
    active,direction,next_cell=H,"left",0
    allstats=[]
    nodeproof=[]
    def snap(direction,i,history):
        cp=freeze_history(history,checkpoint_dir/(direction+"-history.json"))
        progress("whole_GDC_checkpoint",dict(direction=direction,next_cell=i,
            complete_history=cp,complete_private_matrices=store.receipt(),complete_packets_and_frames=pool.receipt()))
        budget()
    def observe(direction,i,row):
        if i in (80,81,82) or not bool(row["complete_new_denominator_lower"]>0):
            progress("GDC_actual_current_gate",dict(direction=direction,index=i,actual=row))
    try:
        for i in range(n):
            f=pool(i,"left")
            require(f["panel"]==i and f["all193_coordinates_retained"] and not f["actual_S_changed"]
                    and set(f["true_moments"]["inputs"])==set(graph_math.ROLES),"complete physical packet")
            if i<81:
                nf=oldstore.get(("frame",i+1))
                old_pair=(oldstore.get(("Z",i+1)),oldstore.get(("Uinv",i)),api.rational(2)**old_gap_powers[i])
                z1=point(old_pair[0])
            elif i==81:
                nf=failed_frame
                old_pair=None
                z1=e.zero(q,p)
            else:
                # The nominal centre is zero in these moving rational frames.
                col=e.product(f["forward"],frame,e.vcat(e.eye(p),point(Z))).c
                vec=pool.freeze_vectors(i+1,graph_math.propose_householders(np,e,col))
                nf=graph_math.certify_householder_frame(e,vec)
                old_pair=None
                z1=e.zero(q,p)
            trans=e.product(e.transpose(nf),f["forward"],frame)
            Z,U,row=method.step(engine=e,np=np,math_module=graph_math,transfer=trans,graph=Z,
                next_centre=z1,history=H,old_pair=old_pair,diagnostic=lambda r:observe("left",i,r))
            store.put(("frame",i+1),nf)
            store.put(("Z",i+1),Z)
            store.put(("Uinv",i),U)
            frame,Z=store.get(("frame",i+1)),store.get(("Z",i+1))
            allstats.append({k:f[k] for k in ("panel","subboxes","beta_sum_upper","beta2_sum_upper",
                "complete_raw_prefix_and_inverse_upper","largest_local_tail_upper")})
            next_cell=i+1
            progress("new_GDC_left",dict(index=i,record=row))
            if i==81:
                finish82(row)
                snap("left",i+1,H)
                pool._fill()
            elif i%64==63 or i+1==n:
                snap("left",i+1,H)
            budget()
        pool.close()
        outer=graph_math.original_outer_boundary(e,frame)
        Y=e.scale(-api.one,e.multiply(verified_inverse(e,np,graph_math,method,e.columns(outer,range(p))),
                                      e.columns(outer,range(p,p+q))))
        HR=method.History(e,np,Y.r)
        active,direction,next_cell=HR,"right",n-1
        def node(i,frame,Z,Y):
            W=verified_inverse(e,np,graph_math,method,e.subtract(e.eye(q),e.multiply(Z,Y)))
            YW,WZ=e.multiply(Y,W),e.multiply(W,Z)
            left=e.multiply(frame,e.vcat(e.eye(p),Z))
            right=e.multiply(frame,e.vcat(Y,e.eye(q)))
            ell=e.multiply(e.hcat(e.add(e.eye(p),e.multiply(YW,Z)),e.scale(-api.one,YW)),e.transpose(frame))
            rho=e.multiply(e.hcat(e.scale(-api.one,WZ),W),e.transpose(frame))
            for name,ball in (("left",left),("right",right),("ell",ell),("rho",rho)):
                store.put(("node",i,name),ball)
            nodeproof.append((i,W.norm()))
            progress("new_GDC_node",dict(index=i,transversality_inverse_upper=W.norm()))
        node(n,frame,Z,Y)
        store.remove(("Z",n))
        swap=tuple(range(p,p+q))+tuple(range(p))
        for i in range(n-1,-1,-1):
            old=store.get(("frame",i))
            T=e.submatrix(e.product(e.transpose(old),pool(i,"right")["backward"],frame),swap,swap)
            t=np.array([[float(v.mid()) for v in r] for r in T.c.values])
            y=np.array([[float(v.mid()) for v in r] for r in Y.c.values])
            acc=t[:q,:q]+t[:q,q:]@y
            rhs=t[q:,:q]+t[q:,q:]@y
            proposed=np.linalg.solve(acc.T,rhs.T).T
            require(np.all(np.isfinite(proposed)),"whole reverse graph centre proposal")
            pred=graph_math.MatrixBall(e,e.km.Matrix(p,q,[[e.exact_float(float(v)) for v in r] for r in proposed]),api.zero)
            Y,V,row=method.step(engine=e,np=np,math_module=graph_math,transfer=T,graph=Y,next_centre=pred,history=HR,
                                diagnostic=lambda r:observe("right",i,r))
            store.put(("Vinv",i),V)
            Z=store.get(("Z",i))
            node(i,old,Z,Y)
            store.remove(("Z",i))
            frame=old
            next_cell=i-1
            progress("new_GDC_right",dict(index=i,record=row))
            if i%64==0:
                snap("right",i-1,HR)
            budget()
    except BaseException:
        # The old mathematical failure or wall remains the actual exception even if storage fails.
        try:
            cp=freeze_history(active,checkpoint_dir/(direction+"-terminal-history.json"))
            progress("GDC_terminal_private_history",dict(direction=direction,next_cell=next_cell,
                complete_history=cp,complete_private_matrices=store.receipt(),complete_packets_and_frames=pool.receipt()))
        except Exception as storage_error:
            print("Terminal chronological history checkpoint:",repr(storage_error),flush=True)
        raise
    require(H.count==HR.count==n and len(nodeproof)==n+1,"all whole true left/right graphs and complementary nodes")
    return dict(kind="R149_actual_low193_joint_Grassmann_inverse_v1",context=context,joint_store=store,
        packet_provider=pool,complete_refined_cells=n,local_statistics=allstats,all_transversalities=nodeproof,
        true_hybrid_BVP_verified=True,private_model_token=object(),all193_original_mean_and_boundary_coordinates_retained=True,
        ordinary_dr_and_true_root_lengths_retained=True,exact_rational_householder_frames=True,
        physical_S_replaced_by_internal_balance=False,new_chronological_method=True)
