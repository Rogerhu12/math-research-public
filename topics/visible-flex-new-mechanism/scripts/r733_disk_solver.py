"""Independent public R733 disk continuation, including its own physical field and paid archive."""
import builtins
import hashlib
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ORIGINAL = {
    "r732_disk_solver.py": "ed1dd8910eaf8dba190308d7717a4ec9053302f62e1181d10b446f9b24257472",
    "r732_disk_qualification.py": "08feb20d441a5695b6d07e531d71ad3569afe7f874637ef8926a23041855a033",
    "r732_disk_fields.py": "c403b3d979273760fe5ccfd68ba5f7c929f56a28d9113df4770e5a346a109d71",
    "r732_physical_disk.py": "752165ed2eac07e18c9993ede8218a15de16a8820d42210f1cf801d346d10369",
    "r732_closed_ring.py": "58c04599e8d24b0aee8204426491fb0d0132922900b2014fdcbab0f4b1a578e0",
    "r732_compensated_pulses.py": "8df0b12620daf51978873d29319da4b05028088803de570c0995ad98448c7f11",
}


def private_module(label, filename):
    spec = importlib.util.spec_from_file_location(label, HERE/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY","").lower() != "rogerhu12/math-research-public"
            or not os.environ.get("GITHUB_RUN_ID","").isdigit()):
        raise SystemExit("R733 scientific work requires the public research Actions runner")
    for filename,expected in ORIGINAL.items():
        if hashlib.sha256((HERE/filename).read_bytes()).hexdigest() != expected:
            raise ValueError("incompatible original disk routine " + filename)

    import numpy as np
    from scipy.spatial import ConvexHull
    from r733_inserted_meridian import InsertedMeridian
    from r733_physical_disk import R733Build, R733Profile, R733Frame

    # Both callers that construct a field during physical integration must use
    # this same R733 source and rotation seed. The original modules stay untouched.
    geometry = private_module("_r733_bound_physical_qualification","r732_disk_qualification.py")
    geometry.Frame = R733Frame
    engine = private_module("_r733_bound_continuation","r732_disk_solver.py")
    engine.Build = R733Build
    engine.Frame = R733Frame
    engine.FILES = (*engine.FILES, "r733_inserted_meridian.py","r733_physical_disk.py","r733_disk_solver.py")
    engine.TYPES.update({t.__name__:t for t in (InsertedMeridian,R733Profile,R733Build,R733Frame)})

    class Continuation(engine.Continuation):
        def qualify(self, phase, degree, q):
            key = [phase,degree,engine.array_id(q)]
            def actual():
                data = geometry.qualify(self.build,phase,q,degree,level=self.level,
                                        outdir=self.p.root/"physical")
                data.update(source="R733 reverse-meridian disk", source_zmax_bound=.334,
                            true_meridian_length=self.build.identity["meridian_to_core"],
                            physical_field="R733Frame with native constant-curvature S seed")
                return data
            report = dict(self.p.get("qualification",key,actual))
            file = self.p.root/"physical"/Path(report["physical_archive"]).name
            if not file.is_file() or engine.digest(file.read_bytes()) != report["archive_sha256"]:
                raise ValueError("missing or mismatched actual R733 physical jet archive")

            def physical_hull():
                # Match the same native ring columns, reflected disk and real
                # optically held cylinder; its axial interior is a segment
                # between two rim points and does not enlarge this finite hull.
                with np.load(file,allow_pickle=False) as a:
                    right = a["physical_jets"][0].reshape(-1,3)
                    center = a["physical_center_jets"][0].reshape(-1,3)
                    base = a["s"]
                circ = self.build.target(phase).jets(base)[0]
                rim = np.column_stack((np.full(len(base),self.build.identity["W"]),circ))
                points = np.concatenate((right,center,rim))
                both = np.concatenate((points,points*np.array([-1.,1.,1.])))
                return both[ConvexHull(both).vertices]
            stage = self.p.get("native_shell_hull",key,physical_hull)
            old = self.s["records"]
            # Each record identifies its own paid convex hull, never an array
            # recovered from another source or an independently best trial.
            keys = [[a["phase"],a["degree"],a["q"]] for a in old]
            if key not in keys:
                keys.append(key)
            def combined():
                blocks = [stage if k==key else self.p.get("native_shell_hull",k,None) for k in keys]
                pts = np.concatenate(blocks)
                vertices = pts[ConvexHull(pts).vertices]
                return dict(vertices=vertices,diameter=float(geometry.diameter(vertices)),
                            phases=[k[0] for k in keys],source_included=any(k[0]==0. for k in keys))
            joint = self.p.get("cross_phase_sampled_shell",keys,combined)
            report["cross_phase_sampled_shell"] = dict(
                diameter=joint["diameter"],actual_phases=joint["phases"],source_included=joint["source_included"],
                physical_hull=engine.array_id(joint["vertices"]),continuous_material_time="open")
            return report

    engine.Continuation = Continuation
    def print_receipt(marker,*args,**kwargs):
        labels = {"R732_PHASE":"R733_PHASE","R732_DISK_FINAL":"R733_DISK_FINAL"}
        builtins.print(labels.get(marker,marker),*args,**kwargs)
    engine.print = print_receipt
    if not any(a=="--state" or a.startswith("--state=") for a in sys.argv[1:]):
        sys.argv.extend(("--state","r733-paid-state"))
    engine.main()


if __name__ == "__main__":
    main()
