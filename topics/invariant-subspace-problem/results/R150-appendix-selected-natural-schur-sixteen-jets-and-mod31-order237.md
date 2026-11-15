# R150：同一自然 Schur 十六阶续接与模31阶下界237

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

[八阶证明](R150-appendix-selected-natural-schur-eight-jets-and-mod31-order184.md)已固定原 $I,J$、原自然 $u$、$4318$ 维单位块及真实 $36\times36$ Schur 系列。本次从完整八阶检查点继续到十六阶，新增七个已定正 Smith 指数；余四个至少为17，因此同一子式模31消失阶至少为237。

## 1. 同一数学对象的续接

未修改原数学 runner，SHA256 仍为
80f6815133250cf559f81afb557f138952f7268ce2d2b43e2c15bfb822775e67。
原 native SHA256 仍为
40dc42b367d241fb7d1cf0c3dd9ef35d61ad0ce756a63559ca8110188b2206dd，
输入绑定仍是
1fdb07aa85a565c45d7adfe04721a29cdbe6911cc0cb50ca45044c51f88ccc01。

实际回执明确记录 previouslyCompletedNaturalDegree=8、
completedNaturalDegree=16。旧0至8阶的来源、Schur、完整原残量文件按完整SHA恢复，只新增9至16阶，仍逐阶核原选列支撑、36自由坐标、4318单位输出和全部4367残量。没有新大消元或Dixon位。

[薄包装](../notes/2026-11-15-r150-selected-natural-u-schur-compact-continuation-789f.py)只在写主回执时建立浅副本，省去重复的4318个单位输出编号。旧数学模块的真实文件路径、源哈希、内存对象和所有输入身份不变；包装身份另记在参数中。原八阶完整回执为98033字节，本次为54740字节；这项格式压缩没有重求已付来源。

## 2. 新增精确指数与未定块

原八阶已定25个正指数，和为85。新层为：

| 指数 | 新确定重数 |
| --- | ---: |
| 9 | 0 |
| 10 | 0 |
| 11 | 3 |
| 12 | 2 |
| 13 | 1 |
| 14 | 1 |
| 15 | 0 |
| 16 | 0 |

故已定32个正指数，总和
$$
85+3\cdot11+2\cdot12+13+14=169.
$$
同一小单位 Schur 算法在16阶末留下4维余块，它的全部指数至少17。于是
$$
\boxed{v_u\det\overline B(u)\ge169+4\cdot17=237.}
\tag{2.1}
$$
零重数来自对应层完整常数余块的实际零矩阵，不是没有输出就推定为零。余块仍只在有限精度下已知，因此不把它当成恒零块或完整长度。

全部33条原第一校正仍按已付文件身份复用，哈希
b61e873692e022c4376adc32286afbb6bcc46f116e94a55c8114857e55b08bb4；
完整原乘回标志保持为真。

## 3. 实际执行及边界

实际 run **43679903558**，step **selected-natural-u-schur-through16**，
执行源码提交 **af766074f7f7c5a583d5028ec25cf934e8f726ad**。
新增数学时间 **5.094191521999164 秒**，其中 native **4.740621686 秒**；
墙钟 **5.178499729998293 秒**，退出码0。显式预算为数学60秒、内存512MiB。

临时完整回执54740字节，SHA256
081a83c48f6a04a8683869a989ede0279a7e166e1db1f5bfecd82376e72e786d。
薄包装SHA256
f699fd8598fb8340933f7938d592ffb0c088115f8086dec6a51ad2e141030ae6。
[实际小记录](../notes/r150-infinity-remote-session-789f/43679903558-selected-natural-u-schur-through16.json)保逐层完整哈希和小Smith层记录；全部可重算来源数组仅留临时目录。

本次 completeSelectedInfinitySmithLengthComputed=false。特征零完整长度、原目标的 $\mathbb Q[s]$ 成员性、指定子式首系数的31单位性仍未由这个有限域下界推出。后继在同一检查点继续四个未定方向。
