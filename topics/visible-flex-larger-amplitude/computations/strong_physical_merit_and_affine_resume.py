"""Fixed-coordinate Newton merit and exact saved affine-inner restart.

The positive diagonal scale changes only the globalization norm. The original
matrix solve, residual, domain checks and final nonlinear physical gates stay
in force. The saved H0 response is used only as the original affine anchor;
the restored state's different H is never reported as already audited.
"""
from __future__ import annotations
import atexit
import ast
import gzip
import hashlib
import inspect
import json
from pathlib import Path
import textwrap
import time

HERE = Path(__file__).resolve().parent
EXPECTED_ACTUAL = '03bd353875b4a7ca248c938887b706ce6e2d3115e9b82f2cf772ccc4b5ce98b7'
EXPECTED_NEWTON = 'fd0f63fed7d74115c6e482bf47560230409ce2c20880aaa91e4e4ea1fbda0c83'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


class Runtime:
    def __init__(self, configuration, out):
        import numpy as np
        from strong_actual_fixed_control_response import raw_flat
        self.np = np
        self.configuration = dict(configuration)
        self.out = Path(out)
        self.started = time.monotonic()
        self.closed = False
        self.disk = None
        self.M = int(configuration['modes'])
        self.q = float(configuration['gauge'])
        self.weights = np.asarray(configuration['fixed_parameter_weights'], dtype=float)
        if (self.weights.shape != (self.M+3,) or not np.isfinite(self.weights).all()
                or not np.all(self.weights > 0)):
            raise ValueError('A complete, fixed, strictly positive diagonal parameter scale is required')
        self.weights.setflags(write=False)
        self.hashes = {str(HERE/name): sha(HERE/name) for name in (
            'strong_physical_merit_and_affine_resume.py', 'strong_physical_merit_actual_bvp.py',
            'strong_actual_fixed_control_response.py', 'root_actual_neck_bvp.py', 'root_domain_newton.py')}
        self.raw_path = Path(configuration['resume_raw'])
        self.packet_path = Path(configuration['affine_anchor_packet'])
        if sha(self.raw_path) != configuration['resume_raw_sha256']:
            raise ValueError('Frozen raw input changed after preparation')
        if sha(self.packet_path) != configuration['affine_anchor_packet_sha256']:
            raise ValueError('Frozen H0 packet changed after preparation')
        self.raw = document(self.raw_path)
        self.packet = document(self.packet_path)
        entry_path = Path(configuration['original_entry_raw'])
        if sha(entry_path) != configuration['original_entry_raw_sha256']:
            raise ValueError('Original inner-entry bytes changed after preparation')
        entry = document(entry_path)
        self.input_shapes = {}
        self.input_hashes = {}
        for name in ('x', 'y', 'p'):
            value = np.asarray(raw_flat(self.raw_path, self.raw, name, self.hashes), dtype=float)
            shape = self.raw['arrays'][name]['shape']
            value = value.reshape(shape)
            self.input_shapes[name] = list(value.shape)
            self.input_hashes[name] = hashlib.sha256(value.tobytes(order='C')).hexdigest()
        entry_y = np.asarray(raw_flat(entry_path,entry,'y',self.hashes),float).reshape(entry['arrays']['y']['shape'])
        self.original_entry_terminal = entry_y[:,-1].copy()
        del entry_y
        entry_x = np.asarray(raw_flat(entry_path,entry,'x',self.hashes),float)
        if hashlib.sha256(entry_x.tobytes(order='C')).hexdigest() != self.input_hashes['x']:
            raise ValueError('This exact first-inner restart requires the original complete mesh')
        del entry_x
        self.H0 = np.asarray(self.packet['request']['height'], dtype=float)
        self.K0 = np.asarray(self.packet['response']['jets']['slope'], dtype=float)
        self.J0_full = np.asarray(self.packet['response']['heightJetJacobian'], dtype=float).reshape(3*self.M+2,self.M)
        if self.H0.shape != (self.M,) or self.K0.shape != (self.M,):
            raise ValueError('The complete original affine anchor has the wrong dimension')
        if not all(np.isfinite(v).all() for v in (self.H0,self.K0,self.J0_full)):
            raise ValueError('The complete original affine anchor is nonfinite')
        self.stats = dict(merit_evaluations=0, original_affine_anchor_restorations=0)
        self.transform_records = {}
        self.anchor_record = None
        self._newton_installed = False
        atexit.register(self.finish)

    def emit(self, event, **data):
        if self.disk is not None:
            self.disk.emit(event, **data)
        else:
            print(json.dumps(dict(event=event, **data),allow_nan=False),flush=True)

    def install_disk_backend(self, bounded, disk_configuration):
        import strong_disk_actual_backend as backend
        original = backend._Runtime
        owner = self
        class AnnotatedDiskRuntime(original):
            def emit(self, event, **data):
                if event == 'disk_backend_started':
                    data.pop('newton_and_final_gates_unchanged', None)
                    data.update(original_equations_and_final_gates_unchanged=True,
                        newton_merit_changed=True, fixed_merit_configuration=owner.configuration)
                return super().emit(event, **data)
        try:
            backend._Runtime = AnnotatedDiskRuntime
            self.disk = backend.install_disk_backend(bounded,self.out,disk_configuration)
        finally:
            backend._Runtime = original
        self.disk.hashes.update({Path(name).name: value for name,value in self.hashes.items()})
        return self.disk

    def cost(self, step, n, nodes):
        np = self.np
        v = np.asarray(step, dtype=float)
        if n != 3*self.M+1 or v.shape != (n*nodes+self.M+3,):
            raise ValueError('Fixed merit received a different complete field/parameter layout')
        field = v[:n*nodes]
        parameters = v[n*nodes:]
        scaled = parameters*self.weights
        raw = float(v@v)
        field_cost = float(field@field)
        raw_parameter_cost = float(parameters@parameters)
        scaled_parameter_cost = float(scaled@scaled)
        weighted = field_cost+scaled_parameter_cost
        if not np.isfinite([raw,weighted,field_cost,raw_parameter_cost,scaled_parameter_cost]).all():
            raise FloatingPointError('Nonfinite fixed-coordinate Newton merit')
        self.stats['merit_evaluations'] += 1
        self.emit('fixed_physical_merit_evaluated', evaluation=self.stats['merit_evaluations'],
            raw_merit=raw, raw_field_cost=field_cost, raw_parameter_cost=raw_parameter_cost,
            fixed_scaled_parameter_cost=scaled_parameter_cost, returned_merit=weighted,
            maximum_raw_field_step=float(np.max(abs(field))),
            maximum_raw_parameter_step=float(np.max(abs(parameters))),
            weights_fixed_for_run=True, final_physical_gates_unchanged=True)
        return weighted

    def install_newton(self, loaded, path, adapter):
        path = Path(path)
        if sha(path) != EXPECTED_NEWTON or self._newton_installed:
            raise ValueError('Expected the unchanged original Newton and one explicit merit installation')
        transform = adapter.TRANSFORMS[path.name]
        source = path.read_text()
        if transform['original_sha256'] != EXPECTED_NEWTON:
            raise ValueError('Owned Newton source identity differs')
        for item in transform['replacements']:
            if source.count(item['old']) != item['count']:
                raise ValueError('Existing owned Newton transform does not reproduce')
            source = source.replace(item['old'],item['new'])
        edits = [
            ('            cost = float(step@step)',
             '            cost = _strong_fixed_physical_merit(step,n,m)'),
            ('                newcost = float(newstep@newstep)',
             '                newcost = _strong_fixed_physical_merit(newstep,n,m)'),
        ]
        for old,new in edits:
            if source.count(old) != 1:
                raise ValueError('The original correction-norm anchor is not unique')
            source = source.replace(old,new)
            transform['replacements'].append(dict(old=old,new=new,count=1))
        ast.parse(source)
        transform['fixed_physical_coordinate_merit'] = dict(
            fixed_parameter_weights=self.weights.tolist(), field_weights=1.,
            original_euclidean_merit_changed=True, original_linear_system_unchanged=True,
            original_RMS_BC_and_true_tail_gates_unchanged=True)
        self.transform_records['newton'] = dict(original_sha256=EXPECTED_NEWTON,
            before_checkpoint_observer_compiled_sha256=hashlib.sha256(source.encode()).hexdigest(),
            replacements=[dict(old=a,new=b,count=1) for a,b in edits])
        loaded._strong_fixed_physical_merit = self.cost
        self._newton_installed = True

    def restore_anchor(self, obj, x, y, p):
        np = self.np
        if self.stats['original_affine_anchor_restorations']:
            raise ValueError('The saved initial affine anchor may be consumed only once')
        if obj.M != self.M or obj.q != self.q:
            raise ValueError('The original affine anchor mode/gauge differs')
        original_H = np.asarray(obj.tail_height(self.original_entry_terminal),float)
        if original_H.tobytes(order='C') != self.H0.tobytes(order='C'):
            raise ValueError('The declared H0 is not the complete actual height at the original inner entry')
        for name,value in (('x',x),('y',y),('p',p)):
            value = np.asarray(value,dtype=float)
            if (list(value.shape) != self.input_shapes[name] or
                    hashlib.sha256(value.tobytes(order='C')).hexdigest() != self.input_hashes[name]):
                raise ValueError('The restored complete raw state differs before affine restart: '+name)
        port = obj.tail
        if (not hasattr(port,'saved_response') or
                port.provenance.get('packet_sha256') != self.configuration['affine_anchor_packet_sha256'] or
                not port.provenance.get('all_recorded_tail_source_hashes_checked') or
                not port.provenance.get('complete_packet_ready_binding')):
            raise ValueError('Exact original H0 requires the original strict audited-packet port')
        requests_before = port.provenance.get('live_new_Node_requests',0)
        response = port.solve(self.H0.copy(),jacobian=True,audit=False)
        if port.provenance.get('live_new_Node_requests',0) != requests_before:
            raise ValueError('The original frozen anchor unexpectedly launched a new tail solve')
        values = [np.asarray(response['jets']['slope'],float),
                  np.asarray(response['heightJetJacobian'],float).reshape(3*self.M+2,self.M)]
        for value,expected in zip(values,(self.K0,self.J0_full)):
            if value.tobytes(order='C') != expected.tobytes(order='C'):
                raise ValueError('The complete saved K0/J0 was not restored byte for byte')
        current_H = np.asarray(obj.tail_height(y[:,-1]),float)
        self.stats['original_affine_anchor_restorations'] = 1
        self.anchor_record = dict(
            original_H0=self.H0.tolist(), restored_raw_H=current_H.tolist(),
            original_H0_Float64LE_sha256=hashlib.sha256(self.H0.astype('<f8').tobytes()).hexdigest(),
            original_K0_Float64LE_sha256=hashlib.sha256(self.K0.astype('<f8').tobytes()).hexdigest(),
            complete_original_J0_Float64LE_sha256=hashlib.sha256(self.J0_full.astype('<f8').tobytes()).hexdigest(),
            source_packet_sha256=self.configuration['affine_anchor_packet_sha256'],
            original_inner_entry_sha256=self.configuration['original_entry_raw_sha256'],
            original_inner_entry_H0_bitwise_equal=True,
            complete_raw_x_y_p_bitwise_equal=True, complete_K0_J0_bitwise_equal=True,
            no_new_Node_request=True, reused_audited_packet_for_H0_only=True,
            restored_raw_H_equals_H0=current_H.tobytes()==self.H0.tobytes(),
            restored_raw_H_has_not_been_audited_here=True,
            original_true_new_H_check_and_final_audit_still_required=True)
        self.emit('original_affine_anchor_restored', **self.anchor_record)
        self.write_record()
        return self.H0.copy(),response

    def install_affine_on_class(self, cls):
        original = cls.solve_coupled
        if sha(HERE/'root_actual_neck_bvp.py') != EXPECTED_ACTUAL:
            raise ValueError('The original actual outer coupling source differs')
        physical_source = (HERE/'root_actual_neck_bvp.py').read_text()
        definitions = [node for node in ast.walk(ast.parse(physical_source))
                       if isinstance(node,ast.FunctionDef) and node.name == 'solve_coupled']
        if (len(definitions) != 1 or original.__name__ != 'solve_coupled'
                or 'Actual.solve_coupled' not in original.__qualname__
                or 'Eight actual nonlinear tail outer corrections exhausted' not in original.__code__.co_consts):
            raise ValueError('The unchanged Actual.solve_coupled method was not selected')
        # The current loader compiles an explicit client-import transform.
        # Its synthetic filename need not have a linecache entry; obtain the
        # unchanged method from the hash-locked original AST instead.
        node = definitions[0]
        source = textwrap.dedent(''.join(physical_source.splitlines(keepends=True)[node.lineno-1:node.end_lineno]))
        before = '        H=self.tail_height(y[:,-1]);response=self.tail.solve(H,jacobian=True,audit=False)'
        after = ('        if iteration == 0 and not _strong_affine_runtime.stats["original_affine_anchor_restorations"]:\n'
                 '            H,response=_strong_affine_runtime.restore_anchor(self,x,y,p)\n'
                 '        else:\n'
                 '            H=self.tail_height(y[:,-1]);response=self.tail.solve(H,jacobian=True,audit=False)')
        if source.count(before) != 1:
            raise ValueError('The original first affine anchor assignment is not unique')
        changed = source.replace(before,after)
        marker = '        self.outer_history.append(row)'
        if changed.count(marker) != 1:
            raise ValueError('The original outer-history insertion differs')
        changed = changed.replace(marker,
            '        if iteration == 0:\n'
            '            row["explicit_saved_initial_affine_anchor"]=_strong_affine_runtime.anchor_record\n'+marker)
        namespace = dict(original.__globals__)
        namespace.update(inspect.getclosurevars(original).nonlocals)
        namespace['_strong_affine_runtime'] = self
        exec(compile(changed,'<explicit-original-affine-anchor-restart>','exec'),namespace)
        cls.solve_coupled = namespace['solve_coupled']
        self.transform_records['affine_coupling'] = dict(
            source_file_sha256=EXPECTED_ACTUAL,
            original_method_sha256=hashlib.sha256(source.encode()).hexdigest(),
            transformed_method_sha256=hashlib.sha256(changed.encode()).hexdigest(),
            anchor_replacement=dict(old=before,new=after,count=1),
            original_true_Hnew_request_BC_check_and_final_audit_unmodified=True)

    def write_record(self):
        result = dict(scope=__doc__, configuration=self.configuration, source_sha256=self.hashes,
            stats=dict(self.stats), original_affine_anchor=self.anchor_record,
            runtime_source_transforms=self.transform_records, seconds=time.monotonic()-self.started,
            original_newton_merit_changed=True, original_linear_system_unchanged=True,
            original_final_RMS_BC_full_H_and_physical_audit_gates_unchanged=True,
            no_success_implied_by_merit_or_affine_restart=True)
        path = self.out.with_name(self.out.name+'-fixed-merit-affine-adapter.json')
        temporary = path.with_name(path.name+'.tmp')
        temporary.write_text(json.dumps(result,indent=2)+'\n')
        temporary.replace(path)
        return result

    def finish(self):
        if self.closed:
            return
        record = self.write_record()
        for path in (self.out.with_suffix('.json.gz'),self.out.with_name(self.out.name+'-summary.json')):
            if not path.is_file():
                continue
            data = document(path)
            data['fixed_physical_merit_and_affine_resume'] = record
            value = (json.dumps(data,indent=2)+'\n').encode()
            if path.suffix == '.gz':
                value = gzip.compress(value,mtime=0)
            if len(value) >= 5_000_000:
                raise ValueError('Final adapter metadata exceeds the file size gate')
            temporary = path.with_name(path.name+'.fixed-merit.tmp')
            temporary.write_bytes(value);temporary.replace(path)
        self.closed = True
