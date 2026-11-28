# 正确 $\Phi=0,\ f=u,\ u=2$ 的整原值排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：literature_deddens；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 在当前 $D_{\mathrm{val}}\ne0$ 的正确原 $\Phi=0$ 图中，本稿排除整个 $f=u=2$ 支。使用真实均值和已刊自由 $f,t$ 原低 N/P 组合；不重跑任何矩阵、结果式或旧 GB。

## 1. 全原均值迫 $t=4$

$\Phi=0,u=2$ 给
$$
\ell=1,\quad \delta=1-Q,\quad \theta=2-Q,\quad
bc=-\frac Q{4\delta},\quad P_{02}=2Q.
$$
当前 $Q,\delta,t$ 已付；[原 $\theta$ 单位](R150-appendix-unit211-Phi-zero-fu-t-minus-two-and-theta-original-units.md)支付 $Q-2$。所有这些都来自正确原公式，未移入旧半权支。

写 $X=x+\rho y_0,\ Y=x-\rho y_0,\ \rho^2=\delta$。
正确 $R/t$ 和 $E_0$ 给
$$
x=2+\frac t4,\qquad
y_0=\frac12-\frac{t-2}{2(2-Q)}.
$$
由真实 $B/C$ 均值奇部，
$$
\delta E_{\mathrm{Bo}}=1-\frac{(t-2)^2}{4}
=\frac{t(4-t)}4.
$$
故整个原支上 $t=4$，没有只取平方根的某个数值分支。于是
$$
x=3,\qquad y_0=\frac{Q}{2(Q-2)},\qquad
V=3+y_0,\quad W=6-\frac Q2.
\tag{1}
$$

## 2. 原偶均值与 $N_0$ 的准确误差

令
$$
\Psi_2(Q)=Q^3-7Q^2+16Q-16,\qquad h=Q-2.
$$
把 (1) 代回原偶均值得
$$
E_{\mathrm{Be}}=\frac32-\frac Q2-\frac2h-\frac{2\delta}{h^2}
=-\frac{\Psi_2}{2h^2}.
\tag{2}
$$
原 Gram 的
$$
A_1=2u-2V+2bc\,t=-2-\frac Qh-\frac{2Q}{\delta}.
$$
既有正确 $N_0$ 恢复给 $A_1=8/Q-2+4\lambda$，故完整地
$$
\lambda=\frac1\delta-\frac{\Psi_2}{4Q\delta h}.
\tag{3}
$$
(3) 保留 $\Psi_2$ 误差；没有提前把原偶均值替换为零后忘记其来源。

## 3. 完整原低 N/P 组合返回单位

引用[全自由 $f,t$ 的原低加权 N/P 身份](R150-appendix-unit211-unrestricted-f-and-t-original-low-weighted-NP-identities.md)。在 $f=u$ 时，其第二低式为原必要条件
$$
\mathcal L_\lambda=2P_{02}\lambda(2\ell-1)-bc\,tK_\lambda=0,
\tag{4}
$$
其中 $\sigma=p+q=2$，
$$
\begin{aligned}
K_\lambda=2[&t^2+2(3u-S_x-\sigma)t+2XY+3P_x\\
 &+(\sigma-2u)S_x-2W+4u^2-8\sigma u+\sigma^2+\ell Q],
\end{aligned}
$$
$S_x=X+Y,\ P_x=pX+qY$。它是原 N/P、jets 及均值的完整组合，而不是新假设。

在 (1) 上，
$$
S_x=6,\quad P_x=6+\frac{\delta Q}{h},\quad
XY=9-\frac{\delta Q^2}{4h^2},
$$
所以直接得到
$$
K_\lambda=4Q+\frac{\delta Q(5Q-12)}{h^2}.
\tag{5}
$$
使用 (2)–(5)，完整有理恒等式为
$$
\boxed{\quad
\mathcal L_\lambda+4E_{\mathrm{Be}}
=-\frac{2Q^2}{\delta(Q-2)}.
\quad}
\tag{6}
$$
右侧由原已付单位组成，左侧在任何原点为零，矛盾。因此整个 $f=u=2$ 支排除。未使用任何 $D_{\mathrm{val}}$ 范数逆，也没有把 $u=2$ 外推为一般 $\Phi$ 单位。

## 4. 与终端权覆盖的直接合成

[一次 $C_{17}$ 原覆盖](R150-appendix-unit211-Phi-zero-true-fu-terminal-C17-once-original-ideal-cover.md)的平方自由部分次数 $16$，其中 $u-2$ 是一个真实因子；$C_{17}$ 中它的重数为二。本稿关闭的是它的**整个原几何纤维**，所以所有重数不会留下任何复原点。

剩余权支持为
$$
(2u-1)(2u^2-4u+1)(2u^3-8u^2+12u-7)F_9(u)=0.
$$
因此不同 $u$ 至多 $15$，首一 $\Psi(Q)$ 给不同权对至多 $45$。再合[全 $f=u$ 中心首一二次](R150-appendix-unit211-Phi-zero-true-fu-centered-v-monic-quadratic-and-two-mean-source.md)，不同 $(u,Q,\lambda,T,t)$ 至多 $90$，有序 Gram 至多 $180$，完整固定规范不同点至多 $360$。其余四因子的完整原纤维保留；不宣称整个 $f=u$ 已闭。

## 5. 小源与实际记录

新源为
[2026-11-28-unit211-Phi-zero-true-fu-u-two-original-low-unit-8542.js](../notes/2026-11-28-unit211-Phi-zero-true-fu-u-two-original-low-unit-8542.js)。

源 SHA256：`06d4601d821897a7ec680cb742a0fa0cd7ef1f3c9ecf25dfdf0bb5e4eb45a6cf`；3172 字节。首次 V8 BigInt 实际 1 毫秒，250 次整数多项式乘法，四个完整有理恒等式返回：(2)、(3)、(5)、(6)。所有有理等式都以分子交叉乘回为零验证，无浮点或取样。

这里新执行的是四个小恒等式；原均值、$N_0$ 和低 N/P 的来源由上述已刊完整原身份连接，没有重放旧完整 Gram、矩阵或结果式。
