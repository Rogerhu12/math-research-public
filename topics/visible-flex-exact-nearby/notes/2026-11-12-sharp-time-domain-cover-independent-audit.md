# sharp time-domain cover：独立数学与来源核查

2026-11-12，independent_audit。核查源码
[fourfold_phase_sharp_time_domain_cover.py](../scripts/fourfold_phase_sharp_time_domain_cover.py)，
SHA256：

    582d97cf2a14b7d45050770527acf97a3bde1cfda565df4f29dc309633950ba3

已读完整351行，并回读冻结 PiTime 和前一篇 sine/reflection/turn 审查涉及
的接口。本次没有重跑整条时间网格；下面是新分割、继承和覆盖逻辑的核查，
不是额外数值证书。

## 1. 准确端点给真实 germ 覆盖

PiTime 保存准确有理 \(q+p\pi\)，反向时间先按有向差的严格符号排序。
两个端点均明确检查在物理支 \([-\pi/2,\pi/2]\)。在这个支上，真实正根
\(t\) 的 \(t\sin\tau\) 单调，故分别计算左端球的下端和右端球的上端，
就包住整条真实径向像。准确端点 \(\pm\pi/2\) 直接使用 \(\pm t\)；
这避免在转折端靠三角舍入决定是否越根。

arf 端点经 fmpq 变成准确 Fraction；没有通过 binary64 中点选择 span。
所有与该闭像相交（包括仅相触）的共同 spline spans 都保留，且检查
首末包含与逐段相邻。因此极窄或端点相触的多项式 germ 不会丢失。
真实径向像还必须严格位于共同物理定义域及其反射交集中。

## 2. 同一真实对象的域继承

Domains.add 只接受已标记完整且已证明全角/复时间域的来源报告，并要求
同一准确对象 SHA、同一真实根报告 SHA。继承以准确共同 germ 作为 key，
且旧物理角宽必须包含新角宽。

若中心与半宽（允许半宽反号）准确相同，且新 normalized radius 不大于
旧值，圆盘包含准确成立。否则程序向外计算

\[
 |c-c_{\rm old}|+R|h|<R_{\rm old}|h_{\rm old}|
\]

的严格间隙。这里使用真实 \(\tau=c+hu\) 的物理时间圆盘，故没有漏掉
新旧半宽比例。PiTime 的球误差全部进入所需上界及已付下界。

反射条目把 germ、中心、半宽同时取反。由真
\(F(-r)=\operatorname{diag}(1,1,-1)F(r)\)，
\(\mathcal D,\mathcal W,K\) 偶，\(\mathcal M\) 奇。
两分支的场模数和其角一、二阶导数都采用
\(|\mathcal M|+|\kappa\mathcal W|\) 的共同上界，故反射及交换分支不改变
这些可用上界。原来使用 root-deflated \(Q\) 的域继承后仍标记其原
curvature kind，没有伪装成普通域的 \(\operatorname{Re}(-K)>0\) 证明。

继承的 true field moduli 属于已付物理域。下游若重新选另一普通/turn
计算 frame，仍须使用其自己的真实 field 实现；本记录不据继承字典
抹掉 signed root factor 或将其替换成未经证明的平方根分支。

## 3. 新门与全闭区间递归

未继承时，anchor 根据实际所选 germ 的正负决定是否反射；在腰圈
相邻正负 germs 上不能只根据同一个时间中心的符号决定。
反射同时改变中心、半宽，所以真实 normalized anchor 不被错移。
原有 D 差量从准确 anchor 减去常数项，初值和外盘尾费用均保留。

有 \(\pi\) 分量的端点使用已付 turn 实现，且要求真实根 germ 唯一；
普通段使用保持物理支的 sine 实现。两个实现的数学域门分别是
真实 deflated \(Q\) 和普通负曲率门，失败就细分；未把两者混用。

每个失败段按准确 Fraction 中点二分。成功 leaf 的 normalized 子区间
由程序构造保证正长度；最终逐项检查从0开始、到1结束及相邻端点准确
相等。因此只有全 leaf 成功才将该 case 标记 proved。父段的失败记录
被保留，但不阻止两个完整子段替代它。到最大深度仍失败时，留下的缺口
使 case proved 为 false。

全两腿结论还要求全部 requested cases 已证明、forward/backward 均在
请求中且请求为 all。顶层 complete 只表示本次循环结束；实际消费者
必须读取 proved_all_requested_cases 或 whole_both_branches，不能只看
complete。源码已经将这些状态分开。

## 4. 文件和范围

resume 比较实际对象、根、网格、源码、域宽、精度和采样参数；成功 leaf
还核对其准确端点与子区间。索引保存 leaf 路径和 SHA。对最终可重放包，
应照这些 SHA 保全并核对全部 leaf 文件；resume 的 done 集本身不是
重新验证每个已保存 leaf 文件内容的工具。数学继承把已证明来源报告
作为输入，来源报告的完整性不能由同名文件自动替代。

本轮未发现 sharp endpoint、圆盘包含、反射或递归覆盖公式的实质缺口。
它支付的仍是实际场的全角/复时间定义域及模数，不是积分轨道、ODE
缺陷、全返回映射、KAM 条件或完整 PDE 逆。
