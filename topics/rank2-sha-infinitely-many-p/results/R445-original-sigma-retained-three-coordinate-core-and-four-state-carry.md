# R445 — 保留原 sigma 输入的三坐标完整核心与四态 carry

日期：2026-11-14。**状态：已证明。** 本篇不先将独立 sigma 输入
卷掉，而在同一个原三变量测度上保留它。总伴随输出及一个真正正交
输出的整个 theta degree 分别为 $7956,85680$。第一算子的平方为一；
第二算子的绝对平方由原三输入同时深的非零张量锚定，准确为二挠算子

\[
K_{85680}^2=\frac12\sum_{t\in E[2]}T_t^{(85680)}-I.
\]

实际来源只需四条固定整态。所有独立输出深度、原 sigma 的单位条件、
carry 内部测试和移动中心都因此有完整联合返回。忘掉第三输出后，
准确还原 R442 的两个 carry 公式；不把这个忘却步骤倒过来用于隐藏
输入条件。R441 的已知非零域原来是两个新输出均为单位的斜管；本文
将其准确送进同一原来源的两层单位 carry，但保留一条真实内部斜管
条件，未由整个 carry 的恒等式推出原完整中央非零。

## 1. 同一原测度的三个整坐标

保持 R439 的固定 ray 和全部原规范：

\[
\pi_0\equiv158774527+130245570\omega\pmod{253955520},
\qquad \omega^2+\omega+1=0,
\]
\[
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad
\eta=\eta_{5,p}\in\{1,-1\},\qquad p>19.
\tag{1}
\]

原残余两态为 R439 的 $\mathcal L_0,\mathcal L_1$，原输入记为

\[
\rho_i=\nu_{\mathcal L_i}(W,Q)\otimes\nu_\sigma(c),\qquad i=0,1.
\]

它们的完整 $W,Q,c$ 核心分别是 $-\lambda,\eta\lambda$
乘两态交换、$-\lambda$。这里 $c$ 是同一独立 sigma 的输入，
没有改为仅有相同边际的辅助来源。

定义新输出

\[
\boxed{A=Q+26c,\qquad U=Q-280c,\qquad W=W.}
\tag{2}
\]

变换矩阵和完整 Gram 式为

\[
M=\begin{pmatrix}1&0&0\\0&1&26\\0&1&-280\end{pmatrix},
\quad \det M=-306,
\quad M\operatorname{diag}(52,7280,1)M^{\mathsf t}
 =\operatorname{diag}(52,7956,85680).
\tag{3}
\]

逆式准确为

\[
\boxed{c=(A-U)/306,\qquad
Q=(280A+26U)/306=(140A+13U)/153.}
\tag{4}
\]

因为 $306=2\cdot3^2\cdot17$，这是当前每个普通处的整自同构。
原物理输出仍然是

\[
\boxed{Y=(17W+A)/26,\qquad X=(9W-A)/26.}
\tag{5}
\]

尤其，任何条件 $c\in\mathbf Z_p^\times$、$Q\in p^r$ 都可以
用 (4) 精确恢复。没有隐藏输入被遗忘。

## 2. 真正的三变量整 theta 张量

令 $\nu_i=M_*\rho_i$。其完整生成函数是

\[
\boxed{\Phi_i(w,a,u)
 =\sigma(26a-280u)\mathcal L_i(w,a+u).}
\tag{6}
\]

由原 $\mathcal L_i\in\mathcal S_{52}\boxtimes\mathcal S_{7280}$，
三个 degree 和交叉项准确为

\[
N_W=52,\quad N_A=26^2+7280=7956,\quad
N_U=280^2+7280=85680,
\quad 26(-280)+7280=0.
\tag{7}
\]

$W$ 与另外两轴的交叉项已由 R439 消去。两个新 sigma 系数
$26,-280$ 都为偶数，所以原 odd sigma 的半特征在新轴周期上
为平凡；$\mathcal L_i$ 的两个 degree 也均为偶数。因此 (6)
是整个无平坦 twist 的外积线丛截面：

\[
\boxed{\Phi_i\in\mathcal S_{52}\boxtimes\mathcal S_{7956}
                         \boxtimes\mathcal S_{85680}.}
\tag{8}
\]

这还是整张量格中的元素。原 Amice 级数整有界，(2) 是整线性
输入变换；R413 的原正式群基
$\sigma^Nx^j,\sigma^Nyx^j$ 首阶互异、首系数为单位。
在其三重张量基中按首阶逐项消元，系数逐个整。此处没有除以可能
含 $p$ 的大阶乘，也不以有限 Taylor 截断替代全局截面性质。

## 3. 整个 A 空间的绝对平方

统一使用 R413 的完整整核心

\[
K_N=\frac{\bar\pi_{17}}p\mathscr M_{\pi_{17}},\qquad
\pi_{17}=-\pi_0,
\qquad \nu_F|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_NF}.
\tag{9}
\]

记 $K_W=K_{52},K_A=K_{7956},K_U=K_{85680}$，分别作用于
(8) 的三条轴，故互相交换。R431 已付整个 $K_W^2=I$。

当前固定 ray 在完整中心模数上给

\[
\boxed{g=\pi_0/\bar\pi_0\equiv2107\pmod{15912},\qquad
2107^2=1+279\cdot15912.}
\tag{10}
\]

因此 $K_A^2$ 与整个 Heisenberg 群交换，先得它是一个标量。
使用真实非零张量锚

\[
\Phi_0(w,a,0)=\sigma(26a)\mathcal L_0(w,a)
             =\widetilde{\mathcal K}_0(w,a).
\tag{11}
\]

R431 的同一原小核给 $K_A\widetilde{\mathcal K}_0 =\widetilde{\mathcal K}_0$。在 $w$ 的任一非零系数上，
这就是一条非零 $\mathcal S_{7956}$ 锚，故平方标量为一：

\[
\boxed{K_A^2=I\quad\text{于整个 }\mathcal S_{7956}.}
\tag{12}
\]

同一含中心交织与同一非零锚还付 $K_A$ 是固定算子：当前 ray
内两个普通素数的算子只差标量，而 (11) 的已付像固定该标量。
不需要计算整个 $7956$ 阶矩阵或另选未知中央值定标。

## 4. 整个 U 空间的平方形状

写 $N=85680$。同一 ray 的精确约化为

\[
\boxed{g\equiv95131+128520\omega\pmod{171360},\qquad
g^2\equiv42841+85680\omega\pmod{171360}.}
\tag{13}
\]

两条格基的像分别为

\[
g^2\cdot1=42841+N\omega,\qquad
g^2\cdot\omega=-N-42839\omega.
\]

它们的两个对称 lift 交叉指数模 $2N$ 都为 $N$。在标准
Schrödinger 基 $Xe_j=\zeta_N^je_j,Ze_j=e_{j+1}$ 中，完整平方
交织因而是

\[
K_U^2X(K_U^2)^{-1}=-X^{42841},\qquad
K_U^2Z(K_U^2)^{-1}=-Z^{42841}.
\tag{14}
\]

这两个负号不能从模 $N$ 的约化中删去。
因 $N/4=21420$ 为偶数，原二挠 lift 满足

\[
T_{(s+r\omega)/2}^{(N)}e_j=(-1)^{sj}e_{j+Nr/2}.
\]

定义固定整算子

\[
B_U=\frac12\sum_{t\in E[2]}T_t^{(N)}-I.
\]

逐基求和得到

\[
\boxed{B_Ue_j=(-1)^je_{42841j+42840},\qquad B_U^2=I.}
\tag{15}
\]

它实现 (14) 的同一个完整交织，所以 $K_U^2=c_pB_U$，尚须
支付绝对标量 $c_p$。下一节使用原三输入而非假定另一个 norm 锚。

## 5. 原三输入同时深付清绝对标量

先看实际张量的二挠行为。对任意 $t\in E[2]$，(6) 中
$u\mapsto u+t$ 使 sigma 参数平移 $-280t\in2\Lambda$，
其 odd 半特征为正；同时使 $\mathcal L_i$ 的 $Q$ 参数平移 $t$，
后者由 R439 在整个 $Q$ 二挠群下固定。准周期的交叉项由 (7)
准确抵消。因此

\[
\boxed{T_{t,U}^{(N)}\Phi_i=\Phi_i,\qquad B_U\Phi_i=\Phi_i.}
\tag{16}
\]

由 (3)，原 $W,Q,c$ 同时深一层，等价于新 $W,A,U$ 同时深一层。
先用原三个输入核心，系数为

\[
(-\lambda)(\eta\lambda)(-\lambda)=\eta\lambda^3,
\]

且 $i$ 变为 $1-i$。再用新三轴 (9)，消去共同的非零缩放及
$\lambda^3$，得到完整张量身份

\[
\boxed{K_WK_AK_U\Phi_i=\eta\Phi_{1-i},\qquad i=0,1.}
\tag{17}
\]

两边再作用同一算子，使用 $\eta^2=1$、轴算子交换以及
$K_W^2=K_A^2=I$，严格得

\[
K_U^2\Phi_i=\Phi_i.
\tag{18}
\]

原 $\Phi_0$ 非零；(16)、(18) 与 $K_U^2=c_pB_U$ 共同迫
$c_p=1$。于是整个空间的绝对公式是

\[
\boxed{K_{85680}^2=B_U=\frac12\sum_{E[2]}T_t^{(85680)}-I,
\qquad K_{85680}^4=I.}
\tag{19}
\]

这里的锚是同一个非零联合来源，不依赖其任何未知 Mellin 导数。

## 6. 四条固定整来源的完整闭包

定义

\[
\Psi_i=K_A\Phi_i,\qquad i=0,1.
\tag{20}
\]

它们由固定整算子作用于实际 (6)，故也是固定整来源。无需假设
这四条线性独立。原 $W$ 核心给 $K_W\Phi_i=-\Phi_i$，再由
轴算子交换，$K_W\Psi_i=-\Psi_i$。结合 (12)、(17)，完整得到

\[
\boxed{
\begin{array}{c|cc}
 &\Phi_i&\Psi_i\\ \hline
K_W&-\Phi_i&-\Psi_i\\
K_A&\Psi_i&\Phi_i\\
K_U&-\eta\Psi_{1-i}&-\eta\Phi_{1-i}
\end{array}}
\tag{21}
\]

所以 $\eta K_U$ 在这个实际闭包上也固定。以任一非零 (21)
的锚和完整交织比较，还可知整个 $\eta K_U$ 在当前 ray 上固定；
本篇不需要将真实符号 $\eta_{5,p}$ 猜成一个常数。

令 $P$ 交换 $\Phi_i,\Psi_i$，令 $I$ 同时交换两组中的下标
$0,1$。它们交换且平方为一。对任意非负整数 $r,s,t$，所有
另外输出测试都保留的测度式为

\[
\boxed{
\nu_{\Phi_i}|_{\{W\in p^r,A\in p^s,U\in p^t\}}
=(-\lambda)^r\lambda^s(-\eta\lambda)^t
 [\kappa^r,\kappa^s,\kappa^t]_*
 \nu_{P^{s+t}I^t\Phi_i}.}
\tag{22}
\]

同式也适用于 $\Psi_i$。这是全部三输出的完整联合限制，而非
三个边际公式的拼接。

## 7. 保留原 c 的准确 carry

任意 $r\ge1$，原外部 carry 域是

\[
\Gamma_r=\{A\in p^r,\ (Q,c)\notin p^r\mathbf Z_p^2\}.
\]

(4) 是整可逆变换，所以准确等价于

\[
\boxed{\Gamma_r=\{A\in p^r,U\notin p^r\}.}
\tag{23}
\]

由 (22) 的 $A$ 深与 $A,U$ 同深两式相减，得到保留完整
$U$ 输出的身份

\[
\boxed{\begin{aligned}
\nu_{\Phi_i}|_{\Gamma_r}
={}&\lambda^r[1,\kappa^r,1]_*
              \nu_{P^r\Phi_i}\\
 &-(-\eta)^r\lambda^{2r}[1,\kappa^r,\kappa^r]_*
              \nu_{\Phi_{i+r\bmod2}}.
\end{aligned}}
\tag{24}
\]

这里没有把 $U$ 质量取掉。因此对原 $c$ 的任意连续测试都
仍合法。若左侧还加 $W\in p^n$，就在右边两项同时使用 (22)
的 $W$ 核心和真实 $W$ 参数；不更改 sigma 的条件。

只规范化确实深的总输出 $A/\kappa^r$，(24) 变为

\[
\boxed{\begin{aligned}
 (W,A/\kappa^r,U)_*(\mathbf1_{\Gamma_r}\nu_{\Phi_i})
 ={}&\lambda^r\nu_{P^r\Phi_i}\\
 &-(-\eta)^r\lambda^{2r}[1,1,\kappa^r]_*
                         \nu_{\Phi_{i+r\bmod2}}.
\end{aligned}}
\tag{25}
\]

为说明移动测试不能遗漏，若在 (24) 左侧测试原 $f(W,Q,c)$，
第一项的原输入精确变为

\[
Q=\frac{280\kappa^r A+26U}{306},\qquad
c=\frac{\kappa^r A-U}{306};
\tag{26}
\]

第二项则是

\[
Q=\kappa^r\frac{280A+26U}{306},\qquad
c=\kappa^r\frac{A-U}{306}.
\tag{27}
\]

例如 $r=1$ 的 carry 上 $c$ 必为单位，因为 $A\in p,U$ 为
单位；但 $r\ge2$ 时 $U\notin p^r$ 允许中间赋值，不能把整个
carry 都称为两个单位输入。逐层环带仍须按 (23)、(26) 保留。

## 8. 忘却 U 后准确还原原两 carry

只有在测试本来不含 $U$ 或原 $c$ 时，才可以把 (25) 推到
$(W,A)$。在生成函数中这是取 $u=0$。由 (11)、R443 的完整
总伴随作用和 $K_A$ 与该取值交换，得到

\[
\boxed{
\Phi_0\mapsto\mathcal K_0,\quad
\Phi_1\mapsto\mathcal K_1,\quad
\Psi_0\mapsto\mathcal K_0,\quad
\Psi_1\mapsto\mathcal K_1^R.}
\tag{28}
\]

所以 $r=1$ 的 (25) 准确成为

\[
\lambda\mathcal K_0+\eta\lambda^2\mathcal K_1,
\qquad
\lambda\mathcal K_1^R+\eta\lambda^2\mathcal K_0.
\tag{29}
\]

偶数 $r$ 时则为

\[
\lambda^r(1-\lambda^r)\mathcal K_i,
\tag{30}
\]

正是 R442 的原公式。反过来，(29)、(30) 只有忘却后的信息，
不足以对 $c$ 单位或 $Q$ 深追加条件；这类条件须使用 (24)。

## 9. 原非零单位管的准确位置

R441 的真实域，对正偶数 $n$，是

\[
\mathscr D_n=\{W,Q\in p^n,\ c\in\mathbf Z_p^\times\}.
\]

在本篇保全部输入的新坐标中，准确为

\[
\boxed{\mathscr D_n=
\{W\in p^n,\ 140A+13U\in p^n,\ A-U\text{ 单位}\}.}
\tag{31}
\]

该域中 $A=Q+26c,U=Q-280c$ 都为单位，因为 $p>19$ 排除了
$26,280$ 的所有素因子。其斜率条件是

\[
U\equiv-(140/13)A\pmod{p^n}.
\tag{32}
\]

相反，(23) 的 carry 要求 $A$ 深；这两种域确实不交。
在 $A$ 轴或 $U$ 轴施加 (22) 时，原 $Q,c$ 均按 (4) 移动，
不能保持 (31) 不变而只给中央乘一个标量。

R441 已证在 $\mathscr D_n$ 上的同一 $X^6$ 原中央值准确有
赋值 $5n$，而完整中央为单位倍 $14976b\Omega^6J'_S(0)$。
下面将这条非零管送进实际 carry，明确保留其内部测试。

### 9.1 同一原来源中真正的两层单位 carry 管

任意 $r\ge1$，记 $S_r(W,A,U)=(W,\kappa^rA,U)$，并令

\[
\mathscr D'_{n,r}=S_r\mathscr D_n.
\]

它的准确整坐标条件是

\[
\boxed{\begin{gathered}
W\in p^n,\qquad A'\in p^r,\\
140A'/\kappa^r+13U\in p^n,\qquad
A'/\kappa^r-U\text{ 单位}.
\end{gathered}}
\tag{33}
\]

由 (31)，这里 $A'/\kappa^r$ 与 $U$ 都为单位，所以 $v_p(A')=r$。
对于新的原输入

\[
c'=(A'-U)/306,\qquad Q'=(140A'+13U)/153,
\]

两者也都为单位；其总和 $Q'+26c'=A'$ 相消到恰好 $r$ 层。
因此 (33) 是原真实单位 carry 中一条具体斜管。

对来源 $P^r\Phi_i$ 使用完整 $A$ 核心，且 $P^{2r}=I$，得

\[
\boxed{\nu_{P^r\Phi_i}|_{\mathscr D'_{n,r}}
 =\lambda^r(S_r)_*
                (\nu_{\Phi_i}|_{\mathscr D_n}).}
\tag{34}
\]

在右边使用 R441 的同一原中央测试，左边必须使用

\[
Y_r=(17W+A'/\kappa^r)/26,\qquad
X_r=(9W-A'/\kappa^r)/26,
\]

\[
F_r=\mathbf1_{Y_r\ {\rm unit}}d\log_p\langle Y_r\rangle X_r^6.
\tag{35}
\]

于是对 $i=0$ 和每个正偶数 $n$，准确有

\[
\boxed{\int_{\mathscr D'_{n,r}}F_r\,d\nu_{P^r\Phi_0}
       =\lambda^r\mathcal C_n,\qquad
v_p\!\left(\int_{\mathscr D'_{n,r}}F_r\,d\nu_{P^r\Phi_0}\right)=5n.}
\tag{36}
\]

尤其固定 $r=2$ 时，$P^2\Phi_0=\Phi_0$，所以完全回到同一
原 $\sigma(c)\otimes\mathcal L_0$，没有额外联合来源。其规范总输出
正是 R442 两层 carry 使用的 $A'/\kappa^2$。

仍须区别整个 carry 和 (33) 的内部斜管。忘掉 $U$ 后，整个两层
carry 的同一测试为 $\lambda^2(1-\lambda^2)$ 乘完整原中央；而
(36) 还保 $140A'/\kappa^2+13U\in p^n$、$W\in p^n$ 等条件。
完整中央零不会自动把这些更细条件内的积分逐个赋零。
本篇已经支付真实域运输；余下是这条明确非零管与其完整 carry
补域的抵消问题。主目标仍未完成。

## 依赖

- [R413：任意偶 degree 的完整整 theta 核心与三输出方法](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R431：整个 degree52 与原总伴随的实际锚](R431-original-degree52-full-core-and-fixed-thirteen-ray.md)。
- [R439：同一固定 ray、原两态及 Q 二挠固定性](R439-original-residual-companion-two-state-core-and-exact-depth-comparison.md)。
- [R443：乘回 sigma 后两态的准确反射核心](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R442：忘却原 sigma 输入后的完整 carry 与全部外部补域](R442-original-external-carry-matrix-and-complete-boundary-equations.md)。
- [R441：原同深非零域及完整中央比例](R441-original-sixth-moment-row-and-uniform-same-depth-nonvanishing.md)。
