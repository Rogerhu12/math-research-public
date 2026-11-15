# R788 — 原五型中 b=3 强接触因子的全素数排除

日期：2026-11-15。**状态：以下全素数排除已证明。** 公共精确计算与原十九角几何共同排除了最小三次因子窗口；更高 b、其他合法 r/k/mq 窗口和主目标继续保持开放。

## 1. 定理及其真实范围

保 R782 的原系数域 $\mathbf F_p$，以及
$$
p=12h+11=6s-1>101,\qquad s=2h+2,\qquad
r=2,\quad\ell=1,\quad k_{\rm carry}=0,\quad f_D<p.
\tag{1}
$$
假设原 primitive 不可约因子满足
$$
qt^2F^3\in\overline{\mathcal W}_D,\qquad m_q=0,\qquad
b=\deg_YF=b_0=3,\qquad D\ge9,
$$
$$
F(0,1)=0,\qquad F_Y(0,1)q(0,1)\ne0.
\tag{2}
$$
用 R495 同一十九角曲面上严格变换 $C$ 的准确自交数
$\kappa=C^2$。这里的 $\kappa$ 是几何整数，不是普通分支的缩放参数。

**定理。** 不存在同时满足 (1)、(2) 及
$$
\boxed{
F(t,g(t))\in t^h\mathbf F_p[[t]],\qquad h\ge\kappa+14
}
\tag{3}
$$
的原因子 $F$。

最后一条正是 R750 在当前 $r=2$ 窗口的
$T_M-h=h-13>\kappa$，不是另加的任意高接触假设。
此定理覆盖所有允许的素数，未将有限素数样本外推。
证明分为：两个有理最大子式支付所有大素数；准确几何把剩余强窗口压到一个有限特征；该特征上的原非齐次系统不相容。

不使用原三条中央零来给因子各列添零，不替换已固定的整提升或同一个首次修正。
结论仅排除 (2) 的 $b=3$；$b\ge4$ 仍须继续。

## 2. 五型的实际系数和两个最大子式

记
$$
d=1+8t,\qquad h_7=7+4t+16t^2,\qquad
\rho=d\Theta^{17}.
$$
R782 已证明，可以按一个常数单位规范
$$
F(t,0)=d^c,\qquad G=F/d^c,\qquad G(t,0)=1,
\tag{4}
$$
且 $G$ 属于五型之一。
因 $b=3$，其每条非恒定 charge 都没有额外的 $t$ 因子。
准确写成
$$
G=1+\sum_{n=1}^3Y^n
 h_7^{B_n}(t-1)^{C_n}d^{-Z_n}p_n(t),
\qquad\deg p_n\le E_n.
\tag{5}
$$
下表的每组三元组按 $n=1,2,3$ 排列：

| mask | $(B_n,C_n,Z_n,E_n)$ | 非恒定列数 $N_A$ | 使用的最高 Taylor 行 |
|---|---|---:|---:|
| $1$ | $(1,1,0,2),(1,1,1,7),(1,1,1,12)$ | 24 | 25 |
| $t-1$ | $(1,0,0,2),(1,1,1,7),(1,1,1,11)$ | 23 | 24 |
| $(t-1)^2$ | $(1,0,0,2),(1,0,1,8),(1,1,1,11)$ | 24 | 25 |
| $h_7$ | $(0,1,0,3),(0,1,1,9),(1,1,1,11)$ | 26 | 27 |
| $d^2$ | $(1,1,1,2),(1,1,1,7),(1,1,2,12)$ | 24 | 25 |

这些是 R782(19) 的全部允许乘子，未取随机或缩小列集。
在 $Y=\rho$ 上，列准确为
$$
t^j h_7^{B_n}(t-1)^{C_n}d^{\,n-Z_n}\Theta^{17n},
\qquad 0\le j\le E_n .
\tag{6}
$$
原低轴给 $g\equiv\rho\bmod t^s$，而 $h<s$。
故在需要的接触行中，(6) 与原实际因子完全相同。

将 (6) 的有理系数矩阵记作 $A_A$。
在每一行分别取全部分母的最小公倍数，得到整数矩阵 $\mathcal A_A$。
另外添常数列 $1$。
我们使用两组完整最大子式：
$$
I_{A,1}=\{0,1,\ldots,N_A\},\qquad
I_{A,2}=\{0,2,3,\ldots,N_A+1\}.
\tag{7}
$$
常数列在第零行为 $1$，其他行为 $0$，
所以两个行列式等于非恒定列在正行 $1,\ldots,N_A$、
$2,\ldots,N_A+1$ 上的整数行列式，记为 $\Delta_{A,1},\Delta_{A,2}$。

公开精确执行证明两式均非零，并给出其 gcd 的完整素因子支持：

| mask | $\gcd(\Delta_{A,1},\Delta_{A,2})$ 的素因子集合 |
|---|---|
| $1$ | $2,3,5,11,13,23,29,41,47,53,59,71,181,211$ |
| $t-1$ | $2,3,5,11,13,23,29,41,47,53,59$ |
| $(t-1)^2$ | $2,3,5,11,13,23,29,41,47,53,59$ |
| $h_7$ | $2,3,5,11,13,23,29,41,47,53,59$ |
| $d^2$ | $2,3,5,11,13,23,29,41,47,53,59,71,181,211$ |

这里是实际整数 gcd 的完整分解支持，不是只列出试除发现的一部分因子。
producer 的循环把全部所列小素数除尽后，余因子准确为 $1$。
每个原子式的完整 SHA256 及 gcd 指数均由下述公开 run 保留。

### 2.1 有理系数及分母的原规范

精确生成式为
$$
q_1=-\frac25,\qquad
q_j=q_{j-1}\frac{6j-4}{6j-1}\quad(j\ge2),\qquad
\log\Theta=-\sum_{j\ge1}\frac{q_j}{3j}t^j .
\tag{8}
$$
因此 $\rho'(0)=154/15$，与原低轴一致。
对 $\Theta^{17n}$ 使用普通指数系数递推
$$
a_0=1,\qquad
a_k=\frac1k\sum_{j=1}^k
 j(17n)[t^j]\log\Theta\;a_{k-j}.
\tag{9}
$$
再与 (6) 的全部整数多项式卷积。

在最高行27以前，所有分母的素因子至多为 $6\cdot27-1=161$：
(8) 的因子为 $3j,6j-1$，(9) 只另除 $k\le27$。
所以对每个 $p>211$，各行清分母都是合法单位操作。
表中 gcd 不含该 $p$，故两个最大子式至少一个模 $p$ 为单位。
于是常数列和全部非恒定列在行 $0,\ldots,27$ 已线性独立。

特别，若 $p\ge347$ 且 $p=12h+11$，则 $h\ge28$。
常数列不能由其余列表示为相反数，故
$$
\boxed{
p\ge347\quad\Longrightarrow\quad
G(t,g)\notin t^h
\quad\text{对五型中全部 }G.}
\tag{10}
$$
这一步甚至不需要不可约、光滑或 (3) 的自交数门。
它是同一完整原矩阵上的全素数结论。

## 3. b=3 的十九角给出准确的小自交数分类

以下只用 (2)、(4)、R782 全角条件及 R495 的实际吹起公式。

令
$$
u=\max_{0\le n\le3}(\deg_t f_n-4n),\qquad
v=u-c\ge0,\qquad F=\sum_{n=0}^3f_nY^n .
\tag{11}
$$
R782 的端点亏损记为 $\delta_d,\delta_\infty\in\{0,1\}$，
且 $\delta_d+\delta_\infty\le1$。
其分母和次数帽给
$$
c\le\left\lfloor\frac{3+\delta_d}{2}\right\rfloor,\qquad
0\le v\le1+\delta_\infty.
\tag{12}
$$

由于 $f_3(0)\ne0$，原 $t=0$ 四步链的全部重数为零。
设两个 $h_7$ 角的共同重数序列为
$\boldsymbol\mu_h$（长度4），$t=1$ 为
$\boldsymbol\mu_1$（长度3），另外两条链为
$\boldsymbol\mu_d,\boldsymbol\mu_\infty$（均长度2）。
$p\equiv5\bmod6$ 时 $h_7$ 不可约，因此前两条几何链确用同一个序列。

每条序列非负、非增。
这也可从 R495 的累计值是有限多条仿射函数的最小值直接看出，
没有另加光滑中心或一般位置假设。
其累计末值为
$$
\sum\mu_h=3-m_h\le3,\qquad
\sum\mu_1=3-m_1\le3,
$$
$$
\sum\mu_d=2c-\delta_d,\qquad
\sum\mu_\infty=2v-\delta_\infty.
\tag{13}
$$
常数项 $f_0=d^c$ 在两条二步链的第一步又给
$\mu_{d,1}\le c$、$\mu_{\infty,1}\le v$。
结合非增性和 (13)，得到实际的准确二步序列
$$
\boxed{
\boldsymbol\mu_d=(c,c-\delta_d),\qquad
\boldsymbol\mu_\infty=(v,v-\delta_\infty).}
\tag{14}
$$
负分量当然不允许；因此当 $\delta=1$ 时相应的 $c$ 或 $v$ 至少为1。

原交数公式现在是
$$
\kappa
=36+6(c+v)
-2\sum\mu_h^2-\sum\mu_1^2
-\bigl(c^2+(c-\delta_d)^2\bigr)
-\bigl(v^2+(v-\delta_\infty)^2\bigr).
\tag{15}
$$
因两条前述序列的总和不超过3，
$$
2\sum\mu_h^2+\sum\mu_1^2\le27.
$$
定义
$$
\epsilon(q,\delta)=6q-\bigl(q^2+(q-\delta)^2\bigr).
$$
由 (12)—(14)，其允许值只为
$$
\epsilon(0,0)=0,\qquad
\epsilon(1,0)=4,\qquad
\epsilon(1,1)=5,\qquad
\epsilon(2,1)=7.
\tag{16}
$$
所以
$$
\boxed{\kappa\ge9.}
\tag{17}
$$

若进一步 $\kappa\le11$，则 (15)、(16) 迫
$c=v=\delta_d=\delta_\infty=0$。
从最大平方和27下降，任一长度4或长度3序列若不为
$(3,0,\ldots,0)$，平方和至少下降4。
因此该小自交数范围只有
$$
\boxed{
c=u=0,\quad
\boldsymbol\mu_h=(3,0,0,0),\quad
\boldsymbol\mu_1=(3,0,0),\quad
\boldsymbol\mu_d=\boldsymbol\mu_\infty=0,\quad
\kappa=\chi=9.}
\tag{18}
$$
这里 $\chi=-K_XC$；其原公式为
$9+2m_h+m_1+\delta_d+\delta_\infty$。

(18) 的整个允许来源也准确可写出。
第一步重数3迫
$h_7^n(t-1)^n\mid f_n$；$u=0$ 迫 $\deg f_n\le4n$。
故所有候选都属于
$$
\boxed{
F(t,Y)=1+
 \sum_{n=1}^3\bigl(h_7(t)(t-1)Y\bigr)^n p_n(t),
\qquad \deg p_n\le n.}
\tag{19}
$$
这保整个小自交数来源，不只取若干代表。

## 4. 剩余 p=311 的真实非齐次方程

由 (3)、(17)，必有 $h\ge23$。
若 $p<347$，则 $23\le h\le27$。其中
$$
12h+11\in\{287,299,311,323,335\};
$$
$287=7\cdot41$、$299=13\cdot23$、
$323=17\cdot19$、$335=5\cdot67$。
所以唯一可能的素数是
$$
\boxed{p=311,\qquad h=25.}
\tag{20}
$$
此时 (3) 迫 $\kappa\le11$，只能使用 (19)。

置
$$
V(t)=h_7(t)(t-1)\rho(t).
$$
对全部九个原未知系数定义
$$
\mathsf H_{311}(i;(n,j))
=[t^{i-j}]V(t)^n,\qquad
0\le i<25,\quad1\le n\le3,\quad0\le j\le n.
\tag{21}
$$
准确接触条件是
$$
\boxed{
\mathsf H_{311}\mathbf x=(-1,0,\ldots,0)^T
\quad\text{于 }\mathbf F_{311}.}
\tag{22}
$$
这是固定小自交数类中整个允许来源，不从五型任取一个代表。
系数由 (8)、(9) 生成；所用所有分母在311处为单位。

公共精确执行对 (22) 做完全模311行消元，得到
$$
\boxed{
\operatorname{rank}[\mathsf H_{311}\mid(-1,0,\ldots,0)^T]
>
\operatorname{rank}\mathsf H_{311}.}
\tag{23}
$$
因此 (22) 无解，连未加不可约性和光滑性的扩大来源也不含候选。
与 (10)、(17)—(20) 联合，证明定理。

这里几何门不可省略：同一次精确执行表明，
$p=263,h=21$ 的五型原接触方程都有解；
$p=311,h=25$ 的最大 $h_7$ 型原接触方程也有解。
这些接触解不能满足所需的实际 $\kappa$ 强窗。
所以本篇并没有证明这些特征上的五型全接触矩阵都无解。

## 5. 有限几何检验的完整枚举规则

为使 (23) 不依赖未显示的来源筛选，producer 同时实施了以下完整枚举，
并在其公开输出中单列 $p=311$ 的唯一允许几何类。

对每个五型最大亏损，逐一取其允许的实际
$m_h,m_1,\delta_d,\delta_\infty$；
取 (12) 允许的 $c,u$。
依 (13) 枚举全部非负非增序列，并保常数项约束。
由 (15) 精确计算 $\kappa$，由
$$
\chi=9+2m_h+m_1+\delta_d+\delta_\infty
$$
计算规范交数；保原伴随必要条件
$\kappa\ge\chi-2$ 及 $\kappa-\chi$ 为偶数。
每个实际因子必出现，不把它的重数改成型的最大预算。

对于一组累计值
$V_j^h,V_j^1,V_j^d,V_j^\infty$，其原全部系数来源由
$$
f_n=h_7^{b_n}(t-1)^{c_n}d^{z_n}p_n(t)
\quad(1\le n\le3)
$$
准确包含，其中
$$
\begin{aligned}
b_n&=\max\left(0,\max_{1\le j\le4}
       \left\lceil\frac{V_j^h-3+n}{j}\right\rceil\right),\\
c_n&=\max\left(0,\max_{1\le j\le3}
       \left\lceil\frac{V_j^1-3+n}{j}\right\rceil\right),\\
z_n&=\max\left(0,\max_{1\le j\le2}
       \left\lceil\frac{V_j^d-n}{j}\right\rceil\right),\\
K_n&=\min\left(u+4n,\ 
       \min_{1\le j\le2}
       \left\lfloor\frac{ju+(4j+1)n-V_j^\infty}{j}\right\rfloor\right),\\
\deg p_n&\le K_n-2b_n-c_n-z_n .
\end{aligned}
\tag{24}
$$
负帽时该组为空。
这些条件由 R495 各累计值逐项解出，是每个所列几何类的整个线性包络。
它可能还包含角重数更大的特例；用这样较大的来源证明不相容是合法的。
右端始终是实际 $-d^c$，而不是任意齐次核问题。

公开执行生成180个允许的完整几何类。
按 $h=(p-11)/12$ 和 $\kappa+14\le h$ 筛选后，对
$101<p\le587$ 的所有有关素数共检查775个不同非齐次矩阵。
其中 $p=263$ 无允许几何类；
$p=311$ 恰有一类，它正是 (18)、(19)，并且不相容。
其余有关素数的允许类也全不相容。
定理只需要第2—4节较短的推论；这个枚举完整保留了所用来源的复现方式。

模 $p$ 消元仅处理当前特征上的实际接触方程，
不把模 $p$ 核认作特征零饱和核。
第2节的大素数门则先证明真实有理子式存在、再控制其所有共同坏素数；
两种用途没有混同。

## 6. 公开精确执行和复现信息

唯一数学执行为公共 GitHub Actions：

- producer：[check-r788-original-b3-contact-all-primes.py](../scripts/check-r788-original-b3-contact-all-primes.py)；
- 参数：--max-order=48；使用 Python 标准库中的精确整数和 Fraction，不依赖浮点运算；
- 来源提交：bec1dc708a3b6cf7c2a5482073079f8625d093b0；
- [公开 run 43735456684](https://github.com/Rogerhu12/math-research-public/actions/runs/43735456684)，job132876943772；
- producer SHA256：f729371aa6867a84e1a4de18abdcd6d2451987e7174809a0a19269631c68da0e；
- 完整标准输出13045字节，SHA256：151b4768e186744be1f64817efaf5f5796f9a93bbfb7b4dafc941622e3007caf。

producer 的整数行列式用带换行的 Bareiss 消元，
每一步都检验除法余数准确为零。
各非零最大子式和实际 gcd 均在整数中计算；
gcd 的小素数试除结束后要求剩余因子为1，
因此没有依赖不完全因数分解。
有限域消元保全部行与原非齐次右端，
不相容的判据正是出现零系数行、非零右端。

程序还逐项检查原 $\rho'(0)=154/15$、
所有有理行分母的支持、允许的有界运行参数和输出预算。
最终报告 all_strong_b3_excluded=true、remaining_candidates=[]。
不把生成的矩阵、长有理行列式或标准输出另存仓库或 Release；
以上 producer、参数、公开 run 与哈希足以重新生成全部数值。

## 7. 关闭的分支与继续的原问题

R768 原 $r=1,b_0\ge3$ 窗口曾被次数门排空；
本篇进一步排除实际 $r=2,m_q=0$ 强窗的最小 $b=b_0=3$。
这是一个新的全素数存在性结论，不是新的 Sha 结论。

仍保持：

- $r=2,b_0=3$ 的 $b\ge4$ 五型因子；
- $m_q=1$ 及其它合法 $r,k$ 窗口；
- R787 全 $F^2$ 块之外的同一个首次修正、全部 normal、两条十三行和下一精度；
- 原固定曲线在无穷不同素数上的完整中央非零。

本篇未把 $b=3$ 的两个子式模式自动推广到变动的 $b$。
更高次数若要使用相同方法，必须支付该次数的完整原矩阵、
共同坏素数和实际几何类，而不能从这里的固定证书直接推断。

依赖：
[R782](R782-original-r2-five-profile-factor-and-inhomogeneous-contact-gate.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R787](R787-original-factor-return-and-whole-square-source-normal-kernels.md)。
