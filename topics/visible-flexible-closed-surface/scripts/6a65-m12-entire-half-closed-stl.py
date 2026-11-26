#!/usr/bin/env python3
"""Complete, temporary STL samples of one identified original-M12 field.

The sampling angle is the uniform material angle u. The saved Cartesian
field is evaluated at theta=U0^{-1}(u), before the phase action. Thus an
integer cyclic shift implements u-alpha, not a shift of the native angle.
Meshes are numerical representatives; their topology checks do not replace
the continuous map's metric, reach, or fixed-g convergence certificates.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, struct, time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

LD=np.longdouble
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def require(value,message):
    if not value: raise ValueError(message)


def faces_for(rings,N):
    faces=[(0,1+(j+1)%N,1+j) for j in range(N)]
    for ring in range(rings-1):
        a,b=1+ring*N,1+(ring+1)*N
        for j in range(N):
            k=(j+1)%N
            faces.extend(((a+j,a+k,b+j),(a+k,b+k,b+j)))
    pole,last=1+rings*N,1+(rings-1)*N
    faces.extend((last+j,last+(j+1)%N,pole) for j in range(N))
    return np.asarray(faces,dtype=np.int32)


def topology(faces,nv):
    edge=np.concatenate((faces[:,[0,1]],faces[:,[1,2]],faces[:,[2,0]]))
    orient=np.where(edge[:,0]<edge[:,1],1,-1)
    keys=np.sort(edge,axis=1).astype(np.int64)
    code=keys[:,0]*nv+keys[:,1]
    unique,indices,counts=np.unique(code,return_inverse=True,return_counts=True)
    require(np.all(counts==2),'The complete mesh has boundary or nonmanifold edges')
    require(np.all(np.bincount(indices,weights=orient)==0),'Inconsistent face orientation')
    require(nv-len(unique)+len(faces)==2,'Wrong closed spherical topology')
    # Every ring is connected to the previous one by the actual face list;
    # every vertex is used, including both pole fans.
    require(np.array_equal(np.unique(faces),np.arange(nv)),'An isolated vertex is present')
    return dict(vertices=nv,edges=len(unique),faces=len(faces),EulerCharacteristic=2,
                allEdgesHaveTwoOppositeIncidences=True,allVerticesUsed=True,
                connectedBySuccessiveRingStripsAndBothPoleFans=True)


def cap(radius,u,height,bumps):
    x,y=radius*np.cos(u),radius*np.sin(u);z=np.full(len(u),height)
    if bumps:
        a,b,h=2/25,3/100,1/2000
        for j in range(3):
            angle=2*np.pi*j/3;cx,cy=a*np.cos(angle),a*np.sin(angle)
            z+=h*np.maximum(1-((x-cx)**2+(y-cy)**2)/(b*b),0)**3
    return np.stack((x,y,z),axis=-1)


def write_stl(path,vertices,faces,label):
    # Compute normals from the actual float32 vertices written to STL.
    v=np.asarray(vertices,dtype='<f4');tri=v[faces]
    cross=np.cross(tri[:,1].astype(float)-tri[:,0],tri[:,2].astype(float)-tri[:,0])
    area=np.linalg.norm(cross,axis=1)
    require(np.all(area>0) and np.isfinite(tri).all(),'Degenerate or nonfinite serialized triangle')
    unique=np.unique(v,axis=0)
    require(len(unique)==len(v),'Float32 conversion merged distinct mesh vertices')
    volume=np.sum(np.einsum('ij,ij->i',tri[:,0].astype(float),
                            np.cross(tri[:,1].astype(float),tri[:,2].astype(float))))/6
    require(volume>0,'The complete serialized surface has reversed signed volume')
    dtype=np.dtype([('normal','<f4',(3,)),('vertices','<f4',(3,3)),('attribute','<u2')])
    record=np.zeros(len(faces),dtype=dtype);record['normal']=cross/area[:,None];record['vertices']=tri
    raw=('M12 original fixed-g actual field; material phase '+label).encode()[:80].ljust(80,b' ')
    raw+=struct.pack('<I',len(faces))+record.tobytes()
    require(len(raw)==84+50*len(faces) and len(raw)<5_000_000,'STL must be smaller than 5 MB')
    path.write_bytes(raw)
    # Read the actual file header and complete records back, not just a predicted size.
    restored=path.read_bytes();count=struct.unpack('<I',restored[80:84])[0]
    parsed=np.frombuffer(restored,dtype=dtype,offset=84)
    require(count==len(faces) and np.array_equal(parsed['vertices'],tri),'STL readback mismatch')
    return dict(file=path.name,sha256=sha(path),bytes=len(restored),triangles=count,
                minimumDoubleTriangleArea=float(area.min()),signedVolume=float(volume),
                vertexFloat32MaximumError=float(np.max(abs(v.astype(float)-vertices))),
                actualBinaryReadbackEqual=True),v


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','data','grid','query-report','query-cache','out'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--field',type=Path);ap.add_argument('--result',type=Path)
    ap.add_argument('--geometry-report',type=Path)
    ap.add_argument('--reference-only',action='store_true')
    ap.add_argument('--angular',type=int,default=216)
    ap.add_argument('--prefix-intervals',type=int,default=64)
    ap.add_argument('--tail-intervals',type=int,default=32)
    args=ap.parse_args();started=time.monotonic()
    require(not args.out.exists(),'Fresh mesh manifest required')
    require(args.angular>=48 and args.angular%12==0,'Angular count must be a positive multiple of 12')
    require(args.prefix_intervals>0 and args.tail_intervals>0,'Positive radial sampling counts required')
    if args.reference_only:
        require(not args.field and not args.result and not args.geometry_report,'Reference mode takes no solver field')
    else: require(args.field and args.result,'Actual mesh requires the saved field and matching result')
    whole=load('closed_stl_whole',args.scripts/'6a65-m12-entire-half-cartesian-bvp.py')
    joint=load('closed_stl_joint',args.scripts/'6a65-m12-global-common-cut-position-recovered.py')
    bg=load('closed_stl_background',args.scripts/'6a65-m12-original-tail-background.py')
    grid=json.loads(args.grid.read_text());args.background_tolerance=grid['background_tolerance']
    notes,meta_path,bridge_path,meta,native,chart=whole.definition(args,joint,bg)
    for key,path in [('data_sha256',args.data),('common_meta_sha256',meta_path),('bridge_sha256',bridge_path),
                     ('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg.__file__))]:
        require(grid[key]==sha(path),'Changed grid definition '+key)
    tail=whole.TailQueries(args.query_report,args.query_cache)
    if not args.reference_only:
        result=json.loads(args.result.read_text())
        for key,path in [('field_sha256',args.field),('grid_sha256',args.grid),
                         ('query_report_sha256',args.query_report),('query_cache_sha256',args.query_cache)]:
            require(result[key]==sha(path),'Saved field identity mismatch '+key)
    geometry=None
    if args.geometry_report:
        geometry=json.loads(args.geometry_report.read_text())
        require(geometry['field_sha256']==sha(args.field) and geometry['grid_sha256']==sha(args.grid),
                'Geometry report belongs to a different field')
    source=joint.CommonCutSource(args.data,meta_path,bridge_path,args.query_report,args.query_cache)
    unused,cc=joint.ad.exact_section(args.data,Q(0));central=joint.ad.NativeCurve(cc,512,32)
    basis=whole.basis_for(joint,np.asarray(grid['unit_mesh']),grid['order'],chart)
    if args.reference_only: coefficients=np.zeros((basis.nb,basis.na))
    else:
        with np.load(args.field,allow_pickle=False) as f:
            coefficients=f['coefficients'].copy()
            require(np.array_equal(f['unit_knots'],basis.knots) and np.array_equal(f['planar_modes'],basis.pm)
                    and np.array_equal(f['vertical_modes'],basis.zm),'Changed saved Cartesian basis')
    require(coefficients.shape==(basis.nb,basis.na) and np.isfinite(coefficients).all(),'Incomplete saved field')
    N=args.angular;u=np.arange(N)*2*np.pi/N
    theta=np.concatenate([central.theta(u[j:j+32]) for j in range(0,N,32)])
    recovered=np.concatenate([joint.bvp.glue.material_angle(central,theta[j:j+32]) for j in range(0,N,32)])
    inverse_error=float(np.max(abs(recovered-u)))
    require(inverse_error<3e-12,'Central material inverse failed')
    old0=source.point(LD(0),np.asarray(u,LD))
    target=np.zeros((3,N,3));target[0]=joint.ad.FixedRadiusCurve(central,1.).derivative(theta,0);target[1,:,2]=1
    delta=target-old0[[0,1,3]]
    h=joint.ad.base.ld(source.metric.Tu*source.metric.eps)
    hermite=np.asarray([[1,0,0,-10,15,-6],[0,h,0,-6*h,8*h,-3*h],
                        [0,0,h*h/2,-3*h*h/2,3*h*h/2,-h*h/2]],LD)
    def correction(z):
        radial=basis.spline(np.asarray([float(z)]))[:,3:-3]@coefficients
        planar=np.exp(1j*theta[:,None]*basis.pm[None,:])@radial[0,:len(basis.pm)]
        height=np.cos(theta[:,None]*basis.zm[None,:])@radial[0,len(basis.pm):]
        return np.stack((planar.real,planar.imag,height),axis=-1)
    def prefix_point(x):
        p=source.point(LD(x),np.asarray(u,LD))[0]
        s=LD(x)*chart.S
        if s<=h:
            H=np.polynomial.polynomial.polyval(s/h,hermite.T)
            p+=np.einsum('a,and->nd',H,delta).astype(float)
        return p+correction(s/chart.total)
    er=np.stack((np.cos(u),np.sin(u),np.zeros(N)),axis=-1)
    def tail_point(r):
        c=tail.coefficient(r);drop=chart.background.point(r)[2]
        p=tail.apply(c[0],np.asarray(u,LD),0)+r*er
        p[:,2]+=source.cut_height+drop
        return np.asarray(p,float)+correction(chart.inverse_radius(r))
    # Select actual cached exact source radii, never interpolate a new tail coefficient.
    candidates=sorted((Q(k) for k in tail.lookup),reverse=True)
    chosen=[]
    for value in np.linspace(float(chart.c),float(chart.cuff),args.tail_intervals+1):
        radius=min(candidates,key=lambda r:abs(float(r)-value))
        if not chosen or abs(float(radius-chosen[-1]))>1e-7: chosen.append(radius)
    require(len(chosen)==args.tail_intervals+1,'Insufficient distinct cached radii for requested mesh')
    radii=[whole.ld(r) for r in chosen]
    require(radii[0]==chart.c and radii[-1]==chart.cuff,'Mesh must include exact cut and true cuff')
    upper=[prefix_point(x) for x in np.linspace(0,1,args.prefix_intervals+1)]
    seams={'centralPlane':float(np.max(abs(upper[0][:,2]))),
           'internalCut':float(np.max(np.linalg.norm(upper[-1]-tail_point(chart.c),axis=1)))}
    upper[0][:,2]=0.;upper[-1]=tail_point(chart.c)
    upper.extend(tail_point(r) for r in radii[1:])
    height=float(source.cut_height+chart.background.point(chart.cuff)[2])
    fixed_cuff=cap(float(chart.cuff),u,height,False)
    seams['trueCuff']=float(np.max(np.linalg.norm(upper[-1]-fixed_cuff,axis=1)))
    require(max(seams.values())<1e-8,'Numerical common seam mismatch')
    upper[-1]=fixed_cuff;active_count=len(upper)-1
    cap_radii=[.13,.11,.095,.08,.065,.05,.025]
    require(all(0<r<float(chart.cuff) for r in cap_radii),'Cap sampling leaves true disk')
    upper.extend(cap(r,u,height,True) for r in cap_radii)
    fixed=[False]*active_count+[True]*(len(upper)-active_count)
    lower=[]
    for i in range(len(upper)-1,0,-1):
        p=upper[i].copy();p[:,2]=-height if i>active_count else -p[:,2];lower.append(p)
    rings=np.stack(lower+upper);fixed_rings=np.asarray(fixed[1:][::-1]+fixed,dtype=bool)
    faces=faces_for(len(rings),N);nv=2+len(rings)*N;top=topology(faces,nv)
    require(84+50*len(faces)<5_000_000,'Requested complete STL exceeds 5 MB')
    mask=np.r_[True,np.repeat(fixed_rings,N),True]
    args.out.parent.mkdir(parents=True,exist_ok=True);meshfiles=[];fixed_first=None
    for t in (Q(0),Q(1,4),Q(1,2)):
        shift=Q(N)*t/3;require(shift.denominator==1,'Material phase is not an integer grid shift')
        phase=np.roll(rings,int(shift),axis=1).copy();alpha=2*np.pi*float(t)/3
        x,y=phase[...,0].copy(),phase[...,1].copy();co,si=np.cos(alpha),np.sin(alpha)
        phase[...,0]=co*x-si*y;phase[...,1]=si*x+co*y
        phase[fixed_rings]=rings[fixed_rings]
        vertices=np.concatenate(([[0,0,-height]],phase.reshape(-1,3),[[0,0,height]]))
        label='0' if t==0 else str(t.numerator)+'of'+str(t.denominator)
        info,v=write_stl(args.out.parent/('entire-half-t'+label+'.stl'),vertices,faces,str(t))
        if fixed_first is None:fixed_first=v[mask].copy()
        else:require(np.array_equal(fixed_first,v[mask]),'Serialized fixed cap vertices changed with time')
        info.update(timeExact=str(t),materialGridShift=int(shift));meshfiles.append(info)
    report=dict(schema='6a65-actual-M12-complete-closed-three-phase-STL-v1',scriptSHA256=sha(__file__),
        referenceOnly=args.reference_only,fieldSHA256=sha(args.field) if args.field else None,
        resultSHA256=sha(args.result) if args.result else None,gridSHA256=sha(args.grid),
        queryReportSHA256=sha(args.query_report),queryCacheSHA256=sha(args.query_cache),dataSHA256=sha(args.data),
        geometryReportSHA256=sha(args.geometry_report) if args.geometry_report else None,
        continuousGeometryTransferChecksPassed=geometry.get('homotopy_embedded_and_reach_transfer_proved') if geometry else None,
        angularNodes=N,prefixIntervals=args.prefix_intervals,tailIntervals=args.tail_intervals,
        exactTailRadiusListSHA256=hashlib.sha256(('\n'.join(map(str,chosen))+'\n').encode()).hexdigest(),
        nativeAngleIsInvertedFromUniformMaterialAngle=True,centralInverseNumericalResidual=inverse_error,
        sameOriginalMetricAndSameSavedField=True,completeCentralPrefixBridgeFiniteTailDeepCollarAndBothCaps=True,
        upperCapBumps=3,lowerCapBumps=0,fixedCapsBitwiseIdenticalInSerializedFloat32=True,
        fixedVertices=int(mask.sum()),topology=top,numericalSeamGaps=seams,meshFiles=meshfiles,
        continuousVertexErrorCertified=False,discreteSelfIntersectionCertified=False,
        fixedMetricRefinementGatePaid=False,READMEComplete=False,
        rawRetention='Temporary local/runner directory only. No raw Git, artifact, or release upload.',
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False),flush=True)


if __name__=='__main__': main()
