# R236 附录：非可和主行二分与全阶 Sylvester 联合逆

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。
**状态：已证明。** 以下给出完整实际证明与范围。
主结论覆盖任意非可和平方可和主行；更一般地，只须主幅度具有指数下界子序列。
全部复相位、物理排列、有限低头例外、固定共振次数和标量位移均允许。
一般 Hilbert 不变子空间问题仍未完成。

## 1. 准确范围与全阶目标

设
$$
a,b\in\ell^2,\qquad a_*,b_*\in\mathbb C,
$$
且 $a$ 有无穷多个非零项。
令 $\rho_1\ge\rho_2\ge\cdots>0$ 为其非零幅度递减重排；
排序保留各项的原物理位标签。

取任意实数 $\kappa>2$。
假设存在常数 $c_-,c_+>0$ 及有限物理阈值 $j_0$，
使对每个 $j\ge j_0$，
$$
\boxed{c_-|a_j|^\kappa\le|c_j|\le c_+|a_j|^\kappa.}
\tag{1.1}
$$
这包括主行零位：若 $j\ge j_0$ 且 $a_j=0$，则必须有 $c_j=0$。
有限集合 $j<j_0$ 上的 $c_j$ 可以任意，
包括缺失所有最早非零主位的辅助项。
由 $\kappa>2$ 和 $a\in\ell^2$，自动有 $c\in\ell^1$。

置
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j,\qquad
v_c=\sum_jc_j(\chi_j-1).
$$
沿用 R270C 的准确共振族
$$
F_k=k![t^k]\exp\left(
tu+\sum_{n=2}^k\frac{2^{n-1}}n t^n
\sum_j a_j^n(\chi_j-1)
\right),\qquad F_0=1,\quad F_1=u.
\tag{1.2}
$$
对固定非恒定标量多项式
$$
q(z)=\sum_{k=0}^p q_kz^k,\qquad p\ge1,\quad q_p\ne0,
$$
记
$$
F_q=\sum_{k=0}^p q_kF_k.
$$

**定理 1（指数下界子序列）。**
若
$$
\boxed{\liminf_{n\to\infty}
\frac{\log^+\rho_n^{-1}}n<\infty,}
\tag{1.3}
$$
则对每个固定非恒定 $q$、每个 $\lambda\in\mathbb C$，
$$
\boxed{[F_q+v_c-\lambda]e^w
\text{ 非零且对原实际 }A\text{ 循环}.}
\tag{1.4}
$$

**推论 2（全部非可和主行）。**
若
$$
a\in\ell^2\setminus\ell^1,
$$
则 (1.3) 自动成立，故全部 (1.4) 成立。
这里无需任何点态两侧幂律、正则变化或全局排序对数下界。

更强地，只要某个固定 $s>1/2$、$C>0$ 满足
$$
\rho_n\ge Cn^{-s}
\tag{1.5}
$$
对无穷多个 $n$ 成立，证明中的第二分支有更低的
$O(N\log N)$ 联合预解成本。
这也包括部分可和而极不规则的主行。

本文的结论是共振族 $F_q$，不是把全部 $F_k$ 换成普通点态 $u^k$。
主行零位上任意无限可和辅助不受 (1.1) 控制时，
下文第二分支的尾估计不成立；这里不作该外推。

## 2. 具有可控前幅度的首次降幅

固定
$$
0<\delta\le
\min\left\{\frac12,
\left(\frac{c_-}{2c_+}\right)^{1/(\kappa-1)}\right\},
$$
取整数
$$
L>\delta^{-2},\qquad K=3L.
\tag{2.1}
$$

**引理 3。**
在 (1.3) 下，存在常数 $C_0$ 及无穷多个整数 $N$，使
$$
\boxed{
\rho_{KN}\le\delta\rho_{3N},
\qquad
\log^+\rho_{3N}^{-1}\le C_0N.
}
\tag{2.2}
$$
若改用 (1.5)，则可令同一无穷子序列满足
$$
\rho_{3N}\ge C_0'(3N)^{-s}
\tag{2.3}
$$
对某个 $C_0'>0$ 成立。

证明。先由 (1.3) 取得无穷多个整数种子 $N_0$，使
$$
\log^+\rho_{3N_0}^{-1}\le C N_0.
\tag{2.4}
$$
从原排序位置 $n$ 取 $N_0=\lfloor n/3\rfloor$ 即可；
单调性及固定常数吸收了取整。

沿 $N_j=L^jN_0$，考察首次满足
$$
\rho_{KN_j}\le\delta\rho_{3N_j}
$$
的位置 $j$。
它必有限：否则
$$
N_j\rho_{3N_j}^2
\ge N_0\rho_{3N_0}^2(L\delta^2)^j\longrightarrow\infty,
$$
与平方可和递减行的 $n\rho_n^2\to0$ 矛盾。

在首次降幅之前，每一步有
$$
\rho_{3N_{j+1}}>\delta\rho_{3N_j}.
$$
故在该首次位置
$$
\log^+\rho_{3N_j}^{-1}
\le C N_0+j|\log\delta|
\le C_0N_j.
\tag{2.5}
$$
这里 $C_0$ 与种子和首次位置均无关，因为 $L\ge2$。
所得 $N_j\ge N_0$，所以随种子无界而得到无穷多个 $N$。

若种子改为 (1.5)，取整后有
$\rho_{3N_0}\ge C_0'(3N_0)^{-s}$。
由于
$$
\delta L^s>1
$$
由 $L\delta^2>1$ 及 $s>1/2$ 推出，
此前每步的因子 $\delta$ 均保留该多项式下界：
$$
\rho_{3N_j}\ge
C_0'\delta^j(3N_0)^{-s}
\ge C_0'(3N_j)^{-s}.
$$
这证明 (2.3)。证毕。

若 $a\notin\ell^1$，则对任意固定 $s>1$，
(1.5) 必有无穷多个解。
否则最终 $\rho_n<Cn^{-s}$，将迫 $\rho\in\ell^1$。
所以推论 2 是该引理的直接子类。

## 3. 第一分支：第二幅度带可用

在引理 3 的无穷子序列上置
$$
M_N=(K+2)N.
$$
先假设有无穷多个 $N$ 满足
$$
\boxed{\rho_{M_N}\ge e^{-N^{3/2}}.}
\tag{3.1}
$$

取排序带
$$
(N,3N],\qquad(KN,(K+2)N].
$$
每带有 $2N$ 项；各删去原物理位小于 $N$ 的项后，各取 $N$ 项。
充分大时这同时删除全部有限例外。
得到不交物理池 $I_N,J_N$，满足
$$
\min(I_N\cup J_N)\ge N,\qquad
\max_{I_N\cup J_N}|a_j|\le\|a\|_2N^{-1/2}.
\tag{3.2}
$$
对任意 $j\in I_N,k\in J_N$，由 (2.1)–(2.2) 和 (1.1)，
$$
\left|\frac{c_k}{a_k}\right|
\le\frac12\left|\frac{c_j}{a_j}\right|.
$$
因此无论相位如何，
$$
\begin{aligned}
|a_kc_j-a_jc_k|
&\ge\frac{c_-}{2}|a_j|^\kappa|a_k|\\
&\ge\frac{c_-}{2}\rho_{3N}^{\kappa}\rho_{M_N}.
\end{aligned}
\tag{3.3}
$$
结合 (2.2)、(3.1)，有
$$
1+\log^+
\left(\min_{I_N\times J_N}|a_kc_j-a_jc_k|\right)^{-1}
\le N^{3/2}+\kappa C_0N+C.
\tag{3.4}
$$
(3.2)–(3.4) 正是已证全阶二位 Bézout 准则。
它立即给全部 (1.4)。

故以下只需处理另一条无穷子序列：
$$
\boxed{\rho_{M_N}<e^{-N^{3/2}}.}
\tag{3.5}
$$
不要求 (3.1) 或 (3.5) 在全部自然数上成立。
两分支至少有一支在引理 3 的子序列中无穷出现，已足完成证明。

## 4. 第二分支的真实辅助尾

令 $H_N$ 为以下真实物理位的并：
排序中前 $M_N$ 个非零主幅度所在的位，以及全部 $j<j_0$。
因此
$$
|H_N|\le (K+2)N+j_0=O(N).
\tag{4.1}
$$
有限例外全部放入头部，而非以比较式估计它们。
由于主行零位上的辅助最终为零，头部之外只剩比较受控的非零主位。

令
$$
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j),\qquad
Y=\sum_jc_j(R_j-I).
$$
取固定
$$
L_b^+=\max(1,\sup_j|t_j|),\qquad
W(z)=\frac{2L_b^+z}{1-L_b^+z}.
$$
这是原实际算子的真实有理演算，且
$$
C_W:=\sup_j\|W(N_j)\|<\infty.
$$
原函数正锥下有
$$
|(R_j-I)f|\le W(N_j)|f|.
$$
故辅助尾的真实正锥主控满足
$$
\begin{aligned}
\left\|\sum_{j\notin H_N}|c_j|W(N_j)\right\|
&\le C_Wc_+\sum_{n>M_N}\rho_n^\kappa\\
&\le C_Wc_+\rho_{M_N}^{\kappa-2}\sum_{n>M_N}\rho_n^2\\
&\le C\|a\|_2^2e^{-(\kappa-2)N^{3/2}}.
\end{aligned}
\tag{4.2}
$$
此处恰用 $\kappa>2$。
有限头任意大或位于任意高物理位置，都不改变 (4.2)。

### 4.1 任意物理头的全方向实际 Laplace 预算

记
$$
Y_H=\sum_{j\in H}c_j(R_j-I).
$$
此前已证的实际有限头估计为
$$
\|e^{sY_H}\|
\le C\exp\!\left(C[\log(2+|s|)]^{4/3}\right)
\prod_{j\in H}(1+C_1|s||c_j|).
\tag{4.3}
$$
常数与 $|H|$ 及 $\max H$ 均无关。

为说明其真实来源，(4.3) 先用非负函数锥与 $W(N_j)$ 主控复指数。
实际 carry
$$
N_j^2=\eta_jN_{j+1},\qquad
\eta_j=\frac{d_{j+1}}{d_j^2}
=\exp(-1400\,16^j+630\,8^j-300\,2^j)
\le e^{-385\,16^j}
$$
给单个高位因子的偶奇幂估计
$$
\|e^{s|c_j|W(N_j)}\|
\le(1+C_1s|c_j|)\exp(C_2s|c_j|\sqrt{\eta_j})
\quad(s\ge0).
$$
按 $\log(2+s)$ 选择一个真正物理低头阈值，
使其以上 carry 总成本有界；
其以下有限项实际写成 $AU$，再用原 $A$ 的四次幂衰减。
这样得到 (4.3) 的对数 $4/3$ 成本，
而不使常数依赖任意排序头的最大物理位。
385 只是粗上界，不是实际 $\eta_j$ 的等式。

若 $0<R\le1$ 且头外正锥主控范数不超过 $R/4$，
那么对每个 $|z|=R$，真正的 Bochner 积分
$$
\boxed{
z(z-Y)^{-1}
=\int_0^\infty e^{-t}e^{tY/z}\,dt
}
\tag{4.4}
$$
绝对算子范数收敛。
头尾交换，尾指数贡献至多 $e^{t/4}$；
(4.3) 的有限多项式增长及对数幂增长均可被余下指数衰减积分。

若 $h=|H|$、$\ell_R=1+\log R^{-1}$，直接估计该积分给
$$
\boxed{
\Gamma_Y(R):=
\sup_{|z|=R}\log^+\|z(z-Y)^{-1}\|
\le C\bigl[
1+h\log(h+1)+h\ell_R+\ell_R^{4/3}
\bigr].
}
\tag{4.5}
$$
例如把
$\log(2+t/R)\le \ell_R+\log(2+t)+C$
代入 (4.3)，吸收后一个对数幂于 $e^{t/4}$，
再用 $(1+Ct/R)^h$ 的 Gamma 积分即可。
这不是 Hilbert 自伴正算子的估计；使用的是原函数锥及真实复指数。

对任意固定 $D>0$ 与 $\epsilon>0$，取
$$
R_N=\epsilon\rho_N^D.
\tag{4.6}
$$
由 $\rho_N\ge\rho_{3N}$ 和 (2.2)，
$$
\ell_{R_N}=O(N).
$$
(4.2) 最终小于 $R_N/4$，因为前者为
$\exp[-(\kappa-2)N^{3/2}]$，后者至少为 $\exp(-C_DN)$。
结合 (4.1)、(4.5)，得到
$$
\boxed{\Gamma_Y(R_N)=O(N^2).}
\tag{4.7}
$$
若有更强的多项式下界 (2.3)，则
$$
\ell_{R_N}=O(\log N),\qquad
\boxed{\Gamma_Y(R_N)=O(N\log N).}
\tag{4.8}
$$

## 5. 实际全阶自然算子与未知核

沿用
$$
X=X_b,\qquad
G_n=(-1)^{n-1}(n-1)!\sum_j a_j^n(R_j-I)^n
\quad(2\le n\le p).
\tag{5.1}
$$
R270C 已证明每个 $G_n$ 真正属于 $\mathcal G$，且字符为零。
不将慢辅助 $Y$ 归入 $\mathcal G$。

对形式变量
$$
\mathbf z=(z_2,\ldots,z_p,y)\in\mathbb C^p
$$
定义有限多项式
$$
P_q(t;\mathbf z)
=\exp\left(\sum_{n=2}^p\frac{z_n}{n!}\partial_t^n\right)q(t).
\tag{5.2}
$$
它不依赖最后的变量 $y$。
当 $p=1$ 时，前一串变量及指数和均为空。
在实际系数处代入后，
$$
P_q(X;G_2,\ldots,G_p)
e^w=F_qe^w.
$$

取
$$
T_\lambda=P_q(X;G_2,\ldots,G_p)+Y-\lambda I,
\qquad
\operatorname{Dom}T_\lambda=\operatorname{Dom}X^p.
\tag{5.3}
$$
R176 给准确自然域上的闭性、完整 $C$ 自伴性与
$\xi=e^w$ 的真实循环图核心。
反设
$$
M=\ker T_\lambda\ne0.
$$
同一最大图结论给
$$
\boxed{
M\subset\mathcal D_\infty(X),\qquad
X_M=X|_M\in B(M).
}
\tag{5.4}
$$
所有 $\mathcal A$ 系数保持 $M$ 和全部自然幂域。

一般 $q,\lambda$ 下不要求 $X_M$ 拟幂零；
以下真实代数恒等式只使用 (5.3) 在 $M$ 上为零。
所有高次有限词只作用于共同深域，不擅自识别全部幂域。

## 6. 单个一次系数的 Sylvester 恒等式

从排序前 $N$ 个非零主位中，删除排序前 $\lfloor N/4\rfloor$ 个，
再删除原物理位小于 $m_N=\lfloor N/4\rfloor$ 的项。
余项至少有 $N/2$ 个。
取其中
$$
Q_N=\lfloor N/2\rfloor
$$
个，组成 $I_N$。
充分大时所有有限例外均已删去，且
$$
\boxed{
\min I_N\ge m_N,\qquad
\rho_N\le|a_j|\le 3\|a\|_2N^{-1/2}\quad(j\in I_N).
}
\tag{6.1}
$$

置
$$
\tau_j=\frac{c_j}{a_j}.
$$
由 (1.1)、(6.1)，
$$
c_-\rho_N^{\kappa-1}\le|\tau_j|
\le c_+\left(3\|a\|_2N^{-1/2}\right)^{\kappa-1}
\longrightarrow0
\tag{6.2}
$$
对所有所选位一致成立。

定义关于 $t$ 的两多项式
$$
\mathscr P(t;\mathbf z)=P_q(t;\mathbf z)+y-\lambda,
\qquad
\mathscr Q_j(t;\mathbf z)=\partial_tP_q(t;\mathbf z)+\tau_j,
$$
以及真实有限 Sylvester 行列式
$$
\mathscr R_j(\mathbf z)
=\operatorname{Res}_t(\mathscr P,\mathscr Q_j).
\tag{6.3}
$$
其系数是 $\mathbf z,\tau_j$ 的多项式。

在 $\mathbf z=0$ 处，若 $q(\mu)=\lambda$ 的根按重数计，
则
$$
\mathscr R_j(0)
=q_p^{\,p-1}\prod_{q(\mu)=\lambda}(q'(\mu)+\tau_j).
\tag{6.4}
$$
对于固定 $q,\lambda$，非零的 $q'(\mu)$ 只有有限多个。
所以存在固定 $\tau_0,C_*>0$，使对所有
$0<|\tau|\le\tau_0$，
$$
\left|
q_p^{\,p-1}\prod_{q(\mu)=\lambda}(q'(\mu)+\tau)
\right|
\ge C_*|\tau|^p.
\tag{6.5}
$$
具体地，零导数的根给若干个 $\tau$ 因子，
非零导数的因子则在小圆盘上统一远离零。
其消失阶至多为 $p$，故得到保守的 $p$ 次下界。
这对任意复相位的 $\tau$ 均成立。
$p=1$ 时结果式就是非零附近的常数 $q_1+\tau$，同样满足此界。

因此对大 $N$，
$$
|\mathscr R_j(0)|
\ge C_1\rho_N^{p(\kappa-1)}
\quad(j\in I_N).
\tag{6.6}
$$
所有结果式均为固定有限次数多项式，
$\tau_j$ 位于同一个固定小圆盘，故存在统一的局部 Lipschitz 常数
$$
|\mathscr R_j(\mathbf z)-\mathscr R_j(0)|
\le C_2\max_\nu|z_\nu|
\qquad(\max_\nu|z_\nu|\le1).
\tag{6.7}
$$

取
$$
D=p(\kappa-1),\qquad
\boxed{R_N=\epsilon\rho_N^D}
\tag{6.8}
$$
并固定足够小的 $\epsilon>0$。
由 (6.6)–(6.7)，在共同闭多圆盘
$\max_\nu|z_\nu|\le R_N$ 上，
$$
\boxed{
|\mathscr R_j(\mathbf z)|
\ge\tfrac12|\mathscr R_j(0)|
\ge C_3\rho_N^D.
}
\tag{6.9}
$$
稍减 $\epsilon$ 后该估计还保持于邻域，供真正 Cauchy 演算使用。

有限 Sylvester 伴随矩阵给系数多项式
$U_j,V_j$，使准确恒等式
$$
U_j(t;\mathbf z)\mathscr P(t;\mathbf z)
+
V_j(t;\mathbf z)\mathscr Q_j(t;\mathbf z)
=\mathscr R_j(\mathbf z)
\tag{6.10}
$$
成立。
可取 $\deg_tV_j\le p-1$；
其全部系数在 $\tau_j$ 的固定小圆盘上统一有界，
作为 $\mathbf z$ 的多项式次数也固定。
$p=1$ 时取 $U_j=0,V_j=1$。

在实际 $\mathbf A=(G_2,\ldots,G_p,Y)$ 及 $X_M$ 处求值，
(5.3) 消去第一项，得到
$$
V_j(X_M;\mathbf A)
\bigl(P_q'(X_M;\mathbf A)+\tau_j\bigr)
=\mathscr R_j(\mathbf A)|_M.
\tag{6.11}
$$
右侧属于 $\mathcal A$ 且字符为 $\mathscr R_j(0)\ne0$，
因而具有真实有界逆，并保持 $M$。
(6.11) 在交换代数中给实际核内双侧逆。
这里没有把形式代数根当作一个未证明的有界分支。

## 7. 所有分母一次支付的真实联合逆

对任意 $F\subset I_N$、$|F|=r$，置
$$
h_F(\mathbf z)=\prod_{j\in F}\mathscr R_j(\mathbf z)^{-1}.
$$
由 (6.9)，
$$
\sup_{\max|z_\nu|\le R_N}|h_F(\mathbf z)|
\le(C\rho_N^{-D})^r.
\tag{7.1}
$$
所有 $G_n,Y$ 都是交换的零字符 $\mathcal A$ 元，
各自谱为 $\{0\}$。
因此在同一半径 $R_N$ 上作一次真正的 $p$ 变量 Cauchy 演算，
得到
$$
\log^+\|h_F(\mathbf A)\|
\le
Dr\log^+\rho_N^{-1}+Cr
+\sum_{n=2}^p\Gamma_{G_n}(R_N)+\Gamma_Y(R_N).
\tag{7.2}
$$
这里
$$
\Gamma_Z(R)=\sup_{|z|=R}
\log^+\|z(z-Z)^{-1}\|.
$$
每个 $G_n\in\mathcal G$ 的零字符及正四次幂型给
$$
\Gamma_{G_n}(R)\le C_n(1+\log^+R^{-1})^{4/3}.
\tag{7.3}
$$
若某个系数为零，它的规范化预解范数恰为1。
(7.3) 来自 R151 的真实 $\mathcal G$ 结论，
不是从一般强理想或范数闭包外推。
$Y$ 只用 (4.7)，没有使用 $Y\in\mathcal G$。

准确一次系数是
$$
L_j=4a_jP_q'(X_M;\mathbf A)+4c_j
=4a_j(P_q'(X_M;\mathbf A)+\tau_j).
\tag{7.4}
$$
定义
$$
\boxed{
\mathfrak R_F
=
\left(\prod_{j\in F}(4a_j)^{-1}\right)
\left(\prod_{j\in F}V_j(X_M;\mathbf A)\right)
h_F(\mathbf A)|_M.
}
\tag{7.5}
$$
由 (6.11)，这是实际核内乘积逆：
$$
\left(\prod_{j\in F}L_j\right)\mathfrak R_F
=
\mathfrak R_F\left(\prod_{j\in F}L_j\right)=I_M.
\tag{7.6}
$$
每个 $V_j$ 为固定次数多项式。
实际 $\mathbf A$ 固定有界，$X_M$ 固定有界，
而 $\tau_j$ 一致小，故
$$
\|V_j(X_M;\mathbf A)\|\le C_M.
$$
这个估计在真实算子处直接求值；
不要求 $\|\mathbf A\|\le R_N$。

结合 (6.1)、(7.2)–(7.3) 和 (4.7)，得
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le K_0N^2+(D+1)r\log^+\rho_N^{-1}+C_Mr+C.
}
\tag{7.7}
$$
同一个 $K_0$ 对所有 $F$ 有效。
它不随 $r$ 次重复收取；公共预解成本在 (7.2) 只支付一次。
若有多项式下界 (2.3)，则 (7.7) 可加强为
$$
\log^+\|\mathfrak R_F\|
\le C N\log N+C r\log N+C_Mr.
\tag{7.8}
$$

## 8. 全阶真实反射、深域与平方零首项

固定 $\theta>0$ 并取
$$
r=\lceil\sqrt{N/\theta}\rceil.
$$
(6.1) 给
$$
\sum_{j\in F}|a_j|\le C_\theta,\qquad
\sum_{j\in F}|c_j|\le C_\theta
\tag{8.1}
$$
对 $|F|=r$ 一致成立。

令
$$
J_F=\prod_{j\in F}M_{\chi_j},\qquad
\gamma_F=\operatorname{Ad}J_F,\qquad
u_j=t_jN_j.
$$
只在所选位将 $u_j$ 改为 $-u_j$，定义带帽的 $X,Y,G_n$。
R260 的最高真实物理位壳估计，
以及已证全阶二位稿对明确 $G_n$ 表达式的完整推广，给
$$
\|\delta_X^s(\gamma_FX-\widehat X)\|
+\|\delta_X^s(\gamma_FY-\widehat Y)\|
+\sum_{n=2}^p
\|\delta_X^s(\gamma_FG_n-\widehat G_n)\|
\le s!\varepsilon_N,
$$
$$
\varepsilon_N\le C_p e^{-385\,16^{m_N-1}}.
\tag{8.2}
$$
这包括实际跨度任意大时的全部必要自然域导数；
常数不依赖 $\max F$。
有限系数乘积的导子由完整导子 Banach 代数支付。

每个 $\widehat G_n-G_n$ 的所选位差含真实 $u_j^n$，
其中 $n\ge2$。
所以它没有平方零商中的一次项。
此外
$$
\widehat X-X=4\sum_{j\in F}a_ju_j
\quad\bmod(u_j^2),
$$
$$
\widehat Y-Y=4\sum_{j\in F}c_ju_j
\quad\bmod(u_j^2).
$$
在 $M$ 上，主多项式为
$$
A_F=
\sum_{\ell=1}^p\frac{P_q^{(\ell)}(X_M;\mathbf A)}{\ell!}
\left(4\sum_{j\in F}a_ju_j\right)^\ell
+4\sum_{j\in F}c_ju_j.
\tag{8.3}
$$
其一次部分正是 $\sum_{j\in F}u_jL_j$。
在 $r$ 个不同位的平方零商中，$r$ 个因子只能各取一次项，
故
$$
\boxed{
A_F^r\equiv
r!t_FN_F\prod_{j\in F}L_j
\pmod{(N_j^2:j\in F)}.
}
\tag{8.4}
$$
所有含更高次差分的词总次数大于 $r$，必有重复位。
它们通过实际 $\eta_j$ 支付，未将平方零模型视为原算子恒等式。

对 $f\in M$，先令
$$
f_F=\mathfrak R_Ff\in M.
$$
由 (5.4)，所有 $X^kf_F$ 在自然域内并满足核内几何范数界。
$J_F$ 双向保持共同深域。
(8.1)–(8.2) 的实际有限词正规排序给
$$
\|X^kJ_Ff_F\|
\le2R_{p,M,\theta}^k\|f_F\|
\qquad(0\le k\le4pr).
\tag{8.5}
$$
全部误差词至多产生
$\varepsilon_Ne^{C_{p,\theta}r\log(r+2)}\|f_F\|$ 的成本。
这里不对核内逆作未知投影导数，也不需要 $J_FM\subset M$。

顺序准确为
$$
T_\lambda^rJ_F\mathfrak R_Ff
=
J_F(\gamma_FT_\lambda)^r\mathfrak R_Ff.
\tag{8.6}
$$
先在 $M$ 中使用 (7.6) 消去乘积，
再作用最左侧 $J_F$。
由于纯位乘积满足 $J_FE_F=(-1)^rE_F$，
得到
$$
T_\lambda^rJ_F\mathfrak R_Ff
=(-1)^rr!t_FE_Ff+\mathcal E_Ff,
\tag{8.7}
$$
其中
$$
\|\mathcal E_Ff\|
\le
\varepsilon_Ne^{C_{p,\theta}r\log(r+2)}
\|\mathfrak R_F\|\|f\|
+
Cr!|t_F|r\eta_{m_N}\|f\|.
\tag{8.8}
$$
$p$ 固定，故全部有限次数增长已被 (8.5) 的 $4pr$ jets 覆盖。

## 9. 精确单池平均与四次成本

定义实际输入平均
$$
\mathcal V_N=
(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F.
\tag{9.1}
$$
其像在共同深域中。
令 $L_b^-=\max(1,\sup_j|t_j|^{-1})$，组合数给
$$
\|\mathcal V_N\|\le A_N,\qquad
A_N=
\max\left\{
1,\frac{(2L_b^-)^r}{r!}
\sup_F\|\mathfrak R_F\|
\right\}.
$$
由 (7.7)，
$$
\log A_N
\le K_0N^2+(D+1)r\log^+\rho_N^{-1}+C_M'r+C.
\tag{9.2}
$$
实际提升 (8.7) 的 $r!$ 与 $\binom{Q_N}r$ 的平均恰好归一化为
$$
C_{I_N}^r,\qquad C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
$$
因此
$$
\|T_\lambda^r\mathcal V_Nf-C_{I_N}^rf\|
\le
\left[
\varepsilon_Ne^{C_{p,\theta}r\log(r+2)}A_N
+C2^rr\eta_{m_N}
\right]\|f\|\longrightarrow0.
\tag{9.3}
$$
双指数 carry 支付这里全部成本。

纯平均有一致范数界
$$
\|C_{I_N}^r\|\le(1+1/Q_N)^r.
$$
在两个固定有限柱之间，其矩阵系数为
$$
\frac{(Q_N)_r}{Q_N^r}.
$$
由于 $Q_N\sim N/2$、$r\sim\sqrt{N/\theta}$，
该系数趋于 $e^{-1/\theta}$。
于是
$$
\boxed{T_\lambda^r\mathcal V_Nf
\rightharpoonup e^{-1/\theta}f.}
\tag{9.4}
$$
此弱极限非零且一致有界。

固定任意前 $h$ 位局部全矩阵 $D_0$。
全阶稿已经逐项证明的真实有限头分解为
$$
T_\lambda=T_{\lambda,\mathrm{tail},h}+A U_h(X),
\qquad
\deg U_h\le p-1.
\tag{9.5}
$$
尾项与 $D_0$ 完整域交换，两个加项在共同深域上交换。
只有固定有限头被真实提出一个 $A$，
没有将完整 $G_n$ 或慢 $Y$ 有界除以 $A$。

因此每次局部交换留下一个实际 $A$ 因子。
$\operatorname{ad}_{T_\lambda}^rD_0$ 的有限词含
$$
A^kU_h(X)^kD_0A^{r-k}U_h(X)^{r-k}.
$$
$X$ 总阶至多 $(p-1)r$，全部由 (8.5) 支付。
固定头 $\delta_X^sD_0$ 的几何界只增加固定几何成本。
由原 $A$ 的四次幂界以及
$k^4+(r-k)^4\ge r^4/8$，
$$
\boxed{
\|(\operatorname{ad}_{T_\lambda}^rD_0)\mathcal V_Nf\|
\le
2\|D_0\|A_NC_{p,D_0,M,\theta}^r
e^{-5r^4/6+105r^3}\|f\|.
}
\tag{9.6}
$$
这是一条具体深域输入上的估计，不是全空间有界交换子断言。

由 (2.2)、(9.2)，
$$
\limsup_{N\to\infty}\frac{\log A_N}{r^4}
\le K_0\theta^2.
$$
因为 $r\log^+\rho_N^{-1}=O(N^{3/2})=o(N^2)$。
取固定足够小的 $\theta>0$，使 $K_0\theta^2<1/4$，
则 (9.6) 趋零。
$\theta$ 的选择与局部测试 $D_0$ 无关。
在多项式下界子类中，(7.8) 甚至给
$\log A_N=o(r^4)$，任意固定 $\theta>0$ 均足。

## 10. 完整 C 配对排除原核

对任意 $f,g\in M$，所有被测试的有限词均在共同深域中。
原完整 $C$ 自伴性与 $T_\lambda g=0$ 给
$$
\mathcal B(D_0T_\lambda^r\mathcal V_Nf,g)
=
(-1)^r\mathcal B(
(\operatorname{ad}_{T_\lambda}^rD_0)\mathcal V_Nf,g),
$$
其中
$$
\mathcal B(f,g)=\int f(y)g(-1-y)\,dy.
$$
不要求 $CM=M$。
由 (9.4)、(9.6)，
$$
\mathcal B(D_0f,g)=0
$$
对全部局部全矩阵 $D_0$ 成立。
局部矩阵代数不可约，迫 $M=0$。

完整 $C$ 自伴性继而给 $T_\lambda$ 的像稠密；
$\xi=e^w$ 的真实循环图核心给
$T_\lambda\xi=[F_q+v_c-\lambda]e^w$ 循环。
第二分支完成；与第三节第一分支合并，定理 1、推论 2 得证。

## 11. 新范围与保留的边界

本定理不要求每个排序位置都有可用下界。
第一次降幅传播只在无穷子序列上工作；
遇到无法形成有限成本第二池的巨大跳跃时，
该跳跃本身通过 $\kappa>2$ 产生真实小辅助尾。
这一步使用全部主行的 $\ell^2$ 质量，而不是仅看单个尾系数。

主行可以为任意相位、任意物理排列的
$\ell^2\setminus\ell^1$ 行；
尤其无须把它改成同射线的旧空谱分支。
迟首辅助及任意有限低头例外均包含在内。
结论同时对全部固定共振次数和全部标量位移成立。

较强的 (1.3) 型充分条件也覆盖不少可和主行。
另一方面，若
$$
\frac{\log^+\rho_n^{-1}}n\longrightarrow\infty,
$$
本稿的种子条件可能失效。
其中满足先前全局
$\log^+\rho_n^{-1}=O(n^{3/2})$
的行仍由自动双池稿覆盖；
其余可和极快行不能仅凭本文判定已闭。
已有快辅助 $\mathcal G$ 理论也必须按其原排序超三次条件使用，
不能把任意超指数行都视作 $\mathcal G$。

若主行零位上另有不受 (1.1) 控制的无限辅助尾，
或辅助与主幅度没有上下比较，
需要另外验证真实小尾或双池行列式条件。
本稿没有将这些情况合并进已证范围。

## 12. 来源

- [自动分离双池源](../notes/2026-11-13-automatic-separated-pools-irregular-l2-and-two-power-auxiliary-envelopes-central-review.md)：
  固定比例降幅、任意物理排序删除及不同辅助幂界。
- [全阶二位 Bézout 源](../notes/2026-11-13-all-order-resonant-two-site-bezout-and-derivation-budgets-central-review.md)：
  完整 $G_n$ 反射导子、全阶平方零计数、真实自然 jets 与固定头四次估计。
- [辅助半径源](../notes/2026-11-13-auxiliary-scale-joint-resolvent-arbitrary-l2-main-and-tail-gaps-central-review.md)：
  单池核内逆的正确反射顺序、精确平均与完整双线性排核。
- [任意物理头及尾间隙源](../notes/2026-11-13-tail-gap-resolvent-budget-and-nonweak-l1-plateau-near-resonance-central-review.md)：
  原函数正锥估计、真实全方向 Laplace 积分及与最大物理位无关的有限头成本。
- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  原自然闭域、完整 $C$ 自伴、核内有界 first 及真实循环图核心。
- [R270C](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) §10：
  准确共振 $F_q$、实际 $G_n$ 与有限自然 jets。
- [R151](../results/R151-quartic-analytic-approximation-gauge-stability.md)：
  真正 $\mathcal G$ 元的四次幂型与实际预解预算。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意跨度最高物理位壳与完整导子 Banach 代数。
- [R109](../results/R109-invariant-restriction-exact-quartic-type.md)：
  原实际 $A$ 的四次幂界与 carry 归一化。

本稿新增的是受控种子下的真实二分、
(6.3)–(7.7) 的全阶 Sylvester 乘积分母一次联合逆，
以及将这些输入接入原自然域和四次配对后的非可和全范围闭合。


[完整工作源](../notes/2026-11-13-nonsummable-main-dichotomy-and-all-order-sylvester-joint-inverses-central-review.md)。
