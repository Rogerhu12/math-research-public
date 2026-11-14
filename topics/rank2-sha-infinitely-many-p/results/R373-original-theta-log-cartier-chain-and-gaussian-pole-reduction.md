# R373：原 theta 对数的三层 Cartier 链与合法 Gaussian 降极

日期：2026-11-14。**状态：已证明。** 原有限 theta 对数的首 Frobenius 系数有一个完整有理恒等式，其 Cartier 链的最后非零项准确为 $-dz/6$。同一个原 Gaussian 重分解可以使该有理对数在三个二挠点的极阶从 $p^2+p$ 降为 $p^2-1$，并保留全部非原点短 jets。物理 Gaussian 补偿完整写出；这里的模 $p$ 降极不等同于删除原模 $p^2$ 边界。

## 1. 原规范及目标

沿 R356、R369、R371，固定
$$
E_b:y^2=x^3+b,\quad b=17,\quad p=6s-1>7,\quad p\nmid b,
$$
在模 $p$ 的完美剩余域中取
$$
Dx=2y,\quad Dy=3x^2,\quad DZ=1,\quad D^p=0,\quad
a=x^2/y,\quad F=1+Za.
$$
常数
$$
c=c_p=\binom{3s-1}{2s-1}b^s\in\mathbf F_p^\times
\tag{1}
$$
保留 R356 的原规范。
同一个有限积分算子及原函数为
$$
\mathcal I_Z(f)=
\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}}{(i+1)!}D^if,
\qquad G=\mathcal I_Z(-x),\qquad H=\mathcal I_Z(G).
\tag{2}
$$
已有的完整恒等式为
$$
DG=-x+cZ^{p-1},\qquad D^{p-1}G=a^p,\qquad
DH=G+Z^{p-1}a^p.
\tag{3}
$$
$H$ 正是原 sigma Gaussian 规范的有限 theta 对数；
它的原点常数及全部非原点测试点值都为零。
本篇不改变这一规范后再把更换藏在记号内。

## 2. 原 H 的准确 p 次根

**定理1。** 同一函数域中
$$
\boxed{
D^{p-1}H
=-D^{p-3}x-\frac c2Z^2-a^pZ
=-\frac{b^p}{2c}\left(\frac{x}{y^2}\right)^p.
}
\tag{4}
$$

**证明。** 从 (3) 微分 $p-2$ 次。
原 $a^p$ 被 $D$ 消去，且
$D^{p-2}Z^{p-1}=-Z$，所以
$$
D^{p-1}H=D^{p-2}G-a^pZ.
$$
再由第一式 (3)，
$D^{p-2}G=-D^{p-3}x-cZ^2/2$，得到 (4) 的第一式。

该式被 $D$ 消去，因此属于函数域的 $p$ 次幂子域。
在每个非零二挠点，右侧至多有 $2p$ 阶极；
在原点它正规，因为 $H$ 正规且 $D$ 是全局不变向量场。
其 $p$ 次根因而至多在三个非零二挠点各有二阶极，在 $O$ 正规。

$H$ 型为零，$D^{p-1}H$ 的 $\mu_6$ 型为二，
其 $p$ 次根型为负二。
对这个极除子的 Riemann--Roch 空间，有实际基
$$
1,\quad 1/y,\quad x/y,\quad 1/y^2,\quad x/y^2,\quad x^2/y^2.
\tag{5}
$$
六个元素在 $O$ 正规，在三点极阶至多二；独立性与 degree-six
Riemann--Roch 给其完备性。型负二的唯一线是 $x/y^2$。
所以 (4) 第一式等于某常数乘 $(x/y^2)^p$。

为支付该常数，取二挠点 $T=(\alpha,0)$，
$\alpha^3=-b$，并以 $y$ 为局部参数。
写 $Z=R_p(x)/y^p$。R371 的
$$D^{p-2}x+cZ+a^p=0$$
在此点的最高极部给
$$
R_p(\alpha)=-\alpha^{2p}/c.
\tag{6}
$$
(4) 第一式的 $y^{-2p}$ 系数因此为
$$
-\frac c2R_p(\alpha)^2-\alpha^{2p}R_p(\alpha)
=\frac{\alpha^{4p}}{2c}.
$$
除以 $(x/y^2)^p$ 的系数 $\alpha^p$，
所得常数恰是
$\alpha^{3p}/(2c)=-b^p/(2c)$。
这证明 (4)，含全部固定二挠点而非只在原点比较。$\square$

## 3. 完整三层 Cartier 链

记 $\mathcal C$ 为 Cartier。
由 $dZ=dz$ 和
$\mathcal C(f\,dZ)=(-D^{p-1}f)^{1/p}dZ$，
(4) 给
$$
\mathcal C(H\,dz)=\frac{b}{2c}\frac{x}{y^2}\,dz.
$$
这里 $b,c,2$ 都在 $\mathbf F_p$，其 $p$ 次根就是自身。
准确微分恒等式
$$
Da=x+3b\,x/y^2
\tag{7}
$$
于是给出
$$
\boxed{
\mathcal C(H\,dz)=\frac1{6c}(da-x\,dz),\qquad
\mathcal C^2(H\,dz)=-\frac16\,dz,\qquad
\mathcal C^3(H\,dz)=0.
}
\tag{8}
$$
第二式使用 $\mathcal C(da)=0$ 和
$\mathcal C(x\,dz)=c\,dz$；
后者由 $D^{p-1}x=-c$ 直接得到。
第三式使用原 $D^p=0$ 下的
$\mathcal C(dz)=\mathcal C(dZ)=0$。

末非零项的系数 $-1/6$ 对每个允许素数都是单位。
整个实际四维空间
$$
\operatorname{span}\{H\,dz,\ da,\ x\,dz,\ dz\}
\tag{9}
$$
因而在 Cartier 下闭合；(8) 保留 exact 项 $da$，
没有在实际配对之前先把它商掉。
这是一条原有限 theta 对数的链，不是新增的中央非零条件。

## 4. 原 H 的完整有限式与真实最高极阶

定义
$$
S_p=\sum_{j=0}^{p-3}
 \frac{(-1)^j(j+1)}{(j+2)!}Z^{j+2}D^jx.
\tag{10}
$$
则准确有
$$
\boxed{
H=-S_p+(Za)^p-cZ^{p+1}
=-S_p-Z^pD^{p-2}x-2cZ^{p+1}.
}
\tag{11}
$$

证明可直接从 (2) 展开。对 $i\ge1$，
$$
D^iG=-D^{i-1}x
+c(-1)^{i-1}(i-1)!\,Z^{p-i}.
$$
第二项在 $\mathcal I_Z(G)$ 中的总系数是
$$
-c\sum_{i=1}^{p-2}\frac1{i(i+1)}=-2c.
$$
把其余项与 $ZG$ 合并，就得到 (11) 第二式。
再使用 R371 的 $D^{p-2}x+cZ+a^p=0$，即得第一式。
全部阶乘及相位均未省略。

在 $T=(\alpha,0)$，$Z$ 极阶为 $p$。
每个 $D^jx$ 在此正规，
所以 $S_p$ 的极阶至多 $p(p-1)$。
$D^{p-2}x$ 是奇函数，在二挠点值为零；
其导数为 $-c\ne0$，故零阶准确为一。
因此 $Z^pD^{p-2}x$ 的极阶准确为 $p^2-1$。
最后一项 $-2cZ^{p+1}$ 则有准确 $p^2+p$ 阶极，
不能被其余项取消。于是
$$
\boxed{
\operatorname{pole}_T(H)=p^2+p
\quad(T\in E_b[2]\setminus\{O\}).
}
\tag{12}
$$

还有一个必须分清的 Frobenius 常数：
$$
H-2F^p=-S_p+Z^pD^{p-2}x-2.
\tag{13}
$$
它的极阶也降到 $p^2-1$，且在 $O$ 与 $H$ 的差从 $Z^{6p}$ 起，
但在每个非原点 $Z=0$ 处，它的值由零变成 $-2$。
所以 (13) 不是保原非原点规范的免费替换。
$F^p\,dz=d(ZF^p)$ 只说明它不改变 (8) 的 Cartier 像，
并不删除这个实际点值差。

## 5. 一个真正允许的 Gaussian 降极规范

R342/R356 允许同一物理来源的整体重分解
$$
\kappa=\kappa_\sigma+\Delta,\quad \Delta\in\mathcal O,\qquad
G_\kappa=G-\bar\delta_\kappa Z^p,\quad
H_\kappa=H-\bar\delta_\kappa Z^{p+1},
$$
$$
\delta_\kappa=(p+1)\Delta/34.
\tag{14}
$$
先取 $p\nmid34$。选任一整提升 $\widetilde c$，
并令
$$
\boxed{\Delta=-68\widetilde c.}
\tag{15}
$$
则 $\bar\delta_\kappa=-2c$，因而模 $p$ 的真实有限代表变成
$$
\boxed{
H_\kappa=H+2cZ^{p+1}
=-S_p-Z^pD^{p-2}x.
}
\tag{16}
$$
它在三个非零二挠点的极阶准确为 $p^2-1$。
此选择使用原允许的 Gaussian 参数，
与 (13) 的任意 Frobenius 常数更换不同。

由于 $Z^{p+1}$ 在所有非原点测试点消失至 $p+1$ 阶，
(16) 仍满足
$$
H_\kappa(P)=0,\qquad
H_\kappa\equiv H\bmod Z^p
\quad(Z(P)=0,\ P\ne O).
\tag{17}
$$
相应 $G_\kappa$ 的低于 $p$ 阶 jets 也未变。
原 $\chi$ 完全不变；(8) 也不变，因为
$\mathcal C(Z^{p+1}dz)=0$。

更准确地，以 $y$ 为二挠点参数，
$$
D^{p-2}x=-\frac{c}{3\alpha^2}y+\cdots,\qquad
Z=-\frac{\alpha^{2p}}c\,y^{-p}+\cdots.
$$
(16) 的最高极系数是
$$
-\frac{\alpha^{2p^2-2}}3=-\frac13.
\tag{18}
$$
这里每个 $\alpha^3=-b$ 属于 $\mathbf F_{p^2}$，
且 $\alpha\ne0$，所以 $\alpha^{p^2-1}=1$。

令 $t=-b/x^3$，$L_0=(p^2-1)/2$。
$H_\kappa$ 型零，故下降到同一有理 $t$ 线。
它在 $t=0$（原点）及 $t=\infty$（两个 $x=0$ 点）均为零，
只在 $t=1$ 有极。
因此有唯一多项式 $N_H(t)$，使
$$
\boxed{
H_\kappa=\frac{N_H(t)}{(1-t)^{L_0}},\quad
\deg N_H\le L_0-1,\quad N_H(0)=0,\quad N_H(1)=-1/3.
}
\tag{19}
$$
最后一个常数不能只由 (18) 不加换参地读取：
$1-t=y^2/x^3$，而
$\alpha^{3L_0}=(-b)^{L_0}=1$，
因为 $p-1$ 整除 $L_0$。
这准确支付 $y$ 到 $1-t$ 的因子。
$\deg N_H<L_0$ 则来自 $t=\infty$ 的真实零。

## 6. 原物理来源的完整补偿

(15) 只改变 Gaussian 分解，不改变原物理来源。
对相对次数 $N$，原 regularized 变量满足
$$
g_\kappa=g_{\kappa_\sigma}e^{-\Delta w^s},\qquad
a_\kappa=p\kappa=a_{\kappa_\sigma}+p\Delta,\qquad
w^s=p\epsilon .
$$
因此准确有
$$
\boxed{
g_\kappa^N e^{Na_\kappa\epsilon}
=g_{\kappa_\sigma}^N e^{Na_{\kappa_\sigma}\epsilon}.
}
\tag{20}
$$
在原三块目标中分别使用完整二次指数 $e_2$；
(20) 的每个混合项仍由同一关系 $w^s=p\epsilon$ 保留。
公共 charge40、$U_0/P_{134}$ 和十三行都按原矩阵的定义不变。

(16)、(19) 是模 $p$ 全局有理代表的降极结果。
对于实际模 $p^2$ 的 Serre 左核及 first-lift 配对，
必须同时使用新的 $a_\kappa$、R363 的真实二阶系数及
(20) 的完整补偿。
本篇没有由模 $p$ 的最高极系数消去，就无证删除整提升中的
$p$ 倍极部或原二挠点边界。

## 7. 当前应用边界

R369 的 $Z^{68}$ 移位及共同 forcing 高尾原始性，
可以在 (15) 的规范中原样使用，因为 (17) 保留其全部所需 jets。
R371 的完整加权式
$$
\operatorname{Res}(f\chi\,dz)
=\frac13\operatorname{Res}\bigl(f\,d\log(Z^3y)\bigr)
+\operatorname{Res}(K_p\,df)
$$
也仍不变。

本篇把固定二挠点处的原 theta 对数压成 (19) 的明确有理格式，
并用 (8) 记录其完整首 Frobenius 方向。
原同一 $P/\lambda$ 配对还须把这些固定极、$x=0$ 的边界、
Gaussian 和 exact 项一起处理。
不能将三层 Cartier 链的单位末项替换成原中央导数的单位断言。

## 引用

- [R342](R342-original-gaussian-recalibration-and-miller-adjoint-residue.md)：同一物理来源的合法 Gaussian 重分解。
- [R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)：原 $G_\sigma,G_\kappa$ 及 $c_p$。
- [R363](R363-original-first-frobenius-quotient-and-second-rational-connection.md)：原模 $p^2$ 连接和完整 first-lift。
- [R369](R369-original-finite-theta-frame-and-shifted-joint-residue-primitivity.md)：有限 $H_\kappa$、原 theta 模型及 $Z^{68}$。
- [R371](R371-original-frame-defect-cartier-logarithm-and-weighted-exact-term.md)：$D^{p-1}G=a^p$、$\chi$ 与完整加权 exact 补项。
