# R154：联合超三次模式的全部非零点态多项式及任意指数权

日期：2026-11-12。作者：l2_moments。
状态：完整证明，根代理、literature 与 critical_kernel 已全文独立审读通过。
本正文在执行器失效后从完整上下文重建并逐式复核。

本稿使用 R151 的四次型解析逼近代数 $\mathcal G$，取消快模式中的全部点态多项式共振条件。
模式数任意有限，允许代数依赖；唯一非零假设直接施加于实际点态向量。
指数方向可为任意复 $\ell^2$ 第一 chaos，不受快尾假设限制。

## 1. 主定理

给定有限个模式
$$
u_\nu=a_{\nu,*}+\sum_{j\ge0}a_{\nu j}\chi_j,\qquad 1\le\nu\le d,
$$
定义联合幅度
$$
s_j=\left(\sum_{\nu=1}^d|a_{\nu j}|^2\right)^{1/2}.
\tag{1.1}
$$
忽略零项，将其非零模长作非增重排，记为 $s_\ell^*$。
假设有限支持，或
$$
\boxed{\frac{-\log s_\ell^*}{\ell^3}\longrightarrow+\infty.}
\tag{1.2}
$$
这尤其保证 $\sum_js_j^\varepsilon<\infty$ 对每个 $\varepsilon>0$ 成立；
全部 $u_\nu$ 都是连续有界函数。

另取任意
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
\tag{1.3}
$$
不要求 $b$ 满足 (1.2)，允许它与所有快模式完全重叠。

**定理1.1。** 对任意标量多项式 $F\in\mathbb C[z_1,\ldots,z_d]$，若实际点态函数
$$
f=F(u_1,\ldots,u_d)
$$
不是零向量，则
$$
\boxed{F(u_1,\ldots,u_d)e^w\text{ 对实际 }A\text{ 循环}.}
\tag{1.4}
$$
没有相位、首位顺序、矩形次数、简单根或平移互素假设。

若 $f$ 不是本质常数，则对全部 $\lambda\in\mathbb C$，
$$
\boxed{(F(u_1,\ldots,u_d)-\lambda)e^w\text{ 循环}.}
\tag{1.5}
$$
若 $f$ 是常数，则精确排除使括号等于零的那个参数。

更强地，证明构造一个实际有界 $P_F^w\in\mathcal G$ 与循环向量 $\xi_w$，使
$$
F(u_1,\ldots,u_d)e^w=B_wP_F^w\xi_w,
\tag{1.6}
$$
其中 $B_w$ 为有界交换单位。
非零 $P_F^w$ 在每个闭 $A$ 不变限制及全部有限放大上都有稠密像。
当 $w=0$ 时，$P_F^0$ 就是点态符号 $f$ 的实际有界乘子，且属于 $\mathcal G$。

## 2. 四次型逼近接口及带因子尾引理

R151 定义 $E\in\mathcal G$：存在真正标量解析芽 $g_n$，使
$$
\|E-g_n(A)\|\to0,\qquad\tau_4(E-g_n(A))\to\infty.
$$
已证 $\mathcal G$ 含所有真解析演算，且对有限加法、乘法、
非零字符单位的逆及 dyadic gauge 稳定。
每个非零 $E\in\mathcal G$ 都单射，且
$$
\overline{EM}=M
$$
对每个闭 $A$ 不变 $M$ 成立；所有有限放大版本亦成立。
本稿仅使用上述有限代数稳定性，不要求 $\mathcal G$ 对任意算子范数极限封闭。

**引理2.1。** 设每个 $U_j$ 是一个真正解析芽在 $A$ 上的值，且
$\sup_j\|U_j\|<\infty$。
若非零 $c_j$ 的降序模长满足超三次条件 (1.2)，则
$$
E=\sum_jc_jN_jU_j\in\mathcal G,\qquad N_j=A^{2^j}/W_{2^j}.
\tag{2.1}
$$
允许 $U_j=0$，也不要求任何首项的字符非零。

**证明。** 取统一常数 $C\ge\sup\|U_j\|$，
将 $C$ 吸收到系数后可设 $\|U_j\|\le1$。
级数绝对范数收敛。每个有限头是真解析芽的有限和。

R115 §2 的真实带因子占据估计只用 $\|U_j\|\le1$，
不使用其单位性或首字符。
将一般归一化指数取为 $2^j$、其余系数为零，得到：
对任意固定 $\gamma>0$ 和 $0<\varepsilon<1$，
去掉有限个最大系数并取实际归一化指数起点 $K$ 足够大后，
$$
\left\|\left(\sum_{2^j\ge K}c_jN_jU_j\right)^n\right\|
\le
\left(\sum_{2^j\ge K}|c_j|^\varepsilon\right)^n
\exp[-b_Kn^4],
\tag{2.2}
$$
其中
$$
A_K=\frac14\left(\sum_{n\ge K}n^{-4/3}\right)^{-3}\to\infty,
\quad D=\frac{(1-\varepsilon)\gamma}{4},
\quad b_K=(A_K^{-1/3}+D^{-1/3})^{-3}\to D.
$$
超三次重排允许 $\gamma$ 任意大。因此尾的 $\tau_4$ 趋于无穷，
范数尾也趋零，证明 (2.1)。

这里没有把重排速度误当作原坐标速度。
对每个固定 $\gamma$，需要移除的最大系数仅有限个；
它们的实际坐标都能包含于某个有限头，故足够大的实际 $K$ 确能移除它们。
R115 的任意有界因子只用于尾估计；
有限头的真正解析性由本引理单独假设并逐项保留。证毕。

### 2.1 快模式本身的有界乘子属于 $\mathcal G$

由 (1.2)，每个 $a_{\nu\cdot}\in\ell^1$。其真实有界乘子为
$$
X_\nu=a_{\nu,*}I+\sum_ja_{\nu j}V_j
=\beta_\nu I-2\sum_ja_{\nu j}N_j(I+N_j)^{-1},
\quad
\beta_\nu=a_{\nu,*}+\sum_ja_{\nu j}.
\tag{2.3}
$$
$\|(I+N_j)^{-1}\|<3$，每个逆都是真解析芽在 $A$ 上的值。
又 $|a_{\nu j}|\le s_j$，降序后仍受 $s_\ell^*$ 控制。
引理2.1与常数稳定性给
$$
\boxed{X_\nu\in\mathcal G\quad(1\le\nu\le d).}
\tag{2.4}
$$

## 3. 局部对数、真实 $N_j$ 因子及统一商

沿用
$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z),\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
\tag{3.1}
$$
R145 给 $H(z,V_j)$ 的算子范数整性；其字符恒为1，
所以它总是 $\mathcal A$ 的单位。
记
$$
L_j(z)=\log H(z,V_j),
\tag{3.2}
$$
其中对谱点1取满足 $\log1=0$ 的全纯演算。
在任意固定 $z$ 附近，可取谱点1的一条小轮廓来定义该对数；
因谱始终为 $\{1\}$，这个局部分支随 $z$ 范数解析。
等价地，对拟幂零 $H(z,V_j)-I$ 取规范的零字符对数。
只需各个 $b_j$ 邻域的分支，不要求一个覆盖所有标量变量的统一圆盘。

**引理3.1。** 对每个固定整数 $r\ge1$，存在真正解析芽乘子 $U_{rj}$，使
$$
\boxed{L_j^{(r)}(b_j)=N_jU_{rj},\qquad
\sup_j\|U_{rj}\|<\infty.}
\tag{3.3}
$$
常数允许依赖固定 $r$ 与指数系数列 $b$，不依赖位 $j$。

### 3.1 高位统一计算

对充分大的 $j$，$|b_j|$ 小且 $\eta_j$ 小。
引入复参数 $\rho$，令
$$
V_j(\rho)=(I-\rho N_j)(I+\rho N_j)^{-1},\qquad|\rho|\le2.
$$
真实关系 $N_j^2=\eta_jN_{j+1}$ 给
$$
(I+\rho N_j)^{-1}
=(I-\rho N_j)(I-\rho^2N_j^2)^{-1}.
$$
选高位使 $4\eta_j\le1/2$，则
$$
\|(I+\rho N_j)^{-1}\|\le6,\qquad
\|V_j(\rho)\|\le18.
\tag{3.4}
$$
取一个固定小圆盘 $|z|\le4r_0$，
使对全部这些 $j,\rho$ 有
$$
\|(\cosh z-1)I+V_j(\rho)\sinh z\|<1/2.
$$
于是可在这个圆盘直接定义
$$
L(z,\rho)=-zV_j(\rho)
+\log(\cosh z\,I+V_j(\rho)\sinh z),
\tag{3.5}
$$
对数使用近恒等的范数级数。
$L(z,0)=0$，并且各因子交换，故
$$
\partial_\rho L(z,\rho)=N_jM_j(z,\rho),
\tag{3.6}
$$
其中
$$
M_j(z,\rho)
=-2(I+\rho N_j)^{-2}
\left[-zI+\sinh z\,
(\cosh z\,I+V_j(\rho)\sinh z)^{-1}\right].
\tag{3.7}
$$
(3.4) 和小圆盘逆界给 $M_j$ 在较小闭圆盘上的统一范数界。

再取高位使 $|b_j|\le r_0$。
在 $b_j$ 周围作半径 $r_0$ 的 Cauchy 估计，
对每个固定 $r$ 得到
$$
\sup_{j\text{ 高位},\,0\le\rho\le1}
\|\partial_z^rM_j(b_j,\rho)\|<\infty.
$$
对 $\rho$ 从0到1积分并对 $z$ 求导，得到
$$
L_j^{(r)}(b_j)=N_j
\int_0^1\partial_z^rM_j(b_j,\rho)\,d\rho.
\tag{3.8}
$$
这已经给出真实有界商和高位的统一范数，不是形式除法。

### 3.2 商的真正解析性及有限低位

固定任意 $j$，把 $N_j$ 暂换成标量变量 $n$，取
$$
V(n)=\frac{1-n}{1+n}.
$$
在 $(z,n)=(b_j,0)$ 附近，
$$
e^{-zV(n)}(\cosh z+V(n)\sinh z)
$$
在 $n=0$ 恒等于1，所以存在满足该处 $\log1=0$ 的联合解析对数。
其第 $r$ 个 $z$ 导数在 $n=0$ 为零，故可在真正解析芽环中除以 $n$。
将此商求值于 $N_j$，得到一个真正解析芽乘子 $\widetilde U_{rj}$，并有
$$
N_j\widetilde U_{rj}=L_j^{(r)}(b_j).
$$
在高位，它与 (3.8) 的有界积分商相同，因为 $N_j$ 单射。
所以高位的统一界确实适用于这个真解析商。
剩余有限低位逐个取范数最大值，证明 (3.3)。

这里从未因“字符为零”就直接断言可以有界除以 $N_j$；
真实有界商来自 (3.6)—(3.8)，真正解析性另由标量局部芽和单射性确认。

## 4. 每个倾斜 Bell 系数属于 $\mathcal G$

置
$$
\lambda_j(t)=\sum_{\nu=1}^dt_\nu a_{\nu j},\qquad
B_w=\prod_jH(b_j,V_j),
$$
以及
$$
\widetilde B(t)
=\prod_jH(b_j+\lambda_j(t),V_j)H(b_j,V_j)^{-1}.
\tag{4.1}
$$
R145 给 $B_w$ 的范数收敛、单位性与字符1。
在零点的固定小参数邻域，(4.1) 局部一致绝对范数收敛：
高位的局部导数和逆均一致有界，
每个比值减 $I$ 的范数由常数乘 $s_j\|t\|$ 控制；
$\sum_js_j<\infty$，有限低位另选共同小邻域即可。

因此可以在该邻域取规范局部对数
$$
\log\widetilde B(t)
=\sum_j[L_j(b_j+\lambda_j(t))-L_j(b_j)]
\tag{4.2}
$$
并逐项求任意固定多重导数。
设 $\alpha\in\mathbb N^d\setminus\{0\}$、$r=|\alpha|$，
记 $a_j^\alpha=\prod_\nu a_{\nu j}^{\alpha_\nu}$。则
$$
\mathcal L_\alpha
:=\partial_t^\alpha\log\widetilde B(0)
=\sum_ja_j^\alpha L_j^{(r)}(b_j)
=\sum_ja_j^\alpha N_jU_{rj}.
\tag{4.3}
$$
因为 $|a_j^\alpha|\le s_j^r$，
这些系数的降序模长仍满足 (1.2)。
引理3.1和引理2.1于是给
$$
\boxed{\mathcal L_\alpha\in\mathcal G\qquad(\alpha\ne0).}
\tag{4.4}
$$

令
$$
C_\alpha=\partial_t^\alpha\widetilde B(0),\qquad C_0=I.
$$
对每个固定 $\alpha$，指数的 Bell/Leibniz 公式只涉及有限多个
$\mathcal L_\beta$、$\beta\le\alpha$ 的有限多项式组合。
所以
$$
\boxed{C_\alpha\in\mathcal G\quad(\alpha\in\mathbb N^d).}
\tag{4.5}
$$
$\chi(\widetilde B(t))=1$，故 $\chi(C_\alpha)=0$ 对 $\alpha\ne0$。
这里没有对无穷 Bell 展开使用 $\mathcal G$ 的未证范数闭性。

## 5. 真正生成恒等式、非零判据与循环性

R16/R147 已证明
$$
e^w\in H,\qquad e^w\text{ 对 }A\text{ 循环}.
$$
令
$$
\xi_w=B_w^{-1}e^w.
$$
$B_w^{-1}$ 是有界交换单位，故 $\xi_w$ 也循环。

所有快模式 $u_\nu$ 有界，所有实际 $X_\nu$ 有界。
有限位的真实生成恒等式，随后取范数与 $H$ 极限，给
$$
\boxed{
e^{\sum_\nu t_\nu u_\nu+w}
=B_w\widetilde B(t)
e^{\sum_\nu t_\nu X_\nu}\xi_w.
}
\tag{5.1}
$$
准确的极限理由是：快模式截断在函数一致范数和乘子算子范数中收敛；
$e^{w_N}\to e^w$ 于 $H$；
联合 Bell 及其单位逆局部一致范数收敛。
所以这里没有把 $X_\nu$ 当作点态乘法，也没有使用未经证明的高次无界域。

对标量多项式 $F$，对 (5.1) 施加 $F(\partial_t)$ 并在零点取值，
得到有限和
$$
\boxed{
F(u_1,\ldots,u_d)e^w
=B_wP_F^w\xi_w,
\quad
P_F^w=\sum_{\alpha\ge0}
\frac{C_\alpha}{\alpha!}
(\partial^\alpha F)(X_1,\ldots,X_d).
}
\tag{5.2}
$$
由于 $F$ 为多项式，和只有有限项。
由 (2.4)、(4.5) 和 $\mathcal G$ 的有限代数稳定性，
$$
\boxed{P_F^w\in\mathcal G.}
\tag{5.3}
$$

$e^w$ 几乎处处非零，故 $F(u)\ne0$ 当且仅当 $F(u)e^w\ne0$。
若后者非零，(5.2) 给 $P_F^w\ne0$。
反向若 $F(u)=0$，则 $P_F^w\xi_w=0$；
$\xi_w$ 循环且 $P_F^w$ 为有界交换子，故 $P_F^w=0$。
因此实际非零条件与实际乘子非零完全对应，无需模式代数独立性。

非零 $P_F^w\in\mathcal G$ 有稠密像，故
$$
\overline{\mathbb C[A]P_F^w\xi_w}
=\overline{P_F^wH}=H.
$$
再乘有界交换单位 $B_w$，得 (1.4)。
将 $F$ 换为 $F-\lambda$ 即得 (1.5)。
当 $w=0$ 时 $B_w=I$、$\xi_w=1$，所以 $P_F^01=F(u)$；
有界乘子的循环向量唯一性说明它就是实际符号乘子。

## 6. 共振平方的一个具体新例子

取
$$
a_0=1,\qquad
a_j=e^{-(j+1)^4}\ (j\ge2),\qquad
a_1=-\sum_{j\ge2}a_j,\qquad
u=\sum_{j\ge0}a_j\chi_j.
\tag{6.1}
$$
系数的非零降序重排满足 (1.2)，且 $u(0)=1$。
于是 $u^2-1$ 的字符锚为零；
其第0行的一阶系数和也因 $\sum_{j>0}a_j=0$ 而消失。
原平移互素平方判据在 $\lambda=a_0^2=1$ 处正好共振。

但 $u^2-1$ 不是零：其 $\chi_0\chi_2$ 系数为
$$
2a_0a_2=2e^{-81}\ne0.
$$
本定理因此给
$$
\boxed{(u^2-1)e^w\text{ 对每个复 }\ell^2\text{ 第一阶 }w\text{ 都循环}.}
\tag{6.2}
$$
第0行具有无限支撑；这不是一个有限柱或局部有限行的重复例子。

## 7. 范围与仍未解决的问题

1. 快条件只施加于有限模式的联合系数幅度，允许任意稀疏坐标排列。
2. 指数方向 $w$ 只要求 $\ell^2$，既可无界，也可与快方向完全重叠。
3. 每个固定 Bell 系数进入 $\mathcal G$ 的证明使用真实 $N_j$ 商及带因子尾估计；
   没有把 $\mathcal G$ 当作一个无条件范数闭代数。
4. 不要求非零标量多项式一定产生非零向量；实际点态非零由 (5.2) 精确识别。
5. 任意慢 $\ell^1$ 或一般复杂 $\ell^2$ 模式的共振平方仍不由本稿处理；
   完整 Hilbert 不变子空间问题仍开放。
