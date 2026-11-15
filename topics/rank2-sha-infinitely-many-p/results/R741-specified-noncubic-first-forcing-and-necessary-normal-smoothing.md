# R741 — 指定非立方首核的原两块值投影与不可保持因子的首次修正

日期：2026-11-15。**状态：已证明。**

本篇继续 R731 的同一个指定镜轴核
$P_B=qt^rF\widetilde B\in\mathcal W_D$。
不要求 R731 的低法向阶门 $\rho<r-k$，
也不将新增的非立方首核重新假设为立方。
我们从原首 Bockstein 的前两块构造一个实际有限投影，
证明它有确定的单位首项。
这给任意完整原来源修正 $R$ 一个非零的曲线限制条件，
并排除所有保持 $F\widetilde B$ 因子分解的整首次修正。

此投影不杀完整原首像，也一般不杀 R731 的垂直单位块。
因此这里证明的是指定 forcing 对同一个 $R|_C$ 的准确要求，
不是完整原余核非零。
所有剩余来源、两条十三行 carry 和下一位 $d_2/G_2$ 继续保留。

## 1. 同一来源及原目标范围

保 R731 的实际因子、十九角整格和整提升：
$$
P^{\rm fact}=qt^rF^3,\qquad q=d^{-C_D}Q,\qquad d=1+8t,
\qquad P_B=qt^rF\widetilde B\in\mathcal W_D.
\tag{1}
$$
$F$ 的同一整 Hensel 分支为 $\widetilde\psi$，
$C=(F=0)$、$P=(0,1)$、$\mathcal E=Y\partial_Y$。
记 $e=(\mathcal EF)|_C$，并保 $e(P),Q(P)$ 为单位、
全部真实角帽及 $f_D<p$。

原整数满足
$$
p=6s-1>101,\qquad 1\le\ell\le r<h,\qquad
k=2h+r-s,\qquad 0\le k<\ell.
\tag{2}
$$
特别，
$$
r>k,\qquad 2h=s-r+k<s.
\tag{3}
$$
若 $\mathsf M_0=J$，置 $\delta_0=0$；
若 $\mathsf M_0=M=c_*U_0m_{13}J$，置 $\delta_0=13$。
相应镜轴长度为
$$
T=s-r-\delta_0=2h-k-\delta_0,\qquad q_T=T-h=h-k-\delta_0.
\tag{4}
$$
继续保 R731 的几何门
$$
h>\kappa=C^2,\qquad q_T>\kappa,\qquad T\le2h.
\tag{5}
$$

假设原指定列首位被真实垂直单位块吸收，
而其 $Z=V(F,e)$ 上的指定值不为零。
于是 R730/R731 已付唯一的类
$$
[B]\in K_{\rm mir}/kF^2,\qquad B|_Z=UA|_Z\ne0.
\tag{6}
$$
它有同源整提升
$$
\widetilde B
=UA+e\widetilde K_1
-F(\mathcal E\widetilde K_1+\widetilde L),
\qquad
\widetilde K_1\in\mathcal H_1,\quad
\widetilde L\in\mathcal L,
\tag{7}
$$
并满足 R731 的完整整来源恒等式。这里不另选环境来源。

在同一有限原目标中保
$$
\eta=\log(g/\widetilde\psi)=\eta_0+p\xi,\qquad
\eta_0=t^hu,\quad u(0)\in k^\times,\qquad
\zeta_{\rm phys}=\eta+a\epsilon,\quad a\in\mathcal O^\times,
\tag{8}
$$
$$
t^s=p\epsilon b_s(t),\qquad b_s=(t/w)^s,\qquad
\vartheta=(t/w)(0)\in\mathcal O^\times.
\tag{9}
$$
模 $p$ 系数仍记为 $a,u,b_s$。
$\xi$ 是原整基准的实际低轴修正，不令其为零。
原 $b=17$ 首尺度、整个 $q$ 和所有坐标单位均保留。

设
$$
B_0=B|_C,\quad B_1=(\mathcal EB)|_C,\quad
\mathscr B=B_0+2\eta_0B_1.
$$
R731 给
$$
\operatorname{ord}\mathscr B\ge T,\qquad
\rho=\operatorname{ord}B_1
=\operatorname{ord}B_0-h,\qquad
0\le\rho\le2\kappa-h<\kappa<q_T.
\tag{10}
$$
记 $b_\rho=[t^\rho]B_1\ne0$。
(10) 因而准确给
$$
B_0=-2u(0)b_\rho t^{h+\rho}
+O(t^{h+\rho+1}).
\tag{11}
$$
加 $kF^2$ 不改变 $B_0,B_1,\rho$ 或 $b_\rho$。

## 2. 原前两块的合法读取，不逆 m13

置
$$
n_0=s-\delta_0,\qquad N=\min(2h,n_0).
\tag{12}
$$
对相对 $J$ 首核，使用原整向量
$\beta_J(P_B)=J(P_B)/p\bmod p$，
其前两块记为 $\beta_0,\beta_1\in k[[t]]/t^s$。

对只在原 $M$ 首核中的 $P_B$，
不写可能并不整的 $J(P_B)/p$。
先仅逆原真正整单位 $c_*U_0$，取
$$
\widehat\beta_M(P_B)
=(c_*U_0)^{-1}M(P_B)/p\bmod p.
\tag{13}
$$
本篇使用其前两块的 $w$ 行 $13,\ldots,s-1$；
将这两段分别除以它们已经具有的 $w^{13}$，
再作同一整坐标变换 $t=t(w)$，得到
$$
\beta_0,\beta_1\in k[[t]]/t^{n_0}.
\tag{14}
$$
这是两个明确行段的读取，不是原目标上 $m_{13}$ 的逆。
对任意目标向量，同一线性操作定义为只选这两个行段、舍去各自其余行，再除显示的 $w^{13}$；
下面额外证明，本篇的 $P_B$ 及原首像确实没有被舍去的最初十三行。

为验证 (14)，R731 已计算普通模 $p$ 值
$$
\begin{aligned}
t^r(qFB)(t,g)
={}&-q_0e\,t^{r+2h}u^2B_1\\
&+O(t^{r+h+T})+O(t^{r+3h}),
\qquad q_0=q|_C.
\end{aligned}
\tag{15}
$$
其首阶为 $s+k+\rho>s-1$。
故在 (13) 第二块中，
普通值的一次进位从 $w$ 行 $13+k+\rho$ 起，
不会产生低于 $13$ 的行。
本已含 $p$ 的低普通项乘 $w^{13}$ 后再进位，
除一次 $p$ 仍为零。
显式 $\epsilon$ 项的顶带则进入第三块，不会回到 (14)。
第一块本身显然具有 $w^{13}$。

原第二块顶端十三行到第三块的 carry 仍然存在；
原第一块到第二块的 carry 也完全按 (15) 读取。
这里只解释为什么 (14) 是合法的指定前两行段。
对任意原修正 $R$，$\overline{(c_*U_0)^{-1}M(R)}$
的前两块同样具有 $w^{13}$，因为其额外进位带一个 $p$。

定义实际有限线性投影
$$
\boxed{
\mathscr V_\eta(\beta)
=\beta_0-\frac{\eta_0}{a}\beta_1
\quad\text{于 }k[[t]]/t^N.
}
\tag{16}
$$
乘法在显示长度内截断。
没有将 $\epsilon$ 取某个值来改变原目标，
也没有删除任何第三块行。

## 3. 任意原来源的首像在此投影下是曲线限制

对任意 $\bar R\in\overline{\mathcal W}_D$，
原物理评价前两块在 (14) 的长度内准确为
$$
R(t,\psi e^{\eta_0}),\qquad
a(\mathcal ER)(t,\psi e^{\eta_0}).
\tag{17}
$$
普通高项的 carry 模 $p$ 为零。
所有原来源在 $P$ 正则，因此同一 Taylor 展开给
$$
R(t,\psi e^{\eta_0})
-\eta_0(\mathcal ER)(t,\psi e^{\eta_0})
=R|_C+O(t^{2h}).
$$
从而
$$
\boxed{
\mathscr V_\eta\overline{\mathsf M_0(R)}
=R|_C\pmod{t^N},
}
\tag{18}
$$
其中 $M$ 端严格使用 (13)–(14) 的单位逆和行段读取。

(18) 对完整 $\mathcal W_D$ 成立，
没有要求 $R$ 带公共 $t^r$ 或被 $F$ 整除。
它同时说明本投影的范围边界：
它杀所有 $F$-整除来源的首像，
却不杀一般原首像。
例如垂直列 $qt^r\mathcal W_FH$ 的投影是
$-2q_0et^rH|_C$，一般非零。
不能将 (16) 当作完整原左核。

## 4. 同一个 P_B 的完整首次值投影首项

定义
$$
H_B=h+k+\rho.
\tag{19}
$$
由 (3)、(4)、(10)，
$$
\boxed{
H_B<2h-\delta_0<s-\delta_0=n_0,
\qquad H_B<N.
}
\tag{20}
$$
对原 $M$，这特别证明真实读取行
$13+H_B<s$；
不能只凭相对 $J$ 的 $H_B<s$ 忽略十三行。

**定理 1。** 在上述同一原来源、原目标及指定类下，
$$
\boxed{
\operatorname{ord}\mathscr V_\eta\beta(P_B)=H_B,
\qquad
[t^{H_B}]\mathscr V_\eta\beta(P_B)
=\frac{q_0(0)e(P)b_s(0)u(0)^3b_\rho}{a}
\in k^\times.
}
\tag{21}
$$
原 $w$ 行的首系数再乘 $\vartheta^{H_B}$。
若用 (13) 的未去 $w^{13}$ 行段，
该单位位于原前两块组合的 $w$ 行 $13+H_B$。
这里 $q_0(0)=d(0)^{-C_D}Q(P)$ 是实际固定余因子的单位，
未被省略或另作来源规范化。

**证明。**
在同一个整 Hensel 分支上写
$$
f(t,\zeta)=q(t,\widetilde\psi e^\zeta)
F(t,\widetilde\psi e^\zeta)
\widetilde B(t,\widetilde\psi e^\zeta).
\tag{22}
$$
准确有 $f(t,0)=0$ 和
$\partial_\zeta f(t,0)=\widetilde q_0\widetilde e\widetilde B_0$。
完整物理来源为
$t^rf(t,\eta_0+p\xi+a\epsilon)$。
原显式 $\epsilon^2$ 项带 $t^r$，
因 $r\ge\ell$ 在对应第三块截断；
原 $M$ 同时带 $w^{13}$，结论相同。

先看不经普通值进位的前两块。
它们的组合由
$$
\frac{t^r}{p}
\{f(t,\eta_0+p\xi)-\eta_0\partial_\zeta
f(t,\eta_0+p\xi)\}
\tag{23}
$$
在原低普通行中读取。
对只属于 $M$ 首核的情形，(23) 仅表示这些已被 $p$ 整除的低坐标，
不表示整个 $J(P_B)$ 可以除 $p$；其合法长度准确是 $n_0$。
由于 $f(t,0)=0$，
$f(t,\eta_0)-\eta_0f_\zeta(t,\eta_0)$
整除 $\eta_0^2$；
乘 $t^r$ 后从 $t^{r+2h}=t^{s+k}$ 起，
在这里使用的普通低块中为零。
这逐项取消了任意整提升 $\widetilde B$ 的低阶 $p$ 倍误差，
没有预先指定这些误差。

展开 (23) 的 $p\xi$ 部分。
恒等式
$$
f_\zeta(t,\eta_0)-\eta_0 f_{\zeta\zeta}(t,\eta_0)
=f_\zeta(t,0)+O(t^{2h})
$$
给该部分的完整低块值
$$
t^r\xi q_0e B_0.
\tag{24}
$$
其阶至少为 $r+h+\rho$，
严格大于 $H_B$，因为 $r-k>0$。
含更高 $p$ 次数的项除一次 $p$ 后仍为零。
因此既没有令 $\xi_0=0$，也没有删去一个可取消 (21) 的低项。

还须保普通模 $p$ 值的第一次 carry。
由 (15) 及 $r+2h=s+k$，它对第二块的贡献为
$$
-q_0e\,b_s\,t^ku^2B_1
+O(t^{k+q_T})+O(t^{k+h}),
\tag{25}
$$
在所读范围内使用整个原 $b_s(t)$。
将 (25) 乘 $-\eta_0/a$，
即得
$$
\frac{q_0e b_s}{a}t^{h+k}u^3B_1
+O(t^{h+k+q_T})+O(t^{2h+k}).
\tag{26}
$$
两个误差阶均严格大于 $H_B$：
前者用 $\rho<q_T$，后者用 $\rho<h$。

本已含 $p$ 的普通高项在进位后再除 $p$ 仍含 $p$；
显式 $\epsilon$ 项的进位只进入第三块。
所以 (24)、(26) 已包括本投影在 $H_B$ 及此前的全部贡献。
其首系数正是 (21)。

对原 $M$，整个计算先乘真实 $w^{13}$。
(20) 保证本次所读前两块行都严格低于 $s$；
第一 carry 正由 (25) 保留，
其余边界如第2节所述落在第三块或带额外 $p$。
因此同一证明不需要假设 $J(P_B)/p$ 整。证毕。

## 5. 代表和整提升的准确不变范围

若换 $B\mapsto B+cF^2$，
则 $P_B$ 增加同一个原 cube 的常数倍。
R502 的完整 cube 公式给其第一块为零，
第二块从 $t^{h+k}$ 起；
乘 (16) 中的 $\eta_0$ 后从 $t^{2h+k}$ 起。
其实际 $\xi$ 项和活着的 $V_1$ 项同样不影响 $t^{<2h}$。
故
$$
\mathscr V_\eta\beta(P_{B+cF^2})
=\mathscr V_\eta\beta(P_B)\pmod{t^N}.
\tag{27}
$$

若只改 (7) 中同一整镜轴代表的提升，
差为 $p\,qt^rF H_2$；
由 (18) 它在 (16) 下同样为零。
因此 (21) 及所读投影不依赖这种真实提升选择。

但若作其他原来源的整单位列消元，
$P_B$ 可以改变 $pA$，$A\in\mathcal W_D$。
这时准确的运输规则是
$$
\boxed{
\mathscr V_\eta\beta(P_B+pA)
=\mathscr V_\eta\beta(P_B)+A|_C\pmod{t^N}.
}
\tag{28}
$$
尤其不能在垂直单位块取商后仍无条件保原 (21) 的数值。
取商时同一个修正必须同步换为 $R-A$。
(28) 明确区分实际代表、商中余类和后续同一个 $R$。

令
$$
\mathcal V_D=\operatorname{im}\left(
\overline{\mathcal W}_D\longrightarrow k[[t]]/t^N,\ 
R\longmapsto R|_C
\right).
$$
(18) 给真实诱导映射
$$
\operatorname{coker}\overline{\mathsf M_0}
\longrightarrow (k[[t]]/t^N)/\mathcal V_D
\tag{29}
$$
在这些前两行段上的解释。
(21) 是商前的非零向量；
本篇不声称其在 (29) 的目标中仍非零，
也不以指定阶数代替对 $\mathcal V_D$ 的实际计算。

## 6. 完整原首次修正必须具有指定非零曲线 jet

假设存在同一个完整原来源 $R\in\mathcal W_D$ 使
$$
\mathsf M_0(P_B+pR)=0\pmod{p^2}.
\tag{30}
$$
应用 (16)、(18) 得
$$
\boxed{
R|_C=-\mathscr V_\eta\beta(P_B)\pmod{t^N}.
}
\tag{31}
$$
特别，
$$
\boxed{
\operatorname{ord}_P(R|_C)=H_B,\qquad
[t^{H_B}]R|_C
=-\frac{q_0(0)e(P)b_s(0)u(0)^3b_\rho}{a}\ne0.
}
\tag{32}
$$
因为 $H_B<N$，(32) 是准确阶数，不是只有模糊下界。
它适用于整个 $\mathcal W_D$ 的 $R$，
不限于公共前缀子格或 R731 显示单位块。

因此 $R$ 不可能被 $F$ 整除。
这个结论对所有允许的 $\rho$ 成立，
包括 R731 第二块低行失效的 $\rho\ge r-k$ 分支。
它也不要求第三块中的 $\mathscr B$ 或 $\mathscr H_B$ 先满足额外条件。

不过 $\overline{\mathcal W}_D$ 的其他列可能有 (32) 的限制，
所以 (32) 本身仍不是不存在 $R$ 的证明。
若首位可解，前两块、第三块及所有边界仍必须由这个同一个 $R$ 同时解决。

## 7. 任何保持原因子分解的整首次修正均被排除

考虑原整局部因子的一次变形
$$
qt^r(F+pA)(\widetilde B+pC_1),
\tag{33}
$$
其中 $A,C_1$ 在原点正则；
还可允许 $q$ 及公共前缀作整一次变形。
即使不先限制它们必须命中原角帽，(33) 在 $C$ 上的首次修正也只能是
$$
R|_C=q_0t^r A_0B_0,\qquad A_0=A|_C.
\tag{34}
$$
$q$ 或前缀的变化、以及 $FC_1$ 项在此限制中均为零。
由 (11)，
$$
\operatorname{ord}(q_0t^r A_0B_0)\ge r+h+\rho
>h+k+\rho=H_B.
\tag{35}
$$
这与 (32) 矛盾。

故不存在在原点正则、保持此因子分解的整首次提升。
该排除当然也适用于满足全部十九角的因子保持型来源。

若只在 Laurent 局部域中形式求解 (34)，
由 (11)、(32) 得所需第一因子变形准确为
$$
\boxed{
A_0
=\frac{e(P)b_s(0)u(0)^2}{2a}\,
t^{\,k-r}
+O(t^{k-r+1}).
}
\tag{36}
$$
它有不可去的极点，阶为 $r-k>0$。
固定余因子 $q_0(0)$ 在 (32) 中完整保留，
在 (36) 中则因除同一 (34) 的 $q_0B_0$ 而真实约掉。
不能将这个有极的形式因子变形当成原 $\mathcal W_D$ 的合法列。

## 8. 对原同 R 问题的新增限制和未付部分

R731 从指定首位吸收得到实际非立方核 $P_B$；
本篇进一步给其完整原首次修正的强制值：
所有可行修正都必须离开 $F$-整除方向，
且不能保持原整因子分解。
该结论由两块的完整组合给出，
无须低 $\rho$ 门，也无须丢掉原实际 $\xi$。

原问题还包括：

1. (31) 的指定 jet 是否落在完整原 $\mathcal V_D$ 中，
   以及满足它的同一个 $R$ 如何作用于全部剩余块；
2. 在原 $M$ 中两条十三行 carry、原 $P_{134}/U_0$、
   低行右逆的完整高尾及 $U_1/p$；
3. 第一提升后，以这个同一个 $R$ 计算原 $p^3$ 障碍，
   不能为后续行块重新选择另一修正；
4. 原完整中央失败对上述真实仿射解空间的约束。

本篇没有让 (29) 的商自动非零，
没有新增来源或中央零，
也没有把因子保持型的排除替换成完整原首次不可解。

依赖：
[R502](R502-full-low-ell-bockstein-and-actual-geometric-residue.md)；
[R547](R547-zero-charge-vertical-unit-block-and-actual-cubic-schur-column.md)；
[R730](R730-specified-ramification-class-linear-contact-bound-and-actual-mirror-kernel.md)；
[R731](R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md)；
[R731 全第三块增补](../notes/2026-11-15-r731-complete-third-carry-and-high-rho.md)。
