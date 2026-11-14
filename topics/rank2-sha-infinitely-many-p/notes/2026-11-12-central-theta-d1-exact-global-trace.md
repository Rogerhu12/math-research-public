# 最低中央迹的严格全局值：d₁=64(−1+i)

**状态：已证明。** 日期：2026-11-12。

沿用固定曲线、导子、周期和轨道
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
f=34(1+i),\quad P_f=\Omega_E/f,\quad
F=K(E[\mathfrak f]).
$$
$\Omega_E>0$ 为微分 $dx/(2y)$ 的最小正实周期。
[中央 theta 对角笔记](2026-11-12-anticyclotomic-theta-diagonal.md)
定义的最低非恒定对角为
$$
d_1=-\operatorname{Tr}_{F/K}(U_{P_f}x(P_f)+y(P_f)),
\qquad U_S=E_1^*(S).
\tag{1}
$$

**定理。**
$$
\boxed{
d_1=64(-1+i),\qquad
N_{K/\mathbb Q}(d_1)=2^{13},\qquad
e_1:=d_1/f^3=\frac4{17^3}.
}
\tag{2}
$$
特别地，$d_1$ 在每个奇素位都是单位。
证明先给出全局分母和复大小的显式上界，再用精确有限环同余唯一认定
全局迹；没有把几个局部样例直接当成全局等式。
固定周期的单位方向只在最后用已核准的旧矩决定。
非零性、范数及所有奇处单位性均不依赖这个方向的选择。

计算脚本：
[check-central-theta-d1.py](../scripts/check-central-theta-d1.py)。
它调用此前两个有限环证书，完整检查本证明所需的数值不等式与同余。

## 1. 各个 primitive 轨道的分母统一由 4 清除

对任意 primitive $\mathfrak f$-点 $S$，记
$$
d_1(S)=-\sum_{\tau\in\operatorname{Gal}(F/K)}
\bigl(U_{S^\tau}x(S^\tau)+y(S^\tau)\bigr)\in K.
\tag{3}
$$
四个可能轨道由 $\mu_4$ 作用互相转换。
先证明与轨道方向无关的结论
$$
\boxed{4d_1(S)\in\mathbb Z[i].}
\tag{4}
$$

### 1.1. 一个适用于好模型的 division-function 估值

若奇数 $n\equiv1\pmod{68}$，则 $[n]S=S$。
标准 sigma 除法关系给
$$
D\log\Psi_n(S)
=n\zeta(nz_S)-n^2\zeta(z_S)
=-n(n-1)U_S.
$$
故
$$
\boxed{U_S=-\frac{D\log\Psi_n(S)}{n(n-1)}.}
\tag{5}
$$
此式属于 $F$，也说明 $U$ 的 Galois 相容性。

在一个整的好 Weierstrass 模型上，若 $n$ 为剩余特征单位，
$S$ 的约化非 $O$ 且 $[n]\bar S=\bar S$，
则 $\Psi_n(S)$ 是单位。
理由是 $\Psi_n$ 的零除子为非零 $n$-division 点，
极点只在 $O$；$n$ 为单位时约化后仍是这一 étale 零除子，
而 $[n]\bar S=\bar S\ne O$ 排除了零点。
标准 division polynomial 的整系数及在 $O$ 的单位首项排除了竖直因子。
好模型的不变导子保持整函数，故 $D\log\Psi_n(S)$ 整。

若原模型和这个好模型之间的变量变换为
$$
x=u^2X+r,\qquad
y=u^3Y+s u^2X+t,
\tag{6}
$$
则 $\omega_{\rm orig}=u^{-1}\omega_{\rm good}$，
因此 $D_{\rm orig}=uD_{\rm good}$。
两模型的 $\Psi_n$ 相差常数 $u^{n^2-1}$，
由其除子和 $O$ 处首项即可核对。
对数导数不受该常数影响，所以 (5) 给
$$
v(U_S)\ge v(u)-v(n(n-1)).
\tag{7}
$$
以下每次都先核对 $\bar S\ne O$，不会只凭 torsion 点在好模型上
就假定它的坐标整。

### 1.2. 剩余特征不为 2、17 的地方

这些地方原曲线有好约化，且 $S$ 是 prime-to-$p$ 的非零 torsion，
所以约化非 $O$，$x(S),y(S)$ 整。
若 $p\ne3,23$，取 $n=69$；
若 $p=3$ 或 $23$，取 $n=137$。
两种选择都满足 $n\equiv1\pmod{68}$，
而在所用的地方 $n(n-1)$ 是单位。
由 (5) 得 $U_S$ 整，故 (3) 整。

### 1.3. 17 处的缩放

在有限扩张中取 $a^4=17$，使用
$$
x=a^2X,\qquad y=a^3Y,\qquad
E_0:Y^2=X^3-X.
\tag{8}
$$
$E_0$ 在 $17$ 处有好约化，$v_{17}(a)=1/4$。
$[17]S$ 是非零的 $\lambda^3$-torsion 点，$\lambda=1+i$，
其阶与 $17$ 互素，所以它的约化非零。
因此 $S$ 在好模型上的约化也非零。
这里无需断言 $S$ 自身约化后的准确阶。

取 $n=69$。它是 $17$-单位，且 $[69]S=S$，
故 $\Psi_{69}$ 在该点为单位。
式 (7) 以及好模型坐标的整性给
$$
v_{17}(U_S)\ge-\frac34,\qquad
v_{17}(x(S))\ge\frac12,\qquad
v_{17}(y(S))\ge\frac34.
\tag{9}
$$
于是
$v_{17}(U_Sx(S)+y(S))\ge-1/4$。
对所有共轭求和仍有该下界；
而 $d_1(S)\in K$，$17$ 在 $K$ 中分裂，其素位上的赋值取整数。
故
$$
v_{\mathfrak q}(d_1(S))\ge0\qquad(\mathfrak q\mid17).
\tag{10}
$$

### 1.4. 2 处的显式好模型

取一个非零 $3$-torsion 点 $(r,t)$。
它的横坐标满足
$$
3r^4-102r^2-289=0.
\tag{11}
$$
该多项式的 Newton polygon 给 $v_2(r)=0$。
更直接地，写 $w=r^2$，则
$$
(w-17)^2=1156/3,
$$
所以
$$
v_2(r^2-17)=1,\qquad
t^2=r(r^2-17),\qquad v_2(t)=1/2.
\tag{12}
$$
令
$$
s=\frac{3r^2-17}{2t}.
$$
由 (11) 可核对 $s^2=3r$，故 $v_2(s)=0$。
再取 $u^3=2t$，于是 $v_2(u)=1/2$。
变换 (6) 将原曲线准确变成
$$
E_0:\quad Y^2+a_1XY+Y=X^3,\qquad a_1=2s/u.
\tag{13}
$$
确实，$a_2=(3r-s^2)/u^2=0$，
$a_4=(3r^2-17-2st)/u^4=0$，
$a_6=(r^3-17r-t^2)/u^6=0$。
又 $v_2(a_1)=1/2>0$，
$$
\Delta(E_0)=a_1^3-27
$$
为单位。因此 (13) 是一个显式好模型。

$[4]S$ 是非零的 $17$-torsion，约化单射说明其约化非零；
故 $S$ 的约化也非 $O$。
再次取 $n=69$，有 $\Psi_{69}(S)$ 为单位，
$v_2(69\cdot68)=2$。于是 (7) 给
$$
v_2(U_S)\ge-\frac32.
$$
由 (6)、(12)–(13) 和好模型坐标整性，
$$
v_2(x(S))\ge0,\qquad v_2(y(S))\ge\frac12.
\tag{14}
$$
从而
$$
v_2(d_1(S))\ge-\frac32,\qquad v_2(4d_1(S))\ge\frac12>0.
\tag{15}
$$
结合其余素位的整性，证明 (4)。

## 2. 不用浮点数的复绝对值上界

下面证明对每个 primitive 轨道都有
$$
\boxed{|d_1(S)|<B:=10190905920.}
\tag{16}
$$

### 2.1. 周期和 torsion 点的距离

对 $E_1:y^2=x^3-x$，最小正实周期为
$$
\Omega_1=\int_1^\infty\frac{dx}{\sqrt{x^3-x}}
>\int_1^\infty x^{-3/2}\,dx=2.
$$
由四次缩放，
$$
\Omega_E=17^{-1/4}\Omega_1>\frac23,
\tag{17}
$$
因为 $17^{1/4}<3$。

写 $z_S=\Omega_E w$，并在模 $\mathbb Z[i]$ 后选
$|\operatorname{Re}w|,|\operatorname{Im}w|\le1/2$。
于是 $|w|<1$。
因 $w\in f^{-1}\mathbb Z[i]\setminus\mathbb Z[i]$，
$$
|w-\gamma|\ge |f|^{-1}>1/49
\quad(\gamma\in\mathbb Z[i]),
\tag{18}
$$
其中 $|f|^2=2312<49^2$。

### 2.2. 方格 lattice 的三个统一界

以下 $\wp_0,\zeta_0$ 对应周期格 $\mathbb Z[i]$。
标准绝对收敛 lattice 展开为
$$
\wp_0(w)=\frac1{w^2}
+\sum_{\gamma\ne0}
\left(\frac1{(w-\gamma)^2}-\frac1{\gamma^2}\right),
$$
$$
\zeta_0(w)=\frac1w+
\sum_{\gamma\ne0}
\left(\frac1{w-\gamma}+\frac1\gamma+\frac{w}{\gamma^2}\right),
\qquad
\frac{\wp_0'(w)}2=-\sum_{\gamma\in\mathbb Z[i]}(w-\gamma)^{-3}.
\tag{19}
$$
第一、二式为 DLMF 23.2.4–23.2.5，第三式逐项求导得到。

恰有 $8$ 个非零格点满足 $|\gamma|<2$。
对其余格点，$|w-\gamma|\ge|\gamma|/2$，且
$$
\sum_{\gamma\ne0}|\gamma|^{-3}
\le\sum_{n\ge1}\frac{8n}{n^3}<16.
\tag{20}
$$
其中按 $\max(|\operatorname{Re}\gamma|,
|\operatorname{Im}\gamma|)=n$ 分层，并用
$\sum_{n\ge1}n^{-2}<2$。

尾项可分别估计为
$$
\left|\frac1{(w-\gamma)^2}-\frac1{\gamma^2}\right|
\le10|\gamma|^{-3},
$$
$$
\left|\frac1{w-\gamma}+\frac1\gamma+\frac{w}{\gamma^2}\right|
\le2|\gamma|^{-3},
\qquad
|(w-\gamma)^{-3}|\le8|\gamma|^{-3}.
\tag{21}
$$
结合 (18) 逐项得到
$$
|\wp_0(w)|<9\cdot49^2+8+160=21777,
$$
$$
|\wp_0'(w)/2|<9\cdot49^3+128=1058969,
$$
$$
|\zeta_0(w)|<49+8(49+2)+32=489.
\tag{22}
$$
方格 lattice 的 $E_1^*$ 修正为 $\pi\bar w$，
所以 $\pi<4$、$|w|<1$ 又给
$$
|\zeta_0(w)-\pi\bar w|<493.
\tag{23}
$$

### 2.3. 将界带回 trace

缩放公式给
$$
x(S)=\Omega_E^{-2}\wp_0(w),\quad
y(S)=\Omega_E^{-3}\wp_0'(w)/2,\quad
U_S=\Omega_E^{-1}(\zeta_0(w)-\pi\bar w).
$$
因此 $256$ 点 trace 满足
$$
\begin{aligned}
|d_1(S)|
&<256\Omega_E^{-3}
\bigl(493\cdot21777+1058969\bigr)\\
&<256\cdot\frac{27}{8}
\bigl(493\cdot21777+1058969\bigr)\\
&=10190905920.
\end{aligned}
\tag{24}
$$
这证明 (16)，全过程没有使用近似周期或数值 $L$ 值。

## 3. 一个高精度局部迹唯一决定全局值

以参数 $3,1,24$ 运行
[惰性有限环脚本](../scripts/check-central-theta-inert.py)，
即在 $3^{24}$ 精度只计算到 $d_1$。
模环、$256$ 点轨道、$U=-r_{34}/34$ 初值和所有单位逆元
按 [惰性样例证书](2026-11-12-central-theta-inert-samples.md) 构造。
Newton 迭代次数由精度自动确定；这里五次迭代足够。
输出为
$$
\boxed{
d_1^{\rm raw}\equiv64+64i\pmod{3^{24}},
\qquad 3^{24}=282429536481.
}
\tag{25}
$$
$m=1$ 的求值多项式是整数多项式 $-UX-Y$，
所以没有额外除法或精度损失。

现在
$$
Z=4d_1^{\rm raw}-256(1+i)\in\mathbb Z[i]
$$
由 (4) 成立；(25) 给 $Z\in3^{24}\mathbb Z[i]$。
若 $Z\ne0$，则 $|Z|\ge3^{24}$。
但由 (16)，
$$
|Z|<4B+256\sqrt2<4B+512
=40763624192<282429536481.
\tag{26}
$$
矛盾。因此得到**全局准确等式**
$$
\boxed{d_1^{\rm raw}=64(1+i).}
\tag{27}
$$
这里只使用一个模同余、严格分母界和严格复界；
没有调用数值识别的经验性高度阈值。

## 4. 固定周期规范的单位方向

(27) 说明规范 $P_f$ 的 $d_1$ 必属于
$$
\{64(1+i),\ 64(-1+i),\ 64(-1-i),\ 64(1-i)\}.
\tag{28}
$$
为确定其中一个，使用已审阅的
[p=13 中央证书](2026-11-12-central-theta-p13-certificate.md)
的同一轨道，不重新选择中央值的单位。

该证书通过旧矩 $\lambda_{13}$ 将点轨道 $S$ 旋转为
$\epsilon S$，其中 $\epsilon=-i$；
因此权 $13$、$25$ 的 trace 乘 $i$。
但 $d_1$ 的权是 $3$，其正确转换为
$$
d_1(\epsilon S)=\epsilon^{-3}d_1(S)=-i\,d_1(S).
\tag{29}
$$
两者的区别必须保留。

在相同的模 $13^5$ 环中，直接求值 $-UX-Y$ 得
$$
d_1(S)\equiv243720\pmod{371293},
$$
随后按 (29) 得
$$
\boxed{
d_1(P_f)\equiv127445
=64(-1+i)\pmod{13^5},
\quad i\equiv228249\pmod{13^5}.
}
\tag{30}
$$
(28) 的四个候选模 $13$ 已互不相同，所以 (30) 唯一选出
$d_1(P_f)=64(-1+i)$。
这完成 (2) 中第一式的证明。
其余两式直接计算：
$$
N(64(-1+i))=64^2\cdot2=2^{13},
$$
$$
f^3=34^3(1+i)^3=78608(-1+i),\qquad
\frac{64}{78608}=\frac4{17^3}.
\tag{31}
$$

规范的单位方向使用 CLS II 已更正的旧非中央表项，
与 p=13 证书完全一致。
若只要“$d_1$ 在所有奇处为单位”这一后续算术输入，
可完全略过本节和该表项：由 (27) 及 $\mu_4$ 轨道关系已经得到。

## 5. 对下一条惰性递推的意义

现在中央对角的首坏层若归约为
$q^2d_{q+2}\equiv C_q^2d_1\pmod q$，
右端的固定最低 trace 不再是未定非零量：
本定理说明它在所有奇素位都为单位。
本文不把该一般递推当作自身证明的一部分；
其独立推导与这里的全局 trace 认证可以直接拼接。

这个最低阶常数的认证也没有完成普通素数 $p$ 上
$d_{p-1}\notin p^4$ 的无穷性。
它提供的是固定序列真实惰性分母结构所需的一个完整算术输入。

## 来源及复算

- [中央 theta 对角笔记](2026-11-12-anticyclotomic-theta-diagonal.md)，
  给 $d_m$、$U_S$、division-function 公式及 Galois 相容性。
- [p=13 中央证书](2026-11-12-central-theta-p13-certificate.md)，
  给准确 $H=\langle-3,-2+i\rangle$ 轨道和最后一步的固定周期方向。
- [惰性样例证书](2026-11-12-central-theta-inert-samples.md)，
  给无分歧模环、torsion Hensel 提升和明确精度规则。
- NIST DLMF，23.2.4–23.2.5 及绝对局部一致收敛说明，
  [原文](https://dlmf.nist.gov/23.2)。
  本文的常数界由这些定义逐项证明，并非外引的数值估计。
- [全局最低迹证书脚本](../scripts/check-central-theta-d1.py)；
  运行时重新执行高精度 $3$-进迹及正确的权 $3$ 定向，
  并以整数比较核验 (26)。
