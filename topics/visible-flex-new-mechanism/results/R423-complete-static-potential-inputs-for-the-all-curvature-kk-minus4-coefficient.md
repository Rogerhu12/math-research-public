# R423：全曲率负四 kk 的原 N0 一次负幂与四个势响应

日期：2026-11-16。仅纸面原式推导和来源只读；没有执行新的 profile 评价、积分、符号程序、人工检查或科学运行。

本稿固定一个可以立即使用的完整原势结论：
$$
\boxed{
[N_0]_{h^{-1}}=k(\tau_2+k^2\tau_{2b})\quad(\omega=0),
}
\tag{1}
$$
其中两三槽算子在下文给出**完整独立 outer 公式**。于是负四 $kk$ 的原势校正准确为
$$
\boxed{
-[h^{-4}]\mathcal B_{m_{2,kk}}N_0
=\frac{S}{16}\mathcal B_{\mathbf S}(\tau_0+k^2\tau_1)
-\frac{k^2}{16}\mathcal B_{\mathbf P}(\tau_2+k^2\tau_{2b}),
\qquad S=1+k^2.
}
\tag{2}
$$
原静态势、参考常数、右锚及左尾都保留。没有假定 $\tau_2,\tau_{2b}\in W$。式(2)特别说明，不能把单锚 $k=\omega=0$ 的 $\mathcal B_{\mathbf S}\tau_0/16$ 直接乘 $S$ 后当作全曲率答案。

本稿只固定(1)(2)，**尚不计算完整负四 $kk$ 自然值，不宣布该正字符已排除，不增加实际联合控制结论。** 完整 $v_2-Y\mathscr A$、$-\mathcal B_{m_0}N_2$ 及原有序尾仍须在同一个正规化中合成。

来源为 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R402](R402-complete-static-low-layer-natural-flux-with-original-potential-and-tails.md)、[R417](R417-two-term-static-minus4-natural-image-and-one-remaining-anchor.md)和 [R421](R421-all-curvature-kk-minus6-natural-identity-and-common-character-cancellation.md)。

## 1. 原右锚、状态和完整 outer

固定原合法正窗口 $0<\ell<r_*$，
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
inner 为紧 $g^2$，outer 为独立的右零函数 $f$，允许 $f$ 带真实左二次尾。内两槽按原对称双线性极化。不是只在 $f=g$ 上求一个 diagonal 后猜测 mixed。

写
$$
p_g=g',\quad r_g=g'',\quad
P_g=J(r_g^2),\quad M_g=J(xr_g^2),\quad
C_g=J(x^2r_g^2+2p_g^2),
$$
$$
R_g=p_g^2+xP_g,\quad T_g=x^2p_g^2+xC_g,\quad
F_g=x^2P_g-C_g,\quad G_f=f-xf'/2.
\tag{3}
$$
$\mathbf P=\Phi_{r_0}$、$\mathbf S=\Phi_{s_0}$、$\mathbf Y=\Phi_{p_2}$ 表示原 E8 算子；例如 $\mathbf S(g,g)=M_g$。它们不能与状态标量 $S=1+k^2$ 混淆。

沿 $\omega=0$ 状态线，
$$
e=hx-k,\qquad Q=1+e^2,\qquad h>0.
$$
原第二局部第一分量在水平 $h$ 方向为
$$
a_g=\frac{SA}{h^3}+\frac{kB}{h^2}+\frac{C_a}{h},
$$
$$
A=\frac{R_g'}{16},\quad
B=\frac{R_g-xR_g'}8,\quad
C_a=\frac{x^2R_g'-2xR_g+F_g}{16}.
\tag{4}
$$
原静态中分量和 scalar 密度为
$$
b_g=\frac{SR_g}{8h}+kb_0+h b_1,
$$
$$
b_0=\frac{gp_g}{2}-\frac{3xp_g^2}{8}-\frac{xM_g}{4},
\qquad b_1=\frac{(g-xp_g/2)^2}{2}+\frac{T_g}{8},
$$
$$
q_g=-\frac{S^2R_g}{8h^2}+\frac{kS E_g}{h}
+k^2V_g-\frac{ST_g}{8}-\frac{kh\,\mathbf Y(g,g)}2,
\tag{5}
$$
其中两个原二次输出为
$$
E_g=-\frac{gp_g}{2}+\frac{xp_g^2}{2}
+\frac{x^2P_g}{8}+\frac{xM_g}{4},
$$
$$
V_g=-\frac{g^2}{2}+xgp_g-\frac{x^2p_g^2}{2}-\frac{x^2M_g}{4}.
\tag{6}
$$
式(3)–(6)全部保留原左常数和多项式尾。

## 2. 六个完整映射与原 h 方向密度

使用 R417(8) 的六个完整映射：
$$
\begin{aligned}
\mathsf A_f(H)&=(f''-f'/x)H+J(f'''H),\\
\mathsf B_f(H)&=(xf''-3f'/2+f/x)H+J(xf'''H),\\
\mathsf C_f(H)&=(x^2f''-2xf'+2f)H+J(x^2f'''H),\\
\mathsf D_f(H)&=f'H'+xJ(f''H''),\\
\mathsf E_f(H)&=xf'H'+xJ(xf''H'')-f'H,\\
\mathsf F_f(H)&=x^2f'H'+xJ(x^2f''H''+2f'H').
\end{aligned}
\tag{7}
$$
这些是完整 Volterra 映射，不只保留最高 jet。固定正窗口使 $1/x$ 合法；最终组合中也均带其原 $x$ 因子。

R417(9)由原 R56/R73 先完成真实恢复导数、再置累计 history 值为零得到：
$$
\begin{aligned}
n_\gamma={}&G_f\left(\frac{\partial_h b_g}{2h}
-\frac{b_g}{2h^2}+\frac{xa_g}{2}\right)\\
&-\frac{S^2x}{4h^2}\mathsf A_f(a_g)
+\frac{kS}{4h}\{x^2\mathsf A_f(a_g)+2x\mathsf B_f(a_g)\}\\
&-\frac{Sx}{4}\mathsf C_f(a_g)
-\frac{k^2x^2}{2}\mathsf B_f(a_g)
+\frac{khx^2}{4}\mathsf C_f(a_g)\\
&+\frac{S}{8h^3}\mathsf D_f(q_g)
-\frac{k}{4h^2}\mathsf E_f(q_g)
+\frac1{8h}\mathsf F_f(q_g).
\end{aligned}
\tag{8}
$$
最后一行是原完整 $-\Psi_\gamma$。其中的 $f'H$ 项及所有 primitive 项均保留。

## 3. 新系数的逐项来源

定义
$$
\mathcal T_2=\frac{G_f(-b_0+xB)}2,
$$
$$
\begin{aligned}
\mathcal L_2={}&
\frac{x^2\mathsf A_f(C_a)+2x\mathsf B_f(C_a)
-x\mathsf C_f(B)+x^2\mathsf C_f(A)}4\\
&-\frac{\mathsf D_f(\mathbf Y(g,g))}{16}
+\frac{\mathsf E_f(T_g)}{32}
+\frac{\mathsf F_f(E_g)}8,\\
\mathcal L_3={}&\frac{x^2\mathsf B_f(B)}2+\frac{\mathsf E_f(V_g)}4.
\end{aligned}
\tag{9}
$$
对(8)每个原项取 $h^{-2}$，得到以下完整表。

| 式(8)中的来源 | $h^{-2}$ 系数 |
|---|---|
| $G_f$ 第一行 | $k\mathcal T_2$ |
| $-S^2x\,\mathsf A_f(a_g)/(4h^2)$ | $0$ |
| $kS\{x^2\mathsf A_f(a_g)+2x\mathsf B_f(a_g)\}/(4h)$ | $kS\{x^2\mathsf A_f(C_a)+2x\mathsf B_f(C_a)\}/4$ |
| $-Sx\,\mathsf C_f(a_g)/4$ | $-kSx\,\mathsf C_f(B)/4$ |
| $-k^2x^2\,\mathsf B_f(a_g)/2$ | $-k^3x^2\,\mathsf B_f(B)/2$ |
| $khx^2\,\mathsf C_f(a_g)/4$ | $kSx^2\,\mathsf C_f(A)/4$ |
| $S\,\mathsf D_f(q_g)/(8h^3)$ | $-kS\,\mathsf D_f(\mathbf Y(g,g))/16$ |
| $-k\,\mathsf E_f(q_g)/(4h^2)$ | $-k^3\mathsf E_f(V_g)/4+kS\,\mathsf E_f(T_g)/32$ |
| $\mathsf F_f(q_g)/(8h)$ | $kS\,\mathsf F_f(E_g)/8$ |

因此
$$
\boxed{
[h^{-2}]n_\gamma
=k\{\mathcal T_2+S\mathcal L_2-k^2\mathcal L_3\}.
}
\tag{10}
$$
第一行中的 $h b_1$ 项在取系数之前准确相消：
$$
\frac{\partial_hb_g}{2h}-\frac{b_g}{2h^2}
=-\frac{SR_g}{8h^3}-\frac{kb_0}{2h^2}.
$$
所以(10)没有漏掉一个应保留的 $b_1$ 项。

原 $N_0=P_h+F_*(k,\omega)$ 是该密度的实际 $h$ 原函数。$h^{-2}$ 的原函数为 $-h^{-1}$，故
$$
\boxed{
\tau_2=-\mathcal T_2-\mathcal L_2,\qquad
\tau_{2b}=-\mathcal L_2+\mathcal L_3,
}
\tag{11}
$$
由 $S=1+k^2$ 即得(1)。参考常数和 $F_*$ 不依赖 $h$，不能贡献 $h^{-1}$。本式没有把某个对数系数替代这个普通负幂。

式(7)–(11)在 outer 与 inner 仍独立时成立，保全部原尾。因此它们确定响应所需的真实 mixed 算子，不只是 diagonal 或 pure 投影。

## 4. 负四 kk 槽中的四个原响应

R417 已给出
$$
[N_0]_{h^{-4}}=0,\quad
[N_0]_{h^{-3}}=kS^2\tau_3,\quad
[N_0]_{h^{-2}}=S(\tau_0+k^2\tau_1).
\tag{12}
$$
在 $\omega=0$，原物理 $k_s^2$ 矩阵为
$$
m_{2,kk}=\frac{k\mathbf P}{16h^3}-\frac{\mathbf S}{16h^2}.
\tag{13}
$$
只有幂指数 $(-3,-1)$ 和 $(-2,-2)$ 的乘积可贡献 $h^{-4}$。对两个原输入因子的线性性直接给(2)。特别，负六层所需的 $\tau_3$ 不能替代本层新出现的 $h^{-1}$ 系数。

原固定八状态归一化 $\Gamma(m_{2,kk})$ 只有(13)的 $h^{-3},h^{-2}$，故其 $h^{-4}$ 系数准确为零。这是原固定归一化的系数结论，不是一般删除它的许可。

在 $k=0$，仅余
$$
-[h^{-4}]\mathcal B_{m_{2,kk}}N_0
=\frac1{16}\mathcal B_{\mathbf S}\tau_0
\tag{14}
$$
R402 给出其完整 outer：
$$
64\tau_0(f;g^2)=2fF_g'-f'F_g+xJ(f'F_g'').
$$
当 $k\ne0$ 时，除非另证完整身份，(2)的四个响应必须全部保留。特别，R420 的 $W_4$ 自然值为零与 R421 的 $B_{\mathbf P}\tau_3$ 消项，都没有赋予(11)新算子任何 $W$ 成员关系或自然消项。

## 5. 后续完整 kk 计算的准确范围

原完整正规系数为
$$
[h^{-4}]\{\mathscr R_{kk}-Y\mathscr A_k
-\mathcal B_{m_0}N_2-\mathcal B_{m_{2,kk}}N_0-\Gamma(m_{2,kk})\}.
\tag{15}
$$
这里 $Y=\partial_k+(2h)^{-1}\partial_\omega$ 必须先作用，再限制 $\omega=0$。其真实中心导数、$P_s/B_s$ histories、$-\Psi(u,n)$ 及有序 $2+2$ 尾均不因本稿改变。

式(1)(2)固定了(15)此前缺少的完整静态势输入。本稿尚不读取这四个 ambient 自然响应，也尚未完成整个 $k=0$ 自然锚；它给出后续计算的准确有限来源，不删除原势，不把已完成的负六答案移用于负四。

因此当前共同增强商的负四二次速度条件仍须支付。这个系数身份不改变任何已有 profile、有限根构造、period 解、合法窗口或实际目标。
