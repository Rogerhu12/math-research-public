# R150：正确 Phi 的全 alpha–chi 原坐标、三个原二次与固定标量条件

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**已证明。** 当前修正后的 $\Phi=0,\ D_{\rm val}\ne0$ 原单位图具有下述完整 $\alpha,\chi$ 坐标。所有恢复仅除已付权参数；$\alpha,\chi,\theta$ 及三个原二次的首项零支全部保留。原 $E_{Be},E_{Bo},N_1$ 真正成为 $\alpha$ 二次，并得到三个完整原必要多项式：

$$
C_3(u,Q,\chi)=C_{BB}(u,Q,\chi)=C_{BN}(u,Q,\chi)=0.
$$

准确三变量次数分别为 $(29,11,6),(38,15,8),(46,18,8)$。**它们仍只是必要条件；本篇没有得到纯权覆盖、权点有限性或整 Phi 排空。**

## 1. 当前正确单位来源

设

$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2s(u-2),\quad K=Q+4s,\quad \ell=L/Q,
$$

$$
m=u-\ell,\quad\theta=u-\ell Q,\quad
M_n=2uL-L^2-u^2Q,\quad M=M_n/Q=4bc\delta,
$$

$$
T_0=-K,\quad J=2u(1-u)+L,\quad P_{02}=2sL,\quad
A=4s^2-Q.
$$

当前原 $uQ\delta sKLM_n$ 已付。正确的 [整 t 零](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)、[整 f=u](R150-appendix-unit211-Phi-zero-true-entire-fu-original-exclusion.md)、[整 A 零](R150-appendix-unit211-Phi-zero-true-Azero-second-linear-and-whole-curve-exclusion.md)排除给 $t(f-u)A\ne0$。

$m\ne0$ 只沿用独立真原 [整个等权排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)第 5 节。本次对应来源已静读到 $\operatorname{vm}(d,d)[1]$：当前 $m=0$ 给旧 $\mu=u=\ell,Q=4-2u,J_{\rm old}=2$，全部旧原分母和 $D_{\rm val}\ne0$ 范围满足。没有恢复已撤回的错误 compact 头或任何旧 Phi 大模型。

原权恒等式

$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q=-sA
$$

支付 $R_w$。以下分母支撑恰包含在

$$
uQ\delta sKLM_nA(uQ-L)
$$

内，完全不要求 $\theta\ne0$。

## 2. 全坐标及同点原恢复

令 $Z=u(u-1)+\ell(1-\ell)Q$，定义

$$
\alpha=4\delta(f-u)-\theta t,\qquad
\chi=\frac{2\delta A_1}{t}-Z.
\tag{1}
$$

采用 [自由原 alpha–chi 身份](R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md)施加 W 权关系之前的部分；本篇没有移用 W 的任何特殊支付。正确原 $R=0$ 给

$$
mR_wt=-\alpha\chi-2\delta\ell R_w.
\tag{2}
$$

因此

$$
t=-\frac{\alpha\chi}{mR_w}-\frac{2\delta\ell}{m},
\qquad f=u+\frac{\alpha+\theta t}{4\delta},
$$

$$
V=f+\frac{(M-Z-\chi)t}{4\delta},\qquad
A_1=\frac{(\chi+Z)t}{2\delta}.
\tag{3}
$$

令

$$
W_1=(T_0+4uf)/2,\quad
x=\frac{\theta V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},
$$

$$
\lambda=\frac{Jf+bcQt-QV-sT_0}{P_{02}},\qquad
T=\frac{T_0A_1}{2P_{02}}-\ell,\qquad w=\lambda-1-T.
\tag{4}
$$

(1)–(4) 在当前原 $t$ 单位图双向；正向较大的多项式环境允许额外 $t=0$ 点，但不删除原点。所有 (3)–(4) 对 $\alpha$ 次数至多 1。源码完整返回 (1)、(2)、$A_1=2f-2V+2bct$、两个均值恢复及正确 $R=0$。

取 $\rho^2=\delta$，恢复 $p=1+\rho,q=1-\rho$、$b,c$、$X=x+\rho y,Y=x-\rho y$ 和完整四行 Gram。实际均值始终用真双点乘法；随后原 $E_0=0$、$E_1=bE_B+cE_C$、$N_0=2\lambda P_{02}$、$P_{\rm jet}=3wP_{02}$ 均从原 $\tau,DK,N_4,P_2$ 返回。

## 3. 三个完整原 alpha 二次

写 $E_B=E_{Be}+\rho E_{Bo}$，并取原双点 N 极化

$$
N_1=N_4(k_0+k_1)-N_4(k_0)-N_4(k_1)-4\lambda wP_{02}.
$$

实际三条原行

$$
F_0=E_{Be},\quad F_1=E_{Bo},\quad F_2=N_1
$$

各准确为

$$
F_i=c_i(u,Q,\chi)+b_i(u,Q,\chi)\alpha
+a_i(u,Q,\chi)\alpha^2.
\tag{5}
$$

九个系数全部只有上述已付权分母。各行三系数的 $\chi$ 次数分别至多 $2,3,4$；实际 $\alpha$ 次数均为 2。

此矩阵是原点的固定系数容器，不假定商自由，也没有声称三式替代全部原 NS/PS 或个别值方程。

## 4. 三个固定原标量，保所有退化首项

对 (5) 的 $3\times3$ 系数矩阵，取常数列 cofactors $\mu_i$，实际全三坐标返回

$$
\sum_{i=0}^2\mu_i(c_i,b_i,a_i)=(C,0,0),
\quad \sum_i\mu_iF_i=C.
\tag{6}
$$

另对 $(F_1,F_0)$、$(F_1,F_2)$，始终取固定次数 $(2,2)$ 的四阶 Sylvester 身份。具体若

$$
F=a\alpha^2+b\alpha+c,\quad
G=d\alpha^2+e\alpha+f,
$$

令 $p=af-cd,q=ae-bd,r=bf-ce$，则

$$
(qe-pd+qd\alpha)F+(-qb+pa-qa\alpha)G=p^2-qr.
\tag{7}
$$

源码对 (7) 返回完整 $\alpha^0,\ldots,\alpha^3$ 四坐标，没有求 a、d、q 或任何新头的逆。原式降次以及两首项同时为零的纤维均被保留。

每个目标先清**实际全部乘子**的权分母，再精除这些乘子的共同内容，并在新乘子下重新返回全部原坐标。因此共同内容为零的整支不被删除。三个实际共同内容依次为 $1,Q,1$。最后仅剥真实已付权因子并规范化非零有理数，所得为：

| 原标量来源 | 原必要多项式 | $(\deg_u,\deg_Q,\deg_\chi)$ | 总次数 | 项数 |
|---|---|---:|---:|---:|
| 三原行固定 $3\times3$ | $C_3$ | $(29,11,6)$ | 29 | 982 |
| EBo、EBe 固定四阶 | $C_{BB}$ | $(38,15,8)$ | 38 | 1797 |
| EBo、N1 固定四阶 | $C_{BN}$ | $(46,18,8)$ | 46 | 3475 |

规范多项式字典 SHA256 为：

- $C_3$：`8c5aa2dd0ddf7406aecf9665d600733904343919d1f4adb6c458f51d4095d2d7`；
- $C_{BB}$：`850cd91a71410cca471bee422b28d09201d00195be810e62ce12a457648835d9`；
- $C_{BN}$：`90149f789bfa1b152b93b74f3890896ebceccb5729d8260a4d9af5d93a121f4d`。

这些是当前已付系数环中有完整原来源的条件，所有剩余零集保留。尤其不能从三条非零多项式直接推共同权投影为真曲线或有限集；后续仍需新的 $\chi$ 消元、首项覆盖及完整原值。

## 5. 唯一实际执行

源：[全 alpha–chi 三原二次输入](../notes/2026-11-28-unit211-Phi-zero-true-whole-alpha-chi-three-original-quadratics-8542.py)，零依赖；blob `d0f4bb3377d2e9bfdecf41c2f9e99fdbb7072fa3`；SHA256：

`1f657b714499108e3efcf000dd0afb2dc2cbf35a4e283216d418dc415db1cef6`。

run **46127135921**，job **140924131042**。source `b0e5dbcc91e880c0ed5dd720c64394801974f354`，真实 pull 在 2026-11-28 08:43:43.304181 UTC 到 `4ec27d84a75d93b680be7c74f13270e5980d6f14`；两 README 无变。

数学末阶段 1.339767688 秒，驱动 1.409140991 秒，RSS 46304 KiB，exit 0。源限 120 秒/1 GiB，外驱动 135 秒。共 110 次精确权多项式整除，所有上述原坐标返回完成。stdout 7290 字节，SHA256：

`684d3f5ecd36df7044d1b021c2873fdfd293e7894819f8b319f59dcca25d9bbf`。

[小回执](../notes/2026-11-28-unit211-Phi-zero-whole-alpha-chi-three-quadratics-execution-8542.json)保存实际阶段和哈希，没有系数载荷。本篇不重放旧 cofactor、大矩阵或已撤回的错误紧凑链；普通 ISP 未完成。
