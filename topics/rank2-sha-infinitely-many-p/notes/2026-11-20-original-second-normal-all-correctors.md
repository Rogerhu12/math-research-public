# 双 jet 尾退出后的原第二法向与全修正预算

日期：2026-11-20。状态：完整符号证明；未执行数学计算。

**作用范围澄清。** 同一原 P 已有 C-nef 下界
d_D≥4κ+3r_src；本注在 T≤3κ 时所得 s+2 预算被该旧界覆盖，
不构成当前 R836 未闭范围的新排除。准确差与潜在严格改进区
见同目录 original-all-correctors-budget-versus-source-nef-bound.md。
下文保留实际第二法向及三种同修正重数的正确结构读取。

本注接 R934 与 R935。R935 处理负 fringe 中
1≤τ≤d₀+1；在 τ=d₀+2 起，原双 jet 的自然尾已退出全 J
读窗，不能继续声称首法向仍有已知非零尾。本注使用仍在实际
第三长行与第四短行中的第二法向，逐一处理同一原修正的
C 重数 0、1、2。首常数 28 是 R824 已有结论；新增的是它在
当前负 fringe、全 WD 修正与完整十九角预算中的具体后果。

## 1. 原来源与额外窗口

保 R935 的全部原定义和门：

\[
p=6s-1>211,\qquad b=\deg_YF\ge5,\qquad
C=(F),\qquad C\cdot f_0=3,\qquad 3b<p,
\tag{1}
\]
\[
\mathcal E=Y\partial_Y,\qquad
e_0=(\mathcal EF)(0,1)\ne0,\qquad q_0=q(0,1)\ne0,
\]
\[
\bar P=t^{r_{\rm src}}F^4q\in\overline{\mathcal W}_D,
\qquad
\jmath(G)=qt^2G\quad(G\in\mathcal H_3).
\tag{2}
\]

F、q 使用原固定 d(t)=1+8t 分母框及 primitive 规范。
r_src 是来源指数，返回指数仍是 2。保 D≥4b≥20、
p>D+40、f_D<p 和原好素数门；不改变原来源格或旗标。

在同一原参数 w 上写

\[
t=t(w)=t_1w+O(w^2),\qquad t_1\ne0,\qquad
F(t(w),\bar g(w))=w^hu(w),\qquad u_0\ne0.
\tag{3}
\]

负 fringe 与三个读窗是

\[
s=2h+d_0+2,\qquad 1\le d_0\le13,\qquad
r_{\rm src}=\tau+d_0+2,
\tag{4}
\]
\[
J=s-2,\qquad T=J-13=2h+d_0-13,\qquad L=\ell-2,
\tag{5}
\]
\[
h<T\le2h,\qquad T-h>\kappa=C^2,\qquad
T-h\le L\le h,\qquad 1<\ell<s-13.
\tag{6}
\]

由原 R815 全 nef 界，

\[
\kappa\ge6b-9\ge21,\qquad h>\kappa,\qquad L>\kappa.
\tag{7}
\]

本注新增处理的范围准确为

\[
\boxed{d_0+2\le\tau<\min(h,\ell).}
\tag{8}
\]

严格的两个上界分别用来避开未知二次 Taylor 尾、以及原第四
短块的未知尾；不允许改成等号。暂时不假设 T≤3κ。
该条件只在 §5 的明确推论中加入。

取 R932 已付全部原 Gauss 帽的同预算整因子提升
P^fact=t^(r_src)F̃⁴q̃。若原 P 不是该提升，仍作 R935 的字面重记账：

\[
\Delta=(P-P^{\rm fact})/p\in\mathcal W_D,\qquad
R^\natural=R+\Delta\in\mathcal W_D,
\]
\[
P+pR+p^2S=P^{\rm fact}+pR^\natural+p^2S.
\tag{9}
\]

假定存在原完整解

\[
M^{\rm orig}(P+pR+p^2S)\in p^3\Gamma_4,
\qquad
\mathcal R=\overline{R^\natural}.
\tag{10}
\]

S 保持原来的同一个允许来源；不要求它可自由取整个 WD。
本注只从 (10) 导出必要条件，绝不把若干选定行的相容性当作
完整 p³ 解的充分条件。

## 2. 从原四行读出 raw R 的实际第二法向

记

\[
B=\frac{\mathcal R}{qt^2}
\tag{11}
\]

为原点邻域的真实 Laurent germ，不假设 B∈H3。
将 R934 用于 P^fact、实际基点 R^natural 与 G=0，给同一个
B 的四条真目标。仍置 A=t(w)^(r_src−2)，
e=(EF)(t(w),bar g(w))、e₂=(E²F)(t(w),bar g(w))，
xi 是该原整提升在 h 以下的真实除 p 商。R934(11) 给

\[
\begin{aligned}
 B(t,\bar g)&=0\pmod{w^J},\\
 (EB)(t,\bar g)&=-\frac1a A w^{4h-s}u^4\pmod{w^J},\\
 (E^2B)(t,\bar g)
 &=-24A w^hu\xi e^2
   -\frac8a A w^{3h-s}u^3e\pmod{w^J},\\
 (E^3B)(t,\bar g)
 &=-24A\xi e^3
   -\frac{36}a A w^{2h-s}u^2e^2
   -\frac{12}a A w^{3h-s}u^3e_2\pmod{w^L}.
\end{aligned}
\tag{12}
\]

全部低 t² 门已经由 (10) 支付。式 (12) 仍是原 B 的关系，
不是任意独立的四个函数。特别 xi 没有改成自由输入。

令

\[
R_i(w)=(\mathcal E^i\mathcal R)(t(w),\bar g(w)).
\tag{13}
\]

必须先按完整 Euler 乘积法则乘回 q t²：

\[
R_i=t^2\sum_{j=0}^i\binom ij(E^{i-j}q)(t,\bar g)
                                  (E^jB)(t,\bar g).
\tag{14}
\]

前三式的真实精度因此为 w^s，第四式为 w^ell。
(14) 保留 q 的所有 Euler 导数，不将它们默认为零。

对于 R₂，来自 −8 项的阶数是

\[
r_{\rm src}+3h-s=h+\tau.
\]

同式的 xi 项从 h+r_src=h+τ+d₀+2 起，
2(Eq)(EB) 项从 2h+τ 起，而 E²q·B 从 s 起。
因此，因 h+τ<2h<s，真实第三长行给

\[
\boxed{
R_2(w)=-\frac8a\,q_0t_1^{r_{\rm src}}u_0^3e_0\,
                 w^{h+\tau}+O(w^{h+\tau+1}).
}
\tag{15}
\]

对于 R₃，来自 −36 项的阶数是

\[
r_{\rm src}+2h-s=\tau.
\]

原 xi 项从 r_src=τ+d₀+2 起；e₂ 项和含 Eq·E²B 的项从
h+τ 起；其余项更晚。因此由 τ<ell，

\[
\boxed{
R_3(w)=-\frac{36}a\,q_0t_1^{r_{\rm src}}u_0^2e_0^2\,
                 w^\tau+O(w^{\tau+1}).
}
\tag{16}
\]

这里 (15)、(16) 的 O 记号只表示所需有限前缀；
原其余行不曾被赋值。来源框的 w¹³ 在真正消去同一公共单位
之后才不再出现于 (13)；原物理第四行仍是
epsilon³·w^(13+τ)，并由 τ<ell 严格落在原短块内。
它不是 epsilon³·w^τ 的一个额外物理行。

令 Y=psi(t) 为同一原光滑支，bar g=psi·exp(eta)，则在原有限
Taylor 窗口

\[
\eta=w^h u/e+O(w^{2h}).
\tag{17}
\]

现在对 raw \(\mathcal R\) 作逆 Taylor，而不是对带 t^(−2)
可能极的 B 作逆 Taylor。raw \(\mathcal R\) 及其所有有限个
Euler 导数在 P₀ 正则，所以

\[
(\mathcal E^2\mathcal R)|_C
  =R_2-\eta R_3+O(w^{2h}).
\tag{18}
\]

未知 E⁴R 项从 2h 起；不需给第四短行补精度。
(15)、(16) 的未知尾分别在 s 和 h+ell 起。由 (8)，

\[
h+\tau<\min(s,\ h+\ell,\ 2h).
\tag{19}
\]

因此 −8 与 −(−36) 真正作用于同一已读系数，得到

\[
\boxed{
(\mathcal E^2\mathcal R)|_C
 =\frac{28}{a}q_0t_1^{r_{\rm src}}u_0^3e_0\,
            w^{h+\tau}+O(w^{h+\tau+1}).
}
\tag{20}
\]

p>211 保 28 为单位。这正是 R824 的 −8+36 机制，
此处已在原 R934 负 fringe、同一 q/frame 和真实长度中付清。
没有用它延长 τ=h 或 τ=ell 的未读端点。

另一方面 R934 的全 J 双 jet、乘回 qt²，仍给

\[
\mathcal R|_C\in t^s k[[t]],\qquad
(\mathcal E\mathcal R)|_C
=t^{2h+\tau}A_P(t)\pmod{t^s}.
\tag{21}
\]

由 τ≥d₀+2，2h+τ≥s，故本范围准确得到

\[
\boxed{
\mathcal R|_C\in t^s,\qquad
(\mathcal E\mathcal R)|_C\in t^s,\qquad
\operatorname{ord}_{P_0}((\mathcal E^2\mathcal R)|_C)=h+\tau.
}
\tag{22}
\]

前两项不是恒等于零的全局截面；它们只在原点有已付的高零阶。
最后一项是真正非零，因而 \(\mathcal R\ne0\)。

## 3. 同一原修正必含严格 f₀

由 (12)–(16)，同一 raw R 在原轴的前三个 Euler 值在 w=0
皆为零。原 R335 canonical 列在 t=0 只剩 n=0、1、2 且 j=0；
所以其限制为二次多项式

\[
\mathcal R(0,Y)\in k[Y]_{\le2}.
\]

三个 Euler 值同时为零迫该多项式为零，故

\[
t\mid\mathcal R\quad\text{于 }k[t,Y,d^{-1}].
\tag{23}
\]

令 \(D_{\mathcal R}\sim\mathcal B_D\) 为同一个非零原截面的全零除子。
按原十九角固定框，(23) 给

\[
D_{\mathcal R}\ge f_0.
\tag{24}
\]

只减一个严格 f₀；不删总零纤维，也不宣称 R/t 仍在 WD。
其余十八角及全部残余有效分量仍在同一个全局除子中。

## 4. C 的三种实际重数

置 \(d_D=\mathcal B_D\cdot C\)。
(20) 迫 C 在 \(D_{\mathcal R}\) 中的重数至多二；
若重数至少三，则其二阶 Euler 值在 C 上恒为零。

### 重数 0

\(D_{\mathcal R}-f_0\) 有效且不含 C。
(22) 在 P₀ 给局部交数至少 s−1，所以

\[
d_D-3\ge s-1,\qquad
\boxed{d_D\ge s+2.}
\tag{25}
\]

### 重数 1

\(D_{\mathcal R}-f_0-C\) 有效且不含 C。
在原点的同一局部框写 \(\mathcal R=tFH\)。
沿 C 有

\[
(\mathcal E\mathcal R)|_C=t e_C H_C.
\]

这里 H_C 非零；(22) 因而给 ord(H_C)≥s−1，
而不是误把 ER_C 当作恒零。因此

\[
d_D-3-\kappa\ge s-1,\qquad
\boxed{d_D\ge s+\kappa+2.}
\tag{26}
\]

### 重数 2

\(D_{\mathcal R}-f_0-2C\) 有效且不含 C。
同一局部框中写 \(\mathcal R=tF^2H\)。完整 Euler 乘积法则在 C 上给

\[
(\mathcal E^2\mathcal R)|_C=2t e_C^2 H_C.
\]

2、e_C 都在 P₀ 为单位，故 (20) 给准确阶

\[
\operatorname{ord}_{P_0}H_C=h+\tau-1.
\]

于是

\[
d_D-3-2\kappa\ge h+\tau-1,\qquad
\boxed{d_D\ge 2\kappa+h+\tau+2.}
\tag{27}
\]

H 只是对应上述实际有效除子的局部截面表达式，
不强行把它放进 H1、H2 或一个另选的较小原像。

三支共同给无额外 T 上界的准确必要门

\[
\boxed{
d_D\ge\min(s+2,\ 2\kappa+h+\tau+2)
     =s+2+\Delta_{\rm geom},
}
\tag{28}
\]
\[
\Delta_{\rm geom}
 =\min(0,\ 2\kappa-h+\tau-d_0-2).
\tag{29}
\]

这一最小值不能在未经核实的 quartic 参数中直接删掉。

## 5. T≤3κ 分支与同一完整预算

若进一步明确核实

\[
\boxed{T\le3\kappa,}
\tag{30}
\]

则由 T=2h+d₀−13 和 κ≥21，

\[
2\kappa-h\ge\frac{\kappa+d_0-13}{2}\ge\frac92.
\]

左边为整数，所以 h≤2κ−5。再用 τ≥d₀+2，
(29) 中第二个参数至少为 5，故

\[
\Delta_{\rm geom}=0,\qquad
\boxed{d_D\ge s+2.}
\tag{31}
\]

(30) 是这个推论的实际假设。open 中原 R836 的未闭范围
2κ<T≤3κ 可在同一对象另核条件后使用本推论；
不能把某个不同 quartic 的范围转给该对象。

更一般地，不需要完整 (30)，只要实际参数满足

\[
h\le2\kappa+\tau-d_0-2
\tag{32}
\]

也有 (31)。若 (32) 未付，则始终保 (28) 的最小值。

沿用 R935 的同一源有效除子与 j≥0：

\[
\operatorname{Div}(\bar P)\ge4C+r_{\rm src}f_0+jH_-.
\]

原十九角给 \(\mathcal B_D\cdot f_0=2\)、
\(\mathcal B_D\cdot H_-=4\)，且 \(\mathcal B_D\) 为 nef，
所以

\[
\mathcal B_D^2\ge4d_D+2r_{\rm src}+4j.
\tag{33}
\]

代入完整身份 \(\mathcal B_D^2=2N_D-2D-17\) 与 (28)，得

\[
\boxed{
N_D-2s\ge D+r_{\rm src}+13+2j+2\Delta_{\rm geom}.
}
\tag{34}
\]

因此实际反门为

\[
\boxed{
N_D-2s\le D+r_{\rm src}+12+2j+2\Delta_{\rm geom}
\ \Longrightarrow\
\text{原完整 (10) 不存在解。}
}
\tag{35}
\]

所有参数都来自当前固定原输入；没有换 D、改变旗标或放宽 S。
j 未知时，可保守使用 j=0。

在 (30) 或 (32) 的已核范围中，Δ_geom=0，(34)、(35)
恰延长 R935 的同一预算门。结合 R935，
在全部其它原假设不变并付 (30) 时，范围成为

\[
\boxed{1\le\tau<\min(h,\ell).}
\tag{36}
\]

其中 1≤τ≤d₀+1 由 R935 的首法向证明；
d₀+2≤τ<min(h,ell) 由本注的第二法向证明。
(7) 保 h>21、ell>23，而 d₀+1≤14，
所以旧区间确包含在 (36) 的真实窗口内。

若使用三长松弛 \(\delta_D^{(3)}=N_D-(3s+\ell)\)，
(34) 必须原样改写为

\[
s+\ell+\delta_D^{(3)}
 \ge D+r_{\rm src}+13+2j+2\Delta_{\rm geom};
\tag{37}
\]

左端不能省略 s。局部双 jet 类在 τ≥d₀+2 的自然陪集中为零，
与这里的必要条件并不矛盾：本注使用的是该双 jet 门之后
同一个原 R 的第二法向与全局有效除子。

## 6. 端点和仍待支付的门

τ=d₀+2 时，首法向的自然尾刚从已读 t^(s−1) 后退出，
但 (20) 仍在真实窗口内；由 (7) 该 τ 严格小于 h、ell。
没有给 t^s 的首法向未知系数赋值。

τ=h 时，未知 E⁴R 的二次 Taylor 项与 h+τ 同阶；
τ=ell 时，原第四短行恰少掉所需 w^τ 项。
两端都不在 (8)，本注不给免费加窗。

若 τ 达到或超过 min(h,ell)，或 (35) 未触发，
仍须支付 R928 的同 H1 完整 normal 像、实际受限 S、
整个原 p³/p⁴ 和普通／无穷 p 主门。这里没有从已读局部非零
直接推出一个未经全局来源测试的自由左行。

依赖：R824 原第二法向常数与有限逆 Taylor；R335 原零角列；
R680/R815 完整十九角 nef 与交数；R928 原选定行；
R932 同预算因子提升；R934 全固定双 jet；R935 全同 R 预算方法。

