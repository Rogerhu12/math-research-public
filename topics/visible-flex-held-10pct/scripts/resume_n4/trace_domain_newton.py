"""Observe the existing domain Newton without changing arithmetic or decisions.

Call install(path) after f6curve_domain_newton.install(). All original function
arguments and return objects pass through unchanged. JSONL records identify
where wall time is spent and retain the original acceptance/rejection counters.
This is a diagnostic hook; it neither resumes nor changes a running solve.
"""
import hashlib
import json
from pathlib import Path
import time


def install(path):
    import f6curve_domain_newton as original
    import scipy.integrate._bvp as scipy_bvp
    target=Path(path);target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():raise FileExistsError('Do not mix Newton traces: '+str(target))
    state=dict(newton_calls=0,phase_calls={})
    started=time.monotonic()
    def emit(event,**fields):
        row=dict(event=event,elapsed=time.monotonic()-started,
                 newton_call=state['newton_calls'],stats=dict(original.STATS),**fields)
        with target.open('a')as out:out.write(json.dumps(row,separators=(',',':'))+'\n')
    emit('installed',source_sha256=hashlib.sha256(Path(original.__file__).read_bytes()).hexdigest(),
         observer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    def observe(kind,fn):
        def call(*args,**kwargs):
            number=state['phase_calls'].get(kind,0)+1;state['phase_calls'][kind]=number
            begin=time.monotonic();emit(kind+'_start',number=number)
            try:result=fn(*args,**kwargs)
            except BaseException as exc:
                emit(kind+'_exception',number=number,seconds=time.monotonic()-begin,error=repr(exc));raise
            emit(kind+'_end',number=number,seconds=time.monotonic()-begin)
            return result
        return call
    def solve_newton(n,m,h,col_fun,bc,jac,y,p,B,bvp_tol,bc_tol):
        state['newton_calls']+=1
        emit('newton_start',equations=n,nodes=m,parameters=len(p),
             p0=float(p[0]),p1=float(p[1])if len(p)>1 else None)
        begin=time.monotonic()
        try:
            result=original.solve_newton(n,m,h,observe('collocation',col_fun),
                observe('boundary',bc),observe('jacobian',jac),y,p,B,bvp_tol,bc_tol)
        except BaseException as exc:
            emit('newton_exception',seconds=time.monotonic()-begin,error=repr(exc));raise
        emit('newton_end',seconds=time.monotonic()-begin,singular=bool(result[2]),
             p0=float(result[1][0]),p1=float(result[1][1])if len(result[1])>1 else None)
        return result
    original_splu=original.splu
    original.splu=observe('sparse_lu',original_splu)
    scipy_bvp.solve_newton=solve_newton
    return state
