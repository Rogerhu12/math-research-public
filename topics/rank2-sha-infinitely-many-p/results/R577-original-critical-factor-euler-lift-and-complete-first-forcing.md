# R577 — 原临界因子的 Euler 整提升与完整首次 forcing

日期：2026-11-14。**状态：已证明。**
本篇处理低 $\ell$ 一般核中的简单临界支：
$$
\ell\in\{1,2\},\qquad
\bar P\in\ker\bar J,\qquad
r=\operatorname{ord}_t(d^{C_D}\bar P)
=\operatorname{ord}_w(\mathcal E^2\bar P)(t(w),\bar g(w))
\in\{\ell,\ldots,2\}.
$$
它不要求 $\bar P$ 是全局平方或立方。

先对同一个实际来源 $\mathcal E\bar P$ 作 R491 的全十九角因子整提升，
再在原正权分量上用单位 $1/n$ 积分，得到真正属于同一
$\mathcal W_D$ 的 $P^{\rm crit}$。它的完整整临界支上有
$\mathcal E P^{\rm crit}=0$。原 $M$ 的全部可见首像随后准确等于
该支上的三法向 jet，首 forcing 的三个分量均由原 $A,B,\xi$
及真正 $s$ 阶 carry 给出。

正文还给此基准的完整 $p^3$ 三块式，保留落在最后一至两条
carry 行中的二次项，并把同一个修正 $R$ 送到原 $d_2$。
这些是实际整来源和原矩阵的结论；尚未证明该 forcing 类非零，
也未给任一新因子赋予中央零。主目标未完成。

## 1. 同一来源与准确范围

保 R491、R481、R449 的原对象
$$
p=6s-1>101,\qquad
1\le\ell\le2,\qquad \ell<s-13,\qquad
f_D=\lfloor9D/2\rfloor+4<p,
$$
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},\qquad
\mathcal E=Y\partial_Y,\qquad d=1+8t.
\tag{1}
$$
$\mathcal O/\mathbf Z_p$ 可为原有限非分歧系数扩张。
所有 $q_n$、次数帽、角点和 $P_{134}$ 都不变。
尤其 $D<p$。

原实际评价是
$$
Y_{\rm phys}=g(w)e_2(a\epsilon),\qquad
a=p\kappa_{\rm Gau}\in\mathcal O^\times,\qquad
w^s=p\epsilon,\quad \epsilon^3=0,\quad w^\ell\epsilon^2=0.
$$
原物理矩阵仍为
$$
M=c_*U_0m_{13}J.
\tag{2}
$$
用整个 $(c_*U_0)^{-1}$ 运输目标后，R449 的准确表示是
$M=(J_A,pJ_B)^t$ 加十三条自由零行；
$B$ 仍是相对第一、第二块的各末十三行。
记
$$
n_0=s-13.
$$
$A$ 因而只读取前两块 $<n_0$ 及第三块 $<\ell$。
这不是删除 carry；第 6 节保其实际下一位。

设非零 $\bar P\in\ker\bar J$，并清原固定分母：
$$
d^{C_D}\bar P=t^rF(t,Y),\qquad t\nmid F.
\tag{3}
$$
本篇的准确假设为
$$
\boxed{
r=\nu\le2,\qquad \nu=
\operatorname{ord}_w(\mathcal E^2\bar P)(t(w),\bar g(w)),
\qquad r\ge\ell.
}
\tag{4}
$$
相对首核还给 $P_0,P_1\in w^s k[[w]]$。
于是
$$
F(0,1)=F_Y(0,1)=0,\qquad F_{YY}(0,1)\ne0.
\tag{5}
$$
反过来，(3)、相对首核和 (5) 正给 (4) 中的二次阶条件。
本篇不包含低 ell 笔记中 $r=1,\nu=2$ 的非单位临界支；
那里额外外支不能免费抹去。

## 2. 同一 P 的真实临界因子提升

在 $k[t,Y]$ 中分解
$$
F_Y=GQ,\qquad
G(0,1)=0,\quad G_Y(0,1)Q(0,1)\ne0,
\tag{6}
$$
其中 $G$ 为包含此简单根的不可约因子。
由 (3)，同一个实际 Euler 来源满足
$$
d^{C_D}\mathcal E\bar P=t^rY GQ.
\tag{7}
$$

**定理 1。** 可选择保持全部原角与次数的整提升
$\widetilde G,\widetilde Q$，并构造 $P^{\rm crit}\in\mathcal W_D$，
使
$$
\boxed{
P^{\rm crit}\bmod p=\bar P,\qquad
\mathcal E P^{\rm crit}
=d^{-C_D}t^rY\widetilde G\widetilde Q.
}
\tag{8}
$$
$P^{\rm crit}$ 还逐系数被 $t^r$ 整除。

**证明。**
$\mathcal E\bar P$ 本来就在同一个来源格；
$\mathcal E$ 只在第 $n$ 权乘以 $n$。
对 (7) 应用 R491 §2 的一般乘积分解提升，
保持固定因子 $t^r$ 和 $Y$ 不变。
该引理逐系数同时保持 $0,h_7$ 两根、$1$、$d=0$
的全部 Gauss 阶及无穷远斜次数，
因而支付同一十九角模型的全部中间条件。
角因子之间的判别式和结果式只需排 $2,3,7$，
当前范围已覆盖；所用 monic Hensel 因子及首系数均为单位。
所得
$$
P_E=d^{-C_D}t^rY\widetilde G\widetilde Q
$$
准确属于 $\mathcal W_D$，且只含正 $Y$ 权。

在原显示基上，
$$
\mathcal E^{-1}
\left(\sum_{n=1}^D Y^nq_nB_n\right)
=\sum_{n=1}^D\frac1nY^nq_nB_n .
\tag{9}
$$
因 $1\le n\le D<p$，每个 $1/n$ 是整单位。
(9) 不改任何角整除阶、次数帽或 $t^r$ 含量。
它把 $P_E$ 积分为 $\bar P$ 的全部正权分量的实际整提升。

最后在第零权加入原 $\bar P$ 的同一常权分量的整提升，
保持其 $t^r$ 含量及原次数帽 $e_1=4$。
其 Euler 导数为零，所以 (8) 仍成立。
这完成同一个 $\bar P$ 的提升，而不是另给 $\mathcal E\bar P$
选一个无法积分回原格的基准。证毕。

(9) 证明的是来源上的整可逆性，没有推出物理像 $p$-饱和。
因子提升也可依赖 $p$，未给与 $p$ 无关的新高度界。

由 (6)，$\widetilde G=0$ 有唯一整分支
$$
Y=\widetilde\psi(t),\qquad \widetilde\psi(0)\equiv1\pmod p.
$$
它在原有限非分歧系数环的形式级数中，
且 $\widetilde G_Y(t,\widetilde\psi)$、$\widetilde Q(t,\widetilde\psi)$
均为原点单位。
定义实际完整函数
$$
A(w)=P^{\rm crit}(t(w),\widetilde\psi(t(w))),
$$
$$
B(w)=(\mathcal E^2P^{\rm crit})(t(w),\widetilde\psi(t(w))),
\qquad
C(w)=(\mathcal E^3P^{\rm crit})(t(w),\widetilde\psi(t(w))).
\tag{10}
$$
因此
$$
\boxed{
\mathcal E P^{\rm crit}|_{\widetilde\psi}=0,\qquad
B=t(w)^r b(w),\quad b(0)\in\mathcal O^\times,\qquad
C\in t(w)^r\mathcal O[[w]].
}
\tag{11}
$$
$A$ 是临界值，不被设为零。

## 3. 接触长度与整个原首像的代数支识别

只在 R481 已付的原有限普通系数窗口内写
$$
\eta(w)=\log\frac{g(w)}{\widetilde\psi(t(w))}
=\eta_0(w)+p\xi(w),
\qquad \eta_0\equiv\eta\pmod p.
\tag{12}
$$
取 $\eta_0$ 为整多项式代表，保持其模 $p$ 的初始零段；
$\xi$ 保原所需的全部两位系数。
形式 log 的常数在 $p\mathcal O$ 中；
有限窗口内的非恒常分母均小于 $p$，由原整轴规范保证整性。
不在未付的无限长 raw sigma 环中使用 (12)。

在模 $p$ 的临界支展开中，
$$
(\mathcal EP^{\rm crit})(t,\bar g)
=B\,\bar\eta+O(t^r\bar\eta^2).
$$
因 $B/t^r$ 为单位，原相对首核给
$$
\boxed{
\operatorname{ord}\bar\eta\ge s-r,\qquad
\eta_0\in w^{s-r}\mathcal O[w],\qquad
\bar A\in w^s k[[w]].
}
\tag{13}
$$
最后一项由
$P^{\rm crit}(t,g)=A+\frac12B\eta^2+\cdots$ 得到：
模 $p$ 时二次项从 $2s-r>s$ 开始。
若接触更高或在该窗口内全零，(13) 仍原样适用。

对原任意修正列 $R\in\mathcal W_D$，
$\bar g-\bar\psi$ 的阶至少是 $s-r>n_0$，
故全部可见首行准确满足
$$
\boxed{
\bar J_A(R)=\mathcal T_\psi(R):=
\left(
\pi_{n_0}R|_\psi,\quad
a\pi_{n_0}\mathcal ER|_\psi,\quad
\frac{a^2}{2}\pi_\ell\mathcal E^2R|_\psi
\right).
}
\tag{14}
$$
$\pi_m$ 表示原 $w$ 次数 $<m$。
第三项也合法，因为 $s-r>\ell$。
这是对**整个同一 $\mathcal W_D$** 的矩阵等式；
没有将来源换成临界曲线上的任意截面。
完整目标的 $c_*U_0$ 在 (14) 后按 (2) 放回。

## 4. 原完整首 forcing 的三个分量

令 $\mathscr S$ 为 R481 的真正 $s$ 阶移位
$$
\mathscr S\left(\sum c_jw^j\right)=\sum_{j\ge s}c_jw^{j-s}.
$$
它先作用于原完整普通系数，不能解释为在来源中免费除 $w^s$。

**定理 2。** 取定 (8) 的实际基准。原首次提升的可见 forcing 为
$$
\boxed{
\mathcal F_P=
\left(
\overline{\frac{\pi_{n_0}A}{p}},\
\pi_{n_0}\overline{aB\xi+\mathscr S A},\
a\pi_\ell\overline{\mathscr S(B\eta_0)}
\right).
}
\tag{15}
$$
第一项的除 $p$ 在截断后整除，见 (13)。
对同一实际 $R\in\mathcal W_D$，
$$
M(P^{\rm crit}+pR)\in p^2
\quad\Longleftrightarrow\quad
\boxed{\mathcal T_\psi(\bar R)=-\mathcal F_P.}
\tag{16}
$$
因而原 $\beta_1^M(\bar P)$ 非零，准确等价于
$\mathcal F_P$ 不属于 (14) 的**全原来源像**。

**证明。** 对 $P^{\rm crit}$ 保原三个普通 Euler 值 $P_0,P_1,P_2$。
R481 的完整整评价为
$$
J(P)=\left(
\pi_sP_0,\
\pi_s(aP_1+p\mathscr SP_0),\
\pi_\ell\left(\frac{a^2}{2}P_2+pa\mathscr SP_1+
p^2\mathscr S^2P_0\right)
\right).
\tag{17}
$$
用 (11)–(13) 展开。第一块读 $<n_0$ 时，所有含 $\eta_0$
的项消失，且除 $p$ 后的二次 $p\xi$ 项模 $p$ 消失，
故得 (15) 的第一项。

第二块的 $P_1/p$ 低段为 $B\xi$；
$\mathscr SP_0$ 中除 $A$ 外的模 $p$ 二次项从
$2s-r-s=s-r>n_0$ 开始，故得第二项。
在第三块，$P_2$ 被 $t^r$ **整系数**整除，而 $r\ge\ell$，
因此其全部 $<\ell$ 行严格为零。
$\mathscr SP_1$ 的唯一模 $p$ 可见项为
$\mathscr S(B\eta_0)$，给第三项。
这没有删去可见的 first carry。

因为 $\bar P\in\ker\bar J$，$J(P^{\rm crit})$ 全部被 $p$ 整除。
在原 $(J_A,pJ_B)$ 中，候选的首 forcing 在另二十六条
carry 分量本来为零；$\bar M R$ 在这些分量也为零。
所以 (15) 加上 (14) 正是原完整首次提升的充要条件，
并未把两条 carry 自由化。证毕。

注意 $A/p$、$\xi$、$\mathscr SA$ 来自同一个 (8) 和同一原轴；
不能分别另选它们来满足 (16)。
换另一实际临界基准只使原 forcing 加上同一来源的
$\bar J_A$ 像，故其原余核类不变。

## 5. 这个实际基准的完整第三精度

为保真正的下一位，下面给 (17) 的全部三块，而不只给 (15)。
所有式均在原目标模 $p^3$；$A,B,C,\eta_0,\xi$ 的含义固定为
(10)–(12)，尤其 $\xi$ 在带一个外部 $p$ 的项中保两位。

准确有
$$
\boxed{
J_0(P^{\rm crit})
=\pi_s\left(A+\frac{p^2}{2}B\xi^2\right)
\pmod{p^3},
}
\tag{18}
$$
$$
\boxed{
\begin{aligned}
J_1(P^{\rm crit})={}&
p\pi_s\left(
aB\xi+\mathscr SA+\frac12\mathscr S(B\eta_0^2)
\right)\\
&+p^2\pi_s\left(
\frac a2C\xi^2+\mathscr S(B\eta_0\xi)
+\frac12\mathscr S(C\eta_0^2\xi)
\right)
\pmod{p^3},
\end{aligned}}
\tag{19}
$$
$$
\boxed{
\begin{aligned}
J_2(P^{\rm crit})={}&
pa\,\pi_\ell\mathscr S(B\eta_0)\\
&+p^2\pi_\ell\left[
a\mathscr S(B\xi+C\eta_0\xi)
+\mathscr S^2 A+\frac12\mathscr S^2(B\eta_0^2)
\right]
\pmod{p^3}.
\end{aligned}}
\tag{20}
$$

为核 (18)–(20)，使用严格的临界 Taylor 式
$$
P_0=A+\frac12B\eta^2+\frac16C\eta^3+\cdots,\qquad
P_1=B\eta+\frac12C\eta^2+\cdots .
$$
全部更高 Euler 系数都被 $t^r$ 整除。
由 $h\ge s-r$，含两个 $\eta_0$ 的项从 $2s-r$ 开始，
含三个者从 $3s-2r>2s+\ell$ 开始。
按每个外部 $p$ 的次数和 (17) 的每次实际移位逐项保留，
恰得 (18)–(20)。
第三块的 $P_2$ 仍在整系数上严格为零。

特别，(19) 中
$$
\frac p2\mathscr S(B\eta_0^2),\qquad
\frac{p^2}{2}\mathscr S(C\eta_0^2\xi)
\tag{21}
$$
可落在第二相对块的最后 $r$ 条行。
它们不进入 (15) 的 $A$ 低段，却是原十三行 carry 的真实项。
(20) 的 $\mathscr S^2(B\eta_0^2)/2$、
$\mathscr S(C\eta_0\xi)$ 以及整个 $\mathscr S^2 A$ 也没有被删去。
所以本篇未从二次局部几何错误地宣布三次正规项在下一位消失。

## 6. 同一个 R、两条十三行与原 d2

若 (16) 可解，取同一实际整提升 $R\in\mathcal W_D$，
令 $Q_2=P^{\rm crit}+pR$。
写
$$
R_i(w)=(\mathcal E^iR)(t(w),g(w)),\quad i=0,1,2.
$$
此处保原完整 $g$；在 carry 高行中不能再把 $R_i$ 一律换成
$R_i|_\psi$。

完整修正为
$$
\begin{aligned}
J_0(Q_2)&=J_0(P^{\rm crit})+p\pi_sR_0,\\
J_1(Q_2)&=J_1(P^{\rm crit})+pa\pi_sR_1
+p^2\pi_s\mathscr SR_0,\\
J_2(Q_2)&=J_2(P^{\rm crit})+\frac{pa^2}{2}\pi_\ell R_2
+p^2a\pi_\ell\mathscr SR_1
\pmod{p^3}.
\end{aligned}
\tag{22}
$$
这和 (18)–(20) 给下一位的全部可读系数。

令 $\pi_B=\pi_s-\pi_{n_0}$。原 $d_2^M(Q_2)$ 的两个 carry
分量准确为下列同一 $R$ 所给的类：
$$
\boxed{
\pi_B\left(\frac{A}{p}+R_0\right),\qquad
\pi_B\left(
aB\xi+\mathscr SA+\frac12\mathscr S(B\eta_0^2)+aR_1
\right)\pmod p.
}
\tag{23}
$$
$A/p$ 仍只在 $<s$ 这段整除。没有独立指定两条边界多项式。

更统一地，在 R449 的整 $(A,B)$ 表示中，原第二障碍代表为
$$
\boxed{
\left(
\overline{\frac{J_A(P^{\rm crit})+pJ_A(R)}{p^2}},\
\overline{\frac{J_B(P^{\rm crit})+pJ_B(R)}p}
\right)
\quad\text{于 }C_2(M).
}
\tag{24}
$$
第一分量的整除由 (16) 保证；第二分量由
$\bar P\in\ker\bar J$ 保证。
其全部数值按 (18)–(22) 读取。
放回整个 $c_*U_0$ 并对最初十三条自由行作恒等延拓，
即恢复原物理矩阵的同一个第二障碍。

所以 (16) 可解不推出 (24) 为零；
也不能在已选 $R$ 的低行之外另造不相容的高尾。
R449 的 $C_2(J)$、真实 carry 像和 $G_2$ 投影继续原样适用。

## 7. 新付输入与剩余问题

本篇新增的是实际 Euler 积分回原格的临界基准、
(14) 对全部原列的代数支识别、(15)–(16) 的完整首次 forcing，
以及 (18)–(24) 中不可删除的原下一位。
所有条件仍在同一个 $\bar P$、同一个来源预算和同一个修正 $R$ 上。

没有证明 $\mathcal F_P$ 落入或不落入 $\operatorname{im}\mathcal T_\psi$。
没有支付 $r=1,\nu=2$ 时非单位临界支的同类整提升；
低 ell 笔记中的光滑外支和二交数在该处仍须保留。
三条原完整中央失败并未参与上述来源提升，也不赋予
$G,Q,\psi$ 或 $A$ 新的中央零。

下一实质接口是 (15) 对同一全来源 jet 像的实际非零或吸收，
并在可解时按 (24) 检查真正第二障碍。
这与仅报告局部近二支、源端单位或形式坐标协变不同。
