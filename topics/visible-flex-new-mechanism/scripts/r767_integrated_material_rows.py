"""Independent quadrature of H_r=mu' D on the fixed positive R764 material.

The caller's PaidBook stores each completed rule or radial column by its full identity.
Only Public Actions may evaluate a rule. None of the arrays is an interval enclosure.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
from numpy.polynomial import chebyshev as cheb
from r726_closed_spinor_fourier import public
from r738_negative_tail_and_macro_source import RATIO, stepp
from r764_positive_slope_material import A0, B0, LOWER, UPPER, PEAK, material as actual_material

MODEL='R767-integrated-D-v1'
CENTERS=(LOWER,UPPER)
R764_BASE_SHA='bf12e73ac01668167581f3a4037d115a226984555ca1c80dc146ee7239f14b73'
CUT=.00785


def digest(a):
    a=np.ascontiguousarray(a,dtype='<f8')
    return hashlib.sha256(a.tobytes()).hexdigest()


def smooth(x):
    return stepp(x)[:2]


def gate(x,a,b,c,d):
    y,yp=smooth((x-a)/(b-a));z,zp=smooth((d-x)/(d-c))
    return y*z,yp*z/(b-a)-y*zp/(d-c)


def material_values(mat):
    w=np.asarray(mat['w']);wp=np.asarray(mat['wp']);m=np.sqrt(np.asarray(mat['E']))
    return w*w/(m*(m+1)),w*wp/m**3


class MaterialTable:
    """Exact float64 physical coordinates. External tables must be verified on archive ingestion."""
    def __init__(self,idmat):
        self.identity=idmat; self.by_radius={}

    def insert(self,r,mu,mp):
        r,mu,mp=map(np.asarray,(r,mu,mp))
        if r.ndim!=1 or not r.shape==mu.shape==mp.shape or not (
                np.isfinite(r).all() and np.isfinite(mu).all() and np.isfinite(mp).all()):
            raise ValueError('Invalid R764 material-node receipt.')
        for a,b,c in zip(r,mu,mp):
            v=(float(b),float(c));old=self.by_radius.setdefault(float(a),v)
            if old!=v:raise ValueError('Two authenticated R764 values disagree at one identical material radius.')

    def mass(self,r):
        r=np.asarray(r)
        if not r.size:return np.zeros_like(r),np.zeros_like(r)
        out=np.asarray([self.by_radius[float(x)] for x in r.ravel()]).reshape(r.shape+(2,))
        return out[...,0],out[...,1]

    def fetch(self,points,book,base):
        rr=np.unique(np.concatenate([np.ravel(x) for x in points]))
        rr=np.asarray([v for v in rr if v not in self.by_radius])
        if not rr.size:return None
        key='r764_mu_mp_'+self.identity+'_'+digest(rr)
        def calculate():
            mat=actual_material(base,rr)
            mu,mp=material_values(mat)
            return dict(r=rr,mu=mu,mu_prime=mp,material_identity=self.identity,
                        radial_sha256=digest(rr),actual_new_physical_radii=len(rr))
        result=book.once(key,'read',calculate)
        if (result['material_identity']!=self.identity or result['radial_sha256']!=digest(rr)
            or not np.array_equal(rr,result['r'])):raise ValueError('Wrong recovered source-node table.')
        self.insert(rr,result['mu'],result['mu_prime'])
        return key


def material_mu_rr(r,mat,M):
    """New mu'' on the true R764 material. W,W' and E themselves come from existing rows."""
    from r738_negative_tail_and_macro_source import HALFWIDTH,FIRST
    r=np.asarray(r);W=-np.asarray(mat['w']);Wp=-np.asarray(mat['wp']);m=np.sqrt(mat['E'])
    Wpp=np.zeros_like(r)
    for c,weight in ((.0875,1.),(.1475,-2.),(.2075,1.)):
        d=(r-c)/HALFWIDTH
        # Positive inside its true mollifier support and zero outside.
        Wpp+=2.01*M*weight*(35/(32*HALFWIDTH))*np.maximum(0.,1-d*d)**3
    Wpp[(r<=LOWER)|(r>=UPPER)]=0.
    for side,rim,edge in ((-1,A0,LOWER),(1,B0,UPPER)):
        use=(r>rim)&(r<edge) if side==-1 else (r>edge)&(r<rim)
        if not np.any(use):continue
        rho=RATIO[side];u=-side*(r[use]-rim);x=u/rho
        slope=.5*x**4;sx=2*x**3;sxx=6*x*x
        inner=x<np.ldexp(1/512.,-FIRST[side])
        if np.any(inner):
            xx=x[inner];L=np.exp2(np.ceil(np.log2(xx*512)))/512
            t=xx/L;d=L/B0
            def jet(a,b):
                f,fp,fpp=stepp((t-a)/b)
                return np.stack((f,fp/b,fpp/b**2))
            H,Ht,Htt=np.array([[.5],[0.],[0.]])-jet(.5+d/2,d/2)/2+jet(.75-d,2*d)-jet(1-d,d/2)/2
            log=np.log(256/xx**2)
            # All these true dyadic cells are below the cutoff. Read the already paid
            # slope and its first derivative and differentiate log W once more.
            w=W[use][inner];dr=-side*rho*Wp[use][inner]/w
            drr=-(5-2*H)/xx**2-4*Ht/(xx*L)+Htt*log/L**2
            slope[inner]=w;sx[inner]=w*dr;sxx[inner]=w*(dr**2+drr)
        c,cp,cpp=stepp((.01-u)/.002)
        Wpp[use]=c*sxx/rho**2-2*cp*sx/(.002*rho)+cpp*slope/.002**2
    return (Wp*Wp+W*Wpp)/m**3-3*(W*Wp)**2/m**5


def layout(degree,h):
    """The label families stay nested. The last family admits arbitrary true dyadic depth."""
    if degree>=1_000_000:
        p,family=divmod(degree-1_000_000,7)
        template=(100,200,400,500,600,700,300)[family]
        row=layout(template,h);row['p']=p+(2 if family in (2,3,4,5) else 0)
        return row
    if 100<=degree<300 or 400<=degree<800:
        if degree<300:
            i,p=divmod(degree-100,100);side=0
        else:
            branch,p=divmod(degree-400,100);i,k=divmod(branch,2)
            side=(-1,1)[k];p+=2
        c=CENTERS[i]
        return dict(kind='high',i=i,p=p,side=side,center=c,span=h,
            cuts=[c+h*z for z in (-1,-.9,-.7,-.6,-.5,-.375,0,.375,.5,.6,.7,.9,1)])
    if 300<=degree<400:
        return dict(kind='broad',p=degree-300,cuts=sorted(set([
            A0+CUT,A0+.00795,A0+.008,LOWER,.09,.095,.105,.132,.14,.145,PEAK,.15,.205,UPPER,
            B0-.008,B0-.00795,B0-CUT]+[rim-side*v for side,rim in ((-1,A0),(1,B0))
                     for v in (.0086,.00885,.00935,.0096)])))
    if degree>=1000:
        # 1000+200*n+100*i+p. Enrich either real cap cell n=0,1,... with p=0,...,99.
        cell,u=divmod(degree-1000,200);i,p=divmod(u,100);side=(-1,1)[i]
        L=np.ldexp(1/512.,-cell);width=RATIO[side]*L;rim=(A0,B0)[i]
        if width<100*np.finfo(float).eps*B0:
            raise ValueError('This true cell requires a higher precision radius representation.')
        nodes=(.78,.795,.81,.85,.865,.875,.895,.905,.92,.94)
        cuts=sorted(rim-side*width*np.array(nodes))
        return dict(kind='cell',i=i,p=p,rim=rim,side=side,width=width,cuts=cuts)
    raise ValueError(f'Unknown direct material degree {degree}.')


def profile(row,r,k):
    kind=row['kind'];p=row['p']
    if kind=='high':
        c=row['center'];h=row['span'];x=(r-c)/h;v=np.abs(x)
        if k==0:
            chi,d=smooth((.5-v)/.125);z=np.clip(x,-1,1)
            on=np.ones_like(x,dtype=bool) if not row['side'] else row['side']*x>0
            return np.where(on,chi*z**p,0.),np.where(on,(-d*np.sign(x)*z**p/.125+
                            (p*chi*z**(p-1) if p else 0.))/h,0.)
        chi,d=gate(v,.6,.7,.9,1.)
        return chi,d*np.sign(x)/h
    if kind=='cell':
        dt=-row['side']/row['width'];t=(r-row['rim'])*dt
        if k:
            v,d=gate(t,.865,.875,.895,.905);return v,d*dt
        v,d=gate(t,.78,.795,.92,.94)
        z=np.clip((t-.86)/.08,-1,1);dz=dt/.08
    else:
        if k:
            if k==2:return gate(r,.095,.105,.132,.14)
            side,rim=((-1,A0) if k==1 else (1,B0))
            v,d=gate(-side*(r-rim),.0086,.00885,.00935,.0096);return v,-side*d
        v,d=gate(r,A0+CUT,A0+.00795,B0-.00795,B0-CUT)
        z=np.clip(2*(r-A0)/(B0-A0)-1,-1,1);dz=2/(B0-A0)
        dt=1.
    co=np.zeros(p+1);co[-1]=1.
    y=cheb.chebval(z,co)
    yp=cheb.chebval(z,cheb.chebder(co)) if p else 0.
    return v*y,d*dt*y+v*yp*dz


class Integrator:
    def __init__(self,mass,order):
        self.mass=mass;self.nodes,self.weights=np.polynomial.legendre.leggauss(order);self.count=0

    def bare(self,start,end,breaks):
        """Yield each ordered physical sub-rule with its signed mu' weights and actual row indices."""
        start,end=np.broadcast_arrays(np.atleast_1d(start),np.atleast_1d(end))
        sign=np.sign(end-start)
        lo=np.minimum(start,end);hi=np.maximum(start,end)
        for a,b in zip(breaks[:-1],breaks[1:]):
            u=np.maximum(lo,a);v=np.minimum(hi,b);ii=np.flatnonzero(v>u)
            if not len(ii):continue
            half=(v[ii]-u[ii])/2
            points=u[ii,None]+half[:,None]*(1+self.nodes)
            yield ii,points,sign[ii,None]*half[:,None]*self.weights

    def pieces(self,start,end,breaks):
        for ii,points,w in self.bare(start,end,breaks):
            self.count+=points.size
            yield ii,points,w*self.mass(points)[1]

    def primitive(self,start,end,row,k):
        ans=np.zeros(np.broadcast(np.atleast_1d(start),np.atleast_1d(end)).shape)
        for ii,z,w in self.pieces(start,end,row['cuts']):
            ans[ii]+=np.sum(w*profile(row,z,k)[0],axis=1)
        return ans


def regions(row):
    cuts=row['cuts']
    if row['kind']=='high':return [(cuts[0],row['center'],1),(row['center'],cuts[-1],1)]
    if row['kind']=='cell':return [(cuts[0],cuts[-1],1)]
    return [(cuts[0],LOWER,1),(LOWER,UPPER,2),(UPPER,cuts[-1],3)]


def source_degree(r,degree,table,h,order):
    q=Integrator(table.mass,order);row=layout(degree,h)
    H=np.zeros_like(r);D=H.copy();Dr=H.copy();Hr=H.copy();B=H.copy();Br=H.copy()
    receipts=[];bd=0.
    for a,b,k in regions(row):
        ix=np.flatnonzero((r>=a)&(r<=b));v=r[ix]
        primary=q.primitive(a,b,row,0)[0];cp=q.primitive(a,b,row,k)[0]
        if not np.isfinite(cp) or cp==0:raise FloatingPointError('Unseparated compensating material moment.')
        gain=primary/cp
        if abs(gain)>64.:raise FloatingPointError('Actual compensating moment exceeded the uniform bound.')
        bd=max(bd,1.+abs(gain))
        anchor=np.where(v-a<b-v,a,b)
        v0,d0=profile(row,v,0);v1,d1=profile(row,v,k)
        H[ix]=q.primitive(anchor,v,row,0)-gain*q.primitive(anchor,v,row,k)
        D[ix]=v0-gain*v1;Dr[ix]=d0-gain*d1
        mu,mp=table.mass(v);Hr[ix]=mp*D[ix]
        live=mu>0;B[ix]=np.divide(H[ix],mu,out=D[ix].copy(),where=live)
        # B_r has two one-sided limits at the high zero. H and the frame agree there.
        Br[ix]=np.divide(mp*(D[ix]-B[ix]),mu,out=(10/11)*Dr[ix],where=live)
        mid=(a+b)/2
        l=q.primitive(a,mid,row,0)[0]-gain*q.primitive(a,mid,row,k)[0]
        rr=q.primitive(b,mid,row,0)[0]-gain*q.primitive(b,mid,row,k)[0]
        receipts.append(dict(lo=a,hi=b,weighted_primary=primary,weighted_compensator=cp,coefficient=gain,
                             dual_at_midpoint_absolute=abs(l-rr),
                             dual_at_midpoint_over_mu=abs(l-rr)/float(table.mass(np.array([mid]))[0][0])))
    # Uniform true integral bounds (R767 section 4). The quadrature ratio remains
    # independently visible and may not exceed the conservative continuum bound.
    uniform=1.08 if row['kind']=='high' else 21.
    if bd>uniform:raise FloatingPointError('Finite moment ratio left the analytic material bound.')
    return dict(H=H,Hr=Hr,D=D,Dr=Dr,B=B,Br=Br,absolute_B_and_D=uniform,finite_B_and_D_bound=bd,
                moment_receipts=receipts,new_material_quadrature_nodes=q.count)


def landmarks(labels,h0,theta):
    phase=theta/np.arcsin(.27);h=h0*(phase**2 if phase else 1.)
    degrees=sorted({100,200}|{d for d,j,trig in labels if d>=100})
    return np.unique(np.concatenate([layout(d,h)['cuts'] for d in degrees]))


def nested_labels(max_frequency,radial):
    if max_frequency<1 or len(set(radial))!=len(radial):raise ValueError('Invalid nested physical basis.')
    zero=sorted(set((0,3,6,9))|set(radial))
    return [(d,0,'cos') for d in zero]+[(d,j,p) for j in range(1,max_frequency+1)
                                       for d in radial for p in ('cos','sin')]


def physical_key(grid,mat,cal,order,phase,h0,source_sha):
    if not 4<=order<=64 or type(order) is not int:raise ValueError('Expected a physical quadrature order in 4..64.')
    r=np.asarray(grid.r);w,wp,E,Ep=(np.asarray(mat[key]) for key in ('w','wp','E','Ep'))
    if any(a.shape!=r.shape for a in (w,wp,E,Ep)) or np.any(np.diff(r)<=0) or r[0]!=A0 or r[-1]!=B0:
        raise ValueError('Wrong physical material grid.')
    if cal['material_definition']!='R764-positive-cutoff' or not 10.87<cal['M']<10.89:
        raise ValueError('Wrong fixed material identity.')
    hashes={name:digest(a) for name,a in zip(('r','w','wp','E','Ep','I'),(r,w,wp,E,Ep,cal['material_I']))}
    if not source_sha or any(len(v)!=64 for v in source_sha.values()):raise ValueError('Request must bind true source bytes.')
    for name in ('r764_positive_slope_material.py','r764_positive_slope_lambert.py',
                 'r767_full_radial_lambert.py','r767_integrated_material_rows.py'):
        file=Path(__file__).resolve().with_name(name)
        if source_sha.get(name)!=hashlib.sha256(file.read_bytes()).hexdigest():
            raise ValueError(f'Unbound R767 dependency {name}.')
    identity=dict(model=MODEL,actual_material='R764-positive-cutoff',base64_sha256=R764_BASE_SHA,
                  M=float(cal['M']).hex(),theta_fraction=float(phase).hex(),window=float(h0).hex(),
                  order=order,sources=source_sha,grid_and_material=hashes,numpy=np.__version__)
    text=json.dumps(identity,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(text).hexdigest(),identity


def seed_rule(r,table,h,order):
    """Quadrature kernel for the FULL flat characteristic slope, independent of its angular data."""
    q=Integrator(table.mass,order);blocks=[]
    for center in CENTERS:
        for sign in (-1,1):
            offset=sign*(r-center)
            idx=np.flatnonzero((offset>=0 if sign==1 else offset>0)&(offset<h))
            v=r[idx];row=layout(100 if center==LOWER else 200,h);end=center+sign*h
            cuts=row['cuts'];mu,mp=table.mass(v)
            cm=q.primitive(center,end,row,1)[0]
            if cm==0:raise ArithmeticError('Singular high-circle moment.')
            total=[];partial=[]
            for ii,z,w in q.pieces(center,end,cuts):
                chi,_=profile(row,z,0)
                if np.any(chi):total.append(dict(z=z[0]-center,w=w[0]*chi[0]/cm))
            gain_l1=sum(float(np.sum(abs(z['w']))) for z in total)
            if not np.isfinite(gain_l1) or gain_l1>.08:
                raise FloatingPointError('Finite characteristic moment left the true high-circle ratio bound.')
            use=np.flatnonzero(mu>0)
            # The primitive can terminate inside either half of the support.
            for ii,z,w in q.pieces(center,v[use],cuts):
                chi,_=profile(row,z,0)
                if np.any(chi):partial.append(dict(i=use[ii],z=z-center,w=w*chi/mu[use[ii],None]))
            chi,cr=profile(row,v,0);comp,comp_r=profile(row,v,1)
            bcomp=np.divide(q.primitive(center,v,row,1),mu,out=np.zeros_like(mu),where=mu>0)
            blocks.append(dict(i=idx,center=center,sign=sign,delta=v-center,chi=chi,chi_r=cr,
                comp=comp,comp_r=comp_r,bcomp=bcomp,total=total,partial=partial,finite_abs_compensator_weights=gain_l1,
                rate=np.divide(mp,mu,out=np.zeros_like(mu),where=mu>0)))
    return dict(blocks=blocks,new_material_quadrature_nodes=q.count)


def radius_plan(r,row,order,seed=False):
    """Coordinates only. A material source is called once per genuinely missing radius."""
    q=Integrator(None,order);points=[]
    for a,b,k in regions(row):
        v=r[(r>=a)&(r<=b)]
        pairs=[(a,b),(np.where(v-a<b-v,a,b),v),(a,(a+b)/2),(b,(a+b)/2)]
        points.extend((np.array([(a+b)/2]),v))
        if seed:
            center=row['center'];end=b if a==center else a
            pairs.extend(((center,end),(center,v)))
        for l,h in pairs:
            points.extend(n for _,n,_ in q.bare(l,h,row['cuts']))
    return points


def prepare(grid,material,calibration,labels,order,book,source_sha,theta,base,shared_tables=()):
    """book.once(key,'read',calculate) persists finished numerical units including all weights and counts."""
    public()
    phase=theta/np.arcsin(.27);h0=float(calibration.get('high_zero_window',1e-5))
    if not 0<=phase<=1 or not 0<h0<=1e-5:raise ValueError('Outside the R764 physical angle or germ.')
    folded={}
    for path,v in source_sha.items():
        if path.endswith('.py'):
            old=folded.setdefault(Path(path).name,v)
            if old!=v:raise ValueError('Ambiguous source basename in R767 request.')
    for name in ('r764_positive_slope_material.py','r738_negative_tail_and_macro_source.py','r738_real_macro_reference.py'):
        if folded.get(name)!=hashlib.sha256(Path(__file__).resolve().with_name(name).read_bytes()).hexdigest():
            raise ValueError('The R764 shared material source must use the authenticated original implementation.')
    key,identity=physical_key(grid,material,calibration,order,phase,h0,folded)
    if base.order!=64 or float(base.M).hex()!=identity['M']:raise ValueError('Incorrect R764 base object.')
    source_names=('r764_positive_slope_material.py','r738_negative_tail_and_macro_source.py','r738_real_macro_reference.py')
    source='|'.join([*(folded[n] for n in source_names),identity['M'],R764_BASE_SHA,np.__version__])
    idmat=hashlib.sha256(source.encode()).hexdigest();table=MaterialTable(idmat)
    table.insert(grid.r,*material_values(material))
    for got in shared_tables:
        if got['material_identity']!=idmat or got['radial_sha256']!=digest(got['r']):
            raise ValueError('R764 external source-table identity mismatch.')
        table.insert(got['r'],got['mu'],got['mu_prime'])
    h=h0*(phase**2 if phase else 1.);r=np.asarray(grid.r)
    if min(h/np.spacing(c) for c in CENTERS)<16:
        raise ValueError('The fixed R767 high window needs more radial precision at this angle.')
    out={};counts={};source_keys=[];plans=set()
    degrees=sorted({d for d,j,trig in labels if d>=100}|({100,200} if phase else set()))
    for d in degrees:
        row=layout(d,h)
        shape=tuple(row['cuts'])
        if shape in plans:continue
        plans.add(shape)
        receipt=table.fetch(radius_plan(r,row,order,row['kind']=='high' and bool(phase)),book,base)
        if receipt:source_keys.append(receipt)
    for deg in sorted({d for d,j,trig in labels if d>=100}):
        val=book.once(f'r767_{key}_radial_{deg}','read',lambda d=deg:source_degree(r,d,table,h,order))
        out[str(deg)]=val;counts[str(deg)]=val['new_material_quadrature_nodes']
    seed=(book.once('r767_'+key+'_characteristic_kernel','read',lambda:seed_rule(r,table,h,order)) if phase
          else dict(blocks=[],new_material_quadrature_nodes=0))
    mr=book.once('r767_'+key+'_mu_rr','read',lambda:dict(mu_rr=material_mu_rr(r,material,base.M),
                   actual_new_second_material_radii=len(r)))
    return dict(identity=identity,key=key,columns=out,seed=seed,mass_second=mr,scientific_quadrature_nodes_by_unit=counts,
                shared_R764_material_identity=idmat,shared_material_table_keys=source_keys)
