# 原连续尾相位的定量宽窗费用：对称 Bernoulli 比较给 \(25e^{80Q^2/x}\)

日期：2026-11-14；工作标识789f。

## 0. 新增结论

保留[平方根宽偶段完整相位稿](2026-11-14-original-continuous-tail-square-root-windows-full-central-phase-bound-789f-next.md)
的原有限 Boolean 行、整个中央源及记号：
\[
 b_i=(x+i)^{-2},\quad 0\le i<Q,\quad
 Q=2d,\quad V=\ker D\cap{\cal H}_{d-1},
\]
\[
 \Phi={\cal H}^*\Gamma_2^{-1}{\cal H},\qquad
 {\cal H}=\Gamma_1^{-1}\Gamma_2-2\Gamma_1
                         -{\mathfrak e}^*P_U{\mathfrak e}|_V.
\]
全部中间逆与硬投影仍在完整实际源上。

**定理。** 对每个 \(2\le Q\le x\) 的偶数 \(Q\)，有明确的实际费用
\[
                         \boxed{\Phi\preceq
                                  25e^{80Q^2/x}I_V.}    \tag{0.1}
\]
因此当 \(Q\le c\sqrt x\) 且 \(Q\le x\) 时，可统一取
\(\kappa_c=25e^{80c^2}\)。尤其 \(Q\le\sqrt x/4\) 时可取 \(25e^5\)。

与前稿相比，本稿不只改善一个常数：当 \(Q\) 和 \(x\) 同阶时，
(0.1) 仍给整个源的指数费用，而不是仅在平方根窗口内给常数。
它仍未支付原无限 graph 的跨段运输。

证明仍使用[完整次数 Bernoulli 比较与同一 Schur](2026-11-14-bounded-degree-bernoulli-comparison-and-common-schur-phase-budget-789f.md)，
但用下面两项更精确的条件坐标界，并保留权的乘积熵。

## 1. 任意均值归一正权的对称比较

先取任意正权平方 \(z_1,\ldots,z_Q\)，准确满足
\[
                            \sum_i z_i=Q.
\]
定义
\[
 P=\prod_i z_i,\qquad
 S_{\rm sym}=\sum_i\frac{(z_i-1)^2}{z_i}.
\]
设 \(\rho\ge1\) 且 \(\rho^{-1}\le z_i\le\rho\)。

在原实际条件概率
\(p_i(t)=z_it/[1+t(z_i-1)]\) 下，标准化坐标关系是
\[
 Z_i=\delta_i(t)+\sigma_i(t)Y_i,
\]
\[
 \delta_i(t)=\frac{(z_i-1)\sqrt{t(1-t)}}{1+t(z_i-1)},
 \qquad
 \sigma_i(t)=\frac{\sqrt{z_i}}{1+t(z_i-1)}.
\]
因为分母随 \(t\) 单调，准确有
\[
                    \rho^{-1/2}\le\sigma_i(t)\le\rho^{1/2}.
                                                               \tag{1.1}
\]
这比把分子和分母的极值分开估计更强。

直接最大化一个二次分式给
\[
 \sup_{0\le t\le1}
      \frac{t(1-t)}{[1+t(z-1)]^2}=\frac1{4z},
 \quad\hbox{最大点 }t=\frac1{1+z}.
\]
同时
\[
 \frac{\delta_i(t)}{\sigma_i(t)}
          =\frac{(z_i-1)\sqrt{t(1-t)}}{\sqrt{z_i}}.
\]
故正向和反向移位都满足同一完整向量界
\[
 \|\delta(t)\|_2\le\frac{\sqrt{S_{\rm sym}}}{2},
 \qquad
 \|(\delta_i(t)/\sigma_i(t))_i\|_2
                             \le\frac{\sqrt{S_{\rm sym}}}{2}.
                                                               \tag{1.2}
\]
按已证平方自由系数移位的算子范数，任意次数至多 \(k\) 的多线性
多项式族可以同时取
\[
              {\cal M}_+,{\cal M}_-
                    \le\rho^{k/2}e^{\sqrt{kS_{\rm sym}}/2}.
                                                               \tag{1.3}
\]
这里保留了整个共同多项式空间及逆变换，没有按坐标或单项式个数求和。

## 2. 原混合密度的乘积界与完整相位

均值归一给 \(P\le1\)。对 \(0\le t\le1\)，凹性及
\(\sum_i(z_i-1)=0\) 给
\[
 \sum_i\log[1+t(z_i-1)]\ge t\sum_i\log z_i\ge\log P,
\]
\[
 \sum_i\log[1+t(z_i-1)]\le t\sum_i(z_i-1)=0.
\]
因此
\[
 P\le F(t)=\prod_i[1+t(z_i-1)]\le1,\qquad
                  P\le\rho_z(t)=F(t)/\int F\le P^{-1}.
                                                               \tag{2.1}
\]
它适用于完整高出生接口中的每个共同正积分权，包括实际可积特征
所配的端点奇异权。

将 (1.3)、(2.1) 代入完整联合 Gram–Schur 比较，得到
\[
 \Theta\le
              P^{-2}\rho^{2k}e^{2\sqrt{kS_{\rm sym}}},
\]
\[
 \log\Theta\le
              -2\log P+2k\log\rho+2\sqrt{kS_{\rm sym}}.   \tag{2.2}
\]
对每个 \(z>0\)，
\[
 z-1-\log z\le\frac{(z-1)^2}{z},
\]
因为右减左为 \(\log z+z^{-1}-1\ge0\)。求和并用均值归一，得
\[
                         -\log P\le S_{\rm sym}.        \tag{2.3}
\]
故也可用
\[
                 \log\Theta\le
                 2S_{\rm sym}+2k\log\rho
                                      +2\sqrt{kS_{\rm sym}}.     \tag{2.4}
\]

当实际物理来源为前述主池缺额接口、并保留全部硬 nuisance 时，
等权标定 \(H_0=L_0=2G_0,\ R_0=0\) 已证。因此
\[
                   \Phi\preceq(2\Theta^2+3\Theta)^2I.
\]
Since \(\Theta\ge1\), this implies the convenient estimate
\[
                              \Phi\preceq25\Theta^4I.  \tag{2.5}
\]
For the original even row below, \(q_0=0,\ k=d+1\le Q\); this is the
entire actual source, not a selected symmetric component.

## 3. A direct bound on \(S_{\rm sym}\) from the original weights

Let \(w_i>0\), let \(\overline w=Q^{-1}\sum_iw_i\), and set
\(z_i=w_i/\overline w\). Then exactly
\[
 S_{\rm sym}=\sum_i(z_i+z_i^{-1}-2)
             =Q\left[\left(\frac1Q\sum_iw_i\right)
                     \left(\frac1Q\sum_iw_i^{-1}\right)-1\right].
                                                               \tag{3.1}
\]
Suppose \(m\le w_i\le M\), and put \(\rho=M/m\). The elementary pointwise
inequality \((w_i-m)(M-w_i)\ge0\) gives
\[
              w_i+mM/w_i\le m+M.
\]
Averaging and then applying \(4ab\le(a+b)^2\) yields
\[
 \left(\frac1Q\sum_iw_i\right)
 \left(\frac1Q\sum_iw_i^{-1}\right)
                      \le\frac{(m+M)^2}{4mM}.
\]
Thus
\[
                        \boxed{S_{\rm sym}
                               \le Q\frac{(\rho-1)^2}{4\rho}.}   \tag{3.2}
\]
This proof uses the actual same list of weights on both sides of (3.1).
It does not separately replace its two averages by incompatible extrema.

For the original row \(w_i=(x+i)^{-4}\), set
\[
 r=(Q-1)/x,\qquad \rho=(1+r)^4.
\]
If \(Q\le x\), then \(0\le r\le1\). On this interval
\[
 \frac{\rho-1}{2\sqrt\rho}
     =\sinh(2\log(1+r))\le2r.                            \tag{3.3}
\]
An algebraic verification is immediate after putting \(A=1+r\in[1,2]\):
\[
 A^2-A^{-2}\le4(A-1)
 \quad\Longleftrightarrow\quad
 (A-1)^2(A^2-2A-1)\le0.
\]
Combining (3.2)–(3.3),
\[
 S_{\rm sym}\le4Qr^2\le4Q^3/x^2,\qquad
 \sqrt{kS_{\rm sym}}\le2Q^2/x,
\]
\[
                         k\log\rho
                    \le4kQ/x\le4Q^2/x.                 \tag{3.4}
\]

## 4. Original phase budget and its meaning

By (2.4), (3.4), and \(Q\le x\),
\[
 \log\Theta
       \le8Q^3/x^2+8Q^2/x+4Q^2/x
       \le20Q^2/x.
\]
Then (2.5) gives (0.1).

The initial normalization \(z_i=w_i/\overline w\) is a common positive
scaling of all deletion weights. The preceding original-tail note proves
that this scaling leaves \(\Phi\) exactly unchanged on the same physical
\(V\). No extra source condition number is introduced when returning to
(0.1).

Thus the exact row already supplies both regimes:

- \(Q=O(\sqrt x)\): one uniform finite phase constant;
- \(Q\le x\): an explicit full-source cost \(25e^{80Q^2/x}\), at most
  \(25e^{80Q}\).

The second statement may be relevant when a proposed graph argument can
pay exponential losses, but that payment has not been made here.
Multiplying the displayed costs over short segments is not justified
without a same-source composition theorem for all cross-segment Schur
terms, inverse layers and both physical energy sides. The finite row
is likewise not asserted to reduce the entire infinite-tail \(D,D^*\).
