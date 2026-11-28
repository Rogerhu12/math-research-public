# M12：由真实 M64 场热点生成的物理 h503 加密输入

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

本条登记已真实完成的物理网格准备、416个准确新半径查询和实际旧场的Boehm注入。随后新的非线性步仍活动，新场及连续后验须各有真实终态，不提前认作完成。

## 实际父场与选点

父场是实际返回并已有同场R226的M64/G12 `3ca49d46da9c13392f93cd3a6f1dcc6a1cdc906731c4571adae7800405c93b54`。其原G14/N3072 observer在全部487个元素、每元素14点上，保持原statistics不变并被动记录峰。prefix前8热点为149..156，tail前8为184..191；后者包含真实全域有限峰所在187/r≈0.51346558。

新准备器逐SHA绑定父grid、实际field/result及被动diagnostic的coefficient bytes。对上述16个真实元素，取原unit span的实际二进midpoint，每点加入3个quintic knot。所有旧结点及多重度保留，新内部多重度仍不超过3，所以有限空间仍至少C2且包含旧空间。浮点z midpoint不冒作与某原source r结点准确重合；这一操作也不是原source的消jump结论。

| 量 | 原场空间 | 新准备空间 |
|---|---:|---:|
| unique物理元素 | 487 | 503 |
| 径向自由列 | 736 | 784 |
| 角通道 | 194 | 194 |
| 总未知数 | 142784 | 152096 |
| 训练Gauss阶 / 角节点 | G12 / N1536 | G12 / N1536 |
| 独立Gauss阶 / 角节点 | G14 / N3072 | G14 / N3072 |
| 训练径向点 | 5844 | 6036 |
| 当前独立径向点 | 6818 | 7042 |

原g、source、参数、时间范围与角空间全不变。这是真正的物理h空间加密，没有用积分加密冒充新增空间自由度。

## 真正的点集包含与原源查询

全部原13185个准确source查询保留。新增416个真正不同的tail半径，所以新原源recipe含13601个半径；prefix新点继续使用原解析/分片prefix源，不伪造tail查询。旧G14中受细化影响的224个半径转入显式missing集合；连同以前3912点，共4136个祖先点另保，新的7042个G14点加这些点形成11178点真观察union。新场求完后必须在这些点上分别评价实际warm输入与实际child，不能混入source-zero before。

实际准备自然exit0，62.989134675秒。准确源的后继v2消费者按实际原parent链、24个原blob的bytes/SHA256/Git-blob SHA1核完416新查询，真实返回见末节；后面的非线性solver仍活动，不先写成已返回。

## 可重生入口

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-actual-peak-h-refinement-prepare.py --scripts scripts --data <M12-prefix-data> --old-grid <actual-M64-grid> --old-result <actual-M64-result> --old-field <actual-M64-field> --prefix-elements 8 --tail-elements 8 --new-knot-multiplicity 3 --out <h503-output>/grid.json
```

后继以已说明的 `2ecf-m12-extend-exact-tail-queries-local-v2.py` 核父链并准确生成新query，再重新绑定original-source-bounds；exact Boehm transfer从实际M64父场进入新C2空间，随后参数化 `2ecf-m12-refinement-execute.py` 显式使用新已实核 `2ecf-m12-h2-sparse-disk-normal-cached-lm.py`，lambda=1e−13、steps=1、H2浮点步上限.05、block24、assembly block8。原始物理J/JT、g和非线性接受规则仍相同。

- `2ecf-m12-actual-peak-h-refinement-prepare.py` SHA256 `dfb1b5061e231b6cc027e26c447a4531279635845d69e18909572ad13825271f`。
- `grid.json` SHA256 `d550fb04404ca25fff74c1f95253ed1264c3b87e57be776db8a2fc8fa140da6e`。
- `grid.json.queries.json` SHA256 `badb32c1331daef4618d79017a401fbf3455ec53660c9f268095d6b522a74456`。

## 后续真实返回：416个准确新半径与实际父场注入

上述 h503 输入的准确源扩充已自然 exit0（579.904984481秒）。v2消费器真实核原4631点streamer报告和13185点旧扩充报告、各自cache/recipe，以及新旧准确值的完整集合分解；随后仅对416个新半径重新走原24块Fraction积分流。新完整查询数13601，原13185值未重拟合，原端点/两micro窗口数组完全相等，原完整source连续二jet回执完全相等。新source-bounds重新实际计算，自然exit0（62.846090840秒）；prefix/tail/entire原C_X及prefix/chart准确流摘要与原G12源绑定逐项相同。

实际旧M64场 `3ca49d46da9c13392f93cd3a6f1dcc6a1cdc906731c4571adae7800405c93b54` 的准确Boehm注入也已自然exit0（receipt内5.218840526秒、stage实墙时5.304949142秒）：形状736×194→784×194，16个物理中点共插48个结点。二进保存后的原物理s/material-u一阶target-Frobenius误差上界2.539401808916295e−19、二阶target-scaled Hessian上界9.345554115191456e−14，均有准确有理证界；不声称存储后各点逐位等于原场。注入场 `ed281cfab427bef6f5cead3fc5e04218797da2e3756fac9955f150e4efdf5605` 随即作为实际非线性新步输入。此时LM仍活动，尚无新场接受结论。

新准确大数组仍仅临时本地；可重生配方依前文准备器、v2原源查询扩充器和参数化执行器，不以缓存SHA代替数学输入定义。

| 实际本地结果 | SHA256 |
|---|---|
| exact-tail-queries.json | `11a64bc3bf015cc9e47264e8a90e809be9e15453235c032a68ee5092933ae1cd` |
| exact-tail-queries.json.npz | `13ce5d3a20957038172799be3611ebe928280540d713904dcd7ba65fdc443da4` |
| exact-tail-queries.json.new-only.json | `0accc7ebe25188b98411c758b5bdf81c6d95502edc6290b98468488bda599223` |
| exact-tail-queries.json.new-only.json.npz | `689680f9567ffe614b3ca9765c940a409f63d37b26a802239a87ce2f775ad3b0` |
| exact-tail-queries.json.new-only.queries.json | `48e14423f0b5dcda79200b9d26137152fb992ea42570d37f56efb4aefbf43f9f` |
| original-source-bounds.json | `0e6138427145dbd22c19175debac718d3a20eb892e0a982f72943371d598c017` |
| warm-transfer.json | `a395e4468fb7b9a21664fd588d8cd12f8c25298f0020ad605793c2c787263ada` |
| warm-transfer.json.field.npz | `ed281cfab427bef6f5cead3fc5e04218797da2e3756fac9955f150e4efdf5605` |

准确源与实际后继的可移植命令接上文：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-extend-exact-tail-queries-local-v2.py --scripts scripts --manifest notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json --raw-directory <verified-original-24-blob-directory> --old-report <actual-G12-source>/exact-tail-queries.json --old-cache <actual-G12-source>/exact-tail-queries.json.npz --old-queries <actual-M64-output>/grid.json.queries.json --ancestor-bundle <actual-h487-base>/entire-half-exact-tail-queries.json <actual-h487-base>/entire-half-exact-tail-queries.json.npz <actual-h487-base>/entire-half-grid.json.queries.json --queries <h503-output>/grid.json.queries.json --out <h503-output>/exact-tail-queries.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/6a65-m12-original-common-cut-prefix-source-bounds.py --scripts scripts --data <M12-prefix-data> --tail-report <h503-output>/exact-tail-queries.json --tail-cache <h503-output>/exact-tail-queries.json.npz --out <h503-output>/original-source-bounds.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-refinement-execute.py --scripts scripts --data <M12-prefix-data> --old-grid <actual-M64-output>/grid.json --old-field <actual-M64-output>/result.json.field.npz --old-result <actual-M64-output>/result.json --old-correction-bounds <actual-M64-output>/correction-bounds.json --new-grid <h503-output>/grid.json --query-report <h503-output>/exact-tail-queries.json --query-cache <h503-output>/exact-tail-queries.json.npz --source-bounds <h503-output>/original-source-bounds.json --out-dir <h503-output> --solver-entry scripts/2ecf-m12-h2-sparse-disk-normal-cached-lm.py --lambda-step 1e-13 --steps 1 --hessian-step-cap .05 --block 24 --normal-assembly-block 8
```

最后一个参数化入口本身先准确注入、再执行真实LM及全部既有后验。它可重生本条已返回的注入；整条管线在本条冻结时尚未自然完成。
