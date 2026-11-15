# actual97：同η=0.1的八轮完整接受，仍未达到原低三根条件

类型：公开Actions数值记录；不构成解析存在性或原大幅BVP验收。作者：ChatGPT（exact_refinement；root整理发布）。日期：2026-11-15。

## 实际来源与停止原因

实际[run43676647334](https://github.com/Rogerhu12/math-research-public/actions/runs/43676647334)，source commit `15b2028e039d2b93ea01b3bf6ef8c1fed8db15ed`，job `132698148882`，全部success。原artifact `14146527398`，478758B，ZIP SHA256 `f041c43023cd5d431d5cb44e7991ed8345050859baf7e228c894c9a71b3fd06b`。

主原件 `small-core-inexact-p3-restoration/inexact-p3-restoration-status.json` 为233256B，SHA256 `d55b5338880cabaae44bd7575db9a10bcba22fad4ae1fce0225f1ef38064f331`。本稿只读原保存值和记录，没有本地重新计算科学量。

入口 `geometry_20261115_small_core_inexact_p3_restoration.py` 的SHA256为 `ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e`；schema为 `R278-original-three-equation-inexact-p3-restoration-LM-v1`。request绑定72源，producer声明消费13源。原方程与J来自 `geometry_20261114_small_core_resonance.py`，SHA256 `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`。

父为实际96的已接受末参数；父status为233129B，SHA256 `3343c5799dcb50a3ff58c52c0dfebaab441bc7a0bfe644a88e9a1a93fae2eacb`。本轮只将父参数作为新初猜，初始评价、完整当前J和最后检查都有真实新调用，未把父J、merit或状态改标签为当前结果。

停止原因原文是 `explicit outer direction budget completed`。八方向均以α=1接受；没有第九个已执行方向，也不是线搜索失败或域异常终止。

| 原字段 | 实际值 |
|---|---|
| fresh初始merit | `16791.96200276451` |
| 最终merit | `15400.321596660777` |
| 接受次数/α | 8；`[1,1,1,1,1,1,1,1]` |
| 最终p | `[0.5050366803948241,-0.3310221447104421,0.5931424079355273]` |
| 最终unit | `[-175.4927978505483,1.7091213848475404,-5.313809937131531e-08]` |

父96保存末merit为 `16791.962002764827`；同参数的本轮fresh初值末位不同。参数相同，初始unit、完整右行、J和merit并非全字节相同。这是实际有限浮点对象的区别；本稿未把差异重算为范数，也未归因到未经检验的环节。

八份inner记录有150次试探、28次内层接受更新、36份内层当前完整J。两份inner达到原第三个unit阈值，六份未达到；未达点仍按既定inexact-restoration定义，携实际非零d3和当前完整J参与外层候选。没有将d3置零或把内层阈值另设为外层禁入门。

## 未通过的原判据

`diagnostic_completed=true`仅表示有界诊断完成。原success、unit停止阈值、完整112行候选标志均未通过；native非零求解器没有调用，原完整BVP尚未验收。

原112×112零尾J完整保留并报告为对角；高109行零泄漏不支付高109自由core的Schur消去、非共振或区间横截性。原圈检查与标量区间诊断保持其作用范围，不构成非零闭场存在性、全C²或reach证书。

末方向保存的scaled Schur/SVD/滤波属于产生方向的基点，末接受态是另一点。不能把该谱改述为末接受态的谱；full3 merit下降也不意味着三个unit分量各自下降。

## 来源复核与复算

原记录已联结2798项文件/来源/JSON/IEEE词：20个artifact成员及本地下载marker、72个request来源、13个消费来源、347条事件（309评价、38个J返回；评价为195real、114complex）、8份inner和245份已保存数组身份。observer错误为空。四数学输入沿actual92已完成的同原件核对与本轮Actions回执；78项恢复源码沿实际回执，不冒本地又下载或重算。

复算使用上述source commit的同名脚本、`public-small-core-resonance-request.json`和对应workflow；完整argv以该run的`exact-diagnostic-command.json`为准，四输入SHA见`request97-input-and-source-identity.json`。核心参数：η=0.1，外层8、回溯20，内层更新12、回溯20，unit容差1e-8，完整三方程merit/gdot与Armijo系数0.2，原最终unit/full112检查不变。

本轮仅显式预算停止，末接受点可作后继初猜。改变η需诚实区分producer身份并保原方程和最终判据；局部滤波预测不等于真实新接受。按根README第15条，本稿不附可重算raw、原文gzip或大审计数据；只保存结论、脚本/参数来源、run和输出SHA。共享终端中断后的额外verifier没有执行，不作为发布条件。
