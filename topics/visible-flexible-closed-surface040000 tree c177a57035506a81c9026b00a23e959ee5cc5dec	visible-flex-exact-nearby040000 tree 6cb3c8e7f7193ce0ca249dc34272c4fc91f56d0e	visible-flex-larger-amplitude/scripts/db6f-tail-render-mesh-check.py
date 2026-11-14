#!/usr/bin/env python3
"""Small static preview from frozen PLY vertices, without new surface solving."""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def resolve(name):
    p = Path(name)
    return p if p.exists() else TOPIC / "notes" / p.name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--out-prefix", type=Path, required=True)
    a = ap.parse_args()
    output = Path(str(a.out_prefix) + ".png")
    metadata_output = Path(str(a.out_prefix) + ".json")
    if output.exists() or metadata_output.exists():
        raise ValueError("refusing to overwrite a preview")
    spec = importlib.util.spec_from_file_location("mesh_reader_for_static_preview", HERE / "db6f-tail-review-closed-mesh.py")
    reader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reader)
    data = json.loads(a.manifest.read_text())
    plan = json.loads(resolve(data["plan"]["file"]).read_text())
    angular = int(plan["angular_nodes"])
    ring_count = int(plan["rings"])
    upper_count = len(plan["upper_rings"])
    fixed = np.load(resolve(data["fixed_vertex_indices_file"]["file"]), allow_pickle=False)["fixed"]
    ring_fixed = fixed[1:-1].reshape(ring_count, angular)[:, 0]
    # Add every fixed/moving interface and the central ring to the regular
    # preview decimation. These new preview faces do not replace the PLY faces.
    selected = set(range(0, ring_count, 3)) | {0, ring_count-1, upper_count-1}
    for j in range(ring_count-1):
        if ring_fixed[j] != ring_fixed[j+1]:
            selected |= {j, j+1}
    selected = sorted(selected)
    angles = np.arange(0, angular, 3)
    preview_faces = []
    for j in range(len(angles)):
        k = (j+1) % len(angles)
        preview_faces.append((0, 1+selected[0]*angular+angles[k], 1+selected[0]*angular+angles[j]))
    for low, high in zip(selected[:-1], selected[1:]):
        for j in range(len(angles)):
            k = (j+1) % len(angles)
            lo, hi = 1+low*angular, 1+high*angular
            preview_faces += [(lo+angles[j], lo+angles[k], hi+angles[j]),
                              (lo+angles[k], hi+angles[k], hi+angles[j])]
    for j in range(len(angles)):
        k = (j+1) % len(angles)
        preview_faces.append((1+selected[-1]*angular+angles[j],
                              1+selected[-1]*angular+angles[k], 1+ring_count*angular))
    preview_faces = np.asarray(preview_faces, dtype=np.int64)
    records = [next(row for row in data["mesh_files"] if row["time_exact"] == t) for t in ["0", "1/2"]]
    geometries = []
    for record in records:
        p = resolve(record["file"])
        if sha(p) != record["sha256"]:
            raise ValueError("frozen PLY hash changed")
        vertices, _, _ = reader.read_ply(p)
        geometries.append(vertices)
    if not np.array_equal(geometries[0][fixed], geometries[1][fixed]):
        raise ValueError("fixed vertices differ")

    fig = plt.figure(figsize=(13.2, 6.1), facecolor="white")
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.02], left=.015, right=.99, bottom=.13, top=.87, wspace=.04)
    colors = ["#397fa8", "#cf784b"]
    light = np.array([.4, -.7, .65])
    light /= np.linalg.norm(light)
    for slot, (vertices, record, color) in enumerate(zip(geometries, records, colors)):
        ax = fig.add_subplot(gs[slot], projection="3d")
        triangles = vertices[preview_faces]
        normals = np.cross(triangles[:, 1]-triangles[:, 0], triangles[:, 2]-triangles[:, 0])
        normals /= np.linalg.norm(normals, axis=1)[:, None]
        shade = .46 + .54 * np.maximum(0, normals @ light)
        rgb = np.tile(to_rgb(color), (len(triangles), 1))
        fixed_faces = np.all(fixed[preview_faces], axis=1)
        rgb[fixed_faces] = to_rgb("#8a9198")
        collection = Poly3DCollection(triangles, facecolors=rgb*shade[:, None],
                                     edgecolors="none", linewidths=0)
        ax.add_collection3d(collection)
        ax.set(xlim=(-1.16, 1.16), ylim=(-1.16, 1.16), zlim=(-1.91, 1.91))
        ax.set_box_aspect((2.32, 2.32, 3.82))
        ax.view_init(elev=16, azim=-57)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_zticks([-1.5, 0, 1.5])
        ax.set_xlabel("x", labelpad=0)
        ax.set_ylabel("y", labelpad=0)
        ax.set_zlabel("z", labelpad=1)
        ax.tick_params(labelsize=8, pad=0)
        ax.set_title("t = " + record["time_exact"], fontsize=13, color=color, pad=8)
        ax.text(0, 0, 1.91, "fixed cap", ha="center", fontsize=8, color="#4d5359")
        ax.text(0, 0, -2.01, "fixed cap", ha="center", fontsize=8, color="#4d5359")
    ax = fig.add_subplot(gs[2])
    central = []
    for vertices, color, record in zip(geometries, colors, records):
        ring = vertices[1+(upper_count-1)*angular:1+upper_count*angular]
        closed = np.r_[ring, ring[:1]]
        ax.plot(closed[:, 0], closed[:, 1], color=color, linewidth=2.0, label="t = " + record["time_exact"])
        central.append(ring[:, :2])
    ax.set_aspect("equal", adjustable="box")
    ax.set(xlim=(-1.16, 1.16), ylim=(-1.16, 1.16), xlabel="x", ylabel="y")
    ax.set_xticks([-1, -.5, 0, .5, 1])
    ax.set_yticks([-1, -.5, 0, .5, 1])
    ax.grid(alpha=.16)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Central cross-section, z = 0", fontsize=12, pad=16)
    ax.legend(frameon=False, loc="lower right")
    fig.suptitle("R18 M8 finite approximation: fixed caps and a changing held image", fontsize=15, y=.96)
    fig.text(.5, .055, "Same coordinate frame; no rigid alignment. Stored PLY vertices; preview faces are decimated.\n"
             "This picture supplies no new isometry, reach, or rigorous vertex-error estimate.",
             ha="center", va="center", fontsize=9, color="#4d5359")
    fig.savefig(output, dpi=170, facecolor="white")
    plt.close(fig)
    if output.stat().st_size >= 1_000_000:
        raise ValueError("preview unexpectedly exceeds the uncompressed data limit")
    report = {
        "status": "static-preview-from-frozen-PLY-vertices-no-new-continuous-map",
        "manifest": {"file": str(a.manifest), "sha256": sha(a.manifest)},
        "script_sha256": sha(__file__),
        "reader_sha256": sha(HERE / "db6f-tail-review-closed-mesh.py"),
        "inputs": [{"file": r["file"], "sha256": r["sha256"]} for r in records],
        "preview_file": str(output), "preview_sha256": sha(output),
        "preview_bytes": output.stat().st_size,
        "preview_faces_per_view": int(len(preview_faces)),
        "original_vertices_per_mesh": int(len(geometries[0])),
        "fixed_vertices_bitwise_identical": True,
        "new_geometric_claim": False,
    }
    metadata_output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"preview": str(output), "bytes": report["preview_bytes"],
                      "sha256": report["preview_sha256"],
                      "faces_per_view": report["preview_faces_per_view"]}))


if __name__ == "__main__":
    main()
