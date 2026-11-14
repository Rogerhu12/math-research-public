# 同一有限图的独立 metric 与曲率证书合并

状态：**以下条件组合证明完整；新 v2 实现待独立审查。** 旧冻结汇总器
和 R18 的所有依赖保持不动。此记录不支付 G5。

## 1. 条件引理

设 F 是一个指定的有限 C² 图，g 是一个指定的正定目标度量。若两份
完整证书分别给

$$
\sup\|g^{-1/2}(F^*e-g)g^{-1/2}\|_{op}\le\epsilon_1,
\qquad
\sup\|g^{-1/2}(F^*e-g)g^{-1/2}\|_{op}\le\epsilon_2,
$$

则同一个 supremum 不超过 $\min(\epsilon_1,\epsilon_2)$。若另有
实际主曲率绝对值上界 K，该结论继续成立；重新估计 metric 不会改变
F 的欧氏主曲率。原 K 的证明即便曾使用较粗的 $\epsilon_1$，也仍是
正确的上界，无须把原推导中的每个中间项换成新值。

因此可以保留旧完整曲率证书，只把更紧的完整 metric 证书用于最终
分块最大值。这里没有从新 w 多项式求导得到 w_r，也没有把两张不同
的有限图拼成一个报告。

## 2. 数据绑定与实现

`scripts/db6f-root-whole-metric-reach-v2.py`，SHA256
`20d9b6127625595afaf14daac4d23ccdd68d10f5d3a36d0697472f5df50d8fc3`，
保留冻结 v1 的全部闭图检查与 Fraction 几何预算。新增可选参数
`--tail-metric-certificate` 后，仅增加以下前提核查：

- 两份报告绑定同一个 finite-tail manifest，且新 manifest 的实际文件
  哈希再次核实；
- 新完整包、数据和逐盒报告的哈希匹配，有限尾及自身 R6 collar 全覆盖；
- 全部旧/新 `background_definition_hashes` 非空且完全相同；因此使用
  同一冻结校准、source 和精确积分参数的数学定义。primitive 的数值
  分割深度可以不同，它不改变被包围的函数；
- 重新逐行检查新 metric 报告的行数、连续包行编号、全部 span 出现、
  非负有限误差值及全局最大值；
- 新报告只改变最终 metric 上界选择，旧曲率报告及其行数据原封不动。

新证明仍依赖 supplier 包含性和 metric-only 算法的独立审查；哈希与
状态字段本身不是数学证明。当前 point-Lipschitz、cap C4 和一阶 phase
供应方法已有各自的完整证明、独审和实际复跑，完整新包仍由后端另算。

## 3. 已完成的真实证书回归

用同一 M8/R18 的完整旧曲率报告，以及已独立重跑的 5237 行 metric-only
报告运行 v2，实际 exit0。新增路径重新核查全部 5237 行；13 个保存
的精确 Fraction 标量字段与原 R18 汇总逐项相同。记录为
`db6f-root-whole-v2-m8-regression.json/.log`。这只验证新增组合接口在
真实已审输入上的兼容性；不把作者回归当作 v2 独立审稿。

## 4. M12 critical 第一档的现有完整界

同图闭账本 `db6f-root-closed-budget-m12-critical-r01.json` 已获独立
全字段复跑。对应的完整尾报告
`db6f-audit-tail-m12-critical-tight-full.json` 使用 manifest
`cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`，
29,023 个包行全部完成且曲率全部 resolved。旧冻结汇总器在这些新图
输入上实际运行给：

$$
\epsilon\le9.93630067500459\cdot10^{-7},\qquad
K\le8.462559071292288,
$$

其中上界按报告保存的 binary64 数解释。支撑、直径、固定 H、非全等
和相位作用使用该图自身已审的公共接缝与闭账本，再按 R10 得

$$
\frac{\operatorname{reach}}D
\ge\frac{1407374883553280}{46687172903089131}
>0.0301447870162247.
$$

原报告为 `db6f-root-whole-metric-reach-m12-critical-r01.json`。这是把
R17 的已审构造和 R18 的已审组合论证应用于新输入，未借用 M8 的实际
尾图数值。当前较粗 metric 上界主要受背景包精度影响；新的完整低 w
后端尚在运行，其结果不在这里预先填入。
