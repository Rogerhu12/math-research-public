"""Actual joint low193 propagation after whole original input admission and context setup."""
import gc
import os
import time
from pathlib import Path


def private_bytes(roots):
    """Count allocated file contents, once per inode even for nested roots and hard links."""
    seen = set()
    count = 0
    for root in roots:
        for directory, _, names in os.walk(root):
            for name in names:
                try:
                    info = os.stat(os.path.join(directory, name), follow_symlinks=False)
                except FileNotFoundError:
                    # Only completed private atomic renames can race this traversal.
                    continue
                identity = info.st_dev, info.st_ino
                if identity not in seen:
                    seen.add(identity)
                    count += max(info.st_size, info.st_blocks * 512)
    return count


def run_joint_targets(*, np, flint, api, km, green, refined, flow, context, provider,
                      charts, balances, original, restore, math_module, carriers_module,
                      private_directory, native_directory, started, wall_seconds,
                      progress, finish_inverse, finish_maps, save_receipts):
    """Callbacks persist the highest attained stage even if the next target fails."""
    root = Path(private_directory)
    root.mkdir(parents=True, exist_ok=False)
    limits = carriers_module.PRIVATE_BUDGET
    pool = store = None
    peak_rss = peak_disk = 0
    last_disk = 0.0

    def budget(force=False):
        nonlocal peak_rss, peak_disk, last_disk
        workers = pool.processes if pool else ()
        rss = carriers_module.aggregate_rss_bytes(workers)
        peak_rss = max(peak_rss, rss)
        if rss > limits["maximum_aggregate_parent_and_worker_rss_bytes"]:
            raise MemoryError("aggregate parent and worker resident byte bound")
        now = time.monotonic()
        if force or now - last_disk >= 5:
            used = private_bytes((root, native_directory))
            peak_disk = max(peak_disk, used)
            if used > limits["maximum_private_directory_bytes"]:
                raise ValueError("aggregate native and private file byte bound")
            last_disk = now
        if now - started > wall_seconds:
            raise TimeoutError("whole scientific process wall bound")

    def observed(stage, detail):
        progress(stage, detail)
        if stage == "new_joint_left_graph" and detail["complete_cells"] == 1424:
            pool.close()
        budget()

    engine = math_module.Engine(api, km, green, flow)
    try:
        budget(True)
        restored = restore.restore_whole_prefix(
            api, flint, km, green, refined, flow, context, provider, charts, balances,
            original, root / "original", observed)
        progress("whole_original81_matched", restored["receipt"].copy())
        def save_packet(record):
            progress("complete_private_packet", {"panel":record["panel"], "bytes":record["bytes"],
                                                 "sha256":record["sha256"]})
        pool = carriers_module.WholePacketCarriers(engine, math_module, root / "packets", budget,
                                                  accepted=save_packet)
        pool.install_restored_prefix(restored)
        del restored
        provider.clear_cache()
        gc.collect()
        budget(True)
        store = carriers_module.DiskJointStore(engine, math_module, root / "graphs")
        pool.start_workers(context, provider, balances, flow)
        model = math_module.certify_complete_joint_model(
            np, engine, context, pool, pool.freeze_vectors, store, observed)
        finish_inverse(model)
        maps = math_module.complete_joint_source_maps(engine, model, observed)
        if maps["private_model_token"] is not model["private_model_token"]:
            raise ValueError("whole maps have a different private model")
        finish_maps(maps)
    finally:
        try:
            if pool:
                pool.close()
        finally:
            save_receipts(pool.receipt() if pool else None, store.receipt() if store else None,
                          {"peak_sampled_aggregate_rss_bytes": peak_rss,
                           "peak_sampled_private_and_native_bytes": peak_disk})
