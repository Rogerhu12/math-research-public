#!/usr/bin/env python3
"""Explicit runtime selection of the reviewed direct canonical CSC prepare_sys.

Import defines standard-library helpers only. Only select_prepare_sys() mutates
one SciPy namespace attribute; it never calls prepare_sys, a Jacobian, Newton,
SuperLU, a candidate callback, or a solver. The complete new entry must supply
closed real prerequisite reports. Original exported construct_global_jac and
compute_jac_indices remain untouched; the selected prepare captures the new
constructor. Release-LU Newton is selected and audited separately.
"""
import ast
import copy
import hashlib
import importlib.util
import marshal
import sys
from pathlib import Path
from types import CodeType, FunctionType, ModuleType

HERE = Path(__file__).resolve().parent
GATES = HERE / 'db6f-prefix-direct-csc-entry-gates.py'
GATES_SHA = 'd110a15669612ae75207d98b46b8ee31c41d5f98dc8a9b693a06a4cbc399606b'
FOUNDATION = HERE / 'db6f-prefix-direct-csc-foundation-v2.py'


def _load_gates():
    raw=GATES.read_bytes()
    if hashlib.sha256(raw).hexdigest() != GATES_SHA:
        raise ValueError('Changed direct-CSC prerequisite gate')
    value=ModuleType('db6f_direct_csc_entry_metadata_gate_v1')
    value.__file__=str(GATES.resolve())
    exec(compile(raw,str(GATES.resolve()),'exec',dont_inherit=True),vars(value))
    return value


def definition_identity():
    """Only pinned bytes and source AST; no scientific imports or installation."""
    gate=_load_gates()
    return {'schema':'db6f-explicit-direct-csc-selection-definitions-v1',
            'selector':gate.identity(__file__),'gates':gate.identity(GATES),
            'foundation_definitions':gate.source_definitions(),
            'selected_attribute':'scipy.integrate._bvp.prepare_sys',
            'original_exported_constructor_retained':True,
            'newton_not_selected_or_changed_here':True}


def runtime_identity(function):
    if not isinstance(function,FunctionType):
        raise ValueError('Expected a Python function')
    return {'module':function.__module__,'qualname':function.__qualname__,
            'filename':function.__code__.co_filename,'firstlineno':function.__code__.co_firstlineno,
            'code_sha256':hashlib.sha256(marshal.dumps(function.__code__)).hexdigest()}


def _closure(function):
    names=function.__code__.co_freevars
    cells=function.__closure__ or ()
    if len(names) != len(cells):
        raise ValueError('Unexpected closure extent')
    return dict(zip(names,(cell.cell_contents for cell in cells)))


def _original_function(backend,compiled,name,defaults):
    gate=_load_gates()
    found=[value for value in compiled.co_consts
           if isinstance(value,CodeType) and value.co_name == name]
    function=getattr(backend,name)
    gate.require(len(found)==1 and isinstance(function,FunctionType)
                 and function.__code__ == found[0]
                 and function.__globals__ is vars(backend)
                 and function.__closure__ is None and function.__kwdefaults__ is None,
                 'Original runtime code/namespace changed: '+name)
    # Defaults contain only None/int/float values in this pinned original.
    gate.equal(function.__defaults__,defaults,'Original defaults changed: '+name)
    return function


def _load_foundation(gate):
    """Compile verified source under a new honest runtime module label."""
    gate.require(gate.RUNTIME_MODULE not in sys.modules,'CSC runtime module label is already used')
    raw=FOUNDATION.read_bytes()
    gate.require(hashlib.sha256(raw).hexdigest()==gate.FOUNDATION_SHA,'Changed CSC foundation')
    module=ModuleType(gate.RUNTIME_MODULE)
    module.__file__=str(FOUNDATION.resolve())
    sys.modules[gate.RUNTIME_MODULE]=module
    try:
        exec(compile(raw,str(FOUNDATION.resolve()),'exec',dont_inherit=True),vars(module))
    except BaseException:
        sys.modules.pop(gate.RUNTIME_MODULE,None)
        raise
    return module


class Selection:
    """The one selected prepare identity and its original replacement target."""
    def __init__(self,backend,spectral,foundation,functions,originals,evidence,gate):
        self.backend=backend
        self.spectral=spectral
        self.foundation=foundation
        self.functions=functions
        self.originals=originals
        self.evidence=copy.deepcopy(evidence)
        self.gate=gate
        self.active=False
        self.newton=backend.solve_newton
        self.newton_identity=runtime_identity(self.newton)
        self.definitions=definition_identity()
        self.provenance=copy.deepcopy(functions.provenance)
        self.original_records={name:runtime_identity(function)
                               for name,function in originals.items()}
        self.foundation_functions={name:getattr(foundation,name)
                                   for name in ('dimensions','column_segments','_assemble_csc')}
        self.foundation_records={name:runtime_identity(function)
                                 for name,function in self.foundation_functions.items()}
        self.prepare_cells=_closure(functions.prepare_sys)
        self.construct_cells=_closure(functions.construct_global_jac)
        gate.require(set(self.prepare_cells)=={
            'collocation_fun','construct_global_jac','estimate_bc_jac','estimate_fun_jac'},
            'New prepare closure differs or retains unwanted global arrays')
        gate.require(set(self.construct_cells)=={
            'csc_matrix','get_index_dtype','np','stacked_matmul'},'New constructor closure differs')
        gate.require(self.prepare_cells['construct_global_jac'] is functions.construct_global_jac,
                     'New prepare does not capture the new constructor')
        csc=self.construct_cells['csc_matrix']
        self.csc_class=csc
        self.csc_methods={name:getattr(csc,name) for name in
                         ('__init__','check_format','prune','_get_index_dtype','_swap')}
        self.method_records={name:runtime_identity(fn) for name,fn in self.csc_methods.items()}
        self.backend_refs={name:getattr(backend,name) for name in
                           ('np','csc_matrix','stacked_matmul','collocation_fun',
                            'estimate_fun_jac','estimate_bc_jac')}
        self.eps=backend.EPS

    def _check_shared(self):
        gate=self.gate
        gate.equal(definition_identity(),self.definitions,'CSC selection sources changed')
        gate.equal(self.functions.provenance,self.provenance,'Factory snapshot was mutated')
        gate.equal(gate.normalized_provenance(self.provenance,gate.RUNTIME_MODULE),
                   gate.normalized_provenance(
                       self.evidence['tested_factory_provenance'],gate.TEST_MODULE),
                   'Fresh runtime source/callback/environment differs from real byte test')
        for name,function in self.originals.items():
            if name != 'prepare_sys':
                gate.require(getattr(self.backend,name) is function,
                             'Original exported function was replaced: '+name)
            gate.equal(runtime_identity(function),self.original_records[name],
                       'Original exported function code changed: '+name)
        gate.require(self.backend.solve_newton is self.newton,
                     'Newton identity changed while CSC was selected')
        gate.equal(runtime_identity(self.newton),self.newton_identity,'Newton code changed')
        gate.require(self.spectral.scipy_bvp is self.backend
                     and self.spectral.scipy_solve_bvp is self.originals['solve_bvp'],
                     'W14 callable no longer invokes the original SciPy solve_bvp')
        for name,function in self.foundation_functions.items():
            gate.require(getattr(self.foundation,name) is function,
                         'Foundation storage helper was replaced: '+name)
            gate.equal(runtime_identity(function),self.foundation_records[name],
                       'Foundation helper code changed: '+name)
        for name,function in self.backend_refs.items():
            gate.require(getattr(self.backend,name) is function,
                         'Original numeric/callback reference changed: '+name)
        gate.equal(self.backend.EPS,self.eps,'Original finite-difference EPS changed')
        for name,function in self.csc_methods.items():
            gate.require(getattr(self.csc_class,name) is function,'CSC class method replaced')
            gate.equal(runtime_identity(function),self.method_records[name],'CSC class method code changed')
        for function,cells in ((self.functions.prepare_sys,self.prepare_cells),
                               (self.functions.construct_global_jac,self.construct_cells)):
            gate.require(function.__globals__ is vars(self.foundation)
                         and function.__defaults__ is None and function.__kwdefaults__ is None,
                         'New function namespace/defaults changed')
            current=_closure(function)
            gate.require(set(current)==set(cells) and
                         all(current[name] is value for name,value in cells.items()),
                         'New function closure changed')
        for name,function in (('prepare_sys',self.functions.prepare_sys),
                              ('construct_global_jac',self.functions.construct_global_jac)):
            gate.equal(runtime_identity(function),self.provenance['new_functions'][name],
                       'New runtime code identity changed')
        # Captured original helper code is independently visible in provenance.
        for name in ('collocation_fun','estimate_fun_jac','estimate_bc_jac'):
            gate.equal(runtime_identity(self.prepare_cells[name]),
                       self.provenance['original_callbacks'][name],'Captured callback code changed')
        for name in ('stacked_matmul','get_index_dtype'):
            gate.equal(runtime_identity(self.construct_cells[name]),
                       self.provenance['original_callbacks'][name],'Captured matrix helper code changed')

    def check(self):
        gate=self.gate
        gate.require(self.active and self.backend.prepare_sys is self.functions.prepare_sys,
                     'Explicit direct-CSC prepare selection is absent or changed')
        self._check_shared()
        return {'schema':'db6f-explicit-direct-csc-runtime-v1',
                'definitions':self.definitions,
                'prerequisite_inputs':self.evidence['inputs'],
                'tested_factory_normalized_sha256':self.evidence['tested_factory_normalized_sha256'],
                'factory_provenance':copy.deepcopy(self.provenance),
                'original_runtime':copy.deepcopy(self.original_records),
                'selected_runtime':copy.deepcopy(self.provenance['new_functions']),
                'foundation_helper_runtime':copy.deepcopy(self.foundation_records),
                'newton_runtime_unchanged':copy.deepcopy(self.newton_identity),
                'only_backend_prepare_attribute_changed':True,
                'old_exported_construct_and_indices_retained':True,
                'no_old_global_coo_index_closure':True,
                'scope':'Runtime identity only; no assertion of a BVP result or peak memory.'}

    def restore(self):
        """Restore only this prepare selection. Never restore/change Newton here."""
        before=self.check()
        self.backend.prepare_sys=self.originals['prepare_sys']
        self.active=False
        self.gate.require(self.backend.prepare_sys is self.originals['prepare_sys'],
                          'Original prepare was not restored')
        self._check_shared()
        return {'schema':'db6f-explicit-direct-csc-restoration-v1',
                'before_restore':before,
                'restored_original_prepare':runtime_identity(self.backend.prepare_sys),
                'newton_runtime_unchanged':runtime_identity(self.backend.solve_newton),
                'backend_prepare_restored':True,
                'scope':'Process-local prepare restored; original release-LU Newton identity retained.'}


def select_prepare_sys(backend,spectral,evidence):
    """Future explicit selection; no matrices or callbacks are evaluated."""
    gate=_load_gates()
    checked=gate.verify_prerequisites(evidence)
    gate.require(backend.__name__=='scipy.integrate._bvp','Wrong SciPy backend')
    gate.require(gate.identity(backend.__file__)['sha256']==gate.BVP_SHA,'Changed SciPy BVP source')
    compiled=compile(Path(backend.__file__).read_bytes(),str(backend.__file__),'exec',dont_inherit=True)
    originals={name:_original_function(backend,compiled,name,defaults) for name,defaults in (
        ('prepare_sys',None),('construct_global_jac',None),('compute_jac_indices',None),
        ('solve_bvp',(None,None,None,None,1e-3,1000,0,None)))}
    gate.require(spectral.scipy_bvp is backend and spectral.scipy_solve_bvp is originals['solve_bvp'],
                 'W14 does not retain the original dynamic-global solve_bvp')
    foundation=_load_foundation(gate)
    try:
        functions=foundation.make_functions(backend)
        gate.equal(gate.normalized_provenance(functions.provenance,gate.RUNTIME_MODULE),
                   gate.normalized_provenance(checked['tested_factory_provenance'],gate.TEST_MODULE),
                   'Fresh factory is not the actually tested source/environment')
        selection=Selection(backend,spectral,foundation,functions,originals,checked,gate)
        # This is the sole SciPy namespace mutation in this module.
        backend.prepare_sys=functions.prepare_sys
        selection.active=True
        try:
            selection.check()
        except BaseException:
            if backend.prepare_sys is functions.prepare_sys:
                backend.prepare_sys=originals['prepare_sys']
            selection.active=False
            raise
    except BaseException:
        sys.modules.pop(gate.RUNTIME_MODULE,None)
        raise
    return selection
