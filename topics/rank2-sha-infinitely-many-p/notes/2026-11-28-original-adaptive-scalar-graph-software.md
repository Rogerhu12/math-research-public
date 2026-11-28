# 原完整单右端与坐标图：独立公开软件检查

2026-11-28 10:54 UTC。会话Astra-rank2-Sha-0b097461-20261127。对应已证明[R1071](../results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。本次只提交可复现源与固定小fixture请求；实际run、终日志和PASS待启动后读取。

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
