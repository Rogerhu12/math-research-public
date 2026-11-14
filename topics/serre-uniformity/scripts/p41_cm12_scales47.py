#!/usr/bin/env python3
"""Exact KS and canonical collision-unit data appended to verified CM12 jets."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path
from verify_p41_cm12_hecke47 import add,mul,power

def kodaira_spencer_scales(folder,cm3,cert):
    # All polynomials below are in v=r^3.  A=(-v-1)/r and
    # A'=(-11v+4)/r, B'=8-14v.  Clearing r^3 gives both discriminants.
    source_D=add([4*x for x in power([-1,-1],3)],[0,27])
    target_D=add([4*x for x in power([4,-11],3)],mul([0,27],power([8,-14],2)))
    assert source_D==[-x for x in mul([4,1],power([-1,2],2))]
    assert target_D==[-16*x for x in mul(power([4,1],2),[-1,2])]
    # r^2(9 B' dA'/dr-6 A' dB'/dr)=-72(v+4).
    target_numerator=add([9*x for x in mul([8,-14],[-4,-22])],[-6*x for x in mul([4,-11],[0,-42])])
    assert target_numerator==[-288,-72]
    # Thus beta_target=9r/[4(v+4)(2v-1)] dr=beta_source/2.
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    raw=(folder/'data/p41_cusp_divisors47_certificate.json.gz').read_bytes()
    canonical=json.loads(gzip.decompress(raw))
    K=r.from_json(kernel(73,canonical['cusp_rank_columns_1based'],canonical['cusp_free_columns_1based'],canonical['canonical_kernel_block']))
    fc=r.mm(K,r.column(canonical['canonical_coefficients']))
    source_value=r.mm(r.from_json([cm3['coarse_evaluation_coefficients'][0]]),fc)
    target_value=r.mm(r.from_json([cert['weight2_evaluation_coefficients'][0]]),fc)
    ab=tuple(x*pow(4608,-1,r.Q)%r.Q for x in source_value)
    au=tuple(x*pow(-1425600,-1,r.Q)%r.Q for x in target_value)
    ratio=r.mul(ab,r.inverse_values(au))
    assert r.units(ab)[0,0] and r.units(au)[0,0]
    assert r.to_json(ab)==[[[3204218,0]]] and r.to_json(au)==[[[2742476,0]]]
    assert r.to_json(ratio)==[[[1525119,0]]]
    return {'source_discriminant_numerator_in_r_cubed':source_D,
            'target_discriminant_numerator_in_r_cubed':target_D,
            'target_KS_numerator_times_r_squared':target_numerator,
            'beta_target_over_beta_source':[1,2],
            'beta_target_in_A_at_zero':[1,12],
            'beta_target_in_j_at_zero':[-1,1425600],
            'source_coarse_weight2_to_dj_factor':[1,4608],
            'coarse_source_parameter_leading_in_target_j':[-1,118800**3],
            'coarse_source_parameter_leading_mod47four':pow(-118800,-3,r.Q),
            'coarse_source_parameter_leading_mod47':pow(-118800,-3,47),
            'canonical_source_sha256':hashlib.sha256(raw).hexdigest(),
            'canonical_source_coarse_weight2_value':r.to_json(source_value),
            'canonical_target_weight2_value':r.to_json(target_value),
            'canonical_source_dj_value':r.to_json(ab),'canonical_target_dj_value':r.to_json(au),
            'canonical_dj_value_ratio':r.to_json(ratio)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_cm12_hecke47_verified.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm12_scales47_certificate.json'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    raw=args.input.read_bytes();cert=json.loads(gzip.decompress(raw))
    assert 'all73 actual jets' in cert['status'] and 'PASS' in cert['status']
    cmraw=(folder/'data/p41_cm3_makdisi47_certificate.json').read_bytes();cm3=json.loads(cmraw)
    assert hashlib.sha256(cmraw).hexdigest()==cert['source_sha256']['p41_cm3_makdisi47_certificate.json']
    data=kodaira_spencer_scales(folder,cm3,cert)
    data.update({'level':41,'auxiliary_prime':47,'precision':4,'verified_CM12_source_sha256':hashlib.sha256(raw).hexdigest(),
                 'source_sha256':{Path(__file__).name:hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                 'status':'exact integer KS identities and both fixed canonical differential unit values PASS; relies on the separately completed all73-jet independent certificate'})
    out=json.dumps(data,sort_keys=True,indent=2).encode()+b'\n';args.output.write_bytes(out)
    print('ACTUAL CM12 KS AND COLLISION UNITS PASS',len(out),hashlib.sha256(out).hexdigest())

if __name__=='__main__':main()
