# 2026-11-26：R582 实际圆核种子与不除 z_s 的核心返回实现

## 固定新输入

源为已付 run45778418134/job139767648038/stage0（source668a3f6c6aee92b00c5ca547dd7677d257d0cdc0）的完整81q，其中前64角坐标精确0、后17是R582逐项核过的真实均值参数。来源actual backend71径向与最终pending75径向全部并入新几何网格；来源actual trust3.796875与next4只作来源记录。本程序不再次优化旧17q，不继续旧小p减半，也不将零系数R569种子当成这组输入。

新source为 scripts/r582_actual_circle_seed_and_return_20261126.py，准确绑定原R566及v2两个物理源。新控制只有(mu,nu)，初值精确(0,0)：
a=a_actual exp(mu psi)，z=z_actual+nu psi。
psi在(.06,.80)外恒0，内部为exp(4−1/t−1/(1−t))；最大值1。盒固定|mu|<=.04、|nu|<=.06。它们严格不触请求尾口s=.82及更靠帽处，也不触开柱核心，因此R582的真实flat seed在全部新控制中不变。这两个控制改变设计度量，不能称固定g族。

几何预算采用已证明可共同支付宏观比例的R_b=1.012、Y=1−.6R_b=.3928、tau=.06R_b=.06072。原circle源使用更紧预算已经有限扫过，但新程序仍完整重建新有限网格，不借其旧状态替代新几何验收。全部reach仍未连续认证。

## 实际正权与规范种子

ActualTail直接实现R582：
u=((L−s)/ell)^−2，
r=a(s)，P=z_s r^8/(a_s²s_u)，epsilon=12(a_s s_u)²/r²。
代码保留真实r、a_s、z_s及完整三阶u jets。它用
log(P/P0)=log(1+Z_s/w0)+6alpha−2log(1−r0 alpha_s)
计算g=P_u/P与其导数，避免把极小修正通过两个相近权相减。u>=1000的单谷/正权合法性由R582支付；实际alpha_n仍重新用实际g求根。

M=168的有限末端准确为rho_(M+1)=0（即y(alpha_(M+1))=0），逐cell向外归一y；同时在同一正式新run计算M+1和8倍容差细化。每一个传递/求根/比较都记入实际cost。精确DtN截断界与数值ODE误差始终分开，M/精度差不是后者的严格证书。

向请求s=.82传递时保留对数幅值和最后完成cell。靠帽证明之外若实际a_s或z_s离开正权图像坐标，明确记录发生位置、已付RHS与最后完整cell，不越过零点除法。此时实际mouth取最后完整合法cell，之后的中段交给undivided方程，不把未传递区域当作零场。数学上未证明的连续符号/浮点传递仍只作数值观察。

mouth的六jets顺序为(A,A_s,A_ss,C,C_s,C_ss)，并按真实C²尺度共同归一。计算A使用 −w_eff r^5 y_u/(3r_u)，在代数上先消去4f−r f_r的相消项；C=r^4y。实际mouth半径取a(s)，不偷换为r0。不同M若实际mouth不同，明确不作同口误差比较。

## 中段的 C² 返回问题

在固定实际mouth与s=.036之间，对(A,C)使用quintic Hermite端口加t³(1−t)³乘次数五B样条。核心端固定A=.5、A_s=A_ss=0、C=C_s=C_ss=0；尾口六jets等于同一个未知幅度lambda乘实际种子jets。所有自由B样条在两端二jets为0。因此C²匹配准确写入表示，非零核心归一排除全零场。

这不表示线性等距已经满足。余下两条**完整**方程逐点保留：
a_s A_s+z_s C_s=0，
a A_s+3a_s A+4z_s C=0。
在整个中段既不除a_s也不除z_s，所以孤立高度导数零点不会被藏在ODE分母里。真实兼容性会表现为残差；不能只因核心C被表示设为0就宣称已shoot返回。

所拟合的是完整非零角第一变分的标准化幅度：
e=2(a_s A_s+z_s C_s)/E，
f=−(aA_s+3a_sA+4z_sC)/(2a sqrt(E))，
E=a_s²+z_s²。
报告 eta=.5(|e|+sqrt(e²+4f²))、全部s导数尺度和独立细格最大值。真实两个分量分别带cos(2theta)、sin(2theta)，不能在同一角同时取绝对幅度；上述eta是角谱范数的保守上界，不是真实连续角峰。源码/日志明确置conservative_angular_spectral_upper_bound=true，true_continuous_angular_maximum_computed=false。其角theta分量的G第一变分准确0。此处只处理非零角分量；以后从圆点推进p时，核心周长均值的一阶变化仍须作为相应的均值设计变化接入，不能把本程序直接当成有限p解。

## 线性消元、新均值控制与硬几何

对每组(mu,nu)，先在固定257 connector节点上解49个线性场未知量（24个A、24个C自由系数及1个种子幅度）。矩阵按列范数缩放，报告实际rank/奇异值，不把截断SVD的近核称成精确核。

新均值控制使用SLSQP、解析参数导数；目标方向使用固定线性场系数时的显式控制导数。只有完整least-squares驻点且解在常rank范围可微时，残差正交才严格消去系数导数而得到variable projection梯度。rcond=1e-13可能截断非零奇异值，rank也可能变化，因此本实现不宣称截断目标的严格梯度证书；每次线性解另报实际rank、完整列rank标记、原/列缩放normal-equation residual及这个条件范围。原物理Dual只承担2个控制方向，旧空间解析公式保持。每个backend trial都保原完整硬几何行：球、条带、meridian及orbit两主曲率的正负界、高度、E/normalized det和mirror必要行。圆背景的主曲率由(a,z)解析二jets直接计算，不靠一个角采样代表非圆曲面。

几何初格含全部源actual+pending径向、513均匀点、固定tail相位点及全部接口；每候选另扫该格全部中点。只有新完整细格raw几何V<=1e−8且独立细格线性eta降低，才记录有限接受。发现新几何极值的位置进入下一轮实际约束，最多4轮；原有点不丢。若已有候选在扩展网格上失去几何资格，明确取消旧资格，不把旧细格合格自动延续。最后实际构造网格与下一proposal分别打印。

新(mu,nu)几何合格候选出来后，冻结这两个数，把线性场基从24加到48、96；在原fit格重解，始终用独立加密格评估。它是同一圆背景的**线性返回表示细化**，不是有限非线性等距族的固定g精化。lambda或C²场范数很大时会准确报告，不能按归一小数隐藏后续有限振幅的曲率代价。

## 完整运行身份与未付门

新请求 computations/request-r582-actual-circle-seed-return-20261126.json，
新workflow .github/workflows/visible-r582-actual-circle-seed-return-20261126.yml。
单lane/max1，1800秒合作科学段、50分钟job，固定Python3.12.14/numpy2.3.5/scipy1.17.0及两个固定Actions SHA，沿用真实双仓pull和README/QUEUE核。只stdout，不artifact/cache/Git写入。本地只AST、源哈希、依赖闭包、旧日志小参数及源码符号核验，未导入或执行任何科学函数。

ClockCheckpoint保存最后完整seed cell及其真实归一状态/对数幅值、已完成seed与比较、最后评估的新控制、实际费用；若已有有限接受，另完整保存overall_best的控制/线性系数和其资格所用细格。实际构造几何格、细格、线性fit/fine格、pending与下一proposal分开，提前中断时都已初始化，可恢复且不会只剩最后trial。普通OptimizeResult、完整细扫保留候选、最后trial和源状态均分开；backend success不等同共振。

R582纸证已给真实近帽flat核；本次新输入把它变成可实际计算的完整端口与core-return残差问题。完整连续线性返回、真实有限非圆分支、有限幅度非线性度量修正、全部闭体/跨片reach及README全门均不能由这里的finite fit代付。后继要将实际合格的新种子/均值背景接入有限非圆预测与完整非线性改正，不能停在这张线性残差表。
