# 固定物理测试族在同一宽负前缀和联合两费余商中的运输

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220。

这是已发表原构造的一条技术应用，不另计主要结果。它把同一个有限维物理测试族与实际缺陷源放进**同一个窗口、同一个线性修正和同一个闭余空间**。测试族的原左误差趋零，测试修正的完整右费虽然可增长，但与实际源的原 flat 费配对仍趋零。剩余余商中的主左配对没有被支付。

依赖：[真实固定测试端点](2026-11-14-fixed-test-endpoint-truncation-and-small-two-fee-source-kernel-2220.md)、[固定测试共同窗口](../results/R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md)、[原完整加平坦修正](../results/R271-appendix-full-plus-flat-negative-prefix-repair-and-complete-top-cost.md)、[宽负前缀及有效预算](../results/R271-appendix-wide-negative-source-prefix-and-exponential-effective-window-budget.md)。

## 1. 原窗口、固定测试族和同源费用

保留原 $m,d=2^m,A_m,D_m,b$，源空间为 $\mathscr R_b$。记
$$
U_b=E_b^\dagger,\qquad
L=(E_bE_b^*)^{-1},\quad B=J_{\rm bare}^{-1},\quad G=J_{\rm right},
$$
$$
\mu(x)^2=\langle Lx,x\rangle,\quad
\alpha(x)^2=\langle Bx,x\rangle,\quad
\lambda(x)^2=\langle G^{-1}x,x\rangle,
$$
$$
\lambda_{\rm flat}(x)^2=\langle LGLx,x\rangle,\qquad
\Xi(x)^2=\langle M_2x,x\rangle,\quad M_2=B+LGL.
\tag{1.1}
$$
全部费用取同一个原源，不交换 $B,L,G$。

取固定物理测试空间 $T_n$，$n$ 固定且 $m$ 足够大。原共同窗口选择同时给实际源 $r$、固定缺陷 $w\ne0$ 和每个 $f\in T_n$：
$$
\|Y_r\|^2\le2\varepsilon^2/K,\qquad
\Xi(r)^2\le4\varepsilon^2/K,\qquad
\|U_br-w\|\le\varepsilon,\quad \varepsilon\to0,
\tag{1.2}
$$
以及真正测试源 $t_b(f)$、其端点截断源 $s_b(f)$ 和真正未来带 $Y_f$：
$$
\mu(t_b(f)-s_b(f))^2+\|Y_f\|^2
=\Delta_b(f)\le\frac{4n}{K}\|f\|^2,
$$
$$
\Xi(s_b(f))^2\le2\|Y_f\|^2.
\tag{1.3}
$$
$t_b,s_b,Y_f$ 都对 $f$ 线性。这里使用端点的真正左最小者 $q_{b+d}-k_{b+d}$；不能改成 $q_{b+d}-k_b$。对两种真实来源，完整加平坦修正所用的同未来恒等式都成立。下文不为修正后的新源沿用旧未来向量。

记 $P_b$ 为原左最小者像空间上的物理正交投影。固定测试定义给
$$
U_bt_b(f)=P_bf,\qquad
\langle Lx,t_b(f)\rangle=\langle U_bx,f\rangle
\quad(x\in\mathscr R_b).
\tag{1.4}
$$
因此 $\|U_bt_b:T_n\to\mathcal H\|\le1$。本文不需要对随 $m,b$ 变化的 $P_b$ 另作统一谱断言。

## 2. 完全相同的三个线性修正

沿宽前缀定理取
$$
h=2^{\lfloor3m/4-3\rfloor},\quad H=2h,\quad
C_-=8e^{20h^4},\quad C_+=8e^{20H^4}.
$$
置 $\delta=\sqrt{C_-^2-1}$、$\vartheta=\delta(\sqrt{1+\delta^2}+\delta)$、
$c=\sqrt2+\vartheta$，并记
$$
k=K_{\rm eff}=K/c^2\ge\frac{e^{59d^3/256}}{2^{19}d}.
\tag{2.1}
$$
$k$ 是真实费用预算，不是重新计算的窗口数。

第一步使用原 $G^{-1}+LGL$ 最小修正算子 $P_0$，它是原稿明确给出的线性算子；其余源位于
$$
\mathscr D_h=\{x:\langle(L+B)x,z\rangle=0
\text{ 对全部 }z\in\mathscr R_b\cap\ker A^h\}.
$$
第二步 $P_H$ 是 $M_2$ 下到
$Z_H=\mathscr D_h\cap\ker A^H$ 的真正正交投影，作用于 $\mathscr D_h$。记
$$
\mathscr D_1=\mathscr D_h\cap Z_H^{\perp_{M_2}}.
$$

为同一有限测试族保留足够预算，将原尾参数仅作如下下限处理：
$$
\rho=\varepsilon/\|w\|,\qquad
\widehat\rho=\max\{\rho,k^{-1/4}\}.
\tag{2.2}
$$
充分大 $m$ 时 $0<\widehat\rho<1$，且 $\widehat\rho\to0$。严格使用宽前缀稿的相同 triplet 和角谱构造，把其中 $\rho$ 替换为 $\widehat\rho$：
$$
\sigma=\min\{\widehat\rho^{-1/2},(d/m^2)^{1/4}\},\quad
R=\left\lfloor\frac{\sigma m\sqrt k}{128}\right\rfloor,
$$
$$
\tau=\max\{\widehat\rho/k,k^{-2}\}.
\tag{2.3}
$$
两旗都先与同一个 $\mathscr D_1$ 相交，再取原 $M_2$ 正交投影
$P_{\rm tr},P_{\rm ang}$。令
$$
\mathsf T=(P_{\rm tr}+P_{\rm ang})/2,\qquad
P_1=1_{[\sqrt{\widehat\rho},1]}(\mathsf T).
$$
这里谱与正交性均在 $M_2$ 内。最终单一线性算子为
$$
\boxed{\mathcal Q=(I-P_1)(I-P_H)(I-P_0).}
\tag{2.4}
$$
它固定后，**同时**作用于 $r$ 和所有 $s_b(f)$。不存在按不同 $f$ 另选窗口、闭交或投影的问题。

(2.3) 的全部原参数仍合法：$R\ge2d$、$R\le b/2$ 最终成立，且原短列参数
$$
\theta\le\frac{90\sigma^2m^2}{16384d}
\le\frac{90m}{16384\sqrt d}\longrightarrow0.
$$
两条真实范围上的完整/裸比较常数都不超过
$$
C_*=\sqrt{k/\widehat\rho}.
\tag{2.5}
$$
这只减小原参数 $\sigma$ 的允许值，没有增加所需的尾收敛速率。

## 3. 可重复用于整个测试族的齐次估计

若一个真实来源 $x$ 的同未来带满足
$$
\|Y_x\|^2\le2\eta^2/K,\qquad \Xi(x)^2\le4\eta^2/K,
\tag{3.1}
$$
则前两步原估计逐字给出
$$
\mu(P_0x+P_H(I-P_0)x)\le a'_m\eta,\qquad
\lambda(P_0x+P_H(I-P_0)x)\le b'_m\eta,
$$
$$
a'_m=4096\sqrt d\,e^{-39d^3/512},\qquad
b'_m=16384\sqrt d\,e^{-19d^3/512},
\tag{3.2}
$$
以及 $x^1=(I-P_H)(I-P_0)x$ 满足 $\Xi(x^1)^2\le2\eta^2/k$。

联合投影的已付费用与 (2.5) 给
$$
\mu(P_1x^1)^2
\le\frac{C_*}{2\sqrt{\widehat\rho}}\Xi(x^1)^2
\le\frac{\eta^2}{\widehat\rho\sqrt k},
$$
$$
\lambda(P_1x^1)^2
\le\frac{C_*^2}{\sqrt{\widehat\rho}}\Xi(x^1)^2
\le\frac{2\eta^2}{\widehat\rho^{3/2}}.
\tag{3.3}
$$
因此
$$
\boxed{
\begin{aligned}
\mu(x-\mathcal Qx)&\le
\eta\bigl(a'_m+\widehat\rho^{-1/2}k^{-1/4}\bigr),\\
\lambda(x-\mathcal Qx)&\le
\eta\bigl(b'_m+\sqrt2\,\widehat\rho^{-3/4}\bigr),\\
\Xi(\mathcal Qx)^2&\le2\eta^2/k.
\end{aligned}}
\tag{3.4}
$$
两费 Pythagoras 仍只从 $(I-P_0)x$ 开始；没有把第一步当成 $M_2$ 正交投影。

## 4. 实际源的已付结论全部保留

令 $\widehat r=\mathcal Qr$。在 (3.4) 中取 $\eta=\varepsilon$，由 $\widehat\rho\ge\rho$ 得
$$
\mu(r-\widehat r)
\le a'_m\varepsilon+\|w\|\sqrt\rho\,k^{-1/4}\to0,
$$
$$
\lambda(r-\widehat r)
\le b'_m\varepsilon+\sqrt2\|w\|\rho^{1/4}\to0.
\tag{4.1}
$$
所以 $U_b\widehat r\to w$，原完整顶部最小链差也趋零。全部低层仍由同一个最终左最小者重建；其来源和反馈差由第一式支付。

最终 $\widehat r\in\mathscr D_1$，并有
$$
\Xi(\widehat r)^2\le2\varepsilon^2/k,\qquad
\frac{\|P_{\rm tr}\widehat r\|_{M_2}^2+
\|P_{\rm ang}\widehat r\|_{M_2}^2}{2}
\le\sqrt{\widehat\rho}\,\Xi(\widehat r)^2.
\tag{4.2}
$$
这保留整个 $h$ 负前缀与精确 $H=2h$ 头交测试。

## 5. 整个固定测试族同时进入相同余空间

定义线性测试源算子
$$
\widehat S_bf=\mathcal Qs_b(f),\qquad f\in T_n.
$$
对 (1.3) 可统一在 (3.1) 取 $\eta=\sqrt{2n}\|f\|$。因为
$\widehat\rho\ge k^{-1/4}$，(3.4) 给
$$
\mu(s_b(f)-\widehat S_bf)
\le\sqrt{2n}(a'_m+k^{-1/8})\|f\|,
$$
$$
\lambda(s_b(f)-\widehat S_bf)
\le\bigl(\sqrt{2n}\,b'_m+2\sqrt n\,k^{3/16}\bigr)\|f\|.
\tag{5.1}
$$
第二式允许增长，并非 $\lambda(\widehat S_bf)$ 的上界。

由 (1.3) 及第一式，
$$
\boxed{
\|U_b\widehat S_b-P_b|_{T_n}\|
\le\sqrt n\,\gamma_m\longrightarrow0,
}
$$
$$
\gamma_m=\frac2{\sqrt K}+\sqrt2\,a'_m+\sqrt2\,k^{-1/8}.
\tag{5.2}
$$
这是整个有限维测试族的算子范数界，不是每个 $f$ 各取一个子序列。相应左 Gram 满足
$$
\|\widehat S_b^*L\widehat S_b
-\iota_n^*P_b\iota_n\|
\le2\sqrt n\,\gamma_m+n\gamma_m^2,
\tag{5.3}
$$
其中 $\iota_n:T_n\hookrightarrow\mathcal H$ 为物理包含。

同源两费有
$$
\boxed{\widehat S_b^*M_2\widehat S_b\preceq\frac{4n}{k}I_{T_n}.}
\tag{5.4}
$$
每个 $\widehat S_bf$ 都属于与 $\widehat r$ 相同的 $\mathscr D_1$，并满足同一相对两旗条件
$$
\frac{\|P_{\rm tr}\widehat S_bf\|_{M_2}^2+
\|P_{\rm ang}\widehat S_bf\|_{M_2}^2}{2}
\le\sqrt{\widehat\rho}\,\Xi(\widehat S_bf)^2.
\tag{5.5}
$$
这里的余条件是真实度量条件；没有将物理坐标、斜条带或整段来源设为零。

## 6. 原配对的完整保留及尚未支付的主项

由 (1.4)、(5.2)，
$$
\bigl|\langle L\widehat r,\widehat S_bf\rangle
-\langle U_b\widehat r,f\rangle\bigr|
\le\mu(\widehat r)\sqrt n\,\gamma_m\|f\|\to0.
\tag{6.1}
$$
因此对所有固定 $f\in T_n$，
$$
\boxed{\langle L\widehat r,\widehat S_bf\rangle
\longrightarrow\langle w,f\rangle.}
\tag{6.2}
$$
有限维上该收敛也是一致的。它不要求先识别 $P_b$ 的极限。

还能直接用原 flat 费支付测试修正的完整右费增长：
$$
|\langle L\widehat r,s_b(f)-\widehat S_bf\rangle|
\le\lambda_{\rm flat}(\widehat r)
\,\lambda(s_b(f)-\widehat S_bf)
$$
$$
\le\left(
2\sqrt n\,\varepsilon b'_m k^{-1/2}
+2\sqrt{2n}\,\varepsilon k^{-5/16}
\right)\|f\|\longrightarrow0.
\tag{6.3}
$$
这一步用同一个 $G$ 的真实 Cauchy 配对，不把 $\lambda_{\rm flat}$ 换成 $\mu$ 或另一最小逆。

到此，两族源都具有原 $k^{-1}$ 两费预算，处于相同宽负图、相同大头交余空间及相同联合谱余空间；其主左配对仍保留固定非零缺陷的所有有限物理测试值。**两费小本身仍不足以令 (6.2) 的左侧趋零。** 所缺正是这个受约束同源主配对、等价局部双链 Gram 或另一条真实右费用估计。本文没有从已付删除推断它为零，也没有支付全部 pure 高深段或无权 $N=M$。
