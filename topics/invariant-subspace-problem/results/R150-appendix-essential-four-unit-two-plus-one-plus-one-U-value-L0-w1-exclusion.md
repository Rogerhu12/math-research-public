# R150 附录：unit 2+1+1 的 L=0、w=1 整层排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录完整排除 $L=0,w=1$，保留两个 lambda 共轭、全部 rho 值及原 P1 系数为零的纤维。结合已付 $w=0$ 排除，所有剩余 $L=0$ 原解必须满足 $w(w-1)\ne0$；本附录不宣称这个剩余范围或整个非零均值层为空。

## 1. 原值图与 L=0 的全部意义

沿用[原 U 值图及原恒等式](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)的 unit 2+1+1 Frobenius 代数

$$
\tau(v)=av_0+v_1+bv_B+cv_C,\qquad a=1-b-c,
$$

以及原活动 Gram 矩阵

$$
K=\begin{pmatrix}
0&0&1&q\\
0&A_1&r&s\\
1&r&0&t\\
q&s&t&0
\end{pmatrix}.
$$

已经关闭的分支允许保留

$$
bcq(q-1)(q+1)uP_0\lambda\ne0,\qquad
u=b+cq,\quad V_2=b+cq^2,
$$

$$
P_0=\frac{b+cq^3-3uV_2+2u^3}{2}.
$$

原临界值归一为 $V=(1,w,h,k)$，满足

$$
\tau V=\lambda,\qquad \tau V^2=2\lambda^2,\qquad
\tau V^3=4\lambda^3,\qquad N(V)=0,
$$

并保留完整原 mean、最高式与第二梯度条件。这里 $\lambda=m/U_0$，没有另行把 $U_0$ 无条件规范为 1。

记

$$
L=q(h-1)-(k-1).
$$

在 $L=0$ 上，令 $\rho=h-1$，于是

$$
h=1+\rho,\quad k=1+\rho q,\quad
V=\mathbf1+\rho k_0+w\epsilon.
$$

$\rho=0$ 会给 $h=k=1$，与已登记的三个矩恒等式不相容。因此 $\rho\ne0$，且在 $q(q-1)\ne0$ 下三个值自动互异。

原 $N$ 的极化身份、以及同一原 $E_0=0,N_0=\lambda P_0$ 给出

$$
N(V)=w(w-1)f+u\left(\frac w2-w^2\right)
+\frac{\rho(V_2-2u^2)}4+\lambda\rho^2P_0. \tag{1}
$$

该身份已在 U 值图的小源中从原 $N$ 核验。它直接支付 $w=0$：此时 $V=\mathbf1+\rho k_0$，原 $P(V)=0$ 变成 $\rho^3P_0=0$，矛盾。下文完整处理另一无法直接解 f 的面 $w=1$。

## 2. w=1 的二次数域与 rho 参数图

置

$$
R=\lambda-2,\quad
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1.
$$

三个原矩逐一给出

$$
\rho u=R,\qquad \rho^2V_2=A,\qquad
\rho^3(b+cq^3)=B.
$$

于是无须使用任何额外方程，

$$
\rho^3P_0=\frac{B-3RA+2R^3}{2}
=6\lambda-\frac{11}{2}. \tag{2}
$$

将 (2) 和两个原矩代入 (1)，精确得到

$$
4\rho N(V)=3(8\lambda^2-6\lambda-1).
$$

因此

$$
8\lambda^2-6\lambda-1=0. \tag{3}
$$

工作数域为

$$
F=\mathbb Q[\lambda]/(8\lambda^2-6\lambda-1).
$$

它是二次数域，两个复嵌入都必须保留；不选择其中某个 lambda 数值。由 (3)，

$$
A=\frac{5-2\lambda}{4},\quad
B=\frac{10\lambda-11}{8},\quad
C=RB-A^2=\frac{3(7-10\lambda)}{16}\ne0.
$$

原谱恒等式 $b+cq^3=(1+q)V_2-qu$ 给出

$$
B=\rho A+q\rho(A-\rho R).
$$

定义

$$
D=A-\rho R,\quad N=B-\rho A,\quad
M=B-2\rho A+\rho^2R,\quad J=B-\rho^2R.
$$

若 $D=0$，上式还给 $N=0$；因 $R\ne0$，这将迫使 $RB-A^2=0$，与 $C\ne0$ 矛盾。所以 D 非零，且完整参数图为

$$
q=\frac{N}{\rho D},\qquad
b=\frac{C}{\rho M},\qquad
c=\frac{D^3}{NM},\qquad
u=\frac R\rho,\qquad V_2=\frac A{\rho^2}. \tag{4}
$$

其中

$$
q-1=\frac{M}{\rho D},\qquad
q+1=\frac{J}{\rho D}.
$$

故以下五个多项式都是已付单位：

$$
\rho,\quad D,\quad N,\quad M,\quad J. \tag{5}
$$

这份清单完整解释了后续每一个参数分母。新源不把共轭范数的零点额外排除，也不借这些范数引入新的参数单位。

## 3. 保留全部原九式的同一 f,t 图

以 (4) 生成 $a,b,c,q,u,V_2,P_0$。同一原 $E_0=0,N_0=\lambda P_0$ 的全局图为

$$
W_1=V_2/2-u^2+2fu,
$$

$$
W_2=uV_2-2u^3+f(V_2+2u^2)-bcqt+2\lambda P_0,
$$

$$
X=\frac{qW_1-W_2}{b(q-1)},\qquad
Y=\frac{W_2-W_1}{cq(q-1)},
$$

$$
r=X-a-ct,\quad s=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct.
$$

这里实际上只需

$$
\frac1{b(q-1)}=\frac{\rho^2D}{C},\qquad
\frac1{cq(q-1)}=\frac{\rho^2}{D},
$$

所以没有未登记的新分母。

源码依原代数乘法、$\tau$、$D_K$、$P$、$N$ 及真正的双点 germ 重建原系统，并逐项检查

$$
f=\tau(D_K\mathbf1)/2,\quad E_0=0,\quad
P(k_0)=P_0,\quad N(k_0)=\lambda P_0,\quad P(V)=N(V)=0.
$$

随后生成完整九式

$$
E_1,E_B,E_C,\quad
P_1-3P_0,\quad P_B-h^3P_0,\quad P_C-k^3P_0,
$$

$$
N_1-2\lambda P_0,\quad
N_B-\lambda h^2P_0,\quad N_C-\lambda k^2P_0.
$$

原最高式乘 2、原第二梯度式乘 4 仅去除有理常数分母。九式对 $(f,t)$ 的真实总次数依次为

$$
2,2,2,1,3,3,2,3,3.
$$

原 P1 在 f,t 中一次，这是双点一阶 germ 的真实次数，未把双点第二行当作另一个简单点。

实现中，参数系数以 $F[\rho]$ 的分子和五个单位 (5) 的指数表表示。加法取分母指数逐项最大值，乘法取和；清分母后只剥离真正整除全部系数的 (5) 中因子。每次整除都回乘检查。内部为判定多项式整除所用的共轭范数除法，只在余数严格为零时接受，并核验商乘回原式；它不改变实际局部化环，也没有删掉共轭单位为零的候选。

## 4. 两个齐次消元方向保留 P1 的全部零首项

把清过已付单位的原 P1 写为

$$
\alpha(\rho)f+\beta(\rho)t+\gamma(\rho)=0,
\qquad \alpha,\beta,\gamma\in F[\rho]. \tag{6}
$$

不假设 $\alpha$ 或 $\beta$ 非零。对于某条原式

$$
G(f,t)=\sum_{i,j}g_{ij}(\rho)f^it^j,
\qquad d=\deg_fG,
$$

定义不作除法的齐次投影

$$
\widehat G_f(t)=
\sum_{i,j}g_{ij}(\rho)\alpha^{d-i}
(-\beta t-\gamma)^it^j. \tag{7}
$$

若 $(\rho_0,f_0,t_0)$ 是原共同零点，(6) 给
$-\beta t_0-\gamma=\alpha f_0$，所以

$$
\widehat G_f(t_0)=\alpha(\rho_0)^dG(f_0,t_0)=0.
$$

这个身份在 $\alpha(\rho_0)=0$ 时仍然成立。特别是 $\alpha=\beta=\gamma=0$ 的参数也没有被除掉。对调 f 与 t，定义第二方向 $\widehat G_t(f)$；同样保留 $\beta=0$ 的全部纤维。

源码对完整九式同时生成两个方向的 (7)，只剥离已付单位 (5)。不以 $\alpha$、$\beta$、投影最高系数或新结果式因子作单位。随后在各方向用完整 Sylvester 行列式计算两条投影原 mean 的结果式。任何原共同有限根必使相应行列式为零；即使专化后次数下降，必要性也不变。

因此两方向给出的是同时适用于每个原解的必要条件，而不是只覆盖 $\alpha\beta\ne0$ 的两个互不重叠图。特别无需额外补一个 P1 首项全零的孤立参数面。

## 5. 三个真实 QQ 范数结果式已经矛盾

记对应 $F[\rho]$ 结果式为 $\mathcal R_i$。源码依次计算：

| 序号 | 消元方向及原 mean 对 | $\deg_\rho\mathcal R_i$ | QQ 范数的累计 gcd 次数 |
|---|---|---:|---:|
| 1 | 消 f，$E_1,E_B$ | 32 | 64 |
| 2 | 消 t，$E_1,E_B$ | 40 | 48 |
| 3 | 消 f，$E_1,E_C$ | 32 | 0 |

这里每个 $\mathcal R_i$ 都来自本附录同一份原九式，没有使用抽象自由 Gram 的另一个系统。

若 $v=a(\rho)+b(\rho)\lambda$，其共轭和范数为

$$
\overline v=a+\frac34b-b\lambda,\qquad
\operatorname{Nm}(v)=a^2+\frac34ab-\frac18b^2.
$$

在任一 lambda 嵌入下，$\mathcal R_i(\rho_0)=0$ 必然推出
$\operatorname{Nm}(\mathcal R_i)(\rho_0)=0$。因此每个原解的同一个 rho 坐标必须是三个 QQ 多项式

$$
\operatorname{Nm}(\mathcal R_1),\quad
\operatorname{Nm}(\mathcal R_2),\quad
\operatorname{Nm}(\mathcal R_3)
$$

的公共零点。实际 QQ Euclidean gcd 为非零常数，故不存在这样的 rho。

此处只用范数零条件的必要性；未把不同 lambda 共轭上的范数交点认成同一原解，也未把范数条件称为充分。累计 gcd 已为常数，所以源码预备的二次数域 gcd 后备分支没有执行。

由此 $L=0,w=1$ 的整个原系统排除。结合第 1 节的 $w=0$ 排除，所有尚存 $L=0$ 解都满足 $w(w-1)\ne0$，因而 (1) 在剩余范围全局给出

$$
f=
\frac{u(w^2-w/2)-\rho(V_2-2u^2)/4-\lambda\rho^2P_0}
{w(w-1)}.
$$

这最后一个公式只是剩余图的坐标覆盖，不是其排除。完整物理几何未被替换；本附录已在原系统的必要子条件中取得矛盾，故无须把任一抽象必要解宣成物理临界点。

## 6. 实际执行身份

[自含源码](../notes/2026-11-26-unit211-U-value-L0-native-algebra-347c.py)及[实际小回执](../notes/2026-11-26-unit211-U-value-L0-native-execution-347c.json)均已保留；可重新生成的投影系数与范数数组不保存。

冻结 blob：c7b972d1fbc52775b2735d7657c0562b249fc397；11806 bytes。

源码 SHA256：

b1b30f4af0ff76187005861f3c1425707cd955e71f049f85ea2cdc4360d86abb。

依赖 Python 3.12.14、python-flint 0.9.0。公开 Actions run 45808873477 / job 139871189527；冻结源提交 e74a6d1b37742414d1215bb37440b7c2fe56851c。实际 pull 到 0423c3c399f117d4ab3e077fbfb8d7f8ee242c3a，根 README 与课题 README 的 blob 均未变。

原参数图核验 0.002742 秒；完整原九式生成核验 0.145116 秒；所有 QQ 结果式与最终 gcd 完成于 0.222536 秒。源内峰值 RSS 34524 KiB；驱动总计 0.298137876 秒、峰值 RSS 35204 KiB，退出码 0。

原九式输入 SHA256：

88918140426e7a9fab4ad2159baa2dd07cc5815a5a87e4c888e74f67803ee7ae。

stdout SHA256：

3bb16c277296eff08994a31cd6af01dea44a238fd180dc1158f2f84db7b6ab5e。

最终状态 exact_original_fiber_excluded，finalNormGcdDegree=0，finalFieldGcdDegree=null；claimLambdaLayerEmpty=false、ordinaryISPClaim=false。

旧 SymPy 分式版本 run 45802044010 / job 139847488409 在 900.011302 秒源内闹钟停止，驱动 900.384475770 秒、退出码 124，尚未输出完整原九式生成阶段。它不构成本排除的依据。新源用原单位指数表保留同一局部化图，实际完整执行如上；没有把旧超时算成已完成的代数计算。
