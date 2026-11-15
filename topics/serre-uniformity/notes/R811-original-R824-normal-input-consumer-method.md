# R811 接续契约：消费真实 R824 关系所生成的原 A/B normal 向量

日期：2026-11-15。状态：仅来源适配与可运行接口；尚无本接续的准确乘法矩阵输出。

本稿配合
[原 R811 证明](../results/R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md)、
[原 R811 执行契约](R811-original-regular-multiplier-and-polar-preimage-method.md)、
[R824 原关系适配证明](R824-original-exact-relation-adapter-to-beta-consumers.md)
及 [R809 A/B 专用消费者](R809-original-A-B-normal-consumer-from-R824-method.md)。
算术仍只由本公开仓库 GitHub Actions 执行。

## 1. 两个不同的真实 R809 来源

原 C0 至 C5 成功 producer 已完成 S5 的 1234 行、短 minor 与完整基标识，
却没有完成 A/B。新 A/B 专用 producer 的真实身份是
`R809-original-A-B-normal-coordinates-from-R824`，
由一条真实 R824 五次准确关系 $A=yB$ 得出原 normal 向量。
这两个 producer 的 run、core、manifest、configuration 和 certificate 都分别保留。

新 R811 核心
`scripts/R811_original_regular_multipliers_from_R824.py`
只适配输入，不修改冻结的
`scripts/R811_original_regular_multipliers.py`。
后者仍保持原 SHA，供已经冻结的 R815 等消费者继续引用。
新核心通过已核 SHA 导入原框架，继承其有限域乘法、插值、CRT、
有理重构、九点完整准确终验与第二图运输。
独立 RESULT 为
`R811-original-regular-multipliers-from-R824-normal-vectors`，
FINAL 为
`p41-original-regular-multipliers-from-R824-certificate.json`。
CLI 仍为
`--config --proof --method --retained --output --budget-minutes`。

三个逻辑输入目录分别为：

| 标签 | 真实内容 | 本接续读取 |
|---|---|---|
| R806 | 已完成的原 primitive 乘法与 cyclic 证书 | 原 $M_w$ 的全部准确坐标组、原正常基、真实 witness |
| R809 | 新 R824 关系所生成的准确 A/B normal producer | 两个 normal index、四个准确坐标组及来源回执 |
| R809_basis | 原 C0 至 C5 成功的 S5 producer | 原 S5 index、原 minor/rank 与 metadata |

`R809` 的证书中 S5 引用仍属于 `R809_basis`。
软件须分别核两个 tag，不能将旧 S5 index 改成新 configuration，
也不能将新 A/B certificate 换名成旧 C-only certificate。
三个输入都必须为已经结束并真实成功的 producer；
pending 请求不会触发计算。

## 2. 原 normal 坐标和函数身份

两个真实 normal 向量使用同一个原 $b$、同一个 $s=1+2\zeta$，
字段顺序为
$b^0,\ldots,b^6,sb^0,\ldots,sb^6$。
原 $B_{\mathrm{fld}}=\lambda b$ 的转换已经在新 R809 producer 完成，
本接续不再乘 $\lambda$、$\zeta$、$s$ 或任何模型尺度。

每个准确坐标组的第 $k$ 列仍按

$$
c_{ik}=
\frac{\mathrm{coordinate\_numerators}_{ik}}
     {\mathrm{column\_denominators}_k}
\cdot \mathrm{original\_target\_rational\_scales}_k
$$

读取；该有理尺度只乘一次。
R824 的共同分母和 content 已在真实关系输出中移除，
本接续不重新插入。
S5 原行序由旧 index 逐行核为 $a$ 外层、
$j=0,\ldots,5-\epsilon_a$ 内层，其中
$\epsilon=(0,1^{144},2^{127})$。

由新 R809 的全部 1380 条准确坐标证书，
这两向量分别就是 $A/\tau^5$ 与 $B/\tau^5$，
且 $B\ne0$。
R824 关系证明保证 $A/B$ 是原 $f_4$ 的 $y$ 函数，
即便这对 $(A,B)$ 与旧 R787 预留关系相差非常数共同因子，
比值仍完全相同。
软件绑定实际 R824 producer、实际关系 SHA 和实际 free column，
不把它冒充旧 R787 的准确完成输出。

## 3. 原冻结算术直接复用

对每个目标的 14 个有理分量，继承原 R811 流程：

1. 从准确 normal 坐标判定分量是否为零；
2. 在每个合法辅助素数的八个实际 Krylov 好点求原乘法矩阵像；
3. 插值并核逐项界 $5+\epsilon_a-\epsilon_b$；
4. 原子合入当前 CRT，按严格矩形界有理重构；
5. 逐系数核原第一列，并在整数点 $0,\ldots,8$
   核完整 $272\times272$ 交换子矩阵。

原 $M_w$ 的逐项界为 $1+\epsilon_a-\epsilon_b$，
所以交换子的每项次数至多 $8$。
九个互异准确点及严格次数界认证完整多项式恒等式，
不是概率性测试；这些准确终验点无须是 Krylov 好点。
这里没有重新生成旧 S5 行、原 q 前缀、原 Laurent、Hom 或短有理坐标。

不同目标和字段分量在同一新 run 中共享原框架已经完成的
同素数同节点缓存。
已完成分量和当前 CRT 都按完整来源标签续接。
原 C-only、R815 或其他 producer 的缓存只有经真实来源和兼容标签
显式导入后才可复用；本首请求不声称尚未提供的跨 producer 缓存已经存在。

## 4. 第二图与输出边界

仍令 $t=1/z$，
$D(t)=\operatorname{diag}(t^{-\epsilon_a})$。
同一齐次截面在第二图的乘法矩阵为

$$
M_{A/\sigma^5}(t)=t^5D(t)M_{A/\tau^5}(1/t)D(t)^{-1},
\qquad
M_{B/\sigma^5}(t)=t^5D(t)M_{B/\tau^5}(1/t)D(t)^{-1}.
$$

逐项非负指数和原第一列运输都由原框架准确核验。
共同 $t^5$ 在原比值中取消。
输出保持全部原系数和两图尺度，不对原 A/B pair 先消去公因子。

成功证书明确区分：

- 原 A/B regular multiplier 及同截面第二图矩阵确已完成；
- 原极理想前像、五函数 DAG、$\eta$ 与高度仍未由本阶段完成。

原 R822 / R824 后继若用另一条更小的完整极除子证书，
不因本接口存在而强制等待这两份大矩阵。
本契约不改变已经运行的旧 R787 或 R809 任务。

## 5. 公开 runner、最小来源闭包与续算

新 runner 的 verifier 只进行文本、schema、文件长度和 SHA 检查，
不 import 数学核心。
首次读取固定原 artifact metadata 后，以 ZIP64/HTTP Range
仅提取所需的 manifest、metadata、索引和准确坐标组；
每个所选原文件均按原 manifest 的 bytes/SHA 核验。
不把服务器宣告的 ZIP digest 说成此次已重哈希全部 ZIP。

随后把三个最小来源目录装入自己的一个一日 carrier。
续算读取前次 carrier，不依赖最早旧 artifact 继续存活。
同核续算对前次整个 ZIP 和全部 manifest 成员作流式 bytes/SHA 核验，
保持所有完整 stage、每个未成分量的最新完整 CRT current
及小历史链。
它不重新构造已完成数学阶段，也不写 main 或 Release。

外层数学进程限时为请求预算加 900 秒；
到限时先终止并给短宽限，必要时强制退出，记录退出码 124，
保留已经原子完成的文件，随后写最终 manifest 并上传一日 artifact。
工作流总时限另为这些 IO 和上传留空间。
Git 只保存脚本、参数、证明、run 和 SHA。

本首 pending request 已绑定真实 R806 与旧 R809_basis；
只有新 A/B producer 的 run/artifact/manifest/certificate
等待真实发布，绝不填造其结果。
