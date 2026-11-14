# R271 附录：深源 jets 的 Schur 消元与同一平坦源支付

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_continue。

状态：**已证明的同源缩减。** 本文接[源 jets 与全部自由坐标](R271-appendix-source-primitive-jets-and-sequential-right-chain.md)和[原头四次幂预算](R271-appendix-primitive-bandwidth-and-far-schur-localization.md)。新增结论是在完整源 Schur 度量内，进一步消去一段强制的深 jets；它们偏离真正最小补全的全部能量由原来的 $c^\flat$ 支付。没有将深坐标置零，没有把顺次右链换成裸费，也未证明剩余浅层的三 Gram 比较。

## 1. 同一个原源及完整度量

固定 $m\ge8$、$d=2^m$、原合法整数 $4d\le q\le e^{d^3/4}$，写 $A=A_m$、$D=D_m$、$K_n=\ker D\cap\mathcal H_n$。沿源 jets 稿，全部自由坐标为 $\mathscr F=\ker\mathcal B$，其正交补为
$$
\mathscr T=\bigoplus_{k=0}^{d-2}
\left(H_{\ge k+1}\otimes K_{q-k}\right),\qquad
H_{\ge k+1}=\operatorname{span}\{e_{k+1},\ldots,e_{d-1}\}.
\tag{1.1}
$$
$B_{\mathscr T}=\mathcal B|_{\mathscr T}$ 是到原完整源空间的有界同构。对于同一个原源 $r$，记其强制坐标为
$$
\sigma=B_{\mathscr T}^{-1}r.
$$
全部自由坐标已经在原左度量中作过真正最小化；得到的完整源 Schur 补记为 $S=S_{\rm src}\succeq I$。写
$$
C=\mathcal C_R|_{\mathscr T},\qquad
c^\flat=F_{\rm flag}^*J_q^{-1}r,\qquad
\lambda^\flat=\|c^\flat\|.
$$
原准确身份是
$$
\mu_q(r)^2=\langle S\sigma,\sigma\rangle,
\qquad S\sigma=-C^*c^\flat,
\qquad C\sigma=-\mathcal R_{\rm seq}r.
\tag{1.2}
$$
$\mathcal R_{\rm seq}$ 是原顺次单步 MP 右链；最后一式不声称它是完整右最小者。

取
$$
h=5d/8,\qquad
\mathscr T_{\rm sh}=\bigoplus_{0\le k<h}H_{\ge k+1}\otimes K_{q-k},
\qquad
\mathscr T_{\rm dp}=\bigoplus_{h\le k\le d-2}H_{\ge k+1}\otimes K_{q-k}.
\tag{1.3}
$$
两者都是原物理坐标中的正交子空间。下标仅表示 jet 深度，不是更换尾出生旗。

## 2. 整段深 jets 的跨界算子确为指数小

仍令 $T=d-1$，并取前稿已经支付的
$$
\mathcal L=512\sqrt{q+2T+1}\,(m+q+2T+1)^{3/2},
\qquad \Theta=\log(12\mathcal L)<d^3/2+11.
$$
对于固定提升阶 $t$，不同输入孔层的输出正交，所以原整段算子满足
$$
\|(-A)^tQ_t\|
\le w_t:=\exp\!\left[t\Theta-\gamma(t-m)_+^4\right],
\qquad \gamma=770/256.
\tag{2.1}
$$
这正是原头四次幂预算；没有对一般幂零矩阵作此断言。

深 jet $k\ge h$ 的 primitive 输入孔层是 $q-k$。要输出在 $q$ 以上，必须提升 $t\ge k+1\ge h+1$。故在整个直和上
$$
\|C|_{\mathscr T_{\rm dp}}\|
\le\sum_{t=h+1}^{d-1}w_t.
\tag{2.2}
$$
这里没有输入孔数 $q$ 或源坐标总数的额外求和因子。

当 $m\ge8$ 时 $m/d\le1/32$。对实数 $t\ge5d/8$，函数
$$
f(t)=\gamma(t-m)^4-(d^3/2+11)t
$$
严格递增：由 $t-m\ge19d/32$，
$$
f'(t)\ge\left[4\gamma(19/32)^3-1/2\right]d^3-11
>2d^3-11>0.
$$
因此
$$
\begin{aligned}
\log w_t
&\le-\left[\gamma(19/32)^4-5/16\right]d^4+(55/8)d\\
&=-\frac{8230545}{134217728}d^4+(55/8)d
<-\frac3{50}d^4+(55/8)d.
\end{aligned}
\tag{2.3}
$$
由于 $d\ge256$ 且 $\log d+(55/8)d\le d^4/100$，(2.2) 给
$$
\boxed{\|C_{\rm dp}\|\le\varepsilon_d:=e^{-d^4/20},
\qquad C_{\rm dp}=C|_{\mathscr T_{\rm dp}}.}
\tag{2.4}
$$
这是全部原合法 $q$ 上、包括所有深层叠加的算子范数界。

## 3. 完整源度量中的第二次 Schur 消元

按 $\mathscr T_{\rm sh}\oplus\mathscr T_{\rm dp}$ 写
$$
S=\begin{pmatrix}S_{00}&S_{01}\\S_{10}&S_{11}\end{pmatrix},
\quad \sigma=(x,y),\quad
C=(C_{\rm sh},C_{\rm dp}).
$$
由 $S\succeq I$，$S_{11}\succeq I$ 有有界逆。定义
$$
\widehat S=S_{00}-S_{01}S_{11}^{-1}S_{10}\succeq I,
\qquad y_0=-S_{11}^{-1}S_{10}x,
\qquad z=y-y_0.
\tag{3.1}
$$
$y_0$ 是保持浅坐标 $x$ 后的真正最小深坐标。一般不为零。
由 (1.2) 的深块，准确有
$$
\boxed{S_{11}z=-C_{\rm dp}^*c^\flat.}
\tag{3.2}
$$
真正左费用因此分解为
$$
\boxed{
\mu_q(r)^2
=\langle\widehat Sx,x\rangle+
\langle S_{11}z,z\rangle,
\qquad
0\le\langle S_{11}z,z\rangle
\le\varepsilon_d^2(\lambda^\flat)^2.
}
\tag{3.3}
$$
证明后一式时，只用
$$
\langle S_{11}z,z\rangle
=\|S_{11}^{-1/2}C_{\rm dp}^*c^\flat\|^2
\le\|C_{\rm dp}\|^2\|c^\flat\|^2.
$$
同理
$$
\boxed{\|z\|\le\varepsilon_d\lambda^\flat.}
\tag{3.4}
$$
所以 (3.3) 消去的是深坐标偏离最小补全的全部真实能量，不只是其普通坐标范数。

定义保留全部 Schur 回馈的跨界映射
$$
\boxed{\widehat C=C_{\rm sh}-C_{\rm dp}S_{11}^{-1}S_{10}.}
\tag{3.5}
$$
将 (1.2) 的浅块减去 $S_{01}S_{11}^{-1}$ 乘深块，得到
$$
\boxed{\widehat Sx=-\widehat C^*c^\flat.}
\tag{3.6}
$$
这里右侧仍是原源 $r$ 的同一个 $c^\flat$；没有重算或替换成另一个源的平坦费用。

## 4. 原裸费用也可同步保留

沿首段先消元的原符号，令 $P_L$ 为右输入低出生投影，$Z=\ker S_L$，$\mathcal U=Z\ominus\ker(F|_Z)$。原真正裸最小者为
$$
a(r)=P_{\mathcal U}P_L\mathcal R_{\rm seq}r
=-P_{\mathcal U}P_LC\sigma,
\qquad \alpha_q(r)=\|a(r)\|.
$$
由 $C\sigma=\widehat Cx+C_{\rm dp}z$，定义
$$
\widehat a(x)=-P_{\mathcal U}P_L\widehat Cx.
$$
两个投影均为原 Hilbert 正交投影，故 (2.4)、(3.4) 给
$$
\boxed{
\|a(r)-\widehat a(x)\|
\le\varepsilon_d^2\lambda^\flat.
}
\tag{4.1}
$$
因此在剩余坐标中可以同时使用原平坦对偶方程 (3.6)，以及仅有已付小误差的原裸输入 (4.1)。不需要假定裸投影与 $S$、$C$ 或深度投影交换。

还可以把这次分解写成两个合法完整源，但必须保留其限度。令
$$
\widehat r=B_{\mathscr T}(x,y_0),\qquad
\delta r=B_{\mathscr T}(0,z),\qquad r=\widehat r+\delta r.
$$
由完整最小左原像关于源的线性性和 $S$ 度量，
$$
\langle E_q^\dagger\widehat r,E_q^\dagger\delta r\rangle=0,
\quad
\mu_q(\widehat r)^2=\langle\widehat Sx,x\rangle,
\quad
\mu_q(\delta r)^2=\langle S_{11}z,z\rangle.
\tag{4.2}
$$
而 $\mathcal R_{\rm seq}\delta r=-C_{\rm dp}z$ 是同一个原旗中的可行完整右链，所以
$$
\boxed{
\mu_q(\delta r)\le\varepsilon_d\lambda^\flat,
\qquad
\lambda_q(\delta r)\le\varepsilon_d^2\lambda^\flat,
\qquad
\alpha_q(\delta r)\le\varepsilon_d^2\lambda^\flat.
}
\tag{4.3}
$$
没有由 (4.3) 宣称 $\lambda_q(\widehat r^\flat)$ 被原 $\lambda^\flat$ 控制。所需同源对偶信息是 (3.6)，不是另造一个免费的平坦源运输。

## 5. 可选深度阈值与剩余问题

更一般地，令
$$
\theta_*=(128/770)^{1/3}=0.549844\ldots.
$$
固定 $\theta_*<\theta<1$，取深度起点 $h=\lceil\theta d\rceil$。由于 $m/d\to0$、$\Theta/d^3\le1/2+o(1)$，且
$$
\beta_\theta=\gamma\theta^4-\theta/2>0,
$$
同一计算证明：对任意 $0<c<\beta_\theta$，充分大 $m$ 时，全部原合法 $q$ 上
$$
\boxed{\|C|_{k\ge\lceil\theta d\rceil}\|\le e^{-cd^4}.}
\tag{5.1}
$$
把 $\varepsilon_d$ 换成该界，§§3–4 原样成立。$5/8$ 的选择提供了不带未指定起点的 $m\ge8$ 明确版本。

新增缩减的实际用途如下。若能对 (3.6) 的剩余浅坐标证明
$$
\langle\widehat Sx,x\rangle^{1/2}
\le K_m\bigl(\|\widehat a(x)\|+\|c^\flat\|\bigr),
$$
则 (3.3)–(4.1) 直接给原源
$$
\mu_q(r)\le K_m\alpha_q(r)
+\left[K_m(1+\varepsilon_d^2)+\varepsilon_d\right]\lambda_q(r^\flat).
\tag{5.2}
$$
这不增加新的大费用。可是 $\widehat S$ 和 $\widehat C$ 仍包含 (3.1)、(3.5) 中的完整回馈，不能把它们改成 $S_{00}$ 和 $C_{\rm sh}$。剩余浅 jets 及其全部头方向与原裸项的温和比较尚未证明；原两形式求和门槛、无权 $N=M$ 与普通 ISP 继续开放。
