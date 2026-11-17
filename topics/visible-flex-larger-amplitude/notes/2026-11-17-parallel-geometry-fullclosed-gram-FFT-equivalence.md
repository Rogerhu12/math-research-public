# 同一真实全闭初猜的 FFT 等价实现与固定线性化缓存

2026-11-17，geometry_amplification。**新实现验证，非新场或新求解。** 消费已完成的唯一 dense 准备试验及原数组；不重算 dense 残差／Jv／Jᵀ，不改变 401255 真实初猜、M160/N2048、923 节点、1845 个原节点／中点或全部 11,335,680 个角值目标。

## 数学上保留的有限节点算子

对 `νj=2j`，原有限合成矩阵为 `C_kj=cos(νjφk)`（含 ν0=0）及 `S_kj=sin(νjφk)`，`φk=2πk/N`。N 为偶数且 N>4M 时，正频槽互异并避开 Nyquist。按 NumPy 的 inverse-DFT 归一化：

- cos 常数放入 rFFT 零槽 `N c0`，非零槽放 `N cj/2`；
- sine 槽放 `−i N sj/2`；
- 普通有限 Euclidean 转置分别取 `Re rFFT(w)_ν` 与 `−Im rFFT(w)_ν`，**不除 N**。

这些是有限 N 点矩阵的逐项恒等式，并不要求 w 自身是有限带宽函数。complex 输入分成实、虚两部分，各做真实 rFFT／irFFT，再线性复合，故不丢 complex-step 的虚部。符号、转置和 `C[:,1:]` 视图都保留；原物理角导的旋转连接项没有省略。

这里只替换有限 q、ρ、Θ 的三角合成／矩阵转置。`exp(i(Θ−φ))` 的完整解析 lift 仍在每个原角节点直接评价，全部 Gram 角值及 core→ρ／Θ／lift 链保持。**没有声称 Gram 是旧 962 项的完整有限谱，也没有截断解析 lift 的无限谱。** 浮点 FFT 与直接 sin/cos 求值不保证逐位一致，实际差异如下支付。

缓存只在显式 `set_base(x)` 时建立，保存该真实线性化点的完整 `(V=Fs,d=Fφ)`。随后仅在固定 operator 参数、相同 dtype/shape 且 `np.array_equal(x,x_base)` 时复用；不按容差匹配（正负零视为同数值）。complex-step 输入不会命中实数基点。实际仅构建一次，三次命中；V/d 数据 181,370,880B，固定基点向量 10,657,960B。缓存是同一有限函数的值复用，不能跨不同 mesh、标量、端口或 x 使用。

## 真实过程含一次已保存的接口失败

第一版 8ea6 源、667f 入口在第一次 `set_base→prepare` 退出 1：父源的 `−self.sin @ v` 按 Python 优先级先对矩阵取负，第一版 `TrigMatrix` 漏了 `__neg__`。失败发生在求 ρφ 时，尚未产生任何 V/d 缓存、FFT 残差、Jv 或伴随对照。920B 失败记录 SHA
`849627ac24bb21755649cdbde87ec6ba2630e9dcaef3a0b9dcff53fc48c81e16` 保留全部输入／源身份和范围。

第二版仅加准确的 ±1 矩阵符号视图，并在转置和切片中传递。原两个源及失败记录保留，场／点集／目标均未变化。随后同一对照完整退出 0。总计两次进程启动、一次接口失败、一次完成的对照；没有失败后调参、加密或重复 dense 试验。

## 同一全体数组的实际差异

参考为 dense 报告 f09148 及其原 304,031,712B 数组 4da176。下表的相对值均用完整 l2 范数，不是只抽样少数行。

| 新 FFT 与已存 dense | 绝对最大差 | 相对 l2 差 |
|---|---:|---:|
| 全部角值残差 | `2.8393287720973603e−11` | `6.613242718994191e−14` |
| 同一完整方向 Jv | `1.9199433154426515e−9` | `8.380907938709269e−14` |
| 同一完整权向量 Jᵀw | `5.974434316158295e−7` | `9.221622602948514e−14` |

最后一项的完整伴随范数约 `1.801413715e7`，所以同时列绝对与相对差，不把绝对差写成零。FFT 自身的完整伴随内积差为
`1.0160761121369433e−12`、相对 `2.7314500518220614e−14`。同一 complex-step 方向与 FFT Jv 的绝对最大差为 `5.4569682106375694e−12`、相对 `3.256132142088684e−16`；与已存 dense Jv 的相对差为 `8.380801124413678e−14`。

| 操作 | 原 dense 秒 | 本次 FFT／缓存秒 |
|---|---:|---:|
| 残差 | 2.0271 | .2450 |
| Jv | 4.4168 | 1.1410 |
| Jᵀw | 3.3726 | 1.0555 |
| complex 输入路径 | 8.8351 | 1.3798 |

另付一次缓存构建 `.4784` 秒；本次含原数组读取／比较约 `6.2882` 秒。计时只描述当前机器／同一输入，不构成普遍加速保证，也不估算尚未执行的大预算非线性收敛。原初猜的 Gram≈147.4 失败状态不因实现等价而改善。

## 冻结身份与入口

| 对象 | SHA256 |
|---|---|
| dense 父算子 `parallel-geometry-fullclosed-gram-operator.py` | `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d` |
| `parallel-geometry-fullclosed-gram-fft-v2.py` | `7ab7391f3d351a5c2314d3c136fe5aa708612bb53e45221d2c09efc0fb622211` |
| `parallel-geometry-fullclosed-gram-actual-fft-compare-v2.py` | `9c0dcfae334333270e33cc6bcd47fe5a5eda4b5fb61cc548327944d5753afe20` |
| 完整实际报告 `parallel-geometry-fullclosed-gram-actual-fft-compare.json` | `882e0c0fa8a1798e0c9cf70b6d4a2b8e1d3b9a8464f7d072159d284f9db5e408` |
| 原 dense 报告 | `f09148db310f0229170207538ecc4d41c723d74130da6897c10bc06fd68e15c4` |
| 原 dense 数组 | `4da17687a6856901d09d92f02ad0c7bd0cdf012475403fbf2f8488579cc0a05e` |

用已校验原 bundle／数组，在新输出位置运行：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-geometry-fullclosed-gram-actual-fft-compare-v2.py \
  --operator parallel-geometry-fullclosed-gram-operator.py \
  --fft-source parallel-geometry-fullclosed-gram-fft-v2.py \
  --bundle parallel-model-fullclosed-hold-warm.npz \
  --arrays parallel-geometry-fullclosed-gram-actual-dense-arrays.npz \
  --dense-report parallel-geometry-fullclosed-gram-actual-probe.json \
  --dense-report-sha f09148db310f0229170207538ecc4d41c723d74130da6897c10bc06fd68e15c4 \
  --out parallel-geometry-fullclosed-gram-actual-fft-compare.json
```

原大数组仍只在 scratch。此结果使后续同一模型的矩阵自由计算可以消费 FFT 实现；不修改任何正在运行的短 LM，不启动新全闭非线性预算，不声称连续 metric／嵌入／reach 或课题完成。

## 原失败源码的完整可逆差异

为避免保存同源码副本，以下是两份原v1到已刊v2的全部差异；在仓库外恢复原basename并反向应用即可逐字恢复。原源8ea6共5838B、入口667f共5627B；完整SHA见差异和前述失败记录。原失败只有接口缺失，未完成几何评价；不删除这次失败。

原 `parallel-geometry-fullclosed-gram-fft.py` SHA256 `8ea6e6e7e587e34657ca9094fbb415aea9c983cbe98a022d93ce53495b392743`。

```diff
--- parallel-geometry-fullclosed-gram-fft.py
+++ parallel-geometry-fullclosed-gram-fft-v2.py
@@ -27,10 +27,12 @@
     The transpose is the finite Euclidean transpose (no 1/N factor).
     """
 
-    def __init__(self,N,M,kind,*,constant=True,transposed=False):
+    def __init__(self,N,M,kind,*,constant=True,transposed=False,sign=1):
         self.N,self.M,self.kind = int(N),int(M),kind
         self.constant = bool(constant and kind=='cos')
         self.transposed = bool(transposed)
+        self.sign = int(sign)
+        if self.sign not in (-1,1):raise ValueError('Only exact signed trig views are supported')
         if self.N%2 or self.N<=4*self.M or self.M<1 or kind not in ('cos','sin'):
             raise ValueError('This finite trig implementation requires even N>4M')
         self.freq=2*np.arange(1,self.M+1)
@@ -42,14 +44,17 @@
 
     @property
     def T(self):
-        return TrigMatrix(self.N,self.M,self.kind,constant=self.constant,transposed=not self.transposed)
+        return TrigMatrix(self.N,self.M,self.kind,constant=self.constant,transposed=not self.transposed,sign=self.sign)
 
     def __getitem__(self,key):
         if (self.transposed or self.kind!='cos' or not self.constant
             or not isinstance(key,tuple) or len(key)!=2
             or key[0]!=slice(None) or key[1]!=slice(1,None)):
             raise IndexError('Only the actual C[:,1:] view is implemented')
-        return TrigMatrix(self.N,self.M,'cos',constant=False)
+        return TrigMatrix(self.N,self.M,'cos',constant=False,sign=self.sign)
+
+    def __neg__(self):
+        return TrigMatrix(self.N,self.M,self.kind,constant=self.constant,transposed=self.transposed,sign=-self.sign)
 
     def _real_product(self,x):
         if self.transposed:
@@ -73,8 +78,8 @@
         if x.ndim!=1 or x.shape[0]!=self.shape[1]:
             raise ValueError('Wrong finite trigonometric matrix-vector shape')
         if np.iscomplexobj(x):
-            return self._real_product(x.real)+1j*self._real_product(x.imag)
-        return self._real_product(x)
+            return self.sign*(self._real_product(x.real)+1j*self._real_product(x.imag))
+        return self.sign*self._real_product(x)
 
 
 class FFTMixin:
```

原 `parallel-geometry-fullclosed-gram-actual-fft-compare.py` SHA256 `667f55a6eb85fb318ba655194e6ad61021610452924e5b103249c7116198baaa`。

```diff
--- parallel-geometry-fullclosed-gram-actual-fft-compare.py
+++ parallel-geometry-fullclosed-gram-actual-fft-compare-v2.py
@@ -18,7 +18,7 @@
 
 DENSE_SHA='e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d'
 PROBE_SHA='803f6c5e121a4f167984cc33371856d9978a3d13177f2315e7321f37ea533483'
-FFT_SHA='8ea6e6e7e587e34657ca9094fbb415aea9c983cbe98a022d93ce53495b392743'
+FFT_SHA='7ab7391f3d351a5c2314d3c136fe5aa708612bb53e45221d2c09efc0fb622211'
 
 
 def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
```

