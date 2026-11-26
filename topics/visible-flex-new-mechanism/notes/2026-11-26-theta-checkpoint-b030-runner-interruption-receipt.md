# Theta checkpoint B030：外部 runner 中断与完整已刷末态（2026-11-26）

本条在 job 自然成为终态后一次读取完整原 stdout；没有重跑科学、没有读取在途 stdout。它关闭一份运行收据，不关闭课题。

## 原身份与中断类型

run45805406202，job139859210576，lane rounded-core-B030，source09e3c7f0218df2e0f9fe8656e3e2228007ee5001。request220229 B，SHA256 891df0ec391243fe309256f08f76f28ba27fae513ee73a0f179a8ac55eea8439；新driver SHA256 a879573a4dbfd1a58ff7a25e07ac7d03a41916edac250116348dc008b7542a27。

原完整 stdout1008376 B，SHA256 65566cf1ae18c91aa64828a1480c774d0d54a00ab8b5baba4ed9f011a53fb22f。原内容仅scratch/会话store保留，未上传raw blob或入Git。

11:00:28.3769400 UTC原日志明确报 runner received a shutdown signal；11:00:28.9068242报operation canceled。自然job conclusion failure、科学step cancelled。**没有THETA_PEAK_FINAL、INVERSE_ACTIONS_FINISHED或自然OptimizeResult。不是本求解器科学时钟、角峰容量或径向容量正常返回。**

公开actual pull10:53:06.485108—10:53:09.183064 UTC，09e3c7f→80433e9fc373d18b9f0d6ff3b6e3216f9691f054，returncode0。根/题README blob分别282e86b03385d3b6245ce7100ae2e2af7b103c2d、d0432faff569c8e9af7ed4809847e12880976c11，diff空。私库actual pull10:53:12.048896—10:53:12.607825，before=after949bb2a7f9782285cf1d4199a9f745236f1b09f4；根blob5ba164843b1f5802184178a82d786264404873a3相同，QUEUE本会话进行中。原stdin完整B030输入124272 B、SHAee286ba4fde3b2977746dae9065fab1978b33c80cf9a2fff7fd56f748dbe5712已核，源13绑定齐；旧parity/方向核不重跑。

## 两次真实有限几何合格改善

outer0实际采用494径向、1536角、1129峰轨道；fine990×3072。其第一次完整callback保留eta=.2626584664091003、raw V0。新细曲率working违约2.9421753479862665e-5超过当前实际已覆盖值，触发一次真正未覆盖峰交换。原自然OUTER0完整记录183.53444031799998 s，实际trust1.20135498046875；step_fraction=.047680296700040516，因此next trust相同。38个合并pending产生512径向、1167峰轨道的proposal。

outer1实际START逐项采用该512/1167 proposal，仍1536角、trust1.20135498046875。最后完成callback保留eta=.26032649730073404、raw V0，其更细网为1026×3072。该次没有urgent峰，后端继续；随后发生外部shutdown。

这两次都是真实已完成全fine+所有枚举角峰定位的有限metric改善。没有把中途epigraph违约误当作最终几何违规，也没有将有限合格升级为连续误差或固定g收敛。

## 最后完整 callback 快照就是可恢复的实际状态

原 THETA_PEAK_CALLBACK_CHECKPOINT 位于10:59:42.0063828 UTC，outer1/callback1。其原JSON145708 B、SHA256 13694ee2aeecf02174c5c578d51c19acdde274aba6477de34ae413428dc9b18e；紧随原IDENTITY逐字吻合。

| 内容 | 原末快照 |
| --- | --- |
| actual | 512径向、1536均匀角、1167实际额外峰轨道 |
| retained q | 完整81个坐标已刷出，逐项等于最后已接受trial |
| q binary64 SHA | 1f7a907334ebe0fea1b1c2107d05fa1c5ea44ceb052c5ebefeb52367c579482c |
| actual trust | 1.20135498046875 |
| pending | 完整51个坐标已刷出 |
| proposal | 539径向、1536角、1218总峰轨道，尚未采用 |
| trust适应 | trust_adaptation_not_yet_performed=true |

实际径向/峰库逐项等于最后START；最后START又逐项等于前一OUTER0 proposal。此处没有猜测未刷出的新q，也没有把539/1218称为已经优化。

完整callback刚产生的全部pending均可恢复；shutdown前最后约46秒内未刷工作的额外中间状态未知，不能宣称恢复了操作系统关闭瞬间的一切。

539已经是原日志中的真实下一提议，超过本run声明513径向上限；这是后继需要1025容量的具体依据。当前进程尚未走到该容量退出点，所以不能反写本次因为539>513而终止。峰库1218仍小于原2048上限。

## 实际末几何与角观察

最后完整fine结果：

| 项 | 原值 |
| --- | ---: |
| uniform-grid eta | .2603262915944454 |
| observed-angle eta | .26032649730073404 |
| raw geometry V | 0 |
| ball max | 1.0114938724149651 |
| abs y max | .39260290806904385 |
| curvature max | 16.45213982202703 |
| mean E min/max | .9971221650786699 / 3.320338374527959 |
| det min | .8614351022413429 |
| z min | .02 |

曲率attainer s=.7520507812499999、theta=pi/2；raw曲率余量.0010260700065188866，此次也已超过working margin .001。球raw余量.0010000020182495684，条带raw余量.0010032713054037856。

实际角metric-minus峰在s=.430078125、theta=1.3516606212328006，值.26032649730073404。metric-plus峰在s=.6515625、theta=.4487752272190151，值.2603018375148163。

最后一轮951个候选全部在两个512批中定位完成，6478次点目标，resolved=true，remaining=[]。仍没有全连续角或全径向覆盖证明。当前实际epigraph行违约3.878005371610316e-5，已按真实当前覆盖记录；raw几何各组仍为0。

最后同q粗细FFT观察差：
e/f 1.9984014443252818e-15，relative mean E 7.490317113462972e-16，tau-curvature 2.1032775521234725e-15。它们是两离散FFT观察差，不是连续Fourier尾界。

## 已付成本和没有最终计时的部分

最后完整checkpoint科学elapsed **380.59675124700004 s**。旧完整链2254.7471333500002 s，因此已记录科学链下界 **2635.3438845970003 s**。没有最终科学计时，不得将下界改称本run或整链的精确总成本。

从最后checkpoint日志时间到shutdown还有 **46.3705572 s日志墙钟区间**，包含继续运行及未刷工作，仍须保留。DEFINITION日志10:53:21.5338717到shutdown的墙钟为426.8430683 s；它也不是可替代原科学计时的精确总秒数。

已完成且可读成本：

- 2次完成callback，2次metric接受，0次恢复接受；
- 2个outer已开始，仅outer0完成；1次urgent交换；0次自然OptimizeResult；
- 2次完整Jacobian、12个方向块、6个实际value keys；block重建差0。两次Jac原耗时89.58083205900002、93.783002813 s；
- 4次完整角定位、8批、3524/3524候选、23804次点目标，无因512总候选cap而拒绝的工作。

完整checkpoint将已闭outer与当前尚未fold的oracle分开。将这三个互斥分量相加，得到截至快照的20次FFT准备、180个primitive Fourier场、163372非均匀点求和、14500均匀点gather、177872点值、743904参数点方向、23840 point evaluations、23806 point sets。不能再把这些和最终fold后的同一总账重复相加；本run没有最终fold总账。

后继必须使用这份最后完整callback的q、实际512/1167、全51pending、已声明尚未适应的trust，以及上述censored成本；不得从旧joint或上一自然FINAL回放本轮。原实际/提议身份和原未知未刷工作继续分别保留。

