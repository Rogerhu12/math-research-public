# R146 实际：完整二次帽严格排除当前 CV/RA 非负费用门

2026-11-26，visible-exact-astra-198c63d-20261126。

**已证明，包含完整公开 Actions 计算。** 当前已选 CV 相关体费用与 RA 根锚定接收器的非负费用格式不能通过完整二维正定门。新的完整必要测试 upper 小于 −0.16618。此结论保留真正 high 压缩逆；不是对实际 BVP 的奇异性或无解结论，也不是本课题的完成。

## 1. 唯一新计算与完整身份

运行：[45765780668/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45765780668)，事件提交 a387e2039ab99a48b81219b8049954b726bccf1e。
科学源码为 [quadratic cap consumer](../scripts/fourfold_codazzi_quadratic_cap_root_screen.py)，SHA256 f3311123e1bb0375c9bbc73366457c0503c1efbd9958f665fb2c8d972077c552。
[完整输入manifest](../notes/2026-11-26-R146-quadratic-cap-root-screen-inputs.json) SHA256
6e0dc5b02f4122c9ffa82c041251b1da72311f0def5817b608580ae85e213f60。

| 记录 | 字节 | SHA256 |
|---|---:|---|
| [完整科学两球](../notes/quadratic_cap_root_screen_ci/run-45765780668-1/quadratic-cap-root-screen.json) | 22092 | 5b14b6f9795a5ebe72585b2e6aaedbe0553fceefa6d2561539a457d2d82cfe18 |
| [完整执行记录](../notes/quadratic_cap_root_screen_ci/run-45765780668-1/execution.json) | 19691 | 1ddf995ecced7309c3e091a07b443f8f8e5201565c3ce0f061e54bb96919dba8 |

32个当前输入回执逐path/bytes/blob/SHA相合，10个历史输入按原身份恢复。
唯一科学子进程返回0；数学时间1.928151968秒、子进程墙时2.039417720秒。
完整418个共同格、13376个子格完成；其中417格使用原positive行，另格使用真根germ。没有未完成prefix提升为结论。
一个新的完整积分目标产生两个完整scalar记录：T2以及由它和旧已成体费用导出的Q。
旧数值producer、旧已成目标重算、容量ODE、geometry ODE、数组/Release/artifact发布均为0。

算术为320bits；每个原共同格32子片。真实根仍为
$$
r_*\in\left[\frac{1191984371497}{5000000000000},
\frac{2383968743003}{10000000000000}\right].
$$
原candidate ac1d5b98…、continuous repair440866a3…、α/ν0/η0、独立mean、3594原接口、原high97及两轴完整保留。原parent intrinsic球不因子分片而缩小。科学输入和明确范围以manifest及完整记录为准。

## 2. 两个保存后读回的完整球

采用 [R146 QP.3–QP.6](R146-quadratic-cap-and-true-root-capacity-screen.md) 的新函数
$$
f_2(x)=(1-x/\ell)_+^2,\qquad \ell=3/200.
$$
科学记录的完整积分球为
$$
\left(10296445808233199453508969746577455698130222248041359588895338967208252515625552
\ \pm2\right)10^{-77}.
$$
因此该所选完整upper满足
$$
102.964<T_2<102.965.
$$
这里T2是对完整非负被积式的有向上界；左端只描述该保存上界的数值，不声称它是原积分的lower。

必要测试保存球为
$$
\left(-16618553692622208609627142589807232476336987182785974743386962564447384758514648
\ \pm2\right)10^{-80}.
$$
所以
$$
-0.166186<Q_+<-0.166185<-0.16618<0.
$$
以上仅为对完整已保存十进制球的有理比较，不另执行积分。
原 T2 和 Q 球都在比较严格符号前保存并读回。
科学记录 complete=true、proved=true，唯一排除门 selected_correlated_RA_receiver_budget_excluded=true。

## 3. 这具体排除了什么

[R146 QP.1–QP.9](R146-quadratic-cap-and-true-root-capacity-screen.md) 已证明：对该费用格式任意合法有限负部支付器、正径向权及自由外截段，完整真实根型迫
$$
(\alpha_E^{\rm root})^2>\frac{148\Lambda^2}{T_2}\ge\frac{148}{T_2},
\qquad \Lambda\ge1 .
$$
该lower来自准确容量的对偶测试，没有从一个容量upper倒推lower，也没有把真正 $D_H^{-1}$ 换成统一λ。

令a、b为R143实际保存的所选aEE、aEB upper，c为原GB所选aBB upper。
完整非负费用门若正定，必须
$$
2-\frac{148}{T_2}-a-\frac{b^2}{4(1-c)}>0,\qquad 1-c>0.
$$
本次用T2完整upper及a、b、c保存球的lower端点计算最有利的必要upper Q+。
其严格为负，故当前CV/RA门不可能通过。加入该格式剩余非负root/source/cross费用不能修复这个负方向。

原[R143实际体三门](R143-supplement-actual-correlated-body-budget.md)的成功、Ccorr等六球及其中“最优必要门当时未排”的准确资格均保留。
新结论排除的是另一个完整体/根组合，不倒改原成功。

## 4. 后续执行选择

不再为这个已排CV/RA非负预算运行新的容量Gram、扩大high截断或只细化DH逆。
保留真实PDE可达迹关系、同向有符号联合估计与直接完整逆作为不同输入；它们不受本次预算排除直接否定。
R142未成低缺陷的实际续算及其真实58/224/32后继仍独立进行，所有均值、源、physical边界、负侧、true phase/ν及非线性匹配继续支付。

本结果是严格路线排除，不是精确闭等距族的存在性或最终验收。
