# R271 附录：固定头相似下对全部孔层统一的无限窗收敛率

日期：2026-11-13（UTC）。作者：boundary_resume_1cf；Astra-ISP-1cf8c51d 已核查准确零源核、有限传播、原范数正交及全部源的 Gram 比较。状态：下述相对能量与极小链收敛率已证明；没有得到真实无权 $N=M$。

本稿承接 [R239 闭链稿 §6](R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)。该节已证明，固定 $m,q$ 时，有限窗最小修复范数下降到无限高尾最小值。本稿补出的范围是：固定有限头相似后，收敛率同时对全部 $q$ 和全部源统一，并给实际极小链及 Gram 的相对误差。头相似的条件数完整保留，不称它是等距。

## 1. 模型、所有极小值及结论

固定 $m$，令 $d=2^m$、$A=A_m$、$D=D_m$、$L=A+D$。头空间为 $\mathbb C^d$，尾空间按孔数正交分解为 $\bigoplus_{p\ge0}\mathcal H_p$，且 $D\mathcal H_p\subset\mathcal H_{p-1}$。本稿的 $q$ 是任意固定非负整数，不要求处于既有真实 lift 的合法大窗内。

在
$
X_q=\mathbb C^d\otimes\bigoplus_{p>q}\mathcal H_p
$
上记
$
K_\infty=\ker(P_{>q}L|_{X_q}),\qquad F c=P_q Lc=D c_{q+1}.
$
对长度 $h$ 的窗口，令
$
X_{q,h}=\mathbb C^d\otimes\bigoplus_{p=q+1}^{q+h}\mathcal H_p,
\qquad K_h=K_\infty\cap X_{q,h}.
$
固定源 $r\in\mathbb C^d\otimes\mathcal H_q$，定义
$
\lambda_h(r)=\min\{\|c\|:c\in K_h,\ Fc=r\},\qquad
\lambda_\infty(r)=\min\{\|c\|:c\in K_\infty,\ Fc=r\}.
\tag{1.1}
$
对 $h\ge d$，这些仿射集非空；可直接使用旧相容原像族构造长度 $d$ 的可行链。它们都是 Hilbert 空间中的闭仿射集，故各有唯一极小元，分别记作 $c_h(r)$、$c_\infty(r)$。这里不使用无限内部输出算子的闭像。

选取任意有限头相似 $S$，使
$
J=S^{-1}AS
$
是带权有限 Jordan 后移；每条链的头级数取 $0,\ldots,\ell-1$，所以 $J$ 准确降低头级数 $1$，最大头级数不超过 $d-1$。对当前单链模型可取一条长度 $d$ 的链。令
$
\kappa=\|S\|\,\|S^{-1}\|\ge1.
\tag{1.2}
$
头链的边权不必均为 $1$。

若 $\kappa>1$，置
$
\rho=\frac{\kappa-1}{\kappa+1},\qquad
a_n=\frac{2\rho^n}{1+\rho^{2n}},\qquad
h_n=d+n(d-1)\quad(n\ge1).
$
则对全部 $q,r,n$，
$
\boxed{
0\le\lambda_{h_n}(r)^2-\lambda_\infty(r)^2
=\|c_{h_n}(r)-c_\infty(r)\|^2
\le(\kappa^2-1)a_n^2\,\lambda_\infty(r)^2.
}
\tag{1.3}
$
特别可把右端放宽为
$
4(\kappa^2-1)\rho^{2n}\lambda_\infty(r)^2.
\tag{1.4}
$
长度 $d$ 本身已满足
$
\boxed{\lambda_\infty(r)\le\lambda_d(r)\le\kappa\lambda_\infty(r).}
\tag{1.5}
$
若 $\kappa=1$，则所有源的无限窗极小元已经支持在前 $d$ 个尾孔层，因而 $\lambda_d=\lambda_\infty$。$d=1$ 也直接属于这一情形。

## 2. 准确零源空间和总级数

把头相似完整张量上尾恒等算子，仍记作 $S$，并通过标量缩放令
$
\|S^{-1}\|=1,\qquad R=S^*S,\qquad I\le R\le\kappa^2I.
\tag{2.1}
$
该缩放不改变 $J$ 或 $\kappa$。

在相似后的坐标里，赋予“头链级数加尾孔数”总级数 $g$。算子 $J+D$ 严格把 $g$ 降低 $1$，而 $P_{>q}$ 与全部总级数投影交换。因此内部核和准确零源核都按总级数正交分解。

本稿使用的零源核为
$
Z=\{u\in X_q:(J+D)u=0\}.
\tag{2.2}
$
它是闭子空间；记其正交投影为 $P_Z$。这里要求完整输出为零，已包括第 $q$ 层输出，故没有把内部核误当成准确零源核。由于上述齐次性，$P_Z$ 与每个总级数投影交换。

相似后所有可行修复构成一个仿射空间 $u_0+Z$，其原范数准确为
$
\|Su\|^2=\langle Ru,u\rangle.
\tag{2.3}
$
头算子 $R$ 不改变尾孔数，只可能改变头级数；所以它在总级数上的带宽不超过
$
b=d-1.
\tag{2.4}
$
同样，$P_ZR|_Z$ 的带宽不超过 $b$。

## 3. 从真正无限窗极小元得到长度 $d$ 的可行锚

令 $u_\infty=S^{-1}c_\infty(r)$。截取其总级数不超过 $q+d$ 的部分：
$
u_0=P_{g\le q+d}u_\infty,\qquad c_0=Su_0.
\tag{3.1}
$
截断保持内部核。第 $q$ 层输出只可能来自尾孔 $q+1$ 且头级数在 $0,\ldots,d-1$ 的输入，即只来自总级数 $q+1,\ldots,q+d$。所以 (3.1) 准确保留源 $r$，而不是只保留其投影。

又因头级数非负，$u_0$ 的尾孔数不超过 $q+d$；$S$ 保留尾孔数，因此 $c_0$ 是长度 $d$ 的真正可行修复，且
$
\|c_0\|\le\|S\|\,\|S^{-1}\|\,\|c_\infty\|
=\kappa\lambda_\infty.
\tag{3.2}
$
这已证明 (1.5)。

令
$
k_\infty=u_\infty-u_0\in Z.
$
真正极小元 $c_\infty$ 与全部零源方向 $SZ$ 正交，故
$
\|Sk_\infty\|^2
=\|c_0-c_\infty\|^2
=\|c_0\|^2-\|c_\infty\|^2
\le(\kappa^2-1)\lambda_\infty^2.
\tag{3.3}
$

## 4. 有带宽的正 Gram 及多项式逆

在 $Z$ 上定义
$
G=P_ZR|_Z,\qquad h=P_ZRu_0.
\tag{4.1}
$
由 (2.1)，
$
I_Z\le G\le\kappa^2 I_Z.
\tag{4.2}
$
因此 $G$ 是整个闭空间 $Z$ 上的有界正可逆算子。此处的逆不是全尾删除算子的无界 Moore--Penrose 逆，也没有改变原 Hilbert 范数。

最小性方程恰为
$
G k_\infty=-h.
\tag{4.3}
$
按 (3.1) 和带宽界，$h$ 只含总级数不超过 $q+d+b$ 的项。任何 $n-1$ 次 $G$ 多项式作用到 $h$，其总级数不超过
$
q+d+b+(n-1)b=q+d+nb=q+h_n.
\tag{4.4}
$

为完整给出所用逼近，取 Chebyshev 多项式 $T_n$，并令
$
p_n(x)=
\frac{
T_n\!\left(\frac{\kappa^2+1-2x}{\kappa^2-1}\right)
}{
T_n\!\left(\frac{\kappa^2+1}{\kappa^2-1}\right)
}.
\tag{4.5}
$
这里 $p_n(0)=1$，所以
$
Q_{n-1}(x)=\frac{1-p_n(x)}{x}
$
是次数不超过 $n-1$ 的真正多项式。对 $1\le x\le\kappa^2$，分子绝对值不超过 $1$；又
$
\frac{\kappa^2+1}{\kappa^2-1}
=\frac{\rho+\rho^{-1}}2,
\qquad
T_n\!\left(\frac{\rho+\rho^{-1}}2\right)
=\frac{\rho^n+\rho^{-n}}2.
$
故
$
\sup_{x\in[1,\kappa^2]}|p_n(x)|\le a_n.
\tag{4.6}
$

定义有限传播的零源修正
$
k_n=-Q_{n-1}(G)h\in Z,\qquad c_n=S(u_0+k_n).
\tag{4.7}
$
它与 $c_0$ 有相同源。由 (4.4)，$u_0+k_n$ 的尾孔数不超过 $q+h_n$；$S$ 不改变尾孔数，所以 $c_n$ 是长度 $h_n$ 的可行修复。

由 (4.3)，
$
k_n-k_\infty=-p_n(G)k_\infty.
$
在 $Z$ 上，$R$ 的二次型等于 $G$ 的二次型。因此谱定理和 (4.6) 给
$
\begin{aligned}
\|c_n-c_\infty\|^2
&=\langle Gp_n(G)k_\infty,p_n(G)k_\infty\rangle\\
&\le a_n^2\langle Gk_\infty,k_\infty\rangle\\
&=a_n^2\|Sk_\infty\|^2\\
&\le(\kappa^2-1)a_n^2\lambda_\infty^2.
\end{aligned}
\tag{4.8}
$
因为 $c_n-c_\infty\in SZ$，它与 $c_\infty$ 正交，故 $\|c_n\|^2$ 是 $\lambda_\infty^2$ 加上 (4.8)。

真正长度 $h_n$ 极小元不比 $c_n$ 大；它与 $c_\infty$ 之差同样属于 $SZ$，因而
$
\|c_{h_n}-c_\infty\|^2
=\lambda_{h_n}^2-\lambda_\infty^2
\le\|c_n-c_\infty\|^2.
$
这证明 (1.3)。若 $\kappa=1$，则 $R=I$，不同总级数本来正交，(3.3) 已直接给 $c_0=c_\infty$。

## 5. 实际 Gram 的统一相对收敛

令
$
\mathsf G_h=F P_{K_h}F^*,\qquad
\mathsf G_\infty=F P_{K_\infty}F^*,
\tag{5.1}
$
其中有限窗投影按零延拓嵌入 $X_q$。固定 $m,q$ 下，长度 $d$ 的有界右逆已给 $\mathsf G_d>0$，故这些 Gram 对 $h\ge d$ 及 $h=\infty$ 都有有界逆。准确最小值公式为
$
\lambda_h(r)^2=\langle\mathsf G_h^{-1}r,r\rangle.
$
由 (1.3)，置 $\varepsilon_n=(\kappa^2-1)a_n^2$，有
$
\boxed{
\mathsf G_{h_n}
\le\mathsf G_\infty
\le(1+\varepsilon_n)\mathsf G_{h_n}.
}
\tag{5.2}
$
此处对全部源同时成立，因此是算子二次型不等式，不仅是某个残量的估计。

若要求实际极小链相对误差不超过 $\varepsilon\lambda_\infty$，由
$
-\log\rho=\log\frac{\kappa+1}{\kappa-1}\ge\frac2\kappa
$
可取满足
$
n\ge\frac{\kappa}{2}
\log\frac{2\sqrt{\kappa^2-1}}{\varepsilon}
\tag{5.3}
$
的正整数；若右侧非正，任意正整数已足。这给出只依赖有限头相似及目标精度的窗口长度，与 $q,r$ 无关。

## 6. 对当前研究边界的准确含义

本稿新增的是固定 $m$ 时对全部 $q$ 和全部源统一的相对收敛率，并没有消去其对 $\kappa_m$ 的依赖。它不假设尾删除在全 Hilbert 空间上满射，也不把有限头 Jordan 相似当成等距。

当 $m=m(q)$ 随原真实大窗增长时，必须重新支付 $\kappa_m$ 及 (5.3) 所需宽度；不能把本稿保证的宽度直接塞进旧真实 lift 的合法范围。旧全低输出坏方向的无限窗下界仍然成立，因为 (1.3) 只比较同一源的有限窗与无限窗能量，没有把任何一者压到所需无权数量级。

因此真实 $w\in M$ 的特殊残量最小能量、低核头跃迁通量，以及普通无权 $N=M$ 仍是未完成项。

## 7. 代入已证最优头条件数后的证书宽度

本节只量化本稿 §4--5 的相似与 Chebyshev 证书所需的窗口，不给实际极小链收敛速度的下界。

[R249 平衡相似](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) §§1--4 已经对两个实际头构造
$
S_m=\operatorname{diag}(e^{-F(n)})\,C_{\widetilde h}^{\mathsf T},
\qquad
S_m^{-1}A_mS_m=\lambda_mJ_d.
$
其中
$
\begin{aligned}
L_m&=\frac{25}{2}\frac{d^4}{d-2},&
F(n)&=L_mn-\omega_n,\\
\omega_{d-1}
&=\frac{20}{3}d^4-15d^3+(150m-275)d+\frac{850}{3},&
\lambda_m&=e^{20-L_m}.
\end{aligned}
$
记
$
\Psi_m=L_m(d-1)-\omega_{d-1}+d\log12+2\log d.
$
该稿准确给出
$
\log\kappa(S_m)\le\Psi_m
=\frac{35}{6}d^4+O(d^3+md).
\tag{7.1}
$

另一方面，[R249 最优性附录](R249-appendix-optimal-true-head-chain-similarity-cost.md) 定理 (1.3)、式 (6.1) 对任意非零加权单链和任意相似矩阵都给
$
\kappa\ge
\frac{s(s-1)}{4(2s-1)m^2}\frac{\alpha_0}{\alpha_{m-1}},
\qquad s=d/2,
$
亦即
$
\begin{aligned}
\log\kappa\ge{}&
\frac{35}{6}d^4-\frac{45}{4}d^3+150d-\frac{850}{3}-20\\
&+\log\frac{s(s-1)}{4(2s-1)m^2}.
\end{aligned}
\tag{7.2}
$
因此，在全部允许的头链和相似中，最佳条件数的对数主项就是 $(35/6)d^4$。本节没有重新构造或重新计数这一旧结论。

现在固定相对链误差目标 $0<\varepsilon<1$。令
$
u=\log\frac{\kappa+1}{\kappa-1}>0.
$
本稿 (1.3) 的准确证书系数是
$
(\kappa^2-1)a_n^2
=(\kappa^2-1)\operatorname{sech}^2(nu).
\tag{7.3}
$
若 $\sqrt{\kappa^2-1}>\varepsilon$，使这个系数不超过 $\varepsilon^2$ 的充要条件为
$
\boxed{
n\ge
\frac{\operatorname{arcosh}\bigl(\sqrt{\kappa^2-1}/\varepsilon\bigr)}
{\log((\kappa+1)/(\kappa-1))}.
}
\tag{7.4}
$
这里的“充要”仅针对明确的数值证书 (7.3)，不是针对实际链误差。若 $\sqrt{\kappa^2-1}\le\varepsilon$，长度 $d$ 的 (1.5) 已足。

当 $\kappa\to\infty$ 而 $\varepsilon$ 固定时，
$
u=\frac2\kappa+O(\kappa^{-3}),\qquad
\operatorname{arcosh}\frac{\sqrt{\kappa^2-1}}{\varepsilon}
=\log\frac{2\kappa}{\varepsilon}+O_\varepsilon(\kappa^{-2}).
$
故由 (7.4) 保证所需精度的最小整数 $n$，及本稿窗口 $h=d+n(d-1)$，满足
$
n=\left(\frac12+o(1)\right)\kappa\log\frac{2\kappa}{\varepsilon},
\qquad
\log h=\log\kappa+\log d+\log\log\kappa+O_\varepsilon(1).
\tag{7.5}
$
结合 (7.1)--(7.2)，在本相似证书中最优选择头链时，
$
\boxed{
\log h_{\rm cert}
=\left(\frac{35}{6}+o(1)\right)d^4.
}
\tag{7.6}
$
下界对所有头相似成立；上界由 R249 的明确 $S_m$ 达到相同主项。

原实际稳定 lift 所覆盖的输入孔数上限则为
$
Q_0\le \exp(d^3/3)
$
（见 [R239 全整数窗口稿](R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md) 的实际线性 lift，以及 [R271 准确插值稿](R271-appendix-exact-stable-range-interpolation-and-norm-defect.md) 对该合法范围的复核）。本稿有限修复的最大孔数为 $Q_0=q+h_{\rm cert}$。对固定精度目标，(7.6) 给
$
\log(q+h_{\rm cert})\ge\log h_{\rm cert}
=\left(\frac{35}{6}+o(1)\right)d^4>d^3/3
$
当 $m$ 充分大时成立。因此，本证书保证精度所需的宽度，不能直接代入现有同一个 $m$ 的真实 lift。

这一比较只排除“把固定头相对率不付条件数地直接接到现有合法大窗”这一步。它既不证明实际 $\lambda_h(r)$ 必须收敛得慢，也不排除对真实源的更快收敛、直接的低核通量估计或另一种保留原范数的证书。

