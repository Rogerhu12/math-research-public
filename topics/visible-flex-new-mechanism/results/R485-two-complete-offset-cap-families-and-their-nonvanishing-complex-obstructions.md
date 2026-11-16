# R485：两条完整 offset cap 族的复障碍不消失与真实凸曲率近似

日期：2026-11-16。本文是原完整积分的纸面推导；没有执行程序、求积、符号消元、秩计算、人工测试或新的 Actions。冻结 $\psi_3$ 的唯一有向区间观察由根代理另行记录，本文不重复该观察。

## 1. 新结论及其准确范围

[R471](R471-five-real-cap-conditions-and-the-complete-complex-second-moment-interface.md) 的必要条件是完整复积分
$$
\mathcal E(z)=\frac32\int_\ell^T(t+z)^2w_z(t)^2a_z(t)^2q(t)\,dt=0,
\tag{1}
$$
其中 $p=u'$、$r=u''$、$q=u'''>0$，
$$
w_z=p-(t+z)r,\qquad
a_z=u-(t+z)p+\frac{(t+z)^2r}{2},
\tag{2}
$$
而 $z$ 是末端 $a_z(T)=0$ 的上半平面根。所有原左端常数均由真实平端恢复。

本文处理两个可用真实 $A_f>0$ cap 逼近的**完整一参数极限族**：

* 临界 power core $u=C+4t^{5/2}/15$，$0<t<1$；
* uniform core $u=C+(t+1)^3/6$，$-1<t<1$。

这里 $C\ge0$ 由一个遥远、微小但真实的公共左尾提供，不是把紧 profile 任意加常数。两个理想 core 都不被冒充为原合法平端 cap：第一族在 core 上 $A_f=0$；第二族的左端三阶 jet 不平。第5节给完整真实近似。

新结论是：

> **定理。** 两族的完整极限积分 $\mathcal E_C$ 对每个 $C\ge0$ 均非零。每族的虚部在参数允许半轴上恰有一个零；在该零点实部严格负。对任意固定紧参数区间 $0\le C\le C_{\max}$，存在同一个有限远尾尺度、有限拼接窗和有限正曲率正则化，使一整族真实平端 cap 保持 $q>0$、内部 $A_f>0$、末端唯一简单 $A_f$ 零点，并且整族完整 $\mathcal E$ 均非零。

这既给明确的真实族排除，也指出一个拓扑推断的失败处：critical、uniform、exponential 三个 core 值处在不同象限，且大 $C$ 的实部为正，仍不能仅凭这些端值宣称某个参数矩形有非零绕数。本文两条 offset 边都通过**负实轴**，不是一条通过正实轴、另一条通过负实轴。

本文不排除其它允许 cap 的 $\mathcal E=0$，不支付全部五门，不宣称实际成本或旧冻结母库发生任何变化。

## 2. 原锚、常数 offset 与必须保留的项

若原平左端的一个真实尾在 core 入口处满足
$$
u\longrightarrow C,\qquad p\longrightarrow0,\qquad r\longrightarrow0,
$$
则 core 上(2)的准确极限为
$$
w_z=-\int_{\text{core left}}^t(s+z)q(s)\,ds,\qquad
a_z=C+\frac12\int_{\text{core left}}^t(s+z)^2q(s)\,ds.
\tag{3}
$$
特别 $a_z$ 的初值是 $C$，不能在 core 入口重新置零。

总积分仍是(1)。由于 core 左端 $w_z=0$，而右端 $a_z(T)=0$，两个分部积分也准确给
$$
\mathcal E=3\int w_z^2a_z^2\,da_z
=-2\int w_za_z^3\,dw_z.
\tag{4}
$$
左端 $a_z=C$ 并不删去 $C$ 或 $C^2$ 项；(4)端项消失的原因是同一个端点的 $w_z=0$。下面均直接使用(1)，没有以(4)替换原锚。

复杂参数随 $C$ 改变，是同一个完整末端二次方程的根。不能固定 $C=0$ 的复根而只改变被积式。

## 3. Uniform core：一个明确的 cubic 与 quartic

取 $q=1$、$-1<t<1$，
$$
u=C+\frac{(t+1)^3}{6},\qquad
p=\frac{(t+1)^2}{2},\qquad r=t+1.
$$
记
$$
v=C+\frac13,\qquad z=i\sqrt v,\qquad v\ge\frac13.
\tag{5}
$$
末端 $a_z(1)=C+1/3-v=0$。整条 core 的真实极限函数为
$$
w_z=\frac{1-t^2}{2}-i\sqrt v(t+1),
$$
$$
a_z=\frac{t^3-3vt-1+3v}{6}
+\frac{i\sqrt v}{2}(t^2-1).
\tag{6}
$$

把(6)代入原(1)，按 $t$ 的奇偶项积分，得
$$
\boxed{
\operatorname{Re}\mathcal E_C
=\frac2{135135}\,\mathsf R(v),\qquad
\operatorname{Im}\mathcal E_C
=\frac{2\sqrt v}{10395}\,\mathsf I(v),
}
\tag{7}
$$
$$
\mathsf R(v)=27027v^4-39897v^3+7865v^2-39v+116,
$$
$$
\mathsf I(v)=-2079v^3+1089v^2+143v-17.
\tag{8}
$$

为使这个全式可独立按原多项式复核，令 $y=t^2$，
$$
Q_e=v^2-\frac v4+
\left(v^2+\frac{3v}{2}+\frac14\right)y
-\left(\frac{13v}{4}+\frac12\right)y^2+\frac14y^3,
$$
$$
Q_o=2vt(v+1-2y),\quad
P_e=-v+(5v+1)y-y^2,
$$
$$
P_o=t\left(v-\frac12+(3v+2)y-\frac32y^2\right),\quad
k=3v-1,\quad A_o=t(y-3v),\quad B=y-1.
$$
这里 $Q_e+Q_o$ 是 $( (t+i\sqrt v)w_z)^2$ 的实部，
其虚部是 $-\sqrt v(P_e+P_o)$。因此积分前的两条完整偶部是
$$
\begin{aligned}
\frac{2}{3}\operatorname{Re}\mathcal E
={}&\int\left\{
\frac{Q_e(k^2+A_o^2)+2kQ_oA_o}{36}
-\frac v4Q_eB^2
+\frac v6(P_ek+P_oA_o)B\right\}\,dt,\\
\frac{2}{3\sqrt v}\operatorname{Im}\mathcal E
={}&\int\left\{
\frac B6(Q_ek+Q_oA_o)
-\frac{P_e(k^2+A_o^2)+2kP_oA_o}{36}
+\frac v4P_eB^2\right\}\,dt.
\end{aligned}
\tag{9}
$$
只需使用
$$
\int_{-1}^1t^{2j}\,dt=\frac2{2j+1},\quad
\int_{-1}^1t^{2j}(t^2-1)\,dt
=-\frac4{(2j+1)(2j+3)},
$$
$$
\int_{-1}^1t^{2j}(t^2-1)^2\,dt
=\frac{16}{(2j+1)(2j+3)(2j+5)}
$$
即可得到(7)—(8)。这不是只记录最高系数。

### 3.1 唯一虚部零点及实部的严格号

在 $v\ge1/3$，
$$
\mathsf I''(v)=-12474v+2178<0,\qquad
\mathsf I'(1/3)=176>0,
$$
$$
\mathsf I(1/3)=\frac{224}{3}>0,\qquad
\lim_{v\to\infty}\mathsf I(v)=-\infty.
$$
所以 $\mathsf I$ 在允许半轴上恰有一个零 $v_{\mathrm u}$。原有理值给
$$
\mathsf I(3/5)=\frac{1472}{125}>0,\qquad
\mathsf I(5/8)=-\frac{5019}{512}<0,
$$
故
$$
\frac35<v_{\mathrm u}<\frac58.
\tag{10}
$$

在这个整个区间内，可以直接保守估计
$$
\begin{aligned}
\mathsf R(v)
&<28000\frac5{32}
-39000\frac{27}{125}
+8000\frac25+120\\
&=4375-8424+3200+120=-729<0.
\end{aligned}
\tag{11}
$$
负的 $-39v$ 已保守舍去；其余每个严格界的方向与正负号一致。因此(7)两分量不可能同时为零。

特别 $C=0$ 时，
$$
\mathsf R(1/3)=-\frac{1504}{9},\qquad
\mathsf I(1/3)=\frac{224}{3}.
$$
该端值在第二象限。但这并非整个 offset 枝的固定象限：它先经过负实轴，再进入下半平面。

## 4. Critical core：完整的两个新增 primitive 及非零结论

取 $0<t<1$，
$$
u=C+\frac4{15}t^{5/2},\qquad
p=\frac23t^{3/2},\qquad r=t^{1/2},\qquad
q=\frac12t^{-1/2}.
$$
令
$$
z=-\frac13+\frac{2i}{3}\sqrt v,\qquad
C=\frac29\left(v-\frac15\right),\qquad v\ge\frac15 .
\tag{12}
$$
则 $a_z(1)=0$。沿 R478 记
$$
k=\frac{(t+z)r}{p},\qquad w=k-1,\qquad
A(k)=\frac{k^2}{2}-k+\frac35=\frac{w^2+1/5}{2},
$$
$$
B(k)=k^2(1-k)^2=w^2(1+w)^2 .
$$
于是
$$
w_z=p(1-k),\qquad
a_z=C+\frac{p^2}{r}A(k).
$$
原被积密度完整分成
$$
\frac{4C^2}{27}t^{9/2}B
+\frac{32C}{243}t^7BA
+\frac{64}{2187}t^{19/2}BA^2.
\tag{13}
$$
三个分项都保留。

[R478](R478-critical-power-complex-cap-obstruction-and-smooth-positive-approximants.md) 已给最后一项的 primitive
$$
\frac{16}{2187}t^{21/2}\rho(w),
$$
其中 $\rho(w)=\sum_{j=0}^8\rho_jw^j$，
$$
(\rho_0,\ldots,\rho_8)=
\left(
\frac{10156}{363738375},
-\frac{10156}{17320875},
\frac{5078}{911625},
-\frac{788}{160875},
\frac{626}{10725},
\frac4{165},
\frac29,\frac4{35},\frac25
\right).
\tag{14}
$$

其余两个**新增完整 primitive** 是
$$
\frac{32C}{243}t^8S_1(w),\qquad
\frac{4C^2}{27}t^{11/2}S_2(w),
\tag{15}
$$
由原 $tk'=3/2-k$ 精确得到
$$
8S_1-(w-\tfrac12)S_1'=BA,\qquad
\frac{11}{2}S_2-(w-\tfrac12)S_2'=B .
\tag{16}
$$
完整系数为
$$
(S_{1,0},\ldots,S_{1,6})=
\left(
\frac{79}{537600},-\frac{79}{33600},
\frac{79}{4800},\frac1{1200},\frac{47}{480},
\frac1{12},\frac14
\right),
$$
$$
(S_{2,0},\ldots,S_{2,4})=
\left(\frac4{1155},-\frac4{105},
\frac6{35},\frac4{15},\frac23\right).
\tag{17}
$$
例如把(16)乘2，第 $j$ 系数分别满足
$(16-2j)S_{1,j}+(j+1)S_{1,j+1}=2[BA]_j$、
$(11-2j)S_{2,j}+(j+1)S_{2,j+1}=2[B]_j$，
从最高次数向下唯一确定(17)。

在 $t\downarrow0$ 时 $w=O(t^{-1})$。(14)—(15)的真实 primitive 分别是 $O(t^{5/2})$、$O(t^2)$、$O(t^{3/2})$，故左端均为零。这里没有把非零 $C$ 当作零端值。末端 $w=i\sqrt v$，所以完整结果是
$$
\boxed{
\mathcal E_C=\frac{16}{2187}
\left\{\rho(i\sqrt v)
+4(v-\tfrac15)S_1(i\sqrt v)
+(v-\tfrac15)^2S_2(i\sqrt v)\right\}.
}
\tag{18}
$$

### 4.1 全实部、全虚部及其唯一实轴交点

写
$$
\mathcal E_C=\frac{16}{2187}
\left\{\mathsf R_c(v)+i\sqrt v\,\mathsf I_c(v)\right\}.
\tag{19}
$$
逐项收集(18)，得到
$$
\begin{aligned}
\mathsf I_c(v)={}&-\frac{v^3}{21}
+\frac{527v^2}{23100}
+\frac{13181v}{18018000}
-\frac{444637}{1939938000},\\
\mathsf R_c(v)={}&\frac{v^4}{15}
-\frac{173v^3}{2520}
+\frac{15499v^2}{1201200}
-\frac{95131v}{1633632000}
+\frac{4552471}{93117024000}.
\end{aligned}
\tag{20}
$$

在 $v\ge1/5$，
$$
\mathsf I_c''(v)=-\frac{2v}{7}+\frac{527}{11550}<0,
$$
且
$$
\mathsf I_c'(1/5)
=\frac{197}{57750}+\frac{13181}{18018000}>0,\qquad
\mathsf I_c(1/5)=\frac{816064}{1818691875}>0.
$$
其最高系数为负，故允许半轴上恰有一个零 $v_{\mathrm c}$。以下完全有理的保守界已足够夹住它：
$$
\mathsf I_c(12/25)>\frac{109304}{10^9}>0,\qquad
\mathsf I_c(1/2)<-\frac{111}{10^6}<0.
\tag{21}
$$
例如第一式分别使用
$527/23100>2281/10^5$、
$13181/18018000>731/10^6$、
$444637/1939938000<23/10^5$，
以及 $(12/25)^3/21<5267/10^6$；
第二式直接对四个有理数向外放宽即可。它们不是浮点数值测试。

对 $12/25\le v\le1/2$，保留负三次项，舍去负一次项，得
$$
\begin{aligned}
\mathsf R_c(v)
&<
\frac{417+323+5}{10^5}
-\frac{17}{250}\frac{11}{100}\\
&=\frac{745-748}{10^5}
=-\frac3{10^5}<0 .
\end{aligned}
\tag{22}
$$
这里用了 $v^4/15\le1/240<417/10^5$，
$15499v^2/1201200<323/10^5$，
常数项 $<5/10^5$，
以及 $173/2520>17/250$、$v^3>11/100$。
所以(19)也不可能为零。

$C=0$ 时还可把 R478 原系数合成
$$
\mathcal E_0=
\frac{16}{2187\cdot9093459375}
\left(1007744+\frac{4080320}{\sqrt5}i\right),
\tag{23}
$$
它在第一象限。尽管如此，整个 offset 枝的唯一虚部零点仍在负实轴上，而不是正实轴。

## 5. 把常数 core 变成真实平端、严格正 Af 的有限 cap

本节证明第1节的真实适用范围。只要求给定一个紧盒 $0\le C\le C_{\max}$；全部尺度最后取成一个共同有限值。

### 5.1 用真正远尾提供 C

采用真正曲率坐标
$$
V=p^{2/3},\qquad
A_f=6pq-2r^2=9V^2V''.
\tag{24}
$$
取固定 $C^\infty$ 函数 $W$，在 $0<y\le1/8$ 精确等于
$$
W(y)=\{\psi_3'(y-1)\}^{2/3},\qquad
\psi_3(x)=e^{-3/(1-x^2)}.
\tag{24a}
$$
这是原允许的精确左 germ，不把一般平坦函数代替 $\psi_3$。在此 collar，$\psi_3'>0$、$\psi_3''>0$，且 $(y-1)^2\ge49/64>3/5$；原 Af 四次式 $F(t)=27t^4+102t^3-46t^2-10t-1$ 降冪係數恰一次變號，$F(0)<0$、$F(3/5)=1232/625>0$，故唯一正根小於 $3/5$，從而 $A_{\psi_3}>0$。于是
$$
W>0,\qquad W'=\frac{2\psi_3''}{3(\psi_3')^{1/3}}>0,\qquad
W''=\frac{A_{\psi_3}}{9(\psi_3')^{4/3}}>0.
$$
原指数平端保证 $W$ 及全部导数在 $y=0$ 为零。保留这个完整 collar，再以正的 $W''$ 光滑延拓到固定区间的其余部分；积分恢复同一个 $W,W'$，所以三者保持正。记 $J=\int W^{3/2}>0$。

在长为 $L$ 的尾上取
$$
V_L(t)=a_LW\!\left(\frac{t-\ell_L}{L}\right),\qquad
a_L^{3/2}LJ=C+L^{-1}.
\tag{25}
$$
从同一个平左端依次积分 $p=V_L^{3/2}$、$u' =p$。尾末准确提供 $u=C+L^{-1}$，并且在整个紧 $C$ 盒上
$$
p=O(L^{-1}),\quad r=O(L^{-2}),\quad q=O(L^{-3}).
\tag{26}
$$
全部函数及其所有 jets 在真实左端为零。更精确地，在(24a)对应的真实 collar 上，
$$
p(t)=a_L^{3/2}\psi_3'\!\left(\frac{t-\ell_L}{L}-1\right),\qquad
u(t)=a_L^{3/2}L\psi_3\!\left(\frac{t-\ell_L}{L}-1\right).
\tag{26a}
$$
因此它恰是正幅、正仿射 $\psi_3$ 左 germ，属于当前同一允许 cap 类；没有只保持平坦性而换掉原 germ。$V_L''>0$ 给尾内部严格 $A_f>0$。这个尾并非一个任意可选的积分常数。

根 $z$ 在紧 $C$ 盒内保持有界。尾上 $|t+z|=O(L)$、
$w_z=O(L^{-1})$、$a_z=O(1)$，所以原(1)的**完整尾贡献**
$$
|\mathcal E_{\mathrm{tail}}|=O(L^{-2})
\tag{27}
$$
一致趋零。隐含常数允许依赖 $C_{\max}$ 和固定 $W$，不能把它移用于无界 $C$。

### 5.2 正曲率的精确接合，不任意插值端 jets

两 core 的 $V_0$ 在左端分别是正线性函数与正倍数的距离 $4/3$ 次幂。由(25)，真实尾末的 $V,V'$ 均趋零。选择一个趋零的接窗，使右端 core 的值大于尾末值，而两端割线斜率严格位于两端导数之间。

这个严格条件足够给一个精确凸接合。确实，对接窗 $[a,b]$ 的未知曲率 $c=V''$，匹配末端 $V,V'$ 等价于
$$
\int_a^b c=\Delta V',\qquad
\int_a^b(b-t)c(t)\,dt
=\Delta V-(b-a)V'(a).
\tag{28}
$$
严格割线条件正是右边第二量位于
$(0,(b-a)\Delta V')$。先保两端真实 collar 的正曲率，再取足够小的全窗正背景；剩余两个矩仍在这个开区间中。取两个内支撑正 bump，其质心分列所需平均值两侧，用两个正系数准确解(28)。这同时保持全部端 collar、$c>0$ 和真实 $V,V'$ 匹配。所有参数可在固定紧盒中连续选择。

第一族的 core 曲率原来为零，故在 core 内另加一个趋零但严格正的光滑曲率；第二族原曲率已经正。近最终端点 $T$ 统一选
$$
c(t)=\varepsilon(T-t),\qquad \varepsilon>0,
\tag{29}
$$
再用同样的两矩接合与前段相接。最终 $V,V'$ 相对于各理想 core 的误差可一致趋零。式(24)给内部 $A_f>0$，且
$$
A_f(T)=0,\qquad A_f'(T)=-9\varepsilon V(T)^2<0.
\tag{30}
$$
因此这是真正唯一、简单的末端 Af 根。其两侧 germ 还可按(29)延到根的内侧；本文不借此自动授全圆或全部旧母条件。

### 5.3 完整 E 的一致连续性

在接窗上 $r$ 单调，$q\,dt=dr$ 是正测度。接窗的 $p,r$ 一致趋零，$u,z$ 有界，故
$$
\int_{\mathrm{join}} |t+z|^2|w_z|^2|a_z|^2q\,dt
\le C_0\sup_{\mathrm{join}}|w_z|^2\,
\Delta r\longrightarrow0.
\tag{31}
$$
这一步保留接合中可能很大的三阶导数，不假定全局 $C^3$ 小。

在固定 core 上，$u,p,r$ 一致趋向相应完整 offset core，且 $r$ 单调、总变差有统一界。因而 $dr$ 弱收敛；(1)中除 $q\,dt$ 外的因子是一致收敛且一致连续的函数。这证明 core 的完整 Stieltjes 积分收敛。也可沿 R471 的完整局部密度加**两端原 primitive**做同一证明，但不能丢 core 左端的 $C$。

两个理想末端的复判别式在允许紧盒中都有严格正下界。因此真实末端二次方程的上根也一致趋向(5)或(12)，不是把旧 $z$ 冻住。结合(27)(31)，完整真实 $\mathcal E$ 对整个 $C$ 盒一致收敛。

由第3、4节，两条理想函数连续且处处非零；每个紧盒上其模都有严格正下界。先固定这个紧盒，再取一个共同有限 $L$、共同有限接窗与正曲率小量，就使整个真实 cap 族的 $\mathcal E$ 非零。没有执行任何极限 profile，也不需要把某个无限尺度当作实际参数。

## 6. 对全局问题的作用与继续保留的门

本文支付了两个此前只有象限端值的完整族：

1. uniform-offset 的全两分量式(7)，以及允许半轴上的准确非零结论；
2. critical-offset 的全部 $C,C^2$ 原 primitive、全两分量式(18)—(20)，以及准确非零结论；
3. 正曲率远尾、精确两矩接合、末端简单 Af 根和完整有序积分收敛，从而得到真实有限 cap 族的非零。

这些结论说明，不能靠“critical 第一象限、uniform 第二象限、exponential 第三象限、大 offset 第四象限”的端点图直接宣布存在零。本文两个完整 offset 边都有同一个负实轴穿越方向；若要得到非零拓扑 degree，还必须支付其余参数边的完整轨迹或一个真正不同的有限族。

仍未支付的是某个允许 cap 的 $\operatorname{Re}\mathcal E=\operatorname{Im}\mathcal E=0$，更未支付原五个共同 self 条件、其同一实际成本、全十三行或主问题。这里没有改动冻结 $\psi_3$ cap、已发表母数据、旧数值状态或任何仓库 refs。后继的新 cap 搜索及全五门研究继续由根代理统一授权；本文不新增数值观察。
