"""Preserve only the paid part of an interrupted original working Jacobian."""
import base64
import hashlib
import json
import time
import zlib
import numpy as np
from r566_working_rows_full_acceptance_20261126 import WorkingRows, check_time, selected_point_rows, hard


def packed(v):
    b=np.ascontiguousarray(v,dtype='<f8').tobytes()
    return {"float64_values":len(b)//8,"little_endian_sha256":hashlib.sha256(b).hexdigest(),
            "zlib_base64":base64.b64encode(zlib.compress(b,3)).decode('ascii')}


class InterruptedRows(WorkingRows):
    def jac(self,value):
        value=np.asarray(value,dtype=float)
        self.fun(value)
        if self.jacobian is not None:
            return self.jacobian
        started=time.monotonic()
        answer=np.empty((len(self.rows),self.size+1))
        complete=[]
        try:
            for batch,(oracle,rows,descriptors,points) in enumerate(self.batches):
                for first in range(0,self.size,self.args.block_directions):
                    check_time(self.deadline)
                    stop=min(first+self.args.block_directions,self.size)
                    columns=np.arange(first,stop)
                    state=oracle.prepare(value[:-1],columns)
                    fields=oracle.evaluate(state,points)
                    reconstructed,derivative,extra=selected_point_rows(fields,descriptors,self.par,
                        self.geo,self.phase,float(value[-1]),len(columns))
                    error=float(np.max(abs(reconstructed-self.values[rows])))
                    self.counts["maximum_block_value_difference"]=max(self.counts["maximum_block_value_difference"],error)
                    if error>1e-12*max(1.,float(np.max(abs(self.values[rows])))):
                        raise ArithmeticError("restricted radial AD changed the actual row or value")
                    answer[np.ix_(rows,columns)]=derivative
                    if first==0:
                        answer[rows,-1]=extra
                    self.counts["direction_blocks"]+=1
                    complete.append((batch,first,stop))
                    oracle.release()
        except hard.EndSegment:
            # Complete blocks have actual values and exact row order. Never read
            # unfilled memory or write the original FFT/AD trajectories.
            blocks=[]
            for batch,first,stop in complete:
                rows=self.batches[batch][1]
                cols=np.arange(first,stop)
                data=answer[np.ix_(rows,cols)].ravel()
                if first==0:
                    data=np.r_[data,answer[rows,-1]]
                blocks.append(data)
            descriptors=json.dumps(self.rows,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
            receipt={"schema":"r692-actual-unfinished-working-derivative-prefix-v1","x":value.tolist(),
                "row_order_canonical_json_sha256":hashlib.sha256(descriptors).hexdigest(),
                "phase":self.phase,"batches_row_indices":[rows.tolist() for _,rows,_,_ in self.batches],
                "actual_complete_working_values":packed(self.values),"completed_batch_first_stop":complete,
                "packed_row_major_derivatives_then_if_first_zero_epigraph_vector":
                    packed(np.concatenate(blocks) if blocks else np.empty(0)),
                "elapsed_unfinished_J_seconds":time.monotonic()-started,"complete_J":False,
                "no_native_QP_or_physical_acceptance_inferred":True}
            hard.emit("R692_ACTUAL_UNFINISHED_WORKING_DERIVATIVE_PREFIX",receipt)
            raise
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError("nonfinite working Jacobian")
        self.jacobian=answer
        self.counts["complete_jacobians"]+=1
        seconds=time.monotonic()-started
        self.counts["jacobian_seconds"]+=seconds
        hard.emit("WORKING_ROWS_JACOBIAN",{"rows":len(self.rows),"columns":self.size+1,
            "sub_radial_batches":len(self.batches),"largest_sub_radial_grid":max(o.uniform.nr for o,_,_,_ in self.batches),
            "FFT_nodes_each_ring":1536,"full_physical_constraint_count_not_replaced_by_working_row_count":True,
            "seconds":seconds,"counts":self.counts})
        return answer
