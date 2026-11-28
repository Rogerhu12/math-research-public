# 修正后的 $\Phi=0$：全 $\alpha,\chi$ 原坐标与三个固定原标量输入

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

本稿是**尚未执行的首次输入说明**。它不恢复已撤回的错误紧凑 $R$ 链，也不预告任一新标量非零或原图为空。唯一源为
`2026-11-28-unit211-Phi-zero-true-whole-alpha-chi-three-original-quadratics-8542.py`，
SHA256 **1f657b714499108e3efcf000dd0afb2dc2cbf35a4e283216d418dc415db1cef6**。
源自含、没有文件依赖；首次界为 120 秒、1 GiB，外驱动 135 秒。只打印小型阶段摘要、次数、项数、哈希及至多 35 项的小式，不保存可重算系数载荷。

## 1. 当前原图与真实单位

范围是当前 unit211 的 $\Phi=0,\ D\ne0$ 原单位图。沿用真正原定义的 $E_0,N_0,P_1$ 恢复，并记

$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2s(u-2),\quad K=Q+4s,\quad
\ell=L/Q,\quad m=u-\ell,
$$

$$
\theta=u-L,\quad
M_n=2uL-L^2-u^2Q,\quad M=M_n/Q=4bc\delta,
$$

$$
T_0=-K,\quad J=2u(1-u)+L,\quad P_{02}=2sL,\quad
A=4s^2-Q.
$$

原 $u,Q,\delta,s,K,L,M_n$ 的单位只取已付原范围。整 $t=0$、整 $f=u$、整 $A=0$ 已从纠正后的原式排除，故本图可用 $t(f-u)A\ne0$。规范来源为：

- [整 $t=0$ 原排除](../results/R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)；
- [整 $f=u$ 原排除](../results/R150-appendix-unit211-Phi-zero-true-entire-fu-original-exclusion.md)；
- [整 $A=0$ 第二线性支及全曲线排除](../results/R150-appendix-unit211-Phi-zero-true-Azero-second-linear-and-whole-curve-exclusion.md)。

$m$ 的单位取自既有 [整个等权原排除](../results/R150-appendix-unit211-equal-weights-complete-original-exclusion.md) 第 5 节。此次仅静读该完整定理、主源及边界来源：实际均值均使用 $\operatorname{vm}(d,d)[1]$，没有错误紧凑式。当前 $m=0$ 给旧权参数 $\mu=u=\ell$、$Q=4-2u$、旧 $J=2$，其全部原单位及 $D\ne0$ 范围满足；并未执行旧门或重新登记旧定理。

最后

$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q=-sA
$$

为当前真单位。源码允许的全部权分母仅来自

$$
uQ\delta sKLM_n A(uQ-L).
$$

尤其**不倒置 $\alpha,\chi,\theta,D,\lambda$ 或任一新头**。

## 2. 全 $\alpha,\chi$ 原坐标

采用已刊 [自由权下的原 $\alpha,\chi$ 身份](../results/R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md) 第 1 节 (2)、第 2 节 (4)–(7)。这些恒等式位于该文施加 W 权关系之前；本输入不采用 W 的任何单位支付。

令 $\eta=f-u$、$Z=u(u-1)+\ell(1-\ell)Q$，定义

$$
\alpha=4\delta\eta-\theta t,\qquad
\chi=\frac{2\delta A_1}{t}-Z.
$$

真实 $t\ne0$ 支付该逆向定义。原 $R=0$ 给

$$
mR_wt=-\alpha\chi-2\delta\ell R_w.
$$

因此完整正向恢复为

$$
t=-\frac{\alpha\chi}{mR_w}-\frac{2\delta\ell}{m},\qquad
f=u+\frac{\alpha+\theta t}{4\delta},
$$

$$
V=f+\frac{(M-Z-\chi)t}{4\delta},\qquad
A_1=\frac{(\chi+Z)t}{2\delta}.
$$

再令

$$
W_1=(T_0+4uf)/2,\qquad
x=\frac{\theta V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},
$$

$$
\lambda=\frac{Jf+bcQt-QV-sT_0}{P_{02}},\qquad
T=\frac{T_0A_1}{2P_{02}}-\ell.
$$

所有恢复量对 $\alpha$ 次数至多 1，系数为 $\mathbb Q(u,Q)[\chi]$，且分母只有上述已付权因子。$\alpha=0$、$\chi=0$ 和 $\theta=0$ 均完整保留。正向和逆向仅在当前原 $t$ 单位图互逆；计算中的较大多项式环境可含 $t=0$ 点，这不会删除原点。

## 3. 真原 Gram、三条 $\alpha$ 二次

源码在 $\rho^2=\delta$ 的完整二次环境内取

$$
b=\frac{\ell+m/\rho}{2},\quad c=\frac{\ell-m/\rho}{2},
\quad p=1+\rho,\quad q=1-\rho,\quad
X=x+\rho y,\quad Y=x-\rho y,
$$

$$
r=X-(1-\ell)p-ct,\qquad s_1=Y-(1-\ell)q-bt.
$$

原四行为

$$
(0,0,p,q),\quad(0,A_1,r,s_1),\quad
(p,r,0,t),\quad(q,s_1,t,0).
$$

双点乘法始终是 $(v_0w_0,v_0w_1+v_1w_0)$，所以均值使用完整 $\operatorname{vm}(d,d)$。源码从原 $\tau,DK,N_4,P_2$ 实际构造并返回 $E_0=0$、$E_1=bE_B+cE_C$、$N_0=2\lambda P_{02}$ 及 $P_{\rm jet}=3wP_{02}$。随后保留

$$
F_0=E_{Be},\qquad F_1=E_{Bo},\qquad F_2=N_1,
\quad E_B=E_{Be}+\rho E_{Bo},
$$

其中 $N_1$ 使用完整 $N_4$ 极化。三式都是真 $\alpha$ 二次。若

$$
F_i=c_i+b_i\alpha+a_i\alpha^2,
$$

则三乘三系数矩阵是**原点的固定容器**，没有假定其商自由，也未将三个新行当成完整 NS/PS 理想。

## 4. 三个新的固定标量来源

第一目标取上述 $3\times3$ 矩阵常数列的 cofactors $\mu_i$。源码逐列返回

$$
\sum_i\mu_i(c_i,b_i,a_i)=(C,0,0),\qquad
\sum_i\mu_iF_i=C.
$$

另两目标是固定二次次数的 $\operatorname{Res}_\alpha(F_1,F_0)$ 与 $\operatorname{Res}_\alpha(F_1,F_2)$。对于

$$
F=a\alpha^2+b\alpha+c,\qquad
G=d\alpha^2+e\alpha+f,
$$

置 $p=af-cd$、$q=ae-bd$、$r=bf-ce$，直接用

$$
(qe-pd+qd\alpha)F+(-qb+pa-qa\alpha)G=p^2-qr.
$$

这是固定 $4\times4$ Sylvester 的真多项式身份；$a=0$、$d=0$、全部进一步降次均保留。源码按 $\alpha^0,\ldots,\alpha^3$ 全四坐标乘回。

每个目标仅清实际乘子的已付权分母，再取这些**全部实际乘子**的共同多项式因子，精确相除后重新返回所有原坐标。因新乘子仍为多项式，这一步保共同因子为零的整支；不是约掉原方程或把该因子假设为单位。最终标量仅再剥已付权因子，全部剩余 $\chi$ 和权零面保留。

## 5. 实际结果的登记界限

若固定目标为零，只登记精确原组合及零事实。若得到非零剩余多项式，只得到当前原点必须满足的新必要 $\chi$–权条件。除非实际原恒等式返回已付单位，不宣称整图为空；不凭单个原标量宣称权投影有限。此次没有重放旧 B 的大矩阵、既有 $\alpha=0$ 门、旧错误 Phi 头、旧结式或任何已成证明门。
