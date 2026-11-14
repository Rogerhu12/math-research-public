#!/usr/bin/env python3
"""Operational checkpoints around the unchanged actual tail linear verifier.

Every completed cell is closed as a separate gzip member, so a later
external process exit does not erase previously completed continuous
bounds. Stage timing/RSS separates input construction from polynomial and
angular work. Mathematical formulas and defining inputs are unchanged.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time

HERE = Path(__file__).resolve().parent
source = HERE/'fd2d-metric-c2-tail-linear-continuous.py'
spec = importlib.util.spec_from_file_location('fd2d_checkpointed_tail_engine', source)
engine = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = engine
spec.loader.exec_module(engine)
started = time.monotonic()
out = Path(sys.argv[sys.argv.index('--out')+1])
checkpoints = out.with_suffix('.checkpoints.jsonl.gz')
if out.exists() or checkpoints.exists():
    raise FileExistsError('Use a new report/checkpoint name')


def event(stage, **values):
    row = dict(stage=stage, seconds=time.monotonic()-started,
               peak_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024, **values)
    with checkpoints.open('ab') as stream:
        stream.write(gzip.compress((json.dumps(row, separators=(',', ':'))+'\n').encode(), mtime=0))
    if stage != 'cell_done' or values.get('ordinal', 0) <= 20 or values.get('ordinal', 0) % 100 == 0:
        print(json.dumps(row), flush=True)


OldReader = engine.light.CheckedTailDefinition


class Reader(OldReader):
    def __init__(self, manifest):
        event('raw_definition_start')
        super().__init__(manifest)
        event('raw_definition_done', nodes=len(self.nodes), coefficients=self.C)


engine.stream.frozen.IntegratedTail = Reader
OldGeometry = engine.stream.StreamingExactIntegratedTail


class Geometry(OldGeometry):
    def __init__(self, *args, **kwargs):
        event('strict_geometry_start')
        super().__init__(*args, **kwargs)
        event('strict_geometry_done', spans=self.N)


engine.stream.StreamingExactIntegratedTail = Geometry
OldField = engine.linear.Field


class Field(OldField):
    def __init__(self, path):
        event('actual_field_start')
        super().__init__(path)
        event('actual_field_done', nodes=len(self.x), modes=self.M)


engine.linear.Field = Field
old_trig = engine.linear.trigonometry
seen_trig = set()


def trigonometry(modes, arcs):
    key = (modes, arcs)
    if key in seen_trig:
        return old_trig(modes, arcs)
    event('trigonometry_start', modes=modes, arcs=arcs)
    result = old_trig(modes, arcs)
    seen_trig.add(key)
    event('trigonometry_done', modes=modes, arcs=arcs)
    return result


engine.linear.trigonometry = trigonometry
OldTail = engine.Tail


class Tail(OldTail):
    def __init__(self, *args, **kwargs):
        event('tail_model_start')
        super().__init__(*args, **kwargs)
        self.ordinal = 0
        event('tail_model_done', radial_cells=len(self.mesh)-1)

    def polynomials(self, left, right):
        if self.ordinal == 0:
            event('first_polynomials_start')
        value = super().polynomials(left, right)
        if self.ordinal == 0:
            event('first_polynomials_done')
        return value

    def bound(self, left, right, angular):
        value = super().bound(left, right, angular)
        self.ordinal += 1
        event('cell_done', ordinal=self.ordinal, left_exact=str(left), right_exact=str(right),
              linear_operator_upper=value[0], packet_row=value[1], tail_span=value[2])
        return value


engine.Tail = Tail
event('start', engine_sha256=hashlib.sha256(source.read_bytes()).hexdigest(), argv=sys.argv[1:])
try:
    engine.main()
    report = json.loads(out.read_text())
    event('complete', complete_tail_activity_domain=report['complete_tail_activity_domain'],
          linear_operator_upper=report['linear_operator_upper'])
    report['operational_checkpoint_adapter'] = engine.identity(__file__)
    report['completed_cell_checkpoints'] = engine.identity(checkpoints)
    report['mathematical_formulas_changed_by_checkpoint_adapter'] = False
    out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
except BaseException as error:
    event('exception', exception_type=type(error).__name__, message=str(error))
    raise
