# 正确 $\Phi=0,\ f=u$ 图的中心二次、真实新单位与两均值来源

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：literature_deddens；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 本稿只处理当前 $D_{\mathrm{val}}\ne0$ 的原 $\Phi=0,\ f=u$ 图。所有均值使用真实双点乘法；不使用已撤回的旧紧凑 $R_{\mathrm{bar}}$。它给出全图的一个首一二次环境及 $\Psi$ 的两个原均值来源，不宣称整个 $f=u$ 已空。

## 1. 已付范围和坐标

沿用[正确单 $y$ 原图](R150-appendix-unit211-Phi-zero-true-fu-single-y-common-weight-curve.md)和[原 $t-2,\theta$ 单位](R150-appendix-unit211-Phi-zero-fu-t-minus-two-and-theta-original-units.md)。写

$$
s=u-1,\quad h=2u-3,\quad \delta=1-Q,\quad
L=Q-2(u-1)(u-2),\quad K=Q+4(u-1),
$$

$$
\ell=L/Q,\quad a=1-\ell,\quad m=u-\ell,\quad
\theta=u-L=u-\ell Q,\quad
M_n=2uL-L^2-u^2Q.
$$

当前图已付 $Q,\delta,s,h,L,K,M_n,t,\theta$。其中 $h$ 仅由整个 $f=u,u=3/2$ 原支排除支付，$\theta$ 由前篇的原均值恒等式支付；没有把这些单位移给一般 $\Phi$ 图。

设

$$
\rho^2=\delta,\quad p=1+\rho,\quad q=1-\rho,\quad
b=\frac{\ell+m/\rho}{2},\quad c=\frac{\ell-m/\rho}{2},
$$

$$
X=x+\rho y_0,\quad Y=x-\rho y_0,\quad
V=bX+cY,\quad v=t-2,\quad \xi=y_0-\frac12.
$$

正确 $R$ 在 $f=u$ 时为 $bcQ^2t(t+4u-4x)$，故

$$
x=u+\frac t4,\qquad E_0=0\Longrightarrow
4\theta\xi+uv=0.
\tag{1}
$$

所以 $\xi=-uv/(4\theta)$。这里没有除 $u$ 或 $m$。

## 2. 两个真正原均值的完整中心式

记 $E_{\mathrm{Be}}=(E_B+E_C)/2$、
$E_{\mathrm{Bo}}=(E_B-E_C)/(2\rho)$。在原 $f=u$ 坐标中，真实 $B$ 均值为

$$
E_B=-ap^2+(2p+2u)X-2p d_1
+ct(t+2u-2p-2Y)-2X^2,
\qquad d_1=(1+\ell)u-V.
\tag{2}
$$

$E_C$ 为 $\rho\mapsto-\rho$ 的同一式。这正是前篇由真实 Gram 给出的原式，不是错误 $d_1^2$ 紧凑化。

将 $x=u+(v+2)/4,\ y_0=1/2+\xi$ 直接代入 (2)，分别取偶部和奇部，得到

$$
E_{\mathrm{Be}}
=s-L+\frac Q2+\frac{2\ell-1}{8}v^2
-mv\xi-2\delta\xi^2,
\tag{3}
$$

$$
\delta E_{\mathrm{Bo}}
=sh-a\delta v\xi-\frac m4v^2.
\tag{4}
$$

例如 (4) 的常数是
$m-a\delta=s+Q-L=s(2u-3)$；(3) 中所有单独的 $v$、$\xi$ 一次项都相消。这两式保留原均值的完整归一。

定义新的纯权多项式

$$
H_f=Q^2-(4u^2-11u+8)Q-4(u-1)(u-2)^2
\tag{5}
$$

以及

$$
P_n=(2L-Q)\theta^2+2(uQ-L)u\theta-\delta u^2Q,
\qquad C_2=2s-2L+Q.
\tag{6}
$$

把 (1) 代回 (3)–(4)，完整得到

$$
4Q\theta\delta E_{\mathrm{Bo}}
=s\bigl(H_fv^2+4Q\theta h\bigr),
\tag{7}
$$

$$
8Q\theta^2 E_{\mathrm{Be}}
=4Q\theta^2C_2+P_nv^2.
\tag{8}
$$

(7) 所用的纯权身份为

$$
(Q-L)\delta u-(uQ-L)\theta=sH_f.
\tag{9}
$$

## 3. 整个 $f=u$ 的真实新单位与首一二次

原点处 $E_{\mathrm{Bo}}=0$，由 (7)

$$
H_fv^2=-4Q\theta h.
\tag{10}
$$

右边是已付单位，故 **$H_f$ 在整个当前 $f=u$ 图上都是单位**；不是只在任取补图上倒置它。其原同点逆可直接写为

$$
H_f^{-1}=-\frac{v^2}{4Q\theta h}.
$$

因此原图位于必要的首一二次环境

$$
\boxed{\quad v^2+\frac{4Q\theta h}{H_f}=0.\quad}
\tag{11}
$$

没有以模非零判单位，也没有倒 $D_{\mathrm{val}}$ 的范数。$H_f=0$ 整权面已由 (7) 的原单位右边排除，全部复权嵌入均包含。

对任一固定剩余 $(u,Q)$，(11) 的必要代数长度为二。真实值与 Gram 坐标由同一个 $v$ 恢复。为避免把本稿的 $\xi,y_0$ 与前篇单坐标混淆，令

$$
Y_f=4s^2-Q+2L\lambda
=\frac{M_nh(v+2)/(2\delta)-L(4s^2-Q)}{2\theta}.
$$

则

$$
t=v+2,\quad
\lambda=\frac{Y_f-(4s^2-Q)}{2L},\quad
T=-\frac LQ-\frac{KY_f}{2QL},\quad
A_1=\frac{2sY_f}{Q},
$$

并由 (1) 恢复 $x,y_0$。所有分母均为当前图已付权单位。因此每个固定权对至多有两个不同的 $(\lambda,T,t,x,y_0)$；不是从有理函数域维数外推特殊权纤维。

## 4. $\Psi$ 已有两个原均值来源

前篇的首一 $Q$ 三次为

$$
\begin{aligned}
\Psi={}&Q^3+(-10u^2+24u-15)Q^2\\
&+(32u^4-152u^3+276u^2-228u+72)Q\\
&-32u^6+224u^5-672u^4+1104u^3
-1040u^2+528u-112.
\end{aligned}
$$

新的小纯权恒等式为

$$
\theta C_2H_f-hP_n=Q\Psi.
\tag{12}
$$

用 (7)–(8) 消去 $v^2$，便得到完整原来源

$$
\boxed{\quad
Q\Psi=2\theta H_fE_{\mathrm{Be}}
-\frac{\delta P_n}{s}E_{\mathrm{Bo}}.
\quad}
\tag{13}
$$

故 $\Psi$ 本身在两个真实均值的理想中；只除既有 $Q,s$。这里没有再计算旧三个 cofactor，也没有使用泛型矩阵逆。

附带的小整数多项式源实际在 V8 返回 (9) 及 (12) 的完整短除身份，2 毫秒；(12) 对 $\Psi$ 的商恰为 $Q$、余式为零。原 Gram 已刊来源通过 (2)–(4) 的纸面展开使用，**没有把此次两变量整数检查写成新的完整 Gram 运行**。

## 5. 已成有限权覆盖的同点后果

[原同点 $C_{92}$ 覆盖](R150-appendix-unit211-Phi-zero-true-fu-C92-same-point-original-weight-cover.md)与独立零基点 mean 排除给出至多 $261$ 个不同 $(u,Q)$ 权对。结合 (11)，得到至多 $522$ 个不同 $(u,Q,\lambda,T,t)$ 点；$x,y_0,A_1$ 随之唯一恢复。

再保留首一 $\rho^2=1-Q$，全部有序 Gram 坐标至多 $1044$ 点。若把规范值的两 simple 坐标也列入，写 $\alpha=h_U-1,\ \beta=k_U-1$；它们满足

$$
b\alpha+c\beta=T,\qquad
b\alpha^2+c\beta^2=A_2,\qquad A_2=2\lambda^2-2\lambda+1.
$$

消去 $\beta$ 得首项已付的

$$
b\ell\alpha^2-2bT\alpha+T^2-cA_2=0.
$$

所以最多再有两个值选择，完整固定规范点数不超过 $2088$；第三矩及个别原值只会进一步缩小集合。这些均是**不同点数上界**，没有把旧权覆盖多项式的次数提升为整体 scheme 长度，也不宣称这些点存在。

## 6. 可读源与实际回执

新整数检查源：
[2026-11-28-unit211-Phi-zero-true-fu-centered-v-two-mean-identities-8542.js](../notes/2026-11-28-unit211-Phi-zero-true-fu-centered-v-two-mean-identities-8542.js)。

其 SHA256 为 `8bc3edd8864ec35dde3b9017890419ea231832b89595fd5414b7151a4836cda2`。小回执另存同 stem 的 `-execution.json`。源只做两变量整数恒等式；首一环境与计数由上述完整原推导给出。不增加任何旧源复现门。
