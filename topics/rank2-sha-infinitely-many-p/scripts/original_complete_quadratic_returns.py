#!/usr/bin/env sage-python
"""Faithful full quadratic polynomial returns for the original thick ideals."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematics only in the public research Actions.")

import ast
import hashlib
import inspect
from collections import OrderedDict
from copy import copy
from pathlib import Path
import original_ys_divisor_ideal_tools as divisor
import original_ys_artinian_norm_tools as norm
import original_projector_hermite as projector

HERE=Path(__file__).resolve().parent
PINNED={
    "original_ys_divisor_ideal_tools.py":"661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7",
    "original_ys_artinian_norm_tools.py":"f604ae5f862519f5ccdce609a78ef05866fd85ae81ea699fb1de06f47b550714",
    "original_projector_hermite.py":"545b330c4b7fb0c876e15f0ea6b94c9e35d29fdaf94b87707b3853dd33c32545",
}
SOURCE_DEPENDENCIES=(
    "original_complete_quadratic_polynomials.pyx",
    "original_complete_quadratic_returns.py",
)+tuple(PINNED)
NATIVE=None
PREPARED=None
BOUND=False
# Transient in-process representations only; never serialized or reused by a later run.
COMPLETE_MATRIX_CACHE=OrderedDict()
CACHE_HITS=0
CACHE_REFRESHES=0
ORIGINAL_REMAINDER=divisor._hermite_remainder_rows
ORIGINAL_COORDINATES=norm._whole_hermite_coordinates
ORIGINAL_PROJECTOR=projector.complete_projector_ideal
ORIGINAL_SPARSE_PRODUCT=projector._sparse_left_product

def prepare_backend():
    """Compile declarations only; run no arithmetic instance."""
    global NATIVE,PREPARED
    if PREPARED is not None:
        return dict(PREPARED)
    for name,expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected
    from sage.misc.cython import cython_import
    source=HERE/"original_complete_quadratic_polynomials.pyx"
    NATIVE=cython_import(str(source),verbose=0,compile_message=False,use_cache=True,
        annotate=False,sage_namespace=False,create_local_c_file=False,
        create_local_so_file=False)
    PREPARED={
        "kind":"complete-original-quadratic-polynomial-preparation",
        "pinned_source_sha256":PINNED,
        "native_source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "adapter_source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "native_metadata":NATIVE.backend_metadata(),
        "mathematical_instances_executed":0,
        "source_file_or_data_written":False,
    }
    return dict(PREPARED)

def _supported(R):
    k=R.base_ring()
    return int(k.degree())==2 and 3<=int(k.characteristic())<2**31

def _complete_native_matrix(M):
    """Cache all entries, with a fresh exact equality check on every use."""
    global CACHE_HITS,CACHE_REFRESHES
    key=id(M)
    item=COMPLETE_MATRIX_CACHE.get(key)
    if item is not None and item[0] is M and item[1]==M:
        COMPLETE_MATRIX_CACHE.move_to_end(key)
        CACHE_HITS+=1
        return item[2]
    snapshot=copy(M)
    snapshot.set_immutable()
    native=NATIVE.CompleteQuadraticMatrix(M.base_ring(),snapshot)
    COMPLETE_MATRIX_CACHE[key]=(M,snapshot,native)
    COMPLETE_MATRIX_CACHE.move_to_end(key)
    while len(COMPLETE_MATRIX_CACHE)>4:
        COMPLETE_MATRIX_CACHE.popitem(last=False)
    CACHE_REFRESHES+=1
    return native

def complete_product(A,B):
    prepare_backend()
    if _supported(A.base_ring()):
        return NATIVE.complete_product(A,_complete_native_matrix(B))
    return A*B

def complete_remainder_rows(rows,H):
    prepare_backend()
    if _supported(H.base_ring()):
        return NATIVE.complete_remainder_rows(rows,_complete_native_matrix(H))
    return ORIGINAL_REMAINDER(rows,H)

def complete_hermite_coordinates(H,rows):
    prepare_backend()
    if _supported(H.base_ring()):
        assert H.is_hermite()
        return NATIVE.complete_hermite_coordinates(_complete_native_matrix(H),rows)
    return ORIGINAL_COORDINATES(H,rows)

def bind_original_returns():
    """Bind exact operations; every original full return identity is retained."""
    global BOUND
    metadata=prepare_backend()
    if BOUND:
        return dict(metadata,already_bound=True)
    import sys
    # Replace existing aliases only when their identity is the pinned original.
    # Restrict this to the topic's loaded original modules.  Future imports from
    # divisor/norm see these same wrappers.
    aliases=[]
    for name,module in list(sys.modules.items()):
        if module is None or not name.startswith("original_"):
            continue
        for attr,old,new in (
            ("_hermite_remainder_rows",ORIGINAL_REMAINDER,complete_remainder_rows),
            ("_whole_hermite_coordinates",ORIGINAL_COORDINATES,complete_hermite_coordinates)):
            if getattr(module,attr,None) is old:
                setattr(module,attr,new)
                aliases.append(name+"."+attr)
    projector._sparse_left_product=complete_product
    source=inspect.getsource(ORIGINAL_PROJECTOR)
    old="    assert C*primary.basis+HMc == H"
    new="    assert _complete_original_product(C, primary.basis)+HMc == H"
    assert source.count(old)==1
    source=source.replace(old,new)
    ast.parse(source)
    namespace=dict(vars(projector))
    namespace["_complete_original_product"]=complete_product
    exec(compile(source,str(HERE/"original_complete_quadratic_returns.py")+
                 ":pinned-full-projector","exec"),namespace)
    projector.complete_projector_ideal=namespace["complete_projector_ideal"]
    BOUND=True
    return dict(metadata,aliases=aliases,projector_exact_text_replacements=1,
        exact_generated_projector_sha256=hashlib.sha256(source.encode()).hexdigest(),
        full_reverse_identity_H_equals_CI_plus_H_one_minus_e_retained=True,
        native_original_constant_embedding_retained=True,
        any_original_acceptance_gate_removed=False)
