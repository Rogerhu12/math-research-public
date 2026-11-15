# Actual74：完整字节读回附记

类型：既有数值证据的字节完整性附记。  
作者：ChatGPT / amplitude。日期：2026-11-15 UTC。

## 结论与来源

第 74 轮只读 Actions 已完成完整导出原件审计。本附记把其中五份原报告副本、四份此前公开报告及实际新 warm 的字节身份再次对应起来。未重新下载 625 MB 原科学包，未执行新的矩阵动作、范数、优化或科学验收。

原科学 run 为 [43659610548](https://github.com/Rogerhu12/math-research-public/actions/runs/43659610548)，source `145d7a53ec05a64d39d0a36ac3e441e3475cb9bf`，原 artifact14139672567 为 625544155 B。只读 run 为 [43660861684](https://github.com/Rogerhu12/math-research-public/actions/runs/43660861684)，job132649649559 全部成功，source `178a1031a41ef6ebac243cdb28220febbb995e12`。根已取得其 918235 B 小 artifact14139424448；本地完成标记与 GitHub digest `126c302d21964dc2cdd28c24632867812b0fe57838d4a51eaaef0f752f70949e` 相同。

完整 Actions 审计在 `request74-readback/large-arrays/complete-original-byte-audit.json`，791537 B，SHA256 `2ef0de58d5234a336feed45b84ef25b97209286740ad9e3f2832d2bc052ed8de`。本地只做标准库读取、流式 SHA、字节相等及原整数描述器对应，见[原件对应回执](actual74-completed-reader-addendum.json)。保存的小主摘要为62958 B，SHA256 `69bdf5b7e79a5a89f7f884dafd026099f6e9a66ce7a313bcc1ea5fb98afff0b6`。

## 23 组实际查询和完整支持

本轮是15组 left-RMS 加8组原collocation midpoint，每组2048角，共47104行。新增的是 **midpoint484**，而 left-RMS484 已在父场中；本轮没有增加下一步计划的 left-RMS485。当前中点顺序为473、475、477、480、481、482、484、485，所有typed行身份逐块对应。

声明局部坐标与实际编译列并集都为7101：21个物理节点466至486的338维状态及3个全局control。`zero_layout_nodes=[]`，零布局列数为0；节点484早已具有真实B列。新增中点复用既有端点484/485，捕获支持未扩大。全部23组的679列映射均逐项对应完整局部索引。原C投影仍只有4059维修正支持，与完整B和完整H恢复的支持分别记录。

实际B模型身份为 `3f45cfe3e690d3e5c97f9712bcdeae3a973909d1d63acff2432ad443a3acaedb`。这项身份和整数映射核验不代替原非线性域检查。

## 已完成的字节范围

| 原件范围 | 完成的 Actions 读回 |
|---|---:|
| domain NPZ / 内含NPY数组 | 207 / 1340 |
| condensed NPZ / 原数组引用 / 唯一完整数组 | 108 / 42 / 38 |
| 凝聚与恢复raw文件 | 14 / 415120992 B |
| 实际源码SHA对照 | 68，缺失声明0 |
| 原collocation observer报告 | 19 |
| 原midpoint observer NPZ | 10，全部有匹配原descriptor |

domain检查包含完整B/Gamma/Pi分块及其拼接身份、原beta、mesh、y/RHS、尺度、原中点输入和原捕获端点J/P。condensed检查保留所有完整数组组成部分，没有截断basis或省略引用。14个raw包括原g、局部索引、完整仿射列及误差、7101维局部平方根/仿射项/梯度/中心，以及实际恢复向量、请求右端、局部不匹配和原H残差。上述是原保存字节的核验，没有重新形成A/B/H或求解。

原observer账记19次原evaluate、1次原weights和0次observer错误；没有额外RHS、J或trial调用。原实现检查值也保留：adjoint error `6.141641548294503e-18`，local/full action error `0.0`，完整complex-chain relative error `9.106907701188957e-13`。这些值由原科学运行产生，本附记只核对应关系。

本次68份源码是完整artifact读者的覆盖范围；正式主报告的60份是此前五原件的primary来源覆盖范围，两者不能混称同一清单。

**完整链QR因子只在原进程内存中，原producer没有导出其全部数组。** 14个raw的审计不等于完整QR因子文件的独立审计，也不是重新检查完整原矩阵。回执明确保持 `full_factor_files_independently_audited=false`。

## 原科学结果与父pair保持

status、model、comparison、QP summary、FD五份原报告副本的完整SHA均匹配原descriptor。其中status、model、QP summary、FD与此前公开取得的原文件逐字相同；实际新warm原压缩字节亦匹配原descriptor。

新warm SHA为 `204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3`，status解压后原SHA为 `09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73`。真实父仍为实际72的warm/status双SHA和完整producer子树。

原`accepted_warm_steps=1`、`success=false`、`new_coupled_finite_acceptance=false`不变。实际接受步长仍为1/64；最近1/32的原节点、中点及23组查询有效，merit实降，但left-RMS485失败。原affine FD四阶误差仍为 `1.1187325453132574e-9`，绑定新warm；不把它写成该新H的真native非线性DN已解。

本附记补充[第74轮正式数值结论](2026-11-14-actual-request74-twenty-three-query-nearest-left485.md)的完整导出字节范围，保留其原试步与下一最小决策。不重跑原科学，不增加第76轮或后继的科学门。
