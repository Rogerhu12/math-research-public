# R16：第四模核投影、紧支均值调节与任意有限阶真实近似

2026-11-10，positive-exact-route。

**状态：已证明的正向中间结论。** 本文构造每个指定有限奇数阶的闭 $C^2$
近似面，完整非均值度量误差在该阶以前严格消失。核心输入是 R12 的真实
全直线逆；第四模共振由一个明确的轴对称均值方向处理，其横截分母严格
大于 $7$。本结果没有证明级数收敛、有限可见幅度的精确零解，亦没有把
R12 的弯曲极点自动换成 R11 的真实固定平帽。

## 1. 对象、源消元与结论

保留 R12 的
$$
\mu=\sqrt2,\quad A=2+\frac{\sqrt2}{4},\quad
q=2-A\operatorname{sech}^2x,\quad
h''=qh,\quad h(0)=1,\ h'(0)=0,
$$
$$
a=h^{-1},\quad z_x=h^{-2},\quad
w=h'/h,\quad X=a e_r+z e_z,\qquad L_m=-\partial_x^2+m^2q.
\tag{1}
$$
背景补两极后为闭 $C^2$ 嵌入。其第四模核及真实向量场是
$$
y=\operatorname{sech}^{4\mu}x,\quad
Z=U\cos4\theta\,e_r+T\sin4\theta\,e_\theta+W\cos4\theta\,e_z,
$$
$$
U=y/h,\qquad T=-U/4,\qquad W=wy-y'/16.
\tag{2}
$$

在本稿中，$P,Q,R$ 分别是目标张量的 $\theta\theta$ 余弦系数、
$x\theta$ 正弦系数、$xx$ 余弦系数。特别，$Q,R$ 使用 $x$ 坐标，
不是经线弧长。对正频率 $m$ 定义源算子
$$
C=\frac{hP}{2},\qquad
J=(hC)'-mh^2Q,\qquad
\mathcal S_m(P,Q,R)=\frac{m^2h^2}{2}R-J'.
\tag{3}
$$
若 $\eta$ 满足 $L_m\eta=\mathcal S_m(P,Q,R)$，令
$$
U_m=\eta/h,\qquad
T_m=(C-U_m)/m,\qquad
W_m=w\eta-\eta'/m^2+J/m^2.
\tag{4}
$$
直接求导，(4) 同时解出三个完整线性度量方程：
$$
2a(U_m+mT_m)=P,
$$
$$
a(T_m)'-a'(mU_m+T_m)-mz'W_m=Q,
\qquad
2(a'(U_m)'+z'(W_m)')=R.
\tag{5}
$$
这是 R8 统一消元写成 $x$ 坐标后的形式；式 (5) 也提供独立核对。

**有限阶定理。** 对每个奇数 $N\ge3$，下面的递推唯一确定有限组
$C^2$ 环境向量场 $Y_1,\ldots,Y_N$（其中 $Y_1=Z$）
及实常数 $\alpha_2,\alpha_4,\ldots,\alpha_{N-1}$。
每个非均值场只有有限个 $4\mathbb Z$ 角频，且在两极有零二 jet。
所有第四模逆均在 $y^\perp$ 中取，以固定核规范。令
$$
F_\varepsilon^{[N]}=X+\sum_{j=1}^N\varepsilon^jY_j,\qquad
g_\varepsilon^{[N]}=\mathcal P_0\bigl((F_\varepsilon^{[N]})^*e\bigr).
\tag{6}
$$
则
$$
(F_\varepsilon^{[N]})^*e-g_\varepsilon^{[N]}
=\sum_{k=N+1}^{2N}\varepsilon^k\,
\mathcal P_{\ne0}
\sum_{\substack{1\le i,j\le N\\i+j=k}}dY_i\cdot dY_j.
\tag{7}
$$
这是完整非线性度量的准确恒等式，未截断角频；各个系数在闭面上为 $C^1$。
对每个固定 $N$，充分小的 $|\varepsilon|$ 下，$F_\varepsilon^{[N]}$
为闭 $C^2$ 嵌入且 $g_\varepsilon^{[N]}$ 正定。

没有声称这些小参数区间有共同正下界，也没有声称 $N\to\infty$ 收敛。
不同 $\varepsilon$ 的平均度量一般不同；(6) 不是已经实现的同度量弯曲族。

## 2. 紧支核心均值方向

取明确的偶函数
$$
\phi(x)=
\begin{cases}
\exp\left(1-\dfrac1{1-64x^2}\right),& |x|<1/8,\\
0,&|x|\ge1/8.
\end{cases}\tag{8}
$$
令
$$
h_\alpha=h e^{\alpha\phi},\quad
a_\alpha=h_\alpha^{-1},\quad
z_\alpha(x)=\int_0^x h_\alpha^{-2},\quad
X_\alpha=a_\alpha e_r+z_\alpha e_z.
$$
采用其真实导数
$$
V=\left.\partial_\alpha X_\alpha\right|_0
=-a\phi\,e_r-2\left(\int_0^x a(u)^2\phi(u)\,du\right)e_z.
\tag{9}
$$
$V$ 为轴对称 $C^2$ 场，且在 $|x|\ge1/8$ 的每个帽端分别只是固定
竖直平移，故 $dV=0$。特别，$h_\alpha$、势 $h_\alpha''/h_\alpha$
和实际径向背景在这个紧核心以外保持不变；帽的高度可整体平移。
这只是均值背景调节，不是要求弯曲场在开帽上的最终非线性匹配。

记 $\mathcal B_X(Y)=dX\cdot dY+dY\cdot dX$。
因为 $V$ 轴对称，$\mathcal P_{\ne0}\mathcal B_X(V)=0$。
因此给偶数阶加上 $\alpha_{2j}V$ 不改变该阶已经完成的非均值方程。

## 3. 第四模横截分母的准确计算

令 $f_V$ 为目标张量 $-\mathcal B_V(Z)$ 的第四模经 (3) 得到的源。
不需要逐项展开这个长表达式来判断其投影。固定 $y$，对每个 $\alpha$
用 (2) 的同一重建公式构造 $Z_\alpha(y)$，只将 $h,w$ 换成
$h_\alpha,h_\alpha'/h_\alpha$。对任意 $y$，准确恒等式是
$$
\mathcal B_{X_\alpha}(Z_\alpha(y))_{\theta\theta}
=\mathcal B_{X_\alpha}(Z_\alpha(y))_{x\theta}=0,
$$
$$
\mathcal B_{X_\alpha}(Z_\alpha(y))_{xx}
=\frac{2}{16h_\alpha^2}L_4(\alpha)y.
\tag{10}
$$
并且
$$
\left.\partial_\alpha(h_\alpha''/h_\alpha)\right|_0
=\phi''+2w\phi'.
$$
对 (10) 求导，使用 $L_4y=0$，再应用 (3)，得到
$$
f_V=L_4(-\phi y)-16(\phi''+2w\phi')y.
\tag{11}
$$
因此真实全直线核投影为
$$
\begin{aligned}
\kappa:=\langle y,f_V\rangle
&=-16\int_{\mathbb R}(\phi''+2w\phi')y^2\,dx\\
&=-32\int_{\mathbb R}\phi\bigl[(y'-wy)^2+15q\,y^2\bigr]\,dx.
\end{aligned}\tag{12}
$$
积分分部合法，因为 $\phi$ 光滑且紧支；$L_4$ 自伴且 $y$ 是核。

下面支付一个明确正下界。在 $|x|\le1/8$，
$\tanh^2x\le x^2$、$7/3<A<19/8$ 给
$$
-3/8<q\le2-\frac73\frac{63}{64}=-19/64<-1/4.
$$
正偶解 $h$ 在这里向外递减且 $h\le1$。由 $h''=qh\ge-3/8$，
$$
h\ge1-\frac3{16}x^2>7/8,\qquad |h'|\le(3/8)|x|\le3/64,
\qquad |w|\le3/56.
$$
又 $|y'/y|=4\mu|\tanh x|<3/4$，故
$$
\frac{(y'-wy)^2+15qy^2}{y^2}
<1-\frac{15}{4}=-\frac{11}{4}.
$$
在更小区间 $|x|\le1/16$，有
$\phi\ge e^{-1/3}>2/3$，而 $\log\cosh x\le x^2/2$ 给
$y^2\ge e^{-4\mu x^2}>125/128$。因此
$$
\boxed{\quad
\kappa>88\int_{-1/16}^{1/16}\phi y^2\,dx
>\frac{1375}{192}>7.
\quad}\tag{13}
$$
这不是待验证的横截性假设。

## 4. 实际三阶构造与任意有限阶递推

先令 $Y_1=Z$。二阶源 $-\mathcal P_{\ne0}(dZ\cdot dZ)$ 只有第八模；
用 R12 的真实 $L_8^{-1}$ 和 (3)、(4) 得到其唯一非均值解
$\widehat Y_2$。暂写
$$
Y_2=\widehat Y_2+\alpha_2V.
$$
三阶目标为
$$
-\mathcal P_{\ne0}\bigl(dZ\cdot d\widehat Y_2+
d\widehat Y_2\cdot dZ+\alpha_2\mathcal B_V(Z)\bigr).
$$
其第四模源为 $f_{3,4}^{\,0}+\alpha_2f_V$，所以
$$
\alpha_2=-\frac{\langle y,f_{3,4}^{\,0}\rangle}{\kappa}
\tag{14}
$$
使它准确属于 $y^\perp$。对第四模使用真实的
$(L_4|_{y^\perp})^{-1}$，对第十二模使用 $L_{12}^{-1}$，再由 (4)
得到 $Y_3$。所有二阶、三阶非均值度量系数因而严格消失。

一般步骤如下。假设此前系数已经确定，令
$$
G_j=\sum_{i=1}^{j-1}dY_i\cdot dY_{j-i},\qquad
\mathcal B_X(Y_j)=-\mathcal P_{\ne0}G_j.
\tag{15}
$$
频率规则是：$Y_j$ 的非均值频率恰在允许集合
$\{4k:1\le k\le j,\ k\equiv j\pmod2\}$ 中；并非声称每个允许系数都非零。
这是余弦、正弦乘积公式的直接归纳。轴对称均值只出现在偶数阶。

当 $j$ 为偶数时，目标没有第四模，所有模式由 R12 的真实逆确定
$\widehat Y_j$，再暂留一个尚未选择的 $\alpha_jV$。
当 $j$ 为奇数时，唯一尚未知的上一阶均值参数 $\alpha_{j-1}$
在 (15) 中只通过 $Y_1$ 与 $Y_{j-1}$ 两个交叉项出现。
所以本阶第四模源准确为
$$
f_{j,4}^{\,0}+\alpha_{j-1}f_V,\qquad
\alpha_{j-1}=-\frac{\langle y,f_{j,4}^{\,0}\rangle}{\kappa}.
\tag{16}
$$
同一个非零分母 (13) 在每一步适用。随后所有模式由真实逆求出；
第四模取 $y^\perp$ 中的唯一解。到任意奇数阶 $N$ 为止，每个暂留的均值
参数都已在下一阶确定，没有未支付的有限维可解条件。

## 5. 源属于真实逆的定义域及两极正则性

以下给递推的合法性，不能把形式角系数当成完整闭面向量场。
R12 的背景满足
$$
h(x)\asymp e^{\mu|x|},\qquad w(x)\to\pm\mu,
$$
且各固定有限阶 $x$ 导数具有相应界。这也可由
$w'=q-w^2$ 和 $q-2=O(e^{-2|x|})$ 的积分因子直接得到。
初始 $Z$ 的各固定阶 $x$ 导数有更强的尾衰减。

统一以较弱但归纳稳定的指数记账：
$$
U_m,T_m=O(e^{-4\mu|x|}),\qquad
W_m=O(e^{-3\mu|x|}),
\tag{17}
$$
同时包含任意预先固定的有限阶 $x$ 导数。
在帽端 $dV=0$，所以与均值场的任何二次源在那里消失。
由有限个满足 (17) 的模式相乘，
$$
P,Q,R=O(e^{-6\mu|x|}),\quad
C=O(e^{-5\mu|x|}),\quad
J,f=O(e^{-4\mu|x|}).
\tag{18}
$$
因此每个真实源 $f$ 属于 $L^2(\mathbb R)$。
偶数阶不含核；奇数阶由 (16) 保证核正交。R12 因而给出真实
$H^2$ 逆解 $\eta$，没有有限区间 Robin 代换。

还需尾衰减。对 $x\ge2$，$\cosh2>3$ 与 $A<5/2$ 给 $q>3/2$。
取 $\beta=3\mu$、$b(x)=e^{-\beta(x-2)}$。对任一 $m\in4\mathbb N$，
$$
L_mb=(m^2q-18)b\ge6b.
$$
$H^2$ 解 $\eta,\eta'$ 趋零。由 (18) 取足够大常数 $B$，
使 $Bb\pm\eta$ 在左端非负，且
$L_m(Bb\pm\eta)\ge6Bb-|f|\ge0$。
内部负最小值原理给 $|\eta|\le Bb$。
由 $\eta''=m^2q\eta-f$、尾积分及继续求导，其各固定有限阶导数
都为 $O(e^{-3\mu|x|})$。另一端相同。代回 (4) 恢复 (17)，归纳闭合。

用真实极点图坐标 $(\xi,\zeta)=(a\cos\theta,a\sin\theta)$。
每次 Cartesian 求导至多花费一个 $O(h)$ 因子；角频在每个指定阶有限。
式 (17) 因而给非均值场及其前两阶 Cartesian 导数
$$
|Y_{\ne0}|=O(a^3),\qquad |DY_{\ne0}|=O(a^2),\qquad
|D^2Y_{\ne0}|=O(a).
$$
补零即得 $C^2$ 场及零二 jet。均值 $V$ 在帽端本来就是常向量，
亦全局 $C^2$。所以每个 $Y_j$ 是真实闭面上的合法场。

## 6. 完整度量恒等式及限制

展开 (6) 中有限多项式的度量。一次项由 $\mathcal B_X(Z)=0$ 消失，
二次至 $N$ 次非均值系数由 (15) 逐项消失，剩余恰为 (7)。
这里包含所有由有限场乘积产生的角频，包括高于 $4N$ 的频率，
没有将它们删掉。充分小参数的嵌入与平均度量正定性来自闭嵌入的
$C^1$ 开放性和紧性。

本结果没有提供各阶系数增长率、统一收敛半径或给定 $\varepsilon$ 的后验零解。
真实 R11 固定平尾的全频边界源逆仍须另外支付；即使紧支均值方向不改远帽势，
其非均值逆解也不能未经匹配就当作 R72 真尾。有限振幅浮点计算只属于
近似输入，不能据残差小登记主任务完成。

## 附注：全局深度方向的另一准确分母

数值探索若采用更宽的轴对称方向 $V_A=\partial_A X_A|_{A=A_4}$，
其中 $h_A''=(2-A\operatorname{sech}^2x)h_A$ 且初值固定，同一微分恒等式给
$$
f_{V_A}=L_4\dot\eta+16\operatorname{sech}^2x\,y,\qquad
\kappa_A=16\int_{\mathbb R}\operatorname{sech}^2x\,y^2\,dx>0.
$$
由 $\int\operatorname{sech}^{p+2}x=(p/(p+1))\int\operatorname{sech}^p x$，
$$
\frac{\kappa_A}{\|y\|_2^2}
=\frac{128\sqrt2}{8\sqrt2+1}\in(14,16).
$$
这解释了深度变化的低模横截性，但不把任意非零深度改动自动纳入
R12 原背景的高频谱隙；本文主定理使用 (8)、(9) 的紧支方向。
