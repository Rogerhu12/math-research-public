# 原固定 genus 4 商的完整 Raynaud 配对消失与指定 e

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta。

**状态：纯纸面已证明的来源等价，未证明原指定非零。**
本篇把 R1061 的同一个 Miller / Picard 系数 $e$ 接到一个固定 genus 4 曲线
的全部正则微分，而不只接一个二维子空间。精确结论为
$$
\boxed{
e=0
\quad\Longleftrightarrow\quad
\beta_Y:\bigwedge\nolimits^2H^0(Y,\Omega_Y^1)
\longrightarrow H^0(Y,\Omega_Y^1)
\text{ 恒为零}.
}
\tag{G4.1}
$$
所有四个正则微分都 Cartier-exact，故这里确实定义了全部全局 Raynaud 配对。
证明保留原曲线、原微分和 absolute / relative Cartier 的差别。
本文不使用、也不声称“全局配对为零推出 hyperelliptic”的逆命题。

## 1. 原 X0(108) 的实际固定商与四个正则微分

保持 R1059、R1061、R1126 的规范
$$
p=6k-1\ge41,\quad N=k-1,\quad
s^2=-3,\quad \kappa=3s,\quad v=-6s=-2\kappa,\quad
\rho^3=2,\quad \rho\in\mathbf F_p,
$$
$$
X:\quad z^3=1-\kappa x^3,\qquad
w^3=1+\kappa x^3,\qquad
\Omega=\frac{dx}{z^2w^2}.
$$
为避免把原形式 $w^2\Omega$ 和椭圆常数 $v$ 混用，本篇记
$$
u=z^2\Omega,\qquad h=zw\Omega,\qquad \nu=w^2\Omega.
$$
在同一函数域置
$$
\eta=\frac zw,\qquad y=\frac{2x}{w^2},\qquad c=\frac2\kappa.
$$
直接代入原两个三次方程，得到实际商
$$
Y:\qquad y^3=c(1-\eta^6).
\tag{G4.2}
$$
映射 $X\to Y$ 的固定群是
$(x,z,w)\mapsto(\zeta^{-1}x,\zeta z,\zeta w)$，
其阶为三。反向由 $w^3=2/(1+\eta^3)$、
$x=yw^2/2$、$z=\eta w$ 恢复整个函数域，故 degree 准确为三。
特别地，当前 $p\ne3$ 下它可分，正则微分的拉回单射并与 Cartier 相容。

$Y$ 指 (G4.2) 的光滑射影正规化。
投影到 $\eta$ 直线在六个有限零点有 ramification index 三，
无穷处有三个不分歧点，所以 Riemann–Hurwitz 给 $g(Y)=4$。
四个正则微分为
$$
\omega_j=\eta^j\frac{d\eta}{y^2}\quad(0\le j\le2),
\qquad a=\frac{d\eta}{y}.
\tag{G4.3}
$$
在有限 branch 点，以 $y$ 为参数，$d\eta$ 有二阶零；
在每个无穷点，$y$ 有二阶极，因此 $\omega_j$ 的阶为 $2-j$，
$a$ 的阶为零。它们线性无关，故构成完整基。

原微分尺度不是重新选择的单位。直接微分
$$
d\eta=-\frac{2\kappa x^2}{z^2w^4}\,dx
$$
给
$$
\boxed{(\nu,h,u)=-c(1,\eta,\eta^2)\frac{d\eta}{y^2}.}
\tag{G4.4}
$$
本篇以后同名 $u,h,\nu$ 均指 (G4.4) 在 $Y$ 上的实际微分。

作为几何范围核对，canonical 比值
$\omega_1/\omega_0=\eta$、$a/\omega_0=y$
生成 $K(Y)$，所以 canonical 映射双有理，$Y$ 不是 hyperelliptic。
这个事实本身仍不排除某个特征下 (G4.1) 右端成立。

## 2. 四个输入全部 Cartier-exact

写 $P(\eta)=c(1-\eta^6)$、$n=(p-2)/3=2k-1$。
对 $0\le j\le2$ 有
$$
\omega_j=y^{-p}\eta^jP(\eta)^n\,d\eta.
$$
分子的指数为 $6i+j$，最高次不超过 $2p-2$。
唯一可能被 Cartier 读到的指数是 $p-1\equiv4\bmod6$，
而 $j=0,1,2$ 都不符合。因此 $C(\omega_j)=0$。

对第四个微分，
$$
a=y^{-2p}P(\eta)^{(2p-1)/3}\,d\eta,
\qquad (2p-1)/3=4k-1.
$$
分子的最高次是 $4p-2$，全部指数为零模六。
可能的 $rp-1$ 中 $1\le r\le3$，其模六类分别为 $4,3,2$，
仍无读取项。因此
$$
\boxed{C(a)=C(\nu)=C(h)=C(u)=0.}
\tag{G4.5}
$$
这里直接计算的是完整有理源，不依赖仅由 Jacobian 的同源类型推断
某个给定微分是否 exact。

对所有 $\alpha,\beta\in H^0(Y,\Omega_Y^1)$，
取有理 primitive $dF_\alpha=\alpha$，定义
$$
\beta_Y(\alpha,\beta)=C_{\mathrm{abs}}(F_\alpha\beta).
\tag{G4.6}
$$
Cartier 核正是有理 exact 微分，保证 primitive 存在。
$p$ 次幂歧义因 $C(\beta)=0$ 消失。
该配对正则、交替，对输入标量按 $p$ 次根半线性；
这些是 R1059 / R1126 已使用的同一 Raynaud 配对。

## 3. 第四个微分与其余三条方向的配对严格为零

在 $Y$ 上有实际 $\mu_6\times\mu_3$ 作用
$$
(\eta,y)\longmapsto(\xi\eta,\zeta y).
$$
用模六、模三指数记录字符，完整正则基的字符为

| 微分 | 字符 |
|---|---|
| $\nu$ | $(1,1)$ |
| $h$ | $(2,1)$ |
| $u$ | $(3,1)$ |
| $a$ | $(1,2)$ |

由于 $p^{-1}\equiv-1\bmod6$ 和 $\bmod3$，
(G4.6) 的输出字符是两个输入字符之和的负数。
因此 $(a,\nu),(a,h),(a,u)$ 的输出字符依次为
$(4,0),(3,0),(2,0)$。
这三条字符都不出现在完整四维正则目标中，故
$$
\boxed{\beta_Y(a,\nu)=\beta_Y(a,h)=\beta_Y(a,u)=0.}
\tag{G4.7}
$$
没有把目标预先限制到某个 CM 子空间，也没有使用向量丛纤维配对的
非退化性来替代这一全局计算。

## 4. 同一个原 e 的精确尺度

原椭圆曲线及其不变微分为
$$
E:V^2=U^3+v^2,\qquad \omega=\frac{dU}{2V}.
$$
在 (G4.2) 上，原实际映射可明确写为
$$
U=\frac{4\eta^2}{y^2},\qquad
V=v\frac{1+\eta^6}{1-\eta^6},\qquad
\omega\longmapsto h.
\tag{G4.8}
$$
曲线方程由 $c^2=-4/27$ 直接验证，
最后一个微分尺度由
$dU/(2V)=4\eta\,d\eta/(v y^2)=-c\eta\,d\eta/y^2$
给出。

保持原 $Q=(0,v)$、$m=(p-1)/2$ 和 Miller 规范
$$
F_Q=\left(\frac{V+v}{V-v}\right)^k,\qquad
D\Psi=\delta,\qquad \delta\in\mathbf F_p^\times.
$$
沿 (G4.8)，$F_Q=\eta^{-(p+1)}$，故严格有
$$
\nu=\eta^p F_Qh,\qquad u=\eta h.
\tag{G4.9}
$$
R1061 的同一个指定系数 $e$ 满足
$$
C_{\mathrm{rel}}(F_Q\Psi\omega)=e\omega',
\qquad e^p=-e.
$$
换成本篇 (G4.6) 的 absolute Cartier 时，准确为
$$
C_{\mathrm{abs}}(F_Q\Psi\omega)=-e\omega.
$$
以 $\Psi/\delta$ 作为 $h$ 的真实 primitive，再用 (G4.9)，得到
$$
\boxed{\beta_Y(h,\nu)=-\frac e\delta\,u.}
\tag{G4.10}
$$
这里外部负号不能丢掉，也不能在 relative 公式中对 base 标量擅取 $p$ 次根。

为与原完整张量逐尺度比较，令 $A,S$ 正是 R1126.6 的有限和，
其中 $S=S_n$，而非另一归一的 inverse-center sum。
R1126 的实际 $X$ 上配对表及可分拉回单射给
$$
\beta_Y(u,h)=B\nu,\qquad
\beta_Y(h,\nu)=Bu,\qquad
\beta_Y(u,\nu)=\frac S s\,h,\qquad
B=-3\rho sA.
\tag{G4.11}
$$
比较 (G4.10) 与 (G4.11)，得到新的精确原尺度身份
$$
\boxed{e=3\rho s\delta A,\qquad B=-e/\delta.}
\tag{G4.12}
$$
它与 $e^p=-e$ 相容，因为 $A,\rho,\delta\in\mathbf F_p$、$s^p=-s$。

## 5. 完整等价及其后继范围

R1061.16–19 已经通过实际双覆盖、relative Cartier 的两个
局部生成元、Frobenius Picard 参数及 trace 因子二证明
$$
e=0\quad\Longleftrightarrow\quad S_n=0.
\tag{G4.13}
$$
本篇只消费这一已付的非零等价，不将它升级为未经证明的
数值恒等式 $e=cS_n$。

若 $e=0$，(G4.12) 给 $A=B=0$，(G4.13) 给 $S=0$；
(G4.11) 中三对全零。结合 (G4.7) 与交替性，
完整四维正则空间上的全部六对均为零。
反过来，若 $\beta_Y$ 恒零，(G4.10) 及 $\delta u\ne0$
立即给 $e=0$。这证明 (G4.1)。

因此原指定非零可等价地研究为：这个明确的固定非 hyperelliptic
genus 4 曲线的全部全局 Raynaud 配对是否非零。
这是新的完整几何输入，不是非零证明。
已知的“hyperelliptic 导致该配对消失”方向不能反用；
全局四维空间在较大秩向量丛中的 isotropic 性也不构成矛盾。
本篇没有由 (G4.1) 推出 $K_4$、原短 $\nu_k$ 或全局主目标已经关闭。

## 来源与审计

- [R1059](../results/R1059-original-fN-actual-X108-Raynaud-pairing-and-inverse-central-sum.md)：
  同一个实际 $X_0(108)$ 模型及原 $\beta$ 来源。
- [R1061](../results/R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)，
  §§8–10：原 $e$、absolute / relative Cartier、$e$ 与 $S_n$ 的实际非零等价。
- [R1126](../results/R1126-original-X108-complete-CM-Raynaud-pairing.md)，
  §§3–5：完整原配对表以及 $A,S,B=-3\rho sA$ 的准确尺度。

o1_theta 全文纸推并逐项核对。
本篇不含数学程序执行、素数窗口或未付的 theta 光滑性断言。

root / o2_high_coefficient 对候选 bbffe156d2dc4674f768daa1929a2ec5ec4eef60 独立全文纸审通过：实际 degree 三商、无穷极阶、四基 Cartier 指数、全部字符以及 (G4.8)–(G4.13) 的绝对负号均保留。已核主来源的单向陈述 [Chidambaram, arXiv:2611.16449, Lemma 2.1](https://arxiv.org/pdf/2611.16449)；该引理只给 hyperelliptic 时配对为零，不提供逆命题。


## 6. 同一原商上方的 Fermat 六次曲线：完整十维配对

本节把 (G4.1) 接到一个完整的固定 $g=10$ 对象。
底域可扩到包含 $\mu _6$ 及以下 $b_0$ 的完美域 $K$；原 $p=6k-1\ge41$、
$c,v,e,\delta$ 及所有原微分的规范不变。置
$$
Z:\quad x^6+y^6=1,\qquad b_0^3=c.
\tag{G4.14}
$$
$Z$ 指光滑射影平面曲线。映射
$$
\pi_y:Z\longrightarrow Y,\qquad
\eta=x,\quad y_Y=b_0y^2
\tag{G4.15}
$$
是实际 degree 二商，其 deck involution 是 $y\mapsto-y$。
这里 $x,y$ 是新曲线 $Z$ 的坐标，$y_Y$ 是 (G4.2) 中的原 $y$。
尤其没有把 $Z$ 认作 $X_0(108)$，也没有从同一个 CM 同源类型替代给定映射。

### 6.1. 全部十个正则微分及无共振 primitive

由平面六次曲线的 adjunction，$g(Z)=10$，完整基为
$$
\omega_{a,b}=x^{a-1}y^{b-6}\,dx,
\qquad a,b\ge1,\quad a+b\le5.
\tag{G4.16}
$$
也可在 $y=0$ 的六点及无穷点直接检查极阶。
用正整数 triple
$$
\alpha=(a,b,c_\alpha),\qquad c_\alpha=6-a-b
$$
记录完整 $\mu _6^2$ 字符；此处 $c_\alpha$ 与原曲线常数 $c$ 不同。
十个 triple 恰为 $(1,1,4)$ 的三种排列、$(1,2,3)$ 的六种排列，
以及 $(2,2,2)$。

每个微分都有如下**完整有理 primitive**：
$$
P_{a,b}
=y^{-bp}
\sum_{i=0}^{bk-1}
 \frac{(-1)^i\binom{bk-1}{i}}{a+6i}\,x^{a+6i},
\qquad dP_{a,b}=\omega_{a,b}.
\tag{G4.17}
$$
证明只用
$$
y^{b-6}=y^{-bp}(1-x^6)^{bk-1}.
$$
所有实际分母均为单位。确实，
$$
0<a+6i\le bp-c_\alpha<bp.
$$
若 $a+6i=rp$，则 $1\le r\le b-1$，而模六给 $a+r\equiv0$；
但 $0<a+r\le a+b-1\le4$，矛盾。
因此 (G4.17) 没有遗漏 $p$ 分母，也直接证明
$$
C(\omega_{a,b})=0
\quad\text{对全部十条基微分成立。}
\tag{G4.18}
$$

沿用 (G4.6) 定义
$$
\beta_Z(\omega_{a,b},\omega_{d,e_2})
=C_{\rm abs}(P_{a,b}\omega_{d,e_2}).
$$
这里第二个下标记 $e_2$，以免与原 Picard 系数 $e$ 混淆。
这个输出是正则微分：在任一点，第一输入有正则形式 primitive；
它与 (G4.17) 的局部差是 $p$ 次幂，乘第二输入后 Cartier 为零。
同理，有理 primitive 的选择不影响输出。
完整配对交替、对输入标量按 $p$ 次根半线性，并与可分拉回及自动同构相容。

### 6.2. 统一的完整张量公式

设
$$
\alpha=(a,b,c_\alpha),\qquad
\beta=(d,e_2,c_\beta)
$$
是上述十个 triple。若三个逐坐标和全部至多为五，置
$$
n=6-a-d,\quad q=6-b-e_2,\quad
M=nk-1,
$$
并定义
$$
\mathcal B_{\alpha,\beta}
=(-1)^M
\sum_{\substack{i+j=M\\0\le i\le bk-1\\0\le j\le e_2k-1}}
\frac{\binom{bk-1}{i}\binom{e_2k-1}{j}}{a+6i}.
$$
则完整公式是
$$
\boxed{
\beta_Z(\omega_{a,b},\omega_{d,e_2})
=
\begin{cases}
\mathcal B_{\alpha,\beta}\,\omega_{n,q},
&
a+d,\ b+e_2,\ c_\alpha+c_\beta\le5,\\
0,&\text{否则}.
\end{cases}}
\tag{G4.19}
$$
所有 $\mathcal B_{\alpha,\beta}$ 都在 $\mathbf F_p$，因而同一
$\mathbf F_p$ 模型的 relative Cartier 公式只把输出改写为
$\mathcal B_{\alpha,\beta}\omega'_{n,q}$；不另对这些有限和取 $p$ 次根。

为逐项验证，(G4.17) 乘第二微分给
$$
y^{-(b+e_2)p}
\sum_{i,j}
 \frac{(-1)^{i+j}\binom{bk-1}{i}\binom{e_2k-1}{j}}{a+6i}
 x^{a+d-1+6(i+j)}\,dx.
$$
分子最高次数是
$(b+e_2)p-1-(c_\alpha+c_\beta)$，严格小于 $(b+e_2)p-1$。
在允许的三组坐标和下，唯一可读 Cartier 指数是 $np-1$：
模六迫 $n=6-a-d$，并且 $1\le n\le b+e_2-1$。
相应条件正是 $i+j=nk-1=M$，输出即
$x^{n-1}y^{-(b+e_2)}dx=\omega_{n,q}$。
这证明非零分支的全部符号和尺度。

其余情形用**完整正则目标**排除，而不省略有理式的其它项。
Cartier 的半线性使输出 triple 是两个输入 triple 之和的负数，模六计算。
若某个坐标和等于六，输出有零字符；若某个和大于六，
三个最小正剩余数之和为十二。两种情形都不在 (G4.16) 的完整基中。
反过来，三个和均小于六时，输出 triple
$$
(6-a-d,\ 6-b-e_2,\ 6-c_\alpha-c_\beta)
$$
为正且总和六。这也验证 (G4.19) 的零分支。

交替号还能在原有限和中独立核对：对 $i+j=M$，
$$
(a+6i)+(d+6j)=np=0\quad\text{于 }K,
$$
所以交换两个输入后的两项 reciprocal 分母之和为零。
(G4.19) 因而给出了全部 $45$ 个无序槽的统一来源，
没有只保留三个 genus 4 子空间各自的内部配对。

### 6.3. 原 $e$ 的准确槽及其全十维 radical 判据

由 (G4.4)、(G4.15) 和 $b_0^3=c$，拉回的原微分准确为
$$
(h,\nu,u)=-b_0(\omega_{2,2},\omega_{1,2},\omega_{3,2}),
\qquad
\frac{d\eta}{y_Y}=b_0^{-1}\omega_{1,4}.
\tag{G4.20}
$$
令 $\mathcal B_{22,12}$ 表示 (G4.19) 中
$\beta_Z(\omega_{2,2},\omega_{1,2})$ 的 $\omega_{3,2}$ 系数。
可分拉回、(G4.10) 和 absolute 半线性给
$$
b_0^{2/p}\mathcal B_{22,12}
=\frac{e b_0}{\delta}.
$$
取 $p$ 次方，使用 $\mathcal B_{22,12},\delta\in\mathbf F_p$、
$e^p=-e$，得到
$$
\boxed{
\mathcal B_{22,12}
=-b_0^{p-2}\frac e\delta
=-c^{\,2k-1}\frac e\delta.
}
\tag{G4.21}
$$
$p-2=3(2k-1)$ 付掉 $b_0$ 的选择。又 $c^p=-c$，
所以右端确实在 $\mathbf F_p$。该式保留了原 absolute 负号；
它不是只在非零性上认同两个未归一的系数。

在射影 Fermat 方程中，先把第三坐标乘一个固定的六次根，
可把 $X^6+Y^6-Z^6=0$ 写成三项同号。
三坐标排列于是给实际的正规化 monomial 自动同构。
它们按非零标量排列 (G4.16) 的 triple，固定
$K\omega_{2,2}$，并在六个 $(1,2,3)$ 字符间传递。
这些自动同构与 absolute Cartier 相容；可能的六次根相位均为单位，
本段只运输准确的零性，不把它们默认为同一标量。

由 (G4.19)，$\omega_{2,2}$ 与三条 $(1,1,4)$ 微分的槽全为零，
与自身的槽也为零；仅余六个 $(1,2,3)$ 槽。
它们由上述实际排列构成一轨。因此 (G4.21) 给
$$
\boxed{
e=0
\quad\Longleftrightarrow\quad
\beta_Z(\omega_{2,2},\tau)=0
\quad\text{对每个 }\tau\in H^0(Z,\Omega_Z^1).
}
\tag{G4.22}
$$
也就是说，原 $e$ 消失恰使同一公共椭圆方向
$\omega_{2,2}$ 落入这个**全局十维配对**的 radical。
反向只需读取已归一的单个槽 (G4.21)，没有使用泛非退化断言。

### 6.4. 三个真实 genus 4 商及仍保留的 cross 槽

两个 sign involution $x\mapsto-x$、$y\mapsto-y$ 生成实际 $V_4$。
其共同商是 $X=x^2,Y=y^2$ 的 Fermat 三次曲线 $X^3+Y^3=1$。
$V_4$ 的平凡字符在 (G4.16) 中恰为 $\omega_{2,2}$。
三个非平凡字符各有三维；故完整空间的实际维数分解为
$$
H^0(Z,\Omega_Z^1)
=K\omega_{2,2}\oplus W_1\oplus W_2\oplus W_3,
\qquad \dim W_i=3.
\tag{G4.23}
$$
每个阶二子群的不变空间是公共一维加上其中一个三维空间。
对 $y$-sign，其完整四基正是 (G4.20)；另两商由已说明的
正规化坐标排列得到，几何上与同一个 $Y$ 同构。
因此 $e=0$ 时，(G4.1) 确实使三个四维子空间内部的配对全零。
这里的总维数是 $1+3(4-1)=10$，不是十二。

这些已付等式尚未证明整个 $\beta_Z$ 为零。
为精确显示留下哪些槽，以下只记录 triple 类型与字符允许的无序槽数；
具体值始终由 (G4.19) 给出：

| 输入类型 | 额外位置条件 | 输出类型 | 允许槽数 |
|---|---|---|---:|
| $222$ 与 $123$ | 无 | $123$ | $6$ |
| $114$ 与不同的 $114$ | 两个 $4$ 在不同坐标 | $114$ | $3$ |
| $114$ 与 $123$ | $4$ 所在坐标与 $1$ 相遇 | $123$ | $6$ |
| 两个不同的 $123$ | 同一坐标为 $1$ | $114$ | $3$ |
| 两个不同的 $123$ | 同一坐标为 $2$ | $222$ | $3$ |
| 两个不同的 $123$ | 相对排列为三循环 | $123$ | $6$ |

其余十八个无序槽由字符为零。
$e=0$ 杀掉表中第一行，并由三个原 genus 4 商杀掉第五行；
其它四行的十八个 cross 槽没有在本节被宣布消失。
本节也没有由 radical 的存在推出矛盾、由向量丛 perfectness 推出
指定 middle Jordan 向量 cyclic，或由此得到原 $e,K_4$ 不能同时为零。
后继必须在这些完整 cross 项与原短两系数之间另付实际关系。

本节来源全为 (G4.2)、(G4.6)、(G4.10) 的同一函数域计算、
平面曲线的正则微分及完整 Cartier 指数读取。
o1_theta 逐式纸推；未执行数学程序或新增素数窗口。


## 7. 同一 Fermat 源的安全高插入与原 $K_4$

本节继续用 (G4.17) 中的同一个
$$
P=P_{2,2},\qquad dP=\omega_{2,2}.
$$
$r\ge2$ 时，$C(P^r\tau)$ 一般是亚纯微分。
下面先支付全部低插入消失时的正则性，才使用十维字符表。
这一步同时保留 primitive 的 $p$ 次幂平移，避免把高插入当作
(G4.19) 的普通全纯槽。

### 7.1. 逐层正则性及 primitive 平移

对任意正则 Cartier-exact 微分 $\tau$，定义有理微分
$$
\mathcal C_r(\tau)=C_{\rm abs}(P^r\tau)\qquad(r\ge0).
$$
在任一点的完备局部域中，可以写
$P=L^p+R$，其中 $R$ 是 $dP$ 的正则形式 primitive。
若 $0\le j<r$ 时 $\mathcal C_j(\tau)=0$，逐次展开二项式便给
$C(R^j\tau)=0$ 对所有这些 $j$ 成立。因此
$$
\boxed{\quad
\mathcal C_j(\tau)=0\ (0\le j<r)
\quad\Longrightarrow\quad
\mathcal C_r(\tau)=C(R^r\tau)\text{ 在每点正则}.
\quad}
\tag{G4.24}
$$
同一展开表明，在这些低项全零的前提下，把全局
$P$ 换成 $P+L_0^p$ 不改变 $\mathcal C_r(\tau)$。
本节只用 $r\le4<p$，没有超出有限二项式范围。

令 $V_{123}$ 为六条 $(1,2,3)$ 字符线之和。
$P$ 的字符正是 $(2,2,2)$；这由其显示式直接成立，
不只是对 $dP$ 成立。
若 $e=0$，(G4.22) 给 $\mathcal C_1=0$ 于全部十维空间，
而 $\mathcal C_0=0$ 已由 (G4.18) 证明。
对 $\tau\in V_{123}$，(G4.24) 先使 $\mathcal C_2(\tau)$ 全纯。
其输出 triple 是 $-(\alpha+(4,4,4))\bmod6$，其中有一个零坐标，
故全纯目标无此字符。再应用 (G4.24)，
$\mathcal C_3(\tau)$ 全纯，而其最小正 triple 是 $-\alpha$，
总和十二，仍不在正则基中。于是
$$
\boxed{\quad e=0\ \Longrightarrow\
\mathcal C_j(V_{123})=0\quad(0\le j\le3),\qquad
\mathcal C_4(V_{123})\subset H^0(Z,\Omega_Z^1).
\quad}
\tag{G4.25}
$$
第四层的输出 triple 是 $\alpha$ 的 $1,3$ 两坐标互换，
并非字符强迫的零。

### 7.2. 与原第四阶 Picard 系数的全部尺度

由 (G4.20)，在同一函数域中
$$
P=-\frac{\Psi}{b_0\delta}+L_0^p.
$$
在 $e=0$ 下，(G4.25) 及上面的三角展开允许去掉此 $p$ 次平移，
同时也证明原 $\Psi$ 的第零至第三插入在这些方向全零。
消费 R1061 §19 的完整第四阶相对 Cartier 公式，在 $e=0$ 后准确为
$$
C_{\rm rel}(F_Q\Psi^4\omega)=4\delta^2K_4\,\omega'.
$$
它是先保全部 $e$ 项和第三类项后得到的专化。
由 $\nu=\eta^pF_Qh$，换成 absolute Cartier 给
$$
C_{\rm abs}(\Psi^4\nu)
=4\delta^2K_4^{1/p}u.
$$
这里先显写 $p$ 次根，避免把 relative 底域线性误用于 absolute 缩放。
因为 $\omega_{1,2}=-\nu/b_0$，
$$
C_{\rm abs}(P^4\omega_{1,2})
=4b_0^{\,1-5/p}\delta^{-2}K_4^{1/p}\omega_{3,2}.
$$
左边在 $\mathbf F_p$ 模型上读取，其系数属于 $\mathbf F_p$。
对该系数取 $p$ 次方，并用
$b_0^{p-5}=c^{2k-2}$、$\delta^p=\delta$，得到
$$
\boxed{\quad
e=0\ \Longrightarrow\
\mathcal C_4(\omega_{1,2})
=\frac{4c^{\,2k-2}}{\delta^2}K_4\,\omega_{3,2}.
\quad}
\tag{G4.26}
$$
这个单位尺度与 (G4.21) 的一次插入在同一 $P$、同一 Fermat 标架下。
没有把 $K_4$ 换成 normal 旁列或另一 theta 方向。

正规化坐标排列使 $P$ 变为一个单位倍的 $P$ 加 $p$ 次幂。
在 (G4.25) 的前提下，此平移不改变第四层零性。
因此完整的六个第四层槽仍构成同一个实际轨道。
又 $\mathcal C_j(\omega_{2,2})=0$ 对 $j\le4$，
因为 $P^jdP=d(P^{j+1}/(j+1))$。故
$$
\boxed{\quad
e=K_4=0
\ \Longleftrightarrow\
C(P^j\tau)=0\quad
\left(\tau\in K\omega_{2,2}\oplus V_{123},\ 0\le j\le4\right).
\quad}
\tag{G4.27}
$$
反向读取 $j=1$ 的 (G4.21) 后，再读 $j=4$ 的 (G4.26)。
这是一条同原两系数严格等价的七维高插入条件，不是非同时零证明。

### 7.3. 第四插入的两个真实 Cartier 指数

为保留高极处的完整消去，置
$$
n=2k-1,\quad t=x^6,\quad
\mathsf R(t)=
\sum_{i=0}^{n}
 \frac{(-1)^i\binom ni}{2+6i}t^i,
\qquad
P=x^2y^{-2p}\mathsf R(t).
\tag{G4.28}
$$
(G4.17) 已支付这些全部分母的单位性。
一次插入的原槽也可写成
$$
[t^{3k-1}]\mathsf R(t)(1-t)^n
=\mathcal B_{22,12}
=-c^{2k-1}e/\delta.
$$
这给后继有限系数比较的同一首列。

第四插入的完整有理源是
$$
P^4\omega_{1,2}
=x^8y^{-10p}\mathsf R(t)^4(1-t)^n\,dx.
$$
分子的最大 $x$ 指数为 $10p-12$。
Cartier 条件 $8+6j=rp-1$ 迫 $r\equiv3\bmod6$；
在这个完整极界内只有 $r=3,9$。令
$$
A_3=[t^{3k-2}]\mathsf R(t)^4(1-t)^n,\qquad
A_9=[t^{9k-3}]\mathsf R(t)^4(1-t)^n.
$$
两个指数及输出的分母都保留后，准确得到
$$
\boxed{\quad
\mathcal C_4(\omega_{1,2})
=\frac{A_3+A_9t}{1-t}\,\omega_{3,2}.
\quad}
\tag{G4.29}
$$
所有 $A_i$ 在 $\mathbf F_p$，所以这里的显示系数没有遗漏根号或
另一相对 Frobenius 标量。

这个输出可能的极仅在 $y=0$ 的六点。
在那里 $\omega_{3,2}$ 有一阶零，$(1-t)^{-1}=y^{-6}$，
故未消去时极阶至多五。
其它有限点以及无穷点均正则。
在 $e=0$ 下，(G4.25) 已独立证明整个输出全纯，
因此它恰迫
$$
A_9=-A_3.
$$
再与 (G4.26) 比较，
$$
\boxed{\quad
e=0\ \Longrightarrow\
A_9=-A_3,\qquad
A_3=\frac{4c^{2k-2}}{\delta^2}K_4.
\quad}
\tag{G4.30}
$$
因此在 $e=0$ 的前提下，$K_4=0$ 恰等价于这两个完整读取同时为零。
本证明不是先删除 $9p-1$ 的高项再计算 $3p-1$，而是从原低层消失
证明全纯性后，强迫这两个真实项的极部相消。

### 7.4. 三个 $114$ 方向的第二层及其高极边界

对三个 $(1,1,4)$ 方向，一次插入总由 (G4.19) 为零，
不需假设 $e=0$。所以 (G4.24) 给它们的第二层全纯。
其输出 triple 正好回到自身的字符线。
例如对 $\omega_{1,1}$，完整读取仅有 $p-1$ 一个指数：
$$
P^2\omega_{1,1}
=x^4y^{-5p}\mathsf R(t)^2(1-t)^{k-1}\,dx.
$$
分子次数为 $5p-9$，模六条件迫 $r\equiv1$，
故 $1\le r\le4$ 中只有 $r=1$。
因此
$$
\boxed{\quad
\mathcal C_2(\omega_{1,1})=\Lambda_p\omega_{1,1},\qquad
\Lambda_p=[t^{k-1}]\mathsf R(t)^2(1-t)^{k-1}
=\frac14[t^{k-1}](1-t)^{k-1}
 {}_2F_1(1/3,2/3;4/3;t)^2 .
\quad}
\tag{G4.31}
$$
最后一式仅使用次数至 $k-1$ 的安全前缀：
$\mathsf R(t)=\frac12\,{}_2F_1(1/3,2/3;4/3;t)\bmod t^k$，
其分母 $3i+1$ 均小于 $p$。
没有在更高共振次数延用一个未付的无限级数。
另两个 $114$ 槽由实际坐标排列运输；这里只对这个固定槽给出精确系数，
不把不同标架的单位相位强行设为一。

本节未证明 $\Lambda_p$ 非零。
若它不为零，第三、第四插入的局部二项展开分别仍含
$3L\,C(R^2\tau)$、$6L^2C(R^2\tau)+4L C(R^3\tau)$ 等亚纯项。
所以不能对这三个方向直接以十维全纯字符表删掉高插入。
同样，(G4.27) 并没有消去 §6.4 留下的十八个 cross 槽。
后继仍须把这些完整有限和、Leibniz 关系或有界 primitive
接到原两读数，不能用一般配对非退化性代替指定非同时零。

本节为同一原源的纸面推导；o2_high_coefficient 已独立核准
(G4.26) 的全部 absolute / relative 缩放。无数学程序执行。


## 8. 完整交换补偿、全部高极系数与原 Dixon 两读数

本节沿用 (G4.28) 的同一个 $\mathsf R$，不改变 $P$ 的规范。
记 $n=2k-1$，并置
$$
r_1=\mathsf R(1),\qquad
E_1=[t^{3k-1}]\mathsf R(t)(1-t)^n.
$$
由 (G4.21)，$E_1=-c^{2k-1}e/\delta$。
以下身份不先假设 $e=0$；第四层的极部与低插入补偿因此全部保留。

### 8.1. 原 primitive 的完整交换 cocycle

系数反转直接给
$$
\mathsf R(t)=t^n\mathsf R(1/t),\qquad
6t\mathsf R'(t)+2\mathsf R(t)=(1-t)^n.
\tag{G4.32}
$$
第一式中，$n$ 为奇数，而
$2+6(n-i)\equiv-(2+6i)\pmod p$，恰好消去分子反转的负号。
有限 Chu--Vandermonde 恒等式又给
$$
\boxed{\quad
r_1=\frac{n!}{2(4/3)_n}\in\mathbf F_p^\times.
\quad}
\tag{G4.33}
$$
这里 $(4/3)_n$ 模 $p$ 的各因子为
$2k+1,\ldots,4k-1$，全部是单位；$n!$ 同样如此。
也可先在有理数中对
$\frac12\,{}_2F_1(-n,1/3;4/3;1)$ 用终止求和再约化，
无共振分母被删除。

对 (G4.32) 乘上 $t^{2k}$，利用 $6k=p+1$，有
$$
\frac d{dt}\bigl(t^{2k}\mathsf R(t)\bigr)
=\frac16t^n(1-t)^n.
$$
因此下面左边导数恒零，次数至多 $4k-1<p$。
读取 $t=0$ 的常数便得准确多项式身份
$$
\boxed{\quad
t^{2k}\mathsf R(t)+(1-t)^{2k}\mathsf R(1-t)=r_1.
\quad}
\tag{G4.34}
$$
令 $\iota(x,y)=(y,x)$，这是同一个 Fermat 模型上的实际 involution。
由 $2p+2=12k$，(G4.34) 等价于
$$
\boxed{\quad
\iota^*P=-P+\left(\frac{r_1}{x^2y^2}\right)^p.
\quad}
\tag{G4.35}
$$
这支付了该坐标交换的完整 $p$ 次 primitive 补偿，
而不只是微分上的 $\iota^*\omega_{2,2}=-\omega_{2,2}$。

### 8.2. 六个高极点上的主部与两类输入

在 $y=0$ 的点取 $x=\xi$，其中 $\xi^6=1$。
用 $y$ 作局部参数，则
$$
x=\xi(1-y^6)^{1/6},\qquad
P=\left(\xi^{-2}r_1y^{-2}\right)^p+R_{\rm loc},
\qquad
R_{\rm loc}=-\frac{\xi^2}{2}y^2+O(y^8).
\tag{G4.36}
$$
确实，显示式中指数均为 $-2p+6j$。
因为 $dP$ 正则，负指数必须被 $p$ 整除；
在这个范围内仅有 $-2p$ 一项。
其系数为 $\xi^2r_1$，而
$(\xi^{-2})^p=\xi^2$。
最后的正则首项由
$\omega_{2,2}=-x^{-4}y\,dy$ 直接积分得到。
所以没有遗漏另一个低阶极部。

先取 $\tau=\omega_{1,2}$。第一层是 $E_1\omega_{3,2}$。
逐层保留 (G4.36) 的二项式展开，得到第二、第三层的最高极部。
另一方面，它们的完整 Cartier 多项式分别为
$$
\begin{aligned}
P^2\omega_{1,2}
 &=x^4y^{-6p}\mathsf R(t)^2(1-t)^n\,dx,\\
P^3\omega_{1,2}
 &=x^6y^{-8p}\mathsf R(t)^3(1-t)^n\,dx.
\end{aligned}
$$
前者分子最高次数为 $6p-8$，仅有 $p-1$ 指数；
后者最高次数为 $8p-10$，仅有 $5p-1$ 指数。
所以每层只有一个全局标量，最高极部已将它唯一确定：
$$
\boxed{\begin{aligned}
\mathcal C_2(\omega_{1,2})&=2r_1E_1\,y^{-6}\,dx,\\
\mathcal C_3(\omega_{1,2})&=3r_1^2E_1\,x^4y^{-8}\,dx,\\
A_3+A_9&=4r_1^3E_1.
\end{aligned}}
\tag{G4.37}
$$
末式使用 (G4.29) 的两个完整指数：
其 $y^{-5}dy$ 首系数由
$4L^3C(R_{\rm loc}\tau)$ 给出，其中
$L=\xi^{-2}r_1y^{-2}$。
其余局部项的极阶严格较低，因此不改变这个首系数。
这同时证明 $A_9=-A_3$ 的必要前提确为 $E_1=0$，
没有提前删除 $9p-1$ 项。

同样，对 $\tau=\omega_{1,1}$，
$\mathcal C_1(\tau)=0$、$\mathcal C_2(\tau)=\Lambda_p\tau$。
第三、第四层分别只有 $5p-1$、$3p-1$ 一个指数；
完整分子最高次数分别为 $7p-11$、$9p-13$。
最高局部极部遂给
$$
\boxed{\begin{aligned}
\mathcal C_3(\omega_{1,1})&=3r_1\Lambda_p\,x^4y^{-7}\,dx,\\
\mathcal C_4(\omega_{1,1})&=6r_1^2\Lambda_p\,x^2y^{-9}\,dx.
\end{aligned}}
\tag{G4.38}
$$
它们在 $y=0$ 分别可有二阶、四阶极。
所以即使 $e=0$，仍不能把这三条 $114$ 方向的高插入当作全纯字符槽。
本式未声称 $\Lambda_p$ 为零或为单位。

### 8.3. 两个高系数准确回到原短 Dixon 源

(G4.32) 还给两个有限多项式身份
$$
\begin{aligned}
\mathsf R(1-t)^n&=3t(\mathsf R^2)'+2\mathsf R^2,\\
\mathsf R^4(1-t)^n&=\frac65t(\mathsf R^5)'+2\mathsf R^5.
\end{aligned}
$$
结合 $\mathsf R$ 的互反性，读取
$3k-1$ 与 $9k-3$ 两个原指数，得到
$$
\boxed{\begin{aligned}
E_1&=\frac12[t^{k-1}]\mathsf R(t)^2,\\
A_9&=\frac15[t^{k-2}]\mathsf R(t)^5,\\
A_3&=4r_1^3E_1-\frac15[t^{k-2}]\mathsf R(t)^5.
\end{aligned}}
\tag{G4.39}
$$
例如第二式中的导数因子为
$(6(9k-3)+10)/5\equiv1/5$，
而 $\deg\mathsf R^5=10k-5$，
所以互反后的指数恰为 $k-2$。
这里 $p\ge41$，$2,3,5$ 均为单位。

为明确这不是另一个未识别的有限和，写
$$
F_D(t)={}_2F_1(1/3,2/3;4/3;t),\qquad N=k-1.
$$
只在所用次数至 $N$ 有
$\mathsf R=F_D/2$。
原 Dixon/Jordan 笔记 J.22--J.24 的同一 top-cyclic 多项式
$q_N(\lambda)$ 满足
$$
q_N(0)=\frac{3N+2}{2}[t^N]F_D^2,\qquad
q_N'(0)=-\frac{3N+2}{120}[t^{N-1}]F_D^5.
$$
由于 $3N+2=(p-1)/2\equiv-1/2$，(G4.39) 精确化为
$$
\boxed{\begin{aligned}
E_1&=-\frac12q_N(0),\\
A_9&=\frac32q_N'(0),\\
A_3&=-2r_1^3q_N(0)-\frac32q_N'(0).
\end{aligned}}
\tag{G4.40}
$$
所有超几何前缀及阶乘均处于原安全范围，
没有从高次无限级数移除一个 $p$-carry。
在 $e=0$ 下，(G4.40) 与 (G4.30) 读取的确是
同一个原 $K_4$，而不是另一个 normal 或邻列单位。

因此本节支付的是实际坐标交换、低层亚纯补偿与
两个原 Dixon 读数之间的全尺度比较。
$r_1$ 的单位性不能替代 $q_N(0)$ 或 $q_N'(0)$ 的非同时零；
§6 的十八个 cross 槽也没有因此被自动消掉。
本节为纸面代数证明，无数学程序执行。


## 9. 原 $114$ 第二插入的实际椭圆原函数与同一 Padé 多项式

本节给 (G4.31) 的同一个 $\Lambda_p$ 一个完整几何来源：
先由原 Fermat 六次曲线下降到一个实际 genus-two 商，
再由该商的第二条椭圆映射，读取一个极阶恰为 $p-2$ 的
唯一奇多项式原函数。其反序多项式与
[R1137 §2](../results/R1137-original-Lame-conjugation-with-complete-boundaries.md)
的同一个 $G_N,D_N$ 准确相接。这里没有另换原 $P=P_{2,2}$ 的
未定常数，也没有证明 $\Lambda_p$ 为单位。

### 9.1. 原 Fermat 曲线上的两个实际下降

继续 $Z:x^6+y^6=1$，令
$$
r=xy,\qquad W=2x^6-1.
$$
则得到实际映射
$$
Z\longrightarrow C_*:\quad W^2=1-4r^6,\qquad
\alpha=-\frac{dr}{W},\qquad h_*=r\alpha .
\tag{G4.41}
$$
这是一个光滑 genus-two 曲线。函数 $r,W$ 对
$(x,y)\mapsto(\xi x,\xi^{-1}y)$、$\xi^6=1$ 不变；
反过来 $x^6=(1+W)/2$、$y=r/x$，所以这是 degree-six 商。
在加入六次单位根后，该群的六个实际自同构也直接核准次数；
$6$ 与 $p$ 互素，映射可分。映射及显示模型本身都在 $\mathbf F_p$ 上。

直接对 $r=xy$ 求导，使用 $y^5dy=-x^5dx$，有
$$
dr=(y^6-x^6)\frac{dx}{y^5}=-W\frac{dx}{y^5}.
$$
因此 (G4.41) 的原微分没有未定尺度：
$$
\boxed{\quad
\alpha\longmapsto\omega_{1,1},\qquad
h_*\longmapsto\omega_{2,2}.
\quad}
\tag{G4.42}
$$
原 $P=x^2y^{-2p}\mathsf R(x^6)$ 也确实下降，其在 $C_*$ 上的函数为
$$
P=r^2\left(\frac{1-W}{2}\right)^{-2k}
       \mathsf R\left(\frac{1+W}{2}\right),\qquad dP=h_* .
$$
这里使用 $p+1=6k$，而不是只比较微分的字符。

第二条实际映射为
$$
\boxed{\quad
\pi_*:C_*\longrightarrow E_*:\ 
z=r^{-2},\quad w=Wr^{-3},\qquad
E_*:w^2=z^3-4,\qquad
\omega_*=\frac{dz}{2w},\quad
\pi_*^*\omega_*=\alpha .
\quad}
\tag{G4.43}
$$
这是一条 degree-two 可分映射；显示函数恒等式支付其在光滑完备模型上的
延拓。特别，下面使用的是这个已固定商的微分 $\omega_*$，
不是凭两条曲线同为 $j=0$ 便将它们的标架等同。

### 9.2. 极阶 $p-2$ 的唯一奇多项式原函数

令 $N=k-1$、$m=3k-1$，并在 $E_*$ 上以
$$
D_*=\omega_*^{-1}d,\qquad D_*z=2w,\quad D_*w=3z^2
$$
作导数。定义次数恰为 $N$ 的多项式
$$
A_N(T)=\sum_{j=0}^N a_jT^j,\qquad
a_N=-\frac12,\qquad
\frac{a_{j+1}}{a_j}=\frac{2j+1}{8(j+1)}
\quad(0\le j<N).
\tag{G4.44}
$$
所有分子、分母都是单位，所以每个 $a_j$ 非零。
递推的全部内容等价于
$$
3A_N+6(T-4)A_N'=T^N.
$$
确实，较低 $T^j$ 系数为
$(6j+3)a_j-24(j+1)a_{j+1}=0$；
最高项为 $(6N+3)a_N=(-2)(-1/2)=1$。
于是实际函数
$$
\boxed{\quad
H_*=wA_N(z^3),\qquad
D_*H_*=z^m,\qquad
dH_*=z^m\omega_*,\qquad
\operatorname{div}_\infty(H_*)=(p-2)O .
\quad}
\tag{G4.45}
$$
最后的极阶是 $3+6N=p-2$，最高系数非零。
在 $L((p-2)O)$ 内它是唯一的奇原函数：
两个解之差导数为零，故属于 $\mathbf F_p(E_*)^p$；
极阶小于 $p$ 又排除任何非恒定的 $p$ 次幂。
常数被 $w\mapsto-w$ 的奇性排除。这里底域是完美的 $\mathbf F_p$，
没有在非完美参数底域上擅取 $p$ 次根。

拉回 (G4.45)，有
$$
d(r^pH_*)=r^p z^m\alpha=r^{p-2m}\alpha=r\alpha=h_*.
$$
所以在 $\mathbf F_p(C_*)$ 中存在一个实际有理函数 $B_*$，使
$$
\boxed{\quad P-r^pH_*=B_*^p.\quad}
\tag{G4.46}
$$
这里 $r^pH_*$ 是拉回后的函数。差的导数为零，
而一变量光滑函数域的导数核正是其 $p$ 次幂子域，
故 (G4.46) 支付了完整 primitive 补偿，不只是一条局部导数身份。

### 9.3. 原 $\Lambda_p$ 的全部 Cartier 尺度与唯一指数

本小节先用绝对 Cartier；全部模型与显示多项式的系数在 $\mathbf F_p$，
因此最终标量亦在 $\mathbf F_p$。
§6 的精确字符表已给
$$
C(\alpha)=0,\qquad C(P\alpha)=0.
$$
它们可由 $Z$ 下降到 $C_*$，因为 Cartier 与可分拉回相容且拉回微分单射。
因此 (G4.46) 的二次 primitive 补偿准确相消：
$$
C(P^2\alpha)=C(r^{2p}H_*^2\alpha)
             =r^2\pi_*^*C(H_*^2\omega_*).
$$
左边正是 (G4.31) 的 $\Lambda_p\alpha$。
由于 $r^2=z^{-1}$，得到完整原式
$$
\boxed{\quad
C(H_*^2\omega_*)=\Lambda_p\,z\omega_*.
\quad}
\tag{G4.47}
$$
等价地，相对 Cartier 写作
$C_{\rm rel}(H_*^2\omega_*)=\Lambda_p\,z'\omega_*'$。
这里的 prime 是实际 Frobenius twist，不是求导；
并没有将扩域上的一般常数都按底域线性搬出绝对 Cartier。

还可独立核定 (G4.47) 的唯一系数。因为
$$
H_*^2\omega_*=
\left(\frac1{2w}\right)^p
 (z^3-4)^{m+1}A_N(z^3)^2\,dz,
$$
括号中的多项式关于 $z$ 的次数为
$3(m+1)+6N=15k-6<3p-1$，且所有指数均为三的倍数。
$p-1\not\equiv0\pmod3$、$2p-1=3(4k-1)$，
所以唯一合法 Cartier 指数是 $2p-1$。
常数 $\Lambda_p\in\mathbf F_p$ 的绝对 $p$ 次根仍是自身，准确给
$$
\boxed{\quad
\Lambda_p=[T^{4k-1}](T-4)^{3k}A_N(T)^2 .
\quad}
\tag{G4.48}
$$
这同时排除了一个未定的 $\omega_*$ 全纯补项。
$H_*^2\omega_*$ 的唯一极点也在 $O$，极阶为 $2p-4$；
所读 $z\omega_*$ 的二阶极与此完全一致。

### 9.4. 同一原 Padé 多项式的明确有限 functional

(G4.44) 直接给
$$
A_N(T)=a_0\sum_{j=0}^N
       \frac{(1/2)_j}{4^j j!}T^j,\qquad
\frac{a_{N-j}}{a_N}
=4^j\frac{(-N)_j}{(1/2-N)_j}.
$$
因而
$$
\boxed{\quad
A_N(T)=-\frac12T^N G_N(4/T),\qquad
G_N(x)={}_2F_1(1,-N;1/2-N;x)
       ={}_2F_1(1,5/6;4/3;x)\quad\bmod p .
\quad}
\tag{G4.49}
$$
两边都表示次数 $N$ 的同一个终止多项式。
所有下参数在 $0\le j\le N$ 均为单位。
右边恰是 R1137 (T47)、(T52) 中原 $S(-v^2x)/a_0$ 的
归一多项式；这里靠的是准确系数递推，未改动那个原 Padé 对。

在 (G4.48) 中反转最高次数
$3k+2N=5k-2$，剩余指数是 $N=k-1$。
由于 $3k\equiv1/2\pmod p$，仅在这个安全前缀读取二项式，得到
$$
\boxed{\begin{aligned}
\Lambda_p
 &=4^{N-1}[x^N](1-x)^{1/2}G_N(x)^2\\
 &=4^{N-1}[x^N](1-x)^{-1/2}D_N(x),
\end{aligned}}
\tag{G4.50}
$$
其中保持 R1137 (T52) 的完整首共振：
$$
(1-x)G_N^2=D_N-g_N^2x^{2N+1},\qquad
D_N=\sum_{j=0}^N\frac{2g_j}{3j+2}x^j .
$$
第二行只读 $x^N$，故首共振项在本次 coefficient 中不贡献；
它没有从整个多项式恒等式中被删除。
尤其可把同一标量明确写为
$$
\Lambda_p
=4^{N-1}\sum_{j=0}^N
 \frac{2g_j}{3j+2}\,
 \frac{(1/2)_{N-j}}{(N-j)!}.
\tag{G4.51}
$$
全部系数均已由原有限输入固定，但不能因为各因子为单位便断言其和为单位。

与 (G4.31) 合并还给一个带完整尺度的安全身份：
$$
[t^N](1-t)^N F_D(t)^2
=4^N[x^N](1-x)^{-1/2}D_N(x).
\tag{G4.52}
$$
这次新增比较支付的是原 $114$ 第二插入及 (G4.38) 的全部高极系数，
使它们可以在同一个实际椭圆原函数和原 Padé 范数多项式上消费。
它不把 $\Lambda_p$ 认作 $e$、$K_4$ 或某个已付 Hurwitz 单位，
也没有消去 §6 的十八个一阶 cross 配对。
即使假设原 $e=K_4=0$，R1137 (T54) 的有界 Pell 余式仍须保留；
(G4.50) 本身没有将其变成矛盾。本节为纯纸面证明，无数学程序执行。


## 10. 剩余 $114$ 交叉项的实际两椭圆来源与同一 $E_*$ 归约

本节只处理 §6 尚保留的三个 $114\times114$ 槽。
它们来自另一个明确的 genus 四中间商；本节不把这个商等同于原 $Y$，
也不把其配对系数认成原 $e$。
所有 $p=6k-1\ge41$、$N=k-1$、$m=3k-1$ 的规范继续不变。

### 10.1. 原 Fermat 曲线的实际 degree 三商

在 $Z$ 中置
$$
r=xy,\qquad a=x^3+y^3,\qquad b=x^3-y^3.
$$
它们给出光滑射影正规化
$$
\mathcal X:\quad
a^2=1+2r^3,\qquad b^2=1-2r^3,\qquad
W=ab=2x^6-1.
\tag{G4.53}
$$
$Z\to\mathcal X$ 是 $(x,y)\mapsto(\zeta x,\zeta^{-1}y)$ 的实际
degree 三商，其中 $\zeta^3=1$。
由 $x^3=(a+b)/2$、$y^3=(a-b)/2$ 和 $xy=r$，函数域的次数确为三。
非平凡 deck 元素在 Fermat 射影曲线上没有不动点：
其三个齐次特征值互异，而 Fermat 曲线不含坐标顶点。
所以 $g(\mathcal X)=4$。
这与 §9 的 degree 六商 $Z\to C_*$ 分开；
$\mathcal X\to C_*$ 由 $(a,b)\mapsto(-a,-b)$ 给出，次数为二。

两条实际椭圆商及其微分为
$$
E_+:\ a^2=1+2r^3,\quad \theta_+=\frac{dr}{a},
\qquad
E_-:\ b^2=1-2r^3,\quad \theta_-=\frac{dr}{b}.
$$
这里微分恰按显示式取值，不能另补或删除因子二。
由 (G4.42)，在 $\mathcal X$ 及其向 $Z$ 的拉回中有
$$
\alpha=\omega_{1,1}=-\frac{dr}{ab},\qquad
\omega_{4,1}=-\frac{\theta_++\theta_-}{2},\qquad
\omega_{1,4}=\frac{\theta_+-\theta_-}{2},\qquad
h_*=r\alpha=\omega_{2,2}.
\tag{G4.54}
$$
这四条微分组成 $\mathcal X$ 的完整正则微分基。
也可从 (G4.16) 直接读取：$\omega_{i,j}$ 中 $i-j\equiv0\bmod3$ 的四个字符
恰是这四条，故没有遗漏第五条微分。
所有拉回都是可分的，因此原 Cartier 和 $\beta$ 的读取可在此商上完成。

### 10.2. 两条完整椭圆 primitive 与原交叉系数

定义次数 $N$ 的多项式
$$
S_+(T)=\sum_{j=0}^N s_jT^j,\qquad
s_0=1,\qquad
\frac{s_j}{s_{j-1}}=-\frac{6j-1}{3j+1}.
$$
所有分子、分母在所用范围均为单位。
两条完整有理 primitive 是
$$
I_+=arS_+(r^3),\qquad
I_-=brS_+(-r^3),\qquad
dI_+=\theta_+,\quad dI_-=\theta_-.
\tag{G4.55}
$$
例如，对 $D_+=a\,d/dr$，
$$
D_+(arS_+(r^3))
=(1+5T)S_+(T)+3T(1+2T)S_+'(T)=1.
$$
次数 $1,\ldots,N$ 的项由递推消失；
最后次数 $N+1$ 的系数为 $(6N+5)s_N=ps_N=0$。
在 $T\mapsto-T$ 下，同一计算给负号模型的第二式。
所以这些是整个函数域中的 primitive，不只是低阶展开。

记原交叉系数为
$$
\beta_Z(\omega_{4,1},\omega_{1,4})=\sigma_p\omega_{1,1}.
$$
(G4.54)、交替性和 (G4.55) 给
$$
\beta(\theta_+,\theta_-)
=C\left(r(1+2r^3)S_+(r^3)\frac{dr}{W}\right),
$$

$$
\boxed{\quad
\sigma_p=-\frac12\,\mathcal L_p,\qquad
\mathcal L_p=[r^{p-1}]\,
r(1+2r^3)S_+(r^3)(1-4r^6)^m .
\quad}
\tag{G4.56}
$$
此处 $\mathcal L_p$ 仅是本节的多项式系数，不是有限对数。
为核完整 Cartier 读取，先抽出 $W^{-p}$。
分子只有 $1\bmod3$ 次幂，最高次数为 $21k-5<4p-1$。
能被 Cartier 读取的指数 $jp-1$ 必有 $j\equiv1\bmod3$；
所以唯一可能的指数就是 $p-1$。
输出为 $\mathcal L_p\,dr/W=-\mathcal L_p\alpha$；
再乘 (G4.54) 的 $1/2$ 即得 (G4.56)。
未省略第二个可能极点，也没有用同一个 $j$-不变量替代拉回尺度。
所有显示系数在 $\mathbf F_p$，相对版本仅将目标微分改成加撇号的微分。

其余两个 $114$ 槽可连同精确相位一起给出：
$$
\boxed{\quad
\beta(\omega_{1,4},\omega_{1,1})
=(-1)^k\sigma_p\,\omega_{4,1},\qquad
\beta(\omega_{1,1},\omega_{4,1})
=(-1)^k\sigma_p\,\omega_{1,4}.
\quad}
\tag{G4.57}
$$
首先 $(x,y)\mapsto(y,x)$ 把 $\omega_{a,b}$ 送到 $-\omega_{b,a}$，
故这两槽的系数相同。
再取 $\varepsilon^6=-1$，使用实际自动同构
$(x,y)\mapsto(x^{-1},\varepsilon y/x)$。
它把 $\omega_{a,b}$ 送到
$\varepsilon^b\omega_{6-a-b,b}$。
absolute Cartier 的输入标量必须取 $p$ 次根，
所以所求第二系数是
$-\varepsilon^{\,1-5/p}\sigma_p=(-1)^k\sigma_p$：
因为 $\varepsilon^{12}=1$、$p^{-1}\equiv p\bmod12$，
且 $1-5p=6(1-5k)$。
这一步保留了扩域相位；最终系数下降到 $\mathbf F_p$。
由 (G4.19)，$h_*$ 与其它三基的槽全为零。
因此 $\mathcal X$ 的完整全局 $\beta$ 为零恰等于 $\sigma_p=0$；
这不是原 $Y$ 的 $e=0$ 判据。

### 10.3. 真正下降到 §9 的同一椭圆曲线

现在使用 (G4.43) 的同一映射
$$
z=r^{-2},\qquad w=Wr^{-3},\qquad
E_*:\ w^2=z^3-4,\qquad
\pi_*^*\omega_*=-dr/W.
$$
记复合映射 $\mathcal X\to C_*\to E_*$ 为 $\pi_{\mathcal X}$。
置 $A(T)=(1+2T)S_+(T)$，并约定 $s_{N+1}=0$。
对 $1\le j\le N+1$，包括最末项在内，
$$
A_j=s_j+2s_{j-1}=\frac{3s_{j-1}}{3j+1}.
$$
完整的 exact 项
$d(I_+I_-)=I_+\theta_-+I_-\theta_+$
使交叉 Cartier 输入可换成其反对称部分，而非只删一个多项式的偶项。
因此
$$
\beta(\theta_+,\theta_-)
=-\pi_{\mathcal X}^*
 \left(\sum_{\ell=0}^{\lfloor N/2\rfloor}
 A_{2\ell+1}\,
 C_{E_*}\!\left(z^{-3\ell-2}\omega_*\right)\right),
\qquad
A_{2\ell+1}=\frac{3s_{2\ell}}{6\ell+4}.
\tag{G4.58}
$$
这次两个源极点正是 $z=0,w=\pm2\sqrt{-1}$。
每个输入的极阶为 $3\ell+2<p$；
因 $\omega_*$ 在 $z=0$ 的展开只有 $z^{3j}dz$，
这些极点都无留数。
下面的 exact 归约将完整给出其 Cartier 输出，不遗留一个待定的全纯项。

令
$$
\Psi_*=wz\,R_*(z^3),\qquad
R_*(T)=\sum_{j=0}^N a_jT^j,\qquad
a_N=-1,\qquad
\frac{a_j}{a_{j-1}}=\frac{6j-1}{8(3j+1)}.
$$
对 $D_*=2w\,d/dz$ 有
$d\Psi_*=\delta_*\omega_*$，其中 $\delta_*=-8a_0$ 是单位。
同一规范下
$$
C_{E_*}(z\omega_*)=-\delta_*\omega_*.
$$
这里也可完全用有限系数验证符号：
Cartier 的系数为
$\binom{3N+2}{2N+1}(-4)^{N+1}$，
而
$\delta_*=8\,4^N(4/3)_N/(5/6)_N$。
模 $p=6N+5$，
$(5/6)_N=(-1)^NN!$，
$(4/3)_N=(3N+2)!/(2N+2)!$；
两系数之比恰为 $-1$。

对每个实际 $\ell$，全函数域中的 exact 微分是
$$
d(wz^{-3\ell-1})
=\left((1-6\ell)z^{-3\ell+1}
       +8(3\ell+1)z^{-3\ell-2}\right)\omega_*.
$$
先取 $\ell=0$，再逐项递推，得到完整相对 Cartier 式
$$
\boxed{\quad
C_{\rm rel}\!\left(z^{-3\ell-2}\omega_*\right)
=\frac{\delta_*}{8}\,
   4^{-\ell}\frac{(5/6)_\ell}{(4/3)_\ell}\,
   \omega_*'.
\quad}
\tag{G4.59}
$$
所有分母 $3\ell+1$ 均非零，底项正是
$d(w/z)=(z+8z^{-2})\omega_*$。
故这个递推同时支付全纯系数和全部极点，没有仅从局部主部猜常数。

代回 (G4.58)，并用
$s_{2\ell}=4^\ell(5/6)_{2\ell}/(4/3)_{2\ell}$ 及 duplication，
得到另一条原交叉系数的完全有限式：
$$
\boxed{\quad
\sigma_p=-\frac{3\delta_*}{64}
\sum_{\ell=0}^{\lfloor N/2\rfloor}
 \frac{(5/12)_\ell(11/12)_\ell(5/6)_\ell}
      {(7/6)_\ell(4/3)_\ell(5/3)_\ell}.
\quad}
\tag{G4.60}
$$
这就是上参数另有 $1$、与 $\ell!$ 抵消的 terminating balanced
$ {}_4F_3(1)$。
当 $p\equiv5\bmod12$ 时，上参数 $5/12$ 使它在 $N/2$ 终止；
当 $p\equiv11\bmod12$ 时，上参数 $11/12$ 使它在 $(N-1)/2$ 终止。
所用所有下参数与递推分母都是单位。
这里没有从逐项单位推出整个和非零。

(G4.48) 与 (G4.58)–(G4.60) 现在确实使用同一 $E_*$、同一
$\omega_*$ 及同一原 Fermat 商：
前者读取 $H_*^2\omega_*$ 的 $z'\omega_*'$ 系数，
后者读取所列两极微分的 $\omega_*'$ 系数。
这明确支付了剩余十八 cross 中的三个 $114\times114$ 槽，
但两个输入、两个输出系数并不相同。
本节未证明 $\sigma_p$ 或 $\Lambda_p$ 非零，
也未把它们等同于原 $e,K_4$，或由此排除 R1137 的双缺陷。
全部为实际函数域与有限 Cartier 指数的纸面计算，无数学程序执行。


## 11. 原 Cartier–Serre 三张量、有限循环律与 e/S 的完整标量

本节取 $K=\mathbf F_{p^2}$，只研究同一 $Z/K$。
这足以包含 $\mu _6$ 以及正规化坐标排列所需的十二次根；
原 $e,s,\delta$ 也在此域中。本文的 absolute Cartier 及下述连接
各对标量取一次 $p$ 次根，二者复合在 $K$ 上线性。
本节不把这一点推广成任意基域上未经扭曲的三线性断言。

### 11.1. 原 primitive 的全部主部与 Serre 对角型

记 $B_Z^1$ 为 exact 微分层。由 §6 的全 Cartier 零性，
$H^0(Z,B_Z^1)=H^0(Z,\Omega_Z^1)$。
exact 序列
$$
0\longrightarrow\mathcal O_Z
 \xrightarrow{F}\mathcal O_Z
 \xrightarrow{d}B_Z^1\longrightarrow0
$$
给一个对标量取 $p$ 次根的连接同构
$$
\mathfrak k:H^0(Z,\Omega_Z^1)\longrightarrow H^1(Z,\mathcal O_Z).
$$
这里使用 absolute Frobenius 的半线性写法；相对版本的右端带一次
Frobenius twist。其为同构，是因为常数上的 Frobenius 双射，
连接映射单射，而两端维数均为十。
固定 principal-parts 的 Čech 约定，使一个有理 primitive 的
$p$ 次根主部表示 $\mathfrak k$；若同时采用相反约定，
以下整个三张量只共同换一个负号。

对 (G4.17) 的同一个 $P_{a,b}$，置
$$
r_{a,b}=
\sum_{i=0}^{bk-1}\frac{(-1)^i\binom{bk-1}{i}}{a+6i}
=\frac{(bk-1)!}{a(1+a/6)_{bk-1}}
=\frac{(ak-1)!(bk-1)!}
 {6((a+b)k-1)!}\in\mathbf F_p^\times.
\tag{G4.61}
$$
中间等式是有限二项式积分恒等式；
末式只用 $1/6=k$ 于 $\mathbf F_p$。
所有指标小于 $p$，所以各因子都是单位。

这些 primitive 只在 $y=0$ 的六个点有极。
无穷点处其各项的阶为 $bp-a-6i\ge6-a-b>0$，
故没有遗漏无穷主部。
在 $x=\xi,\ \xi^6=1$ 处，以 $y$ 为参数，
$x=\xi(1-y^6)^{1/6}$，其 Laurent 指数均为 $-bp+6j$。
由于 $dP_{a,b}=\omega_{a,b}$ 正则，负指数必须被 $p$ 整除；
在 $0\le j<bp/6<p$ 的范围内，这只允许 $j=0$。
准确的唯一负项及其 $p$ 次根是
$$
(P_{a,b})_{\rm pp}=r_{a,b}\xi^a y^{-bp},
\qquad
L_{a,b}=r_{a,b}\xi^{-a}y^{-b}.
$$
又
$$
\omega_{d,e}=-x^{d-6}y^{e-1}\,dy.
$$
先按 $y$ 的阶、再对六个 $\xi$ 求和，得到完整 Serre 配对
$$
\boxed{\quad
\langle\mathfrak k(\omega_{a,b}),\omega_{d,e}\rangle_{\rm Serre}
=-6r_{a,b}\,\mathbf 1_{a=d,\ b=e}.
\quad}
\tag{G4.62}
$$
所以此型的非退化性来自实际六个主部及单位阶乘，
不是借某个未指定的极化重新选择标量。

定义同一全局三张量
$$
\mathscr T(\alpha,\beta,\gamma)=
\langle\mathfrak k(\beta_Z(\alpha,\beta)),\gamma\rangle_{\rm Serre}.
\tag{G4.63}
$$
它在 $K$ 上三线性，因为前两个输入的 $p^{-2}$ 半线性在
$\mathbf F_{p^2}$ 上为恒等。
它首先只已知在前两槽交替；以下真正证明剩余循环律，
不从 Serre perfectness 自动推断。

若 $\beta_Z(\omega_{a,b},\omega_{d,e})
=\mathcal B_{ab,de}\omega_{g,h}$，
则由 (G4.62)
$$
\mathscr T(\omega_{a,b},\omega_{d,e},\omega_{g,h})
=-6r_{g,h}\mathcal B_{ab,de}.
\tag{G4.64}
$$
若第三基向量不是这个实际输出，三张量为零。
因此一个非零候选三元组的三个 triple 必须逐坐标相加为
$(6,6,6)$。

### 11.2. 所用变换是有限多项式恒等式

以下全部 $ {}_3F_2(1)$ 均在一个显示的非正整数上参数处终止。
使用恒等式
$$
\boxed{
 {}_3F_2\!\left(\begin{matrix}-d,a,b\\ c,f\end{matrix};1\right)
 =
 \frac{(c-a)_d}{(c)_d}
 {}_3F_2\!\left(\begin{matrix}-d,a,f-b\\
                 1+a-c-d,f\end{matrix};1\right).
}
\tag{G4.65}
$$
这是有限恒等式，并不引用非终止 Thomae 变换。
自足证明如下：在多项式环中，
$$
 {}_2F_1(-d,a;c;t)=
 \frac{(c-a)_d}{(c)_d}
 {}_2F_1(-d,a;1+a-c-d;1-t).
$$
其在 $t=1$ 的每个导数由有限 Vandermonde 和逐项核准。
再作用有限线性泛函
$t^j\mapsto(b)_j/(f)_j$；
对 $(1-t)^j$，同一 Vandermonde 恒等式给
$(f-b)_j/(f)_j$，即得 (G4.65)。
因此只有所显示的有限分母需要核对，尾项或解析收敛没有参与。

### 11.3. 剩余十五槽中的九槽：同一个有限和

设 $N=k-1$、$C_N=\binom{2N+1}{N}$，并记
$$
A=\mathcal B_{41,12},\qquad B=\mathcal B_{12,13}.
$$
直接在 (G4.19) 中分别使用原范围 $0\le i\le N$
以及换元 $i=k+j$，得到
$$
\begin{aligned}
A&=\frac{(-1)^NC_N}{4}
 {}_3F_2\!\left(\begin{matrix}-N,-N,2/3\\
                      N+2,5/3\end{matrix};1\right),\\
B&=-\frac{C_N}{2}
 {}_3F_2\!\left(\begin{matrix}-N,-3N-2,1/3\\
                      N+2,4/3\end{matrix};1\right).
\end{aligned}
\tag{G4.66}
$$
对第一式在 (G4.65) 中取 $c=5/3,f=N+2$；
对第二式取 $c=4/3,f=N+2$。
由于 $p=6N+5$，两者变换后的有限和都是
$$
J_N={}_3F_2\!\left(\begin{matrix}-N,-N,1/2\\
                         1,N+2\end{matrix};1\right).
$$
两个前因子的分子也都化为 $(5/6)_N=(-N)_N$。
显示的所有下参数、前因子和 $C_N$ 均是单位；
此处没有将 $J_N$ 宣布为单位，也没有除以它。
逐前因子比较给
$$
A=\frac{(-1)^{N+1}}2
       \frac{(4/3)_N}{(5/3)_N}\,B.
$$
而 (G4.61) 与 Wilson 直接给
$$
\frac{r_{4,1}}{r_{1,3}}
=\frac{((4k-1)!)^2}{(5k-1)!(3k-1)!}
=\frac{(-1)^{N+1}}2
       \frac{(4/3)_N}{(5/3)_N}.
$$
这里可逐项使用
$(4N+3)!(2N+1)!=1$、
$((3N+2)!)^2=(-1)^{N+1}$，没有 Legendre-symbol
或未指定平方根的余相位。于是准确有
$$
\boxed{\quad r_{1,3}\mathcal B_{41,12}
       =r_{4,1}\mathcal B_{12,13}.\quad}
\tag{G4.67}
$$
这是同一原三元组 $(\omega_{41},\omega_{12},\omega_{13})$
的真实循环律。
实际三坐标排列将它运输到全部六个 $114\times123$ 槽和
三个共享 $1$ 的 $123\times123$ 槽；
这九槽现在由同一参数及准确单位决定，而不是九个自由值。

### 11.4. 公共椭圆方向的循环律与原 e 的数值桥

设
$$
n=2k-1,\qquad
E=\mathcal B_{22,12},\qquad B_0=\mathcal B_{12,32},
\qquad C=\binom n{k-1}.
$$
(G4.19) 的同一原有限范围给
$$
\begin{aligned}
E&=\frac{(-1)^{k-1}C}{3}
 {}_3F_2\!\left(\begin{matrix}1-k,-n,1/2\\
                         k+1,3/2\end{matrix};1\right),\\
B_0&=-{}_3F_2\!\left(\begin{matrix}-n,-n,k\\
                         1,k+1\end{matrix};1\right).
\end{aligned}
\tag{G4.68}
$$
第一式的换元是 $i=k+j$；原分母
$2+6(k+j)$ 在特征 $p$ 中准确为 $3+6j$，
所以系数是 $1/3$。

对第二式在 (G4.65) 中使用终止指数 $d=n$，
$a=-n,b=k,c=k+1,f=1$。
新上参数 $1-k=-(k-1)$ 在整数中已经使长和截短；
新下参数 $2-5k$ 模 $p$ 为 $k+1$。
对第一式使用 $d=k-1,a=-n,b=1/2,c=3/2,f=k+1$。
新下参数 $3/2-3k$ 模 $p$ 为 $1$，
新上参数 $k+1/2$ 模 $p$ 为 $-n$。
两者于是都化为同一个
$$
J={}_3F_2\!\left(\begin{matrix}1-k,-n,-n\\
                         1,k+1\end{matrix};1\right),
$$
其两个前因子分别为
$$
P_H=\frac{(3k)_n}{(k+1)_n},\qquad
P_E=\frac{(n+3/2)_{k-1}}{(3/2)_{k-1}}.
$$
变换前后所有下参数直到原有限上界均非零；
特别 $n+3/2$ 的所需因子模 $p$ 正是
$-(k-1),\ldots,-1$。
因此两个前因子皆单位，但仍不除以 $J$。

Wilson 逐项消去前因子给
$$
-\frac{3(-1)^{k-1}}{C}\frac{P_H}{P_E}
=\frac{(3k-1)!(4k-1)!}{(5k-1)!(2k-1)!}
=\frac{r_{3,2}}{r_{2,2}}.
$$
例如完全约化只需
$(5k-2)!k!=(-1)^{k-1}$、
$(5k-1)!(k-1)!=(-1)^k$、
$((3k-1)!)^2=(-1)^k$。
于是，不论共同和是否为零，都有
$$
\boxed{\quad r_{3,2}\mathcal B_{22,12}
        =r_{2,2}\mathcal B_{12,32}.\quad}
\tag{G4.69}
$$

现在严格接回原 $S=S_n$。
(G4.11)、(G4.20) 与 absolute Cartier 给
$$
\mathcal B_{22,12}=-c^n e/\delta,\qquad
\mathcal B_{12,32}=-c^n S/s.
$$
第二式也可直接由原非交替有限和
$H_n=2^nS_n$ 核准；这里 $c^n/s=2^n$。
为核这个相位，$\kappa^p=-\kappa$、$n$ 为奇数，故 $\kappa^n s\in\mathbf F_p$；由 $3n=p-2$、$s^3=-3s$、$\kappa=3s$，其立方恰为一。$\mathbf F_p$ 的立方映射双射，故 $\kappa^n=1/s$，即得所述 $c=2/\kappa$ 的身份。
代入 (G4.69)，得到先前 (G4.13) 的完整数值增强：
$$
\boxed{\quad
 e=\frac{\delta}{s}\,
 \frac{(2k-1)!(5k-1)!}{(3k-1)!(4k-1)!}\,S_n.
\quad}
\tag{G4.70}
$$
所有阶乘都是原素数下的单位。这个比值还能完全约简。
事实上
$$
\frac{r_{3,2}}{r_{2,2}}
=\frac{(3k-1)!(4k-1)!}{(2k-1)!(5k-1)!}
=\frac{(1/3)_k}{(2/3)_k}
=2^{1-2k}=\rho.
$$
给出无需另选立方根的有限证明：Wilson 先将中间阶乘比化为
$(-1)^k(3k-1)!(k-1)!/((2k-1)!)^2$。
再用 $3k-1=(p-1)/2=-1/2$ 于 $\mathbf F_p$，
在 $\binom{3k-1}{k-1}$ 上逐因子作半整数二项式展开，
得到该比值为
$-4^{1-k}(2k)/(2k-1)=2^{1-2k}$。
最后 $(2^{1-2k})^3=2^{2-p}=2$，
而 $\mathbf F_p$ 上立方映射双射，所以它就是原规范中的 $\rho$。

因此 (G4.70) 的标量正是
$$
\boxed{\qquad e=\frac{\delta}{\rho s}S_n,\qquad
 S_n=-9\rho^2 A_{\rm orig}.
\qquad}
\tag{G4.70a}
$$
这里 $A_{\rm orig}$ 仅指 (G4.11)–(G4.12) 及 R1126 的原有限和，
不是 (G4.66) 中暂记为 $A$ 的 mixed 槽。
第二式来自已付 $e=3\rho s\delta A_{\rm orig}$ 和 $s^2=-3$，
没有除以 $e,S_n$ 或 $A_{\rm orig}$。
它严格合并了 R1126 的 $A_{\rm orig},S_n$ 两个输入，
但没有把其非 CM 目标方向的 $T$ 和一并消去。

因为 $\rho,\delta,S_n$ 在 $\mathbf F_p$ 而 $s^p=-s$，
(G4.70)–(G4.70a) 准确满足 $e^p=-e$。
这里确实新付了标量；没有以零性等价冒充数值等式，
也没有因这个单位前因子就断言 $e$ 或 $S_n$ 非零。

### 11.5. 全十维三张量交替，仍保原指定缺口

逐坐标相加为 $(6,6,6)$ 的无序基三元组只有以下九组：

| 三元组类型 | 组数 | 循环来源 |
|---|---:|---|
| 三个不同的 $114$ | $1$ | 实际三坐标轮换 |
| $222$ 与共享 $2$ 的两个 $123$ | $3$ | (G4.69) 及实际排列 |
| $114$ 与在其 $4$ 位置共享 $1$ 的两个 $123$ | $3$ | (G4.67) 及实际排列 |
| 同一三循环中的三个 $123$ | $2$ | 实际三坐标轮换 |

这些三元组都由不同基向量组成。
其它三元组由字符使三张量为零；唯一字符允许的重复三元组是三个 $222$，其值由前两槽的交替性为零。
它们对应 §6.4 的全部二十七个可能非零配对槽。

为把排列的相位也付清，在齐次模型
$X^6+Y^6-Z^6=0$ 上取 $\epsilon^6=-1$。
例如 $(X,Y,Z)\mapsto(Y,\epsilon Z,\epsilon X)$
是实际 projective 阶三自动同构。
它的第三次幂是共同齐次标量，所以在每个三循环基轨道上，
三个乘子的积是 $1$，给出表中两类直接循环律。

对其它排列也不必猜测相位：
在 adjunction residue 基
$X^{a-1}Y^{b-1}Z^{c-1}\operatorname{Res}(\Omega/F)$ 中，
三个 triple 相加为 $(6,6,6)$ 时，
一个正规化坐标排列的三个基乘子之积准确为该排列的符号。
这由 $F\circ g=\lambda F$、
$g^*\Omega=(\det g)\Omega$ 和三个坐标的六次幂逐项相乘立即给出。
因此交换上表中后两个基向量的实际 transposition
恰补出交替的负号。
(G4.63) 对这些自动同构自然，且在 $\mathbf F_{p^2}$ 上三线性；
结合前两槽的交替性、(G4.67)、(G4.69)，得到
$$
\boxed{\quad
\mathscr T(\alpha,\beta,\gamma)
=\mathscr T(\beta,\gamma,\alpha),\qquad
\mathscr T\in\bigwedge\nolimits^3
          H^0(Z,\Omega_Z^1)^\vee.
\quad}
\tag{G4.71}
$$
这是在这个实际 Fermat 曲线上由全部有限槽和主部证明的结果；
本文没有声称一般 superspecial 曲线上的同名三张量自动交替。

(G4.62)、(G4.67)、(G4.69) 支付了原全十维配对与
Serre 对偶的真实相容性，并把原十八 cross 中剩余十五槽的九槽
接为同一个有限和；其余两个 $123$ 三循环仍保留实际系数。
(G4.70) 给原 $e/S_n$ 的精确单位比例。
这些结论没有证明共同 $ {}_3F_2$、$\sigma_p$、
$\Lambda_p$ 或两个三循环系数非零。
尤其一个三形式可以有 radical，
不能从 (G4.71) 或 Serre 型的非退化性推出原 $e,K_4$ 不同时为零。
全部为有限多项式恒等式、原主部及 Serre 留数的纸面证明，
未执行数学程序或新增素数窗口。
