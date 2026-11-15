# R837 增补 — 实 nef 权重与不截除高重数的有限线性误差

日期：2026-11-15。**状态：已证明。** 本增补保持
[R837](../results/R837-original-three-long-root-energy-and-uniform-multiplicity-truncation.md)
的同一原来源、目标素数、两种不同长窗及全部 carry，
把其中的高重数截除替换为一个直接的加权根引理。
得到所有有限参数的界
$$
7q(H-r)\le3\mathcal B_D^2+56D
$$
及原两长窗的
$$
4q(H-r)\le3\mathcal B_D^2+32D.
$$
不再要求 $B_K<s$，也不需要选择截除参数 $K$。
主二次常数及尚未排除的密集电荷范围与 R837 一致。

## 1. 仅作实数能量权，不给来源开平方

保持原 $p=6s-1$、$f_D<p$、$\mathcal W_D$、
$\widehat P=d^{C_D}P$、
$r=\operatorname{ord}_t\widehat P$、$H=s-\Delta$、
$S=H-r>0$。
$\Delta=0$ 或 $13$ 按 R837 的真正相对／物理来源范围选取；
原三个长块的使用前提和最后短块均不改。

对一个实际根的整数重数 $m$，定义实数
$$
c_1=1,\qquad c_2=4,\qquad c_m=7(m-2)\quad(m\ge3),
\qquad \lambda_m=\sqrt{c_m}.
\tag{1}
$$
有
$$
1\le\lambda_m\le m,\qquad c_m\le7m.
\tag{2}
$$
这些正实数只作为交数不等式的权。
不在剩余域开平方，不改任何多项式的重数，
也不向原整来源添加带实系数的列。

所需三个初等不等式是
$$
c_m+6\lambda_m\ge7m,\qquad
c_m\ge7(m-2),\qquad
c_m+12\lambda_m\ge7m+6.
\tag{3}
$$
$m=1,2$ 直接核验；
$m\ge3$ 时分别化为
$6\sqrt{7m-14}\ge14$、等号及
$12\sqrt{7m-14}\ge20$。

特别，对任意两个重数 $a,b$，
$$
c_a+c_b+6\lambda_a\lambda_b\ge7(a+b-1).
\tag{4}
$$
若一个为一，由 (3) 的第一式即得；
若二者至少为二，使用第二式和
$\lambda_a\lambda_b\ge4$，左边至少为 $7(a+b)-4$。

三个根的加权基底满足
$$
\sum_{i=1}^3c_{m_i}
+6\sum_{i<j}\lambda_{m_i}\lambda_{m_j}
\ge7\sum_{i=1}^3m_i.
\tag{5}
$$
三个重数均为一时等号成立。
把其中任一重数从一提高为 $m$，另外两个权之和至少为二，
故增量至少为
$c_m-1+12(\lambda_m-1)\ge7(m-1)$。
在已有非空根集上增加新根，若原权之和至少为一，
由 (3) 第一式，能量增量至少为 $7m$。

## 2. 原三个 jet 的完整根引理

在 R837 相同的 tame 完成局部环中写
$$
f=U\prod_i(Y-\psi_i)^{m_i},\qquad U(0,1)\ne0,
\qquad \sum_i m_i<p.
$$
令
$$
h_i=\operatorname{ord}_t(\psi_i-g),\quad
\bar h_i=\min(h_i,s),\quad
d_{ij}=\operatorname{ord}_t(\psi_i-\psi_j).
$$
只计经过该单位点的根，其余因子纳入局部单位 $U$。
若同一个 $f,f_Y,f_{YY}$ 在 $g$ 上均消到 $S$，
其中 $0<S\le s$，则
$$
\boxed{
\mathscr E_\lambda:=
\sum_i c_{m_i}\bar h_i+
6\sum_{i<j}\lambda_{m_i}\lambda_{m_j}d_{ij}
\ge7S.}
\tag{6}
$$
原 Euler 三行与这三个普通 $Y$ jet 由单位下三角矩阵相互转换，
因为 $g(0)\ne0$。

先设全部接触小于 $s$。
置 $H_f=\sum_i m_ih_i$、$w=\max h_i$。
由非阿基米德不等式 $d_{ij}\ge\min(h_i,h_j)$，
(6) 左边至少为各高度处的活跃根能量积分：
$$
\int_0^w\left(
 \sum_{h_i\ge x}c_{m_i}
 +6\sum_{\substack{i<j\\h_i,h_j\ge x}}
 \lambda_{m_i}\lambda_{m_j}\right)\,dx.
\tag{7}
$$

若唯一最近根的重数 $m\ge2$，
$f_{YY}(g)$ 的最低项由该根被求导两次给出，
其非零系数为 $m(m-1)$，
所以 $S\le H_f-2w$。
每个活跃集包含该根；由 (3) 的第二式给基底，
再用增加根的不等式，(7) 至少为 $7(H_f-2w)$。

若唯一最近根的重数是一，
$f_Y(g)$ 的最低项给 $S\le H_{\rm far}:=H_f-w$。
每个较远根的自项及其与最近根的交叉项，
按 (3) 第一式至少支付其 $7m_ih_i$；
其余项非负，故总量至少为 $7H_{\rm far}$。

若恰有两个最近根，写它们与 $g$ 的首差为
$a_1t^w,a_2t^w$，$a_1a_2\ne0$，实际重数为 $m_1,m_2$。
若 $m_1/a_1+m_2/a_2\ne0$，第一导数给
$S\le H_f-w$。
若该和为零，第二导数的领先系数为
$$
-\left(\frac{m_1}{a_1^2}+\frac{m_2}{a_2^2}\right),\qquad
\frac{m_1}{a_1^2}+\frac{m_2}{a_2^2}
=\frac{m_1(m_1+m_2)}{m_2a_1^2}\ne0.
$$
所以 $S\le H_f-2w\le H_f-w$。
这里 $m_1+m_2<p$ 是真正源次数门，不能在正特征删去。
每个活跃集都包含这两个根；
(4) 和增加根的不等式使 (7) 至少为 $7(H_f-w)$。

若至少三个根同为最近根，函数值本身给 $S\le H_f$。
由 (5) 及增加根的不等式，(7) 至少为 $7H_f$。
这支付全部未截断情形；局部单位的导数在以上严格最低项之后出现，
不会改变所用非零系数。

现在允许实际接触达到或超过 $s$，包括某根等于形式延拓的 $g$。
若至少两个根的接触达到 $s$，仅其两个自项和交叉项就至少为 $8s$。
若只有一个这样的根而其重数至少为三，
其自项 $c_m s\ge7s$。
若唯一高根的重数为二，第二导数的严格最低项给
$H_{\rm far}\ge S$；较远根与这个高根的交叉项仍完整读到 $h_i<s$，
(3) 的第一式及 $\lambda_2=2$ 给能量至少 $7H_{\rm far}$。
重数为一时同理由第一导数和 $\lambda_1=1$ 得到。
因此 (6) 保全部最近根截断，不把原 ODE 延长过 $s$。

常数七仍然锐利：
$f=(Y-1)^3-t^{3a}$、$g=1$、$3a\le s$ 时，三根皆为简单根，
(1) 的权全为一，能量为 $21a=7S$。
本增补并未把一般根簇的常数提高到八。

## 3. 同一原十九角给完全有限线性余项

在所有真实单位点 $(0,\zeta)$、$\zeta\in\mu_q$，
将同一个 $\widehat P/t^r$ 的实际接触因子写为
$\prod_iF_i^{m_i}$，严格变换为 $C_i$，
$b_i=\deg_YF_i$。原 charge 对称给这些点同一个长度 $S$ 的三个 jet；
不是给其它分支增加中央零。

对同一个不可约因子，它的所有局部根有同一实际重数 $m_i$。
因此 (6) 的内部根对权恰为 $6c_{m_i}$。
将 R680/R837 的完整 forcing／判别式不等式乘 $c_{m_i}$，
准确支付该因子的全部自项和内部交叉项。
不同因子的根对则由其真实全局交数支付。
得到
$$
\sum_{\zeta\in\mu_q}\mathscr E_{\lambda,\zeta}
\le
3\mathscr C_\lambda^2+
\sum_i c_{m_i}L.C_i,\qquad
\mathscr C_\lambda=\sum_i\lambda_{m_i}C_i.
\tag{8}
$$
这里的 $L$ 是原 R680 的完整固定极除子，$L.C_i\le8b_i$；
没有删去奇点、tame 分支或十九角。

每个 $C_i$ nef。由 $\lambda_{m_i}\le m_i$，
原实际有效除子分解给
$\mathcal B_D-\mathscr C_\lambda$ 为有效实除子。
$\mathcal B_D$ 和 $\mathscr C_\lambda$ 均 nef，故
$$
\mathscr C_\lambda^2\le\mathcal B_D^2.
$$
这是 Néron–Severi 实向量空间中的交数不等式，
不需要该加权除子是某个来源截面的零除子。
最后，真实次数给 $\sum_i m_ib_i\le D$，
所以 (2)、(8) 给
$$
\boxed{
7q(H-r)\le
3\mathscr C_\lambda^2+\sum_i c_{m_i}L.C_i
\le3\mathcal B_D^2+56D.}
\tag{9}
$$
优先保 (9) 中使用实际因子的第一界；
最后一个界对全部有限预算统一成立。

## 4. 原两长窗的相同加强

只假定同一个 $f,f_Y$ 消到 $S$ 时，改取
$$
c'_1=1,\qquad c'_m=4(m-1)\ (m\ge2),\qquad
\lambda'_m=\sqrt{c'_m}.
\tag{10}
$$
有 $1\le\lambda'_m\le m$、$c'_m\le4m$，
以及
$$
c'_m\ge4(m-1),\qquad
c'_m+6\lambda'_m\ge4m+3.
\tag{11}
$$
唯一最近根重数至少二时，第一导数给
$S\le H_f-w$，由 (11) 逐活跃集得到能量至少 $4(H_f-w)$。
唯一最近根重数一时，第一导数给 $S\le H_{\rm far}$，
其与每个较远根的交叉项及该根自项至少支付 $4m_ih_i$。
至少两个最近根时，只用 $S\le H_f$；
两个根的基底能量至少为 $4(m_1+m_2)$：
一个重数为一时由 (11)，二者至少为二时由
$c'_a+c'_b=4(a+b-2)$ 和 $\lambda'_a\lambda'_b\ge4$。
增加其它根仍至少支付 $4m$。

截断也完整保持：
至少两个高根的能量至少 $8s$；
唯一高根重数至少二时其自项至少 $4s$；
唯一简单高根由第一导数及较远根交叉项支付。
因此原 R672 的两 jet 下界四仍成立，
而全局成本按 (8) 改为 $\sum_i c'_{m_i}L.C_i\le32D$：
$$
\boxed{4q(H-r)\le3\mathcal B_D^2+32D.}
\tag{12}
$$
这同样不要求重数有界、最近根低于 $s$ 或额外截除门。

## 5. 准确目标 p 门及范围

仍记 $M_D=5D+4-(D\bmod2)$。
$r\ge H$ 时已有 $p\le6(M_D+\Delta)-1$；
$r<H$ 时 (9)、(12) 分别给
$$
\boxed{
p\le6(M_D+\Delta)-1+
\frac{18}{7q}\mathcal B_D^2+\frac{48D}{q}
\quad\text{（真正三个长窗）},
}
\tag{13}
$$
$$
\boxed{
p\le6(M_D+\Delta)-1+
\frac{9}{2q}\mathcal B_D^2+\frac{48D}{q}
\quad\text{（原两个长窗）}.
}
\tag{14}
$$
所有取整、原十三行带 及
$\mathcal B_D^2$ 的精确十九角公式按 R837/R680 保留。
(13)–(14) 的主项正是 R837 的
$141D^2/(14q)$、$141D^2/(8q)$，
但现在误差是统一 $O(D)$，且没有 $B_K<s$ 的前提。

三长自然临界与旧两长临界仍是两个不同预算。
本增补不把原两长加一个短块当作三个长块，
不删原 $P_{134}/U_0$、三个十三行带、同一 $R$ 或下一位，
也不证明密集电荷 $q=1,2$ 的指定仿射目标不在全原像中。
它只是对同一真实截面给更强的有限全参数必要界，
没有新的计算运行或算术中央条件。
