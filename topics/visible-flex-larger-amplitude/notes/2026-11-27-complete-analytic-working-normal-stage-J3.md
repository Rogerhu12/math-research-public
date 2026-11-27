# 完整 normal-plane 局部 J3 的解析工作导数与来源接线

## 1. 对象与本次改变

本文件只改变每个固定 normal stage 内三维 Newton 矩阵的生产方式。R703 的共同有限分段选择、R707 的全部上游隐式链、R714 的同图 C1 复用和 R715 的完整参考校准六 jet 都保留。全部自由 core、三路径向五次旋转系数、最后自由高度、原谱范数、正权 Gram 行、Phase I、几何和永久材料地址责任不由本改变替换。

直接父源是 d5da 完整 normal，固定提交为 291adcd2b2f4de1dac4c7118dbce69b471dc5813。其 _stage_jacobian 对同一完整三维残差作三次 torch.autograd.grad。已刊相邻 frame helper 955d 只生产选根后的 J6/J9，不替换 Newton J3。本次另核已刊 M320 v2 的 8349：_stage_jacobian、_stage_constraints、_solve_stage、_run_chain、_get_roots、_implicit_jet_value 与 d5da 逐字相同；失联历史草稿 9764 不冒作当前已刊来源。

本次下层可执行链严格绑定 base 6a803 和 R711 0d09 参考。M320 的 base 41c865 尚不在这份 helper 的来源集合，数学公式适用不等于允许换实际 source 标签。上层独立接新 7c 家族时仍须绑定该实际完整 reference、固定 chart 与全部 E 地址，不能由旧 source hash 推导 same-g。

## 2. 实际方程与局部偏导

固定当前外参数点 $x$、材料角 $\phi$、stage $i$ 及实际已选前段控制 $u_-$，记

$$
A_-=f_u(x,\phi,u_-)\in\mathbb R^{3\times6},\qquad
u=u_-+A_-^T\eta,\quad\eta\in\mathbb R^3.
\tag{1}
$$

frame 的第零阶分量是 $A_-$。原 _W 返回完整 world 六控制矩阵

$$
\mathcal B(s,\phi)=
[S\sum_{\ell=1}^2\beta_\ell(s)R_z(\theta_0)Q_{\ell0}R_z(\theta_0)^T,\quad
\gamma(s)I_3].
\tag{2}
$$

两 bubble、额外 gamma、十八个 literal Q 字、固定材料 chart、实际 $S$ 载体及所有积分点保持。当前未加这六控制的 meridian 记为 $V(s,\phi;x)$；它包含完整当前 outer omega 和固定 seed。令 $w=\mathcal B u$、$T=R(w)V$。R715 的中心化完整 stage residual 为

$$
G_i(\eta)=
\frac{(\Gamma-\Gamma_0)-(P-P_0)+
\mathcal Q_{\rm total}[T-T_{\rm ref}]}{S}
-(1-\tau_i)f(0).
\tag{3}
$$

$\mathcal Q_{\rm total}$ 是原 _total 的全部实际归约。局部三维偏导中 $x,\phi,u_-,A_-,S,\Gamma,P,T_{\rm ref},f(0)$ 固定，因此

$$
e_j=\partial_{\eta_j}w=\mathcal B A_-^T e_j^{(3)},
\qquad
(J_i)_{\cdot j}=
\mathcal Q_{\rm total}[D_w(R(w)V)e_j]/S .
\tag{4}
$$

式 (4) 没有漏端点项：式 (3) 的端点及冻结参考对当前局部 $\eta$ 不变。它绝不表示这些量对外参数 $x$ 不变；原 active _implicit_jet_value 仍保留所有 $u_-(x),A_-(x),V(x),\Gamma(x),P(x)$、原零目标及全部更早 stage 的导数边。

## 3. 完整 Rodrigues 微分

记 $q=w\cdot w$、$W=[w]_\times$，准确指数为

$$
R(w)=I+a(q)W+b(q)W^2,\qquad
a(q)=\frac{\sin\sqrt q}{\sqrt q},\quad
b(q)=\frac{1-\cos\sqrt q}{q},
\tag{5}
$$

原点取解析延拓。令 $c=w\times V$、$d=w\times c$。由
$Dq[e]=2w\cdot e$、
$Dc[e]=e\times V$、
$Dd[e]=e\times c+w\times(e\times V)$，
逐项得到

$$
\begin{aligned}
D_w(R(w)V)e={}&a(q)(e\times V)\\
&+b(q)\{e\times(w\times V)+w\times(e\times V)\}\\
&+2(w\cdot e)\{a_q(q)(w\times V)
+b_q(q)(w\times(w\times V))\}.
\end{aligned}
\tag{6}
$$

三列都使用完整六控制投影；结果是完整非对称 $3\times3$ 矩阵。没有对角化、对称化、rank 裁剪、ridge、jitter 或删列。

对准确指数，式 (6) 同时等于

$$
D_w(R(w)V)e=-R(w)[V]_\times J_r(w)e,
\tag{7}
$$

其中 $r=|w|$，右平凡化 Jacobian 为

$$
J_r(w)=I-\frac{1-\cos r}{r^2}[w]_\times
+\frac{r-\sin r}{r^3}[w]_\times^2 .
\tag{8}
$$

因为 $DR(w)e=R(w)[J_r(w)e]_\times$，作用到 $V$ 后正好给式 (7) 的负号。$r=0$ 时 $J_r=I$，式 (6) 直接给 $e\times V$。这个恒等式不证明 $J_r$ 或最终 $J_i$ 可逆；原完整线性求解仍可能失败。实现采用式 (6)，小 $|w|$ 无需除以 $|w|$，也不需要新建完整 $3\times3$ 旋转矩阵。

## 4. 真实工作小角分支

base 的 rotation_coefficients 在 $q<1/4$ 实际用两套 degree-12 Horner 多项式。记原 Python 表达式真正产生的 binary64 系数为 $\widehat a_k,\widehat b_k$，必须微分的是

$$
\widehat a(q)=\sum_{k=0}^{12}\widehat a_kq^k,\qquad
\widehat b(q)=\sum_{k=0}^{12}\widehat b_kq^k.
\tag{9}
$$

系数生成保留原 derivative=0 的完整表达式：

~~~python
factor = math.factorial(power)//math.factorial(power)
coefficient = ((-1.)**power)*factor/math.factorial(2*power+offset)
~~~

原函数另有名为 Az、Bz 的返回值，但这些导数系数另行舍入，不能未经区分就充作式 (9) 完全相同的导数。对原实际值系数，由高次到低次同时递推

$$
d_{\rm new}=q\,d_{\rm old}+v_{\rm old},\qquad
v_{\rm new}=q\,v_{\rm old}+\widehat c_k,\qquad v=d=0\text{ initially}.
\tag{10}
$$

归纳可知第二式给已处理多项式，第一式正是其对 $q$ 的导数。源码先执行 derivative=derivative*q+value，随后才更新 value，未误用更新后的 value。最终值与导数代入式 (6)。

在 $q\ge1/4$，使用原值分支相同的 $\sqrt q,\sin\sqrt q,\cos\sqrt q$，并取

$$
a_q=\frac{r\cos r-\sin r}{2r^3},\qquad
b_q=\frac{r\sin r-2(1-\cos r)}{2r^4}.
\tag{11}
$$

未选的大角分支仍先 clamp 平方范数到 $1/4$，防止 where 的未用分支除零；$q=1/4$ 仍选大角，与原条件 q<.25 相同。

式 (6)、(9)–(11) 是所声明分支的完整代数导数。新浮点乘加顺序与反向 AD 不同，没有声称矩阵逐 bit 等于一次未执行的旧 AD，也没有声称普通浮点程序作为离散映射存在通常实导数。含义与原 AD 相同：固定所选分支和工作常数，微分其基本实运算表达式，再执行声明的浮点导数算法。拼界、多项式截断、系数、trig、归约及 inverse 误差仍未向外支付。

## 5. 原完整积分与张量轴

|量|实际形状|完整含义|
|---|---|---|
|eta|$(A,3)$|当前批所有材料角的局部未知量|
|previous|$(A,3,6)$|前段值及两套角 jet|
|frame|$(A,3,3,6)$|前段 endpoint frame 的三套角 jet|
|W|$(P,A,3,6)$|全部径向节点上的 world 六控制矩阵|
|V|$(P,A,3)$|当前完整未校正 meridian|
|结果|$(A,3,3)$|world 输出为行、局部 $\eta$ 为列|

$P=(J-1)Q$；原 J923 与原积分阶数不变。每一列使用
einsum('paij,aj->pai',W,frame[:,0,j,:])。
完整 $(P,A,3)$ 微分场分别通过原 _total：全 cell/全 Gauss reshape、原 gauss_w 求和、原 np.diff(mesh) 载体、原 cumsum 最后一项、最后除原 $S$。没有摊成九列后改归约，也未裁深尾、boundary、cell 或材料角。准确物理宽度与这些工作载体的费用仍是原连续消费者的责任。

## 6. 真实 residual、失败和计数

每次解析矩阵请求先调用原完整 _stage_constraints。_solve_stage 没改字：原当前 residual、六控制开域、全部回溯、全部角接受、预算和最终同点复读保留。选根后的 _finish_stage_jets 仍解完整一二角方程并复读各阶 residual。矩阵有限不冒作根成功。

解析计算遇到 ArithmeticError、MemoryError 或 RuntimeError 时，保实际失败原因，再对同一完整 eta/data/previous/frame/zero/tau 执行原三个 reverse products 的 AD。source/shape/binding 错误不落入可选数值 fallback。AD 也失败则沿原异常拒绝；失败值不填零。

计数分列逻辑请求、解析尝试/返回、AD fallback、真实 reverse products、完整 residual 读取和实际矩阵行。解析已形成非有限矩阵再执行 AD 时，两次实际矩阵行都付；不会报成一次解析成功。只保最后请求自身的点摘要、eta/previous/frame/zero 全字摘要、实际 tau、矩阵摘要和来源。未把最后记录迁作此前所有 cache 的算法 provenance。

若内层 producer 返回之后发生摘要或发布失败，外层请求仍是失败；纯验证不强迫内层返回数等于已发布返回数。所有缺失实际读数均不补零。

## 7. 全局隐式链与六 jet

局部 J3 属于 detached 数值线性代数，不是展开 Newton 迭代求导。原 _implicit_jet_value 每段仍用完整 residual 建 active graph，保留前段控制、前段 frame、原零目标、完整外参数与更早 stage 的边；原 6/9 维角 jet 下三角求解仍保。

相邻 frame J6/J9 的完整组装、真实 frame 输入 provenance、升级时低阶字保持、必要时完整 angular AD fallback 也保留。新局部矩阵可能因舍入差走到不同工作迭代或数值分支，所以新完整 source/model 身份独立，不继承旧 root cache、branch certificate 或旧接受场结论。

R715 的 fields_torch 仍输出完整校准物理六 jet，包含当前 raw closure lift 的 $h,h',h''$；工作 radial Gram 真读不删。没有只改变中心化 residual 却省略物理 lift。

## 8. 严格独立的三层 cache 来源

C1、detached matrix、adjacent frame 三个原 helper 均核 _stage_jacobian 的 AST；不能覆盖实例方法或仅改 normal import 绕过原检查。本次完整复制如下：

- analytic helper 核新 wrapper 和其余八个完整原 method AST、实际 base、完整 model 与共同 partition。
- C1 副本只改完整新来源、wrapper AST 和 constructor binding；全部 frame/template 数值方法保留。
- detached 副本只改完整来源与实际 scalar policy；所有 key、原值保护、回退和计数方法保留。
- adjacent 副本只改来源和归属文字；相邻矩阵公式与 root protection 保留，明确保留所选择的新 Newton/J3。
- calibration 副本只改 endpoint schema，全部数值方法原体。
- normal 只改 __init__、局部 J3 wrapper、metadata，其余 48 个完整 class method AST 原体。

原 source 文件不改字，也不把旧 whole hash 指向新内容。

## 9. 完整源、再生与已完成静态检查

|完整文件|Bytes|SHA256|远端 blob|
|---|---:|---|---|
|analytic_normal_stage_jacobian.py|24240|64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d|1c4a03b548e7482c14a750919094d69c55591fd1|
|analytic_j3_normal_frame_c1_reuse.py|35625|8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8|d50da850d4c5ff895d990402783f79414604b22e|
|analytic_j3_detached_normal_stage_matrix_reuse.py|47673|5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1|f2aa4f5cae42f96e5710bcafbe87846cbee2bcee|
|analytic_j3_adjacent_normal_frame_matrices.py|36734|8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787|a8e1832cd6c68fe793305e3df6f4bfaeac9613c4|
|reference_centred_analytic_j3_smooth_triangle_calibration.py|11911|4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d|2ebf5e12389a00cf1ee4eb7eb92f8c6f6629917f|
|so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py|96906|04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e|b608ef666d2abdbd93c4fc58776c9195809889fc|

完整标准库再生器：

derive_complete_analytic_normal_stage_sources.py，46780 B；SHA256 288c6bb37550a6c3a2cdbbb0c3560a4f821ec4cd6d55141e0d37cb8562580312；远端完整 blob b1c5b6a04c639feefc036f39b65ec3b361466328。

~~~sh
python derive_complete_analytic_normal_stage_sources.py \
  --source-directory /absolute/original/scripts/resume_20261126 \
  --out /absolute/independent/generated
~~~

输入为固定 d5da/ba3d/375059/955d/ccb334 与 6a803 完整源。再生器核全部原 SHA/bytes、每项准确替换次数，输出全六体；使用 ast.parse、compile、完整 method AST 对照，绝不 import 科学模块。

恢复终端后已实际 source-only replay exit0：全六输出 SHA/bytes 一致，语法、compile、无重复 literal 字典键、无尾空白、全部九个 guarded method AST 通过。wrapper 实际 Python AST 摘要为 6db5897c586c0ec00d04ab0a19bebe2743c742bd5d37c4eee1064db8c0fa2010。没有科学数组、数值算例、F/J/root、积分或预审 fixture。远端 Git blob 保护不等于已发布 refs 或已运行科学。

上层 driver/geometry/transfer/launcher/reader 独立接实际已刊 7c 家族；尚未发生的 report 不成为准入前提。本次也不改已经排队的任何入口。

## 10. 可说的成本与未付责任

每个成功解析 J3 用三个完整方向的闭式微分和原积分，避免该矩阵中的三次 reverse products；仍执行一次完整 stage residual，保留 frame、全部 Newton、angular jet、来源校验和全局 J/J*。实现还重算必要的 $w,a,b,a_q,b_q$，不能由“减少 AD”直接宣布总体更快，也不能由单矩阵推整轮峰值内存。实际作用须由完整 Actions 的计数与时间归因。

准确方程、工作 root、全角 branch、准确参考、积分/舍入、全六 jet、metric、几何、永久地点、全物理 phase 和精化证书，各自保留原责任。本 source 既不降低 README 完成标准，也不新增与求解无关的前置门。
