# R244 后续附录：全部中间比例图的共同奇异序列与紧扰动全谱

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明；Astra-ISP-1cf8c51d 已复核有界 pencil、全部域交换、共同核心奇异列及两侧半 Fredholm 排除。真正秩二见证的比例图不仅没有预解点；全部中间实现、全部有界交换单位倍数及有界交换扰动，在同一个原多项式核心上具有逐参数的弱零单位近似特征序列。加入任意有界紧算子后仍为全平面近似点谱，且任何参数都不是上、下半 Fredholm 点。这不构成原 Hilbert ISP 的完成。

适用范围更新：[R230 逐对比例全谱 §8](R230-appendix-minimal-rank-pairwise-ratio-spectra-and-common-denominators.md)现已把下文全部加强推广到任意最小正秩中所选的两条广义预解行，无需其余行有预解。该处完整替换了排除 pencil 为零时对严格图缺口的旧依赖；允许高秩的最小图与最大图相等。本稿不重复登记这次范围推广。

## 1. 准确设置与去重

沿用 R244 已发的[比例全谱](R244-appendix-resolvent-minimal-cores-and-intermediate-ratio-spectra.md)及[Lagrangian 附录](R244-appendix-invariant-lagrangian-completion-and-full-spectrum-c-selfadjoint-extensions.md)，记
$$
 N=\overline{\{(R_2y,R_1y):y\in H\}},\qquad
 K=\{(x,z):R_1x=R_2z\},\qquad N\subsetneq K.
$$
这里 $R_i\in A'$ 均单射、稠密像，并有 $R_ig_i=1$。
全部 $A'$ 元素满足 $F=CF^*C$。

有
$$
 N=\operatorname{Graph}T_{\min},\quad
 T_{\min}=X_h,\quad h=R_1g_2,\qquad
 K=\operatorname{Graph}T_{\max},\quad
 T_{\max}=R_2^{-1}R_1=T_{\min}^{\top}.
$$
上标 $\top$ 表示 $CT^*C$。
对任意闭的 $A^{(2)}$ 不变空间
$$
 N\subseteq E\subseteq K,
$$
记其稠密定义闭图算子为 $T_E$。它包括定义域地与整个 $A'$ 交换。
已证每个这样的实现满足
$$
 \sigma(T_EU+F)=\mathbb C
 \quad\bigl(U\in(A')^\times,\ F\in A'\bigr).                 \tag{1.1}
$$
这里 $\operatorname{Dom}(T_EU)=\{x:Ux\in\operatorname{Dom}T_E\}
=\operatorname{Dom}T_E$，最后一步使用 U 和 $U^{-1}$ 都保持该域。

[R65 §1.3](R65-closed-critical-quotients-spectrum-and-core.md) 已给一般有界 pencil 与闭比例商的预解、值域接口；
[R201 §6](R201-positive-first-ratio-domain-obstruction-and-full-plane-spectrum.md) 已在其特定独立 first 比例商中证明全连续谱及弱零近似序列。
本文不重计这两个输入，保留真正态产生的全部中间图、任意交换单位/扰动、共同原核心及任意紧扰动的统一结论。

## 2. 有界 pencil 自动排除每个 regular point

固定 U、F、$\lambda$，置
$$
 B=F-\lambda I,\qquad
 L_E=T_EU+B,\qquad P=UR_1+BR_2\in A'.                    \tag{2.1}
$$
$L_E$ 闭且稠密定义：先用 U 的有界可逆性处理 $T_EU$，再加有界 B。
其两个实际等式为
$$
 L_ER_2y=Py\quad(y\in H),\qquad
 R_2L_Ex=Px\quad(x\in\operatorname{Dom}L_E).              \tag{2.2}
$$
第一式来自原有界列图已包含于 N；第二式来自 $E\subseteq K$。
两式都不是形式取消无界分母。

若 $L_E$ 有正下界 c，则
$$
 c\|R_2y\|\le\|Py\|\qquad(y\in H).
$$
$R_2$ 单射使 P 单射。又 $P=CP^*C$，所以
$\ker P^*=C\ker P=0$，即 P 值域稠密。
由 (2.2)，$L_E$ 值域稠密；闭算子有正下界又使其值域闭。
因此 $L_E$ 双射且逆有界，与 (1.1) 矛盾。

所以
$$
 \boxed{\sigma_{\mathrm{ap}}(T_EU+F)=\mathbb C.}          \tag{2.3}
$$
本证明不依赖一个尚未付清的有界模延拓定理。一般最小闭乘子未必具有这里的原有界列分母；本结论使用的正是 (2.2)。

## 3. 所有中间实现具有同一个点谱判据

首先 $P\ne0$。否则令 $V=-U^{-1}B\in A'$，便有
$R_1=VR_2$。$R_2$ 值域稠密给
$$
 N=\operatorname{Graph}V;
$$
$R_2$ 单射又使 $R_1x=R_2z$ 等价于 $z=Vx$，故
$K=\operatorname{Graph}V=N$，矛盾。

(2.2) 精确给
$$
 \boxed{R_2\ker P\subseteq\ker L_E\subseteq\ker P.}       \tag{3.1}
$$
由于 $R_2$ 单射，
$$
 \ker L_E\ne0\quad\Longleftrightarrow\quad\ker P\ne0.      \tag{3.2}
$$
因此固定 U、F 时，点谱集合与中间图 E 无关。这里没有把 (3.1) 擅自加强为三个核空间相等。

若 $\ker P=0$，则 $L_E$ 单射，P 稠密像和 (2.2) 使 $L_E$ 稠密像。
它不满射，否则闭图定理给有界逆，违反 (1.1)。
所以这个参数是连续谱点。
由此，每个中间实现的谱按通常互斥定义只分为点谱与连续谱，剩余谱为空。

若 $\ker P\ne0$，它是原 H 上非零真闭 A 不变空间。
真性来自 $P\ne0$。
它必无限维：若为非零有限维，A 在该空间上的限制既单射又拟幂零，有限维中不可能。
所以 $R_2\ker P$ 和每个 $\ker L_E$ 也无限维。
这没有无条件证明某个 pencil 的核实际非零。

## 4. 近似序列可统一取在原多项式真空核心

令
$$
 \mathcal D=\{p(A)1:p\in\mathbb C[z]\}.
$$
它是 $T_{\min}=X_h$ 的图核心，又由于 $R_2g_2=1$，有
$\mathcal D\subset R_2H$。
在 $\operatorname{Dom}T_{\min}$ 上，
$$
 L_{\min}=UT_{\min}+B,\qquad
 T_{\min}=U^{-1}(L_{\min}-B).
$$
这两式使图范数等价，所以 $\mathcal D$ 也是 $L_{\min}$ 的图核心。

**定理 4.1。** 对每组 U、F、$\lambda$，存在 $v_n\in\mathcal D$，使
$$
 \|v_n\|=1,\qquad v_n\rightharpoonup0,\qquad
 \|(T_EU+F-\lambda)v_n\|\longrightarrow0                 \tag{4.1}
$$
对全部中间图 E 同时成立。

证明分两种情形。

若 $\ker P=0$，第2节应用于最小图 N，证明 $L_{\min}$ 没有正下界。
若其核心上有正下界，该不等式会沿图范数极限延到全域，矛盾。
故可选核心单位向量 $v_n$，使 $\|L_{\min}v_n\|<1/n$。
任一弱收敛子列的弱极限 v 满足 $(v,0)\in\operatorname{Graph}L_{\min}$，因为闭线性图弱闭。
又 $\ker L_{\min}=0$，故 v=0。
有界序列的弱紧性遂给整个序列弱趋零。

若 $\ker P\ne0$，由第3节，线性空间 $R_2\ker P$ 无限维。
在其中逐次 Gram–Schmidt 可取正交单位序列 $e_n$，且
$L_{\min}e_n=0$。
以 $\mathcal D$ 的图核心性选 $w_n\in\mathcal D$，满足
$$
 \|w_n-e_n\|+\|L_{\min}w_n\|<1/n.
$$
归一化后得到 (4.1) 的单位弱零序列。

最后，所有 $T_E$ 都延拓 $T_{\min}$，且 U 保持最小域，故这些 $v_n$ 上的 $L_E$ 全与 $L_{\min}$ 相同。证毕。

换成多项式原式，存在 $p_n$ 使
$$
 \|p_n(A)1\|=1,\qquad p_n(A)1\rightharpoonup0,\qquad
 \|p_n(A)(Uh+(F-\lambda)1)\|\to0.                        \tag{4.2}
$$
未获得这些多项式的次数、系数或算子范数预算。

## 5. 任意有界紧扰动仍为全近似点谱

固定任意 $K_c\in\mathcal K(H)$，不要求 $K_c\in A'$。
紧算子把有界弱零序列送到范数零序列，因此 (4.1) 直接给
$$
 \boxed{
 \sigma_{\mathrm{ap}}(T_EU+F+K_c)=\mathbb C.
 }                                                       \tag{5.1}
$$
原 (4.1) 的序列对每个固定紧扰动均适用，所以谱也等于整个复平面。

还可同时处理伴随。每个 $T_E^\top$ 的图为 $E^\beta$，其中
$$
 \beta((x,z),(x',z'))=B(x,z')-B(z,x').
$$
因为 $N^\beta=K$、$K^\beta=N$，有
$N\subseteq E^\beta\subseteq K$。
交换子的 C 对称性又使 $E^\beta$ 保持 A 不变。
所以 $T_E^\top$ 也是同一类中间实现。

U 有界可逆及完整域交换给
$$
 (T_EU+F-\lambda)^\top=T_E^\top U+F-\lambda.
$$
而 $K_c^\top=CK_c^*C$ 仍紧。
对转置算子使用 (5.1)，再用 C 变换，得到
$(T_EU+F+K_c-\lambda)^*$ 也有弱零单位近似核序列。

因此每个参数既不是上半 Fredholm 点，也不是下半 Fredholm 点。
确实，闭值域及有限维核会给
$\|Lx\|\ge c\,\operatorname{dist}(x,\ker L)$；
弱零单位序列到有限维核的距离趋1，与其像趋零矛盾。
对伴随应用同一事实并用闭值域对偶，排除下半 Fredholm 情形。

第3节关于点谱、连续谱的具体分类只针对交换扰动 F；这里没有把该分类外推到任意紧扰动后的核。

## 6. 对剩余研究的限制

原有界列结构已经排除了这个真秩二图夹层中的全部 regular points，故不能再靠某个平移的正下界来启动有界逆补全。
结论同时说明，仅添加一个紧修正也无法制造预解点。
它仍没有给真实正见证的共同真空域，没有提供紧后退链所需的范数预算，也没有断言上述非零 pencil 之一必有核。
普通复 Hilbert ISP 的完成标准仍未达到。
