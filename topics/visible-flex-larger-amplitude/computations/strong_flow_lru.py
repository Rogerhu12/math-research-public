"""Optional bounded reuse of identical geometric Flow constructions.

This stores actual Flow objects, not numerical derivatives or trial states.
Keys include the complete physical config and port, every constructor scalar
and keyword, bridge identity, reference coefficients/frequencies, numerical
reference knots, and the live chart context supplied by the class factory.
The source constructor and immutable bridge objects must not be monkeypatched
inside a running solve. Unserializable physical data bypass the cache.
"""
from collections import OrderedDict
import json,time

def _json(value):
    def convert(item):
        if hasattr(item,'tolist'):return item.tolist()
        raise TypeError('Not a serializable physical constructor field')
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False,default=convert)

class FlowCache:
    def __init__(self,obj,size,context=None):
        if not 1<=int(size)<=32:raise ValueError('Flow cache size must be between 1 and 32')
        self.obj,self.size,self.context=obj,int(size),context
        self.constructor=obj.Flow;self.entries=OrderedDict()
        self.stats=dict(hits=0,misses=0,bypassed=0,evictions=0,maximum_entries=0,
                        constructor_cpu_seconds=0.,constructor_wall_seconds=0.)

    def key(self,args,kwargs):
        if len(args)<2:raise TypeError('Expected physical config and port')
        # The seventh positional input is the same immutable bridge object
        # passed by DualBVP.flow. All preceding inputs are physical scalars.
        scalars=args[2:6];objects=args[6:]
        obj=self.obj
        payload=dict(physical=args[0],port=args[1],constructor_scalars=scalars,
            keyword_arguments=kwargs,reference_coefficients=obj.ref_coeff,
            reference_frequencies=getattr(obj,'ref_frequencies',[2,4]),
            numerical_reference_knots=getattr(obj,'_neck_knots',None),
            class_chart_context=self.context)
        return (_json(payload),tuple((type(z).__module__,type(z).__qualname__,id(z)) for z in objects))

    def __call__(self,*args,**kwargs):
        try:key=self.key(args,kwargs)
        except (TypeError,ValueError):
            self.stats['bypassed']+=1
            return self.constructor(*args,**kwargs)
        if key in self.entries:
            self.stats['hits']+=1
            value=self.entries.pop(key);self.entries[key]=value;return value
        self.stats['misses']+=1;wall=time.perf_counter();cpu=time.process_time()
        value=self.constructor(*args,**kwargs)
        self.stats['constructor_wall_seconds']+=time.perf_counter()-wall
        self.stats['constructor_cpu_seconds']+=time.process_time()-cpu
        self.entries[key]=value
        if len(self.entries)>self.size:
            self.entries.popitem(last=False);self.stats['evictions']+=1
        self.stats['maximum_entries']=max(self.stats['maximum_entries'],len(self.entries))
        return value

def install_instance(obj,size,context=None):
    if hasattr(obj,'_strong_geometric_flow_cache'):raise ValueError('Flow cache is already installed')
    cache=FlowCache(obj,size,context);obj.Flow=cache;obj._strong_geometric_flow_cache=cache
    return cache

def install_class(cls,size,context=None,on_install=None):
    original=cls.__init__
    def initialize(self,*args,**kwargs):
        original(self,*args,**kwargs)
        cache=install_instance(self,size,context)
        if on_install is not None:on_install(cache)
    cls.__init__=initialize
    return cls
