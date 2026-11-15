# R651 — 原高临界支的同格整提升与完整第二 forcing

日期：2026-11-15。**状态：已证明。**

本篇统一处理原首核中 $1\le r\le\nu\le13$ 的有限临界退化，特别包括 R577/R597 未统一覆盖的 $\nu=3,\ldots,13$。不预设 Euler 临界曲线是普通结点，也不先将它拆成独立分支：用同一 $\mathcal W_D$ 中的真实相邻权列，同时解临界值与两个 Euler jet 的整条件，再用强 $t$-Hensel 取得原近支。

所得基准满足 $A,B\in t^\nu$、$B/t^\nu$ 为单位，并使 $\xi$ 足够深。全文保留同一个 $R$ 的两条十三行及完整 $p^3$ 式；尤其当 $\nu\ge7$ 时，$\frac12\mathscr S(\eta_0^2R_2)$ 可能落入可见第二 forcing，不能借用旧 $\nu\le2$ 的删项。

结果支付实际提升和完整像判据，不证明所指定的余类非零。R637 的旧小预算 Padé 高尾和主目标仍开。

## 1. 原对象与显示范围

保原模型
$$
p=6s-1>101,\quad \ell\in\{1,2\},\quad
n_0=s-13,\quad f_D=\lfloor9D/2\rfloor+4<p,
$$
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad \mathcal E=Y\partial_Y,\quad d=1+8t,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
A_n=\lfloor(n+1)/4\rfloor,\ 
B_n=\lfloor(n+1)/3\rfloor,\ C_n=\lfloor n/2\rfloor,
$$
$$
h_7=7+4t+16t^2,\qquad b_n=A_n+e_{n+1}.
\tag{1}
$$
$\mathcal O$ 为原有限非分歧系数环，$k$ 为剩余域。
原 $t=-w+O(w^2)$、$g(0)=1$、$a=p\kappa\in\mathcal O^\times$，
以及 $P_{134}/U_0$、charge 四十和 $M=c_*U_0m_{13}J$ 不变。

取同一个非零原首核
$$
\bar P\in\ker\bar J,\qquad
r=\operatorname{ord}_t(d^{C_D}\bar P),\qquad
\nu=\operatorname{ord}_t
(\mathcal E^2\bar P)(t,\bar g(t)).
\tag{2}
$$
本文的准确范围为
$$
\boxed{
1\le r\le\nu\le13,\quad \ell\le\nu,\quad D\ge2,
\quad s>\max(3\nu+\ell,\nu+13),
}
\tag{3}
$$
$$
\boxed{
b_{D-2}\ge\nu-1,\qquad b_D\ge2\nu-r+\ell.
}
\tag{4}
$$
(4) 是原来源帽的充分条件，不把大矩形里的列当作原列。

置
$$
m=\nu-r,\qquad M_*=m+\ell+1,\qquad T_*=\nu+M_*.
\tag{5}
$$
由 (3)，$T_*<s$。所有用于初始构造的 $g$ 系数都在原已付的整低窗中。以下使用 $g(t)$ 表示原整逆参数 $w(t)$ 下的同一个 regularized 轴。

## 2. 同一个原 P 的有限整条件

固定
$$
\psi_0(t)=\pi_{T_*}^t g(t)\in\mathcal O[t],\qquad\psi_0(0)=1.
$$
在全局 $t^r$ 含量子格 $\mathcal W_D^{(r)}$ 中施加三个同时条件
$$
\boxed{
P(t,\psi_0)\in t^\nu,\qquad
\mathcal EP(t,\psi_0)\in t^{T_*},\qquad
\mathcal E^2P(t,\psi_0)\in t^\nu.
}
\tag{6}
$$
它们是固定 $\psi_0$ 上的整线性条件。原 $\bar P$ 已满足其约化：前两原 Gaussian 行消到 $s$，第二 Euler 行的阶准确为 $\nu$，且 $T_*<s$。

**引理 1。** 条件 (6) 的完整有限行映射在原 $\mathcal W_D^{(r)}$ 上整满射；可取只用原基列的整右逆。

**证明。** 令 $\rho(R)=\min\{n:b_n\ge R\}$。原 $b_n$ 严格递增，且 $b_n\ge n$。对每个 $r\le R<\nu$，选
$$
n=\rho(R),\ n+1,\ n+2,\qquad
Y^{n+i}q_{n+i}(t)t^{R-A_{n+i}}\quad(i=0,1,2).
\tag{7}
$$
由 $b_{D-2}\ge\nu-1$，三个权均不超过 $D$；
又 $A_{n+i}\le R$，所以自由幂非负并不超过原 $e_{n+i+1}$。
后一个不等式可由 $n\le R$、$A_{n+2}\le\lfloor(R+3)/4\rfloor\le R$ 直接核定，$R\ge1$。这些列的全局 $t$ 阶恰为 $R\ge r$。

在同阶的三个行 $P,\mathcal EP,\mathcal E^2P$ 上，
其首块是三权的 $1,n,n^2$ Vandermonde，乘以原单位
$\chi_n=7^{A_n}(-1)^{B_n}$。
相邻三个权的行列式为 $2$ 乘单位；$D<p$ 保全部使用合法。

对每个 $\nu\le R<T_*$，仅有 $\mathcal EP$ 一条新行。
选正权 $n=\max(1,\rho(R))$ 的原列
$Y^nq_nt^{R-A_n}$。
(4) 给 $b_D\ge T_*-1$，所以该列存在，首系数 $n\chi_n$ 是单位。
所有所选列按 $R$ 递增为块下三角矩阵。
此前列产生的高系数作为真实右端逐阶消去，得到完整整右逆。证毕。

选择原 $\bar P$ 的任意同含量整提升 $P^{\rm base}$。
(6) 的缺陷全部在 $p\mathcal O$ 中，故用引理 1 的右逆减去
$p\mathcal W_D^{(r)}$ 中的一条实际修正，得到
$$
\boxed{
P^{\rm crit}\in\mathcal W_D^{(r)},\quad
P^{\rm crit}\bmod p=\bar P,\quad
P^{\rm crit}\text{ 同时满足 (6)}.
}
\tag{8}
$$
全过程只使用原 $q_n$ 及原自由幂帽，因而十九角、无穷帽和固定分母同时保留。整提升不依赖其它临界分支的分类。

## 3. 真实近支、临界值和足够深的 xi

令
$$
H(t,Y)=d^{C_D}t^{-r}\mathcal EP^{\rm crit}\in\mathcal O[t,Y].
$$
(6) 与原第二 Euler 首系数给
$$
H(t,\psi_0)\in t^{m+M_*},\qquad
H_Y(t,\psi_0)=t^m u(t),\quad u(0)\in\mathcal O^\times.
\tag{9}
$$
因为 $M_*>m$，强 $t$-Hensel 的 Newton 递推整成立：每一步除去的
$t^m$ 已由误差阶支付，其余导数因子为单位。
故存在唯一处于该近球内的
$$
\boxed{
\psi\in\mathcal O[[t]],\qquad
\psi-\psi_0\in t^{M_*},\qquad
\mathcal EP^{\rm crit}(t,\psi)=0.
}
\tag{10}
$$
这是原系数环里的指定近支，不假定其它分支为非垂直或分裂。

模 $p$ 时，原 $H(t,\bar g)$ 消到 $s-r$，
其导数阶为 $m$，且 $s-r>2m$。
同一强 Hensel 根满足
$$
\bar\psi-\bar g\in t^{s-\nu}.
\tag{11}
$$
它与 (10) 的约化相同，因为二者都在同一个
$t^{m+1}$ 近球内。没有使用首共振以后的原 ODE 来延长 (11)。

在同一 $w$ 中定义
$$
A=P^{\rm crit}|_\psi,\qquad
B=\mathcal E^2P^{\rm crit}|_\psi,\qquad
C=\mathcal E^3P^{\rm crit}|_\psi .
$$
由 (6)、(10) 和全部更高 Euler 值的全局 $t^r$ 因子，
$$
\boxed{
A\in w^\nu\mathcal O[[w]],\quad
B=w^\nu b,\ b(0)\in\mathcal O^\times,\quad
C\in w^r\mathcal O[[w]].
}
\tag{12}
$$
例如把 $\psi_0$ 换成 $\psi$ 时，第二 Euler 值的改变量至少从
$r+M_*=\nu+\ell+1$ 起，不改变 $B$ 的单位首系数。
临界值的同样比较保持 $A\in w^\nu$。

在原 R481 有限窗口内，准确写
$$
\eta=\log(g/\psi)=\eta_0+p\xi,\qquad
\boxed{\eta_0\in w^{s-\nu}\mathcal O[w],\quad
\xi\in w^{M_*}\mathcal O[[w]].}
\tag{13}
$$
(10) 及 $\psi_0-g\in t^{T_*}$ 先给 $\eta\in w^{M_*}$；
选 $\eta_0$ 的同一约化代表再用 (11)，得到 (13)。
原第一块还给
$$
\bar A\in w^s k[[w]].
\tag{14}
$$
因为临界值的首误差 $B\eta_0^2/2$ 从 $2s-\nu>s$ 起。

整个原轴上的第二 Euler 值整满足
$$
(\mathcal E^2P^{\rm crit})(t,g)\in w^\nu\mathcal O[[w]].
\tag{15}
$$
事实上，$B$ 的阶为 $\nu$，而 $C\eta$ 的阶至少
$r+M_*>\nu$；更高项也更深。因此原第三低块中该直接项整消失。

由于 $\nu\le13$，$s-\nu\ge n_0$，而 $\pi_{n_0}$ 只读取严格低于 $n_0$ 的项。
所以对**整个同一** $\mathcal W_D$，可见首像准确是
$$
\boxed{
\bar J_A(R)=\mathcal T_\psi(\bar R):=
(\pi_{n_0}R_0,\ a\pi_{n_0}R_1,\ a^2\pi_\ell R_2/2),
\quad R_i=(\mathcal E^iR)|_\psi .
}
\tag{16}
$$
这正是上界十三的用途；不把它外推到 $\nu\ge14$。

## 4. 全来源低行右逆与第一次指定像

以下的 $\mathscr S$ 始终是原 $w$ 中的 $s$ 阶 carry：
$$
\mathscr S(\sum a_jw^j)=\sum_{j\ge s}a_jw^{j-s}.
$$
先作用 $\mathscr S$，再用同一个 $w(t)$ 换参，不能先在来源中除 $t^s$。

由 (12)–(15)，原首次可见 forcing 为
$$
\boxed{
\mathcal F_P=
\left(
\overline{\pi_{n_0}A/p},\
\pi_{n_0}\overline{aB\xi+\mathscr SA},\
a\pi_\ell\overline{\mathscr S(B\eta_0)}
\right).
}
\tag{17}
$$
第一项只在 (14) 保证整除的截断内除 $p$。

同一帽 $b_{D-2}\ge\nu-1$ 还付清完整低行映射
$$
\mathcal L_{\nu,\ell}(R)=
(R_0\bmod t^\nu,\ R_1\bmod t^\nu,\ R_2\bmod t^\ell).
\tag{18}
$$
逐 $t$ 阶 $0\le R<\nu$ 用 (7) 的三个相邻权即可；
$R=0$ 时准确用 $n=0,1,2$，三列均存在。
先得到到三个完整 $\nu$-jet 的整同构块，再投影第三块至 $\ell$。

因此 (18) 有显示的全来源整右逆。
若 $\mathcal B_\nu$ 为所选 $3\nu$ 条原列的自由跨度，
对其余每条原基列减去 $\mathcal B_\nu$ 中相同三个低 $\nu$-jet 的唯一原像；
再加回 $\mathcal B_\nu$ 中第三块 $t^\ell,\ldots,t^{\nu-1}$ 的唯一原像，
就得到
$$
\boxed{\mathcal K_{\nu,\ell}:=\ker\mathcal L_{\nu,\ell}}
\tag{19}
$$
的完整整基。故所有原剩余列及额外第三边界都被包括，来源商秩准确为 $2\nu+\ell$。

置
$$
\alpha=\mathscr SA\bmod t^\nu,\qquad
\beta=\mathscr S(B\eta_0)\bmod t^\ell,
$$
这里均按上述原换参读取。用整右逆选择同一
$R_{\rm bd}\in\mathcal W_D$，使
$$
(R_{\rm bd})_0=0\bmod t^\nu,\quad
(R_{\rm bd})_1=-\alpha/a\bmod t^\nu,\quad
(R_{\rm bd})_2=-2\beta/a\bmod t^\ell.
\tag{20}
$$
可将第三块未指定的 $\nu-\ell$ 条行取零。
(20) 在 $\mathcal O$ 中准确成立，不仅模 $p$。

令
$$
\mathcal D_\psi:\mathcal K_{\nu,\ell}\longrightarrow
(\mathcal O[t]/t^{n_0-\nu})^2,\qquad
S\longmapsto(t^{-\nu}S_0,t^{-\nu}S_1).
\tag{21}
$$
这两个除法由 (19) 真正保证，不是免费除来源。
把 (17) 前两项除去第二行的单位 $a$，改写为 $t$-jet，记为 $f_0,f_1$。
则
$$
\boxed{
\mathcal G_P=
-\left(t^{-\nu}(f_0+\bar R_{{\rm bd},0}),\
t^{-\nu}(f_1+\bar R_{{\rm bd},1})\right)
\bmod t^{n_0-\nu}.
}
\tag{22}
$$
低 $\nu$ 阶恰由 (20) 消掉。

**定理 1。** 原 $M(P^{\rm crit}+pR)\in p^2$ 可解，当且仅当
$$
\boxed{\mathcal G_P\in\operatorname{im}\bar{\mathcal D}_\psi.}
\tag{23}
$$
可将同一个修正整取为
$$
R=R_{\rm bd}+S,\qquad S\in\mathcal K_{\nu,\ell}.
\tag{24}
$$
任何原模 $p$ 解均可如此整提升；不同提升差是 $p\mathcal W_D$，由后续同一 $p^2$ 修正支付。证明即 (16)–(22) 的完整消元，不拆开两个高 jet 或漏掉其余原列。

## 5. 同一个 R 的完整三块至 p³

以下固定 (24) 的同一个整 $R$，并写 $R_i=(\mathcal E^iR)|_\psi$。原三块恒等式为
$$
J(P)=\left(\pi_sP_0,\
\pi_s(aP_1+p\mathscr SP_0),\
\pi_\ell(a^2P_2/2+pa\mathscr SP_1+p^2\mathscr S^2P_0)\right).
\tag{25}
$$

由 (12)–(15)，
$$
J_0(P^{\rm crit})
=\pi_s(A+p^2B\xi^2/2),
$$
$$
\begin{aligned}
J_1(P^{\rm crit})={}&p\pi_s
(aB\xi+\mathscr SA+\mathscr S(B\eta_0^2)/2)\\
&+p^2\pi_s
(aC\xi^2/2+\mathscr S(B\eta_0\xi)
+\mathscr S(C\eta_0^2\xi)/2),\\
J_2(P^{\rm crit})={}&pa\pi_\ell\mathscr S(B\eta_0)\\
&+p^2\pi_\ell
(a\mathscr S(B\xi)+\mathscr S^2A+\mathscr S^2(B\eta_0^2)/2)
\pmod{p^3}.
\end{aligned}
\tag{26}
$$

对任意同源 $R$，所需的完整模 $p^2$ 式为
$$
\begin{aligned}
J_0(R)={}&\pi_s(R_0+\eta_0R_1)
+p\pi_s(\xi R_1+\eta_0\xi R_2),\\
J_1(R)={}&a\pi_s(R_1+\eta_0R_2)\\
&+p\pi_s\{a\xi R_2+a\eta_0\xi R_3+
\mathscr S(R_0+\eta_0R_1+\eta_0^2R_2/2)\},\\
J_2(R)={}&a^2\pi_\ell R_2/2+
pa\pi_\ell\mathscr S(R_1+\eta_0R_2)
\pmod{p^2}.
\end{aligned}
\tag{27}
$$

为核删项，$\operatorname{ord}\eta_0=s-\nu$、
$\operatorname{ord}\xi=M_*=m+\ell+1$，
且全部 $\mathcal E^iP^{\rm crit}$ 有全局 $w^r$ 因子。
含三个 $\eta_0$ 的项即使作两次 carry，也从
$s-3\nu+r>\ell$ 起；对任意 $R$ 的一次 carry 同样由 $s>3\nu+\ell$ 排除。
$\mathscr S(C\eta_0\xi)$ 从 $M_*-m=\ell+1$ 起，故不进第三短块。
但 $\eta_0\xi R_2$ 和 $a\eta_0\xi R_3$ 可落入最后十三行，
在 (27) 中必须保留。

更重要的是
$$
\operatorname{ord}\mathscr S(\eta_0^2R_2)\ge s-2\nu.
\tag{28}
$$
当 $\nu\ge7$ 时，这个阶可小于 $s-13=n_0$。
因此 (27) 的该项可能真正进入 $J_A$ 第二位；
本文没有将旧 $\nu\le2$ 的边界删项搬过来。

## 6. 两条十三行与准确第二类

定义完整普通续段
$$
\boxed{
Z^+=R_1+B\xi+a^{-1}\mathscr SA+\eta_0R_2+
(2a)^{-1}\mathscr S(B\eta_0^2).
}
\tag{29}
$$
它在所需的整个有限窗口内整，所有项来自同一个 $P^{\rm crit},R$。

令
$$
Y^+=\pi_sA/p+\pi_s(R_0+\eta_0R_1)\in\mathcal O[w]/w^s,
$$
$$
H_0=\pi_s(B\xi^2/2+\xi R_1+\eta_0\xi R_2),
$$
$$
\begin{aligned}
H_1=\pi_s\{&
aC\xi^2/2+\mathscr S(B\eta_0\xi)+
\mathscr S(C\eta_0^2\xi)/2\\
&+a\xi R_2+a\eta_0\xi R_3+
\mathscr S(R_0+\eta_0R_1+\eta_0^2R_2/2)\}.
\end{aligned}
\tag{30}
$$
$Y^+$ 的 $\pi_sA/p$ 只在 (14) 已整除的范围定义。
由 (20)、(24)，
$$
\pi_\ell(a\mathscr S(B\eta_0)+a^2R_2/2)=0
\quad\text{在 }\mathcal O\text{ 中准确成立}.
\tag{31}
$$
于是 (26)–(27) 化为
$$
\boxed{
\begin{aligned}
J_0(P^{\rm crit}+pR)&=pY^++p^2H_0,\\
J_1(P^{\rm crit}+pR)&=pa\,\pi_sZ^++p^2H_1,\\
J_2(P^{\rm crit}+pR)&=p^2a\,\pi_\ell\mathscr SZ^+
\pmod{p^3}.
\end{aligned}}
\tag{32}
$$
第三式的抵消是完整恒等：
$a\mathscr S Z^+$ 展开后，
$\mathscr S^2A$ 与 $\mathscr S^2(B\eta_0^2)/2$
正是 (26)–(27) 的对应项。没有单独选择第三尾的修正。

假设 (23) 已通过。按原 R479 表示
$M=(J_A,pJ_B)^t$ 加十三自由零行，
第二次提升首先要求两条 $B$ 带同时为零：
$$
\boxed{
\bar Y^+=0,\qquad \pi_s\bar Z^+=0.
}
\tag{33}
$$
(23) 已支付其中前 $n_0$ 行；(33) 新要求的恰是各自最后十三行。
它准确等价于同一个 $J(P^{\rm crit}+pR)\in p^2$；
第三块已经由 (31)–(32) 付清。

只有通过 (33) 后，下式中的除 $p$ 才全部合法：
$$
\boxed{
\Psi_R=
\left(
\pi_{n_0}\overline{Y^+/p+H_0},\
\pi_{n_0}\overline{aZ^+/p+H_1},\
a\pi_\ell\overline{\mathscr SZ^+}
\right).
}
\tag{34}
$$
$Z^+/p$ 只在 $\pi_s$ 后读取，$\mathscr SZ^+$ 则必须读取原完整续段，
不能先将 $Z^+$ 截成 $\pi_s Z^+$。

**定理 2。** 对 (24) 中固定的同一个 $R$，
存在原 $T\in\mathcal W_D$ 使
$$
M(P^{\rm crit}+pR+p^2T)\in p^3
$$
当且仅当 (33) 成立且
$$
\boxed{\Psi_R\in\operatorname{im}\bar{\mathcal T}_\psi.}
\tag{35}
$$
符号取负即可选消去用的 $T$。

证明：两条 $pJ_B$ 行除 $p^2$ 后的值不能由 $p^2M(T)$ 改动，
故必须是 (33)；通过后，其下一要求已是 $p^3$。
剩余 $J_A$ 的除 $p^2$ 值正为 (34)，而 $p^2J_A(T)$
只读取 (16) 的同一个原像。这给充要性。
原 $c_*U_0$ 的完整整单位运输、十三自由行和两条十三行均在原分解内，
没有改变 $M$ 或另造第二余核。

## 7. 已付内容与仍未付的指定类

本篇新增的是：全部显示范围的同一个原核向量都有原帽内的整临界基准；
不必假定高临界奇点为普通结点；
低行右逆包括全剩余来源；$\nu\ge7$ 的新活项及所有十三行 carry
均进入同一个 (32)–(35)。

原首次问题仍是 (23) 的真实像问题，第二次问题仍是同一个 $R$
上的 (33)、(35)。这些式子没有证明相应指定类非零，
没有把规范选深当成新左核，也没有发现此前未确认的实际双侧缺陷纤维。
R637 继续原小预算 Padé 高尾；原两条或三条完整中央
没有被传播给这些修正列或其乘积。


依赖：原低临界基准见 [R577](R577-original-critical-factor-euler-lift-and-complete-first-forcing.md)、[R597](R597-original-nodal-critical-lift-and-complete-low-ell-second-class.md)；完整 carry 分解及同修正第三精度见 [R479](R479-original-carry-graph-and-two-normal-jets.md)、[R481](R481-full-third-precision-normal-form-and-common-correction.md)；同一 $Z^+$ 的低 $\nu$ 接口见 [R593](R593-original-critical-carry-completion-and-actual-second-normal-tail.md)。本文对高 $\nu$ 重新支付全部整构造及删项范围。
