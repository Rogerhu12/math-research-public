# R1129：线性多个原 Gaussian good 标签必非恒定

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明，纯纸面。** 对每个 $p=4k+3\ge41$，保持 R1071、R1116
的原 Gaussian CM 模型、完整实际 cuspidal 模块、Weil 标记和
Bernoulli-good 归一。原完整 coarse 标签中，必为非恒定的不同
actual-good 角色坐标至少有
$$
\boxed{\qquad
\max\{3,\lfloor p/96\rfloor+2\}.
\qquad}
\tag{1129.1}
$$
更精确的显式下界见 (1129.20)，其渐近为
$p/96+(\log24/12)p/\log p-O(1)$。

本篇证明的是**完整坐标多项式非恒定**，不是每个坐标的中心一阶单位。
这里计数不同角色坐标，不声称这些多项式在函数空间中线性独立。
结论也不推出整个 Gaussian 标签注入、不排共同零或重值，
不处理原 deep disk 内有理点唯一性。全文无数学程序执行。

## 1. 不更换的原对象和安全核范围

固定
$$
E_a:y^2=x^3+ax,\qquad a\in\mathbf F_p^\times,\qquad
p=4k+3\ge41,\qquad \omega=dx/(2y).
\tag{1129.2}
$$
原 $\sigma'(0)=1$、$D=d/\omega$、$D\Psi=\delta$、
$\beta_{\rm Car}=-\delta$，以及 source 单位
$\beta_0,\lambda$ 和真实圆单位系数 $b_{\omega^R}$，
全部保持 R1116 的规范。特别不令 $\beta_0,\lambda$ 任意等于一。

用原 Kronecker 核
$$
\mathscr K(T,U)=\frac{\sigma(T+U)}{\sigma(T)\sigma(U)}.
$$
R1116 §8 已证明，完整实际 good 角色的 centered profile 是
同一有限 gauge $(e^{wTU}-1)\mathscr K$ 的指定系数。
本篇只消费其中各权至 $p-3$ 的有限部分；
不读取第一个可能含 $p$ 分母的权 $p-1$ 核项。

记
$$
m=(p-1)/2,\qquad
\mathcal G_p=
\{R:\ 2\le R\le p-3,\ R\ {\rm even},\
 V_{\omega^R}\ne0,\ p\nmid B_R\}.
\tag{1129.3}
$$
这是完整原实际 good mask。R1070、R1116 §8.3 已付
$V_{\omega^{m+1}}=0$；$m$ 本身为奇数。
所以每个 $R\in\mathcal G_p$ 恰在 $R<m$ 或 $R>m+1$ 两行。

原 fine 变量记为 $t_*$，coarse 变量为 $z=t_*^2$。置
$$
\Pi_R(z)=c_{\omega^R,s}(z)-c_{\omega^R,s}(0).
$$
所有结论均对原 Gaussian 两条 twist line 作同一尺度运输；
非恒定性不因非零 $\beta_0,\lambda,b_{\omega^R}$ 而改变。

## 2. 同一 sigma 的完整热方程

先在一般短模型
$$
y^2=x^3+ax+b
$$
上，取原模参数向量场
$$
\partial=6b\,\partial_a-\frac{4a^2}{3}\,\partial_b.
$$
它与点变量微分 $\partial_T,\partial_U$ 不同。
R1082 所固定的 sigma heat 方程是
$$
\partial\sigma(t)
=\frac12\sigma''(t)-\frac a6t^2\sigma(t),
$$
即
$$
\partial\log\sigma(t)
=\frac12\bigl(\zeta(t)^2-x(t)\bigr)-\frac a6t^2.
\tag{1129.4}
$$
在同一规范下准确有
$$
\boxed{\qquad
\partial\mathscr K
=\left(\partial_T\partial_U-\frac a3TU\right)\mathscr K.
\qquad}
\tag{1129.5}
$$

给出直接证明，避免由一个 SS 值式横向微分。
令
$$
q=\zeta(T+U)-\zeta(T)-\zeta(U).
$$
原加法式给 $x(T+U)=-x(T)-x(U)+q^2$。
于是 (1129.4) 应用于三个 sigma 因子后，除去 $-aTU/3$ 的部分是
$$
\zeta(T)\zeta(U)+q\bigl(\zeta(T)+\zeta(U)\bigr)+x(T)+x(U).
$$
另一方面
$$
\partial_T\log\mathscr K=\zeta(T+U)-\zeta(T),\qquad
\partial_U\log\mathscr K=\zeta(T+U)-\zeta(U),
$$
且 $\partial_T\partial_U\log\mathscr K=-x(T+U)$。
其乘积加交叉导数也正是同一个显示式。
三个二次项的差为 $-aTU/3$，证明 (1129.5)。

特别，(1129.5) 是一般模参数上的真正恒等式。
它没有将 R1075 的 SS-only 反射公式当作可任意横向微分的等式。

## 3. 有限对角递推与模参数消失阶

固定一个偶权 $w_0\ge4$，令
$$
f_n^{(w_0)}(a,b)
=[T^{w_0+n-1}U^n]\mathscr K(T,U),\qquad n\ge0.
$$
由 $\mathscr K(T,U)=U^{-1}+\zeta(T)+O(U)$，
$$
f_0^{(w_0)}=-G_{w_0}.
$$
取 (1129.5) 的指定系数，得到完整递推
$$
\boxed{\quad
(w_0+n)(n+1)f_{n+1}^{(w_0)}
=\partial f_n^{(w_0)}+\frac a3f_{n-1}^{(w_0)},
\qquad f_{-1}^{(w_0)}=0.
\quad}
\tag{1129.6}
$$
这里保留了 $a f_{n-1}/3$，没有把真正 heat 递推换成普通高阶导数。

只要本次涉及的 $n!$、$(w_0)_n$ 都是 $p$-单位，
(1129.6) 逐项给出双向三角关系
$$
f_n^{(w_0)}
=\frac{\partial^n(-G_{w_0})}{n!(w_0)_n}
 +\sum_{j<n}u_{n,j}(a,b)\,\partial^j(-G_{w_0}),
\tag{1129.7}
$$
其中 $u_{n,j}$ 的分母均为本范围内的 $p$-单位。
因此在任一固定点，前 $n+1$ 个 $f_j$ 同时为零，
当且仅当前 $n+1$ 个 $\partial^jG_{w_0}$ 同时为零。

现在付款 $G_{w_0}$ 的整性与非零性，而不要求其 Bernoulli 常数为单位。
若
$$
4\le w_0\le p-3,\qquad w_0\ {\rm even},
$$
原规范
$$
G_{w_0}=\frac{2\mathcal E_{w_0}}{(w_0-1)!},
\qquad
\mathcal E_{w_0}
=-\frac{B_{w_0}}{2w_0}
 +\sum_{n\ge1}\sigma_{w_0-1}(n)q_{\rm Tate}^n
\tag{1129.8}
$$
说明其全部 Fourier 系数 $p$ 整，且 $q_{\rm Tate}^1$ 系数
$2/(w_0-1)!$ 是单位。
常数项 $p$ 整，因为 $w_0<p-1$；没有声称 $B_{w_0}$ 本身为单位。

对 $p>3$，level-one 整权环与 $q$ 展开原理给
$$
G_{w_0}\in\mathbf Z_{(p)}[a,b]_{w_0},\qquad
\overline G_{w_0}\ne0\ \text{于 }\mathbf F_p[a,b].
\tag{1129.9}
$$
这里 $\operatorname{wt}(a)=4,\operatorname{wt}(b)=6$，
且原 $a=-E_4/48,b=E_6/864$ 的缩放是 $p$-单位。
一个具体的整性说明是：同权模形式可用
$E_4^{a_j}E_6^{b_j}\Delta^j$ 的整三角 $q$ 展开基逐项消去；
其首非零系数为一，$\Delta=(E_4^3-E_6^2)/1728$ 的分母也是单位。
所以 (1129.9) 不从有理权环偷偷丢掉一个 $p$ 分母。

对每个固定 $a_0\in\mathbf F_p^\times$，
(1129.9) 仍给非零的单变量多项式
$\overline G_{w_0}(a_0,b)$：
每个给定 $b^j$ 次数只有一个可能的 $a$ 单项式
$a^{(w_0-6j)/4}$，不存在同一 $b$ 次数下的相消。
因此
$$
\nu(w_0):=\operatorname{ord}_{b=0}\overline G_{w_0}(a_0,b)
\le\lfloor w_0/6\rfloor.
\tag{1129.10}
$$
这个阶数与所选非零 $a_0$ 无关。

向量场真正横截 Gaussian 直线：
$\partial b|_{b=0}=-4a_0^2/3\ne0$。
若最低 $b$ 次数为 $\nu<p$，则
$$
\partial^jG_{w_0}(a_0,0)=0\quad(j<\nu),\qquad
\partial^\nu G_{w_0}(a_0,0)
=\left(-\frac{4a_0^2}{3}\right)^\nu
 \nu!\,[b^\nu]G_{w_0}(a_0,b)\ne0.
\tag{1129.11}
$$
同权单项式的唯一性也保证低次系数消失是沿整个 $b=0$ 的消失，
足以支付这里所有可能的 $\partial_a$ 项。
这说明热方向的消失阶确为 (1129.10) 的 $b$ 阶数，
而非只在一个未指定的参数方向取导数。

## 4. 完整原 profile 为常数的充要条件

对 $R\in\mathcal G_p$，定义
$$
(w_R,s_R)=
\begin{cases}
(p+1-2R,\ R),& R<m,\\
(2R-p+1,\ p-R),& R>m+1.
\end{cases}
\tag{1129.12}
$$
两行均有 $4\le w_R\le p-3$。
第一行 $w_R\equiv0\pmod4,s_R$ 偶；
第二行 $w_R\equiv2\pmod4,s_R$ 奇。
记 $\nu_R=\nu(w_R)$。

R1116 (1116.34) 的原完整系数给
$$
[t_*^i]\Pi_R(t_*^2)
=
\frac{\beta_0^{(p+1)R-i(p-1)}\lambda^i}
 {2b_{\omega^R}R!\,i!\,\delta^{p-R-i}}\,
 f_{s_R-i}^{(w_R)}(a,0),
\tag{1129.13}
$$
其中 $i$ 遍历
$2\le i\le\min(R,p-R-1)$ 的偶数。
在第一行使用了 $\mathscr K(T,U)=\mathscr K(U,T)$；
第二行直接读取同一个核。
显示外因子全部是原单位，未重标 period 或 Weil root。

低角色读取 $n=0,2,\ldots,R-2$；
高角色读取 $n=1,3,\ldots,p-R-2$。
权给出的 Gaussian 奇偶性补足其间所有另一个 parity 的零：
$f_n^{(w_R)}$ 权为 $w_R+2n$，
在 $b=0$ 只有该权被 $4$ 整除时才可能非零。

所以 $\Pi_R=0$ 当且仅当全部
$f_n^{(w_R)}(a,0)$、$0\le n\le s_R-2$ 为零。
本次全部核项的最高权为
$$
w_R+2(s_R-2)=p-3.
$$
同时 $n!$ 与 $(w_R)_n$ 的最大因子都严格小于 $p$。
故 (1129.7)–(1129.11) 完全合法，并先给
$\Pi_R=0\Longleftrightarrow\nu_R\ge s_R-1$。

最后一个阶数由原权奇偶性准确支付：
$G_{w_R}(a,b)$ 在低角色行只含偶 $b$ 次，
在高角色行只含奇 $b$ 次。因此 $\nu_R$ 与 $s_R$ 同 parity，
不可能恰为 $s_R-1$。最终得到
$$
\boxed{\qquad
\Pi_R\equiv0
\quad\Longleftrightarrow\quad
\nu_R\ge s_R.
\qquad}
\tag{1129.14}
$$
这里的 $\Pi_R=0$ 是完整 centered polynomial 为零，
也就是原坐标为常数，不是只说它的某个取值为零。

特别，最后一步**没有**调用权 $p-1$ 的
$f_{s_R-1}^{(w_R)}$ 或把它约化。
只用原 $G_{w_R}$ 多项式的 parity，
避免第一个未付高核项进入证明。

若 $\nu_R<s_R$，(1129.7)、(1129.11)、(1129.13)
还给出准确的最高非零次：
$$
\deg_z\Pi_R=(s_R-\nu_R)/2.
\tag{1129.15}
$$
这只是同一完整 profile 的 degree 读数，
不将正 degree 自动提升为 degree 一或注入。

## 5. 与 Bernoulli 值无关的必非恒定区间

由 (1129.10)、(1129.14)，只要 $s_R>w_R/6$，
该实际 good 坐标就必非恒定。因此
$$
\boxed{
\begin{aligned}
R<m,\quad 8R>p+1
&\ \Longrightarrow\ \Pi_R\ne0,\\
R>m+1,\quad 8R<7p-1
&\ \Longrightarrow\ \Pi_R\ne0.
\end{aligned}}
\tag{1129.16}
$$
这些严格不等式不要求 $B_{w_R}$ 为单位。
它们只用于已经在 $\mathcal G_p$ 中的实际角色；
不制造一个原 cuspidal 模块中不存在的标签。

以下要证明，原 actual-good mask 不可能全部避开
(1129.16)。这需要实际低角色出现判据与 irregular 总预算，
不能只数一个没有 mask 的区间。

## 6. 三层互不相交的实际角色链

置
$$
N=k-1=(p-7)/4,\qquad
\mathcal A=\{j\in\mathbf Z:N/4<j\le N\},
$$
$$
\mathcal B=\{j\in\mathbf Z:N/2<j\le N,\ j\ {\rm odd}\},
\qquad
\mathcal C=\{j\in\mathbf Z:N/2<j\le N,\ j\equiv3\pmod4\}.
$$
记其大小为 $u,v,w$；这里 $w$ 仅为有限集合大小，与前文权 $w_R$ 不同。
有 $\mathcal C\subset\mathcal B\subset\mathcal A$。

对每个 $j\in\mathcal A$，从原 forced 角色开始：
$$
n_j=p-1-2j.
$$
若 $j\in\mathcal B$，再接
$$
\ell_j=j+1.
$$
若 $j\in\mathcal C$，再接
$$
\mu_j=(p-j)/2.
\tag{1129.17}
$$
这些链的长度分别为一、二、三。
逐项验证实际范围：

- 所有 $n_j>m+1$，且 $j>N/4$ 正是高行
  $8n_j<7p-1$。
- 所有 $\ell_j$ 为偶数，$2\le\ell_j\le N+1<m$；
  $j>N/2$ 正是 $8\ell_j>p+1$。
- $j\equiv3\pmod4$ 使 $\mu_j$ 为偶数；
  $N+1<\mu_j<m$，且 $8\mu_j>p+1$。

所以每条链的每个位置，只要实际出现且 good，
便由 (1129.16) 给一个非恒定坐标。
三层分别落在 $>m$、$\le N+1$、$(N+1,m)$，
各层内部又分别是 $j$ 的单射函数，
故所有链的全部 Bernoulli 指标互不重复。

R1128 (1128.8) 的完整原低角色判据是
$$
V_{\omega^r}\ne0
\quad\Longleftrightarrow\quad
p\mid\operatorname{num}(B_{T(r)}),
\qquad
T(r)=p+1-2r,\quad 2\le r<m,\ r\ {\rm even}.
\tag{1129.18}
$$
本次准确有
$$
T(\ell_j)=n_j,\qquad T(\mu_j)=\ell_j.
$$
因此一条链若没有提供 actual-good 坐标，
其所有 Bernoulli 指标必全 bad：
forced 根若 good 已成功；根 bad 使首低角色实际出现；
首低若 good 又成功；它 bad 再使第二低角色出现。
这是真正的原模块出现逻辑，不是给每个偶指数任配一个标签。

## 7. 精确计数、线性下界及来源界限

令 $I=i(p)$ 是 $2\le n\le p-3$ 的实际 irregular 偶指标总数，
并保持 R1069、R1128 的明确数
$$
\mathcal H_p=
2p\left(\frac{(p-1)(p-2)}{24p}\right)^{(p-1)/4},
\qquad M_p=\lfloor\log_p\mathcal H_p\rfloor.
$$
已付的无条件界是
$$
I\le M_p,\qquad N-M_p\ge5.
\tag{1129.19}
$$
第二式正是 R1128 (1128.16) 在 $p=4k+3$ 的原 $h=N$，
不需要 regular、Vandiver 或 class-group 循环性。

令 $d_{\rm nc}$ 为整个 $\mathcal G_p$ 中非恒定角色坐标的数量。
由只有根、前两层、全部三层三种计数，准确得到
$$
\boxed{\quad
d_{\rm nc}\ge
\max\left\{
u-M_p,\ 
\left\lceil\frac{u+v-M_p}{2}\right\rceil,\
\left\lceil\frac{u+v+w-M_p}{3}\right\rceil
\right\}.
\quad}
\tag{1129.20}
$$
更原始的版本可把 $M_p$ 换成 $I$。

证明计数时不重复花费 bad 指标。
一层有 $u$ 个原 forced 根，失败根各耗一个 bad。
前两层的失败 pair 耗两个 bad，失败单根耗一个；
相应得到第二项，与 R1128 的 pair 论证相同。
三层共有 $u+v+w$ 个互异顶点。
若 $g$ 条链提供了至少一个 actual-good 非恒定角色，
其余链全 bad，而这 $g$ 条链最多含 $3g$ 个顶点。
所以
$$
I\ge u+v+w-3g,\qquad d_{\rm nc}\ge g,
$$
给第三项。没有要求成功链只含一个 good 角色；
多出的实际好坐标只会提高 $d_{\rm nc}$。

为使显式界完全可检查，有
$$
u=N-\lfloor N/4\rfloor,\qquad
u+v=N+(N\bmod2),
$$
$$
w=\left\lfloor\frac{N+1}{4}\right\rfloor
 -\left\lfloor\frac{\lfloor N/2\rfloor+1}{4}\right\rfloor
 \ge\lfloor N/8\rfloor.
\tag{1129.21}
$$
第二项配合 (1129.19) 给 $d_{\rm nc}\ge3$；
第三项给
$$
d_{\rm nc}\ge
\left\lceil\frac{\lfloor N/8\rfloor+5}{3}\right\rceil
\ge\lfloor N/24\rfloor+2.
$$
最后 $\lfloor N/24\rfloor=\lfloor p/96\rfloor$：
两边唯一可能不同的情形是 $p\equiv3\pmod{96}$，
但这使 $p>3$ 被三整除，不可能为素数。
于是得到 (1129.1)。

此外
$$
u+v+w=\frac{9p}{32}+O(1),\qquad
M_p=\frac p4-\frac{\log24}{4}\frac p{\log p}+O(1).
$$
在 (1129.20) 的第三项代入，得到已显示下界的渐近
$$
\boxed{\quad
d_{\rm nc}\ge
\frac p{96}+\frac{\log24}{12}\frac p{\log p}-O(1).
\quad}
\tag{1129.22}
$$
这不声称实际数量等于该渐近式。

## 8. 已付后果和仍需支付的共同 fiber

本篇对原整个 actual-good mask 证明线性多个完整 Gaussian
坐标非恒定。这些坐标来自同一 R1116 gauge，
其 $\beta_0,\lambda,\delta,b_{\omega^R}$ 全部按原 source 保持；
没有以任意多项式替代实际标签，也没有抹掉 bad 角色。

即使各坐标非恒定，也可能在某两个 coarse 参数取同值。
(1129.15) 允许某个非恒定坐标的中心一阶为零；
所以本篇不替代 R1116 的指定首项共同零问题，
也不从多个非恒定函数推出标签注入。
后继须继续支付同一有限 gauge 差在实际 good mask 上的共同消失，
并保留原 norm-two 分布与 Fay 式中的全部低项乘积。

原 bare $r=2,8$、$f_N/e$、短 $\eta_k,\nu_k$、
一般素数的辅助同点排除和 deep disk 内控制均没有因此自动关闭。

## 来源与纸核范围

- [R1116](R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)
  §§7–8：原完整角色的 Appell primitive、全系数尺度与有限 gauge。
- [R1128](R1128-all-prime-linear-good-cuspidal-rank.md)
  §§2、5：真正低角色出现 iff，$I\le M_p$ 和 $N-M_p\ge5$。
- R1082 采用的原 sigma heat 规范；其已刊主要来源为
  Eilbeck–Gibbons–Ônishi–Yasuda，
  Glasgow Mathematical Journal 67 (2025), §6.3：
  [DOI 10.1017/S0017089524000417](https://doi.org/10.1017/S0017089524000417)。
  本篇 §2 已独立从该规范推导完整 Kronecker 热式。
- 原 $G_w=2\mathcal E_w/(w-1)!$ 及 full-level 权环规范保持
  R1075、R1116，不对 SS-only 恒等式作无来源的横向微分。

o1_theta 已独立纸核 (1129.5)–(1129.16) 的热式、递推、
双向消失阶、奇偶性与安全权界。
root 与 o2_high_coefficient 已分别独立核三层链的出现、范围、
互不相交及其线性计数；global_route 独立核计数，root 已完成
全文逐式转录审并亲读已刊主来源 (0.13)、(6.8)。
所有证明均为纸面推导，无数学程序执行。
