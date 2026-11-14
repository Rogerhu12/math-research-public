# 首个滤子的全局分母与实际 Hurwitz jet 饱和

日期：2026-11-12。状态：下面的坐标环注入、首个全局分母、惰性 Euler
原函数 Hurwitz 整性及真实 Taylor 核均已证明。它们明确显示全局系数格
与 jet 饱和格的区别；没有据此给一般有限前缀 minors 的下界。

## 1. 实际单流坐标没有额外特征零多项式关系

在 $E_0:y^2=x^3-x$ 上，取 R57 的

$$
u=x^{-1/2},\quad v=u',\quad L=\theta'/\theta,
\quad\theta=\theta_T=\sigma/u.
$$

它们满足 $v^2+u^4=1$ 及

$$
u'=v,\qquad v'=-2u^3,\qquad L'=u^2,\qquad\theta'=L\theta.
\tag{1.1}
$$

令 $\Gamma$ 为原平方格。$u,v$ 对 $2\Gamma$ 周期；对
$\lambda\in2\Gamma$，sigma 准周期式给

$$
L(z+\lambda)=L(z)+\eta_\lambda,
$$

$$
\theta(z+\lambda)=\chi(\lambda)
 \exp\bigl(\eta_\lambda(z+\lambda/2)\bigr)\theta(z),
\qquad \eta_\lambda=\bar\lambda/\mathcal A,
\quad |\chi(\lambda)|=1.
\tag{1.2}
$$

**命题。** $z,L,\theta$ 在 $\mathbb C(u,v)$ 上代数独立。

**证明。** 假设有非零关系
$\sum_{k=0}^M P_k(z,L)\theta^k=0$，其中
$P_k\in\mathbb C(u,v)[Z,W]$，$P_M\ne0$。
选一个避开所有极点及 theta 零点的复点 $z_0$。
取 $2\Gamma$ 的两个基 $\lambda_1,\lambda_2$。
平移后 $u,v$ 均不变，$(z,L)$ 分别增加
$(\lambda_1,\eta_1)$ 与 $(\lambda_2,\eta_2)$。
这两个复向量线性无关，因为
$\lambda_1\bar\lambda_2-\lambda_2\bar\lambda_1\ne0$。

固定整数 $m$，沿 $z=z_0+m\lambda_2+n\lambda_1$ 令 $n\to+\infty$。
由 $\eta_1\lambda_1=|\lambda_1|^2/\mathcal A>0$，最高的 theta 次幂
比其余各项至少多一个 $\exp(cn^2+O(n))$ 因子。
除以该最高次幂后，$P_M$ 沿此直线是一个随 $n$ 指数趋零的多项式，
故必恒为零。对所有 $m$ 皆然，说明它在上述二维整数格上恒为零。
该格经一个可逆复线性变换就是 $\mathbb Z^2$，所以作为
$(Z,W)$ 的多项式，它的每个系数在 $u(z_0),v(z_0)$ 处都为零。
令 $z_0$ 变化，得到 $P_M=0$，矛盾。
若 $M=0$，直接使用同一二维格的多项式零性即可。$\square$

因此下述自然坐标环确实注入实际亚纯函数域：

$$
\mathcal R_{(p)}=
 \mathbb Z_{(p)}[z,u,v,L,\theta]/(v^2+u^4-1),
\qquad p\ge7.
\tag{1.3}
$$

本篇的 $1/5$ 在这个环中为单位。它对 $p$ 无挠；其模 $p$ 约化也是
整环，因为 $1-u^4$ 在 $\mathbb F_p(u)$ 中不是平方。
该注入只排除完全相同特征零解析函数的多项式改写，不会使模 $p$
Taylor 映射也注入。

## 2. 首个 Newton 投影的分母在全局环中确实存在

记

$$
A=\theta^{17}\left(u^4+\frac35u^8-\frac15u^{12}+\frac15u^{16}\right),
\qquad \mathscr H(z)=\int_0^zA(w)\,\frac{dw}w.
$$

令 $D=\partial_z+\mathscr V$，其中 $\mathscr V$ 是 (1.1) 的整导子；
置 $\mathscr E=zD$，并用 $\mathscr E\mathscr H=A$ 扩张它。
取惰性 $p=4r-1\ge7$，对
$\epsilon(n)=\mathbf1_{r\mid n}$ 定义

$$
Q_p(Y)=\sum_{k=0}^{p}\Delta^k\epsilon(0)\binom Yk,
\qquad \Pi_p=Q_p(\mathscr E/4).
\tag{2.1}
$$

这是前篇在截断次数 $4p$ 的实际原始 jet 投影。
$Q_p(0)=1$，所以

$$
P_p^{\mathrm{flow}}:=\Pi_p\mathscr H-\mathscr H
\in\mathcal R_{(p)}\otimes\mathbb Q
\tag{2.2}
$$

是只含原流坐标的多项式。各 Newton 项至多带一个 $p$ 分母，故
$pP_p^{\mathrm{flow}}\in\mathcal R_{(p)}$。

**准确剩余式：** 在 (1.3) 模 $p$ 的坐标环中，

$$
\boxed{\quad
pP_p^{\mathrm{flow}}
 \equiv-\frac14 T_p,
\qquad
T_p:=\sum_{k=0}^{p-1}\frac{(-z)^k}{k!}\mathscr V^kA.
\quad}
\tag{2.3}
$$

**证明。** 由于 $p=4r-1$，有
$\Delta^p\epsilon(0)=\sum_{l=0}^3(-1)^{p-lr}\binom p{lr}
\equiv-1\pmod p$。又 $(p-1)!\equiv-1\pmod p$。
因此乘以 $p$ 后，只有最高 Newton 项留下，准确为

$$
p\Pi_p\mathscr H
 \equiv\bigl((\mathscr E/4)^p-\mathscr E/4\bigr)\mathscr H
 =\frac14(\mathscr E^p-\mathscr E)\mathscr H.
$$

在 $z$ 可逆的环中，$Dz=1$ 给出 Weyl 代数恒等式
$\mathscr E^p-\mathscr E=z^pD^p$。因为 $D\mathscr H=A/z$，
Leibniz 公式及 Wilson 定理给

$$
z^pD^{p-1}(A/z)
 =-\sum_{k=0}^{p-1}\frac{(-z)^k}{k!}D^kA=-T_p\pmod p.
$$

$A$ 不含独立坐标 $z$，所以 $D^kA=\mathscr V^kA$。
等式两边已经是未局部化环中的多项式，故得到 (2.3)。$\square$

把独立坐标 $z$ 设为零，右边是 $-A/4\ne0$。因此

$$
pP_p^{\mathrm{flow}}\notin p\mathcal R_{(p)},
\qquad P_p^{\mathrm{flow}}\notin\mathcal R_{(p)}.
\tag{2.4}
$$

结合 §1 的注入，不能靠特征零坐标多项式关系把同一个实际函数
$P_p^{\mathrm{flow}}$ 改写成这个全局整环的元素。
下面的结果同时说明，这个全局分母确实会被实际 Taylor 格吸收。

## 3. 所有惰性处的 Euler 原函数都 Hurwitz 整

写 $A=\sum\beta_mz^m$、$h_m^{(1)}=m!\beta_m\in\mathbb Z$。
由全余类 Stokes 变换，若 $m=dk+j>0$、
$j\in\{0,4,\ldots,d-4\}$，则

$$
\beta_m=a^k\mathcal J_{p,j}(k)/k!,\qquad
v_p(a)=-1,\qquad \mathcal J_{p,j}(k)\in\mathbb Z_p.
\tag{3.1}
$$

这里当 $k=0$ 时必有 $j>0$，而 $j=0$ 时必有 $k\ge1$。
因此 $m-1=pk+k+j-1\ge pk$。记
$q=\lfloor(m-1)/p\rfloor\ge k$。Legendre 公式直接给

$$
v_p((m-1)!)=q+v_p(q!)\ge k+v_p(k!).
\tag{3.2}
$$

结合 (3.1)，得到对全部 $m$ 的定理

$$
\boxed{\qquad
\frac{h_m^{(1)}}m=(m-1)!\beta_m\in\mathbb Z_p,
\qquad
\mathscr H\in\mathcal H_{\mathbb Z_p}
\quad(p\ge7,\ p\equiv3\bmod4).
\qquad}
\tag{3.3}
$$

不是四倍数的系数本来为零。原 $E_{17}$ 整数只相差
$h_{4r}^{(17)}=17^{r-1}h_{4r}^{(1)}$，因此 (3.3) 同样成立。
此证明只使用已证全余类整性和一个阶乘不等式，没有加入新的分布
或 p 曲率猜想，也没有要求中央导数为零。

## 4. 实际模 $p$ Taylor 核与饱和方向

沿 (1.1) 的初值，令

$$
\operatorname{ev}_{\mathrm H}(F)
 =\sum_{n\ge0}(D^nF)(0,0,1,0,1)\frac{z^n}{n!}
\in\mathcal H_{\mathbb Z_p}.
\tag{4.1}
$$

初值的坐标顺序为 $(z,u,v,L,\theta)$。
Leibniz 的整数二项式公式使这个 Hurwitz Taylor 映射成为环同态。

(2.1) 的多项式在每个非负整数 $n$ 都取整数值，因为它以整数
系数写成 $\binom Yk$ 的线性组合。
$\mathscr H$ 只含四倍数次幂，所以 $\Pi_p$ 对其第 $4n$ 个 Hurwitz
系数只乘整数 $Q_p(n)$。由 (3.3)，

$$
\operatorname{ev}_{\mathrm H}(P_p^{\mathrm{flow}})
 =\Pi_p\mathscr H-\mathscr H\in\mathcal H_{\mathbb Z_p}.
\tag{4.2}
$$

这对所有阶的 Hurwitz jet 成立，不只到次数 $4p$。
由 (2.3) 得到一个完全明确的非零 Taylor 核元：

$$
\boxed{\quad
\overline T_p\ne0\text{ 在 }\mathcal R_{(p)}/p,
\qquad \operatorname{ev}_{\mathrm H}(\overline T_p)=0
      \text{ 在 }\mathcal H_{\mathbb F_p}.
\quad}
\tag{4.3}
$$

所以 §1 的特征零注入绝不能被拿来证明模 $p$ jet 注入。
全局整多项式 $pP_p^{\mathrm{flow}}$ 在实际 Hurwitz jet 中被 $p$
整除；其除以 $p$ 的向量属于像格的饱和，而对应解析函数不在原全局
整环中。对于某个给定总次数和有限截断，这个向量是否已经在原像里，
或者能否由前缀核中的别的截面替代，仍须计算该具体矩阵的 minors。
没有由 (4.3) 预先决定任意有限 Smith 不变量。

## 5. 不能免费换成普通系数 jet 范数

Hurwitz 整性 (3.3) 的含义是
$v_p([z^m]\mathscr H)\ge-v_p(m!)$，并不是普通幂级数整性。
若一组全局截面的 Hurwitz jet 矩阵为 $B^{\mathrm H}$，普通 Taylor
系数矩阵为 $B^{\mathrm{ord}}$，则逐行准确有

$$
B^{\mathrm{ord}}_{m,*}=B^{\mathrm H}_{m,*}/m!.
$$

因而对任何相同的行集合 $I$、列集合 $J$，

$$
v_p\det B^{\mathrm{ord}}_{I,J}
 =v_p\det B^{\mathrm H}_{I,J}
       -\sum_{m\in I}v_p(m!).
\tag{5.1}
$$

当独立前缀行的选择会变化时，须对每个候选 minor 保留这个准确
行权，不能只减一个未定义的公共阶乘。
下一步的低次数、高接触饱和格必须使用这种实际换算；(4.3) 提供
一个可放入该格的明确方向，尚未给 $D\asymp\sqrt{k}$ 的统一范数界。

依赖：R57 的真实整数流；R62／全余类 Stokes 笔记的整变换；
[有限滤子稿](2026-11-12-stokes-filters-in-integer-flow-field.md)
的 Newton 投影。§3 的简短阶乘证明由根端提出，本文保留全部规范。
