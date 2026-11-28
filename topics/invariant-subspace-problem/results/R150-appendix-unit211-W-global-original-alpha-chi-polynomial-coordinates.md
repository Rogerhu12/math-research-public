# R150：整个当前 W 的原 $\alpha,\chi$ 多项式坐标与首一二次环境

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-28（Asia/Taipei）。

**状态：完整证明。** 在当前 W 的原 $t\ne0$ 图上，消去正确均值差后，得到只以既有权单位为分母的两个几何坐标 $\alpha,\chi$。$f,t,V,A_1,x,y$ 全对 $\alpha$ 一次；对 $\chi$ 至多二次。这里 $\chi$ 是新标量坐标，与原 singleton 值 $h,k$ 无关。整个 $\alpha=0$ 也被以下多项式身份保留；没有倒 $\alpha$、$\gamma$ 或任何新的几何首项。

本条不是 W 排空结论。完整原 N/P、个别值、物理单位及所有未付参数条件仍需在同一点满足。

## 1. 原范围和两条权身份

沿用当前 W 原规范，记
$$
u=e+1,\quad Q=ek,\quad \overline V=uk+2,\quad
\ell=\frac{u[(k+2)^2-2ek]}{k\overline V},\qquad \delta=1-Q,
$$
$$
m=u-\ell,\quad \widehat U=u-\ell Q,\quad
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
M=\ell V_2-u^2=4bc\delta.
$$
再定义纯权多项式或原权有理函数
$$
Z=u(u-1)+\ell(1-\ell)Q,\qquad
C=u-1+(1-\ell)Q,
$$
$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q.
\tag{1}
$$
直接展开得
$$
\widehat U Z-MC=-mR_w,\qquad
2uZ+mT_0=-\ell R_w.
\tag{2}
$$
当前 W 权公式还有
$$
R_w=-\frac{ue^2}{\overline V}\,H_{\rm old},\qquad
H_{\rm old}=4ek-k^2-4k-8.
\tag{3}
$$
$H_{\rm old}=0$ 已由 [整个原 H 零支排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-H-zero-complete-original-exclusion.md) 支付；这个相同的 $H_{\rm old}$ 及其整支来源也保存在已刊 native 六规则源中。因此 (3) 证明当前 W 上 $R_w$ 是已付的**权单位**。

$m$ 的支付来自 [整个等权排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，这里只应用于当前 distinct-singleton、$D\ne0$ 的 W 原域。不得将此单位或 (3) 移用到一般 $h=k$ 图或任意 Phi 图。

$\delta,M$ 是原 $Q(1-Q)bc$ 条件中的已付单位；$t$ 由 [整个当前 W 的 t 零支排除](R150-appendix-unit211-W-entire-t-zero-complete-original-exclusion.md) 支付。以上足以构造新图，不要求 $\widehat U,Z,C$ 各自非零。

## 2. 正确原均值差与 $A_1$

记
$$
V=bX+cY,\quad W_1=bpX+cqY=(T_0+4uf)/2,
$$
$$
A_1=2f-2V+2bct,\qquad \eta=f-u.
$$
这里 $A_1$ 是同一原 Gram 的双点对角条目。原 $E_0$ 已通过 $W_1$ 恢复。令
$$
\mathcal R=
4(f-u)(V-f)+bct^2+
t\left(4bcu-\ell V+
 \frac{m}{2\delta}(T_0+4uf-2V)\right).
\tag{4}
$$
正确双点乘法的原均值恒等式为
$$
2\mathcal R+E_1-EW-
 \left(\frac{mt}{\delta}-(1-\ell)\right)E_0=0,
\qquad EW=bE_B+cE_C.
\tag{5}
$$
故在原 $E_0=0$ 图中，$\mathcal R=0$ 与 $E_1=EW$ 精确等价。(5) 使用真实 $-2(d^2)_1=-4d_0d_1$，不是已撤回的 compact $-2d_1^2$。正确完整原来源是更正源 blob 0956345ccfc13e0951356fd4ffa53ea68ec508c8，SHA256 a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae；本条未重新运行该旧源。当前 [同点原 Gram 定义](../notes/2026-11-28-unit211-W-gamma-open-direct-native-f-cube-monic-two-8542.py) 使用同一正确乘法。

定义
$$
\alpha=4\delta(f-u)-\widehat U t.
\tag{6}
$$
将 $V=f+bct-A_1/2$ 代入 (4)，用 $4bc\delta=M$，得到完整原身份
$$
2\delta\mathcal R+\alpha A_1
=t\left(2Zf-2bcCt+mT_0\right).
\tag{7}
$$
本次新源码在自由 $u,\ell,Q,f,t,A_1$ 上清分母，以 BigInt 整数多项式逐项核验 (7)，不是只在原解上作数值检查。

## 3. 新坐标及纯权分母恢复

只在当前已付 $t\ne0$ 图定义
$$
\chi=\frac{2\delta A_1}{t}-Z.
\tag{8}
$$
这一步不把 $A_1$ 或 $\chi$ 当单位。由 (7) 的 $\mathcal R=0$、(6)、两条权身份 (2)，得到
$$
mR_wt=-\alpha\chi-2\delta\ell R_w.
$$
因此
$$
\boxed{\quad t=-\frac{\alpha\chi}{mR_w}
                 -\frac{2\delta\ell}{m}\quad}
\tag{9}
$$
以及
$$
\boxed{\quad f=u+\frac{\alpha+\widehat U t}{4\delta},\qquad
 V=f+\frac{M-Z-\chi}{4\delta}\,t,\qquad
 A_1=\frac{\chi+Z}{2\delta}\,t.\quad}
\tag{10}
$$
最后以原两个加权线性式恢复
$$
W_1=(T_0+4uf)/2,\qquad
x=\frac{\widehat U V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},
\tag{11}
$$
$$
X=x+\rho y,\quad Y=x-\rho y,\quad \rho^2=\delta.
$$
所有分母只含有理常数、$\delta,m,R_w,M$，均已支付为纯权单位。没有新的 $\chi$ 首项、$\gamma$、$\alpha$、$f-u$ 或 $\widehat U$ 分母。

从 (9)–(11) 反向计算时，完整返回
$$
\alpha=4\delta(f-u)-\widehat Ut,\quad
2\delta A_1=(\chi+Z)t,\quad
A_1=2f-2V+2bct,
$$
$$
\mathcal R=0,\qquad
V=\ell x+my,\qquad W_1=ux+\widehat Uy.
\tag{12}
$$
在 $t\ne0$ 时，第二式恰恢复 (8)。所以这是真正双向坐标图，不只是一族必要参数点。

更精确地，令 $A_W$ 是这些已付权单位的原权环。正确均值差曲面的环
$$
A_W[f,V,t,t^{-1}]/(\mathcal R)
$$
同构于
$$
A_W[\alpha,\chi,t(\alpha,\chi)^{-1}],
$$
映射由 (6)、(8) 和 (9)、(10) 给出。其它既存物理单位与剩余原方程按同一点传输。没有删去 $t(\alpha,\chi)=0$ 后再声称未局部化环同构。

虽然物理逆图使用已付 $t$，(9)–(12) 清分母后的恒等式在 $\alpha=0$ 和 $t(\alpha,\chi)=0$ 仍然成立。特别是本条既没有依赖 $\alpha=0$ 排除来倒 $\alpha$，也没有为了构造新图重做该已闭分支。

## 4. 次数及完整原二次环境

(9)–(11) 显示全部恢复量对 $\alpha$ 至多一次；对 $\chi$ 的次数为：

| 恢复量 | $\deg_\alpha$ | $\deg_\chi$ |
|---|---:|---:|
| $t$ | 1 | 1 |
| $f$ | 1 | 1 |
| $V,A_1,x,y$ | 1 | 2 |

新源码对清分母后的实际分子确认了此表。原三个剩余二次 $EW,E_B^{odd},N_1$ 因而仍对 $\alpha$ 至多二次。既有 native NS/PS 余式位于
$$
\operatorname{span}_{A_W}(1,x,y,t,y^2,yt);
$$
按 [原 native 五二次的来源](R150-appendix-unit211-W-gamma-native-five-quadratic-original-two-constants.md) 的同一原均值标签身份，它们在新图中也直接成为 $\alpha$ 二次。原三次的系数恰为一，故这里同样得到完整原 $I_6$ 的五二次呈示。这个双向理想等价使用原 native 身份，未借旧 gamma 图上的几何逆。

还可给出首一二次的完整构造性存在证明，而无需把新的大系数显示运行作为证明门。原 native 六均值规则将任意几何三次降到总几何次数至多二。令
$$
L_\alpha=\frac{2\delta}{u}(ux+\widehat Uy)-\widehat Ut
$$
为 (6) 在 $(x,y,t)$ 中的线性部分。用六规则对 $L_\alpha^3$ 约化，得到
$$
L_\alpha^3-R_{\le2}=\sum_{i=0}^3 H_i E_i,
\tag{13}
$$
$H_i$ 总几何次数至多一，且只用已付权分母；这里四个 $E_i$ 是 native 的 $E_1,E_B^{even},E_B^{odd},N_1$。

设 (11) 中 $(x,y,t)$ 的 $\alpha$ 一次方向为 $d(\chi)$。由 (12)，$L_\alpha(d)=1$。对 (13) 取三次最高部并代入 $d$，
$$
1=\sum_{i=0}^3 H_i^{[1]}(d)\,[\alpha^2]E_i(\alpha,\chi).
$$
再用 $E_1=EW$、$E_B^{even}=(EW-mE_B^{odd})/\ell$ 合并，即得三原二次头在 $A_W[\chi]$ 中的 Bézout $1$。因此其实际组合定义
$$
q_\alpha=\alpha^2+q_1(\chi)\alpha+q_0(\chi)
\quad\hbox{且}\quad q_\alpha\in (EW,E_B^{odd},N_1).
\tag{14}
$$
这里 (13)–(14) 是已付六规则给出的完整有限算法和纸面身份，不宣称已经新展开或保存其系数。未局部化的首一环境 $A_W[\chi][\alpha]/(q_\alpha)$ 自由秩二；进一步取原方程商是该环境的商。物理 $t,D$ 等几何局部化不能据此自动宣称仍对 $A_W[\chi]$ 有限自由。

## 5. 本次唯一新小执行

源：[2026-11-28-unit211-W-original-alpha-chi-polynomial-coordinate-identities-8542.js](../notes/2026-11-28-unit211-W-original-alpha-chi-polynomial-coordinate-identities-8542.js)。

源码 5236 字节，SHA256 511e1b5dded4fb4ca77ef1e41230329db451e5846623b8d8a8d68ae9a0d58b49。无外部依赖。实际 functions V8 执行 6 毫秒，174 次 BigInt 整数多项式乘法，11 条完整清分母身份全部返回零。参数为源码列出的十个自由符号，独立 30 秒界未触及。

实际原检查包括 (2)、完整 (7)、(9)–(12) 的 A1/alpha/chi/原 R/V/W1/f 还原，以及完整 W 权支付 (3)。没有运行旧 native determinant、旧十行二列、任何结式、数值采样或素数门。源码仅返回小统计与身份状态，不保存可重算系数。

小回执：[2026-11-28-unit211-W-original-alpha-chi-polynomial-coordinate-identities-receipt-8542.json](../notes/2026-11-28-unit211-W-original-alpha-chi-polynomial-coordinate-identities-receipt-8542.json)。
