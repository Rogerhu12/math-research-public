#!/usr/bin/env python3
"""Complete R270 affine condensation for a noncontiguous whole-node support.

Only public Actions performs scientific arithmetic. The caller retains the
exact actual B support, not a padded zero-B layout. The unchanged original
library first constructs the full physical cover front, including every
free core, global control and affine column. Missing interior physical
columns are moved first and genuinely eliminated by the original complete
orthogonal-prefix routine. The remaining front then follows the unchanged
109-core elimination, local root, inverse and full-H recovery methods.

In exact arithmetic this is conditional minimization, not deletion of
original rows/columns. Binary64 operations have a new declared order; no
word equality or rigorous original-H certificate is asserted. All original
same-A readbacks and nonlinear decisions remain downstream.
"""
from __future__ import annotations

from pathlib import Path
import time

import numpy as np

import root_20261114_complete_local_qp_condensation as original

HERE = Path(__file__).resolve().parent
ORIGINAL_NAME = "root_20261114_complete_local_qp_condensation.py"
ORIGINAL_SHA = "84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b"
SCHEMA = "complete-original-H-noncontiguous-support-affine-square-root-condensation-v1"
CondensationDeadline = original.CondensationDeadline
CondensationFailure = original.CondensationFailure


class CondensedModel(original.CondensedModel):
    """Whole original physical blocks plus all controls; every other column free."""

    def __init__(self, factor, original_g, local_indices, *,
                 deadline, output_directory=None):
        original.require_actions()
        if original.file_sha(HERE/ORIGINAL_NAME) != ORIGINAL_SHA:
            raise ValueError("Keep the frozen original complete affine condensation")
        super().__init__(factor, original_g, local_indices,
            deadline=deadline, output_directory=output_directory)
        # Cover dimensions were used only to form the original central front.
        # After its complete gap elimination the live dimensions are actual.
        self._report.update(
            schema=SCHEMA, source_sha256=original.file_sha(__file__),
            original_condensation_source_sha256=ORIGINAL_SHA,
            retained_physical_nodes=len(self.actual_support_nodes),
            actual_retained_physical_nodes=list(self.actual_support_nodes),
            internal_contiguous_cover_node_count=self.cover_retained,
            internal_cover_central_dimension=self.cover_central_size,
            actual_post_gap_central_dimension=self.central_size,
            internal_missing_physical_nodes=list(self.gap_nodes),
            internal_gap_columns_are_eliminated_not_retained_B_columns=True,
            complete_B_local_support_not_padded=True,
            inherited_complete_affine_and_recovery_methods_unchanged=True,
            original_A_AT_recovery_includes_every_missing_physical_node=True,
            missing_node_full_recovery_rhs_is_original_negative_g=True,
            no_missing_node_value_or_gradient_forced_to_zero=True,
            same_exact_conditional_quadratic_only_not_same_binary64_order=True)
        self._write_status()

    def _bind_support(self, local_indices):
        source=np.asarray(local_indices)
        if source.ndim != 1 or source.dtype.kind not in ("i","u"):
            raise ValueError("A complete integer vector of actual B coordinates is required")
        idx=np.asarray(source,dtype=np.int64)
        if (not idx.size or np.any(idx<0) or np.any(idx>=self.size)
                or np.any(idx[1:]<=idx[:-1])):
            raise ValueError("Actual B coordinates must be unique and ascending")
        physical=idx[idx<self.physical]
        controls=idx[idx>=self.physical]
        expected_controls=np.arange(self.physical+self.free,self.size,dtype=np.int64)
        if (not physical.size or physical.size%self.n
                or not np.array_equal(controls,expected_controls)):
            raise ValueError("Retain whole physical nodes and every global control, not free core")
        blocks=physical.reshape(-1,self.n)
        nodes=blocks[:,0]//self.n
        expected=nodes[:,None]*self.n+np.arange(self.n,dtype=np.int64)[None,:]
        if not np.array_equal(blocks,expected):
            raise ValueError("The actual local support contains a partial physical node")
        first,last=int(physical[0]),int(physical[-1])
        cover=np.concatenate((np.arange(first,last+1,dtype=np.int64),expected_controls))
        # The original binder is applied to its honest INTERNAL cover.
        # Its cover left/right/retained/central_size remain used by the
        # original reverse fronts and central-front construction.
        original.CondensedModel._bind_support(self,cover)
        self.cover_retained=self.retained
        self.cover_central_size=self.central_size
        self.internal_cover_indices=cover.copy()
        self.internal_cover_indices.flags.writeable=False
        self.actual_support_nodes=tuple(int(value)+1 for value in nodes)
        cover_nodes=range(self.left,self.right+1)
        kept=set(int(value) for value in nodes)
        self.gap_nodes=tuple(value+1 for value in cover_nodes if value not in kept)
        gap_columns=np.concatenate([
            np.arange(self.free+(node-1-self.left)*self.n,
                self.free+(node-self.left)*self.n,dtype=np.int64)
            for node in self.gap_nodes]) if self.gap_nodes else np.empty(0,dtype=np.int64)
        central_columns=np.arange(self.central_size,dtype=np.int64)
        keep=np.ones(self.central_size,dtype=bool)
        keep[gap_columns]=False
        remaining=central_columns[keep]
        # Remaining order is original free core, exact selected physical
        # nodes, all controls. The original constructor subsequently
        # eliminates its unchanged self.free leading core columns.
        expected_remaining=np.concatenate((
            np.arange(self.free,dtype=np.int64),
            np.concatenate([np.arange(self.free+(int(node)-self.left)*self.n,
                self.free+(int(node)-self.left+1)*self.n,dtype=np.int64) for node in nodes]),
            np.arange(self.free+self.retained*self.n,self.central_size,dtype=np.int64)))
        if not np.array_equal(remaining,expected_remaining):
            raise ValueError("The full affine remaining-column order changed")
        self.gap_front_columns=gap_columns
        self.front_permutation=np.concatenate((gap_columns,remaining))
        if (len(self.front_permutation)!=self.central_size
                or not np.array_equal(np.sort(self.front_permutation),central_columns)):
            raise ValueError("Every original central column must occur exactly once")
        self.local_indices=idx.copy()
        self.local_indices.flags.writeable=False
        self.local_size=len(idx)
        self._report.update(schema=SCHEMA,source_sha256=original.file_sha(__file__),
            original_condensation_source_sha256=ORIGINAL_SHA,
            actual_query_support_nodes=list(self.actual_support_nodes),
            internal_cover_nodes=[value+1 for value in cover_nodes],
            missing_physical_nodes=list(self.gap_nodes),
            missing_physical_coordinate_count=len(gap_columns),
            actual_local_coordinate_count=self.local_size,
            internal_cover_local_coordinate_count=len(cover),
            internal_cover_central_dimension=self.cover_central_size,
            actual_post_gap_central_dimension=self.free+self.local_size,
            exact_actual_local_indices=original.identity(self.local_indices),
            internal_cover_indices=original.identity(self.internal_cover_indices),
            internal_cover_is_not_a_B_local_layout=True,
            missing_interior_variables_not_zeroed=True,
            no_full_J_or_complete_factor_recomputed=True)

    def _central_front(self, affine, U, V, last_affine):
        # This entire original front includes the pure-global root rows
        # and its complete affine column before any additional rotation.
        front=original.CondensedModel._central_front(self,affine,U,V,last_affine)
        self._report["original_internal_cover_affine_front"]=original.identity(front)
        self._report["original_internal_cover_central_order"]=dict(self._report["central_order"])
        self._report["memory_budget"].update(
            gap_permutation_front_bytes=int(front.nbytes),
            gap_QR_input_copy_bytes=int(front.nbytes),
            post_gap_affine_front_bytes=(self.free+self.local_size)*(self.free+self.local_size+1)*8,
            original_QR_workspace_trailing_rotations_and_transient_copies_additional=True,
            no_completion_or_runtime_speedup_guaranteed=True)
        self._save_array("internal-contiguous-cover-indices",self.internal_cover_indices,
            "Internal elimination cover only; not the actual B local coordinate list")
        self._save_array("missing-interior-front-columns",self.gap_front_columns,
            "Actual free physical columns orthogonally eliminated before the original free core")
        self._save_array("complete-front-column-permutation",self.front_permutation,
            "Permutation of ALL variable columns; the original affine column remains last")
        count=len(self.gap_front_columns)
        if not count:
            self._report["interior_gap_elimination"]=dict(
                required=False,eliminated_columns=0,complete=True,
                original_full_affine_front_returned_unchanged=True)
            return front
        self._check_deadline()
        started=time.monotonic()
        ordered=np.empty(front.shape,dtype="<f8",order="F")
        # Explicit column copies preserve the recorded binary64 words and
        # avoid building a second advanced-indexing temporary of full size.
        for target,source in enumerate(self.front_permutation):
            ordered[:,target]=front[:,source]
        ordered[:,-1]=front[:,-1]
        del front
        permuted_identity=original.identity(ordered)
        # This frozen routine QR-factorizes the first count columns and
        # applies the same Q.T to EVERY remaining variable and affine column.
        rotated=self._qr_prefix(ordered,count,"actual-missing-interior-physical-columns")
        del ordered
        eliminated_diagonal=np.diag(rotated[:count,:count])
        if np.any(eliminated_diagonal==0):
            raise FloatingPointError("A required original gap QR diagonal is zero")
        # These are the remaining orthogonal residual rows AFTER the full
        # rotation. Original unrotated rows or affine terms are never dropped.
        remainder=np.array(rotated[count:,count:],dtype="<f8",order="F",copy=True)
        report=dict(required=True,complete=True,eliminated_columns=count,
            eliminated_physical_nodes=list(self.gap_nodes),
            full_permuted_affine_front=permuted_identity,
            eliminated_upper_diagonal=original.identity(eliminated_diagonal),
            eliminated_upper_diagonal_min_abs=float(np.min(np.abs(eliminated_diagonal))),
            remaining_affine_front=original.identity(remainder),
            remaining_rows=int(remainder.shape[0]),
            remaining_variable_columns=int(remainder.shape[1]-1),
            remaining_order="original free core, actual B physical nodes, every global control, affine",
            pure_global_and_affine_columns_undergo_the_same_orthogonal_action=True,
            no_original_unrotated_row_deleted=True,
            removed_leading_square_has_an_unconstrained_conditional_minimizer=True,
            original_f0_minus_complete_affine_half_norm_constant_unchanged=True,
            all_remaining_pure_constant_rows_kept=True,
            whole_original_g_and_all_exterior_gradients_retained=True,
            original_complete_H_recovery_still_used=True,
            new_numerical_rounding_order_not_an_exact_original_H_certificate=True,
            seconds=time.monotonic()-started,
            crossed_deadline_for_started_complete_QR=bool(time.monotonic()>=self.deadline))
        del rotated
        self._report["interior_gap_elimination"]=report
        self._event("missing-interior-physical-columns-eliminated",**report)
        expected=self.free+self.local_size
        if remainder.shape!=(expected,expected+1) or not np.isfinite(remainder).all():
            raise FloatingPointError("The complete post-gap affine front has the wrong finite dimension")
        # Cover allocation is finished. The live central dimensions now
        # describe the exact actual support, not a padded B layout.
        self.retained=len(self.actual_support_nodes)
        self.central_size=expected
        self._report["central_order"]=dict(
            rows="all remaining orthogonal residual rows after the complete gap prefix",
            columns="all original free core, actual B physical nodes, all controls, affine",
            pure_global_affine_kept=True,core_eliminated=self.free,
            local_retained=self.local_size,central_dimension=self.central_size,
            no_exterior_coordinate_was_set_to_zero=True)
        # The unchanged constructor now performs its original free-core
        # prefix elimination and full local QR on this complete remainder.
        return remainder
