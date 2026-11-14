#!/usr/bin/env python3
"""Observe existing limits of this entry and its own Node child, without changes.

Only read-only resource observations are added to the retained iteration
recovery entry and existing young-space guard.  The exact original spawn
arguments, inherited options, mathematical sources, states and acceptance
gates remain.  Unavailable observations do not become solver failures.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import runpy
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
ENTRY = HERE/'strong_cached_iteration_tail_audit.py'
ENTRY_SHA = '1e00cc9920d2f2dcacedaf034877999259f8962abf931c1e699c3df3035ed6ff'
GUARD_SHA = '867244ef03a99ea50f7629d437873c073e9a07ee8a88b48568c79817be7b7eba'
WORKER = HERE/'strong_exact_stage_tail_worker.mjs'
LIMIT_NAMES = ('CPU', 'AS', 'DATA', 'RSS', 'STACK', 'FSIZE', 'NOFILE', 'NPROC', 'MEMLOCK')


def limits_of_owned_process(pid=None):
    values, errors = {}, {}
    for name in LIMIT_NAMES:
        kind = getattr(resource, 'RLIMIT_'+name, None)
        if kind is None:
            errors[name] = 'Unavailable resource limit identifier'
            continue
        try:
            pair = resource.getrlimit(kind) if pid is None else resource.prlimit(pid, kind)
            values[name] = dict(soft=pair[0], hard=pair[1],
                soft_unlimited=pair[0] == resource.RLIM_INFINITY,
                hard_unlimited=pair[1] == resource.RLIM_INFINITY)
        except (OSError, ValueError, AttributeError) as error:
            errors[name] = repr(error)
    return dict(read_only=True, limits_unchanged=True, limits=values, unavailable=errors)


def persist(prefix, suffix, value):
    from strong_tail_constructor_guard import atomic_same
    path = Path(prefix).with_name(Path(prefix).name+suffix)
    try:
        atomic_same(path, (json.dumps(value, indent=2)+'\n').encode())
    except (OSError, ValueError) as error:
        # Optional diagnostic output cannot change numerical acceptance or
        # hide an original exception; the retained resource guard owns cleanup.
        print(json.dumps(dict(event='owned_limit_observation_unavailable',
            output=str(path), error=repr(error))), file=sys.stderr, flush=True)


def observed_class(Base):
    class LimitObservedPort(Base):
        def __init__(self, *args, **kwargs):
            prefix = kwargs.get('record_prefix', args[2] if len(args) > 2 else None)
            if prefix is None:
                raise ValueError('The owned limit observer needs an explicit record prefix')
            original = subprocess.Popen
            def spawn(command, *rest, **options):
                child = original(command, *rest, **options)
                if isinstance(command, (list, tuple)) and str(WORKER) in command:
                    # The PID is obtained only from this successful owned spawn.
                    self.proc = child
                    persist(prefix, '_Node-limits-spawn.json', dict(
                        observer_sha256=SELF_SHA, phase='immediately-after-owned-spawn',
                        owned_child_pid=child.pid, observed_at_unix=time.time(),
                        actual_command=list(command),
                        NODE_OPTIONS=options.get('env', {}).get('NODE_OPTIONS'),
                        parent_limits=limits_of_owned_process(),
                        child_limits=limits_of_owned_process(child.pid),
                        no_claim_about_prior_termination_cause=True))
                return child
            subprocess.Popen = spawn
            try:
                super().__init__(*args, **kwargs)
                persist(prefix, '_Node-limits-ready.json', dict(observer_sha256=SELF_SHA,
                    phase='after-original-ready', owned_child_pid=self.proc.pid,
                    observed_at_unix=time.time(), child_limits=limits_of_owned_process(self.proc.pid),
                    original_ready_not_modified=True,
                    no_claim_about_prior_termination_cause=True))
            finally:
                subprocess.Popen = original
    return LimitObservedPort


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--entry', type=Path, required=True)
    args, remaining = parser.parse_known_args()
    if (args.entry.resolve() != ENTRY or hashlib.sha256(ENTRY.read_bytes()).hexdigest() != ENTRY_SHA
            or hashlib.sha256((HERE/'strong_tail_young_space_guard.py').read_bytes()).hexdigest() != GUARD_SHA):
        raise ValueError('The retained recovery/resource entry changed')
    if remaining.count('--out-prefix') != 1:
        raise ValueError('One explicit fresh recovery prefix is required')
    prefix = Path(remaining[remaining.index('--out-prefix')+1])
    prefix.parent.mkdir(parents=True, exist_ok=True)
    persist(prefix, '-limit-observer-entry.json', dict(scope=__doc__,
        observer_sha256=SELF_SHA, retained_entry_sha256=ENTRY_SHA,
        retained_young_space_guard_sha256=GUARD_SHA,
        inherited_entry_limits=limits_of_owned_process(),
        original_spawn_and_mathematical_parameters_unchanged=True,
        observations_only_not_a_numerical_execution_claim=True))
    import strong_tail_young_space_guard as guard
    original_factory, old_argv = guard.resource_port_class, sys.argv
    guard.resource_port_class = lambda Base, *a, **kw: observed_class(original_factory(Base, *a, **kw))
    sys.argv = [str(ENTRY), *remaining]
    try:
        runpy.run_path(str(ENTRY), run_name='__main__')
    finally:
        guard.resource_port_class = original_factory
        sys.argv = old_argv


if __name__ == '__main__':
    main()
