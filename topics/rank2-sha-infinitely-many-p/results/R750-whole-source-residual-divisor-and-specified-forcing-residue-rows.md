# R750 — 完整原来源的残余除子、真正留数左行与指定全段 forcing

日期：2026-11-15。**状态：已证明。**

本篇继续 R741 的同一个非立方首核。
在原 $M$、$1\le r\le13$ 的准确范围，把其前两块值投影算到完整长度，
保原 $\xi$ 与由十三行差产生的末段。
随后使用完整原 $\mathcal W_D$，而非只用 $F\mathcal H_2$ 或 $\mathcal H_3$：
先由原低列作整前缀消元，再将其余全部曲线值识别为
原残余除子上的真实主部空间。

这给一族真正杀掉完整原首像的留数行。
其所用的低前缀右逆包含全部高尾；
除子若含奇点或非约化交点，留数也按原对偶化层读取。
指定 forcing 的值段可解，当且仅当它被这批实际左行全杀掉。
剩余法向行、第三块、两组十三行与下一位，仍须由同一个 $R$ 解决。

新的全来源约束是：$\mathcal H_3$ 以外的所有值自由度
都经过一个长度
$\mathcal B_D\cdot C-3\kappa-r$
的确定有限除子；它们不是可任意补写的高 jet。
本篇不声称指定留数已经非零，也不将值段的充要门当成完整 $M$ 的充要门。

## 1. 同一原 M、原非 cube 核和完整值长度

保持 R741 的全部实际数据：
$$
P^{\rm fact}=qt^rF^3,\qquad
P_B=qt^rF\widetilde B\in\mathcal W_D,\qquad
q=d^{-C_D}Q,\quad d=1+8t,
$$
$$
p=6s-1>101,\qquad
1\le\ell\le r\le13,\qquad
k=2h+r-s,\qquad0\le k<\ell,\qquad r<h.
\tag{1}
$$
原 $F$ 与 $\widetilde B$ 的整提升不更换，保原 $f_D<p$。
$C=(F=0)$ 几何整，$P=(0,1)$ 光滑，
$$
e=(\mathcal EF)|_C,\qquad e(P),Q(P)\in k^\times,\qquad
\mathcal E=Y\partial_Y.
$$
保原十九角曲面 $X$、
$$
\kappa=C^2,\quad\chi=-K_XC,\quad
\mathcal N=\mathcal O_C(C),\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)).
$$
本篇专用完整 $M=c_*U_0w^{13}J$，定义
$$
\boxed{
N_0=s-13,\qquad T=N_0-r=s-r-13=2h-k-13.
}
\tag{2}
$$
由 $r-k\le13$，
$$
N_0=2h+r-k-13\le2h.
\tag{3}
$$
仍保 R730/R741 强窗
$$
h>\kappa,\qquad T-h>\kappa,\qquad T\le2h.
\tag{4}
$$

沿同一整 Hensel 支，
$$
\eta=\log(g/\widetilde\psi)=\eta_0+p\xi,\qquad
\eta_0=t^hu,\qquad
\zeta_{\rm phys}=\eta+a\epsilon,\qquad a\in\mathcal O^\times,
$$
$$
t^s=p\epsilon b_s(t),\qquad b_s=(t/w)^s.
\tag{5}
$$
$\xi$ 是同一实际高位；不将其设为零。

记模 $p$ 的
$$
q_0=q|_C,\quad B_0=B|_C,\quad B_1=(\mathcal EB)|_C,\quad
\mathscr B=B_0+2\eta_0B_1.
$$
R731/R741 给
$$
\operatorname{ord}\mathscr B\ge T,\qquad
\rho=\operatorname{ord}B_1,\qquad
\operatorname{ord}B_0=h+\rho,\qquad
0\le\rho\le2\kappa-h<T-h.
\tag{6}
$$
$B_0\ne0$，原 $q_0$ 是实际固定单位。

以下 $\mathscr V_\eta$ 始终指 R741 的原行段操作：
先逆真正整单位 $c_*U_0$，
在前两块各选 $w^{13},\ldots,w^{s-1}$，
只对这些显示行段除 $w^{13}$，换到原 $t$，
再取
$$
\mathscr V_\eta(y)=y_0-\eta_0y_1/a
\quad\bmod t^{N_0}.
\tag{7}
$$
它不是整个目标上 $m_{13}$ 的逆。
对所有真实原来源，R741 已付
$$
\boxed{
\mathscr V_\eta\bar M(R)=R|_C\bmod t^{N_0}.
}
\tag{8}
$$

## 2. 指定 forcing 的全段公式，包含末十三行影响

只用整向量 $M(P_B)/p$；
不假定 $J(P_B)/p$ 整。
设
$$
b_B=\mathscr V_\eta\bigl(M(P_B)/p\bmod p\bigr)
\in k[[t]]/t^{N_0}.
$$

**定理 1。**
$$
\boxed{
b_B
=q_0e\left\{
t^r\xi B_0
-\frac{b_s}{2a}t^ku^2(B_0+\mathscr B)
\right\}\pmod{t^{N_0}}.
}
\tag{9}
$$

**证明。** 在同一个整分支上展开
$$
f(t,\zeta)=q(t,\widetilde\psi e^\zeta)
F(t,\widetilde\psi e^\zeta)
\widetilde B(t,\widetilde\psi e^\zeta)
=C_1\zeta+C_2\zeta^2+C_3\zeta^3+\cdots.
$$
准确有
$$
C_1=q_0eB_0,
$$
$$
C_2=q_0eB_1+
\left(\frac{q_0f_2}{2}+q_1e\right)B_0,
\quad
f_2=(\mathcal E^2F)|_C,\quad q_1=(\mathcal Eq)|_C.
\tag{10}
$$
这里先作整展开，式中模 $p$ 后仍使用原符号。
这里仅在原三块的实际截断内展开；能贡献于所读行的 $\zeta$ 次数均小于 $p$，因而这些有限系数在原点整，不添 $p$ 分母。更高次先由实际 $t/\epsilon$ 截断杀掉，不声称整个指数展开在所有次数整。

不经过普通高项 carry 的组合为
$$
\frac{t^r}{p}\{f(t,\eta_0+p\xi)
-\eta_0 f_\zeta(t,\eta_0+p\xi)\}.
$$
如 R741，$f(t,0)=0$ 使其 native 提升误差的
$\eta_0^0,\eta_0^1$ 项取消；
$\eta_0^2$ 项乘 $t^r$ 已从 $s+k$ 起，
不进入这里的普通低行。
$p\xi$ 部分则准确留下
$$
t^r\xi C_1\pmod{t^{N_0}},
\tag{11}
$$
因为
$f_\zeta(\eta_0)-\eta_0f_{\zeta\zeta}(\eta_0)
=C_1+O(t^{2h})$。
更高 $p$ 次数除一次 $p$ 后仍消失。
这不要求 $\widetilde B$ 的整曲线值本来就有模 $p$ 的高消失阶。

普通模 $p$ 值的第一次 carry
来自 $t^rf(t,\eta_0)$，进入第二块。
再乘 (7) 中的 $-\eta_0/a$，其准确贡献是
$$
-\frac{b_s}{a}t^{r-s}
\{C_1\eta_0^2+C_2\eta_0^3+C_3\eta_0^4+\cdots\}.
\tag{12}
$$
$C_3$ 起的项阶至少 $2h+k\ge N_0$。
(10) 中 $C_2-q_0eB_1$ 含 $B_0$，
其在 (12) 的贡献也从 $2h+k+\rho$ 起。
故 (12) 模 $t^{N_0}$ 为
$$
-\frac{q_0e b_s}{a}t^ku^2(B_0+\eta_0B_1).
$$
代入
$B_0+\eta_0B_1=(B_0+\mathscr B)/2$，
与 (11) 相加即为 (9)。

普通项本已含 $p$ 时，进位后除一次 $p$ 仍留 $p$；
显式 $\epsilon$ 项的进位进入第三块。
原 $w^{13}$ 在全过程中保留，
(3) 恰保证所读两段的截断足以进行上述取消。
因此 (9) 既没有除不整的 $J(P_B)$，
也没有删除第三块中的活项。证毕。

若整个首次修正可解，则 (8) 给
$$
R|_C=-b_B\bmod t^{N_0}.
\tag{13}
$$
右边阶为 R741 的 $h+k+\rho>r$。
除同一个真实局部乘子 $q_0t^r$，得到所需归一值
$$
\boxed{
f_B=-e\xi B_0+
\frac{e b_s}{2a}t^{k-r}u^2(B_0+\mathscr B)
\pmod{t^T}.
}
\tag{14}
$$
$t^{k-r}$ 虽为负幂，乘上的两项均足够深，(14) 仍是整 Taylor jet。

这里 $q_0$ 的约去仅因为 (13) 除的是同一个来源乘子；
没有把原余因子删掉或换成任意单位。
由 (6)，$\mathscr B$ 项在 (14) 中可从
$t^{T-(r-k)}$ 起。
所以其最后 $r-k\le13$ 个位置必须保留。
原两组十三行 carry 并未等同于这个较短尾段；
那些完整行带仍在第8节的剩余目标中。

## 3. 原低 r 列的整直和与右逆高尾

完整来源是原 canonical 直和
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}}.
$$
当前 $D\ge3b\ge3$，因此包含 $n=2$ 原列。
特别原 $n=2$ 列有
$$
q_2=(t-1)/d,\qquad e_3=13.
$$
因此下列都是原真实列：
$$
L_j=Y^2q_2(t)t^j,\qquad0\le j<r\le13.
\tag{15}
$$
在同一个整 Hensel 分支 $\widetilde\psi$ 上，
$L_j|_C=\widetilde\psi^2q_2t^j$；
其 $r$ 个低系数的矩阵为三角形，主对角为单位 $-1$。
由此得到整右逆
$$
\iota_r:\mathcal O[[t]]/t^r\longrightarrow\mathcal W_D
$$
以及整分解
$$
\boxed{
\mathcal W_D=
\operatorname{span}_{\mathcal O}\{L_0,\ldots,L_{r-1}\}
\oplus\mathcal W_D^{(r)},
}
\tag{16}
$$
$$
\mathcal W_D^{(r)}
=\{R:R(t,\widetilde\psi)\equiv0\bmod t^r\}.
$$
右逆使用的每条 $L_j$ 都是整个原来源列，
包含其真实高尾，不是目标中的自由低单位向量。

模 $p$ 时，对任意 $f\in k[[t]]/t^{N_0}$ 定义
$$
\boxed{
\mathfrak n_r(f)=
\frac{f-\iota_r(\pi_r f)|_C}{q_0t^r}
\pmod{t^T}.
}
\tag{17}
$$
分子确被 $t^r$ 整除。
$(q_0)^{-1}$ 是原单位逆。
对任何原 $R$，
(17) 读取的是
$$
\frac{R^{(r)}|_C}{q_0t^r},\qquad
R^{(r)}=R-\iota_r(\pi_r(R|_C)).
\tag{18}
$$
不能省去 (17) 中右逆的高尾。

对 (13) 的指定右端，其前 $r$ 系数已经为零，
所以 (17) 正是 (14)。
在整首次修正中，若低 $r$ 个来源系数为 $p$ 倍，
它们不是被删掉：
写 $R=R^{(r)}+pA$ 时，
同一个 $P_B+pR$ 准确变为
$P_B+pR^{(r)}+p^2A$。
这项必须进入下一位的实际来源。
(16) 只是整基变换，不是把第三精度重置。

## 4. 全部 W_D 值自由度的真实残余除子

令 $\mathcal B_D$ 为 R555/R680 的原十九角线束类，
$$
H^0(X,\mathcal O_X(\mathcal B_D))
=d^{C_D}\overline{\mathcal W}_D.
\tag{19}
$$
原 $P^{\rm fact}$ 的清分母截面为 $t^rQF^3$。
$Q(P)\ne0$ 保 $F\nmid Q$，
所以其零除子准确写为
$$
\boxed{
\operatorname{div}(P^{\rm fact})=3C+E,\qquad
E\ge0,\quad E\sim\mathcal B_D-3C,\quad C\not\subset E.
}
\tag{20}
$$
(20) 包括固定角、垂直部分、其他因子和全部例外除子的真实重数。

乘原 $qt^r$ 的全局截面就是
$\sigma_E\in H^0(X,\mathcal O_X(E))$。
在清分母框中它是 $t^rQ$；
在原 $P$ 邻域的物理框中它是 $q t^r$。
二者差的是显示的 $d^{C_D}$ 单位，不能在 $d=0$ 处混用框。

在 $C$ 上，
$$
\boxed{
E|_C=rP+E',\qquad E'\ge0,\quad P\notin E',\quad
e'=\deg E'=\mathcal B_D\cdot C-3\kappa-r.
}
\tag{21}
$$
$E|_C$ 是有效 Cartier 除子，因为 (20) 在整 $C$ 上非零；
$P$ 光滑且 $Q(P)$ 单位给其在 $P$ 的准确重数 $r$。
因此 $E'$ 也是原 $C$ 上的有效 Cartier 除子。
它可含奇点与非约化结构，不换成自由简单点集。

对所有 $\bar R\in\overline{\mathcal W}_D^{(r)}$，
$$
u_R=\frac{R|_C}{q_0t^r}
$$
是一个真正的全局截面
$$
u_R\in H^0(C,\mathcal N^3(E')).
\tag{22}
$$
(22) 中的除法按 (20) 的全局线束解释；
它在 $P$ 无极，因为 (16) 已消掉低 $r$ 段。

定义实际空间
$$
\mathcal U_D=\{u_R:\bar R\in\overline{\mathcal W}_D^{(r)}\}
\subset H^0(C,\mathcal N^3(E')).
\tag{23}
$$
由 R495，
$\mathcal H_3\to H^0(C,\mathcal N^3)$ 满射，
且 $qt^r\mathcal H_3\subset\mathcal W_D^{(r)}$。
因此
$$
H^0(C,\mathcal N^3)\subset\mathcal U_D.
\tag{24}
$$

取完整主部空间
$$
\mathcal P_{E'}=
H^0(E',\mathcal N^3(E')|_{E'}),\qquad
\dim\mathcal P_{E'}=e',
$$
并只取原所有列给出的像
$$
\boxed{\mathcal V_{E'}=\operatorname{pp}_{E'}(\mathcal U_D)
\subset\mathcal P_{E'}.}
\tag{25}
$$
不能把 (25) 自动换成整个 $\mathcal P_{E'}$。

**定理 2（完整原值空间的有限边界）。**
$$
\boxed{
0\to H^0(C,\mathcal N^3)\to\mathcal U_D
\xrightarrow{\operatorname{pp}_{E'}}\mathcal V_{E'}\to0.
}
\tag{26}
$$
特别，原 $\mathcal H_3$ 以外的所有值自由度至多为 $e'$。

**证明。** 无主部的 (22) 正是全局 $\mathcal N^3$ 截面，
而这些截面已全部由 (24) 的同预算真实来源得到。
核、像因此均为 (26) 所写对象。
没有在证明中补造任何原来源或局部值。证毕。

若需要直接生成 (25)，只须对每条原 canonical 列
先作 (16) 的同一个低前缀消元，再取 (22) 在整个 $E'$ 的主部。
这给有限、明确且保所有原列的矩阵；
高尾不是新参数。

## 5. 真正杀全 W_D 像的留数行

原 $C$ 为整 Gorenstein 曲线，令
$$
\boxed{
\mathcal D_T=
H^0(C,\omega_C\mathcal N^{-3}(TP)).
}
\tag{27}
$$
其线束次数为
$$
d_T=T-2\kappa-\chi.
\tag{28}
$$
$\deg\mathcal N^3=3\kappa>\kappa-\chi=2g_C-2$，
故 $H^1(C,\mathcal N^3)=0$。
原点 $P$ 光滑，Serre 对偶给准确的完美配对
$$
\boxed{
\left(
k[[t]]/t^T\,/\,\operatorname{ev}_T H^0(C,\mathcal N^3)
\right)^*
\simeq\mathcal D_T,\qquad
(f,\omega)\longmapsto\operatorname{Res}_P(f\omega).
}
\tag{29}
$$
所有局部线束框在此使用同一个原 $P$ 框。

对 $v\in\mathcal V_{E'}$，取任一个真实 $u\in\mathcal U_D$ 的主部为 $v$，
定义
$$
\boxed{
\mathfrak r(v,\omega)=
\sum_{Q\in\operatorname{supp}E'}
\operatorname{Res}_Q(u\omega).
}
\tag{30}
$$
若 $Q$ 为奇点，(30) 是正规化各支留数在同一个原点处的和，
即原对偶化层的 Rosenlicht 留数；
不将各支单独当成独立行。
可先在代数闭剩余域计算，再作原常数域的迹下降。

(30) 只依赖主部。
改变 $u$ 一个全局 $\mathcal N^3$ 截面后，
所增微分在 $E'$ 正则于原对偶化层，其每个原奇点的留数和为零。
而全局留数定理给
$$
\operatorname{Res}_P(u\omega)=-\mathfrak r(v,\omega).
\tag{31}
$$
这里 $u\omega$ 除 $P,E'$ 外正则于 $\omega_C$；
其余原奇点虽在正规化框中可能出现极，Rosenlicht 条件使其分支留数和为零。

置
$$
\boxed{
\mathcal L_D^{\rm val}
=\{\omega\in\mathcal D_T:
\mathfrak r(v,\omega)=0\text{ 对全部 }v\in\mathcal V_{E'}\}.
}
\tag{32}
$$

**定理 3（全部原值左核）。**
$\mathcal L_D^{\rm val}$ 正好是 (23) 在长度 $T$ 的实际 jet 像的左核。
而下式是在原完整目标上真正杀掉全部 $\bar M\overline{\mathcal W}_D$ 的行：
$$
\boxed{
\lambda_\omega(y)=
\operatorname{Res}_P\left[
\mathfrak n_r(\mathscr V_\eta y)\,\omega
\right],
\qquad \omega\in\mathcal L_D^{\rm val}.
}
\tag{33}
$$
$\mathscr V_\eta$ 包含 (7) 的原单位逆和合法行段读取。

**证明。** (24)、(29) 先迫任何值左行属于 $\mathcal D_T$。
再由 (26)、(31)，它杀掉其余所有真实来源
当且仅当满足 (32)。
(8)、(17)、(18) 随即证明 (33) 对每条完整原列为零。
反向，归一值空间 (23) 的任一左行都已由 (29) 与 (32) 读取。
这不是只对某个 $F$-整除子格成立的行。证毕。

保 (17) 的完整低右逆高尾是 (33) 成立的必要部分。
直接对任意目标除 $q_0t^r$ 没有定义；
只保一个在来源上同阶的低多项式也不能替代该右逆。

## 6. 指定全 forcing 的准确值门

将 (14) 直接代入 (29)–(33)，定义
$$
\boxed{
\begin{aligned}
\Omega_B(\omega)
=\operatorname{Res}_P\biggl[
\biggl\{-e\xi B_0
+\frac{e b_s}{2a}t^{k-r}u^2(B_0+\mathscr B)\biggr\}
\omega\biggr].
\end{aligned}}
\tag{34}
$$
全部系数是同一个原 $P_B$ 的实际系数。

**定理 4。**
存在一个原 $\bar R\in\overline{\mathcal W}_D$，
使 R741 的完整值条件 (13) 成立，当且仅当
$$
\boxed{
\Omega_B(\omega)=0
\quad\text{对全部 }\omega\in\mathcal L_D^{\rm val}.
}
\tag{35}
$$

**证明。** (13) 的右端在低 $r$ 阶为零。
所以任何解的模 $p$ 来源必须在 (16) 的
$\overline{\mathcal W}_D^{(r)}$；
其归一值正是 (23)。
有限 jet 空间上的完整对偶 (29)、定理3
将成员性准确变为 (35)。证毕。

特别，(34) 是商后的真实配对，不是 R741 的商前单位首项。
它同时保实际 $\xi$、整个 $b_s$ 和最后 $r-k$ 阶的 $\mathscr B$。
没有将这些尾段分开求原像。

### 整个不含 xi 的初段已被原来源吸收

由 (6)，(14) 中 $\xi$ 项从阶
$$
h+\rho\le2\kappa
$$
起。
而曲线上任意长度
$$
L\le2\kappa+\chi-1
$$
的 $\mathcal N^3$ jet 均由全局截面实现：
其 Serre 对偶次数 $L-2\kappa-\chi<0$，
所以评价满射。
这些截面全由 (24) 返回同一原来源。

因此，(14) 在 $\xi$ 尚未进入前的**整个**初段，
都能由同一原来源吸收，不仅是其单位首项。
更准确地，不存在只支撑在该初段的非零值型左障碍。
在原强窗中 $\chi\ge2b>0$，这个结论还留有正余量。

这不意味着不同尾段可以独立选择 $R$。
R495 的联合返回可以在其准确长度门内同时指定 normal 初段；
它并未支付超过该门的全部 normal 尾，
也没有使 (34) 的其余项自动消失。

## 7. 有限边界成本和原临界窗

由 R680，$\mathcal B_D$ 与 $C$ 均为 nef，
而 (20) 的 $E$ 有效。
所以
$$
\mathcal B_D^2-9\kappa
=(\mathcal B_D+3C)\cdot E
=\mathcal B_D\cdot E+3C\cdot E
\ge3C\cdot E.
$$
结合 (21)，得到准确有限界
$$
\boxed{
0\le e'
=\mathcal B_D\cdot C-3\kappa-r
\le
\left\lfloor\frac{\mathcal B_D^2-9\kappa}{3}\right\rfloor-r.
}
\tag{36}
$$
这里 $\mathcal B_D^2$ 使用 R680 的十九个准确取整重数，
不以其主项替代有限参数。

令 $w_T=\dim\mathcal D_T$。
(30)–(32) 给
$$
\boxed{
\dim\mathcal L_D^{\rm val}
=w_T-\operatorname{rank}(\mathfrak r|_{\mathcal V_{E'}}),
}
\tag{37}
$$
以及
$$
\boxed{
\max(0,w_T-e')\le
\dim\mathcal L_D^{\rm val}\le w_T.
}
\tag{38}
$$
(37) 用真实主部像，未将 $e'$ 本身当成已实现的秩。

在另满足 R743 最高系数及 tame 门的临界族
$$
h/\kappa\to9/8,\qquad T/\kappa\to9/4,\qquad
a_F+b=o(\kappa),\quad\chi=o(\kappa)
$$
中，R743 对同一个 (27) 给
$$
w_T\le\frac5{48}\kappa+o(\kappa).
\tag{39}
$$
若还处于同预算的主阶无余量范围
$$
\mathcal B_D^2-9\kappa=O(b),
\tag{40}
$$
例如原 $D=3b+O(1)$、
$\kappa=47b^2/12+O(b)$，
则 (36) 给 $e'=O(b)$。
所以完整原 $\mathcal W_D$ 超出 $\mathcal H_3$ 的所有值列，
在该临界比较中只能通过 $O(b)$ 维的真实有限边界修改 (29)。

(39) 是上界；$w_T$ 本身可能为零。
(38) 也不证明指定 $\Omega_B$ 非零。
(40) 只在写明的实际来源范围使用，
不对有大 $D$ 余量的候选自动断言。

## 8. 所有值解的同一原来源纤维与剩余完整行

令
$$
\mathcal F_D
=\{R\in\overline{\mathcal W}_D:R|_C=0\},
$$
这是整个原格中的真实 $F$-整除空间，
不只取 $qt^rF\mathcal H_2$。

值零核为
$$
\mathcal K_{\rm val}
=\{R\in\overline{\mathcal W}_D^{(r)}:
R|_C=0\bmod t^{N_0}\}.
$$
由定义与 (23) 准确有
$$
\boxed{
0\to\mathcal F_D\to\mathcal K_{\rm val}
\to
\mathcal U_D\cap
H^0(C,\mathcal N^3(E')(-TP))
\to0.
}
\tag{41}
$$
再令
$$
\mathcal V_{E'}^0=
\{v\in\mathcal V_{E'}:
\mathfrak r(v,\omega)=0
\text{ 对全部 }\omega\in\mathcal D_T\}.
$$
则有第二个准确序列
$$
\boxed{
0\to H^0(C,\mathcal N^3(-TP))
\to
\mathcal U_D\cap H^0(C,\mathcal N^3(E')(-TP))
\to\mathcal V_{E'}^0\to0.
}
\tag{42}
$$

**证明。** (41) 的核正是完整曲线限制为零的来源，
且右侧每个元素按 $\mathcal U_D$ 的定义都有同一原来源。

对 (42)，无主部的核由 (26) 读取。
若 $v\in\mathcal V_{E'}^0$，任选其实际 $u\in\mathcal U_D$。
由 (29)、(31)，$u$ 在 $P$ 的长度 $T$ jet
属于全局 $\mathcal N^3$ 的评价像。
减去这个已由 (24) 返回的同源截面，
便得到 (42) 的同一实际原像。
反向对一个消到 $T$ 的 $u$ 用 (31) 即得。
这里未将 $\mathcal V_{E'}$ 的元素从某个环境空间自由提升。证毕。

如果 (35) 通过，固定一个真实值解 $R_*$。
所有值解准确为
$$
\boxed{R_*+\mathcal K_{\rm val}.}
\tag{43}
$$
记原完整目标的约化为 $Y_{\rm old}/p$，
原首 forcing 为 $\bar\beta_B=M(P_B)/p\bmod p$。
(13) 只保证
$$
\bar\beta_B+\bar M R_*\in\ker\mathscr V_\eta.
$$
完整首次修正可解，还必须、且只须
$$
\boxed{
-\bar\beta_B-\bar M R_*
\in
\bar M(\mathcal K_{\rm val})
\subset\ker\mathscr V_\eta.
}
\tag{44}
$$
(41)、(42) 指明 (44) 中所有允许的来源自由度：
完整 $\mathcal F_D$、同一高值核及实际边界主部核。
它们的 normal 数据都由其真实原列给出，
不是在 (35) 之后另外填写。

特别，两组十三行、第三块、$U_1/p$ 和原低行右逆高尾
全在 (44) 的同一目标中保留。
第一提升后，原 $d_2/G_2$ 必须继续用这个同一个 $R$ 计算；
(16) 中的 $p$ 倍低列则按第3节准确进入下一位。
本篇没有从值解的存在推全 $p^2$ 解，
更没有推 $p^3$ 解。

## 9. 新增内容与仍未付的非零

R741 的值投影本身不杀原全像。
本篇先支付了它的全部实际 forcing (9)，
再通过原来源的低右逆和确定残余除子，
得到真正杀全像的行 (33)。
完整 $\mathcal W_D$ 的额外值列准确由 (25) 控制，
有有限成本 (36)，其与同一个 $R$ 的 normal 自由度由 (41)–(44) 保留。

仍未证明 (34) 对某个原 $\omega$ 非零，
也未证明 (44) 的指定类为零或非零。
这些判断要用实际 $\xi$、实际主部矩阵及剩余原行，
不能用边界长度、Clifford 上界或一个环境满射替代。

原完整中央失败、全 $P_{134}/U_0$、
$\xi_0$、两条十三行 carry、
同一个 $P_2=P_B+pR$ 与下一位继续按原规范。
没有新来源、新中央零或对固定曲线无穷素数结论的提前声明。

依赖：
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)；
[R731](R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md)；
[R741](R741-specified-noncubic-first-forcing-and-necessary-normal-smoothing.md)；
[R743](R743-normalization-genus-and-actual-two-kernel-rank-improvement.md)。

本篇是原实际有限来源、整低基变换及全局对偶的证明，
不新增数值扫描或可重算数据文件。
