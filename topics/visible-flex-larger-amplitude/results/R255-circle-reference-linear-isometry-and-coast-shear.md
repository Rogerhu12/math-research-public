# R255. 精确圆参考的线性等距模态、coast 仿射传播与非正规剪切

日期：2026-11-14。

**状态。** 本文是精确未截频圆参考上的完整条件证明，不使用新数值。它说明为什么 coast 的大 $k^2$ 矩阵项并不产生 $k^2$ 指数增长，以及为什么谱值很小仍可有很大的传播范数。它不把真实非圆 warm、物理 $\phi$ 截频场、FFT 投影或实际全设计 Jacobian 等同于这个圆参考。

## 1. 固定的参考面、度量与变分

令 $I$ 为区间，$a\in C^2(I)$，并假设
$
a(s)>0,\qquad |a'(s)|<1.
$
记
$
p=a',\qquad w=\sqrt{1-p^2}>0,\qquad b=a''.
$
取 $z'=w$，定义精确圆参考
$
F(s,\theta)=a(s)e_r(\theta)+z(s)e_z,
$
其中
$
e_r=(\cos\theta,\sin\theta,0),\qquad
e_\theta=(-\sin\theta,\cos\theta,0),\qquad e_z=(0,0,1).
$
于是
$
F_s=p e_r+w e_z,\qquad F_\theta=a e_\theta,\qquad
F^*e=ds^2+a(s)^2d\theta^2.
\tag{255.1}
$

这里固定完整 scalar $a(s)$ 和共同材料角 $\theta$。不同时变更 core 的材料图，也不变更设计参数。撇号表示同一个连续函数的真实导数；若某程序把 a、ap、app 按独立有限求积公式提供，必须先核其导数身份，不能仅凭字段名套用本定理。令一个变分向量场为
$
V=u(s,\theta)e_r+v(s,\theta)e_\theta+h(s,\theta)e_z.
$
线性等距条件是
$
\delta g_{ij}
=\langle V_i,F_j\rangle+\langle F_i,V_j\rangle=0.
$
直接求导给出
$
V_s=u_s e_r+v_s e_\theta+h_s e_z,
$
$
V_\theta=(u_\theta-v)e_r+(u+v_\theta)e_\theta+h_\theta e_z.
$
因此三个独立条件恰为
$
\boxed{\begin{aligned}
p u_s+w h_s&=0,\\
a v_s+p(u_\theta-v)+w h_\theta&=0,\\
u+v_\theta&=0.
\end{aligned}}
\tag{255.2}
$
这三个等式分别来自 $ss,s\theta,\theta\theta$ 分量；没有删去高度均值来代替第一式。

以下逐模态结论只需这些导数有意义。由于 $a\in C^2$、$a,w>0$，得到的 ODE 系数为 $C^1$，所以模态解实际上具有所需的二阶 $s$ 正则性。

## 2. 定理 R255-A：每个非零角模态的精确二维系统

固定整数 $k\ge1$。先取一个实 parity：
$
u=U(s)\cos(k\theta),\qquad
h=H(s)\cos(k\theta),\qquad
v=V_k(s)\sin(k\theta).
$
由第三式
$
U+kV_k=0,\qquad V_k=-U/k.
\tag{255.3}
$
代入第二式，其 $\sin(k\theta)$ 系数为
$
aV_k'-pkU-pV_k-wkH=0.
$
再用 (255.3)，得到
$
aU'=p(1-k^2)U-wk^2H.
\tag{255.4}
$
第一式给出 $pU'+wH'=0$。因此
$
\boxed{
\binom{U}{H}'=\frac1a N_k\binom{U}{H},\qquad
N_k=
\begin{pmatrix}
p(1-k^2)&-wk^2\$2pt]
p^2(k^2-1)/w&pk^2
\end{pmatrix}.}
\tag{255.5}
$

**必要性和充分性。** 上述推导证明必要性。反过来，任何 (255.5) 的解，连同 $v=-U\sin(k\theta)/k$，满足 (255.2) 的三个等式，因此给出固定 (255.1) 度量的一阶等距变分。

另一个实 parity 为
$
u=U\sin(k\theta),\qquad h=H\sin(k\theta),\qquad
v=U\cos(k\theta)/k,
$
其 $(U,H)$ 满足同一个二维系统。系数不依赖角度，所以不同 $k$ 和两个 parity 不互相耦合。对具有足够正则性的 Fourier 展开，可以逐项应用；本文不依赖任意粗糙级数的形式求导。

### 2.1 零模态另行处理

不能在 $k=0$ 代入 $v=-U/k$。对角度无关的 $u_0,v_0,h_0$，第三式首先强制 $u_0=0$。第一式与 $w>0$ 给出 $h_0'=0$。第二式变为
$
a v_0'-p v_0=0,\qquad (v_0/a)'=0.
$
因此零模态只包含共同竖直平移 $h_0=\text{常数}$ 和轴向刚体旋转 $v_0=C a$。

### 2.2 $k=1$ 的核对

当 $k=1$ 时，(255.5) 化为
$
U'=-wH/a,\qquad H'=pH/a.
$
故 $H=C a$、$U=C_0-Cz$。对应上述 cosine parity 的三维变分为
$
V=C_0 e_x+C(-z e_x+a\cos\theta\,e_z),
$
即水平平移和绕水平轴的刚体转动；另一个 parity 给出另两项。连同零模态，恰好核对了欧氏刚体变分的六个自由度。这也是 (255.3) 中符号的一项直接检验。

## 3. 正交变量 $P,Q$ 揭示 shear 与曲率耦合

定义
$
P=pU+wH,\qquad Q=-wU+pH.
\tag{255.6}
$
矩阵
$
R=\begin{pmatrix}p&w\\-w&p\end{pmatrix}
$
为正交矩阵，$\det R=1$。因此在每个固定 $s$，
$
P^2+Q^2=U^2+H^2.
$
这不是通过一个病态相似变换人为缩小范数。

由 $p'=b$、$w'=-pb/w$，
$
R'R^T=
\begin{pmatrix}0&-b/w\\b/w&0\end{pmatrix}.
\tag{255.7}
$
另一个直接矩阵乘法给出
$
R N_k R^T=
\begin{pmatrix}
0&0\\
(k^2-p^2)/w&p
\end{pmatrix}.
\tag{255.8}
$
所以 (255.5) 与下式严格等价：
$
\boxed{
\begin{aligned}
P'&=-\frac{b}{w}Q,\\
Q'&=\frac{b+(k^2-p^2)/a}{w}P+\frac{p}{a}Q.
\end{aligned}}
\tag{255.9}
$
这里 $P$ 是变分在参考子午线切向 $F_s$ 上的分量；$Q$ 是相应法向分量。大的 $k^2$ 项首先表现为从 $P$ 向 $Q$ 的耦合。若 $b=0$，反方向耦合完全消失，这正是下一节的精确仿射传播机制。

## 4. 定理 R255-B：常斜率 coast 的完整传播恰为仿射

设在某区间内
$
p(s)\equiv p_0,\qquad |p_0|<1,\qquad
a(s)=a_0+p_0(s-s_0)>0,\qquad a_0=a(s_0).
\tag{255.10}
$
此时 $w=w_0=\sqrt{1-p_0^2}$ 和 $N_k=N$ 均为常数。

**代数恒等式。**
$
\boxed{N^2=p_0N.}
\tag{255.11}
$
例如，可写成秩一分解
$
N=
\binom{1}{-p_0/w_0}
\begin{pmatrix}p_0(1-k^2)&-w_0k^2\end{pmatrix}.
\tag{255.12}
$
右行乘左列等于 $p_0$，即得 (255.11)。

**传播公式。** 对任意初值 $X_0=(U_0,H_0)^T$，唯一解为
$
\boxed{
X(s)=E(s,s_0)X_0,\qquad
E(s,s_0)=I+\frac{s-s_0}{a_0}N.}
\tag{255.13}
$
证明不需要除以 $p_0$。令 $t=s-s_0$，则
$
E'=\frac{N}{a_0},
$
而利用 (255.11)，
$
\frac{N}{a(s)}E
=\frac{N+(t/a_0)N^2}{a_0+p_0t}
=\frac{N(1+p_0t/a_0)}{a_0+p_0t}
=\frac{N}{a_0}.
$
又 $E(s_0,s_0)=I$，由线性 ODE 唯一性即得结论。这个直接证明同时涵盖 $p_0=0$ 的圆柱 coast；此时 $N^2=0$，仍有同一公式。

因此 $U,H$ 关于 $s$ 严格仿射。由于 $v$ 的模态系数为 $-U/k$ 或 $U/k$，全部三分量模态亦严格仿射。这里说的是精确圆参考的变分，不是在声称一个实际非圆 BVP 状态沿 coast 必定仿射。

对于 $p_0\ne0$，也可以用
$
\int_{s_0}^s\frac{d\sigma}{a(\sigma)}
=\frac1{p_0}\log\frac{a(s)}{a_0}
$
检查矩阵指数与 (255.13) 一致。指数中的可变系数积分和最小多项式恰好消去所谓 $k^2$ 指数因子；不能把一个瞬时大矩阵项直接乘以区间长度来推测真实传播。

### 4.1 在正交变量中是显式剪切

coast 上 $R$ 为常数。令
$
c_k=\frac{k^2-p_0^2}{w_0}>0,\qquad
r=\frac{a(s)}{a_0}=1+\frac{p_0t}{a_0},\qquad
\sigma=\frac{t\,c_k}{a_0}.
$
由 (255.8)，
$
\boxed{
\binom{P(s)}{Q(s)}
=
\begin{pmatrix}1&0\\ \sigma&r\end{pmatrix}
\binom{P(s_0)}{Q(s_0)}.}
\tag{255.14}
$
特别地 $P(s)=P(s_0)$，
$
Q(s)=rQ(s_0)+\sigma P(s_0).
$
这精确显示了大 $k^2$ 项引起的 shear。

## 5. 强非正规性与“不出现 $k^2$ 指数增长”的精确含义

### 5.1 瞬时谱与矩阵范数分离

由 (255.11) 或秩一分解，$N$ 的特征值为 $0,p_0$，故生成矩阵 $N/a(s)$ 的谱为 $0,p_0/a(s)$，与 $k$ 无关。但其二范数为
$
\boxed{
\|N\|_2
=\frac{\sqrt{k^4-2p_0^2k^2+p_0^2}}{w_0}
\sim\frac{k^2}{w_0}.}
\tag{255.15}
$
证明是对 (255.12) 的秩一乘积取两个向量的欧氏范数。

在正交 $P,Q$ 坐标中，$N$ 变成
$
B=\begin{pmatrix}0&0\\c_k&p_0\end{pmatrix}.
$
有
$
BB^T-B^TB=
\begin{pmatrix}
-c_k^2&-c_kp_0\\
-c_kp_0&c_k^2
\end{pmatrix}\ne0.
\tag{255.16}
$
所以对于每个 $k\ge1$、$|p_0|<1$，它确实是非正规矩阵。正交相似保持正规性，原 $N$ 亦然。$p_0=0$ 时它是非零幂零矩阵，是同一机制的极端情形。

### 5.2 传播的精确范数

(255.14) 的两个特征值为 $1,r$，所以传播的谱半径为
$
\max(1,r),
$
仍与 $k$ 无关。令
$
T=1+\sigma^2+r^2.
$
由于传播矩阵的行列式为 $r>0$，其最大奇异值满足
$
\boxed{
\|E(s,s_0)\|_2^2
=\frac{T+\sqrt{T^2-4r^2}}2.}
\tag{255.17}
$
这是直接计算
$
\begin{pmatrix}1&\sigma\\0&r\end{pmatrix}
\begin{pmatrix}1&0\\\sigma&r\end{pmatrix}
=
\begin{pmatrix}1+\sigma^2&\sigma r\\\sigma r&r^2\end{pmatrix}
$
的特征值所得。正交坐标变换使这也是 $(U,H)$ 的二范数。

特别地
$
\sqrt{1+\sigma^2}\le\|E\|_2
\le\sqrt{1+\sigma^2+r^2}.
\tag{255.18}
$
在 $a_0>0$、$p_0\in(-1,1)$、$t\ne0$ 固定且区间满足 $a>0$ 时，
$
\|E\|_2\sim \frac{|t|\,k^2}{a_0w_0}
\qquad (k\to\infty).
\tag{255.19}
$
这是关于频率的多项式放大，不是 $\exp(Ck^2|t|)$。对固定 $k$，(255.13) 又说明传播矩阵关于区间长度严格仿射。

这不等于“高频安全”或“矩阵条件数很小”。很大的剪切完全能放大误差、造成坏尺度并损害某个数值消元过程；单看特征值会漏掉这件事。同样，一般 Gronwall 估计若使用 $\int\|N/a\|$ 得到一个带 $k^2$ 的指数**上界**，仍可能是正确但极不锐的上界。该上界不能被误读为本 coast 的实际增长率。

## 6. 可选三分量扩展：代数恒等式全空间成立，等距条件只在约束子空间成立

为了准确区分某些三分量演化表示与固定 $g$ 变分，考虑列次序 $(U,H,V_k)$ 的显式扩展系统
$
\begin{pmatrix}U\\H\\V_k\end{pmatrix}'
=\frac1a K
\begin{pmatrix}U\\H\\V_k\end{pmatrix},
$
$
K=
\begin{pmatrix}
p(1-k^2)&-wk^2&0\\
p^2(k^2-1)/w&pk^2&0\\
kp&kw&p
\end{pmatrix}.
\tag{255.20}
$
它的前两行是 (255.5)，第三行是 (255.2) 的混合分量条件。定义角度量约束
$
\ell=U+kV_k.
$
直接相加得到
$
\boxed{\ell'=(p/a)\ell,\qquad (\ell/a)'=0.}
\tag{255.21}
$
因此 $\ell=0$ 的二维子空间保持不变，并且恰好还满足
$\delta g_{\theta\theta}=0$。在这个子空间内，(255.20) 与定理 R255-A 完全等价。

对任意不满足 $\ell=0$ 的初值，(255.20) 仍使
$\delta g_{ss}=\delta g_{s\theta}=0$，但
$
\delta g_{\theta\theta}=2a\ell\cos(k\theta)
$
一般非零。它保持的是这个角度量相对缺陷沿 $s$ 的比值，并不能称为固定 $g$ 的等距变分。

在常 $p$ coast 上，写
$
K=\begin{pmatrix}N&0\\d^T&p\end{pmatrix},
\qquad d^T=(kp,kw).
$
除了 $N^2=pN$，直接计算还给出 $d^TN=0$。于是
$
\boxed{K^2=pK}
\tag{255.22}
$
作为三维全空间的纯代数恒等式成立，而不限于 $\ell=0$ 子空间。因此这个**明确定义的扩展系统**也有传播
$
I+\frac{s-s_0}{a_0}K.
\tag{255.23}
$
(255.22) 的全空间性质不能消除 (255.21) 的固定度量约束。是否某个实现的完整连续 Frenet RHS 正好具有 (255.20) 的线性化，须由该 RHS 的定义另行核对；是否其物理截频和离散 Jacobian 继承该式，更不能由本节自动推出。

## 7. 非常斜率 bridge：局部尺度解释及其限度

对于一般 $b=a''$，(255.9) 的瞬时系数矩阵为
$
A_k(s)=
\begin{pmatrix}
0&-b/w\$2pt]
\bigl(b+(k^2-p^2)/a\bigr)/w&p/a
\end{pmatrix}.
$
冻结某一位置的所有系数时，其特征多项式为
$
\boxed{
\lambda^2-\frac pa\lambda+
\frac{b}{w^2}\left(b+\frac{k^2-p^2}{a}\right)=0.}
\tag{255.24}
$
因此在固定 $a,w>0$、固定 $b\ne0$ 的高频极限，冻结矩阵的主尺度是
$
|\lambda|\asymp k\sqrt{\frac{|b|}{a w^2}}.
\tag{255.25}
$
当 $b>0$，高频主部给出虚共轭频率；当 $b<0$，给出一正一负的实主部。这是精确的**冻结局部矩阵**计算，不是可变系数 bridge 的全局谱定理，也不是整个设计边值问题的条件数定理。

由此可形成一个供数值网格选择参考的局部长度
$
\ell_k(s)=\frac{w\sqrt a}{k\sqrt{|a''|}},
\qquad a''\ne0.
\tag{255.26}
$
要解析这种局部变化，可以把步长与 $\ell_k$ 比较。同时，coast 型的单步剪切尺度
$
\frac{\Delta s\,k^2}{a w}
\tag{255.27}
$
仍可能影响数值尺度。两者描述不同机制；(255.27) 大并不证明存在 $k^2$ 指数不稳定。

系数随 $s$ 变化时，不同 $A_k(s)$ 一般不交换；$a''$ 的过零、材料图、边界条件以及实际离散方式都可能重要。没有额外一致控制，不能把 (255.25) 当作变系数传播范数的严格上下界。本文不给当前 bridge 宣布未经计算的安全网格或严格谱界。

## 8. 对连续圆参考的离散核对：一个明确条件推论

若某个线性 coast 区间离散残差使用端点值和端点 ODE 导数构造插值，并且对真实仿射解的中点或 collocation 残差精确为零，则它在本参考问题上可以通过 (255.13) 作代数核对。原因是 $X(s)$ 仿射，且
$
X'(s)=N X(s)/a(s)
$
在整个 coast 上都是同一个常向量；匹配这些端点值和导数的 Hermite 插值也就是这条仿射函数。

若消去其他已定义量之后，该区间残差恰写成
$
L X(s_0)+R X(s_1)=0,
$
上述精确性对所有初值成立便推出
$
L+R E(s_1,s_0)=0.
\tag{255.28}
$
只有 $R$ 可逆时，才能进一步写
$
-R^{-1}L=E(s_1,s_0).
$
没有先证 $R$ 可逆，不能把一个矩阵关系冒充一个已存在的离散 transfer；更不能仅凭连续 ODE 有唯一解就推断某种离散块一定可逆。

这个推论有明确的“圆参考、同一度量、未截频、仿射精确的离散残差”前提。它不提供当前实际有限场的 $L,R$ 数值，也不免除真实全状态离散 Jacobian 的检查。

## 9. 与本题实际 full-DN 求解的边界

本定理使用共同材料 $\theta$ 中的精确圆，而现有求解保存物理 $\phi$ 的有限 Fourier 状态，并通过完整材料图联系两种角。一个 $\theta$ 的单模态拉回 $\phi$ 后通常有无限 Fourier 谱；有限投影、FFT 求积和原非线性 RHS 不一定与上述角分解交换。

因此不能从 R255 得到以下未经支付的结论：

- 当前非圆 warm 或真实 BVP Jacobian 恰等于 (255.5) 或 (255.20)；
- 某个物理截频索引 $M$ 可无损直接替代此处材料波数 $k$；
- 全 core、physical、设计参数的完整 Jacobian 都有 coast 的最小多项式；
- 当前 QR、banded 消元或某个端点块已可逆、已良态或必会收敛；
- 换用 [R252](R252-physical-angle-DN-Galerkin-boundary.md) 的有限测试空间已通过其实际边界验收；
- 同一 $g$ 的完整 metric、cut 九 jets、曲率、reach、真实 Hausdorff 幅度或固定 marker 的刚性排除已经成立。

R255 给出的直接用途是一个可核对的解析参考：coast 必须区分大剪切与指数增长，bridge 的局部频率尺度必须与完整离散证据分开。新的实际全场若成功，仍须沿其真实 scalar、材料图、完整均值及本身的尾部完成后续验证。
