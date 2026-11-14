# R442 — 原外部两输入 carry 矩阵与完整边界方程

日期：2026-11-14。**状态：已证明。** 本篇始终保原 $W$ 轴，
在同一个 $\nu_\sigma(c)\otimes\nu_{\mathcal L_i}$、$i=0,1$ 中处理
外部相加 carry。两个单位输入相消到一层深度后，规范化的真实
carry 中央行组成一个行列式为单位的两行矩阵。
其一条明确单位线性组合与原 $J'_S(0)$ 完全等价；
不要求把新来源 $\mathcal K_1$ 的中央先设为零。

全来源级还保留 $\mathcal K_1-R_Y\mathcal K_1$。
这个余项只有在完整第一 principal 测试下才被杀掉；
加 $W$ 深条件后，余项准确成为 $W$、$V$ 两条不同深管之差。
本篇同时给真实两层 carry 的全来源返回，以及 R441 同深非零域
与整个原条件中央之间的全部外部分支。
规范化总输出与原总输出、残余深条件与整体输出深条件均未混用。
主目标未完成。

## 1. 同一个两态乘积来源和实际输出

沿用 R431、R437、R439、R441 的同一固定普通 ray、原周期，
写
$$
\lambda=-\bar\pi_0^{-1},\qquad
\lambda_\sigma=-\lambda,\qquad
\kappa=p/\bar\pi_0^2,\quad v_p(\kappa)=1,\quad
\eta=\eta_{5,p}\in\{\pm1\}.
\tag{1}
$$
原 $1-\lambda$、$1+\lambda$ 均为单位。
令 $C=26c$，其测度为同一原 $[26]_*\nu_\sigma$，
没有把周期重新规范化。记
$$
\rho_i=\nu_{\mathcal L_i}(W,Q)\otimes[26]_*\nu_\sigma(C),
\qquad i=0,1,
$$
其中是 R439 的实际固定两态
$$
\mathcal L_0=\mathcal L,\qquad
\mathcal L_1=\frac18\sum_{t\in E[4]}T_{t,Q}^{(7280)}\mathcal L.
$$
实际总输出、物理输出为
$$
\boxed{A=Q+C,\qquad
Y=(17W+A)/26,\qquad X=(9W-A)/26.}
\tag{2}
$$
令 $\mathfrak k_i=(W,A)_*\rho_i$。
其物理来源就是
$\mathcal K_i=\sigma(26q)\mathcal L_i(w,q)$ 经同一坐标读取，
$\mathcal K_0$ 为原 R430 小核。

R439 的完整输入 core 准确给
$$
\boxed{
\rho_i|_{\{W\in p^a,\ Q\in p^b,\ C\in p^c\}}
=(-\lambda)^{a+c}(\eta\lambda)^b
 [\kappa^a,\kappa^b,\kappa^c]_*
                         \rho_{\,i+b\bmod2}.}
\tag{3}
$$
这里三个指数都可独立，全部另外输出仍保留。

## 2. 原总 A 的实际核心，保新的反射态

设 $R=R_Y$ 是物理第一输入的普通反射
$(Y,X)\mapsto(-Y,X)$。
R443 已在完整原 theta 格上支付
$$
K_{34}=R_Y,\qquad K_{18}=-I,
$$
并由真正总和核心与全深域比较得到总 $A$ 的完整作用：
$$
\boxed{
\begin{aligned}
\mathfrak k_0|_{A\in p}
 &=\lambda[1,\kappa]_*\mathfrak k_0,\\
\mathfrak k_1|_{A\in p}
 &=\lambda[1,\kappa]_*(R_*\mathfrak k_1),\\
(R_*\mathfrak k_1)|_{A\in p}
 &=\lambda[1,\kappa]_*\mathfrak k_1.
\end{aligned}}
\tag{4}
$$
$R_*\mathfrak k_0=\mathfrak k_0$。
这些是保 $W$ 的真正核心公式，不是从两个相同边际拼出的等式。

须区分：核心的坐标缩放保 $W$，但来源 $R_*\mathfrak k_1$
本身是完整反射后的另一来源。$R$ 在 $(W,A)$ 坐标中是
$$
\boxed{\binom{W}{A}\longmapsto
\frac1{13}
\begin{pmatrix}-4&-1\\-153&4\end{pmatrix}
\binom{W}{A}
=\binom{V}{-P_*},}
\tag{5}
$$
其中 $V=X-Y,\ P_*=9Y+17X$。
它一般不保持 $W$ 的深度条件。

迭代 (4)，对 $i=0,1$ 有
$$
\boxed{
\mathfrak k_i|_{A\in p^r}
=\lambda^r[1,\kappa^r]_*(R^r_*\mathfrak k_i).}
\tag{6}
$$
对 $i=0$，反射始终固定该来源；对 $i=1$，它在两条真实来源中交替。
下文没有把 $R_*\mathfrak k_1$ 写成 $\mathfrak k_1$。

## 3. 第一层真正的单位消去 carry

置
$$
\alpha=-\eta\lambda^2\in\mathcal O^\times.
\tag{7}
$$
由 (3)，两个外部输入同时深的完整推前为
$$
(W,A)_*(\rho_i|_{\{Q,C\in p\}})
=\alpha[1,\kappa]_*\mathfrak k_{1-i}.
\tag{8}
$$
当 $A\in p$ 时，若 $Q,C$ 不同时在 $p$，就必定两者都是单位。
所以定义实际单位 carry
$$
\mathscr B_i(1)=\{Q,C\in\mathbf Z_p^\times,\ A=Q+C\in p\},
$$
并用真正的普通尺度规范化其总输出：
$$
\mathfrak b_{i,1}
=(W,A/\kappa)_*(\mathbf1_{\mathscr B_i(1)}\rho_i).
\tag{9}
$$
$A/\kappa$ 只在显示的深域上使用，故仍为整坐标。
从 (4) 减去 (8)，完整得到
$$
\boxed{
\mathfrak b_{0,1}
=\lambda\mathfrak k_0+\eta\lambda^2\mathfrak k_1,\qquad
\mathfrak b_{1,1}
=\lambda R_*\mathfrak k_1+\eta\lambda^2\mathfrak k_0.}
\tag{10}
$$
这保 $W$ 的任意完整测试，没有丢掉输入 carry 或改变第二态的来源。

因此来源级的消元式准确为
$$
\boxed{
\mathfrak b_{0,1}-\eta\lambda\mathfrak b_{1,1}
=\lambda(1-\lambda^2)\mathfrak k_0+
       \eta\lambda^2(\mathfrak k_1-R_*\mathfrak k_1).}
\tag{11}
$$
最后一个完整余项一般非零。

## 4. 真正两层 carry 的全来源返回

任意 $r\ge1$，定义
$$
\mathscr G_i(r)=
\{A\in p^r,\ (Q,C)\notin p^r\mathbf Z_p^2\},
$$
$$
\mathfrak g_{i,r}
=(W,A/\kappa^r)_*
                    (\mathbf1_{\mathscr G_i(r)}\rho_i).
$$
共同 $r$ 层输入 core 的系数是 $\alpha^r$、来源变为
$\mathfrak k_{i+r\bmod2}$。由 (6)，完整得到
$$
\boxed{
\mathfrak g_{i,r}
=\lambda^rR_*^r\mathfrak k_i
             -\alpha^r\mathfrak k_{i+r\bmod2}.}
\tag{12}
$$
尤其对每个偶数 $r$，
$$
\boxed{\mathfrak g_{i,r}
=\lambda^r(1-\lambda^r)\mathfrak k_i.}
\tag{13}
$$
取 $r=2$，比例 $\lambda^2(1-\lambda^2)$ 是当前原 ray 上已付单位。
这里不需要第一 principal 测试杀余项；这是完整来源身份。

还可把 (12) 逐个写回真实单位输入管。
在 $\mathscr G_i(r)$ 上，必有
$v_p(Q)=v_p(C)=j<r$；不同 $j$ 不交。
设
$$
\mathfrak b_{i,s}
=(W,A/\kappa^s)_*
 \bigl(\mathbf1_{\{Q,C\ {\rm unit},\ A\in p^s\}}\rho_i\bigr).
$$
对共同深度 $j$ 用 (3)，得到精确分拆
$$
\boxed{\mathfrak g_{i,r}
=\sum_{j=0}^{r-1}\alpha^j\mathfrak b_{i+j\bmod2,r-j}.}
\tag{14}
$$
例如
$$
\boxed{\mathfrak b_{0,2}
-\eta\lambda^2\mathfrak b_{1,1}
=\lambda^2(1-\lambda^2)\mathfrak k_0.}
\tag{15}
$$
两个 carry 的原始深度分别为二和一，必须分别使用
$A/\kappa^2$、$A/\kappa$，之后才是同一个规范输出的等式。
不能把它改写成两份原总输出 $A$ 的同一个测试。

## 5. 两条真实 carry 中央行的单位消元

对任意连续 $h(X)$，记
$$
F_{u,h}(W,A)
=\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}h(X),
\quad (Y,X)\text{ 按 (2) 读取},
$$
$$
\Gamma_i(u,h)=\int F_{u,h}\,d\mathfrak k_i,\qquad
B_i(u,h)=\int F_{u,h}\,d\mathfrak b_{i,1}.
$$
$F_{u,h}$ 对真实反射 $Y\mapsto-Y$ 不变，因为 principal 部分
$\langle-Y\rangle=\langle Y\rangle$，而 $X$ 不变。
所以在这个**完整测试**下，
$\int F_{u,h}\,dR_*\mathfrak k_1=\Gamma_1(u,h)$。
(10) 因而给准确两行矩阵
$$
\boxed{
\binom{B_0(u,h)}{B_1(u,h)}
=\lambda
 \begin{pmatrix}1&\eta\lambda\\\eta\lambda&1\end{pmatrix}
 \binom{\Gamma_0(u,h)}{\Gamma_1(u,h)}.}
\tag{16}
$$
其行列式为 $\lambda^2(1-\lambda^2)\in\mathcal O^\times$。

原 (R430) 条件中央全函数是
$$
\Gamma_0(u,h)=-\frac23J_S(u)\int h\,d\nu_{G_{18}}.
$$
故无需对新 $\Gamma_1$ 作任何零假设，已准确得到
$$
\boxed{
B_0(u,h)-\eta\lambda B_1(u,h)
=-\frac23\lambda(1-\lambda^2)J_S(u)
                          \int h\,d\nu_{G_{18}}.}
\tag{17}
$$
左侧是真正两个单位 carry 中使用规范总输出的同一 principal 行。

在原中央求导，并取 R441 的 $h(X)=X^6$，
$$
\boxed{
B'_0(0,X^6)-\eta\lambda B'_1(0,X^6)
=14976b\Omega^6\,\lambda(1-\lambda^2)\,J'_S(0).}
\tag{18}
$$
显示比例为单位。因此原算术中央零与这个完整两 carry 行的
单位组合零严格等价。
这没有把 $B'_0$、$B'_1$ 或 $\Gamma'_1$ 分别赋为零。

## 6. 加 W 深条件后的准确余项

若额外插入 $W\in p^N$，(11) 仍是完整测度等式，
但反射余项不再由 principal 性自动消失。
令 $\Gamma_{i,W^N}'(h)$ 表示 $\mathfrak k_i$ 在
$W\in p^N$ 的原第一中央行；同样定义 $\Gamma_{i,V^N}'(h)$。
由 (5)，且主中央测试本身对 $Y$ 反射不变，严格得到
$$
\boxed{\begin{aligned}
&B'_{0,W^N}(0,h)-\eta\lambda B'_{1,W^N}(0,h)\\
&=\lambda(1-\lambda^2)\Gamma'_{0,W^N}(h)
 +\eta\lambda^2
       \{\Gamma'_{1,W^N}(h)-\Gamma'_{1,V^N}(h)\}.
\end{aligned}}
\tag{19}
$$
在 $Y$ 为单位处，$W\in p$ 与 $V\in p$ 不可能同时成立，
因为 $2Y=W-V$；这是两条真实不同的管。

所以不能在 (18) 上直接附加 $W$ 深限制。
即使用 (13) 的偶层全来源式避免反射余项，其右侧也变成
$\Gamma'_{0,W^N}$，不是已知的完整 $\Gamma'_0$。
原 $J'_S(0)=0$ 并未单独控制这一附加条件。

式 (19) 保的是规范化 carry 的 $W$ 坐标；
它确由全部输入运算原样保留。
如果同时要求一个 $R$ 不变的域，例如对称的 $W/V$ 条件和，
反射余项可以相消，但该附加域中的原 $\Gamma_0$ 仍须另付，
不能由完整 (17) 免费分配。

## 7. R441 的同深域与原完整中央的全部外部分支

以下始终在同一个 $\rho_0(W,Q,C)$ 上，使用原总输出
$A=Q+C$，不作 carry 规范化。
令
$$
F_h(W,A)=\mathbf1_{Y\ {\rm unit}}d\log_p\langle Y\rangle h(X).
$$
取任意 $N\ge1$。当 $W\in p^N$ 时，原 $Y$ 为单位等价于
$A$ 为单位。
此时至少一个 $Q,C$ 为单位，实际域有如下不交分拆：

| 域 | 原输入条件，均另保 $W\in p^N$ |
|---|---|
| $\mathscr D_N^Q$ | $Q\in p^N,\ C$ 单位 |
| $\mathscr D_N^C$ | $C\in p^N,\ Q$ 单位 |
| $\mathscr S_{j,N}^Q$ | $v_p(Q)=j,\ C$ 单位，$1\le j<N$ |
| $\mathscr S_{j,N}^C$ | $v_p(C)=j,\ Q$ 单位，$1\le j<N$ |
| $\mathscr H_N$ | $Q,C$ 都单位，$Q+C$ 仍为单位 |

此外保完整外域
$$
\mathscr O_N=\{W\notin p^N,\ Y\text{ 单位}\}.
$$
这些域准确穷尽整个原 $Y$ 单位域：如果 $Q,C$ 都非单位，则
$A$ 非单位；如果两者单位，就必须保总和是否仍为单位的 carry。

令各符号的花体积分表示在对应域测试同一个 $F_h$。
对 $h=X^6$，原完整中央因而准确为
$$
\boxed{\begin{aligned}
14976b\Omega^6J'_S(0)
={}&\mathcal C_N+\mathcal D_N^C
 +\sum_{j=1}^{N-1}
       \left(\mathcal S_{j,N}^Q+\mathcal S_{j,N}^C\right)\\
 &+\mathcal H_N+\mathcal O_N.
\end{aligned}}
\tag{20}
$$
这里 $\mathcal C_N$ 是 R441 的同一真实域：
$C=26c$ 为单位，残余 $W,Q$ 同时深。
对每个正偶数 $N$，已经严格有 $v_p(\mathcal C_N)=5N$。

其余每一项都保留原总输出与真实单位条件。
特别 $\mathscr H_N$ 是两个单位输入的**不相消**支；
(9)、(12) 的 carry 则要求 $A$ 深。
它们与 $\mathscr D_N^Q$ 不相交，不能用同一个“单位输入”名称混同。

### 7.1 所有单输入深度与环带的来源式

为使 (20) 可直接接原两态，定义完整推前
$$
\mathfrak a_i(N;b,c)
=(W,A)_*(\rho_i|_{\{W\in p^N,\ Q\in p^b,\ C\in p^c\}}).
$$
(3) 给其对任意连续测试 $F$ 的准确公式
$$
\boxed{\begin{aligned}
\int F(W,A)\,d\mathfrak a_i(N;b,c)
={}&(-\lambda)^{N+c}(\eta\lambda)^b\\
&\cdot\int
 F(\kappa^NW,\kappa^bQ+\kappa^cC)
                       \,d\rho_{i+b\bmod2}.
\end{aligned}}
\tag{21}
$$
所以每一条 (20) 中的一单位支、环带都有明确的有限差：
$$
\mathscr D_N^Q:\quad
\mathfrak a_0(N;N,0)-\mathfrak a_0(N;N,1),
$$
$$
\mathscr D_N^C:\quad
\mathfrak a_0(N;0,N)-\mathfrak a_0(N;1,N),
$$
$$
\mathscr S_{j,N}^Q:\quad
\mathfrak a_0(N;j,0)-\mathfrak a_0(N;j+1,0)
-\mathfrak a_0(N;j,1)+\mathfrak a_0(N;j+1,1),
\tag{22}
$$
另一环带式交换 $b,c$ 读取，但仍按 (21) 保正确的两态与符号。

(21) 中的完整物理测试参数是
$$
Y=\frac{17\kappa^NW+\kappa^bQ+\kappa^cC}{26},\qquad
X=\frac{9\kappa^NW-\kappa^bQ-\kappa^cC}{26}.
\tag{23}
$$
它们不能简写成只给一个 Mellin 变量乘幂。
例如 $N,b,c\ge1$ 时原 $Y$ 必非单位，所以在 $F_h$ 下该项
确实为零；这是显示参数给出的域结论，不是按一条边际猜零。

## 8. 原 carry 控制与剩余零传播的精确距离

本篇得到两种完整的正向返回：

1. (10)–(18) 把原完整条件中央送入两个真实外部单位 carry，
   保第二来源及规范总和，并用单位矩阵消去新的未知行。
2. (12)–(15) 给偶层 carry 的全来源标量返回，尤其二层比例为单位。

但 R441 的已证非零域在 $W$ 深、$A$ 单位的一单位支中。
它既不属于总 $A$ 深的 carry，也不由 $W$ 未限制的
principal 奇性消去自动控制。
准确剩余量是 (19) 的两条不同深管差，以及 (20) 的不相消、
中间环带和 $W$ 外部原单位域。所有这些都已写在同一个
$\sigma(c)\otimes\mathcal L_0/\mathcal L_1$ 的实际来源和输出中，
没有用抽象参考源替代。

## 依赖

- [R439：实际残余两态、全输入 core 与输出深度](R439-original-residual-companion-two-state-core-and-exact-depth-comparison.md)。
- [R443：真实第二来源及完整总 A 反射核心](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R441：完整 X6 行与同深非零及其准确赋值](R441-original-sixth-moment-row-and-uniform-same-depth-nonvanishing.md)。
- [R430：原 principal 条件中央](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)。
- [R410：原固定 ray 上全部所用单位](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)。

