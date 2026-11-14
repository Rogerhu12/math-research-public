# 次数十七 theta 截面的准确多项式：Gaussian 区间与全局分母证书

日期：2026-11-12。状态：已证明。本文将四参数的数值候选认定为实际固定截面，
使用有理性、有效全局分母界、严密复区间以及有理数之间的离散间距。
另有独立的 $3^{400}$ 完整轨道迹证书。

## 1. 实际截面与结论

采用[次数十七下降](2026-11-12-theta-seventeen-isogeny-descent.md)
及[四参数有理性](2026-11-12-theta-four-parameter-rationality.md)。
固定首项为 $z^4$ 的实际截面写作

$$
 A(z)=\vartheta(z)\sigma_E(z)^{16}
       \bigl(x(z)^6+u_2x(z)^4+u_3x(z)^2+u_4\bigr)
       =\sum_{4\mid m}b_mz^m,\qquad b_4=1,
 \tag{1}
$$

其中 $u_j\in\mathbb Q$、$\vartheta^2=x\sigma_E^2$、$\vartheta(0)=1$。
有理性是此前十维满秩证书的结论，本篇不再次假定任何逐权平方根符号。

**定理。** 实际参数及截面准确为

$$
 \boxed{
 (u_2,u_3,u_4)=\left(\frac{51}{5},-\frac{289}{5},\frac{4913}{5}\right),
 }
 \tag{2}
$$

$$
 \boxed{
 A(z)=\frac15\vartheta(z)\sigma_E(z)^{16}
       (x(z)^2+17)(5x(z)^4-34x(z)^2+289).
 }
 \tag{3}
$$

等价的固定 torsion 除子形式为

$$
 \boxed{
 A(z)=\frac15\vartheta(z)\vartheta(2z)\sigma_E(z)^2
                   \sigma_E((2+i)z)\sigma_E((2-i)z).
 }
 \tag{4}
$$

实际低权系数为

$$
 b_8=\frac{1649}{60},\qquad
 b_{12}=\frac{9313603}{50400},\qquad
 b_{16}=\frac{2421363742117}{1297296000}.
 \tag{5}
$$

[独立的完整轨道迹证书](2026-11-12-degree17-central-traces-and-square-constant.md)
给 $e_4=25/(2^9 17^{10})$，所以中央平方公式的准确常数为

$$
 \kappa_{\mathbb Q}=e_4(17\,Nf)^4=57800,\qquad 17Nf=8\cdot17^3.
$$

从而对全部 $4\mid m$，

$$
 \boxed{
 e_m=57800(8\cdot17^3)^{-m}b_m^2.
 }
 \tag{6}
$$

对于目标普通 $p$，(1) 的实际 principal Mellin 因子 $J_p$ 满足

$$
 F_p^{\Theta,-}(T)=57800f\Omega_p
       (1+T)^{\log_p\langle136\rangle/\log_p(1+p)}J_p(T)^2.
 \tag{7}
$$

这明确了输入的固定函数和全部常数，尚未证明无穷多个 $p$ 的
$J_p'(0)\ne0$。不将固定截面的显式性当成跨素数非消失。

## 2. 实际有限 theta 权重的方向

### 2.1 证明 $\lambda(3)=-i$

固定 $17$ 处第一分量 $i\equiv4\pmod{17}$，并取
$\varpi=4-i$。设 $\lambda$ 为此分裂分量上的四次单位特征。
对 $E_0:y^2=x^3-x$ 和 $E_{17}$，直接数 $\mathbb F_5$ 点给

$$
 a_5(E_0)=-2,\qquad a_5(E_{17})=-4.
$$

在 $\mathfrak q=(2+i)$ 处，同一 CM 型的 Hecke 值为

$$
 \psi_0(\mathfrak q)=-1+2i,\qquad
 \psi_{17}(\mathfrak q)=-2-i,\qquad
 \psi_{17}(\mathfrak q)/\psi_0(\mathfrak q)=i.
$$

第一式为 primary generator，第二式同时由迹与所生成素理想确定。
两曲线在 $2$ 处的局部分量相同，见 dyadic 向量证明；
无穷分量也相同。把比角色应用于主 idèle $2+i$，
$5$ 处的 $i$ 必由 $17$ 处的 $-i$ 抵消。

$2+i$ 在 $17$ 两分量的剩余值为 $(6,15)$，
因此该比角色在 $17$ 处的值为

$$
 \lambda(6)\lambda^{-1}(15)
 =\lambda(6/15)=\lambda(14)=\lambda(3)^9=\lambda(3).
$$

这证明准确方向 $\lambda(3)=-i$，并非从拟合符号选择该角色。

### 2.2 从既有局部 Fourier 公式得到一份固定级数

$i$ 的上述 Hensel lift 模 $17^2=289$ 为 $38$。
实结构证明的局部 Fourier 核使用 $c=i^3=-i$，
所以 $c/2\equiv-19\pmod{289}$。
全局标准加法特征在 $17$ 处为负指数方向。
把所有不依赖 $n$ 的非零常数合并后，
有限权重准确为

$$
 a_n=
 \begin{cases}
 \lambda(n)\exp(2\pi_{\mathbb C}i\,19n^2/289),&17\nmid n,\\
 0,&17\mid n.
 \end{cases}
 \tag{8}
$$

这里省略的共同常数只改变整体 $C$，会在下面的系数比中消失。
$\lambda(-1)=1$，所以 $a_{-n}=a_n$。

同一个 Hermite 生成函数为

$$
 B(t)=e^{-t^2}\sum_{n\in\mathbb Z}a_n
       \exp\!\left(-\frac{\pi_{\mathbb C}n^2}{289}
          +2\sqrt{2\pi_{\mathbb C}}\frac n{17}t\right)
       =\sum_m B_mt^m.
 \tag{9}
$$

记

$$
 \Omega_E=
 \frac{\Gamma(1/4)^2}{2\sqrt{2\pi_{\mathbb C}}\,17^{1/4}},
 \qquad c_{17}=\sqrt{\pi_{\mathbb C}/2}\,17/\Omega_E.
 \tag{10}
$$

周期公式可由
$\Omega_1=2\int_0^1(1-t^4)^{-1/2}dt$
及 beta 积分直接得到；与 NIST DLMF 19.20.2 相同。
次数十七下降给 $A(z)\propto B(c_{17}z/(4-i))$。
因此实际的首项一归一化准确为

$$
 \boxed{
 b_m=\frac{B_m}{B_4}
          \left(\frac{c_{17}}{4-i}\right)^{m-4}.
 }
 \tag{11}
$$

这同时保留了同一周期、同一有限角色、同一复方向与共同标量；
不在不同权重中重新挑选平方根。

## 3. 中央系数的有效全局分母

写

$$
 \frac z{\sigma_E(z)}=\sum_{j\ge0}q_jz^j.
$$

只有 $4\mid j$ 的项可能非零，且 $q_j\in\mathbb Q$。
沿用中央 theta 对角公式，置

$$
 D=-X\partial_U+2Y\partial_X+(3X^2-17)\partial_Y,\qquad
 C_0=1,\quad C_{n+1}=(D+U)C_n.
$$

则

$$
 d_m=\sum_{j=0}^{m}
  \frac{q_j}{m!(m+1-j)!}
    \sum_{S\in\mathcal S}(D^mC_{m+1-j})(U_S,x(S),y(S)).
 \tag{12}
$$

$n=0$ 项的 $D^m$ 为零，所以求和可写为 $j\le m$。
每个 $C_n$、$D^mC_n$ 为整数系数多项式。
给 $U,X,Y$ 权 $1,2,3$，$D$ 至多增加一权，
故 (12) 中各多项式的权至多 $2m+1$。

[最低中央迹的全局证明](2026-11-12-central-theta-d1-exact-global-trace.md)
§1 已在所有 primitive 点及其所有共轭处证明：

- 好素位 $p\ne2,17$：$U_S,x(S),y(S)$ 全部整。
- $2$ 上方：$v_2(U_S)\ge-3/2$，$v_2(x(S))\ge0$，
  $v_2(y(S))\ge1/2$。
- $17$ 上方：$v_{17}(U_S)\ge-3/4$，
  $v_{17}(x(S))\ge1/2$，$v_{17}(y(S))\ge3/4$。

这些界使用显式好模型和 division polynomial，
不假设坏约化处的 torsion 坐标天然整。

定义

$$
 C_m^{\rm den}=
  \mathop{\rm lcm}_{0\le j\le m}
     \operatorname{den}\!\left(\frac{q_j}{m!(m+1-j)!}\right).
$$

清掉 (12) 的系数分母后，两个坏素位的赋值分别至少为
$-\tfrac32(2m+1)$ 和 $-\tfrac34(2m+1)$。
又 $v_2(f)=3/2$、$v_{17}(f)=1$，
而 $e_m=d_m/f^{2m+1}\in\mathbb Q$。因此

$$
 \boxed{
 D_m e_m\in\mathbb Z,\qquad
 D_m=C_m^{\rm den}\,
    2^{3(2m+1)}17^{\lceil7(2m+1)/4\rceil}.
 }
 \tag{13}
$$

本界特意取宽，不需要计算整个高权迹多项式。
脚本直接由 $x''=6x^2-34$ 及 $\sigma'/\sigma=\zeta$ 递推 $q_j$，
得到：

| $m$ | $C_m^{\rm den}$ | 已严格检查的简便上界 |
|---:|---:|---:|
| 4 | $2880$ | $D_4<10^{32}$ |
| 8 | $73156608000$ | $D_8<10^{64}$ |
| 12 | $14913764632166400000$ | $D_{12}<10^{96}$ |
| 16 | $37209866619278579466240000000$ | $D_{16}<10^{130}$ |

## 4. 一个充分的复上界，以及有理间距

同一最低中央迹证明 §2 的 lattice 估计给每个 $S\in\mathcal S$：

$$
 |U_S|<740,\qquad |x(S)|<50000,\qquad |y(S)|<3600000.
$$

取 $M=10^4$，则分别小于 $M,M^2,M^3$。
对权至多 $w$ 的整数多项式，
导子 $D$ 的系数一范数满足
$\|DP\|_1\le7w\|P\|_1$：
单项式 $U^aX^bY^c$ 的导数系数绝对值之和为
$a+2b+20c\le7(a+2b+3c)$。
从而

$$
 \|C_n\|_1\le8^n n!,\quad
 \|D^4C_5\|_1\le7^4\cdot5\cdot8!\cdot8^5,\quad
 \|D^4C_1\|_1\le7^4\cdot4!\cdot8.
$$

因 $q_0=1$、$q_4=17/60$，(12) 在 $m=4$ 的两个非零项给

$$
 |d_4|<
 256\left(
 \frac{7^4\cdot5\cdot8!\cdot8^5}{4!\,5!}M^9
 +\frac{17}{60}\frac{7^4\cdot4!\cdot8}{4!}M^5
 \right)<10^{50}.
$$

$|f|>1$，所以

$$
                         |e_4|<10^{50}.                     \tag{14}
$$

把 $e_4=a/b$ 写成既约有理数，则 (13)–(14) 给
$|a|<D_4\,10^{50}$。
由已证明的中央平方公式，

$$
 b_m^2=\frac{e_m}{e_4}(17Nf)^{m-4}\qquad(m=4,8,12,16).
 \tag{15}
$$

右边的既约分母不超过 $D_mD_4\,10^{50}$。
此前的有理下降已经证明 $b_m\in\mathbb Q$；
因此 $b_m$ 的既约分母不超过

$$
 H_m=\left\lfloor\sqrt{D_mD_4\,10^{50}}\right\rfloor.
 \tag{16}
$$

特别地 $H_8<10^{73}$、$H_{12}<10^{89}$、$H_{16}<10^{106}$。
(5) 中各候选分母小于 $10^{10}$。
若实际 $b_m$ 与对应候选不同，其差的绝对值必大于 $10^{-116}$。
所以严密区间误差 $10^{-250}$ 已足以唯一认定它们，
而不只是说明很多小数位吻合。

## 5. 有限 Gaussian 求和及完整尾界

式 (9) 的第 $m$ 系数中，令
$X_n=\sqrt{2\pi_{\mathbb C}}\,n/17$。其 Hermite 多项式因子是

$$
 h_m(X_n)=
   \sum_{j=0}^{\lfloor m/2\rfloor}
     \frac{(-1)^j(2X_n)^{m-2j}}{j!(m-2j)!}.
 \tag{17}
$$

取 $|n|\le350$ 作有限求和。
对 $|n|\ge351$、$m\le16$，有 $1<2|X_n|<|n|$；
故

$$
 |h_m(X_n)|\le e(2|X_n|)^m<3|n|^{16}.
$$

双边尾和于是至多

$$
 6\sum_{n\ge351}n^{16}e^{-3n^2/289}.
$$

相邻项比值不超过

$$
 \exp\!\left(\frac{16}{n}-\frac{3(2n+1)}{289}\right)
 \le \exp\!\left(\frac{16}{351}-\frac{3\cdot703}{289}\right)
 <e^{-7}<\frac12.
$$

因此尾界可取

$$
 12\cdot351^{16}e^{-3\cdot351^2/289}
 <12\cdot351^{16}(3/8)^{1278}<10^{-500}.
 \tag{18}
$$

最后一步由脚本用纯整数准确检查

$$
 12\cdot351^{16}\cdot3^{1278}\cdot10^{500}<8^{1278};
$$

中间使用 $3\cdot351^2/289>1278$ 与 $e>8/3$。
本界同时适用于四个所选系数，包含两个方向的全部遗漏项。

## 6. 严密区间输出与参数认定

证书脚本：

[check-theta-explicit-section.py](../scripts/check-theta-explicit-section.py)

使用 python-flint 0.9.0 的 Arb/Acb，工作精度为 $1024$ 二进制位。
每个有限项用球算术计算，随后在实部和虚部各加入半径 $10^{-500}$，
所以得到整个无限和的包含区间。
它先确认 $B_4$ 的区间不含零，再按 (11) 作区间除法与缩放。

所有 Gamma、$\pi$、平方根、指数及有理输入均通过包含区间运算；
没有把普通浮点近似当作准确中点。
脚本准确检查：

$$
 \left|b_8-\frac{1649}{60}\right|<10^{-250},\quad
 \left|b_{12}-\frac{9313603}{50400}\right|<10^{-250},\quad
 \left|b_{16}-\frac{2421363742117}{1297296000}\right|<10^{-250}.
 \tag{19}
$$

各区间真实部严格为正，虚部包含零。
事实上本次三个误差上界分别小于
$1.12\cdot10^{-303}$、$7.00\cdot10^{-302}$、
$3.37\cdot10^{-300}$；证明只使用较宽的 (19)。
第 4 节的有理间距立即把 (19) 提升为准确等式 (5)。

最后在有理数上对
$\vartheta\sigma^{16}(x^6,x^4,x^2,1)$ 的前四个系数作三角求解，
准确得到 (2)。
因此固定的整截面、所有后续 Taylor 系数及各素数处实际 Mellin
测度都被确定；并非只认出了四个数值样例。

## 7. 独立的完整轨道复核，以及固定 torsion 除子

[中央迹证书](2026-11-12-degree17-central-traces-and-square-constant.md)
另由 $3^{400}$ 下全部 $256$ 点及有效全局界唯一恢复
$e_4,e_8,e_{12},e_{16}$。
它给 (15) 的三个准确平方；本文的严格正区间又独立确定相容正号。
这条路线不依赖第 4 节较宽的有理重构界。

对 (3)，已证明的 CM division 规范给

$$
 \frac{\sigma_E((2+i)z)}{\sigma_E(z)^5}
       =(2+i)x(z)^2-17i,
$$

及其共轭式。相乘得 $5x^4-34x^2+289$。
另一方面 $\vartheta(2z)$ 与 $(x^2+17)\sigma_E^4$
有相同的除子和准周期，并在原点都取一：
其四个零点是 $[2]^{-1}(0,0)$。
因此 (4) 是准确恒等式。

(4) 的零除子由以下固定 torsion 点组成：
原点四阶，$T_0$ 一阶，$[2]^{-1}T_0$ 四个点各一阶，
以及 $E[2+i]\setminus\{O\}$、$E[2-i]\setminus\{O\}$
各四个点一阶，总次数十七。
这识别的是已经认证的实际截面，不是先猜其除子再宣称匹配。

### 来源与复查范围

- 有限向量、局部 Fourier 规范与共同 theta 生成函数：
  R46，实结构笔记，以及 dyadic 向量笔记；
  其外部输入是 Yang 1997 与 Yang 1999 已核原文。
- 全局坏位估值及复 lattice 界：
  [最低中央迹证明](2026-11-12-central-theta-d1-exact-global-trace.md)
  §§1–2。本文已写出推广到全部所需权的清分母步骤。
- NIST DLMF（2010 年首次发布），
  [19.20.2](https://dlmf.nist.gov/19.20.E2)，
  给与 (10) 相同的 lemniscatic beta 积分常数。
- F. Johansson，*Arb: efficient arbitrary-precision midpoint-radius interval arithmetic*，
  IEEE Transactions on Computers **66** (2017), 1281–1292：
  [作者原文](https://fredrikj.net/math/arbpaper.pdf)。
  Arb 只负责有限运算的包含区间；本文单独证明了无限 Gaussian 尾界。
- 两份计算脚本均保留准确的固定输入。
  没有使用未证的 BSD、$p$-进高度非退化或跨素数有限性假设。
