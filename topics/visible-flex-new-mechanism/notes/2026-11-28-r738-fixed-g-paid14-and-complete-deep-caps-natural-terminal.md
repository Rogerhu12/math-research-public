# R738：第一厚源固定g真实终态及准确付费输入

会话 Astra-new-mechanism-8cdb3418-20261128；2026-11-28。原固定 Esharp 全程未改，14次接纳后细误差仍约 .328，曲率门未过；本条不授连续或精确解资格。
## 原运行与完整原态

[run 46171769763](https://github.com/Rogerhu12/math-research-public/actions/runs/46171769763)，job **141061557951**，head `ebd6fb99d537edc6500baf8ccd33bc53cab63d01`；17:45:40 UTC自然success。原 request SHA `f28f994be993f51d9d62d2e8a19cf1fa402ff96d04ce8a764aa9503773af5c75`，原39文件/27 Python输入不变。

artifact **15274590266**，**481437487 B**，ZIP SHA `ebb897bc617788549d2f68738f080c7a3aa425f24bf8c076b0db27ee6fbd1d62`，名称 `visible-r738-paid-46171769763-1`，到期 **2026-12-28 17:45:17 UTC**。原708成员含699个kept NPZ及9文本；ledger另保2656个retired条目的原账，不冒这些历史数值仍逐个存在。原latest_state为terminal/14接受/[32,6,2]，pending=null，最后context为final_independent_cross/both。

原FINAL字面 **64333 B** / SHA `4a271c0f8df58456a66a71a59e003c5d887c07d54b8bb53290e7269625f3ff7e`；实际1882q little-endian float64 SHA `951ee71b25d7c710ece1d60b4a3e4881fd4203e5a41486212700edc70d862594`。科学fingerprint `970a9c01047f9317c9716c86637ab53342d8a0730fdc3f698d35652bcaa87158`。
## 全列实际求解和失败

| 层 | 真实空间/列 | 接纳 | 原停止条件 | 原跨网η |
|---|---|---:|---|---:|
| 0 | [8, 3, 0]/118 | 14 | iteration_limit | 0.32774125624286021 |
| 1 | [16, 5, 1]/798 | 0 | unaccepted_all_three_models | 0.32774125624285999 |
| 2 | [32, 6, 2]/1882 | 0 | unaccepted_all_three_models | 0.32774125624286166 |

首层从η .6271853460356698降至上述值；后两层完整原三模型均未接受，未伪造新接纳。真末trust **7.991926159452516e−8**，阻尼 **4553155192632.18**。全部16全J、4332实际参数列、20完整QR/SVD已付；第一层118列、第二798列、第三1882列。两步实际空间延拓的径二阶最大差分别2.5411243883814105e−10、4.0657990214097275e−9，保原值，不当作严格零。

| 原独立读取 | η | 曲率最大 |
|---|---:|---:|
| radial_only | 0.32774288458773321 | 33.449740183318404 |
| angle_only | 0.32774687835449179 | 33.450106837825601 |
| both | 0.32774839527767047 | 33.449740183318411 |

同一真圆心 **(−.0005843841817576856,0,−.04010078027856413)**。真实径向目标积分 **.17362149564836446**，长度margin **.011476534448852188**；仅必要长度为正，不意味着原方程已根。whole shell样本仍false，采样曲率超过允许上限；两个`old_input_ray_2/3`原读取等于已列角细网，不重复算两项新科学。

真实深尾整段界已经取得：内旧帽相对Gram≤1.067099150562518e−9、外旧帽≤4.898281227460317e−7，全部遗漏帽`whole_deep_pass=true`。此处只管两个实际未采无穷帽；中央全点、全相位、角单调连续证书仍false，不能以深帽界替代中央.328误差或全壳reach。实际内外六迹最大误差仍单列在原FINAL，归一夹持差.3024与D估计.9833984192602818仍是条件于完整合格壳的读数。
## 全部原费用，继承行不重计

原本次elapsed **215.57633393999998秒**，ledger累计flush **215.574130786秒**，二者重叠不相加。原各分类计数如下，保持生产者语义。

| 原字段 | 数值 |
|---|---:|
| `TSQR_input_rows_including_merges` | 1655471 |
| `actual_local_complex_shape_states` | 4332 |
| `actual_nonzero_support_radii_for_columns` | 140542 |
| `actual_physical_trials` | 111 |
| `all_material_parameter_columns` | 4332 |
| `complete_TSQR_Householder_blocks` | 2292 |
| `complete_new_Fourier_physical_J` | 16 |
| `full_QR_SVD` | 20 |
| `full_real_candidate_shape_states` | 168 |
| `native_physical_base_radii` | 11654 |
| `native_physical_new_tail_radius_reads` | 2638 |
| `new_actual_high_accuracy_RHS` | 38794 |
| `new_interval_and_deep_units` | 41520 |
| `new_segment_dense_solutions` | 140 |
| `paired_complete_physical_reads` | 156 |
| `true_base_angular_quadrature_nodes` | 952 |
| `true_base_center_quadrature_nodes` | 2809800 |
| `true_nested_shape_prolongations` | 2 |

其中`new_interval_and_deep_units=41520`按原R734基线计算，**包括已付R735导入334行**；本run新计算41186行。原8558行R734与32370行R735完整保存，继承334行原秒数.2622702979998621不算新的科学时间。原R735传输入口行政7.408788197000007秒、原已完成日志I/O1次、科学0；导行行政.23273805099998413秒、科学0。所有原重叠分类继续保留，不能与wall盲加。

原140个真实负胞稠密ODE文件、完整tail_source与四个真端口都保存。原高精度RHS38794次、140段dense解、全部41520行有序journal，不在新厚双核或单高度入口重复支付相同胞。
## 真实原成员与后续唯一接收

根在运行自然终止后一次读取日志，随后本地仅做ZIP字节传输/哈希/成员身份检查：48.15646203699998秒行政I/O、新科学0、额外原日志请求0。完整ZIP确实核过，并非只信API digest。

| 必须原成员 | 字节 / SHA-256 |
|---|---|
| `ledger.json` | 369094 / `052906fd4402899775e849b8b2eedc50784da722def835b9d212d06cbc3a58ac` |
| `r738-negative-and-deep.jsonl` | 37193443 / `fd817bd16ec54d06d70094186c5432b0696c48d48c0375faa3a1725873f392f4` |
| `r734-original-tail.jsonl` | 7643515 / `4db22d7323c1ba41df6ad28bfb5c8fd5bc1f81f738050b97b6d472c5afccd2cc` |
| `r734-original-final.json` | 144011 / `a220b21fab92536d5a50bedc6d69b43c301b2eeda9827bdacadf663b2313134c` |
| `r735-original-central.jsonl` | 28837685 / `82cff0ff51929dfc604951198655b268267bd795513f6cd5296bff3e8563f894` |
| `r735-original-final.json` | 15187 / `4de0d3e4487d963923d9bc5ee557ba33271ee0139137115fe312484048f8bf22` |

`complete_tail_source.npz`为13093 B / SHA `cc1826cc43e71c7575ba6a042dcfd06d0df7f1b40e2e17f7696d96f79e9bda20`；140个native成员的原SHA逐个绑定在新纯I/O接收请求，实际R735导入receipt也保留。

同条发布的行政接收器只搬这些已付源、原终态和必要账，给R745/R748共享。原R738 own FINAL此前仅在已完成日志中，接收器为持久化准确输入作一次已完成log I/O并验证64333 B/SHA，不重算科学。该精简输入包不是原R738通用续算checkpoint；若续原大求解器，仍用481437487 B完整原档。新接收器尚未执行，不预写其费用、run或结果。

实际科学Actions开工前公开pull到`9e0fd0ecb4b894ae7e69d75e48f9d95a539eb2d5`，两README未变；私库pull `3b2cd6783d53b0ccac3e2bd494a839b114cb9125`，根未变且QUEUE唯一为本会话进行中。根本地最新实际pull另在HANDOFF记录。

## 后续研究边界

R744只排同一水平轴源的j2小核，不排实际有限倾角场；此数值终态亦不证明该固定g没有解。R748用这份实际1882q场付一次真材料角高度迁移，保真正两径导、完整双帽拼合三Gram与物理门；R745复用原负胞，另求真实厚三肩双核。两条都不得凭单Darboux残差、只采节点或R735薄源的β冒本题完成。原R738失败与费用不撤，继续实际求解。
