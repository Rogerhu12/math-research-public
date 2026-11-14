# 原连续尾完整 graph 的相对孔共轭导数仍有四次指数成本

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：已证明，中间结论。** 对原 $N/Y$ 两个真实有限头和原连续尾 $b_j=(j+1)^{-2}$，完整 first-head Gram 的相对孔交换子，已经有 $\exp((175/32+o(1))d^4)$ 的下界。证明保留实际物理尾，未用一个任意抽象坏 Gram，也未把巨大 Jordan 条件数直接当成核内下界。

本稿只排除对**全部完整 graph 源**使用 $\exp(O(d^3))$ 的相对孔共轭估计。构造的坏方向全部位于低孔真实零核；把该零核先作完整 Schur 消去后，实际 boundary source、固定测试和负图上的相对估计仍未由本稿决定。

## 1. 原对象和精确共轭身份

取 $m\ge8$、$d=2^m$。令 $A=A_m$ 为原 $T_N$ 或 $T_Y$ 的真实前 $m$ 位头，保持全部 carry 和原物理内积。令
$$
D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j
$$
作用于原平方自由尾空间
$$
\mathcal H_{\rm hc}=\bigoplus_{p\ge0}\mathcal H_p.
$$
这里 $E_j$ 是逐位删除，$D$ 因系数属于 $\ell^1$ 而有界。

沿用 [R239 真实头稿 §§1–3](../results/R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) 的归一链
$$
A=VJ_dV^{-1},\qquad V=1\oplus V_+,\qquad J_de_j=e_{j-1}.
$$
记
$$
N_h=\operatorname{diag}(0,\ldots,d-1),\qquad
Z=VN_hV^{-1}.
\tag{1.1}
$$
则
$$
[A,Z]=A,\qquad \operatorname{spec}Z=\{0,\ldots,d-1\}.
\tag{1.2}
$$

令 $\mathsf N$ 为尾孔数算子。对任意整数 $q\ge0$，在同一个闭 first-head 源空间
$$
\mathcal F_{m,q}=\ker D^d\cap\mathcal H_{\le q}
$$
上定义完整 graph
$$
\mathcal T_qf=\sum_{j=0}^{d-1}(Ve_j)(-D)^jf,\qquad
\Gamma_q=\mathcal T_q^*\mathcal T_q.
\tag{1.3}
$$
由原 first-head 规范，$e_0^*\mathcal T_qf=f$，故 $\Gamma_q\succeq I$。逐头方程给
$$
\operatorname{Ran}\mathcal T_q
=\mathcal K_{\le q}
:=\ker(A+D)\cap(\mathbb C^d\otimes\mathcal H_{\le q}).
\tag{1.4}
$$
$\mathcal F_{m,q}$ 是按孔数约化的空间，且 $\mathsf N$ 在其上有界，所以以下共轭和导数均是固定 $m,q$ 的有界算子恒等式，不涉及无界交换子的域选择。

由于 $[\mathsf N,D]=-D$，
$$
e^{\theta\mathsf N}\mathcal T_qe^{-\theta\mathsf N}
=\mathcal T_q(e^{-\theta}D)
=e^{-\theta Z}\mathcal T_q.
\tag{1.5}
$$
取伴随时必须同时反转两个尾共轭的方向。由此得
$$
\boxed{
e^{\theta\mathsf N}\Gamma_qe^{-\theta\mathsf N}
=\mathcal T_q^*e^{\theta Z^*}e^{-\theta Z}\mathcal T_q.
}
\tag{1.6}
$$
特别，
$$
\boxed{
[\mathsf N,\Gamma_q]=\mathcal T_q^*(Z^*-Z)\mathcal T_q.
}
\tag{1.7}
$$
设 $\mathcal V_q=\mathcal T_q\Gamma_q^{-1/2}$；它是从原源空间到真实核 $\mathcal K_{\le q}$ 的等距满射。因此
$$
\boxed{
\mathcal C_{m,q}
:=\Gamma_q^{-1/2}[\mathsf N,\Gamma_q]\Gamma_q^{-1/2}
=\mathcal V_q^*(Z^*-Z)\mathcal V_q.
}
\tag{1.8}
$$
右侧是**真实物理核内的压缩**。单独知道 $\|Z\|$ 很大，尚不能推出 $\|\mathcal C_{m,q}\|$ 很大；下面支付这一点。

## 2. 在原全异连续尾中构造等有效权的物理不变块

置
$$
n=d-1,\qquad a=(m+2n)^{-2}.
\tag{2.1}
$$
把原尾的前 $2n$ 位 $m,\ldots,m+2n-1$ 分为 $n$ 个互不相交的两位块。对一个块的两个实际删除权 $b,c$，有 $b,c\ge a$。置
$$
s=(b^2+c^2)^{1/2},\qquad
g=s^{-1}(b\,|10\rangle+c\,|01\rangle),\qquad
h=s^{-1}(c\,|10\rangle-b\,|01\rangle).
$$
$g,h$ 是该块 one-hole 空间中的正交单位向量，且
$$
Dg=s\,|00\rangle,\qquad Dh=0.
$$
因 $a\le s$，向量
$$
\phi=\frac as g+\sqrt{1-\frac{a^2}{s^2}}\,h
\tag{2.2}
$$
满足
$$
\|\phi\|=1,\qquad D\phi=a\,|00\rangle.
\tag{2.3}
$$

所以每个物理子空间 $\operatorname{span}\{|00\rangle,\phi\}$ 都等距于一个二态空间，保孔次数，并在**实际 $D$** 下不变。把这些子空间张量，其他尾位取真空，得到原平方自由空间中的等距、次数保持的 $D$ 不变子空间，限制算子准确为
$$
a\sum_{i=1}^{n}E_i.
\tag{2.4}
$$
这里不声称该子空间在 $D^*$ 下不变；下文只用实际 $D$ 不变性构造真核，最后在完整物理核中作正交压缩。

令 $\omega_j$ 为这 $n$ 个有效位的归一对称 $j$ 孔向量，$0\le j\le n$。逐集合计数给
$$
D\omega_j=a\sqrt{j(n-j+1)}\,\omega_{j-1}.
\tag{2.5}
$$

## 3. 覆盖全部原头向量的真实核嵌入

对任意 $h\in\mathbb C^d$，定义
$$
\mathcal Rh
=\sum_{j=0}^{d-1}
\frac{(-A)^jh}{a^j\sqrt{j!(n)_{\underline j}}}\otimes\omega_j,
\qquad
(n)_{\underline j}=n(n-1)\cdots(n-j+1).
\tag{3.1}
$$
$j=0$ 的分母按 $1$ 解释。由 (2.5)，相邻两项的 $A$ 和 $D$ 作用逐项抵消；最后一项的头作用是 $A^d=0$。故
$$
\boxed{
(A+D)\mathcal R=0,\qquad
\operatorname{Ran}\mathcal R\subset\mathcal K_{\le d-1}.
}
\tag{3.2}
$$
其 $j=0$ 项是 $h\otimes\omega_0$，所以 $\mathcal R$ 单射。不同 $j$ 的尾孔层正交，完整物理源 Gram 为
$$
H:=\mathcal R^*\mathcal R
=\sum_{j=0}^{d-1}c_j(A^j)^*A^j,\qquad
c_j=\frac1{a^{2j}j!(n)_{\underline j}},
\qquad H\succeq I.
\tag{3.3}
$$
这一步没有把物理源 Gram 替换为单位阵。

### 3.1 嵌入的条件数只有 $\exp(O(m^2))$

[R234 真实四次头幂](../results/R234-appendix-quartic-head-powers-and-super-four-thirds-hole-weights.md)，亦见 [全核零占据稿 §4](2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md)，在原物理头上给
$$
\|A^j\|\le6^j,\qquad
\|A^j\|\le6^je^{-\gamma j^4}\quad(j\ge2m),
\qquad
\gamma=\frac{770}{16^4}>\frac1{100}.
\tag{3.4}
$$
这里 $m\ge8$ 使旧阈值 $\max(2m,16)$ 等于 $2m$。

置
$$
\tau=\log(36/a^2)=\log36+4\log(m+2d-2)
$$
及
$$
\boxed{
C_m'=(2m+102)\exp\bigl(2m\tau+3\tau^{4/3}\bigr).
}
\tag{3.5}
$$
因 $j!(n)_{\underline j}\ge1$，
$$
\|H\|
\le\sum_{j<2m}e^{\tau j}
+\sum_{j\ge2m}e^{\tau j-2\gamma j^4}.
$$
实变量最大值满足
$$
\tau x-\gamma x^4
\le\frac3{4^{4/3}\gamma^{1/3}}\tau^{4/3}
\le3\tau^{4/3}.
$$
又
$$
\sum_{j\ge0}e^{-\gamma j^4}
\le\sum_{j\ge0}e^{-\gamma j}
=\frac1{1-e^{-\gamma}}<102.
$$
于是
$$
\boxed{I\preceq H\preceq C_m'I,\qquad \log C_m'=O(m^2).}
\tag{3.6}
$$
$C_m'$ 与 $q$ 无关。其粗常数足够，因为下面的头斜性具有 $d^4$ 级指数。

## 4. 真核压缩保留头分级的斜性

由 $[A,Z]=A$，
$$
ZA^j=A^jZ-jA^j.
\tag{4.1}
$$
令 $H_1=\sum_jj c_j(A^j)^*A^j$。由 (3.3)–(4.1)，
$$
\mathcal R^*Z\mathcal R=HZ-H_1,\qquad
\mathcal R^*Z^*\mathcal R=Z^*H-H_1.
$$
所以
$$
\boxed{
\mathcal R^*(Z^*-Z)\mathcal R=Z^*H-HZ.
}
\tag{4.2}
$$
次数加权项在同一物理 Gram 中**准确抵消**。

$\widehat{\mathcal R}=\mathcal RH^{-1/2}$ 是等距嵌入。记
$$
Z_H=H^{1/2}ZH^{-1/2}.
$$
则
$$
\widehat{\mathcal R}^*(Z^*-Z)\widehat{\mathcal R}
=Z_H^*-Z_H.
\tag{4.3}
$$
对 $q\ge d-1$，(3.2) 和 (1.8) 因而给
$$
\boxed{\|\mathcal C_{m,q}\|\ge\|Z_H^*-Z_H\|.}
\tag{4.4}
$$

## 5. 真实头迹障碍及其相对 Gram 后果

沿用已经证明的 [真实头分级迹下界 §3](2026-11-12-boundary-true-head-grading-condition-lower-bound-boundary-next.md)。为避免把相似条件数下界误用到本稿所需的次数算子，下面重述其直接输入。

原头的最高位物理分块准确为
$$
A=
\begin{pmatrix}
A_{m-1}&m^{-2}I+R\\
0&A_{m-1}
\end{pmatrix},
\qquad
\|R\|\le26\eta_{m-2},
\tag{5.1}
$$
其中
$$
-\log\eta_{m-2}
=\frac{175}{32}d^4-\frac{315}{32}d^3+75d.
\tag{5.2}
$$
任何满足 $[A,Z]=A$ 的 $Z$ 保持 $\ker A^k=\operatorname{span}\{e_0,\ldots,e_{k-1}\}$，故在原整数基中上三角；其相邻对角差均为 $1$。设两半大小 $\ell=d/2$，上、下对角块为 $Z_0,Z_1$，则
$$
\operatorname{tr}(Z_1-Z_0)=\ell^2.
$$
取 $[A,Z]=A$ 的上右块之迹，得到
$$
\operatorname{tr}\bigl(R(Z_1-Z_0-I)\bigr)
=-m^{-2}\ell(\ell-1).
$$
对任意 $\xi\in\mathbb C$，
$$
\|Z_1-Z_0-I\|\le2\|Z-\xi I\|+1.
$$
因此
$$
\boxed{
\inf_{\xi\in\mathbb C}\|Z-\xi I\|
\ge g_m:=
\frac12\left(\frac{d/2-1}{26m^2\eta_{m-2}}-1\right).
}
\tag{5.3}
$$
这直接适用于 (1.1) 的实际 $Z$。

现在取 $\xi=(d-1)/2$。由 (3.6)，
$$
\|Z_H-\xi I\|
\ge\frac{\|Z-\xi I\|}{\sqrt{C_m'}}
\ge\frac{g_m}{\sqrt{C_m'}}.
\tag{5.4}
$$
$Z_H-\xi I$ 的全部特征值仍是实数，绝对值至多 $(d-1)/2$。对其作酉 Schur 三角化，写成 $\Lambda+N$，其中 $\Lambda$ 实对角、$N$ 严格上三角。于是
$$
\|Z_H-\xi I\|
\le\frac{d-1}{2}+\|N\|_{\rm F},
$$
而
$$
\|N\|_{\rm F}
=\frac1{\sqrt2}\|N-N^*\|_{\rm F}
\le\sqrt{\frac d2}\,\|Z_H-Z_H^*\|.
$$
这里使用的是同一物理 $H$ 变换后的实际矩阵，而非另选 Jordan 链。

合并 (4.4)–(5.4)，对所有 $m\ge8$、$q\ge d-1$ 得到显式下界
$$
\boxed{
\|\Gamma_q^{-1/2}[\mathsf N,\Gamma_q]\Gamma_q^{-1/2}\|
\ge
\sqrt{\frac2d}
\left(\frac{g_m}{\sqrt{C_m'}}-\frac{d-1}{2}\right)_+.
}
\tag{5.5}
$$
特别，
$$
\boxed{
\log\|\Gamma_q^{-1/2}[\mathsf N,\Gamma_q]\Gamma_q^{-1/2}\|
\ge
\frac{175}{32}d^4-\frac{315}{32}d^3+75d-O(m^2),
}
\tag{5.6}
$$
当 $m\to\infty$ 时对全部 $q\ge d-1$ 一致成立。故
$$
\boxed{
\liminf_{m\to\infty}\ \inf_{q\ge d-1}
\frac1{d^4}
\log\|\Gamma_q^{-1/2}[\mathsf N,\Gamma_q]\Gamma_q^{-1/2}\|
\ge\frac{175}{32}.
}
\tag{5.7}
$$

## 6. 已排路线与仍开放的实际源 Schur

R239 真实逆芽半径为
$$
\rho_m=\exp(-110\,8^{m-1})=\exp\left(-\frac{55}{4}d^3\right).
$$
因此对任何固定 $a>0$，本稿的完整相对交换子不可能满足
$$
\|\Gamma_q^{-1/2}[\mathsf N,\Gamma_q]\Gamma_q^{-1/2}\|
\le C\,\rho_m^{-a}
$$
并对所有 $m,q$ 一致。更一般地，任何需先证明该完整导数为 $\exp(O(d^3))$ 的全源相对共轭方案，均不能直接用于原完整 $\Gamma_q$。

证明并未把 $\psi_m(-D)$ 的各列分别估范数；(1.6)–(1.8) 保留了同一实际复合多项式的全部抵消，坏下界仍在真实核中出现。

同时，证人有明确的低源性质：
$$
\operatorname{Ran}\mathcal R
\subset\mathcal K_{\le d-1}
\subset\mathcal K_{\le q}.
\tag{6.1}
$$
它们都是有限左前缀的真实零源核向量。实际 boundary-source 最小化会先对该类自由零核作完整 Schur 消去。因此：

- 本稿没有给出消去左零核后 source Gram 的相对交换子下界；
- 没有否定固定物理测试在真实 $\Gamma^{-1}$ 或 $E$ 滤波中的更小费用；
- 没有证明负图剩余谱隙必须付 $d^4$ 指数；
- 没有从本稿推出 $N\ne M$ 或普通 ISP 的任何答案。

下一有效接口仍须保持原 source Schur、固定测试或实际负图条件。把完整 $\Gamma_q$ 的巨大方向先用一个无源限制的相对估计统一包住，已经不能获得所需的三次指数预算。

## 来源和去重

- R239 真实头稿提供实际 $V$、逆芽及 first-head 规范。
- R234 四次头幂提供 (3.4)；全核零占据稿已将其完整写入原物理头预算。
- 2026-11-12 真实头分级迹稿提供 (5.3) 的旧头障碍；本稿不把这一旧结论重计。
- 本稿新增的是：原全异尾内的等有效权**物理真核嵌入**、其 $\exp(O(m^2))$ Gram 成本、以及由此得到的**完整 graph 相对孔交换子**的实际四次指数下界。
