# R451 — 完整 M 场的闭面几何、公共材料图与显式来源接合

作者：OpenAI ChatGPT /root/exact_refinement（AI），2026-11-16。

## 451.1 结论和准确范围

本结论把已经发表的 R442 完整有限 M 求解/保存/径向重放/共享场，接到新的显式 M 版准确 cut、固定帽、完整相对度量、全 pair reach 和独立 whole-image held 消费者。M 的扩大不以改标签完成：当前场必须有自己的完整 $4M+2$ 维冻结求解，自己的 $3M+2$ 个物理行、M 个 core 系数、全部 native 两均值、全当前 J/FD/final audit、完整有限头/全部 far 行，以及实际数组的来源回执。R442 的原接受责任没有替换。

原六 jet 解释器、四个严格 Loewner 不等式、AA/CC/AC 全 pair 定理、块覆盖和 held 纯数学核本来以实际有限系数/片段表为输入。它们不依赖“112”这个数值。本次须真实推广的是 prefix 物理数组宽度和 core 数、实际 checkpoint/loader 的完整来源元组，以及各层绑定和读回字段。新的 source/schema 与旧 R400/R441/R448 分开，旧文件原样保留。

另给 R447 公共材料 API 一个独立 M 来源分支。首次材料图仍是实际 R437 保存的完整 112 系数定义；当前材料图允许完整的实际 M 系数。二者不要求相同系数数目，不作零填充后冒相等。该 API 提供准确定义及可选闭格六 jet 外包；默认五阶段编排没有实际调用它，不能以“已注册”替代“已计算”。

这是条件包含与源码接线结论，没有选定新的 M、父场、数值参数、请求或运行。没有本地科学执行、导入、AST、编译、fixture 或独立数值审计。没有新的实际 native、metric、reach、held 或全任务成功。

主要来源是：

- 已发表 R442（commit 22a454e3a4705fef552a1938beef655a8bd1ac53）的动态 M 完整链及 [R442 的有限 M 深端范围](R442-fixed-accurate-C-finite-M-modes-and-deep-tail-range.md)。
- 已发表 R441（f2c5653000abedf08622e5e703dffd314aac662a）的完整分辨率消费者；本次数学基线不改其 N/steps 责任。
- 已发表 R448（4af72dc1cc28c5eb6485ac8f829b544630db3b31）的五阶段、静止、同一绝对钟和独立 held 编排。
- [R416](R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md)、R417、R418/R426、R422/R435、R425，以及 [R447](R447-accurate-common-material-phase-and-strong-C2-continuity.md) 的原数学责任。

## 451.2 必须是真正的新有限场

记当前 mode 数为正整数 M。当前冻结物理系统的尺寸为

$$
n_{\rm phys}=3M+2,\qquad n_{\rm core}=M,\qquad
n_{\rm frozen}=4M+2.
$$

左端 $3M+2$ 行、右端 M 行；没有三个仍活动的设计参数，也没有三个额外固定 core 目标。native 状态为 $2M+2$，其中两均值不能删除；每段状态变分的方向数为 $2M$。完整 far 数据是 M 条频率 $2,4,\ldots,2M$ 的 $M\times2M$ 边界行，endpoint 响应为 $(3M+2)\times M$。

R442 的 initial guess 可以把旧高模缺项放为零；这仅是原节点初猜，不能据此删掉新未知量、方程、far 行、角投影或残差。R451 只消费原 R442 owner 返回的实际接受 checkpoint。它核当前 writer/driver/source closure、同一真实父回执、全部十个参数字、当前分辨率、实际采样 result 和原 C 输入，再由实际 SavedPrefix 加载所有数组。

R442 使用固定深端 F=159 的明确有限 M 适用条件。其 $v_*\le1/2$ 和 $\varepsilon_M\le1/64$ 仍由原新深端源负责；本结论不把它推广成任意大 M 的无条件定理。若该责任或任一当前求解责任未付，不存在可供本编排消费的成功场。来源 eligibility 与新增 native 接受阈值是不同事项；这里没有改变原阈值。

## 451.3 准确目标不因有限表示元数据改变

R442 的准确标量目标保留同一完整 continuous C、原三输入、lambda、cut、全深根族、core 几何、全部支撑、准确长度 DAG 和十个准确 dyadic 参数。完整 scalar export 的 field_modes/tail_modes 以及由此变化的 specification 身份必须真实更新。

R451 不要求新旧 specification SHA 相同。准确目标比较执行下面的有限、明确操作：

1. 全十个 binary64 字，包括符号零的实际词，保持原样。
2. 原 R400/R441 target schema 与新的 R442 target schema 明确区分；R442 的 field_modes 必须等于当前 checkpoint M。
3. 只去掉这项已声明的 M 元数据、各自已核的 schema 和完整 numerical specification 的 SHA。
4. **其余整个 target 对象逐字段相同。** 不去掉准确 C、根族、factory、DAG、控制、支撑、长度或来源字段。
5. 原 R442 driver/writer 已另行比较完整 scalar export，例外仅 field_modes/tail_modes；本后继不靠一个简写 target hash 猜测这个事实。

首次 shared definition 可以来自原 R409、R441 或实际 R442 的明确 source/schema 对。当前五阶段入口只接受 R442 owner。借用 R448 编排文本不等于新增了 R448 父到 R442 的路径；R442 owner 仍只注册其原 R400/R431/R441/自身 M 父分支。本次也不将新 R449/205 冒作 joint203。

相同的准确标量目标本身不表示相同的完整闭面度量。完整闭面还须冻结首次 construction 的 W、cap height、全部 marker 字和顺序、材料图与胶合解释。当前编排从真实首次 shared plan 比较全部 W/H/marker 字并保持原 cuff，另记录首图/当前图各自完整 target 身份。材料图可能因为当前 core 改变而改变；其准确共轭在 §451.8 单独处理，不冒逐词相同。

## 451.4 完整 prefix 和 shared 场的包含

PrefixExactField 使用实际 saved.M，要求所有三个 nodal jet 数组都有形状 $(n_{\rm nodes},3M+2)$，core 长度恰为 M。每个物理行的准确五次 Hermite 多项式由原有限字作准确有理数形成，六个系数全保。它不以 rounded PhysicalQuintic 的算术输出替代该准确表达式。

材料密度与提升为

$$
\rho_M(\phi)=1+\sum_{m=1}^{M}(1-4m^2)c_m\cos(2m\phi),
\qquad
\Phi_M(\phi)=\phi+\sum_{m=1}^{M}
 \frac{(1-4m^2)c_m}{2m}\sin(2m\phi).
$$

系数是原 core 字的准确 dyadic 解释；不得先形成 rounded density 再将其当准确系数。原完整 core 的正下界责任仍由 SavedPrefix 处理。

675 解释器从 saved.M 读取维数，prefix 各块列宽和求和随实际 M；它读取全部 shared 节点、全部 coefficient records、实际完整 FFT/Hermite 解释与两均值。M 是物理/材料模式计数，不是允许把 full shared FFT 截到 M 项的理由。当前 angular、material_angles、physical_angles、native quadrature 和 steps 全由实际 R442 回执读取，不能静默恢复成 2048/12。

R451 准确 cut 模块继续只替换原 R416 已声明的 cut target 三个径向 jet。它保留全角复合、真实材料相位、整组前缀/尾/patch/帽缝解释。由此定义的是一个明确的准确有限几何场；原数值 native trajectory 是否为准确连续 C ODE 的真解，仍不是这个几何解释器已经证明的命题。

## 451.5 相对度量的四个原不等式不依赖 M

设当前准确几何表达式为 F，目标为 g，误差为

$$
D=(DF)^\top DF-g.
$$

R251 的四个严格 Loewner 测试只使用每个闭格上完整一阶导数、目标系数和原 eta。若使用同一闭区间包含运算，将有限 Fourier/Hermite 项数从 112 改为 M，不改变这四个测试的充分性。需要重新付的是新场的完整闭格包围，不是定理本身。

前缀采用公共径向变量 $u=s_{\rm num}/L_{\rm num}$。在原计算坐标 $(s_{\rm num},q)$，目标为

$$
g_{ss}=(L_{\rm true}/L_{\rm num})^2,\qquad
g_{qq}=a(L_{\rm true}s_{\rm num}/L_{\rm num};p)^2\,\Theta_M'(q)^2,
\quad\Theta_M(q)=\Phi_M(2\pi q).
$$

准确 a 的每个可能 piece 都须枚举：完整十项、准确 anchor/width/local interval 和所有支撑边界均保留。不能用数值 midpoint 只选一个准确片。

尾的目标保持同一完整 C 的 E(r) 与 $r^2\Theta_M'(q)^2$；固定图帽的目标按原 Cartesian 图表达式付。完整 cap_identity、cut/cuff 和两反射片没有从 prefix 单独结论推得。

R426 live-query provider 原样复用。它只有在同 job 原 C result/input/query 与 complete-source-radial-panels/source-piece-index 仍真实存在且绑定相同时，才能按原全部 primitive/深族精化新 query。固定旧盒和新 query 分开记；资源未完成保准确地址，不换根，不由旧 SHA 恢复原件，也不因 metric 未决阻止独立 reach。

## 451.6 全 pair reach 的 M 独立性

R451 reach 仍对当前完整闭面构造全部根片和 pair：

- 活动片与活动片 AA，包括同片、跨 prefix/native/patch、上下反射和所有真实 seam。
- 两固定帽之间及帽内部 CC，包括完整 marker 图，而非只保未扰动圆盘。
- 活动片与帽 AC，保原全相位责任和两端 normal 责任。

R435 只将原 R422 根 pair 合并为可追溯块。成功块使用原非严格距离充分式；不能因块失败免除其 singleton。细分、singleton 空间/相位 frontier、原 R282 cuff 局部共同图、curvature frontier 和完整未访问后缀仍保。所有原 K、tau 和 $K\tau$ 条件原样，未按 M 重选。

R241、R280/R281 与 R282 的命题以实际场的一/二 jet、曲率、弦/法向、局部图和距离为输入，不使用“只有112项”这个假设。若每个输入包围由完整新 M 表达式给出，则同一充分式仍成立；若新场导致包围过宽、曲率/距离不满足或资源未付，只得到该实际 scope 未付。不能把 finite-M 原求解接受当 embedding/reach 结论，也不能从旧 M 的 pair ledger 继承付款。

完整几何路径上界使用当前实际 q 图、完整径向片和原共同材料运输。增加 M 后其导数上界须重新形成；本源码仍调用原完整算法，既不假设 q 平移就是物理材料角平移，也不借未付全 metric。

## 451.7 Whole-image held 仍是独立消费者

新 held 消费者读取与 metric/reach 相同的准确 cut bundle 和固定帽对象。原 PrefixProofNodeAngles 由 field.M 形成，原 prefix 非平面性、完整尾 witness、共同 B 消去、反射、所有 marker 标签和 O(3) 刚性责任均使用完整当前系数。

R425 的 whole-image 位置包含与非平面 determinant 条件不依赖指定 M；其证明要求的是完整有限表达式和完整像，而非材料坐标某一点的位移。M 改变时不能把旧 witness 或旧位置包围移植。新源只保原数学循环和输出责任，换入明确 M loader/source 及全维 metadata。

独立 held wrapper 只要求同一个实际五阶段 source/input 元组，和 radial、atlas、shared 三项真完成且 owner 静止。它不要求 metric 或 reach 先通过。原位置/非平面/marker/rigidity/Delta-E 的各字段仍各自返回；任何未付项不因 wrapper 返回或来源核对而变成 true。

## 451.8 不同 M 的公共材料图

设首次实际 R437 材料图有 $M_0=112$ 项，当前图有实际有限 M 项。各自保原全圆正下界

$$
\rho_0\ge\beta_0>0,\qquad\rho_M\ge\beta_M>0.
$$

定义全实提升 $\Theta_j(q)=\Phi_j(2\pi q)$。由于 $\Theta_j'>0$ 且 $\Theta_j(q+1)=\Theta_j(q)+2\pi$，每个提升有唯一全实逆 $I_j$。不同项数不影响这个论证；两图不需要同一 core 或逐词相同。

在共同首次材料坐标中，原运动应写为

$$
\widetilde F_{M,t}(x,q)
 =R_{\alpha(t)}
 K_M\!\left(x,I_M(\Theta_0(q)-\alpha(t))\right),
 \qquad \alpha(t)=\pi t/2.
$$

这里 $K_M$ 是当前场的原相位零准确表达式；prefix 的 x 是公共 u，其他活动段用原 r。固定帽保持原 Cartesian 表达式，不要求 marker 帽全闭旋转对称，也不把角逆延拓至帽中心。

设 $z=I_M(\Theta_0(q)-\alpha)$。空间链式微分为

$$
z_q=\frac{\Theta_0'}{\Theta_M'(z)},\qquad
z_{qq}=\frac{\Theta_0''-\Theta_M''(z)z_q^2}{\Theta_M'(z)}.
$$

于是

$$
\partial_q(K_M(x,z))=K_{M,q}z_q,\qquad
\partial_{qq}(K_M(x,z))=K_{M,qq}z_q^2+K_{M,q}z_{qq},
$$

混合导数为 $K_{M,xq}z_q$。prefix 在原 numerical coordinate 中另乘准确常数 $L_{\rm num}$，二阶径向乘其平方；这与 helper 实际六个 jet 顺序 value/u/q/uu/uq/qq 一致。原旋转对每个向量 jet 同时作用，反射由原场评价处理。

原 R447 对每个固定实际场的强 $C^2$ 时间连续性证明仍成立。它使用空间二阶联合连续和准确逆，不要求先证明“时间二次可微到空间 $C^2$”。若另要后者，原12类更高混合 jet 责任仍另列，不能由六 jet 冒付。这里也不证明随 M 增大的一致 $C^2$ 收敛。

## 451.9 全实逆的有限计算保持包含

令

$$
S_M=\sum_{m=1}^{M}
 \left|\frac{(1-4m^2)c_m}{2m}\right|.
$$

对任意目标角闭盒 Y，由 $|\Theta_M(q)-2\pi q|\le S_M$ 得初始完整逆像盒

$$
I_M(Y)\subseteq\frac{Y+[-S_M,S_M]}{2\pi}.
$$

原 helper 以此为起点，用原全局正导数包围和有限 inclusion refinement 求交。每一次完整更新仍包含唯一准确逆像；不按 modulo 折回、不舍弃 q=0/1 seam、不返回中点为“准确逆”，也不以所达盒宽作为 native 或几何接受门。

局部六 jet 评价调用原完整 field.evaluate，保任意实 q 的提升和全部有限 Fourier 项。闭盒过宽或正分母的当前 Arb 表示未隔零时，原包含责任仍可未决；M 注册不预付数值成功或运行代价。精度在 finally 恢复；共享 host budget_check 不重启时钟。

新的 API 明确只增加当前 R451 M tuple。首次输入仍须真实 R437 112 capture、原 plan/assembly 和完整 source 身份；没有制造首个 M capture、没有通用跨 run 语义白名单。原 R416/R441 当前分支仍要求原完整 target identity 相等，不能顺带放宽它们。

## 451.10 同一个完整闭目标的条件

相同准确 C/DAG/十词不能单独证明全闭目标 g 相同。此处条件分四层：

1. 准确 physical-angle/radial 标量目标相同，按 §451.3 的完整字段和原 export 比较。
2. 首次真实 W/H/全 marker/原 cuff 字和材料/胶合解释冻结，实际记录不能只剩一个旧 hash。
3. 使用 §451.8 的准确静态材料拉回 $\psi_M=I_M\circ\Theta_0$ 及原帽 Cartesian 恒等；不能以当前新 Phi 字仍相同代替。
4. 原 R416/R417 全 cut、cuff、反射和准确 target atlas 的胶合前提确实成立。

在这些前提下，原目标张量按准确 pullback 相同。相对 Loewner 界经同一个可逆坐标变换的合同变换保持 eta；reach 和 whole-image held 因静态满域重新参数化不改变当前每个 t 的像。**这只传递同一个当前场在两个坐标中的已付结论，不传递旧父场的几何证书到新 M 场。**

默认五阶段 source 会报告 M 公共材料 API 已注册但未执行。要获得其实际 cell 外包，未来同 job host 必须将已加载的新 cut 对象、真实首次材料记录和当前原绝对钟传给 bind_loaded_common_material。该调用没有成为原求解、五阶段或 held 的新前置门。

## 451.11 原绝对钟、完整未付和源边界

新 Procedure 只接受实际 R442 owner source/schema/input，保原193或joint203 origin 和同一份 deadline 的 bytes/SHA。18900 秒从原 namespace 建立计，2700 秒原读回预留；不是新几何阶段重新计时。五个角色各自的 allowance 按实际剩余量裁剪。全部 C 四件及两原 source ledger 在消费者结束前仍真实保留。

radial 子进程显式设置 tail mode capacity 为当前 checkpoint M，并登记容量记录；不继承原112环境。其实际 N、steps、全部两均值和 576/577 段节点范围仍由 R442 径向 producer 处理。没有删除 modes 或以默认旧环境生成不一致维数。

所有 child 的 PID/start-time/实际组、原 interruption、未启动后缀和独立 scope 保留。五阶段 reader 只有一份必要结论，最多90000字节；超限返回70并明确传输未完，不拆包、不截断原数学 verdict。独立 held 有自己的原必要结论边界。原大账仅同 job 临时存储，包内程序不删除原件；真正 cleanup 仍须未来外层读回和静止责任。

R451 未新增 workflow、请求、场或接受参数。R442 尚未支持的 R448 父、未来205来源、首个 M 材料 capture 等也没有被虚构为已注册。实际运行前所需的只是本接口已经列明的真实来源与参数，不增加 fixture、审计或待批准科学门。

## 451.12 付清与未付的分界

本次付清：完整 M physical/material 尺寸的实际消费者接线；完整新 source closure；当前 M radial/atlas/shared/live metric/block reach 与独立 held 的可执行入口；与真实首次112材料图的准确 M 共轭定义和可选六 jet API；原单摘要/静止/绝对钟合同。

仍未付：任何新 M 的数值求解、全域 metric/reach/held 结果、任意未来实际 M 的资源完成保证、随 M 的一致收敛、准确 native ODE 真解证书、完整闭面存在性及原总任务接受。源身份和条件证明不替代这些实际工作。
