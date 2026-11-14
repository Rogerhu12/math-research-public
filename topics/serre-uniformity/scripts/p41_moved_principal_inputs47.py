#!/usr/bin/env python3
"""Exact input/SLP bindings for two real initial V2 flips plus the frozen scalar chain."""
import gzip,hashlib,json
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p);return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())

def load(self, second_path, multiple_path, directory, flat_path):
    r = self.r
    self.second, self.multiple, self.flat = read(second_path), read(multiple_path), read(flat_path)
    manifest_path = directory/'transport_manifest47.json'
    self.manifest = read(manifest_path)
    assert self.second['complete_actual54_second_kind_center_integrals']
    assert self.flat['complete_exact_integer_principal_function_expression']
    assert self.flat['input_sha256'][second_path.name] == sha(second_path)
    assert self.flat['input_sha256'][manifest_path.name] == sha(manifest_path)
    assert self.second['input_sha256'][multiple_path.name] == sha(multiple_path)
    disk_id = self.second['disk_id']
    assert disk_id == self.multiple['disk_id'] == self.manifest['disk_id'] == self.flat['disk_id']
    self.disk_id = disk_id
    self.scale = self.manifest['final_node']['scalar_coefficient_of_C']
    assert self.flat['combined_function_to_actual_A1_t']['formal_divisor'] == {'C=P_center-P_minus3': self.scale, 'A1(t)': -1}
    self.functions = []
    for entry in self.manifest['functions']:
        if entry['phase'] == 'formal_extraction':
            continue
        path = directory/entry['filename']
        assert sha(path) == entry['sha256']
        self.functions.append(read(path))
    self.functions.sort(key=lambda f: (-3+f['moving_order_0based'],0) if f['phase'].startswith('initial_moving_') else (-1, 0) if f['phase'] == 'initial_negative'
                        else (f['bit'], 0 if f['operation'] == 'double_addflip' else 1))
    assert len(self.functions) == 457
    assert sum(f['line_bundle_power']==2 for f in self.functions)==3
    assert sum(f['line_bundle_power']==3 for f in self.functions)==454
    assert self.manifest['complete_two_actual_initial_moving_flips']
    assert self.flat['complete_two_actual_initial_moving_flips_in_integer_SLP']
    self.coeffs = {f['label']: r.from_json(f['numerator_coefficients']) for f in self.functions}
    self.fixed = {'fb': ('W', self.fb), 'fc': ('W', self.a.fc), 'v1': ('W', self.v1),
                  'FP': ('V2', r.from_json(self.second['endpoint']['terminal_transport_numerator_V2'])),
                  'GQ': ('V2', r.from_json(self.second['endpoint']['terminal_transport_denominator_V2']))}
    self.moved_point = next(x for x in self.based['records'] if x['disk_id'] == disk_id)
    self.moving_transport=self.moved_point['initial_moving_transport']
    tr=self.moving_transport
    self.point=dict(self.moved_point,point_coordinates=tr['original_point_coordinates'],point_frobenius=tr['original_point_frobenius'],point_sha256=tr['original_point_sha256'])
    assert self.point['point_sha256'] == self.manifest['initial_node']['point_sha256']
    assert self.moved_point['point_sha256']==self.manifest['multiplication_start_node']['point_sha256']==self.multiple['input_point_sha256']
    first,second=self.functions[:2]
    assert first['phase']=='initial_moving_first' and second['phase']=='initial_moving_second'
    assert first['numerator_coefficients']==tr['first_flip']['f_V2_coefficients']
    assert second['numerator_coefficients']==tr['second_flip_h_V2_coefficients']
    assert first['input_nodes'][0]['point_sha256']==self.point['point_sha256']
    assert first['output_node']['point_sha256']==second['input_nodes'][0]['point_sha256']==tr['first_flip']['residual_point_sha256']
    assert second['output_node']['point_sha256']==self.moved_point['point_sha256']
    assert self.flat['moving_f_integer_exponent']==self.scale and self.flat['moving_h_integer_exponent']==-self.scale

    assert r.equal(r.from_json(self.flat['f_b_coefficients']), self.fb)
    assert r.equal(r.from_json(self.flat['f0_coefficients']), self.a.fc)
    endpoint = self.flat['combined_function_to_actual_A1_t']
    assert r.equal(r.from_json(endpoint['v1_weight2_coefficients']), self.v1)
    assert r.equal(r.from_json(endpoint['F_terminal_V2_coefficients']), self.fixed['FP'][1])
    assert r.equal(r.from_json(endpoint['G_terminal_V2_coefficients']), self.fixed['GQ'][1])
    assert endpoint['actual_A1_physical_parameters'] == self.second['endpoint']['family1_physical_parameters_mod47four']
    assert self.family['points_1based'] == self.second['endpoint']['family1_points_1based']
    for name, digest in self.inputs.items():
        if name in self.second['input_sha256']:
            assert digest == self.second['input_sha256'][name]
    self.inputs.update({p.name: sha(p) for p in [second_path, multiple_path, flat_path, manifest_path]})
