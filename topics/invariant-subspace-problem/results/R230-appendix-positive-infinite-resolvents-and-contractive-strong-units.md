# R230 附录：无穷正预解式乘积的分类与收缩强单位

日期：2026-11-12（UTC）。独占作者：normal_next。

状态：以下无穷乘积分类及强主理想性质有完整证明。它处理的是此前尚未分类的**规范收缩型非负一阶预解式乘积**，不是把它们等同于单个一阶半群。非零情形自动给 R244 的强主理想锚；指定输入的配对域条件仍未构造。本文不重做 R240 的固定向量反例，也不声称一般正常湮灭者已排除。

## 1. 实际设置和主结论

沿用原 Haar 表示，记 $\mathfrak C=\{A\}'$、$\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$。对非负实行 $b\in\ell^2_+$，令
$$
Z_b=\sum_{j\ge0}b_jV_j,
\qquad \mathsf E(b)=e^{-Z_b}.
\tag{1.1}
$$
$Z_b$ 为 R125/R128 的真实闭极大增生一阶算子。已证的[实际半群附录](../results/R240-appendix-positive-first-semigroups-fail-paired-regularization.md)给
$$
\mathsf E(b)\in\mathfrak C,\qquad \|\mathsf E(b)\|\le1,
\qquad \mathsf E(b)\mathsf E(d)=\mathsf E(b+d).
\tag{1.2}
$$
所有实际 carry 都包含在这些算子中。

给定任意可数族 $b^{(\nu)}\in\ell^2_+$，定义规范收缩预解式和有限乘积
$$
Q_\nu=(I+Z_{b^{(\nu)}})^{-1},\qquad
P_n=\prod_{\nu=1}^nQ_\nu,
\tag{1.3}
$$
以及非负逐坐标总行
$$
b^{[n]}=\sum_{\nu=1}^n b^{(\nu)},\qquad
b_j=\sum_{\nu\ge1}b_j^{(\nu)}\in[0,\infty].
\tag{1.4}
$$
正时间和正预解参数可吸收到各行中：
$\lambda(\lambda I+Z_d)^{-1}=(I+Z_{d/\lambda})^{-1}$，$\lambda>0$。
不包含另加的发散标量重标定、复杂行或符号相消。

**主定理。**

1. 若 $b\notin\ell^2$，则 $P_n\to0$ 于 WOT。因此不存在非零弱子列极限；本项不自动断言 SOT 收敛。
2. 若 $b\in\ell^2$，则 $P_n$ 强收敛到一个非零收缩 $P\in\mathfrak C$。它具有实际随机混合表示
   $$
   \boxed{P x=\mathbb E\big[\mathsf E(c)x\big],\qquad
   c=\sum_{\nu\ge1}\xi_\nu b^{(\nu)}\in\ell^2\quad\text{几乎处处},}
   \tag{1.5}
   $$
   其中 $\xi_\nu$ 为独立的均值 1 指数随机变量。期望是对每个 $x\in H$ 的 Hilbert 空间 Bochner 积分，不要求 $B(H)$ 中的范数可测性。
3. 在第 2 项中，存在明确有界交换子 $F_n\in\mathfrak C$，使
   $$
   \boxed{\|PF_n\|\le1,\qquad PF_n\longrightarrow I\quad\text{SOT}.}
   \tag{1.6}
   $$
   因而
   $$
   \boxed{I\in\overline{P\mathcal A}^{\mathrm{SOT}}.}
   \tag{1.7}
   $$
   $P$ 在任意有限放大闭不变子商上都单射且稠密像，特别在全 $H$ 上如此。

因此非零弱极限的准确判据为 $\sum_\nu b^{(\nu)}\in\ell^2$。非零极限一般是 (1.5) 的混合；本文不把这个混合简化成某个单一 $\mathsf E(c_0)$。

## 2. 预解式的实际 Laplace 公式

对 $d\in\ell^2_+$，$t\mapsto\mathsf E(td)$ 是生成元 $-Z_d$ 的强连续收缩半群。因此
$$
\boxed{(I+Z_d)^{-1}x
=\int_0^\infty e^{-t}\mathsf E(td)x\,dt.}
\tag{2.1}
$$
这里也可以直接支付域：先对 $x\in\operatorname{Dom}Z_d$，使用完整生成元域交换及
$$
-\frac d{dt}\big(e^{-t}\mathsf E(td)x\big)
=(I+Z_d)e^{-t}\mathsf E(td)x.
$$
函数及其 $Z_d$ 像均被可积指数函数控制，故闭性允许在图域中积分，得到右侧属于 $\operatorname{Dom}Z_d$ 且乘 $I+Z_d$ 后为 $x$。再以域内向量逼近任意 $x\in H$，用闭性和收缩界延伸。极大增生性保证逆的唯一性。

所有 $Q_\nu$ 属于 $\mathfrak C$ 并两两交换，$\|Q_\nu\|\le1$。用 (2.1)、有界向量积分的 Fubini 定理和 (1.2)，得到有限乘积的准确表示
$$
\boxed{P_nx
=\mathbb E\big[\mathsf E(c_n)x\big],\qquad
c_n=\sum_{\nu=1}^n\xi_\nu b^{(\nu)}.}
\tag{2.2}
$$
每个样本的 $c_n$ 都属于 $\ell^2_+$。没有对无界 $Z_{b^{(\nu)}}$ 作形式乘积或交换未付域的自然词。

## 3. 随机非负总行的准确平方和判据

下面只用指数变量的
$$
\mathbb E\xi_\nu=1,\quad
\mathbb E\xi_\nu^2=2,
\quad \mathbb E(\xi_\nu\xi_\mu)=1\quad(\nu\ne\mu).
$$
Tonelli 给
$$
\boxed{
\mathbb E\|c_n\|_2^2
=\|b^{[n]}\|_2^2+\sum_{\nu=1}^n\|b^{(\nu)}\|_2^2
\le2\|b^{[n]}\|_2^2.
}
\tag{3.1}
$$
最后一步使用各行非负，因此
$\sum_\nu\|b^{(\nu)}\|_2^2\le\|\sum_\nu b^{(\nu)}\|_2^2$。

若 $b\in\ell^2$，逐坐标 $c_n\uparrow c$，由单调收敛，
$$
\mathbb E\|c\|_2^2\le2\|b\|_2^2<\infty.
\tag{3.2}
$$
故 $c\in\ell^2$ 几乎处处，且对这些样本 $c_n\to c$ 于 $\ell^2$。

反之，设 $b\notin\ell^2$。非负单调收敛给 $\|b^{[n]}\|_2\to\infty$。对任意满足 $m_n=\|b^{[n]}\|_2>0$ 的 $n$，置
$$
w_\nu=\left\langle b^{(\nu)},\frac{b^{[n]}}{m_n}\right\rangle_{\ell^2}\ge0,
\qquad W_n=\sum_{\nu=1}^n w_\nu\xi_\nu.
$$
于是 $\sum_\nu w_\nu=m_n$、$W_n\le\|c_n\|_2$，且
$$
\mathbb EW_n=m_n,\qquad
\mathbb EW_n^2=m_n^2+\sum_\nu w_\nu^2\le2m_n^2.
$$
Cauchy–Schwarz 直接给
$$
m_n\le\frac{m_n}{2}
+(\mathbb EW_n^2)^{1/2}
\mathbb P(W_n\ge m_n/2)^{1/2}.
$$
因此
$$
\boxed{\mathbb P(\|c_n\|_2\ge m_n/2)\ge1/8.}
\tag{3.3}
$$
由于 $\|c_n\|_2$ 逐样本单调，(3.3) 和 $m_n\to\infty$ 迫
$\mathbb P(\|c\|_2=\infty)\ge1/8$。

事件 $\{c\in\ell^2\}$ 是独立变量序列的尾事件：改变有限多个 $\xi_\nu$ 只改变一个 $\ell^2$ 向量，不能改变总行是否在 $\ell^2$ 中。独立尾事件的零一律因而给
$$
\boxed{b\notin\ell^2\quad\Longrightarrow\quad
\mathbb P(c\notin\ell^2)=1.}
\tag{3.4}
$$
这里零一律只使用：该事件独立于每个有限变量生成的 $\sigma$ 代数，继而独立于全体变量生成的 $\sigma$ 代数；它本身属于后者，所以其概率等于自身平方。无需对随机 $\ell^2$ 范数作不存在的一阶有限矩假设。

## 4. 实际无穷乘积的强极限与弱零分类

[可数正半群乘积的实际分类](../results/R240-appendix-countable-positive-first-semigroup-products.md)已经证明：对任意非负逐行累加 $d_n\uparrow d$，若 $d\in\ell^2$，则 $\mathsf E(d_n)\to\mathsf E(d)$ 强；若 $d\notin\ell^2$，则 $\mathsf E(d_n)\to0$ 弱。后者包含某一坐标无限或总行无界时的范数趋零情形，以及有界非平方可和时的实际尾弱零情形。

对每个随机样本，将该定理用于 $d_n=c_n$。若 $b\in\ell^2$，(3.2) 给几乎处处强收敛；对每个 $x$，收缩界与 Hilbert 值支配收敛在 (2.2) 中给
$$
P_nx\longrightarrow\mathbb E[\mathsf E(c)x]=Px.
\tag{4.1}
$$
向量的可测性可先在有限变量的 $c_n$ 上用强连续性取得，再由其逐样本强极限取得。$P$ 是收缩，且 $\mathfrak C$ 强闭，故 $P\in\mathfrak C$。

若 $b\notin\ell^2$，(3.4) 给几乎处处的弱收敛零。对固定 $x,y$，
$$
|\langle\mathsf E(c_n)x,y\rangle|\le\|x\|\|y\|.
$$
标量支配收敛与 (2.2) 给 $\langle P_nx,y\rangle\to0$，即主定理第 1 项。这里没有从逐样本 WOT 收敛推出逐样本 SOT 收敛。

## 5. 非零情形的尾乘积强趋单位

以下固定 $b\in\ell^2$。令
$$
b_{>N}=\sum_{\nu>N}b^{(\nu)}\in\ell^2_+.
$$
逐坐标支配收敛给 $\|b_{>N}\|_2\to0$。对从第 $N+1$ 个因子开始的同一无穷乘积，前节给收缩强极限
$$
K_N=\operatorname*{SOT-lim}_{m\to\infty}
\prod_{\nu=N+1}^m Q_\nu
=\mathbb E\left[\mathsf E\left(\sum_{\nu>N}\xi_\nu b^{(\nu)}\right)\right].
\tag{5.1}
$$
由有限积取强极限，有
$$
\boxed{P=P_NK_N=K_NP_N.}
\tag{5.2}
$$

为了定量证明 $K_N\to I$，令 $g$ 为有限 Walsh 多项式，$X_g\in\mathcal A$ 为真实有界乘子，$X_g1=g$。R125 的完整域交换与 $V_j1=\chi_j$ 给
$$
1\in\operatorname{Dom}Z_d,\quad
Z_d1=\sum_jd_j\chi_j,\quad
g\in\operatorname{Dom}Z_d,\quad
Z_dg=X_gZ_d1.
$$
故
$$
\|Z_dg\|\le\|X_g\|\|d\|_2.
\tag{5.3}
$$
在这个已付域的输入上积分半群微分式，收缩性给
$$
\boxed{\|(\mathsf E(d)-I)g\|
\le\int_0^1\|\mathsf E(td)Z_dg\|\,dt
\le\|X_g\|\|d\|_2.}
\tag{5.4}
$$
对 (5.1) 的尾随机行应用 (3.2)，继而用 Cauchy–Schwarz，得到
$$
\boxed{\|(K_N-I)g\|
\le\sqrt2\,\|X_g\|\,\|b_{>N}\|_2.}
\tag{5.5}
$$
有限 Walsh 多项式稠密且所有 $K_N$ 是收缩，因此
$$
\boxed{K_N\longrightarrow I\quad\text{SOT}.}
\tag{5.6}
$$
特别在 $g=1$ 时，右侧准确为 $\sqrt2\|b_{>N}\|_2$。

## 6. 明确的收缩强近似单位

对 $0<\varepsilon\le1$，令
$$
Q_{\nu,\varepsilon}=(I+\varepsilon Z_{b^{(\nu)}})^{-1},
$$
$$
F_{N,\varepsilon}
=\prod_{\nu=1}^N
\left[\varepsilon^{-1}I+(1-\varepsilon^{-1})Q_{\nu,\varepsilon}\right]
\in\mathfrak C.
\tag{6.1}
$$
每个括号确为有界处处定义算子，并且准确等于
$(I+Z_{b^{(\nu)}})Q_{\nu,\varepsilon}$：预解式的像位于生成元的真实域，而
$$
Z_{b^{(\nu)}}Q_{\nu,\varepsilon}
=\varepsilon^{-1}(I-Q_{\nu,\varepsilon})
$$
为有界算子。因此可按真实逆关系消去，得到
$$
\boxed{
PF_{N,\varepsilon}
=K_N\prod_{\nu=1}^NQ_{\nu,\varepsilon},\qquad
\|PF_{N,\varepsilon}\|\le1.
}
\tag{6.2}
$$
这一步没有把无界乘积 $\prod(I+Z_{b^{(\nu)}})$ 当成全域算子。

用 (2.2) 的有限 Laplace 表示及 (5.4)，对每个有限 Walsh $g$，
$$
\left\|\left(\prod_{\nu=1}^NQ_{\nu,\varepsilon}-I\right)g\right\|
\le\|X_g\|\,\mathbb E\|\varepsilon c_N\|_2
\le\sqrt2\,\varepsilon\|X_g\|\|b\|_2.
\tag{6.3}
$$
与 (5.5)、(6.2) 合并，得到完全统一的核心估计
$$
\boxed{
\|(PF_{N,\varepsilon}-I)g\|
\le\sqrt2\,\|X_g\|
\big(\|b_{>N}\|_2+\varepsilon\|b\|_2\big).
}
\tag{6.4}
$$
因此明确取
$$
\boxed{F_n=F_{n,1/n}\quad(n\ge1)}
\tag{6.5}
$$
即得 $\|PF_n\|\le1$ 和 $PF_n\to I$ 强。核心上的收敛由 (6.4)，全空间收敛由稠密性和统一收缩界支付，不需要按未知尾速率另取子列。

每个固定 $F_n\in\mathfrak C$ 由 R88 可被有界多项式强逼近；左乘固定 $P$ 后，$PF_n$ 属于 $\overline{P\mathcal A}^{\mathrm{SOT}}$。再用该集合的闭性与 (6.5)，得到 (1.7)。

本文的统一收缩序列位于 $P\mathfrak C$。这里只从 R88 推出 $P\mathcal A$ 的强闭包含 $I$，没有额外声称其多项式逼近也保持相同的收缩范数；下文的正常泛函应用直接使用 $P\mathfrak C$ 中的 (6.5)。

## 7. 全部有限放大不变子商上的单射与稠密像

取任意有限 $d$，以及闭 $A^{(d)}$ 不变旗 $N\subset M\subset H^{(d)}$。R88 保证 $P,F_n,PF_n$ 的对角放大都保持该旗。它们在商 $Q=M/N$ 上的诱导算子保留代数乘法和交换，且 (6.5) 给
$$
\|(PF_n)_Q\|\le1,\qquad (PF_n)_Q\longrightarrow I_Q\quad\text{SOT}.
\tag{7.1}
$$
强收敛可在正交商实现 $M\ominus N$ 上直接压缩已有强极限。

每个 $(PF_n)_Q=P_Q(F_n)_Q$ 的像属于 $\operatorname{Ran}P_Q$，所以 (7.1) 给其稠密性。若 $P_Qx=0$，交换性又给
$$
(PF_n)_Qx=(F_n)_QP_Qx=0
$$
对所有 $n$ 成立，(7.1) 迫 $x=0$。因此
$$
\boxed{P_Q\text{ 单射且稠密像。}}
\tag{7.2}
$$
取 $M=H,N=0$ 即证 $P$ 非零、单射、稠密像，完成主定理第 2 项的非零断言。这里的子商结论来自真实强近似单位 (7.1)，没有仅从环境中的单射稠密像推到未知子商。

## 8. 对 R244 的准确用法

设 $S=S_N$ 或 $S_Y$，或任意已经证明全 $H$ 单射的 $S\in\mathfrak C$。假设正有限秩见证
$$
\rho=\sum_{i=1}^d f_i\otimes f_i,\qquad
\phi(S\mathcal A)=0
$$
存在。只要能够选择上述非负行族，使
$$
\sum_\nu b^{(\nu)}\in\ell^2,
\qquad
\boxed{Pf_i\in\operatorname{Dom}X_{Cf_i}\quad(1\le i\le d),}
\tag{8.1}
$$
R244 已给 $\phi(PF)=0$ 对每个 $F\in\mathfrak C$ 成立。代入 (6.5)，得
$$
0=\lim_n\phi(PF_n)=\phi(I)=\operatorname{Tr}\rho,
$$
矛盾。

所以对这一明确的无穷预解式类，**一旦配对域条件成立，就无需另证 $\phi(P)\ne0$**。强单位锚由本文自动提供。没有要求 $PH\subset\operatorname{Dom}X_{Cf_i}$，仍然只要求指定的 $d$ 个输入。

正迹类的可数版本同样成立，但另须支付 R244 的
$$
\sum_i\|X_{Cf_i}Pf_i\|<\infty.
\tag{8.2}
$$
在此条件下 R244 的分解给 $\phi(PF_n)=0$；(6.5) 的**统一收缩强收敛**允许任意正常迹类泛函取极限，因此仍有 $\phi(I)=0$。没有误用迹类泛函对无界强逼近网的连续性。

另外，若把所有行同时乘 $s>0$，对应无穷乘积 $P(s)$ 满足
$$
\|(P(s)-I)g\|\le\sqrt2\,s\|X_g\|\|b\|_2
$$
对有限 Walsh $g$ 成立，所以 $P(s)\to I$ 强且 $\|P(s)\|\le1$。这给状态值趋于迹的另一种锚；它**不说明** (8.1) 的配对域在改变 $s$ 后保持。

## 9. 剩余的开放步骤

本文完成的是非负规范预解式无穷乘积的实际极限及强主理想结构。它没有证明 (8.1) 可对任意假想正常见证达成。

总行不平方可和时，乘积弱趋零，不能给非零强单位或状态锚。总行平方可和时，极限是有界随机混合并有明确强单位；但单个混合分量的指定配对域失败，既不能自动推出混合失败，也不能自动推出混合成功。任何这类结论还需要独立的图域或矩估计。

本文也不讨论非单调复杂行、预解式有限线性组合、额外标量重标定以及其他交换子。这些不应由上述非负概率表示擅自纳入。普通 ISP 和一般 Haar 正常湮灭者排除仍未完成。
