#!/usr/bin/env python3
"""Independent bounded weighted module division, with literal row shifts.

Author: Astra-ISP-789f / literature_audit, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
No Singular reduction or standard-basis attribute is trusted by this file.
The only accepted arithmetic is F127, twelve parameter variables of weights
(1^6,2^6), ten row shifts (0,2^5,4^4), and homogeneous degrees at most ten.
All binary vectors remain temporary mathematical data, never Git artifacts.
"""
from __future__ import annotations
import functools,gzip,hashlib,heapq,json,os,re,struct
from collections import OrderedDict
from pathlib import Path

P=127
VARIABLE_WEIGHTS=(1,)*6+(2,)*6
ROW_WEIGHTS=(0,)+(2,)*5+(4,)*4
NAMES=tuple('y%d'%i for i in range(6))+tuple('w%d'%i for i in range(6))+('zz',)
MAX_DEGREE=10
EXPMASK=(1<<64)-16
FLAGS=sum(16<<(4+5*i) for i in range(12))
MAGIC=b'R15ZGV01'
MAX_VECTOR_BYTES=96+9*77276

def need(v,message):
    if not v:raise ValueError(message)

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')
def sha(b):return hashlib.sha256(b).hexdigest()

def identity(path):
    path=Path(path);h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return {'path':path.name,'bytes':path.stat().st_size,'sha256':h.hexdigest()}

def exact(path,desc):
    got=identity(path)
    need(got['bytes']==desc['bytes'] and got['sha256']==desc['sha256'],'complete exact vector file '+Path(path).name)
    return got

def atomic(path,body):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp');tmp.write_bytes(body);os.replace(tmp,path)

def position(component,exponents):
    need(type(component) is int and 0<=component<10 and len(exponents)==12,'literal shifted module position')
    need(all(type(e) is int and 0<=e<=10 for e in exponents),'bounded actual exponents')
    return component+sum(e<<(4+5*i) for i,e in enumerate(exponents))

def exponents(code):return tuple((code>>(4+5*i))&31 for i in range(12))

def degree(code):
    component=code&15
    need(component<10 and 0<=code<1<<64,'literal packed component and exponent width')
    ee=exponents(code)
    need(all(e<=10 for e in ee),'literal packed exponent range')
    return ROW_WEIGHTS[component]+sum(w*e for w,e in zip(VARIABLE_WEIGHTS,ee))

def order_key(code):
    # All comparisons are within one homogeneous vector.  This is exactly
    # wp(1^6,2^6,1),C on x^e*zz^ROW_WEIGHTS[component]*gen(component+1):
    # first reverse-lex zz, then e_11,...,e_0, then ascending component.
    return ((31-ROW_WEIGHTS[code&15])<<64)+((~code)&EXPMASK)+(code&15)

def divides(lead,term):
    if (lead&15)!=(term&15):return False
    return ((((term&EXPMASK)|FLAGS)-(lead&EXPMASK))&FLAGS)==FLAGS

def lcm_position(a,b):
    need((a&15)==(b&15),'S-pair has the same leading component')
    return position(a&15,tuple(max(x,y) for x,y in zip(exponents(a),exponents(b))))

def normalized_terms(terms,weight,normalize=False):
    need(type(weight) is int and 0<=weight<=10,'explicit homogeneous weight')
    answer={}
    for code,c in terms:
        need(type(code) is int and type(c) is int and 0<c<P and code not in answer,'canonical nonzero sparse vector coordinate')
        need(degree(code)==weight,'every original vector term has the declared shifted weight')
        answer[code]=c
    if not answer:return (),None,0
    lead=max(answer,key=order_key);lc=answer[lead]
    if normalize:
        inv=pow(lc,-1,P);answer={t:c*inv%P for t,c in answer.items()};lc=1
    return tuple(sorted(answer.items())),lead,lc

def write_vector(path,terms,weight,binding,normalize=False):
    need(re.fullmatch('[0-9a-f]{64}',binding) is not None,'literal child binding')
    terms,lead,lc=normalized_terms(terms,weight,normalize)
    raw=bytearray(MAGIC+struct.pack('<4I',1,10,12,weight)+binding.encode('ascii')+struct.pack('<Q',len(terms)))
    for code,c in terms:raw.extend(struct.pack('<QB',code,c))
    need(len(raw)==96+9*len(terms)<=MAX_VECTOR_BYTES,'one complete vector obeys its exact homogeneous monomial bound')
    packed=gzip.compress(bytes(raw),compresslevel=1,mtime=0);atomic(path,packed)
    return {**identity(path),'logicalBytes':len(raw),'logicalSha256':sha(raw),'degree':weight,'terms':len(terms),'leadCode':lead,'leadCoefficient':lc}

def read_vector(path,desc,binding):
    exact(path,desc)
    need(0<desc['bytes']<=MAX_VECTOR_BYTES+4096 and 96<=desc['logicalBytes']<=MAX_VECTOR_BYTES,'bounded complete sparse vector')
    raw=gzip.decompress(Path(path).read_bytes())
    need(len(raw)==desc['logicalBytes'] and sha(raw)==desc['logicalSha256'],'whole decoded vector hash')
    need(raw[:8]==MAGIC and struct.unpack_from('<3I',raw,8)==(1,10,12) and raw[24:88].decode('ascii')==binding,'same vector protocol and mathematical binding')
    weight=struct.unpack_from('<I',raw,20)[0];count=struct.unpack_from('<Q',raw,88)[0]
    need(weight==desc['degree'] and count==desc['terms'] and len(raw)==96+9*count,'whole vector shape and EOF')
    terms=tuple(struct.unpack_from('<QB',raw,96+9*i) for i in range(count))
    actual,lead,lc=normalized_terms(terms,weight)
    need(actual==terms and lead==desc['leadCode'] and lc==desc['leadCoefficient'],'every vector coordinate and leading term')
    return terms

def from_model_vector(vector):
    need(len(vector)==10,'all ten original coordinates')
    terms=[]
    for component,f in enumerate(vector):
        for ee,c in f.to_dict().items():
            need(len(ee)==17 and not any(ee[12:]),'all twelve original parameters, no moment variable')
            terms.append((position(component,tuple(map(int,ee[:12]))),int(c)))
    return terms

def parse_polynomial(path,names=NAMES,max_bytes=16777216):
    path=Path(path);need(path.stat().st_size<=max_bytes,'bounded complete exported polynomial text')
    text=''.join(path.read_text('ascii').split())
    if text=='0':return {}
    tokens=re.findall(r'[+-]?[^+-]+',text)
    need(text and ''.join(tokens)==text,'entire expanded polynomial token coverage')
    indices={name:i for i,name in enumerate(names)};out={}
    for token in tokens:
        c=1
        if token[0] in '+-':
            if token[0]=='-':c=-1
            token=token[1:]
        need(token,'nonempty signed monomial');ee=[0]*len(names)
        for factor in token.split('*'):
            if factor.isdigit():c=c*int(factor)%P;continue
            bits=factor.split('^')
            need(1<=len(bits)<=2 and bits[0] in indices and (len(bits)==1 or bits[1].isdigit()),'only declared polynomial variables and nonnegative powers')
            ee[indices[bits[0]]]+=1 if len(bits)==1 else int(bits[1])
        ee=tuple(ee);out[ee]=(out.get(ee,0)+c)%P
    return {e:c for e,c in out.items() if c}

def shifted_text_vector(paths):
    need(len(paths)==10,'ten complete exported coordinate texts')
    terms=[];weights=set()
    for component,path in enumerate(paths):
        for ee,c in parse_polynomial(path).items():
            need(ee[-1]==ROW_WEIGHTS[component],'candidate preserves the exact coordinate zz exponent')
            code=position(component,ee[:12]);weights.add(degree(code));terms.append((code,c))
    need(len(weights)<=1 and (not weights or max(weights)<=10),'whole candidate column is homogeneous of weight at most ten')
    return terms,next(iter(weights),0)

class Divider:
    """Full ordinary sparse division independent of the candidate producer."""
    def __init__(self,catalog,loader,tick=lambda:None,cache_size=12):
        self.catalog=catalog;self.loader=loader;self.tick=tick;self.cache=OrderedDict();self.cache_size=cache_size
        self.by_component=[[] for unused in range(10)]
        for i,desc in enumerate(catalog):
            need(desc['terms']>0 and desc['leadCode'] is not None and 0<desc['leadCoefficient']<P,'nonzero complete candidate basis column')
            self.by_component[desc['leadCode']&15].append(i)
        for bucket in self.by_component:bucket.sort(key=lambda i:order_key(catalog[i]['leadCode']),reverse=True)
        self.reducer=functools.lru_cache(maxsize=65536)(self._reducer)
        self.total_reductions=0;self.total_term_updates=0

    def vector(self,i):
        if i in self.cache:
            ans=self.cache.pop(i);self.cache[i]=ans;return ans
        ans=self.loader(i);self.cache[i]=ans
        while len(self.cache)>self.cache_size:self.cache.popitem(last=False)
        return ans

    def _reducer(self,code):
        for i in self.by_component[code&15]:
            if divides(self.catalog[i]['leadCode'],code):return i
        return None

    def normal_form(self,terms,weight):
        source,unused,unusedlc=normalized_terms(terms,weight)
        pending=dict(source);queue=[(-order_key(t),t) for t in pending];heapq.heapify(queue)
        remainder={};steps=updates=0;start_reductions=self.total_reductions
        while queue:
            neg,term=heapq.heappop(queue)
            if term not in pending:continue
            need(-neg==order_key(term),'unchanged exact leading priority')
            coeff=pending[term];j=self.reducer(term)
            if j is None:
                remainder[term]=coeff;del pending[term];continue
            desc=self.catalog[j];lead=desc['leadCode'];shift=(term&EXPMASK)-(lead&EXPMASK)
            scale=coeff*pow(desc['leadCoefficient'],-1,P)%P
            for code,c in self.vector(j):
                new=code+shift
                need(degree(new)==weight and order_key(new)<=-neg,'complete homogeneous leading-term reduction, with no hidden zz multiplier')
                val=(pending.get(new,0)-scale*c)%P
                if val:
                    if new not in pending:heapq.heappush(queue,(-order_key(new),new))
                    pending[new]=val
                else:pending.pop(new,None)
                updates+=1
            need(term not in pending,'actual leading coefficient cancelled exactly')
            steps+=1
            if steps%64==0:self.tick()
            if len(queue)>4*len(pending)+10000:
                queue=[(-order_key(t),t) for t in pending];heapq.heapify(queue)
        need(not pending and all(self.reducer(t) is None for t in remainder),'complete irreducible remainder, not a leading-prefix computation')
        self.total_reductions=start_reductions+steps;self.total_term_updates+=updates
        return tuple(sorted(remainder.items())),{'reductions':steps,'ordinaryTermUpdates':updates,'remainderTerms':len(remainder)}

    def pair(self,i,j):
        a=self.catalog[i];b=self.catalog[j]
        if (a['leadCode']&15)!=(b['leadCode']&15):return None
        lcm=lcm_position(a['leadCode'],b['leadCode']);weight=degree(lcm)
        if weight>10:return None
        ans={}
        for k,sign in ((i,1),(j,-1)):
            desc=self.catalog[k];shift=(lcm&EXPMASK)-(desc['leadCode']&EXPMASK)
            scale=sign*pow(desc['leadCoefficient'],-1,P)%P
            for code,c in self.vector(k):
                new=code+shift;val=(ans.get(new,0)+scale*c)%P
                if val:ans[new]=val
                else:ans.pop(new,None)
        need(lcm not in ans and all(degree(t)==weight and order_key(t)<order_key(lcm) for t in ans),'literal complete homogeneous S-pair with strict leading cancellation')
        return tuple(sorted(ans.items())),weight,lcm

def selftest():
    # Compare the packed order with the literal weighted reverse-lex definition
    # on all twelve one-variable axes and each of the ten component shifts.
    by_degree={}
    for component in range(10):
        for axis,w in enumerate(VARIABLE_WEIGHTS):
            for k in range((10-ROW_WEIGHTS[component])//w+1):
                ee=[0]*12;ee[axis]=k;t=position(component,tuple(ee))
                by_degree.setdefault(degree(t),set()).add(t)
    for terms in by_degree.values():
        literal=lambda t:tuple(-x for x in reversed(exponents(t)+(ROW_WEIGHTS[t&15],)))+(t&15,)
        need(sorted(terms,key=order_key)==sorted(terms,key=literal),'packed order equals the literal shifted wp,C order')
    for axis in range(12):
        for a in range(11):
            for b in range(11):
                ea=[0]*12;eb=[0]*12;ea[axis]=a;eb[axis]=b
                need(divides(position(0,tuple(ea)),position(0,tuple(eb)))==(a<=b),'every packed exponent lane has exact divisibility')
    e0=[0]*12;e0[0]=2;e1=[0]*12;e1[0]=e1[1]=1
    y1=[0]*12;y1[1]=1
    g1=((position(0,tuple(e0)),1),(position(1,(0,)*12),1))
    g2=((position(0,tuple(e1)),1),)
    g3=((position(1,tuple(y1)),1),)
    vectors=[normalized_terms(g1,2)[0],normalized_terms(g2,2)[0],normalized_terms(g3,3)[0]]
    catalog=[]
    for v,w in zip(vectors,(2,2,3)):
        vv,l,c=normalized_terms(v,w);catalog.append({'terms':len(vv),'degree':w,'leadCode':l,'leadCoefficient':c})
    d=Divider(catalog,lambda i:vectors[i])
    pair=d.pair(0,1);need(pair is not None and pair[1]==3,'tiny weighted S-pair degree')
    need(d.normal_form(pair[0],pair[1])[0]==(),'tiny completed S-pair vanishes')
    need(d.normal_form(g3,3)[0]==(),'tiny positive module target')
    need(d.normal_form(((position(1,(0,)*12),1),),2)[0]!=(),'tiny nonzero normal form')
    bad=Divider(catalog[:2],lambda i:vectors[i])
    need(bad.normal_form(pair[0],pair[1])[0]!=(),'incomplete candidate is detected by its omitted S-pair')
    # Independent integer-coordinate identity: y1*g1-y0*g2 = g3.
    s0=position(0,tuple(y1));x0=[0]*12;x0[0]=1;s1=position(0,tuple(x0))
    lhs={}
    for v,shift,sign in ((g1,s0,1),(g2,s1,-1)):
        for t,c in v:
            t+=shift;lhs[t]=(lhs.get(t,0)+sign*c)%P
    need({t:c for t,c in lhs.items() if c}==dict(g3),'independent exact tiny source relation')
    return {'weightedOrder':True,'allTwelvePackedDivisibilityLanes':True,'positiveControl':True,'negativeControl':True,'missingSPairDetected':True,'literalSourceProduct':True}

if __name__=='__main__':print(canon(selftest()).decode('ascii'))
