# R683 的 SO(3) 应用：先补真实违规地点，再做同父全行分离与 SOC

日期：2026-11-26。会话：Astra-larger-e4e2a2bf-20261126。
这是一份完整算法应用与源码说明；半空间修正的抽象命题沿用 R683，
不把新增数值策略重复登记为一条已证几何存在定理。
新科学入口尚未执行；下列实际数据只属于已返回的 03b 旧完整 606e 入口。

## 1. 这次改变由什么实际证据决定

公开 run 45820592817/1 的 stage 3 原完整入口使用
606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9。
它的实际 report 为
989740cd8408c317b4540c3efa82b6ab35de269dcb200932f4d1d19d370773d1，
末 checkpoint 为
fbf2b38ca6b4557568d06b05f91589ac4d463f660c877a2cb39396ab0cfe0337。
初始参考仍为 0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1，
固定标量目标仍为
6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb。

后续纯读取 stage 7、10、13 没有重算方向、场或 J。完整实际记录见
2026-11-26-public-actions-45820592817-1-part-002.md 和
2026-11-26-public-actions-45820592817-1-part-003.md。

旧首方向的 QP 是 16 步 iteration_limit，末面投影梯度
2550.6296140330887 对容差 0.002450868590297488；它没有驻点结论。
原选择器实际给 28 条曲率行，附加 6 条幅度行，总共 34 条；
192 是原选择器的上限，并不表示曾删掉另外 164 条实际行。

更直接的阻碍已由完整真筛查明：

| 原射线 alpha | 实际 reach_g | 其他说明 |
|---:|---:|---|
| 1 | 未读几何 | 实际 Phi 未下降，域检查通过 |
| 1/2 | 31.90436616181289 | Phi 真下降，全部幅度行通过 |
| 1/4 | 15.500572782613311 | 同上 |
| 1/8 | 7.27473500670862 | 同上 |
| 1/16 | 3.155814733918934 | 同上 |
| 1/32 | 1.0948541225127562 | 同上 |
| 1/64 | 0.06399761652393754 | 同上 |
| 1/128 | -0.24277976938999402 | 完整真筛通过并接受 |

这六个真几何拒绝均落在 literal 地址
cell=0, u=0.5, phi=1.5707963267948966, branch=0。
不能把已经有真下降的 alpha=1/2 至 1/64 归因为目标函数没有下降，
也不能用调 mu 或盲增 Krylov 预算代替遗漏的曲率约束。
旧方向结束后原 C cache 已按明示规则清理；本入口不声称继承它的字节。

## 2. 完整新入口和来源

新 driver 是整个旧 606e body 的独立完整后继，具有新 schema：

    complete-independent-axisymmetric-fixed-deep-so3-prior-separation-and-SOC-v1

原物理算子 7f26、原世界坐标几何 adapter 2240、原正权谱 Hessian、
原全变量 H2 坐标与 fb4e QPv3 源均保持其真实来源。
没有把旧 canonical source 标签贴到新算法上，也没有重标目标 g。
本次实际使用的是原 SO3 的新 node-jet H2 型范数，
不是旧 q 参数化母范数的冒名替代。

derive_axisymmetric_so3_soc.py 只执行 stdlib 源字节、AST 和 JSON 操作。
它绑定整个 606e / a942 原体及整个新 helper，逐个 literal replacement，
再核所有未涉及的原顶层函数、CommonSlackRows 类和 main 内局部
statistics/geometry 函数的完整 AST。它可重现完整新 driver/launcher；
bind_report 直接比较整个生成体与实际公开体。

最终源码全部位于 scripts/resume_20261126：

| 源码 | 字节 | SHA256 |
|---|---:|---|
| complete_axisymmetric_so3_rows_soc.py | 40311 | 02875e4a150644f8addb6073b346e2de3b0f3cf50498e9cf6efe8fe0333d7c97 |
| fullclosed_axisymmetric_so3_separation_soc.py | 60732 | 359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d |
| launch_axisymmetric_so3_separation_soc.py | 9996 | faf5f67000eb81a0bc6d26126641f10c606a879f935158222b1fce0f50525d02 |
| derive_axisymmetric_so3_soc.py | 34017 | fea20e0b00fc55bc00d450947154a3f17de5a9ee4a71b0ea4b0aec7082ba1aa4 |
| read_axisymmetric_so3_separation_soc_report.py | 37181 | f68618ed67a41d882b4f5eaefc28fa5c50bb77bf016f49fe4d6814304d0f9850 |

完整参数在 axisymmetric-so3-prior-separation-SOC-first-ready.json。
它含一个实际 solver 后继和一个独立纯 reader；根代理是唯一队列写者。
参数草案是同 fbf2 父、同 g、p=4、epsilon=.001、scale=.05、
同 mu=.01、1 个方向、maxiter=64、至多 8 轮 SOC、
tau=0、observed inward fraction=.125；其余完整物理/幅度/观测参数逐项保留。
64 只是新的显式数值预算，不是收敛断言，也不是单一变量的加速比较。

## 3. 先在新父上补行，再解它的 QP

每个新 metric 方向先完整重读当前场与永久地点，并只调用一次原
screen.build_rows。它得到的整个曲率前缀及全部幅度行作为 literal
不可改写前缀。之后从已绑定实际父报告及本次已返回方向报告中，
收集真实完整拒绝的地点，去重键用 literal float.hex，不作小数归并。

继承的只有地址与其真实来源。所有 g、点场、主曲率、世界 VJP、
完整 H2 转置均在这一次的新父 x 重新计算。
每个先前真实 reach 违规地点补两个主曲率分支，并以当前父完整
真筛实际 D 最大分支作直径伙伴。因此首个已知的 cell 0 中点
不会刻意等到另一次新方向真违约后才进入 QP。

原选择器行不被新 selection 替换。补行之后冻结这一次真正送入 QP
的整个前缀，包括曲率、幅度、pre-QP separation 全部行。
记录两份不同含义的 hash：原 selector+amplitude 的 literal 字节前缀，
以及补行后完整实际 QP 的 literal 字节前缀。

若一条新行在当前父的实际 b 为负，源码明确要求真实 restoration
或另一父，不把负 b 的零步称可行；不会为了继续求解而删掉该行。
本次 Phase I 的原完整 CommonSlackRows 主体没有变，
它也从来不把 tau 当作真实几何可行性。

## 4. 新补曲率行的完整当前自由量导数

令 K_b 为某地点的一条主曲率分支，D_j 为一个固定地址的直径下界
函数，rho=.03，sigma=.992。对应必要约束为

$$
g_{bj}(x)=\rho D_j(x)|K_b(x)|-\sigma\le0.
$$

在父点 K_b 非零、主曲率间隙严格正时，

$$
dg_{bj}=\rho\,[D_j\operatorname{sign}(K_b)\,dK_b+|K_b|\,dD_j].
$$

源码对新行显式要求有限非零 K_b 与有限正 principal_gap；
零值绝对值和重特征值的普通分支导数不可直接套用。
该数值导数不可用不是几何不可行或不存在性证明。
这里没有设置人为 gap 容差，也没有放宽实际几何筛阈值。

点半径伙伴满足 D_j=2|F_j|，故 dD_j 的世界 F cotangent 为 4F_j/D_j。
高度伙伴 D_j=2|H| 的导数为 2 sign(H) dH；固定伙伴 D_j=2 的导数为零。
dK_b 的全部六 jet cotangent 通过当前真实 7f q.point_vjp，
随后通过原 coordinates.transpose。不能只微分 Fss、不能冻结当前
core inverse chart、闭合 Delta 或自由 H。

幅度行调用整个原 2240 _amplitude_row。
特别是 witness distance 中 p=(0,1+sum ALL current core,0)，
它的额外自由 core 导数在全坐标转置前加入；两种 witness 符号均保留。
body、cap、height floor 与原预算保持同一语义。

每一行以父点完整坐标 covector 范数作正归一化。若完整梯度为零，
该行按 scale=1 保留，绝不在缓存中删掉。R683 数值内核若因此无法
使用正 Gram 对角，明确返回数值未给出修正；不会冒充 Farkas 证书。

## 5. 同父、同一个原射线锚的多轮全行 SOC

设 T 为当前完整坐标 lift，原 QP 的坐标步为 d。
选择第一次通过真实同 Phi 下降与正域、但完整真几何拒绝的原射线，
记 d_a=alpha d、x_a=x+T d_a。

源码绑定 x、d_a、alpha 与实际 x_a 的字节身份。
后续每一轮都使用同一 x 和 d_a。
上一轮被拒的修正点只提供新的真实违规地址，
它不会变成下轮的父点或新的 d。
若当前原 ray 的实际浮点 point 与 x+T(alpha d) 不同，
明确不使用该锚，不虚构另一次未读的实际点。

对旧 QP 全部行及当前所有追加行，令父归一化为 n_i，
$C_i=dg_i(x)T/n_i$，$b_i=-g_i(x)/n_i$，
$r_i=g_i(x_a)/n_i$。每轮都实际重读所有固定行函数 r_i，
包括相同的原 radius 伙伴地址与原尺度。

取

$$
\operatorname{inward}=\tau\|d_a\|^3+\theta\max(0,\max_i r_i),\qquad
k_i=\min(b_i-C_i d_a,-r_i-\operatorname{inward}).
$$

完整 R683 内核求数值最小范数半空间修正

$$
\min_e\frac12\|e\|^2\quad\text{subject to}\quad Ce\le k.
$$

于是任何精确满足这些半空间的 e 都有
$C(d_a+e)\le b$ 和 $r+Ce\le-\operatorname{inward}$。
这只是 R683 的全行代数应用，不需要 C 满行秩。
theta=.125 付的是本次已观察的违规规模；
它本身不是一个普遍三阶余项定理或严格全局几何可行定理。

数值内核用完整 C C^T 的非负对偶坐标迭代，并从原完整 C
重建 e、直接复读 C e 与 C(d_a+e)。
预算内返回的数值可行迭代可以被提出，
但 minimum_norm_convergence_claimed 字段保持内核实际结果。
失败不证明半空间不可行，投影成功不证明真实几何通过。

每次完整真几何拒绝后，源码在原父 x 补其实际最坏地点的两分支、
该被拒场实际 D 分支地址，并保留此前所有行。
幅度若真违规，同样把真实候选地点的完整原自由量行追加，
距离地点总保两种符号。若无新行，不重放同一投影。
至多八轮；原射线回溯仍保留。

## 6. 修正的接受责任

一条修正 z=d_a+e 有独立的当前 A z，重新计算完整同 Phi
半斜率与二次预测。原 ray 的 A d 或预测不借给修正使用。
随后完整重读实际 residual/statistics、正域、整个原 grid、
所有永久 curvature/radius 地址、两 witness 符号和幅度/曲率真筛。

只有真实 Phi 严格下降、相应 Armijo 规则及完整真几何全部通过，
才接受该修正。所有拒绝试验发现的地点仍进入永久记忆；
最终场还会对扩大的记忆作完整重读。

原 ray 接受保留 accepted_alpha；
SOC 接受的 accepted_alpha 是 null，
另记 accepted_step_kind、accepted_SOC_round 和 original anchor alpha。
SOC 自己的预测比值单列，不能拿原全步预测解释修正的下降率。
当前源在 SOC 接受后保留原实际 mu，不把原 ray 的调参条件移植过来。

这些完整有限读取仍不是连续 metric、reach、all-t 或 C2 数值误差证书。
最终目标函数与几何误差、归一化/求积/逆图误差仍须由同场连续链支付，
并完成固定 g 的 J/M/N/工作求值精化。这里没有解除题 README 的任何条件。

## 7. 同一缓存的 literal 追加

Helper 绑定原 row-major float64 mmap、完整原 bounds 和每行 metadata。
第一次需要扩容时只 extend 同一文件；随后只写新增行索引。
预留容量不是附加约束，used prefix 才交给投影；它也不是 RAM 上界。

每次追加之后直接读旧 selector+amplitude 前缀 hash；
QP 冻结后还读完整 QP 前缀 hash。投影结束后再核两者。
保存真实 used/capacity bytes、已分配磁盘块、原/新增行数。
不会每轮造一个新的多 GB 完整 C 拷贝，也不会用小数地址合并删行。

候选新 covector 的临时数组只供实际源求值与追加使用，留在 runner。
完整 C、checkpoint、场/J 原始数组都不写进仓库。
自然返回后 controller 可按明确目录 pattern 清理新生缓存；
报告保存已发生的 direct-readback/hash 证据，后继新方向再造其真实新 C。

## 8. 纯读取与检查状态

独立 reader 绑定完整新 body/source roles/deriver，而不是冒用旧 6d。
它核 pre-QP 行数、完整 QP 前缀、同 x/d/范数/模型身份、
每轮实际追加数、完整直接读回、真实 A z 与真实接受条件。
原 ray 和 SOC 分别计数；每个实际拒因和未执行的检查分别输出。
8 轮以下 compact JSON 字符串保留全部实际 round，不截断后误称全数。
iteration_limit、projection sweep limit、真实违反、几何可行分别记账。

原 8141 helper 已在环境中实际 AST/compile 通过。
最终 02875 相对它只增加上述非零简单分支合法性条件；
最终五源在环境断开后按完整文本恢复和保存，
字节 SHA 与整源替换已核，尚不声称最终新体已在 Python 中完成
AST/compile 或科学运行。独立 deriver 自带纯 AST/compile/full-body
检查，可在可用执行环境或原 Actions 入口作真实检查。
这一状态不被写成一个数学发现，也不是请求用户等待的审批门。

原公开 606e/a942/6d、原数值源、所有旧实际报告与结论都保持。
新入口是否产生更大的合格实际步，必须以随后真实返回为准。

## 9. 执行环境恢复后的实际静态补记

最终五个完整科学/执行源码的字节与上表锁值完全相同。环境恢复后已真实执行stdlib AST/compile、重复literal-key检查；纯fea2 deriver从完整606/a942/02875重生359f与faf5，完整字节及全部未改函数AST相符。root通读全部helper、driver全部变化段、完整reader/参数及本说明。未在本地运行F/J或任何科学fixture；新实际结果仍须由公开Actions返回。另0f542/95e90/1e207内点继续三源也补做了实际AST/compile-only，其已刊字节未变。
