#!/usr/bin/env python3
"""NEW exact support/factors of the ORIGINAL H1 Dixon source poles.
Read the immutable ef9 source only up to its completed original Dixon8
construction (previous actual 5.10 seconds). Do NOT run any Gaussian
pivot, target solve, final coefficient reconstruction, or old F6 gate.
The resulting paid source support divides the already proved C256.
Its exact QQ factors are a new input for the retained original fibers.
Print definitions/degrees/SHAs and genuinely small polynomial formulas
only: no encoded, split, or full recomputable polynomial payload.
2026-11-28 Asia/Taipei. One original input, 120 seconds / 1 GiB.
"""
import os,time,json,hashlib,signal,resource
from pathlib import Path
NEW_SOURCE_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
BASE_NAME="2026-11-28-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-syntax-fix-8542.py"
BASE_SHA="ef9e285512e1eddcbac0512f853f0b2ac58b57546f9a4bfa7e5621a9eaf8ddcc"
base=Path(os.environ.get("ISP_H1_DIXON_SOURCE",str(Path(__file__).with_name(BASE_NAME))))
raw=base.read_bytes()
assert hashlib.sha256(raw).hexdigest()==BASE_SHA
text=raw.decode()
marker="# All Gaussian rational parameter poles may cancel."
assert text.count(marker)==1
prefix=text.split(marker,1)[0]
assert "source_cover=cover" in prefix
assert "def add_column" not in prefix and "success=None" not in prefix
# The supplied historical loader places the two exact old input files
# beside BASE_NAME. They are read only inside this bounded Actions run.
ns={"__file__":str(base),"__name__":"__isp_original_dixon_prefix__"}
exec(compile(prefix,str(base)+"::<original-prefix-only>","exec"),ns)
pol,one,up=ns["pol"],ns["one"],ns["up"]
exact,monic,pdigest,coefficients=(
 ns["exact"],ns["monic"],ns["pdigest"],ns["coefficients"])
say=ns["say"]
source_cover=ns["source_cover"]
derivative_gcd=source_cover.gcd(source_cover.derivative())
support=monic(exact(source_cover,derivative_gcd))
assert monic(support*derivative_gcd)==source_cover
assert support.gcd(support.derivative()).degree()==0
removed=[]
for label,p in [("already paid u",up),("already paid u-1",up-1)]:
 gg=support.gcd(p)
 if gg.degree()>0:
  old=support;support=monic(exact(support,gg))
  assert monic(support*gg)==old
  removed.append({"originalUnit":label,"degree":int(gg.degree())})
assert support.degree()<=256
say("new_original_Dixon_source_pole_support",
 originalSourceLCM=pdigest(source_cover),
 exactPaidSourceSupport=pdigest(support),
 onlyRemovedOriginalUnits=removed,
 exactSourceSupportDividesPreviouslyProvedC256=True,
 previouslyProvedFullCoverDegree=256,
 fullC256IdentifiedByDivisibilityAndEqualDegree=(support.degree()==256),
 unidentifiedFinalCoefficientSupportDegreeAtMost=256-int(support.degree()),
 noOldGaussianOrTargetReplay=True)
if support.degree()==256:
 assert pdigest(support)["sha256"]=="4d1acbe8d27ede6154ef4a25b363d02982c22ae46426943881843661694607a3"
unit,factors=support.factor()
reconstructed=pol(unit)
for p,m in factors:
 reconstructed*=p**int(m)
assert reconstructed==support
factor_rows=[]
normalized_product=one
for p,m0 in factors:
 m0=int(m0);assert m0==1
 p=monic(p);normalized_product*=p
 dd=pdigest(p)
 row={"degree":int(p.degree()),"multiplicity":m0,
      "exactCoefficientIdentity":dd,
      "definition":"the monic QQ factor with this digest of the source-defined paid support"}
 # A small exact formula is a parameter definition, never a data dump.
 small=str(p)
 if p.degree()<=8 and len(small)<=400:row["smallParameterFormula"]=small
 factor_rows.append(row)
assert monic(normalized_product)==support
factor_rows.sort(key=lambda x:(x["degree"],x["exactCoefficientIdentity"]["sha256"]))
say("new_original_Dixon_source_support_complete_QQ_factorization",
 factors=factor_rows,numberOfFactors=len(factor_rows),
 degreeSum=sum(x["degree"] for x in factor_rows),
 completeUnnormalizedFactorProductReturned=True,
 completeMonicFactorProductReturned=True,
 noFactorCalledOriginalUnitWithoutSeparateOriginalReturn=True,
 allWholeQQuarticRootFibersRemain=True,
 fullH1Excluded=False,ordinaryISPClaim=False)
say("new_H1_source_pole_support_input_finished",
 sourceSHA256=NEW_SOURCE_SHA,originalFullSourceSHA256=BASE_SHA,
 originalPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 recomputableCoefficientPayloadTransmitted=False,
 encodedOrSplitPayloadCreated=False,
 existing1024BoundUnchangedUnlessSeparateOriginalExclusionReturned=True)
signal.alarm(0)
