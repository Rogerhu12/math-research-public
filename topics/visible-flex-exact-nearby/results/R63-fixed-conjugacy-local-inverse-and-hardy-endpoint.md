# R63：固定共轭的局部 Wiener 逆与 Hardy 端点转换

2026-11-12。两个实际减费接口：固定已保存的有限 $H$ 后，在恒等坐标使用
R31；将 R61 的端点复带误差以 Parseval 而非逐系数求和转换为 Wiener 误差。
本结果不宣布实际返回已通过 KAM，也不替代全时间残差或完整参数导数。

## 1. 记号与准确对象

$A_s$ 是 $2\pi$ 周期 Fourier Wiener 代数，
$\|v\|_s=\sum_k|v_k|e^{s|k|}$。固定真实有限实三角多项式
$H(x)=x+h(x)$，$H'(x)>0$ 于实圆。$\omega$ 是准确目标旋转角。
$F_p$ 表示同一真实几何对象产生的返回 lift；参数变化时 **$H$ 固定**。
假设实际复合误差

\[
 E_p(x)=F_p(H(x))-H(x+\omega)\in A_s                 \tag{63.1}
\]

已存在，并在所声明的整个真实参数区间连续或可微。这个假设须由 R60/R61
的真实流和域门支付，不能用有限射线、有限 Fourier 插值或本文的有限 $H$ 预算代付。

## 2. 直接在 Wiener 代数解局部逆

设

\[
 \|(H')^{-1}\|_s\le R,\qquad
 \|H''\|_{s+r}\le B_H,\qquad
 \kappa=R B_H r\le\tfrac12,\qquad
 R\sup_p\|E_p\|_s\le r/2.                            \tag{63.2}
\]

则唯一的 $u_p\in A_s$、$\|u_p\|_s\le r$ 满足

\[
 H(x+\omega+u_p(x))=H(x+\omega)+E_p(x).              \tag{63.3}
\]

这里的唯一性是闭球 $\|u\|_s\le r$ 内的唯一性。定义
$q_\omega=1/H'(x+\omega)$，并写

\[
 N(u)=H(x+\omega+u)-H(x+\omega)-H'(x+\omega)u.
\]

有限 Fourier 复合和 $A_s$ 代数性质给
$\|N(u)\|_s\le B_H\|u\|_s^2/2$，以及在该球上
$\|N(u)-N(v)\|_s\le B_Hr\|u-v\|_s$。
算子 $u\mapsto q_\omega E_p-q_\omega N(u)$ 将球映入半径
$r/2+\kappa r/2\le3r/4$ 的球，并以常数 $\kappa$ 收缩。
Banach 定理因此给 (63.3)，且

\[
 \|u_p\|_s\le\frac{R\|E_p\|_s}{1-\kappa/2}
 \le2R\|E_p\|_s,\qquad
 \left\|\frac1{H'(x+\omega+u_p)}\right\|_s
 \le\frac R{1-\kappa}.                              \tag{63.4}
\]

最后一个不等式由
$H'(x+\omega+u)=H'(x+\omega)+\Delta H'$、
$\|q_\omega\Delta H'\|_s\le\kappa$ 的 Neumann 级数得到。
整个证明只用有限 $H$ 的 Fourier 复合，未假设一个额外的全复带单叶域。
由于收缩与共轭复数运算可交换，实参数给实 $u_p$；真实 $F_p$ 若保向，
$G_p=x+\omega+u_p$ 在实圆满足
$G_p'=F_p'(H)H'/H'(G_p)>0$。它就是准确的实圆 $H^{-1}F_pH$ 分支。
参数光滑性由统一收缩及可逆的线性化算子继承。

## 3. 真正的预共轭参数源与 R31 接口

在同一个固定 $H$ 下准确微分 $H(G_p)=F_p(H)$：

\[
 \partial_pG_p=\frac{(\partial_pF_p)(H)}{H'(G_p)},
 \quad
 \partial_p^2G_p=
 \frac{(\partial_p^2F_p)(H)-H''(G_p)(\partial_pG_p)^2}{H'(G_p)},       \tag{63.5}
\]

\[
 \partial_x\partial_pG_p=
 \frac{(\partial_x\partial_pF_p)(H)H'(x)
       -H''(G_p)(\partial_pG_p)G_p'}{H'(G_p)}.        \tag{63.6}
\]

这些导数必须来自真实两腿流及移动根链式源（R62），并取实际连续 Wiener 界。
八条射线或其插值值只用于选择计算策略，不能充当 $P,Q,T$。
若 (63.2) 已在外宽 $s+\eta$ 上支付，则内宽可取

\[
 \|G_p''\|_s=\|u_p''\|_s
 \le \frac2{\eta^2}\|u_p\|_{s+\eta}.                \tag{63.7}
\]

证明是逐 Fourier 模使用 $k^2e^{-\eta|k|}\le2/\eta^2$。
这避免从非线性的原坐标给出过大的二阶界，但外宽实际误差仍须供应。
现在可对 $G_p$ 在恒等共轭处使用 R31：初始 $M_0=R_0=1$，误差是
$u_{p_0}$，所有中间域必须包含于已经验证的 $G_p$ 域。
若 R31 真正产生 $k$，则物理初值角共轭为 $H\circ k$。
本节仅给准确转换，未支付 R31 的横截、误差、参数盒或迭代不等式。

## 4. Hardy/Parseval 的全模端点界

设 $g$ 在闭复带 $|\Im x|\le S$ 上连续、内部解析并 $2\pi$ 周期，
且归一化边界平方平均满足

\[
 \varepsilon_B^2=
 \frac{\|g(\cdot+iS)\|_{L^2}^2+\|g(\cdot-iS)\|_{L^2}^2}{2},
 \quad \|v\|_{L^2}^2=\frac1{2\pi}\int_0^{2\pi}|v(x)|^2dx.
\]

Parseval 给 $\sum_k|g_k|^2\cosh(2kS)=\varepsilon_B^2$。对 $s<S$，
$d=S-s$，Cauchy–Schwarz 于是给

\[
 \boxed{\ \|g\|_s\le\varepsilon_B
  \left(\sum_{k\in\mathbb Z}\frac{e^{2s|k|}}{\cosh(2kS)}\right)^{1/2}
  \le\varepsilon_B\sqrt{1+\frac4{e^{2d}-1}}
  =\varepsilon_B\sqrt{2\coth d-1}.\ }                \tag{63.8}
\]

其中常数模恰贡献 $1$，每对 $\pm k$ 的贡献至多 $4e^{-2dk}$；没有漏掉
常数、负模或无限尾。若只有全边界 sup 界 $\varepsilon$，可取
$\varepsilon_B\le\varepsilon$。若边界被完整无缺口的有限实弧覆盖，每弧
误差上界 $\varepsilon_j$，可按准确弧长对 $\varepsilon_j^2$ 求和；上下两条
边界分别支付并取平均，实对称时仅一边的求和即可。单个已验证弧不提供这个平均。

R61 中 $g=Z_{\rm end}-Y_{\rm end}$ 为物理角误差。于是完整归一化返回残差满足

\[
 \|E\|_s\le\|E_{\rm ref}\|_s
   +4\varepsilon_B\sqrt{2\coth(S-s)-1}.              \tag{63.9}
\]

系数 $4$ 来自归一化角 $x=4\theta$；有限 $E_{\rm ref}$ 仍须保留准确
$-\omega$ 常数、真实两腿端点和所有跳跃。全流解析性和整条边界覆盖仍由
R60/R61 提供，(63.8) 不使单弧证明变成全复带证明。

## 5. 同一已保存有限 H 的实际预算

脚本 `scripts/fourfold_circle_local_inverse_budget.py` 对 δ₃ 的 H129 与 δ₄
的 H258，独立准确整数卷积 $H'q-1$，之后才用 192-bit Arb 对加权模和、
Neumann 逆、$H''$ 以及 (63.8) 的因子作有向计算。所有输出都有准确 dyadic
上下端点；浮点显示仅方便阅读。$H'(0)>0$ 以整数验证，$\|H'q-1\|_s<1$
排除实圆零点，从而全实圆 $H'>0$。

结果存 `notes/2026-11-12-R63-finite-local-inverse-budget.json`，输入SHA列在报告。
取 $s=1/128,r=1/1000$，两个有限 H 的收缩门均通过。
这里的可容许实际返回误差阈值只是 (63.2) 的最后一项上限；没有把未知
$\|E_p\|_s$ 置零。宽差 $1/512,1/256,1/128$ 的新因子分别约为
$31.9844,22.6054,15.9689$，原逐系数因子分别约为 $1024,512,256$。
这些减费只改变证明预算，主目标仍须实际 KAM、完整全频逆及非线性精确族。
