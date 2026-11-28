"""Signed whole selected forcing and the actual high return in the genuine low graph."""
from fractions import Fraction
from hashlib import sha256
import multiprocessing as mp
import os
import queue
import signal
import time


def require(ok,message):
    if not ok:
        raise ValueError(message)


def pooled_panels(indices, initial, evaluate, accept, budget, progress, stage, deadline):
    """Four forked independent cells. Both serial graph recurrences remain in their natural order."""
    ctx=mp.get_context("fork")
    tasks,answers=ctx.Queue(8),ctx.Queue(8)
    processes=[]
    def work():
        signal.signal(signal.SIGTERM,signal.SIG_DFL)
        while True:
            arg=tasks.get()
            if arg is None:
                return
            i,data=arg
            try:
                answers.put((i,evaluate(i,data),None))
            except BaseException as error:
                answers.put((i,None,type(error).__name__+": "+str(error)))
                return
    indices=list(indices)
    next_task=0
    pending,ready=set(),{}
    try:
        for _ in range(4):
            process=ctx.Process(target=work)
            process.start()
            processes.append(process)
        for position,i in enumerate(indices):
            # Enqueuing a new initial value can advance the forward node recurrence.
            while next_task<min(len(indices),position+8):
                j=indices[next_task]
                tasks.put((j,initial(j)))
                pending.add(j)
                next_task+=1
            while i not in ready:
                budget(processes)
                require(time.monotonic()<deadline,"complete combined response job deadline")
                try:
                    j,data,error=answers.get(timeout=2)
                except queue.Empty:
                    require(all(p.is_alive() for p in processes),"whole affine panel worker alive")
                    continue
                require(j in pending and error is None and data is not None,
                        "complete new signed panel "+str((j,error)))
                pending.remove(j)
                ready[j]=data
            accept(i,ready.pop(i))
            if (position+1)%16==0 or position+1==len(indices):
                progress(stage,dict(completed=position+1,whole=len(indices)))
    finally:
        for p in processes:
            if p.is_alive():
                p.terminate()
        for p in processes:
            p.join(timeout=5)
        tasks.cancel_join_thread()
        tasks.close()
        answers.close()


def source_columns(*, engine, model, provider, balances, graph_math, carriers, gsr, field,
                   source_store, source_expected, rows, read_ball, work_store, budget, progress, deadline):
    """A genuine particular of the full linear decomposition, with both boundary coordinates free later."""
    e,api,km=engine,engine.api,engine.km
    context,original=model["context"],model["joint_store"]
    n=model["complete_refined_cells"]
    require(os.environ.get("GITHUB_ACTIONS")=="true" and graph_math.Engine is type(e)
            and model["kind"]=="R149_actual_low193_joint_Grassmann_inverse_v1"
            and model["true_hybrid_BVP_verified"] and n==1424 and len(balances)==155
            and context is provider.context and work_store is not original and not work_store.data,
            "same genuine private graph; new signed response store")
    f=field.PhysicalBoxReader(source_store,source_expected,api,km,context.domain,rows,read_ball)
    require(f.source_roles==() and tuple(f.column_names)==("ordinary_Newton_minus_f_delta",
            "ordinary_nu_proposal_defect_s_delta"),"both original signed columns from all 577")
    def pack(x):
        payload=carriers.packed_ball(e,x)
        return sha256(payload).hexdigest(),payload
    def unpack(packet,nrow,ncol):
        digest,payload=packet
        require(sha256(payload).hexdigest()==digest,"identical entire private worker matrix")
        return carriers.unpacked_ball(e,graph_math,nrow,ncol,payload)
    def node(i,name):
        return original.get(("node",i,name))
    def increment(i,unused):
        inc=gsr.cell_columns(e,model,provider,balances,f,i,km.zeros(api,193,2))
        return pack(e.from_interval(inc))
    # This is exactly the zero-boundary affine constant: a_N=0, b_0=0.
    # Both nonzero free homogeneous data are separate columns of GBC.
    a=e.zero(97,2)
    b=e.zero(96,2)
    work_store.put(("a",n),a)
    def backward(i,packet):
        nonlocal a
        inc=unpack(packet,193,2)
        work_store.put(("inc",i),inc)
        stored_inc=work_store.get(("inc",i))
        a=e.multiply(original.get(("Uinv",i)),e.subtract(a,e.multiply(node(i+1,"ell"),stored_inc)))
        work_store.put(("a",i),a)
        a=work_store.get(("a",i))
    pooled_panels(reversed(range(n)),lambda i:None,increment,backward,budget,progress,
                  "complete_signed_forcing_and_backward_coordinates",deadline)
    start,cut,end=Fraction(17,20),Fraction(9,10),Fraction(19,20)
    Gram={name:e.zero(2,2) for name in ("weighted_body","physical_low_window","physical_shell33_96")}
    observations={}
    def save(name,x):
        work_store.put(("physical",name),x)
        row=work_store.get(("physical",name))
        observations[name]=dict(record=dict(work_store.data[("physical",name)]),
                                column_norm_upper=[e.columns(row,(j,)).norm() for j in (0,1)])
    def local(i,packet):
        x=gsr.interval_matrix(e,unpack(packet,193,2))
        cur_gram={k:km.zeros(api,2,2) for k in Gram}
        trace=None
        intervals=[]
        def accumulate(name,span,weight,rows):
            # Interval squares on the original orthonormal mean/nonmean coordinates.
            for j in range(2):
                for k in range(j,2):
                    value=sum((weight[r]*span.values[r][j]*span.values[r][k] for r in rows),api.zero)
                    cur_gram[name].values[j][k]+=dt*value
                    if j!=k:
                        cur_gram[name].values[k][j]=cur_gram[name].values[j][k]
        def observe(box,duration,span,endpoint):
            nonlocal trace,dt
            dt=duration
            lo,hi=context.domain.exact_physical_cover(box)
            q=context.reference_qs[i]
            accumulate("weighted_body",span,[api.one]*96+[q*q]*97,range(193))
            if hi==cut:
                require(trace is None,"one exact physical cut in this cell")
                trace=pack(e.from_interval(endpoint))
            if hi<=start or lo>=end:
                return
            require(start<=lo<hi<=end and (not intervals or intervals[-1][1]==lo),
                    "entire physical shell pieces")
            intervals.append((lo,hi))
            K=None
            for j,_,_ in provider._body_intersections((lo,hi)):
                v=api.old_interval(provider.rows[j]["original_intrinsic_enclosure"]["K"])
                K=v if K is None else K.union(v)
            require(K is not None and api.lower(K)>0,"whole positive shell curvature")
            w=api.sqrt(K)
            factors=[api.one/w]*96+[w]*97
            accumulate("physical_low_window",span,factors,range(193))
            accumulate("physical_shell33_96",span,factors,tuple(range(32,96))+tuple(range(129,193)))
        dt=None
        gsr.cell_columns(e,model,provider,balances,f,i,x,observe)
        cover=(intervals[0][0],intervals[-1][1]) if intervals else None
        return {k:pack(e.from_interval(v)) for k,v in cur_gram.items()},trace,cover
    cursor=start
    def collect(i,result):
        nonlocal cursor
        mats,trace,cover=result
        require(set(mats)==set(Gram),"all three response Grams")
        for k,packet in mats.items():
            Gram[k]=e.add(Gram[k],unpack(packet,2,2))
        if cover:
            require(cover[0]==cursor<cover[1]<=end,"complete signed physical shell order")
            cursor=cover[1]
        if trace is not None:
            require("cut_raw193" not in observations,"sole physical cut across all panels")
            save("cut_raw193",unpack(trace,193,2))
    def send_initial(i):
        nonlocal b
        x=e.add(e.multiply(node(i,"left"),work_store.get(("a",i))),e.multiply(node(i,"right"),b))
        work_store.remove(("a",i))
        if i==0:
            weight=[api.rational(1+16*j*j)**api.rational(1,6) for j in range(1,97)]+[api.one]*97
            save("root_raw97",e.rows(x,range(97)))
            scaled=gsr.interval_matrix(e,x)
            save("root_mixed_full193",e.from_interval(e.flow.diagonal_left(km,scaled,weight)))
        if i==n:
            scaled=gsr.interval_matrix(e,e.rows(x,range(97,193)))
            save("outer_weighted96",e.from_interval(e.flow.diagonal_left(km,scaled,
                                                   [context.reference_thetas[k] for k in range(1,97)])))
            return None
        inc=work_store.get(("inc",i))
        b=e.add(e.multiply(original.get(("Vinv",i)),b),e.multiply(node(i+1,"rho"),inc))
        work_store.remove(("inc",i))
        return pack(x)
    pooled_panels(range(n),send_initial,local,collect,budget,progress,"complete_signed_whole_body_and_shell",deadline)
    send_initial(n)
    require(cursor==end and "cut_raw193" in observations,"whole original 0.85..0.95 and its cut")
    # Each exact Gram is positive; the stored matrix also retains the signed off-diagonal.
    for k,value in Gram.items():
        work_store.put(("gram",k),value)
        G=work_store.get(("gram",k))
        diag=[api.sqrt(e.submatrix(G,(i,),(i,)).norm()).upper() for i in range(2)]
        observations[k]=dict(record=dict(work_store.data[("gram",k)]),column_norm_upper=diag)
    require(len(work_store.data)==7,"only the four signed outputs and three entire Grams remain")
    return dict(kind="R149_signed_selected_affine_low_response_both_whole_forcing_columns_v1",
        private_model_token=model["private_model_token"],source_index=source_expected["complete_index_sha256"],
        original_source_columns=list(f.column_names),original_source_rows=577,solved_low_rows=193,
        weighted_body_uses_original_S=True,complete_cells=n,whole_source_map_targets_called=0,
        observations=observations,private_observation_index=work_store.receipt(),physical_matching_proved=False)


def local_return_geometry(engine,model,provider,budget):
    """Unchanged A^c and S on the actual shell, including the exact left traces of .9."""
    e,api=engine,engine.api
    context,domain=model["context"],model["context"].domain
    shell=(Fraction(17,20),Fraction(19,20))
    cut=Fraction(9,10)
    lengths=tuple(Fraction(1,k) for k in (100,200,500,1000))
    factors={h:dict(A=api.zero,Sinv=api.zero,through=cut-h) for h in lengths}
    cover=shell[0]
    physical_weight=api.zero
    for i in range(model["complete_refined_cells"]):
        lo,hi=domain.exact_physical_cover((i,Fraction(0),Fraction(1)))
        l,r=max(lo,shell[0]),min(hi,shell[1])
        if l>=r:
            continue
        require(l==cover and domain.cells[i]["parent_panel"]>0,"shell covered by the real fixed panels")
        cover=r
        q=context.reference_qs[i]
        require(api.lower(q)>0,"positive original physical S")
        for j,_,_ in provider._body_intersections((l,r)):
            K=api.old_interval(provider.rows[j]["original_intrinsic_enclosure"]["K"])
            require(api.lower(K)>0,"positive on this entire original shell piece")
            w=api.sqrt(api.sqrt(K))
            physical_weight=max(physical_weight,api.magnitude(1/w),api.magnitude(w/q))
        # Partition at the distinct trace starts once; all relevant nested arcs use these same boxes.
        points=sorted({l,r}|{v for v in (cut,*(cut-h for h in lengths)) if l<v<r})
        for a,b in zip(points,points[1:]):
            active=[h for h in lengths if cut-h<=a<b<=cut]
            if not active:
                continue
            box=(i,(a-lo)/(hi-lo),(b-lo)/(hi-lo))
            A=provider.centre_matrix(e.flow.HEAD,e.flow.HEAD,box)
            M=e.from_interval(A).norm()
            for h in active:
                f=factors[h]
                require(f["through"]==a,"each entire trace arc")
                f.update(A=max(f["A"],M),Sinv=max(f["Sinv"],api.one,api.magnitude(1/q)),through=b)
            budget([])
    require(cover==shell[1] and all(f["through"]==cut for f in factors.values()),"whole physical trace geometry")
    return physical_weight,factors


def actual_known_high_returns(*,engine,model,provider,particular,part_store,boundary,boundary_store,
                            admitted,gtp,ohr_raw,wob_raw,emit,budget):
    """The fourth GG source map pays the actual signed-equation high feedback.

    The directions of v_i and d_i need not be known to bound their *joint*
    image. No norm here is used as a signed vector.
    """
    import json
    e,api=engine,engine.api
    require(sha256(ohr_raw).hexdigest()=="312c60afba95bc4e41bd29549a444031cbd633cd252be981bcccb329e54a4993",
            "entire genuine OHR first complete result")
    ohr=json.loads(ohr_raw)
    require(ohr["proved"] and ohr["independent_height_and_root_retained"]
            and all(x is True for x in ohr["rational_comparisons"].values())
            and len(ohr["whole_inputs"])==19 and len(ohr["rational_comparisons"])==34
            and sha256(wob_raw).hexdigest()==ohr["whole_inputs"]["WOB"],"entire original L_* source and OHR")
    wob=json.loads(wob_raw)
    L=gtp.saved_upper(api,wob["copied_original_scalar_records"]["L_star"])
    require(model["true_hybrid_BVP_verified"] and admitted["reference_identity"]==model["context"].reference_identity
            and admitted["low_inverse_basis"]==gtp.TRUE_BASIS and "private_token" in admitted
            and particular["private_model_token"] is model["private_model_token"] is boundary["private_model_token"]
            and particular["private_observation_index"]==part_store.receipt()
            and boundary["complete_private_store"]==boundary_store.receipt()
            and particular["complete_cells"]==1424 and boundary["complete_boundary_columns"]==193,
            "same actual low equation, complete signed body/endpoint source and homogeneous columns")
    src=admitted["source_bounds"]
    raw,centre,correction=(src[k] for k in ("ordinary_raw_low_source","centre_high0_return_source",
                                            "low_second_kind_correction"))
    op={}
    for name in ("body","root","outer"):
        def amplification(rec):
            return rec["body"] if name=="body" else api.sqrt(rec[name+"_actual_squared"]).upper()
        G,Gc=amplification(raw),amplification(centre)
        op[name]=min((L*G).upper(),(Gc+admitted["delta_C"]*G).upper())
    # The original right lift is D plus G_c times the original second-kind correction acting on D.
    D=gtp.saved_upper(api,admitted["D"]["reference_weighted_right97_body_upper"])
    right_body=(api.one+correction["body"])*D
    mixed=api.rational(1+16*96**2)**api.rational(1,6)
    P,arcs=local_return_geometry(e,model,provider,budget)
    geometry={}
    for h,v in arcs.items():
        t=api.sqrt(api.rational(h.numerator,h.denominator))
        geometry[str(h)]=(v["Sinv"]*op["body"]*(api.one/t+t*v["A"])+t*L).upper()
    gain=dict(weighted_body=op["body"],root_raw97=op["root"],root_mixed_full193=mixed*op["root"],
              outer_weighted96=op["outer"],cut_raw193=min(geometry.values()),
              physical_low_window=P*op["body"],physical_shell33_96=P*op["body"])
    names=dict(root_raw97="root_raw97",root_mixed_full193="root_mixed_full193",
               outer_weighted96="outer_weighted96",cut_raw193="cut_raw193",
               physical_low_window="low_physical_shell_Gram193",physical_shell33_96="shell_physical_shell_Gram193")
    right={"weighted_body":right_body}
    for k,g in names.items():
        right[k]=boundary["actual_directed_observations"][g]["charted_right97"]
    out={}
    def save(name,value):
        point=value.upper()
        result=emit(name,point,"upper")
        require(result.is_finite() and bool(result>=point),"directed actual scalar readback")
        return result
    def q(s):
        v=Fraction(s)
        return api.rational(v.numerator,v.denominator)
    for j,key in enumerate(("Newton","nu")):
        data=ohr["source_columns"][key]
        C,d=q(data["ordinary_high_raw_L2"]),q(data["charted_right97"])
        values={}
        for name,coefficient in gain.items():
            p=particular["observations"][name]
            storekey=("gram",name) if name in ("weighted_body","physical_low_window","physical_shell33_96") else ("physical",name)
            require(part_store.data[storekey]==p["record"],"original signed matrix readback metadata")
            error=save(key+"_"+name+"_actual_known_high_and_physical_radius",coefficient*C+right[name]*d)
            value=save(key+"_"+name+"_complete_affine_constant_upper",p["column_norm_upper"][j]+error)
            values[name]=dict(radius=error,total_known_affine=value)
        out[key]=values
    return dict(kind="R149_actual_signed_low_particular_plus_true_known_high_and_physical_returns_v1",
                private_model_token=model["private_model_token"], source_index=particular["source_index"],
                actual_affine_independent_observations=out, complete_cut_trace_arc_gains=geometry,
                original_joint_boundary_body_upper=save("actual_hybrid_joint_boundary_body_upper",
                    (api.one+correction["body"])*gtp.saved_upper(api,admitted["D"]["reference_joint193_boundary_body_upper"])),
                authentic_fourth_and_raw_GG_maps_retained=True,true_signed_zero_boundary_columns=particular["observations"],
                full_free_boundary_columns=boundary["complete_private_observations"],
                independent_mean_retained=True,actual_physical_and_negative_matching_proved=False,
                actual_nonlinear_family_proved=False,old_successful_source_map_calls=0)


def apply_free_boundary(*,engine,particular,part_store,boundary,boundary_store,returns,
                        left96,charted_right97,output_store):
    """Evaluate on prescribed true two-column free data, excluding d_i already in OHR."""
    e,api=engine,engine.api
    require(particular["private_model_token"] is returns["private_model_token"] is boundary["private_model_token"]
            and particular["source_index"]==returns["source_index"]
            and particular["private_observation_index"]==part_store.receipt()
            and boundary["complete_private_store"]==boundary_store.receipt()
            and output_store is not part_store and output_store is not boundary_store and not output_store.data,
            "the same original source, root frames, and two independent physical boundary data")
    l,r=e.as_ball(left96),e.as_ball(charted_right97)
    require((l.rows,l.cols,r.rows,r.cols)==(96,2,97,2),"both actual complete left96 and charted-right97")
    D=e.vcat(l,r)
    result={}
    for name in ("root_mixed_full193","root_raw97","outer_weighted96","cut_raw193"):
        p=part_store.get(("physical",name))
        H=boundary_store.get(("observation",name))
        x=e.add(p,e.multiply(H,D))
        key=("affine",name)
        output_store.put(key,x)
        centre=output_store.get(key)
        values=[]
        for j,col in enumerate(("Newton","nu")):
            radius=returns["actual_affine_independent_observations"][col][name]["radius"]
            values.append((e.columns(centre,(j,)).norm()+radius).upper())
        result[name]=dict(signed_affine_centre_record=dict(output_store.data[key]),upper=values)
    for name,gram in (("weighted_body",None),("physical_low_window","low_physical_shell_Gram193"),
                      ("physical_shell33_96","shell_physical_shell_Gram193")):
        if gram:
            signed=e.quadratic(boundary_store.get(("gram",gram)),D)
            key=("boundary_gram",name)
            output_store.put(key,signed)
            G=output_store.get(key)
        values=[]
        for j,col in enumerate(("Newton","nu")):
            free=(api.sqrt(e.submatrix(G,(j,),(j,)).norm()) if gram else
                  returns["original_joint_boundary_body_upper"]*e.columns(D,(j,)).norm())
            total=returns["actual_affine_independent_observations"][col][name]["total_known_affine"]
            values.append((total+free).upper())
        result[name]=dict(upper=values)
    return dict(kind="R149_affine_selected_solutions_at_two_prescribed_whole_boundary_columns_v1",
                actual_directed_observations=result,private_output=output_store.receipt(),
                low_feedback_body_plus_other_inhomogeneities_still_required=True,
                full_physical_and_waist_height_matching_proved=False)
