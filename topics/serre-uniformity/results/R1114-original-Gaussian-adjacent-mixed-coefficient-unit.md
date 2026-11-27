# R1114：原 Gaussian 相邻混合系数的二分布单位组合

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明。** 保留 R1082 的原 Gaussian 曲线、marked CM lift、
不变微分与全部 Hurwitz 归一：
$$
E_a:y^2=x^3+ax,\qquad a\in\mathbf F_p^\times,\qquad
p\ge41,\quad p\equiv3\pmod4,\qquad \omega=dx/(2y).
$$
写
$$
p=4k+3,\qquad n=k-1,\qquad
F(z)={}_2F_1\left(\frac14,\frac12;\frac54;z\right),\quad
G(z)={}_2F_1\left(\frac34,\frac12;\frac74;z\right),
\qquad W(z)=F(z)^6G(z).
\tag{1114.1}
$$
以下只约化明确读取的安全前缀，不声称整个 $G$ 在 $\mathbf Z_p[[z]]$
内：其第一个 $p$ 分母恰在未读取的第 $k$ 项。

令 $W_j=[z^j]W$，$D=d/\omega$，并沿用原 $D\Psi=\delta$。
则
$$
\boxed{\quad
5W_n+4W_{n-1}
=360(-a)^{-k}G_{p-3}
=\frac{144a(-a)^{-k}}{\delta^3}
\in\mathbf F_p^\times .
\quad}
\tag{1114.2}
$$
此处 $G_{p-3}$ 是原 Hurwitz 数，而不是 (1114.1) 中的函数 $G(z)$。

特别，两个指定相邻混合系数不能同时为零。
原 R1082 的 $\mathcal H_p$ 准确满足
$$
\mathcal H_p=\frac{2}{45}(-a)^kW_n.
\tag{1114.3}
$$
所以若原 Gaussian 斜率失败，即 $\mathcal H_p=0$，则
$$
W_{n-1}=90(-a)^{-k}G_{p-3}\ne0.
\tag{1114.4}
$$
本文没有证明 $W_n$ 本身非零；不把 (1114.2) 改写成原 Gaussian
斜率已经为单位。后一系数进入第二条原 forced 首项的完整公式见 §7；
其中三个原低卷积仍须联合控制。

## 1. 同一个原参数与两个 Abel 积分

在原 characteristic-zero Gaussian CM lift 上先作恒等式。
以 $t$ 表示 tangent-one 的 additive logarithm，取在 $O$ 的分支
$$
u=x^{-1/2}=t+O(t^5),\qquad
y=-u^{-3}\sqrt{1+au^4},\qquad z=-au^4.
$$
于是
$$
\omega=\frac{du}{\sqrt{1+au^4}},\qquad
t=uF(z),\qquad
S(t):=\int_0^u\frac{s^2\,ds}{\sqrt{1+as^4}}
       =\frac{u^3}{3}G(z).
\tag{1114.5}
$$
积分下限均在 $O$ 的形式邻域；$S$ 的首项为 $t^3/3$，
且 $DS=1/x$。因此没有未定的积分常数。

R1071、R1079、R1082 的整 eigenparameter $T$ 满足
$t(T)=T+O(T^{p^2})$，其第 $p^2$ 项可含 $p$ 分母。
本篇所有最终读取次数至多 $p-5$，
故这些低阶 additive-coordinate 读数与原整 $T$ 完全相同。
本文不约化完整 logarithm，也不使用第 $p^2$ 项。

若记 $s_j=(1/2)_j/j!$，则
$$
[z^j]F=\frac{s_j}{4j+1},\qquad
[z^j]G=\frac{3s_j}{4j+3}.
\tag{1114.6}
$$
对本篇 $0\le j\le n=k-1$，
两个显示分母分别不超过 $p-6$ 和 $p-4$；
$2,j!$ 也均为单位。所有乘法与换元因此可在这些前缀上约化。
下一项 $[z^k]G=3s_k/p$ 不被擅删或使用为整系数。

置 $R(z)=(1-z)^{-1/2}$。同源的一阶恒等式为
$$
4zF'(z)+F(z)=R(z),\qquad
4zG'(z)+3G(z)=3R(z).
\tag{1114.7}
$$

## 2. 原二挠点与 $1+i$ 的准确二次变换

取原二挠点 $Q=(0,0)$。加法律给
$$
x(t+Q)=\frac a{x(t)},\qquad
y(t+Q)=-\frac{ay(t)}{x(t)^2}.
\tag{1114.8}
$$
选择 $i^2=-1$，令 $\lambda=1+i$。
原 CM 自同态 $[\lambda]$ 的 normalized pullback 是
$[\lambda]^*\omega=\lambda\omega$，且
$$
x(\lambda t)=\frac{x+a/x}{\lambda^2},\qquad
y(\lambda t)=\frac{y(1-a/x^2)}{\lambda^3}.
\tag{1114.9}
$$
因此在所取形式分支
$$
u(\lambda t)=\frac{\lambda u}{\sqrt{1-z}},\qquad
z(\lambda t)=\phi(z):=\frac{-4z}{(1-z)^2}.
\tag{1114.10}
$$
由 $t=uF(z)$ 立即得到
$$
\boxed{F(\phi(z))=(1-z)^{1/2}F(z).}
\tag{1114.11}
$$

第二类积分必须保完整附加项。
取原 $\zeta=t^{-1}-\sum G_jt^{j-1}$。原加法律与
$x(Q)=y(Q)=0$ 给
$$
\zeta(\lambda t)=\frac{2\zeta(t)+y(t)/x(t)}{\lambda}.
\tag{1114.12}
$$
可由 (1114.9) 求导核对；两边在 $O$ 的首项相同，
没有常数或线性误差。另有
$$
D(y/x)=x-a/x,\qquad
S(t)=-\frac{\zeta(t)+y(t)/x(t)}a.
\tag{1114.13}
$$
后一式导数为 $1/x$，且首项 $t^3/3$，所以正是 (1114.5)
的同一个 primitive。

将 (1114.9)、(1114.12) 代入 (1114.13)，得到
$$
S(\lambda t)=\frac2\lambda
 \left(S(t)-\frac{u^3}{\sqrt{1-z}}\right).
$$
再用 $\lambda^4=-4$ 与 (1114.5)，准确化为
$$
\boxed{\quad
G(\phi(z))
=-\frac12(1-z)^{3/2}G(z)+\frac32(1-z).
\quad}
\tag{1114.14}
$$
右边第二项来自真实二挠平移的第二类修正。
它的常数项使右边等于一，不能删除。

合并两式：
$$
W(\phi(z))
=-\frac12(1-z)^{9/2}W(z)+\frac32(1-z)^4F(z)^6.
\tag{1114.15}
$$
这些是 characteristic-zero 原曲线的形式恒等式；
后面才按 §1 的精度约化。

## 3. 残数换元给相邻两项，而非单项

因 $\phi(z)=-4z+O(z^2)$ 的首系数为单位，
对 $n=k-1$ 作形式残数换元：
$$
(-4)^nW_n
=[z^n](1-z)^{2n-1}(1+z)W(\phi(z)).
\tag{1114.16}
$$
代入 (1114.15)。两个幂次恰为
$$
2n+\frac72=\frac p2,\qquad
2n+3=\frac{p-1}{2}.
$$
至所读次数 $n<p$，
$$
(1-z)^{p/2}\equiv1,\qquad
(1-z)^{(p-1)/2}\equiv R(z)\pmod p.
$$
所以
$$
(-4)^nW_n
=-\frac12(W_n+W_{n-1})
+\frac32[z^n](1+z)R(z)F(z)^6.
\tag{1114.17}
$$

由 (1114.7) 及 $(F^7)'=7F^6F'$，准确有
$$
\boxed{RF^6=F^7+\frac47z(F^7)'.}
\tag{1114.18}
$$
其 $n$ 次系数因 $1+4n/7=p/7$ 而为零，
其 $n-1$ 次系数则为
$$
[z^{n-1}]RF^6=-\frac47[z^{n-1}]F^7.
$$
于是
$$
(-4)^nW_n
=-\frac12(W_n+W_{n-1})-\frac67[z^{k-2}]F^7.
\tag{1114.19}
$$

特征 $p$ 中 $i^p=-i$，故 $\lambda^{p+1}=2$。
又 $4n=p-7$，因而
$$
(-4)^n=\lambda^{p-7}=\frac{2}{\lambda^8}=\frac18.
$$
将 (1114.19) 乘八，得到完整相邻关系
$$
\boxed{\quad
5W_n+4W_{n-1}=-\frac{48}{7}[z^{k-2}]F^7.
\quad}
\tag{1114.20}
$$
没有把右边换成某个未核的低 period。

## 4. 右端来自同一个二挠平移的原 Hurwitz 单位

这里单独支付 (1114.20) 的右端。
置
$$
M=p-7,\qquad g(t)=D^{p-5}x(t).
$$
由 $x''=6x^2+2a$ 和 $M>0$，
$$
[T^M]x^{-2}
=\frac{a^{-2}}{6M!}\,g(Q).
\tag{1114.21}
$$
此处先在 additive $t$ 中读取，随后用 §1 的安全精度换成原 $T$。
恒等式的来源是 $x^{-2}=a^{-2}x(t+Q)^2$，
不是同权猜测。

原 norm-two trace 是
$$
x(t)+x(t+Q)=\lambda^2x(\lambda t).
$$
施加 $D^{p-5}$，再只比较在 $O$ 的常数项，得
$$
g(Q)=(\lambda^{p-3}-1)g_0,\qquad
g_0=(p-5)!(p-4)G_{p-3}.
\tag{1114.22}
$$
所有较低正项经这些导数后不贡献常数；首负极仍是负次。
这里所有下降阶乘均小于 $p$。由
$\lambda^{p-3}=2/\lambda^4=-1/2$，准确有 $g(Q)=-3g_0/2$。

于是 (1114.21) 化为
$$
\boxed{\quad
[T^{p-7}]x^{-2}=30a^{-2}G_{p-3}.
\quad}
\tag{1114.23}
$$
具体常数来自
$(p-5)!/(p-7)!=(p-5)(p-6)\equiv30$、
$p-4=-4$、以及 $(-3/2)/6$，全部保留。

另一方面，对 $t=uF(-au^4)$ 用同一个 Lagrange 公式：
$$
[t^M]u(t)^4
=\frac4M[u^{M-4}]F(-au^4)^{-M}.
$$
因 $M=p-7$，在次数 $M-4=p-11<p$ 内
$F^{-M}\equiv F^7$，因为 $F^p$ 的首个非常数项次数至少 $p$。
所以
$$
[T^{p-7}]x^{-2}
=-\frac47(-a)^{k-2}[z^{k-2}]F(z)^7.
\tag{1114.24}
$$
比较 (1114.23)–(1114.24)，得到
$$
\boxed{\quad
[z^{k-2}]F^7
=-\frac{105}{2}(-a)^{-k}G_{p-3}.
\quad}
\tag{1114.25}
$$

R1082 (1082.22) 已由完整同权 theta-cycle 支付
$$
G_{p-3}=\frac{2a}{5\delta^3}\ne0
\tag{1114.26}
$$
于当前 $\mathbf F_p$ reference。
该证明保留 Frobenius 项，使用原 $G_4=-a/15$ 与
$C_{\rm rel}(x\omega)=\beta\omega'$、$\beta=-\delta$。
本篇只消费该已成单位，不重新扫描任何 prime。
将 (1114.25) 代入 (1114.20) 即得 (1114.2)。

## 5. 原 Gaussian 横向目标准确是 $W_n$

为完整接回原目标，这里给出低阶 Lagrange 推导，
不对仅在 supersingular locus 上成立的值式求导。

在通用 $y^2=x^3+ax+b$ 上，仍取 $u=x^{-1/2}$，令
$$
\mathscr F(u;a,b)
=\frac1u\int_0^u\frac{ds}{\sqrt{1+as^4+bs^6}}.
$$
同一 Hurwitz 规范给
$$
G_d=-\frac{2}{(d-1)(d-2)}
          [u^d]\mathscr F^{\,2-d}.
\tag{1114.27}
$$
先对 $b$ 求导，再取 $d=p-5$、$b=0$，可约化为
$$
(\partial_bG_{p-5})(a,0)
=-\frac13[u^{p-5}]F(-au^4)^6\,\mathscr F_b(u;a,0).
\tag{1114.28}
$$
全部读取低于 $p$，因此 $F^{6-p}$ 换成 $F^6$ 不漏项。
直接积分分部得到
$$
\mathscr F_b(u;a,0)
=\frac{u^2}{4a}
 \left((1+au^4)^{-1/2}-G(-au^4)\right).
\tag{1114.29}
$$
由 (1114.18)，$[u^{p-7}]F^6(1+au^4)^{-1/2}=0$，
故
$$
(\partial_bG_{p-5})(a,0)
=\frac1{12a}[u^{p-7}]F(-au^4)^6G(-au^4).
\tag{1114.30}
$$

最后使用 R1082 的通用 sigma-heat 身份
$\mathcal H_p=-8a^2(\partial_bG_{p-5})(a,0)/15$，
得到
$$
\mathcal H_p
=-\frac{2a}{45}[u^{p-7}]F(-au^4)^6G(-au^4)
=\frac2{45}(-a)^kW_n,
$$
即 (1114.3)。从原 marked lift 到原 $T$、
Hurwitz 数、heat transverse direction 的每个尺度均保留。

也可把相邻量写为真正的同一 $u$-series 系数
$$
\mathcal K_p=[u^{p-11}]F(-au^4)^6G(-au^4).
$$
则 (1114.2) 等价于
$$
\boxed{\quad
5\mathcal H_p+\frac{8a^2}{45}\mathcal K_p
=16G_{p-3}.
\quad}
\tag{1114.31}
$$
所以在 $\mathcal H_p=0$ 支上
$$
\boxed{\mathcal K_p=\frac{90}{a^2}G_{p-3}
                         =\frac{36}{a\delta^3}\ne0.}
\tag{1114.32}
$$

## 6. 精确范围和下一实际缺口

(1114.2)、(1114.31) 是完整原系数身份，其右端为单位。
它们没有把 $W_n$ 或 $\mathcal H_p$ 本身证明为单位。
R1082 第一 forced 角色的原 coarse polynomial 已是仿射式：
其 fine 指数只有 $0,2$。
所以若 $\mathcal H_p=0$，不能称 (1114.32)
自动给该同一角色的一个未出现的更高 coarse coefficient。

若要用失败支上的 $\mathcal K_p$，必须把它准确接到另一条
原 forced 标签、实际高变分或其它已经授权的几何读数；
所有 regularizer、Weil phase 和两条 Gaussian twist descent
仍须保留。§7 给这座桥的完整公式，仍保三个待控制的原低卷积。

本篇也不把 Gaussian $\mathcal H_p$ 或 $\mathcal K_p$ 换成
O2 原 $r=2,8$ bare coefficient、原 $f_N/e$、短 $D^6$ 的
$\eta_k,\nu_k$ 或原 QC 最低 functional。
全文没有任何新数学程序执行，也未扩大或重复已有 prime 窗口。

来源：[R1082](R1082-original-Gaussian-high-Hurwitz-and-complete-short-convolution.md)
的 (1082.3)、(1082.21)、(1082.22)，以及本篇完整写出的原
Gaussian 二挠加法律、$1+i$ 分布、形式残数和 Lagrange 公式。


## 7. 相邻量进入第二个原 forced 首项的完整公式

本节把 §6 留下的来源比较推进到准确的全项公式，不删去剩余卷积。
仍取同一个原 $t,u,z,F,G$，另写
$$
R_0(z)=(1-z)^{-1/2},\qquad
h=u^{-1}R_0(z)^{-1},\qquad
A=\frac{u^3}{3}G(z).
$$
这里 $A$ 是 §1 的原 $S(t)$，而
$$
x=u^{-2},\quad y=-u^{-3}R_0^{-1},\quad
\zeta=h-aA.
\tag{1114.33}
$$
最后一式正是 (1114.13)，不是另选一个第二类 primitive。

记 R1116 的同一最高安全 band 为
$P_k(t,U)=\sum_s c_s t^{p-4-s}U^s$。
由原完整 Appell 多项式，
$$
24c_3=[t^{p-7}]\mathcal C_4(\zeta;x,y,a),
$$
$$
\mathcal C_4=\zeta^4-6x\zeta^2-8y\zeta-3x^2-\frac{12a}{5}.
\tag{1114.34}
$$
此处仍保 sigma 分母给的 $-12a/5$。

### 7.1 在原 $u$ 中的六项完整展开

用 $h^2=x+au^2$、$y=-xh$ 展开 (1114.34)，准确得到
$$
\begin{aligned}
\mathcal C_4={}&
 \frac{8a}{5}+a^2u^4
 -\frac{4a^2}{3}u^4R_0^{-1}G
 +\frac{2a^3}{3}u^8G^2\\
&-\frac{4a^3}{27}u^8R_0^{-1}G^3
 +\frac{a^4}{81}u^{12}G^4.
\end{aligned}
\tag{1114.35}
$$
例如线性 $A$ 项是
$-4ah^3A+4axhA=-4a^2u^2hA$；
二次项是 $6a^2(h^2-x)A^2=6a^3u^2A^2$。
常数部分为
$h^4+2xh^2-3x^2-12a/5=8a/5+a^2u^4$。
这逐项支付了全部符号及系数。

令 $M=p-7$。在真实换元 $t=uF(z)$ 下，
$dt=R_0(z)\,du$，所以形式残数给
$$
[t^M]\mathcal C_4(t)
=[u^M]\mathcal C_4(u)F(z)^{-M-1}R_0(z)
=[u^M]\mathcal C_4(u)F(z)^6R_0(z)\pmod p.
\tag{1114.36}
$$
最后一步只在这次安全前缀上使用 $-M-1=6-p$。
$\mathcal C_4(u)$ 是正规幂级数，$F^{-p}-1$ 首项至少为 $u^{4p}$；
它不可能回流到 $M<p$。
所有 $G$ 只读到 $j\le k-1$，未读取第一个 $p$ 分母。
$t(T)$ 与原整 eigenparameter 的差仍在本次范围之外。

常数部分的贡献恰为零：
$$
[u^M]F^6R_0
=\left(1+\frac M7\right)[u^M]F^7=0\pmod p,
$$
这里用 $R_0=F+u\,dF/du$。
$a^2u^4$ 项则由同一个残数换元和 (1114.23) 给
$$
a^2[u^{p-11}]F^6R_0
=a^2[t^{p-7}]x^{-2}
=30G_{p-3}.
\tag{1114.37}
$$

定义三个明确的原低卷积
$$
\begin{aligned}
\mathcal V_2&=[u^{p-15}]F(-au^4)^6R_0(-au^4)G(-au^4)^2,\\
\mathcal V_3&=[u^{p-15}]F(-au^4)^6G(-au^4)^3,\\
\mathcal V_4&=[u^{p-19}]F(-au^4)^6R_0(-au^4)G(-au^4)^4.
\end{aligned}
$$
将 (1114.35) 全部代入，得到
$$
\boxed{
24c_3=
30G_{p-3}-\frac{4a^2}{3}\mathcal K_p
+\frac{2a^3}{3}\mathcal V_2-\frac{4a^3}{27}\mathcal V_3
+\frac{a^4}{81}\mathcal V_4.
}
\tag{1114.38}
$$
再仅用本篇已证 (1114.31) 消去 $\mathcal K_p$：
$$
\boxed{
24c_3=
-90G_{p-3}+\frac{75}{2}\mathcal H_p
+\frac{2a^3}{3}\mathcal V_2-\frac{4a^3}{27}\mathcal V_3
+\frac{a^4}{81}\mathcal V_4.
}
\tag{1114.39}
$$
特别在 $\mathcal H_p=0$ 支，已知单位项是
$-90G_{p-3}$；其余三项仍必须共同结算，不能删去后宣称 $c_3$ 单位。

### 7.2 原角色、尺度和仍未付的非零

这个 $c_3$ 确实是第二 forced 角色
$$
R=p-5,\quad r=4,\quad \chi=\omega^{p-5},\quad
d=p^2-6p-3
$$
的原 coarse 一阶读数。若该角色实际 Bernoulli-good，
即 $p\nmid B_{p-5}$，R1116 (1116.20) 精确给
$$
[z_{\rm coarse}]
 \bigl(c_{\chi,s}(z_{\rm coarse})-c_{\chi,s}(0)\bigr)
=-\frac{6\,\beta_0^d\lambda_{\rm src}^{\,2}}
        {b_\chi\delta^3}\,c_3.
\tag{1114.40}
$$
这里 $\lambda_{\rm src}$ 是 R1071 的原节点尺度，
不是 §2 的 CM 同源 $1+i$；真实 Weil 相位及两条 twist line
仍按原公式共同运输。若该角色不 good，不能除以 $b_\chi$。

该角色的完整 fine 指数还允许 $i=4$，所以其完整 coarse
profile 一般为二次式；(1114.40) 只声明中心一阶的来源。
本节给出了 $\mathcal K_p$ 到一个真正 forced 首项的完整比较，
同时准确显示了必须继续控制的三个原卷积。
它未证明 $c_3$ 非零、未排原全 good 首项共同零或完整标签重值。

本节由 root 推导，o2_high_coefficient 独立逐项纸核。
只消费 R1114 的同一安全 Lagrange 与 R1116 的原 Appell/角色尺度，
无数学程序执行。
