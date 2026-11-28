# 正确 $\Phi=0$ 图的整个 $f=u$ 原值排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：literature_deddens；AI-assisted GPT-6 Astra Pro。

**状态：完整证明，首次精确执行成功。** 在当前 $D_{\mathrm{val}}\ne0$、非零孤立 mean 的正确原 $\Phi=0$ 图中，整个 $f=u$ 支无原解。因此此范围内以后可支付 $f-u$。本稿闭合此前一次 $C_{17}$ 覆盖中的全部四个剩余常数纤维；没有复用已撤回的错误紧凑 $E_1$，也不宣称整个 $\Phi=0$ 图或普通 ISP 已完成。

## 1. 原范围和全部剩余权因子

采用[正确单 $y$ 原输入](R150-appendix-unit211-Phi-zero-true-fu-single-y-common-weight-curve.md)及[中心 $v$ 的完整两均值来源](R150-appendix-unit211-Phi-zero-true-fu-centered-v-monic-quadratic-and-two-mean-source.md)。记

$$
s=u-1,\quad h=2u-3,\quad \delta=1-Q,\quad
L=Q-2(u-1)(u-2),\quad K=Q+4(u-1),
$$

$$
\ell=L/Q,\qquad
M_n=2uL-L^2-u^2Q,\qquad
\theta=u-L,\qquad
H_f=Q^2-(4u^2-11u+8)Q-4(u-1)(u-2)^2.
\tag{1}
$$

原图已付 $Q,\delta,s,L,K,M_n$。整个 $t=0$ 的正确原排除支付 $t$；整个 $f=u,u=3/2$ 支的原排除支付 $h$；[原均值的 $t-2,\theta$ 身份](R150-appendix-unit211-Phi-zero-fu-t-minus-two-and-theta-original-units.md)支付 $\theta$。$u$ 由独立真实双点乘法的[零基点 mean 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)支付。上述范围不包含被撤回的旧首头、旧 $H_{42}$、旧 $583$ 模型或其单位。

[终端一次 $C_{17}$ 原理想覆盖](R150-appendix-unit211-Phi-zero-true-fu-terminal-C17-once-original-ideal-cover.md)已精确证明

$$
C_{17}\ \sim\
(u-2)^2(2u-1)(2u^2-4u+1)
(2u^3-8u^2+12u-7)F_9(u)
\tag{2}
$$

是原方程的必要纯权条件，其中 $\sim$ 只差非零有理常数，

$$
\begin{aligned}
F_9(u)={}&32u^9-320u^8+1440u^7-3848u^6+6870u^5\\
 &-8886u^4+8828u^3-6650u^2+3296u-763.
\end{aligned}
\tag{3}
$$

[整个 $f=u,u=2$ 的原低式排除](R150-appendix-unit211-Phi-zero-true-fu-entire-u-two-original-low-unit-exclusion.md)已处理 (2) 的第一因子及其全部原值。因此本次只有四个完整有理不可约因子

$$
\phi_1=2u-1,\quad
\phi_2=2u^2-4u+1,\quad
\phi_3=2u^3-8u^2+12u-7,\quad
\phi_9=F_9.
\tag{4}
$$

(2) 的精确因式分解来自已完成的终端来源；本次不重算旧十八列、终端乘子或该因式分解。

## 2. 每个完整常数域上的原有限代数

对 (4) 中的任意 $\phi$，取

$$
K_\phi=\mathbb Q[u]/(\phi_{\mathrm{monic}}).
$$

该完整域保留 $\phi$ 的全部复嵌入，不选某个数值根。原两均值给同一个首一 $Q$ 三次

$$
\begin{aligned}
\Psi={}&Q^3+(-10u^2+24u-15)Q^2\\
&+(32u^4-152u^3+276u^2-228u+72)Q\\
&-32u^6+224u^5-672u^4+1104u^3
-1040u^2+528u-112.
\end{aligned}
\tag{5}
$$

代码从 $\Psi$ 开始，只针对已经支付的七项

$$
Q,\ \delta,\ L,\ K,\ M_n,\ \theta,\ H_f
\tag{6}
$$

反复作完整 $K_\phi[Q]$ gcd。每次被移除的因子 $g$ 都同时整除当前多项式和所标出的原单位；实际返回这两次整除，并始终返回

$$
\Psi=G_\phi\,R_\phi.
\tag{7}
$$

因此任何物理原点必落在保留的 $G_\phi$ 上。这里不是把整个 $Q$ 商假定为域；其余分量及全部 $Q$ 重数仍保留。随后对 (6) 逐项作完整 Bézout 并实际乘回逆，故它们在

$$
A_\phi=K_\phi[Q]/(G_\phi)
$$

中都是真单位。常数 $u,s,h$ 的真逆同样逐项返回。

中心均值身份给

$$
4Q\theta\delta E_{\mathrm{Bo}}
=s\bigl(H_fv^2+4Q\theta h\bigr),\qquad v=t-2.
\tag{8}
$$

所以整个原 $f=u$ 图上 $H_f$ 为单位；其逆由
$-v^2/(4Q\theta h)$ 给出。使用它只是在已付原范围中工作，并未删除新的未处理权面。定义完整首一二次代数

$$
B_\phi=A_\phi[v]\Big/\left(v^2+\frac{4Q\theta h}{H_f}\right).
\tag{9}
$$

在 (9) 中保留所有 $v$ 重数。常数、$Q$ 和 $v$ 的每次短除都返回完整乘积恒等式。全 $\mathbb Q$ 基为

$$
u^iQ^jv^k,\qquad
0\le i<\deg\phi,\quad 0\le j<\deg G_\phi,\quad 0\le k<2.
\tag{10}
$$

每个原点都给 (9) 的一个评价映射；构造只扩大必要环境，没有假定反向每个环境点都是原解。

## 3. 在同一个有限环境中重建真正原 Gram

由中心图的已付原坐标恢复

$$
t=v+2,\qquad
x=u+\frac t4,\qquad
y_0=\frac12-\frac{uv}{4\theta},
$$

$$
Y_f=\frac{M_nh(v+2)/(2\delta)-L(4s^2-Q)}{2\theta},
\qquad
\lambda=\frac{Y_f-(4s^2-Q)}{2L},
$$

$$
T=-\frac LQ-\frac{KY_f}{2QL},
\qquad A_1=\frac{2sY_f}{Q},\qquad w=\lambda-1-T.
\tag{11}
$$

仅为计算完整原式，附加 $\rho^2=\delta$ 并保留两个谱系数：

$$
p=1+\rho,\quad q=1-\rho,\quad
b=\frac{\ell+(u-\ell)\rho/\delta}{2},\quad
c=\frac{\ell-(u-\ell)\rho/\delta}{2},
$$

$$
X=x+\rho y_0,\quad Y=x-\rho y_0,\qquad
r=X-(1-\ell)p-ct,\quad
s_{\mathrm G}=Y-(1-\ell)q-bt.
$$

原四行是

$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s_{\mathrm G}),\quad
g_B=(p,r,0,t),\quad g_C=(q,s_{\mathrm G},t,0).
\tag{12}
$$

全程使用真正双点乘法

$$
a\cdot b=(a_0b_0,\ a_0b_1+a_1b_0,\ a_Bb_B,\ a_Cb_C),
\qquad
\tau(a)=(1-\ell)a_0+a_1+ba_B+ca_C,
$$

及 $1=(1,0,1,1)$、$(\mathcal K a)_i=\tau(g_i\cdot a)$、
$d=\mathcal K1$、$F_2=\tau(d)$。原值式准确为

$$
\begin{aligned}
N_4(a)={}&2\tau(d\cdot a^2)-F_2\tau(a^2)
-4\tau(a)\tau(d\cdot a)\\
&+2F_2\tau(a)^2+\tau(a\cdot\mathcal Ka),\\
P_2(a)={}&\tau\bigl((a-\tau(a)1)^3\bigr).
\end{aligned}
\tag{13}
$$

记 $P_{02}=2sL$，$A_2=2\lambda^2-2\lambda+1$，
$B_3=4\lambda^3-6\lambda^2+3\lambda-1$。本次逐式重建的三个必要值是

$$
\begin{aligned}
N_1={}&N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)
       -4\lambda wP_{02},\\
NS={}&bN_4(g_B)+cN_4(g_C)
       -2\lambda P_{02}(\ell+2T+A_2),\\
PS={}&bP_2(g_B)+cP_2(g_C)
       -P_{02}(\ell+3T+3A_2+B_3).
\end{aligned}
\tag{14}
$$

代码实际返回 $F_2=2u$、$N_4(g_0)=2\lambda P_{02}$，并核 (14) 的 $\rho$ 奇系数全部为零。因此 (14) 是 $B_\phi$ 中同一点的三个真实原值，而不是形式三维矩阵的替代条件。未除 $\lambda,t,D_{\mathrm{val}}$ 或它们的范数。

## 4. 全部四个原理想的精确单位返回

令 $n_\phi=\dim_{\mathbb Q}B_\phi$，将 (14) 的每一行乘以 (10) 的全部基元，构成

$$
\mathcal M_\phi:\mathbb Q^{3n_\phi}\longrightarrow\mathbb Q^{n_\phi}.
\tag{15}
$$

它的像正是原理想 $(N_1,NS,PS)\subset B_\phi$；这次是完整有限商中的乘法，不是仅有 $y$ 次数上界的固定容器。

首次实际结果如下。表中“删除”仅指具有已付原单位来源的 $Q$ 分量。

| 原 $\phi$ 次数 | 已付单位删除 | 保留 $\deg_QG_\phi$ | $n_\phi$ | 原矩阵 | 实际秩 | 真返回目标 |
|---:|---|---:|---:|---:|---:|---|
| $1$ | $Q-1$（来自已付 $\delta$） | $2$ | $4$ | $4\times12$ | $4$ | $1$ |
| $2$ | 无 | $3$ | $12$ | $12\times36$ | $12$ | $1$ |
| $3$ | $Q$（来自已付 $Q$） | $2$ | $12$ | $12\times36$ | $12$ | $1$ |
| $9$ | 无 | $3$ | $54$ | $54\times162$ | $54$ | $1$ |

前三项选择 $N_1$ 的全部基元倍数即得到可逆方阵。九次域中选择 $N_1$ 的前 $45$ 列与 $NS$ 的前 $9$ 列；它们均为实际原列，未使用 Gaussian 余向量冒充原来源。

在每项中，实际返回所选方阵的左右逆、全部原列坐标，以及目标 $1$ 的全部 $n_\phi$ 个坐标。因此

$$
\boxed{\quad 1\in(N_1,NS,PS)\subset B_\phi
\quad\text{对 (4) 的全部四个 }\phi.\quad}
\tag{16}
$$

核回的左右逆坐标数依次为 $32,288,288,5832$；全部原列坐标数为
$48,432,432,8748$。本源允许寻找正目标
$(\lambda tD_{\mathrm{val}})^n$，但四项均在 $n=0$ 已返回 (16)。
结论不是“模素数满秩”，也不是仅有函数域泛型无解；全部运算在完整 $\mathbb Q$ 常数代数中完成。

(7) 保留每个物理原点，(9) 保留中心二次的全部根，而 (16) 排除其所有评价映射。故四个完整权因子的全部复嵌入和全部原值纤维均无原解。

## 5. 整个 $f=u$ 闭合及后续可用范围

由一次原条件 (2)，任何原 $f=u$ 点只能落在 $u=2$ 或 (4)。前者已由独立原低式完整排除，后四者由 (16) 全部排除。因此

$$
\boxed{\quad
\Phi=0,\ f=u
\quad\text{在当前正确 }D_{\mathrm{val}}\ne0
\text{ 原图中无解。}\quad}
\tag{17}
$$

以后可在这一图的物理原点使用 $f-u\ne0$。这是整个 $f=u$ 权面及其原值的排除，不只是某个有限点数界；原 $B=0$ 的 $34/40$ 次权纤维与一般斜率零面仍按各自未付状态继续。

本次没有恢复错误 $R_{\mathrm{bar}}$ 的旧结论，没有把 $f=u$ 排除移给 $\Phi\ne0$ 或 $D_{\mathrm{val}}=0$，也没有给普通不变子空间问题宣称完成。

## 6. 唯一实际执行身份

源：[2026-11-28-unit211-Phi-zero-true-fu-centered-four-whole-constant-fibers-8542.py](../notes/2026-11-28-unit211-Phi-zero-true-fu-centered-four-whole-constant-fibers-8542.py)。

- Git blob：`92a13aee42a5bc7545a6520124b9b64943742e55`。
- 源 SHA-256：`1f88fcd42c37dd94c5477e6acdaad4eee091055ef36c1001f22bf442e4b2944a`。
- 唯一 run/job：46122658831/140910328595，内部退出码 $0$。
- 驱动时间 $3.829886557$ 秒；最大子进程 RSS $43184$ KiB。
- 源提交 `717b58238c4174784ffa481b4e3506bc3cc6e99c`。
- 真 pull 于 2026-11-28 07:45:38.974887 UTC 到 `43a487c4e92ad89cffac108e1eb8c34c3c73d8ea`；两 README blob 无变化。
- 数学 stdout $9591$ bytes，SHA-256 `413569e67a50a1d020be11e76964f52fc5cd64388b3772b4486b9ad32190d581`。

限额为总 $120$ 秒、$1$ GiB，外层驱动 $135$ 秒。没有新依赖文件、没有旧计算复现门，也没有保存大系数载荷；完整精确构造和每项原恒等式均由上述小源再生。
