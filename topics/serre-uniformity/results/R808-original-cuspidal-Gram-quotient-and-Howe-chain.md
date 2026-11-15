# R808：原 cuspidal 轨道格、split 向量与双变量振子链

日期：2026-11-15。状态：**原轨道格的非退化约化商、原 period/split/torus 像及振子链已证明；实际 sigma 源的同 h 配对尚未证明。**

本篇接续 R727、R770，以及 FT、OP、QS
（notes/2026-11-15-sigma-horizontal-quintic-lift-and-Steinberg-coefficients.md）。
这里不把一个统一的 Steinberg 表示直接冒认为所有原 cuspidal 表示。
先用原 R727 的全部群元素矩阵系数构造准确商，
再将该商与双变量振子的一个实际链比较。

## 1. 原稳定轨道格及其 Gram 商

固定原允许标签
$$
7\le h\le p-4,\quad h\equiv1\pmod6,\quad(h,p+1)=1,
$$
并置
$$
r=\min(h-1,p-h).
\tag{CH1}
$$
r 是偶数。因 h=(p+1)/2 不可能 primitive，
$$
2r\le p-3.
\tag{CH2}
$$

令 mathsf G=PGL_2(F_p)，保留原 R727 的有限 cuspidal 表示、
原 split 向量 e_0 和原 Hermitian 型 G。
在所选 p-adic 嵌入处取包含原 character 值的非分歧整数环 O，
并定义实际稳定轨道格
$$
\Lambda_h=\sum_{g\in\mathsf G}O\,(g e_0).
\tag{CH3}
$$
这是有限生成、无挠且 mathsf G 稳定的 O 模；
并不假定旧 e_a 格在 Weyl 元素下稳定。

R727(727.16) 对全部 g 证明配对整性，且若
g=[[a,b],[c,d]]、delta=ad-bc，则
$$
G(e_0,g e_0)\equiv
-P_{h-1}\!\left(\frac{ad+bc}{\delta}\right)\pmod p.
\tag{CH4}
$$
由不变性，任意两个轨道生成元的配对
G(g e_0,g'e_0)=G(e_0,g^(-1)g'e_0) 也整。
所以 G 准确降到 bar Lambda_h=Lambda_h/pLambda_h；
只需再商掉该约化型的 radical。

原 character 的复共轭为 theta_h mapsto theta_h^(-1)。
在这里的非分歧剩余域 F_(p^2) 上，它正是 Frobenius c mapsto c^p。
下面的模型首先在 F_p 上定义双线性型，
再以该 Frobenius 延伸为原规范的 Hermitian 型。
所有显示 Gram 系数均在 F_p；不把此半线性共轭换成无关的恒等共轭。

## 2. 一个完全匹配的有限表示

令
$$
W_r=\operatorname{Sym}^{2r}(k^2)\otimes\det^{-r}.
\tag{CH5}
$$
用标准 covariant 约定：
g 作用于 X、Y 时分别送到 aX+cY、bX+dY，
再乘 delta^(-r)。
这是真正的 PGL_2(F_p) 表示，因标量矩阵作用抵消。
记
$$
v_{\rm sp}=X^rY^r.
$$
split 对角环面准确固定这个向量。

在基 X^jY^(2r-j) 上取通常的 SL_2 不变双线性型，
其反对角系数为 (-1)^j/binom(2r,j)，其余为零，
再作唯一标量归一化使
$$
\langle v_{\rm sp},v_{\rm sp}\rangle=-1.
\tag{CH6}
$$
(CH2) 保证所有相关阶乘和二项式都是单位，所以此型非退化。
det^(-r) 正好抵消 GL_2 的 similitude 因子；
因此它是 mathsf G 不变型。

原整数恒等式
$$
\delta^{-r}[X^rY^r]\,
(aX+cY)^r(bX+dY)^r
=P_r\!\left(\frac{ad+bc}{\delta}\right)
$$
给
$$
\langle v_{\rm sp},g v_{\rm sp}\rangle
=-P_r\!\left(\frac{ad+bc}{\delta}\right).
\tag{CH7}
$$
R770(770.33) 的准确反射
P_(p-1-n)=P_n mod p 表明
P_r=P_(h-1)。
所以 (CH7) 对每个 g 都与原 (CH4) 相同，
不只是在 CM 环面上有相同的一个范数。

为完整说明轨道张成，Sym^n(k^2)、n=2r<p 的
SL_2(F_p) 限制是不可约的：
若子空间被全部上、下单参根群保持，
把 exp(te) 和 exp(tf) 展成次数小于 p 的 t 多项式，
在 t in F_p 的 Vandermonde 评价迫使该子空间被 e、f 保持。
h 的权 2j-n 两两不同模 p，故可取出某个单项式；
e、f 的内部系数 1,...,n 均非零，于是连接全部单项式。
因此 v_sp 的 mathsf G 轨道张成 W_r。

现在取自由 k 模 k[mathsf G]，将基向量 [g] 分别送到
g bar e_0 及 g v_sp。两边由 (CH4)、(CH7) 拉回的全部 Gram 矩阵相同。
后一边轨道张成且型非退化，所以其映射核恰为公共 Gram radical；
前一边的同一 radical 恰是 bar Lambda_h 的 radical 的逆像。
由此得到保持原 split 向量和全部群作用的准确同构
$$
\boxed{
\overline\Lambda_h/\operatorname{rad}G
\ \simeq\ W_r,\qquad
\overline e_0\longmapsto v_{\rm sp}.
}
\tag{CH8}
$$
这是由实际原轨道格和原型得到的非退化商。
它没有声称整个 p-1 维 cuspidal 约化就是 W_r，
也没有把其 radical 或另一组成因子丢失的信息当成已控制。

## 3. 原 period basis 中的 torus 与 split 平均像

保留原 period basis (zeta,1)，zeta^2+zeta+1=0，
s=zeta-zeta^2，故 s^2=-3。
原 CM torus 是
$$
\mathsf T_\zeta=
\left\{
\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}
\right\}/F_p^\times.
\tag{CH9}
$$
在 (CH5) 的标准向量多项式中，取
$$
v_1=\zeta X+Y,\qquad v_2=\zeta^2X+Y.
$$
它们是 (CH9) 的特征向量，特征值分别为
a-zeta^2 b、a-zeta b；两特征值互为 Frobenius 共轭。
尤其
$$
v_1v_2=X^2-XY+Y^2.
\tag{CH10}
$$
这个减号是 covariant 向量多项式的对偶二次型。
它不能与 period 坐标中被矩阵保 similitude 的
x^2+xy+y^2 混用。

因 2r<p+1，W_r 的 mathsf T_zeta 不变线唯一，
由 v_1^r v_2^r 张成。令
$$
\mathsf P_T=\frac1{p+1}\sum_{t\in\mathsf T_\zeta}t.
$$
将 X^rY^r 用 v_1、v_2 展开，平衡项系数准确为
$$
s^{-r}P_r(-1/s)=s^{-r}P_r(1/s),
$$
最后一步使用 r 偶。
所以原 split 向量的平均像完整写成
$$
\boxed{
\mathsf P_Tv_{\rm sp}
=s^{-r}P_r(1/s)(X^2-XY+Y^2)^r.
}
\tag{CH11}
$$
没有只改 torus 而保留错误的 split 向量。

同时
$$
[X^rY^r](X^2-XY+Y^2)^r=s^rP_r(1/s).
$$
结合 (CH6) 得
$$
\boxed{
\langle v_{\rm sp},\mathsf P_Tv_{\rm sp}\rangle
=-P_r(1/s)^2=-P_{h-1}(1/s)^2.
}
\tag{CH12}
$$
未归一化 trace 多一个 p+1 因子，约化后该因子为一。
这正是原 R727 的 N_h 约化；
由 (CH8) 同时保持的是原 u_h 与原 period/split 标记。

## 4. 在五次 lift 空间上的真正原 torus 作用

先把原 period 坐标写为 (x,y)，避免与 (CH5) 的向量变量 X、Y 混淆。
(CH9) 的矩阵保
$$
Q_\zeta(x,y)=x^2+xy+y^2
$$
的 similitude，乘子 nu=a^2+ab+b^2=det g。
设
$$
C=\begin{pmatrix}1&1/2\\0&\sqrt3/2\end{pmatrix},
\qquad z=x+y/2,\quad t=\sqrt3\,y/2.
\tag{CH13}
$$
则 Q_zeta=z^2+t^2，且准确有
$$
CgC^{-1}=
\begin{pmatrix}
a+b/2&-\sqrt3\,b/2\\
\sqrt3\,b/2&a+b/2
\end{pmatrix}.
\tag{CH14}
$$

取 gamma^2=nu。QS 五次 lift 后的向量在总偶子空间中。
在这个完整商空间上定义
$$
\rho_{\rm pos}(g)
=\gamma^{p-1}T_{CgC^{-1}/\gamma}.
\tag{CH15}
$$
右边的变量替换是正交的，因此与 QS 的完整 mathcal K 交换。
gamma 改号时，替换同时改号；总偶性使其作用不变。
原矩阵乘 F_p^\times 标量时，额外因子为 lambda^(p-1)=1。
乘法的平方根符号也由总偶性消去。
所以 (CH15) 是原 PGL torus 的真正水平作用。

在总度 p-1 上，gamma 的次数准确抵消，
(CH15) 就是自然的 T_(CgC^{-1})，没有遗漏 det 的二次角色。
在原坐标中的特征线性式为
$$
u=x-\zeta^2y=z+\iota t,\qquad
v=x-\zeta y=z-\iota t,\qquad \iota\sqrt3=s.
$$
若 lambda=a-zeta^2b、q=lambda^(p-1)，
则 g 的两个特征值是 lambda、lambda^p，
且
$$
u^n v^{p-1-n}
\quad\hbox{的字符为}\quad
q^{-n-1}.
\tag{CH16}
$$
因此 n=h-1 精确对应原 theta_h(q)=q^(-h) 方向。
这补齐了 QS 抽象 rho(q) 与原 period torus 的具体常数运输。

这里的“位置 torus”选择的是振子链的标签。
它与下一节链内部的 oscillator SL_2 作用是两种不同、互相交换的作用，
不能把这两次出现的原矩阵族混成同一个操作。

## 5. 每个位置字符链恰是上述对称幂

在 u、v 中，
$$
z^2+t^2=uv,\qquad
\partial_z^2+\partial_t^2=4\partial_u\partial_v.
$$
定义
$$
E=uv,\qquad F=-\partial_u\partial_v,\qquad
H=u\partial_u+v\partial_v+1.
\tag{CH17}
$$
它们满足 [E,F]=H、[H,E]=2E、[H,F]=-2F。
下式与 (CH21) 中的 $X$ 是辅助曲线 $Y^2=X^3+16$ 的坐标，
与 (CH5) 表示模型的形式变量区分。原标量 oscillator 连接成为
$$
D+\frac13F-\frac{3X}{4}E.
\tag{CH18}
$$

对原 h，令 ell=p-1-2r。
若 h<=(p+1)/2，取 c_j=u^jv^(ell+j)；
若 h>=(p+1)/2，取 c_j=u^(ell+j)v^j，
其中 0<=j<=2r。
这恰是 (CH15) 的字符 theta_h 子空间。
直接求导得到
$$
Ec_j=c_{j+1},\qquad
Fc_j=j(2r+1-j)c_{j-1},\qquad
Hc_j=(2j-2r)c_j.
\tag{CH19}
$$
两端不存在的基向量按零处理；
第二式使用 ell+1=p-2r，不能提前用错误的整数长度。

映射
$$
c_j\longmapsto
\frac{r!}{(2r-j)!}X^jY^{2r-j}
\tag{CH20}
$$
把 (CH19) 准确识别为 Sym^(2r) 的标准 Lie 作用，
并且特意把中心向量 c_r 送到原 v_sp=X^rY^r。
所有显示阶乘都小于 p。
链内部对有限 PGL_2(F_p) 的延伸明确采用 (CH5) 的 det^(-r) 规范，
由原 split 矩阵系数固定，不任意添加行列式二次扭。

(CH18) 对应于二阶连接矩阵
$$
M_{\rm GM}=
\begin{pmatrix}0&3X/4\\-1/3&0\end{pmatrix}.
\tag{CH21}
$$
其下分量满足 D^2A=-XA/4；
向量 (-3DA,A)^t 正是已用的 Hasse 水平向量。
所以原 Hasse/oscillator 结构与 (CH8) 的实际有限商在这里使用同一标量连接。

在八个有限 sigma 通道中，字符链保留全部
M_e tensor I+I tensor M_o 项；
FT 的可分平凡化可运输这些项，不能在原源里直接删去它们。
真正位置字符投影与完整 mathcal K 交换，
故可以把 QS 的五次 lift 源方程逐 h 限制到这些链。

## 6. 尚缺的准确 sigma 配对

以上已完整识别：

1. 原 cuspidal 轨道格的非退化 Gram 商；
2. 原 e_0 的 split 向量、原 T_zeta 平均像和 N_h；
3. 同一 h 的位置字符链及其中心向量；
4. 链上的原 Gauss–Manin/oscillator 连接。

但实际 QS 原向量是
$$
(6B)^5\sum_i f_i g_{N-1-i}\,
z^{6i+6}t^{p-7-6i}
$$
的指定有限通道。
(CH16) 的字符中心则是 u^(h-1)v^(p-h)。
将 z=(u+v)/2、t=(u-v)/(2iota) 代入，会产生完整 Krawtchouk 混合；
其 h 系数不是由上面识别自动等于原 f_i g_(N-1-i)。
原投影障碍 DP 已明确禁止直接把这种混合忽略。

因而：一个真正位置 Cartan 投影非零，
或其链内原 toric 平均非零，
目前仍不能替换 R770 要求的同一原标签乘积。
需要继续从完整八通道源、原 period 标记或实际配对中证明
该指定输出与原两条 Cartier 系数相连；
不能只因为两个表示中都出现 P_(h-1) 就声明算术桥完成。

本篇没有增加有限素数扫描，也没有推断未筛 critical 或真正 primitive/Legendre 非零。
