# 原实际源 Schur 的相对孔导数仍可昂贵，而同源两费已便宜

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：已证明，中间结论。** 本稿使用原 $N/Y$ 真实头、原全异连续尾和原 $L,B,G$。即使先消去 joined first-head Gram 的**全部零源自由量**，其全源相对孔交换子仍具有四次指数下界；该结论对每个孔切口 $q$ 都成立，因而不限于低孔切口。

另一方面，构造的这批真实源具有两个准确性质：其真正左最小者只在第 $q$ 孔层，故对固定低孔测试配对严格为零；其原完整 flat 费已经以 $\exp(O(m^2))$ 支付左费。因此本稿排除全源相对导数小界，不否定固定测试传播或原负图两费用目标。

依赖：[原首物理头商 Gram](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)、[原尾完整 graph 导数稿](2026-11-14-actual-tail-full-graph-relative-hole-commutator-obstruction-789f-next.md)。后者的两位工作块和头迹障碍在下文重新写出所需内容。

## 1. 实际零源空间确实按尾孔数分解

固定 $m\ge8$、$d=2^m$、任意整数 $q\ge0$。记原真实头为 $A=A_m$，原尾
$$
D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j.
$$
所有源和 MP 都限于这组固定参数；原无限正尾在每个固定有限孔层上的满射性保证相应源度量有界严格正。本文不使用全孔直和上的有界 $D^\dagger$。

沿用原商坐标
$$
\mathcal F_d=
\left(\bigoplus_{p\le q}E_{d,p}\right)
\oplus
\bigoplus_{j=1}^{d}
(E_{d,q+j}\cap E_{j-1,q+j}^{\perp}),
\qquad E_{h,p}=\ker D^h\cap\mathcal H_p.
$$
令 $\delta$ 为原高出生共同不变商中的压缩删除。真实归一链为
$$
A=VJ_dV^{-1},\qquad V=1\oplus V_+,
$$
并定义
$$
T=\sum_{i=0}^{d-1}(Ve_i)(-\delta)^i,\qquad
\Gamma=T^*T\succeq I,\qquad
Z=V\operatorname{diag}(0,\ldots,d-1)V^{-1}.
\tag{1.1}
$$
物理第 $i$ 头的 $\psi(-\delta)^i/W_i$ 一般含不同删除幂；本文不将其当成齐次行。

然而，**实际 cut 源本身**有已经证明的完整公式
$$
\mathcal Bf
=\sum_{j=1}^{d-1}(-1)^jVe_{j-1}D^jf_{q+j}.
\tag{1.2}
$$
对这个真实等式作用同一个 $V^{-1}$ 后，第 $j-1$ 源头准确只有
$(-1)^jD^jf_{q+j}$。不同 $j$ 的源头独立，因而
$$
\boxed{
\mathcal C:=\ker\mathcal B
=\left(\bigoplus_{p\le q}E_{d,p}\right)
\oplus\bigoplus_{j=1}^{d}W_{j,q+j},
\quad
W_{j,p}=E_{j,p}\ominus E_{j-1,p}.
}
\tag{1.3}
$$
于是
$$
\mathcal U=\mathcal C^\perp
=\bigoplus_{j=1}^{d-1}(E_{d,q+j}\cap E_{j,q+j}^{\perp}).
\tag{1.4}
$$
$\mathcal C,\mathcal U$ 都约化**真实尾孔数** $\mathsf N$。这是 (1.2) 的结果，不是用 formal grade 替换尾孔数。

## 2. 完整最小 lift 的 Schur 导数

在 $\mathcal C\oplus\mathcal U$ 分块中，定义
$$
R_{\mathcal U}u=
(-\Gamma_{CC}^{-1}\Gamma_{CU}u,u),\qquad
S=R_{\mathcal U}^*\Gamma R_{\mathcal U}
=\Gamma_{UU}-\Gamma_{UC}\Gamma_{CC}^{-1}\Gamma_{CU}.
\tag{2.1}
$$
$\Gamma_{CC}\succeq I$，且 $S\succeq I$。$R_{\mathcal U}$ 是对**全部**零源自由量取出的实际 $\Gamma$ 最小 lift。

记原实际源空间为
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q},
$$
其原总左加 bare 度量为
$$
\mathscr H=L+B.
$$
$\mathcal B_{\mathcal U}=\mathcal B|_{\mathcal U}$ 是到 $\mathscr R_q$ 的有界双射，且
$$
\boxed{
S=\mathcal B_{\mathcal U}^*\mathscr H\mathcal B_{\mathcal U}.
}
\tag{2.2}
$$
$TR_{\mathcal U}u$ 的两部分正是源 $\mathcal B_{\mathcal U}u$ 的真正左最小者和带负号的真正 bare 最小者。

因 $[\mathsf N,\delta]=-\delta$，与完整 graph 相同，
$$
\Gamma_\theta
:=e^{\theta\mathsf N}\Gamma e^{-\theta\mathsf N}
=T^*e^{\theta Z^*}e^{-\theta Z}T.
\tag{2.3}
$$
(1.3) 保证其 $C$ 块逆为
$e^{\theta N_C}\Gamma_{CC}^{-1}e^{-\theta N_C}$，
故 $\Gamma_\theta$ 的真实 Schur 补是
$e^{\theta N_U}Se^{-\theta N_U}$。在 $\theta=0$ 对完整 Schur 公式求导：
$$
\boxed{
[N_U,S]
=R_{\mathcal U}^*[\mathsf N,\Gamma]R_{\mathcal U}
=(TR_{\mathcal U})^*(Z^*-Z)(TR_{\mathcal U}).
}
\tag{2.4}
$$
固定 $q,d$ 时所有次数算子有界。$\theta\ne0$ 时 $\Gamma_\theta$ 不必自伴，但以上只是有界块消元的代数导数，逆和各因子的次序均已保留。

令
$$
\mathcal Z=Z\otimes I|_{\mathscr R_q}.
$$
它保持源的全部短核旗；$\mathcal Z^*$ 下文指**原源 Hilbert 空间中的伴随**，不免费删除短核投影。(1.2) 给
$$
\mathcal B_{\mathcal U}N_U
=(q+1+\mathcal Z)\mathcal B_{\mathcal U}.
\tag{2.5}
$$
所以
$$
[N_U,S]
=\mathcal B_{\mathcal U}^*
(\mathcal Z^*\mathscr H-\mathscr H\mathcal Z)
\mathcal B_{\mathcal U}.
\tag{2.6}
$$
$\mathscr H^{1/2}\mathcal B_{\mathcal U}S^{-1/2}$ 是酉映射，从而
$$
\boxed{
\|S^{-1/2}[N_U,S]S^{-1/2}\|
=
\|\mathscr H^{-1/2}
(\mathcal Z^*\mathscr H-\mathscr H\mathcal Z)
\mathscr H^{-1/2}\|.
}
\tag{2.7}
$$

## 3. 同一原尾中的工作块和任意出生 primitive

置
$$
n=d-1,\qquad a=(m+2n)^{-2}.
$$
取原尾前 $2n$ 位为工作块，按两位配对。对实际权 $b,c$ 的一个配对，以真空和归一 one-hole 向量 $\phi$ 形成二态子空间，使
$$
D\phi=a\,|00\rangle.
$$
这样的 $\phi$ 可以显式取
$$
\phi=\frac as\,\frac{b|10\rangle+c|01\rangle}{s}
+\sqrt{1-\frac{a^2}{s^2}}\,
 \frac{c|10\rangle-b|01\rangle}{s},
\qquad s=\sqrt{b^2+c^2}.
$$
每个 $b,c\ge a$，故合法。张量全部配对得到原平方自由空间内等距、次数保持、$D$ 不变的 $n$ 位等有效权块。其归一对称孔向量 $\omega_j$ 满足
$$
D\omega_j=a\sqrt{j(n-j+1)}\,\omega_{j-1}.
\tag{3.1}
$$
不假定该块在 $D^*$ 下约化。

再从工作块之外选 $q$ 个互不相交的两位配对。每个配对取
$$
\chi=\frac{c|10\rangle-b|01\rangle}{\sqrt{b^2+c^2}},
\qquad D\chi=0.
$$
它们的张量记为 $\kappa_q$；$q=0$ 时取真空。于是
$$
\boxed{\|\kappa_q\|=1,\qquad
\kappa_q\in\mathcal H_q,\qquad D\kappa_q=0.}
\tag{3.2}
$$
工作位与 primitive 位严格不相交，所以以下张量的 $D$ 作用准确分开。无论 $q$ 多大，都只使用有限个真实尾位。

对 $h\in\mathbb C^d$ 定义
$$
\mathcal R_qh
=\sum_{j=0}^{d-1}
\frac{(-A)^jh}{a^j\sqrt{j!(n)_{\underline j}}}
\otimes\omega_j\otimes\kappa_q.
\tag{3.3}
$$
(3.1) 逐项抵消且 $A^d=0$，故
$$
(A+D)\mathcal R_qh=0,\qquad
\operatorname{supp}_{\rm holes}\mathcal R_qh
\subseteq[q,q+d-1].
\tag{3.4}
$$
其物理 Gram 与 $q$ 无关：
$$
H_m^{\rm work}
=\mathcal R_q^*\mathcal R_q
=\sum_{j=0}^{d-1}
\frac{(A^j)^*A^j}{a^{2j}j!(n)_{\underline j}}.
\tag{3.5}
$$

原四次头幂界 $\|A^j\|\le6^j$、$\|A^j\|\le6^je^{-\gamma j^4}$ 对 $j\ge2m$ 成立，其中 $\gamma=770/16^4>1/100$。置
$$
\tau_m=\log36+4\log(m+2d-2),
$$
$$
C_m'=(2m+102)\exp(2m\tau_m+3\tau_m^{4/3}).
\tag{3.6}
$$
利用 $\tau x-\gamma x^4\le3\tau^{4/3}$ 和
$\sum_{j\ge0}e^{-\gamma j^4}<102$，直接得到
$$
\boxed{I\preceq H_m^{\rm work}\preceq C_m'I,\qquad
\log C_m'=O(m^2).}
\tag{3.7}
$$
这里没有使用 $\kappa_q$ 的任何 MP 范数。

## 4. 真正 source Schur 上的整个 $d-1$ 维物理子空间

记 $\mathcal H_+=e_0^\perp\subset\mathbb C^d$，定义
$$
\mathcal E_q:\mathcal H_+\to\mathscr R_q,\qquad
\mathcal E_qh=Ah\otimes\kappa_q.
\tag{4.1}
$$
$A$ 的核准确是 $\mathbb Ce_0$，所以该映射单射。$Ah$ 只有头 $0,\ldots,d-2$，而 $\kappa_q$ 是 primitive，故源的全部真实短核旗满足。

**准确左最小者。** 向量 $h\otimes\kappa_q$ 只放在第 $q$ 孔层。其低行残量为 $Dh\otimes\kappa_q=0$，边界源是 $\mathcal E_qh$，所以它是原左可行者。任何左零源核 $k\in\ker(A+D)\cap\mathcal H_{\le q}$ 的顶层都满足 $Ak_q=0$，即 $k_q\in e_0\otimes\mathcal H_q$。因 $h\perp e_0$，上述可行者正交于整个左零核。因此
$$
\boxed{
U_q\mathcal E_qh=h\otimes\kappa_q,\qquad
\mu(\mathcal E_qh)^2=\|h\|^2.
}
\tag{4.2}
$$
这里 $U_q=E_q^\dagger$ 是原真正左最小提升，不是另一条任意左链。

**准确完整右候选。** (3.3) 的 $j\ge1$ 部分取负号，即为同源的完整右链。其第 $j$ 段的头在 $\operatorname{Ran}A^j$ 中，头指标至多 $d-j-1$，尾在 $\ker D^{j+1}$；所以原全部逐头短核旗和末段封口均满足。由真实最小性，
$$
\boxed{
\alpha(\mathcal E_qh)^2
\le\lambda(\mathcal E_qh)^2
\le\langle(H_m^{\rm work}-I)h,h\rangle.
}
\tag{4.3}
$$
没有把此候选当成最小完整链，也没有把 complete 和 bare Gram 互换。

于是对同一个真实源总 Gram，
$$
P_{m,q}:=\mathcal E_q^*\mathscr H\mathcal E_q
=I+\mathcal E_q^*B\mathcal E_q,
$$
$$
\boxed{I\preceq P_{m,q}\preceq H_m^{\rm work}\preceq C_m'I.}
\tag{4.4}
$$
这就是零源已全部消去后的 $d-1$ 维真实 source 压缩，且上界对所有 $q$ 一致。

## 5. 该真实 source 压缩仍保留四次指数斜性

由 $V=1\oplus V_+$，
$$
Z=0\oplus Z_+.
$$
$[A,Z]=A$ 给
$$
ZA=A(Z-I).
$$
因此 $\operatorname{Ran}\mathcal E_q$ 在 $\mathcal Z$ 下不变，且
$$
\boxed{\mathcal Z\mathcal E_q
=\mathcal E_q Z_0,\qquad Z_0=Z_+-I_{\mathcal H_+}.}
\tag{5.1}
$$
$Z_0$ 的真实特征值为 $0,\ldots,d-2$。

$\mathscr H^{1/2}\mathcal E_qP_{m,q}^{-1/2}$ 是等距嵌入，故由 (2.7)、(5.1)，
$$
\begin{aligned}
\|S^{-1/2}[N_U,S]S^{-1/2}\|
&\ge
\left\|P_{m,q}^{-1/2}
(Z_0^*P_{m,q}-P_{m,q}Z_0)
P_{m,q}^{-1/2}\right\|\\
&=\|\widehat Z_0^*-\widehat Z_0\|,
\qquad
\widehat Z_0=P_{m,q}^{1/2}Z_0P_{m,q}^{-1/2}.
\end{aligned}
\tag{5.2}
$$

旧真实头迹法直接给
$$
\inf_{\xi\in\mathbb C}\|Z-\xi I\|
\ge g_m
:=\frac12\left(\frac{d/2-1}{26m^2\eta_{m-2}}-1\right),
\tag{5.3}
$$
$$
-\log\eta_{m-2}
=\frac{175}{32}d^4-\frac{315}{32}d^3+75d.
\tag{5.4}
$$
它来自实际最高位分块
$A=\left(\begin{smallmatrix}A_{m-1}&m^{-2}I+R\\0&A_{m-1}\end{smallmatrix}\right)$、
$\|R\|\le26\eta_{m-2}$，及
$\operatorname{tr}(R(Z_1-Z_0-I))=-m^{-2}(d/2)(d/2-1)$。
这是次数算子本身的旧下界，不是只对某个 Jordan 相似的条件数估计。

$m\ge8$ 时 $g_m>d/2$。由于 $Z=0\oplus Z_+$，取 $\xi=d/2$ 得
$$
\left\|Z_0-\frac{d-2}{2}I\right\|
=\left\|Z_+-\frac d2I\right\|
\ge g_m.
$$
(4.4) 因而给
$$
\left\|\widehat Z_0-\frac{d-2}{2}I\right\|
\ge\frac{g_m}{\sqrt{C_m'}}.
$$
对这个具有实谱的 $d-1$ 阶矩阵作酉 Schur 三角化。严格上三角部分 $N$ 满足
$$
\|N\|_{\rm F}
=\frac1{\sqrt2}\|N-N^*\|_{\rm F}
\le\sqrt{\frac{d-1}{2}}\,
\|\widehat Z_0-\widehat Z_0^*\|.
$$
所以对每个 $q\ge0$，
$$
\boxed{
\|S^{-1/2}[N_U,S]S^{-1/2}\|
\ge
\sqrt{\frac2{d-1}}
\left(\frac{g_m}{\sqrt{C_m'}}-\frac{d-2}{2}\right)_+.
}
\tag{5.5}
$$
特别，
$$
\boxed{
\log\|S^{-1/2}[N_U,S]S^{-1/2}\|
\ge
\frac{175}{32}d^4-\frac{315}{32}d^3+75d-O(m^2)
}
\tag{5.6}
$$
对全部 $q$ 一致成立。

因此，即使已完整消去原 $\ker\mathcal B$，仍不能对全部源证明该相对导数为 $\exp(O(d^3))$。任意固定次幂的旧或新逆芽半径倒数，都不足以控制这个**全源导数范数**。

## 6. 同一坏族的原两费却已支付

(4.2)–(4.3) 给
$$
\lambda(r)^2\le(C_m'-1)\mu(r)^2
\qquad(r\in\operatorname{Ran}\mathcal E_q).
\tag{6.1}
$$
在原同一个完整右 $G$ 度量下，Cauchy 不等式准确为
$$
\mu(r)^2=\langle Lr,r\rangle
\le\|G^{1/2}Lr\|\,\|G^{-1/2}r\|
=\lambda_{\rm flat}(r)\lambda(r).
$$
故
$$
\boxed{
\mu(r)^2\le(C_m'-1)\lambda_{\rm flat}(r)^2
\le(C_m'-1)\bigl(\alpha(r)^2+\lambda_{\rm flat}(r)^2\bigr).
}
\tag{6.2}
$$
所有因子顺序均为原 $LGL$；没有把 $L$ 与 $G$ 交换。

因此 (5.5) 的巨大相对导数与原两费比较的巨大常数**不是同一命题**。此实际族的两费常数已经只有 $\exp(O(m^2))$。它不提供 $E$ 滤波谱隙、剩余负图角度或原来源预算的反例。

## 7. 固定低物理测试在该族上严格为零

取任意物理测试 $f$，其尾孔支撑不超过固定 $s$。若 $q>s$，由 (4.2)，
$$
\boxed{
\langle f,U_qr\rangle=0
\qquad(r\in\operatorname{Ran}\mathcal E_q).
}
\tag{7.1}
$$
若以原实际测试源 $t_q(f)$ 表示相同功能，
$$
\langle Lr,t_q(f)\rangle=\langle U_qr,f\rangle,
$$
则它在这整个 $d-1$ 维源空间上同样严格为零。这里没有重选测试源，也没有将原 good-top 来源换成一个任意小费源。

后续仍可以研究原固定测试列、实际负图及其同一来源上的压缩传播；本稿并未否定这些较窄目标。实际教训是：即使先消零源，全源相对孔导数仍可能付原头分级的四次指数，而真正目标可以已经很便宜。若采用相对共轭或 Combes–Thomas 方式，必须进一步保留固定物理测试或已付两费的准确剥离，不能再用这个全源导数范数作为统一前置预算。
