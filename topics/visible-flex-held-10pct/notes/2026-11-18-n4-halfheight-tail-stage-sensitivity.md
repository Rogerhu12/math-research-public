# n4：0.5H 新失败态的高模残差与单 stage 灵敏度

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

## 原完整路径上的新定位

本条只读分析[新的 $0.5H$ 原真尾失败态](2026-11-18-n4-raw-b016-halfheight-tail-terminal.md)，
输入 SHA-256 为
`2adbe5798de593cd851268d780a3d8ac719e5564a367223551b60e650e530af2`。
原 full-Jacobian 路径重放全部 1152 stages，完整残差
$1.0124347707417067\times10^{-8}$ 与原停止值逐位相同。
原残差门仍为 $2\times10^{-9}$，没有改变任何状态或再次调用求解器。

| 位置 | 分量 | 有符号残差 | 归一化绝对残差 |
|---|---|---:|---:|
| stage 22，cell 0 / segment 7，$[.5625,.625]$ | mode 80 动量 | $+5.5138116294983774\times10^{-12}$，即 $+97$ ULP | $1.0124347707417067\times10^{-8}$ |
| stage 18，同 cell / segment，$[.8125,.875]$ | mode 80 动量 | $-5.4569682106375694\times10^{-12}$，即 $-48$ ULP | $9.509445298782182\times10^{-9}$ |

mode 76 的其它行也超过原门。这份新态的主导行已经不同于旧 $0.2H$ 输入，
不能沿用先前的单 ULP 修补标签或旧主导排序。
$\min A=.9807524169893398$ 仍在另一处发生；本次没有观察到根域退出。

## 原解析 Jacobian 的具名局部诊断

对前三个主导行及其上游邻行，用相同保存状态、相同物理 profiles、
相同 RK16 和原 `flowStateWithJacobian` 计算局部解析 Jacobian。
与 locator 重合的各行完整残差逐位一致。
总共分析 6 个具名行/分量组合，没有求解新状态。

记原行 $R_n=\Phi_n(X_{n+1})-X_n$、原归一化尺度 $s_n$。
诊断量为

$$
L_{n,j}=\frac{\max_i|\partial_{X_{n+1,j}}\Phi_{n,i}|\,
\operatorname{ulp}_+(X_{n+1,j})}{s_n}.
$$

它是保存点的**线性化输入 ULP 灵敏度**，不是对一次实际浮点改动的
非线性误差包围，也不是误差下界或不可能性证书。

| 具名行/输入分量 | 对角解析导数 | $L_{n,j}$ | 相对原门 |
|---|---:|---:|---:|
| stage 22 / mode 80 动量 | $-95.97367782317134$ | $1.2521532023729498\times10^{-9}$ | .6261 |
| stage 18 / mode 80 动量 | $-11.747860911773785$ | $4.6548183632589245\times10^{-9}$ | 2.3274 |
| stage 21 / mode 76 动量 | $-13.164579698048511$ | $5.4119548449659306\times10^{-9}$ | 2.7060 |

stage 21 的该列最大项位于同一动量分量，输入 node 22 的值为
$-1027.1155863335441$，朝正方向的 ULP 为
$2.2737367544323206\times10^{-13}$。
这些数值表明单 stage 的高模传递与原容差处在有实际影响的精度尺度。
记录中的混合单位行和不被称为坐标不变的 condition number。

## 后继试验的依据与严格范围

多行高频残差、正的根域余量、以及上述局部传递灵敏度共同说明：
值得用**只改变 shootingParts 的嵌套精化**检验单 stage 传递风险。
它们没有证明 parts32 必然改善，也没有证明当前失败完全由舍入造成。
后继若从 parts16 改为 parts32，必须保持相同 $0.5H$、原物理几何、
M20/N512、原 RK16、全部原门及完整 audit，并用原 nested remesh 作初猜。
该精化的实际接受与 metric 仍须另行记录，本条不预先认定成功。

本次没有重新运行已完成的单峰或多峰候选 screen，
也没有改变正在求解的生产源。

## 可再生来源

紧凑记录：
[`raw_primaryb016_lam002_m20_halfheight_residual_diagnosis.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_halfheight_residual_diagnosis.json)。
新增只读源
[`probe_recorded_stage_jacobian.mjs`](../scripts/resume_n4_tail/probe_recorded_stage_jacobian.mjs)
与采集源
[`record_stage_residual_diagnosis.py`](../scripts/resume_n4_tail/record_stage_residual_diagnosis.py)
保存完整输入、源码和输出 hash；原全重放仍使用已发布的 locator。
完整矩阵、状态和六行原输出只留 scratch，紧凑记录仅保留必要具名行和标量。

全重放 session 35040 于 2026-11-17 23:41:08 UTC 记录 exit 0；
局部解析导数 session 62047 于 23:42:24 UTC 记录 exit 0。
两者都是只读诊断的正常结束，不是 nonlinear DN 接受。
