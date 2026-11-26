# R946 — 原四长窗的锐利十倍根能量与完整线性成本

日期：2026-11-26。**状态：以下目标素数内、原完整来源上的四长窗必要界已证明。** 本篇接 R943 的真实五块评价，给
$$
10q(H-r)\le3\mathcal B_D^2+80D.
\tag{1}
$$
所有因子都来自同一个原截面，所有重数均保留；无需重数上界或高重数截除门。十为该局部根能量的最佳常数。原五块的四条十三行带、完整来源帽及共同单位均不变。

在旧三长维数尺度中，如果同一候选确实又通过了第四条真实长行，(1) 排除所有 charge 差公因子 $q\ge2$。在五块自身的四长自然临界中，它只排除 $q\ge3$，仍留稠密 $q=1,2$。这些是全候选必要界，不把第五中央条件免费改成深核或无穷非零。

## 1. 原完整来源、实际长度与明确次数门

沿 [R837](R837-original-three-long-root-energy-and-uniform-multiplicity-truncation.md) 的同一个 canonical 格
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},\qquad
\mathcal E=Y\partial_Y,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad
C_n=\lfloor n/2\rfloor,
$$
$$
f_D=\lfloor9D/2\rfloor+4<p,\qquad
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{2}
$$
不把新 $W_{178}$、独立倍点列或免费角乘子加入这个格。

设 $p=6s-1>211$。使用 R943 原
$\Gamma_{4s+\ell+13}^{(5)}$，$1\le\ell<s-13$。
对非零约化候选 $\bar P\in\mathcal W_D$，置
$$
\widehat P=d^{C_D}\bar P,\quad
r=\operatorname{ord}_t\widehat P,\quad
M_D=f_D+C_D=5D+4-(D\bmod2).
$$
原全部帽给
$$
\deg_t\widehat P\le M_D,\qquad
\deg_Y\widehat P\le D<p.
\tag{3}
$$
两种真实使用范围分别为
$$
(\Delta,H)=
\begin{cases}
(0,s),&\bar P\in\ker\bar J_5,\\
(13,s-13),&\bar P\in\ker\bar M_5^{\rm orig}.
\end{cases}
\tag{4}
$$
R943(67)–(71) 的完整单位、四十 charge 和 $t/w$ 下三角运输给
$$
(\mathcal E^i\widehat P)(t,g)\in t^Hk[[t]],
\qquad i=0,1,2,3.
\tag{5}
$$
第五行仍只有原短长度；本篇不扩它。四条十三行跨界带的固定成本52没有删除。

若已给原物理 $M_5$ 的 primitive 模 $p^2$ 或更深右核，原 $m_{13}$ 的 Smith 因子仅为单位或一次 $p$，故
$m_{13}J_5(P)\in p^2$ 迫 $J_5(P)\in p$；此时可用 (4) 的 $\Delta=0$。
这只是该已存在深核的必要条件，不从中央零构造此深核。

$t=0$ 处只有 $n=0,1,2$ 的原列可非零。前三个常数 Euler 行的单位 Vandermonde 因而给 $r\ge1$。由 (3)，$r\le M_D$。
$r\ge H$ 时立即有 $p\le6(M_D+\Delta)-1$；
以下取
$$
S=H-r>0.
\tag{6}
$$
除去真实 $t^r$ 后，四个长零都读到 $S$，且 $S\le s$。若来源只有一个非零 charge，$g$ 为单位使其函数值的阶恰为 $r$，与 $r<H$ 矛盾；因此当前非平凡情形的 charge 差公因数确为正且不超过 $D$。
$g$ 只需原模 $t^s$ 低轴；所有接触均在 $s$ 截断，不在特征 $p$ 中延长完整 sigma 连接。

若非零 charge 支持落在一个模 $q$ 类，
$1\le q\le D<p$，则原恒等式
$$
\widehat P(t,\zeta Y)=\zeta^{n_*}\widehat P(t,Y)
\quad(\zeta\in\mu_q)
\tag{7}
$$
把同一四行送到 $q$ 个互异原单位点 $(0,\zeta)$。
$q$ 始终是这个同一候选的实际 charge 差公因子或其一个除数，不是可任选的目标数量。

## 2. 实重数权与全部初等集合不等式

对真实整数重数 $m\ge1$，定义
$$
c_m=\min(m^2,10m),\qquad\lambda_m=\sqrt{c_m}.
\tag{8}
$$
这些只是 Néron–Severi 实空间的交数权，绝不在剩余域开平方，不改变源多项式重数。准确有
$$
1\le\lambda_m\le m,\qquad c_m\le10m,\qquad
c_m\ge10(m-3)\quad(m\ge3).
\tag{9}
$$
最后一式在 $m\le10$ 化为 $(m-5)^2+5\ge0$，在 $m>10$ 显然。

对一组不同根的重数 $m_1,\ldots,m_a$，记 $M=\sum m_i$，
$$
\mathcal E_{\rm set}
=\sum_i c_{m_i}+6\sum_{i<j}\lambda_{m_i}\lambda_{m_j}.
$$
有下列精确下界：
$$
\begin{array}{c|c}
\text{条件}&\mathcal E_{\rm set}\text{ 的下界}\\ \hline
M\ge3&10(M-3)\\
a\ge2&10(M-2)\\
a\ge3\text{，或 }a\ge2,\ M\ge5&10(M-1)\\
a\ge4&10M.
\end{array}
\tag{10}
$$

证明先看存在某个 $m_b>10$ 的情形。该根的自项是 $10m_b$。
其余 $m_i>10$ 的自项各自已经支付 $10m_i$；
其余 $m_i\le10$ 的自项与它同 $b$ 的交叉项为
$m_i^2+6m_i\lambda_{m_b}\ge10m_i$，因为 $\lambda_{m_b}>10$。
所以此时甚至有 $\mathcal E_{\rm set}\ge10M$。

否则所有 $m_i\le10$，权就是原整数重数。若 $Q=\sum m_i^2$，
$$
\mathcal E_{\rm set}=3M^2-2Q.
$$
有 $a\ge j$ 时，$Q\le(M-j+1)^2+j-1$。
对 $j=2,3,4$，分别得
$M^2+4M-4$、$M^2+8M-12$、
$M^2+12M-24$。
它们与 (10) 所列下界之差分别为
$(M-3)^2+7$、
$M^2-2M-2$（$M\ge3$）、
$(M-4)(M+6)$。
$a\ge2,M\ge5$ 的第三行差为 $M^2-6M+6\ge1$。
第一行在 $a=1$ 由 (9)，在 $a\ge2$ 由第二行。证毕。

唯一最近简单根需要一个不同的、保留它全部交叉项的集合量：
$$
\mathcal G_{\rm set}
=\sum_i(c_{m_i}+6\lambda_{m_i})
 +6\sum_{i<j}\lambda_{m_i}\lambda_{m_j}.
$$
准确有
$$
\mathcal G_{\rm set}\ge10(M-1)\quad(a\ge1),\qquad
\mathcal G_{\rm set}\ge10M\quad(a\ge2).
\tag{11}
$$
若有重数 $>10$，刚才的证明已给更强的第一量 $\mathcal E_{\rm set}\ge10M$。
否则 $\mathcal G_{\rm set}=3M^2-2Q+6M$。
用 $Q\le M^2$，第一式差为
$M^2-4M+10=(M-2)^2+6>0$；
用 $a\ge2$ 时 $Q\le(M-1)^2+1$，第二式差为 $M^2-4\ge0$。
这证明 (11)，包括全部大重数情形。

最后记录截断时要用的系数式
$$
c_m+12\lambda_m\ge10m,\qquad
c_m+18\lambda_m\ge10m\quad(m\ge1).
\tag{12}
$$
$m\le10$ 时由 $m^2+12m\ge10m$，$m>10$ 时自项已足够。

## 3. 四个真实 jet 的十倍局部根引理

在 R837 的同一 tame 完成局部环中写
$$
f(t,Y)=U(t,Y)\prod_{i=1}^{a}(Y-\psi_i(t))^{m_i},
\quad U(0,1)\ne0,\quad\psi_i(0)=1,
\quad\sum_i m_i<p.
$$
$\psi_i$ 两两不同，局部单位的导数均整。取 $g_0(0)=1$，假定
$$
f(t,g_0),\quad f_Y(t,g_0),\quad
f_{YY}(t,g_0),\quad f_{YYY}(t,g_0)\in t^S,
\qquad0<S\le s.
\tag{13}
$$
原 Euler 四行与 (13) 通过单位下三角矩阵等价，因为 $g_0$ 为单位且 $2,6$ 在当前特征下可逆。

记
$$
h_i=\operatorname{ord}_t(\psi_i-g_0),\quad
\bar h_i=\min(h_i,s),\quad
d_{ij}=\operatorname{ord}_t(\psi_i-\psi_j),
$$
允许 $h_i=\infty$。定义
$$
\mathscr E_\lambda(f)=
\sum_i c_{m_i}\bar h_i+
6\sum_{i<j}\lambda_{m_i}\lambda_{m_j}d_{ij}.
\tag{14}
$$

**引理。**
$$
\boxed{\mathscr E_\lambda(f)\ge10S.}
\tag{15}
$$

### 3.1 全部接触严格小于 $s$

置
$H_f=\sum_i m_ih_i$、$w=\max h_i$。
每个活动高度 $x\in(0,w]$ 的根集为 $\{i:h_i\ge x\}$，总重数为 $M(x)$。
非阿基米德不等式 $d_{ij}\ge\min(h_i,h_j)$ 给
$$
\mathscr E_\lambda(f)
\ge\int_0^w\mathcal E_{\rm set}(\{h_i\ge x\})\,dx.
\tag{16}
$$
积分只是有理分段常数的实求和。以下按真正最近的不同根数穷尽分类。

**唯一最近根，重数 $m\ge3$。**
第三导数的最低项由该根被求导三次给出，系数
$m(m-1)(m-2)$ 非零；其余根及单位的求导严格较高。
故 $S\le H_f-3w$。
每个活动集有 $M(x)\ge3$，(10) 第一行和 (16) 给
$\mathscr E_\lambda\ge10(H_f-3w)\ge10S$。

**唯一最近根，重数 $m=2$。**
第二导数的最低项系数为2，给 $S\le H_f-2w$。
若一个活动集只有最近根，其能量4至少为 $10(M-2)=0$；
若还有别的根，由 (10) 第二行仍至少为 $10(M-2)$。
积分给 $10(H_f-2w)\ge10S$。

**唯一最近根，重数 $m=1$。**
这一情形不能仅把旧七倍引理改写成十。
以 $X=Y-g_0(t)$ 写
$$
f=(X-\alpha)U_1(t,X),\qquad v_t(\alpha)=w,
$$
其中 $U_1$ 含全部较远根和同一个整单位。
若没有较远根，$f_Y(t,g_0)$ 是单位，与 $S>0$ 矛盾。
否则设这些根的最大接触为 $v<w$，
$H_{\rm far}=\sum_{\rm far}m_ih_i=v_t(U_1(t,0))$。
原求导的完整前三式为
$$
f_Y=U_1-\alpha U_{1,Y},\quad
f_{YY}=2U_{1,Y}-\alpha U_{1,YY},\quad
f_{YYY}=3U_{1,YY}-\alpha U_{1,YYY}.
\tag{17}
$$
各导数至少满足
$v_t(U_1^{(j)}(t,0))\ge H_{\rm far}-jv$。
因此第一式的首项准确是 $U_1(t,0)$，
$$
H_{\rm far}\ge S.
\tag{18}
$$
这里没有把 $U_1$ 的三个 jet 无证都赋深 $S$；只使用 (17) 真正保证的领先条件。

若较远根有至少两个同为最近根，每个 $x\le v$ 的较远活动集至少含两个根。
最近简单根与每个较远根的交数准确为 $h_i$；
把它的这些交叉项并入较远能量，正得到 (11) 的 $\mathcal G_{\rm set}$。
故 (11)、(18) 给
$$
\mathscr E_\lambda(f)\ge
\int_0^v10M_{\rm far}(x)\,dx
=10H_{\rm far}\ge10S.
$$

若较远根恰有一个最近根，重数为 $m_0$，
$U_{1,Y}(t,0)$ 的最低项准确非零，阶为
$H_{\rm far}-v$，因为 $m_0<p$。
(17) 的第二式中另一项阶至少
$w+H_{\rm far}-2v>H_{\rm far}-v$，所以
$$
H_{\rm far}-v\ge S.
\tag{19}
$$
每个较远活动集非空，用 (11) 第一式积分得
$\mathscr E_\lambda(f)\ge10(H_{\rm far}-v)\ge10S$。
第三式完整保留在 (17) 中；上述两类只需它所处四 jet 假设中的前两条非平凡领先约束，未假装除线性因子后得到一个自由三 jet 来源。
这支付唯一最近简单根的全部重数和相消情形。

**恰有两个不同最近根。**
记其总重数为 $M_0=m_1+m_2$，首差为
$c_1t^w,c_2t^w$，$c_i\ne0$；允许 $c_1=c_2$。
若 $M_0\ge5$，至少一阶或二阶导数的领先系数非零：
若 $m_1/c_1+m_2/c_2=0$，则
$$
\frac{m_1}{c_1^2}+\frac{m_2}{c_2^2}
=\frac{m_1(m_1+m_2)}{m_2c_1^2}\ne0.
$$
$c_1=c_2$ 时第一和已非零。
因此 $S\le H_f-w$。每个活动集至少两根且总重数至少5，
由 (10) 第三行得到 $10(H_f-w)\ge10S$。

若 $2\le M_0\le4$，实际领先多项式
$Q(X)=(X-c_1)^{m_1}(X-c_2)^{m_2}$
的二阶或三阶导数在零点必非零。
$M_0=2$ 用 $Q''=2$，$M_0=3$ 用 $Q'''=6$。
$M_0=4$ 时，若 $Q'''(0)=0$，重数为 $(1,3)$（或反序）时有
$c_1+3c_2=0$、二次系数 $-6c_2^2\ne0$；
重数为 $(2,2)$ 时有 $c_1+c_2=0$、二次系数 $-2c_1^2\ne0$。
同首差的情形也包含在这些式子中，或直接用 $Q=(X-c)^{M_0}$。
故 $S\le H_f-2w$。现在用 (10) 第二行积分，得 (15)。

**恰有三个不同最近根。**
把相同首差合并，剩下 $b\le3$ 个互异非零首差 $c_j$，
重数和 $\mu_j$ 满足 $0<\mu_j<p$。
若前三个领先导数都为零，Newton/Bell 恒等式依次给
$$
\sum_j\frac{\mu_j}{c_j}
=\sum_j\frac{\mu_j}{c_j^2}
=\sum_j\frac{\mu_j}{c_j^3}=0.
$$
取前 $b$ 行，非零节点的 Vandermonde 可逆，迫全部 $\mu_j=0$，
矛盾。这里只用真正次数门 $\sum m_i<p$。
所以至少一个阶数 $j\in\{1,2,3\}$ 的领先导数非零，
$S\le H_f-jw\le H_f-w$。
每个活动集至少三根，(10) 第三行给 (15)。

**至少四个不同最近根。**
直接有 $H_f=v_t(f(t,g_0))\ge S$。
所有活动集至少四根，(10) 最后一行积分给
$\mathscr E_\lambda\ge10H_f\ge10S$。

这证明全部未截断情形；局部单位的导数在所用严格最低项之后出现，不改变显示非零系数。

### 3.2 接触达到 $s$ 或无穷的全部情形

现在称 $h_i\ge s$ 的根为高根，其余根的最大接触严格小于 $s$。
若至少三个高根，仅这些根的三个自项与三个交叉项已至少为
$21s\ge10S$。
若至少两个高根，且至少一个重数不小于二，最小配置的能量为
$(1+4+12)s=17s\ge10S$。
这使用 $\lambda_m\ge1$，重数不小于二时 $\lambda_m\ge2$。

若恰有两个高根且都简单，写
$f=(X-\alpha)(X-\beta)U_1$，$v_t(\alpha),v_t(\beta)\ge s$。
第二导数的最低项是 $2U_1(t,0)$；其它项多一个高根差，却最多损一个较远接触，所以严格较高。于是 $H_{\rm far}\ge S$。
两个高根与较远根的交叉项，加较远根自项，至少为
$$
\sum_{\rm far}(c_{m_i}+12\lambda_{m_i})h_i
\ge10H_{\rm far}\ge10S
$$
，由 (12) 得到；其它能量非负。

若只有一个高根，重数 $m\ge4$，其自项
$c_m s\ge16s\ge10S$。
若其重数为二或三，相应二阶或三阶导数的最低项是
$2U_1(t,0)$ 或 $6U_1(t,0)$，所以 $H_{\rm far}\ge S$。
其自项可舍去，用 (12) 分别以 $12\lambda_{m_i}$ 或
$18\lambda_{m_i}$ 支付全部较远根，仍得 (15)。

最后，若唯一高根简单，3.1 的 (17)–(19) 仍逐字成立：
高根差的阶大于所有较远接触；其全部交叉项准确读到较远 $h_i<s$。
按较远最近根是一条或多条，仍用 (11) 的相应一式。
若某根恰等于形式延拓的 $g_0$，直接置 $\alpha=0$；
(17) 没有对零值作对数除法，证明不变。

所有情况均保 $s$ 截断，因此没有使用原 ODE 未授权的更高轴。
引理证毕。

### 3.3 十的锐利性

在 $p>3$、$4a\le s$ 时，取局部例子
$$
g_0=1,\qquad f=(Y-1)^4-t^{4a}.
$$
四根不同、简单、同接触 $a$，四个 jet 都深 $S=4a$。
能量为 $4a+6\binom42a=40a=10S$。
因此不能把一般四长候选的十提高到纯重复因子的十二。
这个例子只证局部常数锐利，不把它当作原 $W_D$ 的截面。

## 4. 同一原十九角支付全部全局成本

这里使用 R680/R837 已完整证明的原几何输入，不重新计算它们。
在十九角光滑模型 $X$ 上，$\widehat P$ 是 nef 类 $\mathcal B_D$ 的实际截面，
$$
\mathcal B_D^2=\frac{47}{12}D^2+O(D).
\tag{20}
$$
有限式始终使用原十九个取整重数给出的准确整数 $\mathcal B_D^2$。

将接触所读 $q$ 个单位点的实际几何整非垂直因子写为
$\prod_iF_i^{m_i}$，严格变换为 $C_i$，$b_i=\deg_YF_i$。
每个 $C_i$ nef，且
$$
\sum_i m_ib_i\le D,\qquad
\mathcal B_D-\sum_i m_iC_i\text{ 为有效除子}.
\tag{21}
$$
固定 forcing 极除子记为 $L_{\rm pole}$，避免与物理窗口混名。
原完整 Euler forcing 给非零截面
$$
K^E_{F_i}|_{C_i}\in
H^0(C_i,\mathcal O_{C_i}(3C_i+L_{\rm pole})),\qquad
L_{\rm pole}.C_i\le8b_i,
\tag{22}
$$
并在全部所读单位点同时支付截断接触和三倍完整判别式。
不同实际因子的交叉根由真实全局交数 $C_iC_j$ 支付。
所有奇支、tame 分歧、无穷及十九角均包括在这个原输入中。

同一个不可约因子的所有局部根有同一个真实重数 $m_i$；
乘 (22) 以 $c_{m_i}$，恰支付其自项和内部交叉项。
对不同因子用 $\lambda_{m_i}\lambda_{m_j}$ 倍的交数。
因此对同一个原截面的所有 $q$ 个点，有
$$
\sum_{\zeta\in\mu_q}\mathscr E_{\lambda,\zeta}
\le3\mathscr C_\lambda^2+
 \sum_i c_{m_i}L_{\rm pole}.C_i,\qquad
\mathscr C_\lambda=\sum_i\lambda_{m_i}C_i.
\tag{23}
$$
$\lambda_{m_i}\le m_i$ 与 (21) 给
$\mathcal B_D-\mathscr C_\lambda$ 有效实，且两类均 nef，故
$\mathscr C_\lambda^2\le\mathcal B_D^2$。
又由 (9)、(21)、(22)，固定极成本至多
$$
\sum_i c_{m_i}L_{\rm pole}.C_i
\le80\sum_i m_ib_i\le80D.
\tag{24}
$$
应用第3节引理及 (7)，得到所有有限参数都成立的准确必要界
$$
\boxed{
10q(H-r)\le
3\mathscr C_\lambda^2+
 \sum_i c_{m_i}L_{\rm pole}.C_i
\le3\mathcal B_D^2+80D.
}
\tag{25}
$$
优先保中间的实际因子界；最后一界才是统一预算。
没有把加权除子宣称为某个来源的零除子，没有对原矩阵作饱和，
没有给任一商因子免费添加列。

原总 $Y$ 次数 $D<p$ 保所有 Puiseux 分裂 tame，其分裂群阶整除
$D!$；导数中的重数和 $m(m-1)(m-2)$ 及最近根合并后的总重数均为当前单位。
(25) 因而不遗漏正特征不可分或大重数例外。

## 5. 完整目标 p 门与两个不同临界

由 $H=s-\Delta$、$r\le M_D$，(25) 给
$$
\boxed{
p\le6(M_D+\Delta)-1+
 \frac9{5q}\mathcal B_D^2+\frac{48D}{q}.
}
\tag{26}
$$
$r\ge H$ 的简单情况也满足此较弱式。
全部物理前缀13、四条十三行带、原全来源帽和精确十九角自交均保留。
其二次主项为
$$
p\le\frac{141}{20q}D^2+O(D).
\tag{27}
$$

原来源维数仍为 $\dim\mathcal W_D=47D^2/24+O(D)$。
若使用五块自身的四个长块并有 $\ell=o(D^2)$，自然临界是
$$
4s+\ell=\dim\mathcal W_D+o(D^2),\qquad
p/D^2\longrightarrow47/16.
\tag{28}
$$
$q\ge3$ 时，(27) 的主系数至多 $47/20<47/16$，矛盾。
所以此真正五块临界中，充分大的非零候选只能有
$$
\gcd\{\text{非零 charge 差}\}\in\{1,2\}.
\tag{29}
$$

另一方面，若仍在旧四块的三长维数尺度
$p/D^2\to47/12$，而同一实际候选另已通过第四条真实长行，
$q\ge2$ 时 (27) 至多给 $141/40<47/12$，矛盾。
于是这个更小预算中的四长候选只能有
$$
\gcd\{\text{非零 charge 差}\}=1.
\tag{30}
$$
仅有原三个长块加一个短块时，不得使用 (30)。
第五原中央的存在、五轴 Jacobian 可逆、第五位 Hensel 必要值，也不单独支付“同一候选通过第四长行”这个前提。

本篇把一般原 $W_D$ 的四长门从三长七倍严格提升为四长十倍，
并保所有有限重数与线性误差。它没有排除 (29)–(30) 剩余的密集 charge，
没有与已知局部单位子式未经联合独立性证明相加，
也没有证明原完整仿射修正或跨素数中央非零。

## 依赖与复现范围

- [R943](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)：真实第五算术源、五轴必要系统、原五块评价、52跨界成本和全部三/四/五次折回。
- [R837](R837-original-three-long-root-energy-and-uniform-multiplicity-truncation.md)：同一 canonical 来源、tame 根接触、原 forcing/判别式、十九角 nef 全局输入；本篇只增加四 jet 的新局部证明。
- [R837 实权增补](../notes/2026-11-15-r837-real-nef-root-weights-and-linear-multiplicity-cost.md)：实 Néron–Severi 权不改来源的原解释。新权 (8) 与十倍证明均在本文给出，未把旧七倍常数直接改数。
- [R821](R821-original-four-central-axes-and-complete-four-block-carries.md)：原完整普通单位、四十 charge 与各前缀的实际三角逆。

本文全部结论为显示不等式与统一代数证明，无新增数学执行、素数扫描或可重算输出。
