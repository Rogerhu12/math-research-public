# R150：原无穷远小投影的有理 Smith 入口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。

## 1. 当前状态与目标

这是新小矩阵的可执行接口；源码已冻结，尚未声称新数学运行成功。
当前已付的是同一原自然无穷远模型的五阶完整连接
$(4,0,1,3,1)$、十八条实际五阶左链、原全模的模 $31$ 完整谱及十三条特征零原始形式左核。
本入口直接读取当前任务实际保存的十八条链，核验其精确支撑，再计算真实原投影的
$\mathbb Q[[u]]$ 与 $\mathbb F_{31}[[u]]$ Smith 谱。

执行源码：

- 路径：notes/2026-11-15-r150-infinity-small-original-projection-smith-789f.py
- Git blob：74d4c918faf3d5b791493a94bd7df3000395805b
- 字节数：37379
- SHA256：dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79

没有改变已付的原算子或五阶程序，没有重新执行原大正常形。
只在当前临时任务目录保存可重算矩阵、原来源映射与完整阶段检查点。

## 2. 从原 $6188$ 行到真实 $224$ 行

使用已付原 $17$ 式的自然无穷图 $u=1/s$，再作常数反序与普通二项式共动变换。
这些是相对于已经定义好的自然齐次图的源、靶局部单位变换。
不把从裸矩阵 $A(1/u)$ 引入自然权的步骤说成单位变换。

保留原输出中的 $20$ 个纯切向和 $135$ 个一次横向坐标。实际源行按横向次数分成
$170,918,2295,2805$ 行。后两组在这 $155$ 个输出上的每项严格为零；
本程序仍按原源字典逐项核验这个支撑结论。

在切向平面，原式精确具有

$$
F_i(u,c,d,0)=g_\infty(u)d^2q_i(u),\qquad
g_\infty(u)=-2u^2-8u^3+24u^4,
$$

其中 $q_8(0)=4$。这里 $i=8$ 是固定原物理生成器的零基编号；
其与 primitive 原 $17$ 式的常比例从已付 Q13 回执读取，并逐分子、分母核验为 $31$ 单位。
程序从原 $K_\infty$ 逐系数重建全部 $17$ 个纯多项式，实际验证
$F_8/u^2$ 的常数项为 $-8$。

对同一个一次横向乘子及切向单项式，保留原 $i=8$ 方程的实际行。
共有 $54$ 行。其他 $864$ 行是这些行的正则倍数

$$
\frac{F_i}{F_8}=\frac{q_i}{q_8}\in\mathbb Q[[u]],
$$

并且此比例在 $\mathbb Z_{(31)}[[u]]$ 中也合法。
实施原行减法便将它们消成零。完整 $F_8$ 的 $u^2$ 因子始终保留；
程序没有把这些行除以 $u^2$ 当作单位行。

因此原转置算子在这 $155$ 靶坐标上的限制，与一个真实 $224\times155$ 矩阵
$P(u)$ 加 $5964$ 个零源行局部等价。这里 $5964=864+2295+2805$。
常数秩 $128$ 在两域中均由实际矩阵核验。
所有 $918$ 个一次横向原行及全部高横向零行的有限前缀都逐原字典验证。

## 3. 先读实际五阶来源，而不是仅信零块摘要

输入的第五检查点 manifest 和 verified pack 都锁实际字节数、SHA256、语义 binding。
程序完整读取 $4650\times18$ 个有理系数，并做：

1. 核全部实际分段和规范矩阵 SHA；
2. 逐元素检验各二次、三次横向块为零；
3. 逐元素检验已存正阶纯切向块为零；
4. 在真实 $155\times18$ 初值矩阵上计算秩，要求等于 $18$；
5. 将这十八条链再次作用于本次重建的原系数，
   对六个阶次的全部 $6188$ 原来源乘回。

最后一项对应 $668304$ 个原产品坐标。
既有零块 SHA 只用于输入绑定；它不代替这些实际支撑和乘回断言。

## 4. 原来源随每次 Schur 消去保留

首先在真实 $P_0$ 中选 $128$ 个单位行列，并核两边常逆。
把 $P$ 写成

$$
P=\begin{pmatrix}U&B\\ C&D\end{pmatrix},
\qquad
T=\begin{pmatrix}-U^{-1}B\\ I\end{pmatrix},
\qquad
S=D-CU^{-1}B.
$$

所有原行的系列乘积 $PT=(0,S)^{\mathsf T}$ 都实际验证。
小余块为 $96\times27$。随后只在真实常数余块中选新单位，
保存全部余行、完整原 $155$ 坐标映射及每层原乘积。
只有整个当前常数余块为零，才将其整体除以 $u$。

若某层原映射已经满足 $PK\in u^\ell R^{224}$，
在该层的列变换只需知道模 $u^{N-\ell+1}$。
其后未指定的高项可取零；它们对原 $PKT$ 模 $u^{N+1}$ 没有影响。
程序仍将实际选定的 $155$ 坐标映射保留到原 $N$ 阶，
而不是把剩余 Schur 的精度冒充原形式核的无限精度。

每个退出的正 Smith 方向均保存其原 $155$ 坐标链。
实际核它在全部 $6188$ 原来源上的低阶乘积为零，
并核其退出阶的原投影产品具有相应真秩。
剩余自由链同样在所保精度内逐原来源验证。
全部 $27$ 个已退出与剩余初值始终做独立性检验。

这些有限链不会被称为已恢复的完整有理函数核。
完整泛核上界来自已经付过全部原恒等和原始性的十三条 Q13 核；
本次有限链给出真实单位、指数和有限原来源证书。

## 5. 何时可以宣布完整谱

原 Q13 回执给 $P$ 的十三条独立泛核，故 $\operatorname{rank}_{\mathbb Q((u))}P\le142$。
其全部 $155$ 归一系数 $31$ 整、同自由坐标块为单位，所以模 $31$ 同样有这十三条泛核。
本次新的有限域小投影计算必须实际付出 $128+14$ 个单位方向。

特征零部分只有在十四个正方向全部退出、其余十三列的保留余项全为零、
原初值独立及全原乘回完成后，才报告完整谱。
输入先取 $0,\ldots,11$ 阶。
如特征零仍有正方向未退出，报告真实前缀并保存全部状态；
不把第 $11$ 阶自动当成特征零截止。

本次小投影与原全模存在真实余核满射

$$
\operatorname{coker}A\longrightarrow\operatorname{coker}P^{\mathsf T}.
$$

两者泛自由秩都是 $13$。因此诱导自由商上的满射是同秩自由模同构，
原满射的核位于扭子部分，并诱导扭子满射。
于是

$$
\delta(P)\le\delta(A)_{\mathbb Q}\le66.
$$

若实际 $\delta(P)=66$，这个扭子满射等长，因而是同构：
完整原特征零谱等于本次实际 $P$ 谱。
这一步使用原商映射和等长，绝不是比较两个无关的谱总和。

随后程序独立比较实际 $P_{\mathbb Q}$、实际 $P_{31}$ 和已付原全模 $31$ 谱。
只有逐指数确实吻合，才记 fullQAndF31AllSmithIndicesActuallyEqual。
不从长度 $66$ 单独推逐指数一致，也不由此预填旧固定 Koszul 族的 $149$、
高商的 $26$ 或同选方阵的首项单位。

## 6. 调用与输入

建议原调用：

~~~text
python {scripts}/2026-11-15-r150-infinity-small-original-projection-smith-789f.py
  --generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py
  --jet-actions {scripts}/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py
  --fifth-checkpoint-dir {work}/infinity-fifth-true-incoming-checkpoint
  --fifth-receipt {scripts}/43740928483-infinity-fifth-true-shifted-incoming.json
  --q13-receipt {scripts}/43736746064-original-characteristic-zero-free13-projection.json
  --field-full-receipt {scripts}/43740928483-full-infinity-original-dual27-through32.json
  --degree 11
  --out {work}/infinity-small-original-projection-smith
  --remaining-seconds 180
  --memory-mib 2048
~~~

只依赖当前已安装的 Python、python-flint 0.9.0 和标准库。
无 NumPy、无新 native 编译、无网络读写。
建议外层墙钟 $240$ 秒。完整输入 pin 在同名 inputs JSON。
现有五阶 verified pack 必须来自当前仍存活的任务；
输入缺失时明确失败，不能从旧任务路径假设临时文件仍在。

程序主回执：
~~~text
{out}/small-original-projection-smith-receipt.json
~~~

同源码、同输入、同 degree 和同 out 再次调用会核全部语义 binding，
复用完整系数、有限域状态和有理状态。
预算及内存参数不进入数学语义 binding。
每个检查点保存的是完整阶段；没有把未返回的原生 RREF 说成已保存。

## 7. 完成状态与范围

退出 $0$：完整 Q 投影谱、全部十四正方向及原乘回已完成。
outcome 为 complete-characteristic-zero-original-projection-smith；
只有实际投影长度 $66$ 才改为 complete-projection-and-full-characteristic-zero-smith。

退出 $75$：共享时钟或信号到达完整阶段边界，或者有理投影需要更高 Taylor 精度。
回执保留真实完成的阶段和指数，不预报完整结论。

退出 $1$：输入、原支撑、完整矩阵恒等或原乘回失败。
保失败原因，不放宽门槛。

关键输出包括：

- parameters.allPaidHigherNormalEntriesExactlyZero；
- parameters.actualFifthPureAndOneNormalLeadingRank；
- parameters.all17OriginalRowScalesActually31Units；
- parameters.originalProjection；
- parameters.QProjectionSmith 与 F31ProjectionSmith；
- parameters.allOriginal6188PositiveAndRemainingJetProductsZero；
- parameters.newOriginalSourceProductCoordinates；
- fullOriginalCharacteristicZeroSpectrumProved；
- parameters.fullToProjectionTorsionIsomorphismBySurjectionAndEqualLength（仅适用时）；
- parameters.fullQAndF31AllSmithIndicesActuallyEqual（仅适用时）。

其他已付全来源计算不由本任务覆盖；所有新结论只在实际回执之后登记。
