# R940 — 原双惰性增广导数的实际下降与有条件深增广界

会话：Astra-rank2-Sha-7d29daa5-20261126，global 子任务。

**状态：下述原类下降、惰性检测及条件界已证明。** 深增广界显式假设原端点 $c_1\ne0$；不证明这个假设，不证明 R893 的 $s=0$，也不给无穷系数素数结论。

使用同一原十八阶 $\eta$、最高角色、固定格、$q/q^4$ 端点、旧副本和 $\mathfrak p$ full／$\bar{\mathfrak p}$ zero 条件。只处理 finite tame 基层的实际双新类；不把 fixed-p 的界说成 wild 层统一或跨 p 统一的界。

## 1. 原对象与精确结论

固定原 ordinary $p>211$ 和一个最高标签。按 R891(B7)–(B8)记
\[
\mathcal O_0=\mathbf Z_p[\mu_{18}],\quad
T_0=\mathcal O_0(\rho),\quad
\rho=\eta^e\psi_0^3\varepsilon_{\rm cyc}^{-1},\quad
e\in\{5,17,11\}.
\]
$\mathcal O_0/\mathbf Z_p$ 不分歧，原格为
$T=T_0\otimes_{\mathcal O_0}\mathcal O$；使用 R891 的同一固定基。系数扩大只作有限自由基变换，不把有限 Galois 加法像误认成整个扩大系数模。

取两不同的原允许惰性素数
\[
q_i\nmid30\cdot34p,\quad h_i=p^{e_i},\quad
e_i=v_p(q_i+1),\quad u_i=(q_i+1)/h_i.
\]
令
\[
R_i=\mathcal O[C_{h_i}],\quad
N_i=\sum_{a=0}^{h_i-1}\sigma_i^a,\quad
A_i=R_i/(N_i),\quad j_i=\sigma_i-1,\quad
\mathfrak d_i=\sum_{a=1}^{h_i-1}a\sigma_i^a.
\]
保 R901 的真实 $j_i:A_i\simeq I_i\subset R_i$。同一个原 finite tame 双新项及其唯一整提升为
\[
\mathcal N_{12}\in H^1(K,R_1\otimes R_2\otimes T),\qquad
x_{12}:=\mathcal N_{12}^{\rm aug}
 \in H^1(K,A_1\otimes A_2\otimes T),
\]
\[
\mathcal N_{12}=j_1j_2x_{12}.
\tag{1}
\]
这里按 Shapiro 识别原 $K[q_1q_2]$ 上的类；没有选一个角色平均。

对 $1\le m\le\min(e_1,e_2)$，真正的系数增广
\[
\pi_m:A_1\otimes A_2\longrightarrow\mathcal O/p^m,\qquad
\sigma_1,\sigma_2\longmapsto1
\]
良定，因为 $p^m\mid h_1,h_2$。定义实际类
\[
\kappa_{12,m}:=(\pi_m)_*(x_{12})
 \in H^1(K,T/p^m).
\tag{2}
\]

**结论 A（原下降及局部条件）。** 原双导数的唯一下降正是 (2)：
\[
\operatorname{res}_{K[q_1q_2]/K}\kappa_{12,m}
  =\mathfrak d_1\mathfrak d_2\mathcal N_{12}\pmod{p^m}.
\tag{3}
\]
令 $D$ 为 R908 附录 A 的同一固定 tame/CM 整数，则
\[
D\,\operatorname{loc}_{q_i}\kappa_{12,m}=0
\quad(i=1,2).
\tag{4}
\]
$D\kappa_{12,m}$ 在原固定
$\Sigma=\{v:v\mid2\cdot3\cdot17p\}$ 外未分歧，且在
$\bar{\mathfrak p}$ 为零。$\mathfrak p$ 仍为 full。

**结论 B（保原底类假设的深增广界）。**
假设原端点 $c_1\ne0$ 于 $H^1(K,T\otimes\operatorname{Frac}\mathcal O)$。
存在只依固定 $p,T$ 及原固定尺度 $D$ 的整数 $B_p\ge0$，使对每个 $m\ge1$ 可选一个正密度的惰性素数集合 $\mathcal Q_m$，满足
$q\equiv-1\pmod{p^m}$，并且：

若 $q_1\in\mathcal Q_m$，而 $q_2\ne q_1$ 是任意原允许惰性素数且 $p^m\mid q_2+1$，则同一个原类 (2) 满足
\[
p^{B_p}\kappa_{12,m}=0.
\tag{5}
\]
若 $m>B_p$，令 $M=m-B_p$，则
\[
(\pi_M)_*(x_{12})=0
\quad\text{于 }H^1(K,T/p^M).
\tag{6}
\]
更准确地，令
\[
J_{12,M}:=\ker(A_1\otimes A_2\xrightarrow{\pi_M}\mathcal O/p^M)
       =(p^M,j_1,j_2)(A_1\otimes A_2).
\tag{7}
\]
则 $x_{12}$ 有唯一的原格原像
\[
x_{12}^{J}\in H^1(K,J_{12,M}\otimes T).
\tag{8}
\]
(8) 是系数子格上的上同调原像；不等同于宣布
$x_{12}\in(p^M,j_1,j_2)H^1(K,A_1\otimes A_2\otimes T)$，
更不等同于 scalar $p^M$ 整除。

## 2. 原有限群环导数确实给 (2)

在整群环中，按原生成元与符号有
\[
\mathfrak d_i j_i=h_i-N_i.
\tag{9}
\]
若 $\bar a\in A_i$，任取 $a\in R_i$ 提升，则
\[
\mathfrak d_i j_i(\bar a)=h_i a-\epsilon_i(a)N_i.
\]
改提升加 $N_i b$ 不改变右边，因为 $N_i^2=h_iN_i$。模 $p^m$ 后，得到真实系数映射恒等式
\[
\mathfrak d_i j_i=-\iota_i\epsilon_{i,m},
\qquad
\iota_i:\mathcal O/p^m\to R_i/p^m,\quad1\mapsto N_i.
\tag{10}
\]
这里 $\epsilon_{i,m}$ 是 $A_i\to\mathcal O/p^m$，不是整 $A_i\to\mathcal O$ 的不存在的增广。

两因子相乘，两负号相消，故
\[
\mathfrak d_1\mathfrak d_2j_1j_2
  =(\iota_1\otimes\iota_2)\pi_m.
\tag{11}
\]
在原 Shapiro 的 identity coset evaluation 下，
$1\mapsto N_1N_2$ 所诱导的上同调映射正是 restriction。
将 (11) 用于同一 $x_{12}$，即为 (3)。

唯一性也不附加假设。原十七惯性元在 $K[q_1q_2]/K$ 中为一，在 $T/p^m$ 上为 $-1$，故
\[
H^0(K[q_1q_2],T/p^m)=0.
\]
Inflation–restriction 给 restriction 的单射性，因此 (3) 的下降唯一。没有用对全群取平均的 $1/(h_1h_2)$。

## 3. 新增位的几何零准确传至该下降

R908(21)–(24)给在 $q_1$ 处的整局部读取
\[
H^1(K_{q_1},A_1\otimes A_2\otimes T)
  \simeq(A_2/h_1A_2)\otimes T,
\]
且到原全部 Shapiro 素点的像为
$u_1j_2a_{12}$。$u_1$ 是单位，$j_2:A_2/h_1A_2\to R_2/h_1R_2$ 单射。因此 R908(A3) 的
$D\,\operatorname{loc}_{q_1}\mathcal N_{12}=0$ 准确推出
\[
D\,\operatorname{loc}_{q_1}x_{12}=0.
\]
交换两个素数同理。随后施 $\pi_m$ 给 (4)。这一步保留了原固定 $D$；没有把 $p>211$ 偷换成 $p\nmid D$。

在 $\bar{\mathfrak p}$，原 $\mathcal N_{12}$ 为零。R921(39)给这里各系数短正合列的残余 $H^0=0$，整系数亦然；所以原两次 $j_i$ 所诱导的局部 $H^1$ 映射单射，得到
$\operatorname{loc}_{\bar{\mathfrak p}}x_{12}=0$。施 $\pi_m$ 后仍为零。
在 $\mathfrak p$ 没有增加条件。

在 $\Sigma\cup\{q_1,q_2\}$ 之外，$T$、各 $A_i$ 与 $R_i$ 均未分歧。原整 $\mathcal N_{12}$ 的惯性限制为零。此处对整无挠系数的惯性 $H^1$ 可按连续同态读；其经系数单射 $j_1j_2$ 后为零，故 $x_{12}$ 的惯性限制本身为零。增广保持这个零。
最后，(4)杀掉 $D\kappa_{12,m}$ 在 $q_1,q_2$ 的完整局部类，特别杀掉其惯性。于是它来自固定 $G_{K,\Sigma}$，且满足结论 A。

这不是把 R921 的任意 residual $A$ 类赋一个整提升。这里从开头使用的就是 R901 已构造的整 $x_{12}$；也没有断言未乘 $D$ 的 $\kappa_{12,m}$ 已在固定 $\Sigma$ 上。

## 4. 原本原 Selmer 类的惰性单位检测

本节给结论 B 所需的实际 $\mathcal Q_m$。

由 R891(B6)–(B8)及 $c_1\ne0$，最小环上的原有理 balanced Selmer 群为一维。令 $S_0$ 为其在
$H^1(G_{K,\Sigma},T_0)$ 中的饱和原像。R891 已付：$S_0$ 是自由秩一模，且
$S_0/p\hookrightarrow H^1(K,T_0/p)$。固定一个本原生成元 $z$。
它只是证明中的检测向量；不将原几何底类或整个 Euler 系统改标为 $z$。

记 $z^c(g)=z(cgc^{-1})$，其值域为 $T_0^c$，系数保持固定。
用已证明的
[原有限测试注](../notes/2026-11-16-original-endpoint-finite-test-chebotarev-refinement.md)
A.2，取其原有限阿贝尔域 $\Omega_m$，同时平凡化
$T_0/p^m,T_0^c/p^m,\mu_{p^m}$。该域在复共轭下稳定。
$z$、$z^c$ 的模 p 类各非零，所以同一联合像定理允许在 $G_{\Omega_m}$ 中取 $\tau$，使
\[
z(\tau)=1,\qquad z^c(\tau)=0\pmod{p^m}.
\tag{12}
\]
此调用完整保原十七惯性与最小系数环。其满像依据是该注 A.3–A.5 的两个整符号投影与完整 $\mathcal O_0$ 作用，不是扩大系数后的猜测。

将 $\Omega_m$ 以及上述两个有限 cocycle 的测试域合成，得到在 $\mathbf Q$ 上 Galois 的有限域 $L_m$。
外部复共轭 $c$ 取实际阶二元。令
\[
g=c\tau\in\operatorname{Gal}(L_m/\mathbf Q).
\]
它在 $K$ 上非平凡，在 $\mu_{p^m}$ 上为取逆。又
$g^2=c\tau c\tau\in G_K$。因为 $\tau$ 与 $c\tau c$ 都固定 $\Omega_m$，cocycle 恒等式给
\[
z(g^2)=z(c\tau c)+\rho(c\tau c)z(\tau)
      =z^c(\tau)+z(\tau)=1\pmod{p^m}.
\tag{13}
\]
没有把惰性有理 Frobenius 本身当作 $G_K$ 的元素；真正的 $K$-Frobenius 是它的平方。

Chebotarev 应用于 $g$ 的共轭类，给正密度的有理素数 $q$，可删任意指定有限集，使
\[
q\text{ 惰性},\quad q\equiv-1\pmod{p^m},\quad
z(\operatorname{Fr}_{K_q})\in(\mathcal O_0/p^m)^\times.
\tag{14}
\]
若选测试域上方素点使 Frobenius 正是 $g$，最后读数即 (13) 的1；不作该 frame 选择时只是同步单位变换，不影响其为单位。

原 $T_0$ 在该处的 Frobenius 为 $-q$，故
\[
H^1_{\rm unr}(K_q,T_0/p^m)\simeq\mathcal O_0/p^m,
\]
并且 (14) 说明 $\operatorname{loc}_qz$ 在此群为生成元，具有准确 $p^m$ 阶。定义这些素数构成 $\mathcal Q_m$。
与 R891 的 split 双点矩阵不同，本节使用的是 $c\tau$ 及平方 (13)；不要求在惰性素数的两个不存在的 $K$-素点分别指定读数。

## 5. 固定原 Selmer 复形给一个与新素数无关的误差指数

为避免引入新的固定坏位条件，使用
\[
C_0=\operatorname{Cone}
 \bigl(C^\bullet(G_{K,\Sigma},T_0)
        \longrightarrow C^\bullet(K_{\bar{\mathfrak p}},T_0)\bigr)[-1].
\tag{15}
\]
在 $\mathfrak p$ 及 $\Sigma_0=\{v:v\mid2\cdot3\cdot17\}$ 都是 full。
R891(B1)已给 $\Sigma_0$ 上全部有理局部群为零，所以 (15) 的有理 $H^1$ 正是原 balanced Selmer 群；并未换一个有理 Selmer 问题。

R921(39)给
$H^0(K_{\bar{\mathfrak p}},T_0/p^a)=0$ 对所有 $a\ge1$ 成立，整系数也为零。因此
\[
H^1(C_0)=S_0=\mathcal O_0z,\qquad
H^1(C_0/p^m)=
 \ker\bigl(H^1(G_{K,\Sigma},T_0/p^m)
          \to H^1(K_{\bar{\mathfrak p}},T_0/p^m)\bigr).
\tag{16}
\]
这里没有多余的局部 $H^0$ 边界项。并且对所有 a 的局部模 $p^a$ 不变元为零，由约化长正合列可知 $H^1(K_{\bar{\mathfrak p}},T_0)$ 无 p 挠。因此该局部群中的有理零已经是整零，(16) 的整核确实等于前节的饱和原像 $S_0$，没有额外更换整 Selmer 格。

连续 cochain 在模 $p^m$ 的有限值函数可逐个 clopen 纤维提升，因此
$0\to C_0\xrightarrow{p^m}C_0\to C_0/p^m\to0$
是实际逐项短正合。其长正合列给
\[
0\longrightarrow S_0/p^m
 \longrightarrow H^1(C_0/p^m)
 \longrightarrow H^2(C_0)[p^m]\longrightarrow0.
\tag{17}
\]
固定有限分歧集的全局与局部 Galois 上同调有限生成性，及 (15) 的长正合列，说明 $H^2(C_0)$ 是有限生成 $\mathcal O_0$-模。
选择 $b_p\ge0$，使
\[
p^{b_p}H^2(C_0)_{\rm tors}=0.
\tag{18}
\]
没有要求 $H^2(C_0)$ 本身为有限群或为零；其自由部分可以非零。
$\mathcal O/\mathcal O_0$ 有限自由，因此 (16)–(18)按同一基变换保持，且同一 $b_p$ 仍杀所得 torsion。

由结论 A，$D\kappa_{12,m}$ 属于扩系数后的 (16)。由 (17)–(18)，存在
$a_{12,m}\in\mathcal O/p^m$，使
\[
p^{b_p}D\kappa_{12,m}=a_{12,m}z\pmod{p^m}.
\tag{19}
\]
这是固定复形的有限 torsion 误差，不是 R921 的、随 $h_i$ 增长的残余 $A_i$ 连接线被无证压成有界误差。

## 6. 实际局部零与单位检测给深增广界

令 $q_1\in\mathcal Q_m$，并取结论 B 中的 $q_2$。在 $q_1$ 定位 (19)。
由 (4)，左边为零；由 (14)，右边是 $a_{12,m}$ 乘原未分歧局部群的一个单位生成元。因此
\[
a_{12,m}=0\quad\text{于 }\mathcal O/p^m,
\qquad p^{b_p}D\kappa_{12,m}=0.
\]
置
\[
B_p=b_p+v_p(D).
\tag{20}
\]
$D/p^{v_p(D)}$ 是 $\mathcal O$-单位，故得到 (5)。该指数与 $m,q_1,q_2$ 无关；没有给出其跨 p 上界或断言它等于零。

若 $m>B_p$，系数映射
\[
T/p^m\xrightarrow{\rm quot}T/p^{m-B_p}
 \xrightarrow{p^{B_p}}T/p^m
\]
的复合是乘 $p^{B_p}$。
第二箭头在 $H^1(K,-)$ 上单射：相应短正合列的左端障碍为
$H^0(K,T/p^{B_p})=0$，仍由原十七惯性 $-1$ 得到。
所以 (5)推出 $\kappa_{12,m}$ 约到 $H^1(K,T/p^{m-B_p})$ 为零。
这正是 (6)，因为所有 $\pi_m$ 由同一个原 $x_{12}$ 的系数增广定义，约化彼此相容。

最后，
\[
(A_1\otimes A_2)/(j_1,j_2)\simeq\mathcal O/(h_1,h_2)
\]
且 $p^M\mid h_1,h_2$，所以 (7)是准确的系数核。
对
\[
0\to J_{12,M}\otimes T
 \to A_1\otimes A_2\otimes T
 \to T/p^M\to0
\]
取上同调。(6)给存在性，$H^0(K,T/p^M)=0$ 给唯一性，得 (8)。

## 7. 本结论没有越过的门

- $c_1\ne0$ 是结论 B 的输入。未从 (5)–(8)反推该输入。
- (5)是实际原双导数的统一有界阶；(6)–(8)是实际原增广子格条件。它们没有给原双新类的 scalar $p^m$ 整除。
- $\mathcal Q_m$ 和原双新类随着 $m,q_i$ 改变。不能令 $m\to\infty$ 后宣称某一固定 $x_{12}$ 为零。
- 本文没有宣称 $b_p=0$、$p\nmid D$ 或 wild 版误差独立于 wild 深度。
- 原 ordinary 局部化、R893 的 $s=0$ 和无穷目标系数素数仍开。这里的全部 $q_i$ 都是固定 p 后的辅助素数，不能计入目标 p。

## 依据

- R891，尤其附录 B：原底类非零时 balanced Selmer 秩一、最小系数环、原坏位有理消失与饱和格。
- 原 finite-test Chebotarev 注附录 A.1–A.2：原两个 CM 符号在最小环上的联合满像；本文 §4 将其用于惰性平方。
- R900 附录 A、R901 附录 B：同一个原 Möbius 双新类、真实群环与唯一整增广提升。
- R908，尤其 §§3–5、附录 A：完整局部单射与固定跨 p tame 尺度 D。
- R921 §8：原 ordinary 两 p 位的整／残余 H0 消失。
- 通常的有限扩张 Chebotarev 定理、inflation–restriction，以及数域固定有限分歧集上的 p-adic Galois 上同调有限生成性；未使用新的预稿定理。

全篇为符号证明，没有执行数学程序。

## 后继：R945 的准确指数

[R945](R945-original-residual-selmer-and-augmentation-exponent.md)在同一原 c1≠0 前提下，对完整残余Selmer直接证明可取 b_p=v，其中一次固定的原坐标 c1⁰=p^v z，z为原饱和Selmer本原元。原坏位实际惯性给统一坏位损C=0。故本篇实际双新界可取 B_p=v+v_p(D)；D仍保留，H¹(J)与JH¹之别不变，也不付ordinary或s=0。
