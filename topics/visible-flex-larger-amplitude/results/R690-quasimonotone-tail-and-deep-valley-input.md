# R690：准单调尾的固定帽唯一性判据与可执行深谷新输入

日期：2026-11-26。会话：Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：新增积分判据及新轮廓的解析性质已证明；完整标量源仅 AST，未有实际科学返回。** 本文接 R669/R671，保留它们的准确尾与线性范围，不重证旧末胞缺项，不声称新非圆精确 flex。固定有限均值目标的另一条末端兼容性由独立后继结果处理。这里的 scalar 入口是新 factory/完整 fullclosed 求解管线的第一组件，后续接线和实际方向继续执行，不以此诊断作为任务终点。

## 1. 比单调性更一般的固定帽线性尾判据

沿用 R669 的旋转参考，$a\ge R>0$、$b=a'\in[-1,0]$，开尾 $c>0$ 且 $c(S)=0$，但**不假定 c 单调**。定义

$$\mathcal B(t)=\frac{\int_0^t c(S-v)\,dv}{c(S-t)},\qquad t>0.\tag{1}$$

若 $\mathcal B\in L^1(0,t_0)$，R669 的固定帽无穷小等距尾仍唯一为零。

**证明。** R669 的准确模式积分式未用 c 单调性；只用 a 的单调性及 $a\ge R$，它给

$$
\frac{|v_m(S-t)|}{c(S-t)}
\le\frac{|m|}{R}\mathcal B(t)M_m(t),\qquad
M_m(t)=\sup_{0\le v\le t}|w_m(S-v)|.
$$

代入原两维系统，

$$
|w_m'(S-t)|\le
m^2\left\{\frac1R+\frac{m^2-1}{R^2}\mathcal B(t)\right\}M_m(t).
\tag{2}
$$

固定端值使 $M_m(t)$ 不超过右端从0至 t 的积分。系数可积，积分 Grönwall 给 $M_m=0$，回代给 $v_m=u_m=0$。$m=0$ 沿用 R669 的常数解计算；$|m|=1$ 的第二项本来为零。对全部材料模分别成立，再由 Fourier 唯一性得场为零。证毕。

若存在不减正函数 $E(t)$ 与固定 $0<c_-\le c_+<\infty$，使

$$c_-E(t)\le c(S-t)\le c_+E(t),$$

则 $\mathcal B(t)\le(c_+/c_-)t$。因此

$$e^{-1/t^2}\{1+\tfrac12\sin(t^{-4})\}$$

这种无限转向但谷峰比有界的正 ripple，仍满足唯一性判据；不能仅凭无限振荡称换了有效机制。本次分析曾把该简单式作为初稿方向，随后在科学运行前由此判据排除，未用它生成候选或宣称解决连接。

这是充分唯一性判据；其失败不反向证明非零核或非线性解存在。后继输入必须实际避开它，并继续支付完整求解与几何。

## 2. 一个明确的无界谷峰比新输入

令 d 是原 FullHold out-ramp 的**准确 binary 有理宽度**，$k_p=3/2$，$A=k_pd$，$x=t/d$。原角为

$$\beta_o(t)=A P(x),\qquad P(x)=\tfrac52x^4-3x^5+x^6.$$

新深谷角定义为

$$
\beta_d(t)=A\exp\{-x^{-2}-x^{-4}(1+\sin x^{-4})\},\quad t>0;
\qquad\beta_d(0)=0.
\tag{3}
$$

固定准确 $C^2$ cutoff

$$
\chi(x)=
\begin{cases}
1,&0\le x\le1/8,\\
1-S_5(8x-1),&1/8<x<1/4,\\
0,&x\ge1/4,
\end{cases}
\qquad S_5(u)=10u^3-15u^4+6u^5,
$$

并置

$$\beta_n(t)=(1-\chi(x))\beta_o(t)+\chi(x)\beta_d(t).\tag{4}$$

仅在旧尾 $0\le t\le d/4$ 改变输入。以旧外端 $s_0=S-d/4$ 锚定准确半径与参考高度：

$$
\begin{aligned}
a_n(S-t)&=a_o(s_0)-\int_t^{d/4}\cos\beta_n(v)\,dv,\\
Z_n(S-t)&=Z_o(s_0)+\int_t^{d/4}\sin\beta_n(v)\,dv.
\end{aligned}\tag{5}
$$

$s\le s_0$ 原样采用旧 $a_o,Z_o$。新终端半径和高度增量为 $R_n=a_n(S)$、$Z_n(S)$，不是旧数组中的 R/H；$I_n(s)=Z_n(S)-Z_n(s)$ 同样来自完整积分。

式 (5) 给 $a_n'=-\cos\beta_n$、$Z_n'=\sin\beta_n$，故准确旋转参考仍满足 $a_n'^2+Z_n'^2=1$。新 metric 为 $g_n=ds^2+a_n(s)^2d\theta^2$。这是明确的新设计输入，绝非原 FullHold 或已冻结均值目标的精化。S、原前缀和 core 可以保留；准确帽半径、参考尾及模型身份须更新。

### 2.1 平坦、正性与无限转向

$0<\beta_d\le A e^{-x^{-2}}$。每阶导数都是同一指数乘有限 Laurent 多项式与 sin/cos 乘积；指数压过一切负幂，故全部导数在0趋于0。深谷角在0有 $C^\infty$ 平坦延伸，(4) 在 cutoff 接点为 $C^2$。

纯深谷段满足

$$
\beta_d'(t)=\frac A d e^{-x^{-2}-x^{-4}(1+\sin x^{-4})}
\{2x^{-3}+4x^{-5}(1+\sin x^{-4})+4x^{-9}\cos x^{-4}\}.
\tag{6}
$$

$v=x^{-4}=2\pi n$ 时括号为正；$v=(2n+1)\pi$ 且 n 足够大时为负。因此有无限转向积聚在帽端，而角一直严格正。

### 2.2 确实避开准单调判据

在谷区 $v\in[2\pi n+\pi/6,2\pi n+5\pi/6]$，$\sin v\ge1/2$，角至多 $Ae^{-\sqrt v-3v/2}$。更靠帽端的峰位 $v_p=2\pi n+3\pi/2$ 附近取 $|v-v_p|\le v_p^{-1/2}$；由 $1+\sin v\le(v-v_p)^2/2$，峰窗中的角至少 $Ae^{-\sqrt{v_p+1}-1}$。峰窗物理宽度为常数倍 $d v_p^{-7/4}$。

角小时 $\beta/2\le\sin\beta\le\beta$。式 (1) 的分子包含更靠帽端的峰质量，分母为深谷值，因而在全部足够深的谷区上

$$\mathcal B(t)\ge c\,d\,v^{-7/4}e^v$$

其中 c 是固定正常数。谷区在 t 坐标的宽度为常数倍 $d v^{-5/4}$，所以互不相交谷区上的积分至少为常数倍 $d^2v^{-3}e^v$，连趋于零都不成立。故 $\mathcal B\notin L^1$。

这真正改变了第1节假设，不是只增加有限几个曲率变号。非可积仍只使该唯一性证明不适用，不构成非零核、匹配或非线性解的存在证明。

### 2.3 温和参考几何的完整解析界

修改段 $x\le1/4$ 上，$P(x)\le P(1/4)=29/4096$。由 $e>8/3$、$3^{16}<2^{26}$ 得 $e^{-16}<2^{-22}$，故

$$0\le\beta_n\le B:=A\,29/4096.$$

$x^{-p}e^{-x^{-2}}$ 在 $0<x\le1/4$、$p\le9$ 时不减；式 (6) 给

$$
|\beta_d'|\le k_p\,1056896/2^{22}=k_p\,8257/32768.
$$

旧导数在此至多 $k_pS_5(1/4)=k_p53/512$。又 $|\chi_x|\le15$，两个角都处于 $[0,B]$。完整微分 (4) 得

$$
|\beta_n'|\le
k_p\left(\frac{8257}{32768}+\frac{435}{4096}\right)
=\frac{35211}{65536}<1.
\tag{7}
$$

旧角也在 $[0,B]$。利用 $1-\beta^2/2\le\cos\beta\le1$ 和 $0\le\sin\beta\le B$，

$$
|R_n-R_o|\le\frac{dB^2}{8},\qquad
|Z_n(S)-Z_o(S)|\le\frac{dB}{4}.
\tag{8}
$$

原准确输入有 $R_o>1/2$、$d<1/40$。上述有理界立即给 $R_n>499/1000>9/20$ 及 $B/R_n<1$。新旋转参考两主曲率为 $-\beta_n'$ 与 $-\sin\beta_n/a_n$，修改段均小于1。未修改的 **Hold 扩段** 沿用 R669 的 $5/2$，故完整 Hold 扩段及新尾仍有参考界 $5/2$。此处没有分析更早 scalar 前缀，也不是任意非圆 q 候选的 K/reach 证书。

## 3. 无限尾的完整标量消费

源 [deep_valley_tail_input.py](../scripts/resume_20261126/deep_valley_tail_input.py) 使用同一原 FullHold 整数 oracle，并以 (3)–(5) 定义新尾。未以采样、截断 sin 相位或把未分辨尾设0定义输入。

固定 $\epsilon\le1/8$。指数函数的第 j 阶导数可由 A/B/C 三列 Laurent 多项式准确递推为 $A_j+B_j\sin(x^{-4})+C_j\cos(x^{-4})$。各系数取绝对值，完整 Bell 多项式给

$$|\partial_t^k\beta_d|\le A d^{-k}e^{-x^{-2}}\mathcal P_k(x^{-1}).$$

若出现的每个逆幂 p 满足 $p\le2/\epsilon^2$，则逐项 $x^{-p}e^{-x^{-2}}$ 在 $(0,\epsilon]$ 不减。源码以准确有理上界

$$e^{-\epsilon^{-2}}\le(3/8)^{\lfloor\epsilon^{-2}\rfloor}$$

支付整段所有无限转向，并输出0至4阶完整界。令0阶界为 $B_0$；$0\le t\le d\epsilon$ 上

$$
0\le\int_0^t\sin\beta_n\le tB_0,\qquad
t(1-B_0^2/2)\le\int_0^t\cos\beta_n\le t.
\tag{9}
$$

余下有限区间按准确 cutoff 节点共同分割；使用向外整数/Fraction jet、包围的 $\pi$ 降角、缩放交错 exp 级数、Simpson 四阶余项与完整值域矩形的交集。每个未细分叶本来已有合法整段积分盒。预算到达时自然退出只影响盒宽，不遗漏区域，也不把未达到请求精度写成数学失败。

模型身份含公式、准确参数、原输入及源；积分工作精度和细分不改变数学输入。只发表紧凑总盒、准确尾界、完整域标记和模型身份，叶表留在 runner 内存，不入 git。

首个公开 Actions 入口：

    python "$TOPIC/scripts/resume_20261126/deep_valley_tail_input.py" \
      --scalar-input "$SCALAR_INPUT" \
      --scalar-source "$TOPIC/notes/2026-11-17-parallel-model-full-hold-oracle.py" \
      --integer-source "$TOPIC/notes/2026-11-17-parallel-inward-integral-enclosure.py" \
      --hold-source "$TOPIC/scripts/parallel_20261117_negative_hold_profile_ivp.py" \
      --tail-cutoff 1/8 --integral-tolerance 1e-18 --admission-seconds 300 \
      --out "$WORK/deep-valley-input/report.json"

这不是新必过门，也不安排额外 fixture；仅在选择该输入路线时运行。若返回较宽但完整的盒，可按同一模型提高 enclosure 精度；若返回错误，保留真实错误再修接口，不伪称已有新父。

## 4. 接入非圆求解的具体责任

接口 DeepValleyTail.reference_at_affine(alpha,beta) 接受原准确位置 $s=\alpha S+\beta$，返回完整 $(a,a_s,a_{ss},I,I_s,I_{ss})$ 向外盒。其固定积分表可在同 runner 反复查询；完整域与误差源明确。它可代入 R671 **已有证明**的六 jet/J/J* 公式，不必删原自由 q/core/H 或另造少数模模型。

新 factory 仍须完整更新：新 a 节点/中点/Gauss 载体及误差、新 $R_n$、新 f/h/k、独立 canonical model/source/input 身份、任意点与六 jet 读出，以及新连续 profile reader。S 和原 symbolic 网格可先保留；如添加趋向 S 的 dyadic 节点，那是对已固定 (3)–(5) 的分辨率精化，不移动 profile。

旧 R671/R674 canonical reader 应拒绝不同 schema；旧证书不能由数值接近、相同 q 数组或旧 SHA 转移。准备源没有自动产生冒称接受的新 npz 父。实际非圆连接仍用完整原自由变量和全部观察行求解，幅度见证 p 随全部 core 变化；同场 D/L/K/reach 与固定 g 精化重新支付。

选择这条路线时，先把该明确 profile 作为新的 scalar 输入完整接入，再运行真实 nonlinear 求解。必要时增加端点分辨率或明确调整新输入控制，不能把有无限转向当接受条件，也不能把有限子空间失败当无限维不存在性。本文把简单 ripple 排除，并交出确实改变相关端点假设、保留温和参考几何且可直接求值的下一输入；尚无新科学数值或非圆存在声明。


## 5. 本次实际发布与执行身份

完整标量源 SHA256 `e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2`；此版本完整支付准确位置盒跨新锚点的两侧分支，不以浮点中点选侧。完整首运行参数保 [请求](../computations/resume-20261126-deep-valley-input-first-step.json)，紧凑输出字段保 [字段表](../computations/resume-20261126-deep-valley-input-summary-fields.json)。本次只做 AST/编译和源/参数核验；新输入科学核验已经排入 run45762076394 的同 runner 后继，实际报告未返。新的固定目标是此处明确的 `ds²+a_n(s)²dθ²`，而不是把其分母在移动均值中约掉；完整原变量/全部观察/幅度保护和新场连续几何仍须实际完成。
