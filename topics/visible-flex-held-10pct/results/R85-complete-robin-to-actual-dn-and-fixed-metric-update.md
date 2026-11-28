# R85. 原完整 Robin 系统到真实 DN 的端口更新与固定 g 列替换

作者：analytic_construction；2026-11-28 UTC。状态：原方程的有限维代数推导，未执行新的 J、DN 请求、BVP、固定 g 精化或闭面验收。本文接已登记的原 Schur 引理与 R72，不重新声称一般 Schur/Woodbury 恒等式是新结果；新增内容是当前 R53 全系统的准确端口行、物理缩放、25 维联合更新及其执行边界。

## 1. 原来源与这次冻结的量

原 `db6f-prefix-coupled.py::TailMixin.terminal/bc_jac` 使用

$
 H=\sigma q_gY_z(1),\qquad
 T_N=W^{-1}\{q_g f_z-P(H)/\sqrt{E_c}\}.
\tag{1}
$

这里 $P(H)$ 是同一个真实有限尾的全部 M 个非均值 slope，$W=\operatorname{diag}(\mathrm{bcweights})$。原全部 $(3M+2)M$ 个 heightJetJacobian 条目仍由真实请求返回；终端 BC 只读取其中前 M 行 $L=D_HP$，这不授权删掉其余两jet/mean 行或 audit。

本条将 `obj.q` 写成 $q_g$，将实际核心支撑主系数写成 $q_a$，以免混淆。`SupportBVP.__init__` 把 `self.q` 设为 gauge；`WarpedBVP.initial` 在 fixed=True 时只令局部变量
$q_a=\mathrm{seed\_support\_amplitude}\exp(p_0)$，更新 `self.support_amplitude`，从未把它赋给 `self.q`。入口投影仍除以固定 `self.q`。因此 fixed-g 方向是 $p_0=\eta=\log(q_a/q_{\rm seed})$，而 (1) 中的 $q_g$ 保持不变。

本次原 portable 和 fixed 分支均把 W 显式设为固定 physical_bc_tol/bc_tol 或固定 bc_normalization；不随迭代参数变化。原 adaptive chart 在 cut 恒等至二阶，并把 Dmatrix 设为
$D=\operatorname{diag}(\mathrm{linearSlope}[:M])$。
$\sigma,E_c,D$ 来自同一固定物理 cut/尾/频率集合。R72 §1 已说明原 $\delta$ 设计只移动前缀末端的物理位置，完整短桥在自身局部坐标中固定，故这些 cut 量不随 $\delta$ 改变。改变 $q_a$ 或高支撑控制只改解的核心及完整 lift，不改这些物理尾数据。

以下所有相减和列替换必须使用同一 mesh、同一完整状态、相同 gauge、warp_reference、mean 规则、字面径向/角图和同一全部高支撑物理控制。fixed=True 的一般重构若重新生成了另一条径向 chart，就不满足这个合同；不能只凭 fixed=True 或相同节点数使用以下同点列替换。

## 2. 全系统中的准确行、列与残差身份

记原节点数 K，状态维数 $n=3M+1$，全部未知
$Z=(\operatorname{vec}_F Y,p)\in\mathbb R^N$，$N=nK+M$。
残差的顺序是全部原 collocation、n 条完整入口和 M 条终端；这些行一条也不消去。

令 $U:\mathbb R^M\to\mathbb R^N$ 把向量注入最后 M 条终端行；令

$
 C Z=\sigma q_gY_z(1).
$

C 只取最后一个节点的全部 M 个高度分量，对所有参数列恒为零。它不是投影到首模，也没有省去其余状态。

原线性 Robin 残差记为 $F_L(Z)$，其终端为
$W^{-1}(q_g f_z-DH/\sqrt{E_c})$。定义

$
 g(H)=-\frac1{\sqrt{E_c}}W^{-1}\{P(H)-DH\},\qquad
 G(H)=-\frac1{\sqrt{E_c}}W^{-1}\{L(H)-D\}.
\tag{2}
$

因为两问题的完整内部方程和入口完全相同，直接相减得

$
 \boxed{F_N(Z)=F_L(Z)+U g(CZ).}
\tag{3}
$

因此，同点导数满足

$
 \boxed{J_N(Z)=J_L(Z)+U G(CZ)C.}
\tag{4}
$

这是当前原系统 rank 至多 M 的更新。所有 $\delta$ 对完整场、moving chart、core lift 的影响仍在 $J_L$ 的原参数列中。

式 (3)--(4) 是原方程的实数代数身份。对实际组装矩阵，L 应取该完整真实 packet 的 slope Jacobian，且两边使用同一原数值偏导规则；这时相同推导给所声明数值矩阵的边界更新。原 centered-$\delta$ 列、tail 线性化误差及浮点运算并不会由该身份自动变成严格导数证书；实现也不能由代数身份声称两种不同运算顺序逐位相等。

本次 M24/K879 的 $N=64191$。0-based 列中全部末端高度为 64143:64167，全部原参数为 64167:64191；注入 U 的行恰为 64167:64191。这只是说明原排列，不把参数行与参数列混成同一物理对象。

## 3. 一次完整基逆与 M 维真实端点兼容矩阵

假设同点完整 $J_L$ 可逆，设

$
 V=J_L^{-1}U,\qquad A=CV,\qquad S=I_M+AG.
\tag{5}
$

则 $J_N$ 可逆当且仅当 S 可逆，且
$\det J_N/\det J_L=\det S$。

给定任意完整右端 b，先作一次原完整解 $z=J_L^{-1}b$，再解

$
 h=S^{-1}Cz,\qquad
 \boxed{\Delta Z=z-VGh.}
\tag{6}
$

证明：由 $(I+AG)h=Cz$ 得 $C\Delta Z=Cz-AGh=h$；再代回
$J_L\Delta Z+UGC\Delta Z=b-UGh+UGh=b$。
反过来，若 $Sh=0$，则 $\Delta Z=-VGh$ 满足 $C\Delta Z=h$ 与 $J_N\Delta Z=0$；h 非零时 $\Delta Z$ 也非零。故可逆性等价。行列式式由同一块消元或矩阵行列式引理得到。

Newton 右端必须是 $b=-F_N(Z)$。即使原 source 已接受，也不能省掉 $F_L(Z)$ 的全部非零残差。写 $z_L=-J_L^{-1}F_L(Z)$，则

$
 h=(I+AG)^{-1}\{Cz_L-A g(H)\},\qquad
 \Delta Z=z_L-V\{g(H)+Gh\}.
\tag{7}
$

这给首个全 DN 方向的全部 Y、$\delta$ 及所有 support 参数，未冻结其中任何一项。

V 可以一次逐列算出；M24 时有 1,540,584 个 binary64，12,324,672 字节。这个数只计算 V 本身，不包括原矩阵、完整因子、求解工作区或 native 尾。后续在同一冻结基逆上的端口切线变化只改变 G 和 M 维小块；不需重新组装大矩阵。不过每次仍必须回算完整原矩阵残差

$
 J_L\Delta Z+UGC\Delta Z-b
\tag{8}
$

并检查原非线性残差与域，不能用小块残差代替。

## 4. 旧点矩阵只能是完整 frozen chord

若现成矩阵 $J_0$ 来自另一个真实点 $Z_0$，而当前 packet 在 H=CZ，则

$
 B_0=J_0+U G(H)C
\tag{9}
$

仍能用 (5)--(8) 精确求解这个**声明的矩阵**，但它一般不是当前点的完整 Newton 导数。当前 Jacobian 与它的差是内部/入口/线性端口原导数差 $J_L(Z)-J_0$，以及原数值导数误差；这些不会因低秩更新而消失。

具体地，已存 M24 J 的真实输入
`lambda002_m24_jac_input.npz` 为
`c9c4906fb944a82d59f752d74332157dc564b841d269148de20206d937a4edde`；
全 H packet 81f6eb0f…绑定的 accepted raw 为
`4f5033800dab66e46125d8e88fc4d0eb4dbacfc5dd6d1bd8f7808a74f9193616`。
同 run、同 M、同 879 节点不能推出两个 x/y/p 逐位相同。未实际核对前只能使用 (9) 的 frozen-chord 标签，不能把旧 QR 数字搬成当前点导数或逆证书。mesh、gauge 或状态排列不同，更不能直接相乘；应先回到共同原坐标建立明确运输，或重新组装。

## 5. 与 fixed-g 的完整 logq 列合并

现在另加更强的同点合同：固定 g 模型逐字保留原 gauge、实际 chart、所有高支撑物理列、mean 与完整 core lift；只把原加性 $\delta$ 未知替为
$\eta=\log(q_a/q_{\rm seed})$。在匹配的两个切空间中，令 e 为原第一个参数坐标向量，$v_\delta=J_Le$，$v_q=\partial_\eta F_L$ 为完整新列。由于 gauge $q_g$ 固定，且 cut 高度是 (1) 的原表示，

$
 Ce=0,\qquad \partial_\eta H\big|_{Y,p_{j>0}}=0.
\tag{10}
$

这只是直接偏导；解分支上的 H 当然可以通过 Y 改变。由第1节，G 本身没有额外的直接 $\eta$ 或 $\delta$ 物理尾项。因此真 DN 后的固定 g 矩阵为

$
 J_{q,N}=J_L+UGC+(v_q-v_\delta)e^{\mathsf T}.
\tag{11}
$

令 $w=J_L^{-1}v_q$。将 (11) 写成两个块的低秩更新，得到准确的 $(M+1)$ 维矩阵

$
 \boxed{\mathcal S=
 \begin{pmatrix}
 I_M+GA & GCw\\
 e^{\mathsf T}V & e^{\mathsf T}w
 \end{pmatrix}.}
\tag{12}
$

确实 $J_L^{-1}(v_q-v_\delta)=w-e$，而 $Ce=0$；右下角是
$1+e^{\mathsf T}(w-e)=e^{\mathsf T}w$，没有漏掉常数项。给定完整 $J_L$ 可逆，$J_{q,N}$ 可逆当且仅当 $\mathcal S$ 可逆，行列式之比也为 $\det\mathcal S$。在 M24 它是25维，不是只保留一个首模的近似。

若第3节 S 可逆，可先更新真 DN，再换列。设

$
 w_N=w-VG(I+AG)^{-1}Cw.
$

那么真 DN 后的准确 fixed-g 兼容标量是

$
 \boxed{\chi_N=e^{\mathsf T}w_N
 =\chi_L-e^{\mathsf T}VG(I+AG)^{-1}Cw,\qquad
 \chi_L=e^{\mathsf T}w.}
\tag{13}
$

并有

$
 \frac{\det J_{q,N}}{\det J_N}=\chi_N,\qquad
 \frac{\det J_{q,N}}{\det J_L}=\det(I+AG)\chi_N.
\tag{14}
$

这是此前原 Robin $\delta/\log q$ 标量的完整 DN 修正。已登记的
$\chi_L\approx2.4696192160526124\cdot10^{-5}$ 仅是旧真实 Robin 点上的数值观测，不是本条新的 $\chi_N$，也不是区间逆证明。没有实际计算 (13) 的修正前，不能从旧非零数值推出 fixed-g 真 DN 可逆。

同一更新也能给固定 g 的 $\lambda$ 切线。若完整 $v_\lambda=\partial_\lambda F$ 的 cut 直接项确实为零，并且
$z_{\lambda,N}=-J_N^{-1}v_\lambda$，则

$
 z_{\lambda,q,N}
 =z_{\lambda,N}
 -(w_N-e)\frac{e^{\mathsf T}z_{\lambda,N}}{\chi_N}.
\tag{15}
$

代入 (11) 即证。输出第一个参数分量现在是 $\dot\eta$，不是物理 $\dot\delta$；g 仍固定。此式不能在 $\chi_N=0$ 时使用，也不保证该切线能越过原曲率/域门或连续到 $\lambda=1$。

## 6. 原8outer的实际非线性剩余可准确分离

原 `AffineTailForInnerBVP` 在 H0 使用
$P_{\rm aff}(H)=P(H_0)+L(H_0)(H-H_0)$，只供内步。设原内步实际返回 Z1，H1=CZ1，记其完整仿射残差为 $F_{\rm aff}(Z_1)$。直接用 (3) 相减：

$
 \boxed{
 F_N(Z_1)-F_{\rm aff}(Z_1)
 =-\frac1{\sqrt{E_c}}UW^{-1}
 [P(H_1)-P(H_0)-L(H_0)(H_1-H_0)] .}
\tag{16}
$

内部、入口和全部参数残差仍是原内步的真实值，不能因为 solver_success 就把它们设为零。

若精确有限 DN 在整条高度线段上二次可微，则括号为

$
 \int_0^1(1-t)D^2P(H_0+t\Delta H)[\Delta H,\Delta H]\,dt.
\tag{17}
$

这说明原 outer 在适当逆界下为什么可有二次剩余；本条没有给整段 Hessian 界。只有两个端点 Jacobian 不能认证中间上界。实际原调用已经取得 P(H1) 时，(16) 的完整向量可直接评价，无需假造 Hessian 常数或将 affine response 当真实 nonlinear response。

因此一个安全的实际续入顺序是：从真实 packet 的完整 H/J/audit 建 (2)，用 (6)/(7) 或明确旧点的 (9) 给原全部未知初猜；在原域门和全残差回评后，继续既有8outer，每个新完整 H 都仍由原真尾接受，最终导出 physical quintic 后还须用它自己的 physical-H 做 seam audit。原 packet 的 raw-H 不能代替最终 physical-H。任何有限线性方向、S 的可逆性或仿射内步都不单独构成题目完成。

## 7. 若后来某个冻结量改变，不能漏导数

上述简式依赖第1节已核的冻结合同。更一般地令
$B=E^{-1/2}W^{-1}$，$\Delta P=P(H,\xi)-DH$，则

$
 dg=-(dB)\Delta P
 -B\{(P_H-D)dH+P_\xi d\xi-(dD)H\}.
\tag{18}
$

例如将 physical q 与 gauge q 混成同一未知，会在
$dH=\sigma q_g\,dY_z+\sigma Y_z\,dq_g$ 中出现额外项；改变 cut、角图或尾参数也要保留其全部项。这时仍可写全末端行更新 $J_N=J_L+U\,D_Zg$，rank 至多 M，但不能再无条件写 $D_Zg=GC$ 或 $Ce=0$，也不能沿用 (12)--(15) 的简式。

## 8. 源码定位与执行范围

以下为本次实际读到的 Git blob SHA-1（不是 SHA-256），用于锁定文本：

| 来源 | blob | 直接依据 |
|---|---|---|
| `scripts/resume_m3/neighbor_tail_modules/db6f-prefix-coupled.py` | `d6b54bd088a60624848b0691da032d149704f7c9` | TailMixin 22--31；AffineTailForInnerBVP 46--56；原 outer 92--112 |
| 相邻题 `scripts/950f-prefix-warped-bvp.py` | `64c1c8ed812326a2bbc39007698a914839ac444e` | WarpedBVP 97--145；局部 q_a 与固定 self.q 119--135 |
| 相邻题 `scripts/950f-prefix-adaptive-chart-bvp-v2.py` | `7c299ca34faa3b0b3470ac4a8c3a587d8c6b9f4d` | build_classes；cut Dmatrix 92--99 |
| 相邻题 `notes/fixed_metric_mode3_bvp.py` | `44ea94e8fb63da0cfa97de5856d8621422320549` | gauge 40；flow/initial 55--83；linear terminal/bc 118--132 |
| `scripts/resume_m3/portable_prefix_continue.py` | `d6617f665d75acd31567ae4e1ce32d24d4b61309` | frozen W 120--122；全 H/J/audit 与8outer 227--249 |
| `scripts/resume_20261126/fixed_m3_branch_model.py` | `c1d763877464a381114bcde53df4dab2292a90ad` | 固定 physical tail/gauge/warp 79--96；本条另要求字面 chart 不变 |
| `scripts/resume_20261128/analytic/material_lambda_tangent_predictor.py` | `23e64bad6508ca7bd910a98a778ae077e41eecc3` | 完整 q_a 差分及 gauge/warp/chart 不变检查 278--332 |

配套旧结果为 R72、[真实同 J 的 q Schur记录](../notes/2026-11-28-analytic-material-lambda-tangent-and-q-schur.md)、[原 M24矩阵来源](../notes/2026-11-28-design-complete-csr-assembly-qr-bitwise.json)及旧 n4 fixed-physical-field-refinement 笔记。旧 n4 的固定全部核心参数矩形校正与本条的保留全部设计/固定-g未知并替换实际端口不是同一个问题。

终端失联期间本条没有调用新的数值求解、没有读取不可访问的大矩阵、没有释放冷数据；所有 S、$\mathcal S$、$\chi_N$ 和新方向仍未实测。它给出可复用已经付出的完整 J 的具体方法及严格的来源/同点限制，不把资源故障当作数学失败或不存在性结论。
