# E34 的次数六十八实际截面：完整有理平方与区间证书

日期：2026-11-12。**状态：以下实际截面恒等式已证明。**
本篇不证明两条秩二曲线的中央导数对无穷多个素数不同时为零。

## 1. 原始输入、尺度与结论

沿用 [R112 的实际 dyadic 与十七处向量](2026-11-12-e34-dyadic-theta-and-two-rank-two-rows.md)：
\[
 E_{34}:y^2=x^3-1156x,\quad E_0:y^2=x^3-x,\quad
 \lambda(3)=-i,\quad \alpha=4-i,
\]
\[
 a_n^+=\varepsilon_n\lambda(n)^2\zeta_{289}^{77n^2}\ (17\nmid n),
 \qquad a_n^+=0\ (17\mid n),\qquad
 (\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3)=(1,1,-1,1).
\]
所有整数下标的符号按模四重复。固定同一个 Hermite 生成函数
\[
 B(t)=e^{-t^2}\sum_{n\in\mathbb Z}a_n^+
       \exp\!\left(-\pi_{\mathbb C}(n/34)^2+
                     2\sqrt{2\pi_{\mathbb C}}(n/34)t\right)
       =\sum_m B_mt^m.                                      \tag{1}
\]
令
\[
 \Omega_0=\frac{\Gamma(1/4)^2}{2\sqrt{2\pi_{\mathbb C}}},
 \qquad
 h_0=\frac{\sqrt{\pi_{\mathbb C}/2}\,34}{\Omega_0\alpha},
 \qquad
 b_m=\frac{B_m}{B_4}h_0^{m-4}.                               \tag{2}
\]
下文的严格区间证明 $B_4\ne0$，所以 (2) 有定义。
R112 给 $B_0=B_2=0$，且只有 $4\mid m$ 的项可能非零。

记 $x_0,\sigma_0$ 为 $E_0$ 的 Weierstrass 函数，微分为 $dx/(2y)$。
实际首项一截面是
\[
                         A_{34}(z)=\sum_{4\mid m}b_mz^m.
\]

**定理。** 有准确恒等式
\[
 \boxed{\quad A_{34}(z)=\sigma_0(z)^{68}P(x_0(z)^2),\quad}     \tag{3}
\]
其中
\[
 \boxed{\quad
 P(X)=\frac15X(X-1)(X+1)^2
          (X^2-2X+5)(5X^2-2X+1)Q_8(X),
 \quad}                                                     \tag{4}
\]
\[
 Q_8(X)=X^8+364X^6-1088X^5+1190X^4-1088X^3+364X^2+1.         \tag{5}
\]
特别地
\[
 b_4=1,\qquad b_8=\frac{58}{15},\qquad
 b_{12}=\frac{588146}{1575},\qquad
 b_{16}=\frac{524545948}{10135125}.                            \tag{6}
\]
这里使用 $E_0$ 的尺度；没有将这些数直接当作 $E_{34}$ 微分下的系数。
两种尺度的准确关系是
\[
                   b_m^{(34)}=34^{(m-4)/2}b_m.                \tag{7}
\]

完整可复算证书为
[check-e34-theta-section.py](../scripts/check-e34-theta-section.py)。
它不使用浮点识别作为证明，也不预设未知参数有理。

## 2. 为什么是同一个实际次数六十八截面

R112 的新 dyadic 向量是实值、支撑于 $\frac12\mathbb Z_2$、
在 $2\mathbb Z_2$ 平移下不变，且对整个 $K_2^1$ 不变。
十七处向量仍为一个非平凡 tame 特征的标准 Fourier 像，
本次该特征是 $\lambda^2$。因此 R48 实结构证明 §§2–4 原样适用：
其 Fourier 计算只用特征非平凡，不要求阶恰为四。
二处的相位本次还可直接取为实相位。

具体地，可取全局 $L=34$；$d=L^2=1156$。
在 $E_{34}$ 的格
$\Gamma_{34}=\Omega_{34}\mathbb Z[i]$、
$\Omega_{34}=\Omega_0/\sqrt{34}$ 上，原截面 $S$ 满足
\[
 S(iz)=S(z),\qquad S(0)=0,\qquad
 \overline S(z)=S((\alpha/\bar\alpha)^{-1}z),                  \tag{8}
\]
在一次固定相位调整后成立。这个相位会在 (2) 的系数比中消失。
有理 norm-one 元 $\alpha/\bar\alpha$ 在二处仍固定新 dyadic 线，
故这里没有漏掉一个二处变换。

R49 的下降只用两份准周期、(8) 和 $d/17=68$ 为偶数：
扩大格为 $\alpha^{-1}\Gamma_{34}$，再令 $z\mapsto z/\alpha$，
得到 $S(z/\alpha)$ 是 $E_{34}$ 上的次数六十八截面。
其除以 $\sigma_{34}^{68}$ 后仅在原点有极点；
$i$ 不变性给它是 $x_{34}^2$ 的次数至多十六多项式。
在原点没有常数项且 $B_4\ne0$，所以最高次项可归一为一。

将 $(x_{34},y_{34})=(34x_0,34\sqrt{34}\,y_0)$ 以及
$z_0=\sqrt{34}\,z_{34}$ 代入，得
\[
 A_{34}(z)=\sigma_0(z)^{68}P_{\rm actual}(x_0(z)^2),
 \quad P_{\rm actual}\in\mathbb R_{\rm alg}[X],
 \quad\deg P_{\rm actual}=16.                                \tag{9}
\]
此时尚未假定 $P_{\rm actual}$ 有理。
原 Gaussian 尺度恰成为 (2)；(7) 同时由换元得到。

因此只需准确识别 $b_4,b_8,\ldots,b_{68}$ 共十七项。
相应基
\[
 \sigma_0^{68}x_0^{32},\
 \sigma_0^{68}x_0^{30},\ldots,\sigma_0^{68}
\]
分别从 $z^4,z^8,\ldots,z^{68}$ 起，首项全为一。
这十七项构成单位三角坐标。

## 3. 有理的是每个系数的平方：保留所有局部常数后作比

$E_{34}$ 的 Hecke 导子可取 $f=68$，$Nf=4624$。
二处导子恰为 $(1+i)^4$：
$\psi_0$ 的单位角色在 $1+(1+i)^3\mathcal O_{K,2}$ 上平凡，
但乘 $\chi_8\circ N$ 后，在 $-1+2i=1+(1+i)^3$ 取非平凡值，
因为其范数为 $5$。在 $1+4\mathcal O_{K,2}$ 上，范数属于
$1+8\mathbb Z_2$，两个角色都平凡。十七处分裂的两个单位角色
均为非平凡二次特征，导子各恰一阶。这给 $f=68$。

令 $\mathcal S_{34}$ 为实际 $P_f=\Omega_{34}/68$ 的 CM Galois 轨道。
中央 Kronecker 对角仍记
\[
 d_m=\sum_{j=0}^m\frac{q_j}{m!(m+1-j)!}
          \sum_{S\in\mathcal S_{34}}
          \mathscr D^{\,m}C_{m+1-j}(U_S,x(S),y(S)),
 \qquad e_m=\frac{d_m}{68^{2m+1}},                            \tag{10}
\]
其中
\[
 \frac z{\sigma_{34}(z)}=\sum_jq_jz^j,\quad
 \mathscr D=-X\partial_U+2Y\partial_X+(3X^2-1156)\partial_Y,
 \quad C_0=1,\ C_{n+1}=(\mathscr D+U)C_n.
\]
这就是原实际 Hecke 特征的类数一轨道；不改用任意全部挠点和。
所需权 $4\mid m$ 中的有限角色固定，故 R46 使用的 Yang
平方公式对同一个有限向量适用。

本次 $P_f$ 为实点，曲线与 $\mathscr D$ 都在 $\mathbb Q$ 上定义，
复共轭置换整个 $K$-Galois 轨道，所以 $d_m\in K\cap\mathbb R=\mathbb Q$。
这里也可用下面 (13) 的有理 division-function 表达核对
$U_S$ 的 Galois 相容性。因此 $e_m\in\mathbb Q$。

保留新的 $1/\sqrt2$、十七处 Gauss 常数和 Yang 全部局部因子时，
平方公式具有同一个非零常数 $\kappa$：
\[
              e_m=\kappa(Nf\cdot68)^{-m}
                       \bigl(b_m^{(34)}\bigr)^2.              \tag{11}
\]
归一 $b_4^{(34)}=1$ 时只改变 $\kappa$。
它不随 $m$ 改变；没有在不同权重新选平方根。
将 (11) 除以其 $m=4$ 式并使用 (7)，所有未单独计算的共同常数
准确消去：
\[
 \boxed{\quad
   b_m^2=9248^{\,m-4}\frac{e_m}{e_4}\in\mathbb Q
        \qquad(4\mid m,\ m\ge4).
 \quad}                                                     \tag{12}
\]
这里 $Nf\cdot68/34=9248$ 是整数。
$B_4\ne0$ 和平方公式同时保证 $e_4\ne0$。
(12) 不需要先证明 $P_{\rm actual}$ 的系数有理。

## 4. 全局分母：两个坏位均保留显式模型

取 $n\equiv1\pmod{68}$。在原 square lattice 上，
\[
       U_S=-\frac{\mathscr D\log\Psi_n(S)}{n(n-1)}.             \tag{13}
\]
这里 $\Psi_n=\sigma(nz)/\sigma(z)^{n^2}$。
因为 $[n]S=S$，(13) 来自准周期律；分母是 $n(n-1)$，
不是 $n^2-1$。

在一个整的好模型上，若 $n$ 是单位且 $\bar S\ne O$，
则 $\Psi_n(S)$ 为单位：其零除子是非零 $n$-挠点，而
$[n]\bar S=\bar S\ne O$。无竖直因子由 division polynomial
在原点的单位首项核对。
若原微分为 $u^{-1}$ 倍的好模型微分，则
\[
                  v(U_S)\ge v(u)-v(n(n-1)).                  \tag{14}
\]

对 $p\ne2,17$，原模型好，点为非零 prime-to-$p$ 挠点。
取 $n=69$；仅在 $p=3,23$ 换 $n=137$。
所用 $n(n-1)$ 都是单位，故 $U_S,x(S),y(S)$ 整。

在 $17$ 处，先除 $a=\sqrt{34}$，得到好模型 $E_0$。
$[17]S$ 是非零四挠点，故好模型上 $\bar S\ne O$。
取 $n=69$，$v_{17}(a)=1/2$，得到
\[
        v_{17}(U_S)\ge-\tfrac12,\quad
        v_{17}(x(S))\ge1,\quad v_{17}(y(S))\ge\tfrac32.         \tag{15}
\]

在 $2$ 处，先把 $E_0$ 用非零三挠 flex 变成
$Y^2+a_1XY+Y=X^3$ 的好模型。
[最低迹证明](2026-11-12-central-theta-d1-exact-global-trace.md) §1.4
的同一计算取 $D=1$，给该变换 $v_2(u_0)=1/2$，
原 $E_0$ 坐标下 $v_2(x_0)\ge0,v_2(y_0)\ge1/2$。
再乘 $a=\sqrt{34}$，复合变换 $u=au_0$ 满足 $v_2(u)=1$。
由于 $[4]S$ 是非零十七挠点，约化仍非零。
于是
\[
        v_2(U_S)\ge-1,\quad v_2(x(S))\ge1,\quad v_2(y(S))\ge2. \tag{16}
\]
这些估值对所有轨道点同时成立。

给 $U,X,Y$ 权 $1,2,3$，则 $\mathscr D^mC_{m+1-j}$ 的权至多
$2m+1-j$，系数均为整数。令
\[
 C_m^{\rm den}
   =\mathop{\rm lcm}_{0\le j\le m}
       \operatorname{den}\!\left(\frac{q_j}{m!(m+1-j)!}\right).
\]
由 (15)–(16)、$v_2(f)=2,v_{17}(f)=1$ 得
\[
 \boxed{\quad
 D_me_m\in\mathbb Z,\qquad
 D_m=C_m^{\rm den}\,
       2^{3(2m+1)}17^{\lceil3(2m+1)/2\rceil}.
 \quad}                                                     \tag{17}
\]
这是故意保留余量的统一上界；没有假定坏位挠点在原模型整。

## 5. 分母证书所需的唯一大小界

有 $\Omega_{34}=\Omega_0/\sqrt{34}>1/3$，
因为 $\Omega_0=2\int_0^1(1-t^4)^{-1/2}dt>2$ 且 $\sqrt{34}<6$。
把每个 $z_S/\Omega_{34}$ 移到标准方格内，
它到 $\mathbb Z[i]$ 的距离至少 $1/68$。

在方格 lattice 的 Weierstrass 级数中，将
$\|\gamma\|_\infty\le1$ 的九个位置单列。
其余第 $n$ 层有 $8n$ 个点，并有 $|w-\gamma|\ge n/2$。
使用 $\sum_{n\ge2}n^{-2}<1$，直接得到
\[
 |U_S|<10^5,\qquad |x(S)|<10^{10},\qquad |y(S)|<10^{15}.       \tag{18}
\]
脚本同时检查更小的有理上界：
\[
 3(68+8\cdot70+4+16),\
 9(9\cdot68^2+8+80),\
 27(9\cdot68^3+64).
\]
其中 $U$ 的余项为 $O(|\gamma|^{-3})$，
$x$ 的成对差也是 $O(|\gamma|^{-3})$，
而 $y$ 本身已绝对收敛。

轨道大小至多 $|\mathcal O_K/68|=4624$，但可用更小的
$|(\mathcal O_K/68)^\times|=2048$：
primitive 点的轨道位于单位倍数中。
置 $M=10^5$。对权至多 $w$ 的整多项式，
\[
 \|\mathscr DP\|_1\le2000w\|P\|_1,\qquad
 \|C_n\|_1\le2001^n n!.
\]
(10) 在 $m=4$ 仅有 $j=0,4$ 两项，且 $q_4=1156/60$。
因此
\[
 |e_4|\le|d_4|
 <2048\left[
  \frac{2000^4(5\cdot6\cdot7\cdot8)2001^5 5!\,M^9}{4!\,5!}
  +\frac{1156}{60}
       \frac{2000^4 4!\,2001\,M^5}{4!}
 \right]<10^{100}.                                          \tag{19}
\]
所有不等式由脚本用整数／有理数核对。

若 $e_4=A_4/D_4$，不要求既约，则
$0<|A_4|<D_4\,10^{100}$。由 (12)、(17)，$b_m^2$ 的既约分母
至多
\[
                         H_m=D_mD_4\,10^{100}.               \tag{20}
\]
乘子 $9248^{m-4}$ 是整数，不增大这一分母。

## 6. 完整 Gaussian 区间与离散间距

证书用 Arb/Acb 的 $8192$-bit 包含区间计算 (1) 中 $|n|\le1400$
及全部 $m=4,8,\ldots,68$；无限尾项单独估计。

对 $n\ge1401,m\le68$，归一 Hermite 系数满足
\[
 \left|[t^m]e^{-t^2+2Xt}\right|\le3n^{68},
 \qquad X=\sqrt{2\pi_{\mathbb C}}\,n/34.
\]
理由是 $2X<n$，把有限和的绝对值用
$\sum_j1/j!<3$ 上界。相邻尾项之比小于 $e^{-7}<1/2$，因为
\[
 \frac{68}{1401}-\frac{3(2\cdot1401+1)}{1156}<-7.
\]
所以整个双边尾小于
\[
 12\cdot1401^{68}\exp(-3\cdot1401^2/1156)<10^{-1900}.           \tag{21}
\]
最后一个不等式不用浮点数：
$3\cdot1401^2/1156>5093$、$e>8/3$，
而脚本准确检查
$12\cdot1401^{68}3^{5093}10^{1900}<8^{5093}$。

所得 $B_4$ 区间不含零。将 (2) 作区间运算后，对 (4) 给出的
每个精确有理候选 $\beta_m$，脚本严格检查
\[
 |b_m^2-\beta_m^2|
       <\frac1{H_m\,\operatorname{den}(\beta_m^2)}.            \tag{22}
\]
两个不同的有理数若分母分别不超过 $H_m$ 和
$\operatorname{den}(\beta_m^2)$，距离至少为右边。
故 (12)、(20)、(22) 强制 $b_m^2=\beta_m^2$。
再由实结构和严格正／负区间，确定 $b_m=\beta_m$。
最紧一项的间距分母有 $839$ 位；所用精度保留充分余量。

候选展开完全通过整系数流核对：置
\[
 u=1/\sqrt{x_0},\quad\vartheta_0^2=x_0\sigma_0^2,\quad
 L=\vartheta_0'/\vartheta_0,
\]
则
\[
 u''=-2u^3,\quad u(0)=0,\ u'(0)=1,\qquad
 L'=u^2,\quad \vartheta_0'=L\vartheta_0,\quad\vartheta_0(0)=1.
\]
将 (4) 改写成 $\vartheta_0^{68}u^{68}P(u^{-4})$，
得到全部 $\beta_m$，不依赖 Gaussian 计算。
按降幂排列的十七个系数准确为
\[
 \left(
 1,-\frac75,\frac{1833}5,-\frac{7963}5,\frac{18273}5,
 -\frac{18827}5,-\frac{11387}5,\frac{35521}5,-\frac{35521}5,
 \frac{11387}5,\frac{18827}5,-\frac{18273}5,\frac{7963}5,
 -\frac{1833}5,\frac75,-1,0
 \right).
\]
(9) 的单位三角性遂证明整条恒等式 (3)–(5)。

## 7. 可直接使用的除子信息，以及尚未证明的关系

(4) 已是实际截面的固定代数除子描述。
原点零阶四；$T_0=(0,0)$ 零阶四；
$T_\pm=(\pm1,0)$ 各零阶二；
$[2]^{-1}T_0$ 的四个点各零阶二。
因
\[
 \Psi_{2+i}\Psi_{2-i}=5x_0^4-2x_0^2+1,
\]
两个二次因子给
$E_0[2+i]\setminus\{O\}$、
$E_0[2-i]\setminus\{O\}$ 及它们的 $T_0$ 平移，
共十六个简单零点。
剩下的次数三十二除子由 $Q_8(x_0^2)=0$ 准确给出。
脚本以有理 Euclid 算法核对 $Q_8$ 平方自由，且与其余因子互素，
所以这些零点与前列点不重合。本篇不额外声称它们是挠点。

参考二处向量本身的 theta 为 $\theta_2+\theta_4$。
其次数四截面是 $(x_0^2-1)\sigma_0^4$。
具体地，原 Gaussian 在 $z=\Omega_0/2$ 平移相当于 $n\mapsto n+2$；
偶项变为 $-\theta_4(i)$，奇项为 $\theta_2(i)$，两者相消。
平移后的权仍是偶函数，故一阶导数也为零。
$i$ 对称给 $z=i\Omega_0/2$ 的另一双零。
它们已用完次数四；两边在原点取一，所以准周期和除子唯一确定
上述恒等式。
因此两条实际秩二行及参考截面现在都可用固定代数函数表达；
这里仍没有得到中央 Mellin 导数的非同时消失。

尤其 Jacobi 乘积不能丢掉混合角色：
在 $u=n_1+n_2,v=n_1-n_2$ 下，
原 $F_{17}$ 与共轭有限行的权是
\[
 \lambda(u+v)\lambda^{-1}(u-v)\zeta_{289}^{19uv},
 \qquad u\equiv v\pmod2.                                    \tag{23}
\]
它不是可直接替换的两个一元角色积。
在同一 CM 参数上，两份 $F_{17}$ 各双零，而 $F_{34}$ 是双零、
$\theta_2+\theta_4$ 非零，所以最直接的单项常数倍乘积恒等式也
不成立。带非平凡平移或参考差的分配式仍须另证。

## 来源与核查范围

- Yang **1997** 的全局平方公式、实际有限向量和 Hermite 规范：
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)；
  R46、R48、R49 与 R112 已逐项核定。本篇 (11)–(12) 明确只取消
  同一个非零共同常数，保留全部新 dyadic 因子。
- Bannai–Kobayashi **2010** 的 Kronecker theta 展开，以及实际
  division-function 的 Galois 规范，见原中央对角与最低迹笔记；
  本篇 (13)–(19) 已重新给出 E34 的坏位与大小证明。
- NIST DLMF（2010 年首次发布），
  [19.20.2](https://dlmf.nist.gov/19.20.E2)，固定 (2) 的实周期。
- F. Johansson，*Arb: efficient arbitrary-precision midpoint-radius interval
  arithmetic*，IEEE Transactions on Computers **66** (2017), 1281–1292：
  [作者原文](https://fredrikj.net/math/arbpaper.pdf)。
  Arb 仅用于有限运算的包含区间；(21) 独立控制无限尾项。

这里得到完整精确固定截面，未使用 BSD、任何 $p$-进高度猜想，
也没有把单个中央首层的计算推广为无穷多个素数。
