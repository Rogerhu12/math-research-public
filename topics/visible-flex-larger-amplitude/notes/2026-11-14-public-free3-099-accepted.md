# 公开 Actions 真正接受 free3 到 s=0.99

状态：完整有限正 Gauss 前缀接受及两档实际 C² 读出；尚无完整尾、闭面或完成声明。

## 实际执行与复现身份

- 公开 run [43580643038](https://github.com/Rogerhu12/math-research-public/actions/runs/43580643038)，job 132404442113，源提交 `be989410a0149c2d5b24feec5b32ba3f93ad5c70`。
- 输入是原接受 .984、完整 M96/N1024 文件，SHA256 `3ac8c8efa20670342021487a197443f6e1b2ad60f35c7bf2864f355a06424b69`；只固定前三核心系数，完整其余93模进入原方程。
- 原93行 principal normal 设计边界、RMS `1e-6`、BC `1e-11` 门保留。第一段实际 solver 与两项后处理均退出0。
- 新完整实际场：[actual.json.gz](public-actions-43580643038-1-free3/stage-00/actual.json.gz)，SHA256 `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`；全部 profile/projector/seed/argv 和日志保存在同目录。

| 检查 | 实际结果 |
| --- | ---: |
| 物理末端 / 节点 | 0.99 / 423 |
| 连续 collocation RMS 最大值 | 5.457043306587111e-7 |
| 完整边界残差最大值 | 3.469446951953614e-18 |
| 1024角、径向每段2分的 C² 候选 metric 样本 | 5.773683280363429e-7 |
| 2048角、径向每段4分的 C² 候选 metric 样本 | 5.773683280363429e-7 |
| 上述两档曲率最大样本 | 6.300837559915685 / 6.30137675013796 |
| 反射前缀直径样本代理 | 3.5003721203366602 |
| 球排除见证距离样本 | 0.9600009804543665 |

两档 metric 最大值都在真实末端，不能据此声称整个场已对网格/频率精化到机器精度。这里的 D 仍只是前缀样本代理，不能作为最终完整闭曲面 D。

## 新核心自己的准确证书

[core-certificate.json](public-actions-43580643038-1-free3/stage-00/core-certificate.json) 用全部96个实际 binary64 系数作为精确有理数，应用 R237 的完整界；没有沿用旧核心的下界。它给出

$$ho(\phi)>0.163850119893507701819938,$$

以及准确轴见证差

$$0.960000980454366525895946<G<0.960000980454366525895947.$$

这证明该有限平面核心严格凸、材料圆变换为微分同胚，以及核心轴见证的准确距离。它没有证明后续整个前缀都在排除球外，也没有证明完整闭面的像 Hausdorff 下界。

## 第二段未启动 Newton 的实际原因

原计划第二段 duration .012，在 `normal_bvp_continue.py` 用 Taylor2 外推点构造末端 projector 时，原门
`Principal elliptic boundary requires strictly positive sampled det II and nonzero II_phi_phi`
拒绝初猜。完整 [prepare.log](public-actions-43580643038-1-free3/stage-01/prepare.log) 保留。它是预测点的失败；既不是新 .99 解失效的证据，也不是完整边值问题无解的证据。

`geometry_20261114_public_free3_adaptive.py` 从已接受 .99 原文件接续，先检查实际末端的同一 principal 门；只有预测门失败才二分步长。真实 Newton 不接受会单独保留并返回，绝不改变残差阈值或把失败改称接受。若实际入口已经不在该 principal 域，就转完整 DN 主线，不靠无限缩步掩盖。

## 同时完成的 fixed32 对照

首批 run [43579782197](https://github.com/Rogerhu12/math-research-public/actions/runs/43579782197) 从原 ENOSPC 检查点恢复 fixed32 问题，实际321.75s 后未接受；5次 Jacobian 后回溯失败，连续 RMS 为 `5.936121846280139e-5`，需求764节点超过640上限。BC `3.3881e-21` 不能代替全域残差通过。原423节点 actual/checkpoint 和完整日志已保存在 [fixed32 结果包](public-actions-43579782197-1-m96/publication.json)。

没有把这次真实失败称为 OOM、ENOSPC 或数学不存在。下一步使用已经成功的 free3 分支及完整非均值 DN/真实 scalar 设计，不重复成功 .984→.99。

## 发布恢复

两个计算的 artifact 均完整。原自动提交失败仅因随后 `git pull --rebase` 缺少 committer identity；提交命令自身设 identity 不足以覆盖 rebase。修复为所有 Git 子进程设置临时作者/提交者身份，不在文件中保存凭证。这里恢复原 artifact，未重算或改动原数值结果。原 run 的失败状态保留，与第一段实际数值接受分别记录。
