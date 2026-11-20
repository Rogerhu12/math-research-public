# R141 补篇：用准确 WOB 提升接入原 WPN 两行右端

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**本篇是条件性算子证明与纯标量源码合同，尚未执行新的科学计算。** 它以同一个真正 full-family 的完整低高、physical 外块门和14列端口响应已经完成为前提，将原 WPN 的任意有限行与完整径向零均值尾行准确转成普通源及两个已声明边界端口。它不要求对任意 $L^2$ 右端求导或取端点，不把独立 low jump 的 Dirac 当作 ordinary 零源，也不把旧 finite-$\rho$ / WJK trial 的充分门改写为通过。

以下 $A_L,B_{HL},B_{LH},G_H$ 始终是真正原 full-family 算子。R141 单独的 $A_{L,c}[Q_\delta]$ 是 same-$\eta_\delta$ hybrid；只有已付的完整 $\Delta A_L,\Delta B_{HL},\Delta B_{LH}$ 与实际高逆恢复后，才能进入本篇。准确关系是

\[
A_c[Q_\delta]=\eta_\delta J\partial_\phi+K(Q_c),\qquad
\Delta A=K(Q_\delta)-K(Q_c),\qquad
A_c[Q_\delta]+\Delta A=DF(Q_\delta).
\tag{L.1}
\]

$K$ 包括 drift、全部有序 primitive、输出 mean 和方向 mean rank。共享 principal 已在 $A_c$ 内，不能再把 $(\eta_\delta-\eta_c)J\partial_\phi$ 重付一次；也不能把单独的 hybrid 当成 R138 固定几何的 $DF(Q_c)$。

## 1. 原 WOB square 的两个独立输出域

沿用 [WOB.24–WOB.31](R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md)。令 $E_L$ 为原193维 normalized real fiber，$E_c:\mathbb R^{96}\to E_L$ 插入 even nonmean，$E_d:\mathbb R^{97}\to E_L$ 插入 odd96 与独立 moving mean；它们是正交嵌入。

设 $V_0q(r)=\int_{r_*}^r q(s)\,ds$、$V_{0,R}q=\int_Iq$，$C_*v$ 为常函数 $v$。取真正零独立高端口的两列

\[
\mathcal P_a=G_HB_{HL},\quad \mathcal P_b,
\qquad Y_a=\operatorname{Tr}_{R,e}\mathcal P_a,\quad
Y_b=\operatorname{Tr}_{R,e}\mathcal P_b,
\]
\[
H=A_L+B_{LH}\mathcal P_a,\qquad F_b=B_{LH}\mathcal P_b.
\tag{L.2}
\]

原 unknown 是 $(a,d,b)$，其中

\[
a\in L^2(I;E_L),\quad d\in\mathbb R^{97},\quad
b\in P_\ell H^{-5/6}_{\rm even}.
\tag{L.3}
\]

$b$ 的原Hilbert坐标是 $\Theta b$；以下在写实际函数式时仍用原 $b$，在写范数时用其 $H^{-5/6}$ norm。原独立输出为

\[
(F,e)\in L^2(I;E_L)\oplus E_L.
\tag{L.4}
\]

第二块 $e$ 是193维 raw endpoint **方程右端**；不是任意 $F$ 的端点。精确 square 为

\[
\begin{split}
a-C_*E_dd-V_0(Ha+F_bb)&=F,\\
E_dd+V_{0,R}(Ha+F_bb)
 -B_R^HY_aa-(B_R^\ell+B_R^HY_b)b&=e.
\end{split}
\tag{L.5}
\]

这里 $B_R^\ell$ 和 $B_R^H$ 保留 WOB.3–WOB.4 的全部 genuine physical-angle/Robin/mean 图。特别地

\[
E_c^*B_R^\ell b=b,\qquad E_c^*B_R^Hy_H=0.
\tag{L.6}
\]

第二个零只针对 even **非均值**96输出；$B_R^H$ 的 even mean输出不为零。$E_dd$、$e$ 和全部积分的原符号如(L.5)，没有将外mean塞进 ordinary源。

## 2. 常数提升：只让真正 ODE 解承担端点

将 $e$ 正交拆成

\[
c=E_c^*e,\qquad e_d=E_d^*e,\qquad
e=E_cc+E_de_d.
\]

定义

\[
\ell=C_*E_cc,\qquad k=F+\ell,\qquad a=k+w.
\tag{L.7}
\]

把(L.7)代入第一式后，准确得到

\[
w=C_*(E_dd-E_cc)+V_0(Hw+Hk+F_bb).
\tag{L.8}
\]

因为 $H:L^2\to L^2$ 有界，$w$ 是真正 $H^1$（原系数 seam 上为原对应的 piecewise $H^1$）状态。其 root 及 outer 迹有定义；$F,k,a$ 的一般 $L^2$ 迹始终没有被使用。

令

\[
h=G_H(B_{HL}w+B_{HL}k)+\mathcal P_bb.
\tag{L.9}
\]

则 $h=\mathcal P_aa+\mathcal P_bb$，而(L.8)等价于

\[
w'=A_Lw+B_{LH}h+\underbrace{A_Lk}_{f_L},\qquad
L_Hh=B_{HL}w+\underbrace{B_{HL}k}_{f_H},
\]
\[
E_c^*w(r_*)=-c,\qquad E_d^*w(r_*)=d.
\tag{L.10}
\]

未知 outer $b$ 所产生的高 Poisson列仍是 $\mathcal P_bb$；它不被再次作为独立第4高端口输入。这里的新独立高数据只有 ordinary $f_H$ 的 collar/body两段；stable、原高jump和独立高外输入均为零。

由(L.8)，第二式(L.5)准确化为

\[
w(R)=B_R^\ell b+B_R^Hy_H+e-E_cc.
\tag{L.11}
\]

利用(L.6)，因此 $E_c^*w(R)=b$。以原 $p_0=13/80$ 定义 reference right97数据，则本次 already-charted 源准确是

\[
g_e=(\Theta e^{\rm odd},e^{\rm mean}),\qquad
r=A_bb+A_hy_H+g_e.
\tag{L.12}
\]

没有额外的 $p_0c$：$c$已在(L.11)的 even96输出中被准确消去；reference Robin中的 $p_0b$ 与原 $A_b$保持在同一边。moving mean属于 $e_d$，完整保留；它不被当作独立 physical density-mean residual。

所以任意(L.4)只需[14列合同](R141-supplement-original-seven-ports-after-the-physical-gate.md)的以下5列：

| 原零基列号 | 本次准确输入 |
|---:|---|
| 1 | $P_{I_c}B_{HL}k$，原 ordinary $L^2H^{-2/3}$ |
| 2 | $P_{I_b}B_{HL}k$，原 ordinary $L^2H^{-2/3}$ |
| 7 | $A_Lk$，raw low $L^2$ |
| 9 | $-c$，raw root-even96 |
| 10 | $(\Theta e^{\rm odd},e^{\rm mean})$，already-charted right97 |

此表规定的是准确线性注入。符号在求解时保持；取非负norm表时才使用 $\|c\|$ 和 $\|g_e\|\le\|e_d\|$。同一 $k$同时驱动三条ordinary源，不声称它们是独立输入或输出正交。

## 3. 反向代入与全部独立 atoms

假设未来同一真实physical问题对(L.10)–(L.12)已经有完整有界逆。先解出 $w,h,b$，置 $d=E_d^*w(r_*)$，再以(L.7)恢复 $a$。式(L.8)给第一原WOB行，式(L.11)给第二原WOB行，$h=\mathcal P_aa+\mathcal P_bb$给原高返回。反过来，每个(L.5)解通过(L.7)给同一个(L.10)–(L.12)解，因此该对应是双向的；不会产生仅提升变量非零的伪核。

恢复的Hilbert输出是

\[
(Sa,d,\Theta b)\in
L^2(I;E_L)\oplus\mathbb R^{97}\oplus\mathbb R^{96}.
\tag{L.13}
\]

这193个atoms是原WOB独立有限坐标，具体由 $w$的合法迹读出。$d=E_d^*w(r_*)$，$\Theta b=\Theta E_c^*w(R)$；$E_c c$不改变root97投影。没有把它们定义为任意 $a$ 的迹。P224表的right97在这条一般 $L^2$路由中是辅助解 $w$ 的reference数据；它不被称作 $a$ 的outer Robin迹。

对于原物理来源使 $a$具有真实或piecewise $H^1$正则性的特殊RHS，可以再由原(L.5)/WOB31恢复其实际物理迹。这个额外辨认不从一般Hilbert输入自动推出。

## 4. 两个原 WPN 行的准确重组

令 $E_N$ 为原 $N=24480$ 细胞的 normalized cellconstant embedding，$P_N=E_NE_N^*$、$Q_N=I-P_N$，$S$是同一原piecewiseconstant坐标，**不是**R141用于认证的1424格坐标。

原有限RHS写作 $f_f=(f_{\mathrm{cell}},e)$；完整尾行 $g_t\in Q_NL^2$。定义

\[
f=E_N f_{\mathrm{cell}}+g_t,\qquad F=S^{-1}f.
\tag{L.14}
\]

于是 $E_N^*f=f_{\mathrm{cell}}$、$Q_Nf=g_t$，这是原 [WDS.2–WDS.3](R133-supplement-two-sided-tail-residuals-and-true-finite-Schur-certificate.md) 的准确逆坐标变换。一般 $g_t$没有置零，也没有用两径向moments替代它。

解出(L.13)后，原WPN unknown为

\[
x=(E_N^*Sa,d,\Theta b),\qquad z_{\rm raw}=Q_NSa.
\tag{L.15}
\]

这里 $z_{\rm raw}$沿WPN命名仍指原tail Hilbert坐标，不是撤掉 $S$后的点态raw fiber。正交性准确给

\[
\|(x,z_{\rm raw})\|^2
=\|Sa\|_{L^2}^2+|d|^2+|\Theta b|^2.
\tag{L.16}
\]

因此(L.13)的完整范数正是原有限加无限tail输入空间的范数。不能把finite状态bound与tail状态bound平方相加而把同一body算两次；若单独需要，$\|x\|$由(L.16)控制，$\|z_{\rm raw}\|\le\|Sa\|$。

本路线直接解原WOB square，故它不使用未知 $R^{-1}$、旧WJK trial $F$或旧 $Q_f\Delta_\rho$来构造此源路由。它没有证明原finite-$\rho$充分门、$e+3dt<1$或旧trial的实际残差变小。若后继仍使用原 WPN.7/15 的trial级数、旧finite inverse常数或旧paired-source circuit，必须另给同一 $G_H$与旧$F$差/finite-$\rho$桥；不从本篇直接写那些旧flag为true。

反之，若未来真实physical gate、所有用到的端口有界性和本篇实际响应表均已完成，则(L.7)–(L.16)本身就是同一完整WPN四块算子的有界双侧逆构造。这是一条新的直接证明，其假设和新响应表必须真实支付；当前无此成功结论。

## 5. 不重算旧界的具体范数费用

从已成WHVA run43838214094/1的完整原件只读

\[
G=\texttt{A\_infty},\quad A_c=\texttt{A\_c},\quad
A_b=\texttt{A\_b\_from\_L},\quad t_0=\texttt{C\_R0}.
\tag{L.17}
\]

其中 $G\ge\|A_L\|$作用在完整raw193低fiber，$A_c,A_b$是同一真实 $B_{HL}$从raw low-$L^2$到原 ordinary $H^{-2/3}$的两个区域费，$t_0\ge\sqrt{|I|}$。WHVA的旧N4096充分门false不影响这四条已完成的完整算子上界；不重跑旧最大值或任一旧scalar。

原exact reference规则的body $q\ge1/8$、collar $q=1$给 $\|S^{-1}\|\le8$。该规则是原 `fourfold_codazzi_frozen_cross_block_value_tail.py::exact_reference` 的精确 floor，不从一个展示小数猜测。

另只读已成D run44745017016/1的

\[
d_B=\texttt{reference\_weighted\_right97\_body\_upper}.
\tag{L.18}
\]

它也支配 $\|SC_*E_c\|$。理由是参考独立mean的单位右输入解为常数1，body norm精确为 $(\int_Iq^2)^{1/2}$；常数even96向量受同一 $q$作用，normalized real basis使其operator norm为同一数。用完整right97 body上界支配这个子列合法，未声称常数even列解参考ODE，亦无 $\sqrt{96}$。

设 $h=\|f\|$、$c_0=\|c\|$、$u_0=\|e_d\|$。由(L.7)、(L.14)，

\[
\|k\|_{L^2}\le8h+t_0c_0,
\qquad \|Sk\|_{L^2}\le h+d_Bc_0.
\tag{L.19}
\]

令 $P_{\alpha j}$ 为未来完整224表第$j$输入到第$\alpha$输出的已存有向upper。对每个输出定义

\[
C_\alpha=A_cP_{\alpha1}+A_bP_{\alpha2}+GP_{\alpha7}.
\tag{L.20}
\]

先对已求 $w$及返回高状态取三角式：

\[
Y_\alpha\le8C_\alpha h+
 (t_0C_\alpha+P_{\alpha9})c_0+P_{\alpha10}u_0.
\tag{L.21}
\]

对 `low_body` 和 `low_complete`，恢复 $a=k+w$后还要加(L.19)的 $h+d_Bc_0$。对root97、outer96、joint193及高返回行不加这个body费用；其合法观察已经由第3节固定。

记由此得到的三个非负系数为 $(a_\alpha,b_\alpha,c_\alpha)$。给定 $g_t=0$，$f_{\mathrm{cell}}$、$c$和$e_d$在原有限输入中正交，因此

\[
U_{\alpha,f}=\sqrt{a_\alpha^2+b_\alpha^2+c_\alpha^2},
\qquad U_{\alpha,t}=a_\alpha
\tag{L.22}
\]

分别界整个有限RHS和整个tail RHS两列。第二列取 $f_{\mathrm{cell}}=e=0$，保任意 $g_t$。该平方和只来自**输入**直和的Cauchy–Schwarz；输出不被声称正交。对于同时给定的两行，

\[
Y_\alpha\le U_{\alpha,f}\|f_f\|
                 +U_{\alpha,t}\|g_t\|.
\tag{L.23}
\]

low-complete行与(L.16)给整个四块解的norm；low-body行给tail单独norm。两列只是明确的有界算子响应，还不是某个实际 $\nu$、Newton或外功能RHS的大小。那些RHS自身须另外完整组装并认证。

## 6. 真正物理来源、root96 与独立 low jumps

原WOB31保留全部输入时的raw pair准确是

\[
\begin{split}
F={}&C_*E_cc_*+V_0\Phi x+V_0q_p+J_0\mathbf j,\\
e={}&Q_LB_{R,p}p+B_R^Hy_p-V_{0,R}q_p-\sum_\alpha j_\alpha
      -E_cc_*-(V_{0,R}\Phi-B_R^H\Upsilon)x.
\end{split}
\tag{L.24}
\]

按(L.14)反向，即 $f_f=(E_N^*SF,e)$、$g_t=Q_NSF$。所有ordinary source、height、mean、$\nu$及affine的两条路径均须放入(L.24)；同一输入在两行有相关性，先形成准确式，再取whole norm，不把一行设置为0。

对纯 prescribed-root $c_*$，准确 pair为 $(C_*E_cc_*,-E_cc_*)$，所以 $k=0$、root输入 $-c=c_*$、right97和ordinary源均为0。这正好落在原第9列。$S$在每原fine cell为常数使 $g_t=0$；这是这一个完整pair的恒等式，不是对一般source的结论。恢复后真实root-even96等于 $c_*$，无需另做同一identity的数值determinant。

对真正内部 low jump $j_\alpha$于 $r_\alpha$，其pair必须是

\[
F=J_0\mathbf j=\sum_\alpha 1_{[r_\alpha,R]}j_\alpha,
\qquad e=-\sum_\alpha j_\alpha.
\tag{L.25}
\]

完整阶跃进入 $k$，$w$仍按ordinary $L^2$源求解；$a=k+w$有准确原jump，未把Dirac直接塞入 $L^2$。独立high jump继续按原七端口，不包含在(L.25)内。若某jump在一个fine cell内部，$Q_NSJ_0\mathbf j$一般非零；不得借网格接口假设删除。

具体输入norm仍由其原来源决定。对有限给定jumps，一个合法整上界为
$\|J_0\mathbf j\|\le\sum_\alpha\sqrt{R-r_\alpha}\,\|j_\alpha\|$、$\|\sum j_\alpha\|\le\sum\|j_\alpha\|$；若输入声明为加权序列空间，则必须使用其完整对应的step-map norm。这里没有给impulse加一个假的 $\sqrt{h}$，也没有凭14列存在自动授所有jump源大小。

若实际源光滑且已经以ordinary low源和原七高port给出，可以直接用P224表；这与(L.24)后再lifting是两个等价组织，不能把同一数据在两个组织中各注入一次。

## 7. 高输出与 rough baseline 的边界

在一般WPN pair路线中，独立high资料已经通过(L.24)收进 $(F,e)$。本次(L.9)输出是**零独立高端口返回** $\mathcal P_aa+\mathcal P_bb$，不是已包含外部baseline $v_p$或 rough stable解的全高状态。后继按原单位将它们加回一次。

若某更粗NIF输入只已付 $\Phi x$、$\Upsilon x$等兼容观察，则(L.24)与low square仍可使用那些whole观察；不能因为本返回属于原 $L^2H^{-1}$窗，就把更粗baseline免费升级到whole raw-$H^{-1}$。真正mixed-root、waist、density、$\Theta$和其逆变换仍按原完整receiver逐项恢复。

同理，$\nu$在正区某compact intrinsic bump的局部直接source可以有已证明的零；这不删除其germ/负区/接口/外功能带来的其他原RHS。独立的两个physical-density mean、metric或未知函数也不因为moving mean留在193维里就被消去。若它们是未知量，保持原operator block；本篇只对它们作为给定输入的已组装pair给响应。

## 8. 可执行消费与真正未付的量

纯模块 `fourfold_codazzi_WPN_two_rows_lifted_response_math.py` 实现(L.20)–(L.22)，只读未来完整224表、当前完整D与WHVA。它不import数值库或执行旧producer。输出按 finite-RHS16行、tail-RHS16行的顺序，保存32个新whole upper。每条先完整写入/读回/检查包含原upper，后继只消费保存球的上端。

owner必须先核同对象58量门、全部224完整records与原14输入16输出次序、全旧scope、D同 $S$身份、WHVA的完整科学文件及execution。缺low、low失败prefix、完整2目标false、58门未过或224未完整时均不得运行本合同。不给未来文件填dummy，不把known上界当signed解。

本次未形成这些未来输入、未生成科学manifest、未求值32量。实际独立RHS的全source/mean/height/$\nu$/jump大小、其完整 $(f_f,g_t)$ 球、实际特定解或近似解的两行残差仍待相应新目标；原negative连接、完整几何读出与非线性课题验收仍未完成。
