#!/usr/bin/env python3
"""Complete first image of the actual seven-column integer enlargement.

The original full polynomial kernel contributes zero after quotienting U.
All315 torsion coordinates and all505 free observations are retained first.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
from flint import nmod_mat
READER_SHA="8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
STATE_SHA="06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
SELECTOR_SHA="2d90d72ac72cc63e5531b80a6e788ef82c6bf794481b53546b27b0afcb7134ee"
LABELS=list(range(7001,7008))+list(range(2,11))
def sha(b):return hashlib.sha256(b).hexdigest()
def actual(path,expected):
    data=path.read_bytes()
    if path.suffix==".gz":data=gzip.decompress(data)
    if sha(data)!=expected:raise ValueError("frozen input SHA "+str(path))
    return data
def matrix(data,offset,rows,cols):
    body=data[offset:offset+rows*cols]
    if len(body)!=rows*cols or any(x>30 for x in body):raise ValueError("actual matrix dimensions/field")
    return nmod_mat([list(body[i*cols:(i+1)*cols]) for i in range(rows)],31)
def sub(M,rows,cols):
    rows,cols=list(rows),list(cols)
    answer=nmod_mat(len(rows),len(cols),31)
    for i,r in enumerate(rows):
        for j,c in enumerate(cols):answer[i,j]=M[r,c]
    return answer
def join(*items):
    return nmod_mat([[int(M[i,j]) for M in items for j in range(M.ncols())] for i in range(items[0].nrows())],31)
def serial(M):return bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def pivots(M):
    reduced,rank=M.rref()
    return [next(j for j in range(M.ncols()) if reduced[i,j]) for i in range(rank)]
def nonzero_by_column(M):
    return [sum(bool(M[i,j]) for i in range(M.nrows())) for j in range(M.ncols())]
def main():
    p=argparse.ArgumentParser()
    for key in ("notes-root","selector","image-remainders","image-metadata","original-metadata","out"):
        p.add_argument("--"+key,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
    original=json.loads(a.original_metadata.read_text());im=json.loads(a.image_metadata.read_text())
    if original.get("status")!="completed" or original.get("modulus")!=923521 or original.get("divisor")!=29791 or original.get("targetCount")!=16 or not original.get("allOriginalProductCoefficientsDivisible") or not original.get("originalRowScaleTransportVerified"):
        raise ValueError("all16 actual original seventeen divisibilities required")
    if im.get("status")!="completed" or im.get("targets")!=16 or not im.get("fullImageQuotientIdentity") or not im.get("everyRemainderIsIrreducible"):
        raise ValueError("complete actual16 G quotients/remainders required")
    reader=a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py"
    actual(reader,READER_SHA)
    spec=importlib.util.spec_from_file_location("r150_seven_actual_torsion_reader",reader)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    state_path=a.out/"same-state-input.bin"
    state_path.write_bytes(actual(a.notes_root/"2026-11-14-r150-torsion-state.bin-789f.gz",STATE_SHA))
    state=helper.load_state(state_path);state_path.unlink()
    selector=actual(a.selector,SELECTOR_SHA)
    if selector[:8]!=b"R150PHS1" or struct.unpack_from("<5I",selector,8)!=(31,315,15,7,9):
        raise ValueError("same seven original divided-source basis")
    U=matrix(selector,7723,315,7);J7=matrix(selector,9991,7,7)
    J=nmod_mat(state["matrices"]["action"],31)
    if U.rank()!=7 or J*U!=U*J7:raise ValueError("same global seven-source invariant submodule")
    pivot=pivots(U.transpose())
    if len(pivot)!=7:raise ValueError("seven quotient coordinate pivots")
    free=[i for i in range(315) if i not in set(pivot)]
    Ui=sub(U,pivot,range(7)).inv();Uf=sub(U,free,range(7))
    Jp=sub(J,free,free)-Uf*Ui*sub(J,pivot,free)
    def project(M):return sub(M,free,range(M.ncols()))-Uf*Ui*sub(M,pivot,range(M.ncols()))
    if project(J*U)!=nmod_mat(308,7,31):raise ValueError("full invariant quotient")
    data=a.image_remainders.read_bytes();wide=data[:8]==b"R150NX31"
    if (not wide and data[:8]!=b"R150NF31") or struct.unpack_from("<3I",data,8)!=(0,16,1034):
        raise ValueError("same actual16 complete G remainders")
    index={tuple(c):i for i,c in enumerate(state["coordinates"])}
    V=nmod_mat(820,16,31);offset=20
    for target in range(16):
        raw,label,count=struct.unpack_from("<IHI",data,offset);offset+=10
        if raw or label!=LABELS[target]:raise ValueError("actual new relation and original h0 labels")
        previous=0
        for _ in range(count):
            component=struct.unpack_from("<H",data,offset)[0];offset+=2
            size=2 if wide else 1
            length=int.from_bytes(data[offset:offset+size],"little");offset+=size
            if component<=previous or component>1034 or not length:raise ValueError("actual reduced polynomial dictionary")
            previous=component
            for degree in range(length):
                value=data[offset];offset+=1
                if value>30:raise ValueError("actual residue field")
                if value:
                    if (component,degree) not in index:raise ValueError("actual16 remainder has a high free term")
                    V[index[component,degree],target]=value
    if offset!=len(data):raise ValueError("complete16 remainder tail")
    coordinates=[i for i in range(820) if i+1 not in set(state["pivotStateCoordinates"])]
    D=sub(V,coordinates,range(16))
    K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
    O=nmod_mat(state["observabilityEchelon"],31)
    if K*D!=V or O*V!=nmod_mat(505,16,31):
        raise ValueError("all505 original free observations and315 reconstruction")
    quotient=project(D);beta=sub(quotient,range(308),range(7))
    target=sub(quotient,range(308),range(7,16))
    current=beta;fullcurrent=sub(D,range(315),range(7))
    columns=current;fullcolumns=fullcurrent;previous_rank=-1;stable=False
    for degree in range(309):
        independent=pivots(columns);rank=len(independent)
        print(json.dumps({"phase":"complete-augmented-first-krylov","maximumPower":degree,"columns":columns.ncols(),"rank":rank,"elapsedSeconds":time.monotonic()-start}),flush=True)
        if rank==previous_rank or rank==308:
            stable=True
            break
        previous_rank=rank
        current=Jp*current;fullcurrent=J*fullcurrent
        columns=join(columns,current);fullcolumns=join(fullcolumns,fullcurrent)
    if not stable:raise ValueError("complete308 finite Krylov closure not reached")
    basis=sub(columns,range(308),independent)
    source_basis=sub(fullcolumns,range(315),independent)
    basis_rows=pivots(basis.transpose())
    if rank:
        inverse=sub(basis,basis_rows,range(rank)).inv()
        F=inverse*sub(target,basis_rows,range(9))
        action=inverse*sub(Jp*basis,basis_rows,range(rank))
    else:
        inverse=nmod_mat(0,0,31);F=nmod_mat(0,9,31);action=nmod_mat(0,0,31)
    if basis*action!=Jp*basis:raise ValueError("complete new image must be J invariant")
    residual=target-basis*F
    compatible=[count==0 for count in nonzero_by_column(residual)]
    solution=[[[] for _ in range(9)] for _ in range(7)]
    for row,column in enumerate(independent):
        generator=column%7;power=column//7
        for j in range(9):
            if F[row,j]:
                solution[generator][j]+=[0]*max(0,power+1-len(solution[generator][j]))
                solution[generator][j][power]=int(F[row,j])
    fulltarget=sub(D,range(315),range(7,16))
    difference=fulltarget-source_basis*F
    correction=Ui*sub(difference,pivot,range(9))
    full_residual=difference-U*correction
    if project(full_residual)!=residual:raise ValueError("full315 to308 residual correspondence")
    if any(compatible[j] and any(full_residual[i,j] for i in range(315)) for j in range(9)):
        raise ValueError("compatible target must have full315 actual source reconstruction")
    duals=[]
    for j in range(9):
        if compatible[j]:
            duals.append(None);continue
        row=next(i for i in range(308) if residual[i,j])
        dual=nmod_mat(1,308,31);dual[0,row]=1
        if rank:
            coefficients=sub(basis,[row],range(rank))*inverse
            for i,r in enumerate(basis_rows):dual[0,r]-=coefficients[0,i]
        value=int((dual*target)[0,j]);scale=pow(value,-1,31)
        dual=scale*dual
        if dual*columns!=nmod_mat(1,columns.ncols(),31) or (dual*target)[0,j]!=1:
            raise ValueError("actual full arbitrary-polynomial image dual")
        full_dual=nmod_mat(1,315,31)
        for i,r in enumerate(free):full_dual[0,r]=dual[0,i]
        eliminated=dual*Uf*Ui
        for i,r in enumerate(pivot):full_dual[0,r]-=eliminated[0,i]
        if full_dual*U!=nmod_mat(1,7,31) or full_dual*fullcolumns!=nmod_mat(1,fullcolumns.ncols(),31) or (full_dual*fulltarget)[0,j]!=1:
            raise ValueError("whole315 original source dual")
        duals.append({"target":j+2,"quotientCoordinates308":[int(dual[0,i]) for i in range(308)],
                     "original315Coordinates":[int(full_dual[0,i]) for i in range(315)],
                     "wholeKrylovAnnihilated":True,"UAnnihilated":True,"targetValue":1})
    maximum=max([len(poly)-1 for row in solution for poly in row]+[-1])
    payload=bytearray(b"R150S731")+struct.pack("<8I",31,315,7,308,16,columns.ncols(),rank,9)
    blocks={}
    for name,M in [("oldSevenSources",U),("oldSevenAction",J7),("quotientAction",Jp),("actualAll315NewColumns",D),
                   ("actualQuotientColumns",quotient),("completeKrylov",columns),("full315Krylov",fullcolumns),
                   ("selectedImageBasis",basis),("selectedBasisAction",action),("basisSolution",F),
                   ("oldSevenConstantCorrection",correction),("full315Residual",full_residual)]:
        raw=serial(M);blocks[name]={"offset":len(payload),"rows":M.nrows(),"columns":M.ncols(),"sha256":sha(raw)};payload.extend(raw)
    system=a.out/"complete-augmented-first-image.bin.gz";system.write_bytes(gzip.compress(payload,mtime=0))
    result={"format":"r150-seven-genuine-relations-complete-augmented-first-image-v1","status":"completed","prime":31,
        "newAugmentedFirstImageComplete":True,"originalOldKernelDirectionsPaid":1834,"newRelationDirectionsPaid":7,
        "all16OriginalSeventeenDivisibilitiesVerified":True,"all505FreeObservationsVerified":True,"all315CoordinatesRetained":True,
        "oldSevenUQuotientedExactly":True,"quotientFreeRank":13,"quotientTorsionDimension":308,
        "newGlobalFirstImageRank":rank,"KrylovMaximumPower":degree,"KrylovColumnCount":columns.ncols(),
        "KrylovBasisColumnIndicesZeroBased":independent,"quotientRemovedRowsOneBased":[i+1 for i in pivot],
        "targetLabels":list(range(2,11)),"individualTargetCompatible":compatible,
        "numberOfCompatibleTargets":sum(compatible),"allNineCompatible":all(compatible),
        "newRelationSolutionPolynomialsAscending":solution,
        "oldSevenCorrectionCoefficients":[[int(correction[i,j]) for j in range(9)] for i in range(7)],
        "maximumSolutionDegree":maximum,"completeGlobalDuals":duals,
        "targetScope":"next h0 lift over A+ with mod31 initial(x0,0); not all possible integer or rational initial sources",
        "finiteBudgetVerified":False,"fullOriginalTarget31h0Mod923521IdentityVerified":False,
        "characteristicZeroIdentityAsserted":False,"matrices":blocks,
        "inputs":{"originalMetadataSHA256":sha(a.original_metadata.read_bytes()),"imageMetadataSHA256":sha(a.image_metadata.read_bytes()),
                  "imageRemaindersSHA256":sha(data),"selectorSHA256":SELECTOR_SHA,"stateSHA256":STATE_SHA},
        "system":{"file":system.name,"uncompressedBytes":len(payload),"uncompressedSHA256":sha(payload),
                  "compressedBytes":system.stat().st_size,"compressedSHA256":sha(system.read_bytes())},
        "elapsedSeconds":time.monotonic()-start}
    (a.out/"complete-augmented-first-image-receipt.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["status","newAugmentedFirstImageComplete","newGlobalFirstImageRank",
        "KrylovMaximumPower","allNineCompatible","individualTargetCompatible","maximumSolutionDegree","elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
