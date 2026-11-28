"""Public R740 weak pulse input, native ring/Cartesian joint GN and full physical accounting."""
import builtins
import json
import os
from pathlib import Path
import sys


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public"
            or not os.environ.get("GITHUB_RUN_ID","").isdigit()):
        raise SystemExit("R740 requires the public research Actions runner")
    import numpy as np
    from scipy.spatial import ConvexHull
    from r733_inserted_meridian import InsertedMeridian
    from r733_physical_disk import R733Profile
    import r740_weak_material_disk as weak
    from r740_material_rotation_space import (
        channels, normal_factor, padded, sparse_jac, tagged_terms, tail_weight)

    physics=weak.bound_module("_r740_qualification","r732_disk_qualification.py")
    physics.Frame=weak.R740Frame
    physics.collar_jets=weak.fields.collar_jets
    physics.Ring=weak.ring.Ring
    physics.tail_weight=tail_weight
    old_breaks=physics.true_breaks
    def all_breaks(build,radii):
        z=np.array([.002,.004,.5,.996,.998])
        return np.unique(np.r_[old_breaks(build,radii),weak.physical.R0+.13*z,.24+.38*z])
    physics.true_breaks=all_breaks
    original_center=physics.center_jets
    def center(build,phase,q,level,mean):
        # All additional annular functions and both Cartesian jets vanish
        # in an actual neighborhood of r=0. The core prefix is unchanged there.
        n=3*(level+1)*(level+2)//2
        return original_center(build,phase,q[:n],level,mean)
    physics.center_jets=center
    engine=weak.bound_module("_r740_continuation","r732_disk_solver.py")
    engine.PHASES=(0.,.002,.008,.02,.08,.20,.40,.65,.85,1.)
    engine.OPTIONS=dict(baseline=weak.BASELINE,modes=8192,steps=12,order=48)
    engine.FILES=(*engine.FILES,"r733_inserted_meridian.py","r733_physical_disk.py",
                  "r740_weak_material_disk.py","r740_material_rotation_space.py","r740_disk_solver.py")
    engine.Build=weak.R740Build
    engine.Frame=weak.R740Frame
    engine.uplift=padded
    engine.TYPES.update({t.__name__:t for t in (weak.ring.Line,weak.ring.Ring,weak.pulse.Pulse,
             weak.physical.Profile,weak.physical.Build,InsertedMeridian,R733Profile,weak.R740Frame,weak.R740Build)})

    class Continuation(engine.Continuation):
        def __init__(self,paid,level,iterations):
            super().__init__(paid,level,iterations)
            if not self.path.exists():
                self.s["q"]=[0.]*(3*len(tagged_terms(self.s["degree"])))
                self.put()

        def operator(self,phase,degree,q,frame,residual):
            key=[phase,degree,self.level,engine.array_id(q)]
            if self.p.filename("native_factor",key).is_file():
                return self.p.get("native_factor",key,None)
            # Nine real channel derivatives determine every physical coefficient
            # column by the chain rule, including all three components everywhere.
            ch=self.p.get("nine_angular_derivatives",key,lambda:channels(frame,q))
            full=self.p.get("full_sparse_jacobian",key,lambda:sparse_jac(frame,q,ch))
            return self.p.get("native_factor",key,lambda:normal_factor(full,residual,engine.array_id))

        def qualify(self,phase,degree,q):
            key=[phase,degree,engine.array_id(q)]
            def evaluate():
                val=physics.qualify(self.build,phase,q,degree,level=self.level,outdir=self.p.root/"physical")
                val.update(source="R740 weak genuine S ring",source_zmax_bound=.2125,
                           fitted_columns=3*len(tagged_terms(degree)),
                           weak_reference=dict(baseline=weak.BASELINE,increment=weak.INCREMENT),
                           physical_weight_ell=[.04,.47])
                return val
            report=dict(self.p.get("qualification",key,evaluate))
            file=self.p.root/"physical"/Path(report["physical_archive"]).name
            if not file.is_file() or engine.digest(file.read_bytes())!=report["archive_sha256"]:
                raise ValueError("R740 retained physical arrays are missing or mismatched")
            def hull():
                with np.load(file,allow_pickle=False) as a:
                    r=a["physical_jets"][0].reshape(-1,3)
                    c=a["physical_center_jets"][0].reshape(-1,3)
                    s=a["s"]
                ring=self.build.target(phase).jets(s)[0]
                pts=np.concatenate((r,c,np.column_stack((np.full(len(s),self.build.identity["W"]),ring))))
                pts=np.concatenate((pts,pts*np.array([-1.,1.,1.])))
                return pts[ConvexHull(pts).vertices]
            fresh=self.p.get("sampled_shell_hull",key,hull)
            keys=[[a["phase"],a["degree"],a["q"]] for a in self.s["records"]]
            if key not in keys:
                keys.append(key)
            def combined():
                sets=[fresh if k==key else self.p.get("sampled_shell_hull",k,None) for k in keys]
                p=np.concatenate(sets)
                vertices=p[ConvexHull(p).vertices]
                return dict(vertices=vertices,diameter=float(physics.diameter(vertices)))
            union=self.p.get("sampled_all_pose_hull",keys,combined)
            report["cross_phase_sampled_shell"]=dict(phases=[k[0] for k in keys],diameter=union["diameter"],
                   actual_hull=engine.array_id(union["vertices"]),continuous_material_time="open")
            return report

    engine.Continuation=Continuation
    parent_cost=engine.cost_summary
    def cost(root):
        out=parent_cost(root)
        out.pop("actual_original_cartesian_jacobians",None)
        by_degree={}
        file=root/"cost.jsonl"
        if file.exists():
            with file.open() as stream:
                for line in stream:
                    item=json.loads(line)
                    if item["event"]!="saved" or item["kind"]!="full_sparse_jacobian":
                        continue
                    deg=item["key"][1]
                    by_degree[deg]=by_degree.get(deg,0)+1
        out["all_column_native_operators"]=dict(complete_by_level=by_degree,
              summed_full_physical_columns=sum(n*3*len(tagged_terms(d)) for d,n in by_degree.items()),
              saved_nine_channels=out.get("nine_angular_derivatives",{}).get("saved",0),
              independently_checked_columns_per_operator="explicit in each sparse operator",
              level_column_counts={d:3*len(tagged_terms(d)) for d in (3,5)})
        return out
    engine.cost_summary=cost
    def receipt(marker,*args,**kwargs):
        builtins.print({"R732_PHASE":"R740_PHASE","R732_DISK_FINAL":"R740_DISK_FINAL"}.get(marker,marker),
                       *args,**kwargs)
    engine.print=receipt
    defaults={"--state":"r740-paid-state","--iterations":"8"}
    for key,value in defaults.items():
        if not any(a==key or a.startswith(key+"=") for a in sys.argv[1:]):
            sys.argv.extend((key,value))
    engine.main()


if __name__=="__main__":
    main()
