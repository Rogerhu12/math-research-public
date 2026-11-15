# R827 — 原十九角的精确平衡缺量与完整 profile 的有限交数门

日期：2026-11-15。**状态：下列全 nef 恒等式、实际 r2 角界、临界平衡及完整 profile 的显示充分门已证明。**

R825 排除了全部有界实际 $S$ 次数区域。本文进一步处理原二次临界族的几何位置：当 $\kappa/b^2\to47/12$ 时，全部十九个重数确实趋向 R680 的同一极限类，而不是任取一份具有相同自交数的 nef 类。相应 $S$ 次数准确趋于 $47b/12$。

同时给原来源类的统一交数界
$$
\mathcal B_D C\le D(B_\infty C)+\frac{35}{6}b.
$$
在全部原 $r=2,k_{\rm carry}=0$ profile 中，它把 R795/R802 的完整因子格条件支付为一个显示的有限充分门：
$$
\boxed{p>47b^2+156b+38.}
$$
在此门内，整个所选 profile（含移动 $H$ 的全部低系数）接触核为 $kG$，真实下一行补回单位。这里依然没有认定其唯一整 Schur 缺陷恰含一次 $p$，也没有把因子格核当成原全矩阵核。

## 1. 同一原十九角的完整参数

采用 R815 的基和全部 nef 条件，写
$$
C=bS_0+(u+4b)f-\sum_{i,j}\mu_{ij}E_{ij}.
$$
四条负侧链为 $N=\{0,\alpha_+,\alpha_-,1\}$，长度分别为 $4,4,4,3$；两条正侧链为 $P=\{d,\infty\}$，长度均二。令
$$
s_i=\sum_j\mu_{ij},\qquad
m_i=b-s_i\quad(i\in N),\qquad
w_i=b-s_i\quad(i\in P).
\tag{1}
$$
所有 $m_i,w_i$ 非负。再置
$$
\Delta_P=2u-s_d-s_\infty\ge0,\qquad
\tau=\sum_{i\in N}\frac{m_i}{n_i}+\frac{\Delta_P}{2}.
\tag{2}
$$
$\Delta_P\ge0$ 来自两条长度二链的单调性及
$u\ge\mu_{d1}+\mu_{\infty1}$。
这里 $\Delta_P$ 是显示的几何数，不是原 factor 的整 Schur 余向量。

使用 R680 的固定有理 nef 类
$$
B_\infty=S_0+5f
-\frac14\sum_{\text{三条四步链},j}E_{ij}
-\frac13\sum_{\text{三步链},j}E_{ij}
-\frac12\sum_{\text{两条两步链},j}E_{ij}.
\tag{3}
$$
其平方为 $47/12$。由原交数直接得到
$$
\boxed{
B_\infty C=\frac{47}{12}b+\tau,\qquad
\chi=-K_XC=2b+\sum_{i\in N}m_i+\Delta_P.
}
\tag{4}
$$
本文用 $d=1+8t$ 表示原角多项式；加权边界数始终记为 $\tau$，二者不混用。

## 2. 精确平方和及实际 S 次数

为每条链定义其内部平方差
$$
V_i=\sum_{j=1}^{n_i}\left(\mu_{ij}-\frac{s_i}{n_i}\right)^2\ge0,
$$
并置
$$
\mathcal V=\frac{w_d^2+w_\infty^2}{2}+\sum_iV_i.
\tag{5}
$$

**定理 1。** 对全部上述实 nef 类，准确有
$$
\boxed{
\kappa=C^2
=\frac{47}{12}b^2+2b\tau
-\sum_{i\in N}\frac{m_i^2}{n_i}-\mathcal V.
}
\tag{6}
$$
若 $e=CH_+$ 是原 $S=aY/7$ 的次数，则还准确有
$$
\boxed{
B_\infty C-e
=\frac{w_d+w_\infty}{2}
+\sum_{i\in N}\left(\mu_{i1}-\frac{s_i}{n_i}\right)\ge0,
}
\tag{7}
$$
以及
$$
\boxed{0\le B_\infty C-e\le\sqrt{\frac{47}{12}\mathcal V}.}
\tag{8}
$$

**证明。** 对每一链，
$\sum_j\mu_{ij}^2=s_i^2/n_i+V_i$。
由 (1)–(2)，
$$
u=b-\frac{w_d+w_\infty}{2}+\frac{\Delta_P}{2}.
$$
所以两条正链的平方和与 $2bu$ 合并为
$$
2bu-\frac{s_d^2+s_\infty^2}{2}
=b^2+b\Delta_P-\frac{w_d^2+w_\infty^2}{2}.
$$
而四条负链的平均平方为
$$
\sum_{i\in N}\frac{(b-m_i)^2}{n_i}
=\frac{13}{12}b^2-2b\sum_{i\in N}\frac{m_i}{n_i}
+\sum_{i\in N}\frac{m_i^2}{n_i}.
$$
代入原 $\kappa=4b^2+2bu-\sum\mu^2$ 即为 (6)。

再用 $e=u+4b-\sum_{i\in N}\mu_{i1}$，得 (7)。
各负链首项至少为该链平均，故其右端逐项非负。

为证明 (8)，写 $\varepsilon_{ij}=\mu_{ij}-s_i/n_i$，其和为零。
向量 $\varepsilon_i$ 与第一坐标函数的配对，等于它与
$(1,0,\ldots,0)-(1/n_i,\ldots,1/n_i)$ 的配对，
后者的平方范数为 $(n_i-1)/n_i$。
在 (7) 的全部正交坐标上作一次 Cauchy–Schwarz，
两条 $w_i$ 的贡献为 $1/2+1/2=1$，四条负链的贡献为
$$
3\cdot\frac34+\frac23=\frac{35}{12}.
$$
合计 $47/12$。两条正链的内部平方差只增加 (5) 而不增加左端，所以 (8) 成立。证毕。

(7) 也可直接在原有效锥上核对：
$$
\boxed{
B_\infty-H_+
=\frac12(f_d+f_\infty)
+\sum_{i\in N}\sum_{j=1}^{n_i-1}\frac{n_i-j}{n_i}\,e_{ij}.
}
\tag{9}
$$
这里 $f_i=f-\sum_jE_{ij}$、$e_{ij}=E_{ij}-E_{i,j+1}$ 都是原严格曲线。
(9) 是有效有理除子关系；没有把它误当作 $C$ 的全局分解。

## 3. 原 r2 全部 profile 的统一加权边界

现在取 R792/R797 的同一个实际 primitive 因子，
$$
F(t,0)=\lambda d^cH,\qquad G=F/(\lambda d^c),\qquad z=\deg H\le2.
$$
原 $r=2$ 给 $m_0=3$。
在惰性原域上两个 $h_7$ 角共轭，写其共同亏量为 $m_h$，
另外一条负链亏量为 $m_1$。
按原归一 $G$ 的末 Gauss 值定义
$$
\delta_d=-v_d(G),\qquad \delta_\infty=-v_\infty(G).
$$
原十九角累计式准确给
$$
s_d=2c-\delta_d,\qquad
s_\infty=2u-2c-\delta_\infty,
$$
所以
$$
\boxed{
\Delta_P=\delta_d+\delta_\infty,\qquad
\tau=\frac34+\frac{m_h}{2}+\frac{m_1}{3}
+\frac{\delta_d+\delta_\infty}{2}.
}
\tag{10}
$$
这是实际多项式的角值，不以某个包络的上界冒充其真实重数。

若 $q(t,0)\ne0$，R792 的五个原 profile 逐一给
$$
\boxed{\tau\le7/4.}
\tag{11}
$$
例如最大可能值来自 $h_7$ mask 的 $m_h=2$；
其余四型分别给上界 $5/4,13/12,17/12,5/4$。

若 $q(t,0)=0$，R797 给同一实际因子的某个返回 mask
$$
A_*=(t-1)^i d^j h_7^k,\qquad a_*=i+j+2k\le6-3z,
$$
以及全部必要不等式
$$
m_h\le\frac{4k+1}{3},\quad m_1\le i,\quad
\delta_d\le\frac{2j+1}{3},\quad
\delta_\infty\le\frac{13-2a_*}{3}.
\tag{12}
$$
只放松整数取整上界，不改变实际 $F$ 或原修正。
将 (12) 代入 (10)，所有 $i,j,k$ 项准确抵消：
$$
\tau\le\frac34+
\frac{4k+1+2i+(2j+1)+(13-2i-2j-4k)}6
=\frac{13}{4}.
$$
因而全部实际 r2 profile 统一满足
$$
\boxed{0\le\tau\le13/4.}
\tag{13}
$$
同时各 $m_i,\Delta_P$ 均有绝对上界，与 $b,p$ 无关。
例如 $m_h\le4,m_1\le6,\delta_d\le4,\delta_\infty\le4$ 已足够；
使用具体 profile 时仍保其更小准确上界。

(13) 的最大可能值只在原最大角组合
$m_h=3,m_1=0,\delta_d=\delta_\infty=1$ 取得。
确实 (12) 全部须取等，整数性迫 $k=2,j=1,i=0,z=0$；
这正是 R802 的 $h_7^2d$ 例外。此句只分类可能等号参数，
不制造该类的强接触因子或任何深提升。

## 4. 满自交主阶迫使整个原十九角平衡

考虑实际 r2 因子序列，$b\to\infty$。
由 (6)、(13) 及各 $m_i$ 有界：

**推论 2。** 若
$$
\frac{\kappa}{b^2}\longrightarrow\frac{47}{12},
$$
则
$$
\boxed{
\begin{aligned}
&\mathcal V=o(b^2),\qquad u/b\to1,\\
&\mu_{ij}/b\to1/n_i\quad\text{对全部十九个重数},\\
&e/b\to47/12.
\end{aligned}}
\tag{14}
$$

**证明。** (6) 的非负平方和除以 $b^2$ 后趋零。
故 $w_d,w_\infty=o(b)$，每条链的内部偏差均为 $o(b)$。
四条负链总和为 $b-O(1)$，两条正链总和为 $b-o(b)$，
所以每个重数都有显示极限。
由 $u=b-(w_d+w_\infty)/2+\Delta_P/2$ 得 $u/b\to1$，
由 (4)、(8) 得最后一式。证毕。

若有更强的 $\kappa=47b^2/12+O(b)$，
同一证明给 $\mathcal V=O(b)$，
全部偏差、$u-b$ 和 $e-47b/12$ 都为 $O(\sqrt b)$。
这些是整族结论，未假定某个有限次数的 profile 已有不可约代表。

因此 R825 的一般两侧界在实际满自交临界族中收紧为唯一的 $S$ 次数主比 $47/12$。
这里“平衡”只指原重数的显示极限，
不认接触矩阵饱和、因子可提升或指定余类非零。

## 5. 完整原来源类的统一有限交数上界

令 $\mathcal B_D$ 是 R555/R680 的同一个整个来源除子，
$D\ge3$，
$$
H^0(X,\mathcal O_X(\mathcal B_D))
=d^{\lfloor D/2\rfloor}\overline{\mathcal W}_D.
$$
它的径向次数为 $D$，纤维参数为
$u_D=2\lfloor D/2\rfloor+4$。
全部原重数表具有以下准确性质：

- 三条四步链的序列非增，总和为 $D-2$；
- 三步链的序列非增，总和为 $D-1$；
- 两条两步链均为 $(\lfloor D/2\rfloor,\lfloor D/2\rfloor)$。

这些是原整数重数，未改成极限分数。
记 $\epsilon_D=D\bmod2$，则
$u_D-D=4-\epsilon_D$。

**定理 3。** 对每个原 nef 类 $C$，
$$
\boxed{
\mathcal B_D C
\le D(B_\infty C)+\frac{35}{6}b.
}
\tag{15}
$$
常数 $35/6$ 在全实 nef 锥上尖锐。

**证明。** 对两个非增实序列 $(x_j),(y_j)$，有
$$
\sum_jx_jy_j-\frac{(\sum_jx_j)(\sum_jy_j)}n
=\frac1n\sum_{j<k}(x_j-x_k)(y_j-y_k)\ge0.
\tag{16}
$$
对一条四步链，将来源的整数重数和 $C$ 的重数代入 (16)，得
$$
\sum_j\left(\frac D4-\mu_{ij}(D)\right)\mu_{ij}(C)
\le\frac12 s_i(C)\le b/2.
$$
三步链同理至多 $b/3$。
每条两步链的差为常数 $\epsilon_D/2$，
故两条合计至多 $\epsilon_Db$。

现在准确展开
$$
(\mathcal B_D-DB_\infty)C
=(4-\epsilon_D)b+
\sum_{i,j}\left(\frac D{n_i}-\mu_{ij}(D)\right)\mu_{ij}(C).
$$
应用上述逐链界，得到
$$
(4-\epsilon_D)b+3b/2+b/3+\epsilon_Db=35b/6.
$$
这证明 (15)，没有舍掉来源整数表的误差。
取实 nef 类 $C=B_\infty$ 时所有链为常数序列、总和为一，
每一步都取等，故该统一常数尖锐。证毕。

(15) 对整个来源类成立，不只对一个试验子格；
它也没有将实际 $(b,p)$ 的曲线替换成 $bB_\infty$。

## 6. 全部 r2 profile 的显示一维核门

R795/R802 已为每个完整实际 profile 支付一个共同返回乘子：
通常 $\epsilon=0$，整个 profile 返回 $\overline{\mathcal W}_b$；
唯一最大角包络取 $\epsilon=1$，以 $th_7Y$ 返回
$\overline{\mathcal W}_{b+1}$。
后者不能把新增 charge 隐去。两个返回在原点都恰增加一阶。

所以准确的完整 profile 门是
$$
h+1>\mathcal B_{b+\epsilon}C.
\tag{17}
$$
这里 profile 含常数 charge $H$ 的全部允许低系数；
不以较小 $H^0(X,\mathcal O_X(C))$ 的 $h>\kappa$ 代替 (17)。

对当前全部 r2 范围，由 (4)、(13)、(15) 和 $\epsilon\le1$，
$$
\begin{aligned}
\mathcal B_{b+\epsilon}C
&\le(b+\epsilon)\left(\frac{47}{12}b+\tau\right)
+\frac{35}{6}b\\
&\le\boxed{\frac{47}{12}b^2+13b+\frac{13}{4}}.
\end{aligned}
\tag{18}
$$
于是得到一个不需另枚举十九角类的充分门
$$
\boxed{h+1>\frac{47}{12}b^2+13b+\frac{13}{4}.}
\tag{19}
$$
在原 $s=2h+2,p=12h+11$ 窗，(19) 准确等价于
$$
\boxed{p>47b^2+156b+38.}
\tag{20}
$$
不将其宣称为必要条件；若不满足它，仍可使用更强的实际 (17)。

**推论 4。** 在全部原 r2 profile、原 R795/R802 的低轴整性与精确接触条件以及 (20) 下：

1. 整个所选 profile 的模 $p$ 接触核恰为 $kG$。
2. 用真实 $H$ 的最高系数归一后，全部其余 profile 列具有单位最大子式，包含移动 $H$ 的低系数。
3. 加入真实第 $h$ 行后，整个 profile 矩阵全列为单位。
4. 原长度 $h$ 的整矩阵只剩一个实际 Schur 余向量 $\Delta\in p\mathcal O^{h-N+1}$；factor 首 Bockstein 由 $\Delta/p$ 读取，其赋值仍未知。

这些断言分别正是 R795/R802 在 (17) 下已证明的完整结论，
本文以 (18)–(20) 支付其有限参数输入。
没有把 $\Delta/p$ 写成自由 Gaussian 修正或先认其非零。

若实际临界族满足
$$
\kappa/b^2\to47/12,\qquad h/\kappa\to9/8,
$$
则 $h/b^2\to141/32>47/12$，(19) 最终自动成立。
在这个渐近范围不再需要额外假设整个 profile 的一维核门；
有限参数仍必须保 (17) 或 (19)。

## 7. 尚须接回的完整原矩阵

(14) 约束剩余临界曲线的所有原重数；
(20) 付其完整 factor profile 的真实唯一核和单位补空间。
两者都没有排除该曲线，也没有证明单列 $\Delta$ 的 p 阶恰为一。

原 R790 的完整 forcing 配对依然含固定主部、实际 $V^3$ carry 和
$\langle\nu,\Delta/p\rangle$；
原所有非 $F^2$ 列、两条十三行、同一个 $R$ 的高尾以及下一位仍须同时满足。
R824 的四次纯幂排除也只在它的完整物理来源范围内成立，
不能把本文的三次 factor 分类套成所有四块首核的分类。

主目标仍是固定一条秩至少二曲线，在无穷不同素数上支付完整中央非零和全 Selmer 结论。本文继续收紧其真实几何与整矩阵输入，不改变完成标准。

依赖：
[R680 原整数来源类及极限类](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)；
[R815 全部原 nef 条件](R815-complete-original-mori-nef-cones-and-s-fibration.md)；
[R825 全 nef 上缺量](R825-original-nef-upper-gap-and-bounded-s-degree-exclusion.md)；
[R792](R792-original-nonzero-constant-charge-classification-and-cubic-extension.md)；
[R797](R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)；
[R795 原完整因子格一维核](R795-original-factor-contact-one-dimensional-kernel-and-unit-next-row.md)；
[R802 移动因子及唯一新增 charge](R802-original-moving-factor-return-and-unique-one-charge-exception.md)。

全文为交数、平方和、单调序列恒等式及已付整返回的符号证明；没有数学程序执行或新增可重算输出。
