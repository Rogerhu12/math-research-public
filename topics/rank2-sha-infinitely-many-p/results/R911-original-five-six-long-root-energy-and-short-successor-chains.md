# R911 — 原四块核的短后继链、五／六长根能量与真实联合秩

日期：2026-11-16。**状态：下列固定五／六条长行的全重数根界、原三倍来源成本、真实短链排除和联合秩界已证明。指定 forcing 及主目标仍未完成。**

本篇接 [R907](R907-original-two-step-successor-and-six-dimensional-fiber-feedback.md)。
当原第四短窗严格越过接触阶时，一条已经存在的实际后继链准确等于
同一来源的连续 Euler 导数。五条、六条长零只在这样的链上使用，
不添给任意原核元素。所得结论限制整个原核的维数，
而不只是 R907 的无限续接部分。

## 1. 原来源、轴范围和共同原点帽

保持 R907 的全部对象与原整返回
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D},
\quad \mathcal H_j=H^0(X,\mathcal O_X(jC)),
\quad N=\mathcal O_C(C),\quad \kappa=C^2,
$$
$$
C=(F=0),\quad \mathcal E=Y\partial_Y,\quad
b=\deg_YF,\quad 3b<p,\quad p>211.
\tag{1}
$$
采用同一个原 $r=2,\ C.f_0=3$、$b\ge5$ 的来源范围。
令 $P=(0,1)$、$\gamma=(\mathcal EF)(P)\ne0$，
$g=\psi\exp\eta$、$\operatorname{ord}\eta=h$，并保持
$$
h<T\le2h,\quad T-h>\kappa,\quad T=s-r-13,\quad
\boxed{h<L<T},\qquad L=\max(\ell-r,0).
\tag{2}
$$
所以 R907 所需 $L\ge T-h$ 自动成立；这里的 $L$ 是原物理短窗，
不是人为增加的长块。

记
$$
K=\{G\in\mathcal H_3:
(\mathcal E^jG)(t,g)\in(t^T)\ (0\le j\le2),\
(\mathcal E^3G)(t,g)\in(t^L)\},
$$
$$
V_i(G)=(\mathcal E^iG)|_C,\qquad
V_T=H^0(C,N^3(-TP)).
\tag{3}
$$
R834/R902 给 $V_0,V_1:K\to V_T$ 各自单射。
R907 定义
$$
a(G)=\frac{(\mathcal E^4G)(P)}{6\gamma^3},\qquad
\mathcal TG=\mathcal EG-a(G)F^3.
\tag{4}
$$
对 $G,H\in K$，整个限制截面的相等
$V_1(G)=V_0(H)$ 准确等价于 $H=\mathcal TG\in K$。
再由 $L>h$，每一对这样的后继准确有 $a(G)=0$，所以 $H=\mathcal EG$。

所有低轴只读到 $T<s-4$。
原四轴的修正从 $s-4$ 才开始，故本篇使用的
$g\equiv\rho=(1+8t)\Theta^{17}\pmod{t^T}$
是原已付低窗身份。
为估计根接触，可使用 R680 的参考 $\rho$ 的模 $t^s$ 数据；
不能据此将实际四轴 $g$ 宣称为模 $t^s$ 的同一个参考轴。
原三个十三行带和全部后续高轴不变。

置
$$
e_+=C.H_+,\qquad
R_C=3(e_++\mu_{0,1}).
\tag{5}
$$
R907(16)–(18) 逐个支付全部原 pure charge 的帽。
因为 $\mathcal H_3$ 是同一 $G_m$ 直和，对任意 $0\ne G\in\mathcal H_3$，
其非零 charge 分量仍为实际全局截面，故
$$
v_G:=\min_n\operatorname{ord}_0 [Y^n]G
\le R_C<T.
\tag{6}
$$
这里 $v_G$ 是原多项式的实际 $t$ 因子次数，不只是在 $P$ 的评价阶。
$R_C<T$ 在 (2) 的原 $b\ge5$ 强窗已由 R903/R907 支付。
以下先保 $v_G$，最后才用统一上界 $R_C$。

## 2. 五／六条长行的全重数局部根引理

只在本节令
$$
\nu\in\{5,6\},\qquad c_\nu=3\nu-2\in\{13,16\},
$$
并对真实整数重数 $m\ge1$ 定义实权
$$
w_m=\min\{m^2,c_\nu m\},\qquad
\lambda_m=\sqrt{w_m}.
\tag{7}
$$
有 $\lambda_m\le m$、$w_m\le c_\nu m$。
这些实数只用于交数不等式，不给原来源开平方或改变整数重数。

在原 tame 完成局部环内写
$$
f=U\prod_i(Y-\psi_i)^{m_i},\quad U(0,1)\ne0,\quad
\sum_i m_i<p.
$$
只计经过 $(0,1)$ 的互异根，其余因子入 $U$。
设 $0<S\le s$，同一个 $f$ 满足
$$
\partial_Y^j f(t,\rho)\in(t^S)\qquad(0\le j<\nu).
\tag{8}
$$
令
$$
h_i=\operatorname{ord}_t(\psi_i-\rho),\quad
\bar h_i=\min(h_i,s),\quad
d_{ij}=\operatorname{ord}_t(\psi_i-\psi_j).
$$
允许 $h_i=\infty$。

**引理 1。**
$$
\boxed{
\mathscr E_\nu=
\sum_iw_{m_i}\bar h_i+
6\sum_{i<j}\lambda_{m_i}\lambda_{m_j}d_{ij}
\ \ge\ c_\nu S.}
\tag{9}
$$

**证明。** 先支付一个能量密度不等式。
某高度的活动根总质量为 $M$，其能量密度为
$$
A=\sum_iw_{m_i}+6\sum_{i<j}\lambda_{m_i}\lambda_{m_j}.
$$
若其中某根 $m_i\ge c_\nu$，则
$\lambda_{m_i}\ge c_\nu$、$w_{m_i}=c_\nu m_i$。
其它大根的自项也已付 $c_\nu m_j$；
每个小根与这个大根的交叉项支付其全部亏量
$c_\nu m_j-m_j^2$。因此
$$
A\ge c_\nu M.
\tag{10}
$$
若没有大根，则所有权就是 $w_m=m^2,\lambda_m=m$。
若至少有 $c$ 个不同活动根，
$$
A=3M^2-2\sum_i m_i^2
\ge M^2+4(c-1)M-2c(c-1).
\tag{11}
$$
对 $M\ge\nu,\ 1\le c<\nu$，(11) 与
$c_\nu(M-\nu+c)$ 的差均非负。
全部情形可写为以下完整小表，未进行数值扫描：

| $\nu$ | $c$ | 差的明确表达／下界，$M\ge\nu$ |
|---|---:|---|
| $5$ | $1$ | $(M-13/2)^2+39/4$ |
| $5$ | $2$ | $(M-9/2)^2+59/4$ |
| $5$ | $3$ | $(M-5/2)^2+31/4$ |
| $5$ | $4$ | $M^2-M-11\ge9$ |
| $6$ | $1$ | $(M-8)^2+16$ |
| $6$ | $2$ | $(M-6)^2+24$ |
| $6$ | $3$ | $(M-4)^2+20$ |
| $6$ | $4$ | $(M-2)^2+4$ |
| $6$ | $5$ | $M^2-24\ge12$ |

若 $c\ge\nu$，在 (11) 中仅用 $c=\nu$，
它与 $c_\nu M$ 的差是
$$
M^2+(\nu-2)M-2\nu(\nu-1)\ge0\qquad(M\ge\nu).
\tag{12}
$$
因此无论是否存在大根，活动质量 $M\ge\nu$ 时都有
$$
A\ge
\begin{cases}
c_\nu(M-\nu+c),&1\le c<\nu,\\
c_\nu M,&c\ge\nu.
\end{cases}
\tag{13}
$$

下面从实际导数中取一个不可能相消的最低项。
若达到或超过截断 $s$ 的根总质量至少为 $\nu$，
仅这些根在区间 $[0,s]$ 的能量已经至少为 $c_\nu s$：
有大根时用 (10)；没有时用 $A\ge M^2\ge\nu^2\ge c_\nu$。
此时 (9) 直接成立。

否则按接触从近到远排列。
取累计质量首次达到 $\nu$ 的那一层，高度为 $w<s$。
更近根的总质量为 $M_{\rm prev}<\nu$，
当前层的质量为 $M_{\rm lay}\ge\nu-M_{\rm prev}$。
(8) 模 $t$ 保证过该点的总质量至少为 $\nu$，所以此层确实存在。
将更近根先以其最高 $Y$ 次数提出，
当前层的非零首差多项式记为
$$
P(X)=\prod_{\alpha=1}^c(X-a_\alpha)^{n_\alpha},
\quad a_\alpha\ne0,\quad a_\alpha\text{ 两两不同},
\quad \sum_\alpha n_\alpha=M_{\rm lay}.
\tag{14}
$$
这里 $c$ 是不同首差的数目；若若干真实根首差相同，合并其整数质量。
所以 $P(0)\ne0$，且每个 $n_\alpha$ 及其总和都小于 $p$。

置 $\nu'=\nu-M_{\rm prev}$。
存在一个
$$
\max(0,\nu'-c)\le k\le\nu'-1
$$
使 $[X^k]P\ne0$。
当 $c\ge\nu'$ 时用 $k=0$。
否则令 $A(X)=\prod_\alpha(X-a_\alpha)$，
$B(X)=\sum_\alpha n_\alpha A(X)/(X-a_\alpha)$，
有 $AP'=BP$，$\deg A=c$，$B$ 的最高系数为 $M_{\rm lay}$。
若连续 $c$ 个系数
$P_{\nu'-c},\ldots,P_{\nu'-1}$ 全零，
比较 $AP'=BP$ 的系数会倒推出
$$
(j-M_{\rm lay})P_j=0
\quad(j=\nu'-c-1,\nu'-c-2,\ldots,0).
$$
所有 $0\le j<\nu'\le M_{\rm lay}<p$，
故这些乘子全是单位，最终迫 $P_0=0$，矛盾。

读取原导数阶 $M_{\rm prev}+k<\nu$。
其最低项准确来自：把更近根全部微分掉，
当前层取上述非零第 $k$ 系数，其余根和局部单位取值。
少微分一个更近根，或多微分一个更远根，都会严格提高赋值；
对单位求导也在更高阶。因此这个最低项不能被其它项相消。
所有导数阶与根总次数均小于 $p$，相应阶乘及组合系数为单位。

令
$$
H_w=\sum_i m_i\min(h_i,w),\qquad
\beta=\max(M_{\rm prev},\nu-c)\le\nu-1.
$$
刚才的导数零精确给
$$
S\le H_w-(M_{\rm prev}+k)w\le H_w-\beta w.
\tag{15}
$$
在每一个 $0<x\le w$，活动质量 $M(x)\ge\nu$，
并至少含当前层的 $c$ 个不同真实根。
由 (13) 及 $\beta\ge\nu-c$，有
$A(x)\ge c_\nu(M(x)-\beta)$。
利用 $d_{ij}\ge\min(\bar h_i,\bar h_j)$ 积分，得
$$
\mathscr E_\nu\ge\int_0^w A(x)\,dx
\ge c_\nu(H_w-\beta w)\ge c_\nu S.
$$
更近根可以有无穷接触；它们已全部被微分掉，
且在 $[0,w]$ 上的截断权仍完整。
这同时支付全部最近根截断和正特征首项。证毕。

## 3. 同一个三倍来源的准确全球成本

**命题 2。** 若 $0\ne G\in\mathcal H_3$ 在原轴上有 $\nu=5$ 或 $6$
条真正的长 Euler 零
$$
(\mathcal E^jG)(t,g)\in(t^T)\qquad(0\le j<\nu),
$$
则
$$
\boxed{
\begin{aligned}
13(T-v_G)&\le27\kappa+312b&&(\nu=5),\\
16(T-v_G)&\le27\kappa+384b&&(\nu=6).
\end{aligned}}
\tag{16}
$$

**证明。** 除去原实际 $t^{v_G}$ 后，长行长度为 $S=T-v_G>0$。
Euler 不作用于 $t$，单位轴上的普通 $Y$ jet 与 Euler jet 由可逆三角矩阵相互运输。
只用 $g\equiv\rho\bmod t^T$，即可对同一多项式使用引理 1；
没有延长任何实际读取窗口。

把经过 $P$ 的真实几何整非垂直接触因子记为 $F_i^{m_i}$，
严格曲线为 $C_i$、$b_i=\deg_YF_i$。
原次数 $3b<p$ 使其共同分裂扩张 tame。
R680(13)–(20) 的原 ODE forcing、共振非零和完整十九角极帽给
$$
\sum_{\psi\mid F_i,P}\min(h_\psi,s)+3\Delta_{i,P}
\le3C_i^2+\mathscr L_{\rm ODE}.C_i,\qquad
\mathscr L_{\rm ODE}.C_i\le8b_i.
\tag{17}
$$
$\Delta_{i,P}$ 保全部奇支及内部根对。
本处只用该几何极帽，不把 forcing 当作免费原来源列。

每个 $C_i$ nef，且同一个 $G$ 的完整零除子给
$3C-\sum_i m_iC_i$ 有效。
设 $\mathscr C_\lambda=\sum_i\lambda_{m_i}C_i$。
由 $\lambda_m\le m$，$3C-\mathscr C_\lambda$ 仍为有效实除子；
$3C$ 和 $\mathscr C_\lambda$ 均 nef，故
$$
\mathscr C_\lambda^2\le9\kappa.
$$
把 (17) 整体乘 $w_{m_i}$，同一因子内部根对权恰为 $6w_{m_i}$；
不同因子用其真实交数乘 $6\lambda_{m_i}\lambda_{m_j}$。
因此引理 1 给
$$
c_\nu(T-v_G)
\le3\mathscr C_\lambda^2+\sum_iw_{m_i}\mathscr L_{\rm ODE}.C_i
\le27\kappa+8c_\nu\sum_i m_ib_i.
$$
最后 $\sum_i m_ib_i\le\deg_YG\le3b$，得到 (16)。
垂直含量、两水平截面、其余因子和全部十九角余量留在有效余除子中。
没有假定无重复、固定重数上界或用环境矩形替换原 $\mathcal H_3$。证毕。

## 4. 两个有限的真实后继链排除门

在 (1)–(6) 下，定义实际 $j$ 步链为
$$
G_0,\ldots,G_j\in K,\qquad
V_1(G_i)=V_0(G_{i+1})\quad(0\le i<j).
\tag{18}
$$
由 R907 及 $L>h$，它准确满足 $G_i=\mathcal E^iG_0$。
于是三项链 $j=2$ 给同一个 $G_0$ 的五条长零；
四项链 $j=3$ 给六条。最后一项的第四短行仍保留，未用于减少成本。

所以若
$$
\boxed{13(T-R_C)>27\kappa+312b,}
\tag{19}
$$
则每条三项链均为零；若
$$
\boxed{16(T-R_C)>27\kappa+384b,}
\tag{20}
$$
则每条四项链均为零。
这些都是原实际链的排除，绝不说任一 $G\in K$ 自动带五或六条长行。

例如，在已有 $T>2\kappa$ 下，(20) 的一个直接充分门是
$$
\boxed{5\kappa>48(e_++\mu_{0,1})+384b.}
\tag{21}
$$
没有为使用此门新增 $L>h$ 之外的中央条件。
在另有 $b\to\infty,\ \kappa/b\to\infty$ 的真实序列中，
R819 的
$\kappa\ge(b-3)e_++3b,\ \mu_{0,1}\le b-3$
给 $R_C=o(\kappa)$。
故 (20) 在 $T>2\kappa$ 下最终成立；
若还确有 $T/\kappa\to9/4$，(19) 也最终成立。
这些只适用于同时满足原长短窗 (2) 的序列，
不把原短窗不足的其它临界预算搬到这里。

## 5. 对整个实际四块核的联合秩增益

令 $n_T=\dim_kV_T$，不预设这个线束非特殊。
对同一个核定义完整线性链映射
$$
\mathcal C_j:K^{j+1}\longrightarrow V_T^j,\qquad
(G_0,\ldots,G_j)\longmapsto
(V_1G_0-V_0G_1,\ldots,V_1G_{j-1}-V_0G_j).
\tag{22}
$$
它的核正是 (18)，每一项都来自原同一个 $V_0,V_1$。
若 $G_0=0$，$V_0$ 的真实单射逐项迫全链为零。
因此 (19)、(20) 分别使 $\mathcal C_2,\mathcal C_3$ 单射，严格给
$$
\boxed{
\dim K\le\left\lfloor\frac{2n_T}{3}\right\rfloor
\quad\text{在 (19) 下},
}
\tag{23}
$$
$$
\boxed{
\dim K\le\left\lfloor\frac{3n_T}{4}\right\rfloor
\quad\text{在 (20) 下}.
}
\tag{24}
$$
这约束整个 $K$，包括非稳定部分；
不是把 R902 与 R903 两个分别单射的秩直接相加。
实际子格四块映射的像秩因而至少为
$\dim\mathcal H_3-\lfloor2n_T/3\rfloor$
或 $\dim\mathcal H_3-\lfloor3n_T/4\rfloor$。
其它显示单位块如有重叠，仍不能直接相加。

对非空同目标仿射纤维，其差空间是同一个 $K$，故这些维数界适用；
它们本身不判该纤维为空或指定 $[b_0]$ 为零／非零。
R842 的原 GRes、固定边界补偿、同 $q_{\rm src}$ 的所有 Euler 导数、
唯一 $V_2$、同一个 $3\eta$ 修正、同 $K_{\rm corr}/H_{\rm corr}$、
完整 $R/S$、原三个十三行带和下一精度全部保持。
原 $\mathcal W_D$ 的其余列也未被缩成 $\mathcal H_3$。

### 5.1 当前同因子 quartic 来源的短窗互斥

必须单独保留一个实际适用边界。若当前原候选正是
$$
P_{\rm fact}=t^rq_{\rm src}F^4,\qquad q_{\rm src}(P)\ne0,
$$
其中用的是本篇同一个 F 和同一个物理轴，则直接求导得
$$
\mathcal E^3P_{\rm fact}
=t^r\bigl(24q_{\rm src}F(\mathcal EF)^3+F^2R\bigr)
$$
（R 为实际同源多项式）。因 $\operatorname{ord}F(t,g)=h$、
$\gamma\ne0$、$p>211$，第一项首系数非零，而其余项阶至少 $r+2h$。
故其准确阶为 $r+h$。原物理来源如带共同十三行偏移，
它在真实零条件和此首项中同时加上；按原记号消去之后，
第四短行要求 $\ell\le r+h$，即
$$
\boxed{L=\max(\ell-r,0)\le h.}
$$
所以本篇 (2) 的 $L>h$ 与这种**同 F、余因子为单位的当前 quartic 来源**
互斥。(23)–(24) 是其余满足已列假设的原 $\mathcal H_3$ 窗口定理，
不能拿来补这个 quartic 候选的 forcing。后者须继续保留 R907 的
$a(G)F^3$ 反馈，在它实际具有的 $L\le h$ 窗中作联合论证。

依赖：R680(13)–(20) 的全十九角 forcing／判别式，
R837 实 nef 增补的实际交数运输，R834/R902/R903 的真端点单射，
R907 的全后继式及 pure-charge 帽。
本篇没有新增数学执行、素数扫描或生成数据。
