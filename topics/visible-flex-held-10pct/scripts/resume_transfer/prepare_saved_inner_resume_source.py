#!/usr/bin/env python3
"""Make an owned resume entry with only state-loading/diagnostic hooks.

The original equations, solve_bvp options, boundary checks, C2 exporter and
metric/seam audit stay unchanged. This preparer performs no solve.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


DIAGNOSTICS = '''def restored_solution_message(sol):
    return None if hasattr(sol,'recorded_raw_max_rms') else sol.message


def restored_solution_max_rms(sol):
    if hasattr(sol,'recorded_raw_max_rms'):return sol.recorded_raw_max_rms
    return float(np.max(sol.rms_residuals))


def restored_solution_diagnostics(sol):
    restored=hasattr(sol,'recorded_raw_max_rms')
    return dict(final_solution_is_restored_raw_inner=restored,
        message_provenance='not_saved_in_original_inner'if restored else'new_actual_solve_bvp',
        rms_provenance='recorded_original_maximum_only'if restored else'new_actual_solve_bvp_vector',
        original_interval_rms_reconstructed=False,
        prior_domain_newton_counters_available=False,
        current_domain_newton_counter_scope='This resume process only',
        input_resume_provenance=RESUME_CONTEXT.provenance())


'''


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--owned-topic',type=Path,required=True)
    p.add_argument('--manifest',type=Path,required=True)
    a=p.parse_args()
    source,dest,manifest=a.source_topic.resolve(),a.owned_topic.resolve(),a.manifest.resolve()
    if dest.exists() or manifest.exists():raise FileExistsError('Use new owned output paths')
    if source==dest or source in dest.parents:raise ValueError('Do not modify the source tree')
    original=source/'scripts/db6f-prefix-coupled.py';before=original.read_text()
    old_restart="""    restart_info=None
    if a.preserve_restart_mesh:
        initializer=module('db6f_preserve_restart',S/'db6f-prefix-preserve-restart.py')
        x,y,par,restart_info=initializer.restart(o,a.restart,chart)
    else:x,y,par=o.restart(a.restart)
"""
    new_restart="""    x,y,par,restart_info=RESUME_CONTEXT.restore_inputs(o,a)
"""
    old_diagnostics='message=sol.message,max_rms_collocation_residual=float(np.max(sol.rms_residuals))'
    new_diagnostics='message=restored_solution_message(sol),max_rms_collocation_residual=restored_solution_max_rms(sol)'
    marker="        out['restart_mesh_diagnostics']=restart_info\n"
    with_metadata=marker+"        out['saved_inner_resume_diagnostics']=restored_solution_diagnostics(sol)\n"
    replacements=[(old_restart,new_restart),(old_diagnostics,new_diagnostics),(marker,with_metadata)]
    text=before
    for old,new in replacements:
        if text.count(old)!=1:raise ValueError('Expected original resume boundary changed')
        text=text.replace(old,new)
    if text.count('def main():\n')!=1:raise ValueError('Expected one original main entry')
    text=text.replace('def main():\n',DIAGNOSTICS+'def main():\n')
    reverse=text.replace(DIAGNOSTICS,'')
    for old,new in reversed(replacements):reverse=reverse.replace(new,old)
    if reverse!=before:raise AssertionError('Resume source changed an original mathematical expression')
    dest.mkdir(parents=True);scripts=dest/'scripts';scripts.mkdir()
    for item in source.iterdir():
        if item.name!='scripts':(dest/item.name).symlink_to(item.resolve(),target_is_directory=item.is_dir())
    for item in (source/'scripts').iterdir():
        if item.name!='db6f-prefix-coupled.py':
            (scripts/item.name).symlink_to(item.resolve(),target_is_directory=item.is_dir())
    output=scripts/'db6f-prefix-coupled.py'
    compile(text,str(output),'exec');output.write_text(text)
    if sha(original)!=hashlib.sha256(before.encode()).hexdigest():raise AssertionError('Original changed')
    record=dict(scope=__doc__,command=[sys.executable,*sys.argv],original_topic=str(source),owned_topic=str(dest),
        original_coupler=dict(path=str(original),sha256=sha(original)),
        owned_coupler=dict(path=str(output),sha256=sha(output)),
        preparer_sha256=sha(__file__),reverse_patch_restores_original_bytes=True,
        literal_replacements=replacements,diagnostic_helpers=DIAGNOSTICS,
        runtime_source_root_unchanged=(source/'repro/source-root').resolve()==(dest/'repro/source-root').resolve(),
        original_solver_invoked=False,
        scope_of_runtime_driver='An independent runner restores the saved original inner and resumes the original post-tail boundary check; no original warmup/restart/inner0 is called.')
    with manifest.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
    print(json.dumps(dict(manifest=str(manifest),sha256=sha(manifest),solver_invoked=False)))


if __name__=='__main__':main()
