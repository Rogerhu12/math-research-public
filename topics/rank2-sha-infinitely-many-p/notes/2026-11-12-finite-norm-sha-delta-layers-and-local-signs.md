# 有限范数一 Sha 的 δ 层、实际局部符号与 Heegner 指数

日期：2026-11-12。状态：本文的配对、层分解和符号公式均已证明。
本文件在工作环境重建后按已独立复核的完整论证恢复。

固定 $E:y^2=x^3-17x$、$F=\mathbf Q(\sqrt{-15})$。取此前构造的
真实辅助素数 $\ell$，$\ell+1=pu$、$p\nmid u$，以及环类域中
唯一的次数 $p$ 子扩张 $L/F$。记 $\Gamma=\langle\tau\rangle$，
$c\tau c=\tau^{-1}$，并令
$$
 A=\ker\bigl(\operatorname{Res}_{L/F}E\xrightarrow{N}E\bigr),
 \quad \mathcal O=\mathbf Z_p[\zeta_p],
 \quad \delta=\tau^{(p-1)/2}(\tau-1).
 \tag{1}
$$
$\delta$ 是 $\mathcal O$ 的一致化元，$\bar\delta=-\delta$。
R119 已对实际非零完整 Heegner 迹 $Q=Q_{p,\ell}$ 证明
$$
 A(F)\otimes\mathbf Z_p=\mathcal Oe,\qquad
 S:=\Sha(A/F)[p^\infty]\text{ 有限}.
 \tag{2}
$$
写 $Q=\delta^a ve$、$v\in\mathcal O^\times$。
R116 的实际不可 $p$ 除结论给 $0\le a\le p-2$。
R106 给 $cQ=-\tau^jQ$，其中 $j$ 依所选 Heegner 规范而定。
本文始终保留这个指定 $Q$，不以任意非零点代替它。

## 1. 平衡同源与一个对称的有限配对

R113 及其平衡同源补充构造了整同构
$\iota:A\longrightarrow A^\vee$，满足
$$
 \iota^\vee=-\iota,\qquad
 \delta^\vee\iota=-\iota\delta,\qquad
 c\iota c=-\iota.
 \tag{3}
$$
它来自范数一格上的限制极化除以平衡 $\delta$；这里使用已证
整同构，而非在 $\mathbf Q_p$ 上任意除一个同源。

将有限 Cassels--Tate 完美配对与 (3) 合成：
$$
 B(x,y)=\langle x,\iota y\rangle_{\rm CT},
 \qquad x,y\in S.
 \tag{4}
$$
Cassels--Tate 的反对称性、同源函子性及 (3) 给
$$
 B(y,x)=B(x,y),\qquad
 B(\delta x,y)=-B(x,\delta y),\qquad
 B(cx,cy)=-B(x,y).
 \tag{5}
$$
因此这是一个**对称**完美配对；不能把它误写成交替配对。
它的 $c$ 正、负部分彼此完美配对，每个符号部分自身等零。

## 2. 精确长度的原始商及非退化性

对 $n\ge1$ 定义
$$
 P_n=\frac{S[\delta^n]}
 {S[\delta^{n-1}]+\delta S[\delta^{n+1}]},
 \qquad
 \beta_n(x,y)=B(x,\delta^{n-1}y).
 \tag{6}
$$
这些商是 $\mathbf F_p$ 向量空间；$\beta_n$ 的值在
$p^{-1}\mathbf Z_p/\mathbf Z_p$。后一点是因为
$\delta^{n-1}y$ 被 $\delta$ 杀掉，而 $p$ 是
$\delta^{p-1}$ 乘一个 $\mathcal O$ 单位。

**良定义。** 第一变量加入 $S[\delta^{n-1}]$ 时，用 (5) 将
$\delta^{n-1}$ 移到第一变量，值为零。若加入 $\delta z$，
$z\in S[\delta^{n+1}]$，则
$$
 B(\delta z,\delta^{n-1}y)=-B(z,\delta^ny)=0.
$$
第二变量同理。

**非退化。** 完美性及 (5) 给
$(S[\delta^n])^\perp=\delta^nS$。
如果 $x\in S[\delta^n]$ 与全部 $y\in S[\delta^n]$ 的
$\beta_n$ 值为零，那么
$\delta^{n-1}x\in\delta^nS$。取 $z\in S$ 使
$\delta^{n-1}x=\delta^nz$，则
$x-\delta z\in S[\delta^{n-1}]$；再乘 $\delta^n$ 可得
$\delta^{n+1}z=0$。因此 $x$ 恰在 (6) 的分母中。

式 (5) 还给准确符号
$$
 \beta_n(y,x)=(-1)^{n-1}\beta_n(x,y),\qquad
 \beta_n(cx,cy)=(-1)^n\beta_n(x,y).
 \tag{7}
$$
所以：

- $n$ 奇数时，$\beta_n$ 对称且 $c$ 反等距，故
  $\dim P_n^+=\dim P_n^-$。
- $n$ 偶数时，$\beta_n$ 交替且 $c$ 等距；两个符号部分
  正交，各自有非退化交替配对，故其维数各为偶数。

一个 $\mathcal O/\delta^n$ 循环块恰对 $P_n$ 贡献一维。
其 $P_n$ 顶端与 $S[\delta]$ 的底端符号相差 $(-1)^{n-1}$。
因此如果
$$
                         S[\delta]^-=0,                     \tag{8}
$$
奇长度块全部消失：它们的顶端只能有正号，与奇数情形的
两符号等维矛盾。偶长度块的顶端全为负号，而 (7) 强迫每种
长度的块数为偶数。于是
$$
 S\simeq\bigoplus_{n\ge1}
              (\mathcal O/\delta^{2n})^{2m_n},\qquad m_n\ge0.
 \tag{9}
$$
特别地 $\operatorname{length}_{\mathcal O}S=v_p\#S$ 是 $4$ 的倍数。

## 3. 辅助位的两个对称双曲平面

令 $\lambda\mid\ell$ 为 $F$ 中唯一素位。
$\ell$ 在 $F$、$\mathbf Q(i)$ 都惰性，故 $a_\ell(E)=0$，
并在 $E[p]$ 上有
$\operatorname{Frob}_\ell^2=-\ell=1$。
因此
$$
 H=H^1(F_\lambda,E[p])=H_f\oplus H_{\rm tr},
 \qquad \dim H_f=\dim H_{\rm tr}=2.
 \tag{10}
$$
$H_f$ 是通常 Kummer 条件，$H_{\rm tr}$ 是由 $L_\lambda/F_\lambda$
给出的完整横截条件。两者互补、各为局部 Tate 配对的极大等零
子空间；这使用 R113 的全精度局部比较，不只是交为零。

该局部配对是**对称**的：一次上同调杯积的反号与 Weil 配对
的反号相抵。$c$ 保持它，故
$$
 H=H^+\perp H^-,\qquad \dim H^\pm=2.
 \tag{11}
$$
$H_f$ 上的 $c$ 作用是 $\operatorname{Frob}_\ell$，两个符号
各一维。$H_{\rm tr}$ 上还要乘惯性生成元被 $c$ 反转的负号，
所以其符号作用是 $-\operatorname{Frob}_\ell$。
每个 $H^\pm$ 都是由 $H_f^\pm,H_{\rm tr}^\pm$ 组成的
二维双曲平面。

因为 $p$ 为奇数，二维双曲平面中只有这两条等零直线。
具体地，配对矩阵可写为 $\bigl(\begin{smallmatrix}0&b\\b&0\end{smallmatrix}\bigr)$，
$b\ne0$，等零条件就是两个坐标的乘积为零。

## 4. 真正的全局 Selmer 维数公式

设 $\operatorname{Sel}_{\rm rel}$ 在 $\lambda$ 放宽条件，
其余位保留通常 Kummer 条件。Poitou--Tate 双对偶及通常条件的
自对偶性说明其局部像 $V\subset H$ 是自正交补，且 $c$ 稳定。
故 $V^\pm\subset H^\pm$ 各是一条等零直线。

记
$$
 s_\pm=\dim_{\mathbf F_p}\operatorname{Sel}_p(E/F)^\pm,
 \qquad
 r_\pm=\dim_{\mathbf F_p}
       \operatorname{loc}_\lambda\operatorname{Sel}_p(E/F)^\pm.
$$
则 $r_\pm\in\{0,1\}$，且 $V^\pm$ 只能是
$H_f^\pm$（$r_\pm=1$）或 $H_{\rm tr}^\pm$（$r_\pm=0$）。
将通常条件改成横截条件时，两种 Selmer 群的严格核相同。
因此 R113 的准确 $\delta$-Selmer 比较给
$$
 \dim\operatorname{Sel}_\delta(A/F)^\pm
                  =s_\pm+1-2r_\pm.
 \tag{12}
$$
这里没有预先假设基曲线的 Sha 有限。

有限局部比较本身不要求 $p$ 普通或在 $F$ 分裂：在 $p$ 处
$L/F$ 不分歧、$E$ 好约化，通常范数满射；其余坏位的组件阶
与充分大的 $p$ 互素。R125 的逐精度证明保持这些真实局部条件。
本文的对称配对与 $\lambda$ 处符号计算同样没有普通性输入。

## 5. Kummer 映射的反号与指定点的指数

由 $cQ=-\tau^jQ$、$c\delta c=-\delta$，将
$Q=\delta^ave$ 降到 $\mathcal O/\delta$ 得
$$
 c\text{ 在 }A(F)/\delta A(F)\text{ 上的符号为 }(-1)^{a+1}.
 \tag{13}
$$
然而该群进入 Selmer 群时还要反号。若 $\delta R=Q$，则
$-cR$ 是 $cQ$ 的一个 $\delta$-除点。因此
$$
 \kappa_\delta(cQ)=-c\kappa_\delta(Q).
 \tag{14}
$$
故实际 Mordell--Weil Kummer 线在
$\operatorname{Sel}_\delta(A/F)$ 中的符号是 $(-1)^a$。
不能把 (13) 直接当成该 Selmer 线的符号。

由 Kummer 正合列、(12)、(14)，令
$t_\pm=\dim S[\delta]^\pm$，有
$$
 t_\pm=s_\pm+1-2r_\pm-\mathbf1_{\{\pm=(-1)^a\}}.
 \tag{15}
$$
R103 已证明 $E^{(-15)}(\mathbf Q)$ 秩一且整个 Sha 有限；
删掉固定有限多个 $p$ 后，
$$
 s_-=1,\qquad s_+=2+d_p,\qquad
 d_p=\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p].
 \tag{16}
$$
此处 $d_p$ 允许包含未知的可除部分，并没有使用其有限性。

如果 $r_-=1$，(15) 的负号一侧迫使 $a$ 为偶数，否则维数为
$-1$。于是 $t_-=0$，可以应用 (8)--(9)，得到
$$
 \boxed{\quad a\equiv0\pmod2,\qquad
 S\simeq\bigoplus_{n\ge1}
       (\mathcal O/\delta^{2n})^{2m_n}.\quad}
 \tag{17}
$$
若再有 $r_+=1$，则
$$
 t_+=d_p,\qquad
 \operatorname{length}_{\mathcal O}S\ge2d_p,
 \qquad d_p\equiv0\pmod2.
 \tag{18}
$$
若 $r_+=0$，同样的公式是 $t_+=d_p+2$、
$\operatorname{length}_{\mathcal O}S\ge2d_p+4$。

作为实际充分条件，若已付 $r_-=1$ 且 $\#S<p^4$，则 (17)
迫使 $S=0$；(15) 进一步给 $r_+=1$、$d_p=0$。
本文并未证明这样的阶数上界。

## 6. 已支付的条件与仍未支付的原始性

R121 在原分裂输入集合的相对密度一子集上支付 $r_+=1$，
同时保留真实完整迹非零且不可 $p$ 除。只有这个条件时，
(15) 准确给出：

- $a$ 偶数：$t_+=d_p$、$t_-=2-2r_-$；
- $a$ 奇数：$t_+=d_p+1$、$t_-=1-2r_-$，所以必有 $r_-=0$。

新 R126 的大素因子选择进一步对无穷多个真实输入同时支付
$r_+=r_-=1$ 和 $\widehat h(Q)=o(p)$。
R125 的整 Kolyvagin 系统证明另外给
$$
 \operatorname{length}_{\mathcal O}S\le2a.
$$
合并 (18) 得 $d_p\le a$。这仍允许 $a=2$、$d_p=2$ 及
两个长度为 $2$ 的有限 Sha 块。有限性的已知输入、交替性和
两符号约束都没有自动把指定 $Q$ 的 $a$ 降为零。

## 来源和范围

- R103：固定负扭曲的严格解析秩一及 Gross--Zagier--Kolyvagin 输入。
- R106、R113：实际范数一同源、整平衡同构、全部局部条件及
  指定 Heegner 点的反循环符号；其已给完整证明和原始来源。
- R119：Nekovář（2007），*The Euler system method for CM points
  on Shimura curves*，Theorem 3.2、§3.5.1，
  [作者原文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)，
  支付 (2) 的有限性，包含 $p=\operatorname{ord}\chi$。
- 有限 Selmer 的局部 Tate 对称性及 Poitou--Tate 自正交补采用
  R111、R113 已核的准确通常/横截结构；§3--4 写出在本题中的
  全部维数和符号步骤。
- §2 是从有限完美配对直接推出的原始层证明，不借用一个未说明
  的半单性或 Jordan 长度公式。本文从未把普通 Cassels--Tate
  配对在 Mordell--Weil 像上的零值当成指定点的非零证书。
