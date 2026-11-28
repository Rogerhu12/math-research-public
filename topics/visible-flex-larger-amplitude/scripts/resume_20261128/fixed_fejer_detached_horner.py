"""Runner-local implementation of the original small-argument Rodrigues polynomial.
The owning operator selects this helper only for plain detached unforced closure calls.
No autograd, Jacobian-vector product or forced original reread goes through ctypes.
"""
import ctypes
import hashlib
import math
import os
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile

C_NAME = "fixed_fejer_detached_horner.c"
C_SHA256 = "6dbfbe17c4e535dce61500d9c8da72a088bb377bfba21985f5ef5415cb4e3933"
FLAGS = ("-std=c11", "-O3", "-fPIC", "-shared", "-march=x86-64", "-mfpmath=sse",
         "-msse2", "-fno-fast-math", "-fno-associative-math", "-ffp-contract=off",
         "-fexcess-precision=standard", "-frounding-math")
Pointer = ctypes.POINTER(ctypes.c_double)


def digest(data):
    return hashlib.sha256(data).hexdigest()


class DetachedHorner:
    def __init__(self):
        src = Path(__file__).with_name(C_NAME)
        if digest(src.read_bytes()) != C_SHA256:
            raise ValueError("Complete fixed Rodrigues C source differs from the declared input")
        self.source = src
        self.handle = self.function = self.scratch = None
        self.info = dict(schema="fixed-fejer-whole-detached-horner-v1",
                         c_source_sha256=C_SHA256, binding_python_sha256=digest(Path(__file__).read_bytes()),
                         state="not yet requested", native_calls=0, native_radial_elements=0,
                         element_Horner_updates=0, whole_original_fallback_calls=0,
                         scientific_speedup_measured=False)
        words=[]
        for d in range(3):
            for offset in (1,2):
                for power in range(13):
                    if power < d:
                        words.append(0.)
                    else:
                        factor=math.factorial(power)//math.factorial(power-d)
                        words.append(((-1.)**power)*factor/math.factorial(2*power+offset))
        self.coefficient=(ctypes.c_double*len(words))(*words)
        self.info["native_coefficient_buffer_sha256"]=digest(bytes(self.coefficient))
        self.info["coefficient_hex_rows"]=[[v.hex() for v in words[i:i+13]]
                                          for i in range(0,len(words),13)]

    def build(self):
        if self.info["state"] != "not yet requested":
            return
        if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
            raise RuntimeError("Execute the scientific kernel only on the declared public Actions repository")
        try:
            compiler=shutil.which("gcc")
            if not compiler or platform.machine()!="x86_64":
                raise OSError("Pinned x86-64 GCC arithmetic unavailable")
            compiler=str(Path(compiler).resolve())
            version=subprocess.run([compiler,"--version"],check=True,capture_output=True,text=True).stdout
            target=subprocess.run([compiler,"-dumpmachine"],check=True,capture_output=True,text=True).stdout.strip()
            self.scratch=tempfile.TemporaryDirectory(prefix="fejer-horner-",dir=os.environ.get("RUNNER_TEMP"))
            binary=Path(self.scratch.name)/"fixed_fejer_detached_horner.so"
            argv=[compiler,*FLAGS,str(self.source.resolve()),"-o",str(binary),"-lm"]
            self.info.update(compiler=compiler,compiler_sha256=digest(Path(compiler).read_bytes()),
                             compiler_version=version.strip(), compiler_target=target, compile_argv=argv,
                             machine=platform.machine(),platform=platform.platform(),libc=platform.libc_ver())
            subprocess.run(argv,check=True)
            self.handle=ctypes.CDLL(str(binary))
            self.function=self.handle.fixed_fejer_horner
            self.function.argtypes=[ctypes.c_size_t,ctypes.c_int,Pointer,Pointer,Pointer]
            self.function.restype=None
            self.handle.fixed_fejer_rounding.argtypes=[]
            self.handle.fixed_fejer_rounding.restype=ctypes.c_int
            self.handle.fixed_fejer_mxcsr.argtypes=[]
            self.handle.fixed_fejer_mxcsr.restype=ctypes.c_uint
            raw=binary.read_bytes()
            self.info.update(state="built",binary_bytes=len(raw),binary_sha256=digest(raw),
                             initial_rounding_code=self.handle.fixed_fejer_rounding(),
                             initial_mxcsr=self.handle.fixed_fejer_mxcsr())
        except (OSError,subprocess.CalledProcessError) as exc:
            self.function=None
            self.info.update(state="using complete Torch fallback",compile_error=str(exc))

    def series(self,z,degree):
        import torch
        self.build()
        if self.function is None:
            self.info["whole_original_fallback_calls"]+=1
            return None
        # Metadata/state checks in the owning operator also exclude transforms and duals.
        if (type(z) is not torch.Tensor or z.device.type!="cpu" or z.dtype!=torch.float64 or
                z.requires_grad or torch.is_grad_enabled() or not z.is_contiguous()):
            self.info["whole_original_fallback_calls"]+=1
            return None
        n=z.numel()
        out=torch.empty((2*(degree+1),*z.shape),dtype=z.dtype,device="cpu")
        src=ctypes.cast(z.data_ptr(),Pointer)
        dst=ctypes.cast(out.data_ptr(),Pointer)
        self.function(n,degree,src,self.coefficient,dst)
        self.info["native_calls"]+=1
        self.info["native_radial_elements"]+=n
        self.info["element_Horner_updates"]+=n*(26,50,72)[degree]
        self.info["last_rounding_code"]=self.handle.fixed_fejer_rounding()
        self.info["last_mxcsr"]=self.handle.fixed_fejer_mxcsr()
        return out.unbind(0)
