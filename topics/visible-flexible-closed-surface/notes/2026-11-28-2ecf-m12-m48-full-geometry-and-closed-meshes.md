# M48第三实场：全域两jet、全时几何及完整三时刻闭网格

新M48场 `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61` 的连续几何已实际付清。它不是首场/C2第二场的系数，也不借两场的reach证书。本次调用原R249与R253数学定理及冻结消费者，原源仍X+C、原g/物理参数/全相位范围保持；R250的Q没有加入。

此前[局部cross-Gram](2026-11-28-2ecf-m12-local-p-slope-cross-gram.md)已给本场全域全时metric≤9.963039080e−7。本条加入同一field自身的全时reach、held、固定H及全部帽/真cuff，再真实生成三时刻完整网格。README #5的固定g实际加密收敛仍未完成。

## 1. 完整原R249实际消费

独立进程自然退出0，生产者内部1385.962970371秒；487原径向元准确覆盖为629个Bernstein子片。128个全角盒、8阶Taylor及96bit有向整数包络、全部共用五次Bernstein权重保持。采用原默认 `--max-radial-depth 1 --quick-first 0.0000004 --quick-second 0.01`；这些是预算工作阈值，不是非线性残差或几何验收阈值。

| 已证同场全域量 | 保守显示界 |
|---|---:|
| 位移η | <1.928313e−7 |
| 目标正交微分p | <2.112564e−5 |
| 材料二jet修正cW | <.004841524 |
| 原三角metric上界 | <4.227745e−5，仍未过1e−6 |
| 全闭面直径D | <3.787021 |
| 法支撑下界 | >.73687939 |
| 原R249全局CX转移reach/D | >.03017652 |
| held/D | >.05278311 |
| 固定帽diamH/D | >.93545832 |

原R249本身已经支付全时reach>.03、held>.05以及全部法管条件。原三角metric字段保留，不改为通过；metric门槛由同场完整cross-Gram的独立证明付款。

## 2. 同场R253分区法向进一步收紧

R253再对全部158个可能涉及prefix/准确交界的原片实际求全角微分界；真实总进程23.527220319秒自然退出0，生产者内部23.120375199秒。准确跨cut覆盖采用超集，不把不确定交界排除。

本场得到

\[
p_{\rm prefix}\le
\frac{15577315384557681524131}{39614081257132168796771975168}
<3.932268\times10^{-7}.
\]

以原prefix CX>4461的完整上界、tail CX的原26向外上界分别支付法向变化，原全域cW、η、support及度量浸入预算保持：

\[
K_{\rm prefix}<8.473022,\qquad K_{\rm tail}<8.469407,
\]

从而严格全闭面、全相位

\[
\boxed{\mathrm{reach}/D>0.03116477,\qquad
\mathrm{held}/D>0.05278311.}
\]

整个闭面嵌入、固定有内区域H、帽上全部标记及含反射的δE>0由同场原R10/R16转移条件保持；不只是局部曲率界。held按整个闭面图像距离，D按整个闭面直径，没有缩窄分母或把某个材料点位移冒图像距离。

这次较强reach界来自区域预算与新场实际较小cW，不是新增Newton步。M48真实独立G8/N1536的有限metric峰约6.07253e−10；仍不能用它或正则normal宣称准确等距及#5完成。

## 3. 三时刻完整闭网格

新入口 `2ecf-m12-certified-field-closed-mesh-v2.py` 保留原完整STL生产者和全部field/grid/result绑定，只增加对已证明的局部cross-Gram消费者SHA的明确支持。原v1及其已发表两场网格身份不改。输入必须同一实际field的完整metric报告与R253几何报告，并实际通过全部门槛。

自然OS退出0，外部10.406417849秒，原网格生产内部9.429936918秒。每时刻仍为216均匀材料角、每侧prefix64段/tail32段，准确尾半径选自同一源cache，反解真实native角，完整中央/过渡/有限尾/深collar/上下封帽均生成。

每份44,714顶点、134,136边、89,424面，Euler数2，所有边有两个反向邻面、所有顶点使用、环带/两极扇连通。固定帽3458顶点三时刻序列化float32逐字相同；中央/真cuff数值缝隙0，内部cut最大1.242e−16。全部三角形非退化、正有向体积、二进制读回一致，顶点float32转换实测差<5.961e−8。

| 时刻 | STL SHA256 | bytes |
|---|---|---:|
| 0 | `ce058bc05a3d61a76d6049b4dd56d406f5eb32384c64bb4704cdccf44a50140a` | 4471284 |
| 1/4 | `61a994d01d49333963c0ca88df42690c7e9eebd82d27a286206b95aa14dfa94f` | 4471284 |
| 1/2 | `3c1d9bfeab9837f438fe420b281ffac7a6f9bcc80324aa865957bf880068daae` | 4471284 |

拓扑和浮点检查是有限网格事实；没有把它们当作连续插值误差、自交排除或真实加密收敛。清单中的 `READMEComplete=false`、`fixedMetricRefinementGatePaid=false`、`continuousVertexErrorCertified=false`、`discreteSelfIntersectionCertified=false` 保留。

## 4. 身份与重生

| 输入/输出 | SHA256 |
|---|---|
| M48实际field | `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61` |
| grid | `5f366284b435c8911fa1bddcc9bef4cc92c646f06730a959bd4c773b4c3cd7cd` |
| solver result | `c0ca3ce3832b12c188dca87218d87639cbe266c27c129323505ad1d12225b9c2` |
| 同场R226 | `565a8a5b49e3352cbf09cb5f0bfed4cd0c37ea8348cc1299d46256979bd57d0d` |
| 原全域source-bounds | `3b7c5eeb532c08e7be10f0a3bdce70e739f15316bd8fa264eaaa7b287db483b2` |
| 本次完整R249 | `47720443469edede69e9b583d9fdd4d4f7006182170dfe98c04f3dd9e66a2f93` |
| 本次完整R253 | `be40e6c9f02c5b3f0c1d0e0cbce79aaa52204d52555ea55316ef134d6db622bf` |
| 同场完整cross-Gram | `da4cdc5c98c68aca4f82433b0672ea6fdbb0a31fada016676ca6dc13963e5f7e` |
| 网格v2入口 | `4de40ab1648075ef1804e5d72218deff45f7d6a4156ebbb1a73627739ebad476` |
| 完整网格清单 | `b0b50110b88751dbf515fc7831386548fc02b4090f4b1434cc0016fed2d368cb` |
| R253/网格两进程回执 | `7759a595f999bc7cce89f2c387c1199f8abfb9d8a9a1fea3cf3c867fcd6678ea` |

用上述原M48真实solver输入（C2 736径向列、M48全146角列、107456未知数）重生后，按R249及R253入口运行，全部参数为原默认，R253实际消费本次R249输出。网格命令与[两先前完整场](2026-11-28-2ecf-m12-two-certified-fields-complete-closed-meshes.md)相同，入口换为v2，field/grid/result换到 `h2-c2-m48-03`，metric换为 `h2-c2-m48-full-cross-local.json`，geometry换为 `h2-c2-m48-03-regional-geometry.json`，输出必须新目录。源query/report/cache及全部帽参数保持原身份。

R249源码SHA `c7e5f4c82616ed43103e234ca774a6e5e95cb46e93dc18c6b2463654911fb632`，R253源码SHA `0b62fcd84c7e19155197d6a2719ecd7484ecf515ca5f469fe4d56e52ea921296`，原完整STL源码SHA `0dacc33668048a650e0d7aec63ba57f3906c70e0a247852bf2df0e64f9d6fbfa` 均未改。

曾并行启动一个更粗预算的性能探索；上述完整细预算返回后即实际取消它，工具exit130，只有200片进度、没有完整报告，不作为任何证书或数学失败。没有取消真实新场求解；G12的独立SIGKILL和保原目标的内存修复另记，M64/物理h真实加密继续。

依根README，只将源码、本说明、参数和哈希提交；完整报告、数组与三STL均只留临时可重生数据。
