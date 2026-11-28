#!/usr/bin/env python3
"""Complete-row QR/SVD for Newton residual and actual path predictor together.

This is the unchanged R613 full-row construction with TWO explicit right
hand sides.  No J row, parameter or singular direction is removed.  The
second right hand side is the actual external-P derivative, not a probe.
The same one small-factor SVD supplies Newton and regularized predictor.
"""
from collections import defaultdict
import numpy as np

COUNTS = defaultdict(int)


class CompleteTwoRHSFactor:
    @classmethod
    def from_complete_row_passes(cls, rows, columns, make_blocks, *, batch_rows=4096, deadline_check=None):
        """Two real complete passes when storing J would exceed memory.

        make_blocks(pass_number) yields (first_row, Jblock, residualblock,
        pathblock), in the original order, with every original row exactly
        once. Both analytic J passes are charged; neither is a saved factor.
        The first pass gives exactly the full column scaling of __init__.
        The second applies the identical scaled augmented QR construction.
        """
        if rows < columns+2 or batch_rows < columns+2:
            raise ValueError('complete tall streamed two-RHS range required')
        self = cls.__new__(cls)
        check = (lambda: None) if deadline_check is None else deadline_check
        self.shape, self.batch_rows = (int(rows), int(columns)), int(batch_rows)
        norms, rhsnorm = np.zeros(columns), np.zeros(2)
        for which in (0, 1):
            seen, reduced = 0, None
            for first, block, residual, path in make_blocks(which):
                check()
                if (first != seen or block.ndim != 2 or block.shape[1] != columns
                        or residual.shape != (len(block),) or path.shape != (len(block),)
                        or len(block) == 0 or len(block) > batch_rows):
                    raise ValueError('a declared original Jacobian row block was changed or omitted')
                seen += len(block)
                if not np.all(np.isfinite(block)):
                    raise ArithmeticError('nonfinite complete streamed J block')
                COUNTS['streamed_original_J_entries_really_computed'] += int(block.size)
                if which == 0:
                    norms = np.hypot(norms, np.linalg.norm(block, axis=0))
                    rhsnorm = np.hypot(rhsnorm, [np.linalg.norm(residual), np.linalg.norm(path)])
                    COUNTS['column_norm_rows'] += len(block)
                else:
                    old = 0 if reduced is None else len(reduced)
                    augmented = np.empty((old+len(block), columns+2))
                    if old:
                        augmented[:old] = reduced
                    augmented[old:, :columns] = block/self.scales
                    augmented[old:, columns], augmented[old:, columns+1] = residual, path
                    reduced = np.linalg.qr(augmented, mode='r')
                    COUNTS['complete_two_rhs_QR_blocks'] += 1
                    COUNTS['new_original_rows_reduced'] += len(block)
                    COUNTS['including_previous_R_rows_processed'] += len(augmented)
            if seen != rows:
                raise ValueError('not every original complete J row was consumed')
            COUNTS['complete_analytic_J_passes_for_streamed_factor'] += 1
            if which == 0:
                if not np.all(np.isfinite(norms)):
                    raise ArithmeticError('nonfinite streamed complete column norms')
                self.column_norms, self.scales = norms, np.maximum(norms, 1e-12)
        if reduced.shape != (columns+2, columns+2) or not np.all(np.isfinite(reduced)):
            raise ArithmeticError('invalid complete streamed two-RHS factor')
        check()
        self.R, self.C = reduced[:columns, :columns].copy(), reduced[:columns, columns:].copy()
        self.orthogonal_residual_norms = np.linalg.norm(reduced[columns:, columns:], axis=0)
        self.U, self.s, self.Vt = np.linalg.svd(self.R, full_matrices=False)
        self.UtC = self.U.T@self.C
        self.threshold = max(rows, columns)*np.finfo(float).eps*self.s[0]
        self.original_residual_norms = rhsnorm
        if not np.all(np.isfinite(self.s)):
            raise ArithmeticError('nonfinite complete streamed spectrum')
        COUNTS['complete_J_factorizations'] += 1
        COUNTS['small_factor_SVDs'] += 1
        COUNTS['original_J_entries_consumed'] += rows*columns
        COUNTS['actual_right_hand_side_entries_consumed'] += 2*rows
        return self

    def __init__(self, J, residual, path_derivative, *, batch_rows=4096, deadline_check=None):
        if (J.ndim != 2 or residual.ndim != 1 or path_derivative.ndim != 1
                or len(residual) != J.shape[0] or len(path_derivative) != J.shape[0]):
            raise ValueError('complete J and both actual right hand sides are required')
        m, n = J.shape
        if m < n+2 or batch_rows < n+2:
            raise ValueError('the declared complete tall two-RHS QR range is invalid')
        check = (lambda: None) if deadline_check is None else deadline_check
        self.shape, self.batch_rows = (m, n), int(batch_rows)
        norms = np.zeros(n)
        for first in range(0, m, self.batch_rows):
            check(); block = J[first:first+self.batch_rows]
            norms = np.hypot(norms, np.linalg.norm(block, axis=0))
            COUNTS['column_norm_rows'] += len(block)
        if not np.all(np.isfinite(norms)):
            raise ArithmeticError('nonfinite complete new-design column norms')
        self.column_norms, self.scales = norms, np.maximum(norms, 1e-12)
        reduced = None
        for first in range(0, m, self.batch_rows):
            check(); last = min(m, first+self.batch_rows)
            old = 0 if reduced is None else len(reduced)
            augmented = np.empty((old+last-first, n+2))
            if old:
                augmented[:old] = reduced
            augmented[old:, :n] = J[first:last]/self.scales
            augmented[old:, n] = residual[first:last]
            augmented[old:, n+1] = path_derivative[first:last]
            reduced = np.linalg.qr(augmented, mode='r')
            COUNTS['complete_two_rhs_QR_blocks'] += 1
            COUNTS['new_original_rows_reduced'] += last-first
            COUNTS['including_previous_R_rows_processed'] += len(augmented)
        check()
        if reduced.shape != (n+2, n+2) or not np.all(np.isfinite(reduced)):
            raise ArithmeticError('invalid complete two-RHS factor')
        self.R, self.C = reduced[:n, :n].copy(), reduced[:n, n:].copy()
        self.orthogonal_residual_norms = np.linalg.norm(reduced[n:, n:], axis=0)
        self.U, self.s, self.Vt = np.linalg.svd(self.R, full_matrices=False)
        self.UtC = self.U.T@self.C
        self.threshold = max(m, n)*np.finfo(float).eps*self.s[0]
        self.original_residual_norms = np.asarray([np.linalg.norm(residual), np.linalg.norm(path_derivative)])
        if not np.all(np.isfinite(self.s)):
            raise ArithmeticError('nonfinite actual complete spectrum')
        COUNTS['complete_J_factorizations'] += 1
        COUNTS['small_factor_SVDs'] += 1
        COUNTS['original_J_entries_consumed'] += m*n
        COUNTS['actual_right_hand_side_entries_consumed'] += 2*m

    def direction(self, damping, *, rhs=0):
        if not np.isfinite(damping) or damping <= 0 or rhs not in (0, 1):
            raise ValueError('positive damping and actual Newton/path right hand side required')
        COUNTS['complete_singular_direction_solves'] += 1
        return -(self.Vt.T@(self.s/(self.s*self.s+damping)*self.UtC[:, rhs]))/self.scales

    def predicted_decrease(self, direction, fraction=1., *, rhs=0):
        value = self.R@(self.scales*np.asarray(direction)*fraction)
        return float(-self.C[:, rhs]@value-.5*(value@value))

    def residual_norm_after_direction(self, direction, *, rhs=0):
        value = self.R@(self.scales*np.asarray(direction))+self.C[:, rhs]
        return float(np.hypot(np.linalg.norm(value), self.orthogonal_residual_norms[rhs]))

    def spectrum(self):
        return {'singular_max': float(self.s[0]), 'singular_min': float(self.s[-1]),
            'reported_rank': int(np.sum(self.s > self.threshold)), 'rank_threshold': float(self.threshold),
            'column_norm_min': float(np.min(self.column_norms)), 'column_norm_max': float(np.max(self.column_norms)),
            'columns_below_scale_floor': int(np.sum(self.column_norms < 1e-12)),
            'actual_output_rows': self.shape[0], 'actual_columns': self.shape[1], 'QR_batch_rows': self.batch_rows,
            'original_Newton_and_path_rhs_norms': self.original_residual_norms.tolist(),
            'orthogonal_Newton_and_path_rhs_norms': self.orthogonal_residual_norms.tolist(),
            'all_rows_columns_and_singular_directions_retained': True,
            'same_one_factorization_for_actual_Newton_and_actual_path_predictor': True,
            'normal_equations_or_inverse_certificate': False}
