# R106：完整 pure 幂尾递归的反射奇偶律

日期：2026-11-14。**已证明。** 完整纸面推导，无新的研究运算。本文从 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 的原始完整恢复递归出发，继续 [R104](R104-reflected-reversed-four-block-c8-cancellation.md)。它没有只由 c⁸ 的一个短式猜测其他系数，也没有将反射当作完整右锚第四成本的加法逆元。

结论：对 m=8 的既有有限 pure 尾多项式，scalar 反射 σ:(h,k,ω)↦(h,−k,−ω) 使第 rʲ 系数的完整周期多项式满足

$$
\mathscr A_{j,\sigma B}(c)=(-1)^j\mathscr A_{j,B}(-c),
\qquad r=c-\xi.
\tag{1}
$$

因此 R104 的真实四块闭合带上，D25 周期多项式准确为

$$
\boxed{
\mathscr A_{25,\mathcal C}(c)
=2\{\mathscr A_{25,B}(c)-\mathscr A_{25,B}(-c)\}
=4(a_7c^7+a_5c^5+a_3c^3+a_1c).
}
\tag{2}
$$

最后等式使用 R95 的次数至多八。四个 aⱼ 是原 B 的真实周期系数，并未证明为零。所有偶参数系数准确消失；没有完整第四函数、mixed 模式或 ruling 已付的结论。

## 1. 尾代数与锚的准确含义

沿用已公开 pure-tail 编译的对象 q=(c−ξ)⁸。它在右端附近采用单位幂尾，在该端右边为零；计算其尾表达式时，所有右原函数可取尾端 c 为锚，因为 c 与真正右 collar 之间的被积式为零。原算法保留完整真实 s 历史，不将第三历史或左尾归零。

把当前有限尾表达式写为 r=c−ξ 的多项式，系数是 c、真实几何 jets 和同一 s 首锚历史的有限表达式。原 R56 的有理 z 项已经在完整分子恢复中准确消掉；对 m=8 到第四阶，已发布尾编译采用的正是此有限多项式空间。

在这个代数中，定义

$$
(\mathscr J f)(s,c,\xi)=f(s,-c,-\xi),\qquad
(\mathcal I f)(s,c,\xi)=\int_c^\xi f(s,c,\eta)\,d\eta.
\tag{3}
$$

对每个有限多项式都准确有

$$
\partial_\xi\mathscr J=-\mathscr J\partial_\xi,
\qquad \partial_s\mathscr J=\mathscr J\partial_s,
\qquad \boxed{\mathcal I\mathscr J=-\mathscr J\mathcal I.}
\tag{4}
$$

最后一式直接来自 η↦−η 的换元：上下限 c、ξ 一起变成 −c、−ξ，且 dη 取负。它保持真实尾端锚，不添加积分常数。

此处没有断言固定全带的右端 b 在反射后仍是另一带的右端。若固定全带 [a,b]，改用反射带的右端 −a，则确实还要加[先前反射说明](../notes/pure-tail-c8-sign-reflection-and-right-anchor-20261114.md)中的全带 ruling 积分。本文使用 (3) 的**移动尾端 c**，证明有限尾多项式之间的代数身份。反射后的中间表达式可以位于尾端的另一侧；有限多项式恒等式的延拓不等于把旧全局 profile 反射后仍称为同一物理带。

## 2. 几何系数与第一分子

记 S=diag(−1,1,1)，并令 σ 几何始终保持正向 s。写

$$
z=\xi+\omega,\quad e=hz-k,\quad \gamma=h_s,\quad \nu=\omega_s,
$$

$$
\lambda=\frac{\gamma z-h\nu}{h^2},\qquad
K_0=kz^2-\frac{k^2+1}{h}z.
$$

带波浪号表示在 σ 几何上、使用同一个符号 c、ξ 重新执行原完整递归。直接代入给

$$
\widetilde z=-\mathscr Jz,\qquad
\widetilde e=-\mathscr Je,\qquad
\widetilde\lambda=-\mathscr J\lambda,\qquad
\widetilde K_0=-\mathscr JK_0.
\tag{5}
$$

h、γ 不变，ν 反号，且 Ω(−k)=SΩ(k)S。因此若 Ṽ=S𝒥V，则协变导数满足

$$\widetilde{\nabla_s V}=S\mathscr J(\nabla_s V).\tag{6}$$

对 q=(c−ξ)⁸，有 𝒥q=q。R56 的第一分子

$$V_q=(-q_\xi/2,\ 0,\ hq-eq_\xi/2)$$

由 (4)、(5) 满足

$$\boxed{\widetilde V_q=S\mathscr J V_q.}\tag{7}$$

这一步的 q 在同一 c 下定义，没有更换某个 s 段的 profile。

## 3. 完整 forcing 与右原函数的归纳

假设某次二次 forcing 使用的全部已知分子满足 Ṽᵢ=S𝒥Vᵢ。forcing 的对称系数矩阵与 c、ξ、s 无关，按原递归保持不变。用 R56 四个完整配对，则

$$
\widetilde J_H=\mathscr J J_H,\quad
\widetilde T_\xi=\mathscr J T_\xi,\quad
\widetilde T_s=\mathscr J T_s,\quad
\widetilde T_{s\xi}=-\mathscr J T_{s\xi}.
\tag{8}
$$

两个 ξ 导数给两个负号，而 mixed 配对只有一个。S 是正交矩阵，故点积没有附加符号。

定义真实尾锚分量

$$
P=-\frac{\mathcal I T_\xi}{2h},\qquad
B_H=\frac{J_H}{2h}.
$$

由 (4)、(8)，

$$\boxed{\widetilde P=-\mathscr JP,\qquad
\widetilde B_H=\mathscr JB_H.}\tag{9}$$

R56 的完整 characteristic 密度为

$$
\mathcal R_H=
\frac{T_s}{2h^2}+K_0P-\lambda P_s
+\left(kz-\frac{k^2+1}{h}\right)B_H
-\frac\gamma{h^2}(B_H)_s.
\tag{10}
$$

逐项使用 (5)、(8)、(9)：K₀P 中两个负号相消；λPₛ 亦然；kz 变成 𝒥(kz)，其余局部系数保持。因此

$$\boxed{\widetilde{\mathcal R}_H=\mathscr J\mathcal R_H.}\tag{11}$$

所有 W 都采用同一个真实 s 初值零锚。𝒥 与 s 积分交换，所以

$$\boxed{\widetilde W=\mathscr JW.}\tag{12}$$

这保留沿整条 B 累积的每条真实 s history；没有逐段重锚，也没有把端值未知的第三历史设为零。

## 4. 完整恢复封闭归纳

R56 的另一个完整量为

$$
\eta_0=-\frac{T_{s\xi}}{2h}
+\frac{\gamma z-h\nu}{2h}P_\xi
+\frac\gamma{2h}(B_H)_\xi-\frac12P_s.
\tag{13}
$$

(4)、(5)、(8)、(9) 给四项一致变号：

$$\widetilde\eta_0=-\mathscr J\eta_0.\tag{14}$$

令 a_H=W_ξ/2+η₀/h，则 ã_H=−𝒥a_H。恢复分子是

$$V_{\rm new}=(a_H,\ zP+B_H,\ ea_H-hW).$$

第一分量变号，后两分量不变，故

$$\boxed{\widetilde V_{\rm new}=S\mathscr J V_{\rm new}.}\tag{15}$$

(7) 是归纳起点，(8)–(15) 是完整归纳步。因此原第二、第三和 pure 第四递归都满足这些式子，包含全部 local、mixed、normal 及真实 history 项。pure 第四 forcing 中的既有常数 −1/16、−1/4 不影响推导；本稿未将它替换成只含某个最高 jet 的近似。

已发布尾编译也使用 completed 变量 W⁺=W+λP。因为 λ、P 各取负号，其乘积满足 λ̃P̃=𝒥(λP)，所以 W⁺ 和其 s 密度同样服从 (11)、(12)。故以下奇偶律同时适用于原始和 completed 的完整第四 period 密度，不依赖删掉端势后的表达式选择。

## 5. 系数奇偶律

在 pure 第四层，将完整有限尾密度写为

$$\mathcal R_4(s,c,\xi)=\sum_jD_{j,B}(s,c)(c-\xi)^j.$$

由 (11)，对 σB 得

$$
\sum_jD_{j,\sigma B}(s,c)(c-\xi)^j
=\sum_jD_{j,B}(s,-c)(-c+\xi)^j.
$$

比较 r=c−ξ 的真实多项式系数，得到

$$D_{j,\sigma B}(s,c)=(-1)^jD_{j,B}(s,-c).\tag{16}$$

对相同正向 s 区间积分即得 (1)。这首先是完整尾多项式的身份，随后可以在任意共同正物理 I 内使用 c 的值；不要求 c=0 属于 I。

这里没有从右侧求值点向左侧实际 profile 偷换边界条件。证明在 (3) 的有限多项式代数内保留了所有锚和真实 s history；相同多项式在尾端两侧的延拓仅用于比较其系数。

## 6. R104 四块中的真实支付范围

R104 的每块完整 M=0，所以完整第四成本准确相加，且真实倒行保持第四成本。设 V_B、V_{σB} 分别是两个实际块、同一个全带右锚和 profile 的完整成本，则仍只有

$$V_{\mathcal C}=2V_B+2V_{\sigma B}.$$

对这一函数取当前指定的 D25 尾系数时，才由 (1) 得到 (2)。这是一个真正的消项：此前 c⁰、c²、c⁴、c⁶、c⁸ 全部消失，c¹⁰ 也已由 R95 的零端势消失；可能留下 c、c³、c⁵、c⁷。

更一般地，对当前 m=8 pure 尾展开中的每个 j，四块系数多项式具有与 j 相同的 c 奇偶性：偶 j 保留偶 c 幂，奇 j 保留奇 c 幂。但这不是所有尾系数同时为零，更不将其外推到任意全局 profile 的整个第四函数。

完整第四 ruling 仍采用固定全带右锚，其反射缺陷继续由全带积分给出；(3) 没有替它付款。第三 ruling、合法 profile 圆、完整两个 phase 模式、第四整个 period、有限阶之后的收敛及主课题几何条件也均需另付。
