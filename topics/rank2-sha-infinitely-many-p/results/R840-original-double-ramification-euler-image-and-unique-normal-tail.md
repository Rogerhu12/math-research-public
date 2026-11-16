# R840 — 原二倍分歧 Euler 像、唯一第二法向值与同一末尾标量

日期：2026-11-16。**状态：已证明。指定 forcing 的实际成员性及主目标仍未完成。**

[R836](R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)
把原三长核写为受限 $D_3$ 方程及一个真实 $\mathcal H_1$ 镜轴像。
本篇支付更深的有限像：原 $G\mapsto\mathcal E^2G$ 在整个 $2Z$
上的余核仍只有原负水平的 $z_-\le2$ 个值。
在实际高前缀之后，第二法向值若存在则唯一；
同前三个曲线值的全部修正仅剩 $cF^3$。
这个同一标量必须支付第三长尾和第四短行，不能分别选取。

还给出 $2Z$ 与原点前缀的完整同一全局留数对偶。
其中所有分歧厚化、奇点、原十九角及负水平都保留；
没有把未加前缀的全像认成受限像满射。

## 1. 同一个原格与实际长度

沿用 R833/R834/R836 的实际数据
$$
C=(F=0),\quad P=(0,1),\quad
N=\mathcal O_C(C),\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),
$$
$$
\kappa=C^2,\quad\chi=-K_XC>0,\quad
\mathcal E=Y\partial_Y,\quad e=\mathcal EF.
\tag{1}
$$
$C$ 几何整且是原光滑曲面上的 Cartier 曲线；
$P$ 光滑，$e(P)\ne0$。记
$$
Z=(e|_C),\qquad 2Z=(e^2|_C),\qquad
\operatorname{length}Z=\kappa,\quad
\operatorname{length}(2Z)=2\kappa.
\tag{2}
$$
这里 $2Z$ 是同一 Cartier 除子的二倍，不是两个独立的 $Z$ 值。

保持真实返回
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D},
\quad q_{\rm src}(P)\ne0,\quad
3b<p,\quad b=\deg_YF,
\tag{3}
$$
以及原轴 $g=\psi e^\eta$、$\operatorname{ord}\eta=h$，
$$
\boxed{h<T\le2h,\qquad T>2\kappa.}
\tag{4}
$$
因此 $h>\kappa$。原四块物理矩阵中取
$$
T=s-r-13,\qquad
\ell_{\rm eff}=\max(\ell-r,0)<T,\qquad
q_T=T-h,
$$
$$
\ell_0=\min(\ell_{\rm eff},q_T),\qquad
H_*=h+\ell_0=\min(T,h+\ell_{\rm eff}).
\tag{5}
$$
相对 $J_4$ 如单独使用则另取 $T=s-r$。
原 $G_0$、charge 四十、$P_{134}/U_0$ 和三条十三行带按 R836
作完整单位下三角运输，不能以 (5) 提前除去非单位前缀。

下文所有 $\mathcal E$ 都是该运输后的相对 Euler。
它在全十九角的线束格中保持 $\mathcal H_j$。
不是把 raw 微分次数当成全局截面条件。

## 2. 原 $\mathcal E^2$ 在整个 $2Z$ 上的完整像

记
$$
\mathscr Z_3^{(2)}=H^0(2Z,N^3|_{2Z}),\qquad
Z_-=C\cap H_-,
\quad z_-=C.H_-=u-\mu_{d,1}-\mu_{\infty,1}.
$$
原全部 $r=2$ profile 已由 R833 支付 $0\le z_-\le2$。

**定理 1。** 原实际算子
$$
J_{2Z}:\mathcal H_3\longrightarrow\mathscr Z_3^{(2)},
\qquad G\longmapsto(\mathcal E^2G)|_{2Z}
$$
满足
$$
\boxed{
\operatorname{im}J_{2Z}
=\ker\!\left[\mathscr Z_3^{(2)}
 \longrightarrow H^0(Z_-,N^3|_{Z_-})\right],
\qquad
\dim\operatorname{coker}J_{2Z}=z_-.
}
\tag{6}
$$
特别，厚化到 $2Z$ 没有把这个全像余核变成 $2z_-$。

**证明。** R495 的原消失给
$\mathcal H_3\twoheadrightarrow H^0(C,N^3)$。
又
$$
0\to N\xrightarrow{\ e^2\ }N^3\to N^3|_{2Z}\to0
$$
中的 $H^1(C,N)=0$，因为
$\deg(\omega_C N^{-1})=-\chi<0$；
这里在原 Gorenstein 整曲线上用 Serre 对偶，不先换成正规化。
故原限制满射，且其来源核准确为
$$
\boxed{
\ker[\mathcal H_3\to\mathscr Z_3^{(2)}]
=F\mathcal H_2+e^2\mathcal H_1.
}
\tag{7}
$$
确实，限制在 $2Z$ 上为零的曲线截面可除以 $e^2$，
所得 $N$ 截面由同一 $\mathcal H_1$ 提升；
余项才除以 $F$。这支付了 (7) 的全局来源，而非只在仿射环求商。

$3b<p$ 使每个正 charge 的平方 $n^2$ 为单位，所以
$\mathcal E^2\mathcal H_3=\mathcal H_3^{>0}$。
由 (7)，余核准确为
$$
\mathcal H_3/
(\mathcal E^2\mathcal H_3+F\mathcal H_2+e^2\mathcal H_1)
\simeq\mathcal H_3^0/(F_0\mathcal H_2^0).
\tag{8}
$$
$e^2$ 没有零 charge。
R833 的整个负水平限制为
$\mathcal H_j^0=d^{j\mu_{d,1}}k[t]_{\le jz_-}$，
所以 (8) 是 $Z_-$ 上的自然值商，长度为
$(3z_-+1)-(2z_-+1)=z_-$。

相对 Euler 的线性化在 $H_-$ 上权为零，
故 $\mathcal E^2G$ 的 $Z_-$ 限制为零。
$Z_-\subset Z\subset2Z$ 是概形包含，
有限概形的限制满射与 (8) 合起来给 (6)。
全部非约化部分、无穷远和剩余域均在自然限制中。证毕。

## 3. 两个全局值决定一个真实 $2Z$ 类

令 $D_3$ 为 R836 的同源映射
$$
D_3:H^0(C,N^3)\to H^0(Z,N^3|_Z),\qquad
D_3(V)=(\mathcal EG)|_Z.
$$
定义实际兼容对空间
$$
\mathscr P=
\{(V_0,V_1)\in H^0(C,N^3)^2:
D_3(V_0)=V_1|_Z\}.
\tag{9}
$$
R836 已付：每一这样的对由某个原 $G\in\mathcal H_3$ 实现
$G|_C=V_0,\ (\mathcal EG)|_C=V_1$；
所有实现之差恰为 $F^2\mathcal H_1$。

因此以下是良定义的真实线性映射：
$$
\boxed{
\mathfrak D_2:\mathscr P\to\mathscr Z_3^{(2)},\qquad
\mathfrak D_2(V_0,V_1)
=(\mathcal E^2G)|_{2Z}.
}
\tag{10}
$$
其原因是准确的全局恒等式
$$
(\mathcal E^2(F^2L))|_C=2e^2L|_C,
\tag{11}
$$
在 $2Z$ 为零。并且
$$
\boxed{
\mathfrak D_2(V_0,V_1)|_Z=D_3(V_1).
}
\tag{12}
$$
所以 (10) 的第一层和第二层不能自由分配。
未加前缀时，(10) 的全像就是 (6)；
给定兼容对后，它是一个固定值，并非可另调的补列。

对任意 $H>\kappa$，
$$
\boxed{
H^0(C,N^3(-HP))\longrightarrow\mathscr Z_3^{(2)}
\quad\text{单射},
}
\tag{13}
$$
因为核为 $H^0(C,N(-HP))=0$。
这将用于 $H=H_*$；没有由 (6) 推断 (13) 的像等于整个 (6)。

## 4. 指定 forcing 的第二值唯一，最后只剩同一个 $cF^3$

先照 R836 检验指定原目标属于实际
$w^{13+r}\bar\Gamma^{(4)}$，再用原完整单位逆与已读前缀
得到三个长目标 $f_0,f_1,f_2\in k[[t]]/t^T$
及第四目标 $f_3\in k[[t]]/t^{\ell_{\rm eff}}$。
本篇不跳过这个低行检验。

前两个全局值必须属于实际仿射纤维
$$
[V_0]_{<T}=f_0-\eta f_1,\qquad
[V_1]_{<T}=f_1-\eta f_2,
\qquad (V_0,V_1)\in\mathscr P.
\tag{14}
$$
纤维可为空；固定 $V_0$ 后兼容的 $V_1$ 至多一个，
如 R836 的原 $Z$ 单射所证。

对同一兼容对，第二法向值须满足
$$
\boxed{
V_2|_{2Z}=\mathfrak D_2(V_0,V_1),\qquad
[V_2]_{<H_*}=f_2-\eta f_3,
\quad V_2\in H^0(C,N^3).
}
\tag{15}
$$
右侧只用 $f_3$ 的 $<\ell_0$ 行；
因为 $\eta$ 起于 $h$，没有任意延长一个未读的短目标。
由 (13)，(15) 若可解，则 $V_2$ 唯一。

**引理 2。** 一旦 (15) 成立，存在原 $G_2\in\mathcal H_3$ 同时实现
$$
G_2|_C=V_0,\quad
(\mathcal EG_2)|_C=V_1,\quad
(\mathcal E^2G_2)|_C=V_2.
\tag{16}
$$
全部实现准确为 $G_2+kF^3$。

**证明。** 先取实现前两值的 $G_1$。
(15) 使
$(V_2-(\mathcal E^2G_1)|_C)/(2e^2)$
成为真正全局 $N$ 截面。
取它的同源 $\mathcal H_1$ 提升 $L$，
置 $G_2=G_1+F^2L$，由 (11) 得 (16)。
若差仍为 $F^2L$ 且第二值也不变，则 $e^2L|_C=0$。
$C$ 整且 $e$ 非零，所以 $L|_C=0$，即 $L=cF$。
反向显然。证毕。

设
$$
\sigma_F(t)=6e(t,\psi(t))^3\eta(t)\pmod{t^T}.
$$
全部有限 Taylor 项给
$$
\boxed{
F^3(t,g)=\mathcal E(F^3)(t,g)=0\pmod{t^T},\qquad
\mathcal E^2(F^3)(t,g)=\sigma_F(t)\pmod{t^T}.
}
\tag{17}
$$
首两式分别用 $3h\ge T$、$2h\ge T$；
第三式保持全 $e(t,\psi)$ 和 $\eta(t)$，不是只留首系数。
$\operatorname{ord}\sigma_F=h$，其首系数
$6e(P)^3\eta_h$ 是单位。

令
$$
d_2=f_2-(\mathcal E^2G_2)(t,g)\pmod{t^T}.
$$
由 (15) 的低 $h$ 行，$d_2\in t^h$。
第三长行可解当且仅当
$$
\boxed{d_2\in k\,\sigma_F.}
\tag{18}
$$
若可解，其标量唯一，并且准确为
$$
c=\frac{[t^h]d_2}{6e(P)^3\eta_h},\qquad G^*=G_2+cF^3.
\tag{19}
$$
因此只需在使用这一个 $c$ 后检验
$t^{h+1},\ldots,t^{T-1}$ 的余行。
换一个 (16) 的提升会同步平移 (19) 的 $c$，$G^*$ 不变。

由 (14)、第三长行及 $\eta^2=0\bmod t^T$，
同一个 $G^*$ 的第一、第二长行也分别等于 $f_0,f_1$，
恰如 R836 的有限逆 Taylor 证明。
没有把三块分别用不同的来源解掉。

## 5. 第四短行的前段就是第二值的额外高前缀

在 (18) 已解后，有准确式
$$
\boxed{
\eta\,(\mathcal E^3G^*)(t,g)
\equiv f_2-V_2\pmod{t^T}.
}
\tag{20}
$$
确实，写 $W_j=(\mathcal E^jG^*)|_C$，
则第三长行为 $V_2+\eta W_3=f_2$，
而 $\eta\,\mathcal E^3G^*(t,g)=\eta W_3$ 模 $t^T$。

因 $q_T=T-h\le h$，
$$
(\mathcal E^3G^*)(t,g)
\equiv(f_2-V_2)/\eta\pmod{t^{q_T}}.
\tag{21}
$$
(15) 正好使 (21) 的前 $\ell_0$ 行等于实际 $f_3$。
因此：

- 若 $\ell_{\rm eff}\le q_T$，第四短行全部已经由 (15) 的
  同一个 $V_2$ 和 (18) 支付。
- 若 $\ell_{\rm eff}>q_T$，仍须读取同一个 $G^*$ 的
  $q_T,\ldots,\ell_{\rm eff}-1$ 行，准确剩余长度
  $\ell_{\rm eff}-q_T$。

这不允许为第四块再改 $c$。
特别 $\mathcal E^3F^3(t,g)$ 的常数为 $6e(P)^3$，
故第四块确实会感受到同一个标量；
若读到 $\eta$ 阶，还必须保它的完整高尾。

对零目标，(15) 为
$$
V_2\in H^0(C,N^3(-H_*P)).
\tag{22}
$$
当 $\ell_{\rm eff}\ge q_T$ 时，$H_*=T$，
于是 $V_0,V_1,V_2$ 都在 $V_T$；
(12) 进一步给真正的第二步兼容
$D_3(V_1)=V_2|_Z$。
这只是在同一实际核中的有限链，
不认整个 $V_T$ 对 Euler 稳定。

由此，(14)、(15)、(18) 及上述剩余第四尾
是 R836 指定目标在原 (3) 子格中的一个完整同来源判据。
它不宣称其中的未知成员性已经自动满足或自动失败。

## 6. 两处目标的完整 Serre 左行

(15) 可以直接检验为一个完整全局留数条件，
无需先任选一组 $2Z$ 值，再另补原点高前缀。

令 $\mathscr L=N^3$，并在原 $C$ 上取
$$
D_*=2Z+H_*P.
$$
真正精确序列为
$$
0\to N(-H_*P)\to N^3\to N^3|_{D_*}\to0.
\tag{23}
$$
由 $H_*>\kappa$，其首项没有全局截面；
又 $H^1(C,N^3)=0$。
所以整个联合评价单射，且其余核准确为
$H^1(C,N(-H_*P))$，对偶空间是
$$
\boxed{
\mathcal Q_{H_*}^{(2)}
=H^0(C,\omega_C N^{-1}(H_*P)).
}
\tag{24}
$$
其维数由原 Riemann–Roch 精确为
$$
\dim\mathcal Q_{H_*}^{(2)}
=H_*-\frac{\kappa+\chi}{2}.
\tag{25}
$$
没有用正规化替换原算术亏格，也没有在此补上自由的局部主部。

记 $z_2=\mathfrak D_2(V_0,V_1)$，
$j_2=[f_2-\eta f_3]_{<H_*}$。
则 (15) 可解当且仅当对每个同一个全局
$\omega\in\mathcal Q_{H_*}^{(2)}$，
$$
\boxed{
\sum_{Q\in\operatorname{supp}Z}
\operatorname{Res}^{C}_{Q}
 \frac{\widetilde z_2\,\omega}{e^2}
+
\operatorname{Res}_{P}
 \frac{\widetilde j_2\,\omega}{e^2}
=0.
}
\tag{26}
$$
各项使用原线束的相容局部框；乘积是标量微分，
换框不改配对。$2Z$ 或 $H_*P$ 上的代表改变只添正则的
对偶化微分，故留数不变。
奇点处的符号 $\operatorname{Res}^{C}$ 指原 Gorenstein/Rosenlicht
配对：在正规化上取全部分支的和及剩余域迹，并保导子条件。
不是普通 Artin 代数迹，也不是各分支上可自由选择的行。
(26) 正是 (23) 连接映射与完整 Serre 对偶的非退化配对。

因此 (6) 的至多二维未加前缀余核，
并不删去 (24)–(26) 的实际长前缀左行。

## 7. 指定分歧迹、原余列与精度范围

R822 的实际分歧 GRes 读取 $\mathcal E^2R|_Z$。
在当前真子格 $R=q_{\rm src}t^rG$ 中，它准确为
$$
\left.\mathcal E^2R\right|_Z
=t^r\left(
q_{\rm src}\,\mathfrak D_2(V_0,V_1)|_Z
+2(\mathcal Eq_{\rm src})V_1|_Z
+(\mathcal E^2q_{\rm src})V_0|_Z
\right).
\tag{27}
$$
所以一旦前两个全局值固定，后面的 $F^2\mathcal H_1$ 和最终 $cF^3$
都不能再单独改变这批指定分歧值。
(27) 保留实际余因子的两项 Euler 导数；
不能只把它读成裸 $q_{\rm src}\mathfrak D_2$。
同样，R822 的全局微分依赖的
$$
(\mathcal ER)|_C
=t^r\bigl(q_{\rm src}V_1+(\mathcal Eq_{\rm src})V_0\bigr)
$$
也由同一兼容对固定。
这为指定 trace 提供实际的联合输入，没有证明它与 (26) 自动相等、
自动为零或自动延拓到一个允许的全局 $\omega$。

本篇只支付 (3) 的原全截面子格。
整个 $\mathcal W_D$ 的其余列、原低行右逆高尾、same-$R$ 的下一位、
原两条／三条十三行带及 $p^4$ 末端 quartic $p^3$ 项继续保持。
原固定中央失效到整个深核的桥仍未完成。
没有把 full $2Z$ 像、(25) 的维数或一个局部单位当作全原 $M$ 的非零障碍。
