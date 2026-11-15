# R660 — 原范数一坐标、完整边界轨道与中央正规解的共振理想

日期：2026-11-15。**状态：已证明。**

本篇在 R639 的同一完整中央规范中，给出闭边界缺口的一个实际原系数形式。
原范数一形式 CM 作用可以用整可逆坐标完全线性化；首边界的
$p^2-1$ 个点据此变成一个 degree $p-1$ Eisenstein 多项式的全部根。
原中央源的完整轨道和是一个整级数 $B_m$。

各个边界点局部无对数的条件恰为 $Q_p\mid B_m$。
更强地，若 R639 的原唯一正规解属于闭边界 Tate 代数，则
$$
Q_p^{\,p+1-m}\mid B_m,\qquad
v_p(B_m(0))\ge p+1-m,\qquad m=34,72.
$$
这里 $B_m(0)$ 准确等于原 $[z^{p+1}]A_m$。
结合原全局 Hurwitz 整性和复增长，闭边界条件在充分大 $p$ 时甚至迫这个有理系数严格为零。

这些是已证明的局部判据和闭盘必要条件。原 $j_m=0$ 只给严格内盘；
本文没有把它升级为上述高次理想。

## 1. 原参数、原 Euler 来源与完整规范

固定
$$
p\equiv5\pmod6,\quad p>101,\quad
d=p+1,\quad e=p-1,\quad b=17,\quad
K_p=\mathbf Q_p(\omega),\quad \mathcal O=\mathcal O_{K_p}.
$$
保持
$$
u=x^{-1/2},\quad x=u^{-2},\quad
y=-u^{-3}(1+bu^6)^{1/2},\quad
C(u)=(1+bu^6)^{-1/2},\quad z'(u)=C(u).
\tag{1}
$$
原形式对数 $z=uH(bu^6)$ 和原 zeta 的 Laurent 函数
$$
\Xi(u)=\zeta_{\rm W}(z(u))
=\frac1u\sum_{n\ge0}
 \frac{\binom{-1/2}{n}b^nu^{6n}}{1-6n}
\tag{2}
$$
都在 $0<|u|<1$ 解析；除所示原点极外没有该开盘内的极点。
分母仅按指标对数增长，故 (2) 的收敛性直接成立。

令
$$
F_{\rm c}=\Pi_0\log(\sigma/z),\quad E_{\rm c}=e^{F_{\rm c}},
\quad T=T_{\rm g},\quad
E_{\rm c}=(\sigma/z)T(u),\quad T^{\pm1}\in1+u^2\mathcal O[[u]].
\tag{3}
$$
这些全是 R639 的原对象。中央投影为
$$
\Pi_0 f(z)=\frac1d\sum_{\zeta\in\mu_d}f(\zeta z).
$$
原两条 Euler 来源是
$$
A_m(z)=\sigma(z)^m\phi_m(x(z),y(z)),\qquad m=34,72,
\tag{4}
$$
其中 $\phi_{34}=x^2F_4(x^3)$、$\phi_{72}=x^3F_4(x^3)F_6(x^3)$，
在原点的极阶分别为 $28=m-6$ 和 $66=m-6$。
全部原多项式系数在当前 $\mathcal O$ 中整。

原 $G_{m,{\rm c},0}(X)$、$\mathcal R_m(X)$、$X=z^d$ 满足
$$
G_{m,{\rm c},0}=\Pi_0(E_{\rm c}^{-m}A_m),\qquad
(\partial_X+mF_{\rm c}')\mathcal R_m=G_{m,{\rm c},0}/X,
\qquad\mathcal R_m(0)=j_m.
\tag{5}
$$
R639 已证明 $\mathcal R_m$ 在每个严格 $r<r_E$ 的闭 $X$ 盘上 Tate，其中
$$
R_E=p^{-1/(p^2-1)},\qquad r_E=R_E^d=p^{-1/e}.
\tag{6}
$$
(4) 是完整 Euler 源；此处没有把另一个已经除去 $z^6$ 的来源放进 (5)。

## 2. 整形式 CM 作用的真实线性坐标

对 $\zeta\in\mu_d\subset\mathcal O^\times$，形式级数
$$
\alpha_\zeta(u)=u(\zeta z(u))
$$
是一个整形式群自同构：
$$
\boxed{\alpha_\zeta(u)\in u\mathcal O[[u]],\quad
\alpha_\zeta'(0)=\zeta,\quad
\alpha_\zeta\circ\alpha_\eta=\alpha_{\zeta\eta}.}
\tag{7}
$$

具体证明如下。标准参数 $t=-x/y=u(1+bu^6)^{-1/2}$ 与 $u$ 整可逆。
原好约化模型的全局 CM 乘法在 $t$、从而在 $u$ 中有整系数。
取 $a_n\in\mathbf Z[\omega]$ 趋于 $\zeta$。
每个固定形式系数在
$u(a_nz(u))$ 中是 $a_n$ 的一个固定有理多项式，故逐系数连续。
它是整系数的极限，给 (7)；组合公式同样由极限保持。
$\alpha_{\zeta^{-1}}$ 给整逆。
因此这些映射在整个 $|u|<1$ 解析并保持绝对值，且
$$
z(\alpha_\zeta(u))=\zeta z(u)
\tag{8}
$$
在这个开盘成立。这使用真实形式 CM，而非在边界外直接代入原对数的局部逆。

定义
$$
\boxed{v(u)=\frac1d\sum_{\zeta\in\mu_d}\zeta^{-1}\alpha_\zeta(u).}
\tag{9}
$$
因 $d$ 是单位，
$$
v(u)\in u+u^2\mathcal O[[u]],\qquad
v(\alpha_\eta(u))=\eta v(u).
$$
其形式逆也整，故 (9) 是整个开单位盘上的等距解析坐标。
其导数在该盘处处为单位：所有非线性导数项的绝对值严格小于一。

把 (8) 改写到这个坐标，字符比较给
$$
\boxed{z(u)=v(u)H_p(W),\quad W=v(u)^d,\quad
H_p(W)\in1+WK_p[[W]].}
\tag{10}
$$
$H_p$ 在 $|W|<1$ 收敛。
$H_p$ 不被称为整级数；原对数的小分母仍在 (10)。

## 3. 完整中央源恰给一个整级数

令
$$
F_m(u)=T(u)^{-m}\phi_m(x(u),y(u)).
$$
它在 $u$ 的 Laurent 展开属于
$u^{-(m-6)}\mathcal O[[u]]$。
在 (9) 的整逆坐标中，写成
$$
F_m(u(v))=\sum_{n\ge6-m}f_{m,n}v^n,\qquad f_{m,n}\in\mathcal O.
$$
定义原完整轨道和
$$
\Phi_m(u)=\frac1d\sum_{\zeta\in\mu_d}
                  \zeta^mF_m(\alpha_\zeta(u)).
\tag{11}
$$
投影准确只保 $n\equiv-m\pmod d$。
由于 $m<d$ 且 $-m<6-m$，允许的首阶是
$\ell_m=d-m>0$，于是
$$
\boxed{
\Phi_m(u)=v(u)^{\ell_m}B_m(W),\qquad
B_m(W)=\sum_{j\ge0}f_{m,\ell_m+jd}W^j\in\mathcal O[[W]].
}
\tag{12}
$$
这包括全部 $p+1$ 个 CM 支、所有相位、$T$ 和原椭圆多项式。
没有在模 $p$ 后才定义 $B_m$。

由 $E_{\rm c}$ 的完整中央不变性，
$$
G_{m,{\rm c},0}(z^d)=z^m\Phi_m(u).
$$
结合 (10)–(12)，得到准确形式身份
$$
\boxed{
G_{m,{\rm c},0}\!\left(WH_p(W)^d\right)
       =WH_p(W)^mB_m(W).
}
\tag{13}
$$
特别其首系数是
$$
\boxed{
B_m(0)=g^{\rm c}_{m,1}=[z^d]A_m(z).
}
\tag{14}
$$
最后一步因为 $A_m(0)=0$，而 $E_{\rm c}^{-m}=1+O(z^d)$。
所以此首系数也等于原首 Gaussian 规范的第一中央系数，未重新定义算术行。

## 4. 全部首边界点的 Eisenstein 多项式

R635 证明：原 $z(u)$ 在首边界 $|u|=R_E$ 恰有
$p^2-1$ 个非零简单零点，它们就是原形式群的非零 $p$ 挠点；
其余首闭盘内零点仅有原点。记这些点为 $u_T$。

(7) 保持这些点，且 $\mu_d$ 作用自由。
确实在 (9) 中该作用是 $v\mapsto\zeta v$，而 $v(u_T)\ne0$。
因此它们分为恰 $e=p-1$ 个轨道。
每个轨道的
$$
\xi=W(u_T)=v(u_T)^d
$$
相同，不同轨道的 $\xi$ 不同；所有 $\xi$ 都满足 $v_p(\xi)=1/e$。

定义
$$
\boxed{Q_p(W)=\prod_{\mu_d\text{ 轨道}}(W-\xi).}
\tag{15}
$$
点集及 (9) 的系数都在 $K_p$ 上 Galois 相容，故 (15) 的系数在 $K_p$。
这些值确在有限局部扩张内：在包含原挠点的完备有限扩张中评价整收敛级数即可。
各非首项系数的根赋值下界严格为正；由于 $K_p$ 未分歧、赋值为整数，得到
$$
\boxed{
Q_p\in\mathcal O[W],\quad \deg Q_p=e,\quad
Q_p(W)\equiv W^e\pmod p,\quad v_p(Q_p(0))=1.
}
\tag{16}
$$
所以它是一个真正的 Eisenstein 多项式，其 $e$ 个根互异。
这不是仅按根的数目指定一个形式模 $p$ 多项式。

## 5. 每个边界点的准确共振与对数系数

在原严格内盘令
$$
R_m(u)=\mathcal R_m(z(u)^d).
$$
(3)、(5) 给准确微分方程
$$
\boxed{
R_m'+m\left(\Xi C+\frac{T'}T-\frac C z\right)R_m
      =d\,C\,z^{m-1}\Phi_m(u).
}
\tag{17}
$$
等式先在原盘成立；各系数在首边界附近有上述明确的亚纯延拓。
其中 $-C/z=-z'/z$ 在每个 $u_T$ 的留数是 $-1$。

固定一个这样的点，用真实局部坐标 $t=z(u)$，
$u=u_T(t)$；因 $z'(u_T)=C(u_T)\ne0$，此坐标合法。
记
$$
a_T(t)=m\left(\Xi(u_T(t))+
             \frac{d}{dt}\log T(u_T(t))\right).
$$
它在 $t=0$ 解析。缩小局部盘后，存在解析单位
$L_T(0)=1$、$L_T'+a_TL_T=0$。
将 $R=t^mL_T V$ 代入 (17)，准确得到
$$
V'=\frac{d\,\Phi_m(u_T(t))}{tL_T(t)}.
$$
因而全部形式局部解是
$$
\boxed{
R=t^mL_T(t)\left\{
c_T+d\Phi_m(u_T)\log t+
\int_0^t
 \frac{d\Phi_m(u_T(s))/L_T(s)-d\Phi_m(u_T)}{s}\,ds
\right\}.
}
\tag{18}
$$
括号内积分是一个实际局部解析零初值函数；将盘再缩小即可支付积分分母。
对数系数正是完整轨道和 $d\Phi_m(u_T)$。

由 Laurent 系数直接比较可知：

**局部判据。** (17) 在 $u_T$ 有亚纯解芽，当且仅当
$\Phi_m(u_T)=0$；这时全部亚纯解芽其实解析，且阶至少 $m$。

确实若 Laurent 首阶低于 $m$，其在 (17) 左端产生不能由右端抵消的最低阶；
在首阶 $m$ 处的唯一共振系数正是 (18) 的留数。
$\Phi_m(u_T)=0$ 时，(18) 无对数，给全部解析解。
这个陈述是局部存在性，不断言原点选定的 $\mathcal R_m$ 已经到达该解芽。

由 (12)、(15)，全部首边界点同时通过这个局部判据，恰等价于
$$
\boxed{Q_p\mid B_m\quad\text{于 }\mathcal O[[W]].}
\tag{19}
$$
为支付整除的环，写 $Q_p=W^e+pR(W)$，$\deg R<e$。
先按 $W^e$ 分解，再把出现的 $W^e$ 换成 $Q_p-pR$，逐次校正；
每轮误差多含一个 $p$，在 $\mathcal O[[W]]$ 的逐系数完备拓扑收敛。
这给整 quotient 和 degree $<e$ 的整 remainder。
若 $B_m$ 在全部 $e$ 个根消失，则 remainder 也消失，故为零。
反向显然。相同论证适用于 $Q_p$ 的任意固定正幂和相应重数。

## 6. 原闭 X 盘强迫更高的实际理想

现在假设比 R639 已付结论更强的条件
$$
\mathcal R_m\in K_p\langle X/r_E\rangle .
\tag{20}
$$
R635 给 $\|z(u)\|_{R_E}=R_E$，所以
$\mathcal R_m(z(u)^d)$ 是整个闭 $u$ 盘上的 Tate 函数。
将 (17) 清去所示 $u,z$ 极点后，两侧在该闭盘解析；
原点邻域的身份因此延到这个同一闭盘。
此步骤正是 (20) 额外支付的连通解析身份，不能从严格内盘自动得到。

在每个边界点，所取同一个函数局部准确为
$$
R_m(u_T(t))=\mathcal R_m(t^d).
$$
(17) 的简单极迫 $\mathcal R_m(0)=j_m=0$。
因此若它不恒零，其阶至少为 $d$。
方程左侧阶至少 $d-1$，而右侧为
$d\,t^{m-1}\Phi_m(u_T(t))$。
于是
$$
\operatorname{ord}_{u_T}\Phi_m\ge d-m=\ell_m .
$$
$v(u_T)\ne0$，且 $W'(u_T)\ne0$，所以 $B_m$ 在每个 $\xi$ 的零阶也至少 $\ell_m$。
由上节整除论证：

**定理。** 原闭盘条件 (20) 必须满足
$$
\boxed{
j_m=0,\qquad Q_p^{\,\ell_m}\mid B_m\text{ 于 }\mathcal O[[W]],
\quad \ell_m=p+1-m.
}
\tag{21}
$$
若 $B_m=\sum b_{m,n}W^n$，则更准确地
$$
\boxed{
v_p(b_{m,n})\ge
\max\!\left(0,\ell_m-\left\lfloor\frac n{p-1}\right\rfloor\right).
}
\tag{22}
$$
这是 (16) 的整系数及根赋值给出的 Newton 下界：
$Q_p^{\ell_m}$ 的第 $j$ 个系数赋值至少
$\ell_m-j/e$，取整数上界，再与整 quotient 卷积即可。
特别由 (14)，
$$
\boxed{
v_p([z^{p+1}]A_m)\ge p+1-m.
}
\tag{23}
$$
条件 (21) 比局部无对数的 (19) 强。它仍只是闭盘必要条件，
不反过来保证各局部解与原点解粘合，或保证全部 $t^d$ 同时下降条件。

## 7. 同一原系数的全局 Hurwitz 整性

为使 (23) 的算术强度明确，直接支付原系数的整数分母。
在原 $z$ 时间中取
$$
U=u(z),\quad R=(1+bU^6)^{1/2},\quad B=R^{-1},\quad
V=\zeta_{\rm W}+x^2/y,\quad A=\sigma/U .
$$
它们都在原点正则，初值为 $(0,1,1,0,1)$，满足整多项式系统
$$
\boxed{
U'=R,\quad R'=3bU^5,\quad
B'=-3bU^5B^2,\quad
V'=3bU^4B^2,\quad
A'=(V-bU^5B)A .
}
\tag{24}
$$
这些是原恒等式，(24) 没有改变时间或删 Gaussian。
整多项式向量场在整初值处的任意迭代导数都是整数，
故每个坐标的全部 $n!$ Taylor 系数整。

写
$$
P_4(t)=\frac{(1+t)(1-8t)(7-4t+16t^2)}7,\qquad
P_6(t)=(1+4t)(1-96t+48t^2+64t^3)(1+20t-8t^2).
$$
原 (4) 准确为
$$
A_{34}=U^6A^{34}P_4(bU^6),\qquad
A_{72}=U^6A^{72}P_4(bU^6)P_6(bU^6).
$$
所以 $7A_m$ 是 (24) 的一个整多项式，直接得到
$$
\boxed{7n![z^n]A_m(z)\in\mathbf Z\qquad(n\ge0,\ m=34,72).}
\tag{25}
$$
这不是只在当前惰性素数处的整性。

## 8. 闭边界条件在大素数处迫原有理系数为零

原 $A_m$ 在复平面上整：$\phi_m$ 仅在周期格有极，
其阶 $m-6$ 被 $\sigma^m$ 的零完全消掉。
sigma 准周期公式和 $\phi_m$ 的椭圆周期性给固定常数
$c_0,c_1>0$，使
$$
|A_m(z)|\le c_0e^{c_1|z|^2}\qquad(z\in\mathbf C).
\tag{26}
$$
为核其全平面量词，将 $z=z_0+\lambda$，$z_0$ 在一个固定基本平行四边形内。
$A_m(z_0)$ 有界，准周期指数是 $m\eta_\lambda(z_0+\lambda/2)$，
而 $|\eta_\lambda|=O(|\lambda|)$，所以得到 (26)，含格点邻域。

Cauchy 取 $r^2=n/(2c_1)$，再用 $n!\le n^n$，给
$$
\log|7n![z^n]A_m|
\le\frac n2\log n+O_m(n)
\tag{27}
$$
只要该整数非零。常数固定，与 $n,p$ 无关。
令 $n=p+1$。由于 $p>101$，
$$
v_p(7(p+1)!)=1.
$$
若闭盘条件 (20) 成立而 $[z^{p+1}]A_m\ne0$，
(23)、(25) 使这个非零整数被 $p^{p+2-m}$ 整除，从而
$$
(p+2-m)\log p
\le\frac{p+1}{2}\log(p+1)+O_m(p).
$$
对充分大的 $p$，左侧主项是 $p\log p$，右侧主项只有其一半，矛盾。

因此存在只依赖原固定来源的 $p_0$，使
$$
\boxed{
p>p_0,\quad\mathcal R_m\in K_p\langle X/r_E\rangle
\quad\Longrightarrow\quad [z^{p+1}]A_m(z)=0.
}
\tag{28}
$$
这里的零是特征零有理系数的准确零，不是模 $p$ 的零。
本文未证明这个系数沿所有惰性素数都非零，也没有把 (28) 当作主目标。

## 9. 完整接口的范围

R639 原 $j_m=0$ 等价于零初值正规解在所有严格 $r<r_E$ 盘解析。
本篇的 (19)、(21)、(23) 则逐项描述了跨到真实边界时必须支付的全轨道共振条件。
它们不是由 $j_m=0$ 或严格内盘上的一致范数界自动得到的。

尤其，在某个边界点直接写下 $\mathcal R_m(t^d)$ 当然给一个局部解析函数；
没有 (20) 时，它不必满足从原点延来的 (17)。
将这种局部重写误当同一全盘解析身份，会删除正是 (18) 显示的共振缺项。

所有投影和新坐标都完整保留原 $T_{\rm g}$、两 source 的真极帽和全部 $p+1$ 个 CM 支。
$Q_p,B_m,v$ 依赖当前 $p$，不是原固定全局来源格中的免费列。
本篇不替换旧同一个 $R$ 的 forcing，也不给七原函数或其乘积添加算术中央零。
原普通全补偿与固定曲线无穷素数的主目标继续开放。

依赖：
[R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)；
[R635](R635-all-original-powers-and-formal-logarithm-boundary.md)；
[R632](R632-original-pth-power-formal-group-boundary-and-full-kummer-range.md)；
[R644](R644-bounded-degree-original-polynomials-and-full-boundary-obstruction.md)；
[R652](R652-original-regular-polynomial-flow-and-quantitative-jet-bound.md)。
