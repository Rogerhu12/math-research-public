# R150：一般 h=1/k=1 原碰撞图的完整八式与行列式首一三次头

**状态：已证明并实际返回。** 当前一般 LS 中 h=1 或 k=1 的原值碰撞图，在原两线行列式非零时，完整原均值、N1 与两 singleton 的个别 N/P 已由同一清分母 Gram 返回为三参数上的八条多项式。真实运行10.632秒，未删任何未付首项。另证明原两线行列式对 ell 恰为三次，最高系数是该碰撞图的已付单位；这也给它的整个零图一个全覆盖首一三次输入。

本文不排空碰撞图，不将原方程的抽象解宣称为物理实现。旧碰撞参数化只引用，不作为新发现登记。

Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 旧完整碰撞图与当前原单位

[原 U-value atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)第2.2节已给 h=1/k=1 的完整 moment 参数化。交换两个 singleton 后取 h=1。记

$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad c=A^3/B^2,\quad b=\ell-c.
$$

于是

$$
h=1,\ k=1+\xi,\quad T=A^2/B,\quad w=\lambda-1-T.
$$

这里 A、B、xi 非零由原两矩、bc≠0、h≠k 支付。旧 S0-h1-k1 排除只覆盖 S=0；本文当前图为 S≠0，没有把旧排除误推到整个碰撞图。

用原有序 rho=(p−q)/2，规范 p+q=2：

$$
p=1+\rho,\quad q=1-\rho,\quad Q=1-\rho^2,\quad
u=bp+cq=p\ell-2c\rho.
$$
$$
v_0=\xi/2,\quad v_1=-\xi/(2\rho),\quad
\zeta=\xi p/(2\rho),\quad S=\xi+3-2\lambda.
$$

原 p、q、rho 和当前 S 均非零，故 zeta 自动非零。本次直接核对

$$
c\xi^2=A,\quad c\xi^3=B,\quad c\xi=T,\quad
D=\ell A-T^2=bA,\quad M=4bc\rho^2.
$$

lambda、u、u−1、ell、u−ell、M、P02、T0、J−Q、u+Q−1 等此前已付权条件均保留在其原适用范围。没有额外倒置 ell−2c，也没有除去 A 或 B 的原未覆盖零支：它们的非零性专属于本碰撞图。

## 2. 两条原线与共同缩放

设

$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
P_f=T_0(J-Q),\quad G=\lambda P_{02}-(1-u)T_0,
$$
$$
P_c=QP_{02}(\ell+T)-GT_0.
$$

在 z=(h−1)(k−1)=0 上，准确的原 N(V) 系数为

$$
N_F=(3-4\lambda)Q+S(2uQv_1+\zeta J),\qquad
N_T=bcQS\zeta,
$$
$$
N_C=-GS\zeta+\frac12SQ T_0v_1+
Qw\{u(3-2\lambda+v_0+v_1)-\ell Qv_1\}.
$$

原两线是

$$
P_ff+bcQ\Phi t+P_c=0,\qquad N_Ff+N_Tt+N_C=0.
$$

令

$$
\Delta_*=\Phi N_F-S\zeta P_f.
$$

两线真实行列式为 −bcQ Delta*。在 Delta*≠0 图，定义

$$
H_0=\Delta_*,\quad f_0=S\zeta P_c-\Phi N_C,\quad
t_0=(P_fN_C-P_cN_F)/(cQ).
$$

直接完整乘回得到

$$
P_ff_0+cQ\Phi t_0+P_cH_0=0,\quad
N_Ff_0+cQS\zeta t_0+N_CH_0=0.
$$

因此 f=f0/H0、t=t0/(bH0)，不除以 Phi。本次尝试三分子的共同因子取消，实际 gcd 为1；没有声称此步获得不存在的缩小。

令 H=bH0，原点 H≠0。把 H 乘进同一张原 Gram，避免在每次乘法中处理 H 的逆。此为原方程的同点清分母，不是引入另一个模型。

## 3. 整张清分母 Gram

定义

$$
W_{1P}=T_0H_0/2+2uf_0,\quad
W_{2P}=(uT_0+\lambda P_{02})H_0+(V_2+2u^2)f_0-cQt_0,
$$
$$
X_0=(qW_{1P}-W_{2P})/[p(q-p)],\quad
Y_0=(W_{2P}-pW_{1P})/[cq(q-p)].
$$

这些分母全部位于 (lambda,rho) 基参数环，且已由本图支付。进一步置

$$
r_0=X_0-apH-ct_0,\quad
s_0=Y_0-aqH_0-t_0,\quad
A_0=2f_0-2X_0-2cY_0+2ct_0,\quad a=1-\ell.
$$

四条真实的 H·Gram 行恰为

$$
(0,0,pH,qH),\quad
(0,bA_0,r_0,bs_0),\quad
(pH,r_0,0,t_0),\quad
(qH,bs_0,t_0,0).
$$

这是将原 E0/N0 的同一 X/Y 恢复逐项乘 H 后所得。特别真实 tau(dN)=2bf0。原 P1 的完整极化剩余也实际为零。

按原 Frobenius 乘法、tau、DK 形成原式：均值整体乘 H²；N1 及个别 N/P 整体乘 H³。P1 与 N(V) 的同源关系由当前两线和原矩支付；N(V) 中的 HA 修正保留为准确已付身份，不重复通用大展开。

两个 singleton 分别返回，未用 weighted 投影代替另一谱。k=1 由交换两个标签及 rho 变号覆盖。

## 4. 八条原式的实际大小与同点等价

所有系数始终是 QQ[ell,lambda,rho] 上的分式；源确认每个最终分母只含已付 (lambda,rho) 基域因子。清分母后仅剥原已付单位的真实因子，每次保完整乘回。未付 ell 首项均保留。

| 原式 | 次数界 (ell,lambda,rho) | 项数 | 本次剥除 |
|---|---|---:|---|
| E1 | (11,74,12) | 11458 | b |
| EB | (12,78,12) | 13058 | 无 |
| EC | (12,78,12) | 13059 | b |
| N1 | (13,84,13) | 16106 | p、b²、Delta* |
| NB | (16,107,17) | 32344 | p、b |
| PB | (18,117,18) | 41775 | 无 |
| NC | (17,111,18) | 37573 | b |
| PC | (18,117,18) | 41775 | b |

表中剥除都是当前原点单位，尤其 Delta* 只在本节非零图剥除。它的零图没有被误认为该非零图所覆盖。

每条式子的零性与相应原值方程同点等价，因为 H 与全部清除分母非零。逆向须保留本图的所有原非零条件，以及原模型其余物理实现条件；本文只给本原方程系统的完整返回，不从必要坐标解推断物理临界点存在。

这些多项式仍非低次全局消元证书；本文没有计算它们的参数结式，也没有宣称图为空。大展开只留源和散列，不保存可重算多项式缓存。

## 5. 原行列式整个零图的首一三次输入

这是从同一紧凑原线得到的新增结构。u=p ell−2c rho 对 ell 一次，T、c、S、zeta、v1 都只依赖 lambda/rho。由

$$
\Delta_*=
S\zeta\{J(4u-4+Q)+T_0Q\}
+\Phi\{(3-4\lambda)Q+2uQSv_1\}
$$

可见最高次数至多三。T0、J、Phi 的 ell² 系数都为 −2p²，故 ell³ 系数为

$$
-8S\zeta p^3-4QSv_1p^3
=-4Sp^3(2\zeta+Qv_1)
=-\frac{2S\xi p^5}{\rho}.
$$

最后一步使用 2p−Q=p²。该系数在本原碰撞图非零，因此 Delta* 对 ell **恰为三次**，且可以用已付基域单位首一化。这里没有遗漏新的最高系数零分支。

源实际提取全部 ell³ 系数并逐式核对上述公式为真。这个事实适用于 Delta*=0 的整个碰撞图；可在 QQ[lambda,rho] 的已付基单位局部化环上使用首一三维 ell 商，接原兼容式和原值。尚未排除该零图，也没有从它的首一性推出其无根。

## 6. 源与真实运行

源：notes/2026-11-27-unit211-general-h-one-cleared-original-eight-values-8542.py。

- blob94e47ed8328fb55539c269cd7bb97c9765866f17；
  SHA256 e6dae4937592235db729031ae27ec14e3a3f747fcf648d2d3e66e81eeb1be0a2，7864字节。
- 共同原 Gram helper：blob90dc1acf3173906302095a0670a1c3d40a5ed2a0；
  SHA256 41459fea3ff0419d8c9230a2f6093cc0b1bc5f528b6f2d2e714a4469f11e5c3e。
- run45988578719/job140470355209；内层exit0；源10.544963159秒、驱动10.632351120秒。
- 驱动峰值156116KiB，源末自身峰值153544KiB；配置180秒/4GiB。
- stdout10612字节，SHA256 efa1fe565ec9ca9d2ee1a3f049714fd2ac35841aa9c247bc82649a649f07c227。
- 真实pull在11:12:54.439798 UTC，前后提交7a5c98b8e31f4e4596972d48c233ee6106a2dc5c，两README均无变。
- 小回执：notes/2026-11-27-unit211-general-h-one-cleared-eight-values-receipt-8542.json。

Python3.12.14、python-flint0.9.0、单线程；helper从同一冻结提交读取并在源内核对SHA。完整8原式、26种最终基域分母和全部剥除乘回已实际完成。一般碰撞非零图、零行列式碰撞图及普通ISP均未完成；下一使用第5节真正首一三次与原兼容式的新低维输入。
