"""Recover the signed root Laurent seed and evaluate true mixed derivatives at c.

The full stage provider is required to verify the pinned bytes before decoding.
All scientific functions require the original flint interval arithmetic.
"""
from fractions import Fraction
from math import comb, factorial
from flint import acb, arb
import fourfold_codazzi_root_Laurent_Taylor_algebra as L


LEADING = ("Xp", "T", "Q", "G", "a0", "b0")


def required_stages():
    return (["fold-degree-%03d" % n for n in range(15)]
            + ["leading-complete-"+name for name in LEADING]
            + ["leading-%s-degree-%03d" % (name,n) for name in LEADING for n in range(9,15)]
            + ["first-correction-degree-%03d" % n for n in range(13)])


def signed_series(stages):
    if set(required_stages()) != set(stages):
        raise ValueError("incomplete signed root seed")
    result = {field: [] for field in ("chi", *LEADING, "w1a", "w1b")}
    for n in range(15):
        row=stages["fold-degree-%03d" % n]
        if row["degree"] != n:
            raise ValueError("wrong signed fold degree")
        result["chi"].append(L.LP.restore(row["chi"]))
    for field in LEADING:
        head=stages["leading-complete-"+field]
        coeff=L.unpack_series(head["coefficients"])
        if head["name"] != field or len(coeff) != 9:
            raise ValueError("incomplete signed leading prefix")
        for n in range(9,15):
            row=stages["leading-%s-degree-%03d" % (field,n)]
            if row["degree"]!=n or row["name"]!="leading-"+field:
                raise ValueError("wrong signed leading degree")
            coeff.append(L.LP.restore(row["coefficient"]))
        result[field]=coeff
    for n in range(13):
        row=stages["first-correction-degree-%03d" % n]
        if row["degree"]!=n:
            raise ValueError("wrong signed first correction degree")
        for field,key in (("w1a","a1"),("w1b","b1")):
            result[field].append(L.LP.restore(row[key]))
    return result


def cauchy_tail(majorant, rho, first, radial, angular):
    """Uniform real-angle mixed derivative tail on the old product of disks."""
    bound, radius, strip=majorant
    radius, strip=L.ex(Fraction(radius)), L.ex(Fraction(strip))
    if min(radial,angular)<0 or first<=radial or not rho.lower()>=0:
        raise ValueError("invalid root mixed order or inward coordinate")
    t=abs(rho).upper()/radius
    if not (t<1 and strip>0):
        raise ValueError("outside the genuine root product")
    total=arb(0)
    for k in range(radial+1):
        falling=factorial(first)//factorial(first-k)
        total += (comb(radial,k)*falling*t**(first-k)*factorial(radial-k)
                  /(1-t)**(radial-k+1))
    return (bound * total/radius**radial * factorial(angular)/strip**angular).upper()


def radial_laurent(series, rho, radial):
    """Horner sum of the complete polynomial differentiated in inward rho."""
    if not 0 <= radial < len(series):
        raise ValueError("missing original radial order")
    value=L.LP.zero()
    for n in range(len(series)-1,radial-1,-1):
        value=value.scale(rho)+series[n].scale(factorial(n)//factorial(n-radial))
    return value


def root_mesh(series,majorant,rho,count,max_angular):
    """Node and full centered-bin angular derivatives through max_angular.

    Period pi/2. All finite modes, including aliases, are added with their
    original sign to their exact node DFT bucket. In-cell continuation is
    by Taylor's formula on the real angular segment, never by treating the
    DFT interpolant as a bandwidth assertion for the true root solution.
    """
    if count<2 or count & (count-1) or max_angular<0:
        raise ValueError("invalid complete root mesh")
    poly=radial_laurent(series,rho,0)
    point=[]
    for q in range(max_angular+4):
        folded=[acb(0) for _ in range(count)]
        for j,z in enumerate(poly.c,poly.lo):
            folded[j%count]+=z
        error=cauchy_tail(majorant,rho,len(series),0,q)
        full_error=acb(arb(0,error),arb(0,error))
        point.append([count*z+full_error for z in acb.dft(folded,inverse=True)])
        poly=poly.theta()
    half=arb.pi()/(4*count)
    next_bound=(sum((abs(z) for z in poly.c),arb(0))
                +cauchy_tail(majorant,rho,len(series),0,max_angular+4)).upper()
    full=[]
    # The highest qualified derivative gets its range first. Lower derivatives
    # use its integrated effect through arbitrarily many known signed terms.
    radius=arb(0,half.upper())
    for q in range(max_angular,-1,-1):
        degree=max_angular+3-q
        error=(next_bound*half**(degree+1)/factorial(degree+1)).upper()
        fee=acb(arb(0,error),arb(0,error))
        row=[]
        for j in range(count):
            v=point[-1][j]
            for k in range(degree-1,-1,-1):
                v=point[q+k][j]+radius*v/(k+1)
            row.append(v+fee)
        full.append(row)
    return point[:max_angular+1],list(reversed(full))
