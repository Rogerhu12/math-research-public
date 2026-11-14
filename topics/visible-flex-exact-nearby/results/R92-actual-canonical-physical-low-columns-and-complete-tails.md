# R92：真实根角换元后的有限秩列与完整物理 Fourier 尾

2026-11-12，visible-exact-astra-f6a2。

**状态：完整证明；当前公共参数盒的实际常数已支付。**
本篇把 R87 的 canonical 低模剪切修正准确表示在物理角空间中，
保留根均值、全部低行/低列和无限物理尾。它没有把 canonical
$|k|\le61$ 等同于物理 $|k|\le64$，也不声称低反馈矩阵已经可逆。

## 1. 同一真实角图及已付输入

取 R83、R87 的准确仿射族
$$
 \delta_5=-7789843107295549/4611686018427387904,
 \qquad |\delta-\delta_5|\le1/2500000.
 \tag{92.1}
$$
令 $p=\pi/2$，$H(z)=qY_0(z)$，$Y_0(0)=0$，$q=2\pi/\ell$。
这是真正积分所得的解析角图，满足 $H(z+p)=H(z)+p$。
取 $S=1/256$。已完成的 2048 个连续复矩形给出
$$
 \operatorname{Re}H'\ge m>.4657789869774991,
 \qquad |H'|\le M<3.383705397750172,
 \qquad |v_0|\le V<6004.148324
 \quad (|\operatorname{Im}z|\le S).
 \tag{92.2}
$$
同时 $q\ge q_->8.32788647674253$，且 $H$ 的像包含
canonical 闭条带 $|\operatorname{Im}\psi|\le u$，其中可取
$$
 u>.0009097245839404.
 \tag{92.3}
$$
程序使用完整有向端点，不使用这些放宽小数。
输入报告为 `notes/2026-11-12-actual-root-v0-complex-strip.json.gz`，
并核对它的完整根圆长证书、真正根证书及准确参数区间。
这里只聚合已证明的连续复域，没有重新把节点采样当作角图。

所有空间先取四重周期函数的 $L^2(d\theta/p)$。令
$$
 (U_Hf)(\theta)=\sqrt{H'(\theta)}\,f(H(\theta)).
 \tag{92.4}
$$
实轴上 $H'>0$，准确换元证明 $U_H$ 是 onto unitary。
复条带上由 $\operatorname{Re}H'>0$ 取与实轴相容的唯一平方根，
其模数不超过 $\sqrt M$。这只支付半密度换元；R83 的其它高度、
通量和 shear 因子仍须以其自身公式接入完整 frame。

## 2. 曲边像域上的 Cauchy 投影

固定 $0<s<S$。设 $f(\psi)$ 在 $\Omega=H(\{|\operatorname{Im}z|<S\})$
解析，$g(z)=f(H(z))$ 在外闭条带的模数不超过 $F$。
令 $f_+$ 保留 canonical Fourier 指数 $n\ge0$，$f_-$ 保留 $n<0$。
则在 $|\operatorname{Im}z|\le s$，
$$
 |f_\pm(H(z))|\le C_s F,\qquad
 C_s=\frac{M}{2m}e^{4MS}
       \operatorname{arsinh}\frac{p}{2(S-s)}.
 \tag{92.5}
$$

**证明。** $\operatorname{Re}H'>0$ 和条带凸性给
$$
 |H(z)-H(w)|\ge m|z-w|.
 \tag{92.6}
$$
先在实轴写正投影的移线积分
$$
 f_+(\psi)=\frac1p\int_0^p
 \frac{g(t-iS)H'(t-iS)}
      {1-e^{4i(\psi-H(t-iS))}}\,dt.
 \tag{92.7}
$$
下曲线的虚部严格负，故几何级数和准确 Fourier 移线证明此式。
负投影使用上曲线及核 $(e^{4i(\psi-H(t+iS))}-1)^{-1}$。
因 $H$ 在条带及周期商上单射，两个积分的分母在 $\Omega$ 内
都不为零；解析恒等式将这两个投影延拓到整个曲边像域。
端点积分可先取外条带内部再令其趋于 $S$，连续闭域界保留。

对 $a$ 按模 $p$ 取到 $[-\pi/4,\pi/4]$，有
$$
 |1-e^{4i(a+ib)}|
 =2e^{-2b}\sqrt{\sin^2(2a)+\sinh^2(2b)}
 \ge\frac8\pi e^{-2b}|a+ib|.
 \tag{92.8}
$$
这里使用 $|\sin(2a)|\ge4|a|/\pi$ 和 $|\sinh(2b)|\ge2|b|$。
周期版 (92.6) 和 $|b|\le2MS$ 因而把核模数控制为
$$
 \frac{\pi e^{4MS}}{8m}
 \frac1{\min_{j\in\mathbb Z}|z-(t\mp iS)+jp|}.
 \tag{92.9}
$$
乘上 $|H'|\le M$ 后，角积分至多
$$
 \frac{M\pi e^{4MS}}{8mp}
       \int_{-p/2}^{p/2}\frac{dt}{\sqrt{t^2+(S-s)^2}}
 = C_s.
 \tag{92.10}
$$
这证明 (92.5)。关键在于使用真实曲边像域，不必把物理宽度缩到
$u/M$，也没有假设 $H$ 保持 Fourier 模。

## 3. 正则化剪切的准确有限秩分解

在 canonical 角中令 $e_k(\psi)=e^{4ik\psi}$，
$$
 \Gamma_k=4q|k|\ (k\ne0),\quad\Gamma_0=1,
 \quad L_*=2048,
 \quad A=\Gamma^{-1},\quad T=\max(\Gamma,L_*)^{-1}.
 \tag{92.11}
$$
令 $\widetilde v=v_0\circ H^{-1}$。原剪切与正则化剪切分别为
$A M_{\widetilde v}A$、$T M_{\widetilde v}T$。
由 $q_-$，$D=A-T$ 的支撑包含于 $|k|\le K=61$。
令 $E:\mathbb C^{123}\to L^2$ 为这组 canonical 模的准确嵌入，
$D=EdE^*$，并置
$$
 B=U_HE,\quad C=U_HTM_{\widetilde v}E,\quad
 V_{LL}=E^*M_{\widetilde v}E.
 \tag{92.12}
$$
准确展开 $A=T+D$ 给
$$
 \boxed{\quad
 U_H(A M_{\widetilde v}A-TM_{\widetilde v}T)U_H^*
 = B d C^*+C d B^*+B d V_{LL}dB^*.
 \quad}
 \tag{92.13}
$$
因此秩至多 $246$，但各列仍有全部物理 Fourier 模。
尤其根零模 $d_0=1-1/L_*$ 保留。由真实酉性，
$$
 \|B\|=1,\quad \|C\|\le V/L_*,\quad
 \|V_{LL}\|\le V,\quad \|d\|\le\delta_*:=1-1/L_*.
 \tag{92.14}
$$
无论参数改变后活跃模数是否减少，固定 123 列仍给同一个准确分解；
对应 $d_k$ 取其准确非负值即可。

## 4. 两类真实列在物理复条带上的界

对 $0\le k\le K$ 置
$$
 F_k=V e^{4ku},\quad G_k=V e^{4kMS},\quad r=e^{-4u},
 \tag{92.15}
$$
以及
$$
 W_* =\frac1{L_*}+\frac2{L_*}\sum_{n=1}^K r^n
  +\frac1{2q_-}\left[-\log(1-r)-\sum_{n=1}^K\frac{r^n}{n}\right],
 \tag{92.16}
$$
$$
 J_s=\sum_{n=1}^K
       \left(\frac1{q_-}-\frac{4n}{L_*}\right)e^{4n(Ms-u)}.
 \tag{92.17}
$$
这些括号均正，$K=61$ 是按完整有向 $q_-$ 逐整数验证的上界。
则第 $\pm k$ 列满足
$$
 |B_{\pm k}(z)|\le b_k:=\sqrt M e^{4kMs},
 \tag{92.18}
$$
$$
 |C_{\pm k}(z)|\le c_k:=\sqrt M
 \left[F_kW_*+Ms\left(\frac{2C_sG_k+V}{q_-}+2F_kJ_s\right)\right].
 \tag{92.19}
$$

**证明。** 第一式直接来自 (92.4)。为证第二式，令
$f=\widetilde v e_k$、$w=Tf$。在 canonical 宽度 $u$ 上
$|f|\le F_k$，所以每个完整 Fourier 系数
$|f_n|\le F_k r^{|n|}$。在实轴上，$T_n\le1/\max(4q_-|n|,L_*)$
（$n=0$ 时为 $1/L_*$）；对全部 $n$ 求和得到 $|w|\le F_kW_*$。
这包括真正无限尾，不是有限 DFT 的尾设为零。

又 $T=A-D$。对非零模准确微分有
$$
 (Af)'=\frac i q(f_+-f_--f_0).
 \tag{92.20}
$$
由 $|f_0|\le V$ 及 (92.5)，第一项导数不超过
$(2C_sG_k+V)/q_-$。有限项使用
$4n d_n\le1/q_- -4n/L_*$、$|\operatorname{Im}H(z)|\le Ms$
和完整 Fourier 系数界，得到 $|(Df)'|\le2F_kJ_s$。
沿真实路径 $H(x+it)$ 从实轴积分，路径长度至多 $Ms$，最后乘
$|\sqrt{H'}|\le\sqrt M$，正是 (92.19)。这些式对整个公共参数盒统一。

## 5. 完整物理高尾和有限矩阵替代费

令 $\Pi_N$ 保留物理四重模 $|n|\le N$，$P_N=I-\Pi_N$。
置 $\rho=e^{-8s}$、$a=N+1$，定义
$$
 Z_0(N)=\frac{2\rho^{N+1}}{1-\rho},
 \tag{92.21}
$$
$$
 Z_{1/3}(N)=2\,4^{2/3}\rho^{N+1}
 \left[\frac{a^{2/3}}{1-\rho}
       +\frac{2a^{-1/3}\rho}{3(1-\rho)^2}\right].
 \tag{92.22}
$$
若 $B_2=b_0^2+2\sum_{k=1}^{61}b_k^2$，
$C_2=c_0^2+2\sum_{k=1}^{61}c_k^2$，则
$$
 \|P_NB\|\le\epsilon_B:=\sqrt{Z_0 B_2},\quad
 \|P_NC\|\le\epsilon_C:=\sqrt{Z_0 C_2},
 \tag{92.23}
$$
$$
 \||D_\theta|^{1/3}P_NB\|\le\eta_B:=\sqrt{Z_{1/3} B_2},\quad
 \||D_\theta|^{1/3}P_NC\|\le\eta_C:=\sqrt{Z_{1/3} C_2}.
 \tag{92.24}
$$
这些是 Hilbert--Schmidt 上界，因此也控制算子 norm。
证明是准确移线给 $|\widehat B_k(n)|\le b_k e^{-4s|n|}$，
$C$ 同理。对 $H^{1/3}$ 平方权使用完整凹性界
$(a+j)^{2/3}\le a^{2/3}+(2/3)a^{-1/3}j$ 后求几何级数，
即得 (92.22)。没有省略任一正负物理频率。

记 (92.13) 的完整算子为 $\Delta$。代入
$B_N=\Pi_N B$、$C_N=\Pi_N C$ 得准确有限角矩阵
$\Delta_N=\Pi_N\Delta\Pi_N$。逐项加减并用 (92.14) 得
$$
 \boxed{\quad
 \|\Delta-\Delta_N\|\le
       2\delta_*(\epsilon_C+V\epsilon_B),\qquad
 \||D_\theta|^{1/3}P_N\Delta\|
       \le\delta_*(\eta_C+V\eta_B).
 \quad}
 \tag{92.25}
$$
例如第三项的双侧误差至多
$2\delta_*^2V\epsilon_B$，前两项合计至多
$2\delta_*\epsilon_C+2\delta_*V\epsilon_B/L_*$；
使用 $\delta_*+1/L_*=1$ 即得首式。次式只在左侧施加高投影，
同样恒等式给出。$\Delta$ 自伴，故相应输入侧对偶尾也保留。

## 6. 当前实际常数与适用范围

源 `scripts/fourfold_phase_canonical_physical_low_columns.py` 以
256-bit Arb 聚合完整证书，取 $s=7S/8=7/2048$。实际报告为
`notes/2026-11-12-actual-canonical-physical-low-columns.json`。
每个输入、源 SHA 和每列模界都保存。

| 物理四重 cutoff $N$ | 完整有限角替代的 $L^2$ 误差上界 | 高输出齐次 $H^{1/3}$ 上界 |
|---:|---:|---:|
| 64 | $7.306\,10^6$ | $2.730\,10^7$ |
| 256 | $5.293\,10^5$ | $2.793\,10^6$ |
| 512 | $1.599\,10^4$ | $1.039\,10^5$ |
| 1024 | $14.574$ | $117.987$ |
| 2048 | $1.212\,10^{-5}$ | $1.229\,10^{-4}$ |
| 4096 | **$8.380\,10^{-18}$** | **$1.068\,10^{-16}$** |

粗复模数在物理 $N=64$ 不提供小尾，这个事实明确保留。
$N=4096$ 的结论只使有限秩列的全物理尾变得可支付，
不要求把完整反馈低块盲目扩成 8193 维：可保留 (92.13) 的
123+123 列，计算其与真实低高解算器的耦合，末尾使用 (92.25)。
有限列系数、$V_{LL}$、完整 frame 的其它乘子和真正 Schur 逆
仍须实际形成；本报告没有用这些界捏造尚未计算的矩阵条目。

重放本次有向聚合：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 \
python scripts/fourfold_phase_canonical_physical_low_columns.py \
  --out notes/2026-11-12-actual-canonical-physical-low-columns.json
```

本篇没有宣称完整反馈、实际 R31 KAM 或非线性零解完成。
