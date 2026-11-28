# R150：正确 Phi 的整 alpha 零图、首一 V 二次与三个原权条件

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**已证明。** 当前修正后的 $\Phi=0,\ D_{\rm val}\ne0$ 原图中，整个

$$
\alpha=4(1-Q)(f-u)-(u-\ell Q)t=0
$$

支具有完整纯权恢复 $f,t$，同一个原变量 $V=bX+cY$ 满足全支首一二次。原 $E_{Be},N_1,N_S,P_S$ 已全部返回同一二列环境，并得到三个非零原必要权多项式，双次数分别为 $(17,8),(24,11),(25,11)$。

**本篇没有排空整个 $\alpha=0$ 支，也没有据这三式宣称其共同权点有限。** 全部尚未处理的共同零纤维保留。

## 1. 仅在本支支付的分母

记

$$
s=u-1,\quad\delta=1-Q,\quad
L=Q-2s(u-2),\quad K=Q+4s,\quad\ell=L/Q,
$$

$$
m=u-\ell,\quad\theta=u-\ell Q,\quad
M_n=2uL-L^2-u^2Q,\quad M=M_n/Q=4bc\delta,
$$

$$
T_0=-K,\quad J=2u(1-u)+L,\quad P_{02}=2sL,\quad A=4s^2-Q.
$$

当前原单位包含 $uQ\delta sKLM_n$。另由纠正后的 [整 t 零](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)、[整 f=u](R150-appendix-unit211-Phi-zero-true-entire-fu-original-exclusion.md)和 [整 A 零](R150-appendix-unit211-Phi-zero-true-Azero-second-linear-and-whole-curve-exclusion.md)排除，可用 $t(f-u)A\ne0$。

令 $\eta=f-u$，并取已刊 [自由原身份](R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md)施加 W 权关系之前的部分。其

$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q=-sA
$$

是本 Phi 图的已付单位。正确原 $R$ 满足

$$
\theta\frac{4\delta R}{Q^2}
=\alpha\{4\theta(V-f)-Mt\}
 -2tR_w(2m\eta+\ell\theta).
\tag{1}
$$

在 $\alpha=R=0$ 上，由 $tR_w\ne0$，得到
$2m\eta+\ell\theta=0$。准确组合

$$
t(2m\eta+\ell\theta)+\ell\alpha
=2\eta(mt+2\ell\delta)
$$

再由 $\eta\ne0$ 给 $mt=-2\ell\delta$。故 m 在整个本支非零；再由 $\alpha=0$ 给 $\theta t=4\delta\eta$，所以 $\theta$ 也非零。

因此完整恢复

$$
t=-\frac{2\ell\delta}{m},\qquad
f=u-\frac{\ell\theta}{2m}.
\tag{2}
$$

这次实际源无需一般等权定理或 W 专属单位；$m,\theta$ 都由上述本支原身份支付，而没有先删去它们的零面。

## 2. 同一个原 V 与真正均值首一二次

令

$$
W_1=(T_0+4uf)/2,\quad
x=\frac{\theta V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},
$$

$$
A_1=2f-2V+2bct,\quad
\lambda=\frac{Jf+bcQt-QV-sT_0}{P_{02}},\quad
T=\frac{T_0A_1}{2P_{02}}-\ell,\quad w=\lambda-1-T.
\tag{3}
$$

恢复 $\rho^2=\delta$、$p=1+\rho,q=1-\rho$、
$b=(\ell+m/\rho)/2,c=(\ell-m/\rho)/2$、
$X=x+\rho y,Y=x-\rho y$。原四行仍是

$$
(0,0,p,q),\quad(0,A_1,X-(1-\ell)p-ct,Y-(1-\ell)q-bt),
$$

$$
(p,X-(1-\ell)p-ct,0,t),\qquad
(q,Y-(1-\ell)q-bt,t,0).
$$

实际源使用完整双点乘法，尤其
$\operatorname{vm}(d,d)_1=2d_0d_1$；全部原均值和原 N/P 从这四行重建。$E_0=0$、正确 $R=0$ 和 $E_1=bE_B+cE_C$ 均实际返回。

写 $E_B=E_{Be}+\rho E_{Bo}$。真正原奇均值的 V 二次头是

$$
[V^2]E_{Bo}=\frac{4u\theta}{M^2}.
\tag{4}
$$

(4) 的每个因子均已支付。所以

$$
q_V=\frac{E_{Bo}}{4u\theta/M^2}=V^2+q_1V+q_0
\tag{5}
$$

在整个本支首一，系数只有原已付的纯权分母。二次的两个复根和重复根全保留，不选择特定值嵌入。

## 3. 完整 N/P 同 V 返回

在首一 (5) 的真实多项式商内，源每次乘法都按 (5) 约化并返回原差式。令

$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1.
$$

保留的四条原值是

$$
r_0=E_{Be},
$$

$$
r_1=N_4(k_0+k_1)-N_4(k_0)-N_4(k_1)-4\lambda wP_{02},
$$

$$
r_2=bN_4(k_B)+cN_4(k_C)
 -2\lambda P_{02}(\ell+2T+A_\lambda),
$$

$$
r_3=bP_2(k_B)+cP_2(k_C)
 -P_{02}(\ell+3T+3A_\lambda+B_\lambda).
$$

它们准确写作 $r_i=a_i+b_iV$，全部奇 $\rho$ 系数为零；没有以某个范数替换个别原值。系数分母均在

$$
uQ\delta sKLM_nA(uQ-L)\theta
$$

的原单位支撑内。对每个固定允许权点，尚未取物理开集的必要 V 环境长度为 2；其进一步原条件及开集不增加点数。

## 4. 三个新纯权原必要式

对 $j=1,2,3$，实际取

$$
b_jr_0-b_0r_j=b_ja_0-b_0a_j.
\tag{6}
$$

源码清两个真实乘子的已付权分母，取它们的共同多项式因子，除后重新返回全二坐标。此次三个共同因子都准确为 1。故 (6) 不倒置 $b_0,b_j$，它们同时为零的整支也被保留。

只剥最终标量的已付权因子并规范化非零有理常数，得到：

| 原行对 | 必要多项式 | $(\deg_u,\deg_Q)$ | 总次数 | 项数 |
|---|---|---:|---:|---:|
| EBe、N1 | $C_N$ | $(17,8)$ | 17 | 89 |
| EBe、NS | $C_S$ | $(24,11)$ | 24 | 177 |
| EBe、PS | $C_P$ | $(25,11)$ | 25 | 180 |

原点必使三式同时为零。其规范多项式字典 SHA256 分别为：

- $C_N$：`9da720bb18618e80ba9db96559e73dd25c9e4600a8e1576e6e8f046d36e61ad1`；
- $C_S$：`80c26662a4c2cbde3cb5e55976061cb117ea9a8ad7d9954c50a2b5e22b95ae83`；
- $C_P$：`c04b14a34183209fa97fc6c34f6b503afedbc212c29bbdcc98a0c9b517c5338f`。

这些式子均非恒定，本篇没有计算其完整共同权支持或排除它。后续需新的同点原条件或精确消元，不能只凭三条必要式宣称整个支已闭。

## 5. 唯一实际执行

自含源：[整 alpha 零原返回](../notes/2026-11-28-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-8542.py)，blob `22a90daf4fbd8fe1a8cd8ff451ba345807d7f060`；SHA256：

`58cab31654894e8b4a4309f1c6b69619f5ee19591f74256f3128dd2026a4f025`。

run **46125221539**，job **140918228878**。源提交 `073343139eafcf8ba9c21b1b8de8b694d6d9ded6`；真实 pull 在 2026-11-28 08:19:06.753985 UTC 到 `7b4754c18af63dd4b5dcf3113081e8964dc273c3`，两 README 无变。

数学末阶段 0.388256590 秒，驱动 0.456230013 秒，RSS 39744 KiB，exit 0。限 120 秒/1 GiB、外驱动 135 秒。原值阶段已有 5224 个乘法系数返回，末计 2618 次商乘法和 45 次真权整除。stdout 9411 字节，SHA256：

`1d891c409fabb47085d4e37d52513c93c266d3d58591e18cac20cd63de4ba9c8`。

[小回执](../notes/2026-11-28-unit211-Phi-zero-whole-alpha-zero-monic-V-two-execution-8542.json)记录阶段和哈希，不复制可重算系数载荷。本结果不使用已撤回的紧凑均值链，也未重放旧 B 或 Phi 大门。
