# 2026-11-26 run04 实际46/47：第二个完整后退锚 SOC 真接受，同目标误差继续下降

## 1. 唯一实际范围和来源

本条只登记公开 Actions [45857104277/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45857104277) 中真实返回的阶段46和47。控制器索引在 **20:44:18 UTC** 记录二者均 completed / exit 0。阶段46是从真实阶段44的完整末场继续的一个新全变量方向；47是对该已返回报告的完整纯归因。既不将 iteration_limit 叫收敛，也不继承旧场的连续几何证书。

全部实际命令、输入、队列、输出、清理元数据和紧凑数值保存在[第5卷完整公开记录](2026-11-26-public-actions-45857104277-1-part-005.md)，其实际 Git blob 为 `b517cfd2eeaea926bd281ea73d0f72fea533cd64`。本条没有经连接器读取大科学报告、NPZ 或逐点数组。

| 项目 | 实际身份 |
|---|---|
| 科学阶段46源码提交 | `829a597e67e9e21c4e63f71b17329aac8d5a5a99` |
| 完整科学驱动 SHA256 | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| 完整 launcher SHA256 | `6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e` |
| 纯归因阶段47源码提交 | `7e8375e7a19529600de7f6561b526ce02b99d618` |
| 完整纯 reader SHA256 | `009e1e1d54ccd41e8ac2b4e6efe43541ebc327b7a6f3d4fa743e145517c897e6` |
| 原全行 helper SHA256 | `e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021` |
| 原投影源 SHA256 | `a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e` |
| 真实执行队列 SHA256 | `afdfa2ad0bfdc9735323b98e51be9970d7fab18b53d1e8665b243ab7b14e8783` |

阶段46报告 schema 是 `complete-normalized-parent-cached-interior-separated-SOC-v1`。阶段47 schema 是 `actual-complete-normalized-parent-cached-interior-backtracked-SOC-readout-v1`，其 `whole_body_match=true`。这仍是原 normalized-parent、jet-sum 范数的892f分支；不能把结果重标成 direct 7f/integral 分支。

## 2. 同一固定目标、范数和真实起点

| 项目 | 实际身份 |
|---|---|
| 冻结基础父 bundle | `fcce34129466c5e19df169308c38b76795feff7f7b2384bbcdb10189461d6375` |
| 实际 restart / 新初点 bundle | `9c9f4726d6f6edd23bb874e84aa0f7de91347729de408a11eb5073c3f808a011` |
| restart 的阶段44报告 | `08e30bd4176b73697a9008904bf23d5fecb0a46bcc493f06463299c877679fa5` |
| 完整模型 identity | `ac2cfc0d46a75a2070dfd9b208e3802c895a7bd35a9df5ab60d1016c81aebf19` |
| 固定 scalar metric identity | `2612418a7f6dd3718ec340a37e7793bbedee0a3423f90a4a15c028cdb80492df` |
| 原完整坐标范数 identity | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |

新 `initial-new-field.npz` 的实际 SHA 就是上述9c9f，故没有在本次继续中替换起点。完整自由变量数仍为 **1,333,370**，原全度量观测行仍为 **45,324,288**。实际参数保留 N=2048、angle block=8、radial integration order=8、jet-sum、radial norm length=.05、angular transition=24、4个Torch线程、全部原192几何行选择责任及完整幅度行和真筛。

外层声明1个metric方向、内QP64次advance；restoration仍最多4个方向、每次64 advance。metric和restoration阻尼都明确 .01。谱损失仍 p=4、epsilon=.001、scale=.05、legacy fraction=.5。完整ray15次、SOC最多8轮、tau=0、内缩比例.125、全行可行性容差2e-11。reach ratio .03、安全因子 .992、marked diameter预算4.2、witness下预算.9、height floor1.01和restoration interior margin1e-8全部保留。参数完整原字见第5卷，不用本段缩写替代可复现argv。

地点输入包括原完整准备manifest以及真实阶段39、40、44完整报告。新地点仍在同一实际父上重读和重建导数，不能复制旧场的物理值或协向量。

## 3. 实际下降与真接受

| 读数 | 实际初点 | 实际末点 |
|---|---:|---:|
| 同一 Phi | 0.005665053856316854 | 0.005135593635366869 |
| 最大相对 Gram 缺陷 | 0.03513609110016425 | 0.034109509524516045 |
| 最大真实约束 g | -3.6401591740897743e-7 | -3.72901331765485e-5 |

实际完整有限几何筛返回 true；末场 `all_permanent=true`，曲率永久位置 **2155**、半径永久位置 **2070**。本次 **1个metric方向、0个restoration方向**；阶段47明确统计 **accepted_SOC=1、accepted_ray=0**。因此本次接受由真实纯报告明确给出，而非仅依据方向列表长度推断。

实际末 bundle：

`0c9afcc4971d66b3021bdc11360c6f303c0218d7cf6e14297d85128f3a20bade`

对应 runner 路径：

`so3-closed-actual-profile-cached-backtracked-SOC-v2-second/final.npz`

完整科学报告：

`so3-closed-actual-profile-cached-backtracked-SOC-v2-second/report.json`

报告 SHA256 为 `606e10f8622ab830c122f38c5530e292bf932e2daf2831fb18c12c832b6445a3`，大小 **23,813,424 B**。科学 final 和 initial NPZ 均 **10,720,258 B**，只留runner。命令记录 SHA256 为 `14a14691297bab76fa09edbc900eefbf9a5029adaaa91c03d7a39f856fc06d10`、**16,228 B**。

## 4. 全后退锚 SOC 的实际行为与未收敛内层

本次已通过原ray的 fallback 为 **alpha=0.0625**；最近较大、真实损失下降但几何拒绝的锚是 **alpha=0.125**。完整同父策略从该已观察锚开展分离修正，实际有 **3个SOC真候选、3次投影**，之后 **1次最终候选完整重读**，最后接受类型为 `complete_separation_SOC`。纯报告的 `metric0_alpha=null` 保持原义：被接受的是完整纠正向量，不能冒作一个原ray步长。

这些计数不单独解释前两次修正的具体拒因。第5卷未公开每一轮的全部地址或物理家族，不能从次数推断“都只是同一曲率地址”或把锚值套到修正后的真实Phi。完整892f控制流和纯全body核保留：固定父x、固定锚d、原C前缀和所有追加行、每个候选独立Az/模型/Phi、拒绝后新增永久位置，以及最终候选对最新完整永久集合重新真筛。

| 内层读数 | 实际值 |
|---|---:|
| QP状态 | iteration_limit |
| advances | 64 |
| 投影梯度范数 Pg | 1.4153405937721322 |
| 实际停止容差 | 4.422998593569917e-6 |
| QP实际秒数 | 1170.8562992379993 |
| 整个方向实际秒数 | 1631.1895117169988 |
| 最终metric阻尼 | 0.01 |

Pg仍远大于容差；这次完整真下降没有解决内层驻点责任。亦未将一次全已知点可行提升成连续全域几何证书。连续认证与题目完成字段均明确 false。

## 5. 实际缓存和成本

本次使用同run阶段44的已完成 frozen-parent cache，旧50a9完整源核身份和实际文件字节，没有把跨runner旧raw或SHA当数据：

- 实际复用 **1649** 个缓存文件；计划缺失 **0**；实际新建 **6**。
- 纯reader实际核验 **1655** 个缓存文件。
- 缓存adoption设置实际 **6.632252169998537 s**；完整场设置 **361.8638525309998 s**。
- 新完整缓存manifest SHA256：`36106396a792eae71de2c108b4b57b0e827a0cc2a3a0fe04dbf48e9944a2b764`，`cache_completed=true`。
- 驱动总时间 **1999.1393993799993 s**；外层科学child实际 **2004.633996777 s**；纯reader实际 **5.939124301001357 s**。
- 峰值 RSS **3,065,600 KiB**。

阶段47纯输出位于 `postprocess/so3-cached-backtracked-SOC-v2-second-summary.json`，SHA256 `aa38318914668f1a67a81221ee6f0cc7c0cd313dac3d6ab6797736d0cb7ea2e7`、**205,673 B**，仍只留runner；这里仅消费公开小卷中完整声明的标量。46和47的 `summary_errors=[]`、`missing_outputs=[]`，没有据缺输出补值。

## 6. 实际后继责任

这次结果支持在**同一真实0c9a末场、同892f完整源、同固定g、同c4b2范数、实际mu=.01**上继续完整方向。已经准备新的完整两步参数文件 `resume-20261126-run04-actual46-backtracked-SOC-next64-ready.json`，仅换fresh标识/输出、restart及缓存donor为真实46，增加46完整报告为永久地点来源；原39/40/44地址和所有数值参数、变量、阈值均保留。该参数准备不等于后继已执行；实际准入和返回需另登记。

当前最大的相对缺陷仍为0.034109509524516045，距离README全域1e-6完成要求很远，尚未有全t几何/最终同g精化结论。本条登记的是一次新的实际全空间下降及完整有限筛通过，不是研究完成。
