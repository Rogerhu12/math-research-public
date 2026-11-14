# R277：原首头商的一孔删除行完整分类与零源泄漏链

日期：2026-11-14。作者：Astra-ISP-789f / boundary_core。

**状态：第 2—5、7 节为完整证明，均在原连续尾和原合法窗口上成立。** 本稿不证明边界 $N=M$。它定位了一条新的实际障碍：虽然三次权删除与原删除真正交换，并在未压缩的首头图上保持原范数界，它的物理压缩不能下降到原源商；其零源泄漏包含完整原头 Jordan 链。任何尚未覆盖全部原头的负前缀，均不能仅靠正规方程消去这条泄漏。

## 1. 原对象，不替换为有限异权模型

固定原 $m\ge5$、$d=2^m$ 和任一合法孔切口 $q$。原尾为
$$
D=\sum_{i\ge m}b_iE_i,\qquad b_i=(i+1)^{-2},
\qquad C=\sum_{i\ge m}b_i^3E_i.
\tag{1.1}
$$
两个级数均按算子范数收敛，不同位删除交换，故
$$
CD=DC,\qquad \|C\|\le\sum_{i\ge m}b_i^3<\infty.
\tag{1.2}
$$
记 $\mathcal H_p$ 为原尾的 $p$ 孔层，
$$
E_{h,p}=\ker D^h\cap\mathcal H_p,\qquad
W_{h,p}=E_{h,p}\ominus E_{h-1,p},\qquad
K_p=E_{1,p}.
$$
出生指标为 $a=p-h+1$。

在 $\mathcal E_d=\ker D^d$ 中，令 $Q$ 为出生 $a\ge q+2$ 的原物理正交投影，$P=I-Q$。其低部分
$$
\mathcal F_d=P\mathcal E_d
=\{0\le a\le q+1,\ 1\le h\le d\}
$$
正是[原首物理头商](R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)的参数空间。定义
$$
\delta=PDP|_{\mathcal F_d},\qquad
\kappa=PCP|_{\mathcal F_d}.
\tag{1.3}
$$
因为 $C$ 与 $D$ 交换，$C$ 保持 $\mathcal E_d$，所以这里没有新的最高高度定义域问题。

原头为 $A=VJ_dV^{-1}$，$V$ 为原上三角归一链基。原源映射为
$$
\mathcal Bf
=\sum_{j=1}^{d-1}(-1)^jVe_{j-1}D^jf_{q+j}.
\tag{1.4}
$$
原零源空间和前 $K$ 源头为
$$
\mathcal C_0=\ker\mathcal B
=\left(\bigoplus_{p=0}^qE_{d,p}\right)
\oplus\left(\bigoplus_{j=1}^dW_{j,q+j}\right),
$$
$$
X_K=\mathscr R_q\cap\ker A^K,
\qquad\mathcal C_K=\mathcal B^{-1}X_K,
\qquad0\le K\le d-1.
\tag{1.5}
$$
其中 $X_K$ 使用前 $K$ 个原物理源头，$X_0=0$。

本稿首头图记为 $\mathcal T$，其 Gram 为 $\Gamma_{\rm graph}=\mathcal T^*\mathcal T$；它不是 primitive 真幂 Gram 的阶乘归一矩阵。

## 2. 原连续尾的每个 primitive 层均有非零三次权下降

**引理 2.1。** 对每个整数 $r\ge1$，存在有限支持的
$$
u\in K_r,\qquad Cu\ne0.
\tag{2.1}
$$

**证明。** 在 $[m,\infty)$ 取 $r$ 个两两不交的二元组 $(i_\ell,j_\ell)$，其中 $i_\ell<j_\ell$。定义对应一次孔向量
$$
v_\ell=b_{j_\ell}e_{i_\ell}-b_{i_\ell}e_{j_\ell}.
$$
因 $b_i$ 严格递减，
$$
Dv_\ell=0,\qquad
Cv_\ell=c_\ell\Omega,
\quad c_\ell=b_{i_\ell}b_{j_\ell}
(b_{i_\ell}^2-b_{j_\ell}^2)\ne0.
$$
令 $u=v_1\cdots v_r$，乘积是不同二元组上的实际张量乘积，其余位为真空。删除只作用于各自二元组，故
$$
Du=0,\qquad
Cu=\sum_{\ell=1}^r c_\ell\prod_{k\ne\ell}v_k.
$$
后一和的不同项支持在不同的集合族：第 $\ell$ 项恰缺少第 $\ell$ 个二元组，而在其余每个二元组中有一个孔。因此这些项正交且非零，$Cu\ne0$。此外 $DCu=CDu=0$，所以 $Cu\in K_{r-1}$。证毕。

## 3. 一个原零源 primitive 塔泄漏到完整原头链

固定引理 2.1 给出的
$$
u\in K_{q+1},\qquad Cu\ne0.
$$
原连续尾的每个固定层真幂均有有界最小逆，见[有限模型与连续尾归约 §3](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)。因此对 $1\le j\le d$ 可定义
$$
x_j=J_{j-1,q+1}u
:=(D^{j-1}:\mathcal H_{q+j}\to\mathcal H_{q+1})^\dagger u.
\tag{3.1}
$$
其中 $x_1=u$。由真正最小原像的性质，
$$
D^{j-1}x_j=u,\qquad D^jx_j=0,\qquad
x_j\perp\ker D^{j-1},
$$
所以
$$
x_j\in W_{j,q+j}\subseteq\mathcal C_0.
\tag{3.2}
$$
以下把 $x_j$ 看成只在未来孔层 $q+j$ 有非零分量的参数向量。

**定理 3.1（完整真实泄漏链）。** 对 $2\le j\le d$，
$$
\boxed{
\mathcal B\kappa x_j
=(-1)^{j-1}Ve_{j-2}\,Cu.
}
\tag{3.3}
$$
并且 $\mathcal Bx_j=0$ 对全部 $j$ 成立。

**证明。** 零源断言由 (3.2) 或源公式 (1.4) 直接成立。由于 $C$ 降一孔且保持每个 $\ker D^j$，$Cx_j\in E_{j,q+j-1}$。在未来层 $q+j-1$，投影 $P$ 只删去 $E_{j-2,q+j-1}$。因此
$$
D^{j-1}PCx_j=D^{j-1}Cx_j
=CD^{j-1}x_j=Cu.
$$
在 (1.4) 中只有指标 $j-1$ 的项能出现，得到 (3.3)。整个计算始终在原连续尾中，未将顺次右逆替代真幂 MP 逆。证毕。

这同一 $u$ 的零源塔已经使泄漏像包含
$$
\boxed{
\operatorname{span}\{Ve_0,\ldots,Ve_{d-2}\}\otimes\mathbb C(Cu)
\subseteq\mathcal B\kappa(\mathcal C_0).
}
\tag{3.4}
$$
它是一个完整的长度 $d-1$ 原源头链；不是仅有第零源头的误差。

**推论 3.2。** 对每个 $0\le K\le d-2$，
$$
\boxed{\kappa\mathcal C_0\not\subseteq\mathcal C_K.}
\tag{3.5}
$$
故 $\kappa$ 不能从 $\mathcal F_d/\mathcal C_0$ 到原源商诱导良定义的线性算子，即使允许输出再模去前 $K$ 源头也不行。

**证明。** 在 (3.3) 取 $j=K+2$，则泄漏为非零倍的 $Ve_KCu$。原上三角 $V$ 的第 $K$ 对角元非零，故此向量的第 $K$ 物理源头非零，不属于前 $K$ 头 $X_K$。证毕。

更强地，不存在任何有限常数和任何原源空间范数，使
$$
\|\mathcal B\kappa x\|\le C_0\|\mathcal Bx\|
\quad(x\in\mathcal F_d)
$$
成立；右边在上述 $x_j$ 上为零而左边非零。这是下降映射本身的障碍，不仅是其统一费用过大。

## 4. 压缩交换子确实只落零源，但仍不能据此下降

这里保留一个容易混淆的正面身份。因为 $D$ 保持高出生空间 $Q\mathcal E_d$，$PDQ=0$。由 $CD=DC$，
$$
\boxed{[\delta,\kappa]=PCQDP|_{\mathcal F_d}.}
\tag{4.1}
$$
原 Boolean 两带关系表明 $QDP$ 只能从出生 $q+1$ 越到 $q+2$。另一方面，$C$ 保持核阶且降一孔，故从高度 $h$、出生 $a$ 输入后，任何非零输出高度 $h'\le h$ 的出生为
$$
a'=a+h-h'-1\ge a-1.
$$
因而 $PC$ 对出生 $q+2$ 的低侧输出只能落在出生 $q+1$。该整个出生边界属于 $\mathcal C_0$，所以
$$
\boxed{\operatorname{Ran}[\delta,\kappa]\subseteq\mathcal C_0,
\qquad\mathcal B[\delta,\kappa]=0.}
\tag{4.2}
$$
式 (4.2) 不能替代 $\kappa\mathcal C_0\subseteq\mathcal C_0$；后者已经被 (3.3) 否定。因此“交换子模零源为零”不足以得到商上的交换作用。这两项是不同的代数条件。

结合已证 $\mathcal B\delta=-A\mathcal B$，泄漏行 $F=\mathcal B\kappa$ 满足
$$
F\delta=-AF.
\tag{4.3}
$$
它解释了 (3.4) 为何是一整条原头链，而不是可独立删除的偶发坐标。

## 5. 实际负前缀正规方程也不能独自消去这条泄漏

固定 $K\le d-2$，令 $z=\mathcal B\kappa x_{K+2}\notin X_K$，并取原物理投影
$$
y=P_{X_K^\perp}z\ne0,
\qquad r=(L+B)^{-1}y.
$$
固定原窗口的 $L+B$ 有界严格正，因此 $r$ 是合法原源。它满足真实负前缀
$$
\langle(L+B)r,s\rangle=0\quad(s\in X_K),
$$
但
$$
\boxed{
\langle(L+B)r,\mathcal B\kappa x_{K+2}\rangle
=\|P_{X_K^\perp}z\|^2>0.
}
\tag{5.1}
$$
令 $f_r$ 为原首头最小坐标，$\Gamma_{\rm graph}f_r=\mathcal B^*(L+B)r$，则同一式为
$$
\langle\Gamma_{\rm graph}f_r,\kappa x_{K+2}\rangle\ne0,
\qquad\Gamma_{\rm graph}f_r\perp\mathcal C_K.
\tag{5.2}
$$
所以正规方程只能杀掉已经证明属于 $\mathcal C_K$ 的向量；它不能免费杀掉 $C$ 对零源的全部压缩作用。

这里构造的是合法原源，不声称它来自同一个未知真实缺陷 $w$，不把它当作无权 $N=M$ 的反例。它严格排除的是只依赖该负前缀条件的普遍消项。

## 6. 对原 graph 范数的意义与剩余问题

在未取高出生商的 $\mathcal E_d$ 上，可定义
$$
\mathcal T_{\rm full}f=\sum_{j=0}^{d-1}(Ve_j)(-D)^jf.
$$
由 $CD=DC$，准确有
$$
\mathcal T_{\rm full}C=(I_{\rm head}\otimes C)\mathcal T_{\rm full},
\qquad
\|\mathcal T_{\rm full}Cf\|\le\|C\|\,\|\mathcal T_{\rm full}f\|.
$$
这是真正的未压缩图界。但原 bare 首头图会删去未来高出生输出；$C$ 可以将被删部分送回低侧，而其零源泄漏又包含 (3.4) 的完整源头链。因此该界不能直接下降为原两费用商上的同范数界。

若要继续这条路线，必须实际构造保源的修正并支付相应完整/裸高返回，或证明实际固定低测试没有读到 (3.4) 中未付的部分。单独的原 $C$ 范数界、模零源交换子身份、或增长但未覆盖全部原头的负前缀均不够。one-bit primitive Schur 公式只解决其明确的真 MP 块，仍需支付这里的原 graph 接续。

原固定测试双链 Gram 的窗口阶上界仍未证明；本稿不宣称普通 ISP 或边界 $N=M$ 完成。

## 7. 一孔删除行能下降到原源商的完整分类

上述论证不依赖三次幂的特殊数值。令 $c=(c_i)_{i\ge m}\in\ell^1$ 为任意复系数行，并定义有界算子
$$
C_c=\sum_{i\ge m}c_iE_i,\qquad
\kappa_c=PC_cP|_{\mathcal F_d}.
$$
仍有 $C_cD=DC_c$，且 $C_c$ 保持每个 $\ker D^h$。

**定理 7.1。** 对每个固定原合法窗口，以及任意 $0\le K\le d-2$，下列条件等价：

1. $\kappa_c\mathcal C_0\subseteq\mathcal C_K$；
2. $\kappa_c\mathcal C_0\subseteq\mathcal C_0$；
3. 存在 $\lambda\in\mathbb C$ 使 $c_i=\lambda b_i$ 对所有 $i\ge m$ 成立。

换言之，在全部有界一孔删除行中，能从原参数零源商诱导良定义作用的，恰为原 $D$ 的标量倍。即使只要求输出在模前 $K$ 源头后良定义，只要该前缀尚未覆盖全部原源头，分类仍不改变。

**证明。** $(3)\Rightarrow(2)$：此时 $\kappa_c=\lambda\delta$。由 $\mathcal B\delta=-A\mathcal B$，$\delta$ 保持 $\mathcal C_0$。$(2)\Rightarrow(1)$ 因 $\mathcal C_0\subseteq\mathcal C_K$。

反证 $(1)\Rightarrow(3)$。若 $c$ 不与 $b$ 成比例，因所有 $b_i>0$，可选不同 $i,j$ 使
$$
c_i b_j-c_j b_i\ne0.
$$
把这对作为第一二元组，再任取 $q$ 对与它及彼此均不交的尾指标。对每个二元组仍用
$$
v_\ell=b_{j_\ell}e_{i_\ell}-b_{i_\ell}e_{j_\ell},
\qquad u=\prod_{\ell=1}^{q+1}v_\ell.
$$
则 $Du=0$，且
$$
C_cu=\sum_{\ell=1}^{q+1}
(c_{i_\ell}b_{j_\ell}-c_{j_\ell}b_{i_\ell})
\prod_{k\ne\ell}v_k.
$$
不同项仍正交，第一项非零，所以 $C_cu\ne0$。按 (3.1) 取 $j=K+2$ 的同一真幂最小原像。第 3 节的完整计算逐字给
$$
\mathcal B\kappa_c x_{K+2}
=(-1)^{K+1}Ve_KC_cu\notin X_K,
\qquad x_{K+2}\in\mathcal C_0.
$$
这与 (1) 矛盾，故 $c=\lambda b$。证毕。

此分类只涉及原 $\ell^1$ 一孔删除行及其物理压缩，不扩展为对任意有界算子、任意多孔行或经额外修正后作用的分类。它也没有声称非比例行不能用于更复杂的带修正双链证书；只是说明修正和费用必须实际给出。

## 8. 另一条已排除的有限谱隙捷径

[边界核查笔记](../notes/2026-11-14-boundary-789f.md) §2 给完整有理反例：六位权(2,1,1,1,1,1)、primitive向量(5,−2,−2,−2,−2,−2)满足 ||D*f||²/||f||²=11/3<4（删最大两平方权后之和）。因此一般权的常数一“删最大2a权尾和”primitive谱隙不成立。它不反驳原连续权的已证特殊界，也不反驳primitive相邻Gram序。该笔记另保两种Gram归一和原source接口的核对。
