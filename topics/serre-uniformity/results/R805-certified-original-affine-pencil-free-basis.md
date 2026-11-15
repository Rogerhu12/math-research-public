# R805 原无基点铅笔与分次自由整基的实际认证

日期：2026-11-15。状态：**已证明，且有限证书已由公开 Actions 实际计算并完整核对。**
本文件登记 [R805 两图与极除子适配证明](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)
中铅笔及分次自由基这一步的实际结果。原曲线、原基次序、原整数尺度和原相位不变。

## 1. 实际结论

在原 $g(Y)=127$、$\deg H=272$ 曲线中，令 $e_0,\ldots,e_{145}$
为 R786 保存的原 M2 基，整数尺度 $82^2$。实际首个成功参数是
$$
n=1,\qquad \tau=e_0,\qquad \sigma=e_1+e_{73}.
$$
该二截面铅笔无基点。令 $S=K[\tau,\sigma]$，原截面环有实际的分次自由基
$$
R=S\oplus S(-1)^{144}\oplus S(-2)^{127}.
$$
一次补基为 $e_2,\ldots,e_{145}$。二次补基为原 V2 行
$$
146,147,\ldots,217;\quad219,220,\ldots,272;\quad291,
$$
保持这个原次序，不重标为某个新辅助曲线的基。

在 $\tau\ne0$ 图，以 $z=\sigma/\tau$，正规整基为
$$
1,\quad e_i/\tau\ (2\le i\le145),\quad
c_j/\tau^2\ (1\le j\le127).
$$
其秩为272；另一图和过渡仍按 R805 已证公式。
这是真正原截面环的基，尚未选 primitive 元或构造平面幂基。

## 2. 实际单位 minor 与特征零推论

本次全部关键模见证使用素数739。

| 原矩阵 | 实际秩或分解 | 实际选中 minor 的行列式 mod739 |
|---|---:|---:|
| $\tau V_2+\sigma V_2\longrightarrow V_3$，完整820实坐标/836生成列 | 690 | 509 |
| V2 中的铅笔子空间及127条原补基 | $291+127=418$ | 488 |
| 原分次 S 基的690条三次行，完整820实坐标 | 690 | 332 |

一次补基的坐标变换行列式为1，按原 $e_i$ 次序直接可核。
二次补基以及最后690行的行索引和源行 SHA 均在对应实际 stage 中，
后继必须直接消费这些已成选择，不能重选或重算同一秩。

原有理整数矩阵的一个 minor 模739非零，故对应特征零 determinant 非零。
第一行由 R805 的准确秩公式
$$
\operatorname{rank}(\tau V_2+\sigma V_2)=690-\deg\gcd(\tau,\sigma)
$$
推出无基点。无基点两截面是原截面环的齐次参数，
R805 的完整自由模证明及第二行的实际补基给出上述 $1,144,127$ 度数分布。
第三行则实际认证三次部分的690条基：
$$
\tau^3,\tau^2\sigma,\tau\sigma^2,\sigma^3;
\quad(\tau^2e_i,\tau\sigma e_i,\sigma^2e_i)_{i=2}^{145};
\quad(\tau c_j,\sigma c_j)_{j=1}^{127}.
$$
每条行都有原截面乘积生成见证，并核原 $q_Y/\xi$ 和 $v/t_\xi$ 两套坐标相符。
全部行统一整数尺度 $82^6$。41项乘20坐标给820，超过三次截面次数816，
对应的原短前缀注入足以把这些实际有限认证连接回原曲线。

这里的新690条 **S坐标基** 与旧 R786 的690条 V3 系数基各自保留原身份；
不能把两者的行次序混用。

## 3. 实际运行、参数与冻结来源

- 公开仓库：`Rogerhu12/math-research-public`。
- producer source：`9f960b8e0b2fa825ab1391e86db4e1383ffdd700`。
- producer run：[43705580592](https://github.com/Rogerhu12/math-research-public/actions/runs/43705580592)，attempt1，success。
- 实际核心耗时：15.520676039000001 秒。
- 核心：[`R805_original_affine_pencil_free_basis.py`](../scripts/R805_original_affine_pencil_free_basis.py)，SHA `730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420`。
- wrapper：[`R805_public_original_affine_pencil_free_basis.py`](../scripts/R805_public_original_affine_pencil_free_basis.py)，SHA `0eddbd194b7bfbf44f853fffeee0bef202447e48d22b264b5339229a44bf52b3`。
- proof SHA：`b48d9f8dd5d8d1a89aa2574ab7f9ee014b83ca21baf41694252b9c53993571e8`。
- [方法契约](../notes/R805-original-affine-integral-basis-and-polar-ideal-method.md) SHA：`df706176e53bf46cae0356b4af507aaae74cce5d02e9618aff1150ce4a81f656`。
- [实际请求](../notes/R805-public-original-affine-pencil-free-basis-request.json) SHA：`4b2c6331a3ba8350818dda820f09c869f66892d97fb1eedf9b2cc209fc091460`。
- workflow：`.github/workflows/serre-p41-original-affine-pencil-free-basis.yml`，SHA `d3ef2bdf68c09e5383569a2a7a6de1005b715615c26cb27f60ff66d6ec6db79e`。

准确参数在该 source 的请求中：原 p=41、41项、完整820实坐标、
原 R775/R786/R799 三组来源、只缺失的二/三单项式、参数 $n$ 的既定候选顺序、
739起的实际素数筛选、仅铅笔/补基/S行阶段。没有为得到本结果修改数学核。

## 4. 全产物与来源核对

producer artifact `14158193403`：
`serre-global-R805-original-affine-pencil-free-basis-43705580592-1`，ZIP 55714523 bytes，
SHA `cea9ac5d490722e86a93bbfa41d2061e5153f225359c167263b6d4fdd65d4d30`，临时有效至 2026-11-16T10:45:54Z。

公开纯 IO 审核 run
[43706758013](https://github.com/Rogerhu12/math-research-public/actions/runs/43706758013)，
source `6bdaec3b57a766b596efeaab9b59f2814b7d4bd2`，
使用 [`R805_public_success_io_audit.py`](../scripts/R805_public_success_io_audit.py)，
SHA `5ae35d0c86b20a8b6234f3aac6059c6567cfbea73ed6f835d74f15ba48360e4f`。
它读取真实ZIP，逐项核1322个manifest登记文件的尺寸/SHA；
ZIP共1324个文件，额外两项是总manifest及其引用。
manifest登记的未压缩文件总量 55441341 bytes。
1314个数学stage中有619个确实缺失的新单项式、690条S行，
其余为alias索引、铅笔、补基、S索引和minor等已保存阶段。

原输入包 `R805-retained-producer-inputs.tar.gz` 为 32662339 bytes，
SHA `00eda19de6591df21622a93b97c0bd6722c84d1c98922164dcb0be752eb56d78`。
1272个实际包成员全部核原manifest尺寸/SHA：
R775有6项、R786有1260项、R799有6项。
各组保留原source/run/core/certificate身份；审核直接取 producer source 的冻结文本，
完整比对数学核、wrapper、proof、method、request、两个helper、workflow及两README的SHA。
随后调用**原冻结wrapper未改动的输入选择与verify函数**，返回0；
未导入数学核或flint，未重复原数学计算。

| 实际文件 | bytes | SHA-256 |
|---|---:|---|
| `p41-original-affine-pencil-free-basis-certificate.json` | 5108 | `d65c799fcc1a23dfdf5fee9799b416ae202735a1da45b91e4792abd0236b76d0` |
| `full-outputs-manifest.json` | 451608 | `dfb7a4e58227b8ec4dfd86cc37bd672aeedf0f124776a427a0323220901130d7` |
| `R805-stage-manifest.json.gz` | 67098 | `37d151c36d0c8d01e7ec5af4a1228e1aaa19054889436c4debd17e7b27cc6547` |
| `R805-accepted-pencil.json.gz` | 4053 | `83f333404cb147eebe4b4c0d0f3dd383c20b532c7aab69c27269c111eaf6eb8c` |
| `R805-graded-free-basis.json.gz` | 11649 | `74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9` |
| `R805-degree3-S-basis-index.json.gz` | 43934 | `962694917252e23deb1d185a8caae81da773e314d3fca0475bac18a088dedd7e` |
| `R805-degree3-S-basis-short-minor.json.gz` | 45148 | `a75727f04295dfce77057b2df564a936008fbb6523b346de05e3d009c2ba7118` |
| `R805-original-monomial-alias-index.json.gz` | 83223 | `7be03da22d30c8527afa38bbb22a0e9c4329276f220525fde1dc57ba7a2a2eb5` |

完整IO摘要 SHA `c9b786ab3d62752e267a1db6984ece22918329cc4dac771fc2aec147acf81ba4`，
位于审核run的日志及一日临时artifact，不提交可重算证书到Git或Release。

## 5. 两项已成乘积与直接后继

R807所需的两个非旧alias乘积已经在本次计算中实际完成前41项：

| 原乘积 | stage | bytes | SHA-256 |
| $e_{3}e_{73}$ | `R805-new-monomial-003-073.json.gz` | 9155 | `4ecfd61fd3e47d49231075da11bcce17e1e4e577d8c4266d44e3e2b2267d45a4` |
| $e_{4}e_{73}$ | `R805-new-monomial-004-073.json.gz` | 9163 | `e94730bd1cc3ddad1e0c6ae3c2710c1ac0419a5097629d8631d2509ab65eb450` |

它们整数尺度均为 $82^4=45212176$。R807必须读取这些真实前缀，
只在实际非零核系数需要时续第41至54项；不能再卷积已成的0至40项。

R806可立即消费此处的真实 $n=1$、原690行集和272整基，
开始原primitive乘法与实际cyclic见证。R807独立消费上述两个前缀及原V4，
构造一次M6清极。它们都不得将本次成功预先算作自身已完成。

## 6. 规则同步与完成边界

审核runner实际执行部分clone和 `git pull --rebase origin main`，
完成时刻 `2026-11-15T11:00:18.765935+00:00`，
HEAD与origin/main均为 `6bdaec3b57a766b596efeaab9b59f2814b7d4bd2`。
相对上次已读 `9f960b8e0b2fa825ab1391e86db4e1383ffdd700` 的根README和本课题README差异为空。
这是实际pull记录；之前终端失联期间的API head读取未冒称pull。

本结果仅完成原无基点铅笔、分次自由基、两图正规整基的实际输入。
没有primitive乘法矩阵、原函数DAG、M6清极坐标、极理想、
KM代表、实际η、二挠刚性化或规范高度；Serre一致性主目标仍OPEN。
