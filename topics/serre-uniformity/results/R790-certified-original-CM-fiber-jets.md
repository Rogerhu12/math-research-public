# R790：原 CM 点的146条截面值与首粗导已准确完成

2026-11-15，serre-public-astra-20261115。本文登记公开仓库自己的
[run 43688215703](https://github.com/Rogerhu12/math-research-public/actions/runs/43688215703)
的真实结果；原[正则化与求值证明](R790-original-CM-fiber-regularization-and-155-jet-evaluation.md)
及全部原方向保持。

## 1. 已实际得到的输入

该 run 在原 $P_1$ 上准确算出 R775 全部146条原 M2 基的
$\psi=T E_6/E_4^2$ 值与 $z=a-1$ 首导数，全部在
$K=\mathbb Q(\zeta)$ 的原基 $1,\zeta$ 中输出。
统一整数尺度为 $82^2=6724$；与 R786 的五次乘积尺度
$82^{10}=13744803133596058624$ 一致。

实际选基仅用原种子索引 $0,1,2,3,11$，五种子共十个反射对。
新五阶变形用短倍点链和 $40P=-P$ 提升，先作原 $\mu_3$ 正则投影，
再用两个280次域迹完成原5040项半迹。
没有将半迹替换为归一平均，也没有通过强制平均或浮点嵌入实现下降。
原 $E_{6,\mathrm{alg}}=-c_6$、eta 分支、正 Weil 配对、反射负指数以及
$z=-\varepsilon^3/(81(U/4)^2)+O(\varepsilon^6)$ 全部保留。

完整阶段清单含194个来源绑定的完成阶段，包括146个最终 M2 行。
最后阶段清单完成时，算术日志累计用时1101.720秒。
旧挠点模多项式、Weil 配对、M2 选基以及 power2至5 配方均按原 SHA 读取，
没有重新执行旧数学。

本结果只给原局部截面值和首导数。它没有计算原 $y=A/B$、$\beta$、
Jacobian 上的 $\eta$ 或高度，也没有假定 R787 的分母在 $P_1$ 非零。
R792 对真实共同零阶0或1可直接使用这些值；更高共同零须接真实局部代数。

## 2. 精确来源与复现参数

源提交：`9e4074fd9c99ab3af6bfad363b674e57f938800f`。
公开 job：`132733065732`，2026-11-15 07:03:35–07:22:20 UTC。
执行环境为本公开仓库 GitHub Actions，Python 3.12、python-flint 0.9.0。

| 对象 | SHA256 |
|---|---|
| `scripts/R790_exact_CM_fiber_jets.py` | `981eb543b791db416fad355d83eedb9bfe3b86b3e5461483fe4397e2129040b6` |
| 原 R790 证明 | `83303dcd6abc65875d8c67eb8977126db1c85cf3e9dafb3fbd2881163aadfc39` |
| `scripts/R790_public_original_CM_fiber.py` | `ba59c9407b44e15a26a415939fcaa54947b598bde4c0fe497c5b4948444161e1` |
| 真实请求 | `7d5cb0565cc2fef70ba5a4d7d689c5f94a05bf9e6ee1765d31c5afd21bfbfaa6` |
| workflow | `9100df1a1f1aed6d1406da910b4cb777361fcf69d90b332fc273283438ea72b8` |
| 旧 R754 精确域 helper | `f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251` |

全部实际 R735/R754/R771/R775 生产者、旧文件 SHA 和固定五阶参数见
`notes/R790-public-original-CM-fiber-request.json`。
首 run43687770143 因旧 R735 ZIP 不含 manifest，在准备阶段失败，数学 core 未启动；
此次仅加入已存在 Git 中、逐 SHA 绑定的原 manifest 回退。
两次的数学 core 和证明 SHA 相同，未重复任何完成的新阶段。

## 3. 输出绑定与接续

| 对象 | 字节数或数量 | SHA256 |
|---|---:|---|
| 临时 ZIP，artifact14151827531 | 50949334 B | `605aaaaefc5dc44f459ca4b8567204530e69a36134a52ac9614941c4219ddff2` |
| `full-outputs-manifest.json` | 202文件 | `49b5ccda0bbe3bc9d06a263fa3b15632f34b97ce518bc3825002583fb74afa60` |
| `p41-original-CM-fiber-jets-certificate.json` | 24966 B | `672044345934c0fc16b81ec2e2eaeb2a3282fa785069d53e240845d26b65e1fd` |
| `R790-stage-manifest.json.gz` | 11949 B；194阶段 | `5816cb3bb26fb5748017d3ace5ee65f1c1b87faf39675e6f05289ac0dd48de0b` |
| `R790-retained-producer-inputs.tar.gz` | 7203487 B；29文件 | `d7d906c40c45408ab9889fd9c9a43a6fc000b87dcedcd507046b4a9e5a236cde` |

146个局部输出按原 M2 次序为 `R790-M2-CM-jet-0000.json.gz` 至
`R790-M2-CM-jet-0145.json.gz`，逐行 SHA 和配方由完成证书与阶段清单共同绑定。
后继只须消费这些行、证书与清单；不需要重复五阶变形。
活跃输入包同时保留原 R775 power2至5，供 R792 接续，即使旧生产者 artifact 到期也不重算。

root 已核实际 Actions 成功状态、run/source/core/proof 绑定、ZIP SHA、
完整202项的字节数与 SHA、194阶段配置和146行次序/尺度。
本地只读取及核文件，没有执行新数学。
小来源回执位于 `computations/R790-original-CM-fiber-jets/43688215703-1/`。
原表和可重算证书不入 Git 或 Release；一日临时 artifact 于
2026-11-16 07:22:12 UTC 到期，供直接活跃后继消费后清理。

固定层 R707 的有理点分类已关闭，不重开。本结果补真实高度研究的局部输入；
主目标的全 $p$ 排除仍未完成。
