# R142 supplement: disjoint source slices with one shared Green representation

2026-11-27，visible-exact-astra-fb31ed6-20261127 / positive_inverse。

**状态：已证明（积分分解及定向实现的正确性）；新的并行实际积分尚未执行。**

本篇保留 PS 的同一个 comparison Green、全部155个原父区间、1424个既有细格、真实系数球、完整径向输出及193个端点观察。它允许把尚未接受的输入源区间交给至多三个并行工作进程；全部进程共用一次物化的私人 Green 和输出协方差。它没有放宽原严格门，没有把未完成的积分当成完整范数，也没有重算已接受的源积分。

## 1. 可分割的是源变量

沿用 [PS](R142-supplement-durable-complete-parent-source-moment-prefixes.md) 的核 $G_{\mathsf s}(r,t)$。对原父区间的有限并 $I$，记

$$
 b_{\mathsf s}(I)=\int_I\int_{\text{全部径向输出}}
      \|G_{\mathsf s}(r,t)\|_F^2\,dr\,dt,
\quad
 r_{\mathsf s}(I)=\int_I\|G_{\mathsf s,\mathrm{root97}}(t)\|_F^2\,dt,
\quad
 o_{\mathsf s}(I)=\int_I\|G_{\mathsf s,\mathrm{outer96}}(t)\|_F^2\,dt.
\tag{DP.1}
$$

完整原模型已给出平方可积核；三个被积函数均非负。若 $I_0,\ldots,I_m$ 两两不交且并成整个源区间，则对三者分别有

$$
 b_{\mathsf s}(I_0\cup\cdots\cup I_m)
       =\sum_{a=0}^{m}b_{\mathsf s}(I_a),
\tag{DP.2}
$$

并有完全相同的 $r,o$ 公式。这只是有限可加性；零测度端点的归属不影响积分。源区间之间没有交叉项：这里加的是 kernel 的 Hilbert--Schmidt **平方**积分，而不是把不同源作用于同一输入后相加的算子值平方。由 Cauchy--Schwarz，完整 body 的算子范数仍受完整 Hilbert--Schmidt 范数控制。不同片的 body/root/outer 上界只须逐一有效，无需它们是同一浮点求和顺序的输出。

每一片的内层输出域始终是整个曲面参数区间。特别地，不能把 $t\in I_a$ 换成同时 $r\in I_a$。先前保存的前缀 $I_0$ 是 DP.2 的一个完整输入片，后来的片没有再评价该片中的任何源 covariance 或 moment。

## 2. 与原逐格公式完全相同

一个工作进程负责父区间编号 $a\le p<b$，已接受至 $c$，其中 $a\le c\le b$。它只在 $p=c,\ldots,b-1$ 调用原 `ParentMomentProvider.packet`。原全输出协方差 $A_i,B_i,K_i$ 仍由 PS.3--4 在全部1424个细格上构造。根观察的协方差沿 PS.5 物化到本片第一个未接受细格：

$$
 J_0=\operatorname{Gram}(\mathrm{root97}),\qquad
 J_{i+1}=U_i^{-\mathsf T}J_iU_i^{-1}.
\tag{DP.3}
$$

这一步与源无关，没有重新积分先前片段。对于当前细格，贡献仍逐项为

$$
\begin{aligned}
 b_i&=\operatorname{tr}(A_i I_{L,i})
   +\operatorname{tr}(V_i^{-\mathsf T}B_{i+1}V_i^{-1}I_{R,i})+T_i,\\
 r_i&=\operatorname{tr}(J_i I_{L,i}),\qquad
 o_i=\operatorname{tr}(K_i I_{R,i}).
\end{aligned}
\tag{DP.4}
$$

$T_i$ 是原同格两个有符号三角已经合成的平方范数上界；不把它拆开取绝对值。$I_L,I_R,T$ 保留完整真实 cell 长度。变系数源仍用原 whole-parent PSD majorant，未将区间球当成常函数。因而 DP.4 就是 PS.6--7，在新的源片上逐项累计，所有合法性来自原 GM.1--17 与 PS 的证明。

实现每个完整父区间后才保存新的三球；当前父区间若未完成，其任何部分不进入 accepted cursor。恢复一个片只需它已保存的三个上端点、固定的 $a,b,c$ 和同一个完整模型，随后从 $c$ 开始。不同进程完成次序没有数学作用。

## 3. 三个片与完整结果的准入

新片记录包含源角色、$a,b,c$、已接受细格数、完整模型细格数、193个观察、同格双三角合同，以及三个完整 decimal balls。`validate_slice_metadata` 验证

$$
 0\le a\le c\le b\le155,\qquad
 N_{\rm accepted}=\sum_{p=a}^{c-1}n_p.
\tag{DP.5}
$$

`validate_partition` 要求片按 $a$ 排序、无重叠无空隙，并恰好覆盖旧已接受前缀之后的全部源父区间。调度权 $64+n_p$ 只决定哪个进程处理哪片；它不进入任何范数、积分或误差公式。

`union_complete_slices` 仅在每片均有 $c=b$ 后，依 DP.2 把旧前缀与所有完整片的三个上端点向上相加。随后得到同一个全域三平方上界 $B,R,O$，并沿 PS.8 得到

$$
 \|G_{\mathsf s}\|_{\mathrm{HS,body}}\le\sqrt B,
 \quad \|G_{\mathsf s,\mathrm{atoms193}}\|_{\mathrm{HS}}\le\sqrt{R+O},
 \quad \|G_{\mathsf s,\mathrm{complete}}\|_{\mathrm{HS}}\le\sqrt{B+R+O}.
\tag{DP.6}
$$

严格低系数门继续是完整 body 上界 $\epsilon=\sqrt B<1$；根、外端各自输出不被删去，但不把它们误加到原 body 收缩门。片段尚未覆盖全域时不报完整 $\epsilon$，即使某片上界很大也不称实际算子奇异。

## 4. 一次物化与进程内存

新纯适配器为 [parallel parent slices](../scripts/fourfold_codazzi_low_centre_parallel_parent_slices.py)。普通积分入口 `integrate_remaining_slice` 本身不依赖并行库。可选执行入口 `fork_remaining_slices` 仅在公开 Linux Actions 的数学阶段调用；它在同一个进程完成全部原 Green 和 $A,B,K$ 后，至多 fork 三个工作进程。

fork 保留内存中的原只读 `PackedMatrices`，各工作进程只清理自己的 decoded cache；不会改变已打包矩阵条目。每个进程新建自己的原 provider、Taylor template 和当前父区间源缓存。所有矩阵运算仍是原定向 Arb 运算；并行调度不参与代数，也不降低精度。没有矩阵或数组写到磁盘、仓库、Release 或 artifact。

工作进程只写很小的完整标量片记录。保存先落临时文件、读回每个球并确认包含未序列化的定向结果，再原子替换正式记录。主进程读到的因此总是旧完整父区间或新完整父区间，不可能是半个 JSON 或仅有 counter 的未成片段。主进程必须把这些完整片保存到自身正式科学结果后，回调才返回。工作进程超时或失去执行环境不扩大任何完成标记；可恢复的是最后实际保存的完整片。

源积分阶段的现有重复固定成本来自每次重建全部 Green 和 $A,B,K$。本构造在一个公开作业内只付一次该成本；三个进程分担剩余源片，而非各自重新物化全局对象。实际加速比、峰值物理内存及在6小时内能完成的片数须由新实际执行报告给出，本篇不凭调度结构声称数值门通过。

## 5. 当前未改变的范围

原 PS run45802396138/1 的76个母格只覆盖76个细格；剩余79个母格包含1348个细格。其完整已存三球可以作为本篇 $I_0$，但这不是本篇已经执行。正在运行的既有 owner、manifest、输入身份和实际失败状态均不修改。

只有新的 owner 显式承认旧 PS 前缀及新片 provenance、保存全部源片并完成 DP.6 后，才有新的实际 low193 结论。四个 ordinary sources、point/whole-interval 目标、physical58→224→32、负侧与两 mean、真实有限 Schur、非线性迭代和最终闭曲面几何义务仍分别存在。
