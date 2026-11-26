# R1024：原完整首 log 向量对全部 $p\equiv11\bmod12,\ p\ge47$ 非零

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
o2_high_coefficient / root；global_route 提供 R1023 的原几何来源。

**已证明：在 R1023 的同一个原 Jacobian 和原点
$P=(p-1)D_0$ 上，形式对数准确具有深度 $m=(p-1)/2$。**
这里排除的是完整首向量所有分量同时为零，没有将某个指定分量
预先当成单位，也没有删掉原 Hasse 多项式的任何根。
证明为有限代数恒等式及五阶有理系数的纸面推导，不依赖素数窗口。

## 1. 准确结论和唯一输入

设
$$
p=12g-1\ge47,\quad m=(p-1)/2,\quad
\pi_0^{(p^2-1)/2}=p,\quad \varepsilon=\pi_0^m.
$$
全部对象和整 Lie 格仍为 R1023：
$$
\log_{\mathcal J}(P)\equiv
\varepsilon\sum_{s\in S}
 \theta_s\bigl(\lambda(s)+R_p(s)\bigr)f_s
\pmod{\pi_0^{m+1}}.
$$
**定理 1024.1。**
$$
\boxed{\quad
\log_{\mathcal J}(P)\in
\pi_0^m\operatorname{Lie}(\mathcal J/R)
\setminus
\pi_0^{m+1}\operatorname{Lie}(\mathcal J/R).
\quad}
\tag{1024.1}
$$
因此整个 Lie 格中的准确 $p$-赋值为 $1/(p+1)$。

令
$$
\ell=4g,\qquad d=2g-1,\qquad
q(y)=Q_p(y),\qquad \ell=2d+2,\quad p=3\ell-1.
$$
$q$ 是 R1023 的实际 monic Hasse 因子，简单根避开 $0,1$，并满足
$$
y(1-y)q''+\frac43(1-2y)q'-\frac{25}{36}q=0.
\tag{1024.2}
$$
记
$$
P_1=T_{\le\ell}\frac1{(1-y)q^2},\qquad
P_2=T_{\le\ell}\frac{(1-y)^{\ell-1}}{q^2}.
$$
R1023 已严格证明：原完整首 log 为零当且仅当
$$
q\mid P_1-y^\ell,\quad q\mid P_2-y^\ell,\quad P_2(1)=1.
\tag{1024.3}
$$
本篇证明这三个条件不可能同时成立。特别保留第三个条件，它来自
原 $b=0$ SS 尾，不能用另外两个条件自动替代。

## 2. 两个原截断的准确一阶方程

反设 (1024.3)，写
$$
P_1=y^\ell+qU,\qquad P_2=y^\ell+qU_2,\qquad
\deg U,\deg U_2\le d+2.
$$
因为 $(1-y)^{-1}q^{-2}$ 被一阶算子
$$
L_1=(1-y)q\,\partial_y+2(1-y)q'-q
$$
消去，截断恒等给
$$
L_1P_1=y^\ell F_1,\qquad \deg F_1\le d.
$$
在每个简单根 $\alpha$ 处，$P_1(\alpha)=\alpha^\ell$，所以
$$
F_1(\alpha)=2(1-\alpha)q'(\alpha).
$$
于是 $F_1=2(1-y)q'+k_1q$，其中 $k_1$ 为常数。
代回并除以 $q$，令 $A=k_1+1+\ell$，得到
$$
(1-y)qU'+[3(1-y)q'-q]U
 =y^{\ell-1}(Ay-\ell).
\tag{1024.4}
$$
$A$ 是此式的未知常数，不是原 Hasse 多项式 $A_p$。

同理，$(1-y)^{\ell-1}q^{-2}$ 被
$$
L_2=(1-y)q\,\partial_y+2(1-y)q'+(\ell-1)q
$$
消去。相同的根处比较给
$$
(1-y)qU_2'+[3(1-y)q'+(\ell-1)q]U_2
 =y^{\ell-1}((k_2+1)y-\ell).
$$
原中心条件 $P_2(1)=1$ 迫 $U_2(1)=0$，再在此式代 $y=1$
得 $k_2=\ell-1$。故可写
$$
U_2=(1-y)V,\qquad \deg V\le d+1,
$$
而准确方程成为
$$
(1-y)qV'+[3(1-y)q'+(\ell-2)q]V
 =-\ell y^{\ell-1}.
\tag{1024.5}
$$
此步没有在 $q$ 的根处擅自增加一个导数消失条件。

## 3. 两个方程迫出次数至多二的多项式

在每个 $q$ 的根 $\alpha$，(1024.4)–(1024.5) 给
$$
3(1-\alpha)q'(\alpha)U(\alpha)
 =\alpha^{\ell-1}(A\alpha-\ell),
$$
$$
3(1-\alpha)q'(\alpha)V(\alpha)
 =-\ell\alpha^{\ell-1}.
$$
所以
$$
W=\frac{(Ay-\ell)V+\ell U}{q}
\tag{1024.6}
$$
为次数不超过二的多项式。由原截断的常数项，
$U(0)=V(0)=q(0)^{-3}$，故 $W(0)=0$。

置
$$
h=q/q(0),\quad c=A/\ell,\qquad
ay+by^2=q(0)^4W/\ell.
$$
在模 $y^\ell$ 的有限截断环中，
$$
U\equiv(1-y)^{-1}q^{-3},\qquad
V\equiv(1-y)^{\ell-2}q^{-3}.
$$
因此
$$
h^4(ay+by^2)\equiv
 (1-y)^{-1}-(1-cy)(1-y)^{\ell-2}
 \pmod{y^\ell}.
$$
这里 $\ell\equiv1/3\pmod p$，且所用截断次数小于 $p$；
乘合法的 $(1-y)^{5/3}$，得到
$$
\boxed{\quad
\mathcal G(y)(ay+by^2)\equiv
 (1-y)^{2/3}-1+cy\pmod{y^\ell},
\qquad
\mathcal G=(1-y)^{5/3}h^4.
\quad}
\tag{1024.7}
$$
这是同一个原 $q$ 的有限恒等式，不是换一个形式相似的多项式。

## 4. 原 ODE 的前五阶已导致矛盾

由 (1024.2) 和 $h(0)=1$，低次递推恰为
$$
h(y)={}_2F_1(5/6,5/6;4/3;y)
$$
在所需有限次数的模 $p$ 约化。只需
$$
h_0=1,\quad h_1=\frac{25}{48},\quad
h_2=\frac{3025}{8064},\quad
h_3=\frac{874225}{2903040},\quad
h_4=\frac{462465025}{1811496960}.
\tag{1024.8}
$$
这些数逐项由
$$
h_{j+1}/h_j=
 \frac{(j+5/6)^2}{(j+4/3)(j+1)}
$$
取得。于是
$$
\mathcal G=
1+\frac5{12}y+\frac{1705}{8064}y^2
+\frac{69595}{580608}y^3
+\frac{733145495}{10144382976}y^4+O(y^5).
\tag{1024.9}
$$
下面 §5 保留四次系数的完整纸面算式，以便独立复核。

而 (1024.7) 右边的 $y,\ldots,y^5$ 系数为
$$
c-\frac23,\quad -\frac19,\quad-\frac4{81},
\quad-\frac7{243},\quad-\frac{14}{729}.
$$
由前三阶，
$$
a=c-\frac23,\quad b+\frac5{12}a=-\frac19,\quad
\frac{1705}{8064}a+\frac5{12}b=-\frac4{81},
$$
所以
$$
a=-\frac{224}{2745},\qquad b=-\frac{127}{1647}.
\tag{1024.10}
$$
第四和第五阶还同时要求
$$
E_4=
 \frac{69595}{580608}a+\frac{1705}{8064}b+\frac7{243}
 =\frac{108439}{39844224}=0\quad\text{于 }\mathbf F_p,
\tag{1024.11}
$$
$$
E_5=
 \frac{733145495}{10144382976}a
 +\frac{69595}{580608}b+\frac{14}{729}
 =\frac{11227003}{2762532864}=0\quad\text{于 }\mathbf F_p.
\tag{1024.12}
$$
所有显示分母的素因子只可能是
$2,3,5,7,13,61$，没有一个落在 $p\ge47,\ p\equiv11\bmod12$
这一行。又 $\ell\ge16$，所以 (1024.7) 确实允许比较至 $y^5$。

但两个必要分子满足明确的整数式
$$
\boxed{\quad
1290641\cdot108439-12466\cdot11227003=1.
\quad}
\tag{1024.13}
$$
没有任何素数能同时使它们为零。这与 (1024.11)–(1024.12) 矛盾，
排除 (1024.3)，完成定理 1024.1。

## 5. 系数与两个残差的完整纸面核准

令 $\mathcal H=h^4$。直接卷积给
$$
\mathcal H_1=25/12,\quad
\mathcal H_2=25225/8064,\quad
\mathcal H_3=11943775/2903040.
$$
其四次系数由五项组成：
$$
\mathcal H_4=
4h_4+12h_1h_3+6h_2^2+12h_1^2h_2+h_1^4.
$$
取公共分母 $L=50721914880$，五项的分子依次为
$$
51796082800,\quad95465370000,\quad42824925000,\quad
61936875000,\quad3732421875.
$$
总和为 $255755674675$。
$(1-y)^{5/3}$ 的四个后继系数为
$-5/3,5/9,5/81,5/243$，所以
$$
\mathcal G_4=
\mathcal H_4-\frac53\mathcal H_3+\frac59\mathcal H_2
                 +\frac5{81}\mathcal H_1+\frac5{243}.
$$
在同一分母 $L$ 下，后四项分子为
$$
-347802728000,\quad88146240000,\quad6522880000,\quad1043660800.
$$
全部相加为 $3665727475$，约去五便是 (1024.9) 的四次系数。

对于 (1024.11)，三个项在分母 $39844224$ 下的分子为
$$
-389732,\quad-649605,\quad1147776;
$$
和为 $108439$。
对于 (1024.12)，先取分母 $24862795776$，三个分子为
$$
-146629099,\quad-229802690,\quad477474816;
$$
和为 $101043027$，分子分母同除九即 (1024.12)。

最后，(1024.13) 两个乘积准确为
$139955819399$ 与 $139955819398$，差为一。
以上 o2 与 root 分别作完整纸面重算；不以程序返回的有理数或 gcd
作为核准依据。

## 6. 后继边界与来源

(1024.1) 为整个原 $\mathcal J$ 的结论。它不指定哪一个 SS
分量非零，尤其不声称 $b=0$ 分量必非零。
它不把全向量单位自动转成 R1011 所选非 CM 简单商的整单位，
不保证某个指定 CM jet 的 Chabauty 首项为单位，也不完成 O0
中的其它全局支路。

本篇使用：

- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)：原 entire-Jacobian 首 log 公式、准确 Hasse $Q_p$ 和三条件等价式。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)：原点的准确形式首层，与本篇 log 首层不可在证明前混同。
- [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)、[R1019](R1019-original-CM-killing-correspondences-preserve-first-formal-layer.md)：实际非 CM 商及 CM-killing 对应，保留其整投影的开放条件。
- [执行路径纠正](../notes/2026-11-26-execution-path-deviation-and-correction.md)：global_route 的违规 V8 探索及数值复核不作为本篇证据；这里使用 o2 与 root 的独立纸面推导及上列可逐项核查的整数式。

Serre 主目标仍 OPEN。继续实际非 CM 整投影及原候选排除。


## 后继：单一角色的充分大范围

[R1026](R1026-original-single-remainder-and-integral-CM-annihilating-log-direction.md)
不再联合第二整除或中心条件，而以同一个 $P_1,Q_p$ 的
固定特征零解析来源证明充分大 $p$ 的单一非整除，
继而给实际杀 CM 的整 Lie 方向。它与本篇覆盖全部
$p\ge47,\ p\equiv11\bmod12$ 的 whole-vector 定理互不替换。


## R1038：另一个模十二行的实际应用

[R1038](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md)
补完 $p\equiv5\bmod12$ 的实际 Raynaud、整最低型、
双节点与完整首 log 后，逐项核对本篇 §§2–5 的代数证明
不依赖 $\deg q$ 的奇偶。
它因此给本行全部 $p\ge41$ 的原良好 $B$ 部分及实际
最低型首 log 准确深度 $m$。
本篇的“整个好约化 Jacobian”对象不直接移到该半稳定行。
