# Run04 实际40返回、41早退与42未启动

- 状态：**启发式/数值证据与执行归因；未达到研究完成标准。**
- 时间：2026-11-26 19:07:25 UTC；会话 Astra-larger-e4e2a2bf-20261126。
- 实际公开执行：[45857104277/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45857104277)，job 140038237351。来源为[紧凑完整记录第004卷](2026-11-26-public-actions-45857104277-1-part-004.md)40–42；没有读取或保存大型 raw report。

## 40：原完整内部恢复和目标方向确实返回

完整内部恢复驱动源码的 SHA-256 为 `0f542de9ab1f91f5ca27a0efe315b0ee96beddd3e3972ba12fbc5140221623a6`；launcher 为 `95e90ac02f05df24b2fca7e2cdd6f3dcc051edc6ffd9973e26073a21314057b2`，实际源码提交 `b1733e2dbf9c2887be24655c8f1bc2c539d310f6`。执行1676.9229785250009秒，exit 0，complete=true。

本 run 自身的完整父 checkpoint `68b88eef24d14958476e7b52bec51c0cc395eccd6b68c1134c1eda68fd1f6c8d` 被保留为实际初始 bundle，实际末 bundle 为 `51c8b09be1b1d5baef8c0f5b18f294130727429aeb01485e1b78a72d442d509a`，10720258 bytes。原 report 为 `78fa207b9032f3455ab3037189f0896f2533e4534c8e573d67a326444f442b22`，23576742 bytes，仅 runner 保存。

实际同模型 `ac2cfc0d46a75a2070dfd9b208e3802c895a7bd35a9df5ab60d1016c81aebf19`、标量身份 `2612418a7f6dd3718ec340a37e7793bbedee0a3423f90a4a15c028cdb80492df`、jet-sum范数 `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa`。完整 M160/J923/N2048、1333370自由变量、45324288行不变。

| 实际量 | 初始 | 最终 |
|---|---:|---:|
| Phi | 0.005739450234739567 | 0.005735011506412639 |
| 最大相对Gram误差 | 0.03528317646953211 | 0.0352643275160017 |
| 最大有限几何g | 8.78834209948609e-05 | -2.310963753693329e-09 |

两次恢复方向及一次目标方向均实际接受；最终mu与恢复mu均0.01；永久曲率/半径点2005/1998，全部永久点与两个witness符号均读取。最终K乘积0.9919999976890362；body/plus/minus/cap/H各g依次为 -0.0479613784953179、-0.09215494681843728、-3.309079282357903、-0.12783450981471756、-0.9634913513738413。逆材料图根残差6.661338147750939e-16、采样rho0.1658267040402095。

这些是本次实际有限筛读数；并非连续 reach、完整精确等距或网格精化证书。停止标签是declared_metric_direction_budget，不是目标问题完成；本记录不臆造未公开的alpha或原单位Pg。实际参数保持[完整04队列](../computations/resume-20261126-followups-04.json)及此前完整重建来源，后续必须继承真实地点。

## 41：子进程早退，尚无科学归因

实际 launcher `d0ba8ccd02a811c51cd7006f1c299ad4b7eff57c195ee3a772c38fef1431a434`，源码提交 `6dbfd17cb68f54fc4d9b6dfe7c6923291449a67e`；同51c8实际父。实际5.942594131000078秒，exit 1。只产生命令记录 `f3703daa131fc54b9a8f127f1af009821334aba687120b82d46664e4345bcba8`，15212 bytes。report、initial-new-field.npz、final.npz均未产生。因此不能称SOC科学方向失败、求根失败、几何拒绝或无下降；具体原因待真实日志。

## 42：控制器依赖缺失，reader子进程没有启动

实际reader源 `9e92afc2441e18f15c48cf06d14c7827a6cfc2d864a1826d03734b418093cc28`，记录0.9117949749997933秒，returncode=null。setup_error明确为缺少41的 `so3-closed-actual-profile-cached-backtracked-SOC-first/final.npz`。null不表示科学子进程exit；它没有实际运行。

## 已继续的具体动作

随本记录提交[完整ef017纯trace参数](../computations/resume-20261126-run04-actual41-failure-trace-ready.json)，使用已存在的40末bundle作控制器依赖。它从status.json中精确绑定41记录及其真实log，仅最多32768尾字节/8000 traceback字符，无F/J/求根/数组科学计算。若只能读到外层CalledProcessError，继续读取同日志受限内层原因，不把外层异常冒充归因。当前本地exec仍不可用，未假称本地pull或测试通过。
