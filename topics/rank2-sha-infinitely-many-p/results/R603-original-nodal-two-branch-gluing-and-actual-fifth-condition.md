# R603 — 原结点两支的实际 gluing、第五条角条件与同一修正

日期：2026-11-14。**状态：已证明。**

本篇取 R597 最低角层恰三重的情形。
原 Euler 临界曲线有两条整的非垂直支；
原有限来源在两支的值与一阶法向 jet 之间，
比一般局部四 jet 多一条真实角条件。
准确的 $t$ 对角因子是 $1,1,t,t^4$，而一般环境为 $1,1,t,t^3$。

这不只是一份完成环外包络。
在显示的、约为 $(25/6)D$ 的联合前缀内，
原全部有限来源的像恰好由这五条条件给出。
同一个首次修正的 $Q_n$ 边界系数准确给出其下一条 $t^4$ 值；
第二次修正有完全相同的实际读取规则。

另一临界值有一个明确的 $t^4$ 单位首项，
但它恰处于原真实像允许的第一阶。
物理目标只指定近支；原算术尚未给另一支赋予相同条件。
本篇没有由此宣布原 $d_2$ 非零或主目标完成。

## 1. 同一原范围及两条指定临界支

保 R597 的
$$
p=6s-1>101,\quad \ell=1\ \text{或 }2,\quad
f_D<p,\quad D\ge3,
$$
$$
\bar P\in\ker\bar J,\qquad
d^{C_D}\bar P=tF(t,Y),\quad t\nmid F,\qquad \nu=2.
\tag{1}
$$
原 $\mathcal W_D$、$q_n$、全部十九角、次数帽、
$P_{134}/U_0$、两条十三行和总 charge 四十均不变。

本篇另外明确要求
$$
\boxed{\operatorname{ord}_{Y=1}F(0,Y)=3.}
\tag{2}
$$
若最低角重数大于三，另一临界支一般对 $t$ 垂直；
不得把它代入下文的两个 $k[[t]]$ 图形。

取 R597 的实际整结点基准 $P^{\rm crit}$，
并使用其已付规范 $A_+\in w^5$、$\xi\in w^7$，
或其更深的联合普通前缀规范。
令
$$
H=\frac{d^{C_D}}t\,\mathcal EP^{\rm crit},\qquad
\mathcal E=Y\partial_Y.
$$
R597 已整付 $H(0,1)=H_Y(0,1)=H_t(0,1)=0$。
因 (2)，其二次切锥的两条线均非垂直、互异且在原剩余域定义。
两条简单切线根分别整 Hensel，得到
$$
H(t,\psi_+(t))=H(t,\psi_-(t))=0,\qquad
\psi_\pm(0)=1,
$$
$$
\boxed{\Delta=\psi_- -\psi_+=t\delta(t),\qquad
\delta(0)\in\mathcal O^\times.}
\tag{3}
$$
其中 $\psi_+$ 是与原 $g$ 接触至少 $s-2$ 的指定物理近支。
两支都在原 $\mathcal O[[t]]$ 中，不需另开常量域。

在 $(0,1)$ 的完成局部环内，准确写成
$$
H(t,Y)=U(t,Y)(Y-\psi_+)(Y-\psi_-),
\qquad U(0,1)\in\mathcal O^\times .
\tag{4}
$$
其余局部因子为单位。
(4) 只描述同一原 Euler 多项式，不给第二支新增中央零。

置
$$
B_+=(\mathcal E^2P^{\rm crit})|_{\psi_+},\qquad
b_*=(B_+/t^2)(0)=(B_+/w^2)(0)\in\mathcal O^\times .
$$
R597 的 Laurent 形状系数与两切线差准确满足
$$
\boxed{\kappa_{-1}=2/\delta(0).}
\tag{5}
$$
确实，(4) 给
$H_Y(t,\psi_+)/t=-U(0,1)\delta(0)+O(t)$、
$H_{YY}(0,1)=2U(0,1)$；
再用 R597 的 $\kappa_{-1}=-H_{YY}(0,1)/(H_Y|_{\psi_+}/t)(0)$。
因此 (2) 与该 Laurent 首系数为单位完全相容。

## 2. 四个真实观察及原角格的局部系数限制

对任何实际 $R\in\mathcal W_D$，定义
$$
V_\pm=R(t,\psi_\pm),\qquad
D_\pm=R_Y(t,\psi_\pm)
=\frac{(\mathcal ER)(t,\psi_\pm)}{\psi_\pm}.
\tag{6}
$$
$\psi_\pm$ 是整单位，故 (6) 只是对原 Euler 行作单位换帧。

写 $u=Y-\psi_+(t)$，并将 $R$ 对首一多项式
$$
u^2(u-\Delta)^2
$$
取余，记为
$$
\rho(R)=\rho_0+\rho_1u+\rho_2u^2+\rho_3u^3
\in\mathcal O[[t]][u]_{<4}.
\tag{7}
$$
四个观察 (6) 完全由 (7) 决定，未丢掉任何同支一阶 jet。

先准确说明“局部格”的含义。
令 $\widehat{\mathcal W}_D$ 是全部原有限列在
$\mathcal O[[t]][Y]$ 中的 $\mathcal O[[t]]$-张成；
这不是把任意形式倍数宣称为原有限来源。
由于 $q_n/t^{A_n}$ 在 $t=0$ 为单位，
$$
\widehat{\mathcal W}_D
=\bigoplus_{n=0}^D t^{A_n}\mathcal O[[t]]Y^n,
\qquad A_n=\lfloor(n+1)/4\rfloor .
$$
$A_n$ 单调，且 $\psi_+$ 为单位。
在 $Y^n=(u+\psi_+)^n$ 及反向展开中，
每个低 $u^j$ 的 $t$ 阶至少为 $A_j$，所以准确有
$$
\boxed{
\widehat{\mathcal W}_D
=\bigoplus_{j=0}^D t^{A_j}\mathcal O[[t]]u^j.}
\tag{8}
$$
这一步保留原 $t$ 角限制；其余角在该局部环中为单位。
原全部有限来源仍是其中带原次数帽的子格。

对 $j\ge2$，真实 Hermite 余式为
$$
\boxed{
u^j\equiv(3-j)\Delta^{j-2}u^2
+(j-2)\Delta^{j-3}u^3
\pmod{u^2(u-\Delta)^2},}
\tag{9}
$$
其中 $j=2$ 的第二项为零，按此理解。
由于 $A_0=A_1=A_2=0$、$A_3=1$，
而 $j\ge4$ 对 $\rho_3$ 的贡献从 $t^2$ 起，
(8)–(9) 给准确的完成局部像
$$
\boxed{
\rho(\widehat{\mathcal W}_D)
=\mathcal O[[t]]\langle1,u,u^2,tu^3\rangle.}
\tag{10}
$$
尤其每个实际有限 $R$ 都满足 $\rho_3\in t\mathcal O[[t]]$。
一般环境没有这一个额外 $t$。

## 3. 完整两支 gluing：t 对角因子 1,1,t,t⁴

对 (10) 的基 $1,u,u^2,tu^3$，
四观察 (6) 的准确矩阵是
$$
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
1&\Delta&\Delta^2&t\Delta^3\\
0&1&2\Delta&3t\Delta^2
\end{pmatrix}.
\tag{11}
$$
减去前两行后，余下二乘二块为
$$
\begin{pmatrix}\Delta^2&t\Delta^3\\
2\Delta&3t\Delta^2\end{pmatrix}.
$$
用整单位 $2$ 和 $\delta(t)=\Delta/t$ 消元，
(11) 在 $\mathcal O[[t]]$ 上准确等价于
$$
\boxed{\operatorname{diag}(1,1,t,t^4).}
\tag{12}
$$
这是显示的 $t$ 方向对角化，不是把 $t$ 除掉，
也不是在原 $p$ 进目标中省去非单位行。

等价地，四个整形式函数属于 (10) 的真实两支像，
当且仅当
$$
\boxed{
D_- -D_+\in t\mathcal O[[t]],\qquad
2(V_- -V_+)-\Delta(D_-+D_+)\in t^4\mathcal O[[t]].}
\tag{13}
$$
证明也可直接解 (7)：
$$
V_- -V_+=\Delta\rho_1+\Delta^2\rho_2+\Delta^3\rho_3,
$$
$$
D_- -D_+=2\Delta\rho_2+3\Delta^2\rho_3,
$$
故
$$
\boxed{
2(V_- -V_+)-\Delta(D_-+D_+)=-\Delta^3\rho_3.}
\tag{14}
$$
(13) 迫 $\rho_3\in t$，再由第二式得整 $\rho_2$；
$\rho_0=V_+,\rho_1=D_+$，给充要性。

若只用一般局部多项式环，$\rho_3$ 可以有非零常数，
所得是 $1,1,t,t^3$。
原 $A_n$ 的最低角限制恰给 (13) 中真实新增的第四阶，
即联合目标中的第五条线性 gluing 条件。

## 4. 在明确前缀内，这就是全部原有限来源的像

上一节没有把完成环张成当成有限来源。
现在给实际有限前缀的反向包含。

保 R597 深前缀增补的记号
$$
b_n^{\rm top}=A_n+e_{n+1}.
$$
取
$$
\boxed{5\le N\le b_{D-3}^{\rm top}+1.}
\tag{15}
$$
$D\ge3$ 且 $b_0^{\rm top}=4$，故这个范围非空。
这里的 $N$ 是两支的普通 $t$-jet 长度；
没有更改原 $M$ 的 $s,\ell$。
$\psi_\pm$ 是已构造的整代数支，所以本节不需扩大
raw theta 的可约化窗口。

考虑实际有限映射
$$
\rho_N:\mathcal W_D\longrightarrow
\mathcal C_N:=
(\mathcal O[t]/t^N)^3\oplus t\mathcal O[t]/t^N,
\quad R\longmapsto(\rho_0,\rho_1,\rho_2,\rho_3).
\tag{16}
$$
它整满射，且有只用原列的显示单位三角右逆。

准确构造如下。在 $t$ 阶零使用 $n=0,1,2$ 三列。
在每个 $1\le j<N$，取
$b_n^{\rm top}\ge j$ 的最小 $n$，
使用四个原列
$$
t^{j-A_{n+i}}Y^{n+i}q_{n+i},\qquad i=0,1,2,3 .
\tag{17}
$$
所有来源次数和角条件均实际成立。
若最小 $n=0$，则 $j\ge1=A_3$；
若 $n\ge1$，由
$j>b_{n-1}^{\rm top}$ 及
$A_{n+3}\le b_{n-1}^{\rm top}+1$，
也有 $A_{n+i}\le j$。
同时 $b_n^{\rm top}$ 单调，
故 $j-A_{n+i}\le e_{n+i+1}$。
(15) 还保证 $n+3\le D$。
这些 floor 不等式与 R597 增补同样逐项成立。

在同一 $t$ 阶，(17) 的四个首系数向量是整单位标量乘
$$
\bigl(1,n+i,\binom{n+i}{2},\binom{n+i}{3}\bigr)^t .
\tag{18}
$$
这是因为 $\psi_+(0)=1,\Delta(0)=0$，
对 $u^{\ge4}$ 的余式只会增加 $t$ 阶。
四个连续整数的 (18) 行列式恰为一；
低三列的相应三阶行列式也为一。
按 $t$ 阶排列，得到单位块三角矩阵，
证明 (16) 的实际整满射。
全部 $q_n$ 和次数帽都已在 (17) 支付，没有使用任意形式倍数。

因此对联合目标
$$
\mathcal V_N=(\mathcal O[t]/t^N)^4
$$
中的四个两支 jet，原 $\mathcal W_D$ 的真实像准确为
(13) 的模 $t^N$ 解集。
其余核是 (12) 给出的
$$
\boxed{
\mathcal O[t]/t\ \oplus\ \mathcal O[t]/t^4
\qquad(N\ge5).}
\tag{19}
$$
所以此联合前缀中的全部原左条件恰好是
$D_- -D_+$ 的常数行，以及
$2(V_- -V_+)-\Delta(D_-+D_+)$ 的前四行。
不是只给必要条件或源端自由度计数。

(19) 是本篇这个真实联合观察的余核，
不被冒认为原 $C_2(M)$。
长度超过 (15) 时，原有限次数帽可能给更多全局条件；
本篇不把 (19) 外推过去。

## 5. 同一个首次修正的 Qn 边界恰给下一行

回 R593/R597 的同一个
$$
R=R_{\rm bd}+S,\qquad S\in\mathcal K_{2,\ell}.
$$
其完整实际分解为
$$
S=S_2+\sum_{n=3}^{\min(D,6)}c_nQ_n
+\begin{cases}\gamma Q_{\rm quad},&\ell=1,\\0,&\ell=2,\end{cases}
\qquad S_2\in\mathcal W_D^{(2)} .
\tag{20}
$$
$R_{\rm bd}$ 和 $Q_{\rm quad}$ 的 $Y$ 次数均不超过二。
由原显示列
$$
Q_n=\chi_n t\{Y^n-L_{n,1}(Y)\}\pmod{t^2},
\qquad
\chi_n=7(-1)^{B_n},
$$
其中 $L_{n,1}$ 是 $Y^n$ 在 $1$ 的二次 Taylor 多项式，
准确得到
$$
\boxed{
[t]\rho_3(R)
=\sum_{n=3}^{\min(D,6)}
\chi_n\binom n3 c_n .}
\tag{21}
$$
证明：三次 $u$ 系数的 $t$ 首项，
等于 $(1/6)[t]R_{YYY}(t,\psi_+)$。
$\mathcal W_D^{(2)}$ 不贡献；
两个二次来源不贡献；
$\psi_+(0)=1$ 且 $R(0,Y)$ 为二次式，
故移动中心不添首项。
(9) 中更高 $u^j$ 对 $\rho_3$ 的贡献从 $t^2$ 起。
这给 (21) 的全部项，而非只取某一条 $Q_n$。
若把未出现的 $c_n$ 记为零，该组合明确为
$-7c_3-28c_4+70c_5+140c_6$。

结合 (14)，
$$
\boxed{
[t^4]\{2(V_- -V_+)-\Delta(D_-+D_+)\}
=-\delta(0)^3
\sum_{n=3}^{\min(D,6)}
\chi_n\binom n3 c_n .}
\tag{22}
$$
$\ell=1$ 的同一个 $\gamma$ 不出现在这一首项中；
它仍在 R597 的最高行更新和全部原第二 forcing 内，
不能因此从原问题删除。

三个低系数也由同一真实右逆固定：
$$
\rho_0(0)=0,\qquad
\rho_1(0)=-\alpha_0/a,\qquad
\rho_2(0)=(\alpha_0-2\beta_0)/(2a).
\tag{23}
$$
这里 $\alpha,\beta$ 正是 R593/R597 的原 carry 多项式；
$\rho_2(0)$ 来自
$R_{YY}=(R_2-R_1)/\psi_+^2$，没有改 Euler 归一。

对第二次修正 $T=T_{\rm bd}+H$，
在同一低行整数代表中也有
$H\in\mathcal K_{2,\ell}$。
$T_{\rm bd}$ 同样只用 $n=0,1,2$，
所以 (21)–(22) 对 $H$ 的同一 $Q_n$ 系数逐字成立。
因此可以将原第二目标代入 (13)、(22)，
但必须保留同一个 $R$ 和同一个 $T$ 的其它所有行；
不把这几个边界系数另设为自由参数。

## 6. 另一临界值的单位恰位于第一允许阶

令
$$
A_\pm=P^{\rm crit}(t,\psi_\pm).
$$
两支都是同一 Euler 临界支，所以
$(P^{\rm crit})_Y(t,\psi_\pm)=0$ 整系数成立。
由 (4)，在 $u=Y-\psi_+$ 中
$$
(P^{\rm crit})_Y
=t\,K(t,u)\,u(u-\Delta),\qquad K(0,0)=U(0,1).
$$
沿 $u$ 作真正有限形式积分，保首项：
$$
A_- -A_+
=-\frac16t\,U(0,1)\Delta^3+O(t^5).
$$
而
$b_*=-U(0,1)\delta(0)$，故
$$
\boxed{
A_- -A_+
=\frac{b_*\delta(0)^2}{6}\,t^4+O(t^5)
=\frac{2b_*}{3\kappa_{-1}^2}\,t^4+O(t^5).}
\tag{24}
$$
显示系数为单位。
采用 R597 已付的 $A_+\in w^5=t^5\mathcal O[[t]]$ 时，
$A_-$ 因而准确四阶。

这个单位不构成遗漏的左障碍。
对实际来源 $P^{\rm crit}$，两支导数都为零，
(13) 的第二条件仅要求 $2(A_- -A_+)\in t^4$，
而 (24) 正好处于第一允许阶。
在 (15) 的真实联合前缀中，(19) 已证明除此以外没有新左行。
因此不能将 (24) 的单位单独读成原物理余类非零。

## 7. 接原 M 时仍缺的确切条件

原物理首像及两次提升只指定近支 $\psi_+$ 的数据，
并保 R597 的同一个
$$
\bar{\mathcal D}_\psi^+(\bar S)=\mathcal G_P^+,\qquad
\mathcal H_P(R_{\rm bd}+S)\in
\operatorname{im}\bar{\mathcal D}_\psi^{\rm short}.
$$
两条十三行、整个 $U_0$、原 Gaussian 及高 $Z^+$ 续段均未改变。
本篇未给 $\psi_-$ 的值或法向 jet 赋予相同的算术消失条件。

新增的全局接续接口现在是具体的：
若要在临界长度建立联合两支或全局残数行，
必须同时保 (13) 的完整五行、
(21)–(22) 的同一实际 $Q_n$ 边界、
以及超过 (15) 后的全部有限次数帽。
在未支付另一支的原条件前，
局部单位 (24) 不能替代该全局比较。

本篇没有扩大来源；(16) 反向实现使用的是明确有限原列。
同时也没有将局部完成格或新增联合观察自动识别为原 $M$ 的目标。
真实指定 forcing 的原余核非零仍待继续。

## 依赖

- [R597](R597-original-nodal-critical-lift-and-complete-low-ell-second-class.md)：
  同格结点整提升、两非垂直切线的准确范围、完整原第三精度。
- [R597 深前缀增补](../notes/2026-11-14-r597-joint-ordinary-prefix-normalization.md)：
  $b_n^{\rm top}$、原连续电荷的实际次数门及整三角实现。
- [R578](R578-complete-critical-boundary-elimination-and-fixed-polar-carry.md)、
  [R593](R593-original-critical-carry-completion-and-actual-second-normal-tail.md)：
  全 $\mathcal K_{2,\ell}$、真实 $Q_n/Q_{\rm quad}$、同一 $R/T$ 的低行右逆与 carry。
- R412 的实际逐阶单位三角方法在本篇 (17)–(18) 用四个连续电荷明确重付；
  本篇不重登记其原三块满射范围。

本篇为全参数证明，无新增素数扫描。
