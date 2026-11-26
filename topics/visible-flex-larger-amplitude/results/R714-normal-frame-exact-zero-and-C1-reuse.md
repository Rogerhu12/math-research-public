# R714 — 精确零支与同值 normal-frame 的完整一阶重接

状态：下述准确恒等式与 C1 重接定理已证明；当前实际 seed 的完整工作零残差、重复次数、提速与连续误差均未据此获得。没有执行科学计算。本文不修改已刊 5297、66e81 或其求解参数，不把辅助分段参数当作 README 的物理弯曲参数。

## 1. 此次核读的实际完整来源

| 文件 | SHA256 |
|---|---|
| so3_supported_unit_normal_lift_operator.py | 5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67 |
| supported_unit_meridian_reference.py | 30ea80ec0673f3bdff3e59b97dfb5f7166a296aeb4b989fbca18b2feb5e9544c |
| so3_supported_smooth_triangle_normal_lift_operator.py | 66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68 |
| supported_smooth_triangle_meridian_reference.py | 0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b |
| fullclosed_supported_smooth_triangle_normal_lift_so3_qp.py | fd95d91abe9525cbfa34d55bd576be7dfba1fe25fcafb73bdaaea40e003ad65f |

前两个 seed 表示与 R711 三角型表示的准确端点均值、冻结 core/H、全部外层 omega、共同 normal 分段相同；中央标量相位的实际定义不同，源与 model 均须分别绑定。本文的缓存依据是实际同一完整 source/model 和当前计算图，不是把这两种表示混成一个来源。

## 2. 准确初点确有完整零支

令 x 表示全部外层自由 core、共享 quintic/Fourier 旋转系数与 H。固定参考单位 meridian 记作 T_ref(s,phi)，冻结时使用原 core/H；它在本文内不随 x 改变。内部控制 u 属于 R6，B(s,phi) 是原两个 bubble 加独立 gamma 的完整 3×6 矩阵。定义准确闭合函数

$$
 f(u,x,\phi)=\frac{\Gamma_x(\phi)-P_x(\phi)
       +\int_0^S \exp([B(s,\phi)u]_\times)
          \exp([\omega_x(s,\phi)]_\times)T_{\rm ref}(s,\phi)\,ds}{S}.
 \tag{1}
$$

假设准确参考满足 R708/R709 或 R711 所列的完整均值与正性条件，原初点 x0 保原 core/H 且 omega 恒零。那么

$$
 f(0,x_0,\phi)\equiv0
 \tag{2}
$$

在完整角圈成立。相应一、二角导也为零；这是同一准确函数的导数结论，不是把若干角样本的零值外推。

共同准确分段为 0=tau0<tau1<...<taum=1。每一步按已刊 normal 定义

$$
 A_{i-1}=f_u(u_{i-1},x,\phi),\qquad
 u_i=u_{i-1}+A_{i-1}^{T}\eta_i,
 \qquad
 f(u_i,x,\phi)=(1-\tau_i)f(0,x,\phi).
 \tag{3}
$$

在 (2) 下，u_i=0、eta_i=0 对每一步确为一个根。若 A=f_u(0,x0,phi) 满行秩，则各步 eta 偏导为 AA^T，故正定；由同一可逆局部分支的 IFT，零根在所选局部域中唯一。全角分支仍要求原文中的共同域与对称/周期关联，不能从孤立角根的局部唯一自动推出全圈选枝。

## 3. 准确零值并不删除全部参数敏感度

固定角 phi 和全部外参数方向 h，令

$$
 b=f_x(0,x_0,\phi)h.
$$

因为 seed 冻结，b 包含实际 core、H、omega 的全部支路，但没有假想的随 x 重做 seed。对 (3) 微分，准确零支上的 dA^T eta 一项为零，得到

$$
 \dot u_i=\dot u_{i-1}+A^T\dot\eta_i,\qquad
 A\dot u_i=-\tau_i b.
$$

从 dot u0=0 递推可得

$$
 \dot u_i=-\tau_i A^T(AA^T)^{-1}b,\qquad
 \dot\eta_i=-(\tau_i-\tau_{i-1})(AA^T)^{-1}b.
 \tag{4}
$$

因此“内部根值全为零”不等于“内部根对自由点的导数全为零”。最终导数一般非零。逐 phi 微分 (4) 一、二次时，A_phi、A_phiphi、b_phi、b_phiphi 全部保留；dA^T eta 的消失不能再用来删这些项。

式 (4) 是准确特殊基点的代数简化。当前工作公式没有支付把其实际 f_work(0) 替换为零所需的数值责任，所以本文不把它直接接入当前 solver。

## 4. 为什么现有工作初点不具有 (2) 的逐位恒等式

provider 的 _prepare_plan 使用全部原准确 affine 节点，再按支持端点和端层边界切分；补集与端层在每个新片上用声明的正 Gauss 规则。中央积分另通过完整 profile moment 计算：旧源为五片规则，R711 源为十二片规则。_means 用这些载体构造 K、边层 B 和中央长度，再求均值及两角导。原 mean 默认径向阶数为16，但已刊实际 ready 明确传的是8；“默认16”不是实际此次输入的阶数。

normal 的 _total 则将输入数组直接 reshape 为原 J−1 个胞乘 integration_order，再用原 gauss_w、np.diff(mesh) 和 torch.cumsum。当前 ready 的 integration_order 也是8，但没有 provider 的支持边界细分，也不以独立中央 moment 替换原胞内积分。原 _closure_jets 实际返回

$$
 \widehat f^{(j)}(u)
 =\big(\widehat\Gamma^{(j)}-\widehat P^{(j)}
       +Q_{\rm outer}(\widehat T_{\rm corrected}^{(j)})\big)/\widehat S.
 \tag{5}
$$

_prepare_plan / _means 与 _closure_jets / _total 的以下差异均未由“相同阶数8”消除：

- 径向分割与节点不同；一个精确支持边界可在原胞内部。
- 中央 profile 的 moment 规则与逐原胞外层积分不同。
- provider 的 NumPy 求和、working normalization 与 normal 的 Torch 逐胞累积不同。
- 完整固定 chart、inverse core 与 Gamma/P 的实际计算图也没有承诺跨模块逐位同字。
- 均值核只验声明的实际非零容差，不输出“准确总方程恰等于零”的证书。

_run_chain 先真实读取 zero=_closure_jets(0,data,order)，每步使用此实际 zero 的 (1−tau) 倍。它没有把 zero 强置0。即使 tau·||zero0|| 低于原容差，使 _solve_stage 在 eta0=0 结束，_finish_stage_jets 仍会解一、二角方程；只要 zero 的角导不是逐位零，eta1/eta2 和后续控制 jets 就可能不同。因此不能仅凭 omega=0、core/H 未改、value 根未做 Newton 三个标签宣布三十二步的完整 primal 相同。

## 5. 正确的 C1 重接定理

设 x 属于 Rn，U 属于 Rd，F(x,U) 属于 Rq 是在当前点邻域可微的实际数学映射。这里 d=18 可包含完整 u0/u1/u2；q=36 或54 对应第一或第二角阶的完整 frame。令 U_star 为当前逐位冻结载体，视作与 x 无关的局部常量；各 stage 的真实上游图 U_i(x) 满足 U_i(x0)=U_star。定义

$$
 F_\star(x)=F(x,U_\star),\qquad
 K_\star=D_UF(x_0,U_\star),
$$

以及

$$
 \widetilde F_i(x)=F_\star(x)+K_\star\big(U_i(x)-U_\star\big).
 \tag{6}
$$

则

$$
 \widetilde F_i(x_0)=F(x_0,U_i(x_0)),\qquad
 D_x\widetilde F_i(x_0)
   =D_xF(x_0,U_\star)+D_UF(x_0,U_\star)D_xU_i(x_0).
 \tag{7}
$$

证明：第一式由括号为零；第二式是链式法则，且 K_star 是当前固定矩阵。右端恰是原复合映射的完整一阶导数。证毕。

实现时 F_star 必须保当前完整 data(x) 图。K_star 可以 detach，因为其导数只会乘 U_i−U_star 的零值；这不是删去 K_star 本身。U_i 必须保其全部上游 stage 图。仅缓存旧 active frame 而不加第二项会漏 D_UF·D_xU_i；只将 U_i 值 detach 则有同样错误。

若使用随 x 变化的 K(x) 而不 detach，(7) 仍成立，因为 DK 乘零；但会创建此一阶接口不需要的更高图，不能据此解释成更强二阶正确性。无论 K 是否 detach，(6) 一般不保二阶外参数导数；例如 F(x,U)=U²、U(x)=x、x0=0 时 K_star=0，重接的一阶导正确而二阶导错误。

## 6. 完整 angular-frame map，不能只键入 u0

把 f_u 记为 A，U=(u0,u1,u2)。准确 total angular jets 为

$$
\begin{aligned}
 {\cal A}_0&=A(u_0,x,\phi),\\
 {\cal A}_1&=A_\phi+A_u[u_1],\\
 {\cal A}_2&=A_{\phi\phi}+2A_{u\phi}[u_1]
                    +A_{uu}[u_1,u_1]+A_u[u_2].
\end{aligned}
 \tag{8}
$$

现 _normal_frame_jets 正是从完整 closure total jet 对局部 u0 求偏导得到这些矩阵。定义 F=(A0,A1) 或 F=(A0,A1,A2)，即可用 (6)。同一个 u0 配不同 u1/u2 一般给不同 frame，不能据 value 根同为零而复用整个 active frame。

为核对完整偏导，令 Hj=D_u0 A_j。于是

$$
\begin{aligned}
 D_U{\cal A}_0[\delta U]&=H_0[\delta u_0],\\
 D_U{\cal A}_1[\delta U]&=H_1[\delta u_0]+H_0[\delta u_1],\\
 D_U{\cal A}_2[\delta U]&=H_2[\delta u_0]
                 +2H_1[\delta u_1]+H_0[\delta u_2].
\end{aligned}
 \tag{9}
$$

这是 total-derivative 算子的 Leibniz 公式。H2 包含 f 的混合四阶，不能宣称成本自动降到二阶。最窄实现可以直接对实际全部 frame 元素求其对完整三 jet、18 个局部控制字的 Jacobian，不必在浮点实现中强行使用 (9) 的对称或重复块。此时每角缓存形状为：

| 项 | 第一角阶 | 第二角阶 |
|---|---|---|
| U_star | (3,6) | (3,6) |
| F_star | (2,3,6) | (3,3,6) |
| K_star | (2,3,6,3,6) | (3,3,6,3,6) |

第一角阶的 u2 偏导数学上为零；首实现仍将三 jet 全部作为 literal key，宁可少命中，不用旧第二 jet 的不同载体伪作相同完整状态。

## 7. 为什么此 C1 范围足够当前完整接口

本次读到的原完整 source 明确：

- jvp 用 torch.autograd.functional.jvp，create_graph=False；它给一次外参数方向导。
- vjp 用 autograd.grad(value,x,...)，create_graph=False。
- point_vjp 先保六个真实世界 jet，再对全部自由点作一次 autograd.grad。
- driver 的正残差 Hessian 模型通过完整 J*、残差空间 H 与 J 组合；它没有求物理映射对 x 的二阶 Hessian。

六个空间 jet 及其内部一、二角导已包含在 F 的输入/输出图中；它们不是被“C1”省去的对象。Torch jvp 的 reverse-over-reverse 实现并不改变所请求的导数阶数：第二次反传是对辅助 covector，以得到同一个一阶 Jacobian 乘向量，而不是要求 F 的二阶外参数 Hessian。

原 _implicit_jet_value 为每个 stage 使用其完整缓存的 6×6 或9×9角隐式矩阵，计算零值 residual−residual.detach，再求同一个 stage 的 implicit correction。若仅把 frame_computed 换为 (6)，每一步的值与一次 x 导数保持；由有限链的 C1 复合律，最终所有 control jets、六 jet、J/J* 和 point covectors 都保持对应准确一阶值。所有 m 个 stage、其未知量、tau、上游 control、零目标及隐式矩阵仍存在，不能把它概括成“只求最后一个根”。

若未来入口调用物理二阶外参数 Hessian、可微分 J 或更高外层导数，此实现必须明确拒绝该能力或独立补完整 C2/更高重接，不能沿用上述范围。

## 8. 一次 fields 调用内的完整可实施接线

以下是独立新 source 的实现合同，尚未接入当前运行字节。

1. _get_roots 按原算法完成所有实际根与所需角隐式矩阵，不改其验收、m 或缓存升级。
2. 在本次 _implicit_jet_value 内，取得每一步之前的完整三 control jets：第一步为原零数组，后续为该同角 cache 的上一 stage 控制字。仅用这些字预数重复次数。
3. 缓存作用域严格限本次调用的同 x 张量、同 data 图、同完整 literal phi 顺序、同 order、同 source/model。不得把 active 图放进跨调用的 q._root_cache。
4. 逐 stage 仍构造其真实 previous 上游图。重新取全部 previous 字节并核对预计 key；不相同即走原 _normal_frame_jets，不以近似距离、舍入或容差合并。
5. 第一次实际命中可复用组时，取独立 local=previous.detach().clone().requires_grad_(True)。调用原完整 _normal_frame_jets(local,data,order)，保 F_star 的 x 图；对每一个 frame 输出分量求对整个 local 的偏导，得到完整 K_star，并 detach 该矩阵值。
6. 每次命中返回 F_star+K_star·(previous−U_star)。完整张量 contraction 不删任一输入控制槽。随后仍执行原 frame_hat+(frame_computed−frame_computed.detach())，因此原选定 stage 的 working primal frame 仍由其自身缓存字锚定。
7. 所有原 _stage_constraints、完整隐式求解与 control_hat 值锚保留。局部缓存只能保存此次图，返回后释放 Python 容器；输出图自行保留其真正依赖。
8. 报告 planned/actual repeated groups、命中/未命中、实际原 frame 调用与局部 Jacobian reverse 次数、缓存 bytes、耗时，以及未实施更高外导数的范围。不得预报提速或假记省去的原计算为实际 operator 产品。

没有命中时，新入口必须完全回原完整 frame 路径；它不构成新的科学可行性门。无任何步骤替换当前 f_work0，也不因 seed 正确的准确定义而接受未读实际场。

## 9. 代价与可证明的适用限度

原一次完整 frame 需要3(r+1)次 inner reverse 产品。直接完整 K 的一次模板还需18(r+1)次 frame 输出对 local 的 reverse；总调用数相当于七次 frame 的计数，但每种 reverse 的实际图大小和高阶成本不同，不能把此计数比例冒成墙钟加速。

因此可以按完整 cached primal 预数，先只为至少8次相同三 jet 的组建立模板；其他组原样计算。这是避免明显无命中开销的算法选择，不是新几何/完成门。若实际每一步 U 都不同，收益为零；若只有 u0 相同而两角 jet 不同，首版也不命中。当前源码不足以证明真实 seed19或任何未来三角型输入会出现足够多的相同完整 stage jets。

第二角阶每个组的 K 有54×18=972个 binary64 字，每角7776B；角块8时为62208B，另有实际 active F_star 图、cached frame、U 和结构开销。图峰值/高阶 reverse 真实成本未知，必须由完整实际方向返回，不以此小矩阵字数代替进程内存。

仅 no-grad 下按全部 previous jets 字节复用已算 frame 的值也合法，因为该函数不含 tau；但这不能直接拿到 active 图中。_stage_jacobian 对 eta 的偏导也不含常数右端 (1−tau)zero，若完整 data、previous0、frame0、eta0 同字，可复用其真实 detached 数值矩阵；仍需保原阶段真实残差及其所属状态。本文没有实现更广的近值合并或跨点因子缓存。

## 10. 下一工作的准确边界

式 (2) 提供了准确初点的有用结构；式 (5) 解释了为什么当前已刊数值源不能直接利用“零根”。式 (6) 则在真实完全同值组出现时允许不丢 stage 链的一阶重接。它不能保证出现该组，不能由准确零支证明某次实际 normal 成功，不能说明任何已返失败是秩亏或不可达。

若实际没有足够重复，优先继续 R713 尚未支付的准确总均值方程 residual producer：完整端层/补集、真实固定 chart、同 working v/v_phi/v_phiphi、全部 quadrature/normalization/字运算费用。把准确 seed 的恒等式兑现为同场误差，再讨论独立的 centred working 表示；不能先强制零残差再把这些费用记零。

参考：R708、R709、R710、R711、R713；已刊固定 normal 分段完整证明与 R707 误差账。本文不重复这些存在条件或全角费用结论。
