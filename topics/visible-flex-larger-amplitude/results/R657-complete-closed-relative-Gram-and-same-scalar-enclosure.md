# R657：完整闭场的连续 relative Gram 包围与 def1 胞839的真实误差

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**状态：已证明的完整连续包围算法；同一 def1 父一个完整胞实际应用。** 在胞839的全部径向位置及全部角度上，准确场的 relative Gram 算子范数满足准确有理界

$$
0.10186124
\ \le\ \sup_{\mathrm{cell}\,839,\ \phi\in\mathbb R/2\pi\mathbb Z}
\|\mathcal E(s,\phi)\|_{\mathrm{op}}
\ \le\ 0.10187890. \tag{1}
$$

因此这个父在本胞不可能只靠证书加密达到 $10^{-6}$；仍须改变完整求解未知量。下界来自同一次向外计算中的准确点，非有限 Gauss 读数冒充连续上界。新核不使用 [R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md) 的大分量盒相乘：先准确展开径向 Gram 多项式，保留近等距抵消，再付角区间、同一准确标量和向外算术预算。未扫其他921胞，不登记全闭族已完成。

## 1. 同一准确场与同一 g

固定输入为完整空间实际一步所得 work/fullclosed_solver/gauss-h2-projected-first-fixed/final.npz，SHA-256：

def1ccbded6c463a014a71a39f259c59501412d5c84afec07ce7253c9dc34f5d。

其 J923、M160、全部自由变量、core 和解析 lift 均按 R656 的准确数学解释：自由 binary 数是准确实参数；入口派生 T 系数由准确 $-\nu_jc_j$ 重建；全部 q 三 jet 在原 $s_i=\alpha_iS+\beta_i$ 节点上作共享 quintic。S/R 消费原 FullHold 准确盒，没有改用浮点 mesh 作为另一目标。这里 H 为

$$H={4303641444839649\over2251799813685248};$$

lift 宽仍为准确 binary $w=3602879701896397/72057594037927936$。当前 def1 与 R656 的2038父不同，本条不继承其任何几何数值。

材料角为 $\theta=\Theta(\phi)$，$\rho=\Theta_\phi>0$；目标仍是原准确 Hold 标量定义的

$$g=ds^2+a(s)^2d\theta^2.$$

所以在 $(s,\phi)$ 参数中，相对度量误差准确为

$$
\mathcal E=
\begin{pmatrix}
|F_s|^2-1&
{F_s\cdot F_\phi\over a\rho}\\
{F_s\cdot F_\phi\over a\rho}&
{|F_\phi|^2-a^2\rho^2\over a^2\rho^2}
\end{pmatrix}. \tag{2}
$$

它正是原 ClosedGram 三项组成的对称相对矩阵，不是把目标 a 的样值当作几何。

原符号节点／标量盒报告 SHA-256：

fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692。

同 g 标量输入 pulse-a5-complete-base.json.gz 的 SHA-256：

826106b40f06ddece0500bd5ac7ea1a14ad4edbb9fab0664e3de46a76a76f196。

这个输入仅提供已定义的原标量 knots／initial law；其旧 pulse 曲面不是当前几何场。原 FullHold 源、整数 oracle 和 Hold 源身份分别为 a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670、babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0、ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1。本次消费其已给 a/S/R 盒，没有重跑旧积分证书。

## 2. Gram 的准确抵消展开

沿 R656 的旋转 $\phi$ 正交架，令

$$
F=q+f e_r+\chi H e_z,\quad
e_r=(\cos\delta,\sin\delta,0),\quad
e_\theta=(-\sin\delta,\cos\delta,0),\quad
f=\chi(R+S-s).
$$

设

$$
U=q_s,\quad T=q_\phi,\quad c=f_s,\quad d=H\chi_s.
$$

这里 $q_\phi$ 已包含旋转架连接项，即 R656(7)，不是把三个分量作普通角导数后忘记框架旋转。于是

$$
F_s=U+c e_r+d e_z,\qquad
F_\phi=T+f\rho e_\theta. \tag{3}
$$

先准确使用 $|e_r|^2=|e_\theta|^2=1$、$e_r\cdot e_\theta=0$ 以及二者与 $e_z$ 正交，避免将同一单位向量分别区间化再平方而损失抵消。若 A 是第5节的准确 a 的多项式近似，三个分子写成

$$
N_E=|F_s|^2-1,\quad
N_M=F_s\cdot F_\phi,\quad
N_G=|F_\phi|^2-A^2\rho^2.
$$

每一个都具有

$$N=P+C\cos\delta+S_1\sin\delta \tag{4}$$

的准确形式，其有限角部分如下：

| 分子 | P | C | $S_1$ |
|---|---|---|---|
| $N_E$ | $\lVert U\rVert^2-1+c^2+d^2+2dU_z$ | $2cU_R$ | $2cU_T$ |
| $N_M$ | $U\cdot T+dT_z$ | $cT_R+f\rho U_T$ | $cT_T-f\rho U_R$ |
| $N_G$ | $\lVert T\rVert^2+(f^2-A^2)\rho^2$ | $2f\rho T_T$ | $-2f\rho T_R$ |

表中 T 的下标 R/T/z 表示旋转架分量，$S_1$ 是正弦项系数而非径向端点 S。所有 P/C/$S_1$ 的普通角频率至多 $m=4M$；$\delta$ 的频率至多 $2M$。**(4) 本身在活动 lift 上不是有限带宽函数。**

在一个真实 $\chi$ 多项式 piece 内，$F_s$ 径向次数至多5、$F_\phi$ 至多6。因此 $N_E,N_M$ 的次数分别至多10、11，$N_G$ 至多 $\max(12,2n)$，其中 n 是 A 的次数。源码可为统一数组升阶，升阶不改变函数。

### 径向乘积在取盒之前完成

若 p、q 的 Bernstein 次数分别为 u、v，系数为 $p_i,q_j$，则

$$
(pq)_k=
\sum_{i+j=k}
{\binom ui\binom vj\over\binom{u+v}k}\,p_iq_j. \tag{5}
$$

该式由 Bernstein 基的定义直接相乘得到。源码用准确 Fraction 权及向外算术完成 (5)，并在每个控制点上先相加、相减形成表中的完整分子。径向 De Casteljau 细分也对这些完整分子及其角导数进行。只有这些抵消已经完成后才取 Bernstein 凸包。

这与先给 $F_s,F_\phi$ 大区间再相乘不同：例如 $|F_\phi|^2$ 与 $A^2\rho^2$ 的系数先相减；若准确分子很小，其保留的完整角导数也能很小。源码没有把原分量大小当成不可避免的最终度量误差。

## 3. 全角连续包围：有限部分与解析部分分别支付

取 Q 个等距角点，$\Delta=\pi/Q$。网格三角值均由 f512 的严格区间 radix-two 变换求得。对带宽不超过 m 的任何实三角多项式 p，[R641(6)–(7)](R641-continuous-Gram-certificate-for-one-pulse-cell.md) 给出

$$
\|p\|_\infty\le
{\max_{\mathrm{grid}}|p|\over 1-m^2\Delta^2/2}
\qquad\text{当 }1-m^2\Delta^2/2>0. \tag{6}
$$

它同样用于 p 的任一导数。源码对 P/C/$S_1$ 使用 $m=4M$，对 $\delta$ 使用 $2M$，每个径向控制点分别支付。

### 完整分子在网格上的前二阶角导数

先严格包围 $\delta$ 及其导数，再用 R656(8) 的显式有理 Taylor 余项计算完整 $\sin\delta,\cos\delta$。网格上

$$
\begin{aligned}
(\cos\delta)'&=-\sin\delta\,\delta',&
(\sin\delta)'&=\cos\delta\,\delta',\\
(\cos\delta)''&=-\cos\delta\,(\delta')^2-\sin\delta\,\delta'',&
(\sin\delta)''&=-\sin\delta\,(\delta')^2+\cos\delta\,\delta''.
\end{aligned} \tag{7}
$$

以 Leibniz 公式在 (4) 的完整和上形成 N、N′、N″；它们的抵消没有被拆成分量绝对值之和。径向乘积的角导数同时用

$$
(pq)^{(k)}=\sum_{j=0}^k\binom kjp^{(j)}q^{(k-j)} \tag{8}
$$

准确形成。此处的撇号是旋转架分量作为普通标量角函数的导数；物理连接已经包含在 (3) 的 U/T 中，不重复添加。

### 非带限解析余项

令 $D_j\ge\|\delta^{(j)}\|_\infty$，$j=1,\ldots,4$。链式法则给 $\cos\delta,\sin\delta$ 相应导数共同上界

$$
\begin{aligned}
B_0&=1,& B_1&=D_1,\\
B_2&=D_1^2+D_2,&
B_3&=D_1^3+3D_1D_2+D_3,\\
B_4&=D_1^4+6D_1^2D_2+3D_2^2+4D_1D_3+D_4.
\end{aligned} \tag{9}
$$

例如第四导来自再次求导 (7)；把正弦、余弦绝对值以1控制后得到 (9)。于是每个准确径向控制点的完整 N 都有

$$
L_4:=
\|P^{(4)}\|_\infty+
\sum_{k=0}^4\binom4k
\bigl(\|C^{(k)}\|_\infty+\|S_1^{(k)}\|_\infty\bigr)B_{4-k}
\ \ge\ \|N^{(4)}\|_\infty. \tag{10}
$$

右侧每个有限多项式范数均以 (6) 支付，未给 N 强加错误带宽。

在 $|N''|$ 最大点有 $N'''=0$；取距离至多 Δ 的网格点，Taylor 定理给

$$
\|N''\|_\infty\le
\max_{\mathrm{grid}}|N''|+\frac{\Delta^2}{2}L_4. \tag{11}
$$

因此每个以 $\phi_j$ 为中心的闭半步角盒都满足

$$
N(\phi_j+\eta)\in N(\phi_j)+[-L_j,L_j],\quad
L_j=\Delta|N'(\phi_j)|
+\frac{\Delta^2}{2}
\left(\max_{\mathrm{grid}}|N''|+\frac{\Delta^2}{2}L_4\right),
\quad |\eta|\le\Delta. \tag{12}
$$

若 $\chi=0$，C=$S_1$=0，整个 N 为有限多项式，直接用 (6) 包围 $\|N''\|_\infty$，不支付 (10) 的额外分量损失。

细分径向时，N 的控制点及其角导数作相同的正 Bernstein 线性组合；(10) 的非负上界也作相同组合，仍控制新控制点的四导。先 (12)，后径向凸包，支付完整闭径向／角盒。

当前场的半转和 y 反射使两个对角项为 $\pi$ 周期偶函数、混合项为 $\pi$ 周期奇函数；矩阵算子范数在相应符号共轭下不变。所以2049个闭角盒覆盖 $[0,\pi/2]$，再按对称性覆盖整圆。端点的两侧半步额外覆盖只会使界放宽。

## 4. 正确区分 Gram 余项与 a 的近似

若 $|a-A|\le\epsilon$，则准确有

$$
\mathcal E_{ss}=N_E,\qquad
\mathcal E_{s\phi}={N_M\over a\rho},\qquad
\mathcal E_{\phi\phi}
={N_G\over a^2\rho^2}+{A^2-a^2\over a^2}. \tag{13}
$$

在一个完整盒上，以 A 的 Bernstein 凸包加 $[-\epsilon,\epsilon]$ 包围真实 a。只在 a、$\rho$ 已给正下界时除法。最后一项满足

$$
\left|{A^2-a^2\over a^2}\right|
\le {\epsilon(2|A|+\epsilon)\over a_-^2}. \tag{14}
$$

这里 $\rho^2$ 已按准确式消去，不在小 $\rho$ 处人为将标量余项再放大。A 的系数区间本身包括原积分盒宽和准确 S 参数的不确定性；它们与截断余项 (14) 不重复或遗漏。

对于实际对称矩阵 $\begin{pmatrix}e&m\\m&g\end{pmatrix}$，准确有

$$
\|\mathcal E\|_{\mathrm{op}}=
{|e+g|+\sqrt{(e-g)^2+4m^2}\over2}. \tag{15}
$$

源码以完整符号区间代入 (15) 得上界，保留可能有利的对角符号关系。绝对值区间跨0时下界置0，平方和、平方根也向外。

同一次计算还在径向子胞端点与准确角网格点上，直接对未加角半步损失的完整分子求值并应用 (13)–(15)。其下端值是该准确点的范数下界，故这些下端值的最大值是真连续 supremum 的下界。这没有把离散点集当作连续上界。

## 5. 完整同 g 标量接口

新 [fullclosed_gram_scalar.py](../scripts/resume_20261120/fullclosed_gram_scalar.py) 首先将原场胞与所有准确标量分界、$S-w$ 相交，分别在每个闭 piece 上工作。分界以原 exact binary 常数或 $\alpha S+\beta$ 表达；只在原 S 盒能证明其次序时使用。没有用 carrier 显示值吞掉极短片。

### 5.1 原 quintic 区域

旧标量段按原 knots 的准确 binary 三 jet 形成唯一 quintic；首 jet 依原 initial law 的准确有理式重建。系数以 Fraction 形成，再限制到当前准确 piece 并转换为 Bernstein。此处 A=a，截断余项为0；不调用已经舍入系数的普通 Profile 插值。

### 5.2 常曲率及 ramp 区域

在每个准确扩展 piece 内，

$$a'=\sin\alpha,\qquad \alpha'=-\kappa.$$

其 $\kappa$ 是原固定常数，或原两端曲率之间的 quintic smoothstep。因此 $\alpha$ 是至多六次的准确多项式。初始角、K、S、R 等均消费原 FullHold 的已证盒；末 ramp 的起始角由准确 $-\pi/2+\kappa_+\ell_{\rm out}/2$ 给出。

例如 ramp 以 x 为从准确段首计的物理长度、宽度 w，有

$$
\alpha(x)=\alpha_0-\kappa_Lx
-(\kappa_R-\kappa_L)w
\left\{\frac52(x/w)^4-3(x/w)^5+(x/w)^6\right\}. \tag{16}
$$

源码在同一 piece 内选择最近的一个已有准确节点／中点 a 盒作 anchor。它可以位于当前小片外、但仍在同一个完整标量解析段内；从 anchor 到小片的整段仍使用同一个 (16)。原报告的 a 盒是真实积分值的包围，绝非把样值插值为新目标。

设 $t=s-s_*$，$\alpha(t)=\sum_j\alpha_jt^j$，并写

$$\sin\alpha(t)=\sum_js_jt^j,\qquad
\cos\alpha(t)=\sum_jc_jt^j.$$

由 $s'=\alpha'c$、$c'=-\alpha's$，准确归一化 Taylor 系数递推为

$$
\begin{aligned}
s_{j+1}&={1\over j+1}
\sum_{k=0}^j(k+1)\alpha_{k+1}c_{j-k},\\
c_{j+1}&=-{1\over j+1}
\sum_{k=0}^j(k+1)\alpha_{k+1}s_{j-k}.
\end{aligned} \tag{17}
$$

超过 $\alpha$ 次数的项为0。于是 n 次多项式

$$A(t)=a(s_*)+\sum_{j=0}^{n-1}{s_j\over j+1}t^{j+1} \tag{18}$$

的全部系数可用向外四则运算包围。$s_0,c_0$ 用 R656 已支付的完整 sin/cos Taylor 计算。

### 5.3 不省略高阶 Taylor 余项

令 $A_j\ge\|\alpha^{(j)}\|_\infty$，在整个解析段上取界。常曲率只有 $A_1=|\kappa|$ 非零。Ramp 的 $A_1$ 由两端曲率最大绝对值控制；$A_2,\ldots,A_6$ 由 smoothstep 的准确 Bernstein 差分及物理宽度幂控制；更高阶为0。

定义

$$
\mathcal B_0=1,\qquad
\mathcal B_{j+1}
=\sum_{k=0}^j\binom jk A_{k+1}\mathcal B_{j-k}. \tag{19}
$$

对 $z=e^{i\alpha}$ 的恒等式 $z'=i\alpha'z$ 逐次求导并取绝对值，归纳得到
$|z^{(j)}|\le\mathcal B_j$，从而
$|(\sin\alpha)^{(j)}|\le\mathcal B_j$。
若 $r\ge\max_{\mathrm{piece}}|s-s_*|$，Taylor 定理给完整余项

$$
|a(s)-A(s)|
\le {\mathcal B_n r^{n+1}\over(n+1)!}. \tag{20}
$$

这正是源码的 Bell 递推及余项；右侧最后用准确有理幂／阶乘及向上 binary 转换支付，不用未说明的经验阶数。宽 ramp 如有需要可增加 n 或在同一准确场中限制更小 piece；这不改变 a 的定义。实际本条只执行下节的常曲率胞，不声称 ramp 新数值应用已经运行。

## 6. def1 胞839：全部输入、预算与实际结论

准确端点为

$$
s_L={9\over64}S+{32619031669089217941\over36893488147419103232},\qquad
s_R={5\over32}S+{15996209415667698305\over18446744073709551616}. \tag{21}
$$

宽约 .02006718，处于原 Hold 的 $\kappa=3/2$ 常曲率段，且 $\chi=0$。它是一个完整原胞，无任何截短。a 的 anchor 是原 stage1679 的准确中点

$$
s_*={19\over128}S+
{64611450500424614551\over73786976294838206464}.
$$

消费原准确 a 盒

$$
a(s_*)\in
\left[
{30895041261018147103371\over25000000000000000000000},
{617900825220554483331809\over500000000000000000000000}
\right]. \tag{22}
$$

本次 n=5，故

$$|a^{(6)}|\le(3/2)^5={243\over32}.$$

具体五次式也可直接写为

$$
A(t)=a(s_*)+\sin\alpha_*\,t
-\frac{\kappa\cos\alpha_*}{2}t^2
-\frac{\kappa^2\sin\alpha_*}{6}t^3
+\frac{\kappa^3\cos\alpha_*}{24}t^4
+\frac{\kappa^4\sin\alpha_*}{120}t^5. \tag{23}
$$

完整程序的向外预算为：

| 项 | 实际向外上／下端读数 |
|---|---:|
| 最大 anchor 距离上界 | 0.010033592747889356 |
| $\lvert a^{(6)}\rvert$ 的向外实现上界 | 7.593750000000017 |
| a 的 Taylor 截断上界 | $1.0761247403328082\times10^{-14}$ |
| (14) 相对误差上界 | $1.7437718862308933\times10^{-14}$ |
| 连续 a 下界 | 1.234429157722385 |
| 全角 $\rho$ 下界 | 0.16594914855625276 |
| 完整分子系数区间最大宽度 | $2.3316126807060303\times10^{-11}$ |
| 全胞角 padding 矩阵范数上界的最大值 | 0.00041163922014042173 |
| 非带限四阶角余项 | 0（本胞 $\chi=0$） |

表内展示的是 binary interval 端点的往返十进制记录；正文 (1) 及以下明确放宽的十进制数作为准确有理界使用。系数宽度包括 S、原 a 盒和逐操作区间宽度，不能冒称纯浮点舍入误差。角 padding 的最大值一般不与真实误差最大位置重合，不能把它与 (1) 上下界差简单等同。

Q8192、每 piece 16个闭 dyadic 径向子胞的实际结果：

- 连续算子范数上端：0.10187888873272918；
- 准确点所得真 supremum 下端：0.10186124879530689；
- 三项绝对值上端：0.10187353754672765、0.0266385892772149、0.011476409751120546；
- 最大上界盒地址：径向子胞6、角索引2047；
- 下界见证：$s=s_L+\frac38(s_R-s_L)$、$\phi=\pi/2$。

角索引及“最坏盒”仅定位包围区间，不声称实际极值位于盒中心。向外放宽后的 (1) 来自这些真实上下端，直接排除本父靠证书加密达到 $10^{-6}$。

真实进程 session82406 自然退出0，总耗时8.07秒，其中胞核心5.91秒。没有为了得到更小报告值再改父、重复运行或加密；没有调用旧 dense 全域 probe 或重跑已刊标量积分。

## 7. 预算能否支持未来 $10^{-6}$

### 当前父必须继续求解

(1) 的严格下界已经超过 $10^{-6}$ 五个数量级。加密径向子胞、角网格、Taylor 阶数，都只改善证明的包围，不能改变这个准确场的真实误差。

### 核没有把分量大小硬塞成最终误差底限

在非活动 lift 片，完整分子 N 有限带宽，$\|N'\|_\infty\le m\|N\|_\infty$、$\|N''\|_\infty\le m^2\|N\|_\infty$。因此理论角 padding 随完整分子幅度下降，而不是随 $|F_s|^2$、$|F_\phi|^2$ 的单位量级固定。准确 Gram 分子为零时，其准确径向控制点及导数也为零，除了标量近似和有限区间算术预算，不会残留大分量盒的角误差。

在活动 lift 片，(12) 中为完整解析部分额外支付的项恰为

$$\frac{\Delta^4}{4}L_4. \tag{24}$$

因此该项随 Q 增加以四次幂下降。若 aρ 的正下界为 d，三个分子的四导界分别为 $L_E,L_M,L_G$，则其相对矩阵余项不超过

$$
\frac{\pi^4}{4Q^4}
\max\left\{L_E+\frac{L_M}{d},\
\frac{L_M}{d}+\frac{L_G}{d^2}\right\}. \tag{25}
$$

式 (25) 是误差矩阵的行和界；它给可直接执行的 Q 选择，不需要截去解析 lift 或改换曲面。具体未来活动胞的 $L_j$ 仍需同场读取，当前839不冒充已支付那部分数值。

径向 Bernstein 细分在固定准确多项式上进行，凸包随细分逼近真实连续范围。标量的可控部分由 (20) 显式给出；本宽约 .02 的尾胞已实际证明其相对贡献低于 $1.743772\times10^{-14}$，不是 $10^{-6}$ 的障碍。

这说明完整证明接口有适应更精确候选的机制；它不宣称任意未来系数、任意小胞宽在固定 binary 精度下必能通过。原积分盒宽与 IEEE 包围仍是明确的有限误差来源；本次完整分子系数宽度小于 $2.331613\times10^{-11}$，而当前的 .102 是已由严格下界证实的真实求解误差。未来应先降低候选误差，再按实际预算支付有必要的连续加密。

## 8. 算术模型、源码与复现

完整新源码：

| 文件 | SHA-256 |
|---|---|
| [fullclosed_relative_gram_interval.py](../scripts/resume_20261120/fullclosed_relative_gram_interval.py) | 5bbf821f45fec3a8ecd29ebd64dce8058bb302f7d53416b50158cca743065a13 |
| [fullclosed_gram_scalar.py](../scripts/resume_20261120/fullclosed_gram_scalar.py) | f572c39c7c54f78c360194fd86a1eeba62335ca23f41062f6a7892653ef9a68e |

消费 R656 的几何定义源 SHA 2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377 和 f512 向外核 SHA f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d。

算术假设与 R656 相同：标准 IEEE binary64 四则及平方根，每步一个 nextafter 向外，subnormal 不 flush-to-zero；准确有理输入按 Fraction 比较保证方向。π 与有限角变换使用原整数／有理余项，不假设普通 FFT 或 libm 三角函数严格。所有 (5)、(8)、(10)–(20) 的乘积、累加及除法均向外；不是最后才给普通浮点最大值加一个 eps。

源码 API 为 Gram(...).certify(cell)。标量层 Scalar.pieces(cell) 返回与原同 g 分界／lift 分界的完整交；Scalar.approximation(piece) 返回 A 的 Bernstein 区间系数和完整余项。它们保留原全部未知量，未添加新的科学验收门。

本次可重生报告 work/recover_evidence/continuous-Gram-def1-cell839-q8192-r16.json 的 SHA-256：

9ddf9cd5ff2a823533ad0f64fae5ef0813609079bca3e57b7f1e5a12c66f1746。

在工作根执行的准确 CLI：

```bash
python -u work/recover_evidence/fullclosed_relative_gram_interval.py \
  --bundle work/fullclosed_solver/gauss-h2-projected-first-fixed/final.npz \
  --node-report work/fullclosed_solver/data/fullclosed-hold-warm.json \
  --interval-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
  --geometry-source work/recover_evidence/fullclosed_geometry_interval.py \
  --scalar-source work/recover_evidence/fullclosed_gram_scalar.py \
  --scalar-input work/fullclosed_solver/data/pulse-a5-complete-base.json.gz \
  --cells 839 --angles 8192 --radial-subdivisions 16 --scalar-degree 5 \
  --out work/recover_evidence/continuous-Gram-def1-cell839-q8192-r16.json
```

报告含时间，重新执行的整份 JSON 哈希不承诺逐字相同；准确输入、源码、参数和数学对象均已固定。可重生 raw 不入库。此条完成完整模型连续 relative Gram 的首个实际接口；后续要对真正收敛的同场候选支付其余范围，不能把本胞的应用扩大成全域或闭族完成结论。
