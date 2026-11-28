# R150：h=k、Delta=0 的整个条件 C4 原纤维排除（旧全支排空撤回）

> **2026-11-28 依赖更正：** 本页整个 Delta=0 排除依赖已撤回的 578 次/七个 lambda 覆盖，因此全支排除撤回。固定 C1、C2、C4 条件下直接来自正确 Gram 的返回只按各自条件保留；不能合成全 Delta=0 排空。 参见[原定义与依赖隔离](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md)。

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

**当前保留结论。** 在原 unit211 非零孤立均值图中，附加 C4(lambda)=0 的整个 h=k、Delta=0 条件纤维没有原解。该完整十二维常数代数已返回全部八条真原 Gram 条件；同一个自由 f 下，原 E1 与 EBe 的完整多项式 Bézout 组合为1。

这只关闭附加 C4 条件；不关闭整个 Delta 零面。当前正确剩余覆盖见[三个小因子及4788界](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)。h=k、Delta 非零及其他 R150/R271 接口仍继续；普通复可分无限维 Hilbert ISP 尚未完成。

## 1. 完整参数覆盖与此前已经关闭的纤维

原碰撞矩条件给
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,\quad h=k=1+\xi.
$$
这里 A、B 是已付原单位；h=k=1 的原退化情形此前已经排除。

[完整 Pf 静审](../notes/2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)已独立支付整个当前碰撞图的 Pf；在 Delta=0 上，Phi·NF=S·xi·Pf 又直接支付 Phi。旧578次/七 lambda 全覆盖撤回，下面三个条件不得宣称穷尽 Delta 零原点：
$$
C_1=\lambda-\tfrac13,\qquad
C_2=\lambda^2-\lambda+\tfrac13,\qquad
C_4=\lambda^4-3\lambda^3+3\lambda^2-\tfrac32\lambda+\tfrac38.
$$
本页仅处理附加 C4 条件的整个原纤维。

整个 C1 由[唯一有理原基点及自由 f Gram](R150-appendix-unit211-equal-singleton-Delta-zero-entire-lambda-one-third-exclusion.md)排空。
整个 C2 由[完整四次 u 常数域及原八 Gram](R150-appendix-unit211-equal-singleton-Delta-zero-entire-C2-lambda-exclusion.md)排空。
本次只处理附加条件 C4 的整个纤维，不重跑这些已登记输入。

## 2. 最后完整常数代数，不选择嵌入

在 K=QQ[lambda]/C4 中有 ell=1、T=xi。令
$$
S=2\xi+3-2\lambda,\quad \eta=\xi+3-2\lambda,\quad c=3-4\lambda+\xi\eta,
$$
$$
H(u)=(c+S\xi)u-2c,\qquad C(u)=2\xi u(u-1)(\xi u+2\eta).
$$
[完整 Q 图与三次 u 覆盖](R150-appendix-unit211-equal-singleton-C4-Delta-zero-complete-Q-graph-and-cubic-u-cover.md)
已在整个 K[u] 中支付
$$
\Delta=-2(u-1)(HQ+C),\qquad \gcd(H,C)=1,
$$
所以原 Delta 零面上 H 不为零，且 Q=-C/H。原同点 Tnum 条件进一步给首一
$$
g(u)=u^3+g_2u^2+g_1u+g_0=0.
$$
完整系数按 lambda 升幂为：

| 系数 | 常数 | lambda | lambda² | lambda³ |
|---|---:|---:|---:|---:|
| g0 | -1935968/377807 | -582832/377807 | 2333440/377807 | -734336/377807 |
| g1 | 86116/10211 | 82696/10211 | -151584/10211 | 33024/10211 |
| g2 | -1726012/377807 | -2265096/377807 | 2999120/377807 | -176192/377807 |

本次直接在
$$
\mathcal A=K[u]/(g)
$$
中工作。它是一个十二维 QQ 代数；没有把 g 宣称为不可约，也没有挑选 lambda 或 u 的某个复根。

在这个完整代数中，同一个 Q 的精确余式为
$$
\begin{aligned}
7Q={}&1264-3320\lambda+5664\lambda^2-2496\lambda^3\\
&+(-2008+5272\lambda-8944\lambda^2+3936\lambda^3)u\\
&+(687-1802\lambda+3040\lambda^2-1336\lambda^3)u^2.
\end{aligned}
$$
源从 -C/H 计算它，全部逆都由实际 K[u] Bézout 乘回；原 Delta 和两条相容分子均完整返回为零。若某个逆为非单位，算法保留两个精确因子并分别继续；本次实际不需要任何分裂。不存在通过丢弃某个常数分量来制造单位的步骤。

## 3. 保留同一个自由 f 的原坐标恢复

取 d=1-Q、rho²=d，保留完整二次代数，不选 rho 的符号。原孤立坐标与权为
$$
p=1+\rho,\quad q=1-\rho,\quad
b=\frac{\ell}{2}+\frac{u-\ell}{2d}\rho,\quad
c=\frac{\ell}{2}-\frac{u-\ell}{2d}\rho.
$$
令 f 为无约束多项式变量。由原 P1 定义
$$
t=-\frac{P_f f+P_c}{bc\,Q\Phi}.
$$
所有所除因子都属于此前已排空的原零面；本次完整代数上的逆另有完整 Bézout。

源逐项返回
$$
P_f f+P_c+bcQ\Phi t=0,\qquad
N_Ff+N_C+bcQS\xi t=0.
$$
没有倒置 Delta、NF 或任何 f 系数。之后由同一原 E0、N0 恢复两个原均值坐标，构造原 4×4 Gram、原迹 tau 和原乘法；原 V 的前三矩、E0、N0、P1、NV 以及 Pj 的实际目标均完整乘回。

因此后续八条多项式真正属于同一点、同一个 f 的原条件，不是把不同投影根拼接，也不是把一般 D 非零权图的条件借到碰撞图。

## 4. 全部八条原 Gram 条件与实际单位身份

源实际构造：

| 原行 | f 次数 |
|---|---:|
| E1 | 2 |
| EBe | 2 |
| EBo | 2 |
| N1 | 2 |
| NBe | 3 |
| NBo | 3 |
| PBe | 3 |
| PBo | 3 |

EBe/EBo、NBe/NBo、PBe/PBo 分别是完整 B、C 两个原式在 1,rho 上的系数；同时保留两原式和 rho 非零，使原解必须令相应两系数为零。不是仅用一个选定 rho 根下的单式强迫全部系数为零。

对同一 $\mathcal A[f]$ 中的 E1、EBe，实际多项式扩展欧几里得返回
$$
U(f)E1(f)+V(f)EBe(f)=1.
$$
每次除法都返回商、余式的完整乘积；最终两标签与两条原行的全部系数组合再次乘回 1。由于全程所用系数逆均在完整 $\mathcal A$ 中被证明是单位，这个身份在所有复点、所有 f 值处同时成立。因而整个 C4 原纤维不可能有解。

完整原行与标签的可再生证书为 26989 字节，SHA256
43717a736effeedad28bec7de3b3ca0c5c05736ef129d4ba87850423c307f762。
按仓库规则只保留源、精确输入和小回执，不另存可重算的完整系数证书。

本节仅得整个 C4 条件排除；C1/C2/C4 不能由旧错误覆盖合成全支排空。与正确十七阶覆盖合并后只剩 F99/F300，并给4788个规范点上界，见上述新整合页。此前有理 u cofactor 的120秒超时仍保留并冻结；没有重放或延长该门。

## 5. 实际执行身份

源：
[2026-11-27-unit211-equal-singleton-complete-C4-twelve-dimensional-original-Gram-8542.py](../notes/2026-11-27-unit211-equal-singleton-complete-C4-twelve-dimensional-original-Gram-8542.py)。

- blob：c52031f323be7923be2ce6328f56618d81ad2672。
- SHA256：3b4e352d11a1fefdf496f481c6e1317c72221caef9e8ab90e63d00bbb157600d。
- run/job：46033224090 / 140622042399。
- source commit：b8b8464e2750bbf9bb723e6878dd613763720fe1。
- 内层：1.906244035 秒 / 37028 KiB / exit 0。
- stdout：3104 字节，SHA256 b58d3dec620eaf099a5fc1c31ef6e244bdb3babbe8c59183125a4e13ee1a1ef7。
- 实际常数逆 14309 次、多项式除法 14207 次，全部相应乘回；八原行在 1.678 秒完成，单位组合在 1.829 秒完成。

真实 pull 在 2026-11-27 16:23:53.732931 UTC 读到 65d2065b1fe8c6a34e2850188cd7b5c0e40737ba，根与课题 README 无差异。
