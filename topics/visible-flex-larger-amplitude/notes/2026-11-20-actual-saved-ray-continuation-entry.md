# 已付完整方向的真实接受点射线续步入口

状态：完整源码已写，只有 AST 与逐式静态核对；未进行本地科学计算，也未执行新的 Actions 试步。
它是 [R673](../results/R673-full-Phi-damping-face-gap-and-true-ray-continuation.md) 的实际消费者准备，
是否需要执行由同父 pair 的真实结果与接受点一次 fresh Jv 决定，不是先行检查门。

## 具体输入与可复现命令

完整源 `scripts/resume_20261120/full_phi_saved_ray_continue.py`，19016 B，
SHA256 `45f8f40554d86148c7a5064e2cc59afe25b44452e56ce2fba448577c6e17fe8c`。
输入为本次公开 runner 中已实际完成并接受的单方向完整报告，及 R673
`full_phi_saved_ray_slope.py` 在那个接受点返回的真实导数报告。
源核报告/接受bundle/保存完整自由方向/carrier 与实际用过的全部源码SHA；不从旧数字预设导数。
它明确只接原 lift 的不变完整QP driver；R671新f/h/k工厂的报告不能由此默默按旧场读取。

~~~sh
python "$topic/scripts/resume_20261120/full_phi_saved_ray_continue.py" \
 --report "$chosen_pair/report.json" \
 --slope "$work/chosen-saved-ray-true-slope.json" \
 --outdir "$work/chosen-saved-ray-continuation" \
 --line-trials 15 --max-increment 2 --armijo .0001
~~~

所有路径指公开 Actions 的临时 work。实际运行只允许本公开仓库 Actions；
控制器按该步骤固定源码提交、实际 run、输入/结果SHA与标量发布，数组和逐点报告不入Git/Release/artifact。

## 真实迭代语义

令旧完整方向为 $d$，原接受步长为 $\alpha_0$，当前实际接受场为 $x$。新试步为

$$x(\eta)=x+\eta d,$$

其中 $\eta$ 是追加量，总旧射线参数为 $\alpha_0+\eta$。它没有再缩放一次旧接受步长。
新的QP/Jv/VJP调用数全为0；已付fresh Jv由独立输入报告消费。当前场一次residual实际重读，
随后每个试步读取全部原节点/中点/六Gauss径向行、N2048整圆等价角行和原正权p8目标。
只有真实导数负、当前全部有限域余量严格正且已知点产品低于所声明的同一内部安全余量时才提议延伸。
不满足这些条件则不作科学试步，保持原父的逐字副本，明确返回未延伸状态。

首个增量取正残差Hessian射线模型给出的 $-D\Phi/(2c)$，上限2；
若该正曲率提议不可用则取已声明上限。每次真正下降必须满足

$$\Phi(x+\eta d)<\Phi(x),\qquad
\Phi(x+\eta d)\le\Phi(x)+10^{-4}\eta D\Phi(x)[d].$$

回溯逐次减半，最多15次是本轮明示工作单位，不是课题完成条件，也不声称存在性命题保证15次足够。
目标不同于旧原始SSE，原weighted/all-raw/legacy-raw各自另记，绝不相减冒下降。

每个候选只有在原完整relative Gram域正且真Phi下降后，才付原完整六jet几何与全部永久任意点。
曲率读出、直径点下界和所用 .992 或 .998 来自同一个被选择的实际分支，未放宽那个分支的规则。
拒绝试步发现的新曲率峰与半径位置继续保留。无论最终接受还是保留旧父，只要位置集合增长，
最终成员都会再读取这些新位置；若最终已知点余量未过，报告保留false，不以先前接受覆盖它。

真正接受才产生新q/H场及独立SHA；没有接受时 `final.npz` 是原父逐字复制，明确没有新解。
全部候选、实际异常、真实residual尝试数（含数值异常调用）、完整几何调用数、耗时及RSS均入临时报告。
原始完整方向和父不删除，也不把一维复用写成另一个已求完整QP。

## 未付范围

R673给的是准确有限模型的条件性局部下降结论；实际计算使用普通浮点数，
每个候选仍由真实目标和永久位置读数决定。点产品不是连续K或真正reach，
新的parent也不继承旧连续嵌入、D、held、全域metric或精化证书。
本条只有准备源码，没有新数值接受或完成声明。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
