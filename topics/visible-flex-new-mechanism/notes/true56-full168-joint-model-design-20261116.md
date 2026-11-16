# 真实点56的全168变量联合模型

日期：2026-11-16。范围是一次真正新增的完整场模型，不重开已经接受56而闭合的旧九维账户。主 README 完成门仍未满足。

## 1. 起点、固定对象和来源

[真实56](true55-new-nine-original-two-grid-accepted56-20261116.md)的独立168向量 SHA 为 aa7d8f3fb4d1bfea7aa4a05fef3b23babefbc344c5ea78f7b321b141a2d5181b，物理172状态为 11c07425846f224c2d05997068b6442fa28a65383b5af5dce3eb2789da0593dd。原两网14门和准确172盒已通过；粗/细 $\eta$ 为 .2660099234147515/.2660099232963724，细网曲率57.9994439861529，均不是主完成证书。

当前点的新九个系数非零。全部168列须在同一当前完整场求导，不能拼接55的旧159最终 Jacobian。[导数设计](complete-body168-current-state-selected-jacobian-design-20261116.md)及 [R497](../results/R497-complete-angular-primitive-and-axis-metric-curvature-response.md)保留完整角原函数及其对 $X_s,X_{ss}$ 的记忆。原网格、参数、永久参考 $c_0$、固定 $g,b_0$、所有硬门、容差和 floor 不变。

来源是 run43842056373/research133212892062/source86852956f10ec609ba423990a40327284f081c44。原stdout53920117B/53abf31d239449f7a1c4cddb2b3dd788438e403d6358566296afba7e4c84a042；读原 COMPLETE、CACHE2、FINAL_CLOCK。CACHE2只有当前 U/T/e/f，无位置、曲率二jets和J，故本新模型需两次完整当前 ordinary 输入。

另只读原55 run43832870561/job133182173190 的 COMPLETE，取得56的小checkpoint未重复保存的永久参考/height-map构造资料；校其旧159恰为56的前159、cfg一致。此第二次日志读取不执行55 geometry/J/有限求解/验收，也不恢复旧任务余额。全部来源读取计入本次时钟。新模型的 pools/order/versions 用实际56的4453/4549、v14/14。

## 2. 172物理坐标中的新步长规范

令 $q_*\in\mathbb R^{168}$ 为真实56，$c(q)\in\mathbb R^{172}$ 是原准确仿射物理坐标。其线性部为

$$
M_{172\times168}
 =\operatorname{diag}(I_{154},H_{9\times5},I_9),
\qquad c(q_*+\delta)-c(q_*)=M\delta .
$$

这里 $H$ 为原有理五维高度零空间基，而非旧163归一化矩阵。构造代码逐项保存其有理数定义；浮点有限矩阵只作数值提议，实际点仍按准确仿射有理坐标验172盒。

本新任务有限变量顺序为 $(\delta_{168},\rho,h)$，全部168列可动。目标及步长：

$$
\min \rho+10^{-6}h,\qquad
4\|M\delta\|_\infty\le h,\qquad 0\le h\le1 .
$$

因此每个实际物理系数的提议变化不超过 $1/4$。原163盒加新增九个 $[-1/4,1/4]$ 盒全部保留。旧159学习 gamma、controller 和 defect 范数不移植为新168证书。

## 3. 原行与两个不同的预测函数

两池全部合法行都进入当前 selected168 导数，包括端点、零导数和新增九列支撑区外行；不沿用旧九维支持过滤。原硬行值 $v_i$、容差 $\tau_i$ 和 fraction $f$ 给

$$
v_i^{\rm target}=v_i-f(v_i+\tau_i),
$$

再保留原 strip/curvature floor。硬约束为 $v_i+J_i\delta\ge v_i^{\rm target}$，容差仍为原 $10^{-7}$；原 metric 行容差仍 $10^{-9}$。

记原平滑双分支

$$
\phi_\pm(e,f)=\tfrac12\left(\pm e+
\sqrt{e^2+4f^2+\epsilon^2}\right),\qquad \epsilon=10^{-8}.
$$

有限主模型及全网分离用同一基点的一阶函数

$$
\phi_i(0)+D\phi_i(0)[\delta]\le\rho,\qquad \rho\ge .26.
$$

每次分离完整扫两网、两个分支和常数目标；一个新方向各调用一次当前场全网 first-jet JVP，不铺全网168参数张量。若未合格，只能加入真正缺失的原 material/branch tag；相同有限行集不重解。新增行的梯度仍在56基点，不改成试探点切面。

合格方向的 $(e,f,de,df)$ 缓存供后续独立标量函数

$$
\max_{i,\pm}\phi_\pm(e_i+\alpha de_i,f_i+\alpha df_i)
 +10^{-6}\alpha\,4\|M\delta\|_\infty
$$

使用。这是 affine-observable 预测，既不是前述基点一阶最大值，也不是实际 nonlinear geometry。其合法 $\alpha\in[0,1]$ 区间保全部原硬行、准确盒的浮点区间提议及物理步长；每个舍入实际点再过准确172盒/步长。仅合格预测才进入原实际验收。

## 4. 原实际门与有限返回

每次170变量有限返回先保存真正 raw170、dual/slack、全部原残差和停止原因。把 $q_*+\delta$ 舍入后，重新以其实际位移修复 $\rho,h$ 并判原有限行，不把 solver status 作为几何接受。

实际最多三个不同尺度，先 coarse，只有可能通过才算 fine；原两网14门与172准确盒不变，首次接受57或失败新增物理行/容量事件即闭当前方向。接受点给完整168状态和独立原几何指标。任何有限停止、局部无方向、未达到 .26 都不推出全类无解；即使接受也仍未付连续 reach/主全时同 $g$。

## 5. 一个新账户与输出

所有新研究仅公开 Actions，单核、原固定 Python/numpy/scipy/clarabel；预import启动同一600秒时钟，读取、失败、输出均计入。计数上限：

| 项目 | 上限 |
|---|---:|
| 必要当前 ordinary 网格值 | 2 |
| 当前全部原池 selectedJ168 网格构造 | 2 |
| 完整两网分离 | 8 |
| 新 material/branch metric 行 | 32 |
| 严格新增行集有限主问题 | 8 |
| 每问题 iterations/Newton systems | 96/192 |
| 同账户 iterations/Newton systems | 768/1536 |
| 标量 sessions/queries | 1/64 |
| 实际 pairs/完整网格值 | 3/6 |

旧祖先成本2233.566394556秒/138值只作为闭合历史相加，不重新给旧任务计算额度。实际超时、失败和已开始调用如实保存，最后大输出后 FINAL_CLOCK 为权威时刻。

成功时一次 INPUT 保存 current hardJ168、softg168、base/targets/tags、物理 map 和中心/盒；MODEL只引用此绑定，不重复大零阵或两网 ordinary。每个真实有限原始返回留 stdout，选定方向及新接受点各有缓存记录。构造失败则保存实际已完成输入供同账户接续，不伪称完整模型。机器payload不进Git、artifact、Release或跨run cache；136MiB为本新任务stdout限额，独立只读report至多读160MiB、输出6MiB原语义投影。

源码、参数及本设计随一次提交发布；push启动新 workflow。结果另写人读结论即时推送，HANDOFF持续更新。
