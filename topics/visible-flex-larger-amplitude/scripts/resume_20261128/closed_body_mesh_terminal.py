"""Run the complete finite closed-mesh measurements on the accepted runner-local physical point."""
from pathlib import Path
import gzip
import hashlib
import json
import os

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial import cKDTree

import closed_body_mesh_geometry as geom


def digest(data):
    return hashlib.sha256(data).hexdigest()


def nodes(lo, hi, intervals, extra, periodic=False):
    raw = list(np.linspace(lo, hi, intervals + 1))
    for x in extra:
        x = float(x)
        if not np.isfinite(x) or x < lo or x > hi:
            raise ValueError("breakpoint outside chart interval")
        raw.append(x)
    tol = 64 * np.finfo(float).eps * max(1., abs(lo), abs(hi))
    out = []
    for x in sorted(raw):
        if not out or x - out[-1] > tol:
            out.append(x)
    out[0], out[-1] = lo, hi
    return np.asarray(out[:-1] if periodic else out, dtype="<f8")


class AtlasMesh:
    """Share periodic indices and every chart-interface ring. Use Cartesian jets at the poles."""
    def __init__(self, period, half, end, profile_extra, end_extra, central_extra, center):
        profile = nodes(0., period, 112, profile_extra, True)
        central = nodes(-half, half, 16, [*central_extra, -min(.36,half), min(.36,half)])
        distance = nodes(0., end, 20, end_extra)
        cap = nodes(0., 1., 14, [.007, .035, .25, .5, .75, .9875, .999, .99925, .9995, .99975, .9999])
        self.nodes = dict(profile=profile, cylinder=central, end=distance, cap=cap)
        self.grid = {k: {"n": len(v), "little_endian_f64_sha256": digest(v.tobytes())}
                     for k, v in self.nodes.items()}
        self.parts = []
        def ring_chart(name, radii, sign):
            u = np.tile(profile, len(radii))
            v = np.repeat(radii, len(profile))
            self.parts.append((name, u, v, sign))
        def pole(name, sign):
            self.parts.append((name, np.array([center[0]]), np.array([center[1]]), sign))
        pole("cap-cartesian-", 1)
        ring_chart("cap-", cap[1:], 1)
        ring_chart("end-", distance[-2::-1], -1)
        ring_chart("cylinder", central[1:], 1)
        ring_chart("end+", distance[1:], 1)
        ring_chart("cap+", cap[-2:0:-1], -1)
        pole("cap-cartesian+", -1)

        self.n = sum(len(u) for _, u, _, _ in self.parts)
        self.sign = np.concatenate([np.repeat(s, len(u)) for _, u, _, s in self.parts])
        self.last = np.cumsum([len(u) for _, u, _, _ in self.parts])
        rings = np.arange(1, self.n - 1, dtype=np.int32).reshape(-1, len(profile))
        following = np.roll(rings, -1, axis=1)
        negative = np.stack((np.zeros(len(profile), dtype=int), following[0], rings[0]), axis=-1)
        strip_a = np.stack((rings[:-1], following[:-1], following[1:]), axis=-1).reshape(-1, 3)
        strip_b = np.stack((rings[:-1], following[1:], rings[1:]), axis=-1).reshape(-1, 3)
        positive = np.stack((rings[-1], following[-1], np.full(len(profile), self.n-1)), axis=-1)
        self.faces = np.vstack((negative, strip_a, strip_b, positive)).astype("<i4")
        f = self.faces
        directed = np.vstack((f[:, :2], f[:, 1:], f[:, [2,0]]))
        self.edges, ids, counts = np.unique(np.sort(directed,axis=1), axis=0,
                                            return_inverse=True, return_counts=True)
        balance = np.bincount(ids, weights=np.where(directed[:,0]<directed[:,1], 1., -1.))
        adj = coo_matrix((np.ones(len(self.edges), dtype=np.uint8), self.edges.T),
                         shape=(self.n, self.n)).tocsr()
        self.topology = {
            "vertices": self.n, "edges": len(self.edges), "triangles": len(f),
            "components": int(connected_components(adj, directed=False, return_labels=False)),
            "euler": self.n-len(self.edges)+len(f),
            "edges_without_two_incident_faces": int(np.count_nonzero(counts != 2)),
            "edges_with_inconsistent_face_orientation": int(np.count_nonzero(balance)),
            "faces_le_i32_sha256": digest(f.tobytes()),
            "ring_order": [v[0] for v in self.parts]}

    def jets(self, evaluator, *args):
        vals = []
        for chart, u, v, _ in self.parts:
            # Bound temporary AD material arrays, independently of the full material coverage.
            for start in range(0, len(u), 512):
                sl = slice(start, start+512)
                jet = np.asarray(evaluator(chart, u[sl], v[sl], *args), dtype=float)
                if jet.shape != (len(u[sl]), 6, 3):
                    raise ValueError("physical chart jet has incorrect dimensions for "+chart)
                if not np.isfinite(jet).all():
                    raise FloatingPointError("nonfinite physical chart jet for "+chart)
                vals.append(jet)
        return np.concatenate(vals)

    def address(self, index):
        k = int(np.searchsorted(self.last, index, side="right"))
        chart, u, v, _ = self.parts[k]
        j = index - (int(self.last[k-1]) if k else 0)
        return [int(index), chart, float(u[j]), float(v[j])]


def metric_data(j):
    fu, fv = j[:,1], j[:,2]
    vector = np.cross(fu, fv)
    area = np.linalg.norm(vector, axis=1)
    return (geom.rowdot(fu,fu), geom.rowdot(fu,fv), geom.rowdot(fv,fv), area, vector)


def max_relative_form(reference, form):
    guu, guv, gvv, area, _ = reference
    a, b, c = form
    valid = (gvv > 0) & (area > 0)
    result = np.full(len(a), np.nan)
    q = guv[valid]/gvv[valid]
    e1 = (a[valid] - 2*q*b[valid] + q*q*c[valid])*gvv[valid]/area[valid]**2
    e2 = (b[valid]-q*c[valid])/area[valid]
    e3 = c[valid]/gvv[valid]
    result[valid] = .5*(np.abs(e1+e3) + np.hypot(e1-e3, 2*e2))
    return result


def extrema(values, atlas, maximum=True):
    finite = np.isfinite(values)
    if not np.any(finite):
        return {"value": None, "address": None, "undefined": len(values)}
    ids = np.flatnonzero(finite)
    k = ids[(np.argmax if maximum else np.argmin)(values[ids])]
    return {"value": float(values[k]), "address": atlas.address(int(k)),
            "undefined": int(len(values)-len(ids))}


def metric_curvature(j, target, atlas):
    m = metric_data(j)
    a, b, c, area, cross = m
    n = cross / np.where(area>0,area,1.)[:,None] * atlas.sign[:,None]
    diff = (a-target[0], b-target[1], c-target[2])
    gram = max_relative_form(target, diff)
    curvature = max_relative_form(m, tuple(geom.rowdot(n,j[:,k]) for k in (3,4,5)))
    return n, {"relative_gram_operator_max": extrema(gram,atlas),
               "absolute_principal_curvature_max": extrema(curvature,atlas),
               "area_density_min": extrema(area,atlas,False),
               "singular_target_coordinates": int(np.count_nonzero(target[3]==0)),
               "singular_physical_coordinates": int(np.count_nonzero(area==0))}


def triangle_geometry(p, n, m):
    a,b,c = p[m.faces].transpose(1,0,2)
    cross = np.cross(b-a,c-a)
    double_area = np.linalg.norm(cross,axis=1)
    normals = (n[m.faces[:,0]]+n[m.faces[:,1]]+n[m.faces[:,2]])
    align = geom.rowdot(geom.unit(cross),geom.unit(normals))
    edge = m.edges
    e = np.linalg.norm(p[edge[:,0]]-p[edge[:,1]],axis=1)
    origin = (p.max(axis=0)+p.min(axis=0))*.5
    a,b,c = a-origin,b-origin,c-origin
    signed = geom.rowdot(a,np.cross(b,c))/6
    volume = float(signed.sum())
    first = (signed[:,None]*(a+b+c)).sum(axis=0)/4
    q = (geom.rowdot(a,a)+geom.rowdot(b,b)+geom.rowdot(c,c)+
         geom.rowdot(a,b)+geom.rowdot(b,c)+geom.rowdot(c,a))
    second = float(np.sum(signed*q)/10)
    return {
        "triangle_area_min": float(.5*double_area.min()), "surface_area": float(.5*double_area.sum()),
        "zero_area_triangles": int(np.count_nonzero(double_area==0)),
        "minimum_face_normal_alignment": float(align.min()),
        "faces_with_nonpositive_normal_alignment": int(np.count_nonzero(align<=0)),
        "largest_edge": float(e.max()), "largest_edge_vertices": edge[e.argmax()].tolist(),
        "signed_volume": volume, "world_first_volume_moment": (first+volume*origin).tolist(),
        "world_volume_centroid": (first/volume+origin).tolist() if volume!=0 else None,
        "centred_polar_volume_moment": float(second-first@first/volume) if volume!=0 else None}


def held_distance(p, p0, tree0, edge, edge0):
    da, ja = tree0.query(p)
    db, jb = cKDTree(p).query(p0)
    ka, kb = int(da.argmax()),int(db.argmax())
    a, b = float(da[ka]),float(db[kb])
    return {"vertex_hausdorff": max(a,b),
            "current_to_initial": a, "initial_to_current": b,
            "current_to_initial_vertices": [ka,int(ja[ka])],
            "initial_to_current_vertices": [kb,int(jb[kb])],
            "finite_mesh_lower": max(0.,a-edge0,b-edge),
            "finite_mesh_upper": max(a+edge,b+edge0)}


def seam_jumps(evaluator, t, profile, half, end):
    """Compare normal material parameters across every collar, including cap-normal charts."""
    def edge(name, val):
        a=np.asarray(evaluator(name,profile,np.full(len(profile),val),t),dtype=float)
        if a.shape!=(len(profile),6,3) or not np.isfinite(a).all():
            raise FloatingPointError("invalid physical seam jets for "+name)
        return a
    def compare(left,right,sign):
        jumps=left-right*np.asarray([1,1,sign,1,sign,1])[None,:,None]
        norms=np.linalg.norm(jumps,axis=2)
        return {"maxima":norms.max(axis=0).tolist(),
                "profile_indices":np.argmax(norms,axis=0).tolist()}
    ans={}
    for label,sign in (("+",1),("-",-1)):
        normal=edge("cap-normal"+label,0.)
        ans["cylinder_to_end"+label]=compare(edge("cylinder",sign*half),edge("end"+label,0.),sign)
        ans["end_to_cap_normal"+label]=compare(edge("end"+label,end),normal,1)
        ans["cap_normal_to_polar"+label]=compare(normal,edge("cap"+label,1.),-1)
    return ans


def write_mesh(path, p, faces, point, phase):
    vertex_data = np.asarray(p,dtype="<f8").tobytes()
    packed = np.empty(len(faces),dtype=[("count","u1"),("ids","<i4",(3,))])
    packed["count"] = 3
    packed["ids"] = faces
    header = ("ply\nformat binary_little_endian 1.0\ncomment point "+point+
              "\ncomment phase "+float(phase).hex()+"\nelement vertex "+str(len(p))+
              "\nproperty double x\nproperty double y\nproperty double z\nelement face "+
              str(len(faces))+"\nproperty list uchar int vertex_indices\nend_header\n").encode("ascii")
    plain = header + vertex_data + packed.tobytes()
    if len(plain)>=5_000_000:
        raise ValueError("full uncompressed PLY exceeds the frozen mesh size ceiling")
    tmp = path.with_suffix(".tmp")
    with tmp.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw,filename="",mtime=0,mode="wb",compresslevel=6) as out:
            out.write(plain)
    compressed = tmp.read_bytes()
    if len(compressed)>=5_000_000:
        raise ValueError("full compressed PLY exceeds the frozen mesh size ceiling")
    os.replace(tmp,path)
    return {"path": "closed-body-mesh/"+path.name, "bytes":len(compressed),
            "sha256":digest(compressed), "ply_bytes":len(plain), "ply_sha256":digest(plain),
            "vertex_le_f64_sha256":digest(vertex_data)}


def put_json(path, value):
    raw=(json.dumps(value,ensure_ascii=False,allow_nan=False,sort_keys=True,
                    separators=(",",":"))+"\n").encode("utf8")
    tmp=path.with_suffix(".tmp")
    tmp.write_bytes(raw)
    os.replace(tmp,path)
    return {"path":"closed-body-mesh/"+path.name,"bytes":len(raw),"sha256":digest(raw)}


def export_final(out, point_sha, times, period, half_width, end_length, evaluator, *,
                 target_evaluator, mesh_times, profile_extra=(), end_extra=(),
                 cap_center=(.595,0.), central_extra=(), progress=None):
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
    mesh=AtlasMesh(float(period),float(half_width),float(end_length),
                   profile_extra,end_extra,central_extra,cap_center)
    target=metric_data(mesh.jets(target_evaluator))
    result={"schema":"whole-closed-material-mesh-v1","point_sha256":point_sha,
            "scope":"All material rings and both Cartesian poles. Reported finite-vertex, triangle and jet measurements use floating-point arithmetic.",
            "phase_unit":"radian","phase_detail_columns":
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
            seams=seam_jumps(evaluator,t,mesh.nodes["profile"],half_width,end_length)
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
