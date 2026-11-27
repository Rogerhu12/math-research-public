# R1082：原 Gaussian 近 p² Hurwitz 系数的完整短卷积降阶

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明。** 取原 supersingular Gaussian reference
$$
E_a:y^2=x^3+ax,\qquad a\in\mathbf F_p^\times,\qquad
p\ge41,\quad p\equiv3\pmod4,\qquad \omega=dx/(2y).
$$
在同一 marked CM lift、同一 tangent-one 整 eigenparameter $T$ 中，令
$$
d=p^2-4p-1,\qquad
\mathcal H_p=
2G_{p-3}+
\sum_{\substack{i+j=p-3\\i,j\ge4,\ i,j\ {\rm even}}}G_iG_j.
\tag{1082.1}
$$
每个 $G_i$ 均取原 additive-coordinate Hurwitz 规范；在 Gaussian 行，
不被四整除的下标项严格为零。原 Deuring primitive 的单位仍记
$D\Psi=\delta$，其中 $D=d/\omega$。则
$$
\boxed{\quad
\overline{G_d}=\frac{\mathcal H_p^{\,p}}{2\delta}
             =\frac{\mathcal H_p}{2\delta}.
\quad}
\tag{1082.2}
$$
最后一个等号只在当前 $\mathbf F_p$ reference 上使用。
$\mathcal H_p$ 是**完整**卷积，没有删除任何 regular 项。

因此 R1071 第一 forced 角色在原 $j=1728$ coarse component 上的
真实斜率非零，准确等价于 $\mathcal H_p\ne0$。
本文没有证明这个指定卷积为单位；尤其不能由其中
$2G_{p-3}\ne0$ 排除其余项相消。

## 1. 原参数、低分母和高系数整性

固定 R1071 §11 与 R1079 的同一实际 CM lift 和参数。
以 $z_{\rm add}$ 表示原 invariant logarithm，有
$$
z_{\rm add}(T)=T+O(T^{p^2}),\qquad
\omega=(1+O(T^{p^2-1}))\,dT.
\tag{1082.3}
$$
第一式在同一个 characteristic-zero lift 中成立；
第 $p^2$ 项可含 $p$ 分母，本文不将它整体约化。
原 Hurwitz 定义是
$$
x(z_{\rm add})=z_{\rm add}^{-2}
+\sum_{\substack{j\ge4\\j\ {\rm even}}}(j-1)G_jz_{\rm add}^{j-2}.
\tag{1082.4}
$$

将 (1082.3) 代入首负二极，可能改变的最早次数为 $p^2-3$。
本篇读取的次数
$$
d-2=p^2-4p-3<p^2-3
$$
严格在其前。因此原整 Laurent series $x(T)$ 的这一系数
准确为 $(d-1)G_d$。因 $d-1\equiv-2\pmod p$ 是单位，
这同时证明本篇的 $G_d$ 在此实际 reference 上 $p$-整。
没有借一个尚未整的高阶 $\zeta$ series 反向定义它。

对 $4\le j\le p-3$ 的偶数，低 $G_j$ 的整性由
$$
G_j=2\mathcal E_j/(j-1)!
$$
及 R1075 的 coefficient-one Eisenstein 归一给出。
所有阶乘小于 $p$，Bernoulli 常数也不含 $p$ 分母。
$G_{p-1}=0$ 则由 Gaussian CM 权严格得到，因 $4\nmid p-1$。
所以以下有限 Laurent polynomial 确实可约化：
$$
Z(T)=T^{-1}
-\sum_{\substack{4\le j\le p-1\\j\ {\rm even}}}\overline{G_j}T^{j-1}.
\tag{1082.5}
$$
R1079 给的是实际整 $T$ 中的准确短 carry：
$$
\Psi(T)=Z(T)^p+\delta T+O(T^{p^2}).
\tag{1082.6}
$$
它不表示完整 characteristic-zero $\zeta^p$ 可约化到该精度。

## 2. Gaussian 原 Ψ、β 与两个导数的全局归一

写 $p=4r-1$。R1079 §2.2 的原函数为
$$
\Psi=y\sum_{j=0}^{r-1}c_jx^{2j},\qquad
c_{r-1}=-1,\qquad
\frac{c_j}{c_{j-1}}=-\frac{4j-1}{a(4j+1)}.
\tag{1082.7}
$$
因为
$$
D(yx^{2j})=(4j+3)x^{2j+2}+a(4j+1)x^{2j},
$$
准确有
$$
D\Psi=\delta=ac_0\in\mathbf F_p^\times.
\tag{1082.8}
$$
递推的全部整数因子在 $1,\ldots,p-1$ 内，且 $a\ne0$。
原 $x\sim T^{-2},y\sim-T^{-3}$ 与 $c_{r-1}=-1$
使 $\Psi$ 的首极正是 $T^{-p}$，没有另乘单位。

原 relative Cartier 系数为
$$
\beta=
[X^{p-2}](X^3+aX)^{(p-1)/2}
=\binom{2r-1}{r-1}a^r\in\mathbf F_p^\times,
\quad C_{\rm rel}(x\omega)=\beta\omega'.
\tag{1082.9}
$$
它等于 $x(T)\omega/dT$ 的 $T^{p-1}$ 系数。
全局 differential $\Psi x\omega$ 只有 $O$ 一个 pole。
在 (1082.3)、(1082.6) 的范围内，其 residue 只有两项：
首 $T^{-p}$ 与 $x$ 的 $T^{p-1}$ 项给 $\beta$，
$\delta T$ 与首 $T^{-2}$ 给 $\delta$。
其余指数不能贡献，故 residue theorem 给
$$
\boxed{\beta=-\delta.}
\tag{1082.10}
$$

现在支付两个全局导数的准确常数。
特征 $p$ 中 $D^p$ 仍是平移不变的 derivation，
所以是 $D$ 的常数倍。
由 (1082.3) 在 $O$ 读取 $D^pT$ 的常数项为零，得 $D^p=0$。

因此 $D^{p-1}x$ 是一个 $p$ 次幂函数，且只在 $O$
有至多 $p+1$ 阶 pole。椭圆曲线上只在 $O$ 有 pole 的
非恒定函数，最小 pole 阶为二；其 $p$ 次幂最小为 $2p>p+1$。
故 $D^{p-1}x$ 是常数。用 (1082.3) 读取常数项，
$$
D^{p-1}x=(p-1)!\,\beta=-\beta=\delta.
$$
$D^{p-2}x$ 的首极为
$$
(-1)^{p-2}(p-1)!\,T^{-p}=T^{-p}.
$$
它与 $\Psi$ 导数相同，首极相同，差仅能为常数；
二者均为奇函数，所以
$$
\boxed{D^{p-2}x=\Psi.}
\tag{1082.11}
$$

定义原偶函数
$$
\mathcal R=\frac{\Psi^2-x^p}{2\delta}.
\tag{1082.12}
$$
其导数为 $\Psi$。
(1082.6) 显示首 $T^{-2p}$ 精确抵消，
余下的首负项为 $T^{1-p}$；它没有其它负项，
所以 $\mathcal R$ 只在 $O$ 有恰 $p-1$ 阶 pole。
另一方面 $D^{p-3}x$ 有相同导数和首项，
因为 $(p-2)!=1\pmod p$。
两者之差为常数。
在实际 $\mu_4$ 作用 $T\mapsto\xi T$ 下，
二者权均为 $1-p\equiv2\pmod4$，常数被排除。
因此
$$
\boxed{\quad D^{p-3}x=\mathcal R
       =(\Psi^2-x^p)/(2\delta).\quad}
\tag{1082.13}
$$

这里“差为常数”也可直接由差的导数为零、唯一 pole 小于 $2p$
得到，未假设任意 characteristic-$p$ primitive 唯一。

## 3. 近 p² 的指定系数准确降为短平方差

置
$$
M=p(p-5),\qquad M+p-3=d-2.
$$
由 (1082.3)，在 $D^{p-3}x$ 中，
把 $D$ 换为普通 $\partial_T$ 所能产生的最早误差次数至少
$p^2-p$，严格高于 $M$。
例如一次误差带 $T^{p^2-1}$，原首极是二，
再施至多 $p-4$ 次导数后最早仍为 $p^2-p$；
多次误差只会更高。

因此
$$
[T^M]\mathcal R
=(p-3)!\,[T^{d-2}]x
=(p-3)!(d-1)\overline{G_d}.
$$
这里下降阶乘的每个因子模 $p$ 依次为
$p-3,p-4,\ldots,1$，没有跨过一个零因子。
Wilson 给 $(p-3)!=-1/2$，而 $d-1=-2\pmod p$，故
$$
[T^M]\mathcal R=\overline{G_d}.
\tag{1082.14}
$$

将 (1082.6) 平方时，误差与首负 $p$ 极相乘的最早次数为
$p^2-p>M$。所以在 $T^M$ 处，(1082.12) 准确成为
$$
\mathcal R=
\frac{Z^{2p}-x^p}{2\delta}+TZ^p+\frac{\delta T^2}{2}
\quad\text{至本次所需精度}.
$$
$TZ^p$ 的所有指数都是 $1\bmod p$，不贡献于 $M$；
最后一项也不贡献。Frobenius 逐系数给
$$
[T^M]\mathcal R
=\frac1{2\delta}
\left([T^{p-5}](Z^2-x)\right)^p.
\tag{1082.15}
$$

完整展开这个低系数：
$$
[T^{p-5}]Z^2
=-2G_{p-3}+
\sum_{\substack{i+j=p-3\\i,j\ge4,\ i,j\ {\rm even}}}G_iG_j,
\qquad
[T^{p-5}]x=(p-4)G_{p-3}.
$$
所以差的单项系数是 $-(p-2)G_{p-3}=2G_{p-3}\pmod p$，
恰为 (1082.1)。结合 (1082.14)–(1082.15) 证明 (1082.2)。
在扩域或运输标架时，先保 (1082.15) 的实际 $p$ 次幂；
只有当前 $\mathbf F_p$ 参考才能删去它。

## 4. 回到同一个原 Gaussian cuspidal 斜率

使用 R1071 的奇数 regularizer $c$，其模 $p$ 是 primitive，
以及第一 forced 角色
$$
\chi=\omega^{p-3},\qquad
\kappa_\chi=c^2-c^{-4}\ne0.
$$
同一 sigma/division identity 为
$$
\psi_c(z_{\rm add})
=\sigma(cz_{\rm add})/\sigma(z_{\rm add})^{c^2}.
$$
取同一个 $d\log$，有
$$
d\log\psi_c=(1-c^2)\frac{dz_{\rm add}}{z_{\rm add}}
-\sum_j(c^j-c^2)G_jz_{\rm add}^{j-1}dz_{\rm add}.
$$
改变到原 $T$ 时，首 pole 的 regularizer 修正从次数
$T^{p^2-2}dT$ 才开始，严格高于 $d-1$。
这说明原 R1071 的指定 coefficient 满足
$$
\boxed{\quad A_d=-(c^d-c^2)\overline{G_d}
                  =\kappa_\chi\overline{G_d}.\quad}
\tag{1082.16}
$$
这里 $d\equiv-4\bmod p-1$，且所有实际 first-lift 数据相同；
没有改用任意 Weierstrass 参数的 coefficient。

R1071 §15 的 Lucas 消去使该 fine polynomial 次数至多三；
Gaussian $\mu_4$ 使它只含 $i=0,2$。
其 $i=2$ 恰读取
$$
N=(p+1)(p-3),\qquad d_2=N-2(p-1)=d,
\quad \binom{d-1}{1}/2=-1\pmod p.
$$
保全部原节点尺度，得到原 coarse 参数
$T_{\rm coarse}=t^2$ 上的完整式
$$
\boxed{\quad
\mathcal P_{\chi,s}(T_{\rm coarse})-\mathcal P_{\chi,s}(0)
=\beta_0^d\lambda^2\kappa_\chi
  \frac{\mathcal H_p^p}{2\delta}\,T_{\rm coarse}.
\quad}
\tag{1082.17}
$$
若该实际角色 Bernoulli-good，除以 R1071 的真实 circular-unit
coefficient $b_\chi$ 后，
$$
\boxed{\quad
c_{\chi,s}(T_{\rm coarse})-c_{\chi,s}(0)
=-\frac{\beta_0^d\lambda^2}{4b_\chi\delta}
 \mathcal H_p^p\,T_{\rm coarse}.
\quad}
\tag{1082.18}
$$
$\beta_0,\lambda,b_\chi$ 中原 Weil phase 全部保留。
原 Gaussian 两条 quartic-twist descent lines 仍按 R1071 §8 一起运输，
不能只取一个平方像。
未除圆单位基的 (1082.17) 不要求 Bernoulli-good。

## 5. 同一短卷积的真实 sigma-heat 读数

这个步骤给原 transverse derivative 身份，不给其非零性。
在通用曲线 $y^2=x^3+ax+b$ 上，取同一 sigma 归一，
定义原 Serre 向量场
$$
\partial=6b\,\partial_a-\frac43a^2\,\partial_b.
\tag{1082.19}
$$
经典 Weierstrass heat equation 在
$g_2=-4a,g_3=-4b$ 下准确为
$$
\partial\sigma=\frac12\sigma''-\frac a6 z_{\rm add}^2\sigma.
$$
于是
$$
\partial\log\sigma
=\frac{\zeta^2-x}{2}-\frac a6z_{\rm add}^2.
\tag{1082.20}
$$
此处 $\sigma''/\sigma=\zeta^2-x$，所有符号与原微分一致。

只读取 $z_{\rm add}^{p-5}$，其次数大于二、小于 $p$。
全部 $G_{p-5}$ 及 $1/(p-5)$ 在通用系数环中 $p$-整。
由 $\log(\sigma/z_{\rm add})=-\sum_jG_jz_{\rm add}^j/j$，
在 Gaussian $b=0$ 点准确得到
$$
\boxed{\quad
\mathcal H_p=\frac25(\partial G_{p-5})(a,0)
=-\frac{8a^2}{15}
 \left(\frac{\partial G_{p-5}}{\partial b}\right)(a,0).
\quad}
\tag{1082.21}
$$
这由**通用模参数**上的原 heat identity 先推导再特化。
不对 R1075 仅在 Hasse 零点成立的值式直接求导。
特别 $G_{p-5}(a,0)=0$ 不决定它的 transverse derivative。

直接同模型的已刊来源为 J. C. Eilbeck、J. Gibbons、Y. Ônishi、S. Yasuda，
*Theory of heat equations for sigma functions*, Glasgow Math. J. **67** (2025),
365–422，§6.3，(6.4)、(6.8)，
[DOI](https://doi.org/10.1017/S0017089524000417)。其 $\mu_4=a,\mu_6=b$，
根会话亲读的 (6.8) 即 $(\partial-\tfrac12\partial_z^2+a z^2/6)\sigma=0$，
故没有额外微分尺度。另一个已刊表述为 J. Bernatska,
*Abelian Function Fields on Jacobian Varieties*, Axioms 14 (2025), 90,
§2.7 (31)–(32)，
[全文](https://www.mdpi.com/2075-1680/14/2/90)。
其算子为
$$
6g_3\partial_{g_2}+\frac13g_2^2\partial_{g_3}
-\frac12\partial_z^2-\frac1{24}g_2z^2;
$$
代入所示 $g_2,g_3$ 即为 (1082.20)。
本篇只消费这一椭圆 heat identity，不调用高 genus 或未付的有限域非零命题。

## 6. 已支付的范围与仍需证明的指定非零

与 R1075 相同的同权 divisor-sum 论证，以低权四替代六，给
$$
\mathcal T^{p-4}\mathcal E_4
=H^{p-3}\mathcal E_{p-3}-\mathcal E_{p-3}^p,
\qquad
G_{p-3}^p=6\beta^{p-4}G_4.
$$
这里保完整 Frobenius 项；
$\prod_{j=4}^{p-1}j=-1/6$、$(p-4)!=1/6$ 支付两个尺度。
因 $G_4=-a/15$、$\beta=-\delta$，当前参考上
$$
G_{p-3}=\frac{2a}{5\delta^3}\ne0.
\tag{1082.22}
$$
但 (1082.1) 的其余完整卷积仍存在。
(1082.22) 不是 $\mathcal H_p\ne0$ 的证明；
实际 Gaussian coarse 注入仍待这个指定非零输入。

本结果完成的是原近 $p^2$ coefficient、原 first-lift、
完整低卷积、真实 heat transverse derivative 与原标签斜率之间的
准确来源桥。它没有把这一 Gaussian 读数换成 O2 的
$r=2,8$ bare coefficient、原 $f_N/e$、或短 $D^6$ 的
$\eta_k,\nu_k$；这些来源各自保持。

来源：R1071 §§11、15–16；R1075 原 Hurwitz/Cartier 规范；
R1079 的整 eigen-$T$ 短 carry；本篇给出其余全局导数、
所有误差次数、Wilson 因子及完整卷积证明。
全部为纸面推导，没有运行数学程序，也没有新扫或重跑任何 prime 窗口。
