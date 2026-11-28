"""Both signed ordinary forcing columns for the same selected positive WVC member.

Input scalar jets and cubic arrays are the original TC carriers.  This module
performs no computation at import and never calls a residual-norm producer.
"""
from fractions import Fraction


def require(ok, message):
    if not ok:
        raise ValueError(message)


def cubic_pair(c, tc, helper, saved, offsets, piece, left, right, name):
    """Complete physical value and derivative polynomial, excluding the rotational mean."""
    alpha = helper.ALPHA if name == "base" else Fraction(1)
    knot, end = (Fraction.from_float(float(saved["radial_nodes"][i])) for i in (piece, piece+1))
    require(knot <= left < right <= end, "whole restriction inside exactly one original cubic")
    half = (right-left)/2
    raw = saved["piece_coefficients"][:,piece,:][::-1]
    size = 65 if name == "base" else 193
    require(raw.shape == (4,size), "all four exact stored coefficient vectors")
    coeffs = [c.Box(row.reshape(-1,1))*c.box(alpha) for row in raw]
    coeffs[0] = coeffs[0]+c.Box(offsets["lower"][piece,:,None],offsets["upper"][piece,:,None])
    coeffs = c.affine_polynomial(coeffs,(left+right)/2-knot,half)
    if name == "base":
        expanded = []
        for value in coeffs:
            low,high = c.np.zeros((193,1)),c.np.zeros((193,1))
            for start,stop,source in ((0,32,slice(0,32)),(96,97,slice(32,33)),(97,129,slice(33,65))):
                low[start:stop],high[start:stop] = value.lo[source],value.hi[source]
            expanded.append(c.Box(low,high))
        coeffs = expanded
    # Differentiate the original exact polynomial before Fourier conversion,
    # since conversion or a scalar Taylor remainder cannot be differentiated.
    derivative = [coeffs[k]*(k*c.box(1/half)) for k in range(1,4)]
    zero = tc.BatchRadialFourier.scalar(c,[0.])
    return (tc.unnormalized_background(c,coeffs,zero),
            tc.unnormalized_background(c,derivative,zero))


def whole_polynomials(c, tc, helper, base, direction, offsets, row, piece, left, right, read_ball):
    left,right = Fraction(left),Fraction(right)
    require(left >= helper.ROOT[0] > helper.CONTROL[1] and left < right,
            "positive root cover, fixed intrinsic outside compact control")
    scalar = {n:tc.scalar_taylor(c,row["intrinsic_midpoint_jets"],row["intrinsic_whole_third_jets"],
                               n,*row["interval"],left,right,read_ball) for n in ("beta","K","gamma","s")}
    beta,K,gamma,s = (scalar[n] for n in ("beta","K","gamma","s"))
    (u,w),(ur,wr) = cubic_pair(c,tc,helper,base,offsets["base"],piece,left,right,"base")
    (a,b),(ar,br) = cubic_pair(c,tc,helper,direction,offsets["direction"],piece,left,right,"direction")
    v = s+w
    # s' = beta*s*(1-K*s^2), the exact rotational Codazzi equation.
    # F2-s' uses the full signed factorization of v^3-s^3.
    S = u*u+K*v*v
    linear_S = 2*(u*a+K*v*b)
    quadratic_S = a*a+K*b*b
    d0,d1,d2 = (-beta*h.primitive() for h in (S,linear_S,quadratic_S))
    m,n = v.mean(),b.mean()
    up,vp,ap,bp = (h.derivative() for h in (u,v,a,b))
    F0 = (d0*up+gamma*m*K*vp-beta*u*(1+S)-ur,
          d0*vp-gamma*m*up+beta*(w-u*u*v-K*w*(v*v+v*s+s*s))-wr)
    F1 = (d0*ap+d1*up+gamma*K*(m*bp+n*vp)-beta*(a*(1+S)+u*linear_S)-ar,
          d0*bp+d1*vp-gamma*(m*ap+n*up)+beta*(b*(1-S)-v*linear_S)-br)
    F2 = (d2*up+d1*ap+gamma*n*K*bp-beta*(a*linear_S+u*quadratic_S),
          d2*vp+d1*bp-gamma*n*ap-beta*(b*linear_S+v*quadratic_S))
    F3 = (d2*ap-beta*a*quadratic_S,d2*bp-beta*b*quadratic_S)
    delta = tc.BatchRadialFourier.scalar(c,[c.box(c.exact(-helper.DELTA).union(c.exact(helper.DELTA)))])
    newton = tuple(p0+delta*(p1+delta*(p2+delta*p3)) for p0,p1,p2,p3 in zip(F0,F1,F2,F3))
    nu = tuple(p1+delta*(2*p2+3*delta*p3) for p1,p2,p3 in zip(F1,F2,F3))
    require(all(v.degree <= 288 for pair in (newton,nu) for v in pair),
            "all signed cubic Fourier outputs 0 through 288")
    return newton,nu


def whole_signed_rows(c, pair):
    """Signed normalized physical rows through288, including one independent mean."""
    def range_box(field, component):
        values = getattr(field.Fourier(),component)
        coordinate = c.Box(-1.,1.)
        out = values[:289,-1,0]
        for k in range(values.lo.shape[1]-2,-1,-1):
            out = out*coordinate+values[:289,k,0]
        # One uniform Wiener error controls the absolute error of each coefficient.
        error = float(c.np.max(field.error.hi))
        return c.finite(out+c.Box(-error,error))
    odd,even = range_box(pair[0],"imag"),range_box(pair[1],"real")
    scale = c.arb_box(c.arb(2).sqrt())
    return -scale*odd[1:289],even[0],scale*even[1:289]


class WholePositiveSignedProvider:
    """Intersect each true physical box with every original row and repaired cubic it meets."""
    source_roles = ()
    column_names = ("ordinary_Newton_minus_f_delta", "ordinary_nu_proposal_defect_s_delta")

    def __init__(self, c, tc, helper, base, direction, offsets, rows, read_ball, api, km, domain):
        self.c,self.tc,self.helper,self.base,self.direction = c,tc,helper,base,direction
        self.offsets,self.rows,self.read_ball = offsets,rows,read_ball
        self.api,self.km,self.domain = api,km,domain
        self.knots = [Fraction.from_float(float(v)) for v in base["radial_nodes"]]
        self.bounds = [(Fraction(r["interval"][0]),Fraction(r["interval"][1])) for r in rows]
        self.ends = [b for _,b in self.bounds]
        require(len(self.knots) == 6145 and len(self.bounds) == 7721
                and c.np.array_equal(base["radial_nodes"],direction["radial_nodes"])
                and all(a < b for a,b in zip(self.knots,self.knots[1:]))
                and self.bounds[0][0] == self.knots[0] == 0
                and self.ends[-1] == self.knots[-1] == helper.OUTER
                and all(a < b for a,b in self.bounds)
                and all(a == b for a,(b,_) in zip(self.ends[:-1],self.bounds[1:])),
                "all original radial row/cubic junctions")
        self.cached = None

    def _piece(self, row, piece, left, right):
        pairs = whole_polynomials(self.c,self.tc,self.helper,self.base,self.direction,
                                  self.offsets,self.rows[row],piece,left,right,self.read_ball)
        columns = []
        for pair in pairs:
            odd,mean,even = whole_signed_rows(self.c,pair)
            # All 577 physical rows first. Select low193 only when requested.
            def arb_value(box):
                return self.api.interval(self.api.arb(float(box.lo)),self.api.arb(float(box.hi)))
            columns.append([arb_value(odd[j]) for j in range(288)]+[arb_value(mean)]
                           +[arb_value(even[j]) for j in range(288)])
        return [list(row) for row in zip(*columns)]

    def full(self, box):
        from bisect import bisect_right
        if self.cached and self.cached[0] == box:
            return self.cached[1]
        left,right = self.domain.exact_physical_cover(box)
        require(left < right and self.helper.ROOT[0] <= left and right <= self.helper.OUTER,
                "whole positive cell forcing domain")
        piece,row = bisect_right(self.knots,left)-1,bisect_right(self.ends,left)
        current,combined = left,None
        while current < right:
            end = min(right,self.knots[piece+1],self.ends[row])
            require(current < end and self.bounds[row][0] <= current, "unbroken signed source cover")
            values = self._piece(row,piece,current,end)
            if combined is None:
                combined = values
            else:
                combined = [[a.union(b) for a,b in zip(x,y)] for x,y in zip(combined,values)]
            current = end
            if current == self.knots[piece+1]:
                piece += 1
            if current == self.ends[row]:
                row += 1
        answer = self.km.Matrix(577,2,combined)
        self.cached = (box,answer)
        return answer

    def __call__(self, box):
        value = self.full(box)
        return self.km.Matrix(193,2,value.values[:96]+value.values[288:385])


class WholeSignedBoxCache:
    """One private full 577-by-2 enclosure per physical source box, used by both sweeps."""
    source_roles = ()

    def __init__(self, provider, directory):
        import hashlib
        from pathlib import Path
        self.provider,self.api,self.km,self.domain = provider,provider.api,provider.km,provider.domain
        self.column_names = provider.column_names
        self.directory = Path(directory)
        self.directory.mkdir(parents=True,exist_ok=False)
        self.ends,self.bounds,self.rows,self.read_ball = provider.ends,provider.bounds,provider.rows,provider.read_ball
        self.records = {}
        self.chain = hashlib.sha256(b"original_selected_signed_sources_577x2_v1").hexdigest()

    def full(self, box):
        import hashlib
        import math
        import struct
        def dyadic(value, upper):
            v = float(value)
            require(math.isfinite(v),"finite full signed source endpoint")
            for _ in range(4):
                x = self.api.arb(v)
                if (x >= value if upper else x <= value):
                    return v
                v = math.nextafter(v,math.inf if upper else -math.inf)
            raise ValueError("directed endpoint packing")
        panel,lo,hi = box
        label = "%d-%d_%d-%d_%d"%(panel,lo.numerator,lo.denominator,hi.numerator,hi.denominator)
        path = self.directory/(label+".pair")
        if box not in self.records:
            matrix = self.provider.full(box)
            raw = b"".join(struct.pack("<dd",dyadic(x.lower(),False),dyadic(x.upper(),True))
                           for row in matrix.values for x in row)
            require(len(raw) == 577*2*16 and not path.exists(),"one whole signed source enclosure")
            temp = path.with_suffix(".tmp")
            temp.write_bytes(raw)
            temp.replace(path)
            digest = hashlib.sha256(raw).hexdigest()
            self.records[box] = digest
            self.chain = hashlib.sha256(bytes.fromhex(self.chain)+label.encode()+b"\0"+bytes.fromhex(digest)).hexdigest()
        raw = path.read_bytes()
        require(len(raw) == 577*2*16 and hashlib.sha256(raw).hexdigest() == self.records[box],
                "whole signed source hash on every read")
        it = (self.api.interval(self.api.arb(a),self.api.arb(b)) for a,b in struct.iter_unpack("<dd",raw))
        return self.km.Matrix(577,2,[[next(it),next(it)] for _ in range(577)])

    def __call__(self, box):
        matrix = self.full(box)
        return self.km.Matrix(193,2,matrix.values[:96]+matrix.values[288:385])
