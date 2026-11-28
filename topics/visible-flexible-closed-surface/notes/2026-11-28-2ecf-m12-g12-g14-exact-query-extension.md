# 固定 M48/C2 空间的 G12/G14 原源查询真实扩充

日期：2026-11-28。原 g、几何参数、时间范围、487 个唯一物理片、736 个自由径向列和 M48 全部 146 角列不变。本条完成的是更高阶积分的真实原源输入、旧观察保留与准确暖场绑定，**不**把它记为额外空间自由度或已完成的新非线性场。

`2ecf-m12-quadrature-refinement-prepare.py` 实际生成 G12 训练 5,844 点、G14 独立 6,818 点。旧 G8 的 3,896 点和另外 16 个祖先点都不因更换 Gaussian rule 丢弃：额外 3,912 点逐 binary64 坐标保留，真实独立 union 总计 10,730 径向点。各层的 Gauss 阶数分别记录；没有把旧 G8 改名为 G14。角度仍训练 N768、独立 N1536，旧角网格保留。

同一原物理 chart 准确生成新增查询半径，旧 4,631 个 exact radius 全保，总计 13,185 个。既有 Fraction streamer 每次最多 12,000 请求，因此新消费者 `2ecf-m12-extend-exact-tail-queries-local.py` 只传入真正新增的 8,554 个半径，再与已验证旧 cache 合并；没有修改该生产者的请求上限或数学求值。

## 真实 exact-source 执行

24 个原 raw 文件来自本会话已经恢复的临时只读缓存。每个文件在使用前按 manifest 的 byte count、SHA256 及原 Git blob SHA1 三重核对。读取替换仅限 payload 传输，原 `span_jet`/准确径向归一化/逐 span 积分 Fraction 计算均为既有 source。全程无需网络或凭证。

实际生成和合并 exit 0，用时 987.291402022s。新旧 cache 的准确端点分子/分母、first/second、全部 546 微区诊断数组、Fourier modes 一一相等；完整原源连续 C_X 回执（含全部 18,552 个有限 span、深 collar 和逐行哈希）准确相等。旧 4,631 个求值逐值原样复制，无拟合或新 source。新 cache 仅扩充了同一固定函数的求值集合。

由于 query/report 哈希发生变化，既有 prefix+tail 连续 source-bounds 消费者已真实重跑，绑定这组新端点身份；此重新绑定不声称数学 source 改变。旧完整 M48 实场随后用既有准确 transfer 进入新网格身份，插结点数 0，角阶仍 48，存盘 field SHA256 与父场完全相同 `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`。

G12/G14 的实际 H2 步已独立启动，仍 lambda=1e-13、Hessian 增量筛选 .05；本条不报告尚未返回的非线性结果。随后会在所有原点的真暖 before/after union 上比较，而不只看新 Gauss 点。

## 复现与身份

生成更高阶 recipe 后，调用新增消费者，提供旧 query/report/cache、完整新 recipe、原 manifest 和临时 raw-directory；原 producer 只会算 8,554 个新增点。`raw-directory` 的 24 文件必须逐个通过原 manifest 和 Git blob 验证。中间新点原 producer 的 transport 参数仅为既有解析器占位；最终实际报告的 transport 明确是验证过的本地原 blob 和旧准确求值 cache。

- `grid.json`：`94a48337aedccd79810e02928bbe920334440d14df1eb68435c7a252969c07f0`。
- `grid.json.queries.json`：`9e3c21b04dfbfcf9b0dad933e47751893a5e9eb89b4099f2042f23114dbe3a37`。
- `grid-receipt.json`：`ce70a1b440fd453bba3a1c7b015605f8269af0b33f459610c4ab477410413b71`。
- `exact-tail-queries.json`：`1a222405e67641f5968c3bca36d50e372356ddc9508aeaf25e2267e51b0a698d`。
- `exact-tail-queries.json.npz`：`8c95cfeb3c5ebd186cf299d449d0835d718900c947669a8a862de6d68ff4eacf`。
- `original-source-bounds.json`：`e662014b75ada38faa10d34dcc425ab0275e0b7b660be29ed7f7eb236522cbc1`。
- `warm-transfer.json`：`f9983f25bea4404280473f3badeee548c11877ec8a3833bc8a67b6ee6075aece`。
- `warm-transfer.json.field.npz`：`6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`。
- 源码 `2ecf-m12-quadrature-refinement-prepare.py`：`0844538d6e1506bf60087cfc42920fe8701b1519a8b6881ce8f5aa0c315e9055`。
- 源码 `2ecf-m12-extend-exact-tail-queries-local.py`：`78d9d18434598cfd2174112221d26e5c57972d5e701ec66f7aeb15f1b1f89ee0`。

全部原 raw、query 数组和 field 保留 scratch，不进入 Git。更高阶积分还不是更细物理网格；后续收敛不能偷换这两个概念。
