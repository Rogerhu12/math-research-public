# R787 原清转置第二次启动：eZ 原标签与已成配对继承

## 实际结束与问题位置

公开 run [43787626643](https://github.com/Rogerhu12/math-research-public/actions/runs/43787626643)、compute job 133038797154，
source `1abe47786bd30a2c5f58363ce283e783d797d2c0`，
使用 core `969201b943bf7591baee92c168546b9992e59b94e1b5b1b2304732b85c052407`、
wrapper `611e8ad8670f7c2622130638d398e366d5855fe00875ed09c57d2247fa397d23`。
1481 个原输入通过；核心在 3.841081281 秒后退出，异常位置是
`exact_target` 对 eZ index 的 `exact_K_basis` 字符串断言。

真实旧 index 使用 `"1,s"`；原 power5 **block** 使用
`"1,s; s^2=-3"`。两种序列化标签须分别按原文件核定。index 的
`eZ_computed_in_characteristic_zero` 为真，38 个原 eZ block 的来源、
1214 行形状与原负号已按原字段读取。失败不是有理重构失败，也不接受或拒绝候选 q。

## 必须继承的已成数学

在异常之前，原 Frobenius 系数配对及逆已经完成（该阶段 3.782615902 秒）：

| 原阶段 | 字节 | SHA-256 |
|---|---:|---|
| R787-cleared-dual-coefficient-pairing.json.gz | 4629 | b384a33166820240d22205dd307b4d93b243b02b6dec8a7426967cc4e2072c26 |

原阶段明确记录整数幺模及完整逆恒等式成立。它是原普通系数配对，
不是迹配对或 Hermitian 配对。原配置指纹为
`a05c236e2fee6861d9361d4dda5ea78ed2bd41c6ec3499cfab3db8c85fc9e79c`。
异常使最终 core configuration/new-digits 留空，不能因此丢弃这个原已成阶段。

新核心通过独立 `completed_pairing_source` 精确引用该阶段；
**保持其原字节、原配置及原 core SHA，不重算 J/Jinverse，也不改写旧 tag。**
新源审计把它列为外部 PAIRING 来源，与本次新阶段清单分离。
继承时绑定失败 run/source/manifest、六份原文件、原 1481 输入闭包、
原 g20 模数及 20×20 形状，并核对原完整阶段的已成恒等式标志。
新的 tag 除新增这一外源引用、core SHA 外，与原配对来源的数学身份逐项相容。

## 唯一修正及后继范围

新 core `bad9741493b550b0d3543ec953642c2b2f11f30da4433c9346f0c3215d415323`
（62723B）精确适配 index 标签，并消费旧完成配对；新 wrapper
`5388274c6425e66e6c3d2d8d1d41b5a4a59f7787479695970ede670e0091b32f`
（41592B）保六件独立外源及其最小载体。原证明和方法不变。

新 dual 仍从一位起；旧 primal 的 518 位不是新 dual 精度。
Θ 算子、正 κ 幂、原 14 支逆、Dixon 残差除法、严格 RR、全部 35840 个
有理系数的准确乘回及 Δ 判定公式均未改变。只有准确通过 Θχ 目标后，
才可用 d(A0−qB0)=−Δ 接受 q 或准确拒绝 q；错误 RR 向量不能拒绝 q。

## 来源留存与纯 IO

失败 run 的一日 artifact：

- id `14190707821`，`serre-global-R787-cleared-dual-CM-value-43787626643-1`；
  ZIP 332476787B / `674026f6d746e6324a2ad43b90ed32d6fee7e8efbbf6d3a63c95e638d2132487`。
- manifest 1056B / `f9c75b8338aa38a82e3665f9f8bc4529cdcf240ff670401e9fe5f3ab3685384e`，7 个成员。
- core receipt 477B / `34a53f739a3fcd69b0debd066dd64a2b9ba3b0d4951be42eb646d7049e572745`。
- 六件 PAIRING 来源清单指纹
  `4c48efc28ef586aec57fc7dbf9047586c1ca3c69f8bd3db0575b42123387ec73`；
  最小载体 247565B /
  `17045c3e2c0fd4632da9e9b3375632719a77b16a23ba38a64c8573f7e41e1f03`。

读取只取旧小文件，不为继承 J 下载 331MB 原大载体。六件原 SHA、1481
原源及 carrier 往返均为 IO；未在本地导入数学核心或执行新算术。
全部机器输出仍只在一日 Actions artifact，Git 只保存方法、代码、参数与本说明。
主目标、A.1、原刚性化和高度均未因本次修复完成。
