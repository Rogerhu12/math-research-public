# 实际 theta 因子的全局 Hurwitz 整数与多项式流

日期：2026-11-12。状态：已证明。这里的整数序列来自 R51 的实际
固定因子，不是逐素数另选的测度，也不需要外部 sigma 整性定理。
本文未证明无穷多个素数处的中心斜率非零。

## 1. 无分母的四变量系统

对参数 $D$，令
$$
E_D:y^2=x^3-Dx,\qquad
x(z)=\wp_D(z),\quad \zeta_D'=-x,\quad
\sigma_D(z)=z+O(z^5).
$$
在原点取
$$
u=x^{-1/2}=z+O(z^5),\qquad
\vartheta_D=\frac{\sigma_D}{u},\qquad
L=(\log\vartheta_D)',\qquad v=u'.
\tag{1}
$$
这与 R51 中 $\vartheta_D^2=x\sigma_D^2$、$\vartheta_D(0)=1$
的规范完全一致。由 $(x')^2=4(x^3-Dx)$，
$$
(u')^2=1-Du^4,\qquad u''=-2Du^3.
$$
再直接求导：
$$
L'=-x-\frac{u''}{u}+\left(\frac{u'}u\right)^2
=-\frac1{u^2}+2Du^2+\frac{1-Du^4}{u^2}
=Du^2.
$$
于是四个函数满足
$$
\boxed{
u'=v,\quad v'=-2Du^3,\quad L'=Du^2,\quad
\vartheta_D'=L\vartheta_D;
\quad (u,v,L,\vartheta_D)(0)=(0,1,0,1).
}
\tag{2}
$$
右端是 $\mathbb Z[D]$ 上的多项式，初值也在此环中。

对特征零环 $R$，记
$$
\mathcal H_R=
\left\{\sum_{n\ge0}a_n\frac{z^n}{n!}:a_n\in R\right\}.
$$
此环的乘法系数是整数二项式卷积，求导就是系数移位。
因此 (2) 逐阶唯一确定所有导数，且归纳地给出
$$
u,v,L,\vartheta_D\in\mathcal H_{\mathbb Z[D]},\qquad
\sigma_D=u\vartheta_D\in\mathcal H_{\mathbb Z[D]}.
\tag{3}
$$
这里没有把普通幂级数环的整性与 Hurwitz 整性混为一谈。
例如 $\sigma_D=z-Dz^5/60+\cdots$，其第五个 Hurwitz 系数为 $-2D$。

还可把 (2) 写成一个固定整导子
$$
\mathscr V=
v\partial_u-2Du^3\partial_v+Du^2\partial_L+
L\theta\partial_\theta
\quad\text{作用于 }\mathbb Z[D,u,v,L,\theta].
\tag{4}
$$
任一多项式 $P$ 沿此流的第 $n$ 个 Hurwitz 系数，就是
$\mathscr V^nP(0,1,0,1)$。这是全局整数递推，而不是先固定 $p$
再由 Kummer 同余获得的整性。

## 2. 实际乘积中的 $1/5$ 完全消去

设 $\beta=2+i$，则
$$
\beta\bar\beta=5,\qquad \beta^4=-7+24i.
$$
由 (2) 的唯一性，或直接由 Weierstrass 缩放公式，
$$
\vartheta_D(az)=\vartheta_{Da^4}(z),\qquad
\frac{\sigma_D(az)}a=\sigma_{Da^4}(z).
\tag{5}
$$
在第二式中，先取 $a\ne0$；其两边的每个 Hurwitz 系数实际上
都只是 $D,a$ 的整系数多项式，因而没有引入 $a$ 的分母。

R51 的实际因子为
$$
A_D(z)=\frac15\vartheta_D(z)\vartheta_D(2z)\sigma_D(z)^2
\sigma_D(\beta z)\sigma_D(\bar\beta z).
$$
把 $1/5=1/(\beta\bar\beta)$ 分给最后两个因子，得
$$
\boxed{
A_D=
\vartheta_D\,\vartheta_{16D}\,\sigma_D^2\,
\sigma_{(-7+24i)D}\,\sigma_{(-7-24i)D}
\in\mathcal H_{\mathbb Z[i,D]}.
}
\tag{6}
$$
复共轭交换最后两个因子而固定其余因子。因此其 Hurwitz 系数
同时在 $\mathbb Q[D]$ 和 $\mathbb Z[i,D]$ 中，故在 $\mathbb Z[D]$ 中。
特别地，不需要除去 $2,5,17$ 中任何一个素数：
$$
\boxed{h_m:=m!b_m=A_{17}^{(m)}(0)\in\mathbb Z\quad(m\ge0).}
\tag{7}
$$

由于 $\vartheta_D(iz)=\vartheta_D(z)$、
$\sigma_D(iz)=i\sigma_D(z)$，$A_D$ 仅有 $4$ 的倍数次幂，
最低项为 $z^4$。再次用 (5) 或对 $D$ 赋权 $4$，可得唯一整数
$a_k$，满足
$$
\boxed{
A_D(z)=\sum_{k\ge1}D^{k-1}a_k\frac{z^{4k}}{(4k)!},
\qquad a_k\in\mathbb Z,\qquad a_1=24.
}
\tag{8}
$$
这里的 $A_D$ 是由 (6) 定义的统一解析族；只有 $D=17$ 被 R51
认定为本课题所需的中央 theta 因子，不把其他 $D$ 自动解释为秩二曲线。

## 3. 有限个整多项式流即可生成整条序列

取四份 (2)，其参数分别为
$$
D,\quad16D,\quad(-7+24i)D,\quad(-7-24i)D.
$$
在这四份变量的整多项式环上，把四个导子相加为 $\mathscr V_{\rm tot}$。
记各份的坐标为 $(u_j,v_j,L_j,\theta_j)$，取
$$
P=u_1^2u_3u_4\,\theta_1^3\theta_2\theta_3\theta_4.
\tag{9}
$$
则
$$
h_m(D)=
\mathscr V_{\rm tot}^mP\bigm|_{u_j=L_j=0,\ v_j=\theta_j=1}.
\tag{10}
$$
因为 $\sigma_j=u_j\theta_j$，(9) 正是 (6)，没有遗漏重复的
$\theta_1$ 因子。共轭作用交换第 $3,4$ 份，说明 (10) 的值在
$\mathbb Z[D]$ 中。

为便于独立计算，还可先只算参数 $D=1$ 的一份系统，再用 (5)
缩放并作整数二项式卷积。记 $u_n=u^{(n)}(0)$、
$\ell_n=L^{(n)}(0)$、$t_n=\vartheta^{(n)}(0)$，则
$$
\begin{aligned}
q_n&=\sum_{j=0}^n\binom nj u_j u_{n-j},\\
u_{n+2}&=-2\sum_{j=0}^n\binom nj u_jq_{n-j},\\
\ell_{n+1}&=q_n,\\
t_{n+1}&=\sum_{j=0}^n\binom nj\ell_jt_{n-j},\\
s_n&=\sum_{j=0}^n\binom nj u_jt_{n-j}.
\end{aligned}
\tag{11}
$$
初值为 $u_0=0,u_1=1,\ell_0=0,t_0=1$。
$s_n$ 是 $\sigma_1$ 的 Hurwitz 系数。
所有步骤仅使用整数加乘；参数 $-7\pm24i$ 只需高斯整数加乘。

[整数递推脚本](../scripts/check-theta-hurwitz-integers.py)
实现 (11) 与 (6)，不输入中央迹或 $p$-进 $L$ 值。
它与 R51 已认证的 $b_4,b_8,b_{12},b_{16}$ 精确一致。

## 4. 对无周期极限及全局路线的准确含义

R56 的
$C_{p,n}=(m_n-1)!b_{m_n}$、$m_n=(p-1)p^n$ 现在可写为
$$
C_{p,n}=\frac{h_{m_n}}{m_n},\qquad h_{m_n}\in\mathbb Z.
\tag{12}
$$
所以它的约分后分母确实整除 $m_n$，而不只是“在除有限个素数外整”。
相应地，对所有素数 $\ell$，
$$
v_\ell(b_m)\ge-v_\ell(m!),\qquad
v_\ell((m-1)!b_m)\ge-v_\ell(m).
\tag{13}
$$
对目标普通 $p$，R56 还给 $C_{p,n}\in p\mathbb Z_p$，
故 $p^{n+1}\mid h_{m_n}$。若该处斜率为零，更有
$p^{2n+2}\mid h_{m_n}$：这是
$J_p(T)=O(T^2)$、$v_p(T_n)=n+1$ 直接作用于真实矩公式的结果。

这些结论没有把整数性偷换为赋值上界。特别是：

- 同一整数上仅使用 $p-1\mid m$ 或有限个类似同余分支的整除乘积，
  仍受 R15 的除数计数界限制；本篇不重新以该乘积声称矛盾。
- (4)、(10) 是固定维数的**非线性**整多项式流。
  迭代导子一般提高多项式次数；并未证明 $h_m$ 满足固定阶线性递推，
  也未得到一个固定秩线性 Frobenius 系统。
- 因而现在可以在一个完全明确的整数序列 $a_k$ 上研究额外的全局
  结构，但无穷多个 $p$ 的 $J_p'(0)\ne0$ 仍是待证目标。

### 使用的既有结论

R51（2026-11-12）的实际乘积与规范；
R56（2026-11-12）的无周期有理极限；
R15（2026-11-12）的有限分支同步计数。
本篇整性证明只用 (1)–(11)，没有引用尚待核查的外部 sigma 整性论证。
