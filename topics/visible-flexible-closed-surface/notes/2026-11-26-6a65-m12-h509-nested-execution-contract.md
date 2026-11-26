# 原 M12 第三热点 h509／M48：实际准备与完整暖续入口

日期：2026-11-26；会话 Astra-visible-flex-6a65e705。

本条已完成原第三热点的网格／查询准备和生产执行接线；大场转移、完整 H 求解及其新几何验证尚未执行。它不登记新理论编号，也不借任一个活动 Actions run 尚未返回的场。径向转移使用同日 [完整消费接口](2026-11-26-6a65-m12-nested-warm-transfer-interface.md)；原 Boehm／连续 jet 事实分别见 R196、R208、R226、R236，角向注入见 R243。

## 1. 第三热点来自已完成的真实场

R245 所述 run `45833090043` 的 h487 实际场为

`cdcbbd53c4019d0b4df88043662c13c736b65429575e6276ac44bb482375aa12`。

其独立 $G8/N768$ 峰 $9.839529672210558\times10^{-10}$ 位于材料 $q=2.1414467510787043$、径向索引 1920、角索引 61。用同一 WholeChart 及原网格重建，该点恰为 h487 元 240 的首个 G8 点，和所报 $q$ 的 binary64 差为零；此元素来自原 base 元 181。原两个局部加密仍保留，不把峰留在旧元 190。

当前有限重建给该元 unit 区间 `[0.8663031099808095,0.8691477246620688]`；物理半径显示区间约 `[0.48813591365574328794,0.49473079603213867812]`。峰的半径数值为 `0.49460057788612834574`，位于原源 span 17371。半径只是同一准确图的数值反参，不冒充一个严格反参区间。

## 2. 已实际生成的 h509 集合

原 payload 按 known Git blob `26ce0426c60ef868c53597a82252e0559c1cc21e` 恢复，3,112,330 bytes，SHA256

`359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`。

本地只读取三个明确尾部 blob，恢复 `.432,.5141` 内的准确源节点：

- `1a9cce86c3ad6e88bc07dedb465a08066a62a5ab`，1,787,305 bytes；
- `5f9c90c55334de4a757b7c88708b7b454951585d`，4,418,227 bytes；
- `c706e8235eca11b8def049afe55ca2ee6b36cf4a`，4,418,763 bytes。

每个 payload 都核对原 SHA256 和 Git blob framing。传输适配器只执行明确 blob 的终端 `git show`，不更新 refs、不拉宽历史、不把二进制打印到日志。生成器的全部 cut-backward 有理增量计算原样保持。该准备自身仍要求主 streamer 完整核对 24 块的准确归一化；它不是该全源证明的替代品。

以已经发表的 `6a65-m12-transitive-source-knot-refinement.py` 对 h487 元 240 实际准备得到：

| 项目 | 生成值 |
|---|---:|
| 元素数 | $487\to509$ |
| 新的原源节点 | 17350–17371，共 22 |
| 所有旧 unit knots | 逐值保留 |
| 新 knot 重数 | 一，仍为 $C^4$ quintic 空间 |
| 保存的祖先遗漏 G8 点 | 24（原 16 点加当前 8 点） |
| 旧准确 query 半径数 | 4,631 |
| 新层独立物理 query 数 | 4,925 |
| 合并祖先后的准确 query 数 | 4,953 |
| knot 数值反参最大回程差 | 显示 $1.2899295347146289004\times10^{-16}$ |

原径向 source 节点是有理准确恢复的，进入 solver 的 unit knots 是本次同一材料图数值反参后保存的 binary64 定义；此处没有声称它们恰是准确反参实数。

临时 h509 grid 为 26,281 bytes，SHA256 `9edaf1277dd4903308cf33260f6a0eb0ccca950f52dfbafc61c0a22b3231e1e7`；query recipe 为 236,143 bytes，SHA256 `655295cd3cb016b925a3af9f90f08d1cc8bf44946a51c22d6c9045e8d7a4a9ca`。这些可重算文件不入库。后续独立结构读取实际 exit 0，核对全部旧 unit knots 和准确有理 queries 的集合包含、22 个实际 source 节点及 24 个祖先遗漏点。这里不声称一次新的 field 求解已完成。

新增第三诊断窗 `.4881,.4948` 与原源 span 17349–17371 相交，共 23 spans，保留完整相交 spans 的 93 个不同四分点。原两窗 `.432,.436`、`.5122,.5141` 仍各自保留，绝不把三个窗之间的空隙称为已观察。

准确源 recipe 含执行身份和计时，因此独立重生时整个 grid/recipe SHA 可不同；生产会使用本 job 的实际 SHA，比较固定来源与实际集合定义。既往 grid／field SHA 只作为比较身份，不能强迫新 runner 冒用旧证明。

## 3. 明确的新入口与 17 个阶段

入口为 [6a65-m12-h509-nested-full-normal-cold-run.py](../scripts/6a65-m12-h509-nested-full-normal-cold-run.py)。默认参数固定为原基态 `80/64/depth12/M32/N384/G6/800/1/block24`，旧 h 元素顺序 190、176，再对其 h487 元 240 加密。新的求解层为 h509、M48、N768、G6、800 LSMR、一次 Newton；独立观察 G8/N1536。径向列数 $508$，完整角列数 $146$，合计 74,168 个实际未知数。

它依次执行：

1. 编译新执行源并运行非零准确转移／保存差有限核；
2. 在本 job 重生完整 h487、其 R226／R230 几何、旧两微窗、祖先观察；再执行其 R236 与三张 STL；
3. 从同 job 的准确源节点 recipe 生成 h509 并保留全部祖先 query；在该 h509 上扩到 M48/N768；
4. 消费同 job 的真实 h487 field/result/grid/R226，准确插入及角向补零，实际一次保存并生成连续保存差回执；
5. 从完整原源实际生成新 query cache，恢复三个窗口及完整 source $C_X$，不拿旧 cache 冒充新增径向点；
6. 在进入求解前逐个核对全部旧 query、旧端点和原模式，比较共有缓存系数两 jet 值完全相等；旧两微窗的准确点身份、源值也实际一致。执行时要求实际新增源节点仍为 17350–17371 且新元素数为 509；
7. 以新保存场为真实初值执行完整 H 暖求解；不清零。之后重算新场 R226、全相位几何、暖初／终场的三窗口及完整祖先观察；
8. 外层 supervisor 再消费同一个新场生成三张 STL 及 R236 连续度量界。

这里分组描述 17 个 cold 子阶段及外层消费者；完整命令图由 `--plan-only` 重生。每个新场及其观察都绑定自己的真实 source、query、grid、field SHA。17 阶段 CLI 的 plan-only 已实际 exit 0；没有据此宣称一个数值阶段运行成功。

生产命令形态为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-h509-nested-full-normal-cold-run.py \
  --scripts topics/visible-flexible-closed-surface/scripts \
  --data "$M12_COLD_DIR/m12-prefix-data.npz.gz" \
  --directory "$M12_COLD_DIR/entire-half" \
  --warm-order 48 --warm-angular 768 --warm-iterations 800 --warm-newton 1 \
  --preconditioner-eta 1e-6 --normal-assembly-block 8
```

冷入口有独立 `--plan-only`，只打印命令和 source SHA。它不能替代真实执行回执。

## 4. 与已冻结 M48 源的精确差异

[新的 nested warm core](../scripts/6a65-m12-entire-half-nested-warm-refinement.py) 从 R243 的 `e58d4f3c036a1ec4b78a3c7022ac6e6677e9b7bac4c3be8eea43ed8665a2ae81` 派生；变化只在新 transfer schema／实际保存误差 reader、相应输出标签和明确来源。旧 physical J/JT、三条 Gram 残差、原 target、完整方程、normal/slope 诊断、试步接受规则、独立观察及端点检查均保留。新入口仍明确拒绝含 `unit_knots` 的重 knot 生产定义；不能因有限转移核支持重数三便假称整个 solver 已支持。

[新的完整 H adapter](../scripts/6a65-m12-full-normal-nested-warm-refinement.py) 只把原 adapter 的 frozen core 绑定换到这一明确新源；完整三 Gram 行、Cartesian／角向所有 cross terms、物理梯度恢复 $D^{-1}Lq$ 和参数均保留。取 $P=H+10^{-6}S$ 仅用于右预条件，物理 $\lambda=0$、LSMR `damp=0`；没有增添目标正则项，没有借正 $\lambda$ 的谱下界给此系统。实际下一个 normal、试步和完整残差决定是否改后续方向。

对照是同配置的 h487 完整 H run `45851669566`、冻结源 `0ce2394f1b0b049be99e4e622d504ff5660a5843`。本新入口从自己重生的 h487 开始，不消费或假设那一 job 的终场。更大空间的准确初值是原场的表示变换，其函数本身未改善；一次存储误差另有严格界。真正下降只由后续实际求解、相同祖先观察和完整连续核来判断。

## 5. 规则、权限和发布

独立 workflow 为 `.github/workflows/6a65-m12-h509-nested-full-normal.yml`，唯一 push 触发路径是该文件及 topic 下 `ci-requests/6a65-m12-h509-nested-full-normal.json`，同时保留 workflow_dispatch。job 最大 350 分钟，supervisor 每 2700 秒 literal `git pull --rebase` 并立即检查两份 README 差异；数值源码先冻结在另一个 RUNNER_TEMP 目录。

新独立 HANDOFF marker 为 `<!-- 6a65-m12-h509-ci-rules -->`。每次实际 pull 后记录实际 SHA；若 README 变化，立即终止数学进程组，先以普通提交发布 H-only 的“已见变化／待应用”记录，再 exit 42，不发布旧规则下的数学结论。写 H 前保留 10,000 bytes 检查。持久 Git author、精确并发拒绝分类、普通 NFF pull/rebase 循环、H-only 冲突保留其他文字、空 rebase skip 都来自已审原 controller；不用 force。

全部 field、cache、STL、JSON、证书、日志只保留 RUNNER_TEMP／Actions logs。发布器只写一份小 Markdown 结论：实际阶段退出、关键指标、全部完整输出的 SHA、source／request／run 身份和剩余结论边界；不将完整可重算输出分件入库。新发布路径不接触两个活动 M48 run 的已有摘要。github.token 仅供恢复和普通发布，全部数值求解子进程剥离恢复 token。

本地五个新 Python 文件实际 AST 通过；workflow 10 段 run shell 经 `bash -n`、5 段 Python 经 AST 通过，窄触发和 350 分钟参数已实际检查。此为接线和语法回执，**新全场数学执行状态仍为未运行**。

## 6. 冻结源身份

下列全部是本条明确新身份，不替换既有已执行代码。

| 文件 | bytes | SHA256 |
|---|---:|---|
| `6a65-m12-entire-half-nested-warm-refinement.py` | 26104 | `39f4b31bcf50123cd9cb6ce69db8415c9ed28e0999c568f579439c01d7a88899` |
| `6a65-m12-full-normal-nested-warm-refinement.py` | 6679 | `ba597744a30508e953354077987135ed86ed05f967c43a986453f2b3ae659871` |
| `6a65-m12-h509-nested-full-normal-cold-run.py` | 18935 | `0db68c932d90effcee86ffeee1c602f00dc40226ae3c6b72d672fe2bb2ea4012` |
| `6a65-m12-h509-rules-supervisor.py` | 12577 | `5b338c7aee125ef7c4b7ac5e3f7705b25a15dcdc8ddb3283a2bee04945f4cb75` |
| `6a65-m12-h509-summary-publisher.py` | 17646 | `fe5ee53b67845bd5fe5d51290c71c427ef61551a1147c27546c1449f502e7fa3` |
| `6a65-m12-h509-nested-full-normal.json` | 2987 | `7c56c624e9a089cadc02fe7f221866746d77459cabdbbe79af9a2b3d879fed2d` |
| `6a65-m12-h509-nested-full-normal.yml` | 13835 | `7405f5acaf463014a9bc7c7cd652a87ca61c6535f8cc0f277cacf1c3084f8b79` |

旧结论和原数学定义只作依赖消费。本条没有新的精确等距证明、没有当前 M12 whole-field 的新数值残差、也不完成 README 第 5 项。
