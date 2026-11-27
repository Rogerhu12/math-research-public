# R1013 — 原十三权的原点平坦化、完整长系数窗与全部 Cartier 边界

日期：2026-11-27 UTC。**已证明。** 对 R1005 的同一原来源
$f=\mathcal K,\mathcal C_{130}$，本篇把 R1010 的隔核操作扩至
R1000 检出 old 对数所需的整个 $L_p$ 窗口。新增的权在原点作显示的有限阶
平坦化；因此保留的是完整原系数前缀，而不是只保留六个 diagonal 系数，
也不把权产生的较低系数赋零。随后完整补偿原 sigma、指定 $Z_\pi$、
单 $P_{10}$ 及两个 Gaussian 之间的三角变换。

长窗出现的原点留数、非 principal 的二挠对数及一个可能的全纯微分均在
下文保留。两个 exact 层仍只在原二挠点有极，第二层的有理部分仍有
$(p-1)/2$ 的商坐标帽；两个可能的指定 $Z$ 分量另列。最后一节回到
原 canonical 必要行的真实模 $p^H$ 读取，不将特征 $p$ 的亚纯来源
认成已知中央零的全纯 $S_{10}$。

## 1. 范围、原来源和实际长窗

沿用

$$
E_1:y^2=x^3+1,\quad X=x^3,\quad
\delta^2=-3,\quad \pi=(7+\delta)/2,\quad \pi\bar\pi=13.
\tag{1}
$$

本篇取惯性素数

$$
\boxed{p=6s-1>13^3,\qquad
1\le H\le L_p,\qquad N=H(p+1),}
\tag{2}
$$

其中 $L_p$ 是 R1000(27) 的原整数

$$
L_p=\left\lfloor
\frac{(p+1)\log13}{2\log p}
+\frac{\log(2/\sqrt3)}{\log p}\right\rfloor.
\tag{3}
$$

这里增加的只是显示的有限删集 $p\le13^3$。由
$\log p>3\log13$ 及
$\log(2/\sqrt3)/(3\log13)<1/6$，直接得到

$$
\boxed{L_p\le(p+1)/6=s.}
\tag{4}
$$

这比 R1000 对所有 $p>211$ 使用的 $L_p\le(p+1)/4$ 更窄，
用来同时控制完整前缀中非 diagonal 的系数。

写 $f=\sigma^{130}R_f$，其中

$$
R_f=x^2P_f(X),\qquad
(X+1)^2\mid P_f,\qquad
\operatorname{ord}_Of\ge12,\qquad
\operatorname{pole}_OR_f\le118.
\tag{5}
$$

这些是 R1005 的原完整来源身份：
$\mathcal K=51840z^{12}+\cdots$、
$\mathcal C_{130}=-3151872z^{18}+\cdots$。
本篇没有扩大这份来源的中央零范围。

仍使用原 $DZ=1$、$G$、$c_p=\binom{3s-1}{2s-1}\in\mathbf F_p^\times$，以及

$$
\begin{aligned}
R_\pi(X)&=X^2+(2+6\delta)X+(40+24\delta)/13,\\
P_{10}&=-(D-10G)^{p-1}Z^{p+9},\\
u=Z_\pi&=Z(\pi z)/\pi,\qquad
\mathscr P_\pi=\frac{P_{10}(\pi z)}{\pi^{10}R_\pi(X)^{10}},\\
U_{\pi,f}(u)&=\mathscr P_\pi R_f.
\end{aligned}
\tag{6}
$$

$U_{\pi,f}$ 在 $O$ 的阶至少12。所有有限域身份都先在原完美剩余域
及其函数域内成立；需要时可到代数闭包读局部主部，最后按原 Galois
作用下降。$13$ 挠点的 lift 和 $\pi$ 的选择与 R1007/R1010 相同。

## 2. 一整块前缀共用的平坦化权

令

$$
v_\pi=\frac{R_\pi(X)}{(X+1)^2},\qquad
k_r=\lfloor r/6\rfloor,\qquad 0\le r\le H.
\tag{7}
$$

对整数 $a\ge1$ 定义

$$
B_{a,k}(T)=\sum_{j=0}^{k}(-1)^j
\binom{a+j-1}{j}(T-1)^j.
\tag{8}
$$

这是 $T^{-a}$ 在 $T=1$ 的指定截断，故

$$
T^aB_{a,k}(T)=1+O((T-1)^{k+1}),\qquad
B_{a,k}(0)=\binom{a+k}{k}.
\tag{9}
$$

第二式是完整的有限 hockey-stick 求和，不含未定标量。
采用两个实际权

$$
\boxed{\begin{aligned}
W_{r,+}&=v_\pi^{r+1}B_{r+1,k_r}(v_\pi),\\
W_{r,0}&=v_\pi^{r}B_{r,k_r}(v_\pi)\quad(r\ge1),\\
W_{0,0}&=1.
\end{aligned}}
\tag{10}
$$

$v_\pi=1+6\delta z^6+\cdots$，所以两权在 $O$ 都满足

$$
W_{r,\epsilon}=1+O(u^{6(k_r+1)}).
\tag{11}
$$

在每个非零 $T\in\ker\pi$，$W_{r,+}$ 恰有 $r+1$ 阶零，
$W_{r,0}$ 恰有 $r$ 阶零。所用二项式在模 $p$ 均为单位，因为
$r+1+k_r<p$。在原三个非零二挠点，极阶分别为
$4(r+1+k_r)$、$4(r+k_r)$；此外没有极。权可能有其它零点，
但这些零点不产生任何删项或新的极。

现在取前缀中的任意指数

$$
12\le n\le N,\qquad n=rp+b,\quad0\le b<p.
\tag{12}
$$

由 $r\le H$、$6(k_r+1)\ge r+1$，

$$
6(k_r+1)p+12>rp+b=n.
$$

Frobenius 与(5)于是逐系数给

$$
\boxed{[u^n]W_{r,\epsilon}^{\,p}U_{\pi,f}
=[u^n]U_{\pi,f}.}
\tag{13}
$$

这同时保留该 $r$ 块中的所有实际指数。它没有将
$[u^{(h-6j)p+h}]U_{\pi,f}$ 误写成较低 diagonal 系数。
特别，单用 $v_\pi^h$ 在 $h>6$ 时出现的碰撞，已由(8)的真实有限多项式
在原点消去。此消去只在本篇指定的模 $p$ 前缀中使用。

## 3. 全 trace、每个前缀系数和低 jet 核项

使用未平均的函数域 trace，定义实际下层函数

$$
A_{r,\epsilon,p}(f)
=\pi^{-10}\operatorname{Tr}_{[\pi]}
\left(W_{r,\epsilon}^{\,p}\frac{R_f}{R_\pi^{10}}\right).
\tag{14}
$$

对 $b$ 定义完整微分

$$
\eta_{\pi,b}(f)=u^{-b-1}\mathscr P_\pi R_f\omega_E,\qquad
\eta_{10,r,b}^{\epsilon}(f)
=Z^{-b-1}P_{10}A_{r,\epsilon,p}(f)\omega_E.
\tag{15}
$$

与 R1010 相同的原微分尺度逐式给

$$
\boxed{[\pi]_*
\bigl(W_{r,\epsilon}^{\,p}\eta_{\pi,b}(f)\bigr)
=\pi^b\eta_{10,r,b}^{\epsilon}(f).}
\tag{16}
$$

证明中先有 $u^{-b-1}=\pi^{b+1}(Z^{-b-1}\circ[\pi])$，
再有 $\mathscr P_\pi=\pi^{-10}R_\pi^{-10}(P_{10}\circ[\pi])$；
微分 pushforward 另除一次 $\pi$，所以剩下
$\pi^{b-10}\operatorname{Tr}=\pi^b A$。没有平均掉原13项。

记

$$
t_n^\pi(f)=[u^n]U_{\pi,f},\qquad
t_n^{10}(A)=[Z^n]P_{10}A.
\tag{17}
$$

在 $O$，第一 Cartier 的 $u^{r-1}\omega_E$ 系数为
$(t_n^\pi)^{1/p}$。在每个非零 $T\in\ker\pi$，原输入极阶至多
$b+1\le p$；因此第一 Cartier 只留下一个可能的简单极。
其留数准确为

$$
c_b(T_Tf)^{1/p}.
\tag{18}
$$

这里 $c_b(T_Tf)$ 是原规范 Miller 平移来源的完整 $b$ 阶 Taylor 系数，
包括全部指数 prefactor。理由是 $b<p$，而原 $P_{10}$ 与 sigma 模型的首差、
Gaussian 项和 $Z$ 参数差均高于这一局部读取。没有把它改成质量
$c_0$，也没有把它认作中央导数。

$W_{r,+}$ 将(18)乘到 $u^r\omega_E$ 或更高，故不贡献所读
$u^{r-1}\omega_E$。$W_{r,0}$ 则恰留下

$$
\begin{aligned}
\lambda_{r,\pi}(T)
&=\binom{r+k_r}{k_r}
\left(\frac{DR_\pi(T)}{(X(T)+1)^2}\right)^r,\\
\mathcal B_{r,b,\pi}(f)
&=\sum_{0\ne T\in\ker\pi}
\lambda_{r,\pi}(T)^p\,c_b(T_Tf).
\end{aligned}
\tag{19}
$$

$r=0$ 时按 $\lambda_{0,\pi}=1$ 解释。所有12个非零核点均保留；
若按 $\mu_6$ 轨道压缩，必须使用(19)的实际权与实际角色。

局部目标参数是严格的 $Z=\pi u$，所以
$u^{r-1}du=\pi^{-r}Z^{r-1}dZ$。将 Cartier 后的(16)取 $p$ 次方，
结合(13)，得到完整前缀身份

$$
\boxed{\begin{aligned}
t_n^\pi(f)
&=\pi^n\,t_n^{10}(A_{r,+,p}(f)),\\
t_n^\pi(f)
&=\pi^n\,t_n^{10}(A_{r,0,p}(f))
-\mathcal B_{r,b,\pi}(f).
\end{aligned}}
\tag{20}
$$

准确的尺度是 $\pi^{rp+b}$。只有在 diagonal $r=b=h$ 时，
它才是 $\pi^{h(p+1)}=13^h$。这保留了全部非 diagonal 项的
原 CM 相位。核项的负号来自从左边移到右边，没有额外因子13。

## 4. 全支撑、原点留数与第三 Cartier 的完整小边界

第4–7节均消费 $+$ 权。
对 $r\ge1$ 的 $0$ 权，可将 $r+1+k_r$ 换成 $r+k_r$ 得到相应上界；
$r=0$ 的 $W_{0,0}=1$ 未消去十三核，故只保留(20)的完整 trace 身份，
不对该下层函数套用以下原点正则性与极帽。记

$$
e_r=r+1+k_r,\qquad
C_{r,b}=8-b+4e_r,\qquad
d_{r,b}=p^3-p^2+C_{r,b}p-3.
\tag{21}
$$

### 4.1 没有遗漏原 Z 的其它零点

由定义有整个函数域身份

$$
P_{10}=-Z^p(D-10G)^{p-1}Z^9.
\tag{22}
$$

在 $O$ 和原二挠之外的 $Z=0$ 点，$G$、$Z$ 及右边余因子均正则，
所以 $P_{10}$ 至少有 $p$ 阶零。因 $b+1\le p$，
(15)中的 $Z^{-b-1}$ 不产生其它极。这使用的是原指定 $Z$，
不是把移动零点从一个没有该因子的模型中删去。

在上游，$W_{r,+}^p/R_\pi^{10}$ 于非零 $\ker\pi$ 的零阶至少
$(r+1)p-10>0$；在 $O$，$R_f/R_\pi^{10}$ 至少有二阶零。
因此 $A_{r,+,p}$ 只在原二挠点有极，极阶至多 $4e_rp-4$，并且
$\operatorname{ord}_O A_{r,+,p}\ge2$。
原 $P_{10}$ 的二挠帽为 $p^3-p^2+9p+1$，
所以(15)的二挠帽正是(21)。

由(4)，

$$
C_{r,b}\le12+\frac{14H}{3}
\le12+\frac{7(p+1)}9<p.
\tag{23}
$$

故全部前缀微分的二挠帽严格小于 $p^3$。
在 $O$ 的极阶至多 $b-11<p$。第三 Cartier 后，二挠和 $O$
都只可能有简单极；此外可能有一个全纯微分，不能直接宣布全部为零。

### 4.2 原点留数的实际值

在 $b<p$ 的低 jet 中，trace 的非零核点分支从
$z^{(r+1)p}$ 才开始。$O$ 分支准确是 $f(z/\pi)$；
权的 $p$ 次幂和两个 Gaussian 在这一低窗均不改变系数。因此

$$
\boxed{\operatorname{res}_O\eta_{10,r,b}^{+}
=\pi^{-b}c_b(f)=:\rho_b.}
\tag{24}
$$

$f$ 是 principal，所以 $c_b(f)=0$，除非 $6\mid b$。
特别，当 $b\ge12$ 时不能仅凭 $f$ 从十二阶起就删掉这个留数。

### 4.3 所有六种角色

令原 $\mu_6$ 生成元为 $\varepsilon=-\omega$。
原微分(15)的角色是 $\varepsilon^{-b}$；
每次 Cartier 对角色取 $p$ 次根，故第三次后的角色是
$\varepsilon^b$。

写

$$
r_E=\frac{x^2}{y},\qquad
\beta_1=-\frac3y\omega_E,\qquad
\beta_2=-\frac{3x}{y}\omega_E.
\tag{25}
$$

$r_E\omega_E$ 在 $O$ 的留数为 $-1$，在每个非零二挠点为 $1/3$。
若 $e^3=-1$，则

$$
\beta_j=\frac12\sum_{e^3=-1}e^j\,d\log(x-e)\quad(j=1,2).
\tag{26}
$$

因此其二挠留数分别是 $e,e^2$，在 $O$ 留数为零。这里的绝对符号为

$$
\mathcal C(r_E\omega_E)=r_E\omega_E,\qquad
\mathcal C\beta_1=-\beta_2,\qquad
\mathcal C\beta_2=-\beta_1.
\tag{27}
$$

后两式的负号来自 $e^p=e^{-1}=-e^2$，不能只看模3的角色而丢掉它。

若 $b\equiv0\pmod6$，令 $\ell_b=-\rho_b r_E\omega_E$。
若 $b\equiv2,4\pmod6$，令 $j$ 为 $-b\bmod3$ 的 $1,2$ 代表，
并以原 $(-1,0)$ 二挠点的实际留数确定唯一
$a_b$，使 $\ell_b=a_b\beta_j$ 与(15)的全部二挠留数相同。
具体是 $a_b=(-1)^j\operatorname{res}_{(-1,0)}\eta_{10,r,b}^{+}$。
若 $b$ 为奇数，令 $\ell_b=0$。

这是全部留数：奇角色在被 $[-1]$ 固定的二挠点没有对数留数；
偶角色的三个留数由原 $\mu_3$ 作用和全局留数定理确定。
于是有完整分类

| $b\bmod6$ | $\mathcal C^3\eta_{10,r,b}^{+}$ |
|---|---|
| $0$ | $\mathcal C^3\ell_b=-\rho_b^{1/p^3}r_E\omega_E$ |
| $1$ | $\alpha_{r,b}(f)\omega_E$ |
| $2,4$ | $\mathcal C^3\ell_b$，保(27)的负号 |
| $3,5$ | $0$ |

表中唯一可能的全纯项出现在 $b\equiv1$，因为
$H^0(E_1,\Omega^1)$ 的角色是 $\varepsilon$。
$\alpha_{r,b}$ 是实际微分第三 Cartier 的系数，不是新增可调参数。
例如可直接用原 $p$ 基连续作三次 Cartier，或在 $O$ 读
$[Z^{p^3-1}](\eta/\omega_E)$ 后取 $p^3$ 次根，得到同一个确定值。
其余角色没有全纯余项。这个表保留了长窗新增的全部小边界。

## 5. 两 exact 层、两个指定 Z 分量与可计算的原点权

本节给完整构造，不以“存在某个 primitive”省掉原点读取。
全部操作在同一特征 $p$ 曲线上进行，保原 $Z$。

### 5.1 一个只有原二挠极的 Cartier 截面

有显示的微分

$$
\varphi=-\frac{3x}{c_p(X+1)}\omega_E,\qquad
\mathcal C\varphi=\omega_E.
\tag{28}
$$

证明：$D^{p-1}x=-c_p$ 给
$\mathcal C(x\omega_E)=c_p\omega_E$，而原倍点公式给
$(4x(2z)-x(z))/3=-3x/(X+1)$。
Cartier 与 $[2]$ 及原微分尺度交换，故(28)成立。
$\varphi$ 仅在原二挠有二阶极。

对任何只在原二挠有极、留数为零的微分 $\nu$，构造
$\mathfrak S(\nu)$ 如下。先在 $T=(e,0)$ 固定代数参数
$\tau_T=y/(3e^2)$；以 $\tau_T$ 展开 $\omega_E$，
取唯一常数项为零、所有正 $p$ 倍次系数为零的形式原函数 $u_T$。
它存在，因为 $\mathcal C\omega_E=0$，并且
$u_T=\tau_T+\cdots$、$du_T=\omega_E$。
该选择与原 Galois 及 $\mu_6$ 作用相容。
在这些指定的完整形式参数中，
将每个实际主部 $a_m u^{-m}du$（$m\ge2$）换成
$a_m^p u^{-p(m-1)-1}du$。这些主部没有留数，故由微分的
Mittag-Leffler 定理给一个全局微分 $\theta$，仅有指定的二挠极；
令它在 $O$ 的 $\omega_E$ 常数项为零，固定其唯一全纯歧义。
$\mathcal C\theta-\nu$ 是 $c\omega_E$；
减去 $c^p\varphi$ 后得到

$$
\boxed{\mathcal C\mathfrak S(\nu)=\nu,\qquad
\operatorname{pole}\mathfrak S(\nu)
\le\max\{p(d-1)+1,2\}}
\tag{29}
$$

（$\nu$ 的逐点极帽为 $d$）。
取原 $\mu_6$ 投影保持所需角色；上述归一保持不变，因为
$\varphi$ 在 $O$ 从四阶起。这个截面是确定的 $p$ 次线性映射，
特别 $\mathfrak S(a\omega_E)=a^p\varphi$。
这个过程只解显示主部和一个全纯系数，
每一步均由原微分确定，且没有添加其它极。

置

$$
\psi=\mathfrak S(\varphi),\qquad
\chi=\mathfrak S(\psi).
\tag{30}
$$

则 $\mathcal C\psi=\varphi$、$\mathcal C\chi=\psi$、
$\mathcal C^3\chi=\omega_E$；
其逐点极帽分别为 $p+1,p^2+1$，角色分别为
$\varepsilon,\varepsilon^{-1}$。

### 5.2 Cartier 零微分的全局 primitive

若 $\nu$ 只在原二挠有极、$\mathcal C\nu=0$，
则其局部原函数的所有非 $p$ 倍负次项都可按单位分母逐项积分。
记这些指定主部为 $V_T$。它们确实能全局拼成一个只在二挠有极、
$V(O)=0$ 的有理函数 $V$。

为核最后一个全局条件，$DZ=1$ 使在每个点
$Z=u+h_T(u)^p$。于是

$$
\operatorname{res}_T(V_T\omega_E)
=-\operatorname{res}_T(Z\nu).
\tag{31}
$$

右边在全部点的和为零；$Z$ 与 $\nu$ 的极都只在原二挠。
所以(31)恰支付函数 Mittag-Leffler 的唯一全局障碍。
$\nu-dV$ 为 $a\omega_E$，从而

$$
\boxed{\nu=d(V+aZ).}
\tag{32}
$$

$V$ 的逐点极帽至多为 $\nu$ 的帽减一。
按角色投影后，$a$ 仅可能在 $\nu$ 的角色为
$\varepsilon$ 时非零。这里单独保留 $aZ$，不把正则
$\omega_E=dZ$ 的有理 primitive 冒称为全局正则函数。

### 5.3 对本篇长窗的完整应用

记 $\eta=\eta_{10,r,b}^{+}$。若 $b\equiv1\pmod6$，令
$\alpha=\alpha_{r,b}(f)$；其余情形令 $\alpha=0$。
定义

$$
\eta^\circ=\eta-\ell_b-\alpha^{p^3}\chi.
\tag{33}
$$

由上表，$\mathcal C^3\eta^\circ=0$。
原点的小于 $p$ 阶极在第一次 Cartier 后只留下留数，
已由 $\ell_b$ 完整消去。因此
$\nu_1=\mathcal C\eta^\circ$、
$\nu_2=\mathcal C^2\eta^\circ$ 都只在原二挠有极，
且 $\mathcal C\nu_2=0$。

按(32)写

$$
\nu_2=dH_1,\quad H_1=V_1+a_1Z,\qquad
\nu_1-\mathfrak S(\nu_2)=dH_0,\quad H_0=V_0+a_0Z.
\tag{34}
$$

于是整条第一 Cartier 的身份为

$$
\boxed{\mathcal C\eta
=\mathcal C\ell_b
+\alpha^{p^2}\psi
+\mathfrak S(dH_1)+dH_0.}
\tag{35}
$$

每一项都保留真实原点权。最终的下层系数准确是

$$
\boxed{t_n^{10}(A_{r,+,p})
=\left([Z^{r-1}]
\frac{\mathcal C\ell_b+\alpha^{p^2}\psi+
\mathfrak S(dH_1)+dH_0}{\omega_E}\right)^p.}
\tag{36}
$$

$r=0$ 按 $Z^{-1}$ 留数读取解释，仍是同一公式。
不以两个无权数 $H_0'(O),H_1'(O)$ 代替(36)；
只有在 principal 的六阶特例，才可改用 R1010 的原
$Y=(t-1)^{-1}$ 表达，回到其带 $-6$ 的两导数式。

### 5.4 全部极帽

第一 Cartier 后的形式上界是
$d_1=p^2-p+C_{r,b}$。
在二挠处，$[-1]$ 的角色要求实际极阶与 $b+1$ 同奇偶，
而 $d_1\equiv b\pmod2$，故实际帽至多 $d_1-1$。
第二 Cartier 后的帽准确满足
$d_2\le\lfloor(d_1-2)/p\rfloor+1\le p$，因而
$p(d_2-1)+1\le d_1-1$。
这逐式证明构造(29)不增加第一层的实际帽，
包括 $C_{r,b}<2$ 的非 diagonal 情形。
(30)的两个固定边界帽也都更小。

令 $t=-X^{-1}$。一个指定角色的函数可唯一写成
$x^j y^\epsilon R(t)$，$0\le j\le2$、$\epsilon\in\{0,1\}$；
$R$ 除 $t=1$ 外没有极，且在 $t=0,\infty$ 满足原正则条件。
其 $t=1$ 分母次数帽由(34)准确给

$$
\boxed{\begin{aligned}
\deg_1 V_0
&\le\frac{p(p-1)}2+
\left\lfloor\frac{C_{r,b}-1}{2}\right\rfloor,\\
\deg_1 V_1&\le\frac{p-1}{2}.
\end{aligned}}
\tag{37}
$$

这里 $\deg_1$ 指剥除该指定 $x^jy^\epsilon$ 后的
$(t-1)$ 分母次数，不是任意新增多项式的自由度。
另外

$$
a_0=0\ \text{除非 }b\equiv1\pmod6,\qquad
a_1=0\ \text{除非 }b\equiv5\pmod6.
\tag{38}
$$

这两个指定 $Z$ 分量完整进入(35)–(36)。
对 $dH_0$，其 $a_0\omega_E$ 只在 $r=1$ 的读数贡献；
对 $a_1\omega_E$，其真实 Cartier 截面按(28)为
$a_1^p\varphi$，仍保留在 $\mathfrak S(dH_1)$ 中。
因此没有把 supersingular 的全纯 exact 分量删掉。

## 6. 回到原 sigma 与 Gaussian 的完整三角矩阵

前述输入是指定有限 $P_{10}$。现在逐项付回真正的原长窗。
以下(39)–(44)均在模 $p$ 的完整有限 jet 内使用；
所需 sigma 级数先在 R614 的完整整 jet 内形成再约化。
因为 $N\le(p+1)^2/6$，本篇所需次数加固定130仍严格低于
$p^2-1$；没有越过原高度二整性端点。

用原 $\sigma^\circ(z)=\sigma(z)e^{-cz^{p+1}}$ 定义确定的单位级数

$$
E_{\pi,p}(z)=\frac{\sigma^\circ(\pi z)^{10}}{P_{10}(\pi z)},
\qquad u(z)=Z(\pi z)/\pi=z\,V_{\pi,p}(z).
\tag{39}
$$

先剥掉分子分母共同的十阶零，(39)就是模 $p$ 常数项1的单位相除。
可先任选指定 $P_{10}$ 的整提升作单位相除，再约化；结果与提升无关。
不要求未约化的微分算子表达也以1为首系数。
该模 $p$ 单位在本篇完整有限窗内有唯一确定的逆。
R887 的原首差仅用于说明

$$
E_{\pi,p}=1+O(z^{6p}),\qquad
V_{\pi,p}=1+O(z^{5p-1});
\tag{40}
$$

高于该首差的所有系数都从(39)读取，不能由(40)宣布为零。
它们由同一原 sigma、同一 $P_{10}$ 和同一 $Z$ 计算，
没有任何新的 Frobenius 初始变量。

对 $0\le m,n\le N$，定义完整下三角矩阵

$$
\boxed{
M_{\pi,p}(m,n)
=[z^{m-n}]\,E_{\pi,p}(z)V_{\pi,p}(z)^n
\quad(n\le m),}
\tag{41}
$$

其余项为零。每个 diagonal 项为1。所有项可用有限单位级数的
乘法、反演及幂直接生成，不需除以 $p$；
原 sigma 系数的真实除 $p$ 则仍由 R614 的整窗支付。
因原角色，实际只需 $6\mid m,n$ 的子矩阵，但不是仅需
$m,n$ 都为某个 $h(p+1)$。

适配 Gaussian 的真实来源为

$$
f(z)e^{-10c\pi^{p+1}z^{p+1}}
=E_{\pi,p}(z)\,U_{\pi,f}(u(z)).
\tag{42}
$$

故其全部前缀系数为 $M_{\pi,p}(m,n)t_n^\pi$ 的完整和。
这同时补偿了 $P_{10}$ 的高项和原 $Z$ 的非线性参数差。
例如六阶时出现的原 $7\kappa_5a^+$ 项就在(41)的实际非 diagonal
项中，没有被删掉；长窗的所有后继项也按同一方式保留。

令

$$
\gamma_{\pi,p}=10c(\pi^{p+1}-13)\in\mathcal O,\qquad
g_h(f)=[z^{h(p+1)}]e^{-130cz^{p+1}}f(z).
\tag{43}
$$

$\gamma_{\pi,p}$ 为整量，因为 $\pi^{p+1}\equiv13\bmod p$，
而原 $v_p(c)=-1$。由(42)，对所有 $h\le H<p$，准确有

$$
\boxed{
\overline{g_h(f)}
=\sum_{j=0}^{h}\frac{\overline\gamma_{\pi,p}^{\,j}}{j!}
\sum_{\substack{12\le n\le(h-j)(p+1)\\6\mid n}}
M_{\pi,p}((h-j)(p+1),n)\,t_n^\pi(f).}
\tag{44}
$$

这里所有 $j!$ 均为单位。(20)、(36)、(44)合成一个从原
完整 trace／小 Cartier 边界／两 exact 到原实际
$\overline g_h$ 的有限计算程序。矩阵(41)为单位下三角，
故其逆也只是逐行单位递推；不会把一个未付的低系数当自由量或零。
整个过程同时保留全部 $n\le N$，所以确实封闭，而非停在 diagonal
以外仍未登记的系数上。

## 7. 同一 canonical 必要行的真实模 p^H 读取

保持原
$q=65/17$、$\mathfrak a=p\kappa\in\mathcal O^\times$，
并令

$$
F_f^{[H]}(0)=
\sum_{h=1}^{H}
\frac{(-1)^{h-1}(h-1)!p^{h-1}}
{q^h\mathfrak a^{h-1}}\,g_h(f).
\tag{45}
$$

R1000 的完整整窗及强 Hurwitz 全尾逐项给

$$
\boxed{F_f^{[H]}(0)\equiv\frac{\mathfrak a}{p}j_f
\pmod{p^H}\qquad(H\le L_p).}
\tag{46}
$$

记 $\mathscr R_{p,H}(f)$ 为(44)在 $h=H$ 的完整右边，
其中每个 $t_n^\pi$ 使用(20)、(36)的实际值。
则同一个原必要行准确变成

$$
\boxed{
F_f^{[H]}(0)\equiv
F_f^{[H-1];\,H}(0)
+\frac{(-1)^{H-1}(H-1)!p^{H-1}}
{q^H\mathfrak a^{H-1}}\,
\widetilde{\mathscr R}_{p,H}(f)
\pmod{p^H}.}
\tag{47}
$$

$F^{[H-1];H}$ 是(45)的真实前 $H-1$ 项，**仍读模 $p^H$**；
它不是只给模 $p^{H-1}$ 的任意提升。
$\widetilde{\mathscr R}$ 可取任意整提升，差乘 $p^{H-1}$ 后消失。
本篇没有把模 $p$ Cartier 公式宣称为全部低项的高精度提升；
所需的高精度低项继续由同一原 sigma 整窗生成。
因此(47)与 R1010 的六位式具有完全相同的真实精度范围，
但现在明确覆盖所有 $H\le L_p$。

在原两 canonical 坏假设下，R1005 给

$$
j_{\mathcal K}=0,\qquad
j_{\mathcal C_{130}}
=-\frac{\delta(p+1)}{112}\log_p(\pi/\bar\pi)\ne0.
\tag{48}
$$

取 $H=L_p$，R1000 的 Lucas 估计严格给

$$
\boxed{
F_{\mathcal K}^{[H]}(0)=0\pmod{p^H},\qquad
F_{\mathcal C_{130}}^{[H]}(0)\ne0\pmod{p^H}.}
\tag{49}
$$

故这两个真实值现已可以在(47)的**同一个完整长读者**中比较。
它没有把下层 $A_{r,+,p}$、所有 $T_Tf$、$\alpha_{r,b}$、
二挠对数或两个 exact 另行赋零；要从 canonical 坏条件导出矛盾，
仍必须消费这些显示的实际项。这里不把(49)本身当作完成主目标。

## 8. 双支、输入和坏素数

对 $\bar\pi$ 逐式使用原共轭函数与实际 $\bar\pi^n$，
得到完整第二支。不能把(20)的非 diagonal $\pi^n$ 换成
$13^{n/(p+1)}$，也不能因两支共轭而先认其中央读数相同。

本篇仅删去 $p\le13^3$，并限定原惯性类 $p\equiv5\bmod6$。
原来源的固定分母及 $2,3,5,7,13,17$ 均已在这个范围之外；
二项式、$j!$、原 $c_p$、微分投影的6及函数 trace 的13全部为单位。
没有使用 R1010 核项分别非零的额外范数删集，
也没有宣称(19)对每个 $r,b$ 非零。

本篇不需要新数学运行。原 $\mathcal K,\mathcal C_{130}$、
全部 $R_\pi,P_{10},Z$、原平移 lift 均来自已支付的完整来源；
长窗身份由显示有限权、完整函数域 trace、Cartier 的局部公式及
全局主部拼合逐式证明。实际生产若执行(39)的高 jet，
仍须从原完整 sigma 递推支付每次真实除 $p$，而不能只重用 R941
到第六窗的两次除 $p$ 回执。

引用：R614（原高度二完整整窗）；R887（原 $Z,G,P_a$、首差和
全角色）；R1000（$L_p$ 与全 Newton 尾）；R1004（原完整十三核
及平移规范）；R1005（$\mathcal K,\mathcal C_{130}$ 和真中央值）；
R1007（适配模型及 Gaussian）；R1010（六阶隔核和未平均 trace）。


## 9. 同一个平坦权作用整个原22维来源，及保全 W 的配对

本节是在上述结论之后的完整来源扩展。令

$$
\mathcal V_{130}=\Pi_0\mathcal S_{130}
=\left\{\sigma^{130}x^2P(X):\deg P\le21\right\}.
\tag{50}
$$

取其原整基 $\sigma^{130}x^{2+3j}$（$0\le j\le21$）上的
$\mathcal O$ 系数。现在允许质量和六阶非零，也不要求
$(X+1)^2\mid P$。下面重新支付因此改变的帽，不沿用(5)的增益。

### 9.1 整个前缀保留，不需要十二阶起点

本节 $U_{\pi,f}$ 仅从零阶起。原(10)的同一个 $W_{r,+}$ 仍满足

$$
6(k_r+1)p\ge(r+1)p>rp+b=n.
\tag{51}
$$

因此(13)对全部 $0\le n\le N$ 原样成立；不需增加一个可调权。
原(16)、(18)–(20)的完整 trace、全部核低 jet 和 $\pi^n$ 尺度均保持。
在(39)–(44)使用同一单位下三角矩阵，但(44)的内和下限准确改为
$n=0$，完整保留质量项及其 Gaussian 卷积。

$+$ 权仍消掉非零十三核的全部极。现在只能断言
$\operatorname{ord}_O A_{r,+,p}\ge-10$；
乘 $\sigma^{10}$ 或 $P_{10}$ 后仍正则，质量正是原 $m_0(f)$。
在二挠处，$R_f$ 是正则函数，失去原四阶零的增益，所以

$$
\boxed{\begin{aligned}
\operatorname{pole}_{E[2]\setminus O}\eta_{10,r,b}^{+}
&\le d_{r,b}^{\rm full}
=p^3-p^2+C_{r,b}p+1<p^3,\\
\operatorname{pole}_O\eta_{10,r,b}^{+}&\le b+1\le p,\\
\operatorname{res}_O\eta_{10,r,b}^{+}
&=\pi^{-b}c_b(f).
\end{aligned}}
\tag{52}
$$

这里仍是(21)的同一 $C_{r,b}$。由(23)和 $p>13^3$，
$C_{r,b}\le p-1$，所以第一式的严格不等号成立。
当 $b=0$ 时，最后一式包括真实的 $m_0(f)$，不能省去。
(22)仍付全部其它 $Z=0$ 点的正则性。

### 9.2 重新支付第一层精细帽

本节第一 Cartier 的形式帽为

$$
d_1^{\rm full}=p^2-p+C_{r,b}+1.
\tag{53}
$$

它已经与 $b+1$ 同奇偶，因此这次**不能**再减一。
第二层满足

$$
d_2^{\rm full}
\le\left\lfloor\frac{d_1^{\rm full}-1}{p}\right\rfloor+1
\le p,\qquad
p(d_2^{\rm full}-1)+1\le d_1^{\rm full}.
\tag{54}
$$

原 §4.3 的六种角色表完整保持；其 $\rho_b$、$a_b$、
$\alpha_{r,b}$ 都读取本节实际完整微分。
同样的(28)–(36)于是仍给全部边界和两 exact，但精细帽改为

$$
\boxed{\begin{aligned}
\deg_1 V_0^{\rm full}
&\le\frac{p(p-1)}2+
\left\lceil\frac{C_{r,b}}2\right\rceil,\\
\deg_1 V_1^{\rm full}&\le\frac{p-1}{2}.
\end{aligned}}
\tag{55}
$$

这恰比(37)的第一层上限增加一，而不是无声地保留旧帽。
两个 $a_0Z,a_1Z$ 的角色范围与原点权仍为(38)。
因此全22维扩展并未删除质量、原点小留数或全纯 exact 分量。

### 9.3 全22维的真实 Tate 尾和质量修正

用 R602 的原 $W=z^2x$、$U_\sigma=\sigma^\circ/z$，
第 $j$ 个整基的整个 Gaussian 来源准确为

$$
e^{-130cz^{p+1}}\sigma^{130}x^{2+3j}
=w^{21-j}U_\sigma^{130}W^{2+3j},\qquad 0\le j\le21.
\tag{56}
$$

全部指数非负。这些式子属于同一个完整整 Hurwitz 代数，
并在 R614 的 $w<s(p-1)$ 窗口内系数全整。
质量非零没有增加一个负幂输入。

令 $J_f(v)$ 为原 Newton 级数，保其 $h=0$ 常数项 $m_0(f)$。
该项的导数为零，故原(45)的导数截断形式保持。
对每个完整基，强 Hurwitz 界给归一后第 $h$ 项

$$
v_p(\text{第 }h\text{ 项})
\ge h-1-v_p((hs)!)+v_p((h-1)!)
\ge\frac{h(5p-7)}{6(p-1)}-1.
\tag{57}
$$

取 $h_0=(p-1)/2$。在 $h\le h_0$ 时，所读 $hs$ 严格小于
原整窗端点，故 $h>H$ 的各项含 $p^H$。
在 $h>h_0$ 时，(57)严格大于 $(p+1)/6\ge H$；
在首端点这归结为 $3p^2-14p+7>0$，随后随 $h$ 单调增加。
所以(46)–(47)对整个原整 $\mathcal V_{130}$ 仍成立。
该论证保全部无限尾，未沿用质量零时的额外六阶增益。

若另以适配 Gaussian 定义整个 $J_f^{(\pi)}$，则质量修正为

$$
J_f^{(\pi)}(v)=q_\pi^{-v}J_f(v),\qquad
j_f^{(\pi)}=j_f-m_0(f)\log_pq_\pi,\qquad
q_\pi=\pi^{p+1}/13.
\tag{58}
$$

这由原所有非负整数权及上述 Tate 收敛得到。
本篇实际(44)已经换回原 Gaussian，所以使用(47)时不再另减一次；
若直接比较适配中央值，则必须保(58)。尤其不将质量一伴线的
两个适配导数冒认相同。

### 9.4 几何投影只与整个带权 trace 交换

对全 $\mathcal S_{130}$ 定义同一亚纯 theta 算子

$$
\mathscr A_{r,p}(f)=\sigma^{10}A_{r,+,p}(f).
\tag{59}
$$

$W_{r,+}(X)$ 是完整几何主型，$[\pi]$ 与 $\mu_6$ 交换，
且 $130-10=120$ 被6整除。因此原两个 theta frame 的实际角色给

$$
\boxed{\Pi_0^{(10)}\mathscr A_{r,p}
=\mathscr A_{r,p}\Pi_0^{(130)}.}
\tag{60}
$$

这是一条**整个** trace 算子的等变身份。
若先分成 R1012 的字 $G_j^pF_{-pj}$，
(60)仍要求对完整 product 作 $\Pi_0$；
它不允许把单个非 principal $G_j^p$ 留在外面，只投影 $F_{-pj}$。

使用 R1012 的原绝对相位，记
$\nu_\pi=g m_\pi/13$、
$\rho_\pi=-11(1+\delta)/40$、
$L_\pi=(t x_{\bar\pi}-x_\pi)/(t-1)$、
$\Psi=\Psi_{571220}$。
其整个来源身份通过(60)给，对每个 $i\ne0$，

$$
\boxed{\begin{aligned}
\Pi_0^{(10)}\mathscr A_{r,p}
      (\mathcal P_{\pi,i}\Phi_*)
 &=\frac{\mathscr A_{r,p}(\Phi_*)}{12}
   +\varepsilon(i)\nu_\pi\,\mathscr A_{r,p}(L_\pi),\\
\Pi_0^{(10)}\mathscr A_{r,p}
      (\mathcal P_{\pi,i}\Phi_{260})
 &=\frac{\mathscr A_{r,p}(\Phi_{260})}{12}
   +\varepsilon(i)\rho_\pi\nu_\pi\,
       \mathscr A_{r,p}(\Psi).
\end{aligned}}
\tag{61}
$$

还可在完整 product 上直接核(61)。令
$\mathfrak f=R_f/R_\pi^{10}$，
$\mathfrak F_i$ 是它的第 $i$ 个原 deck Fourier 分量，
$G_j$ 是整个 $W_{r,+}$ 的第 $j$ 个 deck 分量（都含实际 Kummer 字幂）。
当 $i+pj\equiv0\pmod{13}$ 时，完整未平均 trace 和正交投影给

$$
\boxed{\begin{aligned}
[\pi]^*A_{r,+,p}(\mathcal P_{\pi,i}f)
 &=13\pi^{-10}G_j^p\mathfrak F_i,\\
\Pi_{-10}(G_j^p\mathfrak F_i)
 &=\frac{\pi^{10}}{13}[\pi]^*
 A_{r,+,p}(\Pi_0\mathcal P_{\pi,i}f).
\end{aligned}}
\tag{62}
$$

$\Pi_{-10}$ 是源函数的实际 $\varepsilon^{-10}$ 角色投影，
与除去 $\sigma(\pi z)^{10}$ 的原 frame 相容。
将 R1012 的全来源式代入(62)，就是(61)的逐个带权字版本；
投影始终施在 $G_j^p\mathfrak F_i$ 整体上。

这里的右边仍是同一 $W_{r,+}^p$ 的完整加权输入。
$L_\pi,\Psi$ 的质量一和全部高系数均保留；
不能将 $\mathscr A(L_\pi)$ 或 $\mathscr A(\Psi)$
直接换成未加权的两个数 $j(L_\pi),j(\Psi)$。
对 $\bar\pi$ 原样保其全部相位得到第二支。
质量匹配与双支差可以在(61)上作真正线性运算，
但两支各自的带权 trace 算子也必须保留。

这些实际伴线属于本节整格：$L_\pi$ 的唯一新分母为
$t-1$（范数16）；$\Psi$ 由 R1012(30)的完整整 theta 投影及
$\rho_\pi\nu_\pi$ 规范。
该规范量的所有零极只在 $2,3,5,7,11,13$，所以本篇
$p>13^3$ 没有额外的整性删集。

最后，R1012(44)给(14)的完整、无需选择 torsion 根的13维有理余式。
可将本篇已经显示的 $W_{r,+}$ 直接代入该式，计算所有
$A_{r,+,p}$，再使用本篇完整前缀与(55)。
因此(61)是固定字线与原 canonical 长窗之间可直接消费的实际配对；
它仍不把 canonical 零传播给各字或各亚纯伴线。


