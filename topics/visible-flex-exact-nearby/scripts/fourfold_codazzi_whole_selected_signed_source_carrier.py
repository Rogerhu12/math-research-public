"""True whole-domain signed Newton and parameter forcing in the original 577 rows."""
from bisect import bisect_right
from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path
import struct


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def partition(helper, rows, base, direction):
    knots = [Fraction.from_float(float(x)) for x in base["radial_nodes"]]
    require(len(knots) == 6145 and
            knots == [Fraction.from_float(float(x)) for x in direction["radial_nodes"]]
            and all(x<y for x,y in zip(knots,knots[1:])), "both original complete one-sided cubics")
    bounds = [tuple(map(Fraction,r["interval"])) for r in rows]
    ends = [b for _,b in bounds]
    require(len(ends) == 7721 and all(a<b for a,b in bounds) and
            all(x==y for x,(y,_) in zip(ends[:-1],bounds[1:]))
            and bounds[0][0] == knots[0] == 0 and ends[-1] == knots[-1] == helper.OUTER,
            "all 7721 consecutive original scalar rows from the waist to the actual outer end")
    cuts = sorted({*knots,*ends,*helper.CONTROL,*helper.ROOT,helper.NEGATIVE_CUT,
                   helper.POSITIVE_CUT,Fraction(17,20),Fraction(9,10),Fraction(19,20)})
    output = []
    for lo,hi in zip(cuts,cuts[1:]):
        j,k = bisect_right(ends,lo),bisect_right(knots,lo)-1
        require(bounds[j][0] <= lo < hi <= bounds[j][1] and knots[k] <= lo < hi <= knots[k+1],
                "every coefficient and derivative uses its own original one-sided piece")
        output.append((j,k,lo,hi))
    return output


def historical_ball(flint, record):
    value = (flint.arb(record["lower"]).lower().union(flint.arb(record["upper"]).upper())
             if "lower" in record and "upper" in record else flint.arb(record["ball"]))
    require(value.is_finite(),"finite original whole scientific interval")
    return value


def compact_fields(c,tc,helper,whole,K,gamma,lo,hi,read):
    """Signed intrinsic increments and actual parameter derivatives; no finite differences."""
    a,b = helper.CONTROL
    zero = tc.BatchRadialFourier.scalar(c,[0.])
    if hi <= a or lo >= b:
        return K,gamma,zero,zero,zero,zero
    require(a<=lo<hi<=b,"no compact support seam inside a source interval")
    def as_field(value):
        return tc.BatchRadialFourier.scalar(c,[c.arb_box(value)])
    x = c.exact((lo-a)/(b-a)).union(c.exact((hi-a)/(b-a)))
    W = 4096*x**6*(1-x)**6
    Wp = 24576*x**5*(1-x)**5*(1-2*x)/c.exact(b-a)
    original_a,original_g = read(whole["a"]),read(whole["gamma"])
    require(original_a.lower()>0 and original_g.lower()>0,"two actual compact metric reciprocals")
    L = read(whole["beta"])*Wp/(2*(original_a*original_g)**2)
    delta = c.exact(-helper.DELTA).union(c.exact(helper.DELTA))
    e = delta*W
    dK = K*as_field((-e).expm1())+as_field(delta*(-e).exp()*L)
    actual_K = K+dK
    actual_g = gamma*as_field((e/2).exp())
    dKn = as_field((-e).exp())*(as_field(L)-as_field(W)*(K+as_field(delta*L)))
    dJ12 = gamma*as_field((-e/2).exp())*(as_field(L)-as_field(W/2)*(K+as_field(delta*L)))
    dJ21 = -actual_g*as_field(W/2)
    return actual_K,actual_g,dK,dKn,dJ12,dJ21


def signed_pair(c,tc,positive,helper,base,direction,offsets,row,piece,lo,hi,read):
    if lo >= helper.ROOT[0]:
        return positive.whole_polynomials(c,tc,helper,base,direction,offsets,row,piece,lo,hi,read)
    scalar = {name:tc.scalar_taylor(c,row["intrinsic_midpoint_jets"],row["intrinsic_whole_third_jets"],
                    name,*row["interval"],lo,hi,read) for name in ("K","gamma","s","beta")}
    beta,s = scalar["beta"],scalar["s"]
    K,gamma,dK,Kn,J12n,J21n = compact_fields(c,tc,helper,row["intrinsic_whole_third_jets"],
                                               scalar["K"],scalar["gamma"],lo,hi,read)
    (u0,w0),(ur0,wr0) = positive.cubic_pair(c,tc,helper,base,offsets["base"],piece,lo,hi,"base")
    (a,b),(ar,br) = positive.cubic_pair(c,tc,helper,direction,offsets["direction"],piece,lo,hi,"direction")
    delta = tc.BatchRadialFourier.scalar(c,[c.arb_box(c.exact(-helper.DELTA).union(c.exact(helper.DELTA)))])
    u,w = u0+delta*a,w0+delta*b
    v = s+w
    up,vp = u.derivative(),v.derivative()
    S,m = u*u+K*v*v,v.mean()
    drift = -beta*S.primitive()
    # s satisfies the rotational equation for ORIGINAL K. The radial source
    # retains the extra genuine term -(K_delta-K0)s^3 on the compact support.
    F0 = (drift*up+gamma*m*K*vp-beta*u*(1+S)-ur0-delta*ar,
          drift*vp-gamma*m*up+beta*(w-u*u*v-K*w*(v*v+v*s+s*s)-dK*s*s*s)-wr0-delta*br)
    operator = tc.prepare_operator((u,v),{**scalar,"K":K,"gamma":gamma})
    Az = tc.apply_operator(operator,(a,b))
    v2 = v*v
    primitive = v2.primitive()
    Fnu = (-beta*Kn*(primitive*up+v2*u)+m*J12n*vp,
           -beta*Kn*(primitive*vp+v2*v)+m*J21n*up)
    F1 = (Az[0]+Fnu[0]-ar,Az[1]+Fnu[1]-br)
    require(all(field.degree <= 288 for pair in (F0,F1) for field in pair),
            "all signed sources fit the genuine cubic support")
    return F0,F1


COLUMNS = ("ordinary_Newton_minus_f_delta","ordinary_nu_proposal_defect_s_delta")
BYTES_PER_CELL = 577*2*2*8
MAGIC = b"R149-SIGNED-577x2-v1\n"


def packed_pairs(c,positive,pairs):
    columns = []
    for pair in pairs:
        odd,mean,even = positive.whole_signed_rows(c,pair)
        columns.append([odd[j] for j in range(288)]+[mean]+[even[j] for j in range(288)])
    payload = bytearray()
    for first,second in zip(*columns):
        for value in (first,second):
            low,high = float(value.lo),float(value.hi)
            require(math.isfinite(low) and math.isfinite(high) and low<=high,"finite signed coefficients")
            payload.extend(struct.pack("<dd",low,high))
    require(len(payload)==BYTES_PER_CELL,"complete normalized 577 by 2 coefficient box")
    return bytes(payload)


def endpoint_pair(c,positive,pair):
    """Only called on exact radial POLYNOMIAL carriers; read both signed scalar means."""
    fields = []
    for p in pair:
        f = p[1]
        z = f.Fourier()[0:1].real
        error = float(c.np.max(f.error.hi))
        for endpoint in (-1,1):
            v = z[0,-1,0]
            for k in range(z.lo.shape[1]-2,-1,-1):
                v = endpoint*v+z[0,k,0]
            v = v+c.Box(-error,error)
            fields.extend((float(v.lo),float(v.hi)))
    require(len(fields)==8 and all(math.isfinite(x) for x in fields),"all four one-sided mean observations")
    return fields


class SignedSourceStore:
    """Fresh private signed two-column carriers, precise whole definition at each read."""
    def __init__(self, directory, plan):
        self.directory,self.plan = Path(directory),plan
        self.directory.mkdir(parents=True,exist_ok=False)
        self.records = {}
        self.ends = [hi for _,_,_,hi in plan]

    def put(self,index,payload,means):
        require(index not in self.records and len(payload)==BYTES_PER_CELL and len(means)==8,
                "one new complete raw signed piece")
        row,piece,lo,hi = self.plan[index]
        record = {"index":index,"row":row,"piece":piece,"interval":[str(lo),str(hi)],
                  "columns":list(COLUMNS),"rows":577,"even_mean_index":288}
        head = canonical(record)
        raw = MAGIC+struct.pack("<I",len(head))+head+struct.pack("<8d",*means)+payload
        path = self.directory/(str(index)+".signed")
        require(not path.exists(),"fresh whole private source piece")
        tmp = path.with_suffix(".partial")
        tmp.write_bytes(raw)
        tmp.replace(path)
        require(path.read_bytes()==raw,"whole new source piece write/readback")
        self.records[index] = dict(bytes=len(raw),sha256=sha256(raw).hexdigest())

    def get(self,index):
        raw = (self.directory/(str(index)+".signed")).read_bytes()
        spec = self.records[index]
        require(len(raw)==spec["bytes"] and sha256(raw).hexdigest()==spec["sha256"] and raw.startswith(MAGIC),
                "whole signed source piece on every subsequent use")
        offset = len(MAGIC)
        size = struct.unpack_from("<I",raw,offset)[0]
        offset += 4
        header = json.loads(raw[offset:offset+size])
        row,piece,lo,hi = self.plan[index]
        require(header=={"index":index,"row":row,"piece":piece,"interval":[str(lo),str(hi)],
                         "columns":list(COLUMNS),"rows":577,"even_mean_index":288},
                "full original source interval, both signs, all rows and actual mean")
        offset += size
        endpoints = struct.unpack_from("<8d",raw,offset)
        payload = raw[offset+64:]
        require(len(payload)==BYTES_PER_CELL,"entire new source payload")
        return endpoints,payload

    def receipt(self):
        require(set(self.records)==set(range(len(self.plan))),"complete whole original domain")
        digest = sha256(b"R149-SIGNED-all-contiguous-source-cells-v1")
        size = 0
        for i in range(len(self.plan)):
            self.get(i)
            rec = self.records[i]
            size += rec["bytes"]
            digest.update(canonical([i,rec]))
        return {"whole_private_piece_count":len(self.plan),"complete_index_sha256":digest.hexdigest(),
                "whole_file_bytes":size,"complete_domain":["0","25/8"],"physical_source_rows":577,
                "source_columns":list(COLUMNS),"new_arrays_published":False}


class PhysicalBoxReader:
    """Authentic whole signed source boxes on the true positive or negative domain."""
    source_roles = ()
    column_names = COLUMNS

    def __init__(self,store,expected,api,km,domain,rows,read_ball):
        require(store.receipt()==expected,"no source exposed before the entire original carrier matches")
        self.store,self.api,self.km,self.domain = store,api,km,domain
        self.rows,self.read_ball = rows,read_ball
        self.bounds = [tuple(map(Fraction,r["interval"])) for r in rows]
        self.ends = [b for _,b in self.bounds]
        self.cached = None

    def full(self,box):
        if self.cached and box==self.cached[0]:
            return self.cached[1]
        lo,hi = self.domain.exact_physical_cover(box)
        require(0<=lo<hi<=self.store.ends[-1],"whole physical source interval")
        i = bisect_right(self.store.ends,lo)
        cursor,pairs = lo,None
        while cursor<hi:
            row,piece,left,right = self.store.plan[i]
            stop = min(right,hi)
            require(left<=cursor<stop,"all physical source pieces with no gap")
            _,payload = self.store.get(i)
            values = list(struct.iter_unpack("<dd",payload))
            if pairs is None:
                pairs = values
            else:
                pairs = [(min(a,c),max(b,d)) for (a,b),(c,d) in zip(pairs,values)]
            cursor,i = stop,i+1
        a = self.api
        raw = [a.interval(a.arb(x),a.arb(y)) for x,y in pairs]
        result = self.km.Matrix(577,2,[raw[2*i:2*i+2] for i in range(577)])
        self.cached = box,result
        return result

    def __call__(self,box):
        m = self.full(box)
        return self.km.Matrix(193,2,m.values[:96]+m.values[288:385])
