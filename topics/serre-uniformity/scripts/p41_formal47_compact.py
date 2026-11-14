#!/usr/bin/env python3
"""Persist final actual logarithms, hashes and zero-test metadata without raw charts."""
import argparse,gzip,hashlib,json
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--raw-log',type=Path,default=Path('/tmp/p41_formal47_log_certificate.json.gz'))
    parser.add_argument('--point',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();folder=args.script_dir.resolve()
    pointpath=args.point or folder/'data/p41_formal47_multiplication_saved.json.gz'
    raw=args.raw_log.read_bytes();point_raw=pointpath.read_bytes()
    data=json.loads(gzip.decompress(raw));point=json.loads(gzip.decompress(point_raw))
    assert data['multiplication_sha256']==hashlib.sha256(point_raw).hexdigest()
    assert point['bits_done']==point['target_bits']==304 and len(point['steps'])==454
    assert point['target_multiplier']==point['magnitude']==data['formal_input_multiplier']
    assert point['point_sha256']==data['formal_input_point_sha256']
    assert data['zero_test_mod47']==point['zero_test_mod47'] and point['sign']==data['formal_input_sign']==1
    z=data['log_of_B_minus4'];assert len(z)==1 and len(z[0])==54
    assert all(a%47==b%47==0 for a,b in z[0])
    assert all(a//47%47 or b//47%47 for a,b in z[0])
    keep=['level','auxiliary_prime','precision','modulus','source_sha256','algorithm_sha256',
          'calibration_source','calibration_sha256','formal_input_sign','formal_input_multiplier',
          'formal_input_point_sha256','zero_test_mod47','selected_Lie_coordinates',
          'log_of_signed_multiple','log_of_B_minus4','nonzero_coordinate_indices_1based','differential_basis','status']
    summary={k:data[k] for k in keep}
    summary['format']='compact final logarithms; raw group/chart witnesses reproducible'
    summary['multiplication_source']='p41_formal47_multiplication_saved.json.gz'
    summary['multiplication_sha256']=hashlib.sha256(point_raw).hexdigest()
    summary['raw_log_sha256']=hashlib.sha256(raw).hexdigest()
    summary['log_algorithm_sha256']=hashlib.sha256((folder/'p41_formal47_log.py').read_bytes()).hexdigest()
    summary['bits_done']=304;summary['number_of_AddFlip_operations']=454
    summary['log_of_B_divided47_mod47']=[[a//47%47,b//47%47] for a,b in z[0]]
    encoded=(json.dumps(summary,sort_keys=True,separators=(',',':'))+'\n').encode();packed=gzip.compress(encoded,mtime=0)
    out=args.output or folder/'data/p41_formal47_log_compact.json.gz';out.write_bytes(packed)
    print('Final actual log compact:',out,len(packed),'bytes; SHA256',hashlib.sha256(packed).hexdigest(),flush=True)


if __name__=='__main__':main()
