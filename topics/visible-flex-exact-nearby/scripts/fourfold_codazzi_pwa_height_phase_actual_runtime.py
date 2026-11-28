"""Read the immutable APHI runtime in its original schema for the first PWA96 target."""
import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path
from types import ModuleType

S = "topics/visible-flex-exact-nearby/scripts/"
SOURCE = S + "fourfold_codazzi_pwa_height_phase_actual_runtime.py"
BRIDGE = S + "fourfold_codazzi_pwa_height_phase_after_728.py"
BRIDGE_SHA = "6706378a51b4b90fd1f01fa0e7e005b3fffbca3021c3da5aa3d4bd84d9153f82"
APHI = {
    "manifest":"6ca3b71339e0ece21f10f7474011b9632e47034f5848f0fbb8fc92053c3c0a5e",
    "actual":"0bedee9032270a0b0a24ed5af57bc7773a8a6f0b8d913e19cdc7593f877a163e",
    "execution":"368d0048a8d6b5b89c940b5e026f3126f9f732fb09b6b8f2be94afdcf64c1694"}
H96 = {
    "actual":"a49119d596956029d4b51179ed0e694878032a92facdab1e8fa083de83dd8fbe",
    "execution":"73d78ed9c25dd9fda3ade00d2e4694c2d0e7fadd2bc149a32f0b2cd980cb8699"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load_bridge(path):
    raw = Path(path).read_bytes()
    require(sha(raw) == BRIDGE_SHA, "whole original H96-728 admission bridge")
    bridge = ModuleType("_whole_H96_728_bridge")
    bridge.__file__ = str(path)
    exec(compile(raw, str(path), "exec"), vars(bridge))
    original_load = bridge.load

    def load(bound_path, digest, name):
        owner = original_load(bound_path, digest, name)
        if name != "_original_PWA96_science":
            return owner
        require(digest == bridge.ORIGINAL_SHA, "whole original PWA scientific owner")
        raw = Path(bound_path).read_bytes()
        require(sha(raw) == digest, "same whole original PWA source for the schema correction")
        fn, = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name == "admit"]
        old = ast.parse('actual["runtime"] == {**old["runtime"],"OPENBLAS_CORETYPE":"Haswell"}', mode="eval").body
        hit, = [n for n in ast.walk(fn) if isinstance(n, ast.Compare) and ast.dump(n) == ast.dump(old)]
        hit.comparators = [ast.IfExp(test=ast.parse('name == "APHI"',mode="eval").body,
            body=ast.parse('old["runtime"]',mode="eval").body,orelse=hit.comparators[0])]
        tree = ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[]))
        exec(compile(tree,str(bound_path),"exec"),vars(owner))
        return owner

    bridge.load = load
    bridge.SOURCE = SOURCE
    bridge.__file__ = __file__
    original_configure = bridge.configure

    def configure(original, resumed):
        owner = original_configure(original, resumed)
        old_gather, old_admit = owner.gather, owner.admit

        def gather(root, height_actual, height_execution):
            table = old_gather(root, height_actual, height_execution)
            raw = (root / BRIDGE).read_bytes()
            role = "PWA_prior_728_bridge"
            require(sha(raw) == BRIDGE_SHA and role not in table["roles"]
                    and BRIDGE not in table["roles"].values(), "one whole original admission bridge")
            table["files"].append({"role":role, "path":BRIDGE, "bytes":len(raw), "sha256":BRIDGE_SHA,
                "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()})
            table["files"].sort(key=lambda item:item["role"])
            table["roles"][role] = BRIDGE
            return table

        def admit(manifest, raws):
            roles = manifest["roles"]
            require(sha(raws[roles["PWA_prior_728_bridge"]]) == BRIDGE_SHA,
                    "whole original admission in the declared input map")
            for parent, identities in (("APHI",APHI),("H96",H96)):
                for kind, digest in identities.items():
                    require(sha(raws[roles[parent+"_"+kind]]) == digest, "actual fixed parent "+parent+" "+kind)
            admitted = old_admit(manifest, raws)
            a = admitted["APHI"]["identity"]
            require(a["run_id"] == "45915169627" and a["event_commit"] ==
                    "888d23a7ef20cf333436d8ed7654f3c6b6871312"
                    and admitted["H96"]["identity"]["run_id"] == "46135898111",
                    "true distinct APHI and H96-728 terminal publications")
            return admitted

        owner.gather, owner.admit = gather, admit
        return owner

    bridge.configure = configure
    return bridge


def companion(role, path):
    directory = Path(__file__).resolve().parent
    alias = directory / (role+".py")
    return alias if alias.is_file() else directory / Path(path).name


def bridge_module():
    return load_bridge(companion("PWA_prior_728_bridge",BRIDGE))


def admit(manifest, raws):
    return bridge_module().admit(manifest,raws)


def validate_output(raw, manifest, manifest_sha, source_sha, run, attempt):
    return bridge_module().validate_output(raw,manifest,manifest_sha,source_sha,run,attempt)


def main():
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--input-map",type=Path)
    args, _ = parser.parse_known_args()
    if args.input_map:
        paths = json.loads(args.input_map.read_bytes())
        bridge = load_bridge(paths["PWA_prior_728_bridge"])
    else:
        bridge = bridge_module()
    return bridge.main()


if __name__ == "__main__":
    raise SystemExit(main())
