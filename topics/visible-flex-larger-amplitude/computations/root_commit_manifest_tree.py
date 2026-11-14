#!/usr/bin/env python3
"""Commit a verified topic manifest without touching an active Git index.

The existing HEAD, working files and any index lock are preserved. Tree-object
updates copy the known parent and replace only explicitly hashed topic files.
A newly created owned ref retains the resulting ordinary child commit. No
network operation, force update, checkout or repository-wide index is used.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--selection", type=Path, required=True)
    ap.add_argument("--parent", required=True)
    ap.add_argument("--owned-ref", required=True)
    ap.add_argument("--message", required=True)
    ap.add_argument("--state", type=Path, required=True)
    ap.add_argument("--topic", default="topics/visible-flex-larger-amplitude")
    a = ap.parse_args()
    repo = a.repo.resolve()
    if a.topic != "topics/visible-flex-larger-amplitude":
        raise ValueError("This task only authorizes the stated topic")
    if not a.owned_ref.startswith("refs/heads/agent-visible-larger-source-"):
        raise ValueError("Require a fresh uniquely named owned source ref")
    if a.state.exists():
        raise FileExistsError("Use a fresh source state")

    def git(*args, data=None, check=True):
        p = subprocess.run(["git", "-c", "gc.auto=0", *args], cwd=repo,
                           input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check and p.returncode:
            raise RuntimeError("git " + args[0] + ": " + p.stderr.decode()[-2000:])
        return p

    def value(*args):
        return git(*args).stdout.decode().strip()

    parent = value("rev-parse", a.parent + "^{commit}")
    initial_head = value("rev-parse", "HEAD")
    if git("show-ref", "--verify", "--quiet", a.owned_ref, check=False).returncode == 0:
        raise ValueError("The named ref already exists; do not overwrite it")
    selection = json.loads(a.selection.read_text())
    records = list(selection["files"])
    if "aggregate" in selection:
        records.append(selection["aggregate"])
    seen, changes = set(), []
    for r in records:
        relative = Path(r["path"])
        if relative.is_absolute() or ".." in relative.parts or r["path"] in seen:
            raise ValueError("Manifest paths must be unique topic-relative paths")
        seen.add(r["path"])
        path = repo / a.topic / relative
        if not path.is_file() or path.is_symlink():
            raise ValueError("Only regular explicitly selected files are permitted")
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != r["sha256"] or len(raw) != r["bytes"]:
            raise ValueError("The immutable selection changed: " + r["path"])
        if len(raw) >= 5_000_000 or (len(raw) > 1_000_000 and path.suffix != ".gz"):
            raise ValueError("The file size/compression rule failed")
        if path.suffix == ".md" and len(raw) >= 100_000:
            raise ValueError("A Markdown file is too large")
        if path.name == "HANDOFF.md" and len(raw) >= 10_000:
            raise ValueError("The HANDOFF bound failed")
        if path.suffix == ".mjs":
            raise ValueError("The current exact-cache MJS tree is frozen")
        oid = git("hash-object", "-w", "--stdin", data=raw).stdout.decode().strip()
        mode = "100755" if path.stat().st_mode & 0o111 else "100644"
        changes.append((Path(a.topic, relative).parts, [mode, "blob", oid]))

    def update_tree(tree, updates):
        entries = {}
        if tree:
            for raw in git("ls-tree", "-z", tree).stdout.split(b"\0"):
                if raw:
                    meta, name = raw.split(b"\t", 1)
                    entries[name.decode()] = meta.decode().split()
        children = {}
        for parts, entry in updates:
            children.setdefault(parts[0], []).append((parts[1:], entry))
        for name, sub in children.items():
            leaves = [(parts, entry) for parts, entry in sub if not parts]
            if leaves:
                if len(sub) != 1:
                    raise ValueError("A selected path is both a file and directory")
                entries[name] = leaves[0][1]
            else:
                prior = entries.get(name)
                if prior and prior[1] != "tree":
                    raise ValueError("An existing file collides with a directory")
                entries[name] = ["040000", "tree", update_tree(prior[2] if prior else None, sub)]
        payload = b"".join((" ".join(entry) + "\t" + name).encode() + b"\0"
                           for name, entry in entries.items())
        return git("mktree", "-z", "--missing", data=payload).stdout.decode().strip()

    tree = update_tree(value("rev-parse", parent + "^{tree}"), changes)
    changed = value("diff", "--name-only", parent, tree).splitlines()
    selected_paths = {str(Path(a.topic, r["path"])) for r in records}
    if not changed or any(p not in selected_paths for p in changed):
        raise ValueError("The new tree is empty or changed an unselected path")
    git("diff", "--check", parent, tree)
    source = git("commit-tree", tree, "-p", parent,
                 data=(a.message.rstrip()+"\n").encode()).stdout.decode().strip()
    # An expected all-zero old value creates this ref only if it is still absent.
    git("update-ref", a.owned_ref, source, "0"*40)
    state = dict(status="Ordinary exact-manifest child source commit retained on a new owned ref",
                 source=source, parent=parent, owned_ref=a.owned_ref,
                 source_topic_tree=value("rev-parse", source+":"+a.topic),
                 source_root_tree=tree, changed_files=len(changed),
                 selected_files=len(records), selection_path=str(a.selection),
                 selection_sha256=hashlib.sha256(a.selection.read_bytes()).hexdigest(),
                 initial_HEAD=initial_head, final_observed_HEAD=value("rev-parse", "HEAD"),
                 no_HEAD_index_lock_or_worktree_write=True, network_operations=0,
                 force_updates=0, utc=datetime.now(timezone.utc).isoformat(),
                 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    a.state.write_text(json.dumps(state,indent=2)+"\n")
    print(json.dumps(state),flush=True)


if __name__ == "__main__":
    main()
