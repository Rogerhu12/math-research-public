"""Closed R772 axial tube terminal with one rounded head per side and the true two-variable cap transitions."""
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree

import closed_body_mesh_geometry as geom
from closed_body_mesh_terminal import (AtlasMesh, digest, extrema, held_distance, metric_curvature, metric_data, put_json, triangle_geometry, write_mesh)


def pullback(physical, a, b):
    """Compose a physical six-jet with both true two-variable material scalar jets."""
    _, fu, fv, fuu, fuv, fvv = physical.transpose(1, 0, 2)
    def column(q):
        return np.asarray(q, dtype=float)[..., None]
    def first(i):
        return column(getattr(a,i))*fu + column(getattr(b,i))*fv
    def second(i,j,ij):
        ai,bi = getattr(a,i),getattr(b,i)
        aj,bj = getattr(a,j),getattr(b,j)
        return (column(ai*aj)*fuu + column(ai*bj+bi*aj)*fuv + column(bi*bj)*fvv
                + column(getattr(a,ij))*fu + column(getattr(b,ij))*fv)
    return np.stack((physical[:,0], first("s"), first("a"), second("s","s","ss"),
                     second("s","a","sa"), second("a","a","aa")), axis=1)


def cap_overlaps(cap_atlas, profile, order):
    J = cap_atlas.J
    s = J(profile, s=1.)
    normal = []
    for w in (0., .003, .01):
        a,b = cap_atlas.normal_to_disk_material(s, J(np.full(len(profile),w), a=1.), order)
        normal.append((w,a,b))
    polar = []
    _, rim_offset = cap_atlas.end_limits(order)
    rim_x, rim_z = cap_atlas.offset(s,rim_offset,order)
    for r in (.25,.875,1.):
        radial = J(np.full(len(profile),r),a=1.)
        polar.append((r,radial*rim_x,radial*rim_z))
    return normal,polar


def seam_jumps(evaluator,t,profile,half,end,overlaps):
    def query(name,u,v):
        a = np.asarray(evaluator(name,u,v,t),dtype=float)
        if a.shape != (len(profile),6,3) or not np.isfinite(a).all():
            raise FloatingPointError("invalid physical material jets for "+name)
        return a
    def edge(name,val):
        return query(name,profile,np.full(len(profile),val))
    def compare(left,right,sign=1):
        diff = left-right*np.asarray((1,1,sign,1,sign,1))[None,:,None]
        norms = np.linalg.norm(diff,axis=2)
        if not np.isfinite(norms).all():
            raise FloatingPointError("nonfinite six-jet transition")
        return {"maxima":norms.max(axis=0).tolist(),
                "profile_indices":np.argmax(norms,axis=0).tolist()}
    answer={}
    normal_transitions, cartesian_transitions = overlaps
    for label,sign in (("+",1),("-",-1)):
        answer["cylinder_to_end"+label] = compare(edge("cylinder",sign*half),edge("end"+label,0.),sign)
        answer["end_to_cap_normal"+label] = compare(edge("end"+label,end),edge("cap-normal"+label,0.))
        for w,a,b in normal_transitions:
            polar = query("cap"+label,a.v,b.v)
            answer["cap_normal_to_polar"+label+"@"+str(w)] = compare(
                edge("cap-normal"+label,w),pullback(polar,a,b))
        for r,a,b in cartesian_transitions:
            cartesian = query("cap-cartesian"+label,a.v,b.v)
            answer["cap_polar_to_cartesian"+label+"@"+str(r)] = compare(
                edge("cap"+label,r),pullback(cartesian,a,b))
    return answer


def export_final(out, point_sha, times, period, half_width, end_length, evaluator, *,
                 target_evaluator, mesh_times, cap_atlas, material_order, profile_extra=(), end_extra=(),
                 central_extra=(), progress=None):
    """Evaluate the same complete physical field and target as the parent, in world coordinates.

    times are actual phase values in radians. mesh_times adds any specifically requested
    export phases even if the independent scalar evaluation schedule did not contain them.
    Raw mesh and detailed finite diagnostic records stay under out on this same runner.
    """
    if len(point_sha)!=64 or any(x not in "0123456789abcdef" for x in point_sha):
        raise ValueError("a full actual lowercase point SHA256 is required")
    folder=Path(out)/"closed-body-mesh"
    folder.mkdir(parents=True,exist_ok=True)
    phases=sorted(set(map(float,times))|set(map(float,mesh_times))|{0.})
    selected=set(map(float,mesh_times))
    if not phases or phases[0]!=0. or not np.isfinite(phases).all():
        raise ValueError("phase-zero anchored finite times are required")
    zero=cap_atlas.J(np.array([0.]))
    cap_center=tuple(float(j.v[0]) for j in cap_atlas.disk_world(zero,zero,material_order))
    mesh=AtlasMesh(float(period),float(half_width),float(end_length),
                   (*profile_extra,*cap_atlas.profile_marks()),
                   (*end_extra,cap_atlas.SM,end_length-cap_atlas.SM),
                   (*central_extra,*cap_atlas.axial_marks()),cap_center)
    overlaps=cap_overlaps(cap_atlas,mesh.nodes["profile"],material_order)
    target=metric_data(mesh.jets(target_evaluator))
    result={"schema":"r772-whole-closed-single-rounded-head-material-mesh-v1","point_sha256":point_sha,
            "scope":"All material rings and both Cartesian poles. Reported finite-vertex, triangle and jet measurements use floating-point arithmetic.",
            "cap_disk_cartesian_center_xz":list(cap_center), "cap_transition_order":int(material_order),
            "normal_overlap_widths":[v[0] for v in overlaps[0]], "polar_overlap_radii":[v[0] for v in overlaps[1]],
            "single_rounded_head_length":float(end_length),"phase_unit":"radian","phase_detail_columns":
            ["phase","relative_gram_op","abs_principal_curvature","area_density_min","diameter",
             "maximum_ordered_inverse_normal_chord","vertex_hausdorff_vs_initial","finite_mesh_hausdorff_lower",
             "signed_volume","centred_polar_volume_moment","possible_extra_contact_pairs","zero_area_triangles","all_material_seams_maximum_sixjet_jump"],
            "topology":mesh.topology,"grid":mesh.grid,"phases":[],"details":[],"meshes":[],"errors":[]}
    p0=None
    for i,t in enumerate(phases):
        measurements={"point_sha256":point_sha,"phase":t}
        try:
            jet=mesh.jets(evaluator,t)
            p=jet[:,0]
            n,metrics=metric_curvature(jet,target,mesh)
            seams=seam_jumps(evaluator,t,mesh.nodes["profile"],half_width,end_length,overlaps)
            surface=triangle_geometry(p,n,mesh)
            if t==0.:
                p0=p.copy()
                tree0=cKDTree(p0)
                e0=surface["largest_edge"]
            if t in selected:
                file=write_mesh(folder/("phase-%03d.ply.gz"%i),p,mesh.faces,point_sha,t)
                result["meshes"].append({"phase":t,**file})
            diam=geom.diameter(p)
            chord=(geom.ordered_chords(p,n,mesh.edges) if not metrics["singular_physical_coordinates"]
                   else {"maximum":None,"scope":"unit smooth normal undefined at a singular material point"})
            contacts=geom.triangle_contacts(p,mesh.faces)
            held=(held_distance(p,p0,tree0,surface["largest_edge"],e0)
                  if p0 is not None else {"vertex_hausdorff":None,"finite_mesh_lower":None})
            measurements.update(metrics=metrics,polyhedron=surface,diameter=diam,
                                ordered_normal_chords=chord,triangle_contacts=contacts,held=held,seam_jumps=seams)
            row=[t,metrics["relative_gram_operator_max"]["value"],metrics["absolute_principal_curvature_max"]["value"],
                 metrics["area_density_min"]["value"],diam["value"],chord["maximum"],held["vertex_hausdorff"],
                 held["finite_mesh_lower"],surface["signed_volume"],surface["centred_polar_volume_moment"],
                 sum(contacts["possible_contacts_by_shared_vertex_count"]),surface["zero_area_triangles"],
                 max(max(j["maxima"]) for j in seams.values())]
            result["phases"].append(row)
        except Exception as exc:
            measurements["exception"]={"type":type(exc).__name__,"message":str(exc)}
            result["errors"].append({"phase":t,**measurements["exception"]})
        detail=put_json(folder/("phase-%03d-geometry.json"%i),measurements)
        result["details"].append({"phase":t,**detail})
        result["completed_phases"]=i+1
        result["phase_count"]=len(phases)
        if progress is not None:
            progress({"point_sha256":point_sha,"completed_phases":i+1,"phase_count":len(phases),
                      "phase":t,"last_phase_values":result["phases"][-1] if "exception" not in measurements else None,
                      "last_error":measurements.get("exception"),"detail":detail})
    result["complete_requested_meshes"]=len(result["meshes"])==len(selected)
    result["all_phase_measurements_returned"]=len(result["phases"])==len(phases)
    result["finite_extrema"]={}
    for idx,key in enumerate(result["phase_detail_columns"][1:],1):
        finite=[(row[idx],row[0]) for row in result["phases"] if row[idx] is not None]
        if finite:
            lo,hi=min(finite),max(finite)
            result["finite_extrema"][key]={"min":lo[0],"min_phase":lo[1],"max":hi[0],"max_phase":hi[1]}
    result["index_file"]=put_json(folder/"index.json",result)
    return result
