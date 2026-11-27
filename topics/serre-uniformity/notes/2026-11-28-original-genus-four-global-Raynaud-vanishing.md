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
