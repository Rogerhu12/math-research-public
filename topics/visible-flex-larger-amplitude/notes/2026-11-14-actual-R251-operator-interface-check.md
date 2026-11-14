# 2026-11-14：R251 三解析场接口的真实 Actions 回执

状态：**compile/import 与三个指定解析场核验实际通过**。没有修改数值源，没有追加更多测试，也没有把这些构造例登记为本课题候选。完整 scalar 包络、实际接受场的全 prefix 与闭曲面仍未由本次运行验证。

## 1. 运行与原件

- 公开仓库 run：`43597596523`，attempt `1`。
- source commit：`89b0882ce3bd7057642da944a6163e3da6c18fc2`。
- 实际 job：`132455364296`（`Mainline operatorcheck`），结论 `success`。
- 编译和三个解析例 step 成功；公开 publisher 也成功，在实际非快进后反复 rebase/push，最终推进到日志中的 `9eee945`。
- artifact：`14115152863`，`visible-mainline-operatorcheck-43597596523-1`，ZIP 为 8,135 bytes，SHA256 `512c22aac5bf30bb252de7041122dcbb83f6d18f4c222a183f3f83bbe4b3a34a`。
- 真实报告：[operator-interface.json](public-actions-43597596523-1-operatorcheck/operator-interface.json)，59,634 bytes，SHA256 `b5c39076de5be6efe50e35f6e29b3dca9bd757838f048699d19674c1477fa65c`；[publication.json](public-actions-43597596523-1-operatorcheck/publication.json) 保存相同原件身份。

运行采用 `python-flint 0.9.0`、160-bit Arb 工作精度。日志与报告均记 `passed=true`、`completed_cases=3`；实际接口运行耗时 `0.13164894099999458` 秒。这只是三个 M=1 解析场的实测成本，不外推为 M112 或完整 prefix 的耗时。

报告中的三个源码 SHA 与此前交付完全一致：

| 源 | SHA256 |
|---|---|
| 单 cell 原语 | `1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce` |
| full-prefix / scalar exporter | `a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703` |
| 三解析场接口 | `ae58f455992523327991a784bb935012121be3850bc0da33bb40f46c197f389f` |

源与接口定义见 [可执行消费者说明](2026-11-14-R251-full-prefix-operator-consumer.md)；四正性定理为 [R251](../results/R251-direct-relative-operator-metric-certificate.md)。

## 2. 圆柱的全 cell 正性

第一例的精确输入为 M=1、完整 core c=0、a=2、R=2、T=0、Z=s，物理单元为 `[0,1]`，eta=10⁻⁶。其完整高度均值不能删除，否则 E=1 的预期不会成立。

独立解析值 E=1、B=0、C=4 被实际严格球包含。`Uplus/Uminus` 的全部 9 个径向 Bernstein 控制函数均通过全角核定，`Dplus/Dminus` 的全部 19 个也通过。四量对应 eta、eta、4eta²、4eta²；两个行列式的实际最坏下界均在 `4e-12` 附近，保持严格正性。程序没有产生失败点。

这些输出验证了完整 z0、旋转框架角导数、`JT=iT` 和 `JB=iB` 的符号、径向 Bernstein 运算以及本次数值路径的全角核定。

## 3. 高度斜率错误的真实失败点

第二例只把 Z 改为 `(101/100)s`，其 E 为 `10201/10000`。实际 Uplus 球包含

$$
1+10^{-6}-(101/100)^2=-0.020099
$$

且其上端点严格为负。程序报告 s=1/2、phi=0 的真实点失败，`uses_actual_scalar_value=true`、`uses_a_Bernstein_control_as_a_point=false`。因此这个失败不是由粗 Bernstein 控制值或未经证明的 scalar 包络代替实际点。

## 4. Mixed term 主导的失败

第三例为

$$
R=2,\qquad T=(s/10000)\sin(2\phi),\qquad Z=s.
$$

在真实点 s=1/2、phi=pi/4，独立解析微分给出

$$
E=1+10^{-8},\qquad B=2\cdot10^{-4},
\qquad C=4+2.5\cdot10^{-9}.
$$

所以两个归一化对角误差分别是 `1/100000000` 与 `1/1600000000`，都小于 eta；归一化 mixed entry 为 `1/10000`，大于 eta。

实际严格球同时包含以下有理预期，并核出相应符号：

| 函数 | 实际报告所包含的值 | 符号 |
|---|---:|---|
| Uplus | `9.9e-7` | 严格正 |
| Uminus | `1.01e-6` | 严格正 |
| Dplus | `-3.9996042475e-8` | 严格负 |
| Dminus | `-3.9995957475e-8` | 严格负 |

两个第一主元还通过了整个 cell 的全角正性检查，最坏下界分别约 `9.8997590428613e-7`、`9.9997590428613e-7`。因此本例实际检验了“只看两个对角项会漏掉 mixed term”的接口风险。

pi/4 处另用精确四次单位根取完整 Laurent 点值，并与 Arb/Bluestein 路径独立比较。两个路径都包含预期值。通用失败点搜索首先在 phi=0 捕到另一真实 Dplus 负值；报告另存的 pi/4 结果才是上述 mixed 主导见证，二者没有混为一处。

## 5. 实际验证边界

原 scalar 余项所需的 `arb_series.sin` 六个已知 Taylor 系数 API 也通过，报告逐项保留严格球。但本次没有实际执行 AngleConnector / terminal bridge 的 48/64 点 finite-Gauss 包络，也没有调用真实完整 v3/v4 接受场的 reader 或验证其全 prefix。

因此此次结论是：故障后重建源码已真实编译和导入，单 cell 算子核心按三个指定解析预期运行，包括两个正确失败。现在无须修源或重复这三个例子。后续应直接消费真正接受的完整场，或处理具体尚未核验的同源 scalar 接口；不能把该接口成功记成课题完成标准 4 已满足。
