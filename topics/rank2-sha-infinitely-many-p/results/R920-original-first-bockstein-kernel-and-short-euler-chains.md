# R920 — 原完整首 Bockstein 核的精确 Euler 后继与三／四来源联合秩

日期：2026-11-16。**状态：以下负 fringe 中的完整首 Bockstein 核、精确 Euler 后继、三／四来源链排除及真实维数界已证明。未证明整个原核稳定，未判定指定第二／第三页仿射类；主目标仍未完成。**

[R918](R918-original-stable-direction-carry-unit-and-native-endpoint.md)
在特殊零纤维的稳定方向上给出原十三带单位行。本篇保留完整首 Bockstein，
并回到一般原零纤维：只要接触处在同一个负 fringe，
两个确实能够续接的来源之间，R907 的 $F^3$ 反馈系数就必须为零。
因此三、四个真实来源分别给同一来源的五、六条长行，
不再需要先合成六次 $Q_f$。

全部论证在同一个已付 $q_{\rm src}t^r\mathcal H_3$ 子格进行。
原 $\mathcal W_D$ 的其它列、三个十三行 carry、原末端四次项以及
同一 $R/S$ 的其它条件均保持。

## 1. 原格、完整首 Bockstein 和准确假设

保持
[R907](R907-original-two-step-successor-and-six-dimensional-fiber-feedback.md)
与 [R914](R914-original-nonstable-kernel-eight-nine-step-cutoff-and-joint-rank.md)
的原十九角曲面 $X$、几何整曲线 $C=(F=0)$、光滑点 $P=(0,1)$，
以及
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad
\kappa=C^2,\quad
b=\deg_YF,\quad
\mathcal E=Y\partial_Y,\quad e=\mathcal EF.
\tag{1}
$$
仍取原
$$
r=2,\qquad C.f_0=3,\qquad b\ge5,\qquad
3b<p,\quad p=6s-1>211,
$$
$$
F(t,0)\ne0,\qquad \gamma=e(P)\ne0.
$$
这里 $f_0$ 是原严格零纤维；不将 $F$ 在 $(0,0)$ 的偶然零
赋给整个 $\mathcal H_j$。

只使用已整返回同一原预算的来源
$$
\boxed{
\jmath:\mathcal H_3\longrightarrow\overline{\mathcal W_D},
\qquad G\longmapsto q\,t^rG,\qquad q=q_{\rm src},\quad q(P)\ne0.
}
\tag{2}
$$
$q$ 的全部 charge、原 $P_{134}$、$c_*U_0$、
固定角与原总 charge 四十均在这条返回中。
不假设 $\mathcal Eq=q$，也不要求 $q(0,Y)$ 只有一个 charge。

写同一实际轴
$$
g=\psi\exp\eta,\qquad \operatorname{ord}_t\eta=h,\qquad
F(t,g)=t^h u_t(t),\quad u_t(0)\ne0.
$$
原长度及强窗为
$$
\boxed{
T=s-r-13,\quad L=\max(\ell-r,0),\quad
h<T\le2h,\quad T-h>\kappa,\quad
T-h\le L\le h.
}
\tag{3}
$$
另保原物理 $0<\ell<s-13$。
本篇不使用 $L>h$；R911 中该较长短窗的结论不代替这里的原窗口。

定义同一个完整四块首核
$$
K=\left\{G\in\mathcal H_3:
(\mathcal E^jG)(t,g)\in(t^T)\ (0\le j\le2),\
(\mathcal E^3G)(t,g)\in(t^L)\right\}.
\tag{4}
$$
R836 的完整单位下三角运输给 $\jmath(K)\subset K_1=\ker\overline M^{\rm orig}$。
令
$$
\beta_1:K_1\longrightarrow\operatorname{coker}\overline M^{\rm orig}
$$
为同一整矩阵的**完整**首 Bockstein，并置
$$
\boxed{K'=K\cap\ker(\beta_1\circ\jmath).}
\tag{5}
$$
(5) 不是仅要求下文三条显示 carry 为零。

记
$$
J=s-r=T+13,\qquad
\delta=r+2h-s=2h-J.
$$
本篇的新范围准确是
$$
\boxed{-13\le\delta<0,\quad\text{即}\quad 2h<J\le2h+13.}
\tag{6}
$$
左端由 $T\le2h$ 已保证，右端是额外的真实负 fringe 条件。

### 1.1 本篇所用低阶不等式在原强窗中已经支付

R815 对原 $C.f_0=3$ 的完整 nef 界给
$$
\kappa\ge6b-9\ge21.
$$
由 $T\le2h$ 与 $T-h>\kappa$，
$$
h\ge T-h>\kappa\ge21,\qquad
L\ge T-h>\kappa,\qquad \ell=r+L>4.
\tag{7}
$$
所以以下所需的 $h>13$、$\ell>4$、$s-13>4$ 都不是额外猜测。
这里使用的是原 $b\ge5,\ C.f_0=3$ 分支；
若换成其它来源类，必须重新明示这些门。

另记 R907 已逐 charge 支付的统一帽
$$
e_+=C.H_+,\qquad R_C=3(e_++\mu_{0,1}).
\tag{8}
$$
对每个 $0\ne G\in\mathcal H_3$，
$$
v_G:=\min_n\operatorname{ord}_t[Y^n]G\le R_C<T.
\tag{9}
$$
最后严格号由 R819 的
$\kappa\ge(b-3)e_++3b$、$\mu_{0,1}\le b-3$ 和 $T>2\kappa$ 给出。
(9) 用整个原 $G_m$ 直和，不只检查最高 charge。

## 2. 完整首 Bockstein 真正把前三行延长十三位

采用同一个 Hasse 对齐后的完整实际轴和参考运输。
令
$$
\mathcal U(w)=c_*U_0^\flat(w)\in k[[w]]^\times,\qquad
t(w)=t_1w+O(w^2),\quad t_1\ne0.
$$
对 (2)，实际四个读取仍为
$$
W_j(\jmath G)=
\mathcal U(w)t(w)^r
\bigl[(\mathcal E+40)^j(qG)\bigr](t(w),g(w)).
\tag{10}
$$
原参考坐标写法与 (10) 的转换包括公共载体的全部高轴变化。

原三 carry 注
[§1–3](../notes/2026-11-16-r828-three-native-carry-recursions-and-last-block-tails.md)
给 $1\le j\le3,\ 0\le i\le12$ 的首 Bockstein 行
$$
\frac{a^{j-1}}{(j-1)!}
\left(
[w^{s-13+i}]W_{j-1}
+H_p[w^{i-9}]BW_j
\right),
\qquad a\in k^\times.
\tag{11}
$$
这些真实行杀整个 $\operatorname{im}\overline M^{\rm orig}$，
所以 $\beta_1(\jmath G)=0$ 确实迫 (11) 为零；
不是另选一个提升使其为零。

对 $G\in K$，原首核已有
$$
W_0,W_1,W_2\in(w^{s-13}),\qquad W_3\in(w^\ell).
\tag{12}
$$
由 (7)，(11) 中所有 $H_p$ 项只读 $\le3$ 阶且全部为零。
因而对 $G\in K'$，
$$
\boxed{W_0,W_1,W_2\in(w^s).}
\tag{13}
$$
若先在原参考上使用 (11)，参考改成完整实际轴的一次差从
$w^{s-4}$ 起，在所读 $<s$ 行中只乘 $W_1,W_2,W_3$ 的 $\le3$ 阶；
它们由 (12)、$\ell>4$ 同样为零。
二次差从 $w^{2s-8}$ 起，严格在所读窗外。
故 (13) 是 (10) 的实际原轴结论，不把参考 $g_0$ 当成完整 $g$。

现在才按原单位下三角逆运输 (13)。
$\mathcal U$ 为单位，$t/w$ 为单位，且
$(\mathcal E+40)^j(qG)$ 关于 $G,\mathcal EG,\ldots,\mathcal E^jG$
的对角是同一个 $q(t,g)$ 单位。于是
$$
\boxed{
G(t,g),\quad(\mathcal EG)(t,g),\quad
(\mathcal E^2G)(t,g)\in(t^J)
\qquad(G\in K').
}
\tag{14}
$$
$J=T+13$ 来自原三条十三带；第四短行仍然只是长度 $L$。
(14) 只是完整 $\beta_1=0$ 的必要条件，不是其充分条件。

## 3. 同一来源的两个完整值都落在更深的真实截面格

记
$$
V_i(G)=(\mathcal E^iG)|_C,\qquad
V_J=H^0(C,N^3(-JP)),\qquad n_J=\dim_kV_J.
\tag{15}
$$

**引理 1。** 对每个 $G\in K'$，
$$
\boxed{V_0(G),V_1(G)\in V_J.}
\tag{16}
$$
两条映射 $V_0,V_1:K'\to V_J$ 各自单射。

**证明。** 同一轴的有限逆 Taylor 身份给
$$
\begin{aligned}
V_0(G)&=G(t,g)-\eta\,\mathcal EG(t,g)
+\frac{\eta^2}{2}\mathcal E^2G(t,g)\pmod{t^{3h}},\\
V_1(G)&=\mathcal EG(t,g)-\eta\,\mathcal E^2G(t,g)
+\frac{\eta^2}{2}\mathcal E^3G(t,g)\pmod{t^{3h}}.
\end{aligned}
\tag{17}
$$
这里仅使用二阶 Taylor，$p>211$ 保全部分母为单位。
由 (6)、(7)，$3h>J$；
又由 (3)，
$$
2h+L\ge h+T=J+h-13>J.
\tag{18}
$$
所以 (14)、原第四短行与 (17) 给 (16)。
全局截面性仍来自原十九角 Euler 保格，没有用局部级数代替全局提升。
单射直接继承 R834/R902 在同一个 $K$ 上已付的值、第一法向值单射。证毕。

$n_J$ 始终是真实维数。
当 $J>3\kappa$ 时，次数为负而 $n_J=0$，于是 $K'=0$。
其它范围不假设非特殊性，也不把 Riemann–Roch 的 Euler 特征当作 $n_J$。

## 4. 负 fringe 中真实后继准确等于 Euler

沿用 R907 的同源算子
$$
a(G)=\frac{(\mathcal E^4G)(P)}{6\gamma^3},\qquad
\mathcal TG=\mathcal EG-a(G)F^3.
\tag{19}
$$

**定理 2。** 若 $G,H\in K'$ 且作为整个 $C$ 上的限制截面有
$$
V_1(G)=V_0(H),
\tag{20}
$$
则
$$
\boxed{a(G)=0,\qquad H=\mathcal EG.}
\tag{21}
$$
反之，对给定 $G\in K'$，这个后继在 $K'$ 中存在，
当且仅当 $\mathcal EG\in K'$；存在时唯一。

**证明。** 因 $G,H$ 同在原 $K$，R907 的同一限制序列给
$H=\mathcal TG$。
该结论实际先得到
$\mathcal EG-H=F^2A$、$A\in\mathcal H_1$，
再由 $T-h>\kappa$ 得 $A=cF$，
最后由 $H$ 的第四短行固定 $c=a(G)$。
所有商的原次数帽已在该限制序列中支付。

对这条完整等式作用 $\mathcal E$，得
$$
(\mathcal EH)(t,g)-(\mathcal E^2G)(t,g)
=-a(G)\,\mathcal E(F^3)(t,g).
\tag{22}
$$
左边两项分别由同一个 $H,G$ 的 (14) 属于 $(t^J)$。
另一方面，
$$
\mathcal E(F^3)=3F^2e,\qquad
\operatorname{ord}_t\mathcal E(F^3)(t,g)=2h<J,
\tag{23}
$$
且首系数 $3u_t(0)^2\gamma$ 非零。
所以 (22) 迫 $a(G)=0$，证明 (21)。
反向若 $\mathcal EG\in K'$，其值就是 $V_1(G)$；
唯一性由引理 1。证毕。

这里没有对任意 $G\in K'$ 添加下一条 Euler 零行：
(21) 只在真正满足 (20) 的两来源之间成立。
特别，$\mathcal E K'\subset K'$ 仍未证明。

### 4.1 真稳定部分为零，不需特殊零纤维

定义
$$
K'_\infty=\{G\in K':\mathcal T^jG\in K'\text{ 对所有 }j\ge0\}.
\tag{24}
$$
每对相邻的实际迭代均满足 (20)，故由定理 2，
$\mathcal T^jG=\mathcal E^jG$。
因此 $K'_\infty$ 是真实 Euler 稳定子空间。
原 charge $0,\ldots,3b$ 在 $k$ 中互异；
非零稳定子空间必含一个非零纯 charge 投影。
它由 (9) 的阶帽不能通过第一长行，矛盾。故
$$
\boxed{K'_\infty=0.}
\tag{25}
$$
这不需要 R916 的 $F(0,Y)=Y^2(Y-1)$ 或六系数非零分类，
也不把 (25) 改写成 $K'=0$。

## 5. 只在已付轴精度内使用五／六长根能量

置
$$
\boxed{S=\min(J,s-4).}
\tag{26}
$$
原 R821(10) 的实际 $g$ 在 Gaussian 项之前同
$\rho=(1+8t)\Theta^{17}$；
R821(18)–(20) 的四轴参考与实际轴的差从 $t^{s-4}$ 才开始。
因此无论采用该同源运输的哪一种书写，
在本篇使用的精度内都有
$$
\boxed{g\equiv\rho\pmod{t^S}.}
\tag{27}
$$
这是原公式支付的比较，不将高轴或 $H_p$ 自由删除。

因为 $r=2$，
$$
S=s-4=T+11,\qquad R_C<T<S\le s.
\tag{28}
$$
保留 (26) 的形式可明确每次读取的原上限；
并未把所有实际 $g$ 或参考延长到未经支付的模 $t^s$ 等式。

R911§3 的全重数原十九角根能量只要求真实
$0\ne G\in\mathcal H_3$、$v_G<S\le s$、(27) 及指定五／六长行，
**不要求 $L>h$**。它给
$$
\begin{array}{ll}
(\mathcal E^jG)(t,g)\in(t^S),\ 0\le j\le4
&\Longrightarrow\quad 13(S-v_G)\le27\kappa+312b,\\[2mm]
(\mathcal E^jG)(t,g)\in(t^S),\ 0\le j\le5
&\Longrightarrow\quad 16(S-v_G)\le27\kappa+384b.
\end{array}
\tag{29}
$$
其中 $27\kappa$ 来自同一真实 $3C$，
重复因子、所有十九角、固定五／六阶 frontier 和正特征导数范围
都沿用该证明；这里没有增加多项式乘子或换成环境格。

记两个明确反门
$$
\boxed{\mathsf B_5:\quad13(S-R_C)>27\kappa+312b,}
$$
$$
\boxed{\mathsf B_6:\quad16(S-R_C)>27\kappa+384b.}
\tag{30}
$$
它们仍是条件，不宣称所有原 profile 自动满足。
R914 使用 $T$ 的相应 $\mathsf A_5/\mathsf A_6$ 分别蕴含 (30)，
因为 $S>T$；原 $D/s/\ell$ 预算没有改变。

**定理 3。**

- 在 $\mathsf B_5$ 下，若 $G_0,G_1,G_2\in K'$ 且
  $V_1(G_i)=V_0(G_{i+1})$，$i=0,1$，则三个来源全为零。
- 在 $\mathsf B_6$ 下，若 $G_0,G_1,G_2,G_3\in K'$ 且
  $V_1(G_i)=V_0(G_{i+1})$，$i=0,1,2$，则四个来源全为零。

**证明。** 定理 2 沿每条实际相等逐次给
$G_i=\mathcal E^iG_0$，没有先假稳定。
每个 $G_i$ 本身有 (14) 的三个长行。
三个来源因此给 $G_0$ 的 $0,\ldots,4$ 阶长行至 $J$，
四个来源给 $0,\ldots,5$ 阶长行至 $J$。
降到已付比较长度 $S$，应用 (29) 和 $v_{G_0}\le R_C$，
在对应 (30) 下若 $G_0\ne0$ 即矛盾。
所以 $G_0=0$，再由 (21) 其余全零。证毕。

等价地，所示反门分别给真正有限交
$$
\boxed{
\bigcap_{j=0}^2\mathcal T^{-j}K'=0\quad(\mathsf B_5),
\qquad
\bigcap_{j=0}^3\mathcal T^{-j}K'=0\quad(\mathsf B_6).
}
\tag{31}
$$
每个逆像都是原完整首 Bockstein、四块和全部来源帽的共同测试。

## 6. 三／四来源的真实联合秩

定义同一个深值格中的线性链映射
$$
\mathcal C'_2:(K')^3\longrightarrow V_J^2,
\quad
(G_0,G_1,G_2)\longmapsto
\bigl(V_1G_0-V_0G_1,\ V_1G_1-V_0G_2\bigr),
\tag{32}
$$
以及
$$
\mathcal C'_3:(K')^4\longrightarrow V_J^3,
\quad
(G_0,G_1,G_2,G_3)\longmapsto
\bigl(V_1G_i-V_0G_{i+1}\bigr)_{i=0}^2.
\tag{33}
$$
引理 1 支付了这些映射的实际目标。
定理 3 分别证明它们单射，故
$$
\boxed{
3\dim K'\le2n_J\quad(\mathsf B_5),\qquad
4\dim K'\le3n_J\quad(\mathsf B_6).
}
\tag{34}
$$
这是同一对 $V_0,V_1$ 的联合链秩，
没有把两个端点单射或两个显示子块直接相加。

对完整首 Bockstein 在本原子格上的限制，(34) 同时给
$$
\operatorname{rank}(\beta_1\circ\jmath|_K)
\ge
\max\!\left\{0,\dim K-\left\lfloor\frac{2n_J}{3}\right\rfloor\right\}
\quad(\mathsf B_5),
\tag{35}
$$
以及在 $\mathsf B_6$ 下将 $2n_J/3$ 换成 $3n_J/4$ 的对应界。
若两门同时成立，可取较强者。
这是完整第一页的秩限制，不据此指定所有 Smith 指数或更高页。

## 7. 同一修正与尚未关闭的范围

本篇每个 $G_i$ 必须各自在 (5) 的**完整**核内，
而不是只满足 (13) 或 (14)。
原第一／第二／第三页继续使用同一个 $P,R,S$：
本篇没有赋给 $\mathcal TG$ 新的中央零，也没有为三条带分别选择修正。
若固定一个 $P$，其首修正的差一般仍属于整个 $K_1$；
不能未经原下一页论证就把该仿射差空间替换成这里的 $K'$。
只有实际已识别为本篇同源差或同源链的部分，才能应用 (31)–(35)。

边界 $\delta=0$ 时，(23) 的首项恰在第 $J$ 阶，
不被 $<J$ 的长行读取，因而不能迫 $a(G)=0$。
R918 的 native 行在该边界允许并实际指定一个非零第 $J$ 阶值；
本篇不将它抹成更深消失。
$\delta>0$ 时更不能使用 (23) 的负 fringe 论证。

因此 (25)、(34) 没有排除全部非稳定 $K'$，
没有给原 $W_T$ 或指定 $[b_0]$ 满像／零像，
也未解决原非齐次 forcing。
所有 $q$ 的 Euler 项、$U_0/P_{134}$ 完整尾、
三个十三行带、原第四短行、十九固定边界与 conductor，
以及同 $R/S$ 的其它 normal 条件均保持。

依赖：R815/R819 的实际 $m_0=3$ 角界，R821 的四轴及真实精度，
R828 三 carry 注，R836 的原单位运输与全局限制，
R907 的真实后继和逐 charge 帽，R911 的五／六长全重数根界，
以及 R914/R918 的原窗口与端点范围。
本篇为同来源代数证明，没有新增数学运行或数值证书。

## 附录 A. 同一个固定 $P$ 的完整 $p^3$ 解纤维

本附录固定原整源格 $\mathscr L_D$、原整目标格及同一个完整实际矩阵
$M$，包括同一 $h_\Theta$、Hasse 规范、全部 carry 和 normal 行。
固定一个实际整 $P$。若
$$
X=P+pR+p^2S,\qquad X'=P+pR'+p^2S',
\qquad MX,MX'\in p^3\mathscr T
\tag{A1}
$$
都是原格内的完整解，则相减并除以共同的 $p$ 给
$$
M\bigl((R'-R)+p(S'-S)\bigr)\in p^2\mathscr T.
\tag{A2}
$$
因此 $\overline{R'-R}\in K_1$，并且
$$
\beta_1(\overline{R'-R})
=\left[\frac{M(R'-R)}p\bmod p\right]
=-[\overline M\,\overline{S'-S}]=0.
\tag{A3}
$$
若还实际有 $\overline{R'-R}=\jmath(G)$、$G\in\mathcal H_3$，
则 R836(20)–(22) 的**四块等价**
$\jmath^{-1}(K_1)=K$，而非仅一个包含，先给 $G\in K$；
再由 (A3) 给 $G\in K'$。
所以正文 (31)–(35) 可以作用于这些真实有限解纤维的同源差。
若 (A1) 仅通过 $p^2$，(A2) 只能降为模 $p$ 的式子，
只得到 $K_1$，不能得到 $K'$。

当 $S$ 允许在整个原 $\mathscr L_D$ 内变化，且没有另加矩阵以外的指定值时，
上述差空间还有准确反向。固定一组 (A1) 的解，取任意 $G\in K'$，
以及原源格中 $\jmath(G)$ 的整提升 $Y$。
由 $G\in K$ 有 $MY\in p\mathscr T$，
而 $\beta_1(\jmath G)=0$ 保证存在同一个原源格的 $Z$，使
$$
MY/p+MZ\in p\mathscr T.
$$
于是 $(R+Y,S+Z)$ 仍满足完整 (A1)。
故在固定的剩余类陪集
$\bar R+\jmath(\mathcal H_3)$ 内，所有可延至原 $p^3$ 的
$\bar R'$ 准确组成
$$
\boxed{\bar R+\jmath(K').}
\tag{A4}
$$
这里补偿 $Z$ 在原 $\mathcal W_D$ 的全部真实列中求解，
没有换成自由目标格，也没有要求它属于同一个较小 $\mathcal H_3$。
若 $S$ 已固定、另受子格或其它指定条件限制，
只保留 (A3) 的必要结论，不冒用 (A4) 的反向。
对 $p^4$ 及更高页仍须用这一同 $R/S$ 继续读取，(A4) 本身不判定其可解性。
