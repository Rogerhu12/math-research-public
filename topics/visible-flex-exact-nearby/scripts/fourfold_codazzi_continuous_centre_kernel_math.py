"""WVC complete physical Fourier and paired continuous-kernel norm engine.

No entry point, numerical import, file access, or old-producer call.
All arrays are temporary Actions working state.  The caller must admit the
published WPS/WIC/WQS identities, common ordinary-dr cells, the actual
193-dimensional reflected basis, and the complete old coefficient scopes.

Numerical API: zero, one, upper(x), lower(x), magnitude(x), sqrt(x), exp(x).
upper/magnitude return finite nonnegative directed point uppers. lower is a
finite directed point lower.  Every denominator below is checked positive.
Input boxes are complete enclosures, not values recovered from old uppers.
"""

def require(ok, message):
    if not ok:
        raise ValueError(message)


def maximum(api, values):
    values = list(values)
    require(bool(values), "nonempty complete upper set")
    return max(api.upper(value) for value in values)


def positive_lower(api, value):
    value = api.lower(value)
    require(value > 0, "strict positive lower endpoint")
    return value


def band(first, last):
    require(type(first) is int and type(last) is int and 0 <= first <= last,
            "complete physical Fourier band")
    return tuple([(0, j) for j in range(max(1, first), last + 1)] +
                 [(1, j) for j in range(first, last + 1)])


def multiplier_entry(poly, parity, output, input_, sqrt_two, zero):
    """Exact real-normalized multiplication, before taking an absolute value.

    parity=0: real even Laurent coefficients poly[j].
    parity=1: real odd polynomial with Laurent coefficients i*poly[j].
    State parity is 0=odd sine, 1=even cosine; its mean vector has norm one.
    All consumers admit degree32 u/v and at most degree64 local coefficients.
    The separate full96 error never enters this finite coefficient graph.
    """
    oc, k = output
    ic, j = input_
    if parity == 0:
        if oc != ic:
            return zero
        if j == 0:
            return poly.get(0, zero) if k == 0 else sqrt_two * poly.get(k, zero)
        if k == 0:
            return sqrt_two * poly.get(j, zero) if ic == 1 else zero
        minus = poly.get(k-j, zero)
        plus = poly.get(k+j, zero)
        return minus - plus if ic == 0 else minus + plus
    require(parity == 1, "polynomial parity")
    if oc == ic:
        return zero
    if ic == 1:
        require(oc == 0 and k > 0, "odd multiplier even-to-odd range")
        if j == 0:
            return -sqrt_two * poly.get(k, zero)
        return -(poly.get(k-j, zero) + poly.get(k+j, zero))
    require(oc == 1 and j > 0, "odd multiplier odd-to-even range")
    if k == 0:
        return -sqrt_two * poly.get(j, zero)
    return poly.get(k-j, zero) - poly.get(k+j, zero)


def full_mean_row(packet, input_, sqrt_two, zero):
    """The COMPLETE raw generator mean row, after the proved exact cancellation."""
    ic, j = input_
    beta, curvature, mean = packet["beta"], packet["K"], packet["v"][0]
    if j == 0:
        return beta * (1-packet["S_mean"]-2*curvature*mean*mean)
    if ic == 0:
        return 2*sqrt_two*beta*mean*packet["u"].get(j, zero)
    return -2*sqrt_two*beta*mean*curvature*packet["v"].get(j, zero)


def local_entry(packet, output, input_, sqrt_two, zero):
    """All LOCAL, principal and mean-rank entries; no primitive word here."""
    oc, k = output
    ic, j = input_
    value = zero
    if oc == ic:
        value += multiplier_entry(packet["la"] if oc == 0 else packet["le"],
                                  0, output, input_, sqrt_two, zero)
        if j:
            derivative_output = (1-ic, j)
            derivative_sign = 4*j if ic == 0 else -4*j
            value += derivative_sign * multiplier_entry(
                packet["d"], 1, output, derivative_output, sqrt_two, zero)
    else:
        value += multiplier_entry(packet["Kell"] if oc == 0 else packet["ell"],
                                  1, output, input_, sqrt_two, zero)
        if j == k and j:
            value += 4*j*packet["eta"]*(packet["K"] if oc == 0 else 1)
    if ic == 1 and j == 0 and k:
        if oc == 0:
            value += -sqrt_two*4*k*packet["gamma"]*packet["K"]*packet["v"].get(k,zero)
        else:
            value += sqrt_two*4*k*packet["gamma"]*packet["u"].get(k,zero)
    return value


def frozen_principal_entry(eta, q, output, input_, zero):
    oc, k = output
    ic, j = input_
    if oc == ic or j != k or j == 0:
        return zero
    return 4*j*eta*(q*q if oc == 0 else 1)


def physical_word(packet):
    # a[0] even, a[1] odd; b[0] odd, b[1] even. I acts on EVEN nonmean.
    return (packet["a"], packet["b"])


def difference_word(left, right, zero):
    return {j: left.get(j, zero)-right.get(j, zero)
            for j in set(left) | set(right)}


class AngularMajorant:
    """One declared full positive majorant of a signed physical angular map.

    The local entries are formed signed first.  Each ordered primitive word
    retains its true intermediate projection and I multiplier.  A complete
    mean row replaces the entire local-plus-primitive row, never one term.
    """
    def __init__(self, api, inputs, outputs, sqrt_two, local, words, mean_row=None):
        self.api, self.inputs, self.outputs = api, tuple(inputs), tuple(outputs)
        self.sqrt_two, self.local, self.words = sqrt_two, local, list(words)
        self.mean_row = mean_row
        self.local_bandwidth = 64
        require(len(set(self.inputs)) == len(self.inputs)
                and len(set(self.outputs)) == len(self.outputs), "unique physical coordinates")
        largest = max((j for _, j in self.inputs), default=0)
        degree_b = max((abs(j) for _, b in self.words for p in b for j in p), default=0)
        degree_a = max((abs(j) for a, _ in self.words for p in a for j in p), default=0)
        largest_out = max((j for _, j in self.outputs), default=0)
        # Both factors must have support at this TRUE intermediate mode.
        self.intermediate = tuple(range(1, min(largest+degree_b, largest_out+degree_a)+1))

    def apply(self, values, transpose=False):
        api, zero = self.api, self.api.zero
        source = self.outputs if transpose else self.inputs
        target = self.inputs if transpose else self.outputs
        require(len(values) == len(source), "complete angular input")
        result = [zero for _ in target]
        for o, output in enumerate(self.outputs):
            if output == (1, 0) and self.mean_row is not None:
                for i, input_ in enumerate(self.inputs):
                    coefficient = api.magnitude(self.mean_row(input_))
                    if transpose:
                        result[i] += coefficient*values[o]
                    else:
                        result[o] += coefficient*values[i]
                continue
            for i, input_ in enumerate(self.inputs):
                if abs(output[1]-input_[1])>self.local_bandwidth:
                    continue
                coefficient = api.magnitude(self.local(output, input_))
                if transpose:
                    result[i] += coefficient*values[o]
                else:
                    result[o] += coefficient*values[i]
        for a, b in self.words:
            adegree=[max((abs(j) for j in poly),default=0) for poly in a]
            bdegree=[max((abs(j) for j in poly),default=0) for poly in b]
            require(max(adegree+bdegree)<=32,"complete degree32 primitive factors")
            middle = [zero for _ in self.intermediate]
            if not transpose:
                for mindex, m in enumerate(self.intermediate):
                    for i, input_ in enumerate(self.inputs):
                        if abs(m-input_[1])>bdegree[input_[0]]:
                            continue
                        p = b[input_[0]]
                        coefficient = multiplier_entry(
                            p, 1 if input_[0] == 0 else 0,
                            (1,m), input_, self.sqrt_two, zero)
                        middle[mindex] += api.magnitude(coefficient)*values[i]
                    middle[mindex] /= 4*m
                for o, output in enumerate(self.outputs):
                    if output == (1,0) and self.mean_row is not None:
                        continue
                    p = a[output[0]]
                    for mindex, m in enumerate(self.intermediate):
                        if abs(output[1]-m)>adegree[output[0]]:
                            continue
                        coefficient = multiplier_entry(
                            p, 0 if output[0] == 0 else 1,
                            output, (0,m), self.sqrt_two, zero)
                        result[o] += 2*api.magnitude(coefficient)*middle[mindex]
            else:
                for mindex, m in enumerate(self.intermediate):
                    for o, output in enumerate(self.outputs):
                        if output == (1,0) and self.mean_row is not None:
                            continue
                        if abs(output[1]-m)>adegree[output[0]]:
                            continue
                        p = a[output[0]]
                        coefficient = multiplier_entry(
                            p, 0 if output[0] == 0 else 1,
                            output, (0,m), self.sqrt_two, zero)
                        middle[mindex] += 2*api.magnitude(coefficient)*values[o]
                    middle[mindex] /= 4*m
                for i, input_ in enumerate(self.inputs):
                    p = b[input_[0]]
                    for mindex, m in enumerate(self.intermediate):
                        if abs(m-input_[1])>bdegree[input_[0]]:
                            continue
                        coefficient = multiplier_entry(
                            p, 1 if input_[0] == 0 else 0,
                            (1,m), input_, self.sqrt_two, zero)
                        result[i] += api.magnitude(coefficient)*middle[mindex]
        return [api.upper(v) for v in result]


def selected_principal_entry(principal, output, input_, zero):
    """The same old off-diagonal plus the declared signed low tracefree diagonal."""
    value=frozen_principal_entry(principal["eta"],principal["q"],output,input_,zero)
    oc,k=output;ic,j=input_
    if j>0 and j==k and oc==ic:
        diagonal=principal.get("diagonal",{}).get(j,zero)
        value+=diagonal if oc==0 else -diagonal
    return value


def complete_tracefree_reference_profiles(api,lengths,etas,qs,diagonals,modes,p_outer):
    """One full continuous kernel for the new reference, not new actual data.

    The exact clipped diagonal definitions are admitted by the caller.
    The physical S and mesh remain the old ones. Both propagation rates
    coincide for tracefree D and are bounded below by c/32. The old H
    bound 1/(2*pmin) is NOT reused. Every result encloses a whole cell.
    """
    n=len(lengths)
    require(n==len(etas)==len(qs)==len(diagonals)>0,
            "complete same physical profile partition")
    result={};pstar=api.rational(1,16)
    for j in modes:
        require(type(j) is int and 1<=j<=96,"true low nonzero mode")
        p=[api.zero for _ in range(n+1)];p[n]=p_outer
        taus=[api.zero for _ in range(n)]
        sigmas=[api.zero for _ in range(n)]
        for i in range(n-1,-1,-1):
            c=(4*j)*etas[i];q=qs[i];a=diagonals[i][j]
            require(api.lower(c)>=0 and api.lower(q)>=api.rational(1,8),
                    "same nonnegative c and admitted reference q floor")
            positive_lower(api,lengths[i])
            if api.upper(c)==0:
                require(api.upper(api.magnitude(a))==0,"zero-rate root has a=0")
                p[i]=p[i+1];taus[i]=api.one;sigmas[i]=api.zero
            else:
                omega=api.sqrt(a*a+c*c*q*q)
                positive_lower(api,omega)
                half_decay=api.exp(-omega*lengths[i])
                e=half_decay*half_decay
                A=(1+e)/2
                B=(1-e)/(2*omega)
                den=A+B*(a+c*p[i+1])
                positive_lower(api,den)
                p[i]=(B*c*q*q+p[i+1]*(A-B*a))/den
                taus[i]=half_decay/den
                sigmas[i]=B*c/den
            positive_lower(api,p[i])
        H=api.zero;parents=[]
        for i in range(n):
            c=(4*j)*etas[i];a=diagonals[i][j]
            pmin=max(api.lower(pstar),
                     min(positive_lower(api,p[i]),positive_lower(api,p[i+1])))
            pmax=maximum(api,[p[i],p[i+1]])
            rate=max(api.lower(a+c*pmin),api.lower(c/32))
            require(rate>=0,"whole tracefree lower decay in both directions")
            invariant=api.upper(1/pmin)
            if api.upper(c)==0:
                Hsup=min(api.upper(H),invariant)
            else:
                require(rate>0,"positive body comparison rate")
                comparison=maximum(api,[H,api.upper(c)/(2*rate)])
                Hsup=min(comparison,invariant)
            if rate==0:
                decay=(api.one,api.upper(lengths[i]))
            else:
                decay=(api.upper(api.exp(-rate*positive_lower(api,lengths[i]))),
                       api.upper((1-api.exp(-rate*api.upper(lengths[i])))/rate))
            parents.append({"p":pmax,"H":Hsup,"K":api.one,"rate":rate,"decay":decay})
            # Both are complete uppers for the SAME exact H endpoint.
            H=min(api.upper(taus[i]*taus[i]*H+sigmas[i]),
                  api.upper(1/max(api.lower(pstar),positive_lower(api,p[i+1]))))
            require(H>=0,"complete positive H endpoint")
        result[j]=parents
    return result


def generator_majorant(api, packet, inputs, outputs, sqrt_two, principal=None):
    def local(output, input_):
        value = local_entry(packet, output, input_, sqrt_two, api.zero)
        if principal is not None:
            value -= selected_principal_entry(principal,output,input_,api.zero)
        return value
    mean = lambda input_: full_mean_row(packet, input_, sqrt_two, api.zero)
    return AngularMajorant(api, inputs, outputs, sqrt_two, local,
                           [physical_word(packet)], mean_row=mean)


def difference_majorant(api, actual, reference, inputs, outputs, sqrt_two,
                        reference_scale=None):
    """reference_scale*REFERENCE minus ACTUAL, with both primitive factors.

    This is a genuine signed interval-minus-reference formula. No upper
    estimate is subtracted. The full mean difference is independently exact.
    """
    scale = api.one if reference_scale is None else reference_scale
    def local(output, input_):
        return scale*local_entry(reference,output,input_,sqrt_two,api.zero) - (
            local_entry(actual,output,input_,sqrt_two,api.zero))
    a0 = [{j: scale*v for j,v in p.items()} for p in reference["a"]]
    da = [difference_word(a0[k],actual["a"][k],api.zero) for k in range(2)]
    db = [difference_word(reference["b"][k],actual["b"][k],api.zero) for k in range(2)]
    mean = lambda input_: scale*full_mean_row(reference,input_,sqrt_two,api.zero)-(
        full_mean_row(actual,input_,sqrt_two,api.zero))
    return AngularMajorant(api, inputs, outputs, sqrt_two, local,
                           [(da,actual["b"]),(a0,db)], mean_row=mean)


def diagonal_action(api, values, diagonal):
    require(len(values)==len(diagonal), "complete diagonal")
    return [api.upper(v*d) for v,d in zip(values,diagonal)]


class PointwiseMap:
    def __init__(self, api, maps, input_diagonal, output_diagonal):
        self.api, self.maps = api, list(maps)
        self.input_diagonal, self.output_diagonal = input_diagonal, output_diagonal
        require(len(maps)==len(input_diagonal)==len(output_diagonal),
                "all parent pointwise maps")
        self.in_dim, self.out_dim = len(maps[0].inputs), len(maps[0].outputs)
        self.atoms = 0
        require(all(len(m.inputs)==self.in_dim and len(m.outputs)==self.out_dim for m in maps),
                "same complete angular input/output bands")

    def forward(self, field):
        require(len(field)==len(self.maps), "whole pointwise input interval")
        return {"body":[diagonal_action(self.api,
            m.apply(diagonal_action(self.api,row,di)),do)
            for m,row,di,do in zip(self.maps,field,self.input_diagonal,self.output_diagonal)],
            "atoms":[]}

    def reverse(self, value):
        require(value["atoms"]==[] and len(value["body"])==len(self.maps)
                and all(len(row)==self.out_dim for row in value["body"]),
                "whole pointwise adjoint body and no atom")
        return [diagonal_action(self.api,
            m.apply(diagonal_action(self.api,row,do),transpose=True),di)
            for m,row,di,do in zip(self.maps,value["body"],
                self.input_diagonal,self.output_diagonal)]


def scalar_positive_sweep(api, lengths, rates, drivers, boundary, reverse=False, coefficients=None):
    """Envelope of ONE fixed continuous exponential kernel, including an atom.

    Rates are declared nonnegative lower point bounds; coefficients/drivers are
    whole parent uppers. The returned cell supremum bounds the comparison ODE,
    not the possibly nonmonotone original variable forcing. Reverse means
    the SAME kernel in opposite radial order.
    """
    n=len(lengths)
    require(n==len(rates)==len(drivers) and n>0, "complete scalar kernel partition")
    require(coefficients is None or len(coefficients)==n,"complete cached decay coefficients")
    state=api.upper(boundary)
    result=[api.zero for _ in range(n)]
    order=range(n-1,-1,-1) if reverse else range(n)
    for i in order:
        lo=positive_lower(api,lengths[i])
        hi=api.upper(lengths[i])
        rate=api.lower(rates[i])
        require(rate>=0, "nonnegative comparison rate")
        if coefficients is not None:
            transition,integral=coefficients[i]
        elif rate==0:
            transition=api.one
            integral=hi
        else:
            transition=api.upper(api.exp(-rate*lo))
            integral=api.upper((1-api.exp(-rate*hi))/rate)
        following=api.upper(transition*state+integral*api.upper(drivers[i]))
        result[i]=maximum(api,[state,following])
        state=following
    return result,state


def complete_reference_profiles(api,lengths,etas,qs,modes,p_outer):
    """New reference expressions only, with continuous raw seam identity.

    Return complete parent coefficients for the same two-sided Green kernel.
    Zero-rate collars have their exact limits. Every p/H denominator is paid.
    """
    n=len(lengths)
    require(n==len(etas)==len(qs)>0, "common exact reference partition")
    result={}
    for j in modes:
        require(type(j) is int and j>0, "nonzero reference mode")
        p=[api.zero for _ in range(n+1)]
        p[n]=p_outer
        taus=[api.zero for _ in range(n)]
        sigmas=[api.zero for _ in range(n)]
        for i in range(n-1,-1,-1):
            eta=etas[i];q=qs[i]
            require(api.lower(eta)>=0, "nonnegative reference eta")
            positive_lower(api,q);positive_lower(api,lengths[i])
            x=4*j*eta*q*lengths[i]
            if api.upper(eta)==0:
                p[i]=p[i+1];taus[i]=api.one;sigmas[i]=api.zero
            else:
                half_decay=api.exp(-x)
                e=half_decay*half_decay
                t=(1-e)/(1+e)
                den=1+(p[i+1]/q)*t
                positive_lower(api,den)
                p[i]=(p[i+1]+q*t)/den
                taus[i]=2*half_decay/((1+e)*den)
                sigmas[i]=t/(q+p[i+1]*t)
            positive_lower(api,p[i])
        H=api.zero;parents=[]
        for i in range(n):
            pmin=min(positive_lower(api,p[i]),positive_lower(api,p[i+1]))
            pmax=maximum(api,[p[i],p[i+1]])
            rate=api.lower(4*j*etas[i]*pmin)
            require(rate>=0, "whole profile lower decay")
            if api.upper(etas[i])==0:
                Hsup=api.upper(H)
            else:
                Hsup=maximum(api,[H,api.one/(2*pmin)])
            if rate==0:
                decay=(api.one,api.upper(lengths[i]))
            else:
                decay=(api.upper(api.exp(-rate*positive_lower(api,lengths[i]))),
                       api.upper((1-api.exp(-rate*api.upper(lengths[i])))/rate))
            parents.append({"p":pmax,"H":Hsup,"K":api.one,"rate":rate,"decay":decay})
            H=api.upper(taus[i]*taus[i]*H+sigmas[i])
            require(H>=0, "analytic H>=0 with a complete upper")
        result[j]=parents
    return result


class GreenMajorant:
    """The exact WPS positive two-triangle majorant in physical real coordinates.

    Input is raw body Fourier L2. Output is body scaled by S, plus optional
    root odd/mean and true H^-5/6 outer atoms. No high inverse is extended to
    an unrelated full-circle domain. Root/outer atoms occur only for low.
    """
    def __init__(self,api,lengths,modes,profiles,scales,thetas,include_mean=False,
                 include_atoms=False):
        self.api,self.lengths=api,list(lengths)
        self.modes=tuple(modes);self.profiles=profiles
        self.scales=list(scales);self.thetas=thetas
        self.include_mean,self.include_atoms=include_mean,include_atoms
        self.coords=tuple([(0,j) for j in modes]+
            ([(1,0)] if include_mean else [])+[(1,j) for j in modes])
        self.position={key:i for i,key in enumerate(self.coords)}
        self.in_dim=self.out_dim=len(self.coords)
        self.atom_coords=tuple(([(0,j) for j in modes]+
            ([(1,0)] if include_mean else [])+[(2,j) for j in modes])
            if include_atoms else [])
        self.atom_position={key:i for i,key in enumerate(self.atom_coords)}
        self.atoms=len(self.atom_coords)
        require(len(scales)==len(lengths),"complete S factors")

    def forward(self,field):
        api,n=self.api,len(self.lengths)
        require(len(field)==n and all(len(r)==self.in_dim for r in field),
                "whole continuous raw source")
        body=[[api.zero for _ in self.coords] for _ in range(n)]
        atoms=[api.zero for _ in self.atom_coords]
        for j in self.modes:
            odd=self.position[(0,j)];even=self.position[(1,j)]
            profiles=self.profiles[j]
            rates=[p["rate"] for p in profiles]
            decay=[p["decay"] for p in profiles]
            fj=[api.upper(p["H"]*row[odd]+p["K"]*row[even])
                for p,row in zip(profiles,field)]
            fl=[api.upper(row[odd]+p["p"]*row[even])
                for p,row in zip(profiles,field)]
            forward,end=scalar_positive_sweep(api,self.lengths,rates,fj,api.zero,coefficients=decay)
            backward,start=scalar_positive_sweep(api,self.lengths,rates,fl,api.zero,True,decay)
            for i,p in enumerate(profiles):
                body[i][odd]=api.upper(p["p"]*forward[i]+p["K"]*backward[i])
                body[i][even]=api.upper(self.scales[i]*(
                    forward[i]+p["H"]*backward[i]))
            if self.include_atoms:
                atoms[self.atom_position[(0,j)]]=start
                atoms[self.atom_position[(2,j)]]=api.upper(self.thetas[j]*end)
        if self.include_mean:
            mean=self.position[(1,0)]
            backward,start=scalar_positive_sweep(api,self.lengths,
                [api.zero]*n,[row[mean] for row in field],api.zero,True)
            for i in range(n):
                body[i][mean]=api.upper(self.scales[i]*backward[i])
            if self.include_atoms:
                atoms[self.atom_position[(1,0)]]=start
        return {"body":body,"atoms":atoms}

    def reverse(self,value):
        api,n=self.api,len(self.lengths)
        require(len(value["body"])==n and len(value["atoms"])==self.atoms,
                "whole continuous adjoint body and atoms")
        field=[[api.zero for _ in self.coords] for _ in range(n)]
        for j in self.modes:
            odd=self.position[(0,j)];even=self.position[(1,j)]
            profiles=self.profiles[j];rates=[p["rate"] for p in profiles]
            decay=[p["decay"] for p in profiles]
            f=[api.upper(p["p"]*row[odd]+self.scales[i]*row[even])
                for i,(p,row) in enumerate(zip(profiles,value["body"]))]
            r=[api.upper(p["K"]*row[odd]+self.scales[i]*p["H"]*row[even])
                for i,(p,row) in enumerate(zip(profiles,value["body"]))]
            outer=(api.upper(self.thetas[j]*value["atoms"][self.atom_position[(2,j)]])
                   if self.include_atoms else api.zero)
            root=(value["atoms"][self.atom_position[(0,j)]]
                  if self.include_atoms else api.zero)
            backward,_=scalar_positive_sweep(api,self.lengths,rates,f,outer,True,decay)
            forward,_=scalar_positive_sweep(api,self.lengths,rates,r,root,coefficients=decay)
            for i,p in enumerate(profiles):
                field[i][odd]=api.upper(p["H"]*backward[i]+forward[i])
                field[i][even]=api.upper(p["K"]*backward[i]+p["p"]*forward[i])
        if self.include_mean:
            mean=self.position[(1,0)]
            root=(value["atoms"][self.atom_position[(1,0)]]
                  if self.include_atoms else api.zero)
            forward,_=scalar_positive_sweep(api,self.lengths,[api.zero]*n,
                [self.scales[i]*row[mean] for i,row in enumerate(value["body"])],root)
            for i in range(n):
                field[i][mean]=forward[i]
        return field


class Composition:
    def __init__(self,left,right):
        require(right.atoms==0 and right.out_dim==left.in_dim,"typed complete composition")
        self.left,self.right=left,right
        self.in_dim,self.out_dim,self.atoms=right.in_dim,left.out_dim,left.atoms
    def forward(self,field):
        return self.left.forward(self.right.forward(field)["body"])
    def reverse(self,value):
        return self.right.reverse({"body":self.left.reverse(value),"atoms":[]})


class SumMap:
    def __init__(self,api,maps):
        require(bool(maps),"complete nonempty map sum")
        self.api,self.maps=api,list(maps)
        first=maps[0]
        self.in_dim,self.out_dim,self.atoms=first.in_dim,first.out_dim,first.atoms
        require(all((m.in_dim,m.out_dim,m.atoms)==
                (self.in_dim,self.out_dim,self.atoms) for m in maps),"same whole operator spaces")
    def forward(self,field):
        values=[m.forward(field) for m in self.maps]
        return {"body":[[self.api.upper(sum((v["body"][i][j] for v in values),self.api.zero))
                        for j in range(self.out_dim)] for i in range(len(field))],
                "atoms":[self.api.upper(sum((v["atoms"][j] for v in values),self.api.zero))
                         for j in range(self.atoms)]}
    def reverse(self,value):
        values=[m.reverse(value) for m in self.maps]
        return [[self.api.upper(sum((v[i][j] for v in values),self.api.zero))
                 for j in range(self.in_dim)] for i in range(len(value["body"]))]


class DiagonalMap:
    def __init__(self,api,diagonal):
        self.api,self.diagonal=api,diagonal
        self.in_dim=self.out_dim=len(diagonal[0]);self.atoms=0
    def forward(self,field):
        require(len(field)==len(self.diagonal)
                and all(len(row)==self.in_dim for row in field),"whole diagonal field")
        return {"body":[diagonal_action(self.api,row,d)
                        for row,d in zip(field,self.diagonal)],"atoms":[]}
    def reverse(self,value):
        require(value["atoms"]==[],"diagonal has no atoms")
        return self.forward(value["body"])["body"]


def full_kernel_schur(api,operator,input_weights,output_weights):
    """Whole weighted Schur for the SAME declared kernel, not sampled columns.

    Each forward/reverse routine gives a pointwise envelope of its declared
    positive kernel on the full ordinary-dr source measure. Atomic output
    rows occur in reverse as mass-one atoms. No numerical envelope routine is
    assumed to be its own transposed matrix.
    """
    require(len(input_weights)==len(output_weights["body"])
            and all(len(row)==operator.in_dim for row in input_weights)
            and all(len(row)==operator.out_dim for row in output_weights["body"])
            and len(output_weights["atoms"])==operator.atoms,"complete comparison coordinates")
    vu=[[api.upper(v) for v in row] for row in input_weights]
    vl=[[positive_lower(api,v) for v in row] for row in input_weights]
    wu={"body":[[api.upper(v) for v in row] for row in output_weights["body"]],
        "atoms":[api.upper(v) for v in output_weights["atoms"]]}
    wl={"body":[[positive_lower(api,v) for v in row] for row in output_weights["body"]],
        "atoms":[positive_lower(api,v) for v in output_weights["atoms"]]}
    rows=operator.forward(vu);cols=operator.reverse(wu)
    row_ratios=[api.upper(v/l) for row,lower in zip(rows["body"],wl["body"])
                for v,l in zip(row,lower)]
    row_ratios.extend(api.upper(v/l) for v,l in zip(rows["atoms"],wl["atoms"]))
    col_ratios=[api.upper(v/l) for row,lower in zip(cols,vl) for v,l in zip(row,lower)]
    r=maximum(api,row_ratios);c=maximum(api,col_ratios)
    return {"row_upper":r,"column_upper":c,
            "full_input_not_samples":True,"all_output_atoms_retained":True}


def complete_E_D_T(api,e_rho,w0,K_H,eps_H,eps_b,o_H,o_b,t_H,t_b):
    """Exactly WPS.24; all arguments are saved complete same-candidate bounds."""
    one=api.one
    head=K_H+eps_H
    e=api.upper(e_rho+(one+e_rho)*api.sqrt(w0*w0*head*head+eps_b*eps_b)
                +api.sqrt(w0*w0*o_H*o_H+o_b*o_b))
    d=api.upper((one+e_rho)*head+o_H)
    t=api.upper(api.sqrt(w0*w0*t_H*t_H+t_b*t_b))
    defect=api.upper(e+3*d*t)
    return {"e":e,"d":d,"t":t,"complete_finite_defect":defect,
            "strict_finite_gate":defect<one}


def published_kernel_norm(api, operator, input_weights, output_weights, emit, prefix):
    """Save each completed whole row/column/norm before using its readback."""
    require(len(input_weights)==len(output_weights["body"])
            and all(len(row)==operator.in_dim for row in input_weights)
            and all(len(row)==operator.out_dim for row in output_weights["body"])
            and len(output_weights["atoms"])==operator.atoms,"complete Schur spaces")
    upper_in=[[api.upper(v) for v in row] for row in input_weights]
    rows=operator.forward(upper_in)
    ratios=[api.upper(v/positive_lower(api,w))
            for row,weights in zip(rows["body"],output_weights["body"])
            for v,w in zip(row,weights)]
    ratios += [api.upper(v/positive_lower(api,w))
               for v,w in zip(rows["atoms"],output_weights["atoms"])]
    r=emit(prefix+"_row_upper",maximum(api,ratios))
    upper_out={"body":[[api.upper(v) for v in row] for row in output_weights["body"]],
               "atoms":[api.upper(v) for v in output_weights["atoms"]]}
    columns=operator.reverse(upper_out)
    ratios=[api.upper(v/positive_lower(api,w))
            for row,weights in zip(columns,input_weights)
            for v,w in zip(row,weights)]
    c=emit(prefix+"_column_upper",maximum(api,ratios))
    return emit(prefix+"_norm_upper",api.upper(api.sqrt(r*c)))


def local_norm(api, majorant):
    """Complete whole angular norm; not a sampled matrix or a norm difference."""
    rows=majorant.apply([api.one]*len(majorant.inputs))
    cols=majorant.apply([api.one]*len(majorant.outputs),transpose=True)
    return api.upper(api.sqrt(maximum(api,rows)*maximum(api,cols)))


class ZeroMap:
    def __init__(self,api,parents,in_dim,out_dim,atoms=0):
        self.api,self.parents=api,parents
        self.in_dim,self.out_dim,self.atoms=in_dim,out_dim,atoms
    def forward(self,field):
        require(len(field)==self.parents and all(len(r)==self.in_dim for r in field),
                "whole zero-map input")
        return {"body":[[self.api.zero]*self.out_dim for _ in range(self.parents)],
                "atoms":[self.api.zero]*self.atoms}
    def reverse(self,value):
        require(len(value["body"])==self.parents
                and all(len(r)==self.out_dim for r in value["body"])
                and len(value["atoms"])==self.atoms,"whole zero-map adjoint input")
        return [[self.api.zero]*self.in_dim for _ in range(self.parents)]


def kernel_factor_majorant(api,actual,principal,chi,chi_prime,
                          inputs,outputs,sqrt_two):
    """chi' I - chi*(A_HH,repaired-centre-D_H), signed before abs."""
    def local(output,input_):
        identity=api.one if output==input_ else api.zero
        signed=local_entry(actual,output,input_,sqrt_two,api.zero)-(
            frozen_principal_entry(principal["eta"],principal["q"],
                                   output,input_,api.zero))
        return chi_prime*identity-chi*signed
    a=[{j:-chi*v for j,v in p.items()} for p in actual["a"]]
    return AngularMajorant(api,inputs,outputs,sqrt_two,local,[(a,actual["b"])],
                           mean_row=None)
