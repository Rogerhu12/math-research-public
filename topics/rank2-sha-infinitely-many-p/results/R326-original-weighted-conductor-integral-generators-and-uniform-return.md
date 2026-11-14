# R326：原加权导子的整数代表与全次数统一返回

日期：2026-11-13。**状态：R325 的47次关系与五个首40次导子已在原单项式中明确给出。1154个精确恒等式、一个整无基点 pencil 和全次数递推证明：导子乘整个归一化格仍整地返回原幂格，所有代表分母只含2、3。原点行移为13至17，仍须在实际有限目标中付出。**

## 1. 原尺度与全部整数角函数

本篇为消去无关常数，采用
$$A=7bS(z),\quad B=7bS(\delta z),\quad C=7bS(2z),
\qquad\deg(A,B,C)=(1,3,4),\quad b=17.$$
令 $R=\mathbb Z[1/(42b)]$，$\mathcal T_R=R[A,B,C]$。
与原 $S$ 幂格相比，各单项式只差固定 $R$ 单位；没有改变 charge。

取 $t=-b/x^3$，并定义
$$
\begin{aligned}
q_7&=16t^2+4t+7,&g_2&=8t^2+20t-1,\\
f_3&=64t^3-48t^2+228t-1,\\
f_{4,\delta}&=1792t^4-3136t^3+2112t^2-40t+1,\\
f_4&=512t^4-2048t^3+1344t^2-536t-1,\\
f_6&=4096t^6-33792t^5+204288t^4-47936t^3+11040t^2+84t+1.
\end{aligned}
$$
R314/R319 的完整同源式约分后准确为
$$
\boxed{f=\frac B{A^3}=
\frac{27(4t-1)^2f_3f_{4,\delta}}
 {t^2(t-1)^2(8t+1)q_7^2},\qquad
h=\frac C{A^4}=
\frac{-64g_2^2f_4f_6}
 {t^3(t-1)(8t+1)^2q_7^3}.}                     \tag{1}
$$
分别记其整数分子、分母为 $n_f,d_f,n_h,d_h$。

对 $n\ge0$，置
$$
a_n=\lfloor3n/4\rfloor,\quad c_n=\lfloor2n/3\rfloor,
\quad b_n=\lfloor n/2\rfloor,
$$
$$
T_n=t^{a_n}(t-1)^{c_n}(8t+1)^{b_n}q_7^{a_n},
\qquad d_n=3a_n+c_n+2b_n.                         \tag{2}
$$
R325 归一化的明确整数格为
$$\mathcal N_{R,n}=\frac{A^n}{T_n}R[t]_{\le d_n}.                \tag{3}$$
每个原单项式 $A^iB^jC^k$（$i+3j+4k=n$）在 (3) 中的分子是
$$
\boxed{M_{n,j,k}=n_f^jn_h^k
t^{a_n-2j-3k}(t-1)^{c_n-2j-k}
(8t+1)^{b_n-j-2k}q_7^{a_n-2j-3k}.}               \tag{4}
$$
所有指数均非负。这是本文精确线性代数使用的真实整矩阵，未以环境自由列
代替原幂格。

## 2. 47次关系和五个40次乘子的确切定义

变量的加权次数为 $(1,3,4)$。把所有 $i+3j+4k=47$ 按先 $k$ 后 $j$ 升序排列，
有108个单项式。用 (4) 的整数系数列组成183行的矩阵。
数据文件记录其唯一 primitive 核向量，符号规定为首个非零系数正。
记对应多项式为 $F(X,Y,Z)$。其确切代入为零，
$$F(A,B,C)=0,$$
共有96个非零项，最大系数为76位整数。R325 的47次唯一关系定理保证它
生成整个特征零关系理想；本篇数据给出了每一项的整数值。

令 $P(y,z)=F(1,y,z)$，$Q(t)=t(t-1)(8t+1)q_7(t)$，并置
$$
N_{\rm raw}(t)=T_{40}(t)\frac{P_z(f(t),h(t))}{f'(t)Q(t)}.
                                                               \tag{5}
$$
这是一个整数多项式，其内容为 $541653102231552$。
定义
$$\boxed{N(t)=N_{\rm raw}(t)/541653102231552.}                    \tag{6}$$
精确证书证明
$$
\boxed{N\in\mathbb Z[t],\quad\gcd\text{(全部系数)}=1,
\quad\deg N=147,\quad\operatorname{ord}_{t=0}N=3,}
$$
$$\boxed{[t^3]N=87778193643=3^4\cdot7^3\cdot3159421.}           \tag{7}$$
由 R325 的残数形式，五个首导子可以取为
$$\boxed{G_j=\frac{A^{40}N(t)t^j}{T_{40}(t)},
\qquad0\le j\le4.}                                             \tag{8}$$
它们的确切原40次单项式表示也全部记录在证书中，公共分母为
$$\boxed{2^{28}3^{22}.}                                        \tag{9}$$
这五个向量分别有71、71、71、71、73个非零原单项式系数。
因40次低于唯一关系次数47，它们的原表示唯一。

式 (5) 不是需要数值评价的定义：附带 JSON 保存 $F$、$N_{\rm raw}$、
约分后的 $P_z(f,h)/f'$ 的每个系数，核验只用整数多项式乘法和整除。

## 3. 同一十二次整 pencil

取原代数中的两个截面
$$L=A^{12},\qquad M=B^4+C^3.$$
在 $\mathcal O(12D)$ 的分子坐标中，它们为
$$T_{12},\qquad M_{12,4,0}+M_{12,0,3}=:Q_{12}.$$
完全整数计算给出
$$
\boxed{\operatorname{Res}_t(T_{12},Q_{12})
=-2^{2538}3^{2275},\qquad
\deg Q_{12}=47,\quad[t^{47}]Q_{12}=-2^{99}.}                    \tag{10}
$$
所以这两截面在 $\mathbb P^1_R$ 没有共同零点：有限图由 resultant 给出，
无穷点由第二个首项给出。这里没有按次数选择新的 pencil 或新的坏素数。

由无基点的两截面 Koszul 正合列，任意 $n\ge24$ 有
$$
0\longrightarrow\mathcal O(\lfloor(n-24)D\rfloor)
\longrightarrow\mathcal O(\lfloor(n-12)D\rfloor)^{\oplus2}
\xrightarrow{(L,M)}\mathcal O(\lfloor nD\rfloor)
\longrightarrow0.                                             \tag{11}
$$
这是因为 $12D$ 为整除子，故取整与减去 $12D$ 交换。
左端线丛次数非负，其 $H^1$ 在 $\mathbb P^1_R$ 为零，因而
$$\boxed{\mathcal N_{R,n}
=L\mathcal N_{R,n-12}+M\mathcal N_{R,n-12}\quad(n\ge24).}        \tag{12}$$
于是全部归一化格由0至23次部分在 $R[L,M]$ 上生成。这是全次数递推，
不是以有限样例推测一般结论。

## 4. 1154个原恒等式支付所有初值

对 $0\le m\le23$，$G_0,\ldots,G_4$ 乘 (3) 的整基后，所有不同分子为
$$
N(t)\frac{T_{40+m}}{T_{40}T_m}t^\ell,
\qquad0\le\ell\le d_m+4.                                      \tag{13}
$$
其中分母比为整数多项式，因每处的 floor 满足超加性。
证书为每一项给出原单项式中的完整恒等式
$$
N(t)\frac{T_{40+m}}{T_{40}T_m}t^\ell
=\sum_{i+3j+4k=40+m}q_{m,\ell,i,j,k}M_{40+m,j,k}(t),            \tag{14}
$$
且所有 $q$ 均在 $\mathbb Z[1/6]$。24个 $m$ 的恒等式总数准确为1154。
其公共分母为
$$\boxed{2^{215}3^{170}.}                                      \tag{15}$$
这不是任意选择的可行有理解：证书固定 (4) 的列次序，采用有理行约化后
自由变量置零的确切代表，并保存每个系数。核验时直接把 (14) 两边的全部
整数多项式系数相减，结果为零；不依赖浮点、不扫描素数。

**定理。** 对每个 $m\ge0$ 和 $0\le j\le4$，都有
$$\boxed{G_j\mathcal N_{R,m}\subset\mathcal T_{R,40+m}.}         \tag{16}$$

**证明。** $m=0,\ldots,23$ 由 (14)–(15) 给出。
对 $m\ge24$，用 (12) 写 $v=L v_1+M v_2$，其中
$v_1,v_2\in\mathcal N_{R,m-12}$。归纳假设给
$G_jv_i\in\mathcal T_{R,28+m}$，再乘原次数12的 $L,M$ 即得 (16)。
所有运算都在同一个 $R$ 上，因此没有随 $m$ 新增的坏素数。$\square$

因此 R325 的首导子已经得到一份完整的原整数实现。
R322 的逐剩余域饱和论证另可从
$\mathcal N_R\cap\mathcal T_{\mathbb Q}=\mathcal T_R$ 导出同一包含；
本篇 (14) 给出可直接使用的原系数，且 (10)–(16) 独立支付全次数范围。

## 5. 原点成本和有限目标接口

由于 $A=\rho,t(t-1)q_7(t)$、$\rho(0)=1$，且 $t=-bz^6+\cdots$，
式 (2)、(7)、(8) 给
$$\boxed{\operatorname{ord}_{z=0}G_j=78+6j,
\qquad \operatorname{ord}_{w=0}G_j=13+j\quad(w=z^6).}           \tag{17}$$
$G_0$ 的首系数准确为
$$\boxed{[z^{78}]G_0=-3^4\cdot7^{13}\cdot3159421\cdot b^{13}.} \tag{18}$$
所以在 $p\nmid42b\cdot3159421$ 时，$G_0$ 在原形式盘是 $w^{13}$ 乘一个整单位。
该乘子仍有真实 charge40，必须与原 Gaussian 及除幂目标一起运输。
它不能被当成原点单位，也不能删去这13行移和有限目标的边界 $p$ 成本。

式 (16) 使整个归一化角带可经一个固定原导子进入原幂格；它支付的是
**来源整格的包含**。要由此得到 O8 所需的深 Smith 净收益，仍须将这条
实际来源带与原完整中央零所给的同一个有限观察比较。缩放 Stokes 行在
同一精度下仍满足 R314 的重复性，不能把 (16) 另计为新增中央条件。

## 6. 完整证书

- `scripts/check-jzero-weighted-conductor-integral.py`：精确核验 (1)、47次原关系、残数乘子、无基点 pencil 及全部1154恒等式。
- `scripts/check-jzero-weighted-conductor-integral.json`：全部47次关系和40次首导子系数、规范及数据清单。
- `scripts/check-jzero-weighted-conductor-integral-part1.json.gz`、`part2.json.gz`、`part3.json.gz`：依次保存 $m=0\ldots7$、$8\ldots15$、$16\ldots23$ 的每一个完整原代表。

使用 `python-flint` 的整数/有理运算。实际执行已通过，最后输出为1154个
确切恒等式通过，全部分母支撑于2、3。数据按原系数保全并压缩，单文件小于5MB。

依赖：[R314](R314-jzero-actual-doubling-return-and-full-q2-transport.md)、
[R319](R319-jzero-ramified-three-minimal-unit-and-mixed-scaled-return.md)、
[R325](R325-three-true-zero-weighted-normalization-and-conductor.md)。
主目标的跨素数中央非零仍待证明。
