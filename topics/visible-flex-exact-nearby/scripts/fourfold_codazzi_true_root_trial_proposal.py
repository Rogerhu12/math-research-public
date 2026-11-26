"""TC deterministic finite proposal selection, never a certificate.

Pure functions accept numpy and explicit admitted old midpoint-polynomial
inputs.  They perform no IO and import no numerical package.  Floating
matrices and QR only select exact dyadic endpoint data; the separate TC
directed core pays the complete selected PDE residual afterward.
"""
from fractions import Fraction
from math import factorial, comb, ceil

HEAD = 96
DIMENSION = 193
FLOAT_GRID = 512
EXPONENTIAL_DEGREE = 24
MAX_EXPONENTIAL_SPAN = 1.0
MAX_EXPONENTIAL_SUBSTEPS = 512
RIGHT_ROBIN_SLOPE = Fraction(13,80)


def require(ok,message):
    if not ok:
        raise ValueError(message)


class FloatingCentreReference:
    """Full193 projection of the complete repaired M32 centre.

    This is explicitly a proposal reference at delta=0, NOT a selected
    coefficient enclosure and NOT the WVC hybrid operator.  The old eta
    midpoint choice is harmless here because no estimate is taken from it.
    """
    def __init__(self,np,rows,base,exact_base_offset_midpoints,alpha,read_ball):
        self.np,self.rows,self.base,self.alpha = np,rows,base,float(alpha)
        self.offset = np.asarray(exact_base_offset_midpoints,dtype=float)
        self.read_ball = read_ball
        self.left = np.array([float(Fraction(row["interval"][0])) for row in rows])
        self.right = np.array([float(Fraction(row["interval"][1])) for row in rows])
        self.nodes = np.asarray(base["radial_nodes"],dtype=float)
        self.coefficients = np.asarray(base["piece_coefficients"],dtype=float)
        require(self.coefficients.shape == (4,6144,65)
                and self.offset.shape == (6144,65)
                and len(rows) == 7721 and len(self.nodes) == 6145,
                "whole original centre and all forty-part rows")
        theta = 2*np.pi*np.arange(FLOAT_GRID)/FLOAT_GRID
        j = np.arange(1,HEAD+1)
        sin = np.sin(theta[:,None]*j[None,:])
        cos = np.cos(theta[:,None]*j[None,:])
        self.sin,self.cos,self.frequency = sin,cos,4*j
        root2 = np.sqrt(2.)
        self.ba = np.zeros((FLOAT_GRID,DIMENSION))
        self.bb = np.zeros((FLOAT_GRID,DIMENSION))
        self.ba[:,:HEAD] = root2*sin
        self.bb[:,HEAD] = 1.
        self.bb[:,HEAD+1:] = root2*cos
        self.bap = np.zeros_like(self.ba)
        self.bbp = np.zeros_like(self.bb)
        self.bap[:,:HEAD] = root2*cos*self.frequency[None,:]
        self.bbp[:,HEAD+1:] = -root2*sin*self.frequency[None,:]
        self.bmean = np.zeros((1,DIMENSION))
        self.bmean[0,HEAD] = 1.
        self.ifactor = np.zeros(FLOAT_GRID//2+1,dtype=complex)
        self.ifactor[1:] = -1j/(4*np.arange(1,FLOAT_GRID//2+1))
        self._last_row = None
        self._scalar_points = None

    def _locate(self,r):
        np = self.np
        index = min(len(self.rows)-1,max(0,int(np.searchsorted(self.left,r,side="right")-1)))
        # Endpoint calls may choose either adjacent polynomial reference.
        require(self.left[index]-1e-14 <= r <= self.right[index]+1e-14,
                "floating proposal remains within the complete old radial cover")
        piece = min(6143,max(0,int(np.searchsorted(self.nodes,r,side="right")-1)))
        return index,piece

    def scalar_polynomials(self,index):
        if self._last_row != index:
            row = self.rows[index]
            mid,whole = row["intrinsic_midpoint_jets"],row["intrinsic_whole_third_jets"]
            values = {}
            for name in ("beta","K","gamma","s"):
                values[name] = [
                    float(self.read_ball((mid if k < 3 else whole)[name+str(k) if k else name]).mid())/factorial(k)
                    for k in range(4)]
            self._scalar_points = values
            self._last_row = index
        return self._scalar_points

    def jets(self,r,order):
        np = self.np
        require(order in (0,1,2),"the proposal only needs ordinary matrix jets through two")
        index,piece = self._locate(r)
        centre = (self.left[index]+self.right[index])/2
        x = r-centre
        scalar = {}
        for name,coefficients in self.scalar_polynomials(index).items():
            scalar[name] = [sum(comb(k,d)*coefficients[k]*x**(k-d)
                               for k in range(d,4)) for d in range(order+1)]
        y = r-self.nodes[piece]
        raw = self.coefficients[:,piece,:][::-1]
        state = []
        for d in range(order+1):
            v = self.alpha*sum((comb(k,d)*raw[k]*y**(k-d)
                               for k in range(d,4)),np.zeros(65))
            if d == 0:
                v = v+self.offset[piece]
            v[32] += scalar["s"][d]
            state.append(v)
        return scalar,state

    def _primitive(self,value):
        np = self.np
        f = np.fft.rfft(value,axis=0)
        return np.fft.irfft(f*self.ifactor[:,None],n=FLOAT_GRID,axis=0)

    def matrix_jets(self,r,order=0):
        np = self.np
        scalar,state = self.jets(r,order)
        count = order+1
        def add(*polys):
            return [sum((p[k] for p in polys),0.) for k in range(count)]
        def scale(p,s):
            return [s*x for x in p]
        def mul(a,b):
            return [sum((a[j]*b[k-j] for j in range(k+1)),0.) for k in range(count)]
        def constant(value):
            return [value]+[np.zeros_like(value) for _ in range(order)]
        beta,K,gamma = ([np.full((1,1),x) for x in scalar[name]]
                        for name in ("beta","K","gamma"))
        u,v,up,vp,mean = [],[],[],[],[]
        for data in state:
            u.append((self.sin[:,:32]@data[:32])[:,None])
            v.append((self.cos[:,:32]@data[33:]+data[32])[:,None])
            up.append((self.cos[:,:32]@(self.frequency[:32]*data[:32]))[:,None])
            vp.append((-self.sin[:,:32]@(self.frequency[:32]*data[33:]))[:,None])
            mean.append(np.full((1,1),data[32]))
        one = constant(np.ones((1,1)))
        u2,v2,uv = mul(u,u),mul(v,v),mul(u,v)
        S = add(u2,mul(K,v2))
        drift = scale(mul(beta,[self._primitive(x) for x in S]),-1.)
        speed = mul(gamma,mean)
        l11 = scale(mul(beta,add(one,scale(u2,3.),mul(K,v2))),-1.)
        l12 = scale(mul(mul(beta,K),uv),-2.)
        l21 = scale(mul(beta,uv),-2.)
        l22 = mul(beta,add(one,scale(u2,-1.),scale(mul(K,v2),-3.)))
        inner = add([x*self.ba for x in u],[x*self.bb for x in mul(K,v)])
        inside = [self._primitive(x) for x in inner]
        n1,n2 = scale(mul(beta,up),-2.),scale(mul(beta,vp),-2.)
        rank1,rank2 = mul(mul(gamma,K),vp),scale(mul(gamma,up),-1.)
        speed12 = mul(speed,K)
        f1 = add([x*self.bap for x in drift],
                 [x*self.bbp for x in speed12],
                 [x*self.ba for x in l11],[x*self.bb for x in l12],
                 mul(n1,inside),[x*self.bmean for x in rank1])
        f2 = add([x*self.bbp for x in drift],
                 [-x*self.bap for x in speed],
                 [x*self.ba for x in l21],[x*self.bb for x in l22],
                 mul(n2,inside),[x*self.bmean for x in rank2])
        out = []
        for a,b in zip(f1,f2):
            fa,fb = np.fft.rfft(a,axis=0)/FLOAT_GRID,np.fft.rfft(b,axis=0)/FLOAT_GRID
            matrix = np.concatenate((-np.sqrt(2.)*fa[1:HEAD+1].imag,
                                     fb[0:1].real,
                                     np.sqrt(2.)*fb[1:HEAD+1].real),axis=0)
            require(matrix.shape == (DIMENSION,DIMENSION)
                    and np.all(np.isfinite(matrix)),"finite whole floating193 matrix")
            out.append(matrix)
        return out


def exponential_action(np,matrix,value):
    """Only a fixed deterministic floating proposal, never a Taylor certificate."""
    span = float(np.max(np.sum(abs(matrix),axis=1)))
    require(np.isfinite(span),"finite proposal generator")
    steps = max(1,int(ceil(span/MAX_EXPONENTIAL_SPAN)))
    require(steps <= MAX_EXPONENTIAL_SUBSTEPS,"bounded finite proposal exponential work")
    generator = matrix/steps
    out = value.copy()
    for _ in range(steps):
        term = out.copy()
        total = out.copy()
        for k in range(1,EXPONENTIAL_DEGREE+1):
            term = (generator@term)/k
            total = total+term
        out = total
    require(np.all(np.isfinite(out)),"finite complete proposal exponential result")
    return out


def cf4_step(np,reference,r,h,value):
    """Two-exponential fourth-order CF Magnus step; no error claim is made."""
    root3 = np.sqrt(3.)
    c1,c2 = .5-root3/6,.5+root3/6
    a,b = (3-2*root3)/12,(3+2*root3)/12
    A1,A2 = reference.matrix_jets(r+c1*h)[0],reference.matrix_jets(r+c2*h)[0]
    early,late = h*(b*A1+a*A2),h*(a*A1+b*A2)
    return exponential_action(np,late,exponential_action(np,early,value))


def signed_qr(np,value):
    Q,R = np.linalg.qr(value,mode="reduced")
    require(Q.shape == (DIMENSION,HEAD) and R.shape == (HEAD,HEAD)
            and np.all(np.isfinite(Q)) and np.all(np.isfinite(R)),
            "complete finite proposal QR")
    signs = np.where(np.diag(R) < 0.,-1.,1.)
    return Q*signs[None,:],signs[:,None]*R


def choose_all_columns(np,reference,nodes,root_index,allocate,release,progress=None):
    """Fill exact-dyadic physical endpoint values and derivative arrays.

    allocate(name,shape) returns private writable float64 storage.  release
    discards only temporary Q/R storage after its whole values are consumed.
    The owner hashes, saves and rereads the final four arrays before proof.
    """
    nodes = np.asarray(nodes,dtype=float)
    n = len(nodes)-1
    require(n >= 2 and 0 < root_index < n and nodes[0] == 0.
            and nodes[-1] == 25/8 and np.all(np.diff(nodes) > 0),
            "complete declared proposal grid with one internal root node")
    count = n-root_index
    Q = allocate("temporary_right_Q",(count+1,DIMENSION,HEAD))
    R = allocate("temporary_right_R",(count,HEAD,HEAD))
    terminal = np.zeros((DIMENSION,HEAD))
    terminal[:HEAD,:] = -float(RIGHT_ROBIN_SLOPE)*np.eye(HEAD)
    terminal[HEAD+1:,:] = np.eye(HEAD)
    Q[count],unused = signed_qr(np,terminal)
    for i in range(n-1,root_index-1,-1):
        k = i-root_index
        propagated = cf4_step(np,reference,nodes[i+1],nodes[i]-nodes[i+1],Q[k+1])
        Q[k],R[k] = signed_qr(np,propagated)
        if progress is not None and (k % 32 == 0 or k == 0):
            progress("positive_QR_nodes",{"completed":n-i,"total":count})
    value = allocate("trial_value",(n+1,DIMENSION,HEAD))
    C = np.linalg.solve(Q[0,HEAD+1:,:],np.eye(HEAD))
    require(np.all(np.isfinite(C)),"finite complete even96 proposal root solve")
    value[root_index] = Q[0]@C
    # This assignment is the EXACT mathematical root boundary definition.
    value[root_index,HEAD+1:,:] = np.eye(HEAD)
    for k in range(count):
        C = np.linalg.solve(R[k],C)
        value[root_index+k+1] = Q[k+1]@C
    release("temporary_right_Q")
    release("temporary_right_R")
    del Q,R
    for i in range(root_index-1,-1,-1):
        value[i] = cf4_step(np,reference,nodes[i+1],nodes[i]-nodes[i+1],value[i+1])
        if progress is not None and (i % 32 == 0 or i == 0):
            progress("negative_Cauchy_nodes",{"completed":root_index-i,"total":root_index})
    derivatives = [allocate("trial_derivative_"+str(k),(n+1,DIMENSION,HEAD))
                   for k in (1,2,3)]
    for i,r in enumerate(nodes):
        A0,A1,A2 = reference.matrix_jets(float(r),2)
        d1 = A0@value[i]
        d2 = A1@value[i]+A0@d1
        d3 = 2*A2@value[i]+2*A1@d1+A0@d2
        for destination,source in zip(derivatives,(d1,d2,d3)):
            require(np.all(np.isfinite(source)),"complete finite radial derivative proposal")
            destination[i] = source
        if progress is not None and (i % 32 == 0 or i == n):
            progress("physical_derivative_nodes",{"completed":i+1,"total":n+1})
    require(np.array_equal(value[root_index,HEAD+1:,:],np.eye(HEAD)),
            "all true-root prescribed even96 values exactly identity")
    return [value]+derivatives
