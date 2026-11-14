# R271 附录：d^(3/4) 宽负源前缀与仍为指数级的有效窗口预算

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220。AI-assisted，GPT-6 Astra Pro。

状态：**以下原来源构造及全部费用已证明。** 本文将完整 $L+B$ 负源前缀从三次对数宽度扩到 $d^{3/4}$ 量级，同时保持同一个原 good-top、同一个固定缺陷和全部低层来源的相容性。代价是把两费预算中的窗口参数 $K$ 换成明确的 $K_{\rm eff}$，仍满足
$K_{\rm eff}\ge e^{59d^3/256}/(2^{19}d)$。后续两旗必须按这个新参数重新选择；不能把增长常数直接乘到未知速率的实际尾量上。

依赖：[完整加平坦负前缀修正](R271-appendix-full-plus-flat-negative-prefix-repair-and-complete-top-cost.md)、[出生一原 dyadic 头修复](R271-appendix-dyadic-original-heads-birth-one-repair-and-explicit-growing-quotient.md)、[原低 triplet 联合回缩](R271-appendix-low-triplet-count-joint-retraction-and-original-high-energy-bound.md)、[原线性失真](R271-appendix-linear-triplet-count-distortion-by-prefix-splitting.md)、[同源两旗谱余商](R271-appendix-joint-paid-flag-spectral-quotient-at-an-actual-good-top.md)、[固定测试局部 Gram](R271-appendix-fixed-physical-tests-and-minimum-two-chain-local-gram.md)。

## 1. 同一个原窗口和两个 dyadic 头宽

取原 $m\ge47,d=2^m,A=A_m,D=D_m$。令
$$
Q=\lfloor e^{d^3/4}\rfloor,\qquad
Q/2\le b\le Q-d,\qquad
K=K_m^{\rm win}\ge\frac{e^{d^3/4}}{8d},\quad K\le Q/d.
\tag{1.1}
$$
这些是原共同窗口选择在充分大 $m$ 时的计数界。

原源记为 $r$，原未来窗口为 $Y_b$。固定假设中的
$w\ne0$，写 $W_0=\|w\|,\ \rho=\varepsilon_m/W_0$。使用原共同选择
$$
\|Y_b\|^2\le2\varepsilon_m^2/K,\qquad
\Xi(r)^2\le4\varepsilon_m^2/K,\qquad
\|E_b^\dagger r-w\|\le\varepsilon_m.
\tag{1.2}
$$
只要求 $\varepsilon_m\to0$，不要求任何额外速率；下文用于充分大的 $m$，故 $0<\rho<1$。零尾量情形已直接没有非零缺陷。

定义
$$
h=2^{\lfloor3m/4-3\rfloor},\qquad H=2h,
$$
$$
d^{3/4}/16<h\le d^{3/4}/8,\qquad
d^{3/4}/8<H\le d^{3/4}/4.
\tag{1.3}
$$
所有源旗保留原 $d$ 尾阶：
$$
\mathscr F_j=\mathscr R_b\cap\ker A^j.
$$
已有出生一修复对这两个整旗给
$$
\lambda(x)\le C_-\alpha(x)\quad(x\in\mathscr F_h),
\qquad
\lambda(x)\le C_+\alpha(x)\quad(x\in\mathscr F_H),
$$
$$
C_-=8e^{20h^4},\qquad C_+=8e^{20H^4}=8e^{320h^4}.
\tag{1.4}
$$
这里的常数只用于显示原完成链的费用，不把这些旗改成天然小尾阶模型。

## 2. 宽负前缀的完整加平坦修正

沿前稿记
$$
u=B^{1/2}r,\quad\mathsf H=B^{-1/2}LB^{-1/2},\quad
C=B^{1/2}GB^{1/2},\quad0\prec C\preceq I.
$$
在
$$
W=B^{1/2}\mathscr F_h,\qquad
\delta=\sqrt{C_-^2-1}
$$
上，(1.4) 正好给 $\|(C^{-1}-I)^{1/2}|_W\|\le\delta$。
令
$$
\vartheta=\delta\bigl(\sqrt{1+\delta^2}+\delta\bigr),
\qquad c=\sqrt2+\vartheta .
\tag{2.1}
$$
这里允许 $\delta$ 很大。前稿对所有 $\delta\ge0$ 已证明真实
$\mathsf M_3=C^{-1}+\mathsf H C\mathsf H$ 修正 $p_0$ 存在，且
$$
r^0=r-p_0\in\mathscr D_h
:=\{s:\langle(L+B)s,x\rangle=0\ \forall x\in\mathscr F_h\},
\tag{2.2}
$$
$$
\mu(p_0)\le\vartheta\varepsilon_m/\sqrt K,\qquad
\lambda(p_0)\le\sqrt2\vartheta\varepsilon_m/\sqrt K,\qquad
\Xi(r^0)^2\le2c^2\varepsilon_m^2/K.
\tag{2.3}
$$
它同时支付同一个 $p_0$ 的原 flat 费用。初次修正不是原两费正交投影，故 (2.3) 保留三角不等式所得的 $c$。

定义准确的新预算参数
$$
\boxed{K_{\rm eff}=K/c^2.}
\tag{2.4}
$$
它是两费估计的参数，不声称原来额外产生了新的不交窗口。
由 $\vartheta\le2C_-^2,\ C_-\ge1$ 得
$$
c\le4C_-^2=256e^{40h^4},\qquad
c^2\le2^{16}e^{80h^4}.
$$
结合 $h^4\le d^3/4096$ 与 (1.1)，
$$
\boxed{
K_{\rm eff}\ge\frac{e^{59d^3/256}}{2^{19}d}
\longrightarrow\infty,\qquad
\Xi(r^0)^2\le2\varepsilon_m^2/K_{\rm eff}.
}
\tag{2.5}
$$
损失只明确地出现在这个预算中，没有藏入实际尾量。

## 3. 同一个宽负图中的真实大头两费投影

在 $\mathscr D_h$ 内，对
$$
Z_H=\mathscr D_h\cap\mathscr F_H
$$
作真正 $M_2=B+LGL$ 正交投影，记投影源为 $p_H$，余源为
$r^1=r^0-p_H$。令
$$
\mathscr D_1=\mathscr D_h\cap Z_H^{\perp_{M_2}}.
$$
则 $r^1\in\mathscr D_1$，精确保持完整的 $h$ 负源前缀和
$H$ 两费头旗交测试。已有同源 Cauchy 与 (1.4) 给
$$
\mu(p_H)\le \sqrt{C_+}\,\varepsilon_m/\sqrt{K_{\rm eff}},
\qquad
\lambda(p_H)\le\sqrt2C_+\,\varepsilon_m/\sqrt{K_{\rm eff}}.
\tag{3.1}
$$
这些来自
$\mu^2\le(C_+/2)\Xi^2$ 和 $\lambda\le C_+\Xi$，没有把
$p_H$ 的左、裸或平坦源拆开。

明确代入 (1.1)—(2.4) 得
$$
\begin{aligned}
\mu(p_0)&\le512\sqrt{2d}\,e^{-59d^3/512}\varepsilon_m,\\
\lambda(p_0)&\le1024\sqrt d\,e^{-59d^3/512}\varepsilon_m,\\
\mu(p_H)&\le2048\sqrt d\,e^{-39d^3/512}\varepsilon_m,\\
\lambda(p_H)&\le8192\sqrt d\,e^{-19d^3/512}\varepsilon_m .
\end{aligned}
\tag{3.2}
$$
例如 $\lambda(p_H)$ 的指数正是
$40h^4+320h^4-d^3/8\le-19d^3/512$。
所以可统一写为
$$
\boxed{
\mu(p_0+p_H)\le a'_m\varepsilon_m,\quad
\lambda(p_0+p_H)\le b'_m\varepsilon_m,
}
\tag{3.3}
$$
$$
a'_m=4096\sqrt d\,e^{-39d^3/512},\qquad
b'_m=16384\sqrt d\,e^{-19d^3/512}.
$$

## 4. 必须以有效预算重新选择真实 triplet 旗

若沿用旧 $K$ 的两旗，再把整个费用乘 $c$，会出现
$cW_0\rho^{1/4}$；由于没有 $\rho$ 的速率，这不能宣称趋零。
以下重新选旗使该问题消失。

令
$$
\sigma=\min\{\rho^{-1/2},(d/m^2)^{1/4}\},\quad
R=\left\lfloor\frac{\sigma m\sqrt{K_{\rm eff}}}{128}\right\rfloor,
\quad s=R-1,\quad T=2R-1.
\tag{4.1}
$$
充分大 $m$ 时 $R\ge2d$ 且 $R\le b/2$。
使用同一个原配对划分的 $N=b-R+1$ 对，末尾起点
$J=m+2N$。保至多 $R$ 个原 $Q$-triplet 块及完整联合 birth：
零 triplet 时 birth 为 $0,\ldots,R-1$；
$\ell\ge1$ 个 triplet 时 birth 为 $0,\ldots,R-\ell$。
每个 sector 的活跃度
$$
t=s+\ell-\mathrm{birth}\in[\max(0,2\ell-1),T]
$$
均使模型高域为零，所有原 cross-birth 成本由已有短 canonical 截面支付。

所需短列参数是
$$
\theta=\frac{12(2R+d)(R+d-1)}{J+1}.
$$
因为 $R\ge2d,\ J+1\ge b,\ b\ge Q/2,\ K_{\rm eff}\le Q/d$，
$$
\theta\le45R^2/b
\le\frac{90\sigma^2m^2}{16384d}
\le\frac{90m}{16384\sqrt d}\longrightarrow0.
\tag{4.2}
$$
同一估计也保证 $R/b\to0$；参数合法没有使用尾速率。
原前缀分割定理因此给该真实闭回缩范围上的
$$
\lambda(x)\le C_{\rm tr}\alpha(x),\qquad
C_{\rm tr}<32(1+R/m)\le\sigma\sqrt{K_{\rm eff}}
\le\sqrt{K_{\rm eff}/\rho}.
\tag{4.3}
$$
末个 $32+\sigma\sqrt{K_{\rm eff}}/4$ 的常数项由
$\sigma\sqrt{K_{\rm eff}}\to\infty$ 吸收。

同一原角算子 $C$ 的角谱旗取
$$
\tau=\max\{\rho/K_{\rm eff},K_{\rm eff}^{-2}\},\qquad
\mathscr F_{\rm ang}=B^{-1/2}\operatorname{Ran}1_{[\tau,1]}(C).
$$
在它上面
$$
\lambda(x)\le C_{\rm ang}\alpha(x),\qquad
C_{\rm ang}=\tau^{-1/2}
=\min\{\sqrt{K_{\rm eff}/\rho},K_{\rm eff}\}.
\tag{4.4}
$$
这两个范围始终位于同一原源空间，保同一个原 $A_m,D_m,b$。

## 5. 相交、联合与全部最终费用

分别把 §4 两旗与 $\mathscr D_1$ 相交，并令
$P_{\rm tr},P_{\rm ang}$ 为它们在原 $M_2$ 内的真正正交投影。
置
$$
\mathsf T=\tfrac12(P_{\rm tr}+P_{\rm ang}),\qquad
Y_\rho=\operatorname{Ran}1_{[\sqrt\rho,1]}(\mathsf T).
$$
对 $r^1$ 作 $Y_\rho$ 的 $M_2$ 投影，记为 $p_1$，令
$\widehat r=r^1-p_1$。

原联合定理给
$$
\mu(p_1)^2
\le\frac{\overline C}{2\sqrt\rho}\Xi(r^1)^2,\qquad
\lambda(p_1)^2
\le\frac{\overline{C^2}}{\sqrt\rho}\Xi(r^1)^2.
$$
由 (2.5)、(4.3)—(4.4)，
$\overline C\le\sqrt{K_{\rm eff}/\rho}$、
$\overline{C^2}\le K_{\rm eff}/\rho$，从而
$$
\boxed{
\mu(p_1)^2\le W_0^2\rho/\sqrt{K_{\rm eff}},\qquad
\lambda(p_1)^2\le2W_0^2\sqrt\rho.
}
\tag{5.1}
$$
这里已经没有增长的 $c$ 乘在 $\rho^{1/4}$ 前面。

同时
$$
\Xi(r^0)^2=\Xi(p_H)^2+\Xi(p_1)^2+\Xi(\widehat r)^2,
$$
$$
\boxed{
\Xi(\widehat r)^2\le2\varepsilon_m^2/K_{\rm eff},\qquad
\frac{\|P_{\rm tr}\widehat r\|_{M_2}^2+
\|P_{\rm ang}\widehat r\|_{M_2}^2}{2}
\le\sqrt\rho\,\Xi(\widehat r)^2.
}
\tag{5.2}
$$
相对测试只针对实际交 $\mathscr D_1$ 后的两旗，没有加入单旗 KKT 的错误结论。

总修正 $p=p_0+p_H+p_1$ 满足
$$
\boxed{
\mu(p)\le a'_m\varepsilon_m+
W_0\sqrt\rho\,K_{\rm eff}^{-1/4}\to0,
}
$$
$$
\boxed{
\lambda(p)\le b'_m\varepsilon_m+
\sqrt2W_0\rho^{1/4}\to0.
}
\tag{5.3}
$$
因原最小选择子线性，
$$
\|E_b^\dagger r-E_b^\dagger\widehat r\|=\mu(p),\qquad
\|F_b^\dagger r-F_b^\dagger\widehat r\|=\lambda(p).
$$
所以最终左像仍趋同一个 $w$，原顶部完整最小链差也趋零。
从该同一最终左像重建全部低层来源，真实前缀及反馈差仍由
$\mu(p)$ 支付；未逐窗口独立校正，未给新顶部伪造原来的未来。

## 6. 更宽约束下的准确未解局部测试

最终源同时满足：

- 整个 $\mathscr F_h$ 的 $L+B$ 负前缀，$h>d^{3/4}/16$；
- 原 $\mathscr F_H\cap\mathscr D_h$ 的精确两费正交测试，$H=2h$；
- 同闭余空间内重选两旗的相对小投影；
- (5.2) 的有效预算，且 $K_{\rm eff}$ 具有 (2.5) 的明确指数下界。

因此固定测试局部 Gram 稿可以直接取
$\mathscr D=\mathscr D_h$、精确头宽 $H=2h$。
对每个固定物理测试维数 $n$，若能沿无限子序列证明这个真实
局部 Gram 为 $O_n(K_{\rm eff})$，(5.2) 与同一个 $w$ 的强极限
仍给 $w=0$。原共同固定测试的矩阵 Bessel 预算继续使用原 $K$，
比用 $K_{\rm eff}\le K$ 的数值界更强；其旧未来弱配对只用于旧原未来，不自动转给新顶部。

本文没有证明上述局部 Gram 界，没有把两种正交度量换成物理坐标删除，也没有支付实际测试内部 $e_p$ 的右修复、右端点或纯高深段总费。更宽负前缀是已完成的归约，普通 ISP 与原无权 $N=M$ 仍待这些真实余项闭合。
