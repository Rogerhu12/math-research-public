"""Read actual process limits and its readable cgroup memory files.

Missing mounts or inaccessible files are recorded as unknown, never unlimited.
This observer neither changes limits nor enters a different cgroup/namespace.
"""
import os
from pathlib import Path


FILES = ('memory.max', 'memory.high', 'memory.current', 'memory.peak',
         'memory.events', 'memory.events.local', 'memory.swap.max',
         'memory.swap.current', 'memory.limit_in_bytes',
         'memory.soft_limit_in_bytes', 'memory.usage_in_bytes',
         'memory.max_usage_in_bytes', 'memory.failcnt', 'memory.oom_control')


def read(path):
    try:
        return dict(text=Path(path).read_text())
    except OSError as error:
        return dict(error=type(error).__name__, errno=error.errno,
                    message=str(error))


def snapshot(pid=None):
    pid = os.getpid() if pid is None else int(pid)
    proc = Path('/proc')/str(pid)
    cgroup, mountinfo = read(proc/'cgroup'), read(proc/'mountinfo')
    mounts = []
    for line in mountinfo.get('text', '').splitlines():
        left, separator, right = line.partition(' - ')
        if not separator:
            continue
        lf, rf = left.split(), right.split()
        if rf[0] in ('cgroup', 'cgroup2'):
            mounts.append(dict(root=lf[3], mountpoint=lf[4], type=rf[0],
                               super_options=rf[2], raw=line))
    candidates = set()
    for line in cgroup.get('text', '').splitlines():
        _, controllers, group = line.split(':', 2)
        for mount in mounts:
            unified = not controllers and mount['type'] == 'cgroup2'
            memory = ('memory' in controllers.split(',') and
                      mount['type'] == 'cgroup' and
                      'memory' in mount['super_options'].split(','))
            if not (unified or memory):
                continue
            try:
                relative = Path(group).relative_to(mount['root'])
            except ValueError:
                continue
            directory = Path(mount['mountpoint'])/relative
            candidates.add(str(directory))
    # If the process reports membership but the mount is hidden, record the
    # ordinary location's absence too. This is a read, not a mount operation.
    if not candidates:
        candidates.add('/sys/fs/cgroup')
    files = {}
    for directory in sorted(candidates):
        for name in FILES:
            logical = Path(directory)/name
            access = (proc/'root'/logical.relative_to('/')) if pid != os.getpid() else logical
            files[str(logical)] = dict(access_path=str(access), **read(access))
    return dict(pid=pid, cgroup=cgroup, actual_cgroup_mounts=mounts,
        mountinfo_read_error={k:v for k,v in mountinfo.items() if k != 'text'},
        limits=read(proc/'limits'), memory_files=files,
        no_readable_cgroup_is_not_an_unlimited_memory_claim=True,
        limits_or_cgroup_changed=False)


def numeric_values(record):
    result = {}
    for path, value in record.get('memory_files', {}).items():
        text = value.get('text', '').strip()
        if text.isdigit():
            result[path] = int(text)
        else:
            for line in text.splitlines():
                fields = line.split()
                if len(fields) == 2 and fields[1].isdigit():
                    result[path+'::'+fields[0]] = int(fields[1])
    return result


def difference(before, after):
    old, new = numeric_values(before), numeric_values(after)
    return dict(readable_numeric_deltas={key:new[key]-old[key]
        for key in sorted(old.keys() & new.keys())},
        readable_numeric_fields_before=len(old),
        readable_numeric_fields_after=len(new),
        changed_counter_does_not_attribute_a_kill_to_this_process=True)
