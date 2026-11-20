# 持续环境的 q=.006 再生实际返回

维护：Astra-held10-1b6d88ec-20261120；2026-11-20。

## 原事实并列保留

原公开run44718341266的H1七步已成功，见[第二返回](2026-11-20-public-material-second-return.md)。新[持续作业44720589640](https://github.com/Rogerhu12/math-research-public/actions/runs/44720589640)仅为后续实际场审计必要再生，不原先打算新增数学接受。它在首次命令 held10-H1-regenerate-20261120-01 的 q=.006 阶段真实退出2。

| 项 | 先前成功 | 此次再生 |
|---|---:|---:|
| 当前节点 | 579 | 4675 |
| 原 RMS | 9.947402870585667e-7 | 0.000001173712930211244 |
| solver_success | true | false |
| metric_l1 | 2.5223305786616e-9 | 未运行 |
| p0（delta增量） | 0.000014545509598846374 | 0.00001454550957463652 |
| c2（物理support系数） | 0.000004538900758326699 | 0.000004538900758262289 |

此次消息为“The maximum number of mesh nodes is exceeded.”，节点预算保持6000；算法在当前4675点判断所需下一网格会超过预算，不能误记成已经用了6000点。最高RMS仍约1.1737倍原tol=1e−6，不能判接受。run记录error字段为空只表示求解器正常返回失败状态，不代表成功。

两个参数向量近似相同，p0差约2.4e−14，却不是逐位相同。源码及pin的数值库相同，不足以预先判断失败来自舍入、网格、求积、执行平台或其他数值机制。当前没有针对机制的新实测，不能因参数近便把失败撤销，也不能由它推翻原真实成功或宣布物理分支不存在。

## 留在实际运行器中的断点

- WORK=/home/runner/work/_temp/held10-live。
- 原失败目录：height-path-00-q0.0060000；不覆盖。
- raw文件：inner-00.npz，SHA256 a7abf71cf17dcab0324594f6107d2ce94946e4ae1a5566742d09335bcb446754。
- run.json SHA256：281883f93e260d4f100a497f32d7d9129ddb2397e049f48ec2aac280f4f8f577。
- 原线性首DN物理残差：5.024514854495025e-7；它在H1初始化中仍欠付。
- command实际pull后源提交：3bfc61f2a85f455f8c4c3fb0d5c9a305f668b623；原worker记录complete_surface=false。

小标量原样保存于[紧凑记录](2026-11-20-live-q006-regeneration-return.json)。runner还在，原raw未上传、未被改称已接受；暂无physical.npz，因为原driver不对solver失败状态继续作C2/metric接受审计。

## 下一实际动作

读取此raw保存的原cubic、RMS峰位置、局部h、同原F的RMS采点残差和浮点尺度，再决定是否以同一连续cubic重采样到较粗的原网格作为新初猜。重采样只改数值起点，任何新解仍须过原tol、maxnodes、正根、边界和metric门。不得把失败raw或对它的只读分析叫作新的物理解；后续不必重新cold，也不重复已登记R53核检查。
