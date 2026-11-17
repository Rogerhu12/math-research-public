# 新物理端口的真实前缀重配：beta8 与 widecut

维护会话：`Astra-held10-f00f08c9-20261117`；计算与初稿 `literature_mechanisms`，主会话核对终态及独立再生端口。这是原 small-cut q20/q22 分支之外的独立物理端口实验。所有成功条目都是针对指定有限线性 DN 的真实非线性前缀 BVP；`actual_nonlinear_tail=false`。真实尾联立由 `true_a_analysis` 单独进行，不能用这里的 H 或根裕量代替尾的非线性门。

## beta8 raised-valley 端口

物理 cut 为 `r=.30,w=.08,w_r=-7w/r`，真实 worker `spacing=2`、物理频率 `2,4,...`，构造器 `hybrid_outer_cell_v1`。首两列 radial DN 为约 `D1=-185.038625018,D2=7.562536145`。所有 H 为实际 upper-prefix 的 z 高度系数；orientation=+1 的尾输入 -H、目标 -Hr，然后反射整个尾的 z 和 mean。

32 列规范端口（2048 步）的 SHA256 为

`51fca6818d36707fc7f3b0e4aa2073c891fbe67c792295ad04e0917f5889674e`。

首 8 列和 cut 字面保持原 worker；新增 24 列的 1024→2048 步相对差最大约 `5.87e-8`。频率 22 附近存在大的 DN 图斜率，不能仅凭 D 大称为几何不可行。此次均使用同物理参数的端口，512 步 raw 文件中冗余 Ep 的 1 ulp 计算顺序差异已保留原件和规范记录。

### p=.2 分支

下表只列较高角模的真实前缀结果；q02/q04 等 M8 种子另见小型进度表。

|q|角模数|metric_l1|root_min|高度|H1|H2|
|---|---:|---:|---:|---:|---:|---:|
|.06|16|4.06394e-8|.0014978389|1.29348105|-4.10696e-5|.000413263|
|.08|16|1.09066e-6|.0008334549|1.29218727|-5.30927e-5|.000539453|
|.09|24|3.62351e-6|.0001189516|1.29137401|-5.86763e-5|.000591258|

q08/q09 的物理 metric_l1 超过 1e-6，仅作为分支种子。q10 M24 从 q08/q06 secant 的尝试遇到负 Frenet 根 `-1.9524745015209177e-10`，保留失败文件，不把这次试算解释为不存在定理。

定位 q08 的最小根发生在短 bridge 最后 turn-down 段入口附近，因此下一试验只降低峰值参数 p，而不是盲目增加 q。

### p=.05 分支

新设计具有自己的 profile/chart，不能与 p=.2 混称同一目标度量。线性根 `delta=.17185516266356268`，`H1/q=-.0008732238669884929`。

|q|角模数|metric_l1|root_min|高度|H1|H2|
|---|---:|---:|---:|---:|---:|---:|
|.02|8|1.25310e-8|.0051350820|1.29928063|-1.74855e-5|-1.26637e-5|
|.04|16|2.60306e-8|.0043834600|1.29870661|-3.50942e-5|-5.07526e-5|
|.06|16|4.06010e-8|.0035221207|1.29774621|-5.29338e-5|-.000114759|

q06 最终 1271 个节点，原 tol=1e-6 未更改；中间若干轮 collocation 残差约 3.9e-6、网格增长，最终正常收敛。这是实际成功，不能把中途增长误记为失败。q06 H 的 l1 为 `.00016848291973945725`。

p05 相比 p20 的 H2 降低且改变符号，前缀根裕量也增加；但是第一模 H1/q 反而略增。true_a 的真实尾实验已显示首模敏感性，因此此改善不证明尾容量提高。随后同一物理tail端口的p05分支已实际完成q08和q10：metric分别3.48063e−8、4.36751e−8，根裕量.00258648、.00158257，高1.296395、1.294648。各点delta仍按design调整，不能混为固定完整g加密。q10的H1=−8.9493010e−5、H2=−.000331431405，完整H的l1=.000429511491。q12的一次secant试算在629.4秒后触发原Frenet域门−6.1056e−11；这不是振幅不存在界，未继续更高q。

## r=.35,w=.30 的原拓扑 widecut

父会话用原 `closing_weighted_tail_v1` 工厂在新 cut 真实重算，保留旧 valleyControls，未在新 cut 重新校准或优化；没有把旧 DN 随意替换 cut。canonical8 端口 SHA256 为

`8643af3f9392a151146f98f285d69681e0f2c1446b8899ed1a7312a53f7f72d1`。

首模 `D1≈10.2048675443`，全模式 spacing=2。背景 bridge 的比较：

|peak_fraction|线性 delta|H1/q|桥高|桥上背景根最小值|
|---|---:|---:|---:|---:|
|.05|.17143445257634238|.019018314148596286|.458680914165223|.0747254815794|
|.2|.17158581727202496|.018927932254442878|.440704505318549|.0533880093847|

优先选 p=.2，因为首模稍低且桥较短。这里 `w_r=-6`，末端子午曲率约 `5.2724382673`；背景根相对旧 w=.08 大幅提高，但真实尾容量仍由另一路完整非线性试验决定。

真实 q=.02、M8 前缀在 523 节点成功，约 33 秒：

- 实际 profile `delta=.17158372706540223`；线性 chart 文件保持上表固定值。
- `metric_l1=4.595021027110655e-9`，`flow_defect=6.860908697933612e-9`。
- `root_min=.05073361199626458`，采样主曲率 `5.281291364300785`。
- 前缀高度 `1.3536131273721108`，最大 XY 半径 `1.180314170779209`。
- `H1=.0003785999079425029`，`H2=-5.310481121266989e-7`，`||H||1=.00037913384725864424`。

完整 checkpoint、profile/chart 与 H/Hs/Hr 已交 true_a，后者从小倍数 -H 开始真实尾 warm continuation。尚未因本前缀成功而启动大批高 q 试算。

临时 checkpoint SHA256 为 `cc085b02fe9cca183ecf8aa11e428d3b6aa758926a37553224792067a5a9d625`。512 角的完整 Cartesian endpoint（含 X/Xs/Xss、角导数和 mean）已导出，数组 SHA256 为 `44fea789e88240e02236e5515b9cf8e30124d77ff025884952d4402490513b3b`。cut 的 mean z、mean zs、mean zss 分别为 `1.3532350557359614,.2873577705929405,5.0496807468997575`；这些为进一步全 Cartesian 接合检查提供数据，没有把标量 H 匹配当作全部几何条件。

## 重建与临时数据

所有 source 先通过既有 `recover_prefix.py` 和 smallcut manifest patch 恢复。当前文件布局：

- beta8 p20：`hybrid-dn-linear-r30-k4-p20`、`hybrid-dn-m32-r30-k4-p20`。
- beta8 p05：`hybrid-dn-r30-k4-p05`。
- widecut：`widecut-r35-w30-k4-p20`；未求非线性解的 p05 线性资料在 `widecut-r35-w30-k4-p05`。
- 已终态的高模式/secant命令与逐文件hash在 `scripts/nonlinear_tail/ports/hybrid_terminal_commands.json`；初始 M8 sweep 与 widecut q02 命令在各目录 `continuation.json`。
- `hybrid_prefix_progress.json` 是当前成功行的可更新小型索引，标明 port hash、q、p、g、metric 与 checkpoint hash；本 Markdown 是已完成结果快照，不随该索引隐式改写。

widecut 从零重建的首个命令为：

```sh
python -u smallcut_prefix_sweep.py \
  --repo math-research-public --recovery smallcut_highq_work/recovered \
  --output smallcut_highq_work/widecut-r35-w30-k4-p20 \
  --radius .35 --port widecut_tail_work/widecut_port_m8.json \
  --curvature 4 --peak-fraction .2 --vu .55 --vd .6 --cycles 1 \
  --stages .02:8 --tol 1e-6 --max-nodes 4000 --stage-timeout 3600
```

临时 checkpoint、系数、端口数组与 endpoint 只供当前计算消费；持久交接保存源码、恢复命令、物理参数、哈希和必要小型结论，不复制可重算数组。

## 独立重建及恢复入口修复

主会话在空目录独立再生了32列端口，逐值比较历史 `51fca681...` 输入：物理参数、cut和全部32列严格相同，最大差为0。新JSON的元数据路径不同，SHA为 `71a27570137b8c5b6397b74319f6d02384470b1afa9d0242f215c8992eb0ee4c`；这不改变数值列。首8列保持原worker 512步的字面值，其余列2048步，未偷换同g。

该空目录测试发现两个复现细节，现已修正。发布参数中的 `valleyControlsPadTo=160` 必须先展开为原160项数组再去掉辅助字段；转换后的配置SHA必须与原 `c4dc0f98...` 相同。另，早期stage1的39源子清单缺必需 `.cjs` 工厂，不能单独启动worker；默认恢复改用已核验的完整71源清单。初次ENOENT是恢复器依赖缺失，不是数学失败。

完整命令（输出必须在仓库外）：

```bash
python topics/visible-flex-held-10pct/scripts/nonlinear_tail/ports/reproduce_beta8_port.py \
  --repo "$PWD" --dest /absolute/scratch/beta8-port \
  --stage1-dir topics/visible-flex-held-10pct/scripts/nonlinear_tail \
  --linear-script topics/visible-flex-held-10pct/scripts/nonlinear_tail/ports/hybrid_linear_port.mjs \
  --export-script topics/visible-flex-held-10pct/scripts/nonlinear_tail/ports/export_hybrid_ready_port.py
```

前缀求解继续使用已发表smallcut_prefix_sweep.py、smallcut_secant_launcher.py及终态命令表；q10的可执行重放命令明确标为由冻结q08模板、q10配置及两前驱checkpoint重建，没有伪称保存了原argv。widecut的完整物理配置/实际尾与另一个优化端口在widecut笔记和源码目录；它们的结果不能拼接到本表未闭合的高q前缀上。
