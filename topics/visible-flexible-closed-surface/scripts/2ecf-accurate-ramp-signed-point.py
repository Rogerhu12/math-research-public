#!/usr/bin/env python3
"""Compare an exact integral-normalized ramp jet with its literal G10 packet."""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

import numpy as np


def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        while block := f.read(1 << 20):
            h.update(block)
    return h.hexdigest()


def imported(p, name):
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def nc_weights(n):
    """Exact closed Newton-Cotes weights on [0,1], using the Lagrange basis."""
    result = []
    for j in range(n + 1):
        p = [Q(1)]
        for k in range(n + 1):
            if k != j:
                p = [(x - k*y)/(j-k) for x,y in zip([Q(0)] + [n*v for v in p], p + [Q(0)])]
        result.append(sum(v/(i+1) for i,v in enumerate(p)))
    assert all(sum(w*Q(j,n)**m for j,w in enumerate(result)) == Q(1,m+1)
               for m in range(n+1))
    return result


def ellipse_radius(A, B, n=72):
    c, z = (A+B)/2, (A-B)/(A+B)
    b = Q(1)
    total = Q(1)
    for i in range(1, n+1):
        b *= z*Q(2*i-3,2*i)
        total += b*b
    b *= z*Q(2*n-1,2*n+2)
    return c*total,c*(total + b*b/(1-z*z))


def append(a, b, axis):
    return I(np.concatenate([a.lo,b.lo],axis=axis),np.concatenate([a.hi,b.hi],axis=axis))


def stack(xs, axis):
    return I(np.stack([x.lo for x in xs],axis=axis),np.stack([x.hi for x in xs],axis=axis))


def pairsum(a):
    while a.shape[0] > 1:
        n = a.shape[0]//2
        b = a[:2*n:2]+a[1:2*n:2]
        a = append(b,a[-1:],0) if a.shape[0]%2 else b
    return a[0]


def polynomial_coefficients(model, s):
    x = s-model.c
    idx = next(i for i in range(15) if Q(float(model.sx[i])) <= x < Q(float(model.sx[i+1])))
    C, bits, L, left = model.cell(idx)
    t = (x-left)/L
    # real/imag split of true paired Laurent coefficients, including +/-384.
    derivatives = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(2,1)]
    multipliers = {}
    for j in range(3):
        multipliers[j] = [Q(factorial(d), factorial(d-j))*t**(d-j)/(L**j*(1 << bits))
                          for d in range(j,6)]
    rows = []
    for j in range(3):
        co = [[(sum(m*C[p][d][0][k] for p,m in enumerate(multipliers[j],j)),
                sum(m*C[p][d][1][k] for p,m in enumerate(multipliers[j],j)))
               for d in range(3)] for k in range(2*model.degree+1)]
        rows.append(co)
    result = []
    for radial, angular in derivatives:
        field = []
        for k,col in enumerate(rows[radial],-model.degree):
            pairs = []
            for re,im in col:
                for unused in range(angular):
                    re,im = -k*im,k*re
                pairs.append((re,im))
            field.append(pairs)
        result.append(field)
    return idx, result


def grid_transform(coefficients, n):
    """Positive-sign, unscaled DFT of signed-frequency coefficients."""
    count = 3*len(coefficients)
    ar = np.zeros((n,count),dtype=K.LD)
    br = ar.copy()
    ai = ar.copy()
    bi = ar.copy()
    D = (len(coefficients[0])-1)//2
    for mode in range(-D,D+1):
        for j,field in enumerate(coefficients):
            for d,(re,im) in enumerate(field[mode+D]):
                ar[mode,3*j+d],br[mode,3*j+d] = K.qinterval(re)
                ai[mode,3*j+d],bi[mode,3*j+d] = K.qinterval(im)
    rev = np.array([int(f'{j:0{n.bit_length()-1}b}'[::-1],2) for j in range(n)])
    re, im = I(ar[rev],br[rev]), I(ai[rev],bi[rev])
    width = 2
    while width <= n:
        half = width//2
        angles = K.PI*I(np.arange(half).reshape(1,half,1))*Q(2,width)
        sn, cs = K.sincos(angles)
        r, v = re.reshape(-1,width,count),im.reshape(-1,width,count)
        r0, i0 = r[:,:half],v[:,:half]
        rp, ip = r[:,half:],v[:,half:]
        a,b = rp*cs-ip*sn,rp*sn+ip*cs
        re=append(r0+a,r0-a,1).reshape(n,count)
        im=append(i0+b,i0-b,1).reshape(n,count)
        width *= 2
    assert np.all(im.lo<=0) and np.all(im.hi>=0)
    return [re[:,3*j:3*j+3] for j in range(len(coefficients))]


def norms(co, model):
    """Real-circle angular and closed-strip bounds, preserving the full spectrum."""
    deg=model.degree
    H=[Q(32,31)**abs(k) for k in range(-deg,deg+1)]
    def l1(field,weights):
        return sum(w*sum(abs(a)+abs(b) for a,b in row) for w,row in zip(weights,field))
    bounds=[l1(field,H) for field in co]
    real_derivatives=[l1(field,[abs(k) for k in range(-deg,deg+1)]) for field in co]
    # Subtract the literal ellipse tangent before bounding on the real circle.
    ref = [[list(pair) for pair in row] for row in co[2]]
    ref[deg+1][0][1] -= model.A/2
    ref[deg-1][0][1] += model.A/2
    ref[deg+1][1][0] -= model.B/2
    ref[deg-1][1][0] -= model.B/2
    beta = model.B-l1(ref,[1]*len(H))
    delta = l1(co[2],[h-1 for h in H])
    assert beta>2*delta
    # Re(sum U_d(z)^2) >= (|U(real)|-delta)^2 - delta^2.
    square_min = beta*(beta-2*delta)
    qmin = I(square_min).sqrt()
    Y,S,U,SS,SU,UU,SSU = map(I,bounds)
    qs = U*SU/qmin
    qss=(SU.square()+U*SSU+qs.square())/qmin
    integrand_bounds=[U,qs,qss]+[Y*U]*3+[S*U+Y*qs]*3+[SS*U+2*S*qs+Y*qss]*3
    return beta,delta,square_min,I(max(v.hi for v in integrand_bounds)),real_derivatives


def dot(a,b):
    return (a*b).sum(-1)


def expand(a):
    return a.reshape(*a.shape,1)


def density(values):
    Y,S,U,SS,SU,UU,SSU=values
    q=dot(U,U).sqrt()
    qs=dot(U,SU)/q
    qss=(dot(SU,SU)+dot(U,SSU)-qs.square())/q
    return q,qs,qss


def moment_table(values):
    Y,S,U,SS,SU,UU,SSU=values
    q,qs,qss=density(values)
    y=Y*expand(q)
    ys=S*expand(q)+Y*expand(qs)
    yss=SS*expand(q)+2*S*expand(qs)+Y*expand(qss)
    return stack([q,qs,qss]+[arr[:,j] for arr in (y,ys,yss) for j in range(3)],1)


def panel_means(table, count, n, weights, bound):
    m=len(weights)-1
    assert n%m==0 and 0<count<=n//m
    left=m*np.arange(count)
    blocks=sum((table[(left+j)%n]*w for j,w in enumerate(weights)),I(0))
    value=pairsum(blocks)/count
    # Taylor on a radius 1/32 complex disk about each panel midpoint.
    ratio=K.PI*Q(32*m,n)
    assert ratio.hi<1
    err=bound*(1+sum(map(abs,weights)))*ratio**(m+1)/(1-ratio)
    return value.widen(err),err


def display(v):
    return dict(lo=str(K.exact(v.lo)),hi=str(K.exact(v.hi)),
                display=[float(v.lo),float(v.hi)])


def point_jets(local, means, integrals, model, s, u):
    Y,S,U,SS,SU,UU,SSU=local
    a,as_,ass=means[:3]
    C=means[3:6]/a
    Cs=(means[6:9]-C*as_)/a
    Css=(means[9:12]-2*Cs*as_-C*ass)/a
    x=(s-model.c)/model.ramp
    v=model.v
    f=I.bounds(*ellipse_radius(model.A,model.B))+v*model.ramp*(21*x**6-60*x**7+Q(135,2)*x**8-35*x**9+7*x**10)
    fs=v*(126*x**5-420*x**6+540*x**7-315*x**8+70*x**9)
    fss=v/model.ramp*630*x**4*(1-x)**4
    lam=f/a
    ls=(fs-lam*as_)/a
    lss=(fss-2*ls*as_-lam*ass)/a
    q,qs,qss=density(local)
    qt=dot(U,UU)/q
    ts=(u*as_-integrals[1])/q
    tss=(u*ass-integrals[2]-2*qs*ts-qt*ts.square())/q
    tu=a/q
    tsu=(as_-(qs+qt*ts)*tu)/q
    tuu=-a*a*qt/q**3
    V=Y-C
    Vs=S+U*ts-Cs
    return [C+lam*V,Cs+ls*V+lam*Vs,lam*U*tu,
            Css+lss*V+2*ls*Vs+lam*(SS+2*SU*ts+UU*ts.square()+U*tss-Css),
            ls*U*tu+lam*((SU+UU*ts)*tu+U*tsu),lam*(UU*tu.square()+U*tuu)],f


def metric(jets, f):
    Y,S,U,SS,SU,UU=jets
    E,F,G=dot(S,S),dot(S,U),dot(U,U)
    e,b,g=E-1,F/f,G/f.square()-1
    # Both principal curvatures, sorted by value, measured using their own first forms.
    cross=stack([S[(j+1)%3]*U[(j+2)%3]-S[(j+2)%3]*U[(j+1)%3] for j in range(3)],0)
    normal=cross/dot(cross,cross).sqrt()
    p,h,r=dot(SS,normal),dot(SU,normal),dot(UU,normal)
    det=E*G-F.square()
    tr=(G*p-2*F*h+E*r)/det
    gauss=(p*r-h.square())/det
    delta=(tr.square()/4-gauss).sqrt()
    return [e,b,g,tr/2-delta,tr/2+delta]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','ramp','prepared','g11','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args()
    global K,I
    kernel=args.scripts/'prefix-hull-kernel'/'m12-correlated-gram-interval-kernel.py'
    gram=args.scripts/'6a65-geometry-ramp-native-gram-certificate.py'
    inputs={k:sha(p) for k,p in dict(ramp=args.ramp,prepared=args.prepared,g11=args.g11,
                interval=kernel,gram=gram).items()}
    assert inputs['ramp']=='0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7'
    assert inputs['prepared']=='de75e9632855bc3547e174d7e1bfcefaa295d01dbe151d1c087ff0d83682df80'
    assert inputs['g11']=='9681d300b461ca13cd0f357a568d487c98ef3d15fbd45917221dd861ed254ed6'
    assert inputs['interval']=='c62057bc164af305aac63ea20d84570a34c72716bea3ae5788a4344b2c5b6ddf'
    K=imported(kernel,'signed_point_kernel')
    I=K.I
    G=imported(gram,'signed_point_ramp')
    prepared=json.loads(args.prepared.read_text())
    g11=json.loads(args.g11.read_text())
    rows=[]
    literal=None
    for name,rec,i,j in [('G10training',prepared['caches']['training'],154,96),
                          ('G10observer',prepared['caches']['observer'],154,144),
                          ('G11',g11,114,191)]:
        assert rec['sourceDefinitionSHA256']=='90488346b7de882e952b174244f747a85fc6e4d4babb00e8aac8aafcbad35073'
        files={k:args.prepared.parent/Path(rec['files'][k]).name for k in ('jets','radius')}
        for k,p in files.items():
            assert sha(p)==rec['SHA256'][k]
        row=np.load(files['jets'],mmap_mode='r',allow_pickle=False)[i,:,j,:]
        frow=float(np.load(files['radius'],mmap_mode='r',allow_pickle=False)[i,0])
        xi=Q(float(rec.get('physicalNodes',rec.get('nodes'))[i]))
        ui=Q(float(rec['angles'][j]))
        eq=sum(Q(float(z))**2 for z in row[1])-1
        rows.append(dict(group=name,index=[i,j],s=str(xi),u=str(ui),radialGramDefectExact=str(eq),
                         arrayHashes={k:rec['SHA256'][k] for k in files}))
        if name=='G10training':
            s,u,literal,literal_f=xi,ui,I(row),I(frow)
        elif name=='G10observer':
            assert xi==s and ui==u and eq==Q(rows[0]['radialGramDefectExact'])
    model=G.ActualRamp(args.ramp)
    index,coefficients=polynomial_coefficients(model,s)
    beta,strip_delta,strip_lower,bound,dnorms=norms(coefficients,model)
    n=16384
    grids=grid_transform(coefficients,n)
    table=moment_table(grids)
    weights=nc_weights(16)
    means,error=panel_means(table,n//16,n,weights,bound)
    pieces,unused=panel_means(table,3*n//64,n,weights,bound)
    theta=3*K.PI/2
    primitives=theta*pieces[:3]
    root_shift=I((primitives[0]-I(u)*means[0]).abs_upper())/beta
    local=[grid[3*n//4].widen(root_shift*nrm) for grid,nrm in zip(grids,dnorms)]
    primitives=primitives.widen(root_shift*bound)
    jets,f=point_jets(local,means,primitives,model,s,I(u))
    tests=metric(jets,f)
    litmetric=metric(literal,literal_f)
    assert tests[0].hi < -I(Q('0.00000006')).hi
    fields=('X','Xs','Xu','Xss','Xsu','Xuu')
    metric_names=('Eminus1','Foverf','Goverf2minus1','lowerSignedKappa','upperSignedKappa')
    results=dict(schema='2ecf-accurate-normalized-ramp-signed-point-v1',inputSHA256=inputs,
                 entrySHA256=sha(Path(__file__)),literalPacketEvidence=rows,cell=index,
                 exactPhysicalS=str(s),exactMaterialU=str(u),subdivision=dict(grid=n,closedNewtonCotesDegree=16,
                 stripHalfWidth='1/32',minimumRealSpeedLower=display(I(beta)),complexTangentShiftUpper=display(I(strip_delta)),
                 minimumRealSquaredComplexSpeedLower=display(I(strip_lower)),allIntegrandsStripUpper=display(bound),
                 meanQuadratureErrorBound=display(error),trueInverseDistanceFromThreePiOverTwoUpper=display(root_shift)),
                 accurateRadius=display(f),literalRadiusDifference=display(literal_f-f),
                 accurateSixJets={k:[display(z[d]) for d in range(3)] for k,z in zip(fields,jets)},
                 literalMinusAccurateSixJets={k:[display(z[d]) for d in range(3)]
                    for k,z in zip(fields,[literal[i]-v for i,v in enumerate(jets)])},
                 accuratePointMetricAndCurvatures={k:display(z) for k,z in zip(metric_names,tests)},
                 literalPointMetricAndCurvatures={k:display(z) for k,z in zip(metric_names,litmetric)},
                 signedLiteralMinusAccurate={k:display(b-a) for k,a,b in zip(metric_names,tests,litmetric)},
                 entireAngularMeanAndPartialIntegralsEnclosed=True,
                 allMaterialPointsOrFullRampJetDifferenceCertified=False)
    with args.out.open('x') as fp:
        json.dump(results,fp,indent=2,allow_nan=False);fp.write('\n')
    print(json.dumps(dict(cell=index,accurateRadial=display(tests[0]),rootDistance=display(root_shift),
                          maximumSixJetDifference=[float(np.max((literal[i]-v).abs_upper())) for i,v in enumerate(jets)])))


if __name__=='__main__':
    main()
