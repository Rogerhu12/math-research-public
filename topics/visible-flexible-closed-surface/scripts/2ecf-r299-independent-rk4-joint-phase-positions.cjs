'use strict';
// Independent R299 short-phase Cauchy calculation and physical position continuation.
// The Fourier n,m state uses genuine Cauchy data. All spatial derivatives below
// belong to the saved finite RK4/H17 geometric source of this experiment.
let YAW=0;
const PI=Math.PI, NX=2048, hx=PI/(2*NX), shapeK=(PI-.3)/(PI-1.5), lx=new Float64Array(NX+1), ly=new Float64Array(NX+1);
function binomial(n, k){
    let z=1;
    for(let j=1;j<=k;j++)z=z*(n-j+1)/j;
    return z
}
function quadrantAngleAndCurvature(t){
    let x=Math.min(1, Math.max(0, 2*t-1)), u=Math.min(x, 1-x), sp=0, int=0;
    for(let j=0;j<8;j++){
        let v=(j%2?-1:1)*binomial(7, j)*51480*u**(8+j)/(8+j);
        sp+=v;
        int+=v*u/(9+j)
    }
    if(x>.5){
        sp=1-sp;
        int=.5-u+int
    }
    return [.2*t+(shapeK-.2)*(.5*int+Math.max(t-1, 0)), .2+(shapeK-.2)*sp]
}
function quadrantTangentIntegrands(t){
    let b=quadrantAngleAndCurvature(t)[0];
    return [Math.sin(b), Math.cos(b)]
}
for(let i=0;i<NX;i++){
    let a=quadrantTangentIntegrands(i*hx), b=quadrantTangentIntegrands((i+.5)*hx), c=quadrantTangentIntegrands((i+1)*hx);
    lx[i+1]=lx[i]+hx/6*(a[0]+4*b[0]+c[0]);
    ly[i+1]=ly[i]+hx/6*(a[1]+4*b[1]+c[1]);
}
function inletGeometry(u){
    u=(u%(2*PI)+2*PI)%(2*PI);
    let q=Math.floor(u/(PI/2)), t=u-q*PI/2;
    if(q%2)t=PI/2-t;
    let [b, k]=quadrantAngleAndCurvature(t), i=Math.min(NX, Math.floor(t/hx)), d=t-i*hx, h=quadrantTangentIntegrands(i*hx), p=quadrantTangentIntegrands((i*hx+t)/2), f=quadrantTangentIntegrands(t), x=lx[NX]-lx[i]-d/6*(h[0]+4*p[0]+f[0]), y=ly[i]+d/6*(h[1]+4*p[1]+f[1]);
    let sx=q==0||q==3?1:-1, sy=q<2?1:-1;
    return [[x*sx, y*sy, 0], [-sy*Math.sin(b), sx*Math.cos(b), 0], [sx*Math.cos(b), sy*Math.sin(b), 0], k]
}
const smoothStep=t=>t**3*(10-15*t+6*t*t);
function radialMetric(s){
    let t=s/.06;
    return [1+.006*.06*(21*t**6-60*t**7+67.5*t**8-35*t**9+7*t**10), .006*(126*t**5-420*t**6+540*t**7-315*t**8+70*t**9), .1*630*t**4*(1-t)**4]
}
function fourierTransform(re, im, inv=false){
    let n=re.length, j=0;
    for(let i=1;i<n;i++){
        let b=n>>1;
        for(;j&b;b>>=1)j^=b;
        j^=b;
        if(i<j){
            let v=re[i];
            re[i]=re[j];
            re[j]=v;
            v=im[i];
            im[i]=im[j];
            im[j]=v
        }
    }
    for(let l=2;l<=n;l*=2){
        let t=(inv?2:-2)*PI/l, wr=Math.cos(t), wi=Math.sin(t);
        for(let i=0;i<n;i+=l){
            let c=1, s=0;
            for(let j=0;j<l/2;j++){
                let a=i+j, b=i+j+l/2, rr=re[b]*c-im[b]*s, ii=re[b]*s+im[b]*c;
                re[b]=re[a]-rr;
                im[b]=im[a]-ii;
                re[a]+=rr;
                im[a]+=ii;
                let nc=c*wr-s*wi;
                s=s*wr+c*wi;
                c=nc
            }
        }
    }
    if(inv)for(let i=0;i<n;i++){
        re[i]/=n;
        im[i]/=n
    }
}
function projectShapeHarmonics(x, N, M, der, odd){
    let re=new Float64Array(x), im=new Float64Array(N);
    fourierTransform(re, im);
    for(let j=0;j<N;j++){
        let k=j<=N/2?j:j-N;
        if(Math.abs(k)>M||k%2!==0){
            re[j]=im[j]=0;
            continue
        }
        if(odd)re[j]=0;
        else im[j]=0;
        if(der){
            let t=-k*im[j];
            im[j]=k*re[j];
            re[j]=t
        }
    }
    fourierTransform(re, im, true);
    return re
}
function fourierCoefficients(c, N){
    let re=new Float64Array(c), im=new Float64Array(N);
    fourierTransform(re, im);
    return [Array.from(re.slice(0, N/2+1), a=>a/N), Array.from(im.slice(0, N/2+1), a=>a/N)]
}
function angularJet(C, u, j){
    let c=Math.cos(u), s=Math.sin(u), co=1, si=0, ans=(j===0?C[0][0]:0), n=C[0].length;
    for(let k=1;k<n;k++){
        let nc=co*c-si*s;
        si=co*s+si*c;
        co=nc;
        let r=C[0][k], g=C[1][k], v=j===0?r*co-g*si:j===1?-k*(g*co+r*si):-k*k*(r*co-g*si);
        ans+=2*v
    }
    return ans
}
function integrateCauchy(N=128, M=31, steps=128, nodes=17){
    let X=new Float64Array(14*N);
    for(let i=0;i<N;i++){
        let [p, T, n, k]=inletGeometry(i*2*PI/N);
        X[i]=k;
        for(let c=0;c<3;c++){
            X[(2+c)*N+i]=p[c]+(c==2?.78:0);
            X[(5+c)*N+i]=+(c==2);
            X[(8+c)*N+i]=T[c];
            X[(11+c)*N+i]=-n[c]
        }
    }
    X.set(projectShapeHarmonics(X.subarray(0, N), N, M, false, false), 0);
    let output=[];
    function lval(s, X){
        let [f, fp, fpp]=radialMetric(s);
        return Float64Array.from({
            length:N
        }, (_, i)=>(X[N+i]*X[N+i]-fpp/f)/X[i])
    }
    function rhs(s, X){
        let [f, fp, fpp]=radialMetric(s), l=lval(s, X), lu=projectShapeHarmonics(l, N, M, true, false), mu=projectShapeHarmonics(X.subarray(N, 2*N), N, M, true, true), Y=new Float64Array(14*N);
        for(let i=0;i<N;i++){
            let n=X[i], m=X[N+i];
            Y[i]=mu[i]/f+fp/f*(l[i]-n);
            Y[N+i]=lu[i]/f-2*fp/f*m;
            for(let j=0;j<3;j++){
                let p=(2+j)*N+i, v=(5+j)*N+i, e=(8+j)*N+i, nn=(11+j)*N+i;
                Y[p]=X[v];
                Y[v]=l[i]*X[nn];
                Y[e]=m*X[nn];
                Y[nn]=-l[i]*X[v]-m*X[e]
            }
        }
        Y.set(projectShapeHarmonics(Y.subarray(0, N), N, M, false, false), 0);
        Y.set(projectShapeHarmonics(Y.subarray(N, 2*N), N, M, false, true), N);
        return Y
    }
    const h=.06/steps;
    for(let j=0;j<=steps;j++){
        let s=j*h;
        if(j%(steps/(nodes-1))===0){
            let l=lval(s, X), J=[];
            for(let t=0;t<3;t++){
                let xyz=[];
                for(let c=0;c<3;c++){
                    let ar=t<2?X.slice(((t===0?2:5)+c)*N, ((t===0?3:6)+c)*N):Float64Array.from(l, (v, i)=>v*X[(11+c)*N+i]);
                    xyz.push(fourierCoefficients(ar, N))
                }
                J.push(xyz)
            }
            output.push(J)
        }
        if(j==steps)break;
        let A=rhs(s, X), B=rhs(s+h/2, Float64Array.from(X, (a, i)=>a+h/2*A[i])), C=rhs(s+h/2, Float64Array.from(X, (a, i)=>a+h/2*B[i])), D=rhs(s+h, Float64Array.from(X, (a, i)=>a+h*C[i]));
        for(let i=0;i<X.length;i++)X[i]+=h/6*(A[i]+2*B[i]+2*C[i]+D[i])
    }
    return output
}
function leftHermiteBasis(t, L, order){
    let v=order==0?[1-smoothStep(t), t-6*t**3+8*t**4-3*t**5, (t*t-3*t**3+3*t**4-t**5)/2]:order==1?[-30*t*t*(1-t)**2, 1-18*t*t+32*t**3-15*t**4, t-4.5*t*t+6*t**3-2.5*t**4]:[-60*t*(1-t)*(1-2*t), -36*t+96*t*t-60*t**3, 1-9*t+18*t*t-10*t**3];
    return v.map((x, j)=>x*L**(j-order))
}
function physicalJets(P, s, u, delta, L, r){
    let h0=.06, N=P.length-1, h=h0/N, az=.78, g=.10, rad=s-h0, t=Math.max(0, rad/L), q=1-smoothStep(t), qp=-30*t*t*(1-t)**2/L, qpp=-60*t*(1-t)*(1-2*t)/L**2;
    let ang=u+delta*(YAW+(1-YAW)*q);
    let [X, T, no, kk]=inletGeometry(ang);
    let G=[X, T, no.map(x=>-kk*x)], c=Math.cos(ang), si=Math.sin(ang), C=[[r*c, r*si, 0], [-r*si, r*c, 0], [-r*c, -r*si, 0]], J=[];
    function endpoint(i, k, d, co){
        if(i===0){
            if(d===0)return G[k][co]+(k===0&&co===2?az:0);
            return +(d===1&&k===0&&co===2)
        }
        return angularJet(P[i][d][co], ang, k)
    }
    for(let [a, b] of [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1], [0, 2]]){
        let z=[];
        for(let co=0;co<3;co++){
            let v=0;
            if(s<h0){
                let i=Math.min(N-1, Math.max(0, Math.floor(s/h))), t=(s-i*h)/h, vl=leftHermiteBasis(t, h, a), vr=leftHermiteBasis(1-t, h, a);
                for(let d=0;d<3;d++)v+=vl[d]*endpoint(i, b, d, co)+vr[d]*((-1)**(a+d))*endpoint(i+1, b, d, co)
            }
            else{
                let l=G[b][co], rr=C[b][co];
                v=a===0?q*l+(1-q)*rr+(b===0&&co===2?az+s:0):a===1?qp*(l-rr)+(b===0&&co===2?1:0):qpp*(l-rr);
                if(rad<g){
                    let hb=leftHermiteBasis(rad/g, g, a);
                    for(let d=0;d<3;d++){
                        let e=endpoint(N, b, d, co);
                        if(d===0)e-=G[b][co]+(b===0&&co===2?az+h0:0);
                        if(d===1&&b===0&&co===2)e-=1;
                        v+=hb[d]*e
                    }
                }
            }
            z.push(v)
        }
        J.push(z)
    }
    if(s>=h0){
        let v=delta*(1-YAW)*qp, d=delta*(1-YAW)*qpp;
        for(let c=0;c<3;c++){
            J[3][c]+=2*v*J[4][c]+v*v*J[5][c]+d*J[2][c];
            J[4][c]+=v*J[5][c];
            J[1][c]+=v*J[2][c]
        }
    }
    return J
}
function dot(a, b){
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
}
function initialGramNormalization(G){
    let E=dot(G[1], G[1]), F=dot(G[1], G[2]), U=dot(G[2], G[2]);
    return [1/Math.sqrt(E), F/E, 1/Math.sqrt(U-F*F/E)]
}
function normalizedMetricError(V, U, T){
    let A=V.map(v=>v*T[0]), B=U.map((u, i)=>(u-T[1]*V[i])*T[2]), e=dot(A, A)-1, f=dot(A, B), g=dot(B, B)-1;
    return [Math.abs(e+g)/2+Math.hypot((e-g)/2, f), [e, Math.SQRT2*f, g], A, B]
}
function splineBasis(kn, x, m){
    let n=kn.length-6, o=new Float64Array(n-6), p=new Float64Array(n-6), q=new Float64Array(n-6);
    if(x<=kn[0]+1e-14||x>=kn[kn.length-1]-1e-14)return [o, p, q];
    let A=Array.from({
        length:6
    }, ()=>new Float64Array(kn.length));
    for(let i=0;i<kn.length-1;i++)A[0][i]=+(kn[i]<=x&&x<kn[i+1]);
    for(let d=1;d<=5;d++)for(let i=0;i<kn.length-d-1;i++){
        let l=kn[i+d]-kn[i], r=kn[i+d+1]-kn[i+1];
        A[d][i]=(l?(x-kn[i])/l*A[d-1][i]:0)+(r?(kn[i+d+1]-x)/r*A[d-1][i+1]:0)
    }
    function der(i, d){
        let l=kn[i+d]-kn[i], r=kn[i+d+1]-kn[i+1];
        return (l?d/l*A[d-1][i]:0)-(r?d/r*A[d-1][i+1]:0)
    }
    for(let i=3;i<n-3;i++){
        o[i-3]=A[5][i];
        p[i-3]=der(i, 5);
        let l=kn[i+5]-kn[i], r=kn[i+6]-kn[i+1];
        q[i-3]=(l?5/l*der(i, 4):0)-(r?5/r*der(i+1, 4):0)
    }
    return [o, p, q]
}
function choleskyDirection(H, g, n, dam){
    let Z=new Float64Array(H), y=new Float64Array(g), x=new Float64Array(n);
    for(let i=0;i<n;i++)Z[i*n+i]+=(Math.max(1.e-9, H[i*n+i])*dam+1e-13);
    for(let i=0;i<n;i++){
        for(let j=0;j<=i;j++){
            let v=Z[i*n+j];
            for(let k=0;k<j;k++)v-=Z[i*n+k]*Z[j*n+k];
            Z[i*n+j]=i===j?Math.sqrt(Math.max(v, 1e-16)):v/Z[j*n+j]
        }
    }
    for(let i=0;i<n;i++){
        for(let j=0;j<i;j++)y[i]-=Z[i*n+j]*y[j];
        y[i]/=Z[i*n+i]
    }
    for(let i=n-1;i>=0;i--){
        let z=y[i];
        for(let j=i+1;j<n;j++)z-=Z[j*n+i]*x[j];
        x[i]=z/Z[i*n+i]
    }
    return x
}
function observationGrid(P, par, nu, nr, shift){
    let {
        RS, CS, K, delta, L, r
    }
    =par, nB=RS+CS-1, size=nB*(2*K+1)+1, kn=[...Array(5).fill(0), ...Array.from({
        length:RS+1
    }, (_, i)=>.06*i/RS), ...Array.from({
        length:CS
    }, (_, i)=>.06+L*(i+1)/CS), ...Array(5).fill(.06+L)], s=[];
    for(let i=0;i<=Math.max(6, 2*RS);i++)s.push(.06*i/Math.max(6, 2*RS));
    for(let i=0;i<nr;i++)s.push(.06+L*(i+shift)/nr);
    s.push(.06+L);
    let out=[];
    for(let v of s){
        let [B, Bs, Bss]=splineBasis(kn, v, K), t=Math.max(0, (v-.06)/L), gp=30*t*t*(1-t)**2/L, gpp=60*t*(1-t)*(1-2*t)/L**2;
        for(let u0=0;u0<nu;u0++){
            let u=(u0+(shift-.5)*.44)*2*PI/nu, Y=physicalJets(P, v, u, delta, L, r), Ref=physicalJets(P, v, u, 0, L, r), target=initialGramNormalization(Ref), dS=new Float64Array(size), dU=new Float64Array(size), ss=new Float64Array(size), su=new Float64Array(size), uu=new Float64Array(size);
            let A=[1], Ap=[0], App=[0];
            for(let f=0;f<2;f++)for(let k=1;k<=K;k++){
                let z=k*u-f*PI/2;
                A.push(Math.cos(z));
                Ap.push(-k*Math.sin(z));
                App.push(-k*k*Math.cos(z))
            }
            for(let i=0;i<nB;i++)for(let j=0;j<A.length;j++){
                let p=i*A.length+j;
                dS[p]=Bs[i]*A[j];
                dU[p]=B[i]*Ap[j];
                ss[p]=Bss[i]*A[j];
                su[p]=Bs[i]*Ap[j];
                uu[p]=B[i]*App[j]
            }
            dS[size-1]=gp;
            ss[size-1]=gpp;
            out.push([Y, target, dS, dU, ss, su, uu, v, u]);
        }
    }
    return out
}
function evaluateOrLinearize(rows, x, lin, power=0, high=1, curv=false){
    let n=x.length, size=n/3, H=lin?new Float64Array(n*n):null, g=lin?new Float64Array(n):null, max=0, loss=0, mk=0, minarea=1e10, loc=null, A0=new Float64Array(n), A1=new Float64Array(n), A2=new Float64Array(n);
    for(let row of rows){
        let [Y, T, ds, du, ss, su, uu, v0, u0]=row, V=Y[1].slice(), U=Y[2].slice(), Vss=curv?Y[3].slice():null, Vsu=curv?Y[4].slice():null, Vuu=curv?Y[5].slice():null;
        for(let c=0;c<3;c++){
            let b=c*size;
            for(let i=0;i<size;i++){
                let a=x[b+i];
                V[c]+=a*ds[i];
                U[c]+=a*du[i];
                if(curv){
                    Vss[c]+=a*ss[i];
                    Vsu[c]+=a*su[i];
                    Vuu[c]+=a*uu[i]
                }
            }
        }
        let [e, res, A, B]=normalizedMetricError(V, U, T);
        if(e>max){
            max=e;
            loc=[v0, u0]
        }
        loss+=e**6;
        if(lin){
            let wt=Math.max(.04, e/high)**(2*power)/rows.length;
            for(let i=0;i<size;i++){
                let ba=ds[i]*T[0], bb=(du[i]-T[1]*ds[i])*T[2];
                for(let c=0;c<3;c++){
                    let p=c*size+i;
                    A0[p]=2*A[c]*ba;
                    A1[p]=Math.SQRT2*(A[c]*bb+B[c]*ba);
                    A2[p]=2*B[c]*bb
                }
            }
            for(let i=0;i<n;i++){
                let e0=wt*A0[i], e1=wt*A1[i], e2=wt*A2[i];
                if(e0===0&&e1===0&&e2===0)continue;
                g[i]-=e0*res[0]+e1*res[1]+e2*res[2];
                let p=i*n;
                for(let j=0;j<=i;j++)H[p+j]+=e0*A0[j]+e1*A1[j]+e2*A2[j]
            }
        }
        if(curv){
            let E=dot(V, V), F=dot(V, U), G=dot(U, U), det=E*G-F*F, N=[V[1]*U[2]-V[2]*U[1], V[2]*U[0]-V[0]*U[2], V[0]*U[1]-V[1]*U[0]].map(z=>z/Math.sqrt(det)), l=dot(N, Vss), m=dot(N, Vsu), nn=dot(N, Vuu), tr=(l*G+nn*E-2*m*F)/det, K=(l*nn-m*m)/det, k=Math.abs(tr)/2+Math.sqrt(Math.max(0, tr*tr/4-K));
            mk=Math.max(mk, k);
            minarea=Math.min(minarea, det)
        }
    }
    return {
        max, loc, loss:(loss/rows.length)**(1/6), curvature:curv?mk:null, minArea:curv?minarea:null, H, g
    }
}
function observationOnly(d){
    let o={
        ...d
    };
    delete o.H;
    delete o.g;
    return o
}
function solvePhase(P, par, seedState){
    let {
        RS, CS, K, delta, L, r, nu, nr, steps
    }
    =par, rows=observationGrid(P, par, nu, nr, .348), ind=observationGrid(P, par, nu*2+3, nr*2+3, .618), size=rows[0][2].length;
    let x=seedState?new Float64Array(seedState):new Float64Array(3*size), start=observationOnly(evaluateOrLinearize(ind, x, false, 0, 1, true)), trace=[];
    for(let step=0;step<steps;step++){
        let now=evaluateOrLinearize(rows, x, false), lin=evaluateOrLinearize(rows, x, true, step<3?.35:step<8?.8:1.35, now.max), best=null;
        for(let damping of [1e-8, 1e-5, .001, .02]){
            let dx=choleskyDirection(lin.H, lin.g, x.length, damping);
            for(let a of [1, .5, .25, .125, .0625]){
                let xx=Float64Array.from(x, (v, i)=>v+a*dx[i]), obs=evaluateOrLinearize(rows, xx, false), score=obs.loss+.10*obs.max;
                if(obs.loss<now.loss&&obs.max<now.max*1.0005&&(!best||score<best.score))best={
                    xx, obs, score, a, damping
                }
            }
        }
        if(!best)break;
        x=best.xx;
        trace.push({
            step:step+1, a:best.a, damping:best.damping, training:observationOnly(best.obs)
        })
    }
    return {
        params:par, variables:x.length, initial:start, trace, training:observationOnly(evaluateOrLinearize(rows, x, false, 0, 1, true)), independent:observationOnly(evaluateOrLinearize(ind, x, false, 0, 1, true)), state:Array.from(x)
    }
}
function prolongPositionCoefficients(old, newParams){
    let a=old.params, b=newParams, p=5, k0=a.K, k1=b.K, r0=a.RS+a.CS-1, r1=b.RS+b.CS-1, d0=2*k0+1, d1=2*k1+1, s0=r0*d0+1, s1=r1*d1+1, make=(r, c)=>[...Array(5).fill(0), ...Array.from({
        length:r+1
    }, (_, i)=>.06*i/r), ...Array.from({
        length:c
    }, (_, i)=>.06+b.L*(i+1)/c), ...Array(5).fill(.06+b.L)], knot=make(a.RS, a.CS), nk=make(b.RS, b.CS), positive=new Set(knot), newk=nk.filter((x, j)=>j>=6&&j<nk.length-6&&!positive.has(x));
    if(k0>k1||a.L!==b.L||a.r!==b.r||b.CS%a.CS||b.RS%a.RS)throw Error('non-nested integrateCauchy');
    let out=new Float64Array(3*s1);
    for(let c=0;c<3;c++){
        out[c*s1+s1-1]=old.state[c*s0+s0-1];
        for(let j=0;j<d0;j++){
            let f=Array(r0+6).fill(0), u=knot.slice();
            for(let i=0;i<r0;i++)f[i+3]=old.state[c*s0+i*d0+j];
            for(let t of newk){
                let k=u.findIndex(z=>z>t)-1, q=Array(f.length+1);
                for(let i=0;i<q.length;i++){
                    if(i<=k-p)q[i]=f[i];
                    else if(i>k)q[i]=f[i-1];
                    else{
                        let a=(t-u[i])/(u[i+p]-u[i]);
                        q[i]=a*f[i]+(1-a)*f[i-1]
                    }
                }
                u.splice(k+1, 0, t);
                f=q
            }
            let jj=j<=k0?j:k1+j-k0;
            for(let i=0;i<r1;i++)out[c*s1+i*d1+jj]=f[i+3]
        }
    }
    return out
}

function runFamily() {
    const source = integrateCauchy(256, 63, 128, 17);
    YAW = 0;
    const small = solvePhase(source, {RS:2, CS:5, K:3, delta:1/1024, L:.38, r:.62, nu:36, nr:20, steps:12});
    YAW = 1;
    const wide = solvePhase(source, {RS:2, CS:6, K:5, delta:1/1024, L:.58, r:.94, nu:40, nr:25, steps:12});
    const finerParams = {...wide.params, K:8, nu:52, nr:32};
    const fine = solvePhase(source, finerParams, prolongPositionCoefficients(wide,finerParams));
    let last=wide;
    const orbit=[];
    for (const delta of [1/256,1/64,1/16,1/8,1/4,1/2]) {
        const next = {...wide.params, delta, steps:9};
        const ratio=delta/last.params.delta;
        last=solvePhase(source,next,last.state.map(v=>ratio*v));
        orbit.push(last);
    }
    return {schema:'independent-r299-M63-RK4-joint-strip-physical-phases-v1',
            cauchy:{angles:256,shapeBand:63,rk4Steps:128,radialKnots:17,centralHalfHeight:.78,rampLength:.06,quadratureQuarterCells:2048},
            small,wide,fine,orbit};
}
if (typeof require === 'function' && require.main === module) {
    const fs=require('node:fs');
    const out=process.argv[2];
    if (!out) throw new Error('Pass a new output JSON pathname');
    fs.writeFileSync(out,JSON.stringify(runFamily(),null,2)+'\n',{flag:'wx'});
}
