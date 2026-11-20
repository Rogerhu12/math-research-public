#!/usr/bin/env python3
"""Materialize the documented a04 field chain in public repository Actions.

This is orchestration, not a new solver. Every scientific subprocess is an
already published complete source with explicit parameters. Historical names
are recipe labels, never claims that a fresh field has an old byte identity.
Old scientific certificates are not reused. Historical side branches whose
only surviving influence was a list of positions are supplied as small,
ordered position parameters, with their original provenance and no values.

Local --print-only reads source metadata and emits a command plan; it neither
imports a scientific module nor starts scientific computation. Actual runs
require this repository's public GitHub Actions environment.
"""
import argparse
import copy
import gzip
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time


REPOSITORY = 'Rogerhu12/math-research-public'
TOPIC = 'topics/visible-flex-larger-amplitude'
OLD_BLOB = ('60321451c058c6a51da58c37ae5ec6f2d1145f74:' + TOPIC +
            '/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz')
R11 = '.30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26'
R17 = ('.30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,'
       '2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,'
       '2.301232686234047,2.321299871729826')
R22 = ('.30,.60,.83,.99,.995,1.0,1.02,1.05,1.077134370991557,1.097,'
       '1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,'
       '2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826')
FULL_E8_CENTERS = ('.3,.6,.8275,1.0570671854957785,1.1975374839662283,'
                   '1.3580749679324564,1.5587468228902417,1.759418677848027,'
                   '1.9600905328058122,2.140695202267819,2.26109831524249')
FULL_GAUSS_CENTERS = ('0.3,0.6,0.8300000000000001,1.0570671854957785,'
                      '1.1975374839662283,1.3580749679324564,1.5587468228902417,'
                      '1.759418677848027,1.9400233473100337,2.140695202267819,'
                      '2.26109831524249')

SOURCE_NAMES = {
    'reproduce': 'scripts/resume_20261120/reproduce_and_solve.py',
    'prefix_rebuild': 'scripts/resume_20261120/rebuild_fullclosed.py',
    'warm_rebuild': 'scripts/resume_20261120/rebuild_closed_warm.py',
    'operator': 'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
    'batch': 'scripts/resume_20261120_batched_closed_gram.py',
    'base': 'scripts/resume_20261120_physical_subspace.py',
    'coarse': 'scripts/resume_20261120_physical_subspace_v3.py',
    'qp': 'scripts/resume_20261120_curvature_qp.py',
    'memory': 'scripts/resume_20261120_curvature_qp_v2.py',
    'gauss': 'scripts/resume_20261120_curvature_qp_v3.py',
    'v4a': 'scripts/resume_20261120_curvature_qp_v4a.py',
    'v4b': 'scripts/resume_20261120_curvature_qp_v4b.py',
    'v5': 'scripts/resume_20261120_curvature_qp_v5_h2.py',
    'v6': 'scripts/resume_20261120_curvature_qp_v6_spectral.py',
    'v7': 'scripts/resume_20261120_curvature_qp_v7_spectral_hessian.py',
    'observed': 'scripts/resume_20261120/gauss_observed_closed_gram.py',
    'carrier_generator': 'scripts/resume_20261120/read_gauss_closed_gram.py',
    'norm': 'scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py',
    'coordinate': 'notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py',
    'scale': 'scripts/integrated_l2_scale_20261120.py',
    'height': 'scripts/resume_20261120/physical_height_coordinates.py',
    'spectral': 'scripts/resume_20261120/positive_spectral_gram_weights.py',
    'hessian': 'scripts/resume_20261120/positive_spectral_gram_hessian.py',
    'helpers': 'scripts/resume_20261120/fullclosed_lm.py',
    'e8_solver': 'scripts/resume_20261120/fullclosed_integrated_h2_lm_v3.py',
    'def1_solver': 'scripts/resume_20261120/fullclosed_gauss_h2_projected_lm.py',
    'full13_solver': 'scripts/resume_20261120/fullclosed_gauss_physical_height_memory_lm.py',
    'point_observed': 'scripts/resume_20261120/fullclosed_point_cotangent_observed.py',
    'point_memory': 'scripts/resume_20261120/fullclosed_point_cotangent_memory.py',
    'exporter': 'scripts/resume_20261120_export_curvature_history_manifest.py',
}
SOURCE_SHA = {
    'operator': 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d',
    'batch': '02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a',
    'base': '1da3fac6c2050f9615c9c023e87e58a67e1d36cb578e791abb8903a771d2bfc7',
    'coarse': '118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8',
    'qp': 'a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854',
    'memory': '87978e04453f44914efed0bff933e3ff0790d3a24656f941b3a6c296cb458d80',
    'gauss': '3131377740b06ff400b1a74e3efe349c987769c4c4d3c2cbf40ea40ad9c9308e',
    'v4a': 'd3ee2f2dce84ba9401f6a993109741564c65f9317356bd2a9431b489d0a633de',
    'v4b': 'f8dee5e090e9353b611598e42c135bd3855d856aafe6e2e80499478eec40933f',
    'v5': 'fac7b5834a932242f320d91af1dad4466dd2c895b0074a7d4b7ab6601fb5e693',
    'v6': '1872298863d3d0309c74a35f4f93bdf1373528c5e28d3cfd0e6c4545f3be0ea0',
    'v7': '702c9e13db661d39771aa673dca7c19120c695da16556919e63918705b038ec8',
    'observed': '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d',
    'norm': 'd308f6d53ef34be692ca342f93a3874f8b160b41134e0ecc353d9670742523eb',
    'coordinate': 'd429d68baded58908454e49f4bfdf8e43ce9d3f857ed666eafa95c1c366462db',
    'scale': 'ff147637f4d5ebc52700e0ee58ba168374fb86ff72f641ae004ba67e2eb5c560',
    'height': 'f26738f9ee5a27ec861a9a9cbdc99b301edb6c6b3b271320e567a3892fab5f0e',
    'spectral': 'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91',
    'hessian': '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4',
    'e8_solver': '9283403609c185dfcaa9de70038cc98d89618d99e3200a7cfd519f0af650e3d1',
    'def1_solver': 'c6e5fbf2426a273b0672710125720181f7bdd558011717369afe1efb84aac180',
    'full13_solver': 'ae596f07e8808737e26f95ec67d79d81bf696af264b11fc791165abf05a8697b',
    'point_observed': 'de58a82e4a30a794f04e4cbf980d16d0a3b70f47a3afffc71986079ec11e5a5e',
    'point_memory': '029f581c74082e36fd37663192a0bb42a20ef595c324c1d4e1e8f85e1657c26e',
    'exporter': 'f2d7cda73b0b5634a869cb0971c811b24af00e540eff8e62ca6741aba762866f',
}
HISTORICAL_SHA = {
    'warm': '79c161cc11a0743209ca3947e2b0f51f7ab7046e14ebfadf519f5d6e7259edba',
    'af89': 'af89a4414fb0cee35d75dba5530e9b45b62abd248ddf7509cca92c2a9696a505',
    'e8': 'e8b2ca40e184157abba15c3c85ebdd651e38cbb4035edb2cfd652c8b57ad0637',
    '2038': '2038ba41e2001036eebe8bc43fccbb54b8d9ccf180f73139420798de278bcaa9',
    'def1': 'def1ccbded6c463a014a71a39f259c59501412d5c84afec07ce7253c9dc34f5d',
    '6077': '607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941',
    'v4b_12': '2b143b5fb1f68c6bb9fe46ccc748755e125629786e072d8eb42e4903e4e4d453',
    '13ce': '13ce4975470b0aca3717ce20402616688857f5fd3b844f83d1a4f338af418614',
    'e19': 'e19acbc3cc600b37ac5d50bc7448ffe229a6a1c8119798b62165d7460ac9fec7',
    '0241': '0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023',
    '8d': '8d7407edf7587403ebec783d1c208888f78ef78b4079c719ad3c87dcfc50db59',
    'ca367': 'ca3679b4d6401febdf89b222d253ae6ae88b0b3ab2cd7b4464185ae2d9c2c632',
    '077': '077087b778921efd85e1b6bbe3b8389bd60f385e2de0e5a767b8f705bc847dc3',
    'bede': 'bede53ea69f41d6bb4dedd4805cb94e2bc5abefc8ec69fff3a793f4fd3beffa2',
    '35f': '35f74961a297775f7e38c01cee7f9ed5516e98c48964f758f1795b76d2061ebf',
    'a04': 'a04f9faf228c3785ab785314eb14836bdad598a6d6ac826c4abf15100225f4e0',
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def scalar_definition(data):
    profile = data['inward_scalar_profile']
    return dict(fixed_scalar_profile=data['fixed_scalar_profile'],
        analytic_extension_origin=data['analytic_extension_origin'],
        inward_parameters={k: profile[k] for k in
            ('cut', 'curvature', 'ramp_in', 'ramp_out', 'quadrature')},
        compact_curvature_pulse=profile['compact_curvature_pulse'])


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    tmp.replace(path)


def options(**values):
    result = []
    for key, value in values.items():
        if value is None or value is False:
            continue
        key = '--' + key.replace('_', '-')
        if value is True:
            result.append(key)
        else:
            for item in value if isinstance(value, (tuple, list)) else [value]:
                result.extend((key, str(item)))
    return result


def make_plan(repo, work, stop_after):
    topic = repo / TOPIC
    source = {k: topic / v for k, v in SOURCE_NAMES.items()}
    geom = work / 'geometry_path'
    full = work / 'fullclosed_solver'
    carrier = work / 'recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz'
    seed_dir = work / 'historical-position-parameters'
    seed = lambda name: seed_dir / (name + '.json')
    stages = []

    def add(name, argv, *, parent=None, bundle=None, report=None,
            scope='Fresh finite numerical field; no inherited certificate',
            action=None, extra_outputs=(), parameters=None):
        stages.append(dict(name=name, argv=[str(x) for x in argv],
            parent=str(parent) if parent else None,
            bundle=str(bundle) if bundle else None,
            report=str(report) if report else None, scope=scope, action=action,
            extra_outputs=[str(x) for x in extra_outputs], parameters=parameters or {},
            historical_bundle_sha256=HISTORICAL_SHA.get(name)))

    def python(role, **kwargs):
        return [sys.executable, '-u', source[role], *options(**kwargs)]

    warm = full / 'data/fullclosed-mode-damped-warm.npz'
    add('warm', python('reproduce', repo=repo, work=full), bundle=warm,
        report=full / 'rebuild-closed-warm-manifest.json',
        scope='Rebuild actual accepted .99 to .995 prefix, pulse and complete warm; no certificate rerun',
        extra_outputs=(full / 'data/fullclosed-hold-warm.json',
                       full / 'data/pulse-a5-complete-base.json.gz'))
    v1 = geom / 'physical-fit-six-step.json'
    add('af89', python('base', bundle=warm, operator=source['operator'],
        fft_source=source['batch'], quarter=True, angles=2048, low_modes=3,
        steps=6, backtracks=8, damping=.001, seconds=600, out=v1),
        parent=warm, bundle=v1.with_suffix('.npz'), report=v1)

    full_common = dict(repo=repo, operator=source['operator'],
        basis_source=source['base'], coarse_source=source['coarse'],
        helpers=source['helpers'], coordinate_source=source['coordinate'],
        scale_source=source['scale'], angles=2048, stage_block=64,
        low_modes=12, reach_ratio=.03, max_directions=1, maxiter=256,
        lsmr_atol=1.e-6, lsmr_btol=1.e-6, line_trials=15, target=5.e-7)
    e8_dir = full / 'integrated-h2-reach-screen-first'
    add('e8', python('e8_solver', **full_common, bundle=v1.with_suffix('.npz'),
        outdir=e8_dir, implementation=source['batch'],
        coarse_centers=FULL_E8_CENTERS, reach_safety_factor=.98, damping=.005),
        parent=v1.with_suffix('.npz'), bundle=e8_dir / 'final.npz', report=e8_dir / 'report.json')
    add('carrier', python('carrier_generator', repo=repo, bundle=warm,
        node_report=full / 'data/fullclosed-hold-warm.json',
        scalar_input=full / 'data/pulse-a5-complete-base.json.gz',
        outdir=carrier.parent, order=6, angles=2048, stage_block=64, carrier_only=True),
        parent=warm, bundle=carrier, report=carrier.parent / 'report.json',
        scope='New same-scalar Gauss6 carrier; all legacy observations retained')
    seed_outputs = [seed(name) for name in ('legacy_memory', 'restore_grid',
        'restore_local', 'witness_positive', 'witness_lowphi', 'full13_curvature',
        'full13_radius', 'r17_grid', 'r17_local', 'r17_fixed', 'continue_union')]
    add('position_parameters', [], report=seed_dir / 'binding-manifest.json',
        action='materialize_seeds', extra_outputs=seed_outputs,
        scope='Metadata only: ordered historical positions, exact scalar/node checks and explicit current-carrier binding')

    common = dict(qp_source=source['qp'], memory_source=source['memory'],
        observed_source=source['observed'], carrier=carrier,
        operator=source['operator'], batch_source=source['batch'],
        base_source=source['base'], coarse_source=source['coarse'],
        legacy_fraction=.5, memory_curvature=32, memory_radius=4,
        angles=2048, stage_block=64, low_modes=12, centers=R11,
        top_curvature=32, top_radius=4, reach_ratio=.03,
        backtracks=12, seconds=1800)
    g6 = geom / 'curvature-qp-gauss-six-step.json'
    add('2038', python('gauss', **common, bundle=e8_dir / 'final.npz',
        memory_input=seed('legacy_memory'), out=g6, steps=6, damping=.001,
        safety=.98), parent=e8_dir / 'final.npz', bundle=g6.with_suffix('.npz'),
        report=g6, extra_outputs=(g6.with_suffix('.memory.json'),))
    def1_dir = full / 'gauss-h2-projected-first-fixed'
    gauss_full = dict(full_common, implementation=source['observed'],
        base_batch_source=source['batch'], observations=carrier,
        geometry_source=source['qp'], geometry_observed_source=source['gauss'],
        coarse_centers=FULL_GAUSS_CENTERS, legacy_fraction=.5,
        active_band=.025, active_rank_tolerance=1.e-10,
        active_top_curvature=16, active_top_radius=2)
    add('def1', python('def1_solver', **gauss_full, bundle=g6.with_suffix('.npz'),
        outdir=def1_dir, point_source=source['point_observed'],
        active_max_rows=16, reach_safety_factor=.98, damping=.0025),
        parent=g6.with_suffix('.npz'), bundle=def1_dir / 'final.npz', report=def1_dir / 'report.json')
    arbitrary = dict(common, gauss_source=source['gauss'], local_curvature=12,
        local_radius=2, linear_margin=.0002, repair_iterations=40000,
        restoration_attempts=3)
    witnesses = [seed('witness_lowphi'), seed('witness_positive')]
    v4a = geom / 'curvature-qp-arbitrary-def1-six-step.json'
    add('6077', python('v4a', **arbitrary, bundle=def1_dir / 'final.npz',
        memory_input=seed('restore_grid'), local_memory_input=seed('restore_local'),
        witness_input=witnesses, out=v4a, local_refine=4, safety=.98,
        damping=.01, steps=6), parent=def1_dir / 'final.npz',
        bundle=v4a.with_suffix('.npz'), report=v4a,
        extra_outputs=(v4a.with_suffix('.memory.json'), v4a.with_suffix('.local-memory.json')),
        scope='Original v4a six-direction recipe; final old .98 flag may be false, and no reach failure is inferred')
    v4b = geom / 'curvature-qp-protected-992-twelve-step.json'
    first_v4b = v4b.with_suffix('.accepted-1.npz')
    add('v4b_12', python('v4b', **arbitrary, bundle=v4a.with_suffix('.npz'),
        memory_input=v4a.with_suffix('.memory.json'),
        local_memory_input=v4a.with_suffix('.local-memory.json'),
        witness_input=witnesses, protected_point='168,0,.52349044',
        out=v4b, local_refine=4, safety=.992, damping=.04, steps=12),
        parent=v4a.with_suffix('.npz'), bundle=v4b.with_suffix('.npz'), report=v4b,
        extra_outputs=(v4b.with_suffix('.memory.json'), v4b.with_suffix('.local-memory.json'), first_v4b))
    full13 = full / 'gauss-physical-height-memory-first'
    add('13ce', python('full13_solver', **gauss_full, bundle=first_v4b,
        outdir=full13, point_source=source['point_memory'], height_source=source['height'],
        witness_input=seed('full13_curvature'), radius_witness_input=seed('full13_radius'),
        active_max_rows=64, reach_safety_factor=.992, damping=.0025),
        parent=first_v4b, bundle=full13 / 'final.npz', report=full13 / 'report.json',
        scope='Complete-space direction from actual v4b accepted-1, not v4b final; permanent 57/13 position input')

    h2 = dict(arbitrary, centers=R17, norm_source=source['norm'],
        coordinate_source=source['coordinate'], scale_source=source['scale'],
        height_source=source['height'], safety=.992)
    e19 = geom / 'curvature-qp-physical-h2-first.json'
    add('e19', python('v5', **h2, bundle=full13 / 'final.npz',
        memory_input=seed('r17_grid'), local_memory_input=seed('r17_local'),
        fixed_point_input=seed('r17_fixed'),
        protected_point=['227,0,.667566753913', '226,.98,.667566753913'],
        out=e19, damping=.0025, steps=1, local_refine=9),
        parent=full13 / 'final.npz', bundle=e19.with_suffix('.npz'), report=e19,
        extra_outputs=(e19.with_suffix('.memory.json'), e19.with_suffix('.local-memory.json')))
    p0241 = geom / 'curvature-qp-physical-h2-next-six.json'
    add('0241', python('v5', **h2, bundle=e19.with_suffix('.npz'),
        memory_input=e19.with_suffix('.memory.json'),
        local_memory_input=e19.with_suffix('.local-memory.json'),
        fixed_point_input=seed('r17_fixed'), out=p0241,
        damping=.0025, steps=6, local_refine=9),
        parent=e19.with_suffix('.npz'), bundle=p0241.with_suffix('.npz'), report=p0241,
        extra_outputs=(p0241.with_suffix('.memory.json'), p0241.with_suffix('.local-memory.json')))

    def export(name, report, input_manifest, extra_reports=()):
        out = report.with_name(report.stem + '-witnesses.json')
        add('positions_' + name, python('exporter', report=[*extra_reports, report],
            input_manifest=input_manifest, carrier=carrier, bundle=report.with_suffix('.npz'), out=out),
            parent=report.with_suffix('.npz'), report=out,
            scope='Metadata only: retain all actual trial/pinned locations; no geometric values carried forward')
        return out

    manifest = export('0241', p0241, seed('r17_fixed'), extra_reports=(e19,))
    spectral = dict(h2, spectral_source=source['spectral'],
        spectral_p=8, spectral_epsilon=.001, spectral_scale=.05)
    p8 = geom / 'curvature-qp-spectral-p8-six-step.json'
    add('8d', python('v6', **spectral, bundle=p0241.with_suffix('.npz'),
        memory_input=p0241.with_suffix('.memory.json'),
        local_memory_input=p0241.with_suffix('.local-memory.json'),
        fixed_point_input=manifest, out=p8, relative_damping=.001,
        steps=6, local_refine=9), parent=p0241.with_suffix('.npz'),
        bundle=p8.with_suffix('.npz'), report=p8,
        extra_outputs=(p8.with_suffix('.memory.json'), p8.with_suffix('.local-memory.json')),
        scope='New positive spectral p8 objective; Jw remains a separate diagnostic')
    manifest = export('8d', p8, manifest)
    pca = geom / 'curvature-qp-spectral-p8-next-four.json'
    add('ca367', python('v6', **spectral, bundle=p8.with_suffix('.npz'),
        memory_input=p8.with_suffix('.memory.json'), local_memory_input=p8.with_suffix('.local-memory.json'),
        fixed_point_input=manifest, out=pca, damping=.015440957971131026,
        steps=4, local_refine=9, skip_spectral_probe=True),
        parent=p8.with_suffix('.npz'), bundle=pca.with_suffix('.npz'), report=pca,
        extra_outputs=(pca.with_suffix('.memory.json'), pca.with_suffix('.local-memory.json')))
    manifest = export('ca367', pca, manifest)
    exact = dict(spectral, hessian_source=source['hessian'])
    p077 = geom / 'curvature-qp-spectral-hessian-four-step.json'
    add('077', python('v7', **exact, bundle=pca.with_suffix('.npz'),
        memory_input=pca.with_suffix('.memory.json'), local_memory_input=pca.with_suffix('.local-memory.json'),
        fixed_point_input=manifest, out=p077, damping=.015440957971131026,
        steps=4, local_refine=9), parent=pca.with_suffix('.npz'),
        bundle=p077.with_suffix('.npz'), report=p077,
        extra_outputs=(p077.with_suffix('.memory.json'), p077.with_suffix('.local-memory.json')),
        scope='Same true p8 Phi, exact residual E-Hessian and true gradient, physical H2 damping')
    manifest = export('077', p077, manifest)
    exact22 = dict(exact, centers=R22)
    pbede = geom / 'curvature-qp-spectral-hessian-r22-six-step.json'
    add('bede', python('v7', **exact22, bundle=p077.with_suffix('.npz'),
        memory_input=p077.with_suffix('.memory.json'), local_memory_input=p077.with_suffix('.local-memory.json'),
        fixed_point_input=manifest, out=pbede, damping=.0019301197463913783,
        steps=6, local_refine=9), parent=p077.with_suffix('.npz'),
        bundle=pbede.with_suffix('.npz'), report=pbede,
        extra_outputs=(pbede.with_suffix('.memory.json'), pbede.with_suffix('.local-memory.json')),
        scope='2534 coarse columns; historical final false margin is retained, then actual recovery recipe follows')
    manifest = export('bede', pbede, manifest)
    p35 = geom / 'curvature-qp-spectral-hessian-r22-restore-three.json'
    add('35f', python('v7', **exact22, bundle=pbede.with_suffix('.npz'),
        memory_input=pbede.with_suffix('.memory.json'), local_memory_input=pbede.with_suffix('.local-memory.json'),
        fixed_point_input=manifest, out=p35, damping=.004825299365978445,
        protected_point='821,.13182023373669122,.43591193437744524',
        steps=3, local_refine=10, skip_spectral_probe=True),
        parent=pbede.with_suffix('.npz'), bundle=p35.with_suffix('.npz'), report=p35,
        extra_outputs=(p35.with_suffix('.memory.json'), p35.with_suffix('.local-memory.json')))
    manifest = export('35f', p35, manifest)
    pa04 = geom / 'curvature-qp-spectral-hessian-r22-next-six.json'
    add('a04', python('v7', **exact22, bundle=p35.with_suffix('.npz'),
        memory_input=p35.with_suffix('.memory.json'), local_memory_input=p35.with_suffix('.local-memory.json'),
        fixed_point_input=manifest, out=pa04, damping=.012063248414946114,
        protected_point='289,.5290121805813988,.7022676402048246',
        steps=6, local_refine=11, skip_spectral_probe=True),
        parent=p35.with_suffix('.npz'), bundle=pa04.with_suffix('.npz'), report=pa04,
        extra_outputs=(pa04.with_suffix('.memory.json'), pa04.with_suffix('.local-memory.json')))
    manifest = export('a04', pa04, manifest)
    if stop_after == 'continue':
        union = geom / 'curvature-qp-a04-full-union-witnesses.json'
        add('positions_continue_union', python('exporter', report=pa04,
            input_manifest=[manifest, seed('continue_union')], carrier=carrier,
            bundle=pa04.with_suffix('.npz'), out=union),
            parent=pa04.with_suffix('.npz'), report=union,
            scope='Metadata only: union newly generated a04 history and all historical complete-space positions; no old values')
        nxt = geom / 'curvature-qp-spectral-hessian-r22-union-next-four.json'
        add('continue', python('v7', **exact22, bundle=pa04.with_suffix('.npz'),
            memory_input=pa04.with_suffix('.memory.json'),
            local_memory_input=pa04.with_suffix('.local-memory.json'),
            fixed_point_input=union, out=nxt, damping='@ACTUAL_A04_FINAL_DAMPING',
            protected_point=['821,.557082202638,.01647875344',
                '113,.17836061753131477,.11275230115214022'],
            steps=4, local_refine=21, skip_spectral_probe=True),
            parent=pa04.with_suffix('.npz'), bundle=nxt.with_suffix('.npz'), report=nxt,
            extra_outputs=(nxt.with_suffix('.memory.json'), nxt.with_suffix('.local-memory.json')),
            scope='New continuation, four directions maximum; actual new a04 damping, all historical/new position rereads')
        export('continue', nxt, union)
    return stages, source


def materialize_seeds(repo, work, seed_file):
    """Only JSON/identity processing: no field evaluation or scientific import."""
    d = json.loads(seed_file.read_text())
    node_path = work / 'fullclosed_solver/data/fullclosed-hold-warm.json'
    scalar_path = work / 'fullclosed_solver/data/pulse-a5-complete-base.json.gz'
    carrier = work / 'recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz'
    n = json.loads(node_path.read_text())
    raw = json.loads(gzip.decompress(scalar_path.read_bytes()))
    scalar = scalar_definition(raw)
    topo = d['topology']
    if (n['J'] != topo['nodes'] or n['M'] != topo['M'] or
            canonical_sha(n['true_scalar_nodes']) != topo['symbolic_node_definitions_sha256'] or
            canonical_sha(scalar) != topo['scalar_definition_sha256']):
        raise ValueError('Historical indexed locations require the exact same symbolic mesh and scalar definition. '
                         'The fresh reconstruction differs; do not reinterpret old indices or inherit a certificate.')
    carrier_sha = sha(carrier)
    records = []
    folder = work / 'historical-position-parameters'
    for name, record in d['seeds'].items():
        value = copy.deepcopy(record['payload'])
        changes = {}
        for key in ('carrier_sha256', 'observation_carrier_sha256'):
            if key in value:
                changes[key] = dict(historical=value[key], actual=carrier_sha)
                value[key] = carrier_sha
        value['historical_location_source'] = {k: record[k] for k in record if k != 'payload'}
        value['explicit_carrier_rebinding'] = changes
        value['geometric_values_inherited'] = False
        path = folder / (name + '.json')
        write_json(path, value)
        records.append(dict(name=name, path=str(path), sha256=sha(path),
                            original_source_sha256=record['historical_source_sha256']))
    binding = dict(schema='historical-location-carrier-binding-v1',
        seed_file_sha256=sha(seed_file), actual_carrier_sha256=carrier_sha,
        historical_carrier_sha256=d['historical_carrier_sha256'],
        actual_node_report_sha256=sha(node_path), actual_scalar_input_sha256=sha(scalar_path),
        exact_symbolic_nodes_and_scalar_definitions_match=True, outputs=records,
        scope='Only positions and original ordering/capacities; all values, signs and derivatives are recomputed by the solver. No certificate inherited.')
    write_json(folder / 'binding-manifest.json', binding)


def scalar_summary(report):
    if report is None or not Path(report).exists():
        return {}
    d = json.loads(Path(report).read_text())
    state = d.get('final', d.get('current', d.get('native_final', {})))
    result = {}
    for out, keys in {
        'Phi': ('phi_normalized',),
        'max_gram': ('max_gram', 'max_relative_gram', 'sampled_max_gram'),
        'weighted_sse': ('original_weighted_sse', 'weighted_sse', 'radial_weighted_frobenius_sse'),
        'raw_sse': ('raw_sse', 'raw_frobenius_sse'),
    }.items():
        for key in keys:
            if key in state and isinstance(state[key], (int, float)):
                result[out] = state[key]
                break
    geometry = d.get('final_arbitrary_geometry', d.get('final_curvature_filter', d.get('final_geometry', {})))
    if 'necessary_reach_product' in geometry:
        result['product'] = geometry['necessary_reach_product']
    for key in ('final_known_point_safety_pass', 'final_damping', 'status'):
        if key in d:
            result[key] = d[key]
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--work', type=Path, required=True)
    p.add_argument('--stop-after', choices=('a04', 'continue'), default='a04')
    p.add_argument('--seed-data', type=Path, default=Path(__file__).with_name('a04_historical_location_seeds.json'))
    p.add_argument('--print-only', action='store_true')
    a = p.parse_args()
    a.repo, a.work, a.seed_data = a.repo.resolve(), a.work.resolve(), a.seed_data.resolve()
    stages, sources = make_plan(a.repo, a.work, a.stop_after)
    identities = {}
    for role, path in sources.items():
        if not path.is_file():
            raise FileNotFoundError('Complete published source required: ' + str(path))
        digest = sha(path)
        if role in SOURCE_SHA and digest != SOURCE_SHA[role]:
            raise ValueError('Frozen executed source changed: ' + role + ' actual=' + digest)
        identities[role] = dict(path=str(path), sha256=digest)
    if not a.seed_data.is_file():
        raise FileNotFoundError(a.seed_data)
    plan = dict(schema='public-actions-a04-command-chain-v1',
        source_sha256=sha(__file__), seed_data_sha256=sha(a.seed_data),
        repository=REPOSITORY, repo=str(a.repo), work=str(a.work),
        stop_after=a.stop_after, sources=identities, stages=stages,
        numerical_environment=dict(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1'),
        historical_names_are_labels_only=True, old_certificates_inherited=False,
        historical_main_chain_recorded_seconds_approximately=3735,
        runtime_scope='Measured old scientific main-chain time about 62.3 minutes plus carrier/materialization. Different hardware and nonlinear paths can take longer; no six-hour guarantee.')
    if a.print_only:
        for stage in stages:
            print(json.dumps(dict(stage=stage['name'], scope=stage['scope'],
                command=shlex.join(stage['argv']) if stage['argv'] else stage['action'],
                parent=stage['parent'], bundle=stage['bundle'], report=stage['report'])), flush=True)
        print(json.dumps(dict(event='plan_only_complete', stages=len(stages),
            source_sha256=plan['source_sha256'], seed_data_sha256=plan['seed_data_sha256'],
            scientific_subprocesses_started=0)), flush=True)
        return
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true' or
            os.environ.get('GITHUB_REPOSITORY', '').lower() != REPOSITORY.lower()):
        raise RuntimeError('Scientific stages are restricted to this public repository\'s GitHub Actions. '
                           'Use --print-only for local text review.')
    if a.work == a.repo or a.repo in a.work.parents:
        raise ValueError('Raw work directory must be outside the Git repository')
    subprocess.run(['git', 'cat-file', '-e', OLD_BLOB], cwd=a.repo, check=True)
    a.work.mkdir(parents=True, exist_ok=True)
    log_dir = a.work / 'recipe-logs'
    log_dir.mkdir(exist_ok=True)
    (a.work / 'geometry_path').mkdir(exist_ok=True)
    status_path = a.work / 'status.json'
    identity = dict(source_sha256=plan['source_sha256'], seed_data_sha256=plan['seed_data_sha256'],
                    sources_sha256={k: v['sha256'] for k, v in identities.items()})
    if status_path.exists():
        status = json.loads(status_path.read_text())
        if status.get('identity') != identity:
            raise ValueError('Cannot silently resume a work directory using different source/seed bytes')
    else:
        status = dict(schema='public-actions-a04-status-v1', identity=identity,
            stage='initializing', state='running', completed=[],
            run_url='https://github.com/' + REPOSITORY + '/actions/runs/' + os.environ.get('GITHUB_RUN_ID', ''),
            scientific_scope='Fresh actual numerical outputs only. No continuous metric, embedding, reach or held certificate is inherited.')
    write_json(a.work / 'recipe-manifest.json', plan)
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    try:
        for stage in stages:
            name = stage['name']
            old = next((x for x in status['completed'] if x['name'] == name), None)
            if old:
                for item in old['outputs']:
                    if not Path(item['path']).is_file() or sha(item['path']) != item['sha256']:
                        raise ValueError('Previously completed current-run output changed: ' + item['path'])
                if stage['parent'] and sha(stage['parent']) != old.get('parent_sha256'):
                    raise ValueError('Previously completed current-run parent changed: ' + name)
                print(json.dumps(dict(stage=name, state='completed', reused_same_run=True,
                                      output_sha256=old.get('output_bundle_sha256'))), flush=True)
                continue
            for path in filter(None, [stage['bundle'], stage['report']]):
                if Path(path).exists() and name != 'warm':
                    raise FileExistsError('Unjournaled old output needs inspection, not overwrite: ' + path)
            parent_sha = sha(stage['parent']) if stage['parent'] else None
            argv = stage['argv'][:]
            if '@ACTUAL_A04_FINAL_DAMPING' in argv:
                current = json.loads((a.work / 'geometry_path/curvature-qp-spectral-hessian-r22-next-six.json').read_text())
                if not current.get('final_known_point_safety_pass', False):
                    raise ValueError('Fresh a04 recipe endpoint is not currently qualified for optional continuation')
                argv[argv.index('@ACTUAL_A04_FINAL_DAMPING')] = str(current['final_damping'])
            status.update(stage=name, state='running', current_command=argv,
                current_scope=stage['scope'], parent_sha256=parent_sha,
                updated_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
            write_json(status_path, status)
            print(json.dumps(dict(stage=name, state='running', parent_sha256=parent_sha)), flush=True)
            started = time.monotonic()
            log_path = log_dir / (name + '.log')
            if stage['action'] == 'materialize_seeds':
                materialize_seeds(a.repo, a.work, a.seed_data)
                rc = 0
                log_path.write_text('Metadata-only historical position binding completed.\n')
            else:
                with log_path.open('w') as log:
                    proc = subprocess.run(argv, cwd=a.repo, env=env, stdout=log, stderr=subprocess.STDOUT)
                rc = proc.returncode
            elapsed = time.monotonic() - started
            paths = list(dict.fromkeys(filter(None, [stage['bundle'], stage['report'], *stage['extra_outputs']])))
            outputs = [dict(path=path, sha256=sha(path), bytes=Path(path).stat().st_size)
                       for path in paths if Path(path).is_file()]
            record = dict(name=name, seconds=elapsed, returncode=rc, scope=stage['scope'],
                parent=stage['parent'], parent_sha256=parent_sha,
                output_bundle=stage['bundle'], output_bundle_sha256=sha(stage['bundle']) if stage['bundle'] and Path(stage['bundle']).exists() else None,
                report=stage['report'], report_sha256=sha(stage['report']) if stage['report'] and Path(stage['report']).exists() else None,
                log=str(log_path), outputs=outputs, **scalar_summary(stage['report']))
            if stage['historical_bundle_sha256']:
                record['historical_bundle_sha256'] = stage['historical_bundle_sha256']
                record['historical_bytes_match'] = record['output_bundle_sha256'] == stage['historical_bundle_sha256']
            if rc or len(outputs) != len(paths):
                status.update(stage=name, state='failed', failed=record)
                write_json(status_path, status)
                print(json.dumps(dict(stage=name, state='failed', **record)), flush=True)
                raise RuntimeError('Stage did not produce all declared actual outputs: ' + name)
            status['completed'].append(record)
            status.update(stage=name, state='completed')
            write_json(status_path, status)
            print(json.dumps({k: v for k, v in dict(stage=name, state='completed', **record).items()
                              if k not in ('outputs', 'log')}), flush=True)
        status.update(stage=a.stop_after, state='completed', recipe_finished=True)
        write_json(status_path, status)
        print(json.dumps(dict(event='recipe_finished', stage=a.stop_after,
            status=str(status_path), historical_names_are_labels_only=True,
            inherited_scientific_certificates=False)), flush=True)
    except BaseException as error:
        status.update(state='failed', error=repr(error))
        write_json(status_path, status)
        raise


if __name__ == '__main__':
    main()
