# R632：从原盒细分后 47 接受的实际同态继续完整方程

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。public Actions 后继范围；所有科学执行仍在公开 Actions，本地只有源码、原日志解析和字节绑定。

## 1. 接续对象是最后已接受的实际曲线

前置为 [R632 adaptive 自然终态](2026-11-28-r632-adaptive-box-natural-terminal.md)：run `46125262371`、job `140918345548`、source `02f00c15aa90c8fb0620006620ff6b4b21e805f7`，实际 2371.696276725 秒，47 个接受、48 次完整迭代；状态 `actual_true_Hermite_iteration_limit`，没有 exception、inflight trial 或未闭 polynomial frontier。

原接受 payload：

```
6270 bytes
c52a8b287813c8cc2c468ab679ddb3d94938d070a5c84000a048d58a6d660dac
```

257 参数列表身份为 `4920` 字节 / `204cf9ddf6cd11e2307887339aee3698781dc4a27815366e9629ca28f2ec2f87`。保留同一个 h/κ quintic、固定 κ 中心导数、由真积分确定的 α/L、八个中心 A 及三个 gauge。没有切回此前的 19 接受源，也不借 R636 或 R641 的新输入替代本曲线。

本轮以真实下一 trust=1、damping=`1.111111111111111e-10` 继续原完整求解器。前置最后 iteration 48 的求解模型 λ 为 `3.3333333333333327e-10`；该步实际接受后原规则除以 3，故这里继续下一 damping，不混淆两个层次。

原初始 28 个真端恢复步、已付粗墙定位、47 个接受和完整 source fine 都不重播。源 J/QR/原母数组没有保存；本轮首个必要完整 J 直接服务下一实际方向，不另设审计运行。

## 2. 同一完整数学和全部原物理条件

本轮直接复用冻结的 `r632_true_hermite_bvp.py` 和 `r632_adaptive_true_hermite_kinetic_chart.py`，不是重新编写其科学循环。全 257 形状列、全部真 η/A/ρ 链、完整母系数、正势系数 1、全程常 gauge 投影、原 Euclidean QR/SVD、固定 UNIT、方向、trust、实际 delta 的 Armijo、真端恢复和原绝对完成门全部保持。

原 `.8<h<3`、`|k|<2`、`|γ|<6`、`|υ|<6` 继续按同一个表示多项式的 outward de Casteljau 包围判断。任何实际点反例拒绝；32768 nodes / depth 40 尚未闭的原前沿继续 pending。η 的真实积分与有限采样检查仍完整保留，四个多项式盒不冒充其连续资格。

源最后 h(0) 为 `.8001110504996927`，连续 h 下界 `.8000810484979294`，连续 υ 界约 `[−5.51058,5.92417]`。这些是这一个源曲线的资格；新 trial 必须重新判断，不能依赖旧 margin。原 `.8` 或 `6` 不会被放宽。

当前归一 P/r₁ 改善而物理 A_p1 增大已经如实登记，不能写成真十末全改善。使用同一原有残差的理由是其零集与原四偶端完全等价：

\[
A_{p_1}=L e_P,\quad
A_{t_1}=\frac L8(e_K-2e_P),\quad
A_{r_1}=\frac{L}{8H^2}e_r,\quad
A_{s_0}=\frac{L}{4H^2}e_s.
\]

原物理盒中的 L、H 都有固定严格正下界及有限上界；因此归一残差趋零才控制原端趋零，但有限一次 merit 下降不保证每个原端单调。所有实际十末仍输出，原 end 门 `1e-8` 仍逐值判断。没有把未合格端赋零或隐藏在独立记忆中。

本轮仍欠 P、r₁、s₀、两条原 ruling 和原 ODE。源“iteration-limit”只给出继续真实求解的切点，不是研究停止或参数族不可解的证据。

## 3. 固定 fine 与真实资格继承

粗层不变：64 panels ×16 Gauss 加129个读出点，共1153点。新实际 payload 的 fine 为128 panels ×16 Gauss 加257个读出点，共2305点，完整冻结 q、α、L、八中心 A 和三个 gauge。不得重解幅值、尾锚或 gauge 来使 fine 变小。

只有整个物理 payload 与原源逐值相同，才继承前置已完整完成的 fine；其原 end/ruling/ODE 仍失败的结论也一并继承。若首个必要 J 的数值重建改变了任何已表示 α/A/gauge，或任何实际步骤改变 q，则以新 payload 自己的冻结 fine 为准，不能凭“同一函数公式”继承旧数值读出。

原 ODE/feedback `1e-7`、end `1e-8`、ruling `1e-7`、history-change `1e-7` 不变。两网数值变化没有被当成连续积分误差证书，long-double spacing 没有被用作降低门的理由。

## 4. 成本与运行接口

原 2371.696276725 秒、0.7290429109999934 秒 source preload、49 次完整历史调用、48 次 jet 历史、115298 个 coefficient jet、48 个完整因子、52 次阻尼解、70 个原域拒绝及全部旧费用保留。费用链也明确包含原 R632 989.736104011 秒与已自然完成的 R636 3146.9147376349997 秒。不同字段的重叠时长不重复相加；其他活动范围的费用不记成零。

新 driver `scripts/r632_adaptive47_true_bvp_resume.py` 只适配这个真实新 source 的唯一 FINAL、48 个 STATE 事件与47次接受身份，恢复原 trust/damping，输出完整继承链；科学函数直接调用冻结原实现。全部 source 本地检查只解析 AST/JSON 和字节绑定，没有导入并运行科学模块。

请求 `computations/request-r632-adaptive47-true-bvp-resume-20261128.json`，workflow `.github/workflows/visible-r632-adaptive47-true-bvp-resume-20261128.yml`。冻结 launcher 在科学子进程前一次性读取已完成 job log，匹配原字节/SHA后通过内存 stdin 交付；不会落地原日志或给科学子进程凭据。

本轮仍为3300秒科学边界、180秒末读出预留、最多48次完整原迭代。任何自然边界保留最后接受态、实际 pending/exception、所有费用及下一真实参数，随后按实际未解原方程继续。R641 和 B030 的活动科学日志不为准备本范围而读取，原题完成条件没有变更。
