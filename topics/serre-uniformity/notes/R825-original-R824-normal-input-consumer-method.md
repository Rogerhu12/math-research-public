# R825 来源接续：R824 原关系的 A/B normal 向量与冻结导数算术

日期：2026-11-15。状态：来源适配草稿；没有本接续的实际导数输出。

本稿引用原
[R825 对数比值与重数证明](../results/R825-original-logarithmic-ratio-and-multiplicity-preimages.md)、
[R824 原准确关系适配](R824-original-exact-relation-adapter-to-beta-consumers.md)、
[R809 A/B 专用 normal 消费者](R809-original-A-B-normal-consumer-from-R824-method.md)。
本接口不改变原 R825 证明、算术核心或已经冻结的来源。

## 1. 真实输入的划分

新 R809 A/B 专用 producer 的 RESULT 为
`R809-original-A-B-normal-coordinates-from-R824`。
它保留新原关系 $A=yB$ 的真实 R824 run、stage、free column，
并把该对截面准确转换到原 S5 的正常基。
旧 R809 C0 至 C5 成功 producer 仍独立提供 S5 index；
旧 producer 从未被宣称已算出 A/B。

新 consumer 用四个逻辑来源：

| 目录 | 真实 producer | 只读的必需内容 |
|---|---|---|
| R809 | 新 R824-origin A/B normal 成功 | A/B 两 index、四组准确坐标与真实来源回执 |
| R809_basis | 原 C0 至 C5 normal 成功 | 原 S5 index、minor/rank 及原基规范 |
| R815 | 原正常导数算子成功 | 原 $M_g,\Gamma$ 两图全部准确行块 |
| R820 | 原 cusp 理想成功 | 两图原 Hermite 列与准确 cusp 有限代数 |

每组仍保留其独立 manifest、core、run、certificate 与 configuration。
新 A/B 证书中的 S5 index 是对旧 producer 的外部引用。
不得替它生成新 tag 的复制品，或以旧 C-only 成功证书顶替新 A/B。

## 2. 相同比值与导数的依据

新 pair 和旧 R787 预留 pair 都满足原 $A=yB$、$B\ne0$，
不必是常数倍。
无论换成何种相同次数的真实 pair，
在原函数域中均有

$$
\delta y=\frac{B\,\delta A-A\,\delta B}{B^2}.
$$

若另一 pair 为 $(cA,cB)$，乘法法则中的 $\delta c$ 两项准确相消。
本接续并不先求 $c$，也不在输入前约去共同因子。

新 producer 已把 $B_{\mathrm{fld}}=\lambda b$ 的原字段转换完成。
本接续继续读
$b^0,\ldots,b^6,sb^0,\ldots,sb^6$，$s=1+2\zeta$。
坐标仍为 `numerator / column_denominator × original_target_rational_scale`；
只施加一次这一个真实有理尺度，
不重新插入 R824 已移除的共同 denominator/content，
不另乘 $\lambda$、$\zeta$、$s$ 或 82 的幂。

S5 的 1234 行从旧 index 读出，
逐行核 $a$ 外层、$j=0,\ldots,5-\epsilon_a$ 内层，
$\epsilon=(0,1^{144},2^{127})$。
旧基文件保持其真实旧 configuration。

## 3. 算术全部使用原冻结方法

新的小核心只覆写原 R825 的来源初始化、
新结果身份和来源回执；原以下方法直接继承：

- 原 28 个有理字段分量的读取、零判断与一次尺度应用；
- $\delta v=\Gamma v+M_gv'$ 的准确卷积；
- 同一原 derivation 在两图的运输与额外齐次项；
- 原 cusp Hermite 基的准确坐标转换；
- 全部逐系数代回和原有完成 stage 复用。

原输入 degree 5、derivative weighted bound 7、
regular $g$ product weighted bound 8 不变。
新任务只消费真实 R815 / R820 已成产物，
不重新算 $M_g,\Gamma$、cusp 代数、normal basis 或 Fourier 前缀。

独立 RESULT 为
`R825-original-normal-derivatives-from-R824-normal-vectors`，
FINAL 为
`p41-original-normal-derivatives-from-R824-certificate.json`。
CLI 继续
`--config --proof --method --retained --output --budget-minutes`。
原 `R825_original_normal_derivative_inputs.py` 不修改，
由新 subclass 按冻结 SHA 导入。

## 4. 输出与实际完成边界

成功后输出的是这对真实 A/B 的原正常导数向量、
原第二图过渡证书和原 cusp 坐标；
同时保留实际 R824 关系身份和外部 S5 身份。

即便本阶段成功，也不把以下对象称为已算：

- 原 $P,Q$ 的完整乘法矩阵；
- 全局极理想或 $D$；
- 原 $\eta$、主函数、刚性化与高度。

原 R825 后继公式仍可以消费这些真实向量；
相同比值的论证只保证原函数与导数身份，
不自动提供缺失的乘法矩阵、理想运算或高度规范。

## 5. 公开 IO 与续接

首次只提取所需原文件并按原 manifest 核 bytes/SHA，
将四组最小来源放入自己的一日 carrier；
不重新读取旧 S5 的全部 q 行。
同核续算保留所有已经完成的 R825 stage，
保持真实 producer 身份、source/target tags 和原模型。

runner 的 verifier 只进行来源、schema 与 bytes/SHA 核对，
不 import 数学核心。
外层时限为预算加 900 秒，并保留终止宽限、
退出码 124、最终 manifest 与一日上传。
所有新算术只在本公开仓库 Actions 内执行。

未知新 A/B 或 R815 成功产物继续显式 pending；
本方法没有填造任何 producer 或实际导数值。
