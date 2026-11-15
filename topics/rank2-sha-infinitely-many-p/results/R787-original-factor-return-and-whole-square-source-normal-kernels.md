# R787 — 五型因子的零增 charge 返回、全 F² 来源块及最后一条相对 carry

日期：2026-11-15。**状态：本文的全来源核识别、单位块和实际 normal 矩阵已证明；该矩阵的指定右端成员性、全余列吸收以及原主目标仍开。**

R782 已把实际 $r=2,m_q=0$ 因子限制到有限角型。本篇先证明每型的 $G$ 乘一个次数至多二的固定角多项式，已经返回原 $\mathcal W_b$。随后不只取旧 $qt^2F^2\mathcal H_1$ 子格，而完整读取原 $\mathcal W_D$ 中全部 $F^2$ 整除来源。

这个全块在短 $M$ 中只有一个 normal jet；相对 $J$ 恢复的最后一行仍含第三展开项，不能删除。准确门相差十二阶。在可用范围内，全 $F^2$ 首核恰是全 cube 空间，原其余首核方向必须在曲线上保非零限制或只有一个 $F$ 因子。末节给 R782 scalar-projection 尾的完整实际矩阵，不预判它非零，也不把两个单位块相加。

## 1. 同一原范围与两个真实来源子格

保 R782/R771 的
$$
p=12h+11=6s-1>101,\quad s=2h+2,\quad
r=2,\ \ell=1,\ k_{\rm carry}=0,\quad f_D<p,
$$
$$
P^{\rm fact}=qt^2F^3\in\mathcal W_D,\quad
b=\deg_YF\ge3,\quad b_0=3,\quad
m_F=3,\quad m_q=0,\quad D\ge3b .
\tag{1}
$$
$F$ primitive 不可约，原点 $P=(0,1)$ 光滑，
$F_Y(P),q(P)\ne0$。保原十九角曲面 $X$、曲线 $C$、同一整因子提升及全部真实原格。
写
$$
\kappa=C^2,\qquad
\operatorname{div}(P^{\rm fact})=3C+E,\qquad
E|_C=2P+E',\qquad e'=\deg E'.
\tag{2}
$$
因此
$$
\boxed{m_2=(\mathcal B_D-2C)\cdot C=\kappa+e'+2.}
\tag{3}
$$
原 R750 强窗在这里是
$$
h>\kappa,\qquad T_M-h=h-13>\kappa,
$$
所以实际使用时 $h\ge\kappa+14$。后文更强的 $m_2$ 门另行写明，不从这个强窗免费推出。

由 R782，
$$
F(t,0)=\lambda d^c,\qquad
G=F/(\lambda d^c),\qquad G(t,0)=1,
\quad d=1+8t,\ h_7=16t^2+4t+7.
\tag{4}
$$
定义原整个整来源子格
$$
\boxed{
\mathscr D_j=
\{R\in\mathcal W_D:
\widetilde F^{\,j}\mid d^{C_D}R\},
\qquad j=2,3.}
\tag{5}
$$
$\widetilde F$ 是同一个保持全部角值的整提升。
其约化记为 $D_j$。以下证明也明确
$$
D_j=\{R\in\overline{\mathcal W}_D:F^j\mid d^{C_D}R\},
\tag{6}
$$
没有把来源端饱和当物理像饱和。

## 2. 五型 G 的真实 Wb 返回及每个系数帽

对原 $\mathbf F_p$ 的五型，取
$$
\begin{array}{c|ccccc}
A_*&1&t-1&(t-1)^2&h_7&d^2\\ \hline
L_*&t&t&t(t-1)&t&td .
\end{array}
\tag{7}
$$

**定理 1。** 每个 R782 显示格中的 $G$ 都满足
$$
\boxed{L_*G\in\overline{\mathcal W}_b.}
\tag{8}
$$
保持同一固定角的整提升后，同样属于 $\mathcal W_b$。
$L_*$ 恰含一个 $t$，故在原低窗
$$
\operatorname{ord}_tG(t,g)=h
\quad\Longrightarrow\quad
\operatorname{ord}_t(L_*G)(t,g)=h+1.
\tag{9}
$$
这没有使其 Euler 行也有深零。

**证明。** R782 的零角下界为 $-3$，乘 $t$ 后增加四，得到 $1\ge-2$。
其 $h_7$ 角下界不低于 $-2$，无须补；
$t=1$ 只有 $(t-1)^2$ 型可能达到 $-2$，乘一个 $t-1$ 增加三；
$d$ 只有 $d^2$ 型可能达到 $-1$，乘 $d$ 增加二。
其他有限角不受损。
无穷远方面，常数 mask 型的 $v_\infty(G)\ge-1$，
且 $\deg L_*=1$，所以 $v_\infty(L_*G)\ge-3$；
其余型 $v_\infty(G)\ge0$、$\deg L_*\le2$，故下界至少 $-4$。
全部都强于原 $-8$。

逐系数也可直接读取。沿用 R782(19) 的 $r_n,E_n$，
$$
\frac{L_*r_n}{q_n}
=L_*t^{a_n-A_n}h_7^{b_n-A_n}
(t-1)^{c_n-B_n}d^{C_n-z_n}
\in k[t].
\tag{10}
$$
$t$ 指数的唯一损失发生在 $n\equiv3\pmod4$，由 $L_*$ 中的 $t$ 补；
$t-1$ 的唯一损失发生在 $m_1=2,n\equiv2\pmod3$，由表中因子补；
$d$ 的唯一损失发生在 $\delta_d=1,n$ 为奇数，亦由表中因子补。
$h_7$ 指数始终非负。
完整无穷远帽为
$$
\deg(L_*r_np_n)\le\deg L_*+
\left\lfloor\frac{9n+\delta_\infty}{2}\right\rfloor
\le f_n .
\tag{11}
$$
除去 $q_n$ 的准确次数后，正是原 $\le e_{n+1}$ 帽；
常数 charge 为 $L_*$，次数至多二，也在原 $n=0$ 四次帽内。
于是 (8) 保所有原列和十九角。整提升用 R491 的同一角因子与次数保持引理。$\square$

(8) 同样扩展到 R782 的一般系数域、至多十五个 mask。
取 $L_*=t$，仅当下述情形之一出现时再乘一个因子：
$m_1=2$ 乘 $t-1$；$\delta_d=1$ 乘 $d$；
某个分裂 $h_7$ 角有 $m_\alpha=3$ 时乘 $t-\alpha$。
总 mask 次数至多二，保证这些额外需求至多出现一种；
后一种必来自该线性因子的平方，故该角在原系数域中。
有额外因子时 $\delta_\infty=0$。
同一逐角论证给 $L_*G\in\mathcal W_b$，仍只有一个 $t$ 因子。

这个返回可把因子的实际单输出接触交给原格的已付结论。
它不把特征零或辅助素数的连续前缀直接换成目标 $p$ 的单位子式，
也不把 (9) 认成两个 Euler 输出的共同深零。

## 3. 全部 D2/D3 的显示来源，保实际角值

这里必须使用给定 $G$ 的**实际**角亏损，不能用某型的最大上界代替：
$$
\mu_\alpha=-v_\alpha(G)\quad(h_7(\alpha)=0),\qquad
\mu_1=-v_1(G),\qquad
\delta_d=-v_d(G),\qquad\delta_\infty=-v_\infty(G).
\tag{12}
$$
它们非负，满足 R782 的相应限制，且 $v_0(G)=-3$。
对 $j=2,3$、$0\le n\le D-jb$，置
$$
a_{j,n}=\max\left(0,\left\lceil\frac{n-2+3j}{4}\right\rceil\right),
$$
$$
b_{j,\alpha,n}
=\max\left(0,\left\lceil\frac{n-2+j\mu_\alpha}{4}\right\rceil\right),
\qquad
c_{j,n}=\max\left(0,\left\lceil\frac{n-1+j\mu_1}{3}\right\rceil\right),
$$
$$
z_{j,n}=\left\lfloor\frac{n-j\delta_d}{2}\right\rfloor,\qquad
K_{j,n}=\left\lfloor\frac{9n+8-j\delta_\infty}{2}\right\rfloor,
$$
$$
r_{j,n}=t^{a_{j,n}}(t-1)^{c_{j,n}}d^{-z_{j,n}}
\prod_{\varpi\mid h_7}\varpi^{b_{j,\varpi,n}},
\qquad
E_{j,n}=K_{j,n}-\deg_t r_{j,n}.
\tag{13}
$$
不可约二次因子在两个根上用相同指数，$\deg_t r_{j,n}$ 包括负分母次数。

**引理 2。** 原整个 $D_j$ 准确由
$$
\boxed{
G^jY^n r_{j,n}(t)t^v,\qquad
0\le n\le D-jb,\quad0\le v\le E_{j,n}
}
\tag{14}
$$
生成并构成基；负帽组为空。其整提升给 $\mathscr D_j$ 的有限自由呈示，
约化准确为 (6)，且 $\mathscr D_3\subset\mathscr D_2$ 是饱和包含。

**证明。** 写 $R=G^jH$。由 (6)，$H$ 的系数只可有 $d$ 极。
Gauss 乘法把原下界分别变成
$$
v_0(H)\ge-2+3j,\quad
v_\alpha(H)\ge-2+j\mu_\alpha,\quad
v_1(H)\ge-1+j\mu_1,
$$
$$
v_d(H)\ge j\delta_d,\qquad
v_\infty(H)\ge-8+j\delta_\infty.
\tag{15}
$$
逐 charge 解出这些整数条件，正好是 (13)；无穷远余帽给 $E_{j,n}$。
乘回 $G^j$ 后只用原 R491 双向识别，所以无缺列、无免费矩形。

整环中选同一 $\widetilde G=\widetilde F/(\widetilde\lambda d^c)$，
保持全部实际角值及 $Y^0=1$；将 (13) 的固定因子 Hensel 提升。
这给每个约化 multiplier 的实际同帽提升，故 (6) 成立。
若 $pR\in\mathscr D_3$ 且 $R\in\mathscr D_2$，
则 $p$ 与 $\widetilde F$ 互素，约化 $\bar F$ 非零，
所以 $\widetilde F^3\mid d^{C_D}R$，即 $R\in\mathscr D_3$。
有限自由格的商于是无 $p$ 挠。$\square$

在原点，(13) 给关键的全来源前缀
$$
\boxed{
R=G^2H\in D_2\Longrightarrow
H,\mathcal EH,\mathcal E^2H,\ldots\in t\,k[t,Y,d^{-1}],
}
\tag{16}
$$
$$
\boxed{
R=G^3K\in D_3\Longrightarrow
K,\mathcal EK,\ldots\in t^2k[t,Y,d^{-1}].
}
\tag{17}
$$
这对全部实际来源成立，不只针对原 $qt^2$ 子格。
记
$$
d_j=\sum_{n=0}^{D-jb}\max(0,E_{j,n}+1)=\dim D_j.
\tag{18}
$$

## 4. 同一物理展开及短 M 的准确全块

在原光滑支 $Y=\psi(t)$ 上，保同一 logarithmic normal 坐标 $\zeta$：
$$
Y=\psi e^\zeta,\quad
\eta_0=t^hu,\quad u(0)\ne0,\quad
Y_{\rm phys}=\psi e^{\eta+a\epsilon},\quad
\eta=\eta_0+p\xi,\quad a\in\mathcal O^\times.
\tag{19}
$$
令
$$
e=(\mathcal EG)|_C,\qquad f_2=(\mathcal E^2G)|_C,\qquad
H_0=H|_C,\quad H_1=(\mathcal EH)|_C.
$$
$e$ 为单位。对 $R=G^2H$，
$$
R=C_2\zeta^2+C_3\zeta^3+\cdots,
\qquad
\boxed{C_2=e^2H_0,\quad C_3=e^2H_1+ef_2H_0.}
\tag{20}
$$
由 (16)，所有这些系数至少有一个 $t$。

以下采用原已付的共同 Gaussian 上三角单位运输。
它只是将共同 charge 的 $(\mathcal E+c)$ 三行居中成
$1,\mathcal E,\mathcal E^2$；
其在前两条同长度行及第三短行上是完整可逆的原目标变换。
若保未居中的行，相差项为普通行和第一行的固定倍，
下述核条件相同。
保
$$
M=c_*U_0w^{13}J,\qquad N_0=s-13=2h-11.
\tag{21}
$$
$w^{13}$ 只在显示的合法行上读取，未作为全目标单位求逆。

**定理 3。** 原短 $M$ 在整个 $D_2$ 上，逆共同单位后准确只有 first-normal 块
$$
\boxed{
\bar M(G^2H)\ \longleftrightarrow\
\left(0,\ 
2ae^2t^hu\,H_0\bmod t^{N_0},\ 0\right).
}
\tag{22}
$$
所以
$$
\boxed{
\ker\bar M\cap D_2
=\{G^2H\in D_2:\operatorname{ord}_P H_0\ge h-11\}.
}
\tag{23}
$$

**证明。** 普通项至少 $2h+1>N_0$；
第一 Gaussian 项的首项为 $2aC_2t^hu$，
下一项 $3aC_3t^{2h}u^2$ 从 $2h+1>N_0$ 起。
第三块首项为 $a^2C_2$，已有一个 $t$，故在 $\ell=1$ 处为零。
共同 charge 添的项阶更高，或由前行消掉。
(22) 在原 $w^{13}$ 后的两条长度 $N_0$ 中成立；
$f_D<p$、原参数 $t/w$ 单位及完整 $U_0$ 保持这些核。
$2,a,e,u$ 均为单位，得到 (23)。$\square$

$H_0$ 是真实 $H^0(X,\mathcal O_X(\mathcal B_D-2C))$ 的曲线限制，
对应线丛在 $C$ 上次数为 $m_2$。
原点光滑，非零截面不能在该点消失超过线丛次数。
因此
$$
\boxed{
h-11>m_2\quad\Longrightarrow\quad
\ker\bar M\cap D_2=D_3.
}
\tag{24}
$$
$H_0=0$ 等价于再被同一 $F$ 整除，
因为 $C$ 不可约而所有分母在其泛点为单位。
此处无须 $H^1$ 消失、一般位置或普通光滑曲线替代。

在 (24) 下，任选原整饱和直和
$\mathscr D_2=\mathscr D_3\oplus\mathscr L$，
则 $\bar M|_{\bar{\mathscr L}}$ 单射，
所以该真实整限制给出 $d_2-d_3$ 个单位 Smith 因子。
没有令整 $M$ 自动降到 $\mathscr D_2/\mathscr D_3$；
$\mathscr D_3$ 仍有原 $p$ 输出，选补后它与下一位必须继续保留。
也没有将此块与其他已知单位块的秩直接相加。

## 5. 完整 J 的末行及较弱的排除门

相对目标 $J$ 的前两块长度为 $s=2h+2$。
(20) 的第三展开项此时可能落在最后一行，不能沿用 (22) 删去。
完整读取给
$$
\boxed{
\begin{aligned}
\bar J_0(G^2H)
&=e^2t^{2h}u^2H_0\pmod{t^s},\\
\bar J_1(G^2H)
&=a\left\{
2e^2t^huH_0+
3(e^2H_1+ef_2H_0)t^{2h}u^2
\right\}\pmod{t^s},\\
\bar J_2(G^2H)&=0.
\end{aligned}}
\tag{25}
$$
再高项至少 $3h+1>s$，所以 (25) 是全式。

**定理 4。** $G^2H\in D_2$ 属于真正相对首核 $\ker\bar J$，
当且仅当
$$
\boxed{
H_0\in t^{h+1}k[[t]],\qquad
2\alpha+3u_0\beta=0,
}
\tag{26}
$$
其中
$$
H_0=\alpha t^{h+1}+O(t^{h+2}),\qquad
H_1=\beta t+O(t^2),\qquad u_0=u(0).
\tag{27}
$$

**证明。** (25) 第二行中含 $H_1$ 的项最早在 $2h+1=s-1$。
故其在严格小于 $s-1$ 的行首先迫
$H_0\in t^{h+1}$。
这使普通行全零，且 $ef_2H_0$ 那项也超过截止。
在最后一行 $t^{2h+1}$，剩余系数为
$a e(0)^2u_0(2\alpha+3u_0\beta)$。
前因子为单位，得到 (26)。
反向代回 (25) 即得全部三块消失。
在未居中的原行中，此时普通行已为零，
共同 charge 的额外项不改变最后方程。$\square$

由 (17)，全部 $D_3$ 都满足 (26)：此时
$H_0=0$、$H_1=eK|_C\in t^2$。
因此
$$
\boxed{
h+1>m_2
\quad\Longrightarrow\quad
\ker\bar J\cap D_2=D_3.
}
\tag{28}
$$
这个门是
$h>\kappa+e'+1$；
短 $M$ 的 (24) 则是
$h>\kappa+e'+13$。
二者相差十二阶，不能用短 $M$ 删除恢复后的末行。

由原 R449，
$$
K_2^{\rm red}(M)\subset\ker\bar J.
$$
所以在 (28) 的门内，任何属于完整 $F^2$ 整除空间的真实第二核约化，必已属于完整 cube 空间。这不是把整个 $K_1$ 假设为一维，也没有排除全部不含 $F^2$ 的真实余列。

### 两门之间的准确有限尾维数

若
$$
h+1>m_2\ge h-11,
$$
则 (23) 对 $D_3$ 取商后，单射进入
$$
H^0\!\left(C,
\mathcal O_C(\mathcal B_D-2C)(-(h-11)P)\right).
$$
其次数为 $m_2-h+11$，故
$$
\boxed{
\dim\frac{\ker\bar M\cap D_2}{D_3}
\le \max(0,m_2-h+12)\le12.
}
\tag{29}
$$
所用初等界 $h^0(L)\le\deg L+1$ 对 integral 曲线同样成立：
在归一化拉回后，用依次消去光滑点的值或非零截面的零除子证明即可。

这些方向在原 $J$ 中只可能占 first-normal 块的
$$
t^{N_0},\ldots,t^{s-1},
$$
共十三个真实 carry 位置；其实际像秩至多十二。
在 (28) 下，该 carry 映射在 (29) 的真实商上单射。
不能将这十三个位置当成可独立填写的自由目标。

## 6. 原 scalar-projection 尾的完整全 F² 矩阵

回到 R782 的同一整来源
$$
P_\Delta=t^2(q-q(t,0))F^3.
$$
按 (4) 写
$$
P_\Delta=t^2\widetilde q_\Delta G^3,\qquad
\widetilde q_\Delta=\lambda^3d^{3c}(q-q(t,0)).
\tag{30}
$$
其全部系数被 $t$ 整除。
R782(35)、(36) 的准确全首 Bockstein 在当前 $G$ frame 中为
$$
\widehat\beta_0=0,\qquad
\widehat\beta_1
=e^3\widetilde q_{\Delta,C}\,t^hu
\left(b_su^2+6at^2\xi\right)\pmod{t^{N_0}},
\qquad \beta^{(2)}=0.
\tag{31}
$$
此处 $t^s=p\epsilon b_s$，所有原 $\xi$ 与 $b_s$ 高尾保持，未作自由选择。

用 (13) 的**全部** $j=2$ 真实 multiplier 列定义
$$
\mathsf T_2(i;(n,v))
=[t^i]\bigl(\psi(t)^n r_{2,n}(t)t^v\bigr),
$$
$$
0\le i<h-11,\quad
0\le n\le D-2b,\quad0\le v\le E_{2,n}.
\tag{32}
$$
令实际右端
$$
\boxed{
\mathfrak f_\Delta(t)=
-\frac{e\,\widetilde q_{\Delta,C}}{2a}
\left(b_su^2+6at^2\xi\right)
\pmod{t^{h-11}}.
}
\tag{33}
$$
它属于 $t\,k[t]/t^{h-11}$，与全 $H$ 的真实零角前缀一致。

由 (22)、(31)，准确有
$$
\boxed{
\exists R_\Delta\in D_2:
\bar M R_\Delta=-\beta_M(P_\Delta)
\ \Longleftrightarrow\
\mathfrak f_\Delta\in\operatorname{im}\mathsf T_2.
}
\tag{34}
$$
这给出了指定尾对完整 $F^2$ 块的实际检验：
(32) 含所有原允许列，(33) 是同一物理高尾，
不是先选一个环境 section 再假定有原像。
在 (24) 下，一个解的曲线限制唯一；
所有真实来源解只差 $D_3$。
在较弱的 (28) 下，应继续保 (29) 及最后条件 (26)，不能把两者混同。

(34) 若成立，可明确用这个 $R_\Delta$ 比较
$P^{\rm fact}+pR$ 与 scalar projection 的首次提升。
但已固定的 $P_2$ 不会因此自动不变；
下一精度必须计算同一个 $R$ 的实际运输，
且所差的 cube 方向仍须保留 R755 的完整首 Bockstein。
本文没有从 (34) 的表达式推出其成员性，更没有将全 $\mathcal W_D$ 的其余列排除。

## 7. 完成范围与接续

本篇增加了三个全来源事实：有限因子型的零增 charge 返回 (8)，
原全部 $F^2$ 来源的显示基 (14)，以及保最后真实 carry 的核识别 (26)–(29)。
它们可在原平衡窗中使用准确的 $e'$ 判断，
但 $e'=O(b)$ 只能在已经付清的平衡假设下使用；
不能把渐近式替代有限门。

接续仍是指定 (33) 在 (32) 中的实际像，以及完整 $\mathcal W_D$
中不含 $F^2$ 的余列同一个 $R$ 联立。
特别 R765 的指定首次修正本来就必须有非零曲线限制，
所以不能只解决本篇的齐次 $F^2$ 块就声称原 forcing 非零。
原三条完整中央、$P_{134}/U_0$、两条十三行和 $p^3$ 全部保持原范围。

依赖：
[R782](R782-original-r2-five-profile-factor-and-inhomogeneous-contact-gate.md)；
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R755](R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R771](R771-original-r2-full-fiber-and-complete-boundary-compensation.md)。
