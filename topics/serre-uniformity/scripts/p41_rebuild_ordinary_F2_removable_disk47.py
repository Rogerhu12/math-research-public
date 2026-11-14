#!/usr/bin/env python3
"""Rebuild an ordinary F2 disk with removable auxiliary T2 denominators."""
import argparse
from pathlib import Path
import subprocess
import sys
import tarfile


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--disk-id',required=True)
    ap.add_argument('--result-id',required=True)
    ap.add_argument('--work-dir',type=Path,required=True)
    args=ap.parse_args()
    scripts=args.script_dir.resolve();data=scripts/'data';work=args.work_dir.resolve()
    disk=args.disk_id
    assert disk.startswith('ORD_j') and disk[5:].isdigit() and len(disk)==7
    work.mkdir(parents=True,exist_ok=True)
    recovery=work/'recovery-inputs'
    def link(source,target):
        source=source.resolve(strict=True);target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() or target.is_symlink():assert target.resolve(strict=True)==source,target
        else:target.symlink_to(source,target_is_directory=source.is_dir())
    for name in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:
        link(data/name,recovery/name)
    link(data/'SS_second_kind_rhs47',recovery/'SS-second-kind-rhs')
    prefix='CM-ordinary-principal-transports' if int(disk[5:]) in [38,39,40] else 'ordinary-principal-transports'
    with tarfile.open(data/f'p41_{disk}_principal_transports47.tar.gz','r:gz') as archive:
        members=archive.getmembers()
        assert len(members)==459
        for member in members:
            pp=Path(member.name)
            assert member.isfile() and not pp.is_absolute() and '..' not in pp.parts
            assert pp.parts[0]==prefix,pp
            assert (len(pp.parts)>=3 and pp.parts[1]==disk) or pp.parts==(prefix,'run_manifest47.json'),pp
            target=work/pp;content=archive.extractfile(member).read()
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==content,target
            else:target.write_bytes(content)
    second=data/f'{disk}_second_kind_complete47.json.gz';principal=data/f'{disk}_actual_principal_function47.json.gz'
    support=data/f'{disk}_actual_T2_support47.json.gz';canonical=data/'p41_canonical_restriction47_candidate1_raw.json.gz'
    norm=work/f'{disk}_actual_F2_first_variable_norm47.json.gz';center=work/f'{disk}_actual_canonical_F2_height47.json.gz'
    def run(script,argv):subprocess.run([sys.executable,'-u',str(scripts/script)]+[str(x) for x in argv],check=True)
    run('p41_ordinary_f2_fixed_norm47.py',['--script-dir',scripts,'--based-points',data/'p41_all19_based_points47.json.gz','--second-kind-certificate',second,'--multiplication',data/f'{disk}_multiply47.json.gz','--transport-directory',work/prefix/disk,'--principal-expression',principal,'--canonical-algebra',canonical,'--ordinary-lifts',data/'p41_ordinary_point_lifts47.json.gz','--t2-norm',data/f'{disk}_actual_T2_principal_norm47.json.gz','--cache-dir',work/'norm-cache','--output',norm])
    run('p41_ordinary_F2_connection_removable47.py',['--script-dir',scripts,'--recovery-dir',recovery,'--disk-id',disk,'--result-id',args.result_id,'--second-kind',second,'--principal',principal,'--t2-support',support,'--full-norm',norm,'--canonical',canonical,'--work-dir',work/'connection','--output',center])
    run('p41_generic_ordinary_F2_local_polynomial47.py',['--script-dir',scripts,'--disk-id',disk,'--result-id',args.result_id,'--center',center,'--abel',data/f'{disk}_Abel47.json.gz','--multiply',data/f'{disk}_multiply47.json.gz','--tiny',data/'p41_all129_second_kind_tiny47_complete.json.gz','--work-dir',work/'polynomial','--output',work/f'{disk}_actual_canonical_F2_polynomial47.json.gz'])


if __name__=='__main__':main()
