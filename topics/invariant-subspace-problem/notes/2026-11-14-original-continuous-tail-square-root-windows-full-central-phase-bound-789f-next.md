# 原连续尾的平方根宽偶段：整个中央源的统一有限相位界

日期：2026-11-14；工作标识789f。

## 0. 原模型中的有限行与结论

取起点 \(x\ge1\) 和偶数 \(Q=2d\ge2\)，使用原连续尾的真实有限行
\[
                 b_i=(x+i)^{-2},\qquad 0\le i<Q.        \tag{0.1}
\]
这就是原记号 \(b_j=(j+1)^{-2}\) 的一个连续段，起点只作了指标平移。
令 \(D=\sum_{i=0}^{Q-1}b_iE_i\) 是该完整 \(Q\) 位 Boolean 删除，
\[
 V=\ker D\cap{\cal H}_{d-1},\qquad
 U=\ker D\cap{\cal H}_d.
\]
保留这两个空间的全部维数及每个完整中间层。定义
\[
 {\cal J}_1=D^\dagger|_V,\qquad
 {\cal J}_2=\left(D^2/2\right)^{-1}|_V,\qquad
 {\mathfrak e}=\sum_i b_i^{-1}E_i^*,
\]
\[
 \Gamma_1={\cal J}_1^*{\cal J}_1,\qquad
 \Gamma_2={\cal J}_2^*{\cal J}_2,\qquad
 R={\mathfrak e}^*P_U{\mathfrak e}|_V,
\]
\[
 {\cal H}=\Gamma_1^{-1}\Gamma_2-2\Gamma_1-R,\qquad
                         \Phi={\cal H}^*\Gamma_2^{-1}{\cal H}.
                                                               \tag{0.2}
\]
这里 \(D^2/2:{\cal H}_{d+1}\to{\cal H}_{d-1}\) 是完整可逆层间映射，
不是先压缩之后所造的逆。

**定理。** 对每个固定 \(c>0\)，存在明确的有限常数 \(\kappa_c\)，使
\[
                         Q\le c\sqrt x
          \quad\Longrightarrow\quad
                         0\preceq\Phi\preceq\kappa_c I_V.        \tag{0.3}
\]
常数不依赖 \(x,Q,d\) 或源维数。这是原全异权连续段的完整中央源，
没有选取一个置换对称试探块。

一组可直接使用的常数为
\[
 A_c=1+c^2/2,\qquad
 C_c=24c^2+8A_c^7c^2+8A_c^{14}c^4,
\]
\[
                         \boxed{\kappa_c=
                              (2e^{2C_c}+3e^{C_c})^2.}          \tag{0.4}
\]
常数没有优化。例如 \(Q\le\sqrt x/4\) 时可统一取
\[
                         \kappa=(2e^{9/2}+3e^{9/4})^2.
                                                               \tag{0.5}
\]

本稿使用[全部出生的真实主池特征接口](2026-11-14-deficient-main-pool-all-birth-feature-grams-and-full-hard-regression-789f-next.md)
的 \(q_0=0\) 情形，以及
[有限次数 Bernoulli 多项式比较与完整 Schur 预算](2026-11-14-bounded-degree-bernoulli-comparison-and-common-schur-phase-budget-789f.md)。
以下给出从真实权值到常数 (0.4) 的完整推导。

## 1. 共同正缩放准确保持相位

将整行权同时乘以 \(\gamma>0\)。物理空间 \(V,U\) 不变，且
\[
 D'=\gamma D,\qquad {\mathfrak e}'=\gamma^{-1}{\mathfrak e},
\]
\[
 \Gamma_1'=\gamma^{-2}\Gamma_1,\qquad
 \Gamma_2'=\gamma^{-4}\Gamma_2,\qquad R'=\gamma^{-2}R.
\]
因此
\[
                         {\cal H}'=\gamma^{-2}{\cal H},
 \qquad
                         \Phi'=\Phi.                   \tag{1.1}
\]
这是真实同一物理源上的算子等式，不只比较某种特征值代理。

记原权平方 \(w_i=(x+i)^{-4}\)，令
\[
                  \overline w=Q^{-1}\sum_iw_i,\qquad
                  z_i=w_i/\overline w.
\]
选 \(\gamma=\overline w^{-1/2}\) 后，新的权平方就是 \(z_i\)，并准确有
\[
                      D_{\rm tot}:=\sum_i(z_i-1)=0.      \tag{1.2}
\]
注意 \(D_{\rm tot}\) 是标量总漂移，与删除算子 \(D\) 区分。

## 2. 次数增长时的完整实际多项式源

取主池缺额接口中的外部位数 \(Q=2d\)，参数仍为 \(d\)。此时
\(q_0=Q-2d=0\)，所以没有增加任何辅助位。接口使用的整个源是
\[
 {\cal E}_d=\ker\partial^3\cap{\cal P}_{d+1},\qquad
 {\cal U}_d=\ker\partial\cap{\cal P}_d,\qquad
                         \partial=\sum_i\partial_{x_i}.
\]
它们分别是上述完整 \(V,U\) 的固定系数坐标。尤其
\[
 \dim V=\binom Q{d-1}-\binom Q{d-2},\qquad
 \dim U=\binom Qd-\binom Q{d-1}.
\]
这些维数可以随 \(Q\) 很快增长，下面不按矩阵条目求和估计。

令 \(k=d+1\le Q\)。接口中的
\(\phi,\psi_\phi=\partial\phi-2\phi\)、全部硬特征及反射特征
\(\phi(\mathbf1-X)\) 都是次数至多 \(k\) 的多线性多项式。
其共同正积分权包括 \([t(1-t)]^{-d}\)，可以在端点发散；
实际特征的积分可积性已由完整接口证明。
因此多项式比较定理适用于这个同一硬空间与低源的**完整联合 Gram**，
再取实际 \(M^{-1}\) Schur，不需逐个处理指数多的坐标。

等权标定准确为
\[
                         H_0=L_0=2G_0,\qquad R_0=0.
\]
故只需控制该定理中的共同比较比 \(\Theta\)，就能得到
\[
                         \Phi\preceq(2\Theta^2+3\Theta)^2I.
                                                               \tag{2.1}
\]

## 3. 原尾的权比与累计偏差

置
\[
 r_x=(Q-1)/x,\qquad
                  \rho=(1+r_x)^4.
\]
由于 \(\overline w\) 位于最大、最小权平方之间，
\[
                         \rho^{-1}\le z_i\le\rho.       \tag{3.1}
\]
若 \(Q\le c\sqrt x\)，则 \(Q\ge2\) 给
\[
 r_x\le Q/x\le c^2/Q\le c^2/2,\qquad
                         \rho\le A_c^4.                \tag{3.2}
\]
由 \( (1+r)^4-1\le4(1+r)^3r\)，
\[
 \max_i|z_i-1|\le\rho-1
                       \le4A_c^3Q/x.                  \tag{3.3}
\]
记 \(S=\sum_i(z_i-1)^2\)。于是
\[
 S\le16A_c^6Q^3/x^2,\qquad
                         kS\le16A_c^6c^4.              \tag{3.4}
\]
同时
\[
                 k\log\rho
        =4k\log(1+r_x)\le4Q^2/x\le4c^2.                \tag{3.5}
\]
与只知道一个固定权区间相比，(3.4)–(3.5) 保住了“多项式次数也随位数增长”
时真正需要的费用。

## 4. 统一的共同 Gram 比较常数

在多项式比较定理中，可使用这一实际行的
\[
 a=\rho^{-1},\qquad b=\rho,\qquad
 \ell=\rho^{-1},\qquad v=\rho,\qquad D_0=0,\qquad S_0=S.
\]
密度比较常数可以取
\[
                  r_{\rm den}=e^{-S\rho^2/2}.
\]
两方向的完整条件多项式变换常数满足
\[
 {\cal M}_+
 \le\rho^{3k/2}\exp\!\left(\frac{\rho\sqrt{kS}}2\right),
\]
\[
 {\cal M}_-
 \le\rho^{3k/2}\exp\!\left(\frac{\sqrt\rho\sqrt{kS}}2\right)
 \le\rho^{3k/2}\exp\!\left(\frac{\rho\sqrt{kS}}2\right).
\]
因此同一全源上
\[
 \Theta=r_{\rm den}^{-2}({\cal M}_+{\cal M}_-)^2
           \le\exp\{S\rho^2+6k\log\rho+2\rho\sqrt{kS}\}. \tag{4.1}
\]
这个估计保留了正向、反向两个变换及密度归一化；没有只比较一个条件方差。

逐项代入 (3.2)–(3.5)：
\[
 S\rho^2
  \le16A_c^{14}Q^3/x^2
  \le8A_c^{14}c^4,
\]
\[
                         6k\log\rho\le24c^2,
 \qquad
                         2\rho\sqrt{kS}\le8A_c^7c^2.
\]
故
\[
                              \Theta\le e^{C_c}.        \tag{4.2}
\]
结合 (2.1) 与共同缩放不变性 (1.1)，得到 (0.3)–(0.4)。

当 \(c=1/4\) 时，\(A_c=33/32\)，
\((33/32)^7<5/4\)，故
\[
 C_c
   <\frac32+\frac58+\frac{25}{512}
    =\frac{1113}{512}<\frac94.
\]
这给出 (0.5)，无需再运行任何有限行数值搜索。

## 5. 与原 graph 的准确边界

本稿已经付的是：对原连续尾取出的每一个满足
\(Q\le c\sqrt x\) 的真实偶数有限段，其完整中央 primitive 源、
完整硬源、两个真实 Moore–Penrose 层间逆和硬投影共同满足 (0.3)。

它并未宣称这个有限段是整个无限尾的 \(D,D^*\) reducing 子空间。
在原全异权尾中，外部位的创建会离开有限段；把无限尾的完整逆先限制
到有限段，可能改变真正的 nuisance 与源度量，不能免费替换。
本稿也没有把中央出生 \(d-1,d\) 的相位界自动外推到该行的任意其他出生。

原 graph 中起点 \(x\) 与所需源宽度通常由另一组参数共同决定。
若实际所需连续头长远大于 \(\sqrt x\)，则 (0.3) 不能直接调用；
若分成多个短段，还须证明保留全部跨段 Schur、同一祖先源及两侧费用
的运输公式。这里给出的是一个原权值上的完整局部预算，跨段和
moving-source 接口仍须另付。
