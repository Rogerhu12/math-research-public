# R74：当前真实全尾的 Robin 算子与带均值行的正帽强解

2026-11-12，independent-audit。

**状态：完整证明，实际入口常数有向计算。** 从 R69 当前闭近似背景
出发，在其极远径向段加入两个明确的小变形。它们保持第四模的真实
稳定方向，并使全部非零四重频率的完整 R72 尾线同时避开增长方向。
在物理切口 $r=25/8$，所得真实外部 ground-state Robin 算子为正，
且与 $|D_\theta|/(4\omega_*)$ 的归一差小于 $2^{-36}$。
再与 R69 已认证的整个有限正域联立，得到实际、无角权的
Poisson / 普通源 / contact 强界，并保留一个未删除的均值通量行。

这里真正使用无限尾及全部内部标签，未把远端截成一个方便的
Robin 行。改变的径向区不接触当前核心、body 或 graft。本文仍不
证明非径向邻域的全反馈逆、角权预算、非线性收敛或可见幅度。

## 1. 当前入口与新的准确外区

对 R66/R69 的每个固定准确参数
$$
\delta\in\left[
-\frac{7789866024620307}{4611686018427387904}-\frac1{2000000},
-\frac{7789866024620307}{4611686018427387904}+\frac1{2000000}
\right]
\tag{74.1}
$$
使用其真实入口 $a_*,z_*,\omega_*$。R66 的有向数据给
$$
0<a_*<7\,10^{-6},\qquad z_*>9/10,\qquad
\frac75<\omega_*<\frac32.
\tag{74.2}
$$
以下简写 $\omega=\omega_*$，工作坐标为
$u=4c_0(r-25/8)$，$c_0$ 是 R66 的实际末端 $z_r/a^2$。
R69 的未改径向段准确是
$$
a(u)=a_*e^{-\omega u},\quad
z(u)=z_*+\frac{a_*^2}{8\omega}(1-e^{-2\omega u}),\quad
h=1/a,\quad z_u=a^2/4.
\tag{74.3}
$$
取
$$
T=2^{24},\quad \ell=\frac1{16},\quad L=3+2\ell=\frac{25}{8},
\quad B=T-L,\quad \gamma_0=2^{-17},\quad \epsilon_*=2^{-39}.
\tag{74.4}
$$
令 $\phi_1,\phi_2$ 为 R7 (1.2) 的两个宽 $\ell$ 的明确 $C^2$ bump，
支撑分别为 $[B,B+\ell]$、$[T-\ell,T]$。准确定义
$$
h_{s,t}=h\exp\{s\phi_1+\gamma_0t\phi_2\},\qquad
|s|\le\gamma_0,\quad 0\le t\le1,
\tag{74.5}
$$
并以 $z_u=h_{s,t}^{-2}/4$ 定义真实高度。两端的 $h$ 二 jet 不变。
之后继续 R69 的同一个 connector 和按实际 $\epsilon_{\rm tail}$ 调用
的完整 R72 尾，仅将它们的高度平移至新的接缝值；负侧取真实腰反射。

### 1.1 已支付的全频选择

右端真实线来自 R15 的全部内部标签，经同一个 connector 回传。
该线与 $(s,t)$ 无关，因为 (74.5) 保持右端半径、$\omega$、势和
两 jet；外区高度平移不改变高度方程。R69 的第四模真实右端条件为
$$
-y_4'(T)/(4y_4(T))=\omega\in[1,3/2].
\tag{74.6}
$$
未改段的 $-V=h''/h=\omega^2$ 属于 $[1,3]$，$h'/h<2$。
R11 附录 A 的全部输入因此在本对象上成立：其证明只使用这些盒、
(74.6)、真实尾线和固定增长目标，不使用 Pöschl–Teller 的其它公式。
这里增长目标准确取 $\operatorname{span}(1,\omega)$。

故有唯一 $C^1$ 曲线 $s=s(\gamma_0t)$，
$-\gamma_0/64<s\le0$，使第四模回到 $B$ 的方向准确保持
$(1,-\omega)$。在测度至少 $1-83/16384$ 的闭参数集合中，全部
$m=|n|\in4\mathbb N$ 同时满足
$$
\left|\sin\angle\bigl(\Lambda_m(B),(1,\omega)\bigr)\right|
\ge\epsilon_*.
\tag{74.7}
$$
这包含负频率的共轭。两帽是同一径向对象的反射，可用同一个参数。
为固定对象，可取这个非空闭集合的最小元。这个定义是准确的存在
选择，不是有限频率数值搜索。

对本次迁移，R11 的关键数值仍逐字成立：第四模变分密度满足
$(45/4)y_4^2\le D_4\le181y_4^2$，两 bump 横截列之比小于 $1/64$，
全部坏方向的参数测度至多 $83/16384$。基态斜率 $\omega$ 同时处于
该证明要求的 $[4/3,3/2]$ 增长盒。保持的是本径向外区的第四模
稳定线；没有由此断言当前非径向核心自身有第四模核。

对于不同 $\delta$，本节只逐点选参数。没有声称这个最小元随
$\delta$ 连续，也没有把逐点选择当作已付邻域强逆。

### 1.2 真实几何改动的费用

由于两个支撑不相交，
$$
|\psi|\le\gamma_0,\quad
|\psi'|\le15/16384,\quad |\psi''|\le3/16,
\qquad \psi=s\phi_1+\gamma_0t\phi_2.
\tag{74.8}
$$
令 $\widetilde\omega=\omega+\psi'$，
$q_c=\widetilde\omega_u/\widetilde\omega^2$。于是
$$
\widetilde\omega>\frac75-\frac{15}{16384}>0,\qquad
|q_c|\le\frac{3}{16\widetilde\omega^2}.
$$
用 R22 的真实 $k=4$ 曲率公式，
$$
|\kappa_\theta|\le\frac1{4\widetilde\omega},\qquad
|\kappa_s|\le\frac{1+|q_c|}{4\widetilde\omega}<\frac15.
\tag{74.9}
$$
所以新增段仍为正曲率；其支撑不产生新的混合型组件。

记 $a_B=a_*e^{-\omega B}$。由
$|e^{-\psi}-1|\le2\gamma_0$ 和
$|e^{-2\psi}-1|\le3\gamma_0$，
$$
|\Delta a|\le2\gamma_0a_B,\qquad
|\Delta z_{\rm out}|
\le\frac{3L\gamma_0}{4}a_B^2<2^{-14}a_B^2.
\tag{74.10}
$$
当前 $T$ 给两者都小于 $2^{-100}$。两端平移后的 connector 和真尾
形状、尾缩放、曲率以及全部线性方向不变。支撑仍正，星形覆盖论证
仍成立。R69 的直径和两平盘尺寸可宽松改写为
$$
D<2.557687167,\qquad \operatorname{diam}H>1.932397339,
\qquad \operatorname{diam}H/D>3/4.
\tag{74.11}
$$
这仍是闭近似背景的尺寸。当前对象的可见位移和 reach 没有由此得到。

## 2. 同一物理 ground-state frame 的准确两迹

以下先在未改段 $0\le u\le B$。表面为
$F=(a\cos\theta,a\sin\theta,z)$，令
$$
R_F=(a^2+z^2)^{1/2},\quad Y_z=z/R_F,\quad
A(u)=4\omega+\frac{a^2}{z},\quad c(u)=\frac4{A(u)^2}.
\tag{74.12}
$$
这里 $A$ 是一个标量，不是 R37 的矩阵 $\mathsf A$。真实材料密度
算子 $P$ 经 $w=Y_zv$ 的 ground-state 变换，准确满足
$$
Y_zP(Y_zv)=
\partial_u(c\,v_u)+c\omega^2v_{\theta\theta}.
\tag{74.13}
$$
因此本节真实动量为 $p=cv_u$。

**证明。** 取 $E=a^2\omega^2+a^4/16$。实际第二基本形式给
$N=-a^3/(4\sqrt E)$、$L=\omega^2N$、$M=0$。
同时
$$
\zeta=\frac{a(\omega z+a^2/4)}{\sqrt E\,R_F},\qquad
\mathsf A^{uu}=-\frac N{\zeta^2a\sqrt E}.
$$
故 $Y_z^2\mathsf A^{uu}=4/A^2$，
$\mathsf A^{\theta\theta}=\omega^2\mathsf A^{uu}$。
R37 的真实平移 ground state 给 (74.13)，包括零阶项的准确抵消。
换 $u=4c_0(r-25/8)$ 时密度和导数因子互消，$p$ 就是 R69 正域末端
使用的同一个 conormal，而非新定义的方便 Robin 单位。

设 $y''=m^2\omega^2y$，$m\ge4$。R22 的实际物理位移为
$$
U=ay,\quad T_{\rm ang}=-U/m,\quad
C=4\left(\omega y-\frac{y'}{m^2}\right).
\tag{74.14}
$$
于是 $v=w/Y_z=C+(a/z)U$，准确得到
$$
\boxed{\quad
v=Ay-\frac4{m^2}y',\qquad
p=-y+\frac4A y'.\quad}
\tag{74.15}
$$
第二式可用
$A'=4\omega^2-A^2/4$ 直接微分。对状态 $(y,y'/m)$，这个两迹矩阵的
行列式为 $4m(1-m^{-2})$，全非零四重频率均可逆。

它还保留完整度量源的端点项。若第 $m$ 模源的
$\theta\theta,u\theta,uu$ 分量为 $P_m,Q_m,R_m$，令
$$
J=(h^2P_m/2)'-mh^2Q_m,\qquad
f=\frac{m^2h^2}{2}R_m-J',\qquad
-\eta''+m^2\omega^2\eta=f.
$$
R22 的真实重建给
$$
\boxed{\begin{aligned}
v&=A\eta-\frac4{m^2}\eta'+\frac4{m^2}J,\\
p&=-\eta+\frac4A\eta'+\frac{8h^2}{A^2}R_m.
\end{aligned}}
\tag{74.16}
$$
因为 $f+J'=m^2h^2R_m/2$。所以普通源切换时必须同时匹配这些实际
源迹；不能保留 $(\eta,\eta')$ 却删掉 $J,R_m$。

## 3. 真无限尾给出的正 Robin 算子

写未改段齐次解为
$$
y(u)=c_-e^{-m\omega u}+c_+e^{m\omega u}.
$$
取单位行 $\ell_m$，$\ker\ell_m=\Lambda_m(B)$。由 (74.7) 及
$|(1,\omega)|=|(1,-\omega)|$，
$$
\left|\frac{c_+}{c_-}\right|
\le\epsilon_*^{-1}e^{-2m\omega B}=:r_m^*<\frac18.
\tag{74.17}
$$
特别 $y(0)\ne0$。令 $\lambda_m=y'(0)/y(0)$，则
$$
|\lambda_m+m\omega|
\le4m\omega\epsilon_*^{-1}e^{-2m\omega B};
\qquad \lambda_4=-4\omega.
\tag{74.18}
$$
第四模的等式来自准确匹配，不是指数小量近似。

在物理切口处令 $A_0=A(0)$。真正向外区的 DN 系数为
$$
\gamma_m=-\frac{p(0)}{v(0)}
=\frac{1-4\lambda_m/A_0}{A_0-4\lambda_m/m^2}>0.
\tag{74.19}
$$
稳定线的准确值是
$$
\gamma_m^0=
\frac{1+4m\omega/A_0}{A_0+4\omega/m}.
\tag{74.20}
$$
由于 $\lambda_m<0$ 且
$$
\frac{\partial}{\partial\lambda}
\frac{1-4\lambda/A_0}{A_0-4\lambda/m^2}
=-\frac{4(1-m^{-2})}{(A_0-4\lambda/m^2)^2},
$$
有安全的全频界
$$
\frac{|\gamma_m-\gamma_m^0|}{m}
\le2^{42}e^{-2m\omega B}<2^{-100}.
\tag{74.21}
$$
每个固定阶角平滑 norm 同样有限，直接取
$\sup_{m\in4\mathbb N}m^j2^{42}e^{-2m\omega B}$；没有用
“指数很小”把真实余项置零。

当前入口给 $p_0=a_*^2/z_*<2^{-34}$，$A_0=4\omega+p_0<6.01$。
在 $A\ge4\omega$、$m\ge4$ 上，对 (74.20) 关于 $A$ 求导的绝对值
小于 $m/10$。例如分子求导后两项之和小于 $(5/2)m$，而分母平方
大于 $(28/5)^2$。因此
$$
\frac{|\gamma_m^0-m/(4\omega)|}{m}\le\frac{p_0}{10}<2^{-37}.
$$
结合 (74.21)，
$$
\boxed{\quad
\frac m7<\gamma_m<\frac m5,\qquad
\left\||D_\theta|^{-1/2}
\left(\Gamma_{\rm ext}-\frac{|D_\theta|}{4\omega}\right)
|D_\theta|^{-1/2}\right\|<2^{-36}.
\quad}
\tag{74.22}
$$
本式在全部非零 $4\mathbb Z$ 模上；物理角是 $\theta$，未遗漏归一角
$4\theta$ 的因子。$\Gamma_{\rm ext}$ 自伴、实，负模按共轭恢复。

还可保留完整首项而不作粗化。若 $b=4\omega/A_0$，则
$$
\gamma_m^0=\frac b{A_0}m+
 \frac{1-b^2}{A_0}\frac m{m+b}.
\tag{74.23}
$$
当前实际有向计算给所有这些频率同时成立的更窄安全区间
$$
0.1710977721347<\frac{\gamma_m}{m}
                         <0.1710977726510.
\tag{74.24}
$$
这是真尾的方向结果加实际入口区间，不是有限频率抽样的最大值。

## 4. 未改长段的普通源，不将源变成边界跳量

直接对同一标量密度源写
$$
(cv')'-m^2c\omega^2v=s,\qquad p=cv'.
\tag{74.25}
$$
令 $\sigma_m=1-m^{-2}$，准确作状态变换
$$
y=\frac{v/A+p/m^2}{\sigma_m},\qquad
z_1=\frac{v+Ap}{4m\sigma_m}.
$$
即使 $s$ 只有 $L^2$ 正则，也有准确的一阶系统
$$
\binom y{z_1}'=
\begin{pmatrix}0&m\\m\omega^2&0\end{pmatrix}\binom y{z_1}
+\binom{s/(m^2\sigma_m)}{As/(4m\sigma_m)}.
\tag{74.26}
$$
没有对普通源求导来制造额外正则要求。齐次时 $z_1=y'/m$。

允许右端完整仿射条件
$$
\ell_m(y(B),z_1(B))=d_m,\qquad v(0)=a_m.
\tag{74.27}
$$
$d_m$ 是真实右部普通源产生的负荷；当 $B$ 以后齐次时它为0。
先把这个负荷保留，不能把不同 source realization 都写成同一齐次线。

取
$$
\alpha_m=\frac m2+2\omega,\qquad
\mathfrak w_m(u)=h(u)^2e^{mu/2}=h(0)^2e^{\alpha_m u}.
$$
对 $p_*=2,\infty$ 定义
$$
F_{m,p_*}=\left\|\mathfrak w_m\,\frac{s}{m^2}\right\|_{L^{p_*}(0,B)}.
$$
存在唯一解，且
$$
\boxed{\begin{aligned}
&\left\|\mathfrak w_m
  \left(|v|+\frac{|v'|}m+\frac{|v''|}{m^2}\right)\right\|_{L^{p_*}}
\\
&\hspace{1cm}\le
2^{55}\left[
h(0)^2m^{-1/p_*}|a_m|+
F_{m,p_*}+
h(B)^2e^{mB/2}m^{-1/p_*}|d_m|
\right].
\end{aligned}}
\tag{74.28}
$$
通常约定 $1/\infty=0$。此外入口和末端的实际两迹有
$$
\begin{split}
&h(0)^2\left(|v(0)|+\frac{|p(0)|}{m}\right)
+\mathfrak w_m(B)\left(|y(B)|+|z_1(B)|\right)
\\
&\qquad\le
2^{55}\left[
h(0)^2|a_m|+
m^{1/p_*}F_{m,p_*}+
h(B)^2e^{mB/2}|d_m|
\right].
\end{split}
\tag{74.29}
$$

**证明及常数。** 将 (74.26) 的状态写为
$c_-(1,-\omega)+c_+(1,\omega)$。相应源为
$$
f_\pm=\frac12\left(\frac{s}{m^2\sigma_m}
             \pm\frac{As}{4m\omega\sigma_m}\right),\qquad
|f_\pm|\le |s|/m,
$$
最后一步使用 $\sigma_m\ge15/16$、$A<6.01$、$\omega>7/5$。
设 $\kappa=m\omega$、$\alpha=m/2+2\omega$，则
$$
\kappa-\alpha\ge m/5,\qquad \kappa+\alpha>m.
$$
准确积分式为
$$
c_-(u)=e^{-\kappa u}c_-(0)+
 \int_0^u e^{-\kappa(u-t)}f_-(t)\,dt,
$$
$$
c_+(u)=e^{-\kappa(B-u)}c_+(B)-
 \int_u^B e^{-\kappa(t-u)}f_+(t)\,dt.
\tag{74.30}
$$
右边界解 $c_+(B)$ 的分母为
$\ell_m(1,\omega)$，绝对值至少 $\epsilon_*$。
再代入左边界，剩余分母是
$$
A_0+4\omega/m-
(A_0-4\omega/m)
\frac{\ell_m(1,-\omega)}{\ell_m(1,\omega)}e^{-2\kappa B}.
$$
其绝对值至少 $(A_0+4\omega/m)/2$，由 (74.17) 支付。
这也证明唯一性。

加权后的两个卷积核 $L^1$ 范数分别至多 $5/m$ 和 $1/m$；
它们的 $L^{p_*}$ 范数至多 $2m^{-1/p_*}$。
Hölder 给端点源积分至多
$5m^{1/p_*}\|e^{\alpha u}s/m^2\|_{p_*}$。
将两条边界代回 (74.30)，使用
$\epsilon_*^{-1}e^{-(\kappa+\alpha)B}<1$，于是加权状态的
$L^{p_*}$ norm 和端点 norm 分别至多相应右端的
$2^8\epsilon_*^{-1}$。这个常数同时覆盖两个分支和两端源。

最后 $v=Ay-4z_1/m$、$p=-y+4mz_1/A$。当前
$|A'|<1$、$A<6.01$，方程又给
$$
v'=\frac{A^2}4p,\qquad
v''=\frac{AA'}2p+m^2\omega^2v+\frac{A^2}4s.
$$
所以三项输出至多为40倍状态加10倍 $|s|/m^2$。
$40\cdot2^8\epsilon_*^{-1}+10<2^{55}$，证明 (74.28)–(74.29)。

逐模先取上述径向 norm，再以任意固定 $e^{\rho_0m}$ 求和，
$\rho_0\ge0$，即可得到同一个逐渐增宽角空间的强界。
如果 $s$ 位于 $L^2$ 径向空间，端口明确多出 $m^{1/2}$；
不能删除这半阶迹费用。

## 5. 真 connector、全内部标签及源位置

先设 $B$ 以后齐次，即 (74.27) 的 $d_m=0$。由 (74.29)，
$$
\|(y(B),z_1(B))\|_\infty
\le2^{55}h(B)^{-2}e^{-mB/2}
\left[h(0)^2|a_m|+m^{1/p_*}F_{m,p_*}\right].
\tag{74.31}
$$
双 bump 的状态传播 norm 至多 $e^{4mL}$。整个真实 connector 用
$t=\log h$、$Z_m=(y,y_t/m)$，方程为
$$
\frac{dZ_m}{dt}=
\begin{pmatrix}0&m\\m(q_c+1)&-q_c\end{pmatrix}Z_m.
$$
$-8\le q_c\le2$，实际 $t$ 长度小于127，故传播费用至多
$e^{1143m}$。这包括所有非第四模，不是假设它们沿同一稳定方向。

R69 真实尾的参数仍为
$$
\rho=(Hb_{\rm tail})^{-1},\quad
\epsilon_{\rm tail}=(4H\omega_e\overline W_b)^{-1}<1,
\quad \delta_{\rm tail}=\frac2{25}2^{-128},\quad \Omega=2^{360}.
$$
与 R22 (6.2)–(6.3) 同一物理转换给
$$
\zeta_{128}^{-1}\|V^{\rm ref}_{m,128}\|_\infty
\le16\,\delta_{\rm tail}^{-15/4}
\frac{H^2\omega_e^2}{b_{\rm tail}^{10}}m^4\|Z_m\|_\infty .
\tag{74.32}
$$
这里的16是 $k^2$，高度和源中均未将它漏去。
又有 $H^2\omega_e^2<8\Omega^3h(T)^2$、
$h(T)^2/h(B)^2\le e^{3L}$。所以真实 $h(B)^{-2}$ 与径向尺度准确
相消。再乘 R15 全部标签权
$e^{371m+2\cdot10^6(1+\log(1+m))^2}$，得到
$$
|a_m^{\rm tail}|
\le \exp\left\{
\left(-\frac T2+2000\right)m+
2\cdot10^6[1+\log(1+m)]^2
\right\}
\left[h(0)^2|a_m|+m^{1/p_*}F_{m,p_*}\right].
\tag{74.33}
$$
可逐项核算2000：除对数平方项外，频率线性费小于
$1514+(9/2)L$；常数因子至多
$2^{1638}m^4e^{3L}$，在 $m\ge4$ 上再花小于 $292m$。
总数小于1840，故2000有严格余量。
利用 R15 已付的
$2\cdot10^6[1+\log(1+m)]^2\le4500000m$ 和
$(3/8)2^{24}>4502000$，最终
$$
\boxed{\quad
|a_m^{\rm tail}|
\le e^{-Tm/8}
\left[h(0)^2|a_m|+m^{1/p_*}F_{m,p_*}\right].
\quad}
\tag{74.34}
$$
这支付的是全部真实内部标签的 norm；没有只估计一个切口夹角。
齐次强尾 norm 再至多乘4。若总标签 $\ell^1$ norm 不超过 $1/12$，
R72 的完整非线性尾在其真参数球内有定义；其非线性两迹和 mean
仍是输出，不能因此沿用线性 DN 条件。

若 source 位于 bump、connector 或真尾，须用它的完整 particular
solution 回传。准确作法是先在真尾取 R15 的零标签 Green 解，
将其两迹与每段 variation-of-constants 积分回传到 $B$，得到
$g_m(B)$；(74.27) 取 $d_m=\ell_m g_m(B)$。每个有限段的准确源费
分别含
$$
\int_B^T e^{4m(T-u)}\frac{|f(u)|}{m}\,du,\qquad
\int_{t_0}^{t_e}e^{9m(t_e-t)}
                 \frac{|f(u(t))|}{m\omega(t)^2}\,dt,
\tag{74.35}
$$
对于 Sturm 普通源 $-y''+m^2q\,y=f$；其符号放入准确积分解，
绝对值只用于 norm。反向传播的对应费用按相反积分方向保留。
真尾普通高度源必须先作
$F^{\rm ref}=\rho F^{\rm phys}$、
$N^{\rm ref}=\rho^3N^{\rm phys}$，再使用 R15 的
$\mathcal S_1,\mathcal S_2$ 及 $2^{77}$ Green 界。

(74.35) 不是任意 source 的免费小量。本文没有声称全部非线性源
已经进入这些加权空间，也没有将其一般 particular trace 的标签
费用无条件套成齐次式 (74.34)。

## 6. 均值是一条必须保留的有限兼容行

在真实径向外区，ground-state 系数的完整表达仍是
$c=4/(4\omega+a^2/z)^2$；即使后续 $q=h''/h$ 变号，零角模满足
$$
(cv_0')'=s_0.
\tag{74.36}
$$
R72 的平坦端满足 $c\to0$。对在实际平开盘准确为零的 $C^2$
强 realization，齐次解的常通量必为0；于是 $v_0$ 为常数，零值
条件再给 $v_0=0$。因此齐次尾的零模两迹是
$$
v_0(0)=0,\qquad p_0(0)=0.
\tag{74.37}
$$
它不是可为任意平均高度指定一条 Robin 斜率的自由线。
这里极限通量也可在物理半径坐标验证：conormal 系数随真实
$W=-z_a$ 趋零，$C^2$ 零迹使一阶导数有界，因此常通量为零。

非齐次均值必须按准确 source 的加权收敛来积分 (74.36)，所得
两迹仍保留。对真实材料应变源还有直接核查式：二面体反射令
角向均值位移为零；若 $P_0,R_0$ 表示均值的
$\theta\theta,uu$ 分量，则
$$
U_0=\frac{hP_0}{2},\qquad
C_0'=2h^2R_0+2\omega h(hP_0)',\qquad
v_0=C_0+\frac{P_0}{2z}.
\tag{74.38}
$$
平端 $C_0=0$ 和真实源决定积分常数。不能用自由平移补这个常数后
仍声称固定两帽。

在与有限正域联立时，先施加所需的平均高度值；剩余的平均通量
作为一条有限输出行保留。双帽的准确腰反射使两条对应行相互关联，
但并不允许在全局方程中直接删去它。

## 7. 接上 R69 非径向正域：真实 Poisson / contact 与均值输出

采用 R69 的真实剪切坐标和 ground-state frame，有限区间长度为
$L_+<25/8$，能量矩阵相对
$\operatorname{diag}(1,x)$ 满足
$$
m_+I<C<M_+I,\quad m_+>0.005804,\quad M_+<146.966.
$$
其 trace 平方常数 $C_{\rm tr}<37.710$，延拓平方常数
$C_E<2.321$，真实角图导数及逆导数至多 $J_*<4.137$。
所有量来自同一个完整1423-cell报告。

入口的 $\Gamma_{\rm ext}$ 是物理角 $\theta$ 的算子。
若 regular 端角图为 $\theta=\Theta(\varphi)$，正确边界形式是
$$
\langle\Gamma_{\rm ext}(v\circ\Theta^{-1}),
                       w\circ\Theta^{-1}\rangle_\theta .
\tag{74.39}
$$
不能把它直接当作 $\varphi$ 中的同一个 Fourier 乘子。
不过其正性严格保留，且
$$
\|f\circ\Theta^{-1}\|_{H^{1/2}_\theta}
\le\sqrt{J_*}\|f\|_{H^{1/2}_\varphi}.
\tag{74.40}
$$
证明：准确换元分别给 $L^2,H^1$ 的 norm 至多 $\sqrt{J_*}$；
对 Hilbert Fourier 尺度应用三线插值即得 $1/2$。负半阶由对偶给出。

将 $\Gamma_{\rm ext}$ 在常数模上定义为0，仅为了写这个半正边界
形式；同时准确施加 regular 端的物理平均值条件。变分子空间取
转折端 trace 为0、regular 物理平均为0。因为转折端为零，
$$
\|v\|_{L^2}^2\le\frac{L_+^2}{2}\|v_x\|_{L^2}^2.
$$
所以加入真实正 Robin 形式后，能量的强逆仍有
$$
g_* \le\frac{1+L_+^2/2}{m_+}<2^{10}.
\tag{74.41}
$$
全形式 norm 由 (74.22)、(74.39)–(74.40) 给
$$
M_* \le M_++(J_*/5)C_{\rm tr}<180.
\tag{74.42}
$$
这已经处理了真正非径向正域，不要求其系数接近径向基态。

设转折端数据为 $a\in H^{1/3}$，regular 端规定的平均 Fourier
系数为 $\xi\in\mathbb C$，常数模采用单位 $L^2$ 基函数。
普通 source 与外部非齐次 Robin 负荷组成 $F\in\mathcal V^*$。
R69 的完整延拓对 $(a,\xi)$ 有 norm 小于2。Lax–Milgram 因而给
唯一实际解，且
$$
\boxed{\quad
\|v\|_{\mathcal V}
 \le2^{19}\|(a,\xi)\|_{H^{1/3}\oplus\mathbb C}
       +2^{10}\|F\|_{\mathcal V^*}.
\quad}
\tag{74.43}
$$
它的完整输出是转折 conormal 和 regular 平均通量行：
$$
\boxed{\quad
\|(p_{\rm turn},\lambda_0)\|_{H^{-1/3}\oplus\mathbb C}
\le2^{28}\|(a,\xi)\|_{H^{1/3}\oplus\mathbb C}
       +2^{19}\|F\|_{\mathcal V^*}.
\quad}
\tag{74.44}
$$
这里直和均用 Hilbert norm。证明是用同一个完整 extension 定义
contact；其 norm 至多 $2(M_*\|v\|+\|F\|)$。
$\lambda_0$ 是平均值约束的实际乘子，等于尚须与真尾匹配的平均
通量差。使它为0或等于指定均值 source 的目标，仍是中央反馈系统
的一条有限方程。

R69 的内部 $H^{2/3}$ 增益使
$L^2_xH^{-2/3}_\varphi$ 普通源到 $\mathcal V^*$ 的 norm 至多2；
它的实际物理 $L^2$ 密度转换 norm 小于2.034。
regular 端物理 $H^{-1/2}$ 负荷经准确对偶角换元与 trace 的
费用小于
$$
\sqrt{J_*C_{\rm tr}}<16.
\tag{74.45}
$$
这些完整 source/contact 包含 mean 和 cross 项，不是只给齐次
允许线。所有变量和符号仍使用 R69 的真实 source 密度。

### 7.1 一个实际有限低块已经可以直接反演

令 $\phi_0=(2\pi)^{-1/2}$。取转折输入 $a=\phi_0$、regular
平均 $\xi=0$、零 source，记 (74.43) 的真实解为 $v_*$，
$E_*=\mathfrak b(v_*,v_*)$，其中 $\mathfrak b$ 是包含真 Robin
边界项的完整形式。则该列的真实均值输出准确为
$$
\lambda_0(v_*)=-E_*<0.
\tag{74.46}
$$
证明如下。全局常数 $\phi_0$ 的体梯度和外部 Robin 像都为零，
故 contact 对它的配对为0，得到
$\langle p_{\rm turn},\phi_0\rangle+\lambda_0=0$。
另一方面用 $v_*$ 配对，regular 平均为0，得到
$E_*=\langle p_{\rm turn},\phi_0\rangle$。符号因此由真实
conormal 方向确定。

写 regular 端的剪切 Jacobian 为 $J(\varphi)$，则
$\int_0^{2\pi}J\,d\varphi=2\pi$，且 $J\le J_*$。实际平均条件给
$$
\langle J(v_*(L_+)-\phi_0),\phi_0\rangle=-1,\qquad
\|J\phi_0\|_2^2\le J_*.
$$
由 Cauchy–Schwarz 及沿径向的准确迹差，
$$
\|v_*(L_+)-\phi_0\|_2^2\ge J_*^{-1},\qquad
\int_0^{L_+}\|\partial_xv_*\|_2^2\,dx
 \ge (L_+J_*)^{-1}.
$$
正能量遂给
$$
\boxed{\quad
E_*\ge\frac{m_+}{L_+J_*},\qquad E_*^{-1}<2^{12}.
\quad}
\tag{74.47}
$$
这是同一实际非径向正域的有限列横截，不是关于近似径向谱的猜测。

例如将左数据写成 $a=a^\perp+\alpha\phi_0$，先以
$a^\perp,\xi,F$ 求得均值输出 $\lambda_0^{\rm rem}$。
要使最终均值输出等于真尾要求的 $\eta$，唯一选择是
$$
\alpha=\frac{\lambda_0^{\rm rem}-\eta}{E_*}.
\tag{74.48}
$$
相应常数列费用至多 $2^{12}$ 乘右端。它准确把这一均值行解成
转折平均值与其它角模 / 全源的边界关系；中央混合型反馈仍须使用
这条关系，没有因此将其平均值变成一个自由参数或把全低块删掉。

这是无角权 Sobolev 结论。正性不自动给同宽解析或 direct-log
边界共轭；(74.39) 的带权交换费用仍应针对该真实角图另外支付。
同样，实际 turn 的 Airy frame 仍按 R39–R54 的准确变换接入，
不把本节能量 frame 直接改名成 Airy 振幅。

## 8. 实际常数文件与剩余全局条件

[有向程序](../scripts/fourfold_phase_exterior_robin_certificate.py)
读取 R66/R69 的完整报告，核同一对象与输入哈希，用有向端点计算
当前 $A_0$、全部频率的单调上界、真实 bump 费用以及
(74.41)–(74.45)。程序未抽样选择好参数；该选择由 §1 的全频定理
准确供应。输出是
[实际 Robin 及正帽报告](../notes/2026-11-12-actual-exterior-robin-certificate.json)。

重放命令：

~~~bash
PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_phase_exterior_robin_certificate.py \
  --out /workspace/scratch/f6a2c7886477/exterior-robin-replay.json
~~~

当前256-bit输出的 Poisson 上界小于241559，
上述幂二界是其安全简写。R69 的中央图、型别、返回与相位输入完全
没有变；这里只增加极远的准确径向双 bump 和外部完整边界实现。

仍未支付的具体输入包括：全反馈的有限低块及均值行、同一实际
非径向算子的带权邻域强逆、所有 source 的统一有限导阶与 Newton
小量，以及 R71 所需的非线性外区精确性保持。R72 真尾的非线性
输出全部保留；没有用其线性切空间替代完整两迹和 mean。
本文不把闭近似背景、无权强解或极小的尾反射误当作已经达到
README 的精确等距可见族。

