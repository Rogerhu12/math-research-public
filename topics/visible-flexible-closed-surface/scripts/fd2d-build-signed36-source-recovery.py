#!/usr/bin/env python3
"""Reconstruct an explicitly NEW signed36 recovery implementation.

This source was saved through the authorized small-text GitHub fallback
while the execution environment was unavailable. It has not been run.
It verifies every frozen template before making deterministic text changes.
It never claims the newly reconstructed modules have the pre-outage36
source SHA, and it never relabels a historical field, residual or normal.

If the original filesystem returns, prefer its original sources and its
complete raw tile. This generator refuses every differing existing output.
Only missing files, or exactly matching generated files, are accepted.
Actual numerical use requires the new request's own complete baseline.
"""
from __future__ import annotations
import argparse,ast,hashlib,json,os
from pathlib import Path

PAYLOAD=json.loads(r'''{
  "schema": "fd2d-unexecuted-signed36-deterministic-source-reconstruction-v1",
  "jobs": [
    {
      "source": "scripts/fd2d_gc_positive_trace_merit.py",
      "source_git_blob": "30f0e2a7506236adc47c726cbc804fd21e2ceee5",
      "destination": "scripts/fd2d_gc_signed_trace_merit.py",
      "replacements": [
        {
          "before": "from fd2d_gc_raw_bump_positive_trace import actual_state_columns",
          "after": "from fd2d_gc_signed_trace_problem import actual_state_columns",
          "count": 1
        },
        {
          "before": "rows=d2_high_rows(problem);w=problem.window();selected=np.flatnonzero((w[:-1]!=1.)&(problem.x[:-1]<problem.trace_ramp_stop))",
          "after": "rows=d2_high_rows(problem);selected=np.flatnonzero(problem.retained_gauss_mask())",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted source reconstruction during executor outage.\n# Reuses the frozen declared formulas; it does not claim pre-outage36 byte identity.\n",
      "notes": "Actual signed chain columns and actual Gauss platform row selection only.",
      "output_sha256": "efe6ac6ed52ced057593b07823593a5b821c58e25bd1c06eaad64d24edb2854c"
    },
    {
      "source": "scripts/fd2d_gc_positive_trace_interior_merit.py",
      "source_git_blob": "a3dc9f803a2d245fbe2967e585a0c6c9367aa4e6",
      "destination": "scripts/fd2d_gc_signed_trace_interior_merit.py",
      "replacements": [
        {
          "before": "from fd2d_gc_raw_bump_positive_trace import actual_state_columns",
          "after": "from fd2d_gc_signed_trace_problem import actual_state_columns",
          "count": 1
        },
        {
          "before": "fd2d_gc_positive_trace_merit",
          "after": "fd2d_gc_signed_trace_merit",
          "count": 1
        },
        {
          "before": "T=positive_trace_delta(background,bangular,jet['K'][None,:],view.trace_window()[None,:],exact_tail_mask=view.trace_mask()[None,:])",
          "after": "T=view.trace_delta(background,bangular,jet['K'][None,:],exact_tail_mask=view.trace_mask()[None,:])",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted source reconstruction during executor outage.\n# Reuses the frozen declared formulas; it does not claim pre-outage36 byte identity.\n",
      "notes": "Actual signed field at declared P1 interior points; complete state/parameter derivatives unchanged.",
      "output_sha256": "d232f373847660e91647ce6ddb5ce2aeea8cebaf7a99d6d6a62cd33d8e32168b"
    },
    {
      "source": "scripts/fd2d_gc_grouped_coast_stream_normal.py",
      "source_git_blob": "2fe155667e378865e9bd1e186d6b0e4c3afb9d91",
      "destination": "scripts/fd2d_gc_signed_trace_stream_normal.py",
      "replacements": [
        {
          "before": "fd2d_gc_positive_trace_merit",
          "after": "fd2d_gc_signed_trace_merit",
          "count": 1
        },
        {
          "before": "fd2d_gc_raw_bump_positive_trace",
          "after": "fd2d_gc_signed_trace_problem",
          "count": 1
        },
        {
          "before": "fd2d_gc_grouped_coast_codazzi",
          "after": "fd2d_gc_signed_grouped_cells",
          "count": 1
        },
        {
          "before": "gauss_cell_positive_trace_grouped_coast",
          "after": "gauss_cell_signed_trace_grouped",
          "count": 2
        },
        {
          "before": "stream_positive_trace_normal",
          "after": "stream_signed_trace_normal",
          "count": 1
        },
        {
          "before": "    w = problem.window()\n    selected = (w != 1.) & (problem.x < problem.trace_ramp_stop)\n    selected[-1] = False",
          "after": "    selected = np.asarray(problem.retained_gauss_mask(), bool)",
          "count": 1
        },
        {
          "before": "    grouped_rules = []; grouped_cells = []",
          "after": "    grouped_rules = []; grouped_cells = []; signed_rules = []",
          "count": 1
        },
        {
          "before": "        del packet, jr, jh, view",
          "after": "        for observation in packet['info'].get('grouped_signed_rules', []):\n            record = dict(observation, global_cell=first+int(observation['local_cell']),\n                          stream_chunk_first_cell=first)\n            signed_rules.append(record)\n            fine = float(observation['fine_sampled_Gauss_maximum'])\n            previous = maxima['fine_sampled_interior_Gauss']\n            maxima['fine_sampled_interior_Gauss'] = fine if previous is None else max(previous, fine)\n        del packet, jr, jh, view",
          "count": 1
        },
        {
          "before": "        grouped_coast_rules=grouped_rules,",
          "after": "        grouped_coast_rules=grouped_rules, grouped_signed_rules=signed_rules,\n        grouped_signed_global_cells=[r['global_cell'] for r in signed_rules],",
          "count": 1
        },
        {
          "before": "Only explicitly evaluated R165 grouped_coast_rules; None means no such sample in this subset",
          "after": "Only explicitly evaluated coast and signed fine rules; None means no fine sample in this subset",
          "count": 1
        },
        {
          "before": "fd2d-R159-R165-local-node-cell-normal-grouped-consumer-v1",
          "after": "fd2d-R182-recovery-local-node-cell-normal-signed-consumer-v1",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Same local normal blocks and elimination, with actual signed field chain and retained mask; distinct fine diagnostics.",
      "output_sha256": "2730f2c6cd996be468f46b318de19f89e1256e17a17341955e45f8d177b43126"
    },
    {
      "source": "scripts/fd2d_gc_grouped_coast_partitioned_normal.py",
      "source_git_blob": "ac87b618f1e24dabc8bc3af00b524bafd2e81ae6",
      "destination": "scripts/fd2d_gc_signed_trace_partitioned_normal.py",
      "replacements": [
        {
          "before": "fd2d_gc_grouped_coast_stream_normal",
          "after": "fd2d_gc_signed_trace_stream_normal",
          "count": 1
        },
        {
          "before": "stream_positive_trace_normal",
          "after": "stream_signed_trace_normal",
          "count": 2
        },
        {
          "before": "fd2d_gc_positive_trace_interior_merit",
          "after": "fd2d_gc_signed_trace_interior_merit",
          "count": 1
        },
        {
          "before": "fd2d_gc_grouped_coast_codazzi",
          "after": "fd2d_gc_signed_grouped_cells",
          "count": 1
        },
        {
          "before": "gauss_cell_positive_trace_grouped_coast",
          "after": "gauss_cell_signed_trace_grouped",
          "count": 2
        },
        {
          "before": "    window=np.asarray(problem.window())\n    selected=(window!=1.)&(problem.x<problem.trace_ramp_stop);selected[-1]=False",
          "after": "    selected=np.asarray(problem.retained_gauss_mask(),bool)",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Same ordered normal partition and merge; row ledger follows the actual signed platforms.",
      "output_sha256": "53fb692983278bb266a567a677703635a55369baa322331766bbc2c8b98e33c2"
    },
    {
      "source": "scripts/fd2d_gc_positive_trace_value_nodes.py",
      "source_git_blob": "5d0e5ac4bbc940e9bc7c6fa4cdbf4802164edfa7",
      "destination": "scripts/fd2d_gc_signed_trace_value_nodes.py",
      "replacements": [
        {
          "before": "fd2d_gc_positive_trace_stream_normal",
          "after": "fd2d_gc_signed_trace_stream_normal",
          "count": 1
        },
        {
          "before": "selected=np.asarray(problem.retained_actual_gauss_nodes,int)",
          "after": "selected=np.flatnonzero(problem.retained_gauss_mask())",
          "count": 1
        },
        {
          "before": "np.flatnonzero(problem.x[:-1]>=problem.trace_ramp_stop)",
          "after": "np.flatnonzero(problem.trace_window()[:-1]==1.)",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "One-node actual signed field and exact retained rows; independent whole parameter packet avoided.",
      "output_sha256": "05e88258d28fb819ce926ea16072946f8cf39865027ae56763357f2a569f6804"
    },
    {
      "source": "scripts/fd2d_gc_checkpointed_grouped_values.py",
      "source_git_blob": "83331ce3f4ccd39cd6b4a5a3d2fb398ea9120e58",
      "destination": "scripts/fd2d_gc_checkpointed_signed_values.py",
      "replacements": [
        {
          "before": "fd2d_gc_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 3
        },
        {
          "before": "fd2d_gc_grouped_coast_codazzi",
          "after": "fd2d_gc_signed_grouped_cells",
          "count": 2
        },
        {
          "before": "gauss_cell_positive_trace_grouped_coast",
          "after": "gauss_cell_signed_trace_grouped",
          "count": 2
        },
        {
          "before": "fd2d_gc_positive_trace_stream_normal",
          "after": "fd2d_gc_signed_trace_stream_normal",
          "count": 2
        },
        {
          "before": "fd2d_gc_positive_trace_merit",
          "after": "fd2d_gc_signed_trace_merit",
          "count": 2
        },
        {
          "before": "fd2d_gc_positive_trace_interior_merit",
          "after": "fd2d_gc_signed_trace_interior_merit",
          "count": 2
        },
        {
          "before": "fd2d_gc_positive_trace_value_nodes",
          "after": "fd2d_gc_signed_trace_value_nodes",
          "count": 1
        },
        {
          "before": "fd2d-complete-R165-value-block-replay-v1",
          "after": "fd2d-recovery-complete-R182-signed-value-block-replay-v1",
          "count": 1
        },
        {
          "before": "selected=np.asarray(problem.retained_actual_gauss_nodes,int)",
          "after": "selected=np.flatnonzero(problem.retained_gauss_mask())",
          "count": 1
        },
        {
          "before": "np.flatnonzero(problem.x[:-1]>=problem.trace_ramp_stop)",
          "after": "np.flatnonzero(problem.trace_window()[:-1]==1.)",
          "count": 1
        },
        {
          "before": "    grouped_rules=[];block_records=[]",
          "after": "    grouped_rules=[];signed_rules=[];block_records=[]",
          "count": 1
        },
        {
          "before": "        grouped_rules.extend(rows)",
          "after": "        grouped_rules.extend(rows)\n        signed=[]\n        for rule in info.get('grouped_signed_rules',[]):\n            signed.append(dict(rule,global_cell=start+int(rule['local_cell'])))\n        signed_rules.extend(signed)",
          "count": 1
        },
        {
          "before": "    if global_cells!=expected:raise ArithmeticError('Grouped diagnostics omit or duplicate cells')",
          "after": "    if global_cells!=expected:raise ArithmeticError('Grouped diagnostics omit or duplicate cells')\n    signed_cells=[r['global_cell'] for r in signed_rules]\n    selected_signed=np.zeros(ctx.problem.N-1,bool)\n    for window in ctx.problem.signed_windows:\n        A,B,C,D=window['breaks']\n        selected_signed|=(ctx.problem.x[:-1]<D)&(ctx.problem.x[1:]>A)\n    expected_signed=np.flatnonzero(selected_signed).tolist()\n    if signed_cells!=expected_signed:\n        raise ArithmeticError('Signed fine diagnostics omit, duplicate or reorder cells')",
          "count": 1
        },
        {
          "before": "whole_grouped_coast_cell_count=len(global_cells),grouped_block_records=block_records,",
          "after": "whole_grouped_coast_cell_count=len(global_cells),grouped_block_records=block_records,\n        whole_grouped_signed_rules=signed_rules,whole_grouped_signed_cells=signed_cells,\n        whole_grouped_signed_cell_count=len(signed_cells),",
          "count": 1
        },
        {
          "before": "(max(r['fine_sampled_Gauss_maximum'] for r in grouped_rules)\n                                           if grouped_rules else None)",
          "after": "(max(r['fine_sampled_Gauss_maximum'] for r in grouped_rules+signed_rules)\n                                           if grouped_rules or signed_rules else None)",
          "count": 1
        },
        {
          "before": "All grouped coast cells with global saved-mesh indices",
          "after": "All selected coast and signed fine cells with global saved-mesh indices",
          "count": 1
        },
        {
          "before": "This engine evaluates only the explicit R165 complete finite objective",
          "after": "This engine evaluates only the explicit complete signed/coast finite objective",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Complete actual residual replay with identical row order and separate coast/signed fine coverage.",
      "output_sha256": "9ec08c3d4f0491adf688ecf9c96d77fd3db9579da23b402d5ad9115ae89611df"
    },
    {
      "source": "scripts/fd2d_gc_dyadic_grouped_search_context.py",
      "source_git_blob": "f983c43901e241e6f09a81c8d0bcf2bcf117e958",
      "destination": "scripts/fd2d_gc_signed_search_context_v2.py",
      "replacements": [
        {
          "before": "from fd2d_gc_dyadic_tail_problem import create_dyadic_tail_problem,checkpoint_arrays",
          "after": "from fd2d_gc_signed_trace_problem import create_signed_trace_problem,checkpoint_arrays\nfrom fd2d_gc_signed_grouped_cells import FINITE_RULE\nfrom fd2d_gc_signed_search_domain_recovery import install_signed_search_domain",
          "count": 1
        },
        {
          "before": "('candidate','warm_start','radius_packet','reference_inlet','reference_cache','owner_stop_file')",
          "after": "('candidate','warm_start','radius_packet','reference_inlet','reference_cache','owner_stop_file',\n                    'origin_field','signed_domain_path','signed_qp_path')",
          "count": 1
        },
        {
          "before": "create_dyadic_tail_problem(self.args.candidate,saved_field=self.a,split_cells=(),",
          "after": "create_signed_trace_problem(self.args.candidate,origin_field=self.args.origin_field,\n            saved_field=self.args.warm_start,windows=self.args.signed_windows,split_cells=(),",
          "count": 1
        },
        {
          "before": "        problem=self.problem",
          "after": "        problem=self.problem\n        self.signed_domain_handle=install_signed_search_domain(problem,\n            windows=self.args.signed_windows,domain_path=self.args.signed_domain_path,\n            qp_path=self.args.signed_qp_path)\n        if not np.isfinite(self.args.profile_box) or self.args.profile_box<=0 or np.any(\n                self.args.profile_box>self.signed_domain_handle.delta_absolute_bounds):\n            raise ValueError('The search box exceeds the exact signed-domain coefficient box')",
          "count": 1
        },
        {
          "before": "                ('gauss_l_definition',problem.gauss_l_definition),\n                ('positive_trace_definition',problem.positive_trace_definition)):",
          "after": "                ('gauss_l_definition',problem.gauss_l_definition)):",
          "count": 1
        },
        {
          "before": "        self.vector=self.project(old)",
          "after": "        self.vector=self.project(old)\n        self.report['origin_field']=identity(self.args.origin_field)\n        self.report['explicit_signed_representation_transition']=bool(problem.signed_transition_from_original)\n        self.a=checkpoint_arrays(problem,self.vector,self.report['candidate']['sha256'],\n            refinement_definition=problem.radial_refinement_definition)\n        self._refresh_actual_certificates(self.a,self.vector)",
          "count": 1
        },
        {
          "before": "permitted,domain=checked_search_domain(problem,self.vector,self.args.central_cap,self.args.central_floor)",
          "after": "permitted,domain=self.check_domain(self.vector)",
          "count": 1
        },
        {
          "before": "Original R152 split G8 affine coast lifting + original R153/R155 complete nonlinear G2; original actual n/m endpoint differences",
          "after": "Explicit signed actual field, full signed/coast split G8 and original terminal G2",
          "count": 1
        },
        {
          "before": "consumer=identity(here/'fd2d_gc_grouped_coast_codazzi.py')",
          "after": "consumer=identity(here/'fd2d_gc_signed_grouped_cells.py')",
          "count": 1
        },
        {
          "before": "self.report['providers']['fd2d_gc_grouped_coast_codazzi.py']=consumer",
          "after": "self.report['providers']['fd2d_gc_signed_grouped_cells.py']=consumer",
          "count": 1
        },
        {
          "before": "consumer_source=dict(name='fd2d_gc_grouped_coast_codazzi.py'",
          "after": "consumer_source=dict(name='fd2d_gc_signed_grouped_cells.py'",
          "count": 1
        },
        {
          "before": "fd2d_gc_grouped_coast_codazzi_py=consumer['sha256']",
          "after": "fd2d_gc_signed_grouped_cells_py=consumer['sha256']",
          "count": 1
        },
        {
          "before": "            finite_objective_unchanged_by_selected_domain=True)\n",
          "after": "            finite_objective_unchanged_by_selected_domain=True)\n        new_sources=('fd2d_gc_signed_trace_problem.py','fd2d_gc_signed_trace_windows.py',\n            'fd2d_gc_signed_trace_cells.py','fd2d_gc_signed_trace_fine_cells.py',\n            'fd2d_gc_signed_grouped_cells.py','fd2d_gc_signed_trace_merit.py',\n            'fd2d_gc_signed_trace_interior_merit.py','fd2d_gc_signed_trace_value_nodes.py',\n            'fd2d_gc_signed_trace_stream_normal.py','fd2d_gc_signed_trace_partitioned_normal.py',\n            'fd2d_gc_checkpointed_signed_values.py','fd2d_gc_signed_search_domain_recovery.py')\n        for name in new_sources:self.report['providers'][name]=identity(here/name)\n        self.report.update(schema='fd2d-R182-reconstructed-signed-finite-context-v1',\n            recovery_source_reconstruction=True,recovery_sources_executed_before_outage=False,\n            original_preoutage36_source_bytes_claimed=False,\n            physical_field_definition_unchanged_by_cell_rule=True,\n            actual_field_changed_by_signed_representation=bool(problem.signed_transition_from_original),\n            physical_g_changed_by_signed_representation=False,\n            finite_objective_changed_from_original_R170=True,\n            signed_trace_definition=problem.signed_trace_definition,\n            signed_search_domain_definition=self.signed_domain_handle.definition())\n        self.report['grouped_rule_definition'].update(\n            schema='fd2d-R182-recovery-whole-actual-signed-and-coast-G8-v1',\n            signed_windows=problem.signed_windows,\n            outside_coast_consumer_unchanged=False,\n            exact_full_endpoint_functions=True,\n            actual_signed_Gauss_platform_rows_removed=True,\n            fine_rule='R165 whole actual coast plus whole actual signed-window cells at split G8')\n        self.binding.update(schema='fd2d-R182-recovery-signed-field-and-finite-goal-v1',\n            signed_trace_definition=problem.signed_trace_definition,\n            origin_field_content={k:self.report['origin_field'][k] for k in ('bytes','sha256')},\n            grouped_rule_definition=self.report['grouped_rule_definition'],\n            signed_search_domain_definition=self.signed_domain_handle.definition(),\n            complete_profile_linear_matrix=array_identity(problem.profile_domain['matrix']),\n            complete_profile_linear_lower=array_identity(problem.profile_domain['lower']),\n            implementation_sources={name:r['sha256'] for name,r in self.report['providers'].items()},\n            original_preoutage36_source_bytes_claimed=False,\n            recovery_baseline_must_be_actually_evaluated=True)\n",
          "count": 1
        },
        {
          "before": "        return answer\n\n    def checkpoint",
          "after": "        answer['exact_signed_K_domain']=self.signed_domain_handle.verify_delta(p[self.problem.profile_parameter_slice])\n        return answer\n\n    def checkpoint",
          "count": 1
        },
        {
          "before": "        if extra:arrays.update(extra)\n        return save_npz",
          "after": "        if extra:arrays.update(extra)\n        self._refresh_actual_certificates(arrays,v)\n        return save_npz",
          "count": 1
        }
      ],
      "prefix": "# Explicit reconstructed and unexecuted recovery context; not pre-outage36 source bytes.\n",
      "suffix": "\n    def check_domain(self,v,central_cap=None,central_floor=None):\n        cap=self.args.central_cap if central_cap is None else float(central_cap)\n        floor=self.args.central_floor if central_floor is None else float(central_floor)\n        permitted,diagnostic=checked_search_domain(self.problem,v,cap,floor)\n        _,parameters=self.problem.unpack(np.asarray(v,float))\n        exact=self.signed_domain_handle.verify_delta(\n            parameters[self.problem.profile_parameter_slice])\n        diagnostic=dict(diagnostic,exact_signed_K_domain=exact)\n        return bool(permitted and exact['passed']),diagnostic\n\n    def _refresh_actual_certificates(self,arrays,v):\n        _,parameters=self.problem.unpack(np.asarray(v,float))\n        tail=self.problem.tail_control_box.certificate(\n            parameters[self.problem.tail_parameter_slice])\n        exact=self.signed_domain_handle.verify_delta(\n            parameters[self.problem.profile_parameter_slice])\n        if not tail['passed'] or not exact['passed']:\n            raise ValueError('Do not archive a state with stale or failed exact domain certificates')\n        arrays['tail_search_domain_certificate']=np.array(json.dumps(tail,sort_keys=True))\n        arrays['signed_search_domain_definition']=np.array(json.dumps(\n            self.signed_domain_handle.definition(),sort_keys=True))\n        arrays['signed_search_domain_certificate']=np.array(json.dumps(exact,sort_keys=True))\n\n    def objective(self,v,jacobian=False):\n        if jacobian:raise ValueError('Use the actual signed row-partition normal assembler')\n        from fd2d_gc_checkpointed_signed_values import checkpointed_grouped_objective\n        return checkpointed_grouped_objective(self,v,\n            Path(self.request['cache_dir'])/'context-actual-value-cache')\n\n    def diag(self,v,data):\n        out=super().diag(v,data)\n        out.update(finite_radial_scheme=FINITE_RULE,\n            signed_trace_definition=self.problem.signed_trace_definition,\n            physical_field_has_signed_disjoint_traces=True,\n            strong_target_complete=False,continuous_certificate=False)\n        return out\n",
      "notes": "Direct explicit signed constructor; exact active-window domain; fresh current-tail/Delta certificates. Existing R170 projection and original field definitions remain explicit.",
      "output_sha256": "d1aaeadce0a4fb1652df2eb5a1d7ad1415e840e214d3d05acfcb17be066d65b0"
    },
    {
      "source": "scripts/fd2d_gc_dyadic_compressed_normal_tile_io.py",
      "source_git_blob": "237659259bc344b9d7e454cb3f3e002e222bf92d",
      "destination": "scripts/fd2d_gc_signed_compressed_normal_tile_io.py",
      "replacements": [
        {
          "before": "fd2d_gc_dyadic_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 1
        },
        {
          "before": "fd2d_gc_grouped_coast_partitioned_normal",
          "after": "fd2d_gc_signed_trace_partitioned_normal",
          "count": 2
        },
        {
          "before": "fd2d_gc_grouped_coast_stream_normal",
          "after": "fd2d_gc_signed_trace_stream_normal",
          "count": 1
        },
        {
          "before": "fd2d-gc-dyadic-compressed-stage-normal-tile-batch.py",
          "after": "fd2d-gc-signed-stage-normal-tile-batch-v2.py",
          "count": 1
        },
        {
          "before": "fd2d-gc-compressed-piecewise-normal-reduce.py",
          "after": "fd2d-gc-compressed-piecewise-normal-reduce-v2.py",
          "count": 1
        },
        {
          "before": "fd2d_gc_dyadic_compressed_normal_tile_io.py",
          "after": "fd2d_gc_signed_compressed_normal_tile_io.py",
          "count": 1
        },
        {
          "before": "fd2d_gc_compressed_normal_tile.py",
          "after": "fd2d_gc_compressed_normal_tile_v2.py",
          "count": 1
        },
        {
          "before": "fd2d-R170-R165-compressed-partitioned-normal-common-binding-v1",
          "after": "fd2d-R182-recovery-compressed-partitioned-normal-common-binding-v1",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "New complete goal binding and identical durable row partition; never old normal reuse.",
      "output_sha256": "d1113d752ace88441546f6d2b9d4cb0e8bff1af4df04122dcceb35972a7474a8"
    },
    {
      "source": "scripts/fd2d-gc-dyadic-stage-normal-plan.py",
      "source_git_blob": "d5caafcf37fe6d5347a8b9e9f4aa39fa4a8811ba",
      "destination": "scripts/fd2d-gc-signed-stage-normal-plan.py",
      "replacements": [
        {
          "before": "fd2d_gc_dyadic_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 1
        },
        {
          "before": "fd2d_gc_dyadic_normal_tile_io",
          "after": "fd2d_gc_signed_compressed_normal_tile_io",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Plan only, same row coverage methods and actual new context identity.",
      "output_sha256": "f5ef7cf125d7df0c56b288b4024a012cd44ea05dce11399c60d5cf67337343d2"
    },
    {
      "source": "scripts/fd2d-gc-dyadic-stage-baseline-checkpointed.py",
      "source_git_blob": "02ec6a602b2ceff1e5a87169871722d2eeb85785",
      "destination": "scripts/fd2d-gc-signed-stage-baseline-checkpointed.py",
      "replacements": [
        {
          "before": "fd2d_gc_dyadic_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 1
        },
        {
          "before": "fd2d_gc_checkpointed_grouped_values",
          "after": "fd2d_gc_checkpointed_signed_values",
          "count": 1
        },
        {
          "before": "actual_value_baseline",
          "after": "actual_signed_value_baseline",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Real complete signed baseline, independent durable packets; no historical residual reused.",
      "output_sha256": "5b55081ae262ccd43ed44e20fafcc0f0b03afd531945921c44f8928503de9e70"
    },
    {
      "source": "scripts/fd2d-gc-dyadic-stage-schur-selected.py",
      "source_git_blob": "7fd4f8e8d4213f6d88d7c60720def4fe1d42f463",
      "destination": "scripts/fd2d-gc-signed-stage-schur-selected.py",
      "replacements": [
        {
          "before": "fd2d_gc_dyadic_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 1
        },
        {
          "before": "fd2d_gc_dyadic_stage_io_v2",
          "after": "fd2d_gc_signed_stage_io",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Same SPD block solver and Schur packet with current explicit signed normal binding.",
      "output_sha256": "3a3cfd7967da0d478af2d01faeccc774d387b61839440544734be9a4610879cd"
    },
    {
      "source": "scripts/fd2d-gc-dyadic-stage-qp-v2.py",
      "source_git_blob": "45acc5ac04ed03050ec2c79d076a39cf044e6eaa",
      "destination": "scripts/fd2d-gc-signed-stage-qp-v2.py",
      "replacements": [
        {
          "before": "fd2d_gc_dyadic_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 1
        },
        {
          "before": "fd2d_gc_dyadic_stage_io_v2",
          "after": "fd2d_gc_signed_stage_io",
          "count": 1
        },
        {
          "before": "explicit_R170_tail_domain_QP_from_unchanged_same_function_Schur",
          "after": "explicit_R182_signed_domain_QP_from_same_state_Schur",
          "count": 1
        },
        {
          "before": "        information['exact_proposed_dyadic_certificate']=ctx.problem.tail_control_box.certificate(proposed_parameters[ctx.problem.tail_parameter_slice])",
          "after": "        information['exact_proposed_dyadic_certificate']=ctx.problem.tail_control_box.certificate(proposed_parameters[ctx.problem.tail_parameter_slice])\n        information['exact_proposed_signed_domain_certificate']=ctx.signed_domain_handle.verify_delta(proposed_parameters[ctx.problem.profile_parameter_slice])\n        information['signed_search_domain_definition']=ctx.signed_domain_handle.definition()",
          "count": 1
        },
        {
          "before": "profile_box=ctx.args.profile_box,preserve_gap=True,tail_search_domain=ctx.problem.tail_search_domain_definition)",
          "after": "profile_box=ctx.args.profile_box,preserve_gap=True,tail_search_domain=ctx.problem.tail_search_domain_definition,\n                signed_search_domain=ctx.signed_domain_handle.definition())",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Same bounded Schur QP, current full profile rows include selected signed K domain. Exact proposed certificates reported.",
      "output_sha256": "182af43230c5962aa1a4f41838e27c4a37df139ba72d9300ae3f1cacdac89cac"
    },
    {
      "source": "scripts/fd2d-gc-dyadic-stage-trial.py",
      "source_git_blob": "dffc2b69e06a55af69750099379ccf07eef85c9d",
      "destination": "scripts/fd2d-gc-signed-stage-trial.py",
      "replacements": [
        {
          "before": "fd2d_gc_dyadic_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 1
        },
        {
          "before": "fd2d_gc_checkpointed_grouped_values",
          "after": "fd2d_gc_checkpointed_signed_values",
          "count": 2
        },
        {
          "before": "R170_actual_checkpointed_Armijo_trial",
          "after": "R182_actual_checkpointed_Armijo_trial",
          "count": 1
        },
        {
          "before": "permitted,domain=checked_search_domain(ctx.problem,trial,ctx.args.central_cap,ctx.args.central_floor)",
          "after": "permitted,domain=ctx.check_domain(trial)",
          "count": 1
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; no pre-outage36 byte identity is claimed.\n",
      "notes": "Same full actual Armijo inequality, additional explicit exact current signed-domain verification.",
      "output_sha256": "b979d5f8d5b2e47da39db6fef6821685112ae79588d99ef7fb09d2b93a5b1ee6"
    },
    {
      "source": "scripts/fd2d-gc-dyadic-compressed-stage-normal-tile-batch.py",
      "source_git_blob": "ceedc797a31cbdeb7324256bd0b085281dd4c147",
      "destination": "scripts/fd2d-gc-signed-stage-normal-tile-batch.py",
      "replacements": [
        {
          "before": "fd2d_gc_dyadic_grouped_search_context",
          "after": "fd2d_gc_signed_search_context_v2",
          "count": 1
        },
        {
          "before": "fd2d_gc_dyadic_compressed_normal_tile_io",
          "after": "fd2d_gc_signed_compressed_normal_tile_io",
          "count": 1
        },
        {
          "before": "fd2d_gc_grouped_coast_partitioned_normal",
          "after": "fd2d_gc_signed_trace_partitioned_normal",
          "count": 1
        },
        {
          "before": "fd2d_gc_grouped_coast_codazzi",
          "after": "fd2d_gc_signed_grouped_cells",
          "count": 1
        },
        {
          "before": "gauss_cell_positive_trace_grouped_coast",
          "after": "gauss_cell_signed_trace_grouped",
          "count": 2
        }
      ],
      "prefix": "# Explicit unexecuted reconstruction; keep this v1 transport template separate from the v2 actual caller.\n",
      "notes": "Numerical assembly template; actual recovery uses compact-v2 transport.",
      "output_sha256": "3db41d5c3111ff21d5189402667c2be2d3f487061e2bae2a5dc29472c5d7d707"
    }
  ],
  "literals": {
    "scripts/fd2d_gc_signed_stage_io.py": {
      "content": "\"\"\"Explicit fresh signed-normal selection; no old-domain normal reuse.\"\"\"\nimport json\nfrom pathlib import Path\nfrom fd2d_gc_archive_arrays import identity\nfrom fd2d_gc_signed_compressed_normal_tile_io import partition_context,merged_normal_binding\nfrom fd2d_gc_selected_normal_io import load_selected_normal\nfrom fd2d_gc_schur_stage_io import factor_binding\n\n\ndef selected_normal(context):\n    root=Path(context.request['cache_dir'])\n    reference=root/'normal-reference.json'\n    if not reference.exists():\n        _,plan,common,_=partition_context(context)\n        return (root/'normal-partitioned'/'manifest.json',\n            merged_normal_binding(common,plan),dict(kind='fresh_explicit_signed_normal'))\n    description=json.loads(reference.read_text())\n    if description.get('schema')!='fd2d-explicit-piecewise-merged-normal-reference-v1':\n        raise ValueError('Recovery signed context accepts only its freshly assembled piecewise normal')\n    if description['finite_goal']!=context.binding:\n        raise ValueError('Normal belongs to another exact field or finite goal')\n    saved=description['normal_manifest'];actual=identity(saved['path'])\n    if any(actual[k]!=saved[k] for k in ('bytes','sha256')):\n        raise ValueError('Complete signed normal manifest changed')\n    expected=description['transport_binding']\n    if expected.get('common',{}).get('field_and_finite_objective')!=context.binding:\n        raise ValueError('Signed normal transport does not bind the complete current field')\n    _,plan,common,_=partition_context(context)\n    if expected!=merged_normal_binding(common,plan):\n        raise ValueError('Complete signed normal does not bind this actual partition')\n    return Path(saved['path']),expected,dict(kind=description['schema'],reference=identity(reference))\n\n\ndef selected_factor_binding(context,manifest,damping,solver,producer):\n    return factor_binding(context,manifest,damping,solver,producer)\n",
      "sha256": "7ec6ccfa8ccc881837990e4da96f98e12b16db199a29e7720f6fad74ff49e40d"
    },
    "notes/2026-11-12-fd2d-signed36-negative-source-recovery01-request.json": {
      "content": "{\n  \"schema\": \"fd2d-unexecuted-explicit-signed-recovery-request-v1\",\n  \"run_prefix\": \"notes/2026-11-12-fd2d-signed36-negative-source-recovery01\",\n  \"cache_dir\": \"notes/2026-11-12-fd2d-signed36-negative-source-recovery01-work\",\n  \"settings\": {\n    \"candidate\": \"notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json\",\n    \"warm_start\": \"notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz\",\n    \"radius_packet\": \"notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json\",\n    \"reference_inlet\": \"notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz\",\n    \"reference_cache\": \"notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz\",\n    \"reference_rim_fraction\": 0.12,\n    \"out_prefix\": \"notes/2026-11-12-fd2d-signed36-negative-source-recovery01\",\n    \"owner_stop_file\": \"notes/2026-11-12-fd2d-signed36-negative-source-recovery01-stop\",\n    \"max_iterations\": 1,\n    \"modes\": 31,\n    \"mesh_step\": 0.04,\n    \"gap\": 0.8,\n    \"central_floor\": 0.1,\n    \"central_cap\": 7.352941176470588,\n    \"profile_box\": 0.08,\n    \"radius_floor\": 0.1,\n    \"curvature_cap\": 8.1,\n    \"curvature_weight\": 1,\n    \"high_gauss_weight\": 1,\n    \"high_codazzi_weight\": 1,\n    \"mesh_relative_tolerance\": 1e-12,\n    \"damping\": 0.00001,\n    \"finite_tolerance\": 2e-7,\n    \"minimum_active_n\": 0.05,\n    \"interior_cells\": [\n      63,\n      64,\n      65,\n      74,\n      75,\n      76,\n      123,\n      124\n    ],\n    \"interior_gauss_weight\": 1,\n    \"block_cells\": 2,\n    \"prepared_cache_mib\": 16,\n    \"operator_cache_mib\": 32,\n    \"origin_field\": \"notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz\",\n    \"signed_windows\": [\n      {\n        \"name\": \"mid_positive\",\n        \"sign\": 1,\n        \"breaks\": [\n          0.9,\n          0.915,\n          0.985,\n          0.99\n        ]\n      },\n      {\n        \"name\": \"late_negative\",\n        \"sign\": -1,\n        \"breaks\": [\n          1.423,\n          1.428,\n          1.442,\n          1.445\n        ]\n      }\n    ],\n    \"signed_domain_path\": \"notes/2026-11-12-fd2d-signed-domain-recovery-01-domain.json.gz\",\n    \"signed_qp_path\": \"notes/2026-11-12-fd2d-signed-domain-recovery-01-qp.npz\"\n  },\n  \"input_sha256\": \"b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f\",\n  \"owner\": \"numerical_recovery\",\n  \"source_reconstruction_not_original36_bytes\": true,\n  \"actual_field_changed_by_representation\": true,\n  \"physical_g_unchanged_by_representation\": true,\n  \"new_actual_baseline_and_normal_required\": true,\n  \"old36_partial_normal_not_relabelled\": true,\n  \"new_actual_F_J_evaluations\": 0,\n  \"strong_target_complete\": false,\n  \"recovery_generator\": \"scripts/fd2d-build-signed36-source-recovery.py\"\n}\n",
      "sha256": "3ee96e39a9f78998b4d5c3d29c31a1e879a391351b56904c36c780ab84f7a8f7"
    },
    "notes/2026-11-12-fd2d-signed36-positive-source-recovery01-request.json": {
      "content": "{\n  \"schema\": \"fd2d-unexecuted-explicit-signed-recovery-request-v1\",\n  \"run_prefix\": \"notes/2026-11-12-fd2d-signed36-positive-source-recovery01\",\n  \"cache_dir\": \"notes/2026-11-12-fd2d-signed36-positive-source-recovery01-work\",\n  \"settings\": {\n    \"candidate\": \"notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json\",\n    \"warm_start\": \"notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz\",\n    \"radius_packet\": \"notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json\",\n    \"reference_inlet\": \"notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz\",\n    \"reference_cache\": \"notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz\",\n    \"reference_rim_fraction\": 0.12,\n    \"out_prefix\": \"notes/2026-11-12-fd2d-signed36-positive-source-recovery01\",\n    \"owner_stop_file\": \"notes/2026-11-12-fd2d-signed36-positive-source-recovery01-stop\",\n    \"max_iterations\": 1,\n    \"modes\": 31,\n    \"mesh_step\": 0.04,\n    \"gap\": 0.8,\n    \"central_floor\": 0.1,\n    \"central_cap\": 7.352941176470588,\n    \"profile_box\": 0.08,\n    \"radius_floor\": 0.1,\n    \"curvature_cap\": 8.1,\n    \"curvature_weight\": 1,\n    \"high_gauss_weight\": 1,\n    \"high_codazzi_weight\": 1,\n    \"mesh_relative_tolerance\": 1e-12,\n    \"damping\": 0.00001,\n    \"finite_tolerance\": 2e-7,\n    \"minimum_active_n\": 0.05,\n    \"interior_cells\": [\n      63,\n      64,\n      65,\n      74,\n      75,\n      76,\n      123,\n      124\n    ],\n    \"interior_gauss_weight\": 1,\n    \"block_cells\": 2,\n    \"prepared_cache_mib\": 16,\n    \"operator_cache_mib\": 32,\n    \"origin_field\": \"notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz\",\n    \"signed_windows\": [\n      {\n        \"name\": \"mid_positive\",\n        \"sign\": 1,\n        \"breaks\": [\n          0.9,\n          0.915,\n          0.985,\n          0.99\n        ]\n      },\n      {\n        \"name\": \"late_positive\",\n        \"sign\": 1,\n        \"breaks\": [\n          1.423,\n          1.428,\n          1.442,\n          1.445\n        ]\n      }\n    ],\n    \"signed_domain_path\": \"notes/2026-11-12-fd2d-signed-domain-recovery-01-domain.json.gz\",\n    \"signed_qp_path\": \"notes/2026-11-12-fd2d-signed-domain-recovery-01-qp.npz\"\n  },\n  \"input_sha256\": \"b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f\",\n  \"owner\": \"numerical_recovery\",\n  \"source_reconstruction_not_original36_bytes\": true,\n  \"actual_field_changed_by_representation\": true,\n  \"physical_g_unchanged_by_representation\": true,\n  \"new_actual_baseline_and_normal_required\": true,\n  \"old36_partial_normal_not_relabelled\": true,\n  \"new_actual_F_J_evaluations\": 0,\n  \"strong_target_complete\": false,\n  \"recovery_generator\": \"scripts/fd2d-build-signed36-source-recovery.py\"\n}\n",
      "sha256": "0e13a81afb1bb81d423e9f459c58bc13c43845d043313d861f68bf3849d166bd"
    },
    "notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json": {
      "content": "{\n  \"schema\": \"fd2d-unexecuted-explicit-signed-recovery-request-v1\",\n  \"run_prefix\": \"notes/2026-11-12-fd2d-signed36-mid-source-recovery01\",\n  \"cache_dir\": \"notes/2026-11-12-fd2d-signed36-mid-source-recovery01-work\",\n  \"settings\": {\n    \"candidate\": \"notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json\",\n    \"warm_start\": \"notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz\",\n    \"radius_packet\": \"notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json\",\n    \"reference_inlet\": \"notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz\",\n    \"reference_cache\": \"notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz\",\n    \"reference_rim_fraction\": 0.12,\n    \"out_prefix\": \"notes/2026-11-12-fd2d-signed36-mid-source-recovery01\",\n    \"owner_stop_file\": \"notes/2026-11-12-fd2d-signed36-mid-source-recovery01-stop\",\n    \"max_iterations\": 1,\n    \"modes\": 31,\n    \"mesh_step\": 0.04,\n    \"gap\": 0.8,\n    \"central_floor\": 0.1,\n    \"central_cap\": 7.352941176470588,\n    \"profile_box\": 0.08,\n    \"radius_floor\": 0.1,\n    \"curvature_cap\": 8.1,\n    \"curvature_weight\": 1,\n    \"high_gauss_weight\": 1,\n    \"high_codazzi_weight\": 1,\n    \"mesh_relative_tolerance\": 1e-12,\n    \"damping\": 0.00001,\n    \"finite_tolerance\": 2e-7,\n    \"minimum_active_n\": 0.05,\n    \"interior_cells\": [\n      63,\n      64,\n      65,\n      74,\n      75,\n      76,\n      123,\n      124\n    ],\n    \"interior_gauss_weight\": 1,\n    \"block_cells\": 2,\n    \"prepared_cache_mib\": 16,\n    \"operator_cache_mib\": 32,\n    \"origin_field\": \"notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz\",\n    \"signed_windows\": [\n      {\n        \"name\": \"mid_positive\",\n        \"sign\": 1,\n        \"breaks\": [\n          0.9,\n          0.915,\n          0.985,\n          0.99\n        ]\n      }\n    ],\n    \"signed_domain_path\": \"notes/2026-11-12-fd2d-signed-domain-recovery-01-domain.json.gz\",\n    \"signed_qp_path\": \"notes/2026-11-12-fd2d-signed-domain-recovery-01-qp.npz\"\n  },\n  \"input_sha256\": \"b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f\",\n  \"owner\": \"numerical_recovery\",\n  \"source_reconstruction_not_original36_bytes\": true,\n  \"actual_field_changed_by_representation\": true,\n  \"physical_g_unchanged_by_representation\": true,\n  \"new_actual_baseline_and_normal_required\": true,\n  \"old36_partial_normal_not_relabelled\": true,\n  \"new_actual_F_J_evaluations\": 0,\n  \"strong_target_complete\": false,\n  \"recovery_generator\": \"scripts/fd2d-build-signed36-source-recovery.py\"\n}\n",
      "sha256": "6b4b06ac7a9c66a04ba616ded868e3a2b21a6034ef05fd2c50ac0e75d9a19281"
    }
  },
  "dependencies": {
    "scripts/fd2d_gc_signed_trace_problem.py": {
      "git_blob_sha1": "cd34951df353e517f5aa5a8c88e060df382b9712",
      "sha256": "7298d63ef933cfe7f41878a95213db5e19a44ebd3e107429dc43c6015bfd2cd4"
    },
    "scripts/fd2d_gc_signed_trace_windows.py": {
      "git_blob_sha1": "a3e1715dafe619b1111322441d13e34c03fc49e2",
      "sha256": "e8afb39e521c7c8b5324d8c16cc74674f964a991c4d6aec81fac9403a2d8fdd8"
    },
    "scripts/fd2d_gc_signed_trace_cells.py": {
      "git_blob_sha1": "7e441b662da2a08c2ff846f5825594a1a7981fac",
      "sha256": "e5db121fad0f9ad79be9e28eb98dbf0f3bf746e38564d6a7ee04ae0344ea5150"
    },
    "scripts/fd2d_gc_signed_trace_fine_cells.py": {
      "git_blob_sha1": "adcba70688a28a781439fe58e10d878be5d027e5",
      "sha256": "f7a31873b14c512a37d7bcda64531187756ebd5f2a0ec962f86479e0ca6315be"
    },
    "scripts/fd2d_gc_signed_search_domain_recovery.py": {
      "git_blob_sha1": "85638843cc6f33e50f26d9b21550bd504678382e",
      "sha256": "4bd8bdd374ed4280f81f15264510f587ac2af47e2b7e401e71c9ee8c542e6c49"
    },
    "scripts/fd2d_gc_signed_grouped_cells.py": {
      "sha256": "cda8a80e05eaacd1d1f1acfd8ba05d3f34cde404b477fa28e3d45d10edbeca45"
    },
    "scripts/fd2d-gc-signed-stage-normal-tile-batch-v2.py": {
      "sha256": "faa63a5397625af12ce7bad5464a72ddb7a7dddeae5c7a72d3ba2b077d7596be"
    },
    "scripts/fd2d-gc-signed-run-normal-tile-batches-v2.py": {
      "sha256": "ff6bde625fd6a6c8869c3fc70034466659b78000efec6f0f86a9d4239a4cc098"
    },
    "scripts/fd2d-gc-signed-stage-normal-rescue.py": {
      "sha256": "f5cd9bf4b7faf7072c02d442b1b114e066a14a8619b5c27fb39c4bc5754bb342"
    }
  }
}''')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def checked_relative(path):
    value=Path(path)
    if value.is_absolute() or '..' in value.parts:
        raise ValueError('Only explicit topic-relative generated paths are allowed')
    return value


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic-root',type=Path,default=Path(__file__).resolve().parent.parent)
    ap.add_argument('--manifest',type=Path,default=Path(
        'notes/2026-11-12-fd2d-signed36-source-recovery-generated-manifest.json'))
    args=ap.parse_args();root=args.topic_root.resolve()
    source=Path(__file__).resolve()
    plan={};templates=[]
    for rel,expected in PAYLOAD['dependencies'].items():
        data=(root/checked_relative(rel)).read_bytes()
        if sha(data)!=expected['sha256']:
            raise ValueError('A required frozen/current recovery source differs: '+rel)
        if 'git_blob_sha1' in expected and git_blob(data)!=expected['git_blob_sha1']:
            raise ValueError('Git blob identity differs: '+rel)
    for job in PAYLOAD['jobs']:
        rel=checked_relative(job['source']);raw=(root/rel).read_bytes()
        if git_blob(raw)!=job['source_git_blob']:
            raise ValueError('Frozen template differs: '+str(rel))
        text=raw.decode('utf-8')
        for replacement in job['replacements']:
            old,new,count=(replacement[k] for k in ('before','after','count'))
            if text.count(old)!=count:
                raise ValueError('Deterministic replacement count differs: '+str(rel))
            text=text.replace(old,new)
        text=job.get('prefix','')+text+job.get('suffix','')
        data=text.encode('utf-8')
        if sha(data)!=job['output_sha256']:
            raise ValueError('Reconstructed output identity differs: '+job['destination'])
        destination=checked_relative(job['destination'])
        if destination.suffix=='.py':ast.parse(text,filename=str(destination))
        if len(data)>=100_000:raise ValueError('Keep every recovery text source below 100 KB')
        if str(destination) in plan:raise ValueError('Duplicate planned destination')
        plan[str(destination)]=data
        templates.append(dict(path=str(rel),git_blob_sha1=job['source_git_blob'],
            sha256=sha(raw),destination=str(destination),notes=job['notes']))
    for rel,item in PAYLOAD['literals'].items():
        destination=checked_relative(rel);data=item['content'].encode('utf-8')
        if sha(data)!=item['sha256'] or len(data)>=100_000:
            raise ValueError('Literal source/request identity or size differs')
        if destination.suffix=='.py':ast.parse(data.decode(),filename=str(destination))
        if destination.suffix=='.json':json.loads(data)
        if str(destination) in plan:raise ValueError('Duplicate literal destination')
        plan[str(destination)]=data
    # Inspect every destination before writing any. Originals are never
    # overwritten just because an outage made their last status uncertain.
    for rel,data in plan.items():
        path=root/rel
        if path.exists() and path.read_bytes()!=data:
            raise FileExistsError('Original or another version exists; preserve it: '+str(path))
    records=[]
    for rel,data in plan.items():
        path=root/rel;existed=path.exists()
        if not existed:
            path.parent.mkdir(parents=True,exist_ok=True)
            with path.open('xb') as stream:
                stream.write(data);stream.flush();os.fsync(stream.fileno())
        if path.read_bytes()!=data:raise IOError('Generated text did not persist exactly')
        records.append(dict(path=rel,bytes=len(data),sha256=sha(data),
            already_present_identically=existed))
    report=dict(schema=PAYLOAD['schema'],generator=dict(path=str(source),
        bytes=source.stat().st_size,sha256=sha(source.read_bytes())),
        generated_or_reused_files=records,templates=templates,
        all_generated_Python_syntax_parsed=True,
        mathematical_modules_imported=False,actual_F_J_or_solver_evaluations=0,
        source_reconstruction_is_not_original36_byte_recovery=True,
        old_normal_or_value_packet_relabelled=False,
        original_files_overwritten=False,strong_target_complete=False)
    path=root/checked_relative(args.manifest)
    data=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if len(data)>=100_000:raise ValueError('Generated manifest exceeds text limit')
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        old=json.loads(path.read_text())
        # A rerun may report identical files as already present. Do not
        # overwrite the first true execution receipt.
        if [(x['path'],x['sha256']) for x in old['generated_or_reused_files']] != [
                (x['path'],x['sha256']) for x in records]:
            raise ValueError('Existing generation manifest binds different outputs')
    else:
        with path.open('xb') as stream:stream.write(data)
    print(json.dumps(dict(manifest=str(path),files=len(records),
        actual_numerical_evaluations=0,strong_target_complete=False)),flush=True)
    return 0


if __name__=='__main__':
    raise SystemExit(main())
