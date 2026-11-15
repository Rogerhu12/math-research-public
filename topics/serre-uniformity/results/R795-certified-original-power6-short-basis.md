# R795：原普通六次幂的1506条准确短展开已完成

2026-11-15，serre-public-astra-20261115。本文登记公开仓库自己的
[run 43692029484](https://github.com/Rogerhu12/math-research-public/actions/runs/43692029484)
实际结果；输入、原配方和字段规范沿用
[R795方法](../notes/R795-exact-ordinary-power6-prefix-method.md)及
[R793原RR证明](R793-original-RR-pole-divisors-and-CM-local-algebra.md)。

## 1. 新完成的范围

准确生成原 $V_6=H^0(Y,6\mathcal L)$ 的1506条基在
$q_Y^0,\ldots,q_Y^{81}$ 的全部系数。每行沿用原R775的固定顺序和乘积配方，
公共整数尺度为

$$
82^{12}=92420056270299898187776.
$$

实际输出同时保留40个 $\xi$ 坐标，以及换参
$v=\xi^{-10}q_Y$ 后20个 $t=\xi+\xi^{-1}$ 坐标。
全部新系数逐项与原R775的模739短前缀比较，并准确检查反演不变性；
没有用平均替代下降，也没有改变原普通线丛或基点。

原已完成的1506阶模739基 minor 值为297，本次继承该准确选基见证，
不把它登记为一次新的选基计算。
由原全尖点轨道与 $20\cdot82>\deg(6\mathcal L)=1632$，
此准确前缀是固定乘法 $V_3\otimes V_3\to V_6$ 的注入目标接口。
实际乘法坐标求解仍须另行完成；本次没有计算乘法表。

本次只读取原R775的已成六次幂配方与R786的旧一次/五次幂行。
没有重算E1、M2、普通power1–5或旧Laurent，也没有生成$q_Y^{82}$以后系数。
全数学核心实际用时22.7376432秒。

## 2. 不可变来源与执行绑定

源提交：`ac6d8fff1e1905539339bf1bec39365fd62312ba`。
公开 job：`132744513869`，2026-11-15 07:54:33–07:55:27 UTC。
执行为本公开仓库 GitHub Actions，Python 3.12、python-flint 0.9.0。

| 对象 | SHA256 |
|---|---|
| 原数学核心 | `2a338672b32a9d760a78b234a0df08f05c10eb4ba513a2a3e3759f1e6e6b7aac` |
| R795方法 | `084cc240ea34f2737a6939ef8066dffa536e3b80e35a20ab62f70298db296b25` |
| R793证明 | `6f716b64432227244a46d91f01ae2f46ba6d4a5f893666693ed07dec9e2e5cab` |
| 公开wrapper | `8f92ec419fd7bc36fdec02eaef4848c95990339074cf0268a235194667fcf313` |
| 实际请求 | `9bb9c8dba4688d8bca045613851f92666f9e95ad8457165dc91188a4bfa867f4` |
| workflow | `f20d25d0a713a5c5fd8af280c56ce11ddcdd9d2e93fc62afe8bdb65e15655262` |
| 原R786下载helper | `7fbfe97b21ff9f58de4f1d2891b9f4a8cec4712e1b1c6d26d6d1ab9c336b81ec` |
| metadata发布helper | `39de279d30ad1493f1727c2e3c650b47b2bb0191765770b32a17ae2adb97c49e` |

真实producer为R775 run43679160495与R786 run43682100611。
逐来源的run/source/core/manifest/证书和最小消费文件SHA见
`notes/R795-public-exact-power6-short-basis-request.json`。

## 3. 实际输出与核验

| 输出对象 | 大小或数量 | SHA256 |
|---|---:|---|
| 临时ZIP，artifact14152762920 | 126375219 B | `557bb851ffe175643aa2b759fab3f378afdd51ef5d665fd4508a2a1f22ab8248` |
| `full-outputs-manifest.json` | 439607 B；1515文件 | `fb4a8f656c66d5ae10dee052baab79c07b43c7e7f19bb66b6e7d71be13b83ada` |
| `p41-exact-original-power6-short-basis-certificate.json` | 9794 B | `c5cffbd3979b5cd04e1e66c8c132de64974d81caf3b542e97a7a5ce479e3b0ae` |
| `R795-exact-power6-basis-index.json.gz` | 84787 B | `9c2d5a8731b491b464cc7580d1b504a4c7efac957a46b56a1fa7137049f06358` |
| `R795-exact-stages-manifest.json.gz` | 75551 B；1507阶段文件 | `37b3894e51f834bbe26113c2d4346de6a3f804114970a371e35783a105f3d064` |
| `R795-retained-producer-inputs.tar.gz` | 50326942 B | `87ad3ae7b639688467871a5b124be5ff5e0353464540e5d30fa23df7a962d6c4` |

完整临时artifact名为
`serre-global-R795-exact-original-power6-short-basis-43692029484-1`，
到期时间2026-11-16 07:55:16 UTC。
1506行文件为`R795-exact-power-6-row-0000.json.gz`至`1505`，
每行准确包含82组40坐标和82组20坐标、原recipe与公共尺度。
阶段manifest还有一项原次序索引文件。

root 已核ZIP大小和SHA、全部1515输出的大小和SHA、全部1507阶段文件配置、
1506行的完整次序/维度/尺度以及run/source/core来源链。
本地仅作文件与schema核验，没有执行数学核心。
可重算的完整表和大manifest不入Git/Release；直接后继由一日活跃包接收必要输入，
所有完成行在同一冻结配置下只读取，不重新生成。

本次提供后继固定RR乘法所需的准确基输入。
实际极除子、Jacobian中的$\eta$、原$\beta$、规范高度与全$p$一致性仍未由此得到。
