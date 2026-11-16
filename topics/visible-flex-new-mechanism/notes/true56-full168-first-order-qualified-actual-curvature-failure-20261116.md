# 真正56上的全168联合模型：一阶合格而实际曲率失败

日期：2026-11-16。可信度：有限原模型数值观察。**当前真正接受点仍是56，没有接受57。** 三个有限主问题收敛，第三个全网格一阶方向合格；其标量预测最优试点在实际粗网格超过原曲率58门，细网格未求值。不能把主问题收敛、预测下降或Actions成功改称几何接受，更不能改称课题完成。

## 1. 来源、任务与已付输入

唯一新[run43847611444](https://github.com/Rogerhu12/math-research-public/actions/runs/43847611444)，research job133231619868，report job133236104610；source a9da16278c336ec5d6ce3be88502263d04429324，workflow .github/workflows/visible-true56-joint168.yml。

设计见[全168联合模型设计](true56-full168-joint-model-design-20261116.md)，参数见[request-true56-joint168.json](../computations/request-true56-joint168.json)。request为60,590 B/SHA256 9272179a7cafad1cde180b5709b548a544e4fdc2b5eb1cff6fb813b5719cedc9；设计6,313 B/b4795b588e61e81dea25976510b035af558b091222a3a6f814a0d88442c09aa2。源文件完整清单在该request中。

这次从[真正56](true55-new-nine-original-two-grid-accepted56-20261116.md)的非零new9场出发，全部168独立参数可动，保同一固定g、永久reference及完整172物理盒。两网格各一次必要ordinary输入与一次selected-J168构造均完成，保全部原9002池行，无支持集过滤、端点删除或旧159-J冒用：

- 原硬行3132，导数3132×168；
- 原软行5870，导数5870×168；
- 原物理线性图172×168，范数为 $h=4\|M\delta\|_\infty\le1$；
- complete-input binding b36f43c371c84644dbe9a96d9acf0bdb107b722eefb5a5a2a2200283099ee431；
- model binding 0eb0dc10dac2acddaea88566b9a18a025c8601d7b2759f38668723fdb2699a4e；
- 物理图原float SHA256 385b561992acb6440f5fa544d7ba0d4a9d35f3a413c495e096bc2279d6cf666a，model规范图binding 522787664d777c0b7c0d1a2b6d34087b54168e3e541477ff96b5224f43203576。

原INPUT3同时保存J、基值、target、原tag及完整绑定；只存在原stdout，不复制到Git、artifact、Release或cache。

## 2. 三个不同原行集上的有限主问题

| 新主问题 | 迭代/系统 | repaired rho | 全两网格一阶最大值 | 扣范数费后全网增益 | 新增原metric行 |
|---|---:|---:|---:|---:|---:|
| 1 | 43/86 | .2655738070964453 | .26755236311975233 | −.0015434397049969315 | 4 |
| 2 | 43/86 | .2655752201684062 | .266871999899474 | −.0008630764847168395 | 4 |
| 3 | 40/80 | .2655777631257589 | .26597413352682137 | .00003478988793597303 | 0 |

每个有限问题都由真实新增原tag形成，保留先前全部行，各自只求解一次。总126次迭代、252个系统，三个返回均为converged；原有限行violation和容差excess均0。第三个 $h=.9999999942645985$，其全网格一阶方向通过本次预测标准。

8个新增原metric行的完整168梯度已付并保存在MODEL，不是后续重新求导的理由。最终direction SHA256 ae7b120d568ffd00c8c2580fcc8aaca3975fa69421091c0bfc3c64557224fd3b。所有预测仍是在固定当前56点的局部模型上，不能把有限rho或全网格一阶值当作实际新曲面的误差。

## 3. 标量预测与实际失败

62次新scalar查询后，预测最优
$$
\alpha=.05665608433177267
=\frac{8165002249114969}{144115188075855872}.
$$
affine-observable预测 $\phi=.2660007356727879$，范数费 $5.665608400682727\times10^{-8}$，总目标 .2660007923288719，相对基准 .2660099234147516 的预测净增益 .000009131085879687806。

仅尝试一个actualpair，先求值粗网格，得到：

| 原实际量 | 观察 |
|---|---:|
| 最大metric eta | .2660499199695634 |
| eta峰位置 | $t=.5925,\ \theta=0$ |
| 最大绝对主曲率 | 58.007888653387816 |
| 曲率峰位置 | $t=.78,\ \theta=\pi/2$ |
| 两主曲率 | −58.007888653387816，−2.614904616558577 |
| 最大球范数平方 | .9905283297524368 |
| 最大绝对y | .3899898518209618 |
| 有限mirror量 | .09744905055906121 |
| signed height | .02 |

试点physical172 SHA256 ce59ca010dc5b46f3c8947264198ba693c86bedbc77038b58ff783ddbb40faf8。原curvature-scaled-PSD、independent-direct-curvature、single-grid-hard/admissible门失败；其余原物理门和准确172盒通过。cap两个微负量约 $-2.78\times10^{-17}$ 与 $-5.55\times10^{-17}$ 仅按原 $10^{-9}$ 容差处理，没有放宽门。

全粗网格有18条curvature-plus-determinant违例，**全部已在原选行中**，遗漏硬行数0。因此本次不能归因于删除曲率约束。实际metric也比56变差，预测下降没有在该试点兑现。

实际分离另得到一个此前未入池的原soft tag：coarse flat-row-id104448、group1、$t=.5925,\theta=0$。原group0/1的定义保持不变，两分支均按原式处理；不改名或互换分支。粗池因该行变为4454/version15，细池仍4549/version14。

按预先发布的新行停止规则，此方向至此结束，未追加其余backtracking，细网格未求值。原acceptance reason为fine-grid-not-evaluated。这是原规则下的实际拒绝，不能补写未执行的细网结果；接受点、物理参数与原56两网格接受记录均未变。

## 4. 原始输出身份

以下为原JSON加LF的字节与SHA256，保持producer字节身份；大型payload只在原Actions stdout。

| 记录 | 字节 | SHA256 |
|---|---:|---|
| INPUT3（完整付费168导数） | 21504677 | 058becbdcdc8746328f702cd0f92e04d622bc387b8c206cc98489beba602691e |
| CACHE1（最终方向e/f/de/df） | 14925219 | 0448ded7cfdf6f6b4cde2595fb9e26e353f62db1cc2d874d28307df3df605f9c |
| ACTUAL_TRIAL1 | 160502 | 08ad2ff04e837ddf5b524644dda0bc7353a2d06f719e1c6174488d3fc2a15d8c |
| MODEL1（含新增8梯度） | 1047239 | 86b10a9a76794839239e678a7af9d545bc627f661d80d746c84b352dfbeb6d4b |
| COMPLETE1 | 2122368 | f8b2bf46220044084bf3726c2062b66e472abeffdd6e44c3e70d6a98a1048473 |
| FINAL_CLOCK1 | 76487 | 39d760b534c554833d6b47f515d417838be64f10fd3a5af440ea10c36a7ad305 |

research stdout 46,110,806 B/28eeef350781fd1a341adad4da553abbc4918bf8aa129ee01a61a6ecc9e3a489；report stdout 3,718,350 B/fde4557819da32a37a8f063a51f77bae867ef385d3420e3b1fa48c28141011d3。87条原记录、0解析错误，report语义投影完整、projection0。两job success仅表示程序结束，原科学状态为complete-true56-full168-original-actual-observation，newacceptances0。

## 5. 完整费用与已读规则

最终权威ledger为 **188.38691980800002秒**，包含imports、输入恢复、必要ordinary、selected导数、三个有限问题、分离、新梯度、62scalar、一次实际粗值及大输出。最后process采样188.38846133500004秒不是替换ledger的另一个任务计时。report只读observer3.097577141秒单列，不加成科学执行。

本次计数：2必要完整值、2selected-J网格构造、3全网格分离、8新metric梯度、3finite-master/126迭代/252系统、1scalar会话/62查询、1actualpair尝试/1实际完整值。总新完整值3，峰RSS774096KiB，无overrun。

前账2233.566394556秒/138完整值完整保留，含此前56账户；故供后续引用的累计祖账为 **2421.953314364秒/141完整值**。本次600秒范围随已声明流程结束而闭合，不把剩余411.613080192秒改为restart或续接同一有限问题的余额。

research于10:18:37 UTC完成public真实pull到390b999ac14be796192984316f3da83a2ba0ad46；report于10:27:12.374618至10:27:12.945970实际pull到8ba72343a6f60a30a37947a6768ece150f13be30。根/题README均空diff、rc0，blob仍21bd547f56590b7f2dd279d0297efb289a9b2783/d0432faff569c8e9af7ed4809847e12880976c11。

对应私有research实际读e9e81c9897965f0a8e6f2e9864f91b30c501512e，report于10:27:14.853179至10:27:15.320961实际读2033fc18ea85fc2b8b1df753375edf89c3ea0e34；私有根README未变，本会话QUEUE唯一进行中。私有正文不公开。下一实际pull最迟11:27:12 UTC。

## 6. 接续是新小域问题，尚无新观察

实际失败没有改变固定g、基准56或验收门。接续拟把真实物理域缩为
$$
h=4\|M\delta\|_\infty\le1/128,
\qquad \|M\delta\|_\infty\le1/512,
$$
保全部168参数、原172盒和全部硬/软行；复用本次已付完整INPUT3与8条新增梯度，并补coarse104448在当前56点的metric-only完整168导数。56旧CACHE2的两网格e/f SHA与本次当前输入逐项相同，可恢复其已付U/T；不重做必要ordinary或原9002行的导数。

小域只是下一项新数学模型的明确选择，不声称能修复实际曲率，也没有把本段写成已经执行。新任务费用从其真实开始时钟独立记录，保上述全部祖账；后续新的原分离行、预测与actual两网格14门仍须分别支付。主README的全时、全域、固定g、reach与误差精化标准都未完成，继续open。
