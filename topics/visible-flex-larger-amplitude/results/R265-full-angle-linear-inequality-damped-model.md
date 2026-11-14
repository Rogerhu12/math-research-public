# R265 — 完整角域线性不等式的正阻尼模型与后验误差

日期：2026-11-14。状态：完整有限维条件定理及代数接口；没有新 QP、BVP、native tail 或候选场数值结果，没有选定优化参数。

## 265.1 问题与范围

[R262](R262-Hermite-RMS-domain-gradient-and-projected-descent.md) 已给出原 RMS Hermite 查询处域余量对全部物理状态、全局 scalar 参数和入口 core chart 的完整导数。实际 request22 的三个点切空间保护没有覆盖邻近角。本文给出有因的下一有限优化工具：保留所声明角网格的全部一阶域不等式，而不继续把每个新坏点逐一改成等式。

向量 $\beta$ 表示基点各固定查询的 **Frenet $\beta^2$ 正余量**，不是平方根。其第 $i$ 项为 $b_i(q)=\beta_{\rm Frenet}^2(q;s_i,\phi_i)$，假设
$$
\beta_i=b_i(q)>0.
\tag{1}
$$
位置、原物理角、网格和 Hermite 分数在当前模型中固定；不对 argmin、材料角反解或移动采样位置求导。

固定有限实矩阵和向量
$$
A\in\mathbb R^{m_R\times n_q},\quad b\in\mathbb R^{m_R},\quad
B\in\mathbb R^{r\times n_q},\quad r\ge1,\quad
\lambda>0,\quad 0<\theta<1.
$$
其中 $z=S\,\delta q$ 是原正对角坐标尺度 $S$ 下的方向，可取
$$
b=W_rR(q),\qquad A=W_rDR(q)S^{-1},\qquad
B=Db_{\rm domain}(q)S^{-1}.
\tag{2}
$$
$W_r,S$ 在本模型和 trial 比较中固定。若 warm 使用已完成零响应/J 的 affine DN，$R$ 就是该明确标识的 warm 残差，不能改称每个新 $H$ 的真实非线性 native map。

定义
$$
c=(1-\theta)\beta>0,\qquad s(z)=Bz+c,
$$
$$
f(z)=\frac12\|Az+b\|_2^2+\frac{\lambda^2}{2}\|z\|_2^2,
\quad H=A^TA+\lambda^2I,\quad g=A^Tb.
\tag{3}
$$
考虑
$$
\boxed{\min_{z\in K}f(z),\qquad K=\{z:Bz+c\ge0\}.}
\tag{4}
$$
不等式逐分量解释，等价于
$$
\beta+Bz\ge\theta\beta.
\tag{5}
$$
本文范数均为欧氏范数及其诱导矩阵范数，另记 $\|v\|_H^2=v^THv$。以下证明针对明确给定的有限实数模型；浮点报告的精度身份见第 265.9 节。

## 265.2 严格可行、存在唯一及正确 KKT 符号

**定理 265.1。** 问题 (4) 有唯一极小点 $z_*$，零方向严格可行。存在乘子 $\mu_*\in\mathbb R^r$，满足
$$
\boxed{
\begin{aligned}
Hz_*+g-B^T\mu_*&=0,\\
s_*:=Bz_*+c&\ge0,\\
\mu_*&\ge0,\\
\mu_{*,i}s_{*,i}&=0\quad(1\le i\le r).
\end{aligned}}
\tag{6}
$$
这些条件也是充分条件；不要求 $B$ 满秩或乘子唯一。

**证明。** $s(0)=c>0$，所以 $K$ 非空、闭、凸。由
$$
f(z)\ge\frac{\lambda^2}{2}\|z\|_2^2
$$
可取有界极小化序列，其收敛子列的极限属于 $K$ 并取得最小值。又有
$$
v^THv=\|Av\|_2^2+\lambda^2\|v\|_2^2
\ge\lambda^2\|v\|_2^2,
$$
故 $f$ 严格凸，极小点唯一。

令 $I$ 为 $z_*$ 的活跃行集合。对任意 $B_Iv\ge0$，充分小正步长使 $z_*+\varepsilon v$ 仍可行：活跃行不变负，有限个非活跃行保持原正余量。因此
$$
(Hz_*+g)^Tv\ge0\qquad\text{对所有 }B_Iv\ge0.
\tag{7}
$$
有限维锥对偶关系给出 $Hz_*+g=B_I^T\mu_I$、$\mu_I\ge0$。其余乘子置零，即得 (6)。

为使该步骤自含，锥对偶关系可如下证明。有限生成锥
$C=\{B_I^T\mu:\mu\ge0\}$ 是闭凸锥：消去线性相关生成元后，每个元素都可用某个线性无关子集非负表示；对收敛序列取固定子集的子列，该子集映射在其像上的逆有界，系数收敛后仍非负，故极限属于 $C$。若 $w\notin C$，取最近点 $p\in C$，令 $h=w-p$。投影变分关系给出 $h^Tp=0$ 及 $h^Tx\le0$ 对所有 $x\in C$。于是 $v=-h$ 满足 $B_Iv\ge0$，却有
$$
w^Tv=-(p+h)^Th=-\|h\|_2^2<0,
$$
与 (7) 矛盾。

反之，对满足 (6) 的 $(z,\mu)$ 及任意可行 $x$，
$$
\begin{aligned}
f(x)-f(z)
&=(Hz+g)^T(x-z)+\frac12\|x-z\|_H^2\\
&=\mu^T(s(x)-s(z))+\frac12\|x-z\|_H^2\\
&\ge\frac12\|x-z\|_H^2\ge0.
\end{aligned}
\tag{8}
$$
这里使用 $\mu\ge0,s(x)\ge0,\mu^Ts(z)=0$。因此 $z=z_*$。证毕。

对本文件的约束方向 $Bz+c\ge0$，Lagrangian 为
$$
\mathcal L(z,\mu)=f(z)-\mu^T(Bz+c),\qquad \mu\ge0.
\tag{9}
$$
若某求解接口使用反向不等式或另一符号的对偶变量，必须先转换，不能把变量名直接当作这里的 $\mu$。

## 265.3 非零最优方向的严格下降

**定理 265.2。** 满足 (6) 的最优方向有
$$
\boxed{
g^Tz_*=-\|Az_*\|_2^2-\lambda^2\|z_*\|_2^2-\mu_*^Tc.}
\tag{10}
$$
因此 $z_*\ne0$ 时 $g^Tz_*<0$。

**证明。** 将 stationarity 左乘 $z_*^T$，得
$$
g^Tz_*=-z_*^THz_*+\mu_*^TBz_*.
$$
由 $Bz_*=s_*-c$ 及互补性，$\mu_*^TBz_*=-\mu_*^Tc$。代入 $H$ 的定义即得 (10)。非零方向有 $\lambda^2\|z_*\|^2>0$，其余被减项非负。证毕。

活跃项的负常数加强下降，不会反向变成正项。若至少一个乘子严格为正，则 $\mu_*^Tc>0$；一个约束即使活跃，其乘子仍可能为零。

由 (10) 可得
$$
f(0)-f(z_*)=
\frac12\|Az_*\|_2^2+\frac{\lambda^2}{2}\|z_*\|_2^2+\mu_*^Tc,
\tag{11}
$$
以及对 $0<\alpha\le1,z_*\ne0$，
$$
\begin{aligned}
&\frac12\|b\|_2^2-\frac12\|b+\alpha Az_*\|_2^2\\
&\quad=\alpha\left[
(1-\alpha/2)\|Az_*\|_2^2+
\lambda^2\|z_*\|_2^2+\mu_*^Tc\right]>0.
\end{aligned}
\tag{12}
$$
式 (12) 是未正则化残差的**线性模型**下降，不是实际非线性 trial 已通过。

零方向最优当且仅当 $g=0$：若 $z_*=0$，严格 slack $s_*=c>0$ 强制 $\mu_*=0$，再由 stationarity 得 $g=0$；反向由强凸性成立。即使 $g=0$，原残差 $R$ 仍可能非零，不能称为 BVP 解。

若 $z$ 满足 (5)，则对 $0\le\alpha\le1$，
$$
\beta+\alpha Bz
=(1-\alpha)\beta+\alpha(\beta+Bz)
\ge[1-\alpha(1-\theta)]\beta\ge\theta\beta>0.
\tag{13}
$$
该式只保持选定有限行的线性预测。实际 Hermite 查询会非线性改变，仍须重算。

## 265.4 截停方向的恒等式及原回溯

对任意有限 $z,\mu$，定义完整 stationarity residual
$$
r=Hz+g-B^T\mu,\qquad s=Bz+c.
\tag{14}
$$
直接左乘 $z^T$，得到
$$
\boxed{
g^Tz=-\|Az\|_2^2-\lambda^2\|z\|_2^2-\mu^Tc
+\mu^Ts+z^Tr.}
\tag{15}
$$
所以精确解的下降式不能直接套在迭代截停值上。

对可行 $z,\mu\ge0$，一个充分条件是
$$
\mu^Ts+\|z\|_2\|r\|_2
<
\|Az\|_2^2+\lambda^2\|z\|_2^2+\mu^Tc
\quad\Longrightarrow\quad g^Tz<0.
\tag{16}
$$
但这不是新的科学门，也不是送入原回溯的必要条件。实际可以直接计算
$$
\mathrm{gdot}=b^TAz,\qquad
\mathrm{pred}(\alpha)=-\alpha\,\mathrm{gdot}
-\frac{\alpha^2}{2}\|Az\|_2^2.
\tag{17}
$$
真实有限且负的 gdot 才表示该模型的一阶下降。实际 trial 仍重算原节点 RHS、Hermite 中点与 RMS 查询、完整原边界、core density 和原 merit；不以 QP 内部停止码、线性可行、乘子估计或 (16) 代替。

原实际 merit 不加入阻尼罚项。若 (2) 的 $A$ 确为同一 $R$ 的导数，gdot 才是该实际固定权重 merit 的方向导数。有限浮点导数和 affine native 的使用范围仍须如实保留。

## 265.5 可行方向及非负乘子的后验

**定理 265.3。** 对任意 $z$ 和 $\mu\ge0$，有
$$
\boxed{
d(\mu):=\inf_w\mathcal L(w,\mu)
=f(z)-\mu^Ts-\frac12r^TH^{-1}r
\le f(z_*).}
\tag{18}
$$
若另有 $z\in K$，则
$$
0\le f(z)-f(z_*)
\le \mu^Ts+\frac12r^TH^{-1}r
\le E(z,\mu),
\tag{19}
$$
$$
\boxed{
E(z,\mu):=\mu^Ts+\frac{\|r\|_2^2}{2\lambda^2},\qquad
\|z-z_*\|_2\le\frac{\sqrt{2E(z,\mu)}}{\lambda}.}
\tag{20}
$$
还有
$$
\frac12\|z-z_*\|_H^2\le f(z)-f(z_*)\le E(z,\mu).
\tag{21}
$$

**证明。** Lagrangian 的 Hessian 是正定矩阵 $H$，在 $z$ 的梯度是 $r$。令 $w=z+h$，
$$
\mathcal L(z+h,\mu)
=\mathcal L(z,\mu)+r^Th+\tfrac12h^THh.
$$
唯一无约束极小点为 $h=-H^{-1}r$，代入即得 (18) 的等式。对任意可行 $x$，
$$
d(\mu)\le\mathcal L(x,\mu)\le f(x)
$$
因为 $\mu\ge0,s(x)\ge0$。这证明 weak-duality 下界。

若 $z$ 可行，$\mu^Ts\ge0$，从 $f(z)$ 中减去 (18) 得到 (19) 的第一上界。由 $H\succeq\lambda^2I$，有
$$
r^TH^{-1}r\le\|r\|_2^2/\lambda^2.
$$
最后，约束极小点满足
$(Hz_*+g)^T(z-z_*)\ge0$，二次展开给出
$$
f(z)-f(z_*)\ge\tfrac12\|z-z_*\|_H^2
\ge\tfrac{\lambda^2}{2}\|z-z_*\|_2^2.
$$
合并即得 (20)–(21)。证毕。

这一易算后验只需完整的 $Az,A^T(Az+b),Bz,B^T\mu$，不必形成 $H$ 或求逆。若可行方向实现模型下降
$$
\Delta=f(0)-f(z)>0,
$$
则
$$
\Delta\le f(0)-f(z_*)\le\Delta+E,\qquad
\frac{f(0)-f(z)}{f(0)-f(z_*)}\ge\frac{\Delta}{\Delta+E}.
\tag{22}
$$
这把内层误差与已获模型下降联系起来，不选定停止比例，也不变成原 BVP 验收。

若返回的乘子有负分量，可取 $\mu_+=\max(\mu,0)$ 构造合法 dual 下界，但必须重新计算
$$
r_+=Hz+g-B^T\mu_+
$$
及全部后验量，不能把旧 residual 冒作新证书。此处理仅作用于诊断乘子，不改变物理 $H$、状态、原方程或原门。

## 265.6 线性可行误差的显式径向修复

严格可行零方向使违反量可以显式处理，无须假定一个未知的 Hoffman 常数。

**定理 265.4。** 对任意有限 $z$，令
$$
v_i=\max(0,-s_i),\qquad
\rho=\max_i\frac{v_i}{c_i},\qquad
t=\frac1{1+\rho},\qquad \bar z=t z.
\tag{23}
$$
则 $0<t\le1,\bar z\in K$，且
$$
\|z-\bar z\|_2=\frac{\rho}{1+\rho}\|z\|_2.
\tag{24}
$$
若 $z$ 原已可行，则 $\rho=0,\bar z=z$。

**证明。** $s_i\ge-v_i\ge-\rho c_i$，故
$$
s_i(\bar z)=t(Bz)_i+c_i
=t s_i+(1-t)c_i
\ge[-t\rho+(1-t)]c_i=0.
$$
式 (24) 由 $\bar z=t z$ 得到。证毕。

这里 $\rho$ 是当前违反量确定的诊断数，不是预选 barrier、ADMM penalty 或新参数。对任意 $\mu\ge0$，在 $\bar z$ 上重新计算
$$
\bar s=B\bar z+c,\quad
\bar r=H\bar z+g-B^T\mu,\quad
\bar E=\mu^T\bar s+\|\bar r\|_2^2/(2\lambda^2).
$$
由定理 265.3 和三角不等式，
$$
f(\bar z)-f(z_*)\le\bar E,\qquad
\boxed{
\|z-z_*\|_2
\le\frac{\rho}{1+\rho}\|z\|_2+
\frac{\sqrt{2\bar E}}{\lambda}.}
\tag{25}
$$

不可行原 $z$ 的 $f(z)-f(z_*)$ 可能为负，不能称为可行目标 gap。若实施修复，实际 direction、gdot 和 nonlinear trial 必须以 $\bar z$ 为准。虽然
$g^T\bar z=t\,g^Tz$ 保留下降符号，原非线性域仍未由此获证。

数值计算中 $t$ 和 slack 也会舍入。浮点执行一次 (23) 不自动证明所有实数不等式，必须区分重新报告的原 slack 与严格有向包络。这里不把严格 QP 认证新增为原流程的科学门。

## 265.7 R262 完整链给出的 matrix-free $B$

节点编号为 $0,\ldots,N_s-1$。对每个固定查询组 $\ell$，设它位于单元 $(i,i+1)$、长度 $h_i$、固定分数 $t_\ell$，并包含所声明的全部原物理角。记 R262 的 Hermite 权重为 $h_{00},h_{10},h_{01},h_{11}$。

令 $Y_i$ 是节点物理系数，$p$ 为全部全局 scalar 参数，原 RHS 是 $f_i=f(s_i,Y_i,p)$。当前表示不显含独立 core 列，因此
$$
J_i=\partial_Y f_i,\qquad P_i=\partial_p f_i,\qquad
\delta f_i=J_i\delta Y_i+P_i\delta p.
\tag{26}
$$
零显式 core 列是当前源结构，不是未来表示的通用结论。

给定 $z$，先取 $\delta q=S^{-1}z$，再由原 exact chart 得到全部方向。入口使用
$$
\delta Y_0=E\delta c_{\rm free},\qquad
\delta r_j=\delta c_j,\quad\delta t_j=-2j\,\delta c_j,\quad
\delta z_j=0.
\tag{27}
$$
固定低 core、常值 core/control 行不变成可逐节点独立变化的新自由度。

查询方向为
$$
\begin{aligned}
\delta Y_\ell={}&
h_{00}\delta Y_i+h_i h_{10}\delta f_i\\
&+h_{01}\delta Y_{i+1}+h_i h_{11}\delta f_{i+1}.
\end{aligned}
\tag{28}
$$
对角行 $a$，以 R262 在真实查询值处的完整局部 covector 记
$$
\gamma_{\ell a}=\partial_Y b_{\ell a},\qquad
\pi_{\ell a}=\partial_p^{\rm direct}b_{\ell a}.
$$
则
$$
\boxed{
(Bz)_{\ell a}
=\gamma_{\ell a}^T\delta Y_\ell+\pi_{\ell a}^T\delta p.}
\tag{29}
$$
两端 $\delta f$ 和直接 scalar 链都不能省略。实际 scalar 字段记为 $a,\nu$，其中 $\nu$ 为源返回的 ap；不假定独立有限积分实现的 $a$ 对 $s$ 的导数恰为 $\nu$。其参数导数来自同源 control jets。

全角动作不需要一个巨大 dense $B$。先算查询方向，原 q.jet 分别作用于查询系数及方向，即给出所有角的
$d,e,\delta d,\delta e$。令 $Q=d\cdot d$、$v=d\times e$、$W=v\cdot v$，按角广播
$$
\begin{aligned}
(Bz)_{\ell a}={}&
-\frac{2\nu Q^3}{a^2W}\delta\nu
-\frac{3\nu^2Q^2}{a^2W}\delta Q
+\frac{2\nu^2Q^3}{a^3W}\delta a
+\frac{\nu^2Q^3}{a^2W^2}\delta W,\\
\delta Q={}&2d\cdot\delta d,\\
\delta W={}&2v\cdot(\delta d\times e+d\times\delta e).
\end{aligned}
\tag{30}
$$
原 q.jet 已含旋转框架的基向量角导数；固定物理角时不再增加旋转项。这里没有材料角反解或 argmin 导数。

给定方向的诊断可以使用完整 augmented 实方向的 complex-step 原 RHS，再对方向作同一 CubicHermiteSpline 查询。通用 $B/B^T$ 接口则必须固定同一组 $J_i,P_i,\gamma,\pi$ 或其一致算子表示，使前向和伴随属于同一有限线性模型。

## 265.8 matrix-free $B^T$ 与 Fourier 归一化

给定角行 dual 向量 $w$，每查询组先求
$$
u_\ell=\sum_a w_{\ell a}\gamma_{\ell a},\qquad
v_\ell=\sum_a w_{\ell a}\pi_{\ell a}.
\tag{31}
$$
将各节点物理 covector $r_i$ 和全局参数 covector $p^\dagger$ 初始化为零，然后每组累加
$$
\begin{aligned}
r_i&\mathrel{+}=h_{00}u_\ell+h_i h_{10}J_i^Tu_\ell,\\
r_{i+1}&\mathrel{+}=h_{01}u_\ell+h_i h_{11}J_{i+1}^Tu_\ell,\\
p^\dagger&\mathrel{+}=
h_i(h_{10}P_i^T+h_{11}P_{i+1}^T)u_\ell+v_\ell.
\end{aligned}
\tag{32}
$$
共享节点、重复查询和不同分数组都须相加，不能覆盖。入口拉回后，
$$
\boxed{
B^Tw=S^{-1}\operatorname{concat}
(r_1,\ldots,r_{N_s-1},E^Tr_0,p^\dagger).}
\tag{33}
$$

**命题 265.5。** (29) 和 (31)–(33) 满足欧氏伴随关系
$$
\langle Bz,w\rangle=\langle z,B^Tw\rangle.
\tag{34}
$$

**证明。** 将 (29) 乘各 $w_{\ell a}$ 并求和，按组得到
$\sum_\ell[u_\ell^T\delta Y_\ell+v_\ell^T\delta p]$。
代入 (28)、(26)，各节点和同一全局 $\delta p$ 的系数就是 (32)。
入口项 $r_0^TE\delta c_{\rm free}$ 给出 $E^Tr_0$。
最后用 $\delta q=S^{-1}z$、$S^{-T}=S^{-1}$，即得 (33)–(34)。证毕。

全局参数累计后只放一次；入口 core 行不能漏掉。若未来 RHS 显含 core，(26) 应加 $C_i\delta c$，转置中必须加入
$$
h_i(h_{10}C_i^T+h_{11}C_{i+1}^T)u_\ell
$$
到全局 core covector。

### 原局部 jet 的欧氏转置

为明确符号和尺度，原物理系数在旋转框架中写为
$$
R=r_0+\sum_{j=1}^Mr_j\cos(k_j\phi),\quad
T=\sum_{j=1}^Mt_j\sin(k_j\phi),\quad
Z=z_0+\sum_{j=1}^Mz_j\cos(k_j\phi),\quad k_j=2j.
$$
原导数为
$$
d=(R'-T,\ T'+R,\ Z'),\qquad
e=(R''-2T'-R,\ T''+2R'-T,\ Z'').
\tag{35}
$$
设各角已有作用于 $d,e$ 的加权 covector
$a_\ell=(a_x,a_y,a_z)$、$b_\ell=(b_x,b_y,b_z)$，例如 R262 的局部梯度乘该角的 $w_\ell$。物理系数 covector 为
$$
\begin{aligned}
(u)_{r_0}&=\sum_\ell(a_y-b_x),\\
(u)_{r_j}&=\sum_\ell[
-k_ja_x\sin(k_j\phi_\ell)+a_y\cos(k_j\phi_\ell)\\
&\hspace{26mm}-(k_j^2+1)b_x\cos(k_j\phi_\ell)
-2k_jb_y\sin(k_j\phi_\ell)],\\
(u)_{t_j}&=\sum_\ell[
-a_x\sin(k_j\phi_\ell)+k_ja_y\cos(k_j\phi_\ell)\\
&\hspace{26mm}-2k_jb_x\cos(k_j\phi_\ell)
-(k_j^2+1)b_y\sin(k_j\phi_\ell)],\\
(u)_{z_0}&=0,\\
(u)_{z_j}&=\sum_\ell[
-k_ja_z\sin(k_j\phi_\ell)-k_j^2b_z\cos(k_j\phi_\ell)].
\end{aligned}
\tag{36}
$$
**证明。** 对 (35) 分别取每个单位系数，代入
$\sum_\ell(a_\ell\cdot\delta d_\ell+b_\ell\cdot\delta e_\ell)$，收集该系数即得。特别地 $r_0$ 给出 $\delta d=(0,1,0)$、$\delta e=(-1,0,0)$；$z_0$ 的两个角导数均为零。证毕。

这里是角行空间的普通欧氏内积，**没有自动的 $1/N$**。原 q.project 带有 Fourier 投影归一化，不能未经换算就当作 q.jet 的欧氏转置。可以用同一固定 Fourier 表、绑定的 jet 线性映射或正确归一化的 FFT 伴随；(36) 规定符号与尺度，不授权另换未核等价的三角浮点求值。

### 坐标和行预条件

若内部取正对角 $C$、$z=C^{-1}v$，目标和约束须共同变为
$$
\frac12\|AC^{-1}v+b\|^2+
\frac{\lambda^2}{2}\|C^{-1}v\|^2,\qquad BC^{-1}v+c\ge0.
$$
恢复原 $z$ 后才计算 (14)–(25)，不把预条件 residual 当作原 KKT residual。

若采用正行缩放 $D>0$，须同时取
$$
\widetilde B=DB,\qquad\widetilde c=Dc,\qquad\mu=D\widetilde\mu.
\tag{37}
$$
则可行集、$B^T\mu=\widetilde B^T\widetilde\mu$、
$\mu^Ts=\widetilde\mu^T\widetilde s$ 及 $\mu^Tc$ 均不变。
只规范化 $B$ 而保留原 $c$ 会改变不等式模型。

## 265.9 后验的精度身份

应分别保留：

- 原 scaled 坐标中的 slack $Bz+c$ 和负部；
- 非负乘子、互补量及完整 $Hz+g-B^T\mu$；
- 若修复可行性，原方向、修复量、新 direction/slack/gdot 和新后验；
- 相对于已获模型下降的 $E$，以及原未正则化 merit 的实际下降；
- 原全部非线性域检查，不能由线性不等式替代。

仅有预条件法向 residual、不同缩放下的乘子或部分行 residual，不能代入 (20)。有关区别见 [R263](R263-projected-KKT-and-damped-model-error.md)。

严格实数后验要求 $z\in K,\mu\ge0$，且相关矩阵动作、内积、范数及可行性有可靠误差界。普通浮点重算是有限模型诊断；没有支付这些误差时，不称为 interval certificate。若要严格认证，可以使用已证的 $\mu^Ts$ 上界和 $\|r\|_2$ 上界代入同一公式。无须先新增严格 QP 认证，才允许一个实际下降方向进入原 nonlinear 检查。

## 265.10 全角探针的作用及完成边界

actual22 的后继探针固定同一 base20 warm 和已存完整方向，消费五个原左 RMS 查询与全部 $N=2048$ 原物理角，记录
$$
\beta_i,\quad v_i=(Bz)_i,\quad
\beta_i^{\rm actual}(\alpha),\quad
\mathcal E_i(\alpha)=\beta_i^{\rm actual}(\alpha)-\beta_i-\alpha v_i.
\tag{38}
$$
对 $v_i<0$，该方向的线性 first-exit 为 $\tau_i=-\beta_i/v_i$；对 $v_i\ge0$，线性模型没有正的首次零点。保持比例 $\theta$ 的同一射线预测界相应是 $(1-\theta)\tau_i$。

比较最小 $\tau_i$、真实首个失效步长、角位置和 $\mathcal E_i$，才能区分遗漏的全角一阶限制与较大步长的非线性余项。若线性预测仍正但实际已负，不能宣称本一阶模型单独足够。

五处乘 2048 是声明的有限行集合，不自动覆盖其它节点、中点、另一组 RMS 查询或连续角。扩展行集合时可以复用这些定理，但须绑定相应实际对象并重新得到完整导数。

本文件不选择 $\theta$、内层算法、penalty 或新阻尼值；数值策略等待真实全角回执。线性域余量恢复没有变成新的 BVP 方程。实际收敛、同 $g$ 精化、闭曲面、全 $t$、operator、曲率、reach 和 held amplitude 仍须由原课题要求及同场真实计算完成。
