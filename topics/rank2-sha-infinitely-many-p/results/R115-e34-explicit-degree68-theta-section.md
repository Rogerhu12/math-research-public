# R115. E34 的实际次数六十八 sigma 截面

日期：2026-11-12。**状态：完整固定截面已证明；
尚未证明与 E17 的中央导数在无穷多个素数上不同时消失。**

## 1. 固定输入与精确结论

在 R112 的原有限向量上取
\[
 a_n^+=\varepsilon_n\lambda(n)^2\zeta_{289}^{77n^2}\ (17\nmid n),
 \quad a_n^+=0\ (17\mid n),\quad\lambda(3)=-i,
 \quad(\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3)=(1,1,-1,1).
\]
其 Hermite 生成函数为
\[
 B(t)=e^{-t^2}\sum_n a_n^+
     e^{-\pi_{\mathbb C}(n/34)^2+2\sqrt{2\pi_{\mathbb C}}(n/34)t}
     =\sum_mB_mt^m.
\]
令
\[
 \Omega_0=\frac{\Gamma(1/4)^2}{2\sqrt{2\pi_{\mathbb C}}},
 \qquad h_0=\frac{\sqrt{\pi_{\mathbb C}/2}\,34}{\Omega_0(4-i)},
 \qquad b_m=\frac{B_m}{B_4}h_0^{m-4}.                         \tag{1}
\]
严格区间证明 $B_4\ne0$；只有 $4\mid m$ 的项可能非零。

**定理。** 对 $E_0:y^2=x^3-x$ 的微分 $dx/(2y)$，
实际首项为 $z^4$ 的截面准确是
\[
 \boxed{\quad
 A_{34}(z)=\sum_{4\mid m}b_mz^m
       =\sigma_0(z)^{68}P(x_0(z)^2),
 \quad}                                                      \tag{2}
\]
\[
 \boxed{\quad
 P(X)=\frac15X(X-1)(X+1)^2
              (X^2-2X+5)(5X^2-2X+1)Q_8(X),
 \quad}                                                      \tag{3}
\]
\[
 Q_8(X)=X^8+364X^6-1088X^5+1190X^4-1088X^3+364X^2+1.          \tag{4}
\]
因此
\[
 b_4=1,\quad b_8=\frac{58}{15},\quad
 b_{12}=\frac{588146}{1575},\quad
 b_{16}=\frac{524545948}{10135125}.                            \tag{5}
\]
这些是 $E_0$ 尺度；$E_{34}:y^2=x^3-1156x$ 的同一微分规范下，
\[
                       b_m^{(34)}=34^{(m-4)/2}b_m.            \tag{6}
\]

## 2. 下降与十七项唯一性

R112 新 dyadic 向量是实值，并对整个 $K_2^1$ 不变。
R48 的十七处 Fourier 实结构计算仅要求 tame 特征非平凡，
故将 $\lambda$ 换为 $\lambda^2$ 后仍适用。
以 $L=34$、$d=1156$ 形成原 theta 截面 $S$，
一次固定相位后有
\[
 \overline S(z)=S((\alpha/\bar\alpha)^{-1}z),\quad
 \alpha=4-i,\qquad S(iz)=S(z),\quad S(0)=0.
\]
R49 的两份准周期扩大格为
$\alpha^{-1}\Omega_{34}\mathbb Z[i]$；
交叉相位因 $d/17=68$ 为偶数而为一。
所以 $S(z/\alpha)$ 是次数六十八截面。
除以 $\sigma_{34}^{68}$，仅在原点有极点且 $i$ 不变，
故是 $x_{34}^2$ 的次数至多十六多项式。

换成 (1) 的 $E_0$ 尺度，再归一首项一，得到
\[
 A_{34}=\sigma_0^{68}P_{\rm actual}(x_0^2),\qquad
 P_{\rm actual}\in\mathbb R_{\rm alg}[X],\quad \deg P_{\rm actual}=16.
\]
此时没有预设其参数有理。
基 $\sigma_0^{68}x_0^{32},\sigma_0^{68}x_0^{30},\ldots,\sigma_0^{68}$
分别从 $z^4,z^8,\ldots,z^{68}$ 起，首项均为一。
因此准确认定这十七项足以认定整条截面。

## 3. 实际中央平方关系与有理分母

曲线的 Hecke 导子为 $f=68$，$Nf=4624$。
二处，$\chi_8\circ N$ 在 $-1+2i\equiv1\bmod(1+i)^3$ 取负值，
在 $1+4\mathcal O_{K,2}$ 平凡；所以导子恰为 $(1+i)^4$。
十七处两个非平凡二次角色各有一阶导子。

令 $\mathcal S_{34}$ 是原实点 $P_f=\Omega_{34}/68$ 的实际
CM Galois 轨道。写
\[
 \frac z{\sigma_{34}(z)}=\sum q_jz^j,\qquad
 \mathscr D=-X\partial_U+2Y\partial_X+(3X^2-1156)\partial_Y,\qquad
 C_0=1,\quad C_{n+1}=(\mathscr D+U)C_n.
\]
原 Kronecker 对角是
\[
 d_m=\sum_{j=0}^m\frac{q_j}{m!(m+1-j)!}
       \sum_{S\in\mathcal S_{34}}
        \mathscr D^mC_{m+1-j}(U_S,x(S),y(S)),
 \qquad e_m=d_m/68^{2m+1}.                                   \tag{7}
\]
复共轭置换整个轨道，所有表达式定义在 $\mathbb Q$ 上，
所以 $e_m\in\mathbb Q$。

R46 的原平方公式应用于 R112 的同一有限向量，
保留新的 $1/\sqrt2$、Gauss 常数及全部局部因子后给
$e_m=\kappa(Nf\cdot68)^{-m}(b_m^{(34)})^2$，其中 $\kappa\ne0$
不随 $m$ 改变。只取与 $m=4$ 的比并使用 (6)，得
\[
 \boxed{\quad b_m^2=9248^{m-4}\frac{e_m}{e_4}\in\mathbb Q,
            \qquad4\mid m,\ m\ge4.\quad}                     \tag{8}
\]
这里 $B_4\ne0$ 同时保证 $e_4\ne0$。
未先假定 $b_m$ 有理；也未单独省去新 dyadic 常数作单位比较。

在所有原轨道点，
\[
 U_S=-\frac{\mathscr D\log\Psi_n(S)}{n(n-1)}
                     \qquad(n\equiv1\pmod{68}).               \tag{9}
\]
取 $n=69$，仅在 $p=3,23$ 换为 $137$。
在好模型中，$[n]\bar S=\bar S\ne O$，故 $\Psi_n(S)$ 为单位。
若原微分为 $u^{-1}$ 倍好模型微分，便有
$v(U_S)\ge v(u)-v(n(n-1))$。

在十七处，用 $\sqrt{34}$ 缩放到 $E_0$；
在二处再使用非零三挠 flex 的好模型，
总缩放参数的二进赋值为一。
$\bar S\ne O$ 分别由 $[17]S$ 的非零四挠部分、
$[4]S$ 的非零十七挠部分保证。准确得到
\[
 \begin{array}{c|ccc}
 &U_S&x(S)&y(S)\\ \hline
 v_2&\ge-1&\ge1&\ge2\\
 v_{17}&\ge-1/2&\ge1&\ge3/2
 \end{array}
\]
其余素位全部整。令
\[
 C_m^{\rm den}=\mathop{\rm lcm}_{j\le m}
       \operatorname{den}\!\left(\frac{q_j}{m!(m+1-j)!}\right),
 \qquad
 D_m=C_m^{\rm den}2^{3(2m+1)}17^{\lceil3(2m+1)/2\rceil}.
\]
加权次数至多 $2m+1$ 给
\[
                              D_me_m\in\mathbb Z.              \tag{10}
\]

由 $\Omega_{34}>1/3$ 和所有非零六十八挠点到方格的距离
至少 $1/68$，逐层估计 Weierstrass 级数给
$|U|<10^5,|x|<10^{10},|y|<10^{15}$。
轨道至多 $2048$ 点；以
$\|\mathscr DP\|_1\le2000w\|P\|_1$、
$\|C_n\|_1\le2001^nn!$ 代入 (7) 的两个 $m=4$ 项，得到
\[
                 0<|e_4|<10^{100},\qquad
 \operatorname{den}(b_m^2)\le H_m:=D_mD_4\,10^{100}.           \tag{11}
\]
全部整数不等式在计算证书中单独核对。

## 4. 严格区间证书

[check-e34-theta-section.py](../scripts/check-e34-theta-section.py)
用 $8192$-bit Arb/Acb 运算包住 (1) 中 $|n|\le1400$ 的有限和。
无限尾项由独立整数不等式给
\[
 12\cdot1401^{68}e^{-3\cdot1401^2/1156}<10^{-1900}.
\]
程序准确检查
$3\cdot1401^2/1156>5093$、
$12\cdot1401^{68}3^{5093}10^{1900}<8^{5093}$；
使用 $e>8/3$ 即足够。

对 (3) 精确有理展开的每个 $\beta_m$，计算得到
\[
 |b_m^2-\beta_m^2|
   <(H_m\operatorname{den}(\beta_m^2))^{-1}.
\]
(8)、(11) 与有理数离散间距强制平方相等；
严格正／负区间再确定一致符号。最紧的间距分母为 $839$ 位。
全部十七项通过，并由第 2 节的单位三角性确定 (2)。

候选展开本身独立用整系数流
\[
 u''=-2u^3,\quad L'=u^2,\quad\vartheta_0'=L\vartheta_0,
 \quad u(0)=0,\ u'(0)=1,\ \vartheta_0(0)=1
\]
计算 $\vartheta_0^{68}u^{68}P(u^{-4})$，不借 Gaussian 值拟合。
程序还以有理 Euclid 算法验证 $Q_8$ 平方自由，
并与其他因子互素。

## 5. 除子及后续关系的准确边界

(3) 给原点四阶、$T_0=(0,0)$ 四阶、
$T_\pm=(\pm1,0)$ 各二阶、
$[2]^{-1}T_0$ 四点各二阶；
norm-five 核与其 $T_0$ 平移贡献十六个简单零点。
剩余三十二个简单零点由 $Q_8(x_0^2)=0$ 给出，
本结果不预设它们是挠点。

参考 dyadic theta $\theta_2+\theta_4$ 的次数四截面是
$(x_0^2-1)\sigma_0^4$：平移到 $\Omega_0/2$ 后两项成为
$-\theta_4(i)+\theta_2(i)=0$，偶性再给一阶导数零；
$i$ 对称给另一双零，次数四及原点值一完成认定。

固定截面的显式性尚不提供两条曲线的中央导数覆盖。
实际 $F_{17}$ 与共轭有限行的乘积，在
$u=n_1+n_2,v=n_1-n_2$ 后保留混合权
$\lambda(u+v)\lambda^{-1}(u-v)\zeta_{289}^{19uv}$ 及
$u\equiv v\bmod2$；不能直接换成两个一元角色。
同一 CM 参数下的零阶也排除不带额外项的
$F_{17}\overline F_{\rm finite}=C F_{34}(\theta_2+\theta_4)$。
非平凡平移或参考差的分配式仍须另证。

## 6. 完整证明与来源

完整尺度、实际轨道、坏位、离散间距及除子说明见
[E34 完整证书笔记](../notes/2026-11-12-e34-degree68-section-and-exact-certificate.md)。

- Yang **1997** 的全局平方公式与局部模型：
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)；
  实际向量及所有固定规范已在 R46、R48、R49、R112 核定。
- Bannai–Kobayashi **2010** 的 Kronecker 展开和 division-function
  规范，及原最低迹证明；本次已重新证明 E34 的两个坏位估值。
- NIST DLMF（2010 年首次发布），
  [19.20.2](https://dlmf.nist.gov/19.20.E2)，固定实周期。
- F. Johansson，IEEE Transactions on Computers **66** (2017),
  1281–1292：
  [Arb 作者原文](https://fredrikj.net/math/arbpaper.pdf)。
  这里只用其有限运算的包含区间，无限尾项另有完整证明。
