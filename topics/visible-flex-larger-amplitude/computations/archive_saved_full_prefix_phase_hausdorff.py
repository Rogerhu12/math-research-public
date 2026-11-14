#!/usr/bin/env python3
"""Freeze complete finite-set phase evidence; do not copy derived point arrays.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This independently consumes the saved rational sandwiches and exact binary
witness distances. The original full point sweeps are not repeated.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def unrat(value):return F(int(value['numerator']),int(value['denominator']))
def rat(value):value=F(value);return dict(numerator=str(value.numerator),denominator=str(value.denominator))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--primary',type=Path,required=True)
    p.add_argument('--resource',type=Path,required=True)
    p.add_argument('--top',type=Path,required=True)
    p.add_argument('--tag',required=True)
    a=p.parse_args()
    result,owned=read(a.primary),read(a.resource)
    producer=Path(__file__).with_name('root_saved_full_prefix_phase_hausdorff.py')
    if not (owned['exitcode']==0 and owned['wait4_observed'] and owned['termination_signal'] is None and
            result['source_sha256']==sha(producer) and result['all_complete_points_and_chunks_consumed'] and
            result['prefix_count']==2_890_752 and result['reflected_union_count']==5_781_504 and
            result['new_ODE_Node_Jacobian_or_geometry_field_calls']==0):
        raise ValueError('The actual complete identified finite-set run is required')
    for path,want in result['input_sha256'].items():
        if sha(path)!=want:raise ValueError('A finite-set input changed: '+path)
    chunk_bytes=0
    for item in result['chunks']:
        if sha(item['file'])!=item['sha256'] or Path(item['file']).stat().st_size!=item['bytes']:
            raise ValueError('An original complete saved point chunk changed')
        chunk_bytes+=item['bytes']
    cursor=0
    for item in result['query_blocks']:
        if item['first']!=cursor or not cursor<item['last']<=result['prefix_count']:
            raise ValueError('The full source sweep has a gap')
        cursor=item['last']
    if cursor!=result['prefix_count']:raise ValueError('The full source sweep is incomplete')
    counts={}
    def check(name,ok):
        counts[name]=counts.get(name,0)+1
        if not ok:raise ArithmeticError(name)
    for key,row in result['directed_cases'].items():
        lo,hi=map(unrat,(row['finite_directed_Hausdorff_lower'],row['finite_directed_Hausdorff_upper']))
        q=unrat(row['exact_witness_selected_pair_squared'])
        source=row['actual_directed_source_point'];target=row['actual_directed_target_point']
        actual=sum(((F.from_float(float(x))-F.from_float(float(y)))**2 for x,y in zip(source,target)),F(0))
        check('exact_binary_actual_pair_identity',q==actual)
        check('nonnegative_exact_finite_sandwich',0<=lo<=hi and lo*lo<=q<=hi*hi)
        check('upper_exact_square_sandwich',hi*hi>=unrat(row['exact_global_selected_pair_squared_upper']))
        check('all_original_sources_scanned',row['complete_base_sources_scanned']==result['prefix_count'])
        check('all_witness_targets_directly_scanned',row['complete_witness_targets_scanned']==result['prefix_count']*(2 if key.startswith('reflected_union') else 1))
        check('original_set_members_and_scope',row['all_selected_pairs_are_actual_set_members'] and row['no_exact_unique_nearest_point_claim'])
        check('actual_core_witness',row['witness_base_point']['radial_index']==0 and row['witness_base_point']['physical_s']==0.)
    aggregate={}
    for name,row in result['sets'].items():
        low,high=map(unrat,(row['finite_Hausdorff_lower'],row['finite_Hausdorff_upper']))
        directed=[result['directed_cases'][name+suffix] for suffix in ('_to_rotated','_rotated_to_original')]
        check('both_directions_aggregated',low==max(unrat(r['finite_directed_Hausdorff_lower']) for r in directed) and high==max(unrat(r['finite_directed_Hausdorff_upper']) for r in directed))
        check('strict_positive_interval',0<low<=high)
        ratios=list(map(unrat,row['finite_Hausdorff_over_same_finite_D_bounds']))
        check('ratio_is_finite_diagnostic_below_one_fifth',0<ratios[0]<=ratios[1]<F(1,5))
        aggregate[name]=dict(H_lower=rat(low),H_upper=rat(high),ratio_lower=rat(ratios[0]),ratio_upper=rat(ratios[1]))
    prior=a.top/'notes/2026-11-13-strong-fine-q126-complete-warm-points-r1-manifest.json'
    if not prior.exists():raise FileNotFoundError('Retain the existing original full warm point reproduction archive')
    receipt=dict(schema='finite-complete-phase-saved-rational-consumption-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        primary_sha256=sha(a.primary),original_owned_resource_sha256=sha(a.resource),
        exact_saved_gate_count=sum(counts.values()),exact_saved_gate_multiplicities=counts,
        all_saved_consumption_gates=True,aggregate=aggregate,
        actual_full_query_block_count=len(result['query_blocks']),
        original_points=dict(chunks=len(result['chunks']),bytes=chunk_bytes,sha256_manifest_complete=True,copied=False),
        original_point_reproduction_archive=dict(path=str(prior.relative_to(a.top)),sha256=sha(prior)),
        no_new_point_scan_ODE_or_geometry_field=True,
        scope='Exact saved binary finite sets and their prescribed ambient rotation only; no continuous curve, accepted A, closure or rigid-motion quotient amplitude theorem.')
    receipt_path=a.primary.with_name(a.primary.stem+'-saved-consumption.json')
    if receipt_path.exists():raise FileExistsError(receipt_path)
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    proof='''# Complete A-warm prefix: quarter-turn finite Hausdorff distance

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Object and result

This is a rigorous finite-data statement about the saved binary64 Cartesian
points of the **unsolved A q126 M32 warm field based on accepted q122**. It is
not the subsequently accepted A solution, and it is not q122's point cloud.
Let P consist of every saved point, N=2,890,752 (3764 radial values, 768 angles).
Let J(x,y,z)=(x,y,-z), S=P union JP, and R(x,y,z)=(-y,x,z). All eighteen saved
chunks were hashed and consumed; S has 5,781,504 listed points (coincident
points need not be removed). The complete production mean at 1552 angles was
used when the original warm points were created.

For both P and S, the two directed finite distances give the same enclosed
Hausdorff distance:

    0.2506934490470827 <= d_H(P,RP), d_H(S,RS)
                         <= 0.25069344904708285.

These decimals are display values. The primary packet stores the controlling
exact rational endpoints. P's already certified finite diameter lies in
[2.7255845000752186,2.7819531656262475], giving a finite distance/diameter ratio
between 0.09011418745097706 and 0.09197786714745566. S's finite diameter lies in
[3.973839591888201,3.973839591888202], giving the ratio interval
[0.06308595081664171,0.06308595081664177]. Neither diameter is identified with
the diameter of a completed closed surface.

The forward witness is the saved core point (radial index 0, angular index 1)
at actual s=0, numerical eta=0.008181230868723419, with Cartesian coordinates
(1.1158349103141398,0.0067531530328886905,0). Its selected nearest target is
R times the core point at angular index 577, namely
(0.865180387494543,0.011170797790274767,0). The reverse-direction witness also
lies on the core, at original angular index 383. Complete direct target scans
are paid for each witness; uniqueness of a nearest point is not asserted.

Thus the complete finite prefix search finds no distance much larger than
the core witness. Its maximum exceeds the earlier single-axis finite witness
0.2506414867725137 by about 0.0000519623. This small difference is not a
continuous-surface improvement: the target is still discretized. No spatial
sampling error has been paid in this packet.

## Phase convention and complete directed coverage

The frozen R1 phase family is F_alpha(s,theta)=R_alpha F_0(s,theta-alpha).
For a complete angular image, reparametrization does not change the set, so
alpha=pi/2 is the actual ambient quarter-turn R. The present computation
selects the saved image points and then applies that exact signed coordinate
permutation. It never replaces a set distance by the displacement of the
same material index. Every target radial and angular index is allowed.

The two original point sweeps compute d(P,RP) and d(P,R^-1 P). Applying R to
both sets in the latter yields d(RP,P). For S, R and J commute and S is
J-invariant. Hence the distance from JP to RS equals that from P to RS; the
same identity applies to the reverse direction. It therefore suffices to
scan all P source points while allowing both P and JP targets. This is an
exact isometry reduction, not a missing half of the source set.

## Finite upper bound without trusting nearest-neighbor optimality

The tree returns one actual saved target for every source point. A selected
target need not be the mathematically nearest target: its distance always
upper-bounds the minimum over the target set. The producer forms the squared
distance to that actual target and takes the maximum over every source,
separately in both directions. Thus even an inaccurate tree search could
only weaken the finite upper bound. The subsequent small consumer verifies
complete source block coverage and the saved pair/rational identities.

For coordinates of magnitude below 1024, compute three rounded differences,
their squares, and the sum of three nonnegative terms. With binary64 unit
roundoff u=2^-53, a path from one squared exact difference to the sum pays at
most five relative factors: two from squaring the rounded difference, one
from the product, and at most two additions. Gradual-underflow errors are
covered by the positive absolute allowance e=2^-1000; the magnitude guard
makes this much larger than the total subnormal contribution. Thus for each
computed squared distance qhat and exact binary-coordinate distance q,

    (qhat-e)/(1+u)^5 <= q <= (qhat+e)/(1-u)^5.

Taking the maximum of the computed selected distances and then the right
endpoint gives a valid exact global upper squared bound. The saved square
root upper endpoint is a dyadic rational with 100 fractional bits, checked
by exact squaring. The arithmetic claim assumes the ordinary IEEE binary64
round-to-nearest elementary operations used by the unchanged NumPy source.

## Finite lower bound by all-target direct scans

At each selected global witness W, the producer separately scans every
actual target point, without the tree. For S this includes both reflected
copies. If qhat_min is the minimum of these computed squared distances, the
uniform left inequality above bounds every exact target distance below by
(qhat_min-e)/(1+u)^5. Its nonnegative part and a dyadic square-root lower
endpoint give a lower bound for the true nearest distance from W, and hence
for the directed Hausdorff distance. The selected witness-target pair is
also evaluated as an exact rational sum of three squared binary-coordinate
differences. Both displayed directional intervals therefore have complete
upper and lower justifications and do not depend on tree optimality.

## Scope that remains open

No unrepresented radial/angle points, continuous sampling error, infinite
tail, fixed cap or marker, all-phase maximum, reach bound, or completed
closed-surface diameter is included. The warm field has not been converted
into the later accepted A field by relabeling. The R1/R7 formulas motivate
the chosen phase, but this finite calculation does not assert that the
entire warm field is an exact isometric deformation.

The Euclidean-motion quotient distance between P and RP (and between S and
RS) is exactly zero, since R^-1 is an allowed ambient rigid motion. A lower
bound for the topic's delta_E requires the completed fixed geometry and a
separate argument excluding all global Euclidean alignments. The present
positive number is only the prescribed quarter-phase finite set distance;
it is neither delta_E nor the full delta_hold of a completed family.

## Reproduction and storage

The owned resource gives the verbatim command. The primary packet records
all source/input hashes, all eighteen chunk hashes, complete source-block
coverage, the four direct scans, and exact rational bounds. The original
complete warm-point archive provides the geometry regeneration chain. Large
derived point blocks stay in scratch and are not copied. The present compact
archive includes this source, full small primary, resource and saved-rational
consumer. No new ODE, Node worker, Jacobian or geometry field was required.
'''
    proof+=f"\nOriginal owned execution: exit 0; {owned['wall_seconds']:.9f} seconds; peak {owned['peak_rss_kib']} KiB.\n"
    pairs=[(producer,a.top/'computations'/producer.name),(Path(__file__),a.top/'computations'/Path(__file__).name),
           (a.primary,a.top/'notes'/f'{a.tag}-primary.json'),(a.resource,a.top/'notes'/f'{a.tag}-resource.json'),
           (receipt_path,a.top/'notes'/f'{a.tag}-saved-consumption.json')]
    files=[]
    for source,dest in pairs:
        data=source.read_bytes()
        if len(data)>=1_000_000:raise ValueError('This compact archive must not copy point blocks')
        if dest.exists():
            if dest.read_bytes()!=data:raise ValueError('Never overwrite a frozen artifact')
        else:dest.write_bytes(data)
        files.append(dict(path=str(dest.relative_to(a.top)),sha256=sha(dest),bytes=len(data),original_path=str(source)))
    note=a.top/'notes'/f'{a.tag}-proof.md'
    if note.exists():raise FileExistsError(note)
    note.write_text(proof);files.append(dict(path=str(note.relative_to(a.top)),sha256=sha(note),bytes=note.stat().st_size))
    manifest=a.top/'notes'/f'{a.tag}-manifest.json'
    if manifest.exists():raise FileExistsError(manifest)
    manifest.write_text(json.dumps(dict(schema='complete-finite-prefix-phase-Hausdorff-archive-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',classification='rigorous binary finite-set bounds; continuous geometry unproved',
        files=files,total_bytes=sum(row['bytes'] for row in files),all_derived_point_hashes_retained=True,
        derived_point_blocks_copied=False,continuous_or_accepted_A_claim=False,
        original_warm_point_reproduction_archive=receipt['original_point_reproduction_archive']),indent=2)+'\n')
    print(json.dumps(dict(manifest=str(manifest),sha256=sha(manifest),files=len(files),total_bytes=sum(row['bytes'] for row in files),saved_gates=sum(counts.values()))),flush=True)


if __name__=='__main__':main()
