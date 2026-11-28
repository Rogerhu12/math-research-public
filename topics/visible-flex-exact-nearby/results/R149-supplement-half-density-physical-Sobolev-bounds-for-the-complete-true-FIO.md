# 已证明：真半密度给出全频物理 Sobolev 界，含均值和低输出

角周期 $l=\pi/2$，$L^2$ 内积按 $d\phi/l$，$n_j=4j$ 带原符号。固定真实径向点及共同的真度一提升 $P$，$p=P'>0$。可取原 [WUB](R133-supplement-complete-dyadic-Airy-source-blocks-and-original-strong-window.md) 的近根 $X$ 或远区任一真 $P_\sigma$。设 $S$ 为任意输入指标集合，
$$
 T_a f(\phi)=\sum_{j\in S} e^{in_j P(\phi)} a_j(\phi) f_j .
$$
允许 $a_j$ 为固定有限维复矩阵，保留原行、独立输入及正确内积。本结果不要求频率相邻的两个 $a_j$ 有任何差分界。

## 一阶角变差和准确单位

令 $U_P f=\sqrt p\,f\circ P$。它是归一化 $L^2$ 上的酉算子。令 $b_j=a_j/\sqrt p$，全圆比较微分可用下列常数：
$$
 \mathcal V_P(a)=
 \min\left\{
 \sup_{j\in S}\left\|\int b_j\,d\phi/l\right\|,
 \sup_{j\in S}\left\|\int p b_j\,d\phi/l\right\|\right\}
 +\frac12\int_0^l\sup_{j\in S}\|b'_j(\phi)\|\,d\phi .
                                                         \tag{1}
$$
则 $\|T_a\|_{\ell^2(S)\to L^2}\le\mathcal V_P(a)$。式中最后为未归一化积分；若每格权重是 $\Delta\phi/l$，其前因子为 $l/2=\pi/4$。

证明：在 $0<t<l$ 令 $K(t)=1/2-t/l$，作周期延拓。其分布导数为周期点质量减 $1/l$，故 $b_j(\phi)=\int b_j/l+\int K(\phi-t)b'_j(t)dt$。任一固定 $t$ 的矩阵族 $b'_j(t)$ 作为频率对角算子之范数为 $\sup_j\|b'_j(t)\|$。右乘此对角，再经 $U_P$，左乘公共函数 $K(\phi-t)$，范数至多上式一半。积分给 (1) 的第一种均值。另一证明先经 $U_P^{-1}$，在 $x=P(\phi)$ 对 $b_j(P^{-1}x)$ 使用同一公式，其均值是 $\int p b_j\,d\phi/l$，变差积分因 $dx=p\,d\phi$ 准确不变。取两套完整界的较小者。论证先对有限输入成立，有限和稠密给出全 $S$。当幅是 $a_j(\phi)=A(\phi)D_j$ 时，还可单独用 $\|A/\sqrt p\|_{\infty}\sup_j\|D_j\|$；若从总幅中扣取此项，应先做同一 $P$ 上的带号差。

## 物理负阶及所有输出

设输入没有 $j=0$。定义 $A_{0,0}=a$，越界指标取零，逐完整带号幅递推
$$
 A_{k+1,m}=A_{k,m-1}/p-\partial_\phi(A_{k,m}/p)
 \qquad(0\le m\le k+1).
$$
令 $D_s$ 乘 $|n_j|^s$，$\Lambda$ 是原输出物理 Bessel 乘子。逐列使用
$e^{inP}a=(\partial_\phi(e^{inP}a/p)-e^{inP}\partial_\phi(a/p))/(in)$ 得
$$
 T_a=\sum_{m=0}^k\partial_\phi^m T_{A_{k,m}}D_{(in_j)^{-k}} .
$$
因此以 $(k+1)$ 个输出的正交直和为值域，令
$$
 C_k=\mathcal V_P\!\left(
      \operatorname{col}_{m=0}^k\{ A_{k,m}/\sqrt{\binom{k}{m}}\}\right).
$$
则 $\|\Lambda^{-k}T_a D_k\|\le C_k$。确实，余下输入仅有模一符号。在每一输出 $\xi=4h$ 上，左接收行的平方范数恰为
$\sum_m\binom{k}{m}|\xi|^{2m}/(1+\xi^2)^k=1$。$h=0$ 时准确留下第零项。没有删除输出均值、低频泄漏或使用带宽平方根。$C_k$ 只用 $a,p$ 到 $k+1$ 阶角导，即相位到 $k+2$ 阶。对 $d=k+\theta$，$0\le\theta\le1$，在有限频率输入上对 $\Lambda^{-(k+z)}T_a D_{k+z}$ 应用三线引理，边界复幂在实际输入/输出上酉，继而稠密延拓，得
$$
 \|\Lambda^{-d}T_aD_d\|\le C_k^{1-\theta}C_{k+1}^{\theta}.            \tag{2}
$$
可直接将任意有界输入滤子或已知权写入 $a_j$ 以后再作 (1)–(2)，也可先在有限输入取界后单调扩展。对 $5/3,2$ 等 WUB 窗最多用三阶角幅；无需另付返回 $\phi$ 的负阶 composition。

## 对原真源的使用

同一 $r$ 上可按 $|n_j|^{2/3}\rho$ 将输入分作近根/远区，使该频率集合与 $\phi$ 无关。近区用原完整 genuine ODE、原独立两列和 $X$；远区用 WUB 的真实 Jost 幅分别搭配两个相位和原 $S_n$。在有界重叠区任选固定归属亦可，因为这只是估已存在的源。若分组正交，输入分组的接收费可按各整组范数的平方和开根。对共用同一输入的两远相位仍保留其联合作用或用三角界；不同相位从不凭列名相减。

具体实现可按同一 $j$ 或覆盖一组 $j$ 的有向区间、同一物理角区间，先积分复向量的带号均值再取范数；变差项在每角格先取所有频率的最大值再积分。`fourfold_codazzi_true_fio_physical_band.py` 给出单输入、复堆叠的完整闭格算术，真实频域覆盖和每一幅的来源仍由相应消费者提供。原图中的非局部 $J$、$I$、输入密度、归一化和末端荷只在规定次序接收，不据 (1) 与它们交换。真实普通 $dr$ 源可对 (2) 的点态算子界平方积分；零长度接缝单独接收。完整均值轨道仍须执行其本身的方程。

另一个现成的数值后果是 [整根片](R149-supplement-small-true-root-label-H1-on-the-complete-physical-root-patch.md) 的两真相位 $C_P f=f\circ P$ 在 $L^2,H^1$ 上，连同逆算子，均有范数 $<1+1/180000$。因为 $|p-1|\le1/93750$，换元后值与角导平方分别有权 $1/p,p$，两者及其倒数均 $\le(1-1/93750)^{-1}<(1+1/180000)^2$。该结论控制范数畸变，未以有限相位替入无限指数。整个原 $B$ 的返回和剩余高频小量仍有各自独立的真实数值义务。
