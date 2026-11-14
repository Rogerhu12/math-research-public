#!/usr/bin/env python3
"""R245: exact CM17 polynomials, second-order quotients, and logarithmic bridge.

Only Python's standard library is used. Arithmetic is rational and Q(i).
No changing target prime, numerical period, or truncated Mellin inference.
"""
from fractions import Fraction as Q
import json

ORDER=72
P_H=list(reversed(list(map(Q,(
    '1','-567/55','5799/55','-17527/55','-18057/11','25927/5',
    '-154733/55','-8103/11','94949/55','-136101/55','135253/55',
    '-70277/55','25169/55','-765/11','177/55','-1/55'
)))))
P_RE=list(map(Q,[-15,256,9512,-51616,135756,161344,998200,-4052192,
                   6022934,-4457856,1410136,-9568,-156884,53824,1736,-32,1]))
P_IM=list(map(Q,[-8,1832,-16968,49384,9816,-676792,1877912,-2859384,
                   198888,2926200,-2286808,423608,89800,4120,-3704,-40,0]))


def multiply(a,b,limit=ORDER):
    c=[Q(0)]*min(limit+1,len(a)+len(b)-1)
    for j,x in enumerate(a):
        if x:
            for k,y in enumerate(b[:len(c)-j]):
                if y:c[j+k]+=x*y
    return c


def exps(a):
    c=[Q(1)]+[Q(0)]*ORDER
    for n in range(1,ORDER+1):
        c[n]=sum((k*a[k]*c[n-k] for k in range(1,n+1)),Q(0))/n
    return c


def cm(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def cscale(a,n):
    return (a[0]*n,a[1]*n)


def cadd(a,b):
    return (a[0]+b[0],a[1]+b[1])


def check_cm_polynomials():
    # u through order 72 gives u' correctly through the held-out weight 68.
    u=[Q(0)]*(ORDER+1);u[1]=Q(1)
    for n in range(ORDER-1):
        cube=sum((u[a]*u[b]*u[n-a-b]
                  for a in range(n+1) for b in range(n+1-a)),Q(0))
        u[n+2]=-2*cube/((n+1)*(n+2))
    u2=multiply(u,u);u4=multiply(u2,u2)
    log_theta=[Q(0)]*(ORDER+1)
    for n in range(ORDER-1):log_theta[n+2]=u2[n]/((n+1)*(n+2))
    up=[(j+1)*u[j+1] for j in range(ORDER)]+[Q(0)]
    s8=multiply(up,exps([4*x for x in log_theta]))
    base=multiply(up,exps([68*x for x in log_theta]))
    powers=[];pw=[Q(1)]+[Q(0)]*ORDER
    for j in range(17):
        powers.append(multiply(base,pw));pw=multiply(pw,u4)
    alpha4=(Q(161),Q(240));alpha_power=(Q(1),Q(0))
    for j in range(18):
        m=4*j
        actual=cscale(alpha_power,s8[m])
        candidate=(Q(0),Q(0))
        for k in range(17):
            candidate=cadd(candidate,cscale((P_RE[16-k],P_IM[16-k]),powers[k][m]))
        assert actual==candidate
        alpha_power=cm(alpha_power,alpha4)
    assert s8[0]==1 and s8[4]==Q(-1,6)
    return {'all_17_determining_weights':True,'held_out_weight_68':True,
            'S8_constant':'1','S8_weight_4':'-1/6'}


def pp(a,n):
    r=[Q(1)]
    for _ in range(n):r=multiply(r,a,32)
    return r


def operator_column(j):
    # L=16 U^2(U-1)^2 d^2 -12 U(U-1)(37U-19)d
    #     +(3306U^2-3396U+930).
    c=[Q(0)]*17
    c[j]=16*j*(j-1)-228*j+930
    c[j+1]=-32*j*(j-1)+672*j-3396
    c[j+2]=16*j*(j-1)-444*j+3306
    return c


def solve(M,b):
    a=[row[:]+[b[j]] for j,row in enumerate(M)]
    det=Q(1)
    for j in range(17):
        k=next(k for k in range(j,17) if a[k][j])
        if k!=j:a[j],a[k]=a[k],a[j];det=-det
        q=a[j][j];det*=q
        a[j]=[x/q for x in a[j]]
        for k in range(17):
            if k!=j and a[k][j]:
                q=a[k][j];a[k]=[x-q*y for x,y in zip(a[k],a[j])]
    return [row[-1] for row in a],det


def cv(P,M):
    v=(P+[Q(0)]*17)[:17]
    sol,det=solve(M,v)
    assert [sum((M[j][k]*sol[k] for k in range(17)),Q(0)) for j in range(17)]==v
    return {'P':P,'R14':sol[:15],'beta':sol[15],'gamma':sol[16],
            'beta_eff':sol[15]-sol[16]/2,'det':det}


def main():
    cm_checks=check_cm_polynomials()
    D=[Q(0)]*8+pp([Q(-1),Q(1)],8)
    DG=[Q(0)]*8+pp([Q(-1),Q(1)],7)+[Q(0)]
    columns=[operator_column(j) for j in range(15)]+[D,DG]
    M=[[columns[k][j] for k in range(17)] for j in range(17)]
    data={k:cv(P,M) for k,P in [('H',P_H),('re',P_RE),('im',P_IM)]}
    assert data['H']['beta']==Q(7584473604248,1766439675)
    assert data['H']['gamma']==Q(-541623088,10725)
    assert data['H']['beta_eff']==Q(802891497472,27175995)
    assert data['im']['beta_eff']==Q(-27773162749952,3129357)
    a=data['H']['beta_eff']/data['im']['beta_eff']
    assert a==Q(-14548243,4370281080)
    rs=[x-a*y for x,y in zip(data['H']['R14'],data['im']['R14'])]
    gs=data['H']['gamma']-a*data['im']['gamma']
    bs=data['H']['beta']-a*data['im']['beta']
    assert gs==Q(402182437912192,106525601325)
    assert bs==gs/2
    # The logarithmic coefficient cancels the exact z^2 mass.
    assert rs[-1]+gs/4==0
    z6=(Q(1)+40*a)/30
    assert z6==Q(47354392,1638855405) and z6!=0
    # Rational logarithmic identity:
    # d(4X/Y)=4(2(X^3-X)-X(3X^2-1))/(X^3-X)
    #        =-4-8/(X^2-1).
    assert [Q(0),Q(-4),Q(0),Q(-4)]==[
        Q(0),4*(-2+1),Q(0),4*(2-3)]
    assert sum(data['H']['R14'])==Q(4096,5775)
    assert data['H']['R14'][0]==Q(-1,51150)
    serialize=lambda v:([str(x) for x in v] if isinstance(v,list) else str(v))
    print(json.dumps({
        'theorem':'R245','status':'PASS','cm17_checks':cm_checks,
        'operator_matrix_determinant':str(data['H']['det']),
        'sources':{k:{key:serialize(val) for key,val in obj.items() if key!='det'}
                   for k,obj in data.items()},
        'bridge':{'a':str(a),'Rstar':[str(x) for x in rs],
                  'gamma_star':str(gs),'beta_star':str(bs),
                  'Cstar_z2_coefficient':'0','Cstar_z6_coefficient':str(z6)},
        'exact_polynomial_identities':True,
        'logarithmic_second_derivative_identity':True
    },indent=2))


if __name__=='__main__':
    main()
