# R824 实际原极模块分裂：28条权五和244条权六

2026-11-15。状态：**已证明并由旧公开原计算的真实非零子式认证；没有重新计算任何矩阵、秩或 Laurent 系数。** 原完整函数 A/B 的有理重构仍未因此完成。

## 1. 实际结论

保留原 $p=41$、$Y_L$、$H$、$y=y_{f_4}$ 和 $E=(y)_\infty$。
本条从旧 R787 已完成的原 Schur 非零子式，认证
$$
\boxed{h^0(Y_L,5H-E)=28,\qquad h^1(Y_L,5H-E)=0.}
\tag{824R.1}
$$
所以 [R824原完整证明](R824-original-pole-module-generators-in-weights-five-to-seven.md)中的实际分裂型为
$$
\boxed{\pi_*\mathcal O_Y(-E)
\simeq\mathcal O(-5)^{28}\oplus\mathcal O(-6)^{244}.}
\tag{824R.2}
$$
相应完整分次模是 $S(-5)^{28}\oplus S(-6)^{244}$，$S=L[\tau,\sigma]$。
因此完整原极模块需要272条自由生成元，其中28条权五、244条权六；没有权七生成元。
这确定的是实际维数与分裂型，尚未给出那272对准确截面的坐标。

## 2. 实际非零见证

消费旧原 run [43683912711](https://github.com/Rogerhu12/math-research-public/actions/runs/43683912711) 的已经完成阶段。
source commit 为 `eab5e58bbf951c48ccf13a109bbdf0b0289a6f23`，原数学核心 SHA256 为
`93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04`。

| 原实际量 | 数值 |
|---|---:|
| 辅助素数 ell | 1000000753 |
| 原 L 约化分支 | 0 |
| 原积分模型 B=lambda*b 的根 | 3197390 |
| 原 s=sqrt(-3) 的根 | 99932770 |
| 原常数项20阶子式 determinant mod ell | 322380492 |
| 原 A 的1234阶子式 determinant mod ell | 336446771 |
| 原 Schur 矩阵形状 | 1326 × 1214 |
| 真实完成的 Schur 秩 | 1186 |
| 所选 Schur 子式阶数 | 1186 |
| 所选 Schur determinant mod ell | 296007862 |
| 正在原 R787 重构的自由列 | 1186 |

上述三个 determinant 都是原已成产物中的真实非零值。
原 selection 阶段准确验证了素性、原积分 $B$ 多项式的七个不同根、$s^2+3$ 的两个不同根、全部十四分支的可逆评价矩阵、原有理分母为单位，以及原 $\kappa$ 在每个分支的可逆性。branch0 的根及 chart SHA 与这些原记录完全相符。

这里的 $B=\lambda b$ 只是原 R781/R787 的积分域坐标；原目标 $C:y^2=x^3+b$、正 CM 方向、$\lambda$ 与 $246^3$ 未改。不能将表中的积分 $B$ 根误作原 $b$ 的根。

## 3. 为什么一个原约化子式已确定特征零维数

原 $V_5$ 的维数为1234。原 cusp 的 $y$ 有简单极，原 R787 先用常数项的20阶满秩约束去掉 $B$ 在 cusp 的不合法值；其准确有理零空间写成 $B=Zc$，其中 $c$ 有1214个原 $L$ 坐标。

原 rational-blocks 阶段保留20个主元列、1214个自由列，并已准确验证 $E_0Z=0$。表中的20阶 determinant 非零且其分母在 ell 可约化，故该参数化没有丢掉一个合法特征零方向。

给定 $c$ 后，原 $A$ 由1234个独立展开行唯一确定。表中的1234阶 determinant 非零，保证该消元在所用约化中合法。剩余1326行组成同一原 $1326\times1214$ 的 Schur 系统 $Sc=0$。

原完整129阶、每阶20个 $L$ 坐标的 Laurent 判据与 R824(824.19–22)一致，故其特征零核恰为 $H^0(5H-E)$：每个核向量给唯一原 $A=yB$，反过来每个这样的 $B$ 都落入该核。因此
$$
\operatorname{rank}_L S=1214-r,
\qquad r=h^0(5H-E).
\tag{824R.3}
$$

真实原约化中的1186阶 determinant 为296007862，且所有消元分母在该分支为单位。因此同一个子式在原特征零 $L$ 中非零，给
$$
\operatorname{rank}_L S\ge1186,\qquad r\le28.
$$
另一方面，原 $\deg(5H-E)=154$、$g(Y)=127$，Riemann--Roch 已给
$$
r=28+h^1(5H-E)\ge28.
$$
两者合并得到(824R.1)，再代入 R824 的完整 Koszul/自由模定理得到(824R.2)。

只要一个真实、合法、源已绑定的约化分支给非零子式，就足以证明上述特征零下界；这里不需要把十四个分支当十四个新维数证明。原 R787 和后继重构整个 $L$ 坐标时仍须保全部十四分支，不能由本条删除它们。

## 4. 本次只读核验的准确范围

原 artifact14159006977 的登记长度为5148711108字节，原登记 ZIP SHA256 为
`32652fdbb99ef41340bffb4ba1c9d1a56479de346c999f723023db2e1427645f`。
本次用 HTTP Range 读取 ZIP 索引和必要成员，没有下载或重新哈希整个5.15GB archive。
安全边界是已经登记的完整 manifest：440819字节、1517项，SHA256
`613f436b2c398cdcd5c9a92c4eb47e72bc81f8d0e8395322eff6455c89c0821c`。
该 manifest 的实际原字节及其 SHA 已重新核对，随后以下七个原成员逐bytes/SHA核对。

| 原成员 | 字节数 | SHA256 |
|---|---:|---|
| R787-prime-1000000753-branch-00.json.gz | 14466056 | c5b75f48b5c5d1cf2d98390e814a245306fa63f10ae43dae194dbfd560d895d7 |
| R787-prime-1000000753-chart.json.gz | 5829 | 47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96 |
| R787-prime-1000000753-rational-blocks.json.gz | 9169464 | fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b |
| R787-prime-1000000753-selection.json.gz | 5759 | a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb |
| core-receipt.json | 308 | ec4673e2b51e4b3e47b2fbea4ac75c34c7923e90d47ab3f80110cf35f426e8f7 |
| public-actions-input.json | 5895 | 500ed43dc256e16fa068e9e02f33c1b80ad2f9d864ba761ed2cbad7465387a03 |
| run-receipt.json | 542 | 09bf889dccc65e6894ce7e86ced1f207f79fa258284307869658411e1c2e619d |

chart、selection、rational-blocks 和 branch0 的数学配置完全相同；原source、run、core和各阶段 SHA 链一致。两个逆矩阵的原记录、主元/自由列尺寸、真实非零 determinant、原分支和完整已核行标志均已读。没有import原数学core/flint、重新求逆、重新求秩或重新代入矩阵。

第一次小索引读取传输238947字节；补足见证及source回执的一次读取传输23871840字节。只读摘要30871字节，SHA256 `4a16cfdade365eaec7028c119c80873c624f364f2bc51db857512a1c063d5bd3`；只读脚本 SHA256 `6355538356c5f985cb8f0d6cf63e2ceaed5d805131cbeee21f62ebea718c4d60`。本地原件和机器摘要不进Git或Release。

原 run 最终在2026-11-15 11:06:48 UTC停止于预算，run-receipt的complete=false、actual_y_map_recovered=false；其已经完成的 modular 阶段独立保留。这里没有把这次完整运行称为success，也没有声称一条特征零 A/B 已从其失败状态恢复。

## 5. 实际后继的缩小

完整极模块消费者现可固定为28条权五和244条权六。原 R787 正在处理的自由列1186继续由其原任务交付，后继只新增其余27条权五方向，并只提升244条真正模补方向；不先恢复300条权六全核。

所需最高原 Laurent 界为 N=142。原 R781 已完成 R0至R142，故不新增 R143至R155、kappa156 或任何 H³尾；当前 R787 的输入carrier只选择了 R0至R129，缺失的旧 R130至R142必须从仍活跃的原 R781 产物补入，不能重新计算。

每一候选仍须在全部20×14原坐标准确认证 A=yB，并取得 R824 所需的真实纤维满秩见证。原normal基、两图运输、最终理想、eta主函数和规范高度尚未由(824R.1–2)得到。正在运行的 R787/R809 不因本条重启或改核；主目标仍OPEN。
