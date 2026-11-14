# R133 补篇：全 regular 边界转置、真实接口与腰幅度校正标量

2026-11-14。**已证明（完整恒等式与可执行消费者）**。本篇接续 [全 regular 补算子与腰幅度 Schur](R133-supplement-full-regular-complement-and-waist-nu-Schur.md)，给出其完整物理边界及有符号接口消费者。新响应和伴随的完整有限试算仍在运行；本文没有原生边界成功值，也没有全频逆或真正 Schur 非零的声明。

新源是 [fourfold_codazzi_regular_mean_completed_physical_boundary.py](../scripts/fourfold_codazzi_regular_mean_completed_physical_boundary.py)。旧 b4-output 源及其真实试算保留，不更名、不改变范围。本篇只复用已经证明的 Laurent 运算、物理矩和真实 DN 预算，另行改变输出及边界投影。

## 1. 完整数据空间与新的外 dual

仍在原 ac1 中心、准确 $\alpha,\nu$、全 $|\eta|\le10^{-9}$ 和原 primitive 尾上工作。状态是物理未规范化 moving 方向 $h=(\delta u,\delta v)$。记

$$
\mathcal D=\partial_r-D_QF,\qquad F_\nu=+\partial_\nu F,
$$
$$
\mathscr A_{\rm reg}h=(\mathcal Dh,U_0h,B_R^{\rm all}h,([h]_i)_i),
\qquad \ell h=D\mathcal A[h_2(0)],
$$

其中 $U_0$ 保所有腰奇 Dirichlet，$B_R^{\rm all}$ 保外偶 mean 和**每个**物理 Robin 行，包括 $\cos4\theta$。完整 response mean 和 adjoint mean 使用同一实际 scalar Green 及其准确 ODE 重构，不以有限试算的 mean 值替代它们。

新消费者要求 trial 的完整 metadata 明确
`Schur_complement=full_regular_waist_amplitude_output`，并绑定实际新 model 的源身份。伴随的初始 mean 必为 $-a_0$，故 body 消费参数准确取 `amp-multiplier=-1`。外 dual 要求新的 kind
`actual_final_physical_all_Robin_dual_regular_complement_v2`，而且完整 $j=1,\ldots,N$ 物理 cosine 幅度乘子全存在；不允许旧 `omitted_physical_mode=4` 字段。

令这些精确有理输入为 $\lambda_{R,j}$。与物理 cosine **幅度**配对的函数为 $2\sum_j\lambda_{R,j}\cos4j\theta$。本篇使用

$$
\boxed{w_R(\theta)=-2\sum_{j=1}^N\lambda_{R,j}\cos4j\theta.}
\tag{A.1}
$$

这里没有旧的 $2\cos4\theta$ 输出项：输出已在腰上。特别地，$\lambda_{R,1}$ 是自由乘子，不能强置零。

## 2. 两端完整转置与均值

写完整均值重构为 $h=w+ze_2$、$\psi=\lambda+\mu e_2$，其中 $w,\lambda$ 的第二均值准确为零。沿用 [物理转置证明](R133-supplement-complete-physical-boundary-transpose-and-Schur-pairing.md) 的完整物理矩泛函 $\mathcal M_{b,c}$ 和原外 mean 行 $\mathcal C$。

腰处准确非mean 幅度梯度为

$$
G_{\mathcal A,\perp}=\frac8{m_0^2}I\sin(4\phi+4\psi_0),\qquad
\ell h=\langle G_{\mathcal A,\perp},w_2(0)\rangle+a_0z(0).
\tag{A.2}
$$

这里 $a_0$ 是已支付的**幅度均值导数列**，并非目标腰半径；源码名称 `bm` 区分两者。所有物理复合由完整指数级数加 Wiener 余项给出。左伴随误差的非mean 第二分量为

$$
P_\perp\{\lambda_2(0)+G_{\mathcal A,\perp}\}.
$$

mean 因 $\mu(0)=-a_0$ 准确满足；奇 Dirichlet 乘子取真实 $\lambda_1(0)$，故第一分量也准确满足。响应的 $U_0h$ 和 $\ell h$ 均照实报告，不能由这一对偶选择设零。

外端令 $\mathcal R$ 是完整非mean regular Robin 行，$\omega_R=\mathcal Ce_2$。选择真实均值乘子

$$
\lambda_{R,0}=\frac{\langle w_R,\mathcal Re_2\rangle-\mu(R)}{\omega_R}.
\tag{A.3}
$$

因为 $w_R$ 已取全非mean 乘子的负号，(A.3) 准确保证
$\psi(R)+(B_R^{\rm all})^*\lambda_R$ 的 mean 为零。此前预算只使用 $\|w_R\|_2$，与它的第四 Fourier 系数是否固定无关，故直接适用于 (A.1)：

$$
|\lambda_{R,0}|<50|\mu(R)|+2.8\cdot10^{-9}\|w_R\|_2.
$$

模型非mean 外误差是

$$
P_\perp\{\mathcal M^*_{-Jw_R,q_{\rm num}w_R}-\lambda(R)\}.
\tag{A.4}
$$

它等于新 $\epsilon_R=\psi(R)+(B_R^{\rm all})^*\lambda_R$ 的相反数，加上被显式支付的完整模型差，因而范数相同。所有真实 regular 误差和未知 nonlinear DN 的转置费用为

$$
1.77\cdot10^{-7}\|w_R\|_2+1.106\cdot10^{-6}|\mu(R)|.
\tag{A.5}
$$

这里保留 $\omega_R^{-1}$、未知物理高模及独立远端背景 $f_B$。只有纯 $\nu$ 响应的独立方向 $\delta f_B$ 取零；原远端 nonlinear matching 方程没有由此消掉。

## 3. 每个原物理 Robin 行及无限尾

完整物理变分矩、指数 Laurent 余项、解析移线和双号尾逐式沿用 [完整边界消费者证明](R133-supplement-complete-boundary-consumer-and-exact-jump-scalar.md) 的 C.2–C.12。它们是任意有限 moving 输入到完整物理角函数的恒等式与上界，不依赖选择哪一条 Schur 输出。

唯一的范数投影变化是：新消费者累加**全部** $k=4j>0$，不排除 $k=4$。对于 $s=0,1/6,1$，若已算至 $j=J$，准确模型范数使用

$$
\left(2\sum_{j=1}^{J}(1+16j^2)^s
  |i\,\delta B_{4j}+q_{\rm num}\delta C_{4j}|^2\right)^{1/2}
+\text{完整双号解析尾}.
\tag{A.6}
$$

真实 DN 与 regular 模型差另付
$(L_{d,s}+\epsilon_{\rm prop})\|\delta Z\|_{H^s}$，其中
$L_{d,0}<5.898255\cdot10^{-6}$、$L_{d,1/6}<1.11\cdot10^{-5}$、
$L_{d,1}<1/4000$，且 $\epsilon_{\rm prop}=9.1496\cdot10^{-18}+2^{-512}$。
外 mean 响应行由同一真实 scalar 重构准确满足；反射只给物理 $B$ 的 mean 恒零，不删除偶 mean。

第四 Robin 的实际响应值仍单独打印为 **retained residual**，以便观察它是否满足原方程；它再也不是本消费者的 scalar 输出。对所有 $j>J$ 的费用与原证明相同，既没有把有限 moving Fourier 当物理截断，也没有将未知 DN 高频清零。

## 4. 完整校正标量与全部准确接口

在两个 trial 的每个真实接口上，源码用输入 double 的精确 dyadic Horner 计算

$$
J_h=\sum_i\langle\lambda(r_i^+),[w]_i\rangle,
\qquad J_\psi=\sum_i\langle[\lambda]_i,w(r_i^-)\rangle.
\tag{A.7}
$$

两份 trial 网格可不同；取迹来自正确单侧片。sine/cosine 系数各带 $1/2$，mean 由连续标量 ODE 重构，故它的跳准确为零。完整 $J_\psi$ 及其范数另列，不能因为 $J_h$ 已进入校正而删除。

记 $R_h=\mathcal Dh-F_\nu$。新模型标量准确组装为

$$
\begin{aligned}
S_{\rm mod}={}&\ell h+
\sum_{j=1}^{N}(w_R)^{\cos}_j
                  (i\,\delta B_{4j}+q_{\rm num}\delta C_{4j})\\
&-\langle\lambda_1(0),w_1(0)\rangle
-\int_0^R\langle\lambda,R_h\rangle,dr-J_h.
\end{aligned}
\tag{A.8}
$$

每个括号是复 Fourier 正系数，(A.1) 中的因子 2 因而准确恢复幅度乘子。外项为 $-\lambda_{R,\perp}B_{R,\perp}^{\rm model}h$。原 body 消费器已证明第二 mean residual 准确为零，真实外 mean 行也准确满足，所以 (A.8) 没有遗漏一个 $\mu R_{h,0}$ 或 $\lambda_{R,0}\mathcal Ch$。

同一完整外误差预算给

$$
|S_0-S_{\rm mod}|<
1.77\cdot10^{-7}\|w_R\|_2\|P_\perp h_2(R)\|_2,
\qquad S_0=\ell h-\mathfrak Y(\mathscr A_{\rm reg}h-\mathfrak F_\nu).
\tag{A.9}
$$

若 $G=\mathscr A_{\rm reg}^{-1}$ 以后被实际支付，则原完整双残差恒等式为

$$
S_{\rm amp}-S_0=-E^*GE,
\quad E=\mathscr A_{\rm reg}h-\mathfrak F_\nu,
\quad E^*=\ell-\mathscr A_{\rm reg}^*\mathfrak Y.
\tag{A.10}
$$

所有体源、边界、mean、两种接口均属于这里同一数据空间。源码只报告 (A.9) 的真实包络及完整残差量；即使该包络排除零，仍不改写为 (A.10) 的真正 Schur 非零结论。

## 5. 实际入口与尚未执行部分

新 source 已实际完成 import/`--help`；这只验证入口，不是 native 成功。需要同一新全 regular response/adjoint 的完整 mean-body 报告后，运行

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python3 \
  scripts/fourfold_codazzi_regular_mean_completed_physical_boundary.py \
  --candidate /path/to/exact-ac1-candidate.json \
  --body /path/to/new-regular-complete-mean-body.json.gz \
  --mean /path/to/complete-original-mean-native.json.gz \
  --response /path/to/new-regular-physical-nonmean-response.json \
  --adjoint /path/to/new-regular-physical-nonmean-adjoint.json \
  --outer-dual /path/to/new-all-Robin-dual.json \
  --moments 256 --max-new-rows 64 --out /path/to/new-boundary-prefix.json.gz
```

恢复时仍只接受同 kind/source/全部输入/全部范围的已成功行前缀；旧 b4-output 报告不会被接收。完整标志仅授予本篇边界、物理无限尾、全部准确接口和校正标量数量，不能授予全频补逆、真实 Schur 非零或最终非线性存在性。
