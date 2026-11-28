# R1133：原尖点 Kummer 坐标的 primitive 单位方程与 full-level Heisenberg 源

日期：2026-11-28（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** 对每个 $p>37$，完整原曲线 $X=X_{\rm ns}^+(p)$ 的每个实际非零
cuspidal $p$-torsion 角色，都能由一个具体 Weierstrass 单位方程的加权 Cartan
范数，以模 $p$ 单位恢复。原函数不取 $12p$ 次幂；原整数指数、实下降、
全部 cusp leading、同一个 Weil root 和 R1064 的无基点归一化均保留。

在 full-level 开曲线上，同一单位方程还给一个写出全部方程和群作用的
有限 étale Heisenberg torsor。本文没有将它称为原 proper $X$ 上的非交换覆盖：
范数后的全部 crossed corestriction 项在 §7 明写；尖点、高层以及 coarse
下降尚须另证。本文没有由单位生成或低阶 torsor 推出有理点排除。

全文为纸面证明，没有数学程序执行。

## 1. 原域、角色、整数指数与几何商

固定
$$
K=\mathbf Q(\zeta_p),\quad F=K^+,\quad
m=(p-1)/2,\quad G=\operatorname{Gal}(F/\mathbf Q).
\tag{1133.1}
$$
沿用 R1062、R1064、R1070 的实际
$$
V=C_\Sigma[p]=U_p/pU,\qquad
V_\chi\ne0,\qquad \chi=\omega^r,\quad r\text{ 为偶数}.
\tag{1133.2}
$$
每个这样的 $V_\chi$ 恰一维。采用同一个非平方 $\delta$、原
$\mathbf F_{p^2}=\mathbf F_p(\sqrt\delta)$、原实际 $p$-torsion 标记
$z\mapsto P_z$ 和 Weil pairing $\zeta_p$。

令 $G=\mathbf F_p^\times/\{\pm1\}$，选 R1064 的整数指数
$$
n_h\equiv m^{-1}\chi(h)^{-1}\pmod p,\qquad
\sum_{h\in G}n_h=0.
\tag{1133.3}
$$
记 $u_\chi\in V_\chi$ 为这些指数固定的原基，$[F_\chi]$ 为
R1064 (1064.4)–(1064.5) 中的规范泛点 Kummer 类：
若 $\widetilde u_\chi$ 是一个实际 modular-unit 代表，则
$$
[F_\chi]=
\left[\frac{\widetilde u_\chi^{\,m}}
 {A(\widetilde u_\chi)}\right]
\in F(X)^\times/F(X)^{\times p}.
\tag{1133.4}
$$
改变允许的代表或局部参数只改 $p$ 次幂，不能另选不明常数。

在固定 Weil pairing 的连通 full-level 曲线 $Z=X(p)_K$ 上，
$Z\to X_K$ 的几何 deck 群是
$$
D=(N_{\rm ns}\cap{\rm SL}_2(\mathbf F_p))/\{\pm I\},
\qquad |D|=p+1.
\tag{1133.5}
$$
这不是把整个 $\mathbf F_{p^2}^\times$ 当成几何 deck 群。
范数一 Cartan 部分作用为 $z\mapsto tz$、$Nt=1$；
另一个陪集作用为 $z\mapsto \alpha\bar z$、$N\alpha=-1$。
因此 $D$ 在 $\mathbf F_{p^2}^\times/\{\pm1\}$ 上的轨道准确是
$[Nz]=h$ 的完整纤维，各有 $p+1$ 个元素。

这几个轨道上作用均自由：Cartan 部分只有已除掉的 $\pm1$ 能固定
$z/\pm$；非 Cartan 元在二维空间的平方是 $-I$，不可能将非零 $z$
送到 $\pm z$ 后再固定它。这里讨论的是 level 向量上的自由作用；
不将 $Z\to X_K$ 在椭圆 coarse 点的分歧擅自删去。

## 2. 实际 Weierstrass 单位方程

对整数
$$
3\le a\le m
\tag{1133.6}
$$
及非零 $P\in E[p]$，定义
$$
B_a(P)=\frac{x([2]P)-x(P)}{x([a]P)-x(P)},\qquad
A_a(P)=\frac{x([a]P)-x([2]P)}{x([a]P)-x(P)}.
\tag{1133.7}
$$
于是有实际函数恒等式
$$
A_a(P)+B_a(P)=1.
\tag{1133.8}
$$
全部 $a,a\pm1,a\pm2$ 均非零模 $p$。对椭圆曲线，
$x(Q)=x(R)$ 当且仅当 $Q=\pm R$；
故 (1133.7) 中各个分子、分母在非 cusp full-level 开曲线上均不为零。
这些函数是该开曲线上的实际单位，零、极点只可能在 compactification 的 cusps。

一般 Weierstrass 变量替换的 $x$ 变化为 $x\mapsto v^2x+s$。
两个差同时乘 $v^2$，所以 (1133.7) 不依赖模型或 invariant differential。
又有 $A_a(-P)=A_a(P)$、$B_a(-P)=B_a(P)$，故采用 $P/\pm$ 无代表歧义。

原标准 division polynomials 满足
$$
x([n]P)-x(P)
=-\frac{\psi_{n+1}(P)\psi_{n-1}(P)}{\psi_n(P)^2},
\qquad \psi_1=1.
\tag{1133.9}
$$
因此
$$
B_a(P)=
\frac{\psi_3(P)\psi_a(P)^2}
 {\psi_2(P)^2\psi_{a+1}(P)\psi_{a-1}(P)},
\tag{1133.10}
$$
$$
A_a(P)=
\frac{\psi_{a+2}(P)\psi_{a-2}(P)}
 {\psi_2(P)^2\psi_{a+1}(P)\psi_{a-1}(P)}.
\tag{1133.11}
$$
第二式也直接来自 Ward identity
$$
\psi_{a+2}\psi_{a-2}
=\psi_{a+1}\psi_{a-1}\psi_2^2-\psi_3\psi_a^2.
\tag{1133.12}
$$
例如 $a=3$ 时，原等式就是
$$
\frac{\psi_5}{\psi_4\psi_2^3}
+\frac{\psi_3^3}{\psi_4\psi_2^3}=1.
\tag{1133.13}
$$
式中没有 $p$ 分母，也没有先把 Siegel 函数取 $p$ 次幂。
(1133.9) 可由同一模型的 multiplication formula，或 Stange 已刊
Lemma 3.5 的 $\wp$–$\sigma$ 公式直接得到；(1133.12) 是其已刊 Eq. (1)。

## 3. 原 half Cartan 产品与严格实下降

按同一实际标记定义
$$
\mathcal B_{a,\chi}
=\prod_{z\in\mathbf F_{p^2}^\times/\{\pm1\}}
 B_a(P_z)^{-n_{[Nz]}},
\quad
\mathcal A_{a,\chi}
=\prod_{z\in\mathbf F_{p^2}^\times/\{\pm1\}}
 A_a(P_z)^{-n_{[Nz]}}.
\tag{1133.14}
$$
两者在 $D$ 下均严格不变，故属于 $K(X)^\times$。
原复共轭的 determinant $-1$ 运输是 $z\mapsto\bar z$，允许同时加负号；
(1133.7) 的代数式固定、范数指标不变、两个函数又都为偶函数。
故严格有
$$
\mathcal A_{a,\chi},\mathcal B_{a,\chi}\in F(X)^\times.
\tag{1133.15}
$$
这里没有 Siegel 根单位相位可任意删除。

若 $z_h$ 是 $D$ 的一个轨道代表，则等价地
$$
\mathcal B_{a,\chi}
=\prod_{h\in G}
 \operatorname{Nm}_{K(Z)/K(X)}(B_a(P_{z_h}))^{-n_h},
\tag{1133.16}
$$
另一个函数同理。这是 degree $p+1$ 的真实范数，每个轨道恰数一次；
没有额外除二或除 $p+1$。

改变 (1133.3) 的整数提升，差为 $p$ 倍、augmentation 仍零，
所以 (1133.14) 只改变实际 modular unit 的 $p$ 次幂。
本篇保持与 R1064 相同的提升，不将这些函数换成别的符号格。

## 4. 精确恢复原 Kummer 坐标

回读 R1070 §9 的全部非零向量乘积：
$$
M_c^{\rm all}=\prod_{z\ne0}\psi_c(P_z)^{-n_{[Nz]}},
\qquad
\kappa_\chi(c)=c^2-\chi(c^2).
\tag{1133.17}
$$
该节对任意正整数 $c$、$p\nmid c$ 支付实际函数、偶数平滑、
全部 leading 和共同 theta 常数；$c=1$ 取 $M_1^{\rm all}=1$。
具体是
$$
[M_c^{\rm all}]_V=2\kappa_\chi(c)u_\chi,\quad
[A(M_c^{\rm all})]=0,\quad
[M_c^{\rm all}]=\frac{2\kappa_\chi(c)}m[F_\chi].
\tag{1133.18}
$$
最后一个等式在 $F(X)^\times/F(X)^{\times p}$ 中成立，包括
$\kappa_\chi(c)=0$。它由前两个式和原规范定义得到，
不是只在某些点取值后才成立。

这里共同 $\Theta$–$\psi_c$ 比较常数是对每个固定 $c$ 的 $\lambda_c(E)$，
它在整个 $M_c^{\rm all}$ 中以 $\sum_{z\ne0}n_{[Nz]}=0$ 次幂出现并严格消去。
不能在未形成完整原产品前逐因子任意删常数。

由 (1133.10)，精确函数等式为
$$
\mathcal B_{a,\chi}^{\,2}
=\frac{M_3^{\rm all}(M_a^{\rm all})^2}
 {(M_2^{\rm all})^2M_{a+1}^{\rm all}M_{a-1}^{\rm all}}.
\tag{1133.19}
$$
平方正是 half 与 all 的区别；偶数 $\psi_c$ 的负号已由 all-vector 源支付。

置 $f_\chi(t)=\chi(t^2)$（$t\ne0$），并写
$$
D_\chi(t)=f_\chi(t+1)+f_\chi(t-1)-2f_\chi(t),\qquad
d_\chi(a)=D_\chi(a)-D_\chi(2).
\tag{1133.20}
$$
这里只在 $t=2,a$ 使用 $D_\chi$，没有把 $f_\chi(0)$ 当作字符值。
直接展开有
$$
\kappa_\chi(3)+2\kappa_\chi(a)-2\kappa_\chi(2)
-\kappa_\chi(a+1)-\kappa_\chi(a-1)=d_\chi(a).
\tag{1133.21}
$$
核常数时，左侧整数平方部分准确为 $-1$，而 $f_\chi(1)=1$；
两项共同给右式，不能单删其中一项。

因为 $p$ 为奇数，(1133.18)–(1133.21) 给出
$$
\boxed{
[\mathcal B_{a,\chi}]_V=d_\chi(a)u_\chi,\qquad
[A(\mathcal B_{a,\chi})]=0,\qquad
[\mathcal B_{a,\chi}]=\frac{d_\chi(a)}m[F_\chi].
}
\tag{1133.22}
$$
特别 $\operatorname{div}\mathcal B_{a,\chi}$ 为 $p$ 倍；
可先由其平方的 divisor 为 $p$ 倍，再用 $p\nmid2$ 得到这一点。
leading 式同样由平方的完整 leading 类为零推出。

因此只要 $d_\chi(a)\ne0$，原全标签准确为
$$
\boxed{
\Phi_y(u_\chi)=\frac m{d_\chi(a)}
 [\mathcal B_{a,\chi}(y)].
}
\tag{1133.23}
$$
在 cusp 使用同一个去除 $p$ 倍参数的 leading 值。
这保持同一个实际 $y$、同一 cyclotomic embedding 和所有原圆单位尺度。

原 $A$ 范数也有完整公式。若
$$
e_\chi(a)=\kappa_\chi(a+2)+\kappa_\chi(a-2)
-\kappa_\chi(a+1)-\kappa_\chi(a-1)-2\kappa_\chi(2),
$$
则
$$
[\mathcal A_{a,\chi}]=\frac{e_\chi(a)}m[F_\chi].
\tag{1133.24}
$$
同一 $\chi$ 的这两个范数类共线；它们自身的 alternating cup 为零
不会提供第二个独立 Kummer 方向。

## 5. 每个实际角色都有可逆的单位方程

由 R1070 §10，实际非零 $V_\chi$ 中既没有 $\chi^2=1$，
也没有使 $\chi(t^2)=t^2$ 的边界角色。
后者在 $p\equiv3\pmod4$ 时是实际缺席的 $\omega^{m+1}$，
在 $p\equiv1\pmod4$ 时没有偶解。

取 $2r\bmod(p-1)$ 的最小非负代表 $k$。于是
$$
k\text{ 为偶数},\qquad 4\le k\le p-3,\qquad
f_\chi(t)=t^k\quad(t\in\mathbf F_p^\times).
\tag{1133.25}
$$
令
$$
P_\chi(T)=(T+1)^k+(T-1)^k-2T^k
-\bigl(3^k+1-2\cdot2^k\bigr).
\tag{1133.26}
$$
它是偶多项式，
$$
\deg P_\chi=k-2,\qquad
\operatorname{lc}(P_\chi)=k(k-1)\ne0\pmod p,\qquad
P_\chi(\pm2)=0,
\tag{1133.27}
$$
且 $P_\chi(a)=d_\chi(a)$。

若 $d_\chi(a)=0$ 对所有 $3\le a\le m$ 成立，偶性连同 $\pm2$
使 $P_\chi$ 在 $\mathbf F_p\setminus\{0,1,-1\}$ 的 $p-3$ 个元素上为零。
但其次数至多 $p-5$，矛盾。因此
$$
\boxed{\text{对每个实际 }V_\chi\ne0，
\text{存在 }3\le a\le m\text{ 使 }d_\chi(a)\in\mathbf F_p^\times.}
\tag{1133.28}
$$
更精确地，坏的正代表至多 $(k-4)/2$ 个，所以
$$
\#\{a\in[3,m]:d_\chi(a)\ne0\}\ge\frac{p-1-k}{2}\ge1.
\tag{1133.29}
$$
也可只查 $3\le a\le k/2+1$：若这个较短范围全为零，
连同 $\pm2$ 已给 $k$ 个不同根，仍超过次数 $k-2$。
这些都是纸面次数界，不是数值窗口。

例如 $k=4$ 时，$P_\chi(T)=12(T^2-4)$，$a=3$ 给 $d_\chi(3)=60$，
在 $p>37$ 为单位；这一例只说明相应角色出现时的源尺度，
不声称该角色对所有 $p$ 都出现。

由 (1133.22)、(1133.28)，选整数 $b_\chi$ 满足
$b_\chi d_\chi(a)\equiv m\pmod p$，则
$\mathcal B_{a,\chi}^{b_\chi}$ 是同一个 $[F_\chi]$ 的实际代表。
所以这些明确 unit-equation 的加权范数恢复整个原 $V$ 的所有坐标，
不只 forced 或 Bernoulli-good 子模块。
是否有唯一全局标签仍按 R1069、R1128 的原条件处理，未被本篇替代。

## 6. 显式 full-level 开曲线 Heisenberg torsor

本节只在固定 $K$ 上的 full-level 开曲线 $\mathscr Y=Y(p)_K$ 工作。
取某个 $a,z$，缩写
$$
U=A_a(P_z),\qquad W=B_a(P_z),\qquad U+W=1.
$$
两者都是 $\mathscr Y$ 上的实际单位，故已有整 Steinberg 关系
$\{U,W\}=0$。下面给出与之相同的显式低 cochain，而不只引用 cup 为零。

依次取
$$
\alpha^p=U,\qquad \beta^p=W,\qquad
\gamma^p=\mathcal D(\alpha),\qquad
\mathcal D(\alpha)=\prod_{i=0}^{p-1}(1-\zeta_p^i\alpha)^i.
\tag{1133.30}
$$
在第一步代数中，
$$
\prod_{i=0}^{p-1}(1-\zeta_p^i\alpha)=1-\alpha^p=W
\tag{1133.31}
$$
为单位，所以各个因子及 $\mathcal D$ 都是单位。
$p$ 在基域中可逆，三步均有限 étale，总秩恰 $p^3$。

定义保持原基曲线的三个自同构：
$$
\begin{array}{c|ccc}
 &\alpha&\beta&\gamma\\ \hline
\sigma&\zeta_p\alpha&\beta&(1-\alpha)\gamma/\beta\\
\tau&\alpha&\zeta_p\beta&\gamma\\
\nu&\alpha&\beta&\zeta_p\gamma .
\end{array}
\tag{1133.32}
$$
关键的完整等式为
$$
\frac{\mathcal D(\zeta_p\alpha)}{\mathcal D(\alpha)}
=\frac{(1-\alpha)^p}{W}.
\tag{1133.33}
$$
所以 (1133.32) 确保持三条方程。又由 (1133.31)，
$$
\sigma^p=\tau^p=\nu^p=1,\qquad
\nu\text{ 中心},\qquad \tau\sigma=\nu^{-1}\sigma\tau.
\tag{1133.34}
$$
例如 $\sigma^p(\gamma)=W\gamma/\beta^p=\gamma$。
在每个几何纤维，先用 $\sigma,\tau$ 选定 $\alpha,\beta$，
再用 $\nu$ 选定 $\gamma$，作用单传递。
因此 (1133.30) 是实际阶 $p^3$ Heisenberg 群的 torsor，
即使总空间不连通也成立。

这一构造保原 $\zeta_p$，不需要取大幂或除以 $p$。
它只证明 full-level open 上每个 primitive pair 的真实低阶提升。
它没有证明 cusp 上无分歧，没有证明该非交换 torsor 的 coarse 或
$\mathbf Q$ 下降，也没有证明原各范数坐标之间的 cup 为零。

## 7. 原范数的完整交叉项

令 $L=K(Z)$、$M=K(X)$，使用 (1133.5) 的真实群 $D$。
对任意实际单位方程 $U+W=1$，$K_2$ transfer 的 projection formula 给
$$
\begin{aligned}
\{\operatorname{Nm}_{L/M}U,\operatorname{Nm}_{L/M}W\}
&=\operatorname{Cor}_{L/M}
 \{U,\operatorname{res}_{L/M}\operatorname{Nm}_{L/M}W\}\\
&=\sum_{d\in D}\operatorname{Cor}_{L/M}\{U,dW\}\\
&=\boxed{\sum_{\substack{d\in D\\d\ne1}}
 \operatorname{Cor}_{L/M}\{U,dW\}}.
\end{aligned}
\tag{1133.35}
$$
只删除了 $d=1$ 的实际 Steinberg 项。
这个式子是整 $K_2$ 恒等式，没有除以 $|D|$，
也没有将 $\operatorname{Nm}U+\operatorname{Nm}W$ 误写成一。

加权范数更须保不同轨道。若在第 $h$ 个轨道取
$U_h=A_a(P_{z_h})$、$W_h=B_a(P_{z_h})$，
并用两组原整数指数 $n_h,n'_k$，则
$$
\left\{\prod_h(\operatorname{Nm}U_h)^{-n_h},
       \prod_k(\operatorname{Nm}W_k)^{-n'_k}\right\}
=
\sum_{h,k}n_hn'_k
 \sum_{d\in D}\operatorname{Cor}_{L/M}\{U_h,dW_k\}.
\tag{1133.36}
$$
一般只能先删除 $h=k,d=1$ 的项。
不同角色、不同 $a$ 的组合也必须保其完整双和；
不能用各槽单独平滑可逆，推断平滑与 Manin row 混合交换。

左侧按 §3 定义在 $F(X)$。
式 (1133.35)–(1133.36) 在 $K(X)$ 中进行实际 field transfer；
随后需要下降时，$[K:F]=2$ 是 $p$ 单位，restriction–norm 保原 $p$-primary
信息，但不会自行杀掉右侧交叉项。

## 8. 与实际后继目标的准确接口

本篇完成了三个不同层次：

1. 用实际 $x$ 坐标差给出 $A_a+B_a=1$，两槽均是原 full-level 单位。
2. 完整原 $V_\chi$ 的每个坐标，由这些第二槽的加权范数以原尺度恢复。
3. 对每个 full-level primitive pair，已给真正 Heisenberg torsor 的整方程。

待付的是 (1133.36) 的原交叉项如何在指定关系中相消，
以及所需 higher cochain、cusp 无分歧和原 coarse/arithmetic 下降。
[R1132](R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md)
与
[整关系提升笔记](../notes/2026-11-28-original-integral-Manin-relations-and-cusp-constants.md)
只能在一个**确已写出的实际符号组合具有有理关系**时消费；
不能替代该关系，也不能由 integral torsion 消失推出任意 $K_2/p$ 类为零。

还有一个 Tate twist 必须保留。
若 $V_\chi$ 的角色是 $\omega^r$，其实际 Kummer 群角色为
$\omega^{1-r}$。对一般常系数 $\mathbf F_p$ 的二次 obstruction，
以 $K_2/p\simeq H^2(\mu_p^{\otimes2})$ 读取时对应的是
$K_2/p$ 的 $\omega^2$ 分量；它不是 $e_0K_2$。
因此四阶 Lie 常中心的形式权和，也不能直接用 R1132 的
$\Delta$-平凡 integral torsion 结论完成。

本篇没有新固定素计算，没有重开已闭合的 $p=47$ 链；
一般 $p$ 的真实同点排除与四阶覆盖仍未完成。


## 9. 同一实际单位范数的四阶相容上链

本节把 §6 的三个根延长为同一个有限 étale 代数，而不是为不同
Steinberg 式各选一份互不相容的抽象零上链。它只完成 full-level
开曲线上的来源；原范数后的指定角色、cusp 无分歧与 arithmetic/coarse
下降仍须另付。

### 9.1. 精确的单位范数条件

更一般，设 $S$ 是一个 $p$ 可逆且固定了 $\zeta_p$ 的基概形，
$a,b\in\mathcal O(S)^\times$，并取实际 cyclic Kummer torsor
$$
C=\operatorname{Spec}_S\mathcal O_S[\alpha]/(\alpha^p-a),
\qquad \sigma_0(\alpha)=\zeta_p\alpha.
\tag{1133.37}
$$
允许 $C$ 不连通。假设给定一个**全局单位**
$f\in\mathcal O(C)^\times$，且它满足完整范数恒等式
$$
\prod_{i=0}^{p-1}\sigma_0^i(f)=b.
\tag{1133.38}
$$
这比在函数域中只知道某个 cup 为零多了具体整输入：
这里的 $f$ 及其全部 conjugates 在 $C$ 上都是单位。
不能仅由 field norm witness 推断 (1133.38) 在所需整开曲线上成立。

本篇原 primitive pair 取
$$
a=U=A_a(P_z),\qquad b=W=B_a(P_z),\qquad f=1-\alpha.
\tag{1133.39}
$$
由 $U+W=1$，式 (1133.38) 正是 §6 已付的实际单位恒等式。
本节临时使用 $a,b$ 表示两个单位，与 §2 的整数标号 $a$ 不混用。

### 9.2. 四个 binomial 根及完整循环作用

记 $F_i=\sigma_0^i(f)$，并对 $0\le j\le3$ 定义
$$
D_j=\prod_{i=0}^{p-1}F_i^{\binom{i}{j}},\qquad
\gamma_j^p=D_j.
\tag{1133.40}
$$
其中 $\binom{i}{j}=0$ 当 $i<j$，且 $D_0=b$。在 $C$ 上依次加入
四个 $\gamma_j$，得到相对 $S$ 秩 $p^5$ 的有限 étale 代数：
所有 $D_j$ 都是单位，且每一步导数 $p\gamma_j^{p-1}$ 可逆。

令
$$
c_j=\binom{p-1}{j}-(-1)^j,\qquad
d_j=c_j/p\in\mathbf Z,\qquad 0\le j\le3.
\tag{1133.41}
$$
这里 $d_0=0$，其余三个数为
$$
d_1=1,\qquad d_2=(p-3)/2,\qquad
d_3=(p^2-6p+11)/6.
\tag{1133.42}
$$
$p>37$ 保证这些都是整数。移位二项式恒等式
$$
\binom{i-1}{j}
=\sum_{k=0}^j(-1)^{j-k}\binom{i}{k}
\tag{1133.43}
$$
在 $i=0$ 用 $\binom{-1}{j}=(-1)^j$ 理解。循环移位唯一的
修正是将此值替成 $\binom{p-1}{j}$。因此实际代数上存在
$$
\sigma(\alpha)=\zeta_p\alpha,\qquad
\sigma(\gamma_j)
=F_0^{d_j}\prod_{k=0}^j\gamma_k^{(-1)^{j-k}}.
\tag{1133.44}
$$
对本篇 $f=1-\alpha$，前三个非平凡式明确为
$$
\begin{aligned}
\sigma(\gamma_1)&=(1-\alpha)\gamma_1/\gamma_0,\\
\sigma(\gamma_2)&=(1-\alpha)^{(p-3)/2}
                    \gamma_2\gamma_0/\gamma_1,\\
\sigma(\gamma_3)&=(1-\alpha)^{(p^2-6p+11)/6}
                    \gamma_3\gamma_1/(\gamma_0\gamma_2).
\end{aligned}
\tag{1133.45}
$$
$\gamma_0=\beta,\gamma_1=\gamma$ 时，第一行严格回到 §6 原
Heisenberg 作用；没有重新选择原来的低上链。

还须证明 $\sigma^p=1$，不能从每个右侧的 $p$ 次幂相同直接推断。
为此在同一个 $C$ 上暂加入全部
$$
\eta_i^p=F_i,\qquad 0\le i<p.
\tag{1133.46}
$$
这个较大代数上，令 $\sigma(\eta_i)=\eta_{i+1}$，指标模 $p$。
这是实际循环作用，故 $\sigma^p=1$。同时
$$
\gamma_j=\prod_i\eta_i^{\binom{i}{j}}.
\tag{1133.47}
$$
在 (1133.47) 上的作用正好给 (1133.44)，包括 $F_0^{d_j}$。
于是较小代数上的 $\sigma^p=1$ 也被逐式支付，而不是差一个
未定的 $\mu_p$ 相位。

### 9.3. 真正的 class-four torsor 与指定首层

令 $\tau_j$ 只把 $\gamma_j$ 乘以 $\zeta_p$，保持其他根不变。
四个 $\tau_j$ 两两交换。设 $L$ 为 $4\times4$ 的下移 nilpotent
矩阵。式 (1133.44) 对四个 $\gamma$ 的指数矩阵是
$(I+L)^{-1}$，故在相位群上的共轭准确为
$$
\sigma\tau_j\sigma^{-1}=\tau_j\tau_{j+1}\quad(0\le j<3),
\qquad
\sigma\tau_3\sigma^{-1}=\tau_3.
\tag{1133.48}
$$
因此作用群为
$$
G_4=\mathbf F_p^4\rtimes C_p,\qquad |G_4|=p^5,
\tag{1133.49}
$$
其中 $C_p$ 以一个长度 $4$ 的 unipotent Jordan block 作用。
采用 $[g,h]=ghg^{-1}h^{-1}$ 时，
$$
[\sigma,\tau_j]=\tau_{j+1}\ (j<3),\qquad
[\sigma,[\sigma,[\sigma,\tau_0]]]=\tau_3\ne1.
\tag{1133.50}
$$
这个抽象有限群的 nilpotency class 恰为 $4$，中心为
$\langle\tau_3\rangle$。这不宣称 pullback 后的实际 monodromy
一定是整个 $G_4$。

式 (1133.46) 给一个秩 $p^{p+1}$ 的
$\mathbf F_p^p\rtimes C_p$ torsor：在每个几何纤维，
$\alpha$ 的 $p$ 个选择和各 $\eta_i$ 的 $p$ 个选择受群单传递作用。
四个行向量
$(\binom{i}{j})_{0\le i<p}$ 在 $\mathbf F_p$ 上独立，因为其前
四列组成对角为 $1$ 的三角矩阵。它们的 span 在循环移位下稳定，
由 (1133.43) 可直接核定。因此核的商正是 (1133.40) 的
秩 $p^5$ 代数，它是真正的 $G_4$ torsor。
整个论证不要求这些代数连通。

为明确四阶上链的首层，可将 $G_4$ 嵌入标准的 $5\times5$
上三角 unipotent 群：
$$
\sigma\longmapsto
\operatorname{diag}(I_4+E_{12}+E_{23}+E_{34},1),
\qquad
\tau_j\longmapsto I_5+E_{4-j,5}.
\tag{1133.51}
$$
这些矩阵逐式满足 (1133.48)，并保 (1133.50) 的非零最高中心。
按这个嵌入延拓结构群，得到一个真实的 $\mathbb U_5(\mathbf F_p)$
torsor；其四个相邻 Kummer 商按原根规范依次为
$$
(a,\ a,\ a,\ b).
\tag{1133.52}
$$
它给同一个 defining system 的所有低层及顶层，而非仅给一个
去中心矩阵商。延拓结构群后的 torsor 仍可不连通。
此处没有使用任意 fourfold Massey product 的消失猜测。

对于原 $U,W$，删去 $\gamma_2,\gamma_3$ 恰恢复
(1133.30)–(1133.34)。因此本节是已经固定的 primitive cochain
的相容延长。与之相应的一般 one-exception word 也见
Efrat 的已刊 generalized Steinberg theorem；本节的整单位范数、
显式方程和开曲线无分歧由上述构造自行支付，不从 field-valued
存在性推断。

### 9.4. 原 forced 权的四阶目标及尚缺接口

这个双字母源允许考虑重复字母的真实四阶 Lie 字
$\operatorname{ad}(x_j)^3(x_k)$。记 $p=8t+\epsilon$，
$\epsilon\in\{1,3,5,7\}$。取
$$
\begin{array}{c|c}
\epsilon&(j,k)\\ \hline
1&(t-1,t+1)\\
3&(t-1,t+2)\\
5&(t-1,t+3)\\
7&(t,t+1)
\end{array}
\tag{1133.53}
$$
$p>37$ 时，两指标不同，且均在原 forced 范围
$1\le j,k\le\lfloor p/4\rfloor-1$。对应
$V_{\chi_j}$ 的原 Kummer 群权是 $\omega^{2j+1}$，所以
$$
3(2j+1)+(2k+1)=p-1.
\tag{1133.54}
$$
故若原两角色的上链与该来源相容，最高中心具有常角色。
式 (1133.50) 保证所选 Lie 字本身确实非零；这里没有以
纯形式权和断言实际 monodromy 或 arithmetic descent。

当前未付的是：怎样将原两个指定 $[F_{\chi_j}]$、
$[F_{\chi_k}]$ 接到 (1133.38) 的**同一个实际全局单位范数见证**，
并在原 coarse 曲线上保 cusp 无分歧及 Galois 相容。
尤其 (1133.24) 只说同一个 $\chi$ 的两个加权范数类成比例；
不能因此把原 $A_a,B_a$ 直接当成两个不同 forced 角色。
§7 的 crossed corestriction 完整双和仍保留。
本节也不把 §8 所述 $K_2/p$ 的 $\omega^2$ 障碍替换成
$e_0$ integral torsion。



### 9.5. 正常完成的精确 cusp moment 判据

设 $S=X\setminus\Sigma$ 是特征零光滑曲线的开子概形，
$a,b,f$ 是 (1133.37)–(1133.38) 的实际单位数据。
若某个几何 cusp $x$ 满足
$\operatorname{ord}_x(a)\in p\mathbf Z$，则 $C$ 的正常完成在
$x$ 上无惯性。在几何严格局部盘上可选一支 $\widetilde x$，
并记
$$
n_i=\operatorname{ord}_{\widetilde x}(\sigma_0^i f),\qquad
M_j=\sum_{i=0}^{p-1}\binom{i}{j}n_i\pmod p,\quad0\le j\le3.
\tag{1133.55}
$$
其余 $\gamma_j^p=D_j$ 的惯性由实际赋值直接给出。若选定的
tame generator 把参数的 $p$ 次根乘以 $\zeta_p$，则总惯性为
$$
\tau_0^{M_0}\tau_1^{M_1}\tau_2^{M_2}\tau_3^{M_3}.
\tag{1133.56}
$$
因此本节的 $G_4$ torsor 在该 cusp 的正常完成 étale，当且仅当
四个 $M_j$ 全为零。更换 $\alpha$ 支只循环平移 $(n_i)$，
低四个 binomial 行的 span 保持，故判据与该选择无关。

这个判据还可完全写成有限群环条件。令
$$
n(X)=\sum_{i=0}^{p-1}(n_i\bmod p)X^i
\in\mathbf F_p[C_p]=\mathbf F_p[X]/(X^p-1).
$$
由 $M_j=[T^j]n(1+T)$，有
$$
M_0=M_1=M_2=M_3=0
\quad\Longleftrightarrow\quad
n(X)\in(X-1)^4\mathbf F_p[C_p].
\tag{1133.57}
$$
范数恒等式只给 $M_0=\operatorname{ord}_x(b)\bmod p$；
即使 $a,b$ 的全部 cusp 阶都是 $p$ 倍，也不能删去后三个
moment。若 $M_0=M_1=M_2=0$ 而 $M_3\ne0$，删去最高中心的
class-three torsor 已在该点无分歧，但原 class-four torsor 仍有
纯最高中心惯性。

若每个 cusp 的 $\operatorname{ord}(a)$ 为 $p$ 倍且 (1133.57)
成立，则原有限 étale torsor 正常延拓为 $X$ 上的有限 étale
torsor。这是几何无分歧判据；它不要求算术 residue extension
分裂，也不把这种未分裂误当成分歧。原 forced 角色尚未获得
(1133.38) 的所需实际见证，故本节没有据此宣称原目标覆盖已完成。


## 10. 交换两槽的精确 Fourier 相容及共同低层

本节仍在原 primitive 单位方程 $U+W=1$ 上工作。
它识别 §6 的两份交换槽位的 Heisenberg torsor，并因此实际拼接
§9 的两条上链。所有公式保留同一个 $\zeta_p$ 和确切圆分常数；
没有把一个任意高上链或范数交叉项设为零。

### 10.1. 原 Fermat Kummer 开曲线上的单位 Fourier 和

先在通用开曲线
$$
\mathcal F^\circ:
\quad \alpha^p+\beta^p=1,\qquad \alpha\beta\ne0
\tag{1133.58}
$$
上证明恒等式，然后沿原
$\alpha^p=U,\beta^p=W$ 的 Kummer cover 拉回。
记
$$
\rho_i=\beta^{-i}\prod_{k=0}^{i-1}(1-\zeta_p^k\alpha),
\quad0\le i<p,\qquad
\mathcal S_j=\sum_{i=0}^{p-1}\zeta_p^{ij}\rho_i
\quad(j\in\mathbf Z/p).
\tag{1133.59}
$$
空积为 $1$，且范数恒等式给 $\rho_p=\rho_0=1$。
由 $\beta\rho_{i+1}=(1-\zeta_p^i\alpha)\rho_i$ 循环求和，
$$
\alpha\mathcal S_{j+1}
=(1-\zeta_p^{-j}\beta)\mathcal S_j,\qquad
\sum_{j=0}^{p-1}\mathcal S_j=p.
\tag{1133.60}
$$
$\alpha,\beta$ 及全部 $1-\zeta_p^i\alpha,1-\zeta_p^i\beta$ 均是
$\mathcal F^\circ$ 上的单位。第一式因此使所有 $\mathcal S_j$
互为单位倍，第二式又以同一个可逆常数 $p$ 给出它们各自的逆。
所以每个 $\mathcal S_j$ 都是实际全局单位，而不只是非零函数。
这里 $p$ 及以后出现的圆分常数都完整保留，未在原 Kummer
类中删除其赋值。

设
$$
D(T)=\prod_{i=0}^{p-1}(1-\zeta_p^iT)^i,\qquad
\lambda_p=(-1)^{m(m-1)/2}\prod_{i=1}^m(1-\zeta_p^i).
\tag{1133.61}
$$
则精确的原根相容式为
$$
\boxed{\quad
D(\alpha)D(\beta)
=\left(\frac{\lambda_p\alpha^{p-1}}{\mathcal S_1}\right)^p.
\quad}
\tag{1133.62}
$$

为证明而不遗漏常数，令
$C=D(\alpha)D(\beta)\mathcal S_1^p$。
对 $\sigma_0:(\alpha,\beta)\mapsto(\zeta_p\alpha,\beta)$ 及
$\tau_0:(\alpha,\beta)\mapsto(\alpha,\zeta_p\beta)$，(1133.59) 给出
$$
\sigma_0(\mathcal S_j)
=\zeta_p^{-j}\frac{\beta}{1-\alpha}\mathcal S_j,\qquad
\tau_0(\mathcal S_j)=\mathcal S_{j-1}.
\tag{1133.63}
$$
配上 (1133.33) 及 (1133.60)，$C$ 对这两个真实 deck 作用不变。
因它是单位，故在商
$K[U,U^{-1},(1-U)^{-1}]$ 中必为 $cU^aW^b$。

在 $\alpha\to0,\beta\to1$ 的分支，
$\mathcal S_0\to p$ 且
$\mathcal S_1=(1-\beta)\mathcal S_0/\alpha
\sim\alpha^{p-1}$，所以 $a=p-1$。
在 $\beta\to0,\alpha\to1$ 的分支，对 $i\ge1$ 有
$\rho_i=O(\beta^{p-i})$，故 $\mathcal S_1\to1$。
于是 $b=0$，且 $c=D(1)$。最后配对 $i,p-i$：
$$
D(1)=
\left(\prod_{i=1}^m(1-\zeta_p^i)\right)^p
(-1)^{\sum_{i=1}^m(p-i)}
\zeta_p^{-\sum_{i=1}^m i(p-i)}
=\lambda_p^p.
\tag{1133.64}
$$
最后一个相位为 $1$，因为
$\sum_{i=1}^m i^2=m(m+1)p/6\equiv0\pmod p$，且 $p>3$；
两个符号指数相差偶数 $m(m+1)$。
这证明了 (1133.62) 的确切常数，而非仅证明某个未知常数的倍数。

### 10.2. 原 Heisenberg 根的实际交换

在 §6 的原代数 $\gamma^p=D(\alpha)$ 中定义
$$
\widetilde\gamma
=\frac{\lambda_p\alpha^{p-1}}{\gamma\mathcal S_1}.
\tag{1133.65}
$$
式 (1133.62) 给 $\widetilde\gamma^p=D(\beta)$。
更重要的是，原 $\sigma,\tau,\nu$ 的完整作用满足
$$
\sigma(\widetilde\gamma)=\widetilde\gamma,\qquad
\tau(\widetilde\gamma)
=\frac{1-\beta}{\alpha}\widetilde\gamma,\qquad
\nu(\widetilde\gamma)=\zeta_p^{-1}\widetilde\gamma.
\tag{1133.66}
$$
例如 $\sigma(\gamma\mathcal S_1)=\zeta_p^{-1}\gamma\mathcal S_1$，
同时 $\sigma(\alpha^{p-1})=\zeta_p^{-1}\alpha^{p-1}$，
两相位准确相消。

因此交换 $U,W$ 的标准 Heisenberg 代数
$(\beta,\alpha,\widetilde\gamma)$ 与原代数实际同构，群的识别是
$$
(\sigma,\tau,\nu)\longleftrightarrow
(\tau,\sigma,\nu^{-1}).
\tag{1133.67}
$$
这不是仅用 cup 的反对称性选择另一份存在性提升。

还可核此交换严格为 involution。
由 (1133.62) 的对称性，
$$
\frac{\mathcal S_1(\beta,\alpha)\alpha^{p-1}}
     {\mathcal S_1(\alpha,\beta)\beta^{p-1}}\in\mu_p.
$$
在通用几何不可约的 Fermat 曲线上它是常数；
取 $\alpha\to0,\beta\to1$ 的同一分支得该常数为 $1$。
于是反向再用 (1133.65) 精确恢复 $\gamma$，没有另一个中心相位。

### 10.3. 同时保留两个实际三阶方向

把 §9 的塔截在 $\gamma_0,\gamma_1,\gamma_2$，
得到群 $\mathbf F_p^3\rtimes C_p$、秩 $p^4$ 的 class-three torsor。
分别对 $(U,W)$ 和 $(W,U)$ 构造，然后利用 (1133.65)–(1133.67)
识别它们的**同一实际 Heisenberg 商**。沿该商作纤维积，得到
一个秩
$$
p^4p^4/p^3=p^5
\tag{1133.68}
$$
的真实有限 étale torsor，允许总空间不连通。

群内取
$$
x=(\sigma_1,\tau_{0,2}),\qquad
y=(\tau_{0,1},\sigma_2),\qquad
z=[x,y]=(\tau_{1,1},\tau_{1,2}^{-1}).
\tag{1133.69}
$$
则
$$
[x,z]=(\tau_{2,1},1),\qquad
[y,z]=(1,\tau_{2,2}^{-1}).
\tag{1133.70}
$$
三个低括号互相独立；连同 $x,y$，它们生成整个秩 $p^5$ 的群。
这里两个不同三阶方向已经由同一代数拼接，不能再把它们视为
各自选取而尚无相容性的零上链。

同样对两份完整 class-four 塔作上述纤维积，秩为
$$
p^5p^5/p^3=p^7.
\tag{1133.71}
$$
它还保留两个独立四阶括号
$$
[x,[x,z]]=(\tau_{3,1},1),\qquad
[y,[y,z]]=(1,\tau_{3,2}^{-1}).
\tag{1133.72}
$$
但在这个具体群中
$$
[x,[y,z]]=[y,[x,z]]=1.
\tag{1133.73}
$$
所以不能把它称为完整的两生成元 free class-four 群：
混合四阶方向在这个商里尚未保留。
本节完成的是原低 Heisenberg 商、两种三阶方向及两个极端
四阶方向的实际相容拼接。

上述新 torsor 全部在同一个原 full-level open 上有限 étale。
要过 cusp，仍须对各个实际塔检查 §9.5 的 valuation moments；
要得到原不同 $V_\chi$ 的 arithmetic/coarse 覆盖，
仍须支付 §7 的交叉范数及 §9.4 的指定单位范数见证。
本节没有将这些待付条件改写成已得结论。



## 11. 原 $D(\alpha)$ 的整五项上链及有限 corestriction

本节完成一个此前仅由 Bloch 边界恒等式不能推出的相容性：
§6 的实际根代数，沿同一个五点配置路径取根时，满足完整算术
Galois 群上的五项 **上链** 恒等式。它保留 ordered Heisenberg
坐标中的二次修正，不把这个修正当成零。随后给出有限
corestriction 的准确同余式。最后仍须把指定四线/Manin 组合
在原模曲线上拼接；本节不声称已经读出 R1153 的 $z_{12}$。

### 11.1. 已刊路径来源与只除 $2$ 的整性

记 $P^\circ=\mathbf P^1-\{0,1,\infty\}$，基点为切向点
$\overrightarrow{01}$。采用 Nakamura–Wojtkowiak 的实际约定
$$
f_\sigma^\gamma=\gamma\,\sigma(\gamma)^{-1},\qquad
\log(f_\sigma^\gamma)^{-1}
=\rho_u(\sigma)X+\rho_{1-u}(\sigma)Y+
\ell i_2(u,\gamma)(\sigma)[X,Y]\pmod{\Gamma^3}.
\tag{1133.74}
$$
这里 $\gamma:\overrightarrow{01}\rightsquigarrow u$ 是同一个
étale 路径，两个 Kummer cocycle 也由它确定，不能另选根后
继续使用原 $\ell i_2$。

已刊来源为 H. Nakamura–Z. Wojtkowiak，
*Tensor and homotopy criteria for functional equations of
$\ell$-adic and classical iterated integrals*，
载 *Non-abelian Fundamental Groups and Iwasawa Theory*，
London Mathematical Society Lecture Note Series **393** (2012)，
258–310。本文消费 §4.2 (4.9)、§5.2 (5.2)–(5.3)、
§6.1 (6.12) 及 §6.4 Theorem 6.1。
[出版页](https://www.cambridge.org/core/books/abs/nonabelian-fundamental-groups-and-iwasawa-theory/tensor-and-homotopy-criteria-for-functional-equations-of-adic-and-classical-iterated-integrals/46039B9B747E29116AC38E68AA297697)
与作者全文
https://math.univ-cotedazur.fr/~wojtkow/11NakamuraWojtkowiak.pdf
定位同一篇；后者的网页缓存仍保完整正文。

该文的 $\widetilde\chi_2^u$ 是由实际根乘积定义的
$\mathbf Z_p$ 值 Kummer 字符，并且
$$
\ell i_2(u,\gamma)
=-\widetilde\chi_2^u-\frac12\rho_u\rho_{1-u}.
\tag{1133.75}
$$
因此本节所有 class-two 坐标均在 $\mathbf Z_p$ 中；
约到 $\mathbf F_p$ 仅用 $2\in\mathbf Z_p^\times$。
这里不是先取一个可能有 $p$ 分母的有理 regulator，再无条件
约模 $p$。

切向基点处的算术作用在 class-two 商上为
$$
X\longmapsto\chi_{\rm cyc}X,\quad
Y\longmapsto\chi_{\rm cyc}Y,\quad
[X,Y]\longmapsto\chi_{\rm cyc}^2[X,Y].
\tag{1133.76}
$$
理由是原实路径 $0\to1$ 的 associator 没有一次项
（同文 (5.12)）；它对 $y^{\chi_{\rm cyc}}$ 的共轭在
$\Gamma^3$ 中才出现。故本节真正保留
$\mathbf F_p(1),\mathbf F_p(1),\mathbf F_p(2)$ 三个算术系数，
未把一般 $G_K$ 限成 $\ker\chi_{\rm cyc}$。

### 11.2. 与 (1133.30) 的同根、同相位比较

先设 $K\supset\mu_p$，$u,1-u\in K^\times$。
沿同一条 $\gamma$ 取
$$
\alpha^p=u,\qquad
\eta_i^p=1-\zeta_p^i\alpha,\qquad
\beta=\prod_{i=0}^{p-1}\eta_i,\qquad
\Gamma=\prod_{i=0}^{p-1}\eta_i^i.
\tag{1133.77}
$$
于是 $\beta^p=1-u$、$\Gamma^p=D(\alpha)$；
这正是 §6 的原 $\beta,\gamma$，本节写 $\Gamma$ 以免与路径混淆。
根的规范是：在切向形式参数 $u=t$ 上，
$\alpha=t^{1/p}$，所有 $\eta_i$ 的 leading 为 $1$，
再沿同一条路径运输。乘积 $\beta$ 因而就是 leading 为 $1$
的 $(1-t)^{1/p}$；没有剩下的自由 $\mu_p$ 倍数。

对 $0\le a<p$，记
$$
R_a=\beta^{-a}\prod_{j=0}^{a-1}(1-\zeta_p^j\alpha).
$$
指标循环重排给出一个保留所有绕回项的整恒等式：
$$
\prod_{i=0}^{p-1}\eta_{i+a}^{\,i}
=\Gamma\,\beta^{-a}\prod_{j=0}^{a-1}\eta_j^p
=\Gamma R_a.
\tag{1133.78}
$$
例如 $j<a$ 时原指数从 $j-a$ 补为 $j-a+p$，
恰贡献 $\eta_j^p$，不是可以丢弃的根相位。

令 $a=\rho_u(g)$、$b=\rho_{1-u}(g)$，均约模 $p$。
原 (1133.32) 的函数域自同构写成
$$
g=\tau^b\sigma^a\nu^h.
$$
由 $\tau$ 对 $R_a$ 中 $\beta^{-a}$ 的作用，
$$
g(\Gamma)=\zeta_p^{\,h-ab}R_a\Gamma.
\tag{1133.79}
$$
另一方面，Nakamura–Wojtkowiak (5.2) 在这一层、同一根规范下
恰将 $g(\Gamma)/(\Gamma R_a)$ 的 $\zeta_p$ 指数定义为
$\widetilde\chi_2^u(g)$。所以
$$
\boxed{\quad
h=\widetilde\chi_2^u+ab,\qquad
h-\frac12ab=-\ell i_2(u,\gamma)\pmod p.
\quad}
\tag{1133.80}
$$
这付清了原 $D$ 与已刊五项式之间的实际箭头。
负号来自 (1133.74) 的逆路径 cocycle 约定；不能在改用
函数域自同构后仍把两个中央坐标写成同号。

### 11.3. 完整算术 Heisenberg cocycle

令
$$
\mathcal H=\mathbf F_p(1)\times\mathbf F_p(1)\times\mathbf F_p(2),
\qquad
(a,b,h)(a',b',h')=(a+a',b+b',h+h'+ab').
\tag{1133.81}
$$
在任意特征零基域 $K$ 上，定义
$$
h_u=-\ell i_2(u,\gamma)+\frac12\rho_u\rho_{1-u}
=\widetilde\chi_2^u+\rho_u\rho_{1-u}\pmod p.
\tag{1133.82}
$$
则 $(\rho_u,\rho_{1-u},h_u)$ 是左
$G_K$-cocycle，且在包含 $\mu_p$ 的域上就是 (1133.79)
所读的原显式 torsor。

这里可直接核微分，不靠 cup 为零的抽象存在性。
由 $f_{gh}=f_g\,g(f_h)$，
$$
f_{gh}^{-1}=g(f_h^{-1})f_g^{-1}.
$$
配上 (1133.76) 的 BCH 公式，若
$a_g=\rho_u(g)$、$b_g=\rho_{1-u}(g)$、$\chi_g=\chi_{\rm cyc}(g)\bmod p$，
则
$$
\ell i_2(gh)=\ell i_2(g)+\chi_g^2\ell i_2(h)
-\frac12\bigl(a_g\chi_g b_h-b_g\chi_g a_h\bigr).
$$
代入 (1133.82) 得
$$
h_u(gh)=h_u(g)+\chi_g^2h_u(h)+a_g\chi_g b_h,
\qquad
d h_u=-\rho_u\smile\rho_{1-u}.
\tag{1133.83}
$$
因此是真正的 class-two 提升，而非一个只在
$G_{K(u^{1/p},(1-u)^{1/p})}$ 上定义的字符。

也可从几何确认其与原根代数的同一性。
在通用 $u$ 开曲线上，绕 $0$ 和 $1$ 的两个 monodromy
有完整首层，两者交换子生成中心，故 (1133.30) 几何连通，
是自由两生成元的 exponent-$p$ class-two 商。
上述切向 leading 指定其同一个点；
这个 pointed 商由 (1133.76) 保持，给算术下降。
沿任意实际单位方程拉回可不连通，仍是原 torsor；
这里没有额外假设某个数值 $u$ 的纤维连通。

### 11.4. 五点配置中的完整有序上链式

令
$$
\xi\eta(1-\xi)(1-\eta)(1-\xi-\eta)\ne0,
$$
并按下列固定顺序取五个参数：
$$
u_1=\xi,\quad
u_2=\frac{\xi}{1-\eta},\quad
u_3=\frac{\xi\eta}{(1-\xi)(1-\eta)},\quad
u_4=\frac{\eta}{1-\xi},\quad
u_5=\eta.
\tag{1133.84}
$$
取 $M_{0,5}$ 上同一个切向基点
$(\mathbf P^1;0,t^2,t,1,\infty)$，
以及从它到
$(\mathbf P^1;0,st,s,1,\infty)$ 的同一条路径，
其中 $s=\xi/(1-\eta)$、$t=\eta/(1-\xi)$。
五个忘点映射的像基点都是 $\overrightarrow{01}$；
各条连接路径为恒等路径。
沿它们运输 (1133.77)，而不是逐项另取根。

Nakamura–Wojtkowiak Theorem 6.1 给
$$
\sum_{i=1}^5(-1)^{i-1}\ell i_2(u_i)=0
\quad\text{作为整个 }G_K\text{ 上的函数}.
\tag{1133.85}
$$
其证明逐项核度二 Lie 映射，全部潜在低项仅为
$-\frac12C_{35}+\frac12C_{35}
-\frac12C_{25}+\frac12C_{25}=0$。
所以这里不是只在 associated graded 上有五项式。
结合 (1133.75)，(1133.85) 可整地约模 $p$。

为给出原 ordered $h$ 坐标，写
$$
A=\rho_\xi,\quad B=\rho_\eta,\quad
C=\rho_{1-\xi},\quad D=\rho_{1-\eta},\quad
E=\rho_{1-\xi-\eta}.
$$
同一切向 leading 保证所有乘法根关系无额外相位：
$$
\begin{array}{c|cc}
i&\rho_{u_i}&\rho_{1-u_i}\\ \hline
1&A&C\\
2&A-D&E-D\\
3&A+B-C-D&E-C-D\\
4&B-C&E-C\\
5&B&D .
\end{array}
\tag{1133.86}
$$
这是上链值的逐点恒等式，而不只是 $H^1$ 中相等。
直接展开给
$$
AC-(A-D)(E-D)+(A+B-C-D)(E-C-D)
-(B-C)(E-C)+BD=2CD.
\tag{1133.87}
$$
由 (1133.80)、(1133.85) 得到所需同源五项式：
$$
\boxed{\quad
h_{u_1}-h_{u_2}+h_{u_3}-h_{u_4}+h_{u_5}
=\rho_{1-\xi}\rho_{1-\eta}.
\quad}
\tag{1133.88}
$$
等价地，五个 BCH 中央坐标
$h_{u_i}-\rho_{u_i}\rho_{1-u_i}/2$ 的交替和严格为零。
原 Kummer 字符则满足
$\sum_i(-1)^{i-1}\widetilde\chi_2^{u_i}=-CD$。
(1133.88) 的右端是两个一次上链在同一 $g$ 上的乘积，
不是一个二次 cup，也不能直接删除。

该证明沿任意特征零基的五点配置拉回相容。
可以在通用配置的函数域上验证，再用有限 étale pointed
cover 的唯一延拓；因此也适用于本题由实际弦交点构成的
五点配置。它不要求五项分别在基域上有一份独立且不相容的
路径选择。

### 11.5. 换路径的误差保留在哪里

若将左 cocycle $c(g)$ 改为
$q^{-1}c(g)g(q)$，其中 $q=(u,v,w)\in\mathcal H$，
则由 (1133.81)
$$
\begin{aligned}
a'(g)&=a(g)+(\chi_g-1)u,\\
b'(g)&=b(g)+(\chi_g-1)v,\\
h'(g)&=h(g)+(\chi_g^2-1)w+\chi_g a(g)v-u b(g)
 +(1-\chi_g)uv .
\end{aligned}
\tag{1133.89}
$$
特别在 $K\supset\mu_p$ 时，中央差仍可为
$a(g)v-u b(g)$。所以不能因所有原 cup 都满足 Steinberg，
就宣称任意逐项选择的 $D$ 根自动满足 (1133.88)。
同一 $M_{0,5}$ 路径及其 leading 规范，正是本节消除这个
实际误差的输入。

### 11.6. 有限 corestriction 的准确相容性

设 $L/K$ 为有限可分扩张，$H=G_L\subset G=G_K$，
对左 $G$-模 $M$ 使用非齐次连续上链。
选右陪集 $H\backslash G$ 的代表集 $\mathcal T$，写
$$
t g=h_{t,g}t_g,\qquad h_{t,g}\in H,\ t_g\in\mathcal T.
$$
一次上链的标准 transfer 为
$$
(\operatorname{Cor} f)(g)
=\sum_{t\in\mathcal T}t^{-1} f(h_{t,g}).
\tag{1133.90}
$$
二次上链用
$\sum_t t^{-1}F(h_{t,g_1},h_{t_{g_1},g_2})$；
代入 $t g_1g_2=h_{t,g_1}h_{t_{g_1},g_2}t_{g_1g_2}$
直接验证
$$
d\operatorname{Cor}=\operatorname{Cor}d.
\tag{1133.91}
$$
这是上链级构造，不需要反除 $[L:K]$，也不要求该次数为
$p$ 的单位。按同一代表集运输五条路径和所有根，
(1133.88) 给出
$$
\sum_i(-1)^{i-1}\operatorname{Cor}(h_{u_i})
=\operatorname{Cor}(CD).
\tag{1133.92}
$$
这里右端准确为
$$
\sum_{t\in\mathcal T}
\bigl(t^{-1}C(h_{t,g})\bigr)
\bigl(t^{-1}D(h_{t,g})\bigr),
\tag{1133.93}
$$
使用了 $\mathbf F_p(1)^{\otimes2}=\mathbf F_p(2)$。
它不是 $(\operatorname{Cor}C)(\operatorname{Cor}D)$；
后者还含不同 $t,t'$ 的交叉项。
因此本节既付真实 finite-field/closed-point transfer，
也保留 §7 和原 aux-$c$ 公式中不能丢掉的 crossed terms。

### 11.7. 对原中央计算的已付与未付范围

已完成的是：同一原 $D(\alpha)$ 源的完整算术 five-term
homotopy、ordered/BCH 坐标换算、同一路径的根相位规范、
以及 (1133.90) 的有限 corestriction。它可以沿实际五点配置
使用，并可纳入原四线 Bloch 表达式的更换关系。

仍须对指定 theta/Manin filling 给出实际组合，证明它在
引入辅助直线后的开集之间按这些相容式拼接，并消除全部
额外内点的中心惯性。完成那一步以后，才能使用
[R1147](R1147-original-canonical-moment-Heisenberg-lift.md)
所付原全模曲线上的 $H^1(\mathcal M,Z)=0$ 识别规范提升；
不能先在较小开集上套用该消失。
本节没有把 Bloch 的 $\delta$ 恒等式独自当成中央 cochain，
没有删除各范数之间的交叉项，也没有宣称已经计算
原 CM 参考 Frobenius 的 $z_{12}$。


## 来源及审核

- [R1064](R1064-original-cuspidal-cover-descent-and-auxiliary-character-visibility.md)
  §§1–4：原 $n_h$、真实基、$u^m/A(u)$、全 cusp leading 和函数域下降。
- [R1070](R1070-original-cuspidal-labels-by-division-polynomial-values.md)
  §§9–10：任意整数平滑的 all-vector 函数、共同常数抵消、
  $\kappa=0$ 时的实际 $p$ 次幂、完整实际角色的两个缺席边界。
- K. Stange, *Elliptic nets and elliptic curves*, Algebra & Number Theory
  **5** (2011), 197–229, DOI 10.2140/ant.2011.5.197。
  已刊全文：
  https://msp.org/ant/2011/5-2/ant-v5-n2-p03-p.pdf 。
  本文消费 Eq. (1)、Lemma 3.5 的实际除法/加法式及 §4 的代数同源；
  原模曲线范数、角色多项式和整 Heisenberg 方程均在上文逐式证明。
- I. Efrat, *Generalized Steinberg relations*, Research in Number Theory
  **8** (2022), no. 4, article 92, DOI 10.1007/s40993-022-00386-x；
  作者公开全文 https://arxiv.org/pdf/2109.13519 ，§1 Main Theorem。
  本节仅用它定位 one-exception word 的已刊范围；
  (1133.37)–(1133.52) 的实际单位范数及 étale 代数另作完整证明。
- $K_2$ 的 Steinberg、transfer 及 projection formula 采用原 Milnor/Quillen
  field $K_2$，不以复解析 rational $K$ 群替代。
  (1133.30)–(1133.34) 自行支付所需低 cochain，不另依赖存在性猜测。

global_route 推导。o2_high_coefficient 已独立回读 R1070 并纸核
Ward 方向、half/all 的二、$d_\chi(a)$、所有实际角色范围、根数证明，
以及三步 étale 代数与 Heisenberg 群作用。全文候选交 root 精确复核。


root 已全文回读 R1070 §§9–10 及 Stange 已刊 Eq. (1)、Lemma 3.5、Lemma 4.2，独立核定原 D 自由轨道、两槽 Ward 方向、half/all 与 leading、根数界及完整 Heisenberg 作用；与 o2 对精确候选的全文纸审一致。


§9 为 global_route 的同源四阶延长。o2_high_coefficient 已独立纸核
二项式循环补项、较大根代数的 $\sigma^p=1$、四行独立、
$(I+L)^{-1}$ 与相位共轭方向，以及标准 $\mathbb U_5$ 首对角；
不将其升级成原 forced 角色的已下降覆盖。


§9 root 独立全文核准最终候选：循环指数的整补项、较大根代数的实际σ^p、相位共轭的逆矩阵、UT5嵌入及几何cusp的四moment判据均通过。原角色的全局单位范数见证与算术下降仍继续；没有将本节通用判据称为已构造原四阶覆盖。


§10 的有限 Fourier 恒等式、$\lambda_p$ 完整相位及两份实际塔的
Heisenberg 商识别由 global_route 推导，o2_high_coefficient 已逐式
独立纸核单位性、原边界 leading、群作用与 $p^5/p^7$ 纤维积；
混合四阶方向及原范数下降未据此宣称完成。


§10 root 对精确候选96b1d45b逐式独立核准：有限Fourier的两个deck作用、全局单位性、D(1)的符号与ζ相位、严格交换involution及两个真纤维积的全部显示括号均通过。只统一数学display定界符；原跨轨道及混合四阶边界保留。
