# R106 补充：同一真实族的移动根非均值密度迁移

2026-11-13，constructive-route。

**已证明并实际执行准确有理核验。** 对当前准确参数
$$
p_5=-\frac{7789843107295549}{4611686018427387904},
\qquad |p-p_5|\le10^{-9},
$$
下面的原 height 约化密度满足
$$
|G_p(\rho,\theta)|<\frac{9327}{200000}=0.046635
\quad\left(|\rho|\le\frac1{2500},\
|\Im\theta|\le\frac1{320}\right). \tag{106G.1}
$$
这是完整非均值函数的复域界，不是角平均的界。它复用三个已经完成的
真实连续证书并对真实参数线积分；本次没有重新采样几何。

## 1. 准确对象、函数与已付原件

令 $t(p)$ 为同一 exact-affine 无限 R33 图的真实正根，
$\rho=t(p)-r$。本篇使用 R50 与 R106 完全相同的原 height 约化密度
$D_{\rm red}(r,\theta,p)$，保留完整 $\ell$、零阶项以及原分部积分口径。
定义
$$
G_p(\rho,\theta)=\rho^{5/2}
 D_{\rm red}(t(p)-\rho,\theta,p),\qquad
H_p(\rho,\theta)=\rho^{7/2}
 \left.\partial_pD_{\rm red}(r,\theta,p)\right|_{r=t(p)-\rho}.
\tag{106G.2}
$$
$H$ 的参数导数固定的是物理 $r$，并不固定 $\rho$。
它不是 $\partial_pG$。本篇没有将 grounded 密度和原 height 密度混用。

全部几何原件的 origin SHA256 为
0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b，
direction SHA256 为
8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab。
旧中心与外参数盒为
$$
p_3=-\frac{7832869216826619}{4611686018427387904},\qquad
\Delta_5=[p_3-10^{-5},p_3+10^{-5}].
$$

| 真实输入 | 原 SHA256 |
|---|---|
| notes/2026-11-12-beta-exact-affine-step3-collar.json | 037cd700677da4a34b423de431e9b22ab9903b5cd844a6a9348e6ccd0ee8918d |
| notes/2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json | b387ede87055d0a990cafca12002b8baead5a2415d2d4cef610dde99405efd08 |
| notes/2026-11-12-beta-step3-parameter-root-derivative-h1e5.json | 3284dfe4d3feaa5eeca5f114844c1052b381434fa1bb0c08def1c45d9b845243 |
| notes/2026-11-12-R106-actual-all-time-ray-tube.json | 6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863 |

第一个报告的 domain.G_bound 来自完整复径向圆盘与连续复角盒，
而非 coefficients 中的角平均系数。它给 $p_3$ 上
$|\rho|\le0.0006$、物理角带 $0.005$ 的非均值模数 $M_G$。
第二个报告的 domain.H_bound 来自整 $\Delta_5$ 的真实固定 $r$
参数导数，覆盖 $|\rho|\le0.0005$、物理角带 $1/320$。
它还保留整复域上的 area2、radius2、support、a、Fz 正实部以及
消根曲率的正实部；最后一项的实际下界大于 $50$。
这些门给根消去后的 $G_p$ 在整个相应复盘中全纯。
第三个报告给同族真实隐式根导数 $0<t'(p)\le T$。

所有报告中的显示球均用“显示中心加/减显示半径”向外取准确有理端点。
特别地，本次使用
$$
\begin{aligned}
M_G&=
0.046633817745567262172698974609375000+10^{-41},\\
M_H&=
3.6677273669738497119396924972534180\,10^{-5}
  +3.13\,10^{-40},\\
T&=
6.1108124782549783429730361206111411\,10^{-5}
  +1.35\,10^{-40}.
\end{aligned} \tag{106G.3}
$$
这些是报告的完整向外值，计算没有用展示用的 binary64 近似。

共同准确 scalar span 是
$$
\left[
 \frac{8556839292003943}{36028797018963968},
 \frac{8636031980136455}{36028797018963968}
\right].
$$
真实根、固定 cut
$r_c=268136140016943/1125899906842624$ 和整个实际实 collar
均在此 span；新的半径 $1/2500$ 包含全部 $0\le t(p)-r_c$。
这仍是该同一 germ 的解析延拓，不是把其它材料段的多项式挪过 knot。

## 2. 固定物理点的参数线迁移

取
$$
\epsilon=|p_5-p_3|+10^{-9}
=\frac{42022188688562917371}{4503599627370496000000000},
\qquad R=\frac1{2500},\qquad d=R-T\epsilon.
$$
准确运算给 $\epsilon<10^{-5}$、$d>0$，以及
$$
T\epsilon<0.0000000005701877081636,\qquad
R+T\epsilon<0.0005<0.0006. \tag{106G.4}
$$

固定一个当前 $p$、$|\rho|=R$ 和 $|\Im\theta|\le1/320$。
在从 $p_3$ 到 $p$ 的实参数线段上，保持
$$
r=t(p)-\rho,\qquad \theta
$$
不变，并记 $\rho_q=t(q)-r$。真实根导数界直接给
$$
R-T\epsilon\le|\rho_q|\le R+T\epsilon. \tag{106G.5}
$$
因而这条线从不碰 $\rho_q=0$，也始终处于已付完整 $H_q$ 域。
在每条这样的非零参数线上连续选择平方根分支即可应用微积分基本定理。
换一条分支会同时改变密度的对应符号，绝对值估计不变。
最后 $G_p$ 的单值全纯性来自 §1 的真实根消去式与分母门；
不能只由边界上的绝对值估计假设它成立。

对固定 $r,\theta$ 积分真实 $\partial_qD_{\rm red}$，再乘 $|\rho|^{5/2}$，
得到
$$
\begin{aligned}
|G_p(\rho,\theta)|
&\le
\left(\frac R{R-T\epsilon}\right)^{5/2}M_G
+\frac{\epsilon M_H R^{5/2}}{(R-T\epsilon)^{7/2}}\\
&=
\left(\frac R{R-T\epsilon}\right)^{5/2}
 \left(M_G+\frac{\epsilon M_H}{R-T\epsilon}\right)\\
&\le
\left(\frac R{R-T\epsilon}\right)^3
 \left(M_G+\frac{\epsilon M_H}{R-T\epsilon}\right)=:M_* .
\end{aligned} \tag{106G.6}
$$
最后一步使用 $R/(R-T\epsilon)\ge1$，所以整个有限证书只含准确有理算术。
在 $\rho$ 圆盘使用最大模原理后，(106G.6) 覆盖闭盘内部及根本身。
准确向外十进制为
$$
M_*<0.0466348727470257305181<\frac{9327}{200000},
$$
从而证明 (106G.1)。

## 3. 同一个实际射线标签下的用途

R106T 对当前整个参数盒、全部前腿实时间和初始标签带 $1/1024$ 已付
$$
|\Im\Theta|\le s_\theta=\frac{8221101}{8000000000}<\frac1{320},
\qquad
|J|=|\Theta_x|\le J_*=\frac{8223669}{7812500}.
$$
因此在实际实 root collar 内，
$$
|G_p(t(p)-r,\Theta(r,x,p))J(r,x,p)|
\le M_*J_*<0.0490892489380685238098
<\frac{491}{10000}. \tag{106G.7}
$$
这里 $J$ 是相同 $H_5/4$ 首标签的真实 Jacobian，未被当成 $1$。
这也不是最终 R101 共轭标签，不能略去后续 frame 变换。

记 $\Delta_\theta=1/320-s_\theta>0$。
完整复角域还直接给
$$
|\partial_\theta^jG_p(\rho,\Theta)|
\le\frac{j!\,M_*}{\Delta_\theta^j},\qquad 0\le j\le4. \tag{106G.8}
$$
对应向外十进制为 $0.046634872748$、$22.235009698$、
$21202.830720$、$30327850.311867$、$57839981632.866643$。
这些是 $G$ 的物理角导数界；没有把它们冒称为整个复合分子
$G\circ\Theta\cdot J$ 的四阶根变量导数。

## 4. 状态与可重放

本次执行器在 2026-11-13 的真实 native bulk/root-field 计算后再次失联，
此前未推送的 41 门程序文本也未能从 V8 store 恢复。
本篇程序依据原始输入重新实现并**重新实际执行**，当前版本有 42 个门。
旧未发布源码的 SHA 不再冒称是新源码的 SHA。

新源 scripts/fourfold_subprincipal_root_density_transfer_exact.mjs
逐字 SHA 检查 §1 四个报告以及四份真实数学内核，
随后执行与本证明相同的 BigInt 有理运算。
本次 V8 实际报告为
notes/2026-11-13-R106-whole-parameter-root-density.json。
它保存每个门和完整准确分数，而非只保存展示近似。

~~~sh
node scripts/fourfold_subprincipal_root_density_transfer_exact.mjs \
  . notes/2026-11-13-R106-whole-parameter-root-density.json
~~~

(106G.7) 只控制根消去后的分子。它没有支付沿真实射线的根有限部分积分、
复根时间延拓、完整 $S$ 角散度项与普通 cut 端项，也没有证明
$D_{\rm red}$ 的 grounded 变换已经免费完成。
完整非均值 $b$、R104 所需的最终标签乘子范数和全 PDE 强逆仍须继续支付。
