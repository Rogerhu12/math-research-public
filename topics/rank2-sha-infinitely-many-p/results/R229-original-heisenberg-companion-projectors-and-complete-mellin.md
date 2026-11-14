# R229 — 原协变伴随截面的精确 Heisenberg 投影、八次 tame 类型与完整补偿

日期：2026-11-13。**状态：以下原截面的四挠投影、两个准确多项式、有限角色识别及完整 Mellin 分解已证明。没有由角色分解推出原中央非零。**

本篇接续 [R227](R227-original-covariant-second-order-and-complete-mellin-compensation.md)。
所有对象均是原固定 $A,B,\Theta$ 的实际伴随截面。
投影用原椭圆曲线的 Mumford 运输实现；不是在另一个抽象表示中寻找同维向量。
首行仍保留模 $p^2$，除以 $p$ 前先合并原整行。

## 1. 原 degree-4 坐标与同一 degree-68 空间

在 $E_0:y^2=x^3-x$ 的原微分坐标上，置
$$
T=\vartheta(2z)=\sigma(z)^4(x^2+1),\quad
F=\sigma(z)^4(x^2-1)=T\rho,\quad
G=2x\sigma(z)^4=T\phi,\quad H=2y\sigma(z)^4.
$$
于是
$$
F^2+G^2=T^2,\qquad H^2=2FG,\qquad
\Theta=T^{17},\qquad
\nu=-\frac H{2T},\quad
t=4q=\frac{G^2}{T^2},\quad
\xi=\frac{H^4}{16T^4}.                                    \tag{1}
$$
在原点，$T=F=1+O(z^4)$、$G=2z^2+O(z^6)$、$H=-2z+O(z^5)$。

这四个截面给 $|4O|$ 的椭圆正规四次嵌入，像由 (1) 的两条二次关系定义。
其次数十七齐次部分正是原次数六十八截面空间。
例如消去 $T^2,H^2$ 后，可取
$$
T^aH^bF^cG^d,\qquad
a,b\in\{0,1\},\quad c+d=17-a-b                              \tag{2}
$$
为基，共 $18+17+17+16=68$ 个元素。
这也可直接由两个首一二次关系逐项除法核对；
椭圆四次的完全交理想保证没有额外关系。

原 CM 作用为
$$
I_{\rm glob}:(T,F,G,H)\longmapsto(T,F,-G,iH).                \tag{3}
$$
它同时包含二处和十七处的作用，不能先把 (3) 当成纯二处 Fourier 作用。

沿用 R227 的多项式 $P_A,P_B$ 及单位 $\beta_A,\beta_B$：
$$
C_A=4\Theta\nu^2P_A(\xi),\qquad
C_B=\Theta\phi P_B(t),\qquad
\beta_B=\frac{2261}{81920}.                                \tag{4}
$$
它们准确满足
$$
A=\frac14\nabla^2 C_A+\beta_A\Theta,\qquad
B=\frac14\nabla^2 C_B+\beta_B\Theta\rho.                    \tag{5}
$$
两条 $C$ 的全局 $i$ 特征均为 $-1$，即只出现 $z^{4j+2}$。

## 2. 真正四挠平移的两个矩阵

令 $S=\Omega_0/4$，则
$$
S=(1+\sqrt2,-(2+\sqrt2)),\qquad 2S=(1,0)=R.
$$
取 $\kappa=2^{-1/4}$ 的正实嵌入。
在 degree-4 坐标上的两个 Mumford lifts 可取为
$$
\begin{array}{c|rrrr}
 &T&F&G&H\\ \hline
M&T\mapsto\kappa(F+G)&F\mapsto\kappa^3(T+H)&
G\mapsto\kappa^3(T-H)&H\mapsto-\kappa(F-G)\\
N&T\mapsto\kappa(F-G)&F\mapsto\kappa^3(T-iH)&
G\mapsto-\kappa^3(T+iH)&H\mapsto-i\kappa(F+G).
\end{array}                                                \tag{6}
$$
这里 $M$ 覆盖平移 $S$，$N=I_{\rm glob}^{-1}MI_{\rm glob}$ 覆盖平移 $iS$。

给出不依赖数值拟合的几何核对。
两个矩阵保持 (1)，且 $M(O)$ 的坐标比给出上述 $S$。
由 $x=(T+F)/G$、$y=H/(T-F)$，在原点展开 $M$ 的 $x$ 坐标：
$$
x(Mz)=1+\sqrt2-2(2+\sqrt2)z+O(z^2)
      =x(S)+2y(S)z+O(z^2).
$$
椭圆曲线自同构移回原点后属于 $\mu_4$；这里的微分为一，
所以它就是平移 $S$。第二个矩阵由 (3) 得到。
直接相乘还给
$$
M^4=N^4=1,\qquad MN=i\,NM,                                \tag{7}
$$
$$
\begin{aligned}
M^2:(T,F,G,H)&\mapsto(T,G,F,-H),\\
N^2:(T,F,G,H)&\mapsto(T,-G,-F,-H).
\end{aligned}                                             \tag{8}
$$
因此 $M^2$ 正是 R226 中固定 $\Theta$ 的实际 $\mathcal T_R$。
在 degree-17 齐次部分，(7) 的中心仍是 $i^{17}=i$。

### 2.1 与原有限高斯规范的精确对应

R115/R226 使用
$$
h_0=\frac{\sqrt{\pi/2}\,34}{\Omega_0(4-i)},\qquad
a_n=\epsilon_{n\bmod4}\,b_{n\bmod17}\,\zeta_{289}^{77n^2}.    \tag{9}
$$
让 $\epsilon,b$ 分别任取四维、十七维有限向量，给出同一个
六十八维有限 theta 空间。高斯级数的 Fourier 唯一性保证这个映射单射；
两个周期的自动因子由下面的平移公式给出，故维数也与 (2) 相同。

若
$\delta=\sqrt{\pi/2}(A+iB)$、$LA$ 为整数，则换求和下标得
$$
\mathcal B_a(u+\delta)
=e^{\,2\bar\delta u+|\delta|^2+\pi iAB}
 \mathcal B_{a^{\rm new}}(u),\qquad
a_n^{\rm new}=a_{n+LA}e^{2\pi iBn/L}.                      \tag{10}
$$
此处 $L=34$。
对 $S$，$(A,B)=(2,1/2)$，下标移 $68$；
十七处向量不变，交叉相位合成 $i^n$，而 $e^{\pi iAB}=-1$。
对 $iS$，$(A,B)=(-1/2,2)$，下标移 $-17$；
十七处交叉相位完全抵消，二处向量变成 $\epsilon_{n-1}$，
共同常数仍为 $-1$。

所以在同一高斯规范下，(6) 对应
$$
M=-M_{\rm st},\quad N=-N_{\rm st},\qquad
(M_{\rm st}v)_a=i^av_a,\quad(N_{\rm st}v)_a=v_{a-1}.         \tag{11}
$$
这些平移只作用于二处因子。共同负号不影响下面每一个非零投影项。
还会用原 $A,B,\mathcal T_RB$ 再作准确校准，避免混淆两个 dyadic 标签。

## 3. 四个准确的二处投影

置
$$
v_0=(1,0,1,0),\quad v_1=(0,1,0,-1),\quad
v_+=(1,1,-1,1),\quad v_-=(1,-1,-1,-1).
$$
这是四维二处空间的一组正交基。其公共 Haar 权重对正交投影的比值没有影响。
一般地，若 $v$ 为其中一条实向量、$n_v=\sum_a v_a^2$，则
$$
\Pi_v=
\frac1{4n_v}\sum_{k,j=0}^3
 (-1)^{k+j}
 \left(\sum_{a=0}^3v_av_{a-j}i^{-ka}\right)M^kN^j.          \tag{12}
$$
证明只需用
$E_{aa}=\frac14\sum_k i^{-ka}M_{\rm st}^k$、
$E_{ab}=E_{aa}N_{\rm st}^{a-b}$；
于是 (12) 就是矩阵 $vv^*/n_v$，张量上十七处的恒等算子。
它们两两正交、幂等，和为一，各秩为十七。

具体为
$$
\Pi_0=\frac14(1+M^2)(1+N^2),\qquad
\Pi_1=\frac14(1-M^2)(1-N^2),                               \tag{13}
$$
以及
$$
\begin{aligned}
16\Pi_-={}&4-4M^2N^2
+(-2+2i)MN+(-2-2i)MN^3\\
&+(-2-2i)M^3N+(-2+2i)M^3N^3,\\
16\Pi_+={}&4-4M^2N^2
+(2-2i)MN+(2+2i)MN^3\\
&+(2+2i)M^3N+(2-2i)M^3N^3.
\end{aligned}                                             \tag{14}
$$
准确校准为
$$
\boxed{\quad
\Pi_0A=A,\qquad \Pi_+B=B,\qquad
\Pi_-(\mathcal T_RB)=\mathcal T_RB .
\quad}                                                     \tag{15}
$$
(8) 还直接给 $\Pi_0C_A=C_A$。
$C_B$ 满足 $M^2N^2C_B=-C_B$，所以
$$
C_B=C_B^-+C_B^+,\qquad C_B^\pm=\Pi_\pm C_B,\qquad
\Pi_0C_B=\Pi_1C_B=0.                                      \tag{16}
$$
这里没有从 $\Pi_\pm B$ 推断 $\Pi_\pm C_B$；它们分别用同一实际输入计算。

## 4. 原 C_B 两块的完整有理多项式

两块都保持原点的 $z^2$ 零，并且准确为
$$
\boxed{\qquad C_B^-=\Theta\phi P_-(t),\qquad
C_B^+=\Theta\phi P_+(t),\qquad P_-+P_+=P_B.\qquad}           \tag{17}
$$
全部系数如下；省略的高次系数为零。

| $j$ | $[t^j]P_-$ | $[t^j]P_+$ |
|---:|---:|---:|
| 0 | $-2261/163840$ | $-2261/163840$ |
| 1 | $18649/6758400$ | $44249/6758400$ |
| 2 | $-24157/4224000$ | $-13119/1408000$ |
| 3 | $-692257/1478400$ | $791323/1478400$ |
| 4 | $39049/147840$ | $-255613/739200$ |
| 5 | $7016189/1848000$ | $-6935389/1848000$ |
| 6 | $-13951679/1716000$ | $97556153/12012000$ |
| 7 | $298820917/48048000$ | $-298820917/48048000$ |
| 8 | $-80295779/48048000$ | $80295779/48048000$ |

这是真正的两个非零投影。
其中 $P_-$ 的八次项非零，因此 $C_B^-$ 不是
$\mathcal T_RB=\Theta\phi b_0((1-t)/4)$ 的标量倍数；
后者多项式次数至多七。
所有新系数分母的素因子都不超过十三，所以对目标 $p>19$ 没有新坏分母。

### 4.1 可复核的整数计算证书

[固定准确脚本](../scripts/check-original-heisenberg-companion-projectors.js)
在本轮的 V8 环境中执行，全部检验为 **PASS**；
[输出](../scripts/check-original-heisenberg-companion-projectors.json)
保留所有系数与检验项。它不使用浮点数、外部软件包或目标素数样本。

计算使用 $\widetilde F=\kappa F,\widetilde G=\kappa G$。
(6) 变成系数在 $\mathbf Q(i)$ 的矩阵，分母至多二；
相应关系是
$$
T^2=\sqrt2(\widetilde F^2+\widetilde G^2),\qquad
H^2=2\sqrt2\,\widetilde F\widetilde G.
$$
每个 $M^kN^j$ 的矩阵分母至多四。统一乘 $4^{17}$ 后，
所有代入、二次关系约化和投影求和均在 $\mathbf Z[i,\sqrt2]$ 中用整数完成。

对 $C_B,\mathcal T_RB,B$ 同时乘 $\kappa$，原输入分别为
$$
\begin{aligned}
\kappa C_B&=\sum_{j=0}^6 p_j(\sqrt2)^j
              T^{16-2j}\widetilde G^{2j+1},\\
\kappa B&=\frac1{20}\sum_{j=0}^7 b_j(\sqrt2)^j
              T^{16-2j}\widetilde F\widetilde G^{2j},\\
\kappa\mathcal T_RB&=\frac1{20}\sum_{j=0}^7\widetilde b_j(\sqrt2)^j
              T^{16-2j}\widetilde G^{2j+1},
\end{aligned}
$$
其中 $p_j$ 是 R227 的原 $P_B$，
$$
(b_0,\ldots,b_7)=(0,5,-18,140,-400,496,-288,64),\qquad
(\widetilde b_0,\ldots,\widetilde b_7)=(-1,11,-14,20,0,-112,160,-64).
$$
第一列输入则是
$$
A=\sum_{j=1}^4\frac{a_j}{16^j}T^{17-4j}H^{4j},\qquad
C_A=\sum_{j=0}^3\frac{[\,\xi^j\,]P_A}{16^j}T^{15-4j}H^{4j+2}.
$$
脚本检验 (7)、(15)、(16)、(17)，并独立检查 $M^2B=\mathcal T_RB$。
因此 (17) 不依赖猜测后作小数拟合。

## 5. 十七处的准确类型与无穷权配平

在 R112 的固定二处 Fourier 规范下，
$$
I_2v_0=v_0,\qquad I_2v_+=v_+,\qquad I_2v_-=-v_-.
$$
结合 (3)、(4)、(16)，得到实际类型表：

| 原伴随截面 | 二处向量 | 十七处 $i$ 特征 | 全局 $i$ 特征 |
|---|---|---:|---:|
| $C_A$ | $v_0$ | $-1$ | $-1$ |
| $C_B^+$ | $v_+$ | $-1$ | $-1$ |
| $C_B^-$ | $v_-$ | $+1$ | $-1$ |

这里的十七处作用是同一参考 splitting、同一 Yang 极化转换下的
$a\cdot f(y)=f(ay)$；并未把实际角色的 splitting 因子再乘一次。
详见
[固定四次族的 primitive 分块](../notes/2026-11-12-seventeen-quartic-family-and-primitive-blocks.md)。

取 $\mathbf F_{17}^{\times}$ 的生成元 $3$，
按 $\chi_e(3)=\zeta_{16}^e$ 标号其乘法角色。
因为 $4=3^{12}$，$i\mapsto4$，所以
$$
\begin{array}{ll}
i=+1:&e=0,4,8,12,\\
i=-1:&e=2,6,10,14.
\end{array}                                                \tag{18}
$$
平凡角色 $e=0$ 另有 $\delta_0$、$\mathbf1_{\mathbf F_{17}^\times}$
两个维数。故 $C_B^-$ 确实落在
$$
2\ {\rm trivial\ dimensions}\ \oplus\
\lambda\ \oplus\lambda^2\ \oplus\lambda^3                  \tag{19}
$$
这个实际五维池中。
另一方面，$C_A$ 与 $C_B^+$ 落在四个 **exact-order-eight** tame 类型之和中。
它们不能被旧 E17/E289/E4913 三条四次 primitive 线吸收；
这由具体 $i$ 特征排除，不由维数大小排除。
这里尚未声称原 $C_A$ 或 $C_B^+$ 的四个八次分量逐一都非零。

无穷 Hermite 权也必须保留。
上表三行的有限 $i$ 特征都是 $-1$，正由 $m\equiv2\pmod4$
的无穷特征配平，符合其真实 Taylor 支撑。
不能删掉二处 $v_-$ 的负特征，再把第三行错认成原 $m\equiv0$ 支。

若把 (19) 的三个非平凡 tame 块分别识别为曲线，
其固定 dyadic 族是
$$
E^{B,k}:\ y^2=x^3-4\cdot17^k x,\qquad k=1,2,3.              \tag{20}
$$
因为 $17$ 在 $\mathbf Q_2$ 中为四次方，这三条曲线与 E34 有相同二处型；
十七处分别是 $\lambda^k$。在 $m\equiv2\pmod4$ 时，
R226 已证明的未分歧二次 splitting 修正固定 $v_-$。
所以这是各自同一 Hecke 角色的相邻权行，$k=2$ 才是原 E34。
这三个具体成员的准确 Mordell--Weil 秩为：

| $k$ | 方程中的 $4\cdot17^k$ | LMFDB / Cremona 标号 | 秩 | 有理挠子 |
|---:|---:|---|---:|---|
| 1 | $68$ | $18496.n1\ /\ 18496k2$ | 0 | $C_2$ |
| 2 | $1156$ | $18496.j3\ /\ 18496i2$ | 2 | $C_2^2$ |
| 3 | $19652$ | $18496.h1\ /\ 18496l2$ | 0 | $C_2$ |

本轮核读官方 [18496.n1](https://www.lmfdb.org/EllipticCurve/Q/18496/n/1)
的完整 Mordell--Weil 群，以及
[18496.j3 数据](https://www.lmfdb.org/EllipticCurve/Q/data/18496.j3)、
[18496.h1 数据](https://www.lmfdb.org/EllipticCurve/Q/data/18496.h1)
中相同方程、准确 rank bounds 与挠子；核读日期 2026-11-13。
这里仅使用准确秩和挠子，不使用页面的预测 Sha 阶。
E34 的独立完整下降另见 R118。

因此这个具体 dyadic 族仍只有 E34 满足秩门槛。
五维池的非零不能代替其原中央非零；
(17) 也没有任意选择逐权归一常数。

## 6. 真实投影产生的极点与原式的准确相消

在 $t=4q$ 变量中，R227 的二阶算子是
$$
D_{1/2}t^n=(4n+1)(2n+1)t^n-4(n+1)(2n+1)t^{n+1}.           \tag{21}
$$
从 (17) 定义两个原点质量为零的实际局部函数
$$
B_\pm=\Theta\rho\bigl(D_{1/2}P_\pm+\beta_B/2\bigr)
     =\frac14\nabla^2 C_B^\pm+\frac{\beta_B}{2}\Theta\rho.
                                                                    \tag{22}
$$
则 $B=B_-+B_+$ 准确成立。

每个 $C_B^\pm$ 仍是整的 degree-68 截面；
但它们有非零八次项，已经离开 R227 的十六维 Lamé 块。
若 $p_j=[t^j]P_\pm$，则 (21) 给
$$
[t^9]D_{1/2}P_\pm=-612p_8,\qquad
[t^8]D_{1/2}P_\pm=561p_8-480p_7.                            \tag{23}
$$
因此 (22) 各自在 $T=0$ 有二阶极点：
$\Theta\rho t^9=T^{-2}FG^{18}$。
原 $P_B$ 的 $t^7,t^8$ 系数均为零，故 (23) 的两个最高项在
$B_-+B_+$ 中准确相消，恢复原 $B$ 的完整整截面。
投影不是免费保持该有限 Lamé 块的算子。

对于目标 $p>19$，这些有理因子在原点的整形式参数中展开为整级数：
分母仅支撑在固定的 prime-to-$p$ 挠点上。
改用原微分对数坐标 $z$ 后，至 $2d$ 的整性仍按 R210 的实际第一带处理，
全级数则使用 R54 的指定半径有界性；不声称全部 $z$ 系数都整。
所以 (22) 可作下节的完整局部 Mellin 比较；
这里不把它们分别认成新的全局 theta 平方行。

## 7. 全部 W 补偿及质量

沿用 R227，令 $d=p+1$、$v=z^d$、$c$ 为原共同 gauge，
$$
W=z\Theta'/\Theta,\quad W_0=W-dcv,\quad E=z\partial_z,\quad
g_\pm=z^{-2}C_B^\pm.
$$
定义同一完整中央泛函的三个 Tate 函数
$$
\begin{aligned}
\mathcal F_\pm(u)&=J(g_\pm;u),\\
\mathcal G_\pm(u)&=J(W_0g_\pm;u),\\
\mathcal H_\pm(u)&=J((W_0^2+EW_0-W_0)g_\pm;u).
\end{aligned}                                             \tag{24}
$$
它们的收敛没有额外假设。
确实 $g_\pm/\Theta$ 是固定代数函数的原点有界幂级数。
写 $\widehat\Theta=e^{-cv}\Theta$，则
$$
e^{-cv}W_0g_\pm=z\widehat\Theta'\frac{g_\pm}{\Theta},\qquad
e^{-cv}(W_0^2+EW_0-W_0)g_\pm
=z^2\widehat\Theta''\frac{g_\pm}{\Theta}.                    \tag{25}
$$
R54/R227 的同一半径 $p^{-1/(2p)}$ 因而给完整 Tate 收敛。
这不是用 $\exp(\text{整输入})$ 宣称单位圆盘收敛。

记 R227 已证的算子
$$
\begin{aligned}
\mathcal P_d(F,G,H;u)={}&(du+1)(du+2)F(u)
+du(d-3-2du)F(u-1)+d^2u(u-1)F(u-2)\\
&-2(du+1)G(u)+2duG(u-1)+H(u).
\end{aligned}
$$
则本篇分解给真正完整等式
$$
\boxed{\quad
J(B_\pm;u)=\frac{\beta_B}{2}J(\Theta\rho;u)
+\frac14\mathcal P_d(\mathcal F_\pm,\mathcal G_\pm,\mathcal H_\pm;u),
\qquad J(B)=J(B_-)+J(B_+).
\quad}                                                     \tag{26}
$$
原第一列仍是 R227 的同一完整式，且其伴随 $C_A$ 的八次类型已由上表认定。
没有把 (24) 的连接补偿当成零。

两块的质量也分别准确相消：
$$
g_-(0)=g_+(0)=2P_\pm(0)=-\beta_B,\qquad
\mathcal G_\pm(0)=\mathcal H_\pm(0)=0.
$$
对常函数 $F_0$，$\mathcal P_d(F_0,0,0)=2F_0$ 恒成立。
所以 (26) 的常数贡献各为
$\beta_B/2-\beta_B/2=0$。
原裸单位没有成为新增的中央常数。

## 8. 首行模 p²、聚合后除 p，以及真实运输缺陷

对任意 $n$，(22) 的完整普通系数为
$$
[z^n]B_\pm=
\frac{\beta_B}{2}[z^n](\Theta\rho)
+\frac14\left\{
(n+1)(n+2)[z^n]g_\pm
-2(n+1)[z^n]Wg_\pm
+[z^n](W^2+z^2V')g_\pm
\right\}.                                                 \tag{27}
$$
特别可以在 $n=d,2d$ 使用；先形成 (27) 的完整组合。
原点质量为零及 R210 的原 gauge 整性给
$R_{1,\pm}$、$\widehat R_{2,\pm}$ 整，且准确有
$$
R_{1,B}=R_{1,-}+R_{1,+}\pmod{p^2},\qquad
\widehat R_{2,B}=\widehat R_{2,-}+\widehat R_{2,+}\pmod p.
                                                                    \tag{28}
$$
即使原首行失败，单块首行也未必在 $pO$ 中。
必须写
$$
K_B=\overline{\widehat R_{2,-}+\widehat R_{2,+}}
-\alpha\,\overline{\frac{R_{1,-}+R_{1,+}}p},
\qquad \alpha=pc\bmod p,                                  \tag{29}
$$
而不能先把两个未证可整除的块分别除以 $p$。
这保留了同一原 first-row 下一位。

最后，有限投影与 $\nabla^2$ 的不交换项也可以准确写出。
对 (12) 中任一实际平移 $U_s$，置
$$
a_s=\partial_z\log\frac{U_s\Theta}{\Theta}
   =17\,\partial_z\log\frac{U_sT}{T}.
$$
在右式中 $U_sT$ 指 degree-4 lift；degree-68 lift 是其次数十七作用。
由实际自动因子直接微分，
$$
\nabla U_s=U_s\nabla+a_sU_s,\qquad
U_s\nabla^2=
\nabla^2U_s-2a_s\nabla U_s+(a_s^2-a_s')U_s.                 \tag{30}
$$
因此每个 $\Pi_v$ 的完整交换差是 (30) 的同一有限带权和。
(24)–(27) 已保留相应普通导数补偿。
不能由某个被平移截面的中央投影为零，推出乘子或协变导数后的中央投影仍为零。

本篇把原两个伴随截面的实际 finite types、投影后的极点、
质量和完整 Mellin 校正放在同一公式中。
接下来若使用 (19) 中的固定曲线，仍需识别其准确分量系数并控制
(24) 的实际补偿；若使用八次类型，则需新的真实算术输入。
本篇不声称这些剩余项由原双零自动消失。

## 来源与复核范围

- 原截面及高斯规范：R115、R226；原二阶恒等式、共同 gauge 与完整收敛：R227。
- 十七处的参考作用、primitive 角色与五维分解：
  [固定四次族](../notes/2026-11-12-seventeen-quartic-family-and-primitive-blocks.md)、
  [有理 CM 缩放类型](../notes/2026-11-12-theta-rational-cm-scaling-type.md)。
- 外部 theta 接口仅使用 T. Yang，*Theta liftings and Hecke L-functions*，
  J. reine angew. Math. **485** (1997)，25–53，Corollary 2.10、
  式 (2.28) 及完整局部—全局平方公式：
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
- 本篇新增的有限矩阵、多项式和极点计算均为上述实际输入上的准确代数证明。
  证书已在 V8 执行通过；没有新增素数扫描、未上传 PDF，也未使用数值拟合认定角色。
