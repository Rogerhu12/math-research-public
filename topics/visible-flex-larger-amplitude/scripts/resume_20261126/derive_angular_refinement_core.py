#!/usr/bin/env python3
"""Pure source construction of the N2048->4096 observer family; no science imports."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PINS = {
 'so3_supported_smooth_triangle_meridian_operator.py':'6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',
 'so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py':'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd',
 'reference_centred_c1_smooth_triangle_calibration.py':'3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991',
 'normal_frame_c1_reuse.py':'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9',
 'supported_smooth_triangle_literal_zero_moment_input.py':'307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7',
}
BASE_SCHEMA='complete-angular-refined-supported-smooth-triangle-reference-so3-meridian-v1'
NORMAL_SCHEMA='complete-angular-refined-reference-centred-C1-fixed-normal-plane-SO3-v1'
BINDER_SCHEMA='angular-refined-supported-smooth-triangle-literal-Q-input-v1'
BINDER_DEFINITION='angular-refined-supported-smooth-triangle-literal-two-bubble-Q-v1'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def replace(text,before,after,count=1):
    if text.count(before)!=count:
        raise ValueError('Exact source replacement count differs: '+before[:100])
    return text.replace(before,after)


def methods(text):
    return {(c.name,n.name):ast.dump(n,include_attributes=False) for c in ast.parse(text).body
        if isinstance(c,ast.ClassDef) for n in c.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}


def derive(parent,observer):
    old={}
    for name,digest in PINS.items():
        old[name]=(parent/name).read_text()
        if sha(old[name])!=digest:
            raise ValueError('Changed complete original source '+name)
    ast.parse(observer)
    observer_sha=sha(observer)
    generated={}
    original=old['so3_supported_smooth_triangle_meridian_operator.py']
    base=original.replace('complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1',BASE_SCHEMA)
    base=replace(base,'seed_parameters=None, seed_mean_kernel_module=None):',
        'seed_parameters=None, seed_mean_kernel_module=None, angular_observation_module=None):')
    base=replace(base,'        self.sqrt_multiplicity = np.sqrt(self.multiplicity)',
        "        if (angular_observation_module is None\n"
        "                or sha(angular_observation_module.__file__) != '"+observer_sha+"'\n"
        "                or sha(angular_observation_module.build.__code__.co_filename) != '"+observer_sha+"'):\n"
        "            raise ValueError('Bind the complete independent angular observation source')\n"
        "        self.reference_full_N = self.full_N\n"
        "        self.phi,self.multiplicity,self.angular_observation = angular_observation_module.build(parent_problem)\n"
        "        self.full_N,self.N = 4096,len(self.phi)\n"
        "        self.sqrt_multiplicity = np.sqrt(self.multiplicity)")
    base=replace(base,'            M=self.M, J=self.J, mesh_sha256=array_sha(self.mesh),',
        '            M=self.M, J=self.J, mesh_sha256=array_sha(self.mesh),\n'
        '            reference_full_N=self.reference_full_N,current_full_N=self.full_N,\n'
        '            angular_observation_refinement=self.angular_observation,')
    base=replace(base,'max(16384, 8*self.full_N)','max(16384, 8*self.reference_full_N)',count=2)
    generated['so3_angular_refined_smooth_triangle_meridian_operator.py']=base
    base_sha=sha(base)
    binder=old['supported_smooth_triangle_literal_zero_moment_input.py']
    binder=binder.replace('complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1',BASE_SCHEMA)
    binder=binder.replace(PINS['so3_supported_smooth_triangle_meridian_operator.py'],base_sha)
    binder=binder.replace('supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1',BINDER_SCHEMA)
    binder=binder.replace('supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1',BINDER_DEFINITION)
    generated['angular_refined_smooth_triangle_literal_zero_moment_input.py']=binder
    calibration=old['reference_centred_c1_smooth_triangle_calibration.py']
    calibration=calibration.replace('complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1',BASE_SCHEMA)
    calibration=calibration.replace('complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1',NORMAL_SCHEMA)
    calibration=calibration.replace(PINS['so3_supported_smooth_triangle_meridian_operator.py'],base_sha)
    generated['angular_refined_reference_centred_calibration.py']=calibration
    c1=old['normal_frame_c1_reuse.py'].replace(PINS['so3_supported_smooth_triangle_meridian_operator.py'],base_sha)
    generated['angular_refined_normal_frame_c1_reuse.py']=c1
    normal=old['so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py']
    for a,b in (
        ('complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1',BASE_SCHEMA),
        ('complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1',NORMAL_SCHEMA),
        ('supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1',BINDER_SCHEMA),
        (PINS['so3_supported_smooth_triangle_meridian_operator.py'],base_sha),
        (PINS['supported_smooth_triangle_literal_zero_moment_input.py'],sha(binder)),
        (PINS['reference_centred_c1_smooth_triangle_calibration.py'],sha(calibration)),
        (PINS['normal_frame_c1_reuse.py'],sha(c1))):
        if a not in normal:
            raise ValueError('Missing complete normal source literal '+a)
        normal=normal.replace(a,b)
    generated['so3_angular_refined_reference_centred_normal_lift_operator.py']=normal
    for name,text in generated.items():
        ast.parse(text);compile(text,name,'exec')
        if len(text.encode())>=100000:
            raise ValueError('Full source exceeds declared public-source bound '+name)
    base_before,base_after=methods(original),methods(base)
    changed=[key for key in base_before if base_before[key]!=base_after[key]]
    if changed!=[('ClosedMeridianOperator','__init__'),('ClosedMeridianOperator','domain')]:
        raise ValueError('Only the constructor and frozen-reference domain-size read may change: '+repr(changed))
    if methods(old['so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py'])!=methods(normal):
        raise ValueError('The complete original normal mathematical method bodies must remain AST-identical')
    return generated


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--parent-directory',type=Path,required=True)
    p.add_argument('--observer-source',type=Path,required=True)
    p.add_argument('--output-directory',type=Path,required=True)
    a=p.parse_args()
    result=derive(a.parent_directory,a.observer_source.read_text())
    a.output_directory.mkdir(parents=True,exist_ok=True)
    for name,text in result.items():
        (a.output_directory/name).write_text(text)
    print(json.dumps({n:dict(bytes=len(t.encode()),sha256=sha(t)) for n,t in result.items()},sort_keys=True))


if __name__=='__main__':
    main()
