# R280：三个真实矩面积与五个完整 block 支付全部 Gaussian 面积

日期：2026-11-15。**完整纸面建设性证明；没有执行求积、序列枚举、符号程序、人工检查或研究计算。**

[R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md) 的等平方背景格点圆已付30个 formal even 条目及全部36个 odd 条目；[R279](R279-finite-frequency-fiber-control-pays-both-even-profile-energies.md) 又能在准确保持全部 Gaussian 数据的纤维中支付六个已识别能量。本稿处理它们留下的六个 even 条目。

新增结论是：完整 self/Green 与对称跨核先按原式消去后，六个余项恰由三个真实三矩路径的有序面积控制。交换两层**真实有限**格点编码可给其中第一个面积严格正、负两种布局；五个最后位置已经选定的完整 block 再以正四次权准确支付全部三个面积。最后在每个 block 的原数据纤维中执行 R279 的有限频率存在论证，不改变任何面积。

因此存在真实有限光滑非分离圆，同时满足三矩、完整第三 range、全部六能量及六个 Gaussian 面积的三个完整角外矩。尚未支付零/一层 history、完整第四 period 与 whole ruling/joint；不能把“全部 Gaussian 面积为零”称作完整第四阶可解。

## 1. 原方程列表与完整消去，先保 self 和 Green

保持 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的共同右锚与三个真实矩

$$
\mathbf m(u)=(m_0,m_1,m_2)
=\left(\int u''{}^2,\int xu''{}^2,
\int(x^2u''{}^2+2u'{}^2)\right).
\tag{1}
$$

实际微包互不交，按从左到右编号。令

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
b_i^2=B>0,
$$

$$
R_i=a_i^2-B\in\{-B/2,8B\},\qquad T_i=a_ib_i.
\tag{2}
$$

原格点满足

$$
\sum_iR_it_i^q=\sum_iT_it_i^q=0,\qquad 0\le q\le10 .
\tag{3}
$$

每个 $u_i$ 最初为共同 even 母包的平移；以后允许 R277 的完整 $\mathcal F$ 纤维替换，准确保留三个矩及全部 self 平移系数。此处 $\mathcal F$ 的定义含真实 Green 端项，单包二次输出的左尾从未被置零。

对任意一个 Gaussian pair、任意外矩，记原 self 为 $S_i$，原跨核为 $\Gamma(\mathbf m_i,\mathbf m_j)$。R259 的完整角式给

$$
E_{04}
=B\sum_jR_j\left[S_j+\sum_{i<j}
\Gamma(\mathbf m_i,\mathbf m_j)\right]=0.
\tag{4}
$$

最后的零使用等距格点、完整 self 的平移次数界、原前缀的次数界及 (3)。它保留 ordered history。

完整相减是

$$
\boxed{
E_{22}-E_{04}
=\sum_i(R_i^2-4T_i^2)S_i
+\sum_{i<j}(R_iR_j-4T_iT_j)
\Gamma(\mathbf m_i,\mathbf m_j).
}
\tag{5}
$$

原背景项 $B\sum_{i<j}R_j\Gamma$ 已由整个 (4) 消去；不能只删这一 cross 项而留下它配套的 self。两值关系给

$$
R_i^2-4T_i^2=\frac{7B}{2}R_i,
\tag{6}
$$

故 (5) 的全部 self 和准确为零。若将 $\Gamma$ 分解为对称部与反对称部，对称部仍给

$$
\begin{aligned}
&\sum_{i<j}(R_iR_j-4T_iT_j)\Gamma_{\rm sym}(\mathbf m_i,\mathbf m_j)\\
&\qquad=-\frac12\sum_i(R_i^2-4T_i^2)
\Gamma_{\rm sym}(\mathbf m_i,\mathbf m_i)=0.
\end{aligned}
\tag{7}
$$

前一等式用 $\sum R_i\mathbf m_i=\sum T_i\mathbf m_i=0$，后一等式用 (3)、(6) 及对角核的四次次数界。式 (5)—(7) 对其余不对称核同样成立；只把其**对称部**消掉，没有将整核假定对称。

因此，R277 剩余六式只保反对称跨核。这是完整原式的结论，不是纯对角或 formal bracket 商的猜测。

## 2. 六个未付条目准确归为三个面积

对 $0\le r<s\le2$，定义真实有限和

$$
\boxed{
\mathcal A_{rs}
=\sum_{i<j}(R_iR_j-4T_iT_j)
(m_{r,i}m_{s,j}-m_{s,i}m_{r,j}).
}
\tag{8}
$$

这三个量来自同一圆、同一真实次序和三矩；没有将它们赋作独立 shape 常数。

原三类核是

$$
\begin{aligned}
\mathbf K_1(\mathbf m,\mathbf n)
&=\left(-m_1n_0,-\frac{m_0n_2+m_2n_0}{2},-m_1n_2\right),\\
\mathbf K_2(\mathbf m,\mathbf n)
&=(-m_0n_0,-m_0n_1,m_2n_0-2m_1n_1),\\
\mathbf K_3(\mathbf m,\mathbf n)
&=\left(\frac{m_0n_2}{2}-m_1n_1,-\frac{m_2n_1}{2},-\frac{m_2n_2}{2}\right).
\end{aligned}
\tag{9}
$$

反对称部按 $(K(\mathbf m,\mathbf n)-K(\mathbf n,\mathbf m))/2$ 定义。
记原 Gaussian 系数

$$
g_1=-\zeta c,\qquad g_2=db/2-ea,\qquad g_3=-\zeta b .
$$

则六个真实余项恰为

| Gaussian pair | 外矩 | 余下的 $E_{22}$ |
|---|---|---|
| $(1,-3)$ | $I_0$ | $g_1\mathcal A_{01}/2$ |
| $(1,-3)$ | $I_2$ | $-g_1\mathcal A_{12}/2$ |
| $(-1,-2)$ | $I_1$ | $-g_2\mathcal A_{01}/2$ |
| $(-1,-2)$ | $I_2$ | $-g_2\mathcal A_{02}/2$ |
| $(1,-2)$ | $I_0$ | $g_3\mathcal A_{02}/4$ |
| $(1,-2)$ | $I_1$ | $g_3\mathcal A_{12}/4$ |

在实际小非零共振 $\varepsilon=\kappa^2/4$，原 $\zeta,b,c,g_2$ 都非零。因此在本等背景类中，剩余六式全部为零，当且仅当

$$
\boxed{\mathcal A_{01}=\mathcal A_{02}=\mathcal A_{12}=0.}
\tag{10}
$$

这给的是准确必要充分重述；不声称三个函数在任意母包点的微分秩为三。若使用其他使某原系数为零的 germ，(10)仍是充分条件，但不应未经检查照搬“当且仅当”。

## 3. 真实累计 primitive 表示，不是 profile 点质量近似

把共同包宽收入 even 母包 $u_0$，记

$$
m=I_0(u_0,u_0)>0,\qquad \nu=I_2(u_0,u_0)/m.
$$

由真实平移公式和偶性，

$$
\boxed{\mathbf m_i=m(1,t_i,t_i^2+\nu).}
\tag{11}
$$

R277 的同 $\mathcal F$ 替换准确保持 (11)，即使某些实际母包的三阶导与基点相差很大。

下面引入两个辅助有限测度，只用于编码 (11)：

$$
\mu_R=\sum_iR_i\delta_{t_i},\qquad
\mu_T=\sum_iT_i\delta_{t_i}.
$$

没有用它们替代真实 $u_i$ 的 self 或 Gaussian 场；这些量已先在 (4)—(7) 用原 Green 表完整处理。该辅助表示是三矩跨核的准确有限编码。

定义左累计阶梯函数

$$
F_R(x)=\sum_{t_i<x}R_i,\qquad
F_T(x)=\sum_{t_i<x}T_i,
$$

$$
G_R(x)=\sum_{t_i<x}t_iR_i,\qquad
G_T(x)=\sum_{t_i<x}t_iT_i.
\tag{12}
$$

由于 (3) 的零次、一次矩，这四个函数在两外侧恒零。对所有 $i<j$，用
$t_j-t_i=\int_{t_i}^{t_j}dx$ 并先求完整左右和，得到

$$
\boxed{
\begin{aligned}
\mathcal A_{01}
&=-m^2\int(F_R^2-4F_T^2),\\
\mathcal A_{02}
&=-2m^2\int x(F_R^2-4F_T^2),\\
\mathcal A_{12}
&=-m^2\int\{G_R^2-4G_T^2-\nu(F_R^2-4F_T^2)\}.
\end{aligned}}
\tag{13}
$$

例如第三式用
$m_{1,i}m_{2,j}-m_{2,i}m_{1,j}
=m^2(t_j-t_i)(t_it_j-\nu)$，
而跨过 x 的两个加权和恰是 $-G_R(x)^2$ 与 $-G_T(x)^2$。
真实 $I_2$ 中的 $2u'{}^2$ 已保在 $\nu$ 中。

若再记 $H_R(x)=\int_{-\infty}^xF_R$、$H_T$ 同理，一次矩零使它们也真紧，并有
$G_R=xF_R-H_R$。完整 IBP 给

$$
\int G_R^2=\int x^2F_R^2+2\int H_R^2
$$

及 T 的对应式。因此第三个条件还保留第二累计量的平方差，不能只配
$F_R^2-4F_T^2$ 的普通二阶位置矩。

同一 $\mathcal F$ 纤维完全固定 (13)。所以 R279 的高阶能量变化不能自己支付一个非零面积；本稿下一步改变的是准确有限布局。

## 4. 两层有限格点编码，保持原全部十阶矩

取

$$
L=17^{11},\qquad K=2^{11}.
$$

先将 $0,\ldots,L-1$ 按17进制数位和模17分类。指定一类为 high，令

$$
r_j=
\begin{cases}
8B,&j\text{ 属于指定类},\\
-B/2,&\text{否则},
\end{cases}
\qquad
\tau_j=\sqrt{B(B+r_j)}\in\{3B,B/\sqrt2\}.
\tag{14}
$$

R277 的原17进制生成函数证明

$$
\sum_{j=0}^{L-1}r_jj^q=0,\qquad 0\le q\le10.
\tag{15}
$$

每个连续17项恰有一个 high，所以这些17项的 r 总和也逐组为零。

令 $\epsilon_k=(-1)^{\operatorname{popcount}(k)}$。
在同一个格距 $d_{\rm g}>0$、同一个长度 $KL$ 的格点上，定义两个不同的真实布局：

$$
\begin{array}{c|c|c}
 &R_i&T_i\\ \hline
+\text{ 布局},\ i=kL+j&r_j&\epsilon_k\tau_j\\
-\text{ 布局},\ i=jK+k&r_j&\epsilon_k\tau_j.
\end{array}
\tag{16}
$$

每一行都对应真实
$b_i=\sqrt B$、$a_i=T_i/\sqrt B$；
所以 (2)、(6) 未改变。它们是把17进制和二进制两个**有限索引层**交换，不是将一个有序 kernel 形式上取负。

对正布局，R 的十阶矩由 (15) 支付，T 的十阶矩由对 k 的 TM 差分支付。对负布局，R 的十阶矩仍由对 j 的 (15) 支付；对每个固定 j，T 的十阶矩直接由对 k 的 TM 差分支付。展开 $(kL+j)^q$ 或 $(jK+k)^q$ 便逐项得到

$$
\sum R_it_i^q=\sum T_it_i^q=0,\qquad 0\le q\le10
\tag{17}
$$

对两个布局均成立，平移后的实际等距坐标也同样成立。

因此 R277 的全部18个 $E_{04}$、另外12个 $E_{22}$、三矩与真实 range 前提仍保留。两个布局可以各自采用原八/十二完整包装，支付全部第三及 odd 条件。这里没有剪去旧核、改变 Gaussian 系数或借用单包假紧。

## 5. 第一个面积具有严格相反号

### 5.1 整块 TM 符号：$\mathcal A_{01}>0$

在正布局中，R 的前缀在每17格归零，且始终满足

$$
|F_R|\le8B.
$$

所以

$$
\int F_R^2<64B^2d_{\rm g}KL.
\tag{18}
$$

TM 的任意偶数长度前缀和为零。因此至少 $K/2$ 个长度 L 的块开始时
$F_T=0$，在该块内所有 T 同号且绝对值至少 $B/\sqrt2$。
对其中第 j 个内部 gap，有 $|F_T|\ge jB/\sqrt2$。
于是

$$
4\int F_T^2
\ge KB^2d_{\rm g}\sum_{j=1}^{L-1}j^2.
\tag{19}
$$

因 $L\ge17$，

$$
\sum_{j=1}^{L-1}j^2-64L
=L\left\{\frac{(L-1)(2L-1)}6-64\right\}>0.
$$

由 (13)、(18)、(19) 得严格

$$
\boxed{\mathcal A_{01}^{+}>0.}
\tag{20}
$$

### 5.2 每个 R 项内作细 TM：$\mathcal A_{01}<0$

在负布局中，每个长度 K 的 T 小块自己归零，TM 前缀绝对值至多1，故

$$
|F_T|\le3B,\qquad
4\int F_T^2<36B^2d_{\rm g}KL.
\tag{21}
$$

另一方面，每个长度 K 的 R 小块是同号常值 $r_j$。
无论其真实起始前缀是哪个 X，都有

$$
\sum_{k=1}^{K-1}(X+kr_j)^2
\ge r_j^2\,\frac{(K-1)K(K-2)}{12}.
\tag{22}
$$

这是对实 X 的完整平方配方；并未把前缀重置为零。
因为 $r_j^2\ge B^2/4$，

$$
\int F_R^2
\ge LB^2d_{\rm g}\frac{(K-1)K(K-2)}{48}.
\tag{23}
$$

$K=2048$ 特别满足 $(K-1)(K-2)>1728$。
结合 (13)、(21)、(23)，

$$
\boxed{\mathcal A_{01}^{-}<0.}
\tag{24}
$$

这两个号对任意非零共同 even 母包均成立；m 只提供一个正因子。
在其完整 $\mathcal F$ 纤维中，号和全部三个面积的值都准确不变。
证明只用了有限求和身份与真实阶梯编码，没有枚举这些序列或执行 profile 计算。

## 6. 真平移与反射的作用，不能偷用形式反序

对整个实际圆作共同平移 d，三个矩按

$$
(m_0,m_1,m_2)\mapsto
(m_0,m_1+dm_0,m_2+2dm_1+d^2m_0).
$$

于是有准确变换

$$
\boxed{
(\mathcal A_{01},\mathcal A_{02},\mathcal A_{12})
\mapsto
(\mathcal A_{01},
 \mathcal A_{02}+2d\mathcal A_{01},
 \mathcal A_{12}+d\mathcal A_{02}+d^2\mathcal A_{01}).
}
\tag{25}
$$

这是实际 profile 和位置共同变换的结果，保留原 $I_2$，并非在固定场外任意指定三个数。

物理反射不仅倒转左右次序，还使 $m_1$ 变号；在以零为中心的坐标中，它给

$$
(\mathcal A_{01},\mathcal A_{02},\mathcal A_{12})
\mapsto(\mathcal A_{01},-\mathcal A_{02},\mathcal A_{12}).
\tag{26}
$$

所以只反射原布局并不能反转 $\mathcal A_{01}$。形式上倒转一个固定矩列表虽使有序楔积取负，却没有同时变换这些矩的实际位置，不能当作合法几何。第4节的两个编码支付了这个区别。

先给每个正、负布局作原八/十二完整包装。不同完整副本的 inner 三矩为零，故跨副本的原核为零；每个副本的三面积按 (25) 变换并乘真实正四次权。特别首面积的正、负号仍保留。

对这两个已经包装的实际模板，分别平移，使第二面积为零。这些平移及接下来的全部最后位置都在能量求根以前选定。记中心化后的面积为

$$
\mathbf A_\pm
=A_\pm(1,0,\chi_\pm),\qquad A_+>0>A_-.
\tag{27}
$$

这里

$$
\chi_\pm=
\frac{\mathcal A_{12}^\pm}{\mathcal A_{01}^\pm}
-\frac{(\mathcal A_{02}^\pm)^2}{4(\mathcal A_{01}^\pm)^2}
$$

来自真实有限模板，不是自由参数。

原 (13) 还表明：$A_\pm/m^2$、中心化所用平移都仅由布局决定；
$\chi_\pm$ 含同一个加项 $-\nu$，所以
$\chi_- -\chi_+$ 也只由布局决定。
因此后面的概率和相对位置可以先由布局确定，不造成选择最大秩母包的循环。

## 7. 五个最后完整 block 的正权准确配平

用一个足够大的有限 R 包住两个中心化模板的全部相对支撑。取有限

$$
\ell>4R,\qquad \ell^2+\chi_- -\chi_+>0 .
$$

再取有限 $D>\ell+4R$，使

$$
0<w:=\frac{\chi_--\chi_++\ell^2}{D^2}<1.
\tag{28}
$$

正布局的三个最后中心为
$C,C-D,C+D$，其概率为
$1-w,w/2,w/2$；
负布局的两个最后中心为 $C-\ell,C+\ell$，概率各为 $1/2$。
五个真实支撑严格不交。最后选择足够大的共同 C，使它们及全部内部完整副本落在一个已允许的正物理区间中，并给 R279 的三个 principal 比值留下统一严格次序。

令 $a_\pm=A_\pm/m^2$。用概率分别除以 $a_+$ 与 $|a_-|$，得到五个**严格正的四次幅权**。取它们的正实四次根作为实际共同 profile 幅度。
于是两组第一面积分别为 $m^2$、$-m^2$，第二面积都按 (25) 给共同中心项。第三面积的总和为

$$
m^2\{C^2+\chi_++wD^2-C^2-\chi_--\ell^2\}=0.
$$

因此准确得到

$$
\boxed{
\mathcal A_{01}=\mathcal A_{02}=\mathcal A_{12}=0 .
}
\tag{29}
$$

每个完整 block 的 inner $D_\theta$ 三矩已经为零，所以不同 block 之间的 R259 跨核准确为零。它们的三面积及全部 Gaussian 观测因而按这些正四次权相加，没有隐藏的新 inter-block history。

第1节已付的30个 even 条目在每个 block 中都为零，并对其任何共同平移成立；odd 条目在各自十二包装中已为零。所以 (29) 和第2节的原系数表给

$$
\boxed{
\text{六个 Gaussian pair 的三个完整角外矩全部为零。}
}
\tag{30}
$$

这是全部72条原标量条件的准确零，不是“达到某个秩”或数值近零。
本节只支付面积；尚未对一个平移后的旧能量零解作任何保持声明。

## 8. 在最终位置固定以后支付六能量，不改变面积

上述模板和五个最后 block 最初都用同一个 even 最大秩母包 $u_0$。
按 R279，从一开始选择其实际正则邻域，使所用中心 cutoff 和两个 bulk 的 principal 比值证明成立。

两个编码都包含 high–low–high 的三个不同基本位置。
选定五个最终中心及全部完整副本后，可统一增大共同正 C：
R279 的准确比值展开

$$
\rho_{i,j}=-\frac3C+
\frac{3(X_j+t_i+\bar d)}{C^2}+O(C^{-3})
$$

中 $X_j\in\{0,\pm D,\pm\ell\}$ 为该最后 block 的相对中心。它在每个模板中使三位置的比值严格相夹。这里只使用已经固定的有限位置、完整副本四次权和原两个 bulk，不能删掉 $\bar d$ 或把比值当作任意控制参数。

对每个最后 block，独立使用 R279 的三个真实有限频率扰动及同一固定 $\mathcal F$-minor 的有限光滑纠正。其有限 N 的完整 $C^1$ 控制给一个准确根

$$
L_c=M_c=0.
\tag{31}
$$

这些替换在每个真实平移位置都保留母包的完整 $\mathcal F$ 数据，故 (4)—(30) 和五个已经选定的幅权一字不变。它不是在面积算完后重新选择数据不同的母包。

全部最后 block 的 odd 能量由原十二包装给
$L_s=M_s=0$。
在共同实际共振 germ 上，R256 已付的一般不交微包身份
$N_c=6M_c$、$N_s=6M_s$ 继续适用。各 block 的真实 inner 三矩使完整能量的总体边界先消失，然后不同微包 bulk 的支撑不交；正幅相加保持全部六个零。

故最后同一个真实圆满足

$$
\boxed{
L_c=L_s=M_c=M_s=N_c=N_s=0,
\qquad
\text{全部 Gaussian 面积为零。}
}
\tag{32}
$$

这里使用的是 R279 已证明的有限频率存在定理，没有执行其振荡序列、人工试验或任何研究运行。若只消费 R277 而暂不消费 R279，同一构造仍可以保持全部面积并只授其已经证明的 $L_c=L_s=0$；不能从 R277 单独跳到(32)。

## 9. 真实选择次序与安装范围

整个构造可按有限顺序完成：

1. 固定共同真实 Gaussian germ、原算子及允许的 profile 支撑类别；两层有限编码及所有相对格点均明确定义。
2. 选择共同 even 光滑最大秩母包和 R279 的固定有限纠正方向；所有原二次矩、自项及有序核都由这个母包确定。相对五块布局的权和差 $\chi_--\chi_+$ 已不依赖 m、ν。
3. 按第7节一次选定有限 $\ell,D$，随后选足够大的共同 C 和允许的有限正 I，保持全部支撑、collar、$x+\omega(s)$ 的余量。不是扩大某个早已冻结的窄区间。
4. 在这些最终位置及正幅确定之后，才在各 block 中用有限 N 的同数据纤维得到(31)。
5. 最后同乘一个正实归一因子，使 $I_0(f,f)=I_0(g,g)=1$、$I_0(f,g)=0$。全部齐次零保持，非退化仍由共同正 $I_0$ 给出。

真实最小包上 f、g 仍成固定常数比例，两个布局均出现
$\pm1/\sqrt2,\pm3$ 的射影方向；固定 $GL_2$ 不能将其改成只有两种支撑不交方向。所有最终函数都是有限个实际 $C^\infty$ 紧包之和，频率、幅度、宽度、间距均有限，支撑严格不交。很大的有限索引数只用于存在证明，没有执行或保存其机器枚举。

共同 scalar 几何及 germ 的安装沿 R277/R279 已声明的合法范围。本稿新增的是 profile 与面积构造，选择新的 seed 和目标；不声称保持某个旧固定圆的目标度量不变，也不把高阶母形变化误作直接改变一个已接受的数值曲面。

## 10. 尚未解决的真实条件

(32) 清除了此前六个 formal even 余项，并保留原六能量；它没有证明这些条件是完整第四阶相容性的充分条件。尤其：

- Gaussian words 的十个对称二层乘积 $E_rE_s$、四个一层 $E_r$ 与零层部分，仍须按真实独立基和原五相位核对；面积零不自动支付这些系数；
- canonical 第四 period、完整第三核修正及同一个二阶 homogeneous gauge 的联合可解性没有由面积零自动推出；
- R276 的解析零端有限判据不能无条件套到本稿另选的最大秩高频母包；若要使用，需另外证明该真实母包类别的解析端芽兼容；
- 有限连续等距族、更高阶收敛、闭曲面嵌入、reach 与宏观幅度仍未支付。

本稿的准确新意义是：剩余的六个面积条目并非需要任意指定六个 shape 数值。保全 self/Green 后，它们由三个真实有序矩面积控制；两种不同的有限编码给首面积双号，五个最终完整 block 再给全部三个的严格正权消去。形状纤维随后只支付高阶能量，不再被错误地指望改变一个已经冻结的面积残差。

