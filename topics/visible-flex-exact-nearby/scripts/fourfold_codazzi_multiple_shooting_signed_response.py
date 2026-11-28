"""Read a signed physical Duhamel column family on all original cells and two original boundary rows."""
from hashlib import sha256
import struct


def require(ok,message):
    if not ok:
        raise ValueError(message)


def solve(model,*,name,source,root_even96,outer_odd_and_mean97,solution_store,progress):
    """source(i) returns the entire true forward physical jump f_i.

    Every residual uses the supplied physical map, not its centre. The
    proposed free sweeps merely choose finite dyadic coefficients. A single
    call can enclose one or several jointly signed columns on all nodes.
    """
    e,np,n=model.e,model.np,model.n
    require(model.true_hybrid_BVP_verified and model.gap>0 and root_even96.e is outer_odd_and_mean97.e is e,
            "the same full multiple-shooting inverse and physical engine")
    cols=root_even96.cols
    require(1<=cols<=193 and root_even96.rows==96 and outer_odd_and_mean97.shape==(97,cols),
            "whole signed physical boundary family with its independent mean")
    P=lambda i:model.store.get(("P",i))
    U=lambda i:model.store.get(("U",i))
    V=lambda i:model.store.get(("V",i))
    native,nums=model.native,model.floats
    c=np.empty((n+1,97,cols))
    d=np.empty((n+1,96,cols))
    root_pre=model.store.get(("root_preconditioner",))
    outer_pre=model.store.get(("outer_preconditioner",))
    d[0]=nums(root_pre)@nums(root_even96)
    c[n]=nums(outer_pre)@nums(outer_odd_and_mean97)
    # T x_i - x_(i+1) = -f_i, hence the scattered jump is -P_i f_i.
    for i in range(n):
        f=source(i)
        require(f.e is e and f.shape==(193,cols),"entire signed physical Duhamel input for every cell")
        g=-nums(P(i))@nums(f)
        c[i]=g[:97]
        d[i+1]=nums(model.store.get(("S",i)))@d[i]+g[97:]
        model.budget()
    for i in range(n-1,-1,-1):
        c[i]+=nums(model.store.get(("R",i)))@c[i+1]
        model.budget()
    require(np.all(np.isfinite(c)) and np.all(np.isfinite(d)),"finite nominal signed proposals")
    wc,wd=model.weights
    def physical(i):
        return e.add(e.multiply(U(i),model.point(c[i])),e.multiply(V(i),model.point(d[i])))
    def norm(M):
        return min(M.norm(),(model.norm(native(M))+M.r).upper())
    left=physical(0)
    da=norm(e.multiply(root_pre,e.subtract(root_even96,e.rows(left,range(97,193)))))
    ic,id_=[],[]
    for i in range(n):
        right=physical(i+1)
        f=source(i)
        require(f.e is e and f.shape==(193,cols),"full directed source on reread")
        T=model.pool(i,"left")["forward"]
        residual=e.subtract(e.subtract(right,e.multiply(T,left)),f)
        g=e.multiply(P(i),residual)
        ic.append(norm(e.rows(g,range(97))))
        id_.append(norm(e.rows(g,range(97,193))))
        left=right
        model.budget()
    db=norm(e.multiply(outer_pre,e.subtract(outer_odd_and_mean97,model.math.original_outer_boundary(e,left))))
    C=model.env.all_observations(injections=ic,endpoint=db,products=model.R.norms,reverse=True,quadratic=False)
    D=model.env.all_observations(injections=id_,endpoint=da,products=model.S.norms,reverse=False,quadratic=False)
    gain=(max(max((v/w).upper() for v,w in zip(C,wc)),max((v/w).upper() for v,w in zip(D,wd)))/model.gap).upper()
    chain=sha256(b"R149-signed-MSS-physical-nodes-v1")
    for i in range(n+1):
        x=physical(i)
        rad=(x.r+(norm(U(i))*wc[i]+norm(V(i))*wd[i])*gain).upper()
        value=model.math.MatrixBall(e,x.c,rad)
        key=(name,"actual_signed_physical_node",i)
        solution_store.put(key,value)
        saved=solution_store.get(key)
        require(saved.shape==(193,cols) and saved.r>=value.r,"outward entire physical solution node on readback")
        rec=solution_store.data[key]
        chain.update(struct.pack("<QQ",i,rec["bytes"])+bytes.fromhex(rec["sha256"]))
        if not i%32 or i==n:
            progress("whole_signed_physical_solution_nodes",dict(source=name,nodes=i+1,ordered_node_chain=chain.hexdigest()))
        model.budget()
    return dict(source=name,original_cells=n,nodes=n+1,physical_angular_columns=193,signed_rhs_columns=cols,
                full_weighted_coefficient_error_upper=gain,whole_ordered_node_chain=chain.hexdigest(),
                all_physical_nodes=solution_store.receipt(),private_model_token=model.private_model_token)
