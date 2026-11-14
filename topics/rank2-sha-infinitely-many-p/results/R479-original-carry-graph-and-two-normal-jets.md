# R479 — 原 M 的两条 carry 图形与同一修正的两个 normal jet

日期：2026-11-14。**状态：已证明。** 本篇把 R459 的相对 $J$ 层首次提升，准确恢复到整个原 $M=c_*U_0m_{13}J$。前两块各十三条首次商是同一个真实修正的输出，不能删去，也不能当作新增自由来源。给出完整有限图形方程，以及单位 $5$、单位 $-2$ 两条 normal 余项的全部 carry 修正。

原 $M$ 层保留单位 $5$ 的准确范围是 $h+k<s-13$；单位 $-2$ 的范围是更强的 $r>2k+13$。窗口外记录真实边界项，不延长已有排除判据。另给同一原 canonical 来源上的完整有限例子：原 $M$ 确实有 $p^2$ 提升，而相对 $J$ 没有；其真实 carry 正好消掉单独的单位 $-2$ 分支值。

## 1. 原目标与两条十三行的完整作用

保 $p=6s-1>83$、$1\le\ell<s-13$，置
$$
L=2s+\ell,\qquad q=s-13.
$$
相对目标为
$$
\Gamma_L=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
$$
原目标为 $\Gamma_{L+13}$，其中第三块截断改为 $w^{\ell+13}\epsilon^2$。
乘 $m_{13}=w^{13}$ 时，前两块中指数 $0\le i<q$ 的行乘单位移到 $i+13$；指数 $q\le i<s$ 的十三条行分别跨到下一块，并乘一个 $p$；第三块全部行作单位平移。这个分解在完整整格上成立。

因此，对任意 $v\in p\Gamma_L$，
$$
\boxed{m_{13}v\in p^2\Gamma_{L+13}
\quad\Longleftrightarrow\quad
\overline{v/p}\in\mathscr B_{26},}
\tag{1}
$$
其中准确的 carry 空间是
$$
\boxed{\mathscr B_{26}
=w^qk[w]_{<13}\ \oplus\ \epsilon w^qk[w]_{<13}.}
\tag{2}
$$
没有第三块自由参数。$c_*U_0$ 是已经支付的整个原整单位，所以 (1) 等价于 $M$ 的 $p^2$ 整除，不省去 $P_{134}/U_0$。原十三个初始自由行及二十六个 $p$ 因子均未改变。

## 2. 两条 carry 是同一个 R 的图形输出

固定一个真实 $\bar P\in\ker\bar J$，并取 R459 的因子提升
$$
P^0=t^r\widetilde F^3\widetilde Q,\qquad
P^{(2)}=P^0+pR.
$$
允许的 $\bar R$ 仍为同一个真实仿射空间
$\bar R^{\rm base}+\overline{\mathcal W}$；不要求 $P^0$、$R$ 各自为原来源。
因为 $\bar P\in\ker\bar J$，$J(P^0)/p$ 在整个相对目标中整。

**定理 1。** 原 $M(P^{(2)})\in p^2\Gamma_{L+13}$ 等价于存在唯一的两个多项式
$B_0,B_1\in k[w]_{<13}$，使
$$
\boxed{
\bar J(\bar R)+\overline{J(P^0)/p}
=w^qB_0+\epsilon w^qB_1
\quad\text{于整个 }\Gamma_L/p.}
\tag{3}
$$

**证明。** 由线性性，左端就是 $\overline{J(P^{(2)})/p}$；然后应用 (1)。两条 carry 的支持不交，故 $B_0,B_1$ 唯一。$\square$

式 (3) 是同一个 $R$ 的有限图形方程。它没有将仿射修正空间扩大为
$(\bar R^{\rm base}+\overline{\mathcal W})\times k^{26}$。
具体地，只有与完整 $\bar J$ 和 forcing 同时相符的 $B_0,B_1$ 才能出现。
取 $B_0=B_1=0$ 才恢复 R459 的较强条件 $J(P^{(2)})\in p^2\Gamma_L$。

这也把 R449 的相对/原接口直接写成同一格上的显示等式：相对首 Bockstein 只须落入两条 carry 的真实像，随后才取 $\ker(\pi\beta_J)$；不能直接以 $\ker\beta_J$ 替代原核。

## 3. 真立方的两个原首次商

保留 R459 的全部假设
$$
\bar P=t^rF^3Q,\quad r\ge1,\quad
F(0,1)=0,\quad (\mathcal EF)(0,1)Q(0,1)\ne0,
$$
$$
h=\operatorname{ord}F(t(w),\bar\vartheta(w)),\quad
k=2h+r-s\ge0,\quad
k<\min(s-h,\ell,h).
\tag{4}
$$
相对 Euler 算子保持原规范，$a=p\kappa\in\mathcal O^\times$。令
$$
\widetilde F(t(w),\vartheta(w))=w^hu+p\xi,\qquad
e=(\mathcal E\widetilde F)(t(w),\vartheta(w)),
$$
$$
C=(t(w)/w)^r\widetilde Q(t(w),\vartheta(w)),\qquad
\xi\in\mathcal O[w]_{<h}.
$$
以下带入同一个约化；$u,e,C$ 都是单位级数，不是可调参数。记 $R_i=(\mathcal E^i\bar R)(t(w),\bar\vartheta(w))$。

在 (3) 中，三个实际块准确给
$$
\boxed{
\begin{aligned}
R_0&\equiv w^qB_0 &&\pmod{w^s},\\
R_1&\equiv-6w^{h+r}Cu\xi e-a^{-1}w^{h+k}Cu^3
             +a^{-1}w^qB_1 &&\pmod{w^s},\\
R_2&\equiv-6w^rC\xi e^2-6a^{-1}w^kCu^2e
                                      &&\pmod{w^{k+1}}.
\end{aligned}}
\tag{5}
$$
这里 $B_1$ 是第二块的真实首次商，所以在 $R_1$ 中准确除以 $a$；没有重新归一化它。

**证明。** R459 的完整评价为
$$
J(P)=\left(P_0,\ aP_1+p\mathscr SP_0,
\ \frac{a^2}{2}P_2+pa\mathscr SP_1+p^2\mathscr S^2P_0\right)
$$
分别截到 $s,s,\ell$。$P^0$ 的第一块首次项从 $r+2h\ge s$ 起；第二块的两个 forcing 首项正是 (5) 中显示的 $6w^{h+r}$ 和 $a^{-1}w^{h+k}$；第三块的 forcing 是显示的两个六系数。由 (3)，前两块分别允许 $w^qB_0,w^qB_1$，第三块仍为零，得到 (5)。$k<\ell$ 使第三式的全部读取合法。$\square$

## 4. 不删 carry 的两个正规分支余项

令 $\psi(t)$ 是 $F=0$、$\psi(0)=1$ 的正规分支。
以下所有分支仍用原 $t(w)$ 参数化。

**定理 2。** 每个真正的原 $M$ 首次提升都满足
$$
\boxed{
(\mathcal ER)(\psi)
\equiv\frac5a C(0)u(0)^3w^{h+k}
       +\frac1a w^qB_1
\pmod{w^{h+k+1}}.}
\tag{6}
$$
若再有 $r>2k$，即 $2h+k<s$，则还满足
$$
\boxed{
R(\psi)\equiv
-\frac{2C(0)u(0)^4}{a e(0)}w^{2h+k}
+w^qB_0-\frac{u(w)}{a e(w)}w^{h+q}B_1
\pmod{w^{2h+k+1}}.}
\tag{7}
$$
在最后一项真的进入窗口时，$u(w)/e(w)$ 是整个实际单位级数，不能只保常数项。

**证明。** R459 的同一完整 Taylor 计算给
$$
(\mathcal ER)(\psi)
\equiv R_1-\frac{w^hu}{e}R_2
\pmod{w^{h+k+1}}.
$$
因 $k<h$，二次误差至少从 $2h$ 起。将 (5) 代入，全部 $\xi$ 项严格相消，留下 (6)。

若 $r>2k$，二阶 Taylor 计算为
$$
R(\psi)\equiv R_0-\frac{w^hu}{e}R_1
+\frac{w^{2h}u^2}{2e^2}R_2
\pmod{w^{2h+k+1}}.
$$
与 R459 相比，$R_1$ 还可能从 $q$ 起；但 $k<\ell<q$，所以 Euler 与普通二阶导数之间的附加项至少为 $2h+q>2h+k$，仍可严格删去。三阶误差至少为 $3h>2h+k$，完整 $R_0$ 余项从 $s>2h+k$ 起。代入 (5)，原两个常数 $1,-3$ 给单位 $-2$，另外恰得 (7) 的两个 carry 项。$\square$

式 (6)–(7) 仍是 (3) 的必要投影，不是全提升的充分条件。其 $B_0,B_1$ 必须同 (3) 联立。

## 5. 原可读范围与保因子限制

由 (6)，单位 $5$ 不受 carry 影响的准确严格范围是
$$
\boxed{h+k<q=s-13.}
\tag{8}
$$
在此范围，任何真正原 $M$ 首次修正都不能属于 $F^2$ 理想。
若 $h+k\ge q$，$B_1$ 的一个真实高边界系数已能进入同一行，不能再单独宣称单位 $5$ 非零。
具体地，若仍有 $F^2\mid R$，(6) 必迫
$$
B_1\equiv-5C(0)u(0)^3w^{h+k-q}
\pmod{w^{h+k-q+1}}.
\tag{9}
$$
这只是实际 carry 必须达到的值，未断言原来源一定能实现它。

当 $k\in\{0,1\}$ 为最小允许接触时，
$h+k\le\lfloor s/2\rfloor+1$，所以 $s\ge29$（即 $p>167$ 的当前素数范围）自动满足 (8)。R472 的单导数真像比较因而仍适用于这段原 $M$ 范围，但它并未解完整图形 (3)。

由 (7)，单位 $-2$ 不受任何 carry 影响的准确范围是
$$
2h+k<s-13
\quad\Longleftrightarrow\quad
\boxed{r>2k+13.}
\tag{10}
$$
此时 $h+k<s-13$ 也成立，两个原 normal jet 必须由同一 $R$ 联立实现，且 $F\nmid R$。
当 $r>2k$ 但 $r\le2k+13$ 时，(7) 仍完整有效，却含真实 $B_0$；不能用 R459 的相对 $J$ 判据直接排除整个原 $M$ 提升。

因此 R475 的 $J$ 层联合必要类在原 $M$ 层无修改可用，须增加 (10)。仅需导数分量时增加 (8) 即可。R475 §4 的原首 Bockstein 高轴不变性本来就直接在整个 $M$ 上证明，不受此范围区分影响。

## 6. 同一原来源上 carry 确实能消掉单位 −2

这不是只把 $B_0$ 设为抽象自由量。取 R475 已显示的原 canonical 来源
$$
p=239,\quad s=40,\quad D=40,\quad
P^0=\mathcal H_DY^{37}(Y-\rho_{<15}(t))^3.
$$
其真实数据为
$$
r=10,\quad h=15,\quad k=0,\quad\ell=25,\quad q=27.
$$
四个来源分量和所有原角次数已在 R475 §7 付清。本篇只使用额外的实际修正子格 $\mathcal W_{12}\subset\mathcal W_{40}$。

完整原 $\bar J|_{\mathcal W_{12}}$ 为 $105\times369$ 矩阵，逐项有限消元得到秩 $105$。在该实际矩阵内求解 (3)，指定
$$
\boxed{B_0=116w^3,\qquad B_1=0.}
\tag{11}
$$
所得同格修正有 $103$ 个非零 canonical 系数，且准确满足
$$
J(P^0+pR)\equiv116p\,w^{30}\pmod{p^2\Gamma_L},
$$
$$
\boxed{M(P^0+pR)\in p^2\Gamma_{L+13},\qquad
J(P^0+pR)\notin p^2\Gamma_L.}
\tag{12}
$$
这由 $w^{13}p w^{30}=p^2\epsilon w^3$ 直接解释，并由整个 $P_{134}/U_0$ 的实际乘法核定。

同一个 $R$ 在真正分支上满足
$$
R|_\psi=0\pmod{w^{31}},\qquad
(\mathcal ER)|_\psi=194w^{15}+O(w^{16}).
\tag{13}
$$
相对 $J$ 的单独单位 $-2$ 系数在这里为 $123$；真实 $B_0$ 给 $116=-123\pmod{239}$，恰好相消。单位 $5$ 的导数因 $15<27$ 完整保留。这个例子没有声称整个 $F\mid R$，只证明不能把已失去的分支首项继续当作原 $M$ 的必要非零值。

本例不是临界低预算的主目标证明，也没有赋予任何新中央零。它是同一个真实来源、同一个修正、同一个完整原矩阵上的严格范围见证。完整计算见
[check-r479-original-carry-normal-correction.py](../scripts/check-r479-original-carry-normal-correction.py)；没有素数扫描。

## 7. 后续实际障碍

现在最小接触的大素数窗中，导数单位 $5$ 仍是合法的原必要量，但 R472 已证明其单独像在显示的最高因子次数范围满射。分支值是否同时存在，必须使用 (3)、(6)、(7)，并保两条 carry 同属实际 $R$ 的图形。

若继续到第二次提升，仍须在 $C_2(J)/\overline H$ 和原首次提升像中作准确商；(12) 这样的 $M$ 层提升不能替代一个 $J$ 层提升来代入下一位公式。三个完整中央条件保持 R468/R469 的原权、实际高轴和三位数据，本篇没有把这些零赋给 $F,Q,R$ 或任何新增计算列。主目标及全量词严格预算仍未完成。
