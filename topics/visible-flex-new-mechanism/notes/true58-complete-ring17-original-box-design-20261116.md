# 真正58整圈17系数：原盒内曲率问题与唯一完整非线性候选

日期：2026-11-16。新科学任务设计；提交时尚未执行，不预授可行性、下降或主完成门。

## 1. 直接问题与已有实际来源

[R510](../results/R510-original-three-spline-ring-metric-neutrality-and-affine-axis-curvature-control.md) 与 [R511](../results/R511-complete-ring-curvature-intervals-and-shared-seventeen-coefficient-control.md) 给原最后三根五次样条的完整 R2 延拓。它在指定实际环上值和一阶径向导数为零、二阶导数为一；原 u 的九个角模态和 v 的八个角模态给共同十七系数。有限变化准确保该环 X、全部一阶 jets、实际第一基本形式及法向，只有正交化 shape 矩阵的第一对角项变化。不是把每个角点独立调成某个曲率。

当前状态来自 [实际58](true57-nonlinear168-original-two-grid-accepted58-20261116.md)：run 43859882465，research job 133273598120，source 0e6fafbf7bce37cd851dfc972b2de1ff3d0d5881，原两网14门/准确172盒通过。最大 η=.26600541463999305、细网最大绝对主曲率57.9997782607127。细网曲率峰在 s=.78、θ=4.818744981678094，是非反射轴点，不能按输出的两条 principal 顺序猜测径向或角向分支。

新任务读取原 research stdout 86358161 B / SHA256 346de3d6027e21e3b3d9dc020b0890c14d65e6dc588c2178ee63eff9f12fca3e。COMPLETE、第二份接受后 CACHE、FINAL_CLOCK 的字面 JSON+LF 长度/摘要在请求和 transfer 源中列全。CACHE 保存该点完整 U/T/e/f、原网格和原 selected pools 的二阶 jets；不是完整网格二阶 jets，也不是58的参数 Jacobian。这里不重放普通几何或旧 Jacobian；圆周尚未保存的真实二阶几何重新收费。

永久 enriched reference 与高度映射构造仍来自原55 COMPLETE。这只是构造来源，当前168坐标及其中旧159分量都读取58。原55、56、57的几何、导数、接受和优化器不重跑。同一固定 g、b0、参数顺序、98项原输入、原14门与容差不变。

## 2. 完整实际环的系数

保原160条径向网格及384/768个角点，目标环使用原下标141。原节点写作39/50；实际代码从已付 radial 数组取得 binary64 值，并按该真实值的精确二进制有理数构造 R2，绝不把实际浮点节点假称准确39/50。

若没有同点完整环二阶缓存，重新计算原下标 [0,141,159] 三条真实径向行、全部角点的曲率预测，以满足原高度/端锚接口。每次新 frame、Π、冷高度积分、二阶 jets、shape/principal 评价都计入同一模型构造账。三行均来自实际网格，不插虚假零边界。完整实际 a、a_s、a_ss 从同一个固定 metric 读取一次；不省略 a_ss，也不把实际 G 改成1。

在实际归一化角基 (X_s,X_θ/a) 中，保完整 I=[[E,F],[F,G]] 和 II。令 η_t=F/G、q_perp²=E−F²/G，得到
$$
A=\frac{II_{00}-2\eta_tII_{01}+\eta_t^2II_{11}}{q_\perp^2},
\qquad
B=\frac{II_{01}-\eta_tII_{11}}{\sqrt{q_\perp^2G}},
\qquad
C=\frac{II_{11}}G.
$$
这里 η_t 是切向 Gram–Schmidt 系数，与全局 metric 目标 η 不混用。全部十七列逐圈使用当前 frame 与完整 Fourier primitive Π；新环模型为
$$
S_\xi(\theta)=
\begin{pmatrix}A(\theta)+\ell(\theta)\cdot\xi&B(\theta)\\B(\theta)&C(\theta)\end{pmatrix}.
$$
原末三样条的完整区间延拓和精确嵌入权保留；不只在末片写多项式而把外段截零。十七参数映到原51个 u/v 物理坐标，原高度/Q/新九列的增量是零，当前新九坐标仍保其真实非零值。

## 3. 原完整盒内的唯一十八变量问题

目标 K=1000/61。先保存全部实际 A、B、C、ℓ 和不变列下界 sqrt(B²+C²)。若任一浮点角点的下界超过 K，该浮点模型已阻断纯 R2 路线，直接结束这次 ring 问题，solver 调用为零；这不是准确连续全圈的不可行证书。

否则只解一次十八变量 (ξ,h) LP，目标 min h。每个两网角点分别使用 K I+S 与 K I−S 的 trace 和 determinant 四条仿射行。这保 |C|=K 的退化边界，不除以 K±C。所有原172上下盒、准确的物理增量映射及 4|Δphysical_j|≤h 都进入问题；所有变量先声明自由。h≥0，并由原盒导出有限上界。

本问题**不把旧1/128限制作为新可行门**。所需 h 与1/128只作为幅度对照；上一已闭小步/锥任务没有重开。LP 是不同的完整圆周问题，不含逐点独立调参或重复原行集。仅一次新 HiGHS 调用，调用时间限最多60秒，同时扣去本次装配和导入已经消耗的时间，且不越过总600秒剩余授权。实际返回可能略超 backend 时间限，必须按真实终时入账，不把配置值当硬墙时间。

所有实际返回的 raw18、slack、dual、con、backend status 和迭代数在判断资格前保存。非成功、超时、缺失/非有限 raw18 都不给候选，也不据此宣数学不可行。成功返回还须检查原单位浮点行容差和精确原盒。ξ的 binary64 值先作为准确有理数与准确 R2 权相乘，保存理想完整168/172嵌入，再只舍入一次得到真实 binary64 候选。理想环恒等不授给舍入后的候选；全部舍入偏差和准确物理 h 分开保存。

## 4. 唯一候选的完整检验出口

最多一个舍入候选进入已发布的完整 nonlinear metric predictor，以及原整个两网的曲率 predictor。每一新 frame、Π、完整一阶/二阶恢复、height 和曲率/principal 计算均收真实费用。没有线搜索、固定α序列或补解 LP。

只有其全两网预测 η 严格下降且达到原最小下降1e−7，并通过原曲率 PSD/direct 容差，才调用一次原 actual pair，两网最多两份新 full values。预测不代替原14门或准确172盒，也不代替连续/nonlocal reach。实际通过才可记接受59；失败保原58，不以环LP可行宣接受。

若实际接受，依原顺序先学习，再从已付 ordinary 保存 full U/T/e/f 与原 selected pools 二阶 jets；没有额外 ordinary 或 J。导出若部分失败，原接受与其实际费用仍保，未导出部分不得作为未来免费缓存。普通 predictor 大数组不保存为下一点缓存；失败时只保真实数组身份/尺寸和已返回语义，不伪造零数据。

## 5. 统一科学账与输出

政策 true58-ring17-original-box-curvature-and-one-nonlinear-candidate-v1。新600秒从科学进程最早时钟起计，含全部输入下载/解析、数值库导入、构造、模型/求解、预测、实际、失败及输出序列化。次数限：固定metric读取1、已付全firstjet绑定2、ring模型1、有限LP1、候选非线性预测1、actual pair1/full values2。模型内部三行两网重建和逐圈列计入同账，不冒免费元数据。

原祖账2830.778901609秒/147份full values已闭，余额不跨点继承。此次不读当前58 J、不做必要普通几何重放；科学计算不在本地运行。任何失败只终止本有限问题，主研究接 open 的下一条。

最多128MiB原数学 stdout；模型完整圆周系数、LP全部返回和实际接受缓存只在原 stdout/临时runner内。Git只存源码、参数、run/SHA和人读结论；不传 artifact、Release 或缓存，不把大数组提交。COMPLETE 后写入权威 FINAL_CLOCK，后者含输出成本，不能用较早时钟替代。

独立 stdlib observer 在 research 完成后只读其原日志一次，最多160MiB，最多8MiB语义报告。它完整转发 FINITE_RESULT 的全部 raw18/dual/slack，保存每条字面 JSON+LF 身份；大模型和缓存数组仅留原元数据。COMPLETE 内重复 ring_solution 由单独 RING_SOLUTION 原记录引用，避免重复整份返回。任何解析/输出缺口明示，job 成功与否不代科学判定，observer 自身用时不并入科学账。

每个 job 先实际 pull public 和 private，核两 README/QUEUE，出现变更只发差异并停止新科学以待执行新规矩；MR_TOKEN 随后移出进程环境。源码提交触发一次新 run。源文件、输入参数和全部来源身份可复查；无本地执行、开发检查、冻结复跑或机械测试。

## 6. 结果后接续

纯 R2 的不变列若已阻断目标，后继改用原末三样条的 R0/R1，使实际值/一阶 jet、法向与 B/C 变化；这是新非线性问题，不能再解同一个 R2 LP。若 ring 可行但完整候选失败，保具体失败门及原成本，结合原前102坐标和三组51环态处理完整中部耦合。任何路线都仍须支付同 g 全时族、连续metric收敛、闭嵌入、全部非局部reach与宏观位移；当前主完成门未付。
