# R150 附录：整个 W/b0 的原 t 参数完整 I6、十四行值加强及两个同点标量

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：唯一首次新源实际完整成功，源 exit 0。
- 范围：当前正确 W、distinct-singleton、物理 $D\ne0$、$b_0=0$ 的既有已付原权图。
- 结果：原首一 $\lambda^2$ 与完整 $I_6$ 十二行二列实际形成；加入原必要 $q_2$ 后十四行二列全返回；两个新的同 $\lambda$ 原标量对 $t$ 的实际次数为 3、4。
- 本篇没有新的纯权覆盖、有限点数上界或整个 b0/W 排空结论。

## 1. 同一原坐标与首一 lambda 二次

沿[整个 b0 的 t 参数首一二次纸证](R150-appendix-unit211-W-entire-b0-original-t-parameter-monic-lambda-two-and-exact-I4.md)，使用已付逆权坐标 $(u,\nu)$，保留原 $t$，并有

$$
A_*=4uQ-J=uQ(\nu+2),\quad
\kappa=uQ\ell/A_*,\quad T=\kappa(2\lambda-3),
$$

$$
f=\frac{P_{02}(T_0-2\kappa Q)\lambda+(u-1)T_0^2
-QP_{02}(\ell-3\kappa)-bcQ\Phi t}{P_f},
$$

$$
V=\frac{Jf-\lambda P_{02}-(u-1)T_0+bcQt}{Q}.
\tag{1}
$$

所有分母已在当前原图支付。一般 W 的 $\Phi$ 项完整保留；$f$ 的 $t$ 系数是旧单位 $-bcQ\Phi/P_f$，所以新 $(\lambda,t)$ 与旧 $(\lambda,f)$ 图真正双向。不存在新增几何开集。

由同一完整真 Gram，三均值 $(\mathcal R,E_{B,e},E_{B,o})$ 对 $(f^2,fV,V^2)$ 的纯权头 $H$ 满足

$$
\det H=32uQ(2\ell-1)/M^2.
$$

$2\ell-1$ 来自[整个 W/Lhalf 的完整原排除](R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)。其余原权分母同上个纸证。令

$$
C=\begin{pmatrix}-1/2&\ell/2&m/2\\0&1&0\\0&0&1\end{pmatrix},
\qquad
\gamma=\frac{(J^2,-2JQ,Q^2)}{P_{02}^2}H^{-1}C.
$$

此次实际返回

$$
\boxed{
q_\lambda=\gamma(E_1,E_{B,e},E_{B,o})^t
=\lambda^2+q_1(t)\lambda+q_0(t),
\quad \deg_tq_1=1,\quad\deg_tq_0=2.
}
\tag{2}
$$

$\gamma$ 完全是纯权行，$\lambda^2$ 系数准确为 1。实际九个头逆坐标、完整原坐标及 (2) 的三原来源均已乘回。$E_1$ 是独立真 germ 均值，一阶平方采用 $2d_0d_1$，没有使用撤回的 compact 错式。

两个新系数只保存定义与 profile：

| 系数 | 分子 $(u,\nu,t)$ 次数 | 分子项数 | 分子 SHA256 |
|---|---|---:|---|
| $q_0$ | $(14,13,2)$ | 466 | dc16d269aa9226c431a3d04e1a14817fe5676f46d5ac3b6db7eedf7016d8ece3 |
| $q_1$ | $(10,10,1)$ | 182 | c14e019d04883f8b093a0a3d260e1ed8c1019af02154c60a21ffb2c9aafb1c40 |

这些分子的对应分母仍只含实际已检查的旧原权支持；它们不是未付几何头。

## 2. 全部六原式与 b0 原值 q2

此次源在同一原 Gram 中直接计算完整 $N_4$、中心 $P_2$，返回原 $N_0=2\lambda P_{02}$、三次 jet $3wP_{02}$，以及两个 singleton 行的完整 $N/P$ 共轭身份。由此构造

$$
F=(E_1,E_{B,e},E_{B,o},N_1,NS,PS,q_2).
\tag{3}
$$

其中 $N_1$ 是完整极化而非其一部分，NS/PS 是完整加权三次。前六式生成原 $I_6$。

第七式沿已刊整个 b0 的原值来源。记

$$
D=\ell(2\lambda^2-2\lambda+1)-T^2,\qquad
C_*=A_*m^2+J\delta\ell^2,
$$

$$
a_d=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQ(3-2\lambda)\ell T+DC_*,
\qquad q_2=2a_d/\ell.
\tag{4}
$$

在 $b_0=0$ 上，原 $C_4=mD\ell q_2$。当前物理 $mD\ell$ 已付，所以所有原物理解都满足 $q_2=0$。这个必要性范围不能移到物理 $D=0$；程序本身没有反演 $D$。也没有反演 $q_2$ 的任何 $\lambda$ 头。

因此

$$
J_7=I_6+(q_2)
$$

是当前原物理系统的必要加强，不被称为完整 $I_{11}$ 的充分呈示。

## 3. 精确十二行与十四行实际返回

对 (3) 的每一式只作首一普通除法

$$
F_i=Q_iq_\lambda+r_i,\qquad
r_i=A_i(t)+B_i(t)\lambda.
\tag{5}
$$

若把 $\gamma$ 用零补到七坐标，原乘子为

$$
\tau_i=e_i-Q_i\gamma,\qquad \tau_iF=r_i.
$$

源对每个普通多项式身份完整乘回。再逐行返回

$$
\lambda r_i-\{-q_0B_i+(A_i-q_1B_i)\lambda\}=B_iq_\lambda
\tag{6}
$$

及其完整七原乘子 $\lambda\tau_i-B_i\gamma$。

实际七条基本余式的 $(\deg_tA_i,\deg_tB_i)$ 为

$$
(2,1),(2,1),(2,1),(2,1),(3,2),(3,2),(2,1).
\tag{7}
$$

因此在首一环境

$$
B=A_W[t][\lambda]/(q_\lambda)
$$

中，前四式及其 $\lambda$ 倍给八行精确 $I_4$，前六式给十二行精确 $I_6$，全部七式给十四行精确 $J_7$。这里自由二坐标只属于 $B$ 的基 $(1,\lambda)$，没有假定原方程商自由。

这次十二/十四行及其原来源都已实际形成，与此前仅纸面给出的再生定义有明确区别。全部七次首一除法、十四个原行和对应乘法来源均完整返回；没有留下未核的整行。

## 4. 两个新同 lambda 标量及真实内容取消

预先固定两对 $(q_2,N_1)$、$(q_2,NS)$。对对应行 $i,j$，取

$$
H_{ij}=A_iB_j-A_jB_i
=B_jr_i-B_ir_j
=\sum_{\ell=1}^7(B_j\tau_{i\ell}-B_i\tau_{j\ell})F_\ell .
\tag{8}
$$

这保留同一个 $\lambda$，不是两个不同根的投影。

源先清七个实际乘子的旧已付纯权分母，再约去**全部七乘子**的共同因子，并直接重新计算、完整返回新七原组合。两个共同因子的实际 profile 都是一项纯 $u$ 多项式，总次数分别为 2、1；即非零有理倍的 $u^2$、$u$。后续只清真正旧分母与剥旧已付支持。没有从一个原标量方程上直接除未知因子。

实际所得两个非零原必要多项式记为 $S_3(u,\nu,t)$、$S_4(u,\nu,t)$：

| 固定原对 | $(u,\nu,t)$ 次数 | 总次数 | 项数 | 定义字节数 | SHA256 |
|---|---|---:|---:|---:|---|
| $(q_2,N_1)$，$S_3$ | $(30,34,3)$ | 49 | 3343 | 104851 | 7f8a07414ed070761193bf4512239422597624bd11cd1b8b22d531b3400d2d9a |
| $(q_2,NS)$，$S_4$ | $(47,53,4)$ | 76 | 10127 | 395909 | d4504c2e3fc58dfe2708bfac12839b38a5effc01484ce1e3edfc98801299ebae |

对应完整原身份是

$$
\boxed{
S_3=\sum_{\ell=1}^7\Omega_{3\ell}F_\ell,\qquad
S_4=\sum_{\ell=1}^7\Omega_{4\ell}F_\ell,
\qquad \Omega_{j\ell}\in A_W[\lambda,t].
}
\tag{9}
$$

源末直接在原七式上返回 (9)，不是只核两个余式坐标。

实际旧支持剥除按 gcd 层数记录：

| 新标量 | $u$ | $u-1$ | 本 b0 已付 $A_*$ |
|---|---:|---:|---:|
| $S_3$ | 2 | 1 | 0 |
| $S_4$ | 3 | 1 | 1 |

这些是算法的逐次 gcd 层数，不冒称整个复合因子的幂。所有已约共同内容零纤维仍由新的完整 (9) 保留；其余未知纯权内容和两个 $t$ 首项的整个零面均未删除。

此次没有对 $S_3,S_4$ 再取结果式、因式分解或多变量 gcd，没有因此得到新的纯权覆盖或排空结论。原 PS 行虽然不参与这两对固定标量，仍完整保留在十二/十四行模型中。

## 5. 唯一实际执行与小回执

- 源：[2026-11-28-unit211-W-b0-t-parameter-monic-lambda-two-complete-I6-q2-two-original-targets-8542.py](../notes/2026-11-28-unit211-W-b0-t-parameter-monic-lambda-two-complete-I6-q2-two-original-targets-8542.py)。
- 输入：[同源输入说明](../notes/2026-11-28-unit211-W-b0-t-parameter-monic-lambda-two-complete-I6-q2-two-original-targets-8542-input.md)。
- 实际回执：[同源 execution.json](../notes/2026-11-28-unit211-W-b0-t-parameter-monic-lambda-two-complete-I6-q2-two-original-targets-8542-execution.json)。
- 源 blob：2f7fd85b7345f8c41747669526ffcf88d9b83acc，16151 字节。
- 源 SHA256：4e6ac873561f4c65491899d2f5edac279e7e44b10057cd86cc9991cbec3bb402。
- 唯一实际运行：[run 46149157665 / job 140991679671](https://github.com/Rogerhu12/math-research-public/actions/runs/46149157665/job/140991679671)。
- 源提交及实际 pull：0b65eec6c741db5c03f663ff2c4856258307f3dd，2026-11-28 13:20:59.815616 UTC；两份 README 无变化。
- 固定源预算 180 秒 / 4 GiB，外驱动 195 秒；自含、零依赖。
- 实际驱动 4.932428614 秒，最大子进程 RSS 91468 KiB，源 exit 0。
- 五个完整数学标记依次为：0.112802871 秒首一二次；3.113863602 秒完整十二/十四行；3.297447022 秒 $S_3$；4.827796256 秒 $S_4$；4.874627711 秒完整结束。
- stdout 11759 字节，SHA256 533442a7deae4d14523104f88deea0debd04af9af0ad6c8749a33d3f50bdf26d。

实际统计：2227 次多项式精确除法乘回、130 个已付分母检查、9 个新头逆坐标、28 次完整降次返回、14 个两坐标行、8 次新原 cofactor 返回。原几何与矩式也按源码逐项返回。

本次没有重播任何旧门或提高预算；未输出或保存上表大多项式的系数载荷、矩阵缓存或编码片。原源、参数定义、所有五个小数学记录和驱动回执完整保留。本文所有空间与点的范围仍是明确规范比值/Gram 坐标，没有另加 $U_0$ 三次尺度或未规范化对象计数。
