# 原完整单右端与坐标图：独立公开软件检查

2026-11-28 10:54 UTC。会话Astra-rank2-Sha-0b097461-20261127。对应已证明[R1071](../results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。本次提交可复现源与固定小fixture请求；随后公开运行已完成，下节记录实际验收。

## 精确来源和范围

请求种类 `original-adaptive-scalar-graph-software-check`；32个完整源码的逐文件SHA保在请求内，规范JSON清单SHA256为 `8457723b6818e2329ad7912cefdc2604292cd605ca106f0c6f6d69faef6638d6`。root逐文件核实际28旧源和4新源、语法AST、全部工作流push路径与bash语法；未在本地导入或运行数学。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `scripts/original_adaptive_dixon_solver.py` | 14088 | `4f25be445fe2717d44e2bebfe2c2379c5ea0b2d709208c46ce1d1b694a4f4509` |
| `scripts/original_adaptive_scalar_graph.py` | 22104 | `b6e5c9a2ad61a9314bac08b0ce221f15076feabd70a7d5b51c86688519df7ede` |
| `scripts/produce-original-adaptive-scalar-graph-shadow.py` | 29671 | `1ce9798d26d2c1029fc56d8c69afcee57158cef600e19c362729d61dc56c8335` |
| `scripts/check-original-adaptive-scalar-graph.py` | 5755 | `61b44d0b58e15db3c2e692b43ce5cd5a32efea54b651e1a2035d3ec88a6b6b92` |
| `scripts/check-original-complete-quadratic-api.py` | 15490 | `2ef9083dcde54d28b3cc9868ad6301b944b6c20a80dedc39a22d1b13b2c0d6af` |
| `ci/original-complete-quadratic-api-request.json` | 6470 | `96d5618d4928186c87240e51b0c7d0bad5e136b6a363d310626e981bcad9c385` |
| `.github/workflows/rank2-sha-complete-quadratic-api.yml` | 2914 | `31c7de95caf2d45c52e357d2eb7430fa02e18608db0126d2672eb444c58de935` |

## 实现与真实验收

单右端在实际一次或二次好底素作有限域PLU及逐位Dixon；全部高次底素进位、原域真转置和最终W M_D=qN身份均保留。图按真实失败列细化，以全部Laurent多项式部分返回完整X。原两ideal实际返回后再次重建全窗比较每个X，不以模t^d身份掩盖高多项式篡改。仍保32m完整X预算及原两ideal_from_rows，未启用可选反向流式分支。producer只备原端点hook和固定13增补pin，软件检查只对其源码作AST/hash，不导入或执行原几何生产。

固定8个完整chart比较覆盖两软件环的4种全输入；两厚例各应出现两次真正坐标细化。另须2次已造ideal后的实际t^d X篡改拒绝、2次真实完整X预算拒绝且无新增审计，以及真正二次好底素/原模块转置。selector先核完整32pins，再执行fixture，最后同时核唯一payload、payload SHA和实际计数才发PUBLIC_RESULT/PUBLIC_SHA256。软件PASS仅说明这些输入，不代原306图、四交/八scalar、Norm18×9或通常全Sha。

## 资源与当前生产

沿已存在complete-quadratic-api的独立concurrency，cancel-in-progress=false；外限420秒、job10分钟，4CPU/16GiB，Sage10.6固定镜像sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb，network none/source只读，OMP/OpenBLAS/MKL各4。根规则13公开Actions允许至多20个并发，本次只有现存v16 heavy与此小检查；本地无数学。

实际7路径只有selector/request匹配该小workflow；原heavy workflow、request、launcher、74源和运行v16 source0b550a6b1818b7875ceb5674fd8a8b2c080203b4均未改。v16仍run46126639698/job140922574854；10:48:10 UTC独立读取仍step4 in_progress，完整可见前缀2101729B/SHA e0e24b4565d45b59d8445515bba42820f6818d9898ab82429c2bbe8ebcea1f0e，末09:53:17.1519988Z，不是终态。

可重算结果只在公开Actions日志；仓库只存源码、请求、run/hash及必要原输入。

## 已完成的独立软件检查

公开[run46137528591](https://github.com/Rogerhu12/math-research-public/actions/runs/46137528591)、job140956064113、attempt1，source `4bb9fbcebbb160796da11f08c5d2b7eef4741b44`。10:56:46 UTC创建，step4为10:57:26–10:57:44，job10:57:46 success。root及arithmetic_ultra各自读取完整终日志，逐一核真实输入和验收，未以job绿灯代替结果。

- 全日志（UTF-8含BOM、LF）31915B/304行，SHA256 `82980684fa32ed676bd1f8f5561a91a44bf2b709acfc8c12358ad4fca2fa9309`。
- fixture正文296B，SHA256 `1207ee8b4975cafa4e9c8194f54fef072ebfe58d9a7d925445f68e7d47d4f763`；public正文4645B，SHA256 `a781c4db0ea3b36ca4e43907e47b5d6bd33565d6b28b8288a3568c102223c28c`。两正文及SHA标记、selector各唯一，内外实际fixture逐项相同。
- 真正8比较完成，两厚例各两次必要坐标细化，全部四次拒绝均经过规定的实际外门/预算路径；真正二次好底素及模块转置通过。实际fixture耗时7.582517183秒。
- 32实际源码逐项与上表/请求清单一致，request/selector/manifest/source/run/attempt、已固定Sage镜像，以及根/课题README blob `99c5ad8d06e939e6cfbbab1afdeffa5463f15f18` / `2f3b3c9264fbba8189f85716e68f768830e921bc` 均核实。真实Docker日志具420s/4cpu/16g/swap16g/network none/只读及三线程变量4。

此软件检查PASS。原306图及heavy producer未执行；生产性能和原四交/Norm/最终门仍需真实完整运行。10:58:32 UTC v16仍step4 in_progress，前缀仍与上述e0e24b45全文相同，未取得终态。没有保存可重算payload或日志。
