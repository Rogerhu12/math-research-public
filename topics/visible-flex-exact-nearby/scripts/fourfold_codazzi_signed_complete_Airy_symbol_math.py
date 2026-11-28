"""New signed, whole-circle Airy source algebra in the original physical angle.

No numerical import, entry point, file access or arithmetic is performed here.
The public owner supplies directed real/complex scalars and the complete finite
Laurent algebra.  The coefficient and operator sums below retain their signs
until the WHOLE requested expression has been formed.  This is neither the old
WSM positive N6 calculator nor an invocation of its successful targets.

Two independent parts are provided:
* complete raw rQ/T0/V0/theta coefficients, with qualified ordinary-r jets;
* the entire U.7/U.9/U.11 and G.7/G.12--14 source, as an exact operator graph.

The graph's I, Pi and J are the original physical-circle operators.  In
particular, a constant multiplied by I(P v) is not passed through I again.
"""
from fractions import Fraction
from math import factorial


PHYSICAL_FREQUENCY = 4
DERIVED_FIELDS = ("tQ", "T0", "vAC", "rQ", "V0", "theta")
COEFFICIENT_TARGET_FIELDS = ("T0", "rQ", "V0", "theta")
REQUIRED_RAW_FIELDS = ("u", "v", "beta", "K", "gamma")


def require(ok, message):
    if not ok:
        raise ValueError(message)


class RadialJet:
    """Actual normalized ordinary-r derivatives at one common, variable point.

    A coefficient may enclose its value on an entire real cell.  It is NOT a
    polynomial approximation with a differentiable scalar error.  Products use
    the intersection of the qualified orders.  Missing derivatives are never
    filled by zero; the only zero extension is an explicitly constant input.
    """
    def __init__(self, coefficients, lp):
        require(bool(coefficients), "a true jet retains its value")
        self.lp = lp
        self.c = tuple(x if isinstance(x, lp) else lp.const(x)
                       for x in coefficients)

    @property
    def n(self):
        return len(self.c)

    @classmethod
    def constant(cls, value, n, lp):
        require(type(n) is int and n > 0, "positive qualified constant order")
        return cls([value]+[0]*(n-1), lp)

    def restrict(self, n):
        require(type(n) is int and 0 < n <= self.n,
                "restriction cannot invent a radial derivative")
        return RadialJet(self.c[:n], self.lp)

    def _coerce(self, other):
        return (other if isinstance(other, RadialJet)
                else RadialJet.constant(other, self.n, self.lp))

    def __neg__(self):
        return RadialJet([-x for x in self.c], self.lp)

    def __add__(self, other):
        other = self._coerce(other)
        require(other.lp is self.lp, "one complete Laurent arithmetic")
        n = min(self.n, other.n)
        return RadialJet([self.c[k]+other.c[k] for k in range(n)], self.lp)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        require(other.lp is self.lp, "one complete Laurent arithmetic")
        n = min(self.n, other.n)
        return RadialJet([sum((self.c[j]*other.c[k-j]
                              for j in range(k+1)), self.lp())
                          for k in range(n)], self.lp)

    __rmul__ = __mul__

    def inverse_scalar(self):
        """Exact reciprocal recurrence, only for a genuinely radial scalar."""
        values = [value.scalar() for value in self.c]
        require(not values[0].contains(0), "true scalar reciprocal gap")
        out = [1/values[0]]
        for k in range(1, self.n):
            out.append(-sum((values[j]*out[k-j] for j in range(1,k+1)),
                            values[0]*0)/values[0])
        return RadialJet(out, self.lp)

    def __truediv__(self, other):
        return self * self._coerce(other).inverse_scalar()

    def __rtruediv__(self, other):
        return self._coerce(other) * self.inverse_scalar()

    def __pow__(self, power):
        require(type(power) is int, "integer exact radial-jet power")
        if power < 0:
            return self.inverse_scalar()**(-power)
        out = RadialJet.constant(1, self.n, self.lp)
        base = self
        while power:
            if power & 1:
                out = out*base
            power //= 2
            if power:
                base = base*base
        return out

    def exp_scalar(self):
        """Ordinary exp on true scalar jets, not exp of a saved norm bound."""
        values = [value.scalar() for value in self.c]
        out = [values[0].exp()]
        for k in range(1, self.n):
            out.append(sum((j*values[j]*out[k-j] for j in range(1,k+1)),
                           values[0]*0)/k)
        return RadialJet(out, self.lp)

    def radial(self, order=1):
        require(type(order) is int and 0 <= order < self.n,
                "actual next ordinary-r derivative is required")
        return RadialJet([factorial(k+order)//factorial(k)*self.c[k+order]
                          for k in range(self.n-order)], self.lp)

    def angular(self, order=1):
        require(type(order) is int and order >= 0, "ordinary angular order")
        return RadialJet([value.d(order) for value in self.c], self.lp)

    def primitive(self):
        return RadialJet([value.primitive() for value in self.c], self.lp)

    def mean(self):
        return RadialJet([value.mean() for value in self.c], self.lp)

    def project(self):
        return RadialJet([value.ne() for value in self.c], self.lp)


def material_derivative(value, drift):
    """D=partial_r-d partial_phi, in outward physical r orientation."""
    return value.radial()-drift*value.angular()


def complete_raw_coefficients(raw):
    """Form the COMPLETE signed U.5/U.6/U.8/U.10 coefficients once.

    All five raw jets belong to one point of one whole original cell and to
    the same selected delta.  The output retains the independent physical
    even mean of v; it does not assume that the repaired background solves
    the nonlinear PDE.  No Fourier product is projected to a retained head.
    """
    require(set(raw) == set(REQUIRED_RAW_FIELDS), "all five full physical fields")
    u,v,beta,K,gamma = (raw[name] for name in REQUIRED_RAW_FIELDS)
    require(all(isinstance(x, RadialJet) and x.n >= 3 for x in raw.values()),
            "three or more true radial derivative slots, including value")
    n = min(x.n for x in raw.values())
    u,v,beta,K,gamma = (x.restrict(n) for x in (u,v,beta,K,gamma))
    for scalar in (beta,K,gamma):
        for coefficient in scalar.c:
            coefficient.scalar()
    m = v.mean()
    eta = -gamma*m
    require(eta.c[0].scalar().lower() > 0, "same true positive eta=-gamma mean(v)")
    d = -beta*(u*u+K*v*v).primitive()
    ell = -2*beta*u*v
    e = -beta*(1+3*u*u+K*v*v)
    b0 = beta*(1-u*u-3*K*v*v)
    eta_ratio = eta.radial()/eta
    tQ = eta_ratio+d.angular()+e
    T0 = tQ+b0
    vAC = ell*ell-4*beta*eta*v*u.angular()
    rQ = (material_derivative(ell,d)+eta*e.angular()
          -2*beta*eta*u.angular()*u-ell*(eta_ratio+d.angular()))
    V0 = tQ*b0-material_derivative(b0,d)-K*vAC
    theta = rQ/eta-2*beta*K*v*v.angular()
    answer = {"u":u,"v":v,"beta":beta,"K":K,"gamma":gamma,"m":m,
              "eta":eta,"d":d,"ell":ell,"e":e,"b0":b0,
              "eta_r_over_eta":eta_ratio,"tQ":tQ,"T0":T0,
              "vAC":vAC,"rQ":rQ,"V0":V0,"theta":theta}
    require(all(answer[name].n >= n-1 for name in DERIVED_FIELDS),
            "the complete true first radial coefficient loss is recorded")
    return answer


class OperatorGraph:
    """Hash-consed exact linear operator expressions, with signed scalars.

    The graph is a concrete representation of the fixed U/G expressions.
    ``apply`` traverses it using one caller-supplied actual circle algebra.
    That algebra has project, multiply, primitive, mean and inverse_A.  Its
    inverse_A MUST be the same true J; substituting an amplitude matrix B_j
    or a finite Fourier inverse is not an implementation of this graph.
    """
    def __init__(self):
        self.nodes = []
        self._keys = {}
        self.zero = self._node(("zero",))
        self.identity = self._node(("identity",))
        self.P = self._node(("project",))
        self.I = self._node(("primitive",))
        self.Pi = self._node(("mean",))
        self.J = self._node(("inverse_A",))

    def _node(self, key):
        if key not in self._keys:
            self._keys[key] = len(self.nodes)
            self.nodes.append(key)
        return self._keys[key]

    def scalar(self, value, node):
        value = Fraction(value)
        if not value or node == self.zero:
            return self.zero
        if value == 1:
            return node
        old = self.nodes[node]
        if old[0] == "scale":
            return self.scalar(value*Fraction(old[1]), old[2])
        return self._node(("scale",str(value),node))

    def add(self, *signed_nodes):
        """Collect exactly identical full graphs BEFORE any interval norm."""
        coefficients = {}
        def collect(node, factor):
            kind = self.nodes[node][0]
            if kind == "zero" or not factor:
                return
            if kind == "sum":
                for coefficient, child in self.nodes[node][1]:
                    collect(child, factor*Fraction(coefficient))
            elif kind == "scale":
                _, coefficient, child = self.nodes[node]
                collect(child, factor*Fraction(coefficient))
            else:
                coefficients[node] = coefficients.get(node,Fraction(0))+factor
        for node in signed_nodes:
            collect(node,Fraction(1))
        terms = tuple((str(value),node) for node,value in sorted(coefficients.items())
                      if value)
        if not terms:
            return self.zero
        if len(terms) == 1:
            return self.scalar(Fraction(terms[0][0]),terms[0][1])
        return self._node(("sum",terms))

    def compose(self, *nodes):
        """Left-to-right written operator product; rightmost acts first."""
        flat = []
        for node in nodes:
            if node == self.zero:
                return self.zero
            if node == self.identity:
                continue
            row = self.nodes[node]
            flat.extend(row[1] if row[0] == "product" else (node,))
        if not flat:
            return self.identity
        if len(flat) == 1:
            return flat[0]
        return self._node(("product",tuple(flat)))

    def M(self, name):
        require(isinstance(name,str) and name, "named complete signed multiplier")
        return self._node(("multiply",name))

    def T(self, name):
        return self.compose(self.P,self.M(name),self.P)

    def rank(self, left, right):
        return self.compose(self.P,self.M(left),self.Pi,self.M(right),self.P)

    def nonlocal_term(self, scale, left, right):
        return self.compose(self.M(scale),self.T(left),self.I,self.T(right))

    def derivative_nonlocal(self, scale, left, right):
        return self.add(self.nonlocal_term(scale+"_r",left,right),
                        self.nonlocal_term(scale,left+"_r",right),
                        self.nonlocal_term(scale,left,right+"_r"))

    def commutator_transport_primitive(self, left, right):
        """The exact three terms of U.3; all two mean ranks remain."""
        first = self.compose(self.add(self.T("d*"+left+"_phi"),
                                      self.scalar(-1,self.rank(left,"d_phi"))),
                             self.I,self.T(right))
        second = self.compose(self.T(left),self.I,self.T("d_phi"),self.T(right))
        third = self.compose(self.T(left),self.I,
                             self.add(self.T("d*"+right+"_phi"),
                                      self.scalar(-1,self.rank(right,"d_phi"))))
        return self.add(first,second,third)

    def evaluate(self, root, value, algebra):
        """Evaluate an entire signed graph in the caller's actual circle space."""
        memo = {}
        # A node can be applied to several different intermediate arguments;
        # only identical (node, immutable state key) applications are shared.
        def walk(node, state):
            key = (node,algebra.state_key(state))
            if key in memo:
                return memo[key]
            row = self.nodes[node]
            kind = row[0]
            if kind == "zero":
                out = algebra.zero_like(state)
            elif kind == "identity":
                out = state
            elif kind == "project":
                out = algebra.project(state)
            elif kind == "primitive":
                out = algebra.primitive(state)
            elif kind == "mean":
                out = algebra.mean(state)
            elif kind == "inverse_A":
                out = algebra.inverse_A(state)
            elif kind == "multiply":
                out = algebra.multiply(row[1],state)
            elif kind == "scale":
                out = algebra.scale(Fraction(row[1]),walk(row[2],state))
            elif kind == "sum":
                out = algebra.add(*(algebra.scale(Fraction(c),walk(child,state))
                                    for c,child in row[1]))
            elif kind == "product":
                out = state
                for child in reversed(row[1]):
                    out = walk(child,out)
            else:
                raise ValueError("unknown exact circle node")
            memo[key] = out
            return out
        return walk(root,value)


def complete_old_circle_graph():
    """The exact complete U.7/U.9/U.11 operators, with no norm substitution."""
    g = OperatorGraph()
    na = g.nonlocal_term("c","v_phi","u")
    nc = g.nonlocal_term("c","u_phi","v")
    ne = g.nonlocal_term("c","u_phi","u")
    nb = g.nonlocal_term("cB","v_phi","v")
    L = g.add(g.T("ell"),na)
    B = g.add(g.T("b0"),nb)
    sac = g.add(
        g.compose(g.M("c*eta"),g.add(
            g.scalar(-1,g.rank("u_phi","v")),
            g.compose(g.T("u_phiphi"),g.I,g.T("v")),
            g.rank("v_phi","u"),
            g.compose(g.T("v_phi"),g.I,g.T("u_phi")))),
        g.scalar(-1,g.rank("ell","ell")),
        g.compose(g.T("ell"),nc),g.compose(na,g.T("ell")),g.compose(na,nc))
    sq = g.add(
        g.derivative_nonlocal("c","v_phi","u"),
        g.scalar(-1,g.compose(g.M("c"),g.commutator_transport_primitive("v_phi","u"))),
        g.rank("ell","d_phi"),
        g.scalar(-1,g.compose(g.M("c*eta"),g.rank("u_phi","u"))),
        g.compose(g.M("c*eta"),g.T("u_phiphi"),g.I,g.T("u")),
        g.scalar(-1,g.rank("ell","e")),g.rank("tQ","ell"),
        g.compose(g.T("ell"),ne),g.compose(na,g.T("e")),g.compose(na,ne),
        g.scalar(-1,g.compose(g.T("tQ"),na)))
    rq = g.add(g.T("rQ"),sq)
    sv = g.add(
        g.scalar(-1,g.rank("tQ","b0")),
        g.scalar(-1,g.rank("b0","d_phi")),
        g.compose(g.T("tQ"),nb),g.compose(rq,g.J,B),
        g.scalar(-1,g.derivative_nonlocal("cB","v_phi","v")),
        g.compose(g.M("cB"),g.commutator_transport_primitive("v_phi","v")),
        g.scalar(-1,g.compose(g.M("K"),sac)))
    return g,{"N_A":na,"N_C":nc,"N_E":ne,"N_B":nb,"L":L,"B":B,
              "S_AC":sac,"S_Q":sq,"R_Q":rq,"S_V":sv}


def coefficient_dictionary(jets):
    """All actual named multipliers required by the fixed full U/G graph."""
    out = dict(jets)
    out["c"] = -2*jets["beta"]
    out["cB"] = -2*jets["beta"]*jets["K"]
    for key in ("u","v","d","ell","e","b0","tQ","c","cB"):
        out[key+"_phi"] = out[key].angular()
        if out[key].n >= 2:
            out[key+"_r"] = out[key].radial()
    for key in ("u","v"):
        out[key+"_phiphi"] = out[key].angular(2)
        out[key+"_phi_phi"] = out[key+"_phiphi"]
        out[key+"_phi_r"] = out[key].radial().angular()
    for key in ("u","v","u_phi","v_phi"):
        out["d*"+key+"_phi"] = out["d"]*out[key+"_phi"]
    out["c*eta"] = out["c"]*out["eta"]
    return out


class CellJet:
    """Directed mixed jets on one common real r/phi/parameter cell.

    Entry (p,q) encloses partial_r^p partial_phi^q/(p!q!) of the SAME
    scalar.  Multiplication is full signed convolution, before absolute
    values.  These are pointwise derivative boxes; no Fourier band or
    scalar interpolation error is silently assigned derivatives.
    """
    def __init__(self, coefficients):
        require(coefficients and coefficients[0], "complete nonempty mixed jet")
        self.c = tuple(tuple(row) for row in coefficients)
        self.nr,self.na = len(self.c),len(self.c[0])
        require(all(len(row) == self.na for row in self.c),
                "complete rectangular derivative shape")

    @classmethod
    def constant(cls, value, nr, na):
        require(type(nr) is type(na) is int and nr > 0 and na > 0,
                "explicit constant derivative domain")
        zero = value*0
        return cls([[value if (p,q) == (0,0) else zero
                     for q in range(na)] for p in range(nr)])

    def restrict(self, nr, na):
        require(0 < nr <= self.nr and 0 < na <= self.na,
                "mixed derivative restriction only")
        return CellJet([row[:na] for row in self.c[:nr]])

    def _coerce(self, other):
        return other if isinstance(other,CellJet) else CellJet.constant(
            self.c[0][0]*0+other,self.nr,self.na)

    def __neg__(self):
        return CellJet([[-x for x in row] for row in self.c])

    def __add__(self, other):
        other = self._coerce(other)
        nr,na = min(self.nr,other.nr),min(self.na,other.na)
        return CellJet([[self.c[p][q]+other.c[p][q] for q in range(na)]
                        for p in range(nr)])

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other)-self

    def __mul__(self, other):
        other = self._coerce(other)
        nr,na = min(self.nr,other.nr),min(self.na,other.na)
        zero = self.c[0][0]*0
        return CellJet([[sum((self.c[i][j]*other.c[p-i][q-j]
                              for i in range(p+1) for j in range(q+1)),zero)
                         for q in range(na)] for p in range(nr)])

    __rmul__ = __mul__

    def reciprocal(self):
        require(not self.c[0][0].contains(0), "actual pointwise reciprocal gap")
        zero = self.c[0][0]*0
        out = [[zero for q in range(self.na)] for p in range(self.nr)]
        out[0][0] = 1/self.c[0][0]
        for total in range(1,self.nr+self.na-1):
            for p in range(self.nr):
                q = total-p
                if not 0 <= q < self.na:
                    continue
                out[p][q] = -sum((self.c[i][j]*out[p-i][q-j]
                    for i in range(p+1) for j in range(q+1) if (i,j) != (0,0)),
                    zero)/self.c[0][0]
        return CellJet(out)

    def __truediv__(self, other):
        return self*self._coerce(other).reciprocal()

    def __rtruediv__(self, other):
        return self._coerce(other)*self.reciprocal()

    def __pow__(self, power):
        require(type(power) is int, "integer exact mixed-jet power")
        if power < 0:
            return self.reciprocal()**(-power)
        out = CellJet.constant(self.c[0][0]*0+1,self.nr,self.na)
        base = self
        while power:
            if power & 1:
                out = out*base
            power //= 2
            if power:
                base = base*base
        return out

    def derivative(self, radial=0, angular=0):
        require(type(radial) is type(angular) is int
                and 0 <= radial < self.nr and 0 <= angular < self.na,
                "all true mixed predecessors retained")
        return CellJet([[
            (factorial(p+radial)//factorial(p))
            *(factorial(q+angular)//factorial(q))*self.c[p+radial][q+angular]
            for q in range(self.na-angular)] for p in range(self.nr-radial)])


def vector_add(*vectors):
    require(vectors and all(len(v) == 2 for v in vectors),
            "two complete genuine reference components")
    return tuple(sum((v[i] for v in vectors[1:]),vectors[0][i]) for i in range(2))


def vector_scale(value, vector):
    require(len(vector) == 2, "two-component amplitude")
    return tuple(value*x for x in vector)


def vector_derivative(vector, radial=0, angular=0):
    return tuple(x.derivative(radial,angular) for x in vector)


def matrix_vector(matrix, vector):
    require(len(matrix) == 2 and all(len(row) == 2 for row in matrix)
            and len(vector) == 2, "complete two-by-two ordered product")
    return tuple(matrix[i][0]*vector[0]+matrix[i][1]*vector[1] for i in range(2))


def complete_genuine_local_packet(coefficients, geometry, potential,
                                  w0, w1ext, inverse_n_squared, sign):
    """New signed global G.5--G.14 packet; no old scalar DAG is evaluated.

    The entire true-flow identity is an ADMITTED mathematical predecessor.
    The numerical caller must provide actual derivative enclosures of that
    same flow, never a fixed approximate phase in an unbounded n exponent.
    Potential is the complete WUA C64 extension, with its true T derivative.
    w1ext contains the NONZERO B_ext tail even when V_ext itself vanishes.

    inverse_n_squared encloses 1/n^2 on a DECLARED whole input-frequency
    interval.  It is a constant in r and phi.  This function first proves its
    new deformed determinant gap, then computes the whole signed vectors.
    """
    require(sign in (-1,1), "both physical carrier signs remain separate")
    require(set(geometry) == {"T","Q","x","y"},
            "same actual fold T,Q,X_phi,T_phi")
    require(set(potential) == {"V","V_T"},
            "complete extended potential and its actual T derivative")
    require(all(isinstance(x,CellJet) for x in geometry.values())
            and all(isinstance(x,CellJet) for x in potential.values())
            and all(isinstance(x,CellJet) for x in (*w0,*w1ext)),
            "full signed mixed derivative packets")
    T,Q,x,y = (geometry[name] for name in ("T","Q","x","y"))
    V,VT = potential["V"],potential["V_T"]
    d,eta,T0,V0,theta = (coefficients[name] for name in ("d","eta","T0","V0","theta"))
    v = coefficients["v"]
    parameter = x._coerce(inverse_n_squared)
    require(parameter.c[0][0].imag.contains(0)
            and parameter.c[0][0].real.lower() >= 0,
            "entire nonnegative real inverse-square frequency interval")
    unit = x.c[0][0]*0+1
    imaginary = coefficients["imaginary_unit"]
    require(imaginary*imaginary == -unit, "exact complex i")
    s = sign*imaginary
    determinant = x*x+(T-parameter*V)*y*y
    det0 = determinant.c[0][0]
    require(det0.imag.contains(0) and det0.real.lower() > 0,
            "NEW complete global deformed old-circle determinant gap")
    invdet = determinant.reciprocal()
    inverse = ((-s*x*invdet,y*(T-parameter*V)*invdet),
               (y*invdet,-s*x*invdet))
    mu = Q*Q*(x*x+T*y*y)
    eta2K = Q*Q*T

    def D_scalar(value):
        return value.derivative(radial=1)-d*value.derivative(angular=1)

    def D(vector):
        return tuple(D_scalar(value) for value in vector)

    def K_action(vector):
        return (T*vector[1],vector[0])

    def R_without_theta(vector):
        # B e1 (i epsilon y, x) is an ORDERED column times row.
        contraction = s*y*vector[0]+x*vector[1]
        return vector_scale(Q*V, (inverse[0][0]*contraction,
                                   inverse[1][0]*contraction))

    def R(vector):
        return vector_scale(theta,R_without_theta(vector))

    # Use the exact characteristic identity DT=Qx before interval arithmetic.
    # Differentiating an approximate T and subtracting independent boxes would
    # reintroduce a false leading-order residual for every unbounded n.
    DT = Q*x
    AT = D_scalar(DT)+eta2K*T.derivative(angular=2)-T0*DT

    def A(vector):
        dw = D(vector)
        return vector_add(D(dw),
            vector_scale(eta2K,vector_derivative(vector,angular=2)),
            vector_scale(-T0,dw),vector_scale(V0-mu*V,vector),
            vector_scale(s*theta*Q,K_action(vector)))

    def C(vector):
        inside = vector_add(
            vector_scale(2*Q*V,vector_add(vector_scale(x,D(vector)),
                vector_scale(Q*T*y,vector_derivative(vector,angular=1)))),
            vector_scale(mu*VT+AT*V,vector))
        # E12 remains on the LEFT after the complete vector is formed.
        return (inside[1],inside[0]*0)

    def old_circle(vector):
        # Exact G.5/G.12 reduction, retaining the complete n^-2 correction.
        p = vector_add(vector_scale(-s*Q,K_action(vector)),
                       vector_scale(-parameter,R_without_theta(vector)))
        h = tuple(value/eta for value in p)
        yy = vector_scale(v,p)
        gg = vector_add(D(vector),vector_scale(-1,vector_derivative(p,angular=1)))
        # q=v*g-v_phi*p is the full signed G.10 identity; it preserves the
        # correlation of v*D(w) and partial_phi(v*p).
        qq = vector_add(vector_scale(v,gg),
                        vector_scale(-v.derivative(angular=1),p))
        return {"p":p,"h":h,"y":yy,"g":gg,"q":qq}

    L1 = vector_add(A(w1ext),vector_scale(-1,C(w0)))
    L2 = vector_add(vector_scale(-1,C(w1ext)),R(w0))
    L3 = R(w1ext)
    return {"deformed_determinant":determinant,"B_genuine":inverse,
            "L1":L1,"L2":L2,"L3":L3,
            "density0":old_circle(w0),"density1":old_circle(w1ext),
            "A_T":AT,"mu":mu,"same_DT_equals_Q_x_used_exactly":True,
            "n_mean_replaced_by_complete_g_identity":True}


def complete_genuine_source(circle, graph, roots, amplitudes):
    """The fixed full G.12/G.13 expression, before any absolute value.

    ``amplitudes`` contains actual U(w), U(h), U(y), U(g), U(q), all at
    the same physical point/column/profile and with the same actual V_ext.
    The identity Pi U(W)=Pi U(g) has already been proved by the exact full
    circle derivative, and is used here instead of introducing an artificial
    positive factor n.  Both occurrences are literally the SAME scalar.
    """
    require(set(amplitudes) == {"w","h","y","g","q"},
            "all five complete genuine amplitude images")
    P = circle.project
    U = amplitudes
    def apply(name, state):
        return graph.evaluate(roots[name],state,circle)
    ph,py,pg,pq,pw = (P(U[key]) for key in ("h","y","g","q","w"))
    ED = circle.add(pg,circle.scale(-1,apply("L",ph)))
    mean_h,mean_y,mean_g,mean_w = (circle.mean(U[key]) for key in ("h","y","g","w"))
    # This is a vector I(Pv) TIMES the complete scalar mean_g.  It must not
    # be confused with I of a constant mean, which would wrongly vanish.
    I_Pv = circle.primitive(circle.project(circle.coefficient("v")))
    cB = "cB"
    ER_terms = (
        apply("S_Q",ph),
        apply("R_Q",circle.inverse_A(ED)),
        circle.multiply(cB,P(circle.multiply("v_phi",circle.primitive(pq)))),
        circle.scale(-1,circle.multiply_state(P(circle.coefficient("rQ")),mean_h)),
        circle.scale(-1,circle.multiply(cB,
            circle.multiply_state(P(circle.coefficient("v_phi")),mean_y))),
        circle.scale(-1,circle.multiply(cB,
            circle.multiply_state(P(circle.multiply("v_phi",I_Pv)),mean_g))),
    )
    ER = circle.add(*ER_terms)
    N_terms = (
        apply("S_V",pw),circle.scale(-1,ER),
        circle.multiply_state(P(circle.coefficient("T0")),mean_g),
        circle.scale(-1,circle.multiply_state(P(circle.coefficient("V0")),mean_w)),
    )
    return {"E_D":ED,"E_R_terms":ER_terms,"E_R":ER,
            "N_terms":N_terms,"N":circle.add(*N_terms),
            "same_complete_mean_W_equals_mean_g":mean_g}


def complete_physical_mean_source(algebra, scalar_source, Fmean, k2, z, Rmean):
    """WUA.43 exactly, retaining the true nonzero physical even mean z."""
    first = algebra.inverse_A(algebra.project(scalar_source))
    second = algebra.multiply_state(Fmean,k2)
    third = algebra.scale(-1,algebra.multiply_state(z,Rmean))
    return {"g1_terms":(first,second,third),
            "g1":algebra.add(first,second,third),
            "g2":algebra.zero_like(first),
            "g2_zero_requires_exact_mean_ODE_and_same_J":True}


def signed_response_tuple(algebra, positive_correction, seam_mismatch,
                          negative_volume, negative_jumps, waist_difference):
    """Keep the SAME complete boundary-response sum before an operator norm.

    Each argument is already in the identical physical waist realization and
    includes its declared full source/trace/phase maps.  This function does not
    turn an old positive upper, a finite96 column, or a raw jump into a response.
    The parent owner must admit each complete typed carrier.  The true negative
    residual is g_U=L U.  Reception uses the ordinary integral from 0 UP TO the
    root/cut while the solution is propagated BACKWARD to 0.  The two orientation
    signs cancel: g_U and forward jumps [U] both enter with PLUS signs.  The
    positive and finite-root convention is fixed in the first two arguments.
    """
    require(isinstance(negative_jumps,(tuple,list)), "all actual signed interfaces")
    parts = [positive_correction,seam_mismatch,negative_volume]
    parts.extend(negative_jumps)
    parts.append(waist_difference)
    return algebra.add(*parts)
