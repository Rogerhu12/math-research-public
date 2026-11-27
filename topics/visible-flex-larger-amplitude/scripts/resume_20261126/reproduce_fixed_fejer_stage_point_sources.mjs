#!/usr/bin/env node
/** Complete independent Fejer stage immutable-point source construction.
 * Full pinned UTF-8 sources and exact text replacements only. No Python,
 * numerical import, F/J/root evaluation, reduced fixture or scientific gate.
 * The two M320 sources supply complete pure history/source-binding text only;
 * no M320 field, checkpoint, numerical value or runtime is consumed here.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const INPUTS={
  "lower": {
    "closure_values": {
      "name": "fixed_fejer_immutable_closure_values.py",
      "bytes": 59048,
      "sha256": "01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595",
      "git_blob_sha": "f8d32aefb1c11152fd39ad1d5b6d160c60d864ef"
    },
    "analytic_J3": {
      "name": "fixed_fejer_analytic_stage_jacobian.py",
      "bytes": 25739,
      "sha256": "7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72",
      "git_blob_sha": "4fd818ed74a7043b955ef036a0cccccdb3cdc710"
    },
    "analytic_frame": {
      "name": "fixed_fejer_analytic_normal_frame.py",
      "bytes": 47286,
      "sha256": "75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c",
      "git_blob_sha": "ee0e9799f87301d8a60d6da20cb68731d031cdb0"
    },
    "frame_C1": {
      "name": "fixed_fejer_normal_frame_c1.py",
      "bytes": 37361,
      "sha256": "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca",
      "git_blob_sha": "9b3464345766a956159db88d5d6c4326b662ece4"
    },
    "stage_matrices": {
      "name": "fixed_fejer_detached_stage_matrices.py",
      "bytes": 47791,
      "sha256": "7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7",
      "git_blob_sha": "4fad02c03e92b5fcd3aa2b3621c58a49d1631eff"
    },
    "adjacent_matrices": {
      "name": "fixed_fejer_adjacent_normal_matrices.py",
      "bytes": 36766,
      "sha256": "257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0",
      "git_blob_sha": "14ad8790e43b2e58f94772aacd98fb61be7826e9"
    },
    "reference_calibration": {
      "name": "fixed_fejer_reference_calibration.py",
      "bytes": 11914,
      "sha256": "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c",
      "git_blob_sha": "c174fcf9712b76abe6f3f3ed307d0115598a1d3d"
    },
    "endpoint": {
      "name": "fixed_fejer_normal_lift_operator.py",
      "bytes": 98490,
      "sha256": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
      "git_blob_sha": "fd9b4ba9526a7805c73957ffc75a3261fa785290"
    },
    "root_packets": {
      "name": "fixed_fejer_immutable_normal_root_packets.py",
      "bytes": 72375,
      "sha256": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468",
      "git_blob_sha": "12d26c8b663d185907feec930aa09def002af4cb"
    }
  },
  "upper": {
    "actual_fixed_input_binding": {
      "name": "fixed_fejer_reference_input_binding.py",
      "bytes": 25672,
      "sha256": "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f",
      "git_blob_sha": "5eab3f96cb8b1bc245f4de33dc2041cf25d22094"
    },
    "independent_envelope_memory": {
      "name": "complete_fixed_fejer_material_envelope_memory.py",
      "bytes": 45988,
      "sha256": "9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a",
      "git_blob_sha": "d9a09a4e76efa1a4e55831fd566192d150ab67e1"
    },
    "binding": {
      "name": "fixed_fejer_complete_source_binding.py",
      "bytes": 32487,
      "sha256": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
      "git_blob_sha": "3073c9490a6bc6ce7dcf323f799ee8075f8bdd78"
    },
    "geometry": {
      "name": "so3_fixed_fejer_complete_geometry.py",
      "bytes": 70709,
      "sha256": "bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26",
      "git_blob_sha": "f2b28d1bf2f994db9866cb58e74a522ff719358a"
    },
    "transfer": {
      "name": "transfer_fixed_fejer_material_envelope_memory.py",
      "bytes": 66839,
      "sha256": "af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566",
      "git_blob_sha": "597f6529dea5ffeb32e8df43a1442f1f7994d48b"
    },
    "driver": {
      "name": "fullclosed_fixed_fejer_immutable_point_so3_qp.py",
      "bytes": 91714,
      "sha256": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
      "git_blob_sha": "feb49510ddada8fb77d0bf9cf3cd78c1de50079d"
    },
    "launcher": {
      "name": "launch_fixed_fejer_immutable_point_actions.py",
      "bytes": 21789,
      "sha256": "0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf",
      "git_blob_sha": "f5d337a07f6b1a0438f33cdaf6fc1845b30f8b84"
    },
    "reader": {
      "name": "read_fixed_fejer_immutable_point_so3_report.py",
      "bytes": 97987,
      "sha256": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
      "git_blob_sha": "feae7eaf1b29ea0ae2563c4fc0d8089794602fa3"
    }
  },
  "complete_parent_bridge_templates": {
    "binding": {
      "name": "fixed_fejer_frequency_source_binding.py",
      "bytes": 35685,
      "sha256": "caf16fbc87ef618ddae5ba42616d9bbe136beac6d32487224073ac6958c4d3c0",
      "git_blob_sha": "8a25d59f8a2fa2c818af8d3d17875d1ca5ae8a33"
    },
    "transfer": {
      "name": "transfer_fixed_fejer_frequency_memory.py",
      "bytes": 84194,
      "sha256": "1d35b2e7231ed5609e066e602f0f4722bb931b89bb9b3acea132cb45cc510bb8",
      "git_blob_sha": "66571893cb9f27a6b830b831e83052d5950059c0"
    }
  }
};
const EXPECTED={
  "stage_matrices": {
    "name": "fixed_fejer_immutable_point_stage_matrices.py",
    "bytes": 61280,
    "sha256": "e4d42910f9550a20d0afc16aab8f54b5ea1ceb18ace375128f3a79bfef0e76ce",
    "git_blob_sha": "002985b6b754585f08f05b349f305adf03ad2f9e"
  },
  "adjacent_matrices": {
    "name": "fixed_fejer_stage_point_adjacent_matrices.py",
    "bytes": 36766,
    "sha256": "d04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5",
    "git_blob_sha": "d5ab132b50b7f5caae92a417f590ee44e77c6ca0"
  },
  "endpoint": {
    "name": "fixed_fejer_stage_point_normal_lift.py",
    "bytes": 98490,
    "sha256": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
    "git_blob_sha": "ffdaf4a094c7a0363bd6bc3ed316ba1e7e8ec25c"
  },
  "root_packets": {
    "name": "fixed_fejer_stage_point_root_packets.py",
    "bytes": 73070,
    "sha256": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
    "git_blob_sha": "310aa66a367efe0bb6ca26da12b4b4395abd3f08"
  },
  "analytic_J3_binding": {
    "name": "fixed_fejer_stage_point_source_binding.py",
    "bytes": 38356,
    "sha256": "9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f",
    "git_blob_sha": "fb9dc94fa9b137dd64f602d9cd84b8997d36bdc2"
  },
  "envelope_transfer": {
    "name": "transfer_fixed_fejer_stage_point_memory.py",
    "bytes": 78863,
    "sha256": "afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed",
    "git_blob_sha": "7f1f3971893d8895d7e1b8cc3612e563a44d3095"
  },
  "geometry": {
    "name": "so3_fixed_fejer_stage_point_geometry.py",
    "bytes": 70709,
    "sha256": "2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471",
    "git_blob_sha": "2677d379e87b359088177b244428894311348996"
  },
  "driver": {
    "name": "fullclosed_fixed_fejer_stage_point_so3_qp.py",
    "bytes": 93158,
    "sha256": "050a6067fbb2fb4d054a97bf73899cfe5d4629197e42c39f00846a1f6a63b268",
    "git_blob_sha": "b0374f2db88ca38a936c7eadfc97f5377922c146"
  },
  "launcher": {
    "name": "launch_fixed_fejer_stage_point_actions.py",
    "bytes": 21785,
    "sha256": "8fed7b6a7ff6c988ee2240a4193f9440fd91ef158e5ac47d6248868d4e19214c",
    "git_blob_sha": "fed243876328a2933fcfb10288f6f42edda16211"
  },
  "reader": {
    "name": "read_fixed_fejer_stage_point_so3_report.py",
    "bytes": 97975,
    "sha256": "42e198f8d886641048059c3cdd8110b8bc3d000cdf350da1de54ac4bb83014a0",
    "git_blob_sha": "4304a1fdbe907bdb9c6708d7a89f5a18733ce15b"
  }
};
const hash=s=>({sha256:crypto.createHash('sha256').update(s,'utf8').digest('hex'),bytes:Buffer.byteLength(s,'utf8')});
function ex(t,n){const a=t.indexOf("def "+n+"(");if(a<0)throw Error("function absent "+n);let b=t.length;for(const mark of ["\ndef ","\nclass ","\nif __name__"]) {const p=t.indexOf(mark,a+4);if(p>=0)b=Math.min(b,p+1);}return t.slice(a,b);}
function buildStage(parent) {
 const patches=[]; let s=parent.text;
 function replace(a,b,count=1){const n=s.split(a).length-1;if(n!==count)throw Error("stage patch multiplicity "+n+" != "+count+": "+a.slice(0,90));s=s.split(a).join(b);patches.push({before:a,after:b,count});}
 replace("SCHEMA = 'complete-closure-value-compatible-same-call-detached-normal-stage-matrix-reuse-v1'","SCHEMA = 'complete-immutable-point-bound-same-call-detached-normal-stage-matrix-reuse-v1'");
 replace("All scientific operations require the public repository Actions runner.\n","All scientific operations require the public repository Actions runner.\n\nThis independent revision replaces only repeated full-point copies inside a\nmatrix scope by a strict immutable-bytes-owner binding.  Scope entry retains\nboth the original full-word read and canonical array SHA check.  Scope exit\nrereads every point word.  All per-stage model/data/control/carrier guards\nand all original scientific matrix methods remain in force.\n");
 replace("        phases=list(PHASES),","        phases=list(PHASES),\n        original_complete_stage_matrix_source_sha256='"+parent.sha256+"',\n        point_guard_policy='whole words and canonical array SHA at entry; same hard immutable bytes owner at every stage; whole words again at exit',\n        point_owner='plain native-float64 non-owning readonly contiguous one-dimensional ndarray directly backed by full immutable bytes',\n        point_array_shape_stride_owner_length_and_selected_object_rechecked_each_stage=True,\n        selected_point_object_identity_and_point_SHA_rechecked_each_stage=True,\n        entry_and_exit_complete_point_words_retained=True,\n        per_stage_full_point_word_copy_performed=False,\n        point_owner_checks_and_whole_word_reads_counted_separately=True,\n        point_guard_costs_are_closed_scope_totals=True,\n        scope_exit_binding_failure_is_not_a_successful_scope=True,\n        original_all_other_stage_guards_unchanged=True,");
 replace("        actual_implicit_jacobian_blocks=0)","        actual_implicit_jacobian_blocks=0,\n        point_owner_entry_checks=0,point_owner_entry_failures=0,\n        point_owner_stage_checks=0,point_owner_stage_failures=0,\n        point_owner_exit_checks=0,point_owner_exit_failures=0,\n        whole_point_entry_reads=0,whole_point_entry_read_failures=0,\n        whole_point_exit_reads=0,whole_point_exit_read_failures=0,\n        whole_point_entry_array_sha_checks=0,whole_point_entry_array_sha_failures=0)");
 replace("    return dict(value)\n\n\ndef validate_metadata",`    for phase in ('entry','stage','exit'):
        if value['point_owner_'+phase+'_failures'] > value['point_owner_'+phase+'_checks']:
            raise ValueError('Immutable point binding failures exceed actual attempts')
    for phase in ('entry','exit'):
        if value['whole_point_'+phase+'_read_failures'] > value['whole_point_'+phase+'_reads']:
            raise ValueError('Complete point read failures exceed actual attempts')
    if (value['whole_point_entry_array_sha_failures'] > value['whole_point_entry_array_sha_checks']
            or value['point_owner_stage_checks'] < value['logical_matrix_requests']):
        raise ValueError('Every actual matrix request retains its own immutable point check')
    return dict(value)


def validate_metadata`);
 replace("for key in ('scope_seconds','original_method_seconds'):","for key in ('scope_seconds','original_method_seconds','point_owner_binding_seconds',\n            'complete_point_word_read_seconds','complete_point_array_sha_seconds'):",2);
 replace("    last = value.get('last_scope')",`    closed = value['scopes_closed']
    if (any(total[key] != closed for key in ('point_owner_entry_checks',
                'whole_point_entry_reads','whole_point_entry_array_sha_checks',
                'point_owner_exit_checks','whole_point_exit_reads'))
            or any(total[key] != 0 for key in ('point_owner_entry_failures',
                'whole_point_entry_read_failures','whole_point_entry_array_sha_failures'))
            or value.get('point_guard_costs_count_only_closed_scopes') is not True
            or value.get('per_stage_complete_point_word_copy_performed') is not False):
        raise ValueError('Closed scopes retain full entry/exit reads without inventing per-stage word reads')
    last = value.get('last_scope')`);
 replace("        keys = binding.get('literal_phi_hex')",`        point_words = binding.get('complete_free_point_word_count')
        expected_words = (model['M']-len(model['fixed_core_first3'])
            +(3*model['J']-3)*(3*model['M']+2)+1)
        if (type(point_words) is not int or point_words != expected_words
                or binding.get('complete_free_point_shape') != [point_words]
                or binding.get('complete_free_point_stride_bytes') != [8]
                or binding.get('immutable_point_owner_bytes') != 8*point_words
                or binding.get('point_dtype') != 'float64'
                or binding.get('point_owner_kind') != 'immutable built-in bytes'
                or binding.get('point_array_is_plain_native_contiguous_readonly_nonowning') is not True
                or binding.get('entry_canonical_array_sha_checked') is not True
                or binding.get('per_stage_complete_point_word_copy_performed') is not False):
            raise ValueError('Keep the entire immutable point layout and original entry SHA check')
        keys = binding.get('literal_phi_hex')`);
 replace("        attempted = last.get('stage_requests_attempted')",`        if (any(current[key] != 1 for key in ('point_owner_entry_checks',
                    'whole_point_entry_reads','whole_point_entry_array_sha_checks',
                    'point_owner_exit_checks','whole_point_exit_reads'))
                or any(current[key] != 0 for key in ('point_owner_entry_failures',
                    'whole_point_entry_read_failures','whole_point_entry_array_sha_failures'))):
            raise ValueError('Every closed scope must retain its actual complete entry and exit checks')
        exit_check = last.get('point_scope_exit_check')
        if (not isinstance(exit_check,dict) or exit_check.get('attempted') is not True
                or type(exit_check.get('immutable_binding_valid')) is not bool
                or exit_check.get('immutable_binding_valid') is not (current['point_owner_exit_failures'] == 0)
                or exit_check.get('complete_point_words_equal') not in (True,False,None)
                or not isinstance(exit_check.get('failures'),list)
                or any(not isinstance(item,dict) or not isinstance(item.get('operation'),str)
                    or not isinstance(item.get('exception_type'),str) or not isinstance(item.get('reason'),str)
                    for item in exit_check['failures'])
                or (current['whole_point_exit_read_failures'] != 0
                    and exit_check['complete_point_words_equal'] is not None)
                or (current['whole_point_exit_read_failures'] == 0
                    and type(exit_check['complete_point_words_equal']) is not bool)):
            raise ValueError('An exit guard must retain its actual failed or successful own-point evidence')
        point_complete = (exit_check['immutable_binding_valid'] is True
            and exit_check['complete_point_words_equal'] is True
            and not exit_check['failures'] and current['point_owner_stage_failures']==0)
        if (last.get('scope_point_binding_complete') is not point_complete
                or (not point_complete and not exit_check['failures']
                    and current['point_owner_stage_failures']==0)):
            raise ValueError('A failed scope-exit binding is never reported as a complete point binding')
        attempted = last.get('stage_requests_attempted')`);
 replace("            scope_seconds=last['scope_seconds'],original_method_seconds=last['original_method_seconds'],",`            scope_seconds=last['scope_seconds'],original_method_seconds=last['original_method_seconds'],
            point_owner_binding_seconds=last['point_owner_binding_seconds'],
            complete_point_word_read_seconds=last['complete_point_word_read_seconds'],
            complete_point_array_sha_seconds=last['complete_point_array_sha_seconds'],
            point_scope_exit_check=_plain_copy(exit_check),
            scope_point_binding_complete=point_complete,`);
 replace("        scope_seconds=value['scope_seconds'],original_method_seconds=value['original_method_seconds'],",`        scope_seconds=value['scope_seconds'],original_method_seconds=value['original_method_seconds'],
        point_owner_binding_seconds=value['point_owner_binding_seconds'],
        complete_point_word_read_seconds=value['complete_point_word_read_seconds'],
        complete_point_array_sha_seconds=value['complete_point_array_sha_seconds'],
        point_guard_costs_count_only_closed_scopes=True,
        per_stage_complete_point_word_copy_performed=False,`);
 const owner=`def _immutable_point_owner(value, shape, expected_owner=None):
    """Read only fixed-size array metadata; never copy or scan full point words."""
    if type(value) is not np.ndarray:
        raise ValueError('The selected complete point must be a plain ndarray')
    owner=value.base
    if (type(owner) is not bytes or value.dtype!=np.dtype('float64')
            or not value.dtype.isnative or value.shape!=shape
            or value.strides!=(np.dtype('float64').itemsize,)
            or value.ndim!=1 or not value.flags.c_contiguous
            or value.flags.writeable or value.flags.owndata
            or value.nbytes!=8*shape[0] or len(owner)!=value.nbytes
            or (expected_owner is not None and owner is not expected_owner)):
        raise ValueError('Bind the entire readonly point directly to its exact immutable bytes owner')
    # The exact-length contiguous array covers the whole bytes allocation;
    # a nonzero slice offset would require bytes beyond the bound owner.
    return owner


`;
 replace("class CompleteDetachedStageMatrices:",owner+"class CompleteDetachedStageMatrices:");
 replace("        self.last_scope = None","        self.last_scope = None\n        self.point_owner_binding_seconds = 0.\n        self.complete_point_word_read_seconds = 0.\n        self.complete_point_array_sha_seconds = 0.");
 replace("        self.last_scope = record",`        self.point_owner_binding_seconds += record['point_owner_binding_seconds']
        self.complete_point_word_read_seconds += record['complete_point_word_read_seconds']
        self.complete_point_array_sha_seconds += record['complete_point_array_sha_seconds']
        self.last_scope = record`);
 replace("            last_scope=_plain_copy(self.last_scope),",`            last_scope=_plain_copy(self.last_scope),
            point_owner_binding_seconds=self.point_owner_binding_seconds,
            complete_point_word_read_seconds=self.complete_point_word_read_seconds,
            complete_point_array_sha_seconds=self.complete_point_array_sha_seconds,
            point_guard_costs_count_only_closed_scopes=True,
            per_stage_complete_point_word_copy_performed=False,`);
 const entry=`        self.point_object = self.q._current_x
        self.point_words,_ = self.module._array_words(self.point_object,(self.q.free_size,))
        self.point_identity = self.q._current_point_sha256
        current_sha = self.kernel.methods['_stage_jacobian'].__globals__['array_sha'](self.point_object)
        if (not isinstance(self.point_identity,str) or current_sha != self.point_identity
                or canonical(self.q.model) != kernel.model_identity_sha256):
            raise ValueError('Use the actual complete selected free point and current model')`;
 const entryNew=`        self.counts = _new_counts()
        self.point_owner_binding_seconds = 0.
        self.complete_point_word_read_seconds = 0.
        self.complete_point_array_sha_seconds = 0.
        self.point_object = self.q._current_x
        self.point_identity = self.q._current_point_sha256
        self.point_owner = None
        self.point_owner = self._point_binding('entry')
        self.point_words = self._read_complete_point_words('entry')
        self.counts['whole_point_entry_array_sha_checks'] += 1
        point_sha_started = time.monotonic()
        try:
            current_sha = self.kernel.methods['_stage_jacobian'].__globals__['array_sha'](self.point_object)
            if (not isinstance(self.point_identity,str) or current_sha != self.point_identity
                    or canonical(self.q.model) != kernel.model_identity_sha256):
                raise ValueError('Use the actual complete selected free point and current model')
        except Exception:
            self.counts['whole_point_entry_array_sha_failures'] += 1
            raise
        finally:
            self.complete_point_array_sha_seconds += time.monotonic()-point_sha_started`;
 replace(entry,entryNew);
 replace("        self.original_seconds = 0.\n        self.counts = _new_counts()","        self.original_seconds = 0.");
 replace("            complete_free_point_words_sha256=hashlib.sha256(self.point_words).hexdigest(),",`            complete_free_point_words_sha256=hashlib.sha256(self.point_words).hexdigest(),
            complete_free_point_word_count=int(self.q.free_size),
            complete_free_point_shape=[int(self.q.free_size)],
            complete_free_point_stride_bytes=[8],
            immutable_point_owner_bytes=len(self.point_owner),
            point_dtype='float64',point_owner_kind='immutable built-in bytes',
            point_array_is_plain_native_contiguous_readonly_nonowning=True,
            entry_canonical_array_sha_checked=True,
            per_stage_complete_point_word_copy_performed=False,`);
 replace("    def _carrier_identity(self):",`    def _point_binding(self, phase):
        self.counts['point_owner_'+phase+'_checks'] += 1
        started = time.monotonic()
        try:
            owner = _immutable_point_owner(self.point_object,(self.q.free_size,),self.point_owner)
            if (self.q._current_x is not self.point_object
                    or self.q._current_point_sha256 != self.point_identity):
                raise ValueError('Do not replace the actual selected point object or its complete identity inside a scope')
            return owner
        except Exception:
            self.counts['point_owner_'+phase+'_failures'] += 1
            raise
        finally:
            self.point_owner_binding_seconds += time.monotonic()-started

    def _read_complete_point_words(self, phase):
        self.counts['whole_point_'+phase+'_reads'] += 1
        started = time.monotonic()
        try:
            return self.module._array_words(self.point_object,(self.q.free_size,))[0]
        except Exception:
            self.counts['whole_point_'+phase+'_read_failures'] += 1
            raise
        finally:
            self.complete_point_word_read_seconds += time.monotonic()-started

    def _carrier_identity(self):`);
 replace("    def _validate(self, previous, frame, zero, tau, stage_index):\n        if", "    def _validate(self, previous, frame, zero, tau, stage_index):\n        self._point_binding('stage')\n        if");
 replace("                or self.q._current_point_sha256 != self.point_identity\n                or self.module._array_words(self.point_object,(self.q.free_size,))[0] != self.point_words\n","                or self.q._current_point_sha256 != self.point_identity\n");
 const closeStart="    def close(self):\n        if self.closed:\n            return\n        record = dict(binding=self.binding,actual_counts=dict(self.counts),";
 replace(closeStart,`    def close(self):
        if self.closed:
            return
        exit_check = dict(attempted=True,immutable_binding_valid=False,
            complete_point_words_equal=None,failures=[])
        try:
            self._point_binding('exit')
        except Exception as error:
            exit_check['failures'].append(dict(operation='immutable point binding at scope exit',
                exception_type=type(error).__name__,reason=str(error)))
        else:
            exit_check['immutable_binding_valid'] = True
        try:
            words = self._read_complete_point_words('exit')
        except Exception as error:
            exit_check['failures'].append(dict(operation='complete point word read at scope exit',
                exception_type=type(error).__name__,reason=str(error)))
        else:
            exit_check['complete_point_words_equal'] = words == self.point_words
            if not exit_check['complete_point_words_equal']:
                exit_check['failures'].append(dict(operation='complete point word equality at scope exit',
                    exception_type='ValueError',reason='The complete selected point words changed inside a matrix scope'))
        point_complete = (exit_check['immutable_binding_valid'] is True
            and exit_check['complete_point_words_equal'] is True and not exit_check['failures']
            and self.counts['point_owner_stage_failures']==0)
        record = dict(binding=self.binding,actual_counts=dict(self.counts),`);
 replace("            original_method_seconds=self.original_seconds,","            original_method_seconds=self.original_seconds,\n            point_owner_binding_seconds=self.point_owner_binding_seconds,\n            complete_point_word_read_seconds=self.complete_point_word_read_seconds,\n            complete_point_array_sha_seconds=self.complete_point_array_sha_seconds,\n            point_scope_exit_check=exit_check,scope_point_binding_complete=point_complete,");
 replace("        self.point_object = None\n        self.point_words = None","        self.point_object = None\n        self.point_owner = None\n        self.point_words = None");
 replace("        self.kernel._finish(record)\n\n    def __enter__", "        self.kernel._finish(record)\n        if not point_complete:\n            raise ValueError('Complete matrix scope point binding failed: '+json.dumps(dict(exit_check=exit_check,stage_binding_failures=self.counts['point_owner_stage_failures'])))\n\n    def __enter__");
 replace("    def __exit__(self, error_type, error, traceback):\n        self.close()\n        return False",`    def __exit__(self, error_type, error, traceback):
        try:
            self.close()
        except Exception:
            if error_type is None:
                raise
            # Preserve the original body exception.  The failed exit guard
            # has already been retained in the closed own-scope record.
        return False`);
 return {text:s,patches,name:"fixed_fejer_immutable_point_stage_matrices.py"};
}
function buildHotLower(parents,stage,hash) {
 const outputs={stage_matrices:stage}, patches=[];
 function rewrite(role,name,changes){
  const parent=parents[role];let text=parent.text;const ps=[];
  for(const [before,after,count=1] of changes){const n=text.split(before).length-1;if(n!==count)throw Error(role+" patch "+n+" "+before);text=text.split(before).join(after);ps.push({before,after,count});}
  outputs[role]={role,name,text,...hash(text),parent:{name:parent.name,sha256:parent.sha256,bytes:parent.bytes,git_blob_sha:parent.git_blob_sha}};
  patches.push({role,patches:ps});return outputs[role];
 }
 const adj=rewrite("adjacent_matrices","fixed_fejer_stage_point_adjacent_matrices.py",[[parents.stage_matrices.sha256,stage.sha256]]);
 const n=rewrite("endpoint","fixed_fejer_stage_point_normal_lift.py",[[parents.stage_matrices.sha256,stage.sha256],[parents.adjacent_matrices.sha256,adj.sha256]]);
 const schema=parents.endpoint.text.match(/^SCHEMA = '([^']+)'$/m)[1];
 const row=`    '${n.sha256}': dict(schema='${schema}',
        base='552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3',
        adjacent='${adj.sha256}',calibration='${parents.reference_calibration.sha256}',
        analytic='${parents.analytic_J3.sha256}',analytic_frame='${parents.analytic_frame.sha256}',
        closure_values='${parents.closure_values.sha256}'),
`;
 rewrite("root_packets","fixed_fejer_stage_point_root_packets.py",[["NORMALS = {\n","NORMALS = {\n"+row]]);
 return {outputs,patches};
}
function buildHotBinding(parent,lowerParents,lower,oldParentValidator,hash) {
 let text=parent.text;const patches=[];
 function replace(before,after,count=1){const n=text.split(before).length-1;if(n!==count)throw Error("binding "+n+" != "+count+" "+before.slice(0,100));text=text.split(before).join(after);patches.push({before,after,count});}
 replace('SCHEMA = "complete-fixed-fejer-source-model-and-report-binding-v1"','SCHEMA = "complete-fixed-fejer-stage-point-source-model-and-report-binding-v1"');
 for(const role of ["stage_matrices","adjacent_matrices","endpoint"]){
  replace(lowerParents[role].sha256,lower[role].sha256);
  replace(lowerParents[role].name,lower[role].name);
 }
 const constants=`STAGE_POINT_PARENT_DRIVER = ('fullclosed_fixed_fejer_immutable_point_so3_qp.py',
    '477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd')
STAGE_POINT_PARENT_BINDING = ('fixed_fejer_complete_source_binding.py',
    '3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88')
STAGE_POINT_PARENT_NORMAL = '1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778'


`;
 let validator=oldParentValidator.replaceAll("_validate_original_parent_model","_validate_stage_point_parent_model")
 .replaceAll("IMMUTABLE_POINT_PARENT","STAGE_POINT_PARENT").replaceAll("frequency_parent_driver","stage_point_parent_driver")
 .replaceAll("frequency_parent_binding","stage_point_parent_binding").replaceAll("_complete_frequency_parent_binding_","_complete_stage_point_parent_binding_");
 const relation=`def _compatible_stage_point_parent(old,new,current_pins,*,source_directory):
    """Same full Fejer field definition; only the declared stage point guard changes."""
    _validate_stage_point_parent_model(old,source_directory,current_pins)
    roles={role:pair[1] for role,pair in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    if (before.get('schema')!=after.get('schema')
            or before.get('base_complete_model')!=after.get('base_complete_model')
            or before.get('base_model_identity_sha256')!=after.get('base_model_identity_sha256')
            or before.get('reference_centering_definition',{}).get('source_sha256')
                !=after.get('reference_centering_definition',{}).get('source_sha256')):
        raise ValueError('The mathematical field schema, entire fixed base and original calibration source stay unchanged')
    for value,expected_source in ((before,STAGE_POINT_PARENT_NORMAL),(after,roles['endpoint'])):
        if (value.get('source_sha256')!=expected_source
                or value.get('reference_centering_definition',{}).get('endpoint_source_sha256')!=expected_source):
            raise ValueError('Keep each actual complete normal source in its own calibration definition')
        value.pop('source_sha256')
        value['reference_centering_definition'].pop('endpoint_source_sha256')
        for key in ('detached_stage_matrix_reuse','adjacent_normal_frame_matrices'):
            value.pop(key)
    if before!=after:
        raise ValueError('All remaining complete model fields, four unchanged working policies, full target, variables and partition must match')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        full_base_reference_chart_profile_and_partition_equal=True,
        only_explicit_source_schema_and_frame_matrix_working_policy_fields_changed=True,
        same_exact_equations_variables_target_and_partition_retained=True,
        complete_stage_point_guard_change_explicit=True,
        four_other_working_policies_exactly_unchanged=True,
        model_schema_and_full_free_layout_exactly_unchanged=True,
        complete_original_110_source_roles_read=True,
        actual_computed_float_field_or_root_words_inherited=False,
        computed_float_field_equality_claimed=False)


`;
 replace("def compatible_legacy_model(old,new,current_pins,*,source_directory):",constants+validator+relation+"def compatible_legacy_model(old,new,current_pins,*,source_directory):");
 replace("    if old.get('source_sha256')==IMMUTABLE_POINT_PARENT_NORMAL:\n","    if old.get('source_sha256')==STAGE_POINT_PARENT_NORMAL:\n        return _compatible_stage_point_parent(old,new,current_pins,source_directory=source_directory)\n    if old.get('source_sha256')==IMMUTABLE_POINT_PARENT_NORMAL:\n");
 return {role:"analytic_J3_binding",name:"fixed_fejer_stage_point_source_binding.py",text,patches,...hash(text),parent:{name:parent.name,sha256:parent.sha256,bytes:parent.bytes,git_blob_sha:parent.git_blob_sha}};
}
function buildHotTransfer(parent,binding,parents,helpers,hash) {
 let text=parent.text;const patches=[];
 function replace(before,after,count=1){const n=text.split(before).length-1;if(n!==count)throw Error("transfer "+n+" != "+count+" "+before.slice(0,100));text=text.split(before).join(after);patches.push({before,after,count});}
 replace('SCHEMA = "complete-fixed-fejer-material-history-and-same-source-continuation-v1"','SCHEMA = "complete-fixed-fejer-stage-point-history-and-same-source-continuation-v1"');
 replace(parents.binding.sha256,binding.sha256);
 replace(parents.binding.name,binding.name);
 const oldDriverSchema=parents.driver.text.match(/^SCHEMA = "([^"]+)"$/m)[1];
 const family=`    '${parents.driver.sha256}': dict(
        report_schema='${oldDriverSchema}',
        reader_sha256='${parents.reader.sha256}',
        reader_relative='scripts/resume_20261126/${parents.reader.name}',
        operator_sha256='1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778',
        operator_schema='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1',
        memory_sha256=CURRENT_MEMORY_SOURCE_SHA256,
        same_predeclared_fixed_fejer_target=True,complete_final_variable_copy_supported=True),
`;
 replace("PARENT_FAMILIES = {\n","PARENT_FAMILIES = {\n"+family);
 replace("        historical_parent_families_are_provenance_not_current_target_parents=True,","        previous_target_parent_families_are_provenance_not_current_target_parents=True,\n        actual_fixed_fejer_parent_driver_sha256='"+parents.driver.sha256+"',\n        actual_fixed_fejer_parent_reader_sha256='"+parents.reader.sha256+"',\n        actual_fixed_fejer_complete_terminal_report_and_full13_final_transfer_supported=True,\n        same_fixed_fejer_target_and_complete_current_layout_required=True,\n        only_stage_point_guard_and_recursive_source_policy_changed=True,\n        every_actual_inbound_history_file_and_inherited_transfer_metadata_retained=True,\n        every_original_typed_row_and_all_three_original_role_arrays_retained=True,");
 replace("        changed_model_fields='new declared mathematical chart and deterministic mesh; no previous-target model or field equivalence asserted',","        changed_model_fields='same predeclared Fejer target and full layout; new stage immutable-owner guard and its exact recursive source policies only',");
 const oldBlock="    if paths:\n        raise ValueError('Previous-target terminal reports cannot supply fields or typed priority to this explicitly new Fejer target; use its same-source complete restart')\n    parent_memory=requested_parent_memory(args)";
 replace(oldBlock,"    parent_memory=requested_parent_memory(args)\n    if paths and parent_memory!=CURRENT_MEMORY_SOURCE_SHA256:\n        raise ValueError('Only the actual same-target complete Fejer parent supplies terminal history or variable words')");
 replace("        terminal = _terminal(payload)\n        model_binding", "        _input_identity(payload,args,q)\n        terminal = _terminal(payload)\n        model_binding");
 replace("        parents.append(dict(record=record,payload=payload,terminal=terminal,\n            model_binding=model_binding,family=family,", "        inbound=_complete_input_reports(payload,current_carrier_sha256=current_carrier_sha)\n        parents.append(dict(record=record,payload=payload,terminal=terminal,\n            model_binding=model_binding,family=family,inbound=inbound,");
 replace("    manifest = [Path(path).resolve() for path in args.manifest]\n    for path in paths:",`    manifest = [Path(path).resolve() for path in args.manifest]
    for parent in parents:
        for item in parent['inbound']:
            path=Path(item['record']['path']).resolve()
            if item['kind']!='complete_preparation' and path not in manifest:
                manifest.append(path)
    for path in paths:`);
 replace("        locations.walk(payload,path=('complete_source_bound_envelope_parent',))\n        locations.resolve_grid",`        locations.walk(payload,path=('complete_source_bound_envelope_parent',))
        for item in parent['inbound']:
            if item['kind']!='complete_preparation':
                locations.walk(item['payload'],path=('complete_source_bound_inbound_history',))
        locations.resolve_grid`);
 replace("            actual_typed_memory_count=len(rows),actual_typed_memory_sha256=canonical(rows),",`            complete_inbound_history_records=[dict(record=item['record'],kind=item['kind']) for item in parent['inbound']],
            inherited_prior_transfer_metadata=copy.deepcopy(payload.get('material_envelope_transfer')),
            complete_original_role_arrays=copy.deepcopy(old_arrays),
            complete_original_typed_rows=copy.deepcopy(rows),
            complete_grid_identity_sha256=canonical(old['implicit_grid']),
            actual_typed_memory_count=len(rows),actual_typed_memory_sha256=canonical(rows),`);
 replace("        actual_current_driver_sha256=caller_record['sha256'],\n        actual_current_model_identity_sha256=q.identity,\n        actual_current_base_model_identity_sha256=q.base.identity,",`        actual_current_driver_sha256=caller_record['sha256'],
        actual_current_driver_source=copy.deepcopy(caller_record),
        actual_current_model_identity_sha256=q.identity,
        actual_current_base_model_identity_sha256=q.base.identity,`);
 replace("    raise ValueError('An old-target final cannot be relabelled as this fixed Fejer field; the complete same-source restart retains its own thirteen members')\n    if checkpoint is None", "    if checkpoint is None");
 const familyOld="    family=_parent_family(payload.get('source_sha256'),payload)\n    pure = _old_reader(topic,family).read_report(args.repo,report_path,verify_final_bundle=True)";
 replace(familyOld,"    family=_parent_family(payload.get('source_sha256'),payload)\n    if family.get('complete_final_variable_copy_supported') is not True:\n        raise ValueError('A previous-target final is not a same-target complete Fejer variable seed')\n    pure = _old_reader(topic,family).read_report(args.repo,report_path,verify_final_bundle=True)");
 replace("    return copy.deepcopy(value)\n\n\ndef validate_metadata", "    _reread_seed(value,report,model,transfer)\n    return copy.deepcopy(value)\n\n\ndef validate_metadata");
 replace("    return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=expected,\n        actual_current_model_identity_sha256=canonical(model),","    _reread_transfer_parents(value,model,envelope,caller_source_sha256,carrier_sha256)\n    return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=expected,\n        actual_current_model_identity_sha256=canonical(model),");
 const reread=`def _reread_transfer_parents(value,model,envelope,caller_source_sha256,carrier_sha256):
    """Read the original whole parent and every original inbound history at pure-read time."""
    source=value.get('actual_current_driver_source',{})
    _same_bytes(source)
    if source.get('sha256')!=caller_source_sha256:
        raise ValueError('Bind the entire actual caller source before reading its parent chain')
    source_path=Path(source['path']).resolve()
    topic=source_path.parents[2]
    pins=_literal_assignments(source_path.read_bytes())['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1]!=sha(__file__)
            or pins.get('independent_envelope_memory',(None,None))[1]!=CURRENT_MEMORY_SOURCE_SHA256):
        raise ValueError('The actual full caller does not bind this complete stage-point transfer')
    for relative,expected in pins.values():
        if sha(topic/relative)!=expected:
            raise ValueError('An actual current source changed during complete parent validation')
    arrays=value['complete_initial_explicit_address_union']
    current_sets={role:{_point(row) for row in arrays[role]} for role in ADDRESS_ROLES}
    for item in value['actual_parent_reports']:
        record=item['report'];_same_bytes(record)
        payload=json.loads(Path(record['path']).read_bytes())
        family=_parent_family(payload.get('source_sha256'),payload)
        if family.get('same_predeclared_fixed_fejer_target') is not True:
            raise ValueError('Only the complete explicitly bound same-target Fejer parent may transfer')
        pure=_old_reader(topic,family).read_report(topic.parent.parent,Path(record['path']),verify_final_bundle=False)
        if (pure.get('report_sha256')!=record['sha256']
                or _terminal(payload)!=item['actual_terminal_report_kind']
                or payload.get('N')!=2048 or payload.get('J')!=model['J']
                or payload.get('observation_carrier_sha256')!=carrier_sha256
                or canonical(payload['representation'])!=item['actual_model_identity_sha256']
                or _compatible_models(payload['representation'],model,pins)!=item['model_binding']
                or payload.get('material_envelope_transfer')!=item.get('inherited_prior_transfer_metadata')
                or payload['material_envelope']['actual_separation_memory']['rows']!=item.get('complete_original_typed_rows')
                or payload['material_envelope']['definition']!=envelope['definition']
                or payload['material_envelope']['implicit_grid']!=envelope['implicit_grid']
                or item.get('complete_grid_identity_sha256')!=canonical(envelope['implicit_grid'])):
            raise ValueError('The actual whole parent target, complete grid, roles, typed records or unresolved lineage changed')
        inbound=_complete_input_reports(payload,current_carrier_sha256=carrier_sha256)
        expected=[dict(record=v['record'],kind=v['kind']) for v in inbound]
        if expected!=item.get('complete_inbound_history_records'):
            raise ValueError('Keep every actual inbound history file in its original order')
        old_arrays=item.get('complete_original_role_arrays')
        if _address_fingerprints(old_arrays)!=item.get('actual_complete_walker_role_fingerprints'):
            raise ValueError('Keep the whole original explicit/protected material sets')
        for role in ADDRESS_ROLES:
            if not {_point(row) for row in old_arrays[role]}<=current_sets[role]:
                raise ValueError('An original explicit/protected material address was lost')
        _same_bytes(record)
    _same_bytes(source)


def _reread_seed(value,report,model,transfer):
    """The original complete pure reader rereads the real whole thirteen-member final."""
    record=value['source_report'];checkpoint=value['source_checkpoint']
    _same_bytes(record);_same_bytes(checkpoint)
    payload=json.loads(Path(record['path']).read_bytes())
    family=_parent_family(payload.get('source_sha256'),payload)
    if family.get('complete_final_variable_copy_supported') is not True:
        raise ValueError('Keep the explicitly supported same-target original complete final')
    source=transfer['actual_current_driver_source'];_same_bytes(source)
    topic=Path(source['path']).resolve().parents[2]
    pure=_old_reader(topic,family).read_report(topic.parent.parent,Path(record['path']),verify_final_bundle=True)
    if (pure.get('report_sha256')!=record['sha256']
            or pure.get('actual_final_bundle_sha256')!=checkpoint['sha256']
            or payload.get('final_bundle_sha256')!=checkpoint['sha256']
            or payload.get('complete') is not True
            or payload.get('model_identity_sha256')!=value['source_complete_model_identity_sha256']
            or payload.get('latest_operator_metadata',{}).get('current_full_point_sha256')!=value['actual_full_free_point_sha256']
            or payload.get('final_geometry',{}).get('current_full_point_sha256')!=value['actual_full_free_point_sha256']):
        raise ValueError('The actual full parent final, complete variable words and recorded point differ')
    _same_bytes(record);_same_bytes(checkpoint);_same_bytes(source)

`;
 const tail="\n"+helpers.completeInputs+"\n"+helpers.inputIdentity+"\n"+reread;
 text+=tail;patches.push({append:tail});
 return {role:"envelope_transfer",name:"transfer_fixed_fejer_stage_point_memory.py",text,patches,...hash(text),parent:{name:parent.name,sha256:parent.sha256,bytes:parent.bytes,git_blob_sha:parent.git_blob_sha}};
}
function buildHotUpper(upper,lowerParents,lower,currentPins,hash) {
 const outputs={},patches=[];
 function rewrite(role,name,changes){
  let text=upper[role].text;const ps=[];
  for(const [before,after,count=1] of changes){const n=text.split(before).length-1;if(n!==count)throw Error(role+" "+n+" != "+count+" "+before.slice(0,110));text=text.split(before).join(after);ps.push({before,after,count});}
  const o={role,name,text,...hash(text),parent:{name:upper[role].name,sha256:upper[role].sha256,bytes:upper[role].bytes,git_blob_sha:upper[role].git_blob_sha}};
  outputs[role]=o;patches.push({role,patches:ps});return o;
 }
 const geometry=rewrite("geometry","so3_fixed_fejer_stage_point_geometry.py",[
  [lowerParents.stage_matrices.sha256,lower.stage_matrices.sha256],
  [lowerParents.adjacent_matrices.sha256,lower.adjacent_matrices.sha256],
  [lowerParents.endpoint.sha256,lower.endpoint.sha256]]);
 const replacements={...lower,geometry};
 const pins=JSON.parse(JSON.stringify(currentPins));
 const aliases={root_packets:"root_packets",stage_matrices:"stage_matrices",adjacent_matrices:"adjacent_matrices",
  endpoint:"endpoint",analytic_J3_binding:"binding",envelope_transfer:"envelope_transfer",geometry:"geometry"};
 for(const [role,alias] of Object.entries(aliases)){
  const old=pins[role];pins["stage_point_parent_"+alias]=old;
  const r=replacements[role];if(!r)throw Error("replacement absent "+role);
  pins[role]=["scripts/resume_20261126/"+r.name,r.sha256];
 }
 pins.stage_point_parent_driver=["scripts/resume_20261126/"+upper.driver.name,upper.driver.sha256];
 pins.stage_point_parent_reader=["scripts/resume_20261126/"+upper.reader.name,upper.reader.sha256];
 const sourceLine=upper.driver.text.match(/^SOURCE_PINS = .+$/m)[0];
 const emit="SOURCE_PINS = {"+Object.entries(pins).map(([k,v])=>JSON.stringify(k)+":("+JSON.stringify(v[0])+","+JSON.stringify(v[1])+")").join(",")+"}";
 const oldSchema="complete-fixed-fejer-immutable-point-material-envelope-SO3-QP-v1";
 const schema="complete-fixed-fejer-stage-point-material-envelope-SO3-QP-v1";
 const originalGuard="    if (args.moment_input_binding!='supported-smooth-triangle-reference'\n            or args.seed_so3_checkpoint is not None or args.material_envelope_seed_checkpoint is not None\n            or args.material_envelope_parent_report):\n        raise ValueError('The predeclared new target uses its explicit current-base literal Q and either the genuine reference or its complete same-source restart')";
 const newGuard="    if (args.moment_input_binding!='supported-smooth-triangle-reference'\n            or args.seed_so3_checkpoint is not None):\n        raise ValueError('Use the unchanged current-base literal Q; the separate complete transfer binds any actual same-Fejer parent')";
 const driver=rewrite("driver","fullclosed_fixed_fejer_stage_point_so3_qp.py",[[sourceLine,emit],[oldSchema,schema],[originalGuard,newGuard],
  ["        new_zero_closure_seed_changes_physical_field=restart is None,",
   "        new_zero_closure_seed_changes_physical_field=(None if prior_final_seed is not None else restart is None),"]]);
 const launcher=rewrite("launcher","launch_fixed_fejer_stage_point_actions.py",[[upper.driver.sha256,driver.sha256],[upper.driver.name,driver.name]]);
 const reader=rewrite("reader","read_fixed_fejer_stage_point_so3_report.py",[[upper.driver.sha256,driver.sha256],[upper.driver.name,driver.name],[oldSchema,schema],["actual-fixed-fejer-immutable-point-envelope-SO3-readout-v1","actual-fixed-fejer-stage-point-envelope-SO3-readout-v1"]]);
 const suffix=t=>t.slice(t.indexOf("    def save_report("));
 if(suffix(driver.text)!==suffix(upper.driver.text))throw Error("full scientific suffix changed");
 for(const pair of Object.values(currentPins))if(!Object.values(pins).some(p=>p[0]===pair[0]&&p[1]===pair[1]))throw Error("lost original parent pair "+pair[0]);
 return {outputs,patches,pins,report_schema:schema,full_scientific_suffix:hash(suffix(driver.text))};
}
function forwardAndInverse(parent,patches,expected){
 let text=parent;const trace=[];
 for(const p of patches){
  if(p.append!==undefined){trace.push({append:p.append,start:text.length});text+=p.append;continue;}
  if(!p.before)throw Error('A complete exact old source fragment is required');
  const positions=[];let cursor=0,at;while((at=text.indexOf(p.before,cursor))>=0){positions.push(at);cursor=at+p.before.length;}
  if(positions.length!==p.count)throw Error('Whole original patch multiplicity differs');
  const finalPositions=positions.map((x,j)=>x+j*(p.after.length-p.before.length));
  text=text.split(p.before).join(p.after);trace.push({before:p.before,after:p.after,positions:finalPositions});
 }
 if(text!==expected)throw Error('Whole forward source text differs');
 for(const p of trace.reverse()){
  if(p.append!==undefined){if(text.slice(p.start)!==p.append)throw Error('Appended complete source changed');text=text.slice(0,p.start);continue;}
  for(const at of p.positions.slice().reverse()){
   if(text.slice(at,at+p.after.length)!==p.after)throw Error('Exact inverse source fragment changed');
   text=text.slice(0,at)+p.before+text.slice(at+p.after.length);
  }
 }
 if(text!==parent)throw Error('Whole inverse original source differs');
 return true;
}
function reproduceAll(inputs){
 const lower=inputs.lower,upper=inputs.upper,templates=inputs.complete_parent_bridge_templates;
 const line=upper.driver.text.match(/^SOURCE_PINS = .+$/m);
 if(!line)throw Error('Keep the original complete literal source table');
 const pins=JSON.parse(line[0].slice('SOURCE_PINS = '.length).replaceAll('(','[').replaceAll(')',']'));
 if(Object.keys(pins).length!==110)throw Error('Keep every original Fejer source role');
 const stage=buildStage(lower.stage_matrices);Object.assign(stage,hash(stage.text));
 const low=buildHotLower(lower,stage,hash);
 const binding=buildHotBinding(upper.binding,lower,low.outputs,
  ex(templates.binding.text,'_validate_original_parent_model'),hash);
 const transfer=buildHotTransfer(upper.transfer,binding,upper,
  {completeInputs:ex(templates.transfer.text,'_complete_input_reports'),
   inputIdentity:ex(templates.transfer.text,'_input_identity')},hash);
 const high=buildHotUpper(upper,lower,{...low.outputs,analytic_J3_binding:binding,envelope_transfer:transfer},pins,hash);
 const outputs={...low.outputs,analytic_J3_binding:binding,envelope_transfer:transfer,...high.outputs};
 const changes={stage_matrices:stage.patches,analytic_J3_binding:binding.patches,
  envelope_transfer:transfer.patches,...Object.fromEntries([...low.patches,...high.patches].map(v=>[v.role,v.patches]))};
 const parents={...lower,...upper,analytic_J3_binding:upper.binding,envelope_transfer:upper.transfer};
 if(Object.keys(outputs).length!==10||Object.keys(high.pins).length!==119)
  throw Error('Keep the complete ten changed sources and all 119 source roles');
 for(const[role,item]of Object.entries(outputs)){
  const wanted=EXPECTED[role];
  if(item.name!==wanted.name||item.bytes!==wanted.bytes||item.sha256!==wanted.sha256||item.bytes>=100000)
   throw Error('Whole independently named source differs: '+role);
  forwardAndInverse(parents[role].text,changes[role],item.text);
 }
 return {outputs,pins:high.pins,scientific_suffix:high.full_scientific_suffix,changes};
}
function readFull(directory,record){
 const file=path.join(directory,record.name),raw=fs.readFileSync(file),text=raw.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(raw)||raw.length!==record.bytes||hash(text).sha256!==record.sha256)
  throw Error('The entire immutable source changed: '+record.name);
 return {...record,text};
}
function main(argv){
 const options={};
 for(let i=0;i<argv.length;i+=2){
  if(!['--source-directory','--generated-directory'].includes(argv[i])||argv[i+1]===undefined||options[argv[i]])
   throw Error('Supply the two complete directory options exactly once');
  options[argv[i]]=path.resolve(argv[i+1]);
 }
 const directory=options['--source-directory'],out=options['--generated-directory'];
 if(!directory||!out||directory===out||out.startsWith(directory+path.sep)||fs.existsSync(out))
  throw Error('Keep complete parent sources and use a separate fresh destination');
 const actual=Object.fromEntries(Object.entries(INPUTS).map(([group,records])=>[group,
  Object.fromEntries(Object.entries(records).map(([role,record])=>[role,readFull(directory,record)]))]));
 const result=reproduceAll(actual);
 for(const records of Object.values(INPUTS))for(const record of Object.values(records))readFull(directory,record);
 fs.mkdirSync(out,{recursive:true});
 for(const item of Object.values(result.outputs))fs.writeFileSync(path.join(out,item.name),item.text,{encoding:'utf8',flag:'wx'});
 console.log(JSON.stringify({complete:true,changed_complete_runtime_sources:10,complete_source_roles:119,
  all_original_110_source_pairs_retained:true,all_whole_forward_and_inverse_texts_match:true,
  entire_scientific_suffix:result.scientific_suffix,
  original_scientific_values_and_budgets_changed:false,Python_AST_or_compile:false,
  scientific_execution:false,source_reproduction_is_not_an_admission_gate:true}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
