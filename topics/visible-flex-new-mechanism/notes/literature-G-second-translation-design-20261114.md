# N²G 单块原式研究接口：R128 的冻结设计

日期：2026-11-14。本稿是接口设计与人工开发回执，**不是 N²G 的研究结果**。真实目标只在本公开仓库 GitHub Actions 运行。

## 1. 只接 R126 已完成结论之后的一步

R126 已证明

$$
G\notin\mathcal R_8,\qquad NG\notin\mathcal R_8,\qquad2\le s\le10.
$$

因此本次只判断

$$
N^2G\stackrel{?}{\in}\mathcal R_{8,-1}.
$$

不会重算 R118 的 7 列 G 分离，或 R126 的 20 个权零原列、4 条依赖、16 列原式评价。旧 first-translation 驱动与成功报告保持原字节。

新驱动 [literature_G_second_translation.py](../scripts/literature_G_second_translation.py) 仅接受 order=2。它复用旧真实平移生成元、完整两模式响应式、原始有理 Volterra evaluator 和报告保存器；不调用旧 main/study，也不调用 forcing、局部第四密度或 W 的编译器。

## 2. 输入身份

先绑定冻结的 R118 原 G 报告，再绑定 R126：

- run：43649525432；
- source：5852d7d4400859e53dde789b4d63f200d0e0acce；
- 主报告：G-first-translation.json，23923 B；
- 主报告 SHA256：9926a1f7026064c95c297b34da60ed5f1b345bc37753a23e75295cf44792fe82；
- receipt：33085 B；
- receipt SHA256：06e5d82a7e7db8922d42347920609c83a3ad0114050cdbbdafc72084c3e25bec；
- 冻结旧驱动：26885 B，SHA256 331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5。

它检查终端发布的 run/source/lane、原驱动身份、20→16 的完整原式依赖计数/哈希、两个非零子式及非成员完成状态。仅有 word 代表秩、资源退出或少一个模式都不能作为合法前序证据。

输入旧 G/W 使用 R115 已成功保存的完整原式 gzip；同一输入文件、所有根 SHA 和 v2 的 36 个真实第三模板仍按既有接口核验。大原式只能由公开 Actions 直接读取，不通过 API 展开或分片搬运。

因为旧 NG 报告只保存原式哈希，而没有独立 NG 原式 export，新驱动从冻结 G 作一次真实 N，逐模式确认

~~~text
-4  de54f551a028ca45ece143f661df99ab4f7541b1ec39cab7add66fc60dd0e130
-2  2eb0fe581f521b2e6f0e520b2ac5f91e09da0349cf71994852369dfeef7409e4
~~~

然后再作一次 N。前一次是目标身份重建，不重新研究旧响应块。

## 3. 数学与证明门

真实生成元固定为

$$
N(\xi)=1,\qquad N(q^{(j)})=N(\bar q^{(j)})=0,\qquad
N(I_rF)=I_r(NF).
$$

共同右锚与输入一起搬移。这不是完整 $\partial_\xi$。驱动准确核 N²G 只含权负一。

完整 E8×W36 权负一共有 **36 个原响应列**。按原基顺序逐项生成完整 $-4,-2$ 两模式；保相同实系数。每一条拟丢列关系必须重新组合两模式原式并证明真零，才得到真实上界 r。代表秩自身不是独立性结论。

若目标归约得到关系，必须重新由原 N²G 与原响应列组成差，逐模式证明为零，才记为 member_identity_verified。前序 R126 立即给 s=2，并停止整个平移链。

若未产关系，不直接宣布非成员。按同一实有理输入

$$
f=t^8(1-t)^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad t=\xi-2,
$$

在原式上计算 24 个内点、两模式实/虚共 96 行。右原函数统一从 3 积至查询点。实际可达输入 jet 阶数会先检查，若超过该零延拓允许的七阶，直接拒绝当前输入。

使用 p=2147483647，检查素数及全部遇到的有理分母。如果控制列模 p 的秩恰达已证上界 r，且某增广 (r+1) 子式非零，才证明完整权负一原式非成员，结合真分权得到 N²G∉R8、s≥3。泛函在 Q 上定义为原有理 Cramer 泛函；模系数不被冒用成 Q 系数，更不提供实数符号。

如果原式评价达不到上界或没有增广子式，本步只能是 undecided。不会借低模秩推断真依赖，也不会自动执行第三阶。

## 4. 有限预算与完整回执

默认与前一次保持同级别：

| 门 | 默认值 |
|---|---:|
| 研究时间软门 | 240 秒 |
| RSS 轮询软门 | 1024 MiB |
| 原式多项式最高次数 | 256 |
| 多项式操作门 | 10000000 |
| 小主报告 | 90000 B |
| 完整压缩报告 | 2500000 B |

资源门、实际输入/目标身份、完成的列、真实上界依赖和评价证书均在报告中保留。完整 JSON 先写 gzip，再写受限小 main；主报告保留前序 NG 绑定、新 N²G 原哈希、原式上界摘要、成功或未决证书。完整有理关系在 gzip 中，不因 main 太大而静默丢弃。

预计文件：

- G-second-translation-development.json；
- G-second-translation-development-complete-report.json.gz；
- G-second-translation.json；
- G-second-translation-complete-report.json.gz。

所有实际目标运算具有双重环境门：GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。人工开发不触发目标。

## 5. 本地人工开发已完成

只运行 py_compile 和十项小人工检查。它们覆盖：

- 两次平移对外层坐标、内层原函数坐标及两个嵌套原函数的乘积法则；
- 人工权一输入被送到权负一；
- 独立有限移位的二阶差分与 N² 相同；
- 与共同右原函数交换及有限链终止；
- 人工前序证书来源接受；
- 错误 NG 哈希、未完成前序和没有真实子式的“代表秩证据”明确拒绝。

运行结果 toy_passed、all_passed=true，0.002243069000542164 秒。没有读取真实 G/NG 原式，没有编译任何新旧研究列，没有评价任何真实 profile/geometry。

人工 main 为 5507 B，SHA256 de2ad266e0a7186cf7d9c2fc250f34db8592a33fb1ebf4dcb1872ac7da517b0b。它明确记录研究未执行，不能当作 public actual 结果。

冻结源码为 24396 B，SHA256

~~~text
3c37aeae4b39ecf68932a069878b41d890afbe2fd4ee9d8675195edc4e5d6bc1
~~~

## 6. 最小公开命令

在仓库根目录，以当前 job 的输出目录替换 OUT：

~~~text
python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_G_second_translation.py

python topics/visible-flex-new-mechanism/scripts/literature_G_second_translation.py \
  --toy-only --order 2 --output OUT/G-second-translation-development.json

python topics/visible-flex-new-mechanism/scripts/literature_G_second_translation.py \
  --order 2 --output OUT/G-second-translation.json
~~~

第一次 actual 不改冻结输入、不增加同块预算、不重跑此前成功目标。任何结果仍只涉及该有限仿射轨道的成员门，不支付全部 U4、第四 ruling、有限等距族或主课题的嵌入、厚度和幅度要求。
