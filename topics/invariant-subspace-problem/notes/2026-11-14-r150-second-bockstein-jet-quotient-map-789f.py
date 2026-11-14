#!/usr/bin/env python3
"""Exact 820 -> 143 -> 39 -> 37 maps for the two genuine Taylor rings.

No old kernel, VQ, normal form, or delta2 calculation is repeated here.
Run once under an external 60-second / 512-MiB limit.
"""
import argparse, gzip, hashlib, importlib.util, json, math, struct, time
from pathlib import Path
from flint import nmod_mat, nmod_poly

P = 31
STATE = '06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf'
READER = '8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2'
FIRST = '71b3ffd524cca40f36ac59fb29694798013987c6153edb0c771420d75780daf8'
SECOND = 'fa9fda1c0176cbf3e8163fcfd26ed11ea4f92947587d3d455859d2b912cb38a4'
FOUR = 'f1f6594b19e844dbc8e387cc7efb822d582b26b9348fb8ab03996e985f94188b'

def sha(b): return hashlib.sha256(b).hexdigest()
def actual(path, expected):
    b = path.read_bytes()
    if path.suffix == '.gz': b = gzip.decompress(b)
    if sha(b) != expected: raise ValueError('input SHA: ' + str(path))
    return b
def zero(M): return M == nmod_mat(M.nrows(), M.ncols(), P)
def identity(n): return nmod_mat([[int(i == j) for j in range(n)] for i in range(n)], P)
def sub(M, ri, ci): return nmod_mat([[int(M[i,j]) for j in ci] for i in ri], P)
def pivots(M):
    R, rank = M.rref()
    return R, [next(j for j in range(M.ncols()) if R[i,j]) for i in range(rank)]
def quotient(M):
    """M has columns spanning a subspace; return its canonical quotient map."""
    R, piv = pivots(M.transpose())
    free = [i for i in range(M.nrows()) if i not in set(piv)]
    Q = nmod_mat(len(free), M.nrows(), P)
    for i, c in enumerate(free):
        Q[i,c] = 1
        for j, pivot in enumerate(piv): Q[i,pivot] = -R[j,c]
    if not zero(Q*M): raise ValueError('quotient identity')
    return Q, piv, free
def evaluate(poly, A):
    I = identity(A.nrows()); result = nmod_mat(A.nrows(), A.ncols(), P)
    for coefficient in reversed([int(poly[i]) for i in range(poly.degree()+1)]):
        result = result*A + coefficient*I
    return result
def block(data, offset, nr, nc):
    return nmod_mat([[data[offset+i*nc+j] for j in range(nc)] for i in range(nr)], P)

def main():
    parser = argparse.ArgumentParser()
    for key in ('notes-root', 'first-system', 'second-system', 'four-system', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    a = parser.parse_args(); started = time.monotonic(); a.out.mkdir(parents=True, exist_ok=True)
    reader = a.notes_root/'2026-11-14-r150-torsion-characteristic-789f.py'
    actual(reader, READER)
    spec = importlib.util.spec_from_file_location('r150_jet_state', reader)
    helper = importlib.util.module_from_spec(spec); spec.loader.exec_module(helper)
    state_file = a.out/'state-input.bin'
    state_file.write_bytes(actual(a.notes_root/'2026-11-14-r150-torsion-state.bin-789f.gz', STATE))
    state = helper.load_state(state_file); state_file.unlink()
    A = nmod_mat(state['matrices']['A'], P); C = nmod_mat(state['matrices']['C'], P)
    K = nmod_mat(state['matrices']['kernelTranspose'], P).transpose()
    J = nmod_mat(state['matrices']['action'], P)
    coords = state['coordinates']; index = {tuple(v): i for i,v in enumerate(coords)}
    if len(index) != 820 or len(state['freeComponents']) != 13: raise ValueError('standard cone dictionary')
    x = nmod_poly([0,1], P); g = (x-1)**3*(x-2)**5
    gc = [int(g[i]) for i in range(9)]
    F = nmod_mat(820,13,P)
    for j,c in enumerate(state['freeComponents']):
        for d in range(8): F[index[c,d],j] = -gc[d]
    Ag = A+F*C
    gAg = evaluate(g,Ag)
    Pi, image_pivots, local_representatives = quotient(gAg)
    if Pi.nrows() != 143 or len(image_pivots) != 677: raise ValueError('full local quotient dimension')
    S = nmod_mat(820,143,P)
    for j,i in enumerate(local_representatives): S[i,j]=1
    J143 = Pi*Ag*S
    if Pi*S != identity(143) or J143*Pi != Pi*Ag or not zero(evaluate(g,J143)):
        raise ValueError('full local quotient action')
    U = Pi*K
    _, torsion_columns = pivots(U)
    if len(torsion_columns) != 39: raise ValueError('local torsion image dimension')
    B = sub(U, range(143), torsion_columns)
    _, torsion_rows = pivots(B.transpose())
    inverse = sub(B,torsion_rows,range(39)).inv()
    L = nmod_mat(39,143,P)
    for i in range(39):
        for j,c in enumerate(torsion_rows): L[i,c] = inverse[i,j]
    if L*B != identity(39): raise ValueError('local torsion left inverse')
    free_rows = [i for i in range(143) if i not in set(torsion_rows)]
    checks = sub(identity(143)-B*L,free_rows,range(143))
    if checks.nrows()!=104 or checks.rank()!=104 or not zero(checks*B): raise ValueError('all104 free checks')
    T = L*U; J39 = L*J143*B
    if B*T != U or B*J39 != J143*B or J39*T != T*J: raise ValueError('faithful39 torsion action')
    first = actual(a.first_system,FIRST)
    if first[:8]!=b'R150FB31' or struct.unpack_from('<7I',first,8)!=(31,315,4,2,9,202,6): raise ValueError('first system')
    W = block(first,36+4*16+2*8+315*4,315,2)
    second = actual(a.second_system,SECOND)
    if second[:8]!=b'R150R231' or struct.unpack_from('<5I',second,8)!=(31,820,315,2,9): raise ValueError('second system')
    R = block(second,28+820*9,315,9)
    if W!=block(second,28+820*9+315*9,315,2): raise ValueError('same first beta image')
    four = actual(a.four_system,FOUR)
    if four[:8]!=b'R150D2S1' or struct.unpack_from('<5I',four,8)!=(31,315,4,6,9): raise ValueError('actual four system')
    D = block(four,28+6*4,315,4)
    W39,R39,D39 = T*W,T*R,T*D
    Q37, Wpiv, Wfree = quotient(W39)
    if Q37.nrows()!=37 or W39.rank()!=2: raise ValueError('whole first beta quotient')
    S37=nmod_mat(39,37,P)
    for j,i in enumerate(Wfree): S37[i,j]=1
    J37=Q37*J39*S37
    if J37*Q37 != Q37*J39: raise ValueError('37 quotient action')
    minimum=J.minpoly(); other,remainder=divmod(minimum,g)
    if remainder: raise ValueError('true minimum polynomial contains g')
    gcd,u,_=other.xgcd(g)
    if gcd!=nmod_poly([1],P): raise ValueError('primary coprime decomposition')
    projector=other*u
    projector %= minimum
    PJ=evaluate(projector,J)
    if PJ*PJ!=PJ or PJ*R!=R or PJ*W!=W or T*PJ!=T or PJ.rank()!=39:
        raise ValueError('actual global primary projector')
    evaluate_matrix=nmod_mat([[math.comb(d,k)*pow(root,d-k,P)%P if d>=k else 0
                              for d in range(8)] for root,length in ((1,3),(2,5))
                             for k in range(length)],P)
    crt=evaluate_matrix.inv()
    packed=bytearray(b'R150JQ31')+struct.pack('<7I',31,820,143,39,37,104,8)
    matrices={}
    for name,M in [('Pi',Pi),('J143',J143),('torsionEmbedding',B),('torsionCoordinates',L),
                   ('freeChecks',checks),('globalTorsionTo39',T),('J39',J39),('W39',W39),
                   ('R39',R39),('D39',D39),('Q37',Q37),('J37',J37),('CRT',crt)]:
        offset=len(packed); payload=bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
        packed.extend(payload); matrices[name]={'offset':offset,'rows':M.nrows(),'columns':M.ncols(),'sha256':sha(payload)}
    output=a.out/'jet-quotient-map.bin'; output.write_bytes(packed)
    result={'format':'r150-exact-two-Taylor-ring-quotient-map-v1','status':'completed','prime':31,
            'sourceSHA256':sha(Path(__file__).read_bytes()),'stateSHA256':STATE,'readerSHA256':READER,
            'firstSystemSHA256':FIRST,'secondSystemSHA256':SECOND,'fourSystemSHA256':FOUR,
            'modulusAscending':gc,'TaylorRings':[{'root':1,'length':3},{'root':2,'length':5}],
            'originalStandardSpaceDimension':820,'gAgRank':677,'localQuotientDimension':143,
            'localFreeDimension':104,'localTorsionDimension':39,'quotientByWholeFirstBetaDimension':37,
            'allFullModuleAndActionIdentitiesVerified':True,'all104FreeTestsRetained':True,
            'globalPrimaryProjectorAscending':[int(projector[i]) for i in range(projector.degree()+1)],
            'globalPrimaryProjectorDegree':projector.degree(),'globalPrimaryProjectorRank':39,
            'globalR2ExactlyInPrimarySpace':True,'standardCoordinates':coords,
            'freeComponents':state['freeComponents'],'localRepresentatives':local_representatives,
            'torsionSelectedGlobalColumns':torsion_columns,'torsionSelectedLocalRows':torsion_rows,
            'freeTestLocalRows':free_rows,'wholeFirstBetaPivots':Wpiv,'matrices':matrices,
            'output':{'file':output.name,'bytes':len(packed),'sha256':sha(packed)},
            'elapsedSeconds':time.monotonic()-started,'new198DirectionsComputed':False,
            'finite_budget_verified':False,'fullOriginalMod29791IdentityVerified':False}
    (a.out/'jet-quotient-map-receipt.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','gAgRank','localQuotientDimension','localFreeDimension','localTorsionDimension','quotientByWholeFirstBetaDimension','globalPrimaryProjectorDegree','elapsedSeconds')}),flush=True)

if __name__=='__main__': main()
