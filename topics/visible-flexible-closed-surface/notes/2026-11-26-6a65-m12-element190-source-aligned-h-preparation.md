# 原 M12 第 190 元的同 g 原微区间径向加密入口

2026-11-26，Astra-visible-flex-6a65e705-20261126 / g5-and-exact。

**状态：完整冷入口、准确节点恢复和最终查询准备已实际验证；
新 428 元 solve 尚未执行。** 本次只给下一轮可执行的 h 加密，
等待同一已保存场的 R230 微区间观察，未预报误差下降。

## 1. 唯一变化与比较对象

原 entire-half 网格有 362 个径向元、35378 个未知系数。
当前目标仍是 R21/R223 的原 M12 固定 g，从中央曲线穿过内部
r=.6 接口一直到真正 flat cuff；完整两帽、中央和 cuff 两 jets 保留。
原位置供应器、精确桥、原尾定义、中央归一化和全域残差一律沿用。

依据 R230 的准确原微区间观察，只在旧零起算第 190 元内部插入
66 个原尾源节点的公共坐标像，对应 global source 节点
17108 至 17173。所有旧 unit knots 逐值保留，得到
428 元、41846 个未知量。节点保持单重，quintic correction 仍为 C4，
本档没有同时改为三重 knot 的 C2 空间。
这直接使用 R189 的旧 knot 包含准则，不把任意增加基数叫作同场加密。

角阶32、训练N384/G6、独立N768/G8、LSMR800、Newton1保持原值。
新冷试验仍从同一个确定参考 W=0 开始；不是未保存旧 CI 场的 warm start。
粗/细两档的 LSMR stop7 若再次出现，仍按实际回执记为迭代上限，
不能单凭空间嵌套宣称求解已收敛。

## 2. 只读准确后缀恢复，无第二次完整整流

新增节点不写成 Git 中的 raw 数组。小 request 只给窗口
r∈[.432,.436] 和旧元索引190。
预处理从准确 cut=c 开始，反向累加同一准确 βell。
它只读取并核实最后3个已知原 blob，合计10,624,295 bytes；
不使用显示累计半径，也不读取新的候选或修改 g。

实际 exit0，12.903971852秒，得到窗口及两侧包围节点共75枚准确 Fraction。
这些75枚节点与 R230 全24块正向整流的节点逐 Fraction 完全相等，
全局节点号17102至17176也逐一一致。
临时节点 recipe SHA256：
9c943e53e7568a54886911a29eb885c0a1d6596cc0522f2031dd995f53caa7f3。

正式冷入口随后只做一次完整24块查询/连续界整流；
它仍检查全部正增量、共享行、全归一化、manifest和源身份。
后缀恢复没有替代这项全域检查。

## 3. 最终网格和 exact-query 锁

原元的 unit 区间约为
[.890806118584362,.8919046421121438]，
公共q区间约为
[2.201873091129276,2.2045883951054535]。
每个准确原 r_i 经同一 R223 逆图转回 q/T，
再冻结成此有限试验实际用的 binary64 knot。
这只选择离散空间，不改变准确公共图或目标 g。

程序逐值核全部旧knots保留，新增节点都严格在选定旧元内；
预设最小新 knot 距离1e−12，本次实际没有因近邻而省掉任何节点。
最大数值 r↔q 回程误差小于1.395e−16。
新训练/独立径点数为2568和3424。

拆分一个元也会移动其中的 Gauss 观察点。
因此最终查询另保旧第190元的8枚G8点，旧径向索引1520至1527。
其余旧观察点逐值属于新观察集合。
最终独立观察使用“新全域G8 ∪ 这8个旧点”，是旧全域观察的真正超集。
程序不把这个集合并称为新的积分公式，也不合并不相容的 quadrature energy。

最终 prepare 实际 exit0，13.834766170秒：

| 项目 | 实际值 |
|---|---:|
| 新径向元 | 428 |
| 新未知量 | 41846 |
| 新增 knots | 66 |
| 训练径点 | 2568 |
| 独立径点 | 3424 |
| 额外旧观察径点 | 8 |
| 最终不同准确 tail radius queries | 3791 |

最终 grid SHA256：
1820e8994f3a16af7c9e030465ab6d4eb89ed0a8f94ae493164b6bed078bbba3。
最终 query-file SHA256：
2cdbcd42135ef6f4d8588a4c85ed82e9c0e07a0cb073c9ef04d06b9cb5ff64bd。

较早仅3783查询的初稿没有保留那8点，已被此最终准备取代；
不把两个查询清单或源码身份混用。
正式 solve 沿用原 whole 接口，要求 cache 的 query_file_sha256
与此最终grid完全一致。

## 4. 冷入口与保存场消费

入口
6a65-m12-entire-half-local-source-knot-cold-run.py
依次执行十阶段：

1. 原 whole prepare，保留临时 base-grid；
2. 准确原尾局部 knot 后缀恢复；
3. 只插入第190元的源节点，生成最终 grid/queries；
4. 原24blob完整查询和连续尾源界；
5. 完整 prefix/bridge/common-cut/整半图源 C_X；
6. 原 whole solver 在最终网格上作同配置试验；
7. R226 对同一次保存的W给连续六 jets；
8. R230 对同一field/grid/cache作全时间几何传递检查；
9. 同一297个原微区间点的实际 field 观察；
10. 只再求那8个旧G8点，给观察并集的真实峰。

root 的实际三相位 STL 生成仍可作为其后的独立临时阶段；
它不改变此数值试验。全部raw只在RUNNER_TEMP。
M12_RECOVERY_TOKEN仅交给两个恢复阶段，所有数值阶段显式剥除。
脚本不直接commit、push、上传artifact或release。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-entire-half-local-source-knot-cold-run.py \
  --scripts topics/visible-flexible-closed-surface/scripts \
  --data /tmp/m12-local-h/m12-prefix-data.npz.gz \
  --directory /tmp/m12-local-h/run \
  --prefix-elements 80 --tail-elements 64 --tail-depth 12 \
  --order 32 --angular 384 --gauss 6 --iterations 800 --newton 1 --block 24 \
  --local-element 190 --diagnostic-window .432 .436
~~~

--plan-only 可核完整源hash和命令图而不运行十阶段。
最终版本实际 plan-only exit0，stages=[]，没有把计划称作执行。
四个新 Python 源均实际 py_compile exit0。

新增最终小报告名为 entire-half-old-observer-union.json；
原 R230 五份小标量报告继续保留。
统一 execution receipt 核 base-grid、局部节点recipe、最终grid、
完整cache、真实field、连续界和旧观察并集的SHA。
不存在“缺少精确查询就临时换近邻点”的回退。

## 5. 冻结源码与范围

| 源码 | SHA256 |
|---|---|
| 6a65-m12-original-tail-local-knot-suffix.py | 8794dc0f510b399f8726f988461a641b46e7808eb185b13c959d8f689e44ca63 |
| 6a65-m12-entire-half-local-source-knot-prepare.py | bd5a876026ef535d661f911e1f302b42dbb89329946b72bf0a086f66fc2bf431 |
| 6a65-m12-entire-half-old-observer-union.py | 3240869420d2dfb975f71cfae48772b30d780a4989adcd6b9e7e3fd8355826b4 |
| 6a65-m12-entire-half-local-source-knot-cold-run.py | 44e3f2082c6f5bbcef9cc88f3450ffb10c4146abfc7eaa42f51105ff50a58648 |

本档不改 g、原 source、角阶、Gauss阶或迭代预算。
它也不改已经发布的 R230 六份源。
空间真正加密及观察集合真正扩大已经落实；
误差、曲率、几何传递和运行时必须等后续实际field回执。

