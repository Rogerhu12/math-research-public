# 双行全共振多项式：平滑字符纤维、二位消元与指数子序列闭合

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。
**状态：已证明。** 以下给出完整实际证明及范围。
本文把“单主行共振多项式加线性辅助”推广为双行的真实非线性共振耦合。
不以未修正的普通点态多项式替换准确共振符号。
一般 Hilbert 不变子空间问题仍未完成。

## 1. 主行、辅助行与双变量共振符号

取复 $a,b\in\ell^2$、任意常数 $a_*,b_*$，且 $a$ 有无限非零支撑。
记非零主幅度递减重排为 $\rho_n$，保留每项的原物理位。

假设某个实数 $\kappa>2$ 及常数 $c_-,c_+>0$ 满足
$$
c_-|a_j|^\kappa\le|c_j|\le c_+|a_j|^\kappa
\quad(j\ge j_0)
\tag{1.1}
$$
对某个有限物理阈值 $j_0$ 成立。
主行零位因此要求 $c_j=0$ 于全部充分高的物理位；
有限低头的辅助值任意。
自动有 $c\in\ell^1$。

令
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v=\sum_jc_j(\chi_j-1),\qquad
w=b_*+\sum_jb_j\chi_j.
$$
给定标量多项式
$$
F(U,V)=\sum_{k=0}^p f_k(V)U^k,
\qquad p\ge1,\qquad
\boxed{f_p(0)\ne0.}
\tag{1.2}
$$
记其总次数为 $d$，故 $d\ge p$。

取只需到总次数 $d$ 的生成 jets
$$
\mathscr E(t,s)=
\exp\left[
tu+sv+
\sum_{n=2}^d\frac{2^{n-1}}n
\sum_j(ta_j+sc_j)^n(\chi_j-1)
\right].
\tag{1.3}
$$
定义准确双行共振符号
$$
\boxed{
\mathfrak F_F
=
\left.F(\partial_t,\partial_s)\mathscr E(t,s)\right|_{t=s=0}.
}
\tag{1.4}
$$
每个 $n\ge2$ 的辅助行绝对可和，所以 (1.3) 的固定 jets 实际存在。
所有有限混合矩乘 $e^w$ 属于 $L^2$。

例如
$$
\mathfrak F_U=u,\qquad \mathfrak F_V=v,
$$
$$
\mathfrak F_{U^2}=u^2+2\sum_j a_j^2(\chi_j-1),
$$
$$
\mathfrak F_{UV}=uv+2\sum_j a_jc_j(\chi_j-1),
\qquad
\mathfrak F_{V^2}=v^2+2\sum_j c_j^2(\chi_j-1).
\tag{1.5}
$$
当 $F(U,V)=q(U)+V$ 时，这恰为此前的 $F_q+v$。

置
$$
f_0^{\mathrm{char}}(z)=F(z,0).
$$
由 (1.2)，它是次数恰为 $p$ 的非恒定多项式。

## 2. 主定理及准确例外集合

假设主幅度满足指数下界子序列条件
$$
\boxed{
\liminf_{n\to\infty}
\frac{\log^+\rho_n^{-1}}n<\infty.
}
\tag{2.1}
$$
所有 $a\in\ell^2\setminus\ell^1$ 自动满足 (2.1)。

**定理 1。**
固定 $\lambda\in\mathbb C$。
若对每个满足 $F(\mu,0)=\lambda$ 的标量根，
$$
\boxed{(F_U(\mu,0),F_V(\mu,0))\ne(0,0),}
\tag{2.2}
$$
则
$$
\boxed{
(\mathfrak F_F-\lambda)e^w
\text{ 非零且对原实际 }A\text{ 循环}.
}
\tag{2.3}
$$
允许该一变量纤维具有重根。
对主行、辅助及指数权的相位和物理排列均无额外限制。

因 $F(U,0)$ 非恒定，集合
$$
\mathcal E_F=
\{F(\mu,0):F_U(\mu,0)=F_V(\mu,0)=0\}
\tag{2.4}
$$
有限，并且至多含 $p-1$ 个值。
定理适用于所有 $\lambda\notin\mathcal E_F$。
若每个 $F_U(\mu,0)=0$ 的点都有 $F_V(\mu,0)\ne0$，
则 $\mathcal E_F$ 为空，全部标量位移均闭合。

(2.4) 只是本判据的未排除集合。
其中某些情形可能已被旧 $\mathcal G[X]$ 或其他定理关闭；
本文不把它们统称为新的开放例。

## 3. 全部混合修正的真实算子实现

令
$$
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j),\qquad
X=X_{u,b},\qquad Y=\sum_jc_j(R_j-I).
\tag{3.1}
$$
$Y$ 为有界零字符 $\mathcal A$ 元。

对 $r,s\ge0$、$2\le r+s\le d$，定义
$$
\boxed{
G_{r,s}
=
(-1)^{r+s-1}(r+s-1)!
\sum_j a_j^r c_j^s(R_j-I)^{r+s}.
}
\tag{3.2}
$$
若某一指数为零，相应标量幂取1。
全部和绝对算子范数收敛。
事实上，$\sum_j|a_j|^r|c_j|^s<\infty$：
纯主项用 $r\ge2$，混合项用平方和或有界性乘可和性，
纯辅助项直接用 $c\in\ell^1$。

更强地，
$$
\boxed{G_{r,s}\in\mathcal G,\qquad\chi(G_{r,s})=0.}
\tag{3.3}
$$
这是局部至少二阶消去的真实 carry 结论。
可直接套 R270B/R270C 的局部归一化定理：
函数
$$
a_j^rc_j^s[V(e^{-2b_j}z)-1]^{r+s}
$$
在固定小圆盘内有统一解析预算，并在零点至少二阶消去。
也可写出 $N_j^2=\eta_jN_{j+1}$，
将余下的统一有界真解析因子交给 R154 引理2.1。
$\eta_j\le e^{-385\,16^j}$ 提供排序超三次系数。
本步没有把 $\mathcal G$ 当成整个 $\mathcal A$ 的理想。

定义实际有限系数多项式
$$
\boxed{
P_F(x,y;\mathbf G)
=
\exp\left(
\sum_{\substack{r,s\ge0\\2\le r+s\le d}}
\frac{G_{r,s}}{r!s!}\partial_x^r\partial_y^s
\right)F(x,y).
}
\tag{3.4}
$$
指数是作用于固定多项式的有限和。

R270C 的单个位恒等式中用 $z=ta_j+sc_j$，
其真实对数修正就是 (3.2)。
有限位恒等式的全部固定混合 jets 再由 R176/R186 的通常伴随核心取极限。
$Y$ 有界，全部辅助自然词只留下主变量的自然幂域。
准确得到
$$
\boxed{
P_F(X,Y;\mathbf G)e^w=\mathfrak F_Fe^w.
}
\tag{3.5}
$$
这也可由 R147 慢辅助附录的完整混合 Bell jets 逐阶核对；
没有把全空间的 $e^{tX}$ 当作有界算子。

关于 $x$ 的最高系数准确为
$$
L(Y;\mathbf G)
=
\left[
\exp\left(\sum_{s=2}^d\frac{G_{0,s}}{s!}\partial_y^s\right)
f_p(y)
\right]_{y=Y}.
\tag{3.6}
$$
它一般不等于未经修正的 $f_p(Y)$，但
$$
\chi(L)=f_p(0)\ne0.
$$
所以 $L$ 是真实 $\mathcal A$ 单位。

因此
$$
T_\lambda=P_F(X,Y;\mathbf G)-\lambda I,
\qquad
\operatorname{Dom}T_\lambda=\operatorname{Dom}X^p
\tag{3.7}
$$
具有 R176 的真实自然闭域、完整 $C$ 自伴性和 $e^w$ 循环图核心。

若 $M=\ker T_\lambda\ne0$，则
$$
M\subset\mathcal D_\infty(X),\qquad X_M\in B(M).
\tag{3.8}
$$
其谱包含于 $F(z,0)=\lambda$ 的有限根集。
按这些根作核内 Riesz 分块：
$$
M=\dotplus_\mu M_\mu,\qquad
\sigma(X_{M_\mu})=\{\mu\}.
\tag{3.9}
$$
各非零块闭且 $A$ 不变，全部 $\mathcal A$ 系数保持它们。
下面可以逐个排除这些块。
不把不同根上的偏导单位性质混为一个统一单位断言。

## 4. 实际一次系数与混合 jets

对任意高物理集合 $E$，置
$$
J_E=\prod_{j\in E}M_{\chi_j},\qquad u_j=t_jN_j.
$$
在所选位把 $u_j$ 改成 $-u_j$，定义带帽的 $X,Y,G_{r,s}$。
R260 的最高真实物理位壳证明适用于每个固定局部多项式
$(R-I)^{r+s}$；
其系数行 $a_j^rc_j^s$ 平方可和。
所以全部混合修正有与主行同一形式的完整导子估计
$$
\|\delta_X^\ell(\gamma_EX-\widehat X)\|
+\|\delta_X^\ell(\gamma_EY-\widehat Y)\|
+\sum_{r,s}\|\delta_X^\ell
(\gamma_EG_{r,s}-\widehat G_{r,s})\|
\le \ell!\varepsilon_m,
$$
$$
\varepsilon_m\le C_d e^{-385\,16^{m-1}},
\qquad m=\min E.
\tag{4.1}
$$
所有有限系数乘积由完整导子 Banach 代数支付。
该估计与 $\max E$ 无关。

每个混合 $\widehat G_{r,s}-G_{r,s}$ 都含所选位的
$u_j^{r+s}$，而 $r+s\ge2$。
因此在平方零商中没有一次项。
准确的一次系数是
$$
\boxed{
L_j=4a_j P_x(X_M,Y;\mathbf G)
+4c_j P_y(X_M,Y;\mathbf G).
}
\tag{4.2}
$$
这里偏导只对显示的两个变量求取，固定全部混合 $G_{r,s}$。
它们真实 gauge 变化的高次项已经由 (4.1) 支付。

若所选位满足 $|a_j|\le C N^{-1/2}$、$|E|=O(r_N)$，
其中 $r_N\asymp\sqrt N$，则
$$
\sum_E|a_j|+\sum_E|c_j|\le C_\theta.
\tag{4.3}
$$
给定任何先在核中形成的输入 $h_E\in M$，
实际正规排序于是给
$$
\|X^kJ_Eh_E\|\le2R_{d,M,\theta}^k\|h_E\|
\qquad(0\le k\le4d\,r_N).
\tag{4.4}
$$
全部误差词至多付
$\varepsilon_m e^{C_{d,\theta}r_N\log(r_N+2)}\|h_E\|$。
混合总次数 $d$ 固定，但不限制其大小。

固定物理低头的局部矩阵 $D_0$ 时，真实有限头分解为
$$
\boxed{
T_\lambda=T_{\lambda,\mathrm{tail},h}+A\,U_h(X),
\qquad \deg U_h\le p.
}
\tag{4.5}
$$
此处允许次数为 $p$，因为最高系数 $L(Y;\mathbf G)$ 也可能有低头变化。
尾算子与 $D_0$ 完整域交换。
每个系数的固定有限头都是真解析零常数项，实际提出一个 $A$；
不对整个慢 $Y$ 或整个混合修正作形式除法。
(4.4) 的 $4d\,r_N$ jets 足以覆盖局部词的至多 $pr_N$ 阶主变量。

因此所有下文输入平均 $\mathcal V_N$，只要范数预算为 $A_N$，均有
$$
\boxed{
\|(\operatorname{ad}_{T_\lambda}^{r_N}D_0)\mathcal V_Nf\|
\le
2\|D_0\|A_NC_{d,D_0,M,\theta}^{r_N}
e^{-5r_N^4/6+105r_N^3}\|f\|.
}
\tag{4.6}
$$
这是原四次幂界在具体深域向量上的估计。
增加一个固定主变量次数只改变几何常数，不破坏四次负项。

## 5. 带有可控前幅度的同一二分

从指数下界种子 (2.1) 出发，沿
$$
N_j=L^jN_0,\qquad L>\delta^{-2},\qquad K=3L,
$$
取第一次满足
$$
\rho_{KN}\le\delta\rho_{3N}
$$
的位置。
原平方可和首次降幅引理给无穷子序列
$$
\boxed{
\rho_{KN}\le\delta\rho_{3N},\qquad
\log^+\rho_{3N}^{-1}=O(N).
}
\tag{5.1}
$$
其中
$$
\delta\le
\min\left\{\frac12,
(c_-/(2c_+))^{1/(\kappa-1)}\right\}
$$
固定。
这个步骤不依赖 $F$、其次数或 $\lambda$。

若有无穷多个所选 $N$ 满足
$$
\rho_{(K+2)N}\ge e^{-N^{3/2}},
\tag{5.2}
$$
则排序带 $(N,3N]$ 与 $(KN,(K+2)N]$ 经各删除低于 $N$ 的物理位，
给两个各含 $N$ 位的真实池 $I_N,J_N$，满足
$$
\min(I_N\cup J_N)\ge N,\qquad
\max|a_j|\le\|a\|_2N^{-1/2},
$$
$$
d_N:=\min_{I_N\times J_N}|a_kc_j-a_jc_k|>0,\qquad
1+\log^+d_N^{-1}=O(N^{3/2}).
\tag{5.3}
$$
反三角估计仍是
$$
d_N\ge(c_-/2)\rho_{3N}^{\kappa}\rho_{(K+2)N}.
$$

否则沿另一无穷子序列有
$$
\rho_{(K+2)N}<e^{-N^{3/2}}.
\tag{5.4}
$$
前 $(K+2)N$ 个主排序位加全部有限例外组成真实物理头 $H_N$，大小 $O(N)$。
其外的辅助正锥主控范数满足
$$
\left\|\sum_{j\notin H_N}|c_j|W(N_j)\right\|
\le C\sum_{n>(K+2)N}\rho_n^\kappa
\le C\|a\|_2^2e^{-(\kappa-2)N^{3/2}}.
\tag{5.5}
$$
因此任意固定 $D>0$、$\epsilon>0$ 的半径
$$
R_N=\epsilon\rho_N^D
$$
都由原真实全方向 Laplace 头尾引理给
$$
\boxed{
\Gamma_Y(R_N)=O(N^2).
}
\tag{5.6}
$$
常数不依赖头部的最大物理位。
这一结论使用 (5.1) 的 $\log^+\rho_N^{-1}=O(N)$；
没有把慢 $Y$ 归为 $\mathcal G$。

## 6. 双池分支中的两种真实根块

固定 (3.9) 的一个非零块 $M_\mu$。
所有下文核内算子都限制于这个块。
它上面的 $X-\mu I$、$Y$ 与各混合 $G_{r,s}$ 是交换拟幂零元。
故任何有界系数多项式在该块上的字符值为其在
$(x,y,\mathbf G)=(\mu,0,0)$ 的值。

### 6.1 主偏导不为零的块

如果
$$
F_U(\mu,0)\ne0,
$$
则
$$
A_\mu=P_x(X_{M_\mu},Y;\mathbf G)
$$
是实际单位。
另记
$$
C_\mu=P_y(X_{M_\mu},Y;\mathbf G).
$$
从前 $N$ 个主排序位双删除最高 $N/4$ 幅度和最低 $N/4$ 物理位，
取 $Q_N=\lfloor N/2\rfloor$ 位。
它们满足
$$
\rho_N\le|a_j|\le3\|a\|_2N^{-1/2},\qquad
|\tau_j|:=|c_j/a_j|\longrightarrow0
$$
一致成立。
所以对于充分大 $N$，
$$
\|(A_\mu+\tau_jC_\mu)^{-1}\|
\le2\|A_\mu^{-1}\|.
\tag{6.1}
$$
由 (4.2)，乘积一次系数的真正核内逆满足
$$
\left\|\prod_{j\in E}L_j^{-1}\right\|
\le(C_{M_\mu}\rho_N^{-1})^{r_N}.
\tag{6.2}
$$
这仅支付 $O(r_NN)=O(N^{3/2})$ 的对数成本。
单池平均和 (4.6) 已足以排掉这个块，
无需任何辅助预解估计或第二池。
详细的平均与配对与第八节相同。

### 6.2 辅助偏导为单位的块

若 $F_U(\mu,0)=0$，则由 (2.2)，
$$
F_V(\mu,0)\ne0.
$$
于是
$$
C_\mu=P_y(X_{M_\mu},Y;\mathbf G)
$$
是固定的实际单位。
对一对 $j\in I_N,k\in J_N$，令
$$
\Delta_{jk}=a_kc_j-a_jc_k,\qquad
P_{jk}=
C_\mu^{-1}
\frac{a_ku_k-a_ju_j}{4\Delta_{jk}}.
\tag{6.3}
$$
在两位平方零商中，
$$
(u_jL_j+u_kL_k)P_{jk}=u_ju_k.
\tag{6.4}
$$
因为交叉项恰为
$$
a_kL_j-a_jL_k=4\Delta_{jk}C_\mu.
$$
这是同一个未知核块内的真实单位消元。

取两池各 $r_N$ 位，固定一个匹配，不重复计数所有匹配。
输入为
$$
P_{I,J}=\prod_{\text{匹配对}}P_{jk}.
$$
其标量部分的绝对系数预算是
$$
H_N\le
\left(\frac{C}{\sqrt N\,d_N}\right)^{r_N},
$$
而 $C_\mu^{-r_N}$ 另贡献恰为固定几何成本
$$
\|C_\mu^{-1}\|^{r_N}.
\tag{6.5}
$$
不能只估计可能发生消去后的输入算子范数。

输入总次数为 $r_N$，所选位数为 $2r_N$。
$T_\lambda$ 的每个实际差分至少一次；
在 $r_N$ 次提升中，只有全部一次项能达到平方零顶部次数。
任何更高混合差分都产生重复位。
因此 (6.4) 给
$$
T_\lambda^{r_N}J_{I\cup J}P_{I,J}f
=r_N!t_{I\cup J}E_{I\cup J}f+\text{已付 carry/导子误差}.
\tag{6.6}
$$
输入先在核内形成，$J_{I\cup J}$ 始终只在最左侧作用。
不把 $C_\mu^{-1}$ 移到反射左边。

取双池平均
$$
\mathcal V_N=
r_N!(2/N)^{2r_N}
\sum_{\substack{|I|=|J|=r_N}}
t_{I\cup J}^{-1}J_{I\cup J}P_{I,J}.
\tag{6.7}
$$
两个阶乘恰好归一化两个池各自的 $r_N$ 次纯平均，
故
$$
T_\lambda^{r_N}\mathcal V_Nf\rightharpoonup e^{-1/\theta}f.
\tag{6.8}
$$
范数预算为
$$
\log A_N
\le r_N(1+\log^+d_N^{-1})+C_{M_\mu}r_N.
\tag{6.9}
$$
取足够小的固定 $\theta$，(5.3)、(4.6) 支付此成本；
完整配对排除 $M_\mu$。

因此双池分支在所有根块上均闭合。
没有要求同一个偏导在所有标量根上同时为单位。

## 7. 小尾分支的固定次数 Sylvester 逆

以下在 (5.4) 子序列上处理整个 $M$，不必先分根。
变量包括一个显示的 $y$ 和全部形式混合变量
$$
\mathbf z=(y,(g_{r,s})_{2\le r+s\le d}).
$$
变量个数固定为
$$
m=1+\sum_{n=2}^d(n+1)
=\frac{(d+1)(d+2)}2-2.
\tag{7.1}
$$
当 $d=1$ 时，空和给 $m=1$。

从前 $N$ 个主排序位作与 §6.1 相同的双删除，
取 $Q_N=\lfloor N/2\rfloor$ 位。
对它们有
$$
c_-\rho_N^{\kappa-1}\le|\tau_j|=|c_j/a_j|
\le C N^{-(\kappa-1)/2}\longrightarrow0.
\tag{7.2}
$$

把 (3.4) 中的 $G_{r,s}$ 换成形式变量，记所得多项式仍为
$P_F(x;\mathbf z)$。
定义
$$
\mathscr P(x;\mathbf z)=P_F(x;\mathbf z)-\lambda,
$$
$$
\mathscr Q_j(x;\mathbf z)
=(P_F)_x(x;\mathbf z)+\tau_j(P_F)_y(x;\mathbf z).
\tag{7.3}
$$
关于 $x$，二者的次数均不超过 $p$。
特别，$(P_F)_y$ 可以仍含 $x^p$，
所以这里必须用固定的 $(p,p)$ Sylvester 矩阵；
不得照抄 $(p,p-1)$ 的 leading 因子。

令其行列式为 $\mathscr R_j(\mathbf z)$。
在 $\mathbf z=0$，若 $F(\mu,0)=\lambda$ 的根按重数计，准确有
$$
\boxed{
\mathscr R_j(0)
=f_p(0)^p
\prod_{F(\mu,0)=\lambda}
\bigl(F_U(\mu,0)+\tau_jF_V(\mu,0)\bigr).
}
\tag{7.4}
$$
当第二个多项式实际次数降低时，固定 Sylvester 行列式保留相应的
$f_p(0)$ 因子；该常数非零。

由 (2.2)，对于每个因子：
若 $F_U(\mu,0)\ne0$，它在小 $\tau$ 圆盘上远离零；
若 $F_U(\mu,0)=0$，则它恰为
$\tau F_V(\mu,0)$ 且 $F_V(\mu,0)\ne0$。
因此对所有充分小的非零复 $\tau$，
$$
|\mathscr R_j(0)|\ge C|\tau_j|^p
\ge C'\rho_N^{p(\kappa-1)}.
\tag{7.5}
$$

全部结果式为同一有限次数的系数多项式，
在 $\tau_j$ 的固定小圆盘上有统一的局部 Lipschitz 常数。
故取
$$
D=p(\kappa-1),\qquad
\boxed{R_N=\epsilon\rho_N^D}
\tag{7.6}
$$
并固定足够小的 $\epsilon>0$，便有
$$
|\mathscr R_j(\mathbf z)|
\ge\tfrac12|\mathscr R_j(0)|
\ge C\rho_N^D
\quad(\max_\nu|z_\nu|\le R_N).
\tag{7.7}
$$
可把估计保留于稍大的邻域。

固定 $(p,p)$ Sylvester 伴随矩阵给实际系数多项式
$U_j,V_j$，其中
$$
\deg_xU_j,\deg_xV_j\le p-1,
$$
满足
$$
U_j\mathscr P+V_j\mathscr Q_j=\mathscr R_j.
\tag{7.8}
$$
全部系数作为 $\mathbf z,\tau_j$ 的多项式具有固定次数和统一常数。
在真实
$$
\mathbf A=(Y,(G_{r,s})_{2\le r+s\le d})
$$
及 $X_M$ 处代入，第一项因 $T_\lambda|_M=0$ 消失。
这给 $\mathscr Q_j(X_M;\mathbf A)$ 的真正核内逆，
而非形式根分支。

对 $E$ 中 $r_N$ 个位，把所有分母先合并：
$$
h_E(\mathbf z)=\prod_{j\in E}\mathscr R_j(\mathbf z)^{-1}.
$$
仅作一次 $m$ 变量 Cauchy 演算，得到
$$
\log^+\|h_E(\mathbf A)\|
\le
D r_N\log^+\rho_N^{-1}+Cr_N
+\Gamma_Y(R_N)+\sum_{r,s}\Gamma_{G_{r,s}}(R_N).
\tag{7.9}
$$
每个 $G_{r,s}\in\mathcal G$ 的预算是
$O((1+\log R_N^{-1})^{4/3})$，
其个数固定。
慢 $Y$ 单独使用 (5.6)。
所以这次联合预解成本为 $O(N^2)$，不随 $r_N$ 次重复收取。

准确乘积逆为
$$
\boxed{
\mathfrak R_E=
\left(\prod_{j\in E}(4a_j)^{-1}\right)
\left(\prod_{j\in E}V_j(X_M;\mathbf A)\right)
h_E(\mathbf A)|_M.
}
\tag{7.10}
$$
它满足
$$
\left(\prod_{j\in E}L_j\right)\mathfrak R_E=I_M.
$$
实际 $\mathbf A,X_M$ 均固定有界，
所以每个伴随多项式在实际算子处的范数至多 $C_M$，
不需要实际算子范数小于公共圆半径。
由此
$$
\boxed{
\log^+\|\mathfrak R_E\|
\le
K_0N^2+(D+1)r_N\log^+\rho_N^{-1}+C_Mr_N+C.
}
\tag{7.11}
$$

## 8. 单池提升、真实顺序与完整配对

在 §6.1 或 §7 的核内乘积逆构造中，
令
$$
h_E=\mathfrak R_Ef\in M.
$$
其所有自然 jets 先由核内有界 $X_M$ 控制，
再由 (4.4) 控制左反射。
实际顺序固定为
$$
T_\lambda^{r_N}J_E\mathfrak R_Ef
=
J_E(\gamma_ET_\lambda)^{r_N}\mathfrak R_Ef.
\tag{8.1}
$$
平方零商中只有一次项给顶部：
$$
(\gamma_ET_\lambda)^{r_N}
\equiv r_N!t_EN_E\prod_{j\in E}L_j.
$$
先在核内取消乘积，再作用最左 $J_E$，得到
$$
T_\lambda^{r_N}J_E\mathfrak R_Ef
=(-1)^{r_N}r_N!t_EE_Ef+\text{已付误差}.
\tag{8.2}
$$
任意高次混合差分均有重复位，通过真实 carry 处理。

定义
$$
\mathcal V_N=
(-1)^{r_N}(2/Q_N)^{r_N}
\sum_{\substack{E\subset I_N\\|E|=r_N}}
t_E^{-1}J_E\mathfrak R_E.
\tag{8.3}
$$
组合数与 (8.2) 的阶乘恰给一个池的纯平均。
因 $Q_N\sim N/2$、$r_N\sim\sqrt{N/\theta}$，
$$
\boxed{
T_\lambda^{r_N}\mathcal V_Nf
\rightharpoonup e^{-1/\theta}f
}
\tag{8.4}
$$
且提升后的范数一致有界。
全部误差由
$$
\varepsilon_{\lfloor N/4\rfloor}
e^{C_{d,\theta}r_N\log(r_N+2)}A_N
+C2^{r_N}r_N\eta_{\lfloor N/4\rfloor}
$$
主控并趋零。

在 §7 的情形，
$$
\log A_N\le
K_0N^2+(D+1)r_N\log^+\rho_N^{-1}+C_Mr_N+C.
$$
而 $\log^+\rho_N^{-1}=O(N)$。
因此
$$
\limsup\frac{\log A_N}{r_N^4}\le K_0\theta^2.
$$
取固定小 $\theta$ 后，(4.6) 趋零。
§6.1 的成本只有 $O(N^{3/2})$，同样可付；
§6.2 的双池成本已由 (6.9) 另付。

对同一核块内的 $f,g$，完整原空间配对给
$$
\mathcal B(D_0T_\lambda^{r_N}\mathcal V_Nf,g)
=
(-1)^{r_N}
\mathcal B((\operatorname{ad}_{T_\lambda}^{r_N}D_0)\mathcal V_Nf,g).
$$
所有词都在 (4.4) 的真实深域中合法。
不要求 $CM=M$。
由非零弱极限及局部四次衰减，
$$
\mathcal B(D_0f,g)=0
$$
对全部局部全矩阵成立，其不可约性迫该块为零。
小尾分支可直接排整个 $M$；
双池分支逐个排除 (3.9) 的全部有限根块。
所以 $\ker T_\lambda=0$。

完整 $C$ 自伴性给稠密像，
(3.5) 的真实循环图核心继而证明 (2.3)。
定理得证。

## 9. 一个真正非线性的不可约耦合例

取
$$
F(U,V)=U^3+(1+U)V+V^2.
\tag{9.1}
$$
它关于 $U$ 的最高系数为1，且
$$
F(U,0)=U^3,\qquad
F_U(U,0)=3U^2,\qquad
F_V(U,0)=1+U.
$$
两个偏导在 $V=0$ 上没有共同零点，所以
$$
\mathcal E_F=\varnothing.
$$
这也是一个不可约二变量多项式：
把它视为关于 $V$ 的首一二次式，其判别式
$$
(1+U)^2-4U^3
$$
为三次，不能是 $\mathbb C[U]$ 中的平方。

其准确共振符号为
$$
\begin{aligned}
\mathfrak F_F={}&
F_3^a+v+uv+2\sum_j a_jc_j(\chi_j-1)\\
&+v^2+2\sum_jc_j^2(\chi_j-1),
\end{aligned}
\tag{9.2}
$$
其中
$$
F_3^a=u^3+6u\sum_j a_j^2(\chi_j-1)
+8\sum_j a_j^3(\chi_j-1).
$$

故任意满足 (1.1)、(2.1) 的行，特别是任意
$a\in\ell^2\setminus\ell^1$，
对于每个 $\lambda\in\mathbb C$ 及每个复 $\ell^2$ 指数权都有
$$
\boxed{(\mathfrak F_F-\lambda)e^w\text{ 循环}.}
\tag{9.3}
$$
可以令所有最早主位的辅助为零，再从任意有限阈值后取
$c_j=\beta|a_j|^\kappa\omega_j$，其中 $\beta\ne0$、$|\omega_j|=1$。
此时首位字符切片在 $\lambda=0$ 仍具有共同临界根；
单靠旧首位切片互素准则不能处理该值。
本文的真实双行机制支付了它。

(9.2) 含 $uv$ 与 $v^2$，不是原单主行共振多项式加一个线性辅助。
也不是未经修正的 $u^3+(1+u)v+v^2$；
全部混合和纯辅助修正均明确保留。

## 10. 更一般的实际尾矩条件

保留 §§1–9 的 $\kappa>2$ 主定理，另有如下严格加强。

**推论 2（一个更低的可和幂）。**
把 (1.1) 中的指数条件改为
$$
\kappa>1,
$$
并另假设存在固定实数 $t$，使
$$
\boxed{
0<t<\kappa,\qquad
S_t:=\sum_j|a_j|^t<\infty.
}
\tag{10.1}
$$
主行仍须属于 $\ell^2$，保留 (2.1)、主行零位条件和所有有限例外规定。
则定理 1 的全部结论仍成立。

证明中唯一需要改变的是 (5.5)：
$$
\begin{aligned}
\left\|\sum_{j\notin H_N}|c_j|W(N_j)\right\|
&\le C\sum_{n>(K+2)N}\rho_n^\kappa\\
&\le C S_t\,\rho_{(K+2)N}^{\kappa-t}\\
&\le C S_t e^{-(\kappa-t)N^{3/2}}.
\end{aligned}
\tag{10.2}
$$
这仍压过全部固定公共半径 $\epsilon\rho_N^D$。
其余步骤只需要以下已有输入：

- $\ell^2$ 给首次降幅和真实高位 jets；
- $\kappa>1$ 给比值 $c_j/a_j\to0$ 及两个幅度带的比值分离；
- (10.1) 给 (10.2) 与 $c\in\ell^1$；
- (2.1) 给 $\log^+\rho_N^{-1}=O(N)$ 的种子传播。

因此全部自然域、结果式、一次联合预解和局部四次成本不变。
$t<1$ 时只使用正数 $S_t$，没有把相应序列空间误当成 Banach 空间。

### 10.1 对前一线性辅助二分的直接推论

取
$$
F(U,V)=q(U)+V
$$
时，$F_V(\mu,0)=1$，所以 (2.2) 对全部 $\lambda$ 自动成立。
于是前一篇线性辅助二分定理也得到明确推论：
$$
\boxed{
\begin{gathered}
a,b\in\ell^2,\quad
\liminf_n\log^+\rho_n^{-1}/n<\infty,\\
\kappa>1,\quad \exists\,0<t<\kappa:\sum_j|a_j|^t<\infty,\\
c_-|a_j|^\kappa\le|c_j|\le c_+|a_j|^\kappa
\text{ 于全部充分高物理位}
\end{gathered}
\Longrightarrow
[F_q+v_c-\lambda]e^w\text{ 对全部固定 }q,\lambda\text{ 循环}.
}
\tag{10.3}
$$
主行零位上的辅助仍须最终为零，有限低头例外仍任意。
当 $a\notin\ell^1$ 时，指数子序列条件仍自动成立。

这允许一些 $\kappa\in(1,2]$ 的不规则行。
它不宣称任意 $\ell^2$ 行都满足某个 $t<\kappa$ 的幂可和条件；
特别是 $\kappa=2$ 而只知 $\ell^2$ 时，(10.2) 不能偷换成带正指数的小尾。
此前已发表的 $\kappa>2$ 版本保持原文，不需据此改写其假设。

## 11. 没有被外推的范围

1. 主行若没有 (2.1) 的指数下界子序列，仍须验证原双池或实际小尾预算。
   可和极快临界行没有因此自动关闭。
2. 主行零位上的无限不受控辅助尾不满足 (1.1)，
   不能使用 (5.5)。
3. (2.2) 允许主偏导为零，但不允许该纤维点的两个偏导同时为零。
   后一情形的结果式可以恒有零常数项，本文不称其为实际单位。
4. 真实最高主系数单位来自 (1.2)、(3.6)，不能只说总次数非零就省略它。
5. 所有混合 $G_{r,s}$ 都有明确的局部至少二阶消去。
   一般任意 $\mathcal G$ 系数的 gauge 差未必没有一次项，不能直接照搬 (4.2)。
6. 全部核内逆先作用，再施最左反射。
   未从全空间单射稠密性推断任意未知限制的稠密像。
7. 这里是一个闭主 first 加一个可和辅助行的双变量结构。
   任意多个独立无界慢模式不在本定理范围内。

## 12. 来源

- [非可和主行二分及全阶 Sylvester 源](2026-11-13-nonsummable-main-dichotomy-and-all-order-sylvester-joint-inverses-central-review.md)：
  指数种子首次降幅、主零位条件、真实任意物理头与一次联合预解。
- [全阶二位 Bézout 源](2026-11-13-all-order-resonant-two-site-bezout-and-derivation-budgets-central-review.md)：
  绝对系数预算、两次阶乘平均及四次局部配对。
- [R147 慢辅助附录](../results/R147-appendix-bounded-slow-auxiliary-slices-and-polynomial-cyclicity.md) §3：
  全部真实混合 Bell jets、最高主系数及自然域。
- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  最高系数单位的闭自然域、核内有界化、完整 $C$ 自伴与图循环。
- [R270C](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) §10：
  单个位共振生成恒等式及局部二阶消去。
- [R154](../results/R154-supercubic-modes-all-polynomials-exponential-weights.md) 引理2.1：
  带统一有界真解析因子的实际快尾归属。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  最高真实物理位壳与完整导子代数。

新增步骤是全部混合共振修正的明确一次系数、
不同根块上的两种偏导单位、
固定 $(p,p)$ Sylvester 行列式及其 leading 因子，
以及把这些步骤与原二分、实际深域和四次配对完整接合。
