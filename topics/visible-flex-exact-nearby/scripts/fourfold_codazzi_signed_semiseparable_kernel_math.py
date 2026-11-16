"""Complete signed continuous-kernel algebra for the W2C candidate.

No entry point, file access, numerical producer import, or scientific execution.
Every field encloses a function on an entire radial box.  A box is never a
quadrature sample.  The owner supplies directed scalar/matrix arithmetic and
a complete finite partition with the genuine variable root as its left end.

All angular coordinates are the actual normalized real parity coordinates:
mean basis 1; nonmean sine/cosine basis sqrt(2).  No complex-space enlargement
is used to invoke the old high inverse.  Independent affine and boundary
ports are retained by the owner, not identified with the reference ports.
"""


def require(ok, message):
    if not ok:
        raise ValueError(message)


class Matrix:
    """A shape-preserving signed interval matrix, including zero-rank factors."""
    def __init__(self, rows, cols, values):
        require(type(rows) is int and type(cols) is int and rows >= 0 and cols >= 0,
                "finite nonnegative matrix dimensions")
        require(len(values) == rows and all(len(row) == cols for row in values),
                "complete matrix shape")
        self.rows, self.cols = rows, cols
        self.values = values

    @property
    def shape(self):
        return self.rows, self.cols


def zeros(api, rows, cols):
    return Matrix(rows, cols, [[api.zero for _ in range(cols)] for _ in range(rows)])


def eye(api, rows, cols=None):
    cols = rows if cols is None else cols
    return Matrix(rows, cols, [[api.one if i == j else api.zero
                               for j in range(cols)] for i in range(rows)])


def add(api, *matrices):
    require(len(matrices) > 0, "nonempty complete signed sum")
    shape = matrices[0].shape
    require(all(x.shape == shape for x in matrices), "same signed sum shape")
    return Matrix(*shape, [[sum((x.values[i][j] for x in matrices), api.zero)
                           for j in range(shape[1])] for i in range(shape[0])])


def scale(api, value, matrix):
    return Matrix(matrix.rows, matrix.cols,
                  [[value * x for x in row] for row in matrix.values])


def transpose(matrix):
    return Matrix(matrix.cols, matrix.rows,
                  [[matrix.values[i][j] for i in range(matrix.rows)]
                   for j in range(matrix.cols)])


def multiply(api, left, right):
    require(left.cols == right.rows, "ordered signed product")
    if left.rows == 0 or right.cols == 0 or left.cols == 0:
        return zeros(api, left.rows, right.cols)
    if hasattr(api, "matrix_product"):
        value = api.matrix_product(left.values, right.values)
        return Matrix(left.rows, right.cols, value)
    return Matrix(left.rows, right.cols,
                  [[sum((left.values[i][k] * right.values[k][j]
                         for k in range(left.cols)), api.zero)
                    for j in range(right.cols)] for i in range(left.rows)])


def product(api, *matrices):
    require(len(matrices) > 0, "nonempty ordered product")
    result = matrices[0]
    for matrix in matrices[1:]:
        result = multiply(api, result, matrix)
    return result


def hcat(*matrices):
    require(len(matrices) > 0 and all(x.rows == matrices[0].rows for x in matrices),
            "complete horizontal factors")
    return Matrix(matrices[0].rows, sum(x.cols for x in matrices),
                  [sum((x.values[i] for x in matrices), [])
                   for i in range(matrices[0].rows)])


def vcat(*matrices):
    require(len(matrices) > 0 and all(x.cols == matrices[0].cols for x in matrices),
            "complete vertical factors")
    return Matrix(sum(x.rows for x in matrices), matrices[0].cols,
                  sum((x.values for x in matrices), []))


def hull(api, *matrices):
    require(len(matrices) > 0 and all(x.shape == matrices[0].shape for x in matrices),
            "complete signed matrix hull")
    rows, cols = matrices[0].shape
    return Matrix(rows, cols,
                  [[api.hull([x.values[i][j] for x in matrices])
                    for j in range(cols)] for i in range(rows)])


class Field:
    """Signed matrix-valued function, never a stored norm differentiated later."""
    def __init__(self, domain, rows, cols, evaluate, label, identically_zero=False):
        self.domain = domain
        self.rows, self.cols = rows, cols
        self.evaluate = evaluate
        self.label = label
        self.identically_zero = bool(identically_zero)

    def at(self, box):
        self.domain.validate_box(box)
        result = self.evaluate(box)
        require(isinstance(result, Matrix) and result.shape == (self.rows, self.cols),
                "whole matrix field: " + self.label)
        return result


def zero_field(domain, rows, cols, label):
    return Field(domain, rows, cols,
                 lambda box: zeros(domain.api, rows, cols), label, True)


def constant_field(domain, matrix, label):
    return Field(domain, matrix.rows, matrix.cols, lambda box: matrix, label)


def sum_field(label, *fields):
    require(len(fields) > 0, "nonempty field sum")
    first = fields[0]
    require(all(f.domain is first.domain and (f.rows, f.cols) == (first.rows, first.cols)
                for f in fields), "one domain and one actual coordinate shape")
    return Field(first.domain, first.rows, first.cols,
                 lambda box: add(first.domain.api, *(f.at(box) for f in fields)),
                 label, all(f.identically_zero for f in fields))


def scaled_field(value, field, label):
    return Field(field.domain, field.rows, field.cols,
                 lambda box: scale(field.domain.api, value, field.at(box)),
                 label, field.identically_zero)


def product_field(label, *fields):
    require(len(fields) > 0, "nonempty field product")
    domain = fields[0].domain
    require(all(f.domain is domain for f in fields) and
            all(fields[i].cols == fields[i+1].rows for i in range(len(fields)-1)),
            "ordered same-domain fields")
    return Field(domain, fields[0].rows, fields[-1].cols,
                 lambda box: product(domain.api, *(f.at(box) for f in fields)),
                 label, any(f.identically_zero for f in fields))


def transposed_field(field, label):
    return Field(field.domain, field.cols, field.rows,
                 lambda box: transpose(field.at(box)), label, field.identically_zero)


class WholePanelIntegral:
    """Exact inclusion by complete interval integration, with signed moments.

    domain.cells refines the genuine reference/S seams, collar cut, and cutoff
    joins. Every original coefficient piece is covered either by a split or by
    the verified whole-cell hull of all its closed intersections. domain supplies
    whole_cell_box(i), full_length(i), partial_box(box, direction),
    partial_length(box, direction), cell_index(box), and ordered_span(left,right).
    These return enclosures of the actual integration sets and lengths, including
    the unknown genuine root.  No interval endpoint is substituted for that root.

    A full panel integral is enclosed by its true length times the WHOLE range
    enclosure of the integrand.  The same rule handles a variable partial panel.
    A replacement backend may use a sharper proved integration rule, but must
    preserve these mathematical sets.  Prefix and suffix are computed separately;
    suffix is never an upper-bound subtraction from a full integral.
    """
    def __init__(self, field, label):
        self.field, self.domain, self.api = field, field.domain, field.domain.api
        self.label = label
        self.full_cache = {}
        self.prefix_cache = {0: zeros(self.api, field.rows, field.cols)}
        self.suffix_cache = {len(self.domain.cells): zeros(self.api, field.rows, field.cols)}

    def _enclose(self, box, length):
        require(self.api.lower(length) >= 0, "true nonnegative integration length")
        if self.api.upper(length) == 0:
            return zeros(self.api, self.field.rows, self.field.cols)
        return scale(self.api, length, self.field.at(box))

    def full_cell(self, index):
        require(type(index) is int and 0 <= index < len(self.domain.cells),
                "whole panel index")
        if index not in self.full_cache:
            self.full_cache[index] = self._enclose(
                self.domain.whole_cell_box(index), self.domain.full_length(index))
        return self.full_cache[index]

    def before(self, index):
        require(0 <= index <= len(self.domain.cells), "complete prefix boundary")
        for k in range(1,index+1):
            if k not in self.prefix_cache:
                self.prefix_cache[k] = add(self.api,self.prefix_cache[k-1],self.full_cell(k-1))
        return self.prefix_cache[index]

    def after(self, index):
        require(0 <= index <= len(self.domain.cells), "complete suffix boundary")
        for k in range(len(self.domain.cells)-1,index-1,-1):
            if k not in self.suffix_cache:
                self.suffix_cache[k] = add(self.api,self.full_cell(k),self.suffix_cache[k+1])
        return self.suffix_cache[index]

    def prefix(self, box):
        index = self.domain.cell_index(box)
        return add(self.api, self.before(index), self._enclose(
            self.domain.partial_box(box, "prefix"),
            self.domain.partial_length(box, "prefix")))

    def suffix(self, box):
        index = self.domain.cell_index(box)
        return add(self.api, self._enclose(
            self.domain.partial_box(box, "suffix"),
            self.domain.partial_length(box, "suffix")), self.after(index+1))

    def between(self, left, right):
        """Enclose the actual ordered integral; never subtract two interval sums."""
        li, ri = self.domain.cell_index(left), self.domain.cell_index(right)
        require(li <= ri, "ordered integration boxes")
        if li == ri:
            box, length = self.domain.ordered_span(left, right)
            return self._enclose(box, length)
        terms = [self._enclose(self.domain.partial_box(left, "suffix"),
                              self.domain.partial_length(left, "suffix"))]
        terms.extend(self.full_cell(i) for i in range(li+1, ri))
        terms.append(self._enclose(self.domain.partial_box(right, "prefix"),
                                   self.domain.partial_length(right, "prefix")))
        return add(self.api, *terms)


class SignedKernel:
    """M(r) delta + U(r)V(s) below + P(r)Q(s) above, and full output atoms.

    Lower and upper factors are exact function definitions with interval
    enclosures.  Their ranks describe a representation, not the physical rank
    of the whole radial operator.  atoms(s) has every genuine output observation.
    """
    def __init__(self, domain, outputs, inputs, local, U, V, P, Q, atoms, label):
        self.domain, self.api = domain, domain.api
        self.outputs, self.inputs = tuple(outputs), tuple(inputs)
        self.local, self.U, self.V, self.P, self.Q, self.atoms = local, U, V, P, Q, atoms
        self.label = label
        no, ni = len(self.outputs), len(self.inputs)
        require(all(f.domain is domain for f in (local,U,V,P,Q,atoms)),
                "same complete kernel domain")
        require((local.rows,local.cols)==(no,ni) and U.rows==no and V.cols==ni
                and U.cols==V.rows and P.rows==no and Q.cols==ni
                and P.cols==Q.rows and atoms.cols==ni, "complete signed kernel shapes")
        self.lower_rank, self.upper_rank = U.cols, P.cols
        self.atom_count = atoms.rows
        self.kernel_override = None

    def kernel(self, output_box, input_box, orientation):
        require(orientation in (-1,0,1), "true radial ordering")
        if self.kernel_override is not None:
            return self.kernel_override(output_box, input_box, orientation)
        lower = lambda: multiply(self.api, self.U.at(output_box), self.V.at(input_box))
        upper = lambda: multiply(self.api, self.P.at(output_box), self.Q.at(input_box))
        if orientation == 1:
            return lower()
        if orientation == -1:
            return upper()
        return hull(self.api, lower(), upper())

    def atom_kernel(self, input_box):
        return self.atoms.at(input_box)


def multiplication(domain, outputs, inputs, field, label):
    no, ni = len(outputs), len(inputs)
    require((field.rows,field.cols)==(no,ni), "actual multiplication coordinates")
    return SignedKernel(domain,outputs,inputs,field,
        zero_field(domain,no,0,label+":U"),zero_field(domain,0,ni,label+":V"),
        zero_field(domain,no,0,label+":P"),zero_field(domain,0,ni,label+":Q"),
        zero_field(domain,0,ni,label+":atoms"),label)


def scaled_kernel(value, operator, label):
    domain = operator.domain
    result = SignedKernel(domain,operator.outputs,operator.inputs,
        scaled_field(value,operator.local,label+":M"),
        scaled_field(value,operator.U,label+":U"),operator.V,
        scaled_field(value,operator.P,label+":P"),operator.Q,
        scaled_field(value,operator.atoms,label+":atoms"),label)
    result.kernel_override = lambda r,s,o: scale(domain.api,value,operator.kernel(r,s,o))
    return result


def sum_kernel(label, *operators):
    require(len(operators)>0, "complete nonempty signed operator sum")
    first=operators[0];domain=first.domain
    require(all(k.domain is domain and k.outputs==first.outputs and k.inputs==first.inputs
                and k.atom_count==first.atom_count for k in operators),
            "same actual spaces and all output atoms")
    result=SignedKernel(domain,first.outputs,first.inputs,
        sum_field(label+":M",*(k.local for k in operators)),
        Field(domain,len(first.outputs),sum(k.lower_rank for k in operators),
              lambda b:hcat(*(k.U.at(b) for k in operators)),label+":U"),
        Field(domain,sum(k.lower_rank for k in operators),len(first.inputs),
              lambda b:vcat(*(k.V.at(b) for k in operators)),label+":V"),
        Field(domain,len(first.outputs),sum(k.upper_rank for k in operators),
              lambda b:hcat(*(k.P.at(b) for k in operators)),label+":P"),
        Field(domain,sum(k.upper_rank for k in operators),len(first.inputs),
              lambda b:vcat(*(k.Q.at(b) for k in operators)),label+":Q"),
        sum_field(label+":atoms",*(k.atoms for k in operators)),label)
    # The whole signed sum is formed before the first absolute value.
    result.kernel_override=lambda r,s,o:add(domain.api,*(k.kernel(r,s,o) for k in operators))
    return result


def compose(left, right, label, integral_factory=WholePanelIntegral):
    """Complete ordered composition, ranks add separately on both triangles.

    A=integral V1 U2, B=integral Q1 P2, C=integral V1 P2,
    D=integral Q1 U2.  D_suffix is an independently enclosed suffix.
    Output atoms of left are transported by the same composition.  An inner
    operator with output atoms is rejected: this body cascade cannot discard
    or silently feed point observations back into a body input.
    """
    domain,api=left.domain,left.api
    require(right.domain is domain and left.inputs==right.outputs,
            "ordered actual physical coordinates")
    require(right.atom_count==0,"inner atoms require a separate declared input-port block")
    A=integral_factory(product_field(label+":V1U2",left.V,right.U),label+":A")
    B=integral_factory(product_field(label+":Q1P2",left.Q,right.P),label+":B")
    C=integral_factory(product_field(label+":V1P2",left.V,right.P),label+":C")
    D=integral_factory(product_field(label+":Q1U2",left.Q,right.U),label+":D")
    def low_u(b):
        first=add(api,product(api,left.local.at(b),right.U.at(b)),
                  product(api,left.U.at(b),A.prefix(b)),
                  product(api,left.P.at(b),D.suffix(b)))
        return hcat(first,left.U.at(b))
    def low_v(b):
        second=add(api,product(api,left.V.at(b),right.local.at(b)),
                   scale(api,-api.one,product(api,A.prefix(b),right.V.at(b))),
                   product(api,C.prefix(b),right.Q.at(b)))
        return vcat(right.V.at(b),second)
    def up_p(b):
        first=add(api,product(api,left.local.at(b),right.P.at(b)),
                  product(api,left.U.at(b),C.prefix(b)),
                  scale(api,-api.one,product(api,left.P.at(b),B.prefix(b))))
        return hcat(first,left.P.at(b))
    def up_q(b):
        second=add(api,product(api,left.Q.at(b),right.local.at(b)),
                   product(api,B.prefix(b),right.Q.at(b)),
                   product(api,D.suffix(b),right.V.at(b)))
        return vcat(right.Q.at(b),second)
    if left.atom_count:
        RU=integral_factory(product_field(label+":atomU2",left.atoms,right.U),label+":atom_suffix")
        RP=integral_factory(product_field(label+":atomP2",left.atoms,right.P),label+":atom_prefix")
        atoms=Field(domain,left.atom_count,len(right.inputs),
              lambda b:add(api,product(api,left.atoms.at(b),right.local.at(b)),
                            product(api,RU.suffix(b),right.V.at(b)),
                            product(api,RP.prefix(b),right.Q.at(b))),label+":atoms")
    else:
        atoms=zero_field(domain,0,len(right.inputs),label+":atoms")
    result=SignedKernel(domain,left.outputs,right.inputs,
        product_field(label+":M",left.local,right.local),
        Field(domain,len(left.outputs),left.lower_rank+right.lower_rank,low_u,label+":U"),
        Field(domain,left.lower_rank+right.lower_rank,len(right.inputs),low_v,label+":V"),
        Field(domain,len(left.outputs),left.upper_rank+right.upper_rank,up_p,label+":P"),
        Field(domain,left.upper_rank+right.upper_rank,len(right.inputs),up_q,label+":Q"),
        atoms,label)
    def direct(r,s,o):
        if o==0:
            return hull(api,direct(r,s,1),direct(r,s,-1))
        local_terms=[product(api,left.local.at(r),right.kernel(r,s,o)),
                     product(api,left.kernel(r,s,o),right.local.at(s))]
        if o==1:
            terms=[product(api,left.U.at(r),C.prefix(s),right.Q.at(s)),
                   product(api,left.U.at(r),A.between(s,r),right.V.at(s)),
                   product(api,left.P.at(r),D.suffix(r),right.V.at(s))]
        else:
            terms=[product(api,left.U.at(r),C.prefix(r),right.Q.at(s)),
                   product(api,left.P.at(r),B.between(r,s),right.Q.at(s)),
                   product(api,left.P.at(r),D.suffix(s),right.V.at(s))]
        return add(api,*(local_terms+terms))
    result.kernel_override=direct
    return result


def body_adjoint(operator, label):
    """True same-L2-pairing adjoint; an output atom is never dropped."""
    require(operator.atom_count==0,"full atom adjoint is a separate input-port operator")
    domain=operator.domain
    result=SignedKernel(domain,operator.inputs,operator.outputs,
        transposed_field(operator.local,label+":M"),
        transposed_field(operator.Q,label+":U"),transposed_field(operator.P,label+":V"),
        transposed_field(operator.V,label+":P"),transposed_field(operator.U,label+":Q"),
        zero_field(domain,0,len(operator.outputs),label+":atoms"),label)
    result.kernel_override=lambda r,s,o:transpose(operator.kernel(s,r,-o))
    return result


def collar_primitive(domain, coordinates, collar_indicator, label):
    """J_c f(r)=integral_a^min(r,c) f; J_c* has true outer upper limit R."""
    n=len(coordinates)
    identity=constant_field(domain,eye(domain.api,n),label+":I")
    require((collar_indicator.rows,collar_indicator.cols)==(n,n),
            "full collar projection on the same actual high coordinates")
    return SignedKernel(domain,coordinates,coordinates,
        zero_field(domain,n,n,label+":M"),identity,collar_indicator,
        zero_field(domain,n,0,label+":P"),zero_field(domain,0,n,label+":Q"),
        zero_field(domain,0,n,label+":atoms"),label)


def whole_signed_kernel_schur(operator, input_weights, body_weights, atom_weights,
                              emit, prefix, progress=None):
    """Full continuous L2 -> L2 plus all finite observations, not sampled columns.

    Each kernel enclosure covers the entire product of two radial cells.
    Its complete signed value is formed before magnitude.  A same-cell box
    takes the hull of both open triangles; the diagonal has measure zero.
    Positive Schur weights are only an inequality device, never new physical
    coordinates. Local multiplication contributes without a radial length factor.
    This streaming correctness backend stores no kernel array.
    """
    domain,api=operator.domain,operator.api
    n=len(domain.cells);ni=len(operator.inputs);no=len(operator.outputs)
    require(len(input_weights)==n and all(len(x)==ni for x in input_weights)
            and len(body_weights)==n and all(len(x)==no for x in body_weights)
            and len(atom_weights)==operator.atom_count,"all continuous/atomic Schur weights")
    for row in input_weights+body_weights+[atom_weights]:
        require(all(api.lower(x)>0 for x in row),"strictly positive Schur weights")
    row_sums=[[api.zero for _ in range(no)] for _ in range(n)]
    column_sums=[[api.zero for _ in range(ni)] for _ in range(n)]
    atom_sums=[api.zero for _ in range(operator.atom_count)]
    if not operator.local.identically_zero:
        for i in range(n):
            matrix=operator.local.at(domain.whole_cell_box(i))
            for a in range(no):
                for b in range(ni):
                    value=api.upper(api.magnitude(matrix.values[a][b]))
                    row_sums[i][a]+=value*api.upper(input_weights[i][b])
                    column_sums[i][b]+=value*api.upper(body_weights[i][a])
    for i in range(n):
        r=domain.whole_cell_box(i);hr=api.upper(domain.full_length(i))
        for j in range(n):
            s=domain.whole_cell_box(j);hs=api.upper(domain.full_length(j))
            orientation=1 if i>j else (-1 if i<j else 0)
            block=operator.kernel(r,s,orientation)
            for a in range(no):
                for b in range(ni):
                    value=api.upper(api.magnitude(block.values[a][b]))
                    row_sums[i][a]+=hs*value*api.upper(input_weights[j][b])
                    column_sums[j][b]+=hr*value*api.upper(body_weights[i][a])
        if progress is not None:
            progress("complete_signed_body_row_panel",{"completed":i+1,"total":n,
                     "kernel_values_cover_whole_radial_products":True})
    for j in range(n):
        hs=api.upper(domain.full_length(j))
        block=operator.atom_kernel(domain.whole_cell_box(j))
        for a in range(operator.atom_count):
            for b in range(ni):
                value=api.upper(api.magnitude(block.values[a][b]))
                atom_sums[a]+=hs*value*api.upper(input_weights[j][b])
                column_sums[j][b]+=value*api.upper(atom_weights[a])
    row_candidates=[api.upper(row_sums[i][a]/api.lower(body_weights[i][a]))
                    for i in range(n) for a in range(no)]
    row_candidates.extend(api.upper(atom_sums[a]/api.lower(atom_weights[a]))
                          for a in range(operator.atom_count))
    column_candidates=[api.upper(column_sums[j][b]/api.lower(input_weights[j][b]))
                       for j in range(n) for b in range(ni)]
    require(row_candidates and column_candidates,"complete nonempty physical kernel")
    row=emit(prefix+"_row_ratio_upper",max(row_candidates))
    column=emit(prefix+"_column_ratio_upper",max(column_candidates))
    norm=emit(prefix+"_norm_upper",api.sqrt(row*column))
    return {"row":row,"column":column,"norm":norm}


class RadialDomain:
    """A finite complete cover with a genuine uncertain root, not a substituted root.

    The caller supplies exact rational body panel endpoints and the exact
    original root interval.  A box (i,t0,t1) denotes the actual affine position
    within cell i for ALL t0<=t<=t1.  The first left endpoint remains r_star.
    Whole coefficient boxes must cover all original closed intersections.
    """
    def __init__(self,api,panels,root_interval,zero_fraction,one_fraction):
        self.api=api
        self.cells=tuple(panels)
        self.root_lo,self.root_hi=root_interval
        self.fzero,self.fone=zero_fraction,one_fraction
        require(self.cells and self.root_lo<=self.root_hi,
                "nonempty genuine-root complete radial cover")
        require(self.cells[0]["left"] is None and
                self.root_hi<self.cells[0]["right"],"first panel has the true root")
        for i,cell in enumerate(self.cells):
            require(set(cell)>={"left","right","parent_index"} and
                    (i==0 or cell["left"]<cell["right"]),"full exact panel")
            if i:
                require(cell["left"]==self.cells[i-1]["right"],
                        "complete contiguous ordinary radial cover")
        self.lengths=[]
        for i,cell in enumerate(self.cells):
            if i==0:
                lo=cell["right"]-self.root_hi
                hi=cell["right"]-self.root_lo
            else:
                lo=hi=cell["right"]-cell["left"]
            value=api.interval(self.exact(lo),self.exact(hi))
            require(api.lower(value)>0,"strict positive genuine panel length")
            self.lengths.append(value)

    def exact(self,value):
        require(hasattr(value,"numerator") and hasattr(value,"denominator")
                and not isinstance(value,bool),"exact rational domain value")
        return self.api.rational(int(value.numerator),int(value.denominator))

    def validate_box(self,box):
        require(isinstance(box,tuple) and len(box)==3 and type(box[0]) is int,
                "immutable complete radial box")
        i,a,b=box
        require(0<=i<len(self.cells) and self.fzero<=a<=b<=self.fone,
                "box lies in one actual radial cell")

    def cache_key(self,box):
        self.validate_box(box)
        i,a,b=box
        return (i,int(a.numerator),int(a.denominator),int(b.numerator),int(b.denominator))

    def whole_cell_box(self,index):
        require(type(index) is int and 0<=index<len(self.cells),"complete cell index")
        return (index,self.fzero,self.fone)

    def point(self,index,fraction):
        box=(index,fraction,fraction)
        self.validate_box(box)
        return box

    def cell_index(self,box):
        self.validate_box(box)
        return box[0]

    def full_length(self,index):
        return self.lengths[index]

    def physical_interval(self,box):
        self.validate_box(box)
        i,a,b=box;cell=self.cells[i]
        if i==0:
            lo=(self.fone-a)*self.root_lo+a*cell["right"]
            hi=(self.fone-b)*self.root_hi+b*cell["right"]
        else:
            h=cell["right"]-cell["left"]
            lo=cell["left"]+a*h;hi=cell["left"]+b*h
        return self.api.interval(self.exact(lo),self.exact(hi))

    def exact_physical_cover(self,box):
        self.validate_box(box)
        i,a,b=box;cell=self.cells[i]
        if i==0:
            return ((self.fone-a)*self.root_lo+a*cell["right"],
                    (self.fone-b)*self.root_hi+b*cell["right"])
        h=cell["right"]-cell["left"]
        return cell["left"]+a*h,cell["left"]+b*h

    def partial_box(self,box,direction):
        self.validate_box(box);i,a,b=box
        require(direction in ("prefix","suffix"),"whole partial integration direction")
        return (i,self.fzero,b) if direction=="prefix" else (i,a,self.fone)

    def partial_length(self,box,direction):
        self.validate_box(box);i,a,b=box
        require(direction in ("prefix","suffix"),"whole partial length direction")
        lo,hi=(a,b) if direction=="prefix" else (self.fone-b,self.fone-a)
        return self.api.interval(self.exact(lo),self.exact(hi))*self.lengths[i]

    def ordered_span(self,left,right):
        self.validate_box(left);self.validate_box(right)
        require(left[0]==right[0],"same-panel ordered span")
        i,a,b=left;_,c,d=right
        require(a<=d,"nonempty possible ordered pair")
        lo=max(self.fzero,c-b);hi=max(self.fzero,d-a)
        return (i,a,d),self.api.interval(self.exact(lo),self.exact(hi))*self.lengths[i]


def matrix_norm_upper(api,matrix):
    """Complete finite angular Hilbert norm, after one entire signed matrix."""
    if matrix.rows==0 or matrix.cols==0:
        return api.zero
    if hasattr(api,"matrix_absolute_row_column_upper"):
        rows,cols=api.matrix_absolute_row_column_upper(matrix.values)
        require(len(rows)==matrix.rows and len(cols)==matrix.cols,
                "complete backend absolute matrix rows and columns")
        rows=[api.upper(x) for x in rows];cols=[api.upper(x) for x in cols]
    else:
        magnitudes=[[api.upper(api.magnitude(x)) for x in row] for row in matrix.values]
        rows=[api.upper(sum(row,api.zero)) for row in magnitudes]
        cols=[api.upper(sum((magnitudes[i][j] for i in range(matrix.rows)),api.zero))
              for j in range(matrix.cols)]
    return api.upper(api.sqrt(max(rows)*max(cols)))


class CompleteBlockEnvelope:
    """Operator-valued Schur envelope of a WHOLE signed continuous kernel.

    Each scalar tile dominates the finite angular operator norm for the
    entire product of two radial cells. The scalar comparison is not claimed
    to be a signed Fourier coefficient or an actual one-dimensional state.
    All finite output observations form one complete Hilbert atom block.
    """
    def __init__(self,operator,input_space,output_space):
        self.operator=operator;self.domain=operator.domain;self.api=operator.api
        self.input_space=input_space;self.output_space=output_space
        self.atom_count=1 if operator.atom_count else 0
        self.tile_cache={};self.local_cache={};self.atom_cache={}

    def local_bound(self,i):
        if i not in self.local_cache:
            self.local_cache[i]=matrix_norm_upper(self.api,
                self.operator.local.at(self.domain.whole_cell_box(i)))
        return self.local_cache[i]

    def tile(self,i,j):
        key=(i,j)
        if key not in self.tile_cache:
            orientation=1 if i>j else (-1 if i<j else 0)
            value=self.operator.kernel(self.domain.whole_cell_box(i),
                                       self.domain.whole_cell_box(j),orientation)
            self.tile_cache[key]=matrix_norm_upper(self.api,value)
        return self.tile_cache[key]

    def atom(self,j):
        require(self.atom_count==1,"complete nonempty output observation block")
        if j not in self.atom_cache:
            self.atom_cache[j]=matrix_norm_upper(self.api,
                self.operator.atom_kernel(self.domain.whole_cell_box(j)))
        return self.atom_cache[j]

    def forward(self,field):
        n=len(self.domain.cells);api=self.api
        require(len(field)==n,"whole-input radial envelope")
        field=[api.upper(x) for x in field]
        body=[]
        for i in range(n):
            value=self.local_bound(i)*field[i]
            for j in range(n):
                value+=api.upper(self.domain.full_length(j))*self.tile(i,j)*field[j]
            body.append(api.upper(value))
        atoms=[]
        if self.atom_count:
            atoms=[api.upper(sum((api.upper(self.domain.full_length(j))*self.atom(j)*field[j]
                                 for j in range(n)),api.zero))]
        return {"body":body,"atoms":atoms}

    def reverse(self,value):
        n=len(self.domain.cells);api=self.api
        require(set(value)=={"body","atoms"} and len(value["body"])==n
                and len(value["atoms"])==self.atom_count,"whole transpose envelope")
        body=[api.upper(x) for x in value["body"]]
        atoms=[api.upper(x) for x in value["atoms"]]
        result=[]
        for j in range(n):
            total=self.local_bound(j)*body[j]
            for i in range(n):
                total+=api.upper(self.domain.full_length(i))*self.tile(i,j)*body[i]
            if atoms:
                total+=self.atom(j)*atoms[0]
            result.append(api.upper(total))
        return result


class PointwiseNormComparison:
    """A proved whole angular operator norm, not an invented signed matrix.

    It may compare distinct finite angular spaces. Every original mean or
    rank term must already be included in the supplied coefficient norm.
    """
    def __init__(self,domain,values,input_space,output_space,label):
        self.domain,self.api=domain,domain.api
        require(len(values)==len(domain.cells),"complete pointwise coefficient cover")
        self.values=[self.api.upper(x) for x in values]
        self.input_space=input_space;self.output_space=output_space
        self.atom_count=0;self.label=label

    def forward(self,field):
        require(len(field)==len(self.values),"complete local comparison input")
        return {"body":[self.api.upper(a*b) for a,b in zip(self.values,field)],"atoms":[]}

    def reverse(self,value):
        require(set(value)=={"body","atoms"} and not value["atoms"]
                and len(value["body"])==len(self.values),"complete local comparison dual")
        return [self.api.upper(a*b) for a,b in zip(self.values,value["body"])]


class PositiveComposition:
    def __init__(self,left,right,label):
        require(left.domain is right.domain and left.input_space==right.output_space
                and right.atom_count==0,"ordered complete Hilbert-block comparison")
        self.left,self.right,self.label=left,right,label
        self.domain,self.api=left.domain,left.api
        self.input_space=right.input_space;self.output_space=left.output_space
        self.atom_count=left.atom_count

    def forward(self,field):
        middle=self.right.forward(field)
        require(not middle["atoms"],"no discarded internal observation")
        return self.left.forward(middle["body"])

    def reverse(self,value):
        middle=self.left.reverse(value)
        return self.right.reverse({"body":middle,"atoms":[]})


class PositiveSum:
    def __init__(self,operators,label):
        require(operators,"complete nonempty positive comparison")
        first=operators[0]
        require(all(op.domain is first.domain and op.input_space==first.input_space
                    and op.output_space==first.output_space and
                    op.atom_count==first.atom_count for op in operators),
                "one complete sum of actual Hilbert-space maps")
        self.operators,self.label=tuple(operators),label
        self.domain,self.api=first.domain,first.api
        self.input_space=first.input_space;self.output_space=first.output_space
        self.atom_count=first.atom_count

    def forward(self,field):
        results=[op.forward(field) for op in self.operators]
        n=len(self.domain.cells);api=self.api
        return {"body":[api.upper(sum((x["body"][i] for x in results),api.zero)) for i in range(n)],
                "atoms":[api.upper(sum((x["atoms"][i] for x in results),api.zero))
                         for i in range(self.atom_count)]}

    def reverse(self,value):
        results=[op.reverse(value) for op in self.operators]
        return [self.api.upper(sum((x[i] for x in results),self.api.zero))
                for i in range(len(self.domain.cells))]


def complete_positive_comparison_norm(operator,emit,prefix):
    """Whole operator-valued Schur test with all output observations."""
    api=operator.api;n=len(operator.domain.cells)
    rows=operator.forward([api.one for _ in range(n)])
    row=emit(prefix+"_row_ratio_upper",max(api.upper(x) for x in rows["body"]+rows["atoms"]))
    columns=operator.reverse({"body":[api.one for _ in range(n)],
                              "atoms":[api.one for _ in range(operator.atom_count)]})
    column=emit(prefix+"_column_ratio_upper",max(api.upper(x) for x in columns))
    norm=emit(prefix+"_norm_upper",api.upper(api.sqrt(row*column)))
    return norm


class CompleteScalarKernelComparison(CompleteBlockEnvelope):
    """Whole angular-norm comparison with scalar radial storage only.

    Each callback bounds the ENTIRE angular operator on a full radial product
    cell. This is an operator-valued comparison, not a sampled scalar kernel.
    Atom callbacks include the complete finite Hilbert observation block.
    """
    def __init__(self,domain,input_space,output_space,tile_callback,
                 local_callback=None,atom_callback=None,label="complete scalar comparison"):
        self.domain,self.api=domain,domain.api
        self.input_space,self.output_space=input_space,output_space
        self.tile_callback,self.local_callback=tile_callback,local_callback
        self.atom_callback=atom_callback
        self.atom_count=0 if atom_callback is None else 1
        self.label=label
        self.tile_cache={};self.local_cache={};self.atom_cache={}

    def local_bound(self,i):
        if i not in self.local_cache:
            value=self.api.zero if self.local_callback is None else self.local_callback(i)
            self.local_cache[i]=self.api.upper(value)
        return self.local_cache[i]

    def tile(self,i,j):
        key=(i,j)
        if key not in self.tile_cache:
            self.tile_cache[key]=self.api.upper(self.tile_callback(i,j))
        return self.tile_cache[key]

    def atom(self,j):
        require(self.atom_callback is not None,"all finite observations are present")
        if j not in self.atom_cache:
            self.atom_cache[j]=self.api.upper(self.atom_callback(j))
        return self.atom_cache[j]


class CompletePositiveAdjoint:
    """True transpose of a body comparison; output observations cannot be dropped."""
    def __init__(self,operator,label):
        require(operator.atom_count==0,
                "a nonempty finite observation block requires its complete dual input")
        self.operator,self.label=operator,label
        self.domain,self.api=operator.domain,operator.api
        self.input_space,self.output_space=operator.output_space,operator.input_space
        self.atom_count=0

    def forward(self,field):
        return {"body":self.operator.reverse({"body":field,"atoms":[]}),"atoms":[]}

    def reverse(self,value):
        require(not value["atoms"],"no artificial omitted adjoint observation")
        return self.operator.forward(value["body"])["body"]
