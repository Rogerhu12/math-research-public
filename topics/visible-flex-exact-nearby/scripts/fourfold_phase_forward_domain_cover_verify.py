#!/usr/bin/env python3
"""Close the complete forward cover and all exact/reflected germ dependencies.

This checks an existing collection of proved R65 domain certificates.  It
rechecks file hashes, exact time partitions, common germs, reflected complex
time-disk inclusion and copied bounds.  It does not rerun the Fourier/time
interval computations that produced each direct domain certificate.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def decode(path, raw):
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def ball(q):
    q = Fraction(q)
    return arb(q.numerator) / q.denominator


@dataclass(frozen=True)
class Time:
    q: Fraction = Fraction(0)
    p: Fraction = Fraction(0)

    @classmethod
    def parse(cls, row):
        if isinstance(row, str):
            return cls(Fraction(row))
        if 'kind' in row:
            q = Fraction(int(row['numerator']), int(row['denominator']))
            if row['kind'] == 'rational':
                return cls(q)
            if row['kind'] == 'rational_multiple_of_pi':
                return cls(Fraction(0), q)
            raise ValueError('unsupported exact endpoint kind')
        return cls(Fraction(row['rational']), Fraction(row['pi_coefficient']))

    def __add__(self, other):
        return Time(self.q + other.q, self.p + other.p)

    def __neg__(self):
        return Time(-self.q, -self.p)

    def __sub__(self, other):
        return self + (-other)

    def scale(self, q):
        q = Fraction(q)
        return Time(q*self.q, q*self.p)

    def value(self):
        return ball(self.q) + ball(self.p)*arb.pi()

    def positive_absolute(self):
        if self == Time():
            return self
        if self.value() > 0:
            return self
        if self.value() < 0:
            return -self
        raise ValueError('exact endpoint orientation not separated')


def required_disk_inclusion(new_center, new_half, new_R, old_center, old_half, old_R):
    """Independent exact q+p*pi arithmetic, then one directed pi comparison."""
    displacement = (new_center-old_center).positive_absolute()
    new_radius = new_half.positive_absolute().scale(new_R)
    old_radius = old_half.positive_absolute().scale(old_R)
    margin = old_radius-displacement-new_radius
    if margin == Time():
        return dict(exact_equality=True)
    lower = margin.value().lower()
    if not lower > 0:
        raise ValueError('inherited actual complex-time disk is not contained')
    return dict(exact_equality=False, directed_margin_lower=str(lower))


def positive_record(record, name):
    if not isinstance(record, dict) or 'ball' not in record:
        raise ValueError('missing directed scalar record: '+name)
    if not arb(record['ball']).lower() > 0:
        raise ValueError('saved directed lower bound is not positive: '+name)


class Closure:
    def __init__(self, base, object_sha, root_sha):
        self.base = base.resolve()
        self.object_sha, self.root_sha = object_sha, root_sha
        self.files, self.documents, self.visiting = {}, {}, set()
        self.direct_rows = self.inherited_rows = 0
        self.disk_checks = []
        self.source_paths = {}
        for path in sorted((self.base/'scripts').glob('*.py')):
            self.source_paths.setdefault(digest(path.read_bytes()), []).append(path)

    def path(self, name):
        p = Path(name)
        p = p.resolve() if p.is_absolute() else (self.base/p).resolve()
        if not p.is_relative_to(self.base):
            raise ValueError('certificate path leaves the topic directory')
        return p

    def read(self, name, expected=None, role='dependency'):
        path = self.path(name)
        raw = path.read_bytes()
        d = digest(raw)
        if expected is not None and d != expected:
            raise ValueError('SHA256 differs: '+str(path))
        label = path.relative_to(self.base).as_posix()
        previous = self.files.get(label)
        if previous is not None and previous['sha256'] != d:
            raise ValueError('a certificate changed during closure checking')
        row = self.files.setdefault(label, dict(path=label, sha256=d, bytes=len(raw), roles=[]))
        if role not in row['roles']:
            row['roles'].append(role)
        return path, raw, d

    def check_sources(self, doc):
        source = doc['source_sha256']
        candidates = self.source_paths.get(source, [])
        if not candidates:
            raise ValueError('the exact domain source is absent: '+source)
        self.read(candidates[0], source, 'proved_domain_source')
        for name, expected in doc.get('dependency_sha256', {}).items():
            self.read(Path('scripts')/name, expected, 'proved_domain_dependency')

    def domain(self, name, expected):
        path, raw, d = self.read(name, expected, 'domain_certificate')
        key = path.relative_to(self.base).as_posix()
        if key in self.documents:
            return self.documents[key]
        if key in self.visiting:
            raise ValueError('cyclic domain inheritance')
        self.visiting.add(key)
        doc = decode(path, raw)
        if (not doc.get('complete') or not doc.get('complete_common_span_coverage')
            or not doc.get('proved_full_physical_angle_and_complex_time_domain')
            or doc.get('target_object_sha256') != self.object_sha
            or doc.get('target_root_sha256') != self.root_sha):
            raise ValueError('incomplete or different-object domain: '+key)
        self.check_sources(doc)
        required = [tuple(map(Fraction, row)) for row in doc['required_common_spans']]
        actual = [tuple(map(Fraction, row['common_span'])) for row in doc['germs']]
        if (not required or actual != required or any(a >= b for a,b in required)
            or any(a[1] != b[0] for a,b in zip(required, required[1:]))):
            raise ValueError('the direct domain common-germ list is not complete and adjacent')
        if 'sharp_real_germ_cover' in doc:
            lo, hi = map(Fraction, doc['sharp_real_germ_cover']['exact_outward_radial_bounds'])
            if not required[0][0] <= lo <= hi <= required[-1][1]:
                raise ValueError('saved sharp actual radial image leaves the germ list')
        ta, tb = map(Time.parse, doc['exact_time_endpoints'])
        c, h = (ta+tb).scale(Fraction(1,2)), (tb-ta).scale(Fraction(1,2))
        if h == Time():
            raise ValueError('zero-length time domain')
        R, S = Fraction(doc['time_radius']), Fraction(doc['physical_theta_strip'])
        if not R > 1 or not S > 0:
            raise ValueError('invalid analytic radii')
        for number, row in enumerate(doc['germs']):
            if not row.get('passed') or 'true_field_moduli' not in row:
                raise ValueError('a required germ has no proved true-field bound')
            positive_record(row['D_lower'], 'D_lower')
            if 'curvature' in row:
                curvature = row['curvature']
                k = 'Q_real_lower' if curvature['kind'] == 'root_deflated_Q' else 'minus_K_real_lower'
                positive_record(curvature[k], k)
            else:
                positive_record(row['minus_K_real_lower'], 'legacy ordinary minus_K_real_lower')
            inherited = row.get('inherited')
            if inherited is None:
                self.direct_rows += 1
                continue
            ancestor = self.domain(inherited['path'], inherited['sha256'])
            j = inherited['germ_index']
            if not isinstance(j, int) or not 0 <= j < len(ancestor['germs']):
                raise ValueError('inherited germ index is outside its source')
            old = ancestor['germs'][j]
            cell = tuple(map(Fraction, old['common_span']))
            aa, bb = map(Time.parse, ancestor['exact_time_endpoints'])
            oc, oh = (aa+bb).scale(Fraction(1,2)), (bb-aa).scale(Fraction(1,2))
            if inherited['reflected_time_and_germ']:
                cell, oc, oh = (-cell[1],-cell[0]), -oc, -oh
            if cell != actual[number]:
                raise ValueError('reflected actual scalar germ does not match')
            if not inherited.get('both_branch_signs_valid'):
                raise ValueError('the inherited modulus was not declared for both physical signs')
            if S > Fraction(ancestor['physical_theta_strip']):
                raise ValueError('inherited physical angular strip is narrower')
            inclusion = required_disk_inclusion(c,h,R,oc,oh,Fraction(ancestor['time_radius']))
            for field in ('D_lower','curvature','true_field_moduli'):
                if row.get(field) != old.get(field):
                    raise ValueError('copied inherited bound differs: '+field)
            self.inherited_rows += 1
            self.disk_checks.append(dict(path=key,germ_index=number,source=inherited['path'],
                reflected=bool(inherited['reflected_time_and_germ']),**inclusion))
        self.visiting.remove(key)
        self.documents[key] = doc
        return doc


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index',type=Path,required=True)
    p.add_argument('--retarget',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--snapshot',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--require-full',action='store_true')
    p.add_argument('--bits',type=int,default=192)
    args=p.parse_args();ctx.prec=args.bits
    base=Path.cwd();raw=args.index.read_bytes();index=decode(args.index,raw)
    if args.snapshot.exists() and args.snapshot.read_bytes()!=raw:
        raise ValueError('refuse to replace an immutable prior index snapshot')
    args.snapshot.parent.mkdir(parents=True,exist_ok=True);args.snapshot.write_bytes(raw)
    descriptor_raw=args.retarget.read_bytes();descriptor=decode(args.retarget,descriptor_raw)
    if digest(descriptor_raw)!=index['retarget_descriptor_sha256']:
        raise ValueError('retarget descriptor identity differs from the cover index')
    closure=Closure(base,index['target_object_sha256'],index['target_root_sha256'])
    closure.read(args.snapshot,digest(raw),'immutable_cover_index_snapshot')
    closure.read(args.retarget,index['retarget_descriptor_sha256'],'retarget_descriptor')
    for name,want in [('target_object',index['target_object_sha256']),('target_root',index['target_root_sha256'])]:
        item=descriptor[name]
        if item['sha256']!=want:raise ValueError('target/root descriptor hash differs')
        closure.read(item['path'],want,name)
    grids={}
    for leg in index['time_grid_sha256']:
        item=descriptor['old_'+leg+'_reference']
        _,rr,_=closure.read(item['path'],item['sha256'],'exact_reference_time_grid')
        grid=json.loads(rr)
        if index['time_grid_sha256'][leg]!=item['sha256']:raise ValueError('time-grid identity differs')
        grids[leg]=grid
    requested=[tuple(row)for row in index['requested_cases']]
    if len(requested)!=len(set(requested)):raise ValueError('duplicate requested case')
    cases=index['cases'];seen=set();checked=[]
    for case in cases:
        key=case['leg'],case['segment']
        if key in seen or key not in requested or not case.get('proved'):
            raise ValueError('duplicate/unrequested/unproved completed index case')
        seen.add(key);leg,i=key;grid=grids[leg]
        a,b=map(Time.parse,grid['exact_time_endpoints'][i:i+2])
        intervals=[]
        for leaf in case['leaves']:
            l,r=map(Fraction,leaf['normalized_subspan'])
            if not 0<=l<r<=1:raise ValueError('invalid normalized leaf interval')
            doc=closure.domain(leaf['path'],leaf['sha256'])
            if (doc.get('leg')!=leg or doc.get('segment')!=i
                or doc.get('branch_sign')!=grid['trace_identity']['sign']
                or doc.get('source_sha256')!=index['source_sha256']
                or list(map(Fraction,doc['normalized_subspan']))!=[l,r]
                or list(map(Time.parse,doc['exact_time_endpoints']))!=[a+(b-a).scale(l),a+(b-a).scale(r)]
                or doc['time_grid_manifest_sha256']!=index['time_grid_sha256'][leg]):
                raise ValueError('leaf does not cover its exact claimed reference time subspan')
            for field in ('time_radius','larger_time_radius','physical_theta_strip','wider_physical_theta_strip',
                          'primitive_nodes','independent_root_nodes','angles','cutoff','time_order','bits','R59_sha256'):
                if doc.get(field)!=index.get(field):raise ValueError('leaf run identity differs: '+field)
            intervals.append((l,r))
        intervals.sort()
        if (not intervals or intervals[0][0]!=0 or intervals[-1][1]!=1
            or any(x[1]!=y[0]for x,y in zip(intervals,intervals[1:]))):
            raise ValueError('completed time case has a gap or overlap')
        for attempt in case.get('failed_attempts',[]):
            closure.read(attempt['path'],attempt['sha256'],'preserved_failed_domain_attempt')
        checked.append(dict(leg=leg,segment=i,leaves=len(intervals),exact_partition_checked=True))
    all_requested=seen==set(requested)
    full_set={(leg,i)for leg,grid in grids.items()for i in range(len(grid['exact_time_endpoints'])-1)}
    full=bool(index.get('complete')and index.get('proved_all_requested_cases')
        and index.get('whole_both_branches')and all_requested and seen==full_set)
    forward_set={('forward',i)for i in range(len(grids['forward']['exact_time_endpoints'])-1)}
    forward_complete=bool(index.get('complete')and all_requested and seen==forward_set)
    if args.require_full and not forward_complete:
        raise ValueError('the complete exact forward cover is not present')
    closure.read(Path(__file__).resolve(),role='closure_checker_source')
    report=dict(kind='complete_forward_exact_time_and_germ_domain_cover',status='complete',
        whole_forward_leg=forward_complete,
        whole_both_branches=full,all_requested_cases_present=all_requested,
        covered_cases=len(seen),requested_cases=len(requested),complete_declared_grid_cases=len(full_set),
        original_live_index_path=str(args.index),snapshot_path=str(args.snapshot),snapshot_sha256=digest(raw),
        source_sha256=digest(Path(__file__).read_bytes()),bits=args.bits,
        exact_time_partitions=checked,direct_germ_certificates=closure.direct_rows,
        inherited_germ_links=closure.inherited_rows,independent_disk_inclusion_checks=closure.disk_checks,
        archive_required=sorted(closure.files.values(),key=lambda r:r['path']),
        limitations=['Existing direct Fourier/time interval certificates are not recomputed',
            'No missing time cases are promoted to proved',
            'No true-flow, defect, KAM, or closed-surface conclusion'])
    data=(json.dumps(report,indent=2)+'\n').encode()
    if len(data)>1000000 and args.out.suffix!='.gz':raise ValueError('report above 1MB requires gzip')
    data=gzip.compress(data,mtime=0)if args.out.suffix=='.gz'else data
    if len(data)>5000000:raise ValueError('split the closure report under 5MB')
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_bytes(data)
    print(json.dumps(dict(whole_forward_leg=forward_complete,whole_both_branches=full,covered_cases=len(seen),direct=closure.direct_rows,
        inherited=closure.inherited_rows,closure_files=len(closure.files),sha256=digest(data))),flush=True)


if __name__=='__main__':main()

