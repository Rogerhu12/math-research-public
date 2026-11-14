# R230 附录：有界近关系与变化源的定量压缩禁阻

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI 辅助：GPT-6 Astra Pro。root 全文核验并补乘积预算、近似生成及条件增长推论。

**状态：完整证明的实际源预算接口。**
在原正循环 $S$ 零商上，有界系数的近源关系迫每个系数强趋零。
这不是仅对固定候选源使用 WOT 紧性：
即使候选源随参数变化，只要它们由原有限源框架及真空以统一有界
实际交换子系数生成，就不能用统一有界系数把全部见证源压缩到
少于最小秩的源数。
本稿给出一个明确正误差下界，所需输入是低重放大中真实
$S$ 逼近的成本函数。这个成本函数已知有限，但尚无统一增长率。

全程使用实际 $\mathfrak C=A'$，不替换成纯有限块代数，
也不对任意右测试宣称此源生成条件自动成立。

## 1. 原正循环零商及低放大输入

沿用
[R228A](R228-appendix-minimal-witnesses-and-positive-quotient-orbits.md)
及
[最小秩有界模与两行共同域定理](R230-appendix-minimal-positive-rank-module-compression-and-pairwise-common-domains.md)
的固定对象：
$$
\rho=\sum_{j=1}^r f_j\otimes f_j,\qquad
r\ge2,\qquad
\tau=\operatorname{Tr}\rho>0,\qquad
x_j=Cf_j,\quad x=(x_j)_{j=1}^r.
$$
$r$ 是非零有限秩分离泛函的最小秩，也等于最小正秩。
原正泛函满足
$$
\phi(SF)=0\quad(F\in\mathfrak C),\qquad
\phi(F)=\langle F^{(r)}x,x\rangle.
$$
定义
$$
M=\overline{\mathfrak C^{(r)}x},\qquad
N=\overline{S^{(r)}M},\qquad Q=M\ominus N,
$$
$$
\pi(F)=P_QF^{(r)}|_Q.
\tag{1.1}
$$
于是
$$
x\in Q,\quad \|x\|=\sqrt\tau,\quad
\pi(S)=0,\quad
\|\pi(F)\|\le\|F\|,
\tag{1.2}
$$
且 $x$ 对 $\pi(\mathfrak C)$ 循环。

本稿反复使用的真实低放大事实是：
若 $k<r$ 且 $Y\subset H^{(k)}$ 闭、对角 $\mathfrak C$ 不变，则
$$
\overline{S^{(k)}Y}=Y.
\tag{1.3}
$$
否则 $Y\ominus\overline{S^{(k)}Y}$ 中的非零向量
产生秩至多 $k$ 的正见证，与最小性矛盾。
这里没有用未证明的正常尾衰减率。

记 $E_i:H^{(r)}\to H^{(r-1)}$ 为删除第 $i$ 坐标。
对 $\varepsilon>0$ 定义
$$
\boxed{
\mathcal C_i(\varepsilon)
=\inf\left\{1+\|SF\|:
F\in\mathfrak C,\
\|(I-S^{(r-1)}F^{(r-1)})E_ix\|\le\varepsilon
\right\}.
}
\tag{1.4}
$$
由 (1.3) 作用于
$Y_i=\overline{\mathfrak C^{(r-1)}E_ix}$，
先在 $Y_i$ 中用 $S$ 逼近 $E_ix$，
再用单个轨道向量逼近所选原像，得到
$$
1\le\mathcal C_i(\varepsilon)<\infty.
\tag{1.5}
$$
令
$$
\mathcal C(\varepsilon)=\max_{1\le i\le r}\mathcal C_i(\varepsilon).
\tag{1.6}
$$
这是固定见证的实际低放大源成本；
(1.5) 本身不提供 $\varepsilon\downarrow0$ 时的速率。

## 2. 有界近源关系的定量系数提取

取任意 $T_1,\ldots,T_r\in\mathfrak C$，令
$$
M_T=\max_j\|T_j\|,\qquad
e=\sum_{j=1}^rT_jx_j.
$$
则对每个 $i$ 及任意 $\varepsilon>0$，
$$
\boxed{
\|\pi(T_i)x\|
\le\sqrt r\,M_T\varepsilon
+\mathcal C_i(\varepsilon)\|e\|.
}
\tag{2.1}
$$

定义有界插入矩阵
$$
(J_i u)_i=-\sum_{j\ne i}T_ju_j,\qquad
(J_i u)_j=T_i u_j\quad(j\ne i).
\tag{2.2}
$$
Cauchy--Schwarz 给
$$
\|J_i\|^2
\le (r-1)M_T^2+M_T^2=rM_T^2.
\tag{2.3}
$$
与准确源关系的情形不同，这次
$$
T_i^{(r)}x=J_iE_ix+\iota_i e,
\tag{2.4}
$$
其中 $\iota_i:H\to H^{(r)}$ 把向量插入第 $i$ 坐标。
所有矩阵项都属于交换代数，故
$J_iF^{(r-1)}=F^{(r)}J_i$。

选择满足 (1.4) 约束的 $F$。
因为 $T_i^{(r)}x\in M$，
$S^{(r)}F^{(r)}T_i^{(r)}x\in N$。
利用 (2.4)，
$$
\begin{aligned}
\|\pi(T_i)x\|
&=\operatorname{dist}(T_i^{(r)}x,N)\\
&\le\|(I-S^{(r)}F^{(r)})T_i^{(r)}x\|\\
&\le\|J_i\|\,\|(I-S^{(r-1)}F^{(r-1)})E_ix\|\\
&\quad +(1+\|SF\|)\|e\|\\
&\le\sqrt r\,M_T\varepsilon+(1+\|SF\|)\|e\|.
\end{aligned}
$$
对这些 $F$ 取下确界就得 (2.1)。
即使下确界未取得，前一项与 $F$ 无关，故取下确界合法。

### 2.1 统一有界近关系的强极限

若
$$
\sup_n\max_j\|T_{j,n}\|<\infty,\qquad
\sum_jT_{j,n}x_j\longrightarrow0
\quad\text{于 }H,
\tag{2.5}
$$
则
$$
\boxed{\pi(T_{j,n})\longrightarrow0
\quad\text{于 }Q\text{ 的强算子拓扑，逐个 }j.}
\tag{2.6}
$$
先固定 $\varepsilon$，在 (2.1) 中令 $n\to\infty$，
再令 $\varepsilon\downarrow0$，得到
$\pi(T_{j,n})x\to0$。
由于商代数交换，
$$
\pi(T_{j,n})\pi(F)x=\pi(F)\pi(T_{j,n})x\to0.
$$
$x$ 的商轨道稠密，且这些商算子范数统一有界；
因此结论扩展到每个 $Q$ 向量。
这个次序不要求 $\mathcal C_i(\varepsilon)$ 有统一速率。

(2.6) 只针对真正的有界系数近源关系，
不是从 $\phi(T_{j,n})\to0$ 推出商算子强趋零。

## 3. 如何合法加入真空项

本节再假设已有两个所选原源乘子的广义预解，
从而前述两行定理在同一个原 $Q$ 上给出
$$
\pi(R_a)=0,\qquad
\pi(D_a)^{-1}=\pi(U_a)
\tag{3.1}
$$
其中 $a$ 是其中任意一行，且
$$
R_a,D_a,U_a\in\mathfrak C,\qquad
D_a1=R_ax_a.
\tag{3.2}
$$
其余行无需预解数据。
固定这一个 $a$，以下简写 $R=R_a,D=D_a,U=U_a$。

取有界系数
$$
e=\sum_{j=1}^rT_jx_j+B1,\qquad
M_T=\max_j\|T_j\|,\quad M_B=\|B\|.
$$
由 (3.2)，
$$
De
=\sum_{j=1}^r\left(DT_j+\delta_{ja}BR\right)x_j.
\tag{3.3}
$$
这是原 $H$ 上的实际有界向量等式。
对右侧用 (2.1)，其最大系数范数不超过
$$
M'=\|D\|M_T+\|R\|M_B.
$$
在商上，
$$
\pi(DT_j+\delta_{ja}BR)=\pi(D)\pi(T_j)
$$
因为 $\pi(R)=0$。
再左乘 $\pi(U)$，得到
$$
\boxed{
\|\pi(T_j)x\|
\le\|U\|\left[
\sqrt r\,(\|D\|M_T+\|R\|M_B)\varepsilon
+\|D\|\,\mathcal C_j(\varepsilon)\|e\|
\right].
}
\tag{3.4}
$$

所以在 $T_{j,n},B_n$ 统一有界、
$\sum_jT_{j,n}x_j+B_n1\to0$ 时，
仍有
$$
\pi(T_{j,n})\longrightarrow0
\quad\text{强算子拓扑}.
\tag{3.5}
$$
没有对 $\pi(B_n)$ 作此结论。
真空项的消去靠的是 (3.1)--(3.3)，
不把真空擅自当作 $M$ 或 $Q$ 中的一个坐标向量。

## 4. 变化源的定量重构问题

取任意整数 $1\le k<r$。
允许候选源 $g_1,\ldots,g_k$ 依赖当前参数，写为
$$
g_\ell=B_{\ell0}1+\sum_{j=1}^rB_{\ell j}x_j,
\qquad B_{\ell j}\in\mathfrak C.
\tag{4.1}
$$
允许任意复系数及任意实际有界交换子。
再取 $A_{i\ell}\in\mathfrak C$，试图重构全部原源：
$$
\widehat x_i=\sum_{\ell=1}^kA_{i\ell}g_\ell,\qquad
\delta=\max_i\|x_i-\widehat x_i\|.
\tag{4.2}
$$
定义预算
$$
a=\max_{i,\ell}\|A_{i\ell}\|,\qquad
b=\max_{\ell,\,0\le j\le r}\|B_{\ell j}\|,\qquad
L=kab.
\tag{4.3}
$$
两侧矩阵可以随参数完全改变；
$g_\ell$ 本身也不要求有任何紧性、固定块或固定相位。

令
$$
m_{ij}=\sum_{\ell=1}^kA_{i\ell}B_{\ell j},\qquad
c_i=\sum_{\ell=1}^kA_{i\ell}B_{\ell0}.
\tag{4.4}
$$
于是
$$
\|m_{ij}\|\le L,\quad \|c_i\|\le L,\qquad
x_i-\widehat x_i
=\sum_{j=1}^r(\delta_{ij}I-m_{ij})x_j-c_i1.
\tag{4.5}
$$
把 (3.4) 用于每一行，
$$
\boxed{
\max_{i,j}\|\pi(\delta_{ij}I-m_{ij})x\|
\le\|U\|\left[
\sqrt r\,(\|D\|+\|R\|)(1+L)\varepsilon
+\|D\|\,\mathcal C(\varepsilon)\delta
\right].
}
\tag{4.6}
$$
这里用了
$\|D\|(1+L)+\|R\|L\le(\|D\|+\|R\|)(1+L)$。

## 5. 交换矩阵的行列式给出正误差下界

矩阵 $\mathbf m=(m_{ij})$ 通过 $k<r$ 个中间列因式分解：
$$
\mathbf m
=(A_{i\ell})_{\substack{1\le i\le r\\1\le\ell\le k}}
 (B_{\ell j})_{\substack{1\le\ell\le k\\1\le j\le r}}.
$$
所有条目在同一个交换代数中，所以
$$
\det\mathbf m=0.
\tag{5.1}
$$
这不依赖域上的矩阵秩理论：
按列多重线性展开行列式，
每项从 $k$ 个中间列选取 $r$ 列，
必有重复列，故其交替行列式为零。

在商代数中记
$$
\mathbf E=(\pi(m_{ij})-\delta_{ij}I_Q).
$$
则
$$
\det(I_r+\mathbf E)=0.
\tag{5.2}
$$
展开为非空主子式，
$$
-I_Q=\sum_{\varnothing\ne J\subseteq\{1,\ldots,r\}}
            \det\mathbf E_{J,J}.
\tag{5.3}
$$
每个条目范数至多 $1+L$。
记
$$
d=\max_{i,j}\|\mathbf E_{ij}x\|.
$$
一个长度 $s$ 的行列式单项，利用条目交换，把任意一个条目
移到最右作用于 $x$，其余 $s-1$ 项以算子范数估计；
故其向量范数至多 $(1+L)^{s-1}d$。
(5.3) 因此给
$$
\begin{aligned}
\sqrt\tau=\|x\|
&\le\sum_{s=1}^r\binom rs s!(1+L)^{s-1}d\\
&\le3r!(1+L)^{r-1}d.
\end{aligned}
\tag{5.4}
$$
最后一式来自
$\binom rs s!=r!/(r-s)!$ 及
$\sum_{t=0}^{r-1}1/t!<3$。

将 (4.6) 代入 (5.4)：
$$
\boxed{
\begin{aligned}
\sqrt\tau
\le {}&3r!(1+L)^{r-1}\|U\|\\
&\times\left[
\sqrt r\,(\|D\|+\|R\|)(1+L)\varepsilon
+\|D\|\,\mathcal C(\varepsilon)\delta
\right].
\end{aligned}
}
\tag{5.5}
$$
$\pi(D)$ 可逆，故 $\|D\|>0$；$\|U\|>0$ 也成立。

具体选择
$$
\boxed{
\varepsilon_L
=\frac{\sqrt\tau}
 {6r!\sqrt r\,\|U\|(\|D\|+\|R\|)(1+L)^r}.
}
\tag{5.6}
$$
(5.5) 中第一项等于 $\sqrt\tau/2$，所以
$$
\boxed{
\delta\ge
\frac{\sqrt\tau}
 {6r!\,\|U\|\|D\|(1+L)^{r-1}\,
  \mathcal C(\varepsilon_L)}
>0.
}
\tag{5.7}
$$

这是固定真见证的实际源预算下界。
它同时允许候选源、生成系数和重构系数改变，
不只处理固定的 $g_\ell$。

## 6. 几个准确推论

### 6.1 统一预算不可能渐近压缩

若 $k<r$ 固定，(4.1)--(4.2) 随 $n$ 改变，
只须乘积 $L_n=k a_n b_n$ 统一有界；不要求 $a_n,b_n$ 各自统一有界。
在 (5.5) 中可直接用统一上界 $\overline L$ 选择同一个正
$\varepsilon_{\overline L}$，
得到一个与 $n$ 无关的正误差下界。
因此
$$
\max_i\left\|x_i-\sum_{\ell=1}^kA_{i\ell,n}g_{\ell,n}\right\|
\not\longrightarrow0.
\tag{6.1}
$$

也可用 §3 的强极限表述：
若该误差趋零，则
$$
\pi(m_{ij,n})\longrightarrow\delta_{ij}I_Q
$$
强收敛且统一有界。
有限个统一有界强收敛算子的乘积也强收敛，
所以行列式强趋 $I_Q$，与每个行列式恒零矛盾。
(5.7) 额外给出了显式误差下界。

进一步，若重构误差确实趋零，则必有 $L_n\to\infty$。
否则存在 $L_n$ 有界的无限子列，上述同一正下界即给矛盾。
因此这里得到趋于无穷，而不只是预算无界。

### 6.2 不含真空项时不需要任何预解数据

若所有 $B_{\ell0}=0$，
直接以 (2.1) 代替 (3.4) 即可。
此时无需 (3.1)，也无需原源乘子的任何预解数据。
具体地，取
$$
\varepsilon_L^{\,0}
=\frac{\sqrt\tau}{6r!\sqrt r\,(1+L)^r},
$$
得到
$$
\boxed{
\delta\ge
\frac{\sqrt\tau}
 {6r!(1+L)^{r-1}\mathcal C(\varepsilon_L^{\,0})}.
}
\tag{6.2}
$$
所以即使只在原 $r$ 个源的统一有界代数模中重选候选源，
也不能近似降低所需源数。

### 6.3 从有限组原逆源产生的候选也有此预算

每个已给的原广义预解逆源满足
$$
g_i=U_ix_i+B_i1.
$$
若候选源由有限个这样的 $g_i$ 及 $1$
经统一有界的实际交换子系数生成，
把此式代入就得到 (4.1)，其系数仍统一有界。
因此只要两行预解已经给出 §3 的商单位数据，
(5.7) 适用于这种变化的逆源混合。
它不把正则器之和的逆误认为逆源之和，
也不假定任意右因子都有这种有限源生成方式。

### 6.4 候选源只近似生成时的准确误差

允许实际候选 $g_\ell$ 不严格满足 (4.1)，只要求
$$
\epsilon_{\rm gen}
=\max_\ell\left\|g_\ell-B_{\ell0}1
              -\sum_{j=1}^rB_{\ell j}x_j\right\|.
$$
记实际重构误差为
$$
\delta_{\rm rec}
=\max_i\left\|x_i-\sum_{\ell=1}^k A_{i\ell}g_\ell\right\|.
$$
将 $g_\ell$ 换成准确生成的
$g_\ell^0=B_{\ell0}1+\sum_jB_{\ell j}x_j$，
逐行三角不等式给
$$
\max_i\left\|x_i-\sum_{\ell=1}^kA_{i\ell}g_\ell^0\right\|
\le\delta_{\rm rec}+ka\,\epsilon_{\rm gen}.
$$
所以 (5.7) 的右端也是
$\delta_{\rm rec}+ka\,\epsilon_{\rm gen}$ 的下界。
没有真空项时，同样以 (6.2) 的右端为下界。
生成误差必须乘重构系数成本，不能只按其未经放大的大小比较。

## 7. 增长预算与尚未支付的成本

若 $L=L_n\to\infty$，(5.7) 仍逐项成立，
但 $\mathcal C(\varepsilon_{L_n})$ 的增长尚未估计。
因此不能仅凭本稿说
$\exp(O(q^2))$ 或 $\exp(O(q^3))$ 的源预算已经被排除。
也不能把 R235 的极小实际 carry 误差直接与一个未知成本相抵消。

本稿把需要进一步证明的量准确隔离为
$$
\mathcal C_i(\varepsilon):
\quad
\text{在固定低放大循环空间中，用实际 }SF
\text{ 逼近 }E_ix\text{ 的成本}.
$$
只要某条具体构造给出这些成本与自身系数预算的相容估计，
(5.5)--(5.7) 就可以直接核验其是否可能实现源压缩。
目前只完成了有限性、准确系数提取及统一预算排除，
没有证明一般正常态不存在，也没有达到普通 Hilbert ISP 的完成标准。


### 7.1 与四次幂误差的一个条件性比较

这只是用于检验后续构造的推论，不给未知见证的成本上界。
假设某个具体构造额外证明，对充分小的 $\varepsilon$，
$$
\mathcal C(\varepsilon)
\le \exp\!\left[K(1+\log(1/\varepsilon))^\gamma\right],
\qquad \gamma>0.
$$
由 $\varepsilon_L=c(1+L)^{-r}$ 和 (5.7)，存在依固定见证、
预解数据及 $K,\gamma$ 的正数 $c_1,C_1$，使有效误差满足
$$
\delta_{\rm rec}+ka\,\epsilon_{\rm gen}
\ge c_1\exp\!\left[-C_1\{
1+\log(1+L)+(1+\log(1+L))^\gamma\}\right].
\tag{7.1}
$$
若同一构造又有 $L_q\le\exp(Cq^3\log q)$ 且 $\gamma<4/3$，
则右端为 $\exp[-o(q^4)]$，不能同时有
$\delta_{\rm rec}+ka\,\epsilon_{\rm gen}\le\exp(-cq^4)$。
在 $\gamma=4/3$ 时，上述预算带来额外 $\log^{4/3}q$，
不能据此判冲突；若另有 $L_q\le\exp(Cq^3)$，临界情形仍须比较常数。
这里没有证明实际 R235 右测试必有该生成形式或满足任一成本增长假设。

## 8. 低放大成本的交叉不等式与必要发散率

本节只用 §§1--2 的原正循环零商及成本定义，
不要求任何原源乘子具有广义预解。

### 8.1 两个删除方向的准确交叉不等式

对任意不同的 $i,j$ 及任意 $\varepsilon,\eta>0$，
$$
\boxed{
\sqrt\tau
\le \sqrt r\,\mathcal C_i(\varepsilon)\eta
   +\mathcal C_j(\eta)\varepsilon.
}
\tag{8.1}
$$

证明如下。固定 $\kappa>0$，按 $\mathcal C_i(\varepsilon)$
的下确界定义取 $F_i\in\mathfrak C$，使
$$
\|(I-S^{(r-1)}F_i^{(r-1)})E_ix\|\le\varepsilon,\qquad
1+\|SF_i\|\le\mathcal C_i(\varepsilon)+\kappa.
$$
记 $T=SF_i$。
因 $j\ne i$，第 $j$ 个源仍在被保留的删除框架中，故
$$
\|(T-I)x_j\|\le\varepsilon.
\tag{8.2}
$$
把只有第 $j$ 个系数非零、该系数为 $T-I$ 的近源关系
代入 (2.1)，并用参数 $\eta$。
$\pi(S)=0$ 使
$$
\pi(T-I)=-I_Q,\qquad
\|\pi(T-I)x\|=\sqrt\tau.
$$
而 $\|T-I\|\le1+\|T\|\le\mathcal C_i(\varepsilon)+\kappa$。
所以
$$
\sqrt\tau
\le\sqrt r\,[\mathcal C_i(\varepsilon)+\kappa]\eta
   +\mathcal C_j(\eta)\varepsilon.
$$
令 $\kappa\downarrow0$ 就是 (8.1)。
下确界不需要取得，也没有同时改变原见证或两个删除空间。

### 8.2 每个单独成本都发散

对每个 $i$，
$$
\boxed{\mathcal C_i(\varepsilon)\longrightarrow\infty
\qquad(\varepsilon\downarrow0).}
\tag{8.3}
$$
若存在 $\varepsilon_n\downarrow0$，
使 $\mathcal C_i(\varepsilon_n)\le K<\infty$，
任选 $j\ne i$，固定足够小的 $\eta>0$ 使
$\sqrt r K\eta<\sqrt\tau/2$。
(1.5) 保证 $\mathcal C_j(\eta)$ 是固定有限数。
在 (8.1) 中令 $\varepsilon=\varepsilon_n$ 并取极限，
便得 $\sqrt\tau\le\sqrt\tau/2$，矛盾。

等价地，如果 $SF_n$ 在原 $H$ 上的算子范数统一有界，
且 $SF_nE_ix\to E_ix$，
则 (8.2) 给一个统一有界的单坐标近源关系。
(2.6) 会迫 $\pi(SF_n-I)\to0$ 强收敛，
但这些商算子恒等于 $-I_Q$。
这说明不能给任何一个删除方向免费使用有界输出近单位。

### 8.3 最大成本的明确倒数下界

在 (8.1) 中取 $\eta=\varepsilon$，
$$
\sqrt r\,\mathcal C_i(\varepsilon)
+\mathcal C_j(\varepsilon)
\ge \frac{\sqrt\tau}{\varepsilon}
\qquad(i\ne j).
\tag{8.4}
$$
因此
$$
\boxed{
\mathcal C(\varepsilon)=\max_i\mathcal C_i(\varepsilon)
\ge\frac{\sqrt\tau}{(\sqrt r+1)\varepsilon}.
}
\tag{8.5}
$$
更准确，对每个固定 $\varepsilon$，
把 $r$ 个成本从小到大排序，第二小者已至少等于
$\sqrt\tau/[(\sqrt r+1)\varepsilon]$：
把最小与第二小的两个索引放进 (8.4) 即可。
所以至多一个删除方向能低于这个倒数门槛。

本节**没有**证明每个单独 $\mathcal C_i$ 都满足 (8.5)；
单独的普遍结论是 (8.3)，以及每一对的 (8.1)。

### 8.4 若纯幂上界存在，其指数必须互补

假设某两个不同的方向存在常数 $A_i,A_j>0$、
$\beta_i,\beta_j\ge0$，对充分小的正参数有
$$
\mathcal C_i(\varepsilon)\le A_i\varepsilon^{-\beta_i},
\qquad
\mathcal C_j(\eta)\le A_j\eta^{-\beta_j}.
\tag{8.6}
$$
由 (8.3)，两指数必须严格正。
选固定
$$
c=\frac{\sqrt\tau}{2\sqrt r\,A_i},\qquad
\eta=c\varepsilon^{\beta_i}.
$$
此时 $\eta\downarrow0$，故两端的上界都适用。
(8.1) 给
$$
\frac{\sqrt\tau}{2}
\le A_jc^{-\beta_j}
       \varepsilon^{\,1-\beta_i\beta_j}.
$$
若 $\beta_i\beta_j<1$，右端趋零，矛盾。
因此
$$
\boxed{\beta_i\beta_j\ge1\qquad(i\ne j)}
\tag{8.7}
$$
对任何这样已实际证明的两端纯幂上界成立。
特别，同一纯幂上界 $O(\varepsilon^{-\beta})$
若覆盖所有删除方向，就必须有 $\beta\ge1$。

同样，§7.1 的对数幂指数假设若与 (8.5) 相容，
必须有 $\gamma\ge1$；
当 $\gamma=1$ 且按该节形式用同一个常数 $K$ 时，
还须 $K\ge1$。
所以那条四次幂误差比较中尚可能相容的次临界指数范围是
$1\le\gamma<4/3$，并非已经构造了这个范围内的上界。

本节给出的都是成本的必要下界和两方向的制约。
它没有提供任何 $\mathcal C_i$ 上界，
没有补齐增长源预算与实际 carry 的相容构造，
也没有排除原最小正见证。


### 8.5 正交坐标乘积给出的更强交叉式

前述结论还可用原正商与两个删除方向直接加强。
按定义取 $T_i,T_j\in S\mathfrak C$，分别在 $E_i x,E_j x$
上有误差至多 $\varepsilon,\eta$，
且 $1+\|T_i\|\le\mathcal C_i(\varepsilon)+\kappa$、
$1+\|T_j\|\le\mathcal C_j(\eta)+\kappa$。
令 $P=(I-T_i)(I-T_j)$。交换性及 $\pi(S)=0$ 给
$\pi(P)=I_Q$，所以
$$
\|P^{(r)}x\|^2\ge\|P_QP^{(r)}x\|^2=\tau.
$$
第 $i$ 坐标由 $T_j$ 的逼近控制，而其余坐标由 $T_i$ 的逼近控制：
$$
\|Px_i\|\le(\mathcal C_i(\varepsilon)+\kappa)\eta,\qquad
\|P^{(r-1)}E_ix\|\le(\mathcal C_j(\eta)+\kappa)\varepsilon.
$$
两部分在 $H^{(r)}$ 中正交。平方相加并令 $\kappa\downarrow0$，得到
$$
\boxed{\tau\le
\mathcal C_i(\varepsilon)^2\eta^2+
\mathcal C_j(\eta)^2\varepsilon^2\qquad(i\ne j).}
\tag{8.8}
$$
于是对每个固定 $\varepsilon>0$，第二小的删除成本至少为
$\sqrt\tau/(\sqrt2\,\varepsilon)$；
这是 (8.5) 的常数锐化，不是每个方向各自的倒数下界。
本证明仍未使用预解数据，也未给成本增长上界。
