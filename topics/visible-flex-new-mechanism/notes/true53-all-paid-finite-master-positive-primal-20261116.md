# true53：全已付有限主问题首次求解得到正收益方向

**分类：数值证据。** 同一个原物理点与原有限约束模型，在新的中心路径方法下得到
满足全部已知行的正 finite gain。这既不是全网格下降证明，也不是新的实际曲面点。

## 1. 原始运行、方法与约束

[实际 run43817336585](https://github.com/Rogerhu12/math-research-public/actions/runs/43817336585)，
research job `133132261671`，源码提交
`de1c7d5a2dfa7b82d63c8e98f460eea269dbdeca`。
[请求](../computations/request-true53-paid-master-central-path.json)
6123 B、SHA `295f3fe94a214d5f16cff80b6ee402c458d15e01d494c3ca07b18c5949085a9d`；
[设计](true53-all-paid-finite-master-central-path-design-20261116.md)。
源码 `frame_metric_true53_paid_master_{input,central_path,audit}.py` 与独立新 workflow
均由请求清单绑定。前一次仅 BOM 输入失败的
[5.828010012000021 秒](true53-paid-master-input-bom-failure-and-same-scope-resume-20261116.md)
完整承接，同一 1 LP／96 迭代／192 系统／240 秒上限没有重置。

原点 accepted53、物理 SHA
`9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e`；
原 MODEL binding
`e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1`。
MODEL 直接读取旧 run43811870681 原始 stdout，未重建 geometry、hard J、
selected soft gradients 或任何旧求解器。

新有限 LP 一并保留：

| 行 | 数量 |
|---|---:|
| 原 hard guard 行 | 2937 |
| 原 163 物理盒与范数行 | 652 |
| 原 160 外界上、下界 | 320 |
| 原已选 metric gradients | 5743 |
| 旧分离已付新增 gradients | 5 |
| 原常数 target | 1 |
| 总计 | 9658 |

变量为 $(z_{159},h,\gamma)$，真实方向 $p=\mathrm{step}\,z$、
收益 $d=0.001\gamma$。范数罚系数仍 $\mu=10^{-6}$。
矩阵 SHA `e2863c9bb22ab35a0c6e018205347e5c79ebb5d8258d88439c1844a3e0e0e29b`，
rhs SHA `1d2840d6d35d4935d554c6586c3a639d288ece560e8f59237962509e695be38c`；
四个字面零行已保留检查，9654 个活跃行进 Newton 系统。
没有删除 hard 约束、放宽原 target、重置学习参数或选点。

## 2. 原求解结果与修复后的有限候选

唯一 core call 完成 **34 次 predictor/corrector 迭代、68 个 Newton 系统**，
原始状态 `converged`，没有系统失败。最终：

- 原 gain 坐标 $\gamma=0.0070414711457307145$；
- 原 gain $d=0.000007041471145730714$；
- 原 primal equation infinity residual `2.220446049250313e-16`；
- relative primal residual `2.220446049250313e-16`；
- relative dual residual `4.2039798066265244e-10`；
- relative complementarity `1.8649112361296705e-10`；
- 全部原始行的正向 violation 及 tolerance excess 均为 0。

按实际线性方向重算 $h=\|Kz\|_\infty$，再以所有 5749 个 metric 分支
取最小余量，得到实际记录中的修复：

$$
h=0.25000001109908276,\qquad
d_{\rm finite}=0.0000070414711481267545>0.
$$

修复后最大原 domain 残差为 `2.7755575615628914e-17`，
最大 metric 残差为 `1.0587911840678754e-22`，
分别通过原 `1e-7` 与 `1e-9` 门。减去范数罚之前的已知分支
最大 affine metric 值为 `0.26600785275869476`；
这不是全网格值或 actual metric 值。

原始完整方向仅保在原 stdout：

| 向量 | 长度 | array SHA |
|---|---:|---|
| 原最后 finite iterate | 161 | `49789bf7828bddaeede9c3a17a8be09a748bb6a4c7a62b0b13287ffedc0d16b5` |
| 修复 finite iterate | 161 | `2b1d6922b274f722826ee1b4fc465963fd849a99e91e48ba96ecc28270c1d5e1` |
| 未圆整独立物理方向 $p$ | 159 | `3fade7f704238c45a9eca095af36035ab10c4741e059d000359cc9d0600f5e09` |
| 线性 163 物理步 | 163 | `73b14d7683879611bdaa9ec400863a1337fce34dd3b1d95348f8ec7d41d2c710` |

不在 Git 复制数组。新阶段直接读这个已付方向，不重新求一次相同 LP。

## 3. 对偶诊断的精确适用范围

原始单位 $\lambda$ 非负，$\nu=\lambda^\top a_\gamma=
0.9999999999807787>0$。
原 finite box 的支持函数给 binary64 严格行模型上界
$\gamma\le0.0070414743227693805$。
同时把每一真实 bound 行按其原 tolerance 向外展开后，
含所有行容差的同式上界为
$\gamma\le0.0070490483076691675$。

这些数值按设计中的弱对偶恒等式计算，保留非零 stationarity 修正；
**没有 outward rounding，不是区间最优性证书。**
它们只约束这 9658 行的 finite LP，不能排除更大的完整非线性下降，
不能宣称驻点或主课题不可行。

## 4. 费用与已付边界

本进程科学耗时 **8.304766884000003 秒**：
原日志读取与输入验证 `7.177843099` 秒，
新行装配 `0.06254533899999615` 秒，
唯一中心路径求解 `0.7324902120000019` 秒；
未分项部分为 imports、诊断、编码与输出等。

加前次真实输入失败，本新 finite 任务累计
**14.132776896000024 秒**；原祖先加本任务累计
**1608.573003992 秒／128 个 ordinary values**。
新 geometry、hard J、JVP、gradient、scalar、actual trial、actual acceptance
均为 0；原大日志因失败共读两次，如实保留，源数组没有二次科学生成。
完整 result 与 complete 输出后才采 FINAL_CLOCK，费用不漏输出。
旧 HiGHS64、cone32、旧 Hildreth/分离任务仍保持原结果与账户。

## 5. 下一个科学问题

立刻消费该确切新方向，恢复必要的原 current53 一阶输入
$(U,T)$ 并算完整两个原网格上的新方向 JVP。
原 MODEL 已有 $e,f$，未保存 $(U,T)$；只恢复这次必要输入，
计入新方向阶段，保留可复用的一阶 cache，不重新生成旧 hard J、
普通位置/曲率几何或既有梯度。

完整分支若通过，再接原 scalar guard、原 exact163 盒及
binary64 实际圆整、完整双网格 actual 接受门；
若新全网格 attainer 使 finite gain 失效，保留其确切新梯度并据新证据
继续下一 finite 问题。不能把旧 23 次分离的已付失败或当前 finite 成功
冒成当前完整网格结论。

实际点仍是 accepted53，原 target `.26` 仍未达到。
主课题的共同度量精化、全时嵌入、reach 和握持位移门仍未达到。

## 6. 实际 pull 与已读规则

本 run 科学前公开 actual pull：
06:31:53.446100 → 06:31:54.156116 UTC，
`de1c7d5a2dfa7b82d63c8e98f460eea269dbdeca` →
**`ed935a62fc7b1f5b266ce3de05723a4d021bd7b5`**，返回码 0。
根与本题 README diff 都为空，原 blob 分别
`21bd547f56590b7f2dd279d0297efb289a9b2783`、
`d0432faff569c8e9af7ed4809847e12880976c11`，已读。
下次 actual pull 最迟 07:31:53 UTC。

私有 actual pull 06:31:56.513823 → 06:31:57.127870，
before=after `832093cccbd36dbbe437eed703bf85a19e7dc339`；
根 blob `5ba164843b1f5802184178a82d786264404873a3` 未变，
私有本题 README 不存在，QUEUE 本会话唯一进行中。
没有发表私有内容。

## 7. 原始输出指纹

原生接口解码串按 UTF-8 编码为 1559099 B，SHA `f597ac00baf733e0de6f0d88647b0c162a37cc9e33e428bd6371a93032e7c087`；下一读取仍核对服务器实际字节，不把已解码来源误称原下载字节。

- PUBLIC_PULL JSON+LF：1610 B，SHA `2ce383e8cf13f5ce59d8809c6a976e21ddc9e03a5bb55b5677550ca3c1e68f74`。
- PRIVATE_PULL JSON+LF：584 B，SHA `122d4250f044941920d4067ca1a5df14d80f2891b822709add14743cbc2cf543`。
- REQUEST JSON+LF：2985 B，SHA `239014ba019928d3ec4685cb601601e2455464d148d1a427abed5d2b2ad1c9b5`。
- SOURCE JSON+LF：2008 B，SHA `4a4a7601cc2a636d8147e7fc0e093f23be18cc34e57d3c0ba773b245d98bd258`。
- ASSEMBLY JSON+LF：6886 B，SHA `bd7c440db806d8f93c3673c646bd8be96741b8cde537829e331fed70e1cc1dc8`。
- RESULT JSON+LF：1139686 B，SHA `9339ef99e4626c194245c89d177a5a4b3a87d8436b5a8ed3dd255ebc40447cb0`。
- COMPLETE JSON+LF：185626 B，SHA `489ecc703840abc6e1c360b10478dbe6ab480002d15f667054b40d912263ff63`。
- FINAL_CLOCK JSON+LF：132797 B，SHA `d6e46f0342664aa8021424114912242bbcc54e7374169c8aeb5635932180b7f8`。
