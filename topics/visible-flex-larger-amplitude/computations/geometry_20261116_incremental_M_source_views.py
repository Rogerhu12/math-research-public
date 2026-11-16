#!/usr/bin/env python3
"""R464 explicit source views for the genuine R463 incremental-M field.

This program only reads, replaces, hashes and writes public source text.
Each original complete source, every literal replacement/count and the full
new source identity is frozen below. It never imports/evaluates a project
module, compiles, runs a fixture, reads a scientific field or rewrites a
result schema. Old source files are read-only; fresh names are created in
the real computations directory used by the R463 driver and all loaders.

These are different public source identities, not byte-equivalent old
sources. The expanded files can be reconstructed from this complete table.
All mathematical consumers keep their independent actual execution duties.
Author: amplitude agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import sys

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R464-incremental-M-explicit-source-views-v1"
HERE=Path(__file__).resolve().parent
LIMIT=90000
PINS={'geometry_20261116_continuous_ten_M_prefix_metric.py': '56a3a9fed5b52130199e0fd6d6d6d72d6d12a82fbbf9c248e77608e8bfd056be',
 'geometry_20261116_continuous_ten_frozen_M_saved_prefix.py': '86a88a66a57c05b64c21efa650374746ad42be272f0d741188ff81bdf4fed2f6',
 'geometry_20261116_continuous_ten_incremental_M_checkpoint.py': '7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39',
 'geometry_20261116_continuous_ten_incremental_M_refinement.py': 'cf86639189e98e7fe5c99f6dfba566fac6dbfd3b142c17ea8b22df6bb039ce28',
 'geometry_20261116_current_C_M_accurate_cut_patch.py': '747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492',
 'geometry_20261116_current_C_M_complete_block_reach_cover.py': '1915bc51508f2a2f8028594a8808fdeb902ea88782a161d94dae14da6b41340e',
 'geometry_20261116_current_C_M_complete_reach_cover.py': 'e69cf21c3800c8ca8b145ac0ea89233ed59571a6c51ca02a7078211b2d254210',
 'geometry_20261116_current_C_M_fixed_cap_balls.py': '21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a',
 'geometry_20261116_current_C_M_held_and_rigidity_inputs.py': '9c5615bbf8f0c895d75b84d7aed0f4297a10c3b0b624336d93bb37b150715c51',
 'geometry_20261116_current_C_M_live_query_complete_metric.py': 'fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47',
 'geometry_20261116_current_C_M_original_cuff_atlas.py': '97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621',
 'geometry_20261116_current_C_complete_multitime_display.py': 'f3211ba9d74cf2be99d47fe56fcbd5526e8143f8a114364ffdc725382c286bf3',
 'geometry_20261116_current_C_incremental_M_common_material_phase.py': '50bf2d04e5e4e505fad6f0ece5a896364bb94c25c9530d6a1e7c2ceef3aec923',
 'geometry_20261116_current_C_incremental_M_owned_launch.py': 'f372081797276ed3bc6c061f91febd97dfad70b742c34d10a9df5ae642a04078',
 'geometry_20261116_current_C_ten_M_radial_readout.mjs': '109507cd981bbff9f0d5e18e2c498ec512876e017fe6f72096876e1b7e9e2853',
 'geometry_20261116_current_C_ten_M_shared_field.py': 'db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87',
 'geometry_20261116_fixed_target_complete_metric_evidence.py': '494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05',
 'root_20261116_continuous_ten_M_phase_readout.py': '31891fe66be3e707173631dd000f625715f34f57110f865797c0a4ecaf22ed56',
 'root_20261116_current_C_M_native_necessary_api.py': '22923f449d363543169446eb970c78f0aaa7410648df4ebc02cd7fd6fafc96c1'}
VIEWS=[{'role': 'saved',
  'schema': 'R464-continuous-ten-incremental-M-complete-saved-prefix-v1',
  'baseline': {'file': 'geometry_20261116_continuous_ten_frozen_M_saved_prefix.py',
               'bytes': 19242,
               'sha256': '86a88a66a57c05b64c21efa650374746ad42be272f0d741188ff81bdf4fed2f6'},
  'generated': {'file': 'geometry_20261116_continuous_ten_incremental_M_saved_prefix.py',
                'bytes': 19270,
                'sha256': '959b1a2b54fd0da8be14c2228d91ca1d1ef312966d6f4ba40be4bbeff4247ce9'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_frozen_M_checkpoint.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_checkpoint.py',
                    'count': 1},
                   {'old': '18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93',
                    'new': '7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39',
                    'count': 1},
                   {'old': 'R442-continuous-ten-frozen-M-complete-saved-prefix-v1',
                    'new': 'R464-continuous-ten-incremental-M-complete-saved-prefix-v1',
                    'count': 1},
                   {'old': 'R442 full-state SavedPrefix',
                    'new': 'R464 source-registered full-state SavedPrefix',
                    'count': 1}]},
 {'role': 'radial',
  'schema': 'R464-current-C-incremental-M-complete-radial-Cartesian-readout-v1',
  'baseline': {'file': 'geometry_20261116_current_C_ten_M_radial_readout.mjs',
               'bytes': 24108,
               'sha256': '109507cd981bbff9f0d5e18e2c498ec512876e017fe6f72096876e1b7e9e2853'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_radial_readout.mjs',
                'bytes': 24141,
                'sha256': '513494eb4569905d45e02326e388fec65e2e42b211ce8e30de31522618295bb9'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_frozen_M_checkpoint.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_checkpoint.py',
                    'count': 1},
                   {'old': '18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93',
                    'new': '7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39',
                    'count': 1},
                   {'old': 'R442-current-C-frozen-M-complete-radial-Cartesian-readout-v1',
                    'new': 'R464-current-C-incremental-M-complete-radial-Cartesian-readout-v1',
                    'count': 1},
                   {'old': 'R442-current-continuous-ten-frozen-M-physical-DN-checkpoint-v1',
                    'new': 'R463-current-continuous-ten-incremental-M-physical-DN-checkpoint-v1',
                    'count': 1},
                   {'old': '// R442 complete-M radial readout',
                    'new': '// R464 source-registered complete-M radial readout',
                    'count': 1}]},
 {'role': 'shared',
  'schema': 'R464-current-C-incremental-M-shared-background-complete-field-v1',
  'baseline': {'file': 'geometry_20261116_current_C_ten_M_shared_field.py',
               'bytes': 49452,
               'sha256': 'db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_shared_field.py',
                'bytes': 49511,
                'sha256': '55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_frozen_M_saved_prefix.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_saved_prefix.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_ten_M_radial_readout.mjs',
                    'new': 'geometry_20261116_current_C_incremental_M_radial_readout.mjs',
                    'count': 1},
                   {'old': '86a88a66a57c05b64c21efa650374746ad42be272f0d741188ff81bdf4fed2f6',
                    'new': '959b1a2b54fd0da8be14c2228d91ca1d1ef312966d6f4ba40be4bbeff4247ce9',
                    'count': 1},
                   {'old': '109507cd981bbff9f0d5e18e2c498ec512876e017fe6f72096876e1b7e9e2853',
                    'new': '513494eb4569905d45e02326e388fec65e2e42b211ce8e30de31522618295bb9',
                    'count': 1},
                   {'old': 'R442-current-C-frozen-M-complete-radial-Cartesian-readout-v1',
                    'new': 'R464-current-C-incremental-M-complete-radial-Cartesian-readout-v1',
                    'count': 1},
                   {'old': 'R442-current-C-frozen-M-shared-background-complete-field-v1',
                    'new': 'R464-current-C-incremental-M-shared-background-complete-field-v1',
                    'count': 1},
                   {'old': 'R442-current-C-frozen-M-shared-field-plan-input-v1',
                    'new': 'R464-current-C-incremental-M-shared-field-plan-input-v1',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_ten_M_shared_field.load_',
                    'new': 'geometry_20261116_current_C_incremental_M_shared_field.load_',
                    'count': 1},
                   {'old': 'R442 current-C complete-M radial Hermite',
                    'new': 'R464 source-registered current-C complete-M radial Hermite',
                    'count': 1},
                   {'old': 'a genuine R442 complete frozen-M checkpoint',
                    'new': 'a genuine R463 complete incremental-M checkpoint',
                    'count': 1}]},
 {'role': 'prefix',
  'schema': 'R464-current-C-incremental-M-frozen-prefix-relative-metric-v1',
  'baseline': {'file': 'geometry_20261116_continuous_ten_M_prefix_metric.py',
               'bytes': 32797,
               'sha256': '56a3a9fed5b52130199e0fd6d6d6d72d6d12a82fbbf9c248e77608e8bfd056be'},
  'generated': {'file': 'geometry_20261116_continuous_ten_incremental_M_prefix_metric.py',
                'bytes': 32810,
                'sha256': 'fd74b6ad9dc1b6069b016dd7fce14e0c35215bc76b045682172e3e10522a7402'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_frozen_M_saved_prefix.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_saved_prefix.py',
                    'count': 2},
                   {'old': '86a88a66a57c05b64c21efa650374746ad42be272f0d741188ff81bdf4fed2f6',
                    'new': '959b1a2b54fd0da8be14c2228d91ca1d1ef312966d6f4ba40be4bbeff4247ce9',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-frozen-prefix-relative-metric-v1',
                    'new': 'R464-current-C-incremental-M-frozen-prefix-relative-metric-v1',
                    'count': 1}]},
 {'role': 'atlas',
  'schema': 'R464-current-C-incremental-M-original-cuff-target-atlas-binding-v1',
  'baseline': {'file': 'geometry_20261116_current_C_M_original_cuff_atlas.py',
               'bytes': 29387,
               'sha256': '97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_original_cuff_atlas.py',
                'bytes': 29440,
                'sha256': '14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_frozen_M_checkpoint.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_checkpoint.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_ten_M_shared_field.py',
                    'new': 'geometry_20261116_current_C_incremental_M_shared_field.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_ten_M_shared_field.load_',
                    'new': 'geometry_20261116_current_C_incremental_M_shared_field.load_',
                    'count': 1},
                   {'old': '18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93',
                    'new': '7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39',
                    'count': 1},
                   {'old': 'db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87',
                    'new': '55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04',
                    'count': 1},
                   {'old': 'R442-current-C-frozen-M-shared-background-complete-field-v1',
                    'new': 'R464-current-C-incremental-M-shared-background-complete-field-v1',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-original-cuff-target-atlas-binding-v1',
                    'new': 'R464-current-C-incremental-M-original-cuff-target-atlas-binding-v1',
                    'count': 1},
                   {'old': 'R442-current-C-frozen-M-shared-field-plan-input-v1',
                    'new': 'R464-current-C-incremental-M-shared-field-plan-input-v1',
                    'count': 1},
                   {'old': 'R442-current-continuous-ten-frozen-M-physical-DN-checkpoint-v1',
                    'new': 'R463-current-continuous-ten-incremental-M-physical-DN-checkpoint-v1',
                    'count': 1},
                   {'old': 'R451 original model-C cuff binding for the complete actual R442 M-field.',
                    'new': 'R464 original model-C cuff binding for the complete actual R463 M-field.',
                    'count': 1},
                   {'old': 'actual R442 checkpoint metadata',
                    'new': 'actual R463 checkpoint metadata',
                    'count': 1},
                   {'old': 'original complete-M R442 loaders',
                    'new': 'source-registered complete-M R463 loaders',
                    'count': 1},
                   {'old': 'actual_frozen_M_arrays_and_all_original_acceptance_remain_R442_loader',
                    'new': 'actual_incremental_M_arrays_and_all_original_acceptance_remain_R463_loader',
                    'count': 1}]},
 {'role': 'cut',
  'schema': 'R464-current-C-incremental-M-accurate-cut-atlas-field-v1',
  'baseline': {'file': 'geometry_20261116_current_C_M_accurate_cut_patch.py',
               'bytes': 26078,
               'sha256': '747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_accurate_cut_patch.py',
                'bytes': 26131,
                'sha256': '8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2'},
  'replacements': [{'old': 'geometry_20261116_current_C_ten_M_shared_field.py',
                    'new': 'geometry_20261116_current_C_incremental_M_shared_field.py',
                    'count': 1},
                   {'old': 'geometry_20261116_continuous_ten_M_prefix_metric.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_prefix_metric.py',
                    'count': 1},
                   {'old': 'db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87',
                    'new': '55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04',
                    'count': 1},
                   {'old': '56a3a9fed5b52130199e0fd6d6d6d72d6d12a82fbbf9c248e77608e8bfd056be',
                    'new': 'fd74b6ad9dc1b6069b016dd7fce14e0c35215bc76b045682172e3e10522a7402',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-accurate-cut-atlas-field-v1',
                    'new': 'R464-current-C-incremental-M-accurate-cut-atlas-field-v1',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_accurate_cut_patch.load_',
                    'new': 'geometry_20261116_current_C_incremental_M_accurate_cut_patch.load_',
                    'count': 1},
                   {'old': 'R451 complete-M accurate-C cut atlas',
                    'new': 'R464 source-registered complete-M accurate-C cut atlas',
                    'count': 1},
                   {'old': 'R442 input and acceptance responsibilities',
                    'new': 'R463 input and acceptance responsibilities',
                    'count': 1}]},
 {'role': 'caps',
  'schema': 'R464-current-C-incremental-M-fixed-cap-rational-six-jets-and-balls-v1',
  'baseline': {'file': 'geometry_20261116_current_C_M_fixed_cap_balls.py',
               'bytes': 23637,
               'sha256': '21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_fixed_cap_balls.py',
                'bytes': 23668,
                'sha256': '3f43b4bf5e3d4e3134904a772abbf36483e1470174a1df9a3657edf03fbfe811'},
  'replacements': [{'old': 'geometry_20261116_current_C_ten_M_shared_field.py',
                    'new': 'geometry_20261116_current_C_incremental_M_shared_field.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_original_cuff_atlas.py',
                    'new': 'geometry_20261116_current_C_incremental_M_original_cuff_atlas.py',
                    'count': 1},
                   {'old': 'db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87',
                    'new': '55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04',
                    'count': 1},
                   {'old': '97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621',
                    'new': '14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5',
                    'count': 1},
                   {'old': 'R442-current-C-frozen-M-shared-background-complete-field-v1',
                    'new': 'R464-current-C-incremental-M-shared-background-complete-field-v1',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-original-cuff-target-atlas-binding-v1',
                    'new': 'R464-current-C-incremental-M-original-cuff-target-atlas-binding-v1',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-fixed-cap-rational-six-jets-and-balls-v1',
                    'new': 'R464-current-C-incremental-M-fixed-cap-rational-six-jets-and-balls-v1',
                    'count': 1}]},
 {'role': 'metric',
  'schema': 'R464-current-C-incremental-M-relative-metric-live-queries-v1',
  'baseline': {'file': 'geometry_20261116_current_C_M_live_query_complete_metric.py',
               'bytes': 55048,
               'sha256': 'fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_live_query_complete_metric.py',
                'bytes': 55099,
                'sha256': '2592d09e9dc471679d4e6d8588a409c3a180132b3b478fc47fbeb1a9d91886f8'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_M_prefix_metric.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_prefix_metric.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_original_cuff_atlas.py',
                    'new': 'geometry_20261116_current_C_incremental_M_original_cuff_atlas.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_accurate_cut_patch.py',
                    'new': 'geometry_20261116_current_C_incremental_M_accurate_cut_patch.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_fixed_cap_balls.py',
                    'new': 'geometry_20261116_current_C_incremental_M_fixed_cap_balls.py',
                    'count': 1},
                   {'old': '56a3a9fed5b52130199e0fd6d6d6d72d6d12a82fbbf9c248e77608e8bfd056be',
                    'new': 'fd74b6ad9dc1b6069b016dd7fce14e0c35215bc76b045682172e3e10522a7402',
                    'count': 1},
                   {'old': '97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621',
                    'new': '14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5',
                    'count': 1},
                   {'old': '747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492',
                    'new': '8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2',
                    'count': 1},
                   {'old': '21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a',
                    'new': '3f43b4bf5e3d4e3134904a772abbf36483e1470174a1df9a3657edf03fbfe811',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-relative-metric-live-queries-v1',
                    'new': 'R464-current-C-incremental-M-relative-metric-live-queries-v1',
                    'count': 1}]},
 {'role': 'reach',
  'schema': 'R464-current-C-incremental-M-closed-reach-cover-v1',
  'baseline': {'file': 'geometry_20261116_current_C_M_complete_reach_cover.py',
               'bytes': 60459,
               'sha256': 'e69cf21c3800c8ca8b145ac0ea89233ed59571a6c51ca02a7078211b2d254210'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_complete_reach_cover.py',
                'bytes': 60498,
                'sha256': '710719dca6ff474c3c73f378b9bba04fad3c5621c86487147d4fe715a47f6f61'},
  'replacements': [{'old': 'geometry_20261116_current_C_M_original_cuff_atlas.py',
                    'new': 'geometry_20261116_current_C_incremental_M_original_cuff_atlas.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_accurate_cut_patch.py',
                    'new': 'geometry_20261116_current_C_incremental_M_accurate_cut_patch.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_fixed_cap_balls.py',
                    'new': 'geometry_20261116_current_C_incremental_M_fixed_cap_balls.py',
                    'count': 1},
                   {'old': '97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621',
                    'new': '14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5',
                    'count': 1},
                   {'old': '747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492',
                    'new': '8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2',
                    'count': 1},
                   {'old': '21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a',
                    'new': '3f43b4bf5e3d4e3134904a772abbf36483e1470174a1df9a3657edf03fbfe811',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-closed-reach-cover-v1',
                    'new': 'R464-current-C-incremental-M-closed-reach-cover-v1',
                    'count': 1}]},
 {'role': 'block',
  'schema': 'R464-current-C-incremental-M-hierarchical-root-pair-reach-v1',
  'baseline': {'file': 'geometry_20261116_current_C_M_complete_block_reach_cover.py',
               'bytes': 45618,
               'sha256': '1915bc51508f2a2f8028594a8808fdeb902ea88782a161d94dae14da6b41340e'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_complete_block_reach_cover.py',
                'bytes': 45633,
                'sha256': 'afa18a5d303806e1a644186ce326644110f0e6a262b878d988b07b5712606ebe'},
  'replacements': [{'old': 'geometry_20261116_current_C_M_complete_reach_cover.py',
                    'new': 'geometry_20261116_current_C_incremental_M_complete_reach_cover.py',
                    'count': 1},
                   {'old': 'e69cf21c3800c8ca8b145ac0ea89233ed59571a6c51ca02a7078211b2d254210',
                    'new': '710719dca6ff474c3c73f378b9bba04fad3c5621c86487147d4fe715a47f6f61',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-hierarchical-root-pair-reach-v1',
                    'new': 'R464-current-C-incremental-M-hierarchical-root-pair-reach-v1',
                    'count': 1}]},
 {'role': 'heldconsumer',
  'schema': 'R464-current-C-incremental-M-whole-image-held-and-planar-germ-inputs-v1',
  'baseline': {'file': 'geometry_20261116_current_C_M_held_and_rigidity_inputs.py',
               'bytes': 53783,
               'sha256': '9c5615bbf8f0c895d75b84d7aed0f4297a10c3b0b624336d93bb37b150715c51'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_held_and_rigidity_inputs.py',
                'bytes': 53822,
                'sha256': '6d3e56b2f8ab636d03d829c7d9bd244cfd7bbf1db0e4cdda6c9329b064440cba'},
  'replacements': [{'old': 'geometry_20261116_current_C_M_original_cuff_atlas.py',
                    'new': 'geometry_20261116_current_C_incremental_M_original_cuff_atlas.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_accurate_cut_patch.py',
                    'new': 'geometry_20261116_current_C_incremental_M_accurate_cut_patch.py',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_M_fixed_cap_balls.py',
                    'new': 'geometry_20261116_current_C_incremental_M_fixed_cap_balls.py',
                    'count': 1},
                   {'old': '97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621',
                    'new': '14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5',
                    'count': 1},
                   {'old': '747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492',
                    'new': '8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2',
                    'count': 1},
                   {'old': '21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a',
                    'new': '3f43b4bf5e3d4e3134904a772abbf36483e1470174a1df9a3657edf03fbfe811',
                    'count': 1},
                   {'old': 'R451-current-C-complete-M-whole-image-held-and-planar-germ-inputs-v1',
                    'new': 'R464-current-C-incremental-M-whole-image-held-and-planar-germ-inputs-v1',
                    'count': 1}]},
 {'role': 'nativeapi',
  'schema': 'R464-current-C-incremental-M-native-necessary-api-v1',
  'baseline': {'file': 'root_20261116_current_C_M_native_necessary_api.py',
               'bytes': 51497,
               'sha256': '22923f449d363543169446eb970c78f0aaa7410648df4ebc02cd7fd6fafc96c1'},
  'generated': {'file': 'root_20261116_current_C_incremental_M_native_necessary_api.py',
                'bytes': 52328,
                'sha256': '4f1c2861a63ba50b6cc6bf3eed4ab2cc1b5fc0a3b7c7de6197b00fd0a810fdf4'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_frozen_M_refinement.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_refinement.py',
                    'count': 1},
                   {'old': '395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12',
                    'new': 'cf86639189e98e7fe5c99f6dfba566fac6dbfd3b142c17ea8b22df6bb039ce28',
                    'count': 1},
                   {'old': 'R442-current-C-complete-M-native-necessary-api-v1',
                    'new': 'R464-current-C-incremental-M-native-necessary-api-v1',
                    'count': 1},
                   {'old': 'R442 metadata-only complete-M sampler/native necessary selection API.',
                    'new': 'R464 metadata-only native selection API for the real incremental-M owner.',
                    'count': 1},
                   {'old': 'by the one bounded R442 owner reader after actual process quiescence.',
                    'new': 'by the bounded R464 owner reader after actual process quiescence.\n'
                           'The inherited sampler_view remains a legacy full-M reader; the R464 caller\n'
                           'uses the actual R462 readback for union records and never passes them to it.',
                    'count': 1},
                   {'old': 'RAW_KEYS={',
                    'new': "SOURCE_PINS.update({'geometry_20261116_continuous_ten_incremental_M_checkpoint.py': "
                           "'7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39',\n"
                           " 'geometry_20261116_current_C_incremental_M_far_union.py': "
                           "'5da13c5f94c59be9f002f906a373d5320ed64d0ac0254af1746a1e5c8ce13c46',\n"
                           " 'geometry_20261116_current_C_incremental_M_native_worker.mjs': "
                           "'b536850a32fb8c26f7bc7a06483a4d3823662ea2fd2a9235e77dbdca069b6b08',\n"
                           " 'geometry_20261116_current_C_incremental_M_owned_launch.py': "
                           "'f372081797276ed3bc6c061f91febd97dfad70b742c34d10a9df5ae642a04078',\n"
                           " 'geometry_20261116_current_C_incremental_M_tail_client.py': "
                           "'d9db5098b8dbf8ebabb83fb25c060faaa0acf28dd9075654b550bdf07ac5a710'})\n"
                           'RAW_KEYS={',
                    'count': 1}]},
 {'role': 'phaseapi',
  'schema': 'R464-continuous-ten-incremental-M-phase-necessary-api-v1',
  'baseline': {'file': 'root_20261116_continuous_ten_M_phase_readout.py',
               'bytes': 19411,
               'sha256': '31891fe66be3e707173631dd000f625715f34f57110f865797c0a4ecaf22ed56'},
  'generated': {'file': 'root_20261116_continuous_ten_incremental_M_phase_readout.py',
                'bytes': 19706,
                'sha256': 'dfda82d609716948994fae95089e8915027a1b0bb1ea59eb1290c213ec9480e6'},
  'replacements': [{'old': 'geometry_20261116_continuous_ten_frozen_M_refinement.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_refinement.py',
                    'count': 1},
                   {'old': 'geometry_20261116_continuous_ten_frozen_M_checkpoint.py',
                    'new': 'geometry_20261116_continuous_ten_incremental_M_checkpoint.py',
                    'count': 1},
                   {'old': 'root_20261116_current_C_M_native_necessary_api.py',
                    'new': 'root_20261116_current_C_incremental_M_native_necessary_api.py',
                    'count': 2},
                   {'old': '395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12',
                    'new': 'cf86639189e98e7fe5c99f6dfba566fac6dbfd3b142c17ea8b22df6bb039ce28',
                    'count': 1},
                   {'old': '18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93',
                    'new': '7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39',
                    'count': 1},
                   {'old': '22923f449d363543169446eb970c78f0aaa7410648df4ebc02cd7fd6fafc96c1',
                    'new': '4f1c2861a63ba50b6cc6bf3eed4ab2cc1b5fc0a3b7c7de6197b00fd0a810fdf4',
                    'count': 2},
                   {'old': 'R442-continuous-ten-complete-M-phase-necessary-api-v1',
                    'new': 'R464-continuous-ten-incremental-M-phase-necessary-api-v1',
                    'count': 1},
                   {'old': 'R442-current-continuous-ten-frozen-M-physical-DN-checkpoint-v1',
                    'new': 'R463-current-continuous-ten-incremental-M-physical-DN-checkpoint-v1',
                    'count': 1},
                   {'old': 'R442-current-C-continuous-ten-frozen-M-original-full-DN-v1',
                    'new': 'R463-current-C-continuous-ten-incremental-M-original-full-DN-v1',
                    'count': 1},
                   {'old': 'R442 metadata-only complete-M phase',
                    'new': 'R464 metadata-only incremental-M phase',
                    'count': 1},
                   {'old': 'Actual R442 complete-M checkpoint schema differs',
                    'new': 'Actual R463 incremental-M checkpoint schema differs',
                    'count': 1},
                   {'old': 'native=doc.get("original_native_binding") or {}',
                    'new': 'native=doc.get("original_native_binding") or {}\n'
                           '    union=native.get("complete_far_union_binding")\n'
                           '    if union is not None:\n'
                           '        '
                           'chosen["actual_complete_far_union_source_scope"]=selected(L,union,tuple(union))\n'
                           '        chosen["complete_far_union_binding_identity"]=member_identity(union)',
                    'count': 1}]},
 {'role': 'evidence',
  'schema': 'R464-same-accurate-closed-target-incremental-M-metric-evidence-v1',
  'baseline': {'file': 'geometry_20261116_fixed_target_complete_metric_evidence.py',
               'bytes': 62091,
               'sha256': '494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05'},
  'generated': {'file': 'geometry_20261116_incremental_M_fixed_target_metric_evidence.py',
                'bytes': 62333,
                'sha256': '0eb5d8171664db099824698a8319e91a0324344b8d915032ebab932c29707f2b'},
  'replacements': [{'old': 'R459-same-accurate-closed-target-complete-relative-metric-evidence-v1',
                    'new': 'R464-same-accurate-closed-target-incremental-M-metric-evidence-v1',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_actual202_M_common_material_phase.py',
                    'new': 'geometry_20261116_current_C_incremental_M_common_material_phase.py',
                    'count': 1},
                   {'old': '059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41',
                    'new': '50bf2d04e5e4e505fad6f0ece5a896364bb94c25c9530d6a1e7c2ceef3aec923',
                    'count': 1},
                   {'old': 'R457-current-C-actual202-capable-complete-M-common-material-phase-v1',
                    'new': 'R464-current-C-incremental-M-common-material-phase-v1',
                    'count': 1},
                   {'old': '\nFAMILIES = {',
                    'new': '\n'
                           'FAMILIES = {\n'
                           '    "incrementalM": {\'file\': '
                           "'geometry_20261116_current_C_incremental_M_live_query_complete_metric.py',\n"
                           " 'sha256': '2592d09e9dc471679d4e6d8588a409c3a180132b3b478fc47fbeb1a9d91886f8',\n"
                           " 'schema': 'R464-current-C-incremental-M-relative-metric-live-queries-v1'},",
                    'count': 1}]},
 {'role': 'display',
  'schema': 'R464-current-accurate-incremental-M-multitime-display-v1',
  'baseline': {'file': 'geometry_20261116_current_C_complete_multitime_display.py',
               'bytes': 41002,
               'sha256': 'f3211ba9d74cf2be99d47fe56fcbd5526e8143f8a114364ffdc725382c286bf3'},
  'generated': {'file': 'geometry_20261116_current_C_incremental_M_multitime_display.py',
                'bytes': 41727,
                'sha256': 'e0b47bbfd355032bb433302425d09a4e6be0413107e20ac3d96e7c52586e88cf'},
  'replacements': [{'old': 'R461-current-accurate-closed-multitime-display-v1',
                    'new': 'R464-current-accurate-incremental-M-multitime-display-v1',
                    'count': 1},
                   {'old': 'geometry_20261116_current_C_actual202_M_common_material_phase.py',
                    'new': 'geometry_20261116_current_C_incremental_M_common_material_phase.py',
                    'count': 1},
                   {'old': '059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41',
                    'new': '50bf2d04e5e4e505fad6f0ece5a896364bb94c25c9530d6a1e7c2ceef3aec923',
                    'count': 1},
                   {'old': '\nFAMILIES = {',
                    'new': '\n'
                           'FAMILIES = {\n'
                           '    "incrementalM": {\'schema\': '
                           "'R464-current-C-incremental-M-accurate-cut-atlas-field-v1',\n"
                           " 'cut': 'geometry_20261116_current_C_incremental_M_accurate_cut_patch.py',\n"
                           " 'cut_sha': '8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2',\n"
                           " 'shared': 'geometry_20261116_current_C_incremental_M_shared_field.py',\n"
                           " 'shared_sha': "
                           "'55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04',\n"
                           " 'atlas': 'geometry_20261116_current_C_incremental_M_original_cuff_atlas.py',\n"
                           " 'atlas_sha': "
                           "'14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5',\n"
                           " 'caps': 'geometry_20261116_current_C_incremental_M_fixed_cap_balls.py',\n"
                           " 'caps_sha': "
                           "'3f43b4bf5e3d4e3134904a772abbf36483e1470174a1df9a3657edf03fbfe811'},",
                    'count': 1}]}]


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=True,allow_nan=False)+"\n").encode("ascii")


def receipt(path):
    path=Path(path);raw=path.read_bytes()
    return dict(file=str(path.resolve()),bytes=len(raw),sha256=sha(raw))


def interrupted(number,frame):
    raise InterruptedError("Source materialization received signal "+str(number))


def materialize(args):
    require(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
        and os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_SHA"),
        "Materialize only in the named public repository Actions")
    comp=args.computations.resolve(strict=True)
    # R463 checks cfg.computations against its own HERE. These fresh files
    # must therefore coexist with that genuine driver, not a second view dir.
    require(comp==HERE and not args.computations.is_symlink(),
        "Use this generator's genuine computations directory, also the R463 driver HERE")
    temp=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out=args.out.resolve()
    require(temp in out.parents and out!=temp and not args.out.is_symlink()
        and not out.exists() and not out.is_relative_to(comp)
        and not comp.is_relative_to(out),"Use a fresh separate owned temporary receipt directory")
    out.mkdir(parents=True)
    report=dict(schema=SCHEMA,repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],source=receipt(__file__),
        computations=str(comp),completed=False,source_preflight_complete=False,
        original_source_files=[],generated_sources=[],unconfirmed_view_roles=[v["role"] for v in VIEWS],
        current_target=None,
        error=None,no_project_module_import_or_scientific_execution=True,
        all_old_source_bytes_preserved=True,new_identities_not_old_schema_relabelling=True,
        no_raw_scientific_data_read_or_encoded=True,
        one_same_computations_directory_for_driver_profile_checkpoint_and_consumers=True)
    old_handlers={}
    try:
        for signum in (signal.SIGTERM,signal.SIGINT):
            old_handlers[signum]=signal.signal(signum,interrupted)
        # Finish every read-only check before creating any fresh source.
        for name,expected in PINS.items():
            require(Path(name).name==name,"A public source basename is required")
            path=comp/name
            require(not path.is_symlink() and path.resolve().parent==comp,
                "A defining source must be a real file in the same computations directory")
            actual=receipt(path)
            require(actual["sha256"]==expected,"Actual defining public source differs: "+name)
            report["original_source_files"].append(actual)
        ready=[];targets=set()
        for entry in VIEWS:
            base,target=entry["baseline"],entry["generated"]
            name=target["file"]
            require(Path(name).name==name and name not in targets and name!=base["file"],
                "Every view needs one distinct new basename")
            targets.add(name);destination=comp/name
            require(not destination.exists() and not destination.is_symlink(),
                "Never overwrite an original or earlier generated source: "+name)
            path=comp/base["file"]
            require(not path.is_symlink() and path.resolve().parent==comp,
                "A baseline must be an actual source in the same directory")
            raw=path.read_bytes()
            require(len(raw)==base["bytes"] and sha(raw)==base["sha256"],
                "The full frozen baseline differs: "+base["file"])
            text=raw.decode("utf-8")
            for index,item in enumerate(entry["replacements"]):
                require(type(item["count"]) is int and item["count"]>0
                    and item["old"]!=item["new"] and text.count(item["old"])==item["count"],
                    "Exact source occurrence count differs: "+name+"/"+str(index))
                text=text.replace(item["old"],item["new"])
            formed=text.encode("utf-8")
            require(len(formed)==target["bytes"] and sha(formed)==target["sha256"],
                "The generated full source identity differs: "+name)
            ready.append((entry,destination,formed))
        report["source_preflight_complete"]=True
        for entry,destination,formed in ready:
            # Exclusive creation also covers a race after the all-target pass.
            report["current_target"]=dict(role=entry["role"],path=str(destination),
                complete_expected_identity=entry["generated"])
            with destination.open("xb") as stream:
                stream.write(formed);stream.flush();os.fsync(stream.fileno())
            actual=receipt(destination)
            require(actual["bytes"]==entry["generated"]["bytes"]
                and actual["sha256"]==entry["generated"]["sha256"],
                "The real generated file write differs")
            report["generated_sources"].append(dict(role=entry["role"],schema=entry["schema"],
                original_source=entry["baseline"],actual_source=actual,
                literal_replacement_count=len(entry["replacements"])))
            report["unconfirmed_view_roles"].remove(entry["role"])
            report["current_target"]=None
        report["completed"]=True
    except BaseException as error:
        report["error"]=dict(type=type(error).__name__,message=str(error))
        report["partially_created_sources_not_deleted_or_relabelled"]=True
    finally:
        for signum,handler in old_handlers.items():signal.signal(signum,handler)
    raw=canonical(report)
    result=out/"source-view-result.json"
    with result.open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    original=receipt(result)
    if len(raw)>LIMIT:
        print(json.dumps(dict(event="R464-source-view-report-over-budget",result=original,
            complete_transported=False,no_split_or_encoded_transport=True)),flush=True)
        return 70
    print("BEGIN_R464_SOURCE_VIEW_RESULT",flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_R464_SOURCE_VIEW_RESULT",flush=True)
    print(json.dumps(dict(event="R464-source-views-returned",completed=report["completed"],
        result=original,no_scientific_execution=True)),flush=True)
    return 0 if report["completed"] else 2


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    return materialize(parser.parse_args(argv))


if __name__=="__main__":raise SystemExit(main())
