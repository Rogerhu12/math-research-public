# 新输入：中心 v 下四个完整 QQ 原权纤维

日期：2026-11-28（Asia/Taipei）。尚未执行；源 SHA256 `1f88fcd42c37dd94c5477e6acdaad4eee091055ef36c1001f22bf442e4b2944a`。总 120 秒、1 GiB，自含零文件依赖，python-flint 0.9.0。每个完整因子实际返回后立即打印小回执；不保存可重算系数缓存。

## 1. 真正剩余输入

[一次 C17 定理](../results/R150-appendix-unit211-Phi-zero-true-fu-terminal-C17-once-original-ideal-cover.md)的五个因子中，[整个 u=2 原 Low 单位排除](../results/R150-appendix-unit211-Phi-zero-true-fu-entire-u-two-original-low-unit-exclusion.md)已经关闭 u−2。此次只取真正剩余四个 QQ 不可约因子

$$
\begin{gathered}
2u-1,\qquad 2u^2-4u+1,\qquad 2u^3-8u^2+12u-7,\\
32u^9-320u^8+1440u^7-3848u^6+6870u^5-8886u^4\\
\hfill +8828u^3-6650u^2+3296u-763.
\end{gathered}
$$

不再再生十八列、C17 终端、旧 GB 或 cofactor。四个因子的不可约性/完整来源已由 C17 实际 QQ 因式证书支付，不重跑因式门。

## 2. 真原单首一二次与完整权代数

使用[中心二次定理](../results/R150-appendix-unit211-Phi-zero-true-fu-centered-v-monic-quadratic-and-two-mean-source.md)。记

$$
s=u-1,\ h=2u-3,\ \delta=1-Q,\ L=Q-2s(u-2),\ K=Q+4s,
$$

$$
\theta=u-L,\quad M_n=2uL-L^2-u^2Q,\quad
H_f=Q^2-(4u^2-11u+8)Q-4s(u-2)^2.
$$

整个当前原图已经支付 $Q,\delta,L,K,M_n,\theta,H_f,s,h,u$。新的 Hf 单位来自完整原 odd mean 的单位右边，不是泛型假设。

对每个因子 phi，以完整
$$
K_\phi=\mathbb Q[u]/(\phi)
$$
运算；每次逆都在全部系数中作真 xgcd 并乘回，不选一个复根。

先将已成首一 Q 三次 Psi 放入 $K_\phi[Q]$。针对上述各个已付 Q 权因子，只按实际 QQ gcd 切去它们的零分量。每步验证 gcd 同时整除 Psi 的当前商和那条原 paid 多项式，并完整返回
$$
\Psi=g_{\rm good}g_{\rm removed}.
$$
反复切除保留各个零分量的全部重数；每个 removed 因子在原点都是单位，所以不会删掉任何原点。其余 Q 分量及所有幂零都保留。

随后只在整个
$$
A_\phi=K_\phi[Q]/(g_{\rm good})
$$
中对具名已付权因子取实际真逆。若遇非单位，保留整个当前因子并记录，不换素数、不作数值选择。

由真实 odd mean，
$$
v^2=-4Q\theta h/H_f,\qquad v=t-2.
$$
所以整几何必要代数为
$$
B_\phi=A_\phi[v]/(v^2+4Q\theta h/H_f).
$$
若 $d=\deg\phi,n=\deg_Q g_{\rm good}$，它是完整 $2dn$ 维 QQ 代数。最大为 $54$；不取平方自由部分，全部 Q/v 重数保留。

## 3. 同一个真实 Gram 的新原值

在这个整代数中恢复

$$
t=v+2,\quad x=u+t/4,\quad y_0=1/2-uv/(4\theta),
$$

$$
Y_f=\frac{M_nh\,t/(2\delta)-L(4s^2-Q)}{2\theta},\quad
\lambda=\frac{Y_f-(4s^2-Q)}{2L},\quad
T=-L/Q-KY_f/(2QL),\quad A_1=2sY_f/Q.
$$

在内部保留 $\rho^2=\delta$ 的完整二坐标，

$$
b=(\ell+(u-\ell)\rho/\delta)/2,\quad c=\bar b,\quad
X=x+\rho y_0,\quad Y=\bar X,
$$

$$
r=X-(1-\ell)p-ct,\quad s_1=\bar r,\quad p=1+\rho,\ q=1-\rho.
$$

直接建立真实四行 Gram，使用 double-germ 乘法
$(ab)_1=a_0b_1+a_1b_0$。新值是原完整

$$
N_1=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)-4\lambda wP_{02},
$$

$$
NS=bN_4(g_B)+cN_4(g_C)
-2\lambda P_{02}(\ell+2T+A_\lambda),
$$

$$
PS=bP_2(g_B)+cP_2(g_C)
-P_{02}(\ell+3T+3A_\lambda+B_\lambda).
$$

每条的 rho 奇坐标必须实际为零。没有将部分 N4 分量冒充完整原值，也没有扩展任何旧原归约器的分母白名单。v 的每次乘法都在已付首一二次中约化；不是先巨大展开。

## 4. 完整原理想与正单位目标

三条新原行各乘 $B_\phi$ 的完整 QQ 基，得到 $2dn\times6dn$ 原理想矩阵。rref 只选实际原列；所选方阵逆必须双向返回，并将所有原列在全部 $2dn$ 坐标中返回。

依次尝试真正的正目标
$$
1,\quad U,\quad U^2,\ldots,U^{2dn},
\qquad U=\lambda tD_{\rm val},
$$
$$
D_{\rm val}=\ell(2\lambda^2-2\lambda+1)-T^2
=bc(h_U-k_U)^2.
$$

只有目标在全部原坐标中实际返回，才排该完整因子。$\lambda,t,D_{\rm val}$ 在当前原图为单位；程序只乘它们，不倒它们或其范数。

这里 lambda/t/D 本来未被写进权逆清单，因此原 QQ 商可以仍有非零维数及幂零。原目标返回才是排除依据，不能以 generic rank、模零或外层工作流绿色替代。

如果四个剩余因子全闭，结合已刊 C17 覆盖和整个 u=2 排除才得到整个当前 f=u 排除。任一因子未返或非单位，则完整保留；源不冒称整个 Phi 或 ordinary ISP 完成。

## 5. 新输入身份

建议 stem：
2026-11-28-unit211-Phi-zero-true-fu-centered-four-whole-constant-fibers-8542。

零源码/数据依赖；源内四个小多项式只是精确原参数定义。每例保存小阶段、实际维数、rank、原列索引与真实目标幂，不输出大矩阵或系数缓存。此前所有成功与冻结门保持原字节。
