# R582 真实共振口之后的有限非圆逆设计入口

状态：新正式计算入口，尚未执行科学数值；不是完成结果。会话
`Astra-new-mechanism-0105020f-20261126`。本条接在
`2026-11-26-r582-true-core-shooting-original-terminal-receipt.md` 后，不重做已付的三份
内/外种子比较、24/48/96 维口到 core 拟合或圆核几何恢复。

## 1. 固定输入及新工作边界

输入来自自然终态 run `45812850055` / job `139884885837` / source
`35c249bcad83b95a9a0da6af8cbcd1a7e17b15d9`。原 FINAL JSON 是
382186 B / `384d5f1b0932d3fb09b5ab916e204f71c7016ed5a3c462b0fb3bbad2aafbe742`；
原 stdout 是 1893538 B /
`125bd6c5aec373f7ecab27301dbae6bea25104bae4ff3bde2789875ccc68d211`。

冻结圆背景的 81 个原 q、

\[
 (\mu,\nu)=(-0.040019082162222074,-0.048942275258064924),
 \qquad \lambda=7.136787019826327
\]

及原 M169/factor8 口。这里的 λ 是已付加密真 s-ODE 所给的 core
`A=1/2` 归一系数。原 core C/A 在两个已付精度分别是
`2.9854333168614608e-15` 与 `7.791287084795113e-13`；它们仍是数值根，
不把它们改写成准确全 core 返回证明。

旧连续正 `z_s` 图只复用于**同一冻结背景**构建线性场。此后有限非圆
Model 直接使用 s 参数的空间 jets，既不除 `a_s` 也不除 `z_s`。
任一几何迭代都不得沿用这个冻结背景的正图来宣称自己的正图或 reach。

旧日志保存了口的六 jets 和归一 inner 状态，没有保存整个径向内场。
因此本次有且仅有一份为新目的付费的 dense outward transfer：复用
`alpha160=1006.8799923538346`、`y=1`、
`z_alpha160=.2232703607873784`，同 M169/factor8，从该内口到 s=.82。
它不是零成本，也不是新的 inner DtN 求解。逐段 RHS、段数、旧口差、
整个新科学时钟及原 `actual_weight/outer_RHS` 计数都输出。

## 2. 数学无限核与实际数值 material field 必须分开

数学参照是 R582 的无限全平核。**本次用于几何计算的数值种子是另一个
明确的 C² Hermite 表示，它在数值内尾上有零 suffix。**
`u>=alpha160` 的未计算内尾返回零；由这些零 jets 生成的 Hermite
表示不与准确无限核认作同一函数。两者的 C² 差、有限 DtN 误差及 ODE
浮点传递误差没有认证。本入口不以数值下溢冒充准确全平核已经全域计算。

数值场的中段以同一冻结背景作两条新 s-ODE：从 open core
`(A,C)=(1/2,0)` 正向到 .82，以及从本次新 dense 尾口反向到 .78。
在 [.78,.80] 以完整 0/1/2 jet 的 C∞ step blend 合并；新口与已付口差、
core forward 与新 tail 口差均输出，blend 缺陷留在非线性实际残差中。

所有 ODE dense 值和方程导数仅用来供给**共享结点的端点数据**。
任意材料点实际使用一个共同的分片 quintic Hermite：

\[
 Y(s)=H_{00}(t)Y_0+hH_{10}(t)Y'_0+h^2H_{20}(t)Y''_0
       +H_{01}(t)Y_1+hH_{11}(t)Y'_1+h^2H_{21}(t)Y''_1,
 \quad t=(s-s_0)/h.
\]

不拟合或展开成按数据舍入的全局幂系数；一、二导数直接微分这六个固定
端点基并除以 h、h²。共享端点 jets 给出数学表达式的 C² 拼接。
各正相邻结点比不超过 2，h 的 binary64 减法满足 Sterbenz；左端 0
单独成立。转换 u→s 会把同一个 .82 端口表示成相邻浮点数，故以
`1e-13` 明确合并新材料采样近重结，优先保留所有命名接口；该操作不
修改任何已付几何约束结点。receipt 给出结点数、合并阈值及完整材料
网格/端 jets 的 binary64 SHA256。

其他原 `beta × degree-5 Bspline` 自由角列仍允许在每个 s<L 变化；
这不消除本次**指定种子**数值零尾的事实，也不弥补其无限尾误差缺口。

## 3. 有限非圆模型

在参考圆背景令

\[
 V=A\cos2\theta\,e_r-\frac A2\sin2\theta\,e_\theta
     +C\cos2\theta\,e_z.
\]

原单位切向表示为
`T=(-sin(theta+u),cos(theta+u),v)/sqrt(1+v*v)`。因此固定一阶输入

\[
 U=\frac{3A}{2a},\qquad V_z=-\frac{2C}{a}
\]

分别乘 `sin(2theta)` 加入 u、v。准确圆口的 `p` 导数已经包含在
`rounded_core(p)` 中，所以 u 另减
`bg_comp * 3/(4*.38)`，完整一、二径向导数同时减去该项的导数。
在 open core 上这个校正严格为零，有限 p 的核心仍由原准确弧长
`rounded_core(p)` 给出。

每个 stage 固定 `p=.18+epsilon`、`q=.18`、offset=.2；初始
epsilon=.001，即 p=.181。Model 冻结上述 μ、ν bump 到 log-radius 与
height 中，原 81 个 q 作为新逆设计未知量，从已付圆背景 q 起步。
**q 的均值坐标、p 与诱导的目标均值度量会改变，本次不是固定 g 精化。**

空间 T/Ts/Tss/Ttheta、周期 primitive、实际 E/F、角平均 Ebar、面积
与形算子公式继承原参数化模型。角 Fourier 与径向 Bspline 改用分离
矩阵收缩，避免在细观察网预存四份 `nr × nt × 32` 大张量；参数导数
仍由同一表达式作指定列 forward AD，块宽 16。均值 Ebar 的参数导数
随 q 变化，未漏掉归一化的导数项。

原 FFT primitive 的角截断/alias、背景高度积分和浮点误差仍是数值
误差来源。端点 Hermite 修复了 material 导数的共同表示问题，不能
自动把这些其他误差变成认证界。

## 4. 完整细网、硬几何、固定幅度接受

初始新 81 变量约束网是 97 个等距点、命名接口及已付几何峰的并集，
角数 96。这不是把旧两控制问题的 2413 个已优化结点冒称为新 81 变量
问题已经优化过。每个细观察网**逐元素保留原全部 4811 个位置**，其
binary64 SHA256 是
`e7e3a5bd71f2f61955b02b8a84d5a498f110e03c17c7d3df9bbf08111bb751d0`，
并加入全部实际约束点、相邻中点和新材料场的附加观察点。

细观察并集使用 exact `np.unique`，随后用 `isin` 核验所有已付/实际
位置仍在。它们只是解析函数求值位置，不是除差结点；不会因相邻
浮点位置很近而删掉旧观察。新实际约束节点追加则优先保留全部旧
实际节点的确切 binary64 值。细网整圈为实际角数的 2 倍。

材料附加观察包括端 jets 超过 `1e-12` 的所有节点及其左右邻居、
选中节点间中点。未选端点的最大 jet 也输出；这仅是有限观察，未称
为区间内或连续尾误差界。完整细几何按 256 个径向位置分块读取，每
一圈仍是完整角网，Ebar 从该圈全角均值取得，分块不会删掉任何位置。

硬门沿用联合充分预算
`R=1.012, Y=.3928=1-.6R, tau=.06072=.06R`，以及
`meanE>=.25, det>=.1, z>=.02` 和原 mirror 必要不等式。
非 height 行有 `1e-3` 工作余量，细网工作违约最大值须不超过 `1e-8`。
这些仍只有局部曲率/包围/镜像必要门，没有把它们冒成全点对 reach。

Phase I 只接受完整细网的几何改善；工作几何全过后才进入 metric。
Phase II 只接受完整细网工作几何合格且 η 实际下降的 q。每个 callback
同时读当前**实际约束**最大违约；只有细峰超过它与当前 slack/epigraph
已经覆盖的量，才立即中断增加约束。较小遗漏先入 pending，在自然
backend 返回后一起采用，避免把中间不可行 trial 误当漏约束而每次
只优化一步。

各 stage 的 η 门为
`max(2e-10,min(1e-5,.25*epsilon^2))`；在最终目标 p=.8 还须
η<=`1e-7`。完全通过后 epsilon 才倍增，最多到 .62；q 原样带入下个
stage，p 不被回缩，也不把新 p 下尚未求值的 q 称已接受。
中间阶段的门只是继续设计的条件，不能替代 README 的宏观/固定 g/
全 reach 完成标准。

初始 trust=.01，最大 .5、最小 1e-6；每 stage 最多 60 外层，每后端
最多 80 次迭代，径向容量 769、实际角容量 384。新参数收缩/AD 仅在
同一个正式 run 里首次需要后端时做一次方向核；核后复用已经付过的
同 x0 Jacobian，自动继续优化，不另开验证 run。

## 5. 身份、成本和发布

每个 retained 与最后完整 trial 都保存 p/stage/epsilon。checkpoint
分别保存 `actual_grid_p`、`actual_retained_p`、最后真实构造的
backend p/outer/trust、实际网格、pending、新网格 proposal；在新 p
初始全细扫中断时，旧 p 的资格不会被挂到新 p。自然 OptimizeResult
与异常退出分别记录。每个完成 callback 都在网格/trust 适配前 flush
完整状态；外部 runner 杀死后的未闭工作仍未知。

原三种子、原核心拟合和 true-s 的所有已付 ledger 随小输入保留；
新 field、geometry、AD 块、扫描和全科学时钟另计，不把它们叫免费。
合作科学预算 2400 秒，末尾保留 30 秒打印检查点，job 50 分钟。
runner 开始真实 pull 双仓并核三 README/QUEUE，source/hash/runtime
全部 stdout；不写大数据、artifact/cache 或凭证。

新增文件：

- `scripts/r582_paid_resonant_field_20261126.py`
- `scripts/r582_finite_resonant_model_20261126.py`
- `scripts/r582_finite_resonant_continuation_20261126.py`
- `computations/request-r582-finite-resonant-20261126.json`
- `.github/workflows/visible-r582-finite-resonant-20261126.yml`

本地仅作源码、AST、SHA、stdin 小输入及导入/稀疏检出闭包核对；未作
科学运行。实际 run 的原终态收据另记。即使最后宏观 p 的有限门通过，
仍需在同一 g/参数/t 范围内做真正精化、补连续全点对 reach 和无限尾/
ODE/primitive 误差，才可能达 README 完成标准。
