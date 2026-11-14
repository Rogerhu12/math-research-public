"""New recovery source for the R181 B32 complete round reference.

This reconstructs the documented mathematical entry from published inputs.
It does NOT claim the SHA or execution receipt of the unavailable 87bde
closed source.  Its local jet formula is inherited from the frozen R166
reader after checking that source; all candidate data are newly resolved.
"""
from __future__ import annotations
from pathlib import Path
import json
from fd2d_frozen_ellipse_candidate import Candidate
from fd2d_gc_archive_arrays import identity
from fd2d_gc_whole_round_reference import FrozenRoundPrefixReference

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
DEFAULT_CANDIDATE=ROOT/'notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json'
CANDIDATE_SHA256='9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d'
ROUND_FORMULA_SHA256='b98a1c32b1e28dc1158803892443f415772a78a3ce397a67038a46e71513ffa7'
RADIUS_READER_SHA256='393848295e1d8e321c057286d722f47a6c51665aa1a35f4b3bbed3a63ddeac30'


def checked_candidate(path=DEFAULT_CANDIDATE):
    path=Path(path)
    if identity(path)['sha256']!=CANDIDATE_SHA256:
        raise ValueError('This new entry binds the exact R181 B32 candidate')
    bundle=json.loads(path.read_text())
    d=bundle.get('shorter_design_definition',{})
    if (d.get('family')!='B_standard_cut' or d.get('cylinder_exact')!='13/128'
            or d.get('cut_radius_exact')!='4/5'
            or d.get('redeepen_rate_exact')!='9/2'
            or not d.get('removed_outward_spacer')
            or bundle['segments'][-1].get('exact_endpoint_phase')!='-pi/2'):
        raise ValueError('Wrong explicit new physical profile')
    return bundle


class R181BRecoveryRoundReference(FrozenRoundPrefixReference):
    def __init__(self,candidate=DEFAULT_CANDIDATE):
        import fd2d_frozen_ellipse_candidate as numeric
        import fd2d_gc_whole_round_reference as formula
        if identity(numeric.__file__)['sha256']!=RADIUS_READER_SHA256:
            raise ValueError('The declared floating radius evaluator differs')
        if identity(formula.__file__)['sha256']!=ROUND_FORMULA_SHA256:
            raise ValueError('The inherited local round jet formula differs')
        self.source=Path(candidate);bundle=checked_candidate(candidate)
        self.base=Candidate(bundle)
        self.a0,self.end=self.base.a0,self.base.end
        self.breaks=self.base.breaks.copy();self.cut_radius=4/5
        final=self.base.segments[-1]
        if (final['kind']!='phase_bridge' or final['ps0']!=0
                or final['ps1']!=0 or bundle['cut']['a_prime']!=-1
                or bundle['cut']['a_second']!=0):
            raise ValueError('Exact flat final phase and derivative required')

    def definition(self):
        return dict(schema='fd2d-R181-B32-recovery-whole-round-reference-v1',
            source=identity(__file__),candidate=identity(self.source),
            inherited_local_formula_sha256=ROUND_FORMULA_SHA256,
            numeric_radius_evaluator_sha256=RADIUS_READER_SHA256,
            mathematical_definition='New R181 B32 a; S0=(cos(phi)/a,0,-phi_s)',
            component_order=['n','m','l'],physical_endpoint_binary64=self.end,
            exact_cut=['4/5','-1','0'],exact_cut_II=['0','0','0'],
            cut_ds='prefix left trace; not asserted equal to flat tail derivative',
            angular_derivatives='zero complete functions',
            target_parameter_derivatives='zero; full delta forcing retained separately',
            inherited_old_candidate_or_old_arrays=False,
            previous_closed_source_byte_identity_claimed=False,
            interval_certificate=False)
