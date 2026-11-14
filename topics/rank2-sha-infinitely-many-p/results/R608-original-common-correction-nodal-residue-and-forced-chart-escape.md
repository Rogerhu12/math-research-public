# R608 — 同一原修正的结点二阶残数与被强迫的临界坐标极

日期：2026-11-14。**状态：已证明。**

本篇继续 R603 的同一两条临界支，
直接计算 R578/R597 中真正的二阶临界值项。
两支各自可能有的二阶极在求和时严格抵消；
余下至多一个简单极，其系数是显示的实际局部残数，
只由同一个首次修正的原低行决定。
任意同预算第二次修正均不能改变这个极部。

当原近支接触恰为 $s-2$ 时，
还证明同一个第一次修正不可能让两条临界支同时整延伸：
若近支保持整，远支必有一个给出首系数的简单极。
这是一条实际坐标延拓限制，不是原 $M$ 余类非零定理。
原物理目标只读取近支，其完整 Taylor 项与两条十三行继续保留。

## 1. 同一来源、两支及同一个 R

保 R597/R603 全部假设，尤其
$$
p=6s-1>101,\quad \ell\in\{1,2\},\quad
r=1,\ \nu=2,\quad f_D<p,
$$
$$
d^{C_D}\bar P=tF,\qquad
\operatorname{ord}_{Y=1}F(0,Y)=3 .
\tag{1}
$$
取同一个真正整基准 $P=P^{\rm crit}\in\mathcal W_D$，
以及 R603 的两条整非垂直临界支
$$
\mathcal EP|_{\psi_\pm}=0,\qquad
\psi_\pm(0)=1,\qquad
\Delta=\psi_--\psi_+=t\delta,\quad \delta(0)\in\mathcal O^\times.
\tag{2}
$$
$\psi_+$ 是原物理近支。
所有原角、次数帽、$P_{134}/U_0$、Gaussian 和两条十三行不变。

令
$$
A_\pm=P|_{\psi_\pm},\qquad
B_\pm=\mathcal E^2P|_{\psi_\pm},\qquad
b_*=(B_+/t^2)(0)\in\mathcal O^\times .
$$
准确有
$$
B_+=b_*t^2+O(t^3),\qquad
B_-=-b_*t^2+O(t^3).
\tag{3}
$$
这来自同一个原 $P_Y/t$ 的两简单分支；
不是为第二支另选相反的规范。

假定原第一解已由同一个
$$
R=R_{\rm bd}+S,\qquad S\in\mathcal K_{2,\ell}
\tag{4}
$$
支付 R597 的完整 $\mathcal D_\psi^+$ 条件。
特别全部二十六条 carry 已与该 $R$ 相容。
下文不再分别另选两支上的修正值。

沿近支，原低行整右逆给
$$
R_0=0\bmod w^2,\qquad
R_1=-\alpha/a\bmod w^2,\qquad
R_2=-2\beta^\sharp/a\bmod w^2,
\tag{5}
$$
其中 $\alpha=\pi_2\mathscr SA$，
$\beta=\pi_\ell\mathscr S(B_+\eta_0)$，
$\beta^\sharp$ 是 R597 指定的零延拓。
全部 $\mathscr S$ 仍是原 $w$ 中的真实 $s$ 阶移位。

由于原来源在 $t=0$ 只有 $Y$ 次数 $0,1,2$，
(5) 准确固定了整个最低纤维：
$$
\boxed{
R(0,1+u)=
-\frac{\alpha_0}{a}u+
\frac{\alpha_0-2\beta_0}{2a}u^2.}
\tag{6}
$$
所有 $Q_n,Q_{\rm quad}$ 及 $\mathcal W_D^{(2)}$ 的其余系数，
都不能改变这个整恒等。

## 2. 两支二次项之和是一个真正局部残数

令
$$
f(t,Y)=P(t,Y)/t\in\mathcal O[[t]][Y],\qquad
f_0(Y)=f(0,Y).
$$
$P$ 有原全局 $t$ 因子，
所以这一步是对固定基准的实际表达，
不是把任意修正免费除以 $t$。

由两支 (2)，在 $(0,1)$ 附近可写
$$
f_Y(t,Y)=U(t,Y)(Y-\psi_+)(Y-\psi_-),
\qquad U(0,1)\in\mathcal O^\times .
\tag{7}
$$
在 $t=0$，
$$
f_0'(1+u)=u^2h(u),\qquad
h_0=h(0)=f_0'''(1)/2\in\mathcal O^\times,\qquad
h_1=[u]h(u)=f_0''''(1)/6 .
\tag{8}
$$
这些是同一个原最低角多项式，不能用新局部模型替换。

定义同一实际修正的 Laurent 二次项
$$
\Sigma_R(t)=
\frac{((\mathcal ER)|_{\psi_+})^2}{B_+}
+\frac{((\mathcal ER)|_{\psi_-})^2}{B_-}.
\tag{9}
$$
在临界支上 $P_Y=0$，故
$B_\pm=\psi_\pm^2P_{YY}|_{\psi_\pm}$。
所以 (9) 准确等于
$$
\frac{R_Y(t,\psi_+)^2}{P_{YY}(t,\psi_+)}
+\frac{R_Y(t,\psi_-)^2}{P_{YY}(t,\psi_-)} .
\tag{10}
$$
这里 Euler 与普通法向归一的两个单位恰相消，
没有漏掉 $\psi_\pm$。

**定理 1。** 有
$$
\boxed{
\Sigma_R\in t^{-1}\mathcal O[[t]],\qquad
\operatorname{pp}_{t=0}\Sigma_R
=\frac{\mathfrak r_P}{t},}
\tag{11}
$$
其中
$$
\boxed{
\mathfrak r_P
=\operatorname{Res}_{Y=1}
 \frac{R_Y(0,Y)^2}{f_0'(Y)}\,dY
=-\frac{\alpha_0\{2(\alpha_0-2\beta_0)h_0+\alpha_0h_1\}}
 {a^2h_0^2}.}
\tag{12}
$$
在原第二精度问题中只需约化该整系数；
其值不依赖 (4) 中任一剩余 $Q_n$ 或 $Q_{\rm quad}$ 系数。

**证明。**
把 $U$ 取为 (7) 的整个单位，置
$$
G(t,Y)=R_Y(t,Y)^2/U(t,Y).
$$
它在该二支邻域是整形式函数。
因 $P_{YY}(t,\psi_\pm)
=t\,U(t,\psi_\pm)(\psi_\pm-\psi_\mp)$，
准确有
$$
\boxed{
t\Sigma_R=
\frac{G(t,\psi_-)-G(t,\psi_+)}{\Delta}.}
\tag{13}
$$
右边是真正整差商：在 $u=Y-\psi_+$ 中展开 $G$，
分子为 $\sum_{j\ge1}G_j(t)\Delta^j$，
除 $\Delta$ 后仍在 $\mathcal O[[t]]$，
因为 $\Delta\in t\mathcal O[[t]]$。
所以两个可能的 $t^{-2}$ 项严格抵消，
且 (11) 的常数准确为
$$
\left.\partial_Y\frac{R_Y(0,Y)^2}{U(0,Y)}\right|_{Y=1}
=\operatorname{Res}_{Y=1}
 \frac{R_Y(0,Y)^2}{f_0'(Y)}\,dY .
$$
这里是整个二根簇的局部残数，
不把两个重合根分别当成模 $t$ 的简单根。

由 (6)，设
$$
D_0=-\alpha_0/a,\qquad D_1=(\alpha_0-2\beta_0)/a.
$$
则
$$
\operatorname{Res}_{u=0}
\frac{(D_0+D_1u)^2}{u^2(h_0+h_1u+\cdots)}\,du
=\frac{2D_0D_1}{h_0}-\frac{D_0^2h_1}{h_0^2}.
$$
代入便是 (12)。证毕。

(13) 给整簇的全部正则剩余项，
不是只在首阶猜测两极相消。
也没有把这一局部簇换成整条临界曲线的所有根；
其它临界点及无穷远边界在全局应用时仍须保留。

## 3. 同一 p³ 来源的完整临界值系数

对任意同预算 $T\in\mathcal W_D$，取同一个
$$
Q_3=P+pR+p^2T .
\tag{14}
$$
在允许 $t$ 倒数的系数环模 $p^3$ 中，
原两个临界根各有唯一形式提升。
用 Euler 坐标写其第一位
$$
\psi_\pm^{(3)}
=\psi_\pm\exp(pv_\pm+O(p^2)),\qquad
\boxed{v_\pm=-R_{1,\pm}/B_\pm,\quad
R_{1,\pm}=(\mathcal ER)|_{\psi_\pm}.}
\tag{15}
$$
$t^2$ 乘单位在此为可逆元，$p>2$，
所以这是合法的有限 Hensel 展开；
它没有宣称这些新根属于 $\mathcal O[[t]]$。

同一实际临界值准确为
$$
\boxed{
Q_3|_{\psi_\pm^{(3)}}=
A_\pm+pR_{0,\pm}
+p^2\left(T_{0,\pm}-\frac{R_{1,\pm}^2}{2B_\pm}\right)
\pmod{p^3}.}
\tag{16}
$$
其中所有 $R_{0,\pm},T_{0,\pm}$ 均沿原整支评价。
证明为原临界 Taylor：
$B_\pm v_\pm^2/2+v_\pm R_{1,\pm}
=-R_{1,\pm}^2/(2B_\pm)$；
下一次根位移乘原一阶导数零，不影响显示系数。

$A_\pm,R_{0,\pm},T_{0,\pm}$ 全在 $\mathcal O[[t]]$。
因此两临界值之和的第二位极部准确为
$$
\boxed{
\operatorname{pp}\left[
\text{(16) 两支之和的 }p^2\text{ 系数}
\right]
=-\frac{\mathfrak r_P}{2t}.}
\tag{17}
$$
模 $p^3$ 的整体极部是 $-p^2\bar{\mathfrak r}_P/(2t)$。
任何原第二次修正 $T$ 都不能改变 (17)。

这保留的是同一个 $Q_3$ 的实际代数临界值，
而非分别给两支选择修正。
$\mathfrak r_P$ 可以为零：
例如 $\alpha_0=0$ 时必为零；
若 $f_0$ 恰为三次式，则 $h_1=0$，
另一个准确零因子是 $\alpha_0=2\beta_0$。
所以两支各自的极或某个局部单位不能代替 (12) 的完整相消。

## 4. 真实接触单位强迫至少一支离开整坐标

现在另假定原接触准确为 $s-2$：
$$
\lambda=[w^{s-2}]\bar\eta_0\ne0.
$$
于是
$$
\boxed{\bar\beta_0=\bar b_*\lambda\ne0.}
\tag{18}
$$
这是同一个原相对首核的条件，不是新增算术中央假设。

一个临界支在模 $p^2$ 仍可整延伸，
准确等价于 $\bar v_\pm$ 没有负 $t$ 项。
因 $B_\pm/t^2$ 为单位，
这也等价于
$$
\bar R_{1,\pm}\in t^2k[[t]] .
\tag{19}
$$

**定理 2。** 在 (18) 下，
(14) 的两条临界支不能同时满足 (19)。
更具体地：

1. 若 $\bar\alpha_0\ne0$，两条 $v_\pm$ 都有准确二阶极，
   首系数分别为
   $\bar\alpha_0/(\bar a\bar b_*)$ 和
   $-\bar\alpha_0/(\bar a\bar b_*)$。
2. 若近支整，即 $\bar\alpha=0$ 于 $k[w]/w^2$，
   则远支有准确简单极，且
   $$
   \boxed{
   \operatorname{pp}\bar v_-
   =-\frac{2\bar\delta(0)\bar\beta_0}
    {\bar a\bar b_*}\,t^{-1}\ne0.}
   \tag{20}
   $$
   任意同预算 $T$ 均不能在这一位改变它。

**证明。**
第一项由 (3)、(5) 和 $\psi_\pm(0)=1$ 直接得到。
若近支整，则 $\bar R_{1,+}\in t^2$，
因而 $\bar D_+=\bar R_{1,+}/\bar\psi_+\in t^2$。
R603 的同一 Hermite 余式给
$$
D_- -D_+=2\Delta\rho_2+3\Delta^2\rho_3.
$$
其原低系数是
$\rho_2(0)=(\alpha_0-2\beta_0)/(2a)$、
$\rho_3\in t$。
所以近支整时
$$
\bar D_-=-2\bar\delta(0)\bar\beta_0t/\bar a+O(t^2).
$$
系数由 (18) 为单位。
乘回 $\psi_-(0)=1$，再用
$B_-=-b_*t^2+O(t^3)$ 及 (15)，即为 (20)。

若近支不整，则本来至少有一支离开整坐标；
若近支整，则上式迫远支不整。
这证明两者不能同时整，不遗漏
$\alpha_0=0$、但 $\alpha$ 的一次项非零的情形。
$p^2T$ 不影响 (15) 的第一修正，故不能改变这一结论。证毕。

特别，(18) 与 $\alpha=0$ 可以同时发生：
此时近支整、远支有单位简单极，
但 (12)–(17) 的二阶迹极部却为零。
坐标不整、单支临界值极、二支迹极是不同的实际条件，
不能相互替换。

## 5. 与原第二 forcing 的准确关系和范围

R597 的整个近支第二代表仍是同一 $R$ 给出的
$\Psi_0,\Psi_1,\Psi_2$，
并最终通过原
$\mathcal D_\psi^{\rm short}$ 的全来源像检验。
(16) 中的单独临界值项不能替换它。

例如在第一可见块中，完整普通 Taylor 的二次项可准确配方为
$$
\boxed{
\frac12B_+\xi^2+\xi R_{1,+}
=
\frac{B_+}{2}
 \left(\xi+\frac{R_{1,+}}{B_+}\right)^2
-\frac{R_{1,+}^2}{2B_+}.}
\tag{21}
$$
左边是原整普通表达。
右边两项可能各有 Laurent 极，但其极部必须严格相消。
若只保 (16) 的临界值二次项、
删掉 (21) 的另一个平方项，
就会制造一个原物理目标并不存在的极障碍。
第二、第三块还保 R597 的全部真实移位、
$Z^+$ 续段和两条十三行，不能由 (17) 代替。

同样，一般 $\bar A_+$ 只在近支有高零，
并不在整条临界曲线上恒为零。
$\pi_sA_+/p$ 是已付的有限整目标，
本篇没有把它约化成一个未付的全曲线有理函数。
(11)–(17) 之所以可作残数，是先对同一个整多项式基准和
同一个 $R/T$ 形成完整二次项，再取实际二根簇。

因此本篇支付的新增输入是：
同一原二阶项的整簇残数、全部二阶极的准确相消、
以及 (18) 下不可同时维持两支整坐标的强迫。
若继续把原 forcing 接到全局残数，
必须再支付其它临界簇、无穷远/全部角边界、
以及原可提升左行和完整实际修正像。
本篇没有把这些未付条件省略，也没有得出原 $d_2$ 非零。

## 依赖

- [R578](R578-complete-critical-boundary-elimination-and-fixed-polar-carry.md)：
  同一个修正的 Laurent 临界位移与二阶临界值。
- [R593](R593-original-critical-carry-completion-and-actual-second-normal-tail.md)、
  [R597](R597-original-nodal-critical-lift-and-complete-low-ell-second-class.md)：
  全低行、同一 $R$ 的完整 carry、真正第二 forcing 与像判据。
- [R603](R603-original-nodal-two-branch-gluing-and-actual-fifth-condition.md)：
  两条整非垂直支、原 $1,1,t,t^4$ gluing、
  全 $Q_n/Q_{\rm quad}$ 边界和另一临界值的准确范围。

本篇为全参数证明，无新增素数扫描；
原无穷素数与完整 $\Sha[p^\infty]$ 主目标仍未完成。
