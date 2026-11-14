# M12 共同闭图与 closed-budget-v2 的独立组合审查

2026-11-09，Astra-visible-flex-db6f0b0e / independent_geometry。

**PASS：新增绑定与组合逻辑、沿用的几何不等式及轻量有理账本重放。** 本稿不复用旧 M8 图的扰动界，不把新 M12 的完整尾部 metric/curvature 提前算作已付，也不支付 G5。

## 1. 冻结输入

- `scripts/db6f-root-closed-budget-v2.py`：`0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641`。
- `scripts/db6f-root-common-cut-v2.py`：`317e519fda8d78fb70b53f8a8c80d51599dec1ac46e92741cd9b2576a3f4fa7d`。
- M12 闭图定义 `2026-11-09-db6f-root-flat17-common-cut-m12s64.json`：`1fa6c8de825be71b90308e72be166dcc7ee6ae7983456d244d2c5609e3d19858`。
- M12 uniform 尾 manifest：`b202b47177bab7491b3bd237c599b7feb7d709828275b3579acd3846a90e7540`。

背景转移使用已独审的35aa8251版本。本稿与同日 R18 的 M8 组合审查是两个不同的对象记录；以下全部实际前缀、一阶尾界与矩输入均绑定 M12。

## 2. v2 新增的背景绑定

完整 diff 表明支撑、直径、held 见证、矩误差与精确前缀 metric 转移的 Fraction 公式没有变化。v2 仅允许在数值 checkpoint 改变时，通过已审 same-background transfer 证明背景引理仍可使用。

新增路径要求高度证明与正 alpha 证明具有同一原 checkpoint；要求 transfer 已完成且当前实现哈希相同；其旧 manifest 的 checkpoint 必须等于背景证明 checkpoint，新 manifest 必须等于本次实际有限尾。然后重新读取两个 manifest 的精确物理网格，核相同端点；对参数字典作并集比较，任何不在已审 numerical whitelist 内的差异均拒绝，还要求实际变化清单与 transfer 的清单完全一致。源 checkpoint 的 hash 再次检查。

这些 guard 在本次输入中足以支持复用同一个解析背景的高度和正归一结论。它没有把新有限扰动的 V、Vr 或 J 界拿旧报告代替：`tail-first` 的 manifest hash 必须等于这个 M12 图的尾 manifest。新的 M12 一阶报告确为本对象重算。

同 g 白名单的含义已经在 transfer 独审中从构造代码核对；特别是 physicalDepth 是固定 protect160 背景的数值截断，并非重新定义物理源。calibrationSteps 与全部物理控制字段仍必须相同。

## 3. 共同端迹 v2 的接口

独立审读 v1/v2 差异：唯一数学表示仍是已有的公共五次修正。新增 `validate_tail` 精确核查正径向增量、归一比例与外锚，要求 cuff<inner<outer 且 outer 等于物理 cut 和精确桥 cut；带符号平面模和高度模的完整频率条件亦受检查。

`Y=I(old.copy(),old.copy())` 取消了上下端点数组的别名。旧 v1 的最终结果已有覆盖顺序证明，本改动使新版本不再依赖该临时别名；没有改动完整高度反射、k/λ/k₂ 变换、R/T 符号或修正基函数。

coupled_prefix 已用独立 Fraction 积分全部18,457跨×141尾系数，并独立检查582个端迹修正区间；其报告为 `2026-11-09-db6f-prefix-review-common-cut-v2-m12.md`。该作者参与过原优化，所以这份组件检查不被本稿改称为最终未参与者的全流程重放。我在此核新接口及绑定；更广范围的最终重跑仍单列。

## 4. 闭图组合与独立账本重放

M12 图仍由两份镜像修正前缀、整体高度反射的显式尾及其 R6 collar、同一固定帽组成。其目标背景未变，帽也未变；切口高度按新图积分均值重新定位，一阶扰动、实际前缀几何和镜像矩全部取新报告。因此已审全相位与支撑嵌入论证可再次使用，并不要求两个不同有限图彼此全等。

从 root M12 报告读取它保存的全部输入路径及同背景 transfer 路径，独立运行 v2 到新文件 `2026-11-09-db6f-audit-closed-budget-m12-replay.json`。**全部 JSON 字段与原报告相同**，包括精确有理数和全部输入 hash。所得安全结论为：

| 项目 | M12 uniform 闭图界 |
|---|---:|
| 全相位全域正支撑 | >0.7370435198976693 |
| 完整初始直径 | ≤3.92 |
| held 位移/完整直径 | >0.0509926386289832 |
| 未标记实体三阶水平矩 | >0.4401644538269835 |
| 精确目标前缀 metric 误差 | <2.572118833×10⁻⁸ |

正三阶矩与固定帽的显式正矩仍给全 E(3) 的严格非全等。它不依赖尚未取得的这个新图的定量 reach；正支撑的全相位闭嵌入和加帽过程已经足以使用体积矩增量论证。

## 5. 尚未转移的结论

上述对象是 M12 uniform 图；新的 critical 网格还须另生成共同端迹、前缀修正与相应预算。背景包可以精确换网格，并不意味着有限几何证书也能换网格。

新 M12 全尾 metric/实际曲率和完整 reach、各项最终组件的未参与者完整数值重跑、G5 与网格交付均不由本轻量组合审查代付。机器记录见 `2026-11-09-db6f-audit-closed-budget-v2-m12.json`。
