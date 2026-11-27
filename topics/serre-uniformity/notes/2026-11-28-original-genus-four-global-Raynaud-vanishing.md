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
