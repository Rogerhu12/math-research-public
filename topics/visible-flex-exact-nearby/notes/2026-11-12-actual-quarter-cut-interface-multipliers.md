# 完整物理接口乘子：同一准确图的 r=1/4 接线

2026-11-12，R88/R95 的实际有限输入补充。

本次对象为显式径向对称化的准确仿射点
\(\delta_5=-7789843107295549/4611686018427387904\)。
物理角模固定为 \(e^{4ik\theta}\)。本报告在真实接口 \(r=1/4\)
重新支付了全角复域和无限 primitive，未把此前只覆盖
\(|r|\le .24\) 的图表移到这个接口。

## 1. 同一真实场的公式

所有向量先用旋转柱坐标表示。令 \(X=F_r\)，
\(T=(-\cos\gamma\sin\beta,\cos\gamma\cos\beta,\sin\gamma)\)，
则 \(F_\theta=aT\) 是准确恒等式。\(F,X\) 来自完整原函数，
保存有限 Fourier 原函数的误差仍进入每一个点值和复域。

记
\[
 h=-\sin\beta X_0+\cos\beta X_1,\quad
 v=-\cos\beta X_0-\sin\beta X_1,\quad
 Q=\cos\gamma X_z-\sin\gamma h,
\]
\[
 D=(1+\beta_\theta)\cos\gamma Q-\gamma_\theta v,
 \qquad M=\beta_r\cos\gamma Q-\gamma_r v.
\]
再令 \(h_F=-\sin\beta F_0+\cos\beta F_1\)、
\(v_F=-\cos\beta F_0-\sin\beta F_1\)，并写
\[
 H=(\cos\gamma F_z-\sin\gamma h_F)v-v_FQ.
\]
此处 \(aH=F\cdot(F_r\times F_\theta)\)，
\(N_{\rm raw}=-a^2D\)、\(M_{\rm raw}=-a^2M\)。因此 R88 的
原始核心主系数为
\[
 A_{rr}=D\frac{F\cdot F}{H^2},\qquad
 A_{r\theta}=-M\frac{F\cdot F}{H^2}.
\]
这些关系只需准确 \(T,T_r,T_\theta\)，未以截断原函数的角导数
替代 \(aT\)。\(F_{r\theta}\) 中的 \(a'T\) 对法向三重积为零。

取右侧正 height
\[
 Y=F_z/\sqrt{F\cdot F},\qquad
 p_Y=A_{rr}Y_r+A_{r\theta}Y_\theta.
\]
将同一 \(F,X,aT\) 代入，实际计算的能量剪切为
\[
 s=Yp_Y=\frac{F_z}{H^2}
 \left[D\left(X_z-\frac{F_z(F\cdot X)}{F\cdot F}\right)
 -M\left((F_\theta)_z-
       \frac{F_z(F\cdot F_\theta)}{F\cdot F}\right)\right].
 \tag{1}
\]
五个保存的函数依次为 \(Y,Y^{-1},p_Y,s,p_Y/Y\)。后两商分别
由 \(p_Y=s/Y\)、\(p_Y/Y=s/Y^2\) 形成，所有分母都在同一
真实对象上排零。

## 2. 新的完整角解析域

使用 512 点 primitive、2048 点原生角 FFT、192-bit Arb 运算，
在归一角 \(x=4\theta\) 的闭带 \(|\Im x|\le1/16\) 上，
连续角格及原函数尾给出安全放宽值
\[
 \Re(F\cdot F)>1.20313092655,\quad
 |F_z|>.281941425705,\quad |H|>1.111760624636.
 \tag{2}
\]
整个实圆另有 \(Y>.239953664371\)。式 (2) 在物理带
\(|\Im\theta|\le1/64\) 上给出位置模平方的单值主平方根，
从而五个函数均为全纯周期函数。每个商的复模数由真实分子上界
及 (2) 的分母下界直接支付。这里既没有只检查实角节点，
也没有使用样本极小值作为全带证明。

准确角对称性使这五个函数为实偶函数，因此
\(f_{-k}=f_k\in\mathbb R\)。NPZ 保存 513 个正频率 binary64
中心 \(c_k\) 和向外 binary64 半径 \(r_k\)，都作为准确 dyadic
数解释，合同为
\[
 f_k\in[c_k-r_k,c_k+r_k],\qquad
 P_f=c_0+2\sum_{k=1}^{512}c_k\cos(4k\theta).
 \tag{3}
\]
每个 \(r_k\) 包含原生点值/FFT 区间误差、完整无限 primitive
误差、中心选择误差和全部 DFT 混叠。若 \(M\) 是上述真复带模界、
\(\sigma=1/16\)、\(N=2048\)，混叠费用取
\[
 M\frac{e^{-(N-k)\sigma}+e^{-(N+k)\sigma}}
          {1-e^{-N\sigma}}.
 \tag{4}
\]

令 \(A_j(f)=\sum_k|4k|^j|f_k|\)，其中 \(j=0\) 的零模权为 1。
在 \(K=512\) 之外的完整尾为
\[
 2M4^j\sum_{k>K}k^je^{-k\sigma},\qquad j=0,1,2.
 \tag{5}
\]
程序用几何级数及其前两次导数的准确闭式求和；保留项误差按
同一权加总。故下表是完整函数与 (3) 的误差，而非截断之间差：

| 函数 | \(A_0(f-P_f)\) 上界 | \(A_1(f-P_f)\) 上界 | \(H^{1/2}\) 乘子误差上界 |
|---|---:|---:|---:|
| \(Y\) | \(2.261937\,10^{-11}\) | \(2.327510\,10^{-8}\) | \(7.482004\,10^{-10}\) |
| \(1/Y\) | \(2.189126\,10^{-10}\) | \(2.259531\,10^{-7}\) | \(7.251974\,10^{-9}\) |
| \(p_Y\) | \(4.999761\,10^{-10}\) | \(5.142081\,10^{-7}\) | \(1.653406\,10^{-8}\) |
| \(Yp_Y\) | \(1.126260\,10^{-10}\) | \(1.158642\,10^{-7}\) | \(3.725009\,10^{-9}\) |
| \(p_Y/Y\) | \(2.192067\,10^{-9}\) | \(2.253992\,10^{-6}\) | \(7.248359\,10^{-8}\) |

全部未放宽的有向数、\(A_2\) 误差和分项费用保存在 JSON 中。
本次实际计算为 1.8824 CPU 秒。

## 3. 物理 H1/2 乘子与准确有限块

R95 的物理迹空间采用 \(w_0=1\)、\(w_k=\sqrt{|4k|}\ (k\ne0)\)。
平移一个 Fourier 指标满足
\[
 w_{j+m}/w_j\le\sqrt{1+4|m|}.
\]
因此
\[
 \|M_f\|_{H^{1/2}\to H^{1/2}}
 \le\sum_m\sqrt{1+4|m|}|f_m|.
 \tag{6}
\]
在该实函数情形，对偶给出同一 \(H^{-1/2}\) 界。
若误差的 \(A_0,A_1\) 费用为 \(E_0,E_1\)，由
\(\sqrt{1+t}\le1+\sqrt t\) 及 Cauchy--Schwarz，(6) 的误差不超过
\(E_0+\sqrt{E_0E_1}\)。实际完整乘子模数安全取
\[
 \|M_Y\|<.266661,\quad \|M_{1/Y}\|<4.203277,\quad
 \|M_{p_Y}\|<6.968074,\quad \|M_{Yp_Y}\|<1.719099,
 \quad\|M_{p_Y/Y}\|<28.263875.
 \tag{7}
\]

任意有限输入/输出的 Toeplitz 条目直接使用 (3) 的真实系数区间。
但只保留压缩条目不等于已经支付全输出：若输入支持 \(|j|\le B\)，
输出切到 \(|k|\le L\)，所需的完整系数尾是 \(|m|>L-B\)，
不是 \(|m|>2B\)。同理，原始核心迹 \(w\) 有限带宽时，
\(U=Y^{-1}w\) 一般不在 R95 已计算的十维 grounded 输入空间；
其输入尾须另付完整帽算子费用，不能沿用有限输入列证明略去。

真实乘子本身的高模并不为零。由 (3) 有
\[
 |f_k|\ge\max(0,|c_k|-r_k).
\]
对已保存的有限系数求和，未知更高系数只会增加尾范数。
独立小入口得到
\[
 \sum_{|k|>16}|(Yp_Y)_k|>.049447341009,
 \qquad
 \left(\sum_{|k|>16}|(Yp_Y)_k|^2\right)^{1/2}
       >.0168849890162.
 \tag{8}
\]
这修正了 R88 旧有限 FFT 诊断的证据口径：当前 (8) 已含无限
primitive、系数舍入和混叠的有向费用。上界本身并不能证明非零，
所以这里显式保存了独立的下界报告。

## 4. 负侧及 core/cap 法向

准确径向反射为 \(F(-r,\theta)=\operatorname{diag}(1,1,-1)F(r,\theta)\)。
原始 \(A_{rr}\) 偶、\(A_{r\theta}\) 奇，\(Y_z\) 奇。
左侧取正 height \(-Y_z\)，它在 \(r=-1/4\) 的值等于右侧 \(Y\)。
相对于全局增大 \(r\) 的方向，其 conormal 为 \(-p_Y\)。
左核心的向外法向另翻号，故以核心向外口径写的正 height
能量剪切在两边同为 \(Yp_Y\)。全局竖直平移的 grounded 常数
符号仍分别为左负、右正，regular 槽随同保留。

在右端 R88 的准确接线为
\[
 U=Y^{-1}w,\qquad
 p_{g,\mathrm{cap}}=-(Yp_w-wp_Y).
 \tag{9}
\]
这些是物理 \(\theta\) 表示；没有把它们认作 canonical
\(\psi\) 模。R83/R92 的真密度和角转换仍是独立必要输入。

## 5. 文件及准确重放

实际源为 `scripts/fourfold_phase_cut_interface_fourier.py`，完整
报告及系数为 `notes/2026-11-12-actual-quarter-cut-interface-Fourier.json`
和同名 NPZ。完整依赖、对象与数组 SHA 全部写在报告中。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cut_interface_fourier.py \
  --out notes/2026-11-12-actual-quarter-cut-interface-Fourier.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_interface_tail_lower.py \
  --out notes/2026-11-12-actual-quarter-cut-interface-tail-lower.json
~~~

这里已经支付的是同一接口的完整乘子和有限数据。核心径向传播、
完整低高 Schur 反馈逆和最终非线性零仍没有由本报告获得。
