# 两个完整连续合格 H2 场的三时刻闭合网格：实际重生与同场绑定

本次使用两个已经分别完成连续度量及全时几何消费的真实保存场，重新生成各自 t=0、1/4、1/2 的整个闭曲面。不是把首场网格改名给第二场，也不是将裸背景网格当非零修正场。原固定 g、时间范围、中央两侧拼接、有限尾、深 collar、两个封帽与固定区域均保留。

## 1. 入口与证明边界

新入口 `2ecf-m12-certified-field-closed-mesh.py` 使用未改动的 `6a65-m12-entire-half-closed-stl.py`，只接入已经实核的完整重结点 C2 基消费者和逐值相同的角缓存 v2。新入口先要求同一 field/grid/solver-result 的 R252 全域度量与 R253 分区法向几何回执；所有 SHA 必须相同，完整覆盖、metric≤1e−6、reach/D≥.03、held/D≥.05 与全闭面条件必须同时通过。

两份连续几何已有完整法管、嵌入、固定 H 和含反射非全等证明。这些结论来自它们各自的连续场证书。下列有限浮点三角网格只是该场的可重生代表，拓扑检查不构成额外的三角网格无自交证书，也不替代固定 g 的真实离散加密收敛。

| 实际输入/输出 | 首 H2 场 | C2 富集第二场 |
|---|---|---|
| field | `b6425243454a6a019d06a729405b0ebdaa0dbbc68b73b7f62745b1587174be1c` | `201de8909dc707c7d91749d812585233d49120c076468e9f2aebe97271114aed` |
| grid | `b01dd07d72c5e6fd29ac2aefd4029717bb41754494335a85bbf34e29aa72387b` | `018c81e5de5b16582ea50560c2dc29a99d0ad2955dea1a69c30a9fecaaa3c481` |
| 完整 solver result | `416d1a541b5ee6ab261b12a097e127e0fb772953060008c844189c450b7ea209` | `4e296d02d152dd9c7d25eeed2ca233c26e840003812336083c386d61530f5de8` |
| R252 全域 metric 回执 | `6a7dc22e0d69a38c45a1e6daa739a13ea7ddbe61c6bf324bc6096a5e01015679` | `bcba37a7c1c835fd491da6487ce6180ec5569b443a2c9cac2d47495638c1e4c8` |
| R253 全时几何回执 | `bd84f5fc47aa0ce29504401a79bb5d08ec5792bcbce2b2deccf34fbf5b83c7d7` | `a20ff53ec9a9da9e474c10dab723184a141e9e70a2bbebc031b56aae4fc5413a` |
| 本次完整网格清单 | `dfe899fbd00c95bb29844eb7567485e78b5d7ba439dbf5c1249b915ff95c11d4` | `000f94df89f3bf03e12992e560e306f2fd8a9de170697e64060a190c169e8846` |

两个场的实际连续 metric 上界分别为 9.999199635623173e−7、9.976475574355162e−7；全时 reach/D 分别 >.03114912、>.03114830，held/D 分别 >.05278319、>.05278314。没有借用另一场较小的 p 或曲率转移预算。

## 2. 实际网格检查

两次独立进程均自然退出0；生产者内部耗时分别16.232049566秒和16.166796567秒。每次都直接求同一非零修正场的六jet和完整几何，完整两侧、全部过渡和上下帽均进入输出。每个相位网格具有：

- 216个均匀材料角，实际反解原native angle；每侧前缀64段、尾部32段，尾半径选自已有准确源缓存。
- 44,714个顶点、134,136条边、89,424个三角面，Euler数2；所有边恰有两个相反定向邻面，全部顶点使用，通过连续环带和两个极点扇连通。
- 3,458个固定区域顶点在三时刻序列化的float32坐标逐字相同，上帽三个固定标记隆起、下帽平帽保持。
- 中央反解残差8.881784197e−16；中央平面和真实cuff接缝数值间隙为0，内部cut接缝最大1.241267077e−16。
- 每份STL均4,471,284 bytes；实际二进制读回坐标全同，所有三角形非退化，有向体积为正。float32顶点转换的实测最大差小于5.961e−8。

以上均是明确有限计算，不把float32转换差说成连续插值误差界。清单中 `continuousVertexErrorCertified=false`、`discreteSelfIntersectionCertified=false`、`fixedMetricRefinementGatePaid=false`、`READMEComplete=false` 均保持原样。

## 3. 三时刻文件身份

| 场 | 时刻 | STL SHA256 |
|---|---|---|
| 首H2 | 0 | `549ecdfcb8e3cc14e564b07ec54d238fc96883177dce61d68bc5243b1666ff15` |
| 首H2 | 1/4 | `179e2bbd26ac65dca2a3bcbb208accc9102185c424b118a54d25a4914bf3c52c` |
| 首H2 | 1/2 | `c6c0771717ac4426c7bce9201503744d90ea50442c1d69dbef3dc9f90892dacf` |
| C2第二场 | 0 | `fa1345a09bed091a24b136ef46b745b1f4119bcd53628f7e07c46dc5a82e9996` |
| C2第二场 | 1/4 | `2ef0a17b0225c6105e8e225f055296b4dd15dd40274230336471e4e368e22ef1` |
| C2第二场 | 1/2 | `7fdb41341dd97eff679ea1fb875873c497a5ea322ad5cda57b10301efbe8f460` |

## 4. 完整复现绑定

先按[实际首H2场](2026-11-28-2ecf-m12-h2-first-actual-field.md)、[实际C2第二场](2026-11-28-2ecf-m12-first-c2-actual-step-and-spectrum.md)、[R252](../results/R252-full-source-cross-Gram-and-actual-H2-metric.md)、[第二场完整cross-Gram](2026-11-28-2ecf-m12-c2-second-full-cross-gram.md)及[R253](../results/R253-regional-source-normal-transfer-and-actual-H2-reach.md)重生各自真实输入和后验。不得用另一个版本的field或人工填写通过标志代替。

共同原source数据SHA256为 `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`，query-report为 `7d75c93355fb5b79077c8b606294487c02f591e70e40111cac97abcf924da6d2`，query-cache为 `a98098ed40ffed92cae3f3ca208c91456d8a7f4958b08c4a21973c79dd881c1b`。网格用准确尾半径表SHA为 `a070ffcf51b5a066186065f301a22bb1520cb98ff1e115d90d84f5f16ff9b675`。源仍X+C，没有静默加入R250的Q。

以S为课题scripts、W为上述生产文件的临时工作根：

```bash
OPENBLAS_NUM_THREADS=1 python3 "$S/2ecf-m12-certified-field-closed-mesh.py" \
  --scripts "$S" --data "$W/m12-work/m12-prefix-data.npz.gz" \
  --field "$W/m12-work/h2-cold-cache-01/result.json.field.npz" \
  --grid "$W/m12-work/h487-base/entire-half-grid.json" \
  --result "$W/m12-work/h2-cold-cache-01/result.json" \
  --query-report "$W/m12-work/h487-base/entire-half-exact-tail-queries.json" \
  --query-cache "$W/m12-work/h487-base/entire-half-exact-tail-queries.json.npz" \
  --continuous-metric "$W/exact-work/h2-cold-full-cross-gram.json" \
  --continuous-geometry "$W/root-work/h2-cold-cache-01-regional-geometry.json" \
  --out "$W/root-work/mesh-h2-first/manifest.json"
```

第二场将field/result替换为 `m12-work/h2-c2-02` 中同名文件，grid替换为 `exact-work/h487-local-c2-grid.json`，metric替换为 `exact-work/h2-c2-full-cross-gram.json`，geometry替换为 `root-work/h2-c2-02-regional-geometry.json`，输出换到新的 `root-work/mesh-h2-c2/manifest.json`。其余输入与参数不变；已存在的STL/输出目录不能覆盖。

- 本入口SHA256：`0018ab2c80cf21ff8a8698d7de23a1b4b89506b46d0d8c2c4384400dd9c4785a`。
- 原完整STL生产者SHA256：`0dacc33668048a650e0d7aec63ba57f3906c70e0a247852bf2df0e64f9d6fbfa`。
- C2基消费者SHA256：`34fb3936a57bef17ceb3c326bdfad885fe7372366e373030ec7a83a4202f8814`。
- 角缓存v2 SHA256：`b69d67754d935a4e4342c934f80e5272d520f86164804c710350cf412a805745`。

依根README数据规则，六份完整STL、两份完整清单和原数组只留可重生临时目录，不进入Git或Release。这里只登记生产源码、参数、实际检查和身份。课题继续同一g的真实加密；本条不声称已达到README完成标准。
