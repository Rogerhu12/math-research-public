"""NP floating forced trial selection; every output is only an exact dyadic choice.

No IO or numerical imports.  Full directed residual certification is separate.
The original M32 centre reference provides genuine radial polynomial carriers;
the old homogeneous TC proposal/QR and the old direction solve are never run.
"""
from fractions import Fraction
from math import ceil, comb, factorial

HEAD, DIMENSION, GRID = 96,193,512
A,B = Fraction(1,20),Fraction(9,50)
MAX_RK4_STEP = Fraction(1,32768)


def require(ok,message):
    if not ok:
        raise ValueError(message)


class ForcedCentreReference:
    def __init__(self,np,original_reference,rows,read_ball):
        self.np,self.reference,self.rows,self.read_ball = np,original_reference,rows,read_ball
        self.frequency = 4*np.arange(GRID//2+1)
        self.primitive_factor = np.zeros(GRID//2+1,dtype=complex)
        self.primitive_factor[1:] = -1j/self.frequency[1:]
        self.root2 = np.sqrt(2.)
        self.calls = 0

    def waves(self,data,normalized):
        np = self.np
        modes = HEAD if normalized else 32
        require(data.shape == (2*modes+1,), "one full real reflected coefficient vector")
        z = np.zeros((GRID//2+1,2),dtype=complex)
        factor = 1/self.root2 if normalized else .5
        z[1:modes+1,0] = -1j*factor*data[:modes]
        z[0,1] = data[modes]
        z[1:modes+1,1] = factor*data[modes+1:]
        values = np.fft.irfft(z*GRID,n=GRID,axis=0)
        derivatives = np.fft.irfft(z*(1j*self.frequency[:,None])*GRID,n=GRID,axis=0)
        return values[:,0],values[:,1],derivatives[:,0],derivatives[:,1],float(data[modes])

    def primitive(self,values):
        np = self.np
        return np.fft.irfft(np.fft.rfft(values)*self.primitive_factor,n=GRID)

    def project(self,first,second):
        np = self.np
        one,two = np.fft.rfft(first)/GRID,np.fft.rfft(second)/GRID
        out = np.concatenate((-self.root2*one[1:HEAD+1].imag,
                              [float(two[0].real)],self.root2*two[1:HEAD+1].real))
        require(np.all(np.isfinite(out)), "finite complete forced proposal vector")
        return out

    def local(self,r,order):
        scalar,state = self.reference.jets(r,order)
        index,_ = self.reference._locate(r)
        row = self.rows[index]
        centre = .5*(self.reference.left[index]+self.reference.right[index])
        mid = row["intrinsic_midpoint_jets"]
        a = float(self.read_ball(mid["a"]).mid())
        beta = [float(self.read_ball(mid["beta"+str(k) if k else "beta"]).mid())
                for k in range(3)]
        polynomial = [a,beta[0]*a,(beta[1]+beta[0]**2)*a/2,
                      (beta[2]+3*beta[0]*beta[1]+beta[0]**3)*a/6]
        radius = [sum(comb(k,d)*polynomial[k]*(r-centre)**(k-d)
                      for k in range(d,4)) for d in range(order+1)]
        require(radius[0] > 0 and scalar["gamma"][0] > 0,
                "finite positive proposal metric denominators")
        return scalar,state,radius

    def bump_jets(self,r,order):
        # Endpoint jets through3 vanish exactly by the actual bump definition.
        if r <= float(A) or r >= float(B):
            return [0.]*(order+1),[0.]*(order+1)
        length = float(B-A)
        t = (r-float(A))/length
        def derivative(k):
            value = 0.
            for ell in range(k+1):
                left,right = ell,k-ell
                if left <= 6 and right <= 6:
                    value += (comb(k,left)*factorial(6)/factorial(6-left)
                              *factorial(6)/factorial(6-right)*(-1)**right
                              *t**(6-left)*(1-t)**(6-right))
            return 4096*value/length**k
        return ([derivative(k)/factorial(k) for k in range(order+1)],
                [derivative(k+1)/factorial(k) for k in range(order+1)])

    def rhs_jets(self,r,h_jets,order=0):
        require(order in (0,1,2) and len(h_jets) == order+1,
                "value and exact requested formal endpoint jet count")
        self.calls += 1
        scalar,state,radius = self.local(r,order)
        count = order+1
        def add(*terms):
            return [sum((term[k] for term in terms),0.) for k in range(count)]
        def multiply(x,y):
            return [sum((x[j]*y[k-j] for j in range(k+1)),0.) for k in range(count)]
        def scale(x,value):
            return [value*y for y in x]
        def reciprocal(x):
            out = [1/x[0]]
            for k in range(1,count):
                out.append(-sum(x[j]*out[k-j] for j in range(1,k+1))/x[0])
            return out
        def primitive(x):
            return [self.primitive(y) for y in x]
        one = [1.]+[0.]*order
        u,v,up,vp,m = map(list,zip(*(self.waves(x,False) for x in state)))
        h1,h2,h1p,h2p,hm = map(list,zip(*(self.waves(x,True) for x in h_jets)))
        beta,K,gamma = (scalar[x] for x in ("beta","K","gamma"))
        u2,v2,uv = multiply(u,u),multiply(v,v),multiply(u,v)
        d = scale(multiply(beta,primitive(add(u2,multiply(K,v2)))),-1.)
        speed = multiply(gamma,m)
        l11 = scale(multiply(beta,add(one,scale(u2,3.),multiply(K,v2))),-1.)
        l12 = scale(multiply(multiply(beta,K),uv),-2.)
        l21 = scale(multiply(beta,uv),-2.)
        l22 = multiply(beta,add(one,scale(u2,-1.),scale(multiply(K,v2),-3.)))
        inside = primitive(add(multiply(u,h1),multiply(multiply(K,v),h2)))
        x = add(multiply(d,h1p),multiply(multiply(speed,K),h2p),
                multiply(l11,h1),multiply(l12,h2),
                scale(multiply(multiply(beta,up),inside),-2.),
                multiply(multiply(multiply(gamma,K),vp),hm))
        y = add(multiply(d,h2p),scale(multiply(speed,h1p),-1.),
                multiply(l21,h1),multiply(l22,h2),
                scale(multiply(multiply(beta,vp),inside),-2.),
                scale(multiply(multiply(gamma,up),hm),-1.))
        w,wp = self.bump_jets(r,order)
        if any(w) or any(wp):
            invg,inva = reciprocal(gamma),reciprocal(radius)
            T = scale(multiply(multiply(beta,multiply(invg,invg)),multiply(inva,inva)),.5)
            P = primitive(v2)
            W1,W2 = add(multiply(P,up),multiply(v2,u)),add(multiply(P,vp),multiply(v2,v))
            a1 = add(scale(multiply(multiply(beta,T),W1),-1.),multiply(multiply(speed,T),vp))
            a2 = scale(multiply(multiply(beta,T),W2),-1.)
            b1 = add(multiply(multiply(beta,K),W1),scale(multiply(multiply(speed,K),vp),-.5))
            b2 = add(multiply(multiply(beta,K),W2),scale(multiply(speed,up),-.5))
            x = add(x,multiply(wp,a1),multiply(w,b1))
            y = add(y,multiply(wp,a2),multiply(w,b2))
        return [self.project(a,b) for a,b in zip(x,y)]

    def rhs(self,r,value):
        return self.rhs_jets(r,[value],0)[0]

    def endpoint_jets(self,r,value):
        first = self.rhs(r,value)
        second = self.rhs_jets(r,[value,first],1)[1]
        third = 2*self.rhs_jets(r,[value,first,second/2],2)[2]
        return value,first,second,third


def choose_particular(np,reference,nodes,progress=None):
    """Forced backward RK4 only chooses exact endpoint dyadics, never an error bound."""
    require(nodes[0] == 0 and nodes[-1] == B, "whole declared strict terminal problem")
    jets = [np.zeros((len(nodes),DIMENSION),dtype='<f8') for _ in range(4)]
    current = np.zeros(DIMENSION)
    substeps = 0
    for i in range(len(nodes)-2,-1,-1):
        left,right = float(nodes[i]),float(nodes[i+1])
        count = max(1,ceil(float((nodes[i+1]-nodes[i])/MAX_RK4_STEP)))
        step = (left-right)/count
        for j in range(count):
            r = right+j*step
            k1 = reference.rhs(r,current)
            k2 = reference.rhs(r+step/2,current+step*k1/2)
            k3 = reference.rhs(r+step/2,current+step*k2/2)
            k4 = reference.rhs(r+step,current+step*k3)
            current = current+(step/6)*(k1+2*k2+2*k3+k4)
            require(np.all(np.isfinite(current)), "finite whole forced trial")
        substeps += count
        for order,value in enumerate(reference.endpoint_jets(left,current)):
            jets[order][i] = value
        if progress is not None and (i%64 == 0 or i == len(nodes)-2):
            progress("new_forced_nu_trial",{"remaining_nodes":i,"nodes":len(nodes),"RK4_substeps":substeps})
    require(all(np.array_equal(x[-1],np.zeros(DIMENSION)) for x in jets),
            "exact zero terminal value and three terminal jets")
    return jets,{"new_RK4_substeps":substeps,"new_rhs_calls":reference.calls,
                 "old_QR_or_direction_solve_calls":0,
                 "floating_residual_used_as_bound":False,
                 "all_endpoint_dyadics_are_new_trial_choices":True}
