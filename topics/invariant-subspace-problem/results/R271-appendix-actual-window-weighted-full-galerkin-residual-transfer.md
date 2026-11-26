# R271 附录：实际方差窗中未加权最小者的物理孔加权残余运输

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：下述完整加权差界已证明。** 本补充接
[联合 carry 的有限 Fock 乘子](R271-appendix-joint-carry-finite-fock-multiplier-and-exponential-strong-prefix-gram.md)。
它保原未加权正交最小者、同一 forcing 与同一个完整子空间；
在明确的原实际窗口内，支付其完整环境残余的真正物理孔权差。
此处不只比较加权候选，也不将 $S\to0$ 极限代替实际 $S_x$。

## 1. 同一完整 Galerkin 来源

取 $m\ge10,d=2^m$，整数 $x$ 与高度 $J$ 满足
$$
 d\le x,\qquad x+1\le d^4/64,\qquad
 0\le J\le\frac{\sqrt{x+1}}{8(m+1)}.
 \tag{1.1}
$$
使用同一原 N 或 Y 头及原全部强位：
$$
 C=A_m+D_{[m,x)},\qquad A=A_x,\qquad s\ge S_x.
$$
令 $F$ 为前 $x$ 位空间中同一个指定闭子空间，$i:F\hookrightarrow\mathcal H_{<x}$。
在两边均按原物理内积定义
$$
 H_X=\sum_{j=0}^{J}\frac{(X^*)^jX^j}{j!s^j},\qquad
 a_X=i(i^*H_Xi)^{-1}i^*f,\qquad
 \xi_X=f-H_Xa_X,\quad X=A,C.
 \tag{1.2}
$$
这里 $f$ 是原同一向量，特别允许 $f=f_1=e_1\otimes\Omega$。
$a_X$ 并未改成物理孔加权度量下的另一个最小者。
两边的 $\xi_X$ 都是完整环境残余，均在 $F^\perp$。

记真正头孔数为 $\mathcal N_{<x}$，并置
$$
 \gamma=1/32,\qquad \Gamma=32^{\mathcal N_{<x}}.
$$
本补充证明
$$
 \boxed{\|\Gamma(\xi_A-\xi_C)\|
 \le e^{-7d^4/4}\|f\|.}
 \tag{1.3}
$$
同时，若 $k_X=\mathcal R_{X,J}(s)a_X$ 是完整有限 Fock 能量列，
则在辅助因子上延拓 $\Gamma$ 为恒等后，有
$$
 \boxed{\|\Gamma(a_A-a_C)\|,
 \quad\|(\Gamma\otimes I)(k_A-k_C)\|
 \le e^{-7d^4/4}\|f\|.}
 \tag{1.4}
$$

## 2. 联合 carry 的相对误差仍在实际窗口内

有限 Fock 乘子稿的条件是
$\sqrt{J/s}\le\mathscr R_m=e^{417d^3/8}$。
由 $s\ge S_x\ge[3(x+1)^3]^{-1}$ 及 (1.1)，
$$
 \frac Js\le\frac{3(x+1)^{7/2}}{8(m+1)}
 \le d^{14}<e^{417d^3/4}.
 \tag{2.1}
$$
所以可取
$$
 0\le\Lambda\le2e^{-15d^4/8}.
 \tag{2.2}
$$
在原同一个 $F$ 上，该稿已经证明
$$
 \|\mathcal R_{C,J}(a_A-a_C)\|
 \le(e^{2\Lambda}-1)\|f\|,
$$
$$
 \|k_A-k_C\|\le(e^{3\Lambda}-1)\|f\|,
$$
$$
 \|H_C^{-1/2}(\xi_A-\xi_C)\|
 \le(e^{4\Lambda}-1)\|f\|.
 \tag{2.3}
$$
这些式子是完整 Gram 比较的后果；没有交换 $P_F$、$\Gamma$
或环境 inverse。

## 3. 实际孔权与完整环境伴随费用

前 $x$ 位有 $0\le\mathcal N_{<x}\le x$，故
$$
 \log\|\Gamma\|=x\log32
 \le\frac{5\log2}{64}d^4<\frac1{16}d^4.
 \tag{3.1}
$$
原完整强头有 $\|C\|\le7$。于是
$$
 \|H_C^{1/2}\|
 \le\sqrt{J+1}\max\{1,(7/\sqrt s)^J\}.
 \tag{3.2}
$$
由 (1.1) 与原方差下界，
$$
 \frac7{\sqrt s}\le7\sqrt3\,(x+1)^{3/2}
 \le\frac{7\sqrt3}{512}d^6<d^6,
 \qquad J\le\frac{d^2}{64(m+1)}.
$$
所以
$$
 \begin{aligned}
 \log\|H_C^{1/2}\|
 &\le\tfrac12\log(J+1)+6J\log d\\
 &\le 2\log d+\frac{3\log2}{32}d^2
 \le\frac1{64}d^4,
 \qquad d\ge1024.
 \end{aligned}
 \tag{3.3}
$$
末一步可用 $2\log d\le d^2/16$ 及
$3\log2/32<3/32$ 后直接比较；$d\ge1024$ 有充分余量。
因此完整环境伴随与真正孔权的共同费用为
$$
 \|\Gamma H_C^{1/2}\|
 \le\|\Gamma\|\|H_C^{1/2}\|
 \le e^{5d^4/64}.
 \tag{3.4}
$$
此处明确支付了整个 $H_C^{1/2}$，没有将能量对偶范数直接当作无权范数。

## 4. 完整残余与原最小者列

因为 $\Lambda$ 在 (2.2) 的范围内，
$$
 e^{4\Lambda}-1\le5\Lambda\le10e^{-15d^4/8}.
$$
利用 (2.3)、(3.4)，
$$
 \begin{aligned}
 \|\Gamma(\xi_A-\xi_C)\|
 &=\|\Gamma H_C^{1/2}H_C^{-1/2}(\xi_A-\xi_C)\|\\
 &\le10e^{-(15/8-5/64)d^4}\|f\|\\
 &=10e^{-115d^4/64}\|f\|
 \le e^{-7d^4/4}\|f\|.
 \end{aligned}
$$
最后只用 $\log10\le3d^4/64$。这证明 (1.3)。

因 $H_C\succeq I$，(2.3) 的第一式也控制 $\|a_A-a_C\|$。
将 (3.1) 乘上 (2.3) 的前两式，并用
$e^{3\Lambda}-1\le4\Lambda\le8e^{-15d^4/8}$，得到 (1.4)。
两个向量始终是 (1.2) 中的原未加权最小者，没有改源或改最小化。

## 5. 高孔 $\mathcal Z_{1/32}$ 的实际差界及最高 carry 入口

取任意同一物理孔门 $A_0$，令
$$
 Z_X=\left\|\sum_{g\ge A_0}32^{g-1}P_g\xi_X\right\|,
 \quad X=A,C.
$$
$P_{\ge A_0}$ 与 $\Gamma$ 交换且为正交投影，反三角不等式和 (1.3) 给
$$
 \boxed{|Z_A-Z_C|\le e^{-7d^4/4}\|f\|.}
 \tag{5.1}
$$
这条真正的加权源差界发生在原 $s\ge S_x$；没有经过 $s\downarrow0$。

在最高 carry 置零的原 N 问题中，若原头为 $m\ge11$，
$d=2^m,n=2^{m-1}$，则
$$
 C_0=A_{m-1}+D_{[m-1,x)}.
$$
保留原真正
$F_0=\lim_{t\downarrow0}\ker C_t^r$、原 $f_1$、原 $S_x$，
在另一边也使用同一个 $F_0$ 来定义 (1.2) 的 $a_{A_x}$。
若
$$
 d\le x,\quad x+1\le n^4/64=d^4/1024,\quad
 r-1\le\frac{\sqrt{x+1}}{8(m+1)},
$$
则将基头 $m$ 换成 $m-1$ 应用本补充，得到
$$
 \boxed{|Z_{A_x,F_0}-\mathcal Z_{1/32}(C_0,F_0;S_x)|
 \le e^{-7n^4/4}=e^{-7d^4/64}.}
 \tag{5.2}
$$
原高度窗比新基头所需的窗更窄，因此合法。改基头后强长度准确为
$R'=x-(m-1)=R+1$，所以新母支持取
$Q'\ge R'+(r-1)=R+r$。若沿用旧 $Q\ge R+r-1$，可明确取
$Q'=Q+1$；也可直接取最小整数 $Q'=R+r$。在本节范围内，后一个选择满足
$$
 Q'=x-m+r\le2(x+1)\le n^4/32<e^{26n^3},
$$
因此确在新基头 $m-1$ 的 c26 母窗口内。

$Z_{A_x,F_0}$ 仍是同一个完整 $F_0$ 上的原源残余。
本补充没有把它改成 $\ker A_x^r$ 上的较小问题，也没有证明它自身的绝对上界。
新增的是原实际允许窗内一个已经全付费的物理加权源运输接口。
