# 任意两种正权、任意偶位数的完整临界相位界

本稿证明：**任意偶数个位、任意两种独立正权、任意两组大小，整个实际低 primitive 源的相位都满足 \(\Phi\preceq I\)**。不是只检查一个选定的对称向量，也不限制有效位数。

证明保留组 Casimir 的全部物理多重性与完整 MP 逆。每个非零低源块恰为一维，只有有效组长 \((p,p)\) 与 \((p,p+2)\) 两类。前者化成一个 Chebyshev 实根不等式，后者给出全部阶数的正系数通项。常数 \(1\) 在等权及真实永久等号模块上达到。

## 1. 目标与完整组模块归约

在 \(M=2s\) 位 Boolean Hilbert 空间上取两组，组大小为 \(q,L\)，权分别为 \(b_A,b_B>0\)。允许先作共同缩放，使平方权分别为 \(z>0\) 与 \(1\)。共同缩放不改变相位。

记
\[
d_b=\sum_i b_iE_i,\quad e_b=\sum_i b_i^{-1}E_i^*,\quad
V_b=\ker d_b\cap\mathcal H_{s-1},\quad U_b=\ker d_b\cap\mathcal H_s.
\]
\(G,L_2\) 分别为完整 \(d_b,d_b^2/2\) 的 MP 逆在 \(V_b\) 上的 Gram；记
\[
A_0=e_b^*|_{U_b},\quad Q_0=P_{V_b}e_b^*e_b|_{V_b}=4G+A_0A_0^*.
\]
目标为
\[
\boxed{
\Phi=H_0^*L_2^{-1}H_0\preceq I,\qquad
H_0=G^{-1}L_2-2G-A_0A_0^*
=G^{-1}L_2+2G-Q_0.
} \tag{1.1}
\]

上述 \(Q_0\) 身份可直接证明：对 \(v\in V_b\)，\([d_b,e_b]v=2v\)，故
\[
e_bv=2\mathcal J_1v+A_0^*v
\]
是最小范数原像与 \(\ker d_b\cap\mathcal H_s\) 的物理正交分解，取 Gram 即得。

分别把两组分成正交 unweighted primitive ladders。组内源次数为 \(a,c\) 的块，等距于有效组长
\[
q'=q-2a,\qquad L'=L-2c
\]
的对称 Boolean 模块，权仍为 \(\sqrt z,1\)。完整 \(d_b,e_b\) 及其伴随保持这些正交模块，故完整 MP 逆也逐块分解；不是先压缩再取逆。具体归一链及最小范数逆的说明见[至多四有效位与方向性局部稿](2026-11-14-even-phase-second-kernel-effective-four-bits-and-directional-local-bound-789f-next.md) §§2、4。

在一个有效模块中，设 \(N=q'+L'=2r\)。临界低源次数为 \(r-1\)。使用聚合多项式坐标
\[
f(\alpha,\beta)=\sum_k f_k\alpha^k\beta^{m-k},
\]
其中实际物理范数为
\[
\|f\|^2
=\sum_k\frac{|f_k|^2}{\binom{q'}k\binom{L'}{m-k}}. \tag{1.2}
\]
即把 \(f_k\) 除以对应两个组的子集计数后，作为每个子集的共同物理振幅。在此坐标下
\[
d_0=\partial_\alpha+\partial_\beta,\qquad
e_0=\alpha(q'-\alpha\partial_\alpha)+\beta(L'-\beta\partial_\beta). \tag{1.3}
\]
次数 \(m\) 的 primitive 若存在，必且仅能为 \((\alpha-\beta)^m\) 的标量倍数；它合法当且仅当 \(m\le\min(q',L')\)。

取 \(m=r-1\)。因为 \(q',L'\) 同奇偶，非零源只可能是
\[
(q',L')=(p,p),\ p\ge1,
\qquad\text{或}\qquad
(q',L')=(p,p+2),\ p\ge0, \tag{1.4}
\]
及后者的组互换。每个这样的 primitive 源是一维，但全部组内 primitive 多重性都仍保留为正交副本。故逐块证明 (1.1) 即证明整个原物理源。

## 2. 一维源的真实共同矩规范

固定 unweighted primitive \(v\)，令 \(N_v=\|v\|^2\)，并以 \(v/\sqrt{N_v}\) 为固定源单位向量。去权映射是在第一组占据数 \(k\) 上乘 \(z^{-k/2}\)。用 \(h,g,\ell,q_0\) 表示其源度量及 \(G,L_2,Q_0\) 的真实二次型。

实际标量算子和相位传输为
\[
G=g/h,\qquad L_2=\ell/h,\qquad Q_0=q_0/h,
\]
\[
\boxed{
\mathcal T=\frac{h\ell/g+2g-q_0}{\sqrt{h\ell}},
\qquad \Phi=\mathcal T^2.
} \tag{2.1}
\]
所有量为实数，但 \(\mathcal T\) 可以变号；不把它先假设为正。

完整源式给
\[
h=\frac{\|D^{-1}v\|^2}{N_v},\qquad
\ell=z^{-q'}\frac{\|Dv\|^2}{N_v},\qquad
q_0=z^{-q'}\frac{\|D_{\rm mid}e_0v\|^2}{N_v}. \tag{2.2}
\]
其中 \(D\) 乘 \(z^{k/2}\)，中央 \(D_{\rm mid}\) 也按中央第一组占据数乘 \(z^{k/2}\)。这些分别是源度量、真实顶 MP Gram、通过中央补集得到的 reciprocal Gram。

下面计算 \(g\) 时使用实际正交身份 \(q_0=4g+\langle A_0A_0^*\rangle_{\rm form}\)。因此它仍是完整第一逆所得的 \(g\)，没有用未验证的压缩逆代替。

## 3. 平衡有效组 \((p,p)\)：实际标量化

令 \(p\ge1\)，低源
\[
v=(\alpha-\beta)^{p-1},\qquad u=(\alpha-\beta)^p
\]
分别生成低源和一维中央硬源。由 (1.2)–(1.3)，
\[
N_v=\frac{(p+1)(p+2)}{6p},\qquad e_0v=(\alpha+\beta)v.
\]
置
\[
D=\frac{p(p+1)(p+2)}6,
\]
\[
A(z)=\sum_{k=0}^p z^k,\quad
C(z)=\sum_{k=0}^{p-1}(k+1)(p-k)z^k,\quad
B(z)=\sum_{k=0}^{p}(p-2k)^2z^k.
\]
直接代入物理范数得
\[
h=\frac{C(z^{-1})}{D}
=\frac{z^{-(p-1)}C(z)}D,\qquad
\ell=\frac{z^{-p}C(z)}D,\qquad
q_0=\frac{z^{-p}B(z)}D. \tag{3.1}
\]

真实 reciprocal lowering 在去权源上满足
\[
A_0(D^{-1}u)=p(z^{-1}-1)D^{-1}v.
\]
因此由两个实际源范数之比，
\[
q_0-4g
=\frac{(z^{-1}-1)^2C(z^{-1})^2}{D A(z^{-1})}
=\frac{z^{-p}(z-1)^2C(z)^2}{D A(z)}.
\]
从而
\[
\boxed{
g=\frac{z^{-p}}{4D}
\left[B(z)-\frac{(z-1)^2C(z)^2}{A(z)}\right].
} \tag{3.2}
\]

给离散概率 \(\mathbb P_z\{k\}=z^k/A(z)\)，\(0\le k\le p\)，记均值 \(\mu\) 与方差 \(\sigma^2>0\)。准确有限和身份
\[
(z-1)C(z)=2zA'(z)-pA(z)
\]
使 (3.2) 化为
\[
\boxed{g=\frac{z^{-p}A(z)\sigma^2}{D}.} \tag{3.3}
\]
这只是同一完整 MP Gram 的显式表达，不额外假设概率矩模型。

因交换两等长组把 \(z\) 变为 \(z^{-1}\)，以下可取 \(z>1\)；\(z=1\) 直接为等权 \(\Phi=1\)。令
\[
n=p+1,\qquad \tau=\tfrac12\log z>0,\qquad X=\cosh\tau>1,
\]
\[
P(X)=\frac{U_p(X)}{p+1}
=\frac{\sinh(n\tau)}{n\sinh\tau}.
\]
\(U_p\) 是由 \(U_0=1,U_1=2X,U_{p+1}=2XU_p-U_{p-1}\) 定义的 Chebyshev 多项式；上式由双曲正弦加法立即验证。

设
\[
U=2\mu-p=n\coth(n\tau)-\coth\tau,\qquad
V=4\sigma^2=\operatorname{csch}^2\tau-n^2\operatorname{csch}^2(n\tau).
\]
于是
\[
V=\frac{1-P(X)^{-2}}{\sinh^2\tau},\qquad
U=\frac{d}{d\tau}\log P(\cosh\tau).
\]
定义
\[
\boxed{\nu(X)=\frac{(X^2-1)P(X)P'(X)}{P(X)^2-1}
=\frac{U\sinh\tau}{1-P(X)^{-2}}.} \tag{3.4}
\]
将 (3.1)、(3.3) 代入 (2.1)，准确得到
\[
\boxed{\mathcal T=\frac{2\nu}{P^2}-\frac1\nu.} \tag{3.5}
\]
例如，可先写
\[
\mathcal T=
\frac{2U}{\sinh\tau\,V}
-\frac{\sinh\tau\,V}{U}
-2\sinh\tau\,U,
\]
再用 (3.4) 把首末两项合并。没有分别估计两项可能很大的数值。

## 4. Chebyshev 实根给 \(1\le\nu\le P\)

从三角正弦加法和上述递推，
\[
U_p(\cos\theta)=\frac{\sin((p+1)\theta)}{\sin\theta}.
\]
故 \(U_p\) 的全部 \(p\) 个根为
\[
c_j=\cos\frac{j\pi}{p+1}\in(-1,1),
\]
且 \(P(1)=1\)。因此
\[
P(X)=\prod_{j=1}^p\frac{X-c_j}{1-c_j}.
\]

**下界。** 写 \(w=X-1>0\)、\(r_j=1-c_j>0\)，则
\[
P=\prod_j(1+w/r_j),\qquad
\frac{(X^2-1)P'}P
=\sum_j\frac{w(w+2)}{w+r_j}.
\]
逐项有
\[
\frac{w(w+2)}{w+r}
\ge 1-\frac{r^2}{(w+r)^2},
\]
因为两边之差为
\[
\frac{w^2(w+r+1)}{(w+r)^2}\ge0.
\]
又对 \(0\le a_j\le1\)，
\[
1-\prod_j a_j\le\sum_j(1-a_j),
\]
所以
\[
\frac{(X^2-1)P'}P\ge1-P^{-2},
\qquad\boxed{\nu\ge1.} \tag{4.1}
\]

**上界。** Chebyshev 根成 \(\pm c\) 对，可能另有一个零根。因此 \(P\) 是若干以下因子的乘积：
\[
F(X)=X,\qquad F_c(X)=\frac{X^2-c^2}{1-c^2},\quad 0<c<1.
\]
每个因子在 \(X\ge1\) 都至少为 \(1\)，且
\[
(X^2-1)F'\le F^2-1.
\]
对 \(F=X\) 是等式；对 \(F_c\)，约去正因子后恰为
\[
2X(1-c^2)\le X^2+1-2c^2,
\]
其右减左等于 \((X-1)^2+2c^2(X-1)\ge0\)。

此不等式在乘积下保持：若 \(F,G\ge1\) 均满足它，则
\[
\begin{aligned}
(X^2-1)(FG)'
&\le G(F^2-1)+F(G^2-1)\\
&=(F+G)(FG-1)\\
&\le(FG+1)(FG-1)=(FG)^2-1,
\end{aligned}
\]
因为 \(F+G\le FG+1\)。故
\[
(X^2-1)P'\le P^2-1,\qquad\boxed{\nu\le P.} \tag{4.2}
\]

对固定 \(P>1\)，函数 \(2\nu/P^2-1/\nu\) 随 \(\nu>0\) 严格递增。由 (4.1)–(4.2)，
\[
-1<-\frac1\nu+\frac{2\nu}{P^2}\le\frac1P<1.
\]
所以所有平衡块的异权相位严格满足
\[
\boxed{\Phi<1\quad(z\ne1),} \tag{4.3}
\]
而 \(z=1\) 时 \(\Phi=1\)。本段对全部整数 \(p\ge1\) 成立。

## 5. 不平衡有效组 \((p,p+2)\)：完整源式

令 \(p\ge0\)，低源
\[
v=(\alpha-\beta)^p,\qquad N_v=\frac{p+3}{3},\qquad e_0v=2\beta v.
\]
该块中央没有硬源：最小总 spin 是 \(1\)，等价地下一次数不存在合法 primitive 多项式。因此 \(A_0=0\)，准确有 \(q_0=4g\)。

置
\[
D=\frac{(p+1)(p+2)(p+3)}3,
\]
\[
A(z)=\sum_{k=0}^{p}(k+1)(k+2)z^k,\quad
A^{\rm rev}(z)=\sum_{k=0}^{p}(p+1-k)(p+2-k)z^k,
\]
\[
C(z)=\sum_{k=0}^{p}(k+1)(p+1-k)z^k.
\]
源范数、顶 MP 与 \(q_0=4g\) 给
\[
h=\frac{A(z^{-1})}{D},\qquad
\ell=\frac{z^{-p}A(z)}D,\qquad
g=\frac{z^{-p}C(z)}D.
\]
\(C\) 回文，且 \(A^{\rm rev}=z^pA(z^{-1})\)。因此
\[
r:=\frac{h\ell}{g^2}
=\frac{A(z)A^{\rm rev}(z)}{C(z)^2},
\qquad
\boxed{\Phi=\frac{(r-2)^2}{r}.} \tag{5.1}
\]
只须证明 \(1\le r\le4\)，并保留 \(p=0\) 的硬端等号。

## 6. 全部 \(p\) 的正系数通项

### 6.1. 下界 \(r>1\)

多项式 \(A A^{\rm rev}-C^2\) 回文，次数 \(2p\)。直接将三个二次系数相乘并求有限和，对 \(0\le m\le p\) 得
\[
\boxed{
[z^m](A A^{\rm rev}-C^2)
=\frac{(m+1)(m+2)(m+3)(p+1)(p+3)}6>0.
} \tag{6.1}
\]
其余系数由回文相同。因此
\[
\boxed{r>1\quad\text{对全部 }z>0.} \tag{6.2}
\]

### 6.2. 上界 \(r\le4\)

若 \(p=0\)，\(A=A^{\rm rev}=2,C=1\)，准确 \(r=4\)、\(\Phi=1\)。这是唯一活动组为两等权位的永久等号块，不能误写严格号。

以下取 \(p\ge1\)。置
\[
F(z)=4C(z)^2-A(z)A^{\rm rev}(z).
\]
它回文、次数 \(2p\)。有限和直接给 \(A(1)=2C(1)=A^{\rm rev}(1)\)，故 \(F(1)=F'(1)=0\)，存在回文次数 \(2p-2\) 的 \(E(z)\) 使
\[
F(z)=(z-1)^2E(z).
\]
对 \(0\le m\le p\)，先有
\[
[z^m]F=
\frac{(m+1)(m+2)(m+3)
(3m^2-15mp-18m+10p^2+10p)}{30}.
\]
对这些系数作两次前缀和，即 \(E_m=\sum_{j=0}^m(m-j+1)F_j\)，给全部前半系数
\[
\boxed{
E_m=
\frac{(m+1)(m+2)(m+3)(m+4)(m+5)}{420}
\left(m^2-7mp-8m+7p^2+7p\right),
\quad0\le m\le p-1.
} \tag{6.3}
\]
这些恒等式可直接展开有限幂和核对，也可把 (6.3) 作二阶差分恢复所列 \(F_m\)。

写 \(p=m+1+h\)、\(h\ge0\)，括号严格等于
\[
7h^2+7hm+21h+m^2+6m+14>0.
\]
所以前半所有 \(E_m>0\)，回文给其余所有系数也严格正。因此对 \(z>0\)，
\[
4C^2-A A^{\rm rev}=(z-1)^2E(z)\ge0,
\]
且 \(z\ne1\) 时严格。结合 (6.2)，
\[
1<r<4\quad(z\ne1,\ p\ge1),\qquad r=4\quad(z=1).
\]
因为
\[
1-\frac{(r-2)^2}{r}=\frac{(r-1)(4-r)}r,
\]
这证明全部不平衡块的相位界，并在 \(p\ge1,z\ne1\) 时严格。

## 7. 整个原源的结论与全部等号模块

**定理 7.1。** 任意 \(M=2s\)、任意两组大小和任意两个正权值，实际相位 (1.1) 满足
\[
\boxed{\Phi\preceq I\quad\text{于整个 }V_b.}
\]

**证明。** §1 保留了全部正交组 primitive 多重性，且完整 MP 逆逐块兼容。每个非零源块只可能是 (1.4) 的两类。§§3–4 和 §§5–6 已证明全部整数参数、全部正权比的标量相位界，故正交直和给整源结论。证毕。

如果两个权值不同，全部等号模块恰为：一组 spin \(1\)，另一组 spin \(0\)。它们就是 §6 的 \(p=0\) 不平衡块；其余块严格。因此：

- 若两组大小都是奇数，则整个 \(V_b\) 上 \(\Phi\prec I\)。
- 若两组大小都是偶数，令
  \[
  m_0(n)=\binom n{n/2}-\binom n{n/2-1},\qquad
  m_1(n)=\binom n{n/2-1}-\binom n{n/2-2}.
  \]
  则完整等号核的准确维数为
  \[
  m_1(q)m_0(L)+m_0(q)m_1(L).
  \]
  其物理源正是两个组内 primitive 多重性空间的张量积，不随权比改变。
- 两权相等时，整源 \(\Phi=I\)。

本稿是任意位数的完整两权类，且真实常数为 \(1\)。三种或更多独立权值的一般偶相位仍未闭合；此类结论不自动替代普适相位界、原 graph 费用或一般复 Hilbert 不变子空间问题。

