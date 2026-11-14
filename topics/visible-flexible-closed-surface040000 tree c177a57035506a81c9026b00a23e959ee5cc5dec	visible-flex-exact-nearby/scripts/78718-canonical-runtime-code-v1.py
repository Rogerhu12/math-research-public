#!/usr/bin/env python3
"""Typed CodeType identity for the separately named restart8000 entry.

Standard library only.  This encodes code values, not marshal reference/intern
layout.  It neither executes compiled code nor installs or calls any solver.
Original raw runtime records and the old selector's namespace/closure checks
remain mandatory; this is an additional, explicitly named source/code gate.
"""
import hashlib
import json
import marshal
from pathlib import Path
import struct
import sys
from types import CodeType, FunctionType

SCHEMA = '78718-typed-runtime-code-v1'
FIELDS = ('co_argcount', 'co_posonlyargcount', 'co_kwonlyargcount', 'co_nlocals',
          'co_stacksize', 'co_flags', 'co_code', 'co_consts', 'co_names',
          'co_varnames', 'co_filename', 'co_name', 'co_qualname', 'co_firstlineno',
          'co_linetable', 'co_exceptiontable', 'co_freevars', 'co_cellvars',
          'co_lnotab')
RAW_KEYS = {'module', 'qualname', 'filename', 'firstlineno', 'code_sha256'}
ROW_KEYS = {'schema', 'runtime', 'source', 'canonical_code_sha256', 'environment'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def serial(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode('ascii')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': sha(raw)}


def environment():
    require(sys.implementation.name == 'cpython' and sys.version_info[:2] == (3, 12),
            'This reviewed code-field schema is for CPython 3.12 only')
    require(sys.flags.optimize == 0, 'An optimized compiler was not reviewed')
    return {'implementation': sys.implementation.name, 'sys_version': sys.version,
            'sys_executable': sys.executable, 'optimization': sys.flags.optimize,
            'marshal_version_for_raw_record_only': marshal.version,
            'compiler_dont_inherit': True}


def value_tree(value):
    """Injective typed value encoding on the explicitly accepted constant domain.

    No repr(), numerical comparison, or NaN equality is used.  Float and complex
    components retain all 64 IEEE bits, including NaN payload and zero sign.
    Unknown values reject instead of being converted to strings.
    """
    t = type(value)
    if value is None:
        return ['none']
    if value is Ellipsis:
        return ['ellipsis']
    if t is bool:
        return ['bool', value]
    if t is int:
        return ['int', str(value)]
    if t is float:
        return ['float64', struct.pack('>d', value).hex()]
    if t is complex:
        return ['complex128', struct.pack('>dd', value.real, value.imag).hex()]
    if t is str:
        return ['str', value]
    if t is bytes:
        return ['bytes', value.hex()]
    if t is tuple:
        return ['tuple', [value_tree(item) for item in value]]
    if t is frozenset:
        members = [value_tree(item) for item in value]
        members.sort(key=serial)
        return ['frozenset', members]
    if t is CodeType:
        return ['code', [[name, value_tree(getattr(value, name))] for name in FIELDS]]
    raise ValueError('Unreviewed code-constant type: ' + t.__name__)


def code_bytes(code):
    require(type(code) is CodeType, 'Expected a CodeType')
    environment()
    # co_lines and co_positions are deterministic decoders of co_linetable;
    # co_lnotab is nevertheless included explicitly as a derived public field.
    public = {name for name in dir(code) if name.startswith('co_')}
    require(public == set(FIELDS) | {'co_lines', 'co_positions'},
            'Unexpected public CodeType field; update requires a new review')
    return serial([SCHEMA, value_tree(code)])


def code_digest(code):
    return sha(code_bytes(code))


def compiled_function(path, filename, qualname):
    """Compile pinned bytes without executing the module or any callback."""
    environment()
    require(type(filename) is str and str(Path(path).resolve()) == filename,
            'Compile filename must be the exact absolute pinned source path')
    code = compile(Path(path).read_bytes(), filename, 'exec', dont_inherit=True, optimize=0)
    for name in (part for part in qualname.split('.') if part != '<locals>'):
        matches = [item for item in code.co_consts
                   if type(item) is CodeType and item.co_name == name]
        require(len(matches) == 1, 'Ambiguous source code object: ' + qualname)
        code = matches[0]
    require(code.co_qualname == qualname, 'Compiled qualified name differs')
    return code


def raw_function(function):
    require(type(function) is FunctionType, 'Expected a Python function')
    code = function.__code__
    return {'module': function.__module__, 'qualname': function.__qualname__,
            'filename': code.co_filename, 'firstlineno': code.co_firstlineno,
            'code_sha256': sha(marshal.dumps(code))}


def check_record(row, raw, path, qualname, module):
    """Closed check of a recorded live code against pinned source compilation."""
    require(type(row) is dict and set(row) == ROW_KEYS and row['schema'] == SCHEMA,
            'Incomplete typed code record')
    require(type(raw) is dict and set(raw) == RAW_KEYS, 'Incomplete original raw code record')
    require(row['runtime'] == raw, 'Canonical record is detached from original raw identity')
    require(row['environment'] == environment(), 'Runtime/compiler environment differs')
    require(row['source'] == identity(path), 'Canonical source byte binding differs')
    require(raw['filename'] == str(Path(path).resolve()) and raw['qualname'] == qualname
            and raw['module'] == module and type(raw['firstlineno']) is int,
            'Runtime source/module/name/line identity differs')
    code = compiled_function(path, raw['filename'], qualname)
    require(raw['firstlineno'] == code.co_firstlineno, 'Runtime first line differs')
    require(row['canonical_code_sha256'] == code_digest(code),
            'Typed runtime code differs from pinned source')
    return True


def capture(function, raw):
    """Capture the actual live object, retaining and cross-checking raw evidence."""
    require(raw_function(function) == raw, 'Live function differs from selector raw record')
    row = {'schema': SCHEMA, 'runtime': dict(raw), 'source': identity(raw['filename']),
           'canonical_code_sha256': code_digest(function.__code__),
           'environment': environment()}
    check_record(row, raw, raw['filename'], raw['qualname'], raw['module'])
    return row


def capture_selection(selection, raw_record):
    """Inspect already-selected function objects only; no numerical calls."""
    functions = {}
    for name, function in selection.originals.items():
        functions['original.' + name] = (function, raw_record['original_runtime'][name])
    for name, function in selection.foundation_functions.items():
        functions['foundation.' + name] = (function, raw_record['foundation_helper_runtime'][name])
    for name in ('prepare_sys', 'construct_global_jac'):
        functions['selected.' + name] = (getattr(selection.functions, name), raw_record['selected_runtime'][name])
    functions['newton.solve_newton'] = (selection.newton, raw_record['newton_runtime_unchanged'])
    require(set(functions) == {
        'original.prepare_sys', 'original.construct_global_jac', 'original.compute_jac_indices',
        'original.solve_bvp', 'foundation.dimensions', 'foundation.column_segments',
        'foundation._assemble_csc', 'selected.prepare_sys', 'selected.construct_global_jac',
        'newton.solve_newton'}, 'Unexpected selected code closure')
    return {name: capture(function, raw) for name, (function, raw) in sorted(functions.items())}
