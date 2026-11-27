# 2026-11-27：完整 working normal frame 的六控制解析角 jets

## 1. 目的、准确对象与执行边界

本说明给出完整 normal frame 的解析实现及其与原 working 表达式的逐项关系。目标是替换每次原 frame 中的 $3(j+1)$ 次反向微分构图，不改变外层全部变量、固定数学目标、normal 的全部段、角集合、径向节点、材料包络、永久行、完整约束或真实线筛。

完整父源是 analytic-J3 normal 算子：

- `so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py` 的实际完整源码 SHA256 为 `04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e`，96906 字节；
- 原 base 的 SHA256 为 `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865`；
- 局部解析 Newton J3 helper 的 SHA256 为 `64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d`；
- C1 helper 为 `8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8`；
- adjacent-frame helper 为 `8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787`。

这里的父对象按完整源码 SHA 标识；不根据近似文件名或某个旧 wrapper 推断实际身份。新独立 helper 为 `analytic_normal_frame_jets.py`。其完整字节及依赖表由交付 manifest 固定。本说明不为尚未执行的后继填写数值、运行时间、加速比、根成功、接受的场或已付认证费用。

run07 的真实终态是取消而非科学结果，最后只有输入阶段 1–3 的返回。这个事实促使处理完整首次 F 的实现成本，但不能代替逐函数实测。新算法仍须由 public Actions 执行；本次只做完整源码、代数、AST/compile 与来源检查，没有本地数值例子、科学导入或 fixture。

## 2. 原 frame 究竟微分什么

设当前角块含 $A$ 个完整材料角，完整径向积分节点数为 $P_{\mathrm{int}}$。每一角有六个 normal 控制变量及其两个角导数，记为

$$
U_0,U_1,U_2\in\mathbb R^6.
$$

原 `_normal_frame_jets(previous,data,order)` 先调用完整 `_closure_jets`，随后对每一个世界分量及每一个所需角 jet，用 `autograd.grad` 对全部局部控制 jet 微分，取返回的零阶控制槽 `[:,0]`。因此真正的对象是

$$
\mathcal A_j
 =\partial_{U_0}\mathcal C_j(U_0,U_1,U_2;\mathcal D)
 \in\mathbb R^{3\times6},
 \qquad 0\le j\le\mathrm{order},
$$

其中求这次局部偏导时 $U_1,U_2$ 和输入 data 独立固定。它们对外层自由点的真实依赖并未取消；最终 frame 函数继续依赖整个 $U$ 和 $\mathcal D$。

原 closure 的完整形式为

$$
\mathcal C_j
 =\frac1S\left[
 (\Gamma_j-\Gamma_j^{\mathrm{ref}})
 -(P_j-P_j^{\mathrm{ref}})
 +\mathcal L\bigl(T_j-T_j^{\mathrm{ref}}\bigr)
 \right].
$$

$\mathcal L$ 是原 `_total`：完整各 cell、原 Gauss 权、原 working 宽度、先 cell 内求和再 `cumsum` 的同一归约。原参考、core 和 cap 不依赖局部 $U_0$，所以对该局部偏导：

$$
\boxed{\quad
 \mathcal A_j[:,\ell]
 =\frac1S\,\mathcal L\!\left(\partial_{U_{0,\ell}}T_j\right),
 \qquad \ell=0,\ldots,5 .
 \quad}
$$

这不删除 core 或 cap 在完整外参数 Jacobian 中的贡献。原 stage residual 仍完整读取它们；此处只是这些加性项的局部控制偏导严格为零。外层所有 core/H 变量与所有原线性、几何和幅度行继续存在。

## 3. 全部六方向与三个旋转 jets

令完整世界控制矩阵为 $W,W_\phi,W_{\phi\phi}\in\mathbb R^{3\times6}$。它包含原两个固定 Q bubble 的所有三个控制列及新增 gamma 的三个控制列，列数始终是六。

原 working 算子使用

$$
w=WU_0,
$$

$$
w_\phi=W_\phi U_0+WU_1,
$$

$$
w_{\phi\phi}
 =W_{\phi\phi}U_0+2W_\phi U_1+WU_2.
$$

固定第 $\ell$ 个零阶控制方向，令

$$
e=W[:,\ell],\qquad
e_\phi=W_\phi[:,\ell],\qquad
e_{\phi\phi}=W_{\phi\phi}[:,\ell].
$$

由于 $U_1,U_2$ 是局部独立槽，完整偏导恰为

$$
\delta w=e,\qquad
\delta w_\phi=e_\phi,\qquad
\delta w_{\phi\phi}=e_{\phi\phi}.
$$

没有把 $e_\phi$ 或 $e_{\phi\phi}$ 误设成零；也没有把 $U_1,U_2$ 当作当前偏导的变化量。

记原径向标量及其角 jets 为

$$
q=w\cdot w,\qquad
q_\phi=2w\cdot w_\phi,\qquad
q_{\phi\phi}=2(w_\phi\cdot w_\phi+w\cdot w_{\phi\phi}).
$$

它们的完整六方向偏导为

$$
\delta q=2w\cdot e,
$$

$$
\delta q_\phi=2(e\cdot w_\phi+w\cdot e_\phi),
$$

$$
\boxed{\quad
\delta q_{\phi\phi}
 =2\left(2w_\phi\cdot e_\phi
        +e\cdot w_{\phi\phi}
        +w\cdot e_{\phi\phi}\right).
\quad}
$$

新实现按六个完整列逐一使用这些式子，没有有限差分、方向子空间截断或低秩替代。

## 4. 必须分别微分六个实际系数函数

原 `rotation_coefficients(q)` 返回六个 working 函数：

$$
A(q),\ B(q),\ A_z(q),\ B_z(q),\ A_{zz}(q),\ B_{zz}(q).
$$

这些命名来自准确 Rodrigues 公式，但小参数分支的三组系数分别按 binary64 算术生成。一般不能把另一张独立舍入表 $A_z$ 当成实际 $A$ 多项式的精确导数，也不能把 $A_{zz}$ 当成实际 $A_z$ 多项式的精确导数。

因此本实现另外计算

$$
\dot A=\frac{dA}{dq},\quad
\dot B=\frac{dB}{dq},\quad
\dot A_z=\frac{dA_z}{dq},\quad
\dot B_z=\frac{dB_z}{dq},\quad
\dot A_{zz}=\frac{dA_{zz}}{dq},\quad
\dot B_{zz}=\frac{dB_{zz}}{dq},
$$

六个导数分别来自相应实际函数。原六个系数的取值仍直接调用原完整 `rotation_coefficients`，并不换成另一组值近似。

### 4.1 小参数分支的逐表 Horner 导数

对 $r=0,1,2$ 和 $o=1,2$，原代码依序计算

$$
c_{n,r,o}
 =\operatorname{fl}\left(
   ((-1.)^n)
   \frac{n!}{(n-r)!}
   \bigg/\,(2n+o)!
 \right),
 \qquad n=r,\ldots,12,
$$

这里 $\operatorname{fl}$ 指原 Python 表达式实际产生的 binary64 常数。将这些实际字作为固定常数，原 Horner 实数表达式对应

$$
P_{r,o}(q)=\sum_{n=r}^{12}c_{n,r,o}q^{n-r}.
$$

新实现使用原代码同一常数表达式，在每个 Horner 步同时传播

$$
v_{\mathrm{new}}=vq+c,\qquad
d_{\mathrm{new}}=dq+v.
$$

右侧 $v$ 是更新前的值。由归纳法，$d$ 恰是当前 Horner 多项式对 $q$ 的导数。六张表分别运行该递推，不从相邻表借导数。

这个结论描述固定实际系数的实数表达式；新的浮点导数归约与反向 AD 的浮点路径可能不同。本源明确记录这种新算术身份，没有宣称逐位相等，也没有据普通浮点结果给出严格舍入误差证书。

### 4.2 大参数分支的完整乘除链

原分支谓词是 $q<1/4$。令 $t=\sqrt{\max(q,1/4)}$。在实际被选中的大参数分支 $q\ge1/4$，六个原表达式是

$$
A=\frac{\sin t}{t},\qquad
B=\frac{1-\cos t}{q},
$$

$$
A_z=\frac{t\cos t-\sin t}{2t^3},\qquad
B_z=\frac{t\sin t-2(1-\cos t)}{2t^4},
$$

$$
A_{zz}
 =\frac{-t^2\sin t-3t\cos t+3\sin t}{4t^5},
$$

$$
B_{zz}
 =\frac{t^2\cos t-5t\sin t+8(1-\cos t)}{4t^6}.
$$

新 `_coefficient_derivatives` 对这六个完整表达式传播值和导数对，使用

$$
(xy)^\cdot=\dot x\,y+x\,\dot y,\qquad
\left(\frac xy\right)^\cdot
 =\frac{\dot x\,y-x\,\dot y}{y^2},\qquad
(x^n)^\cdot=nx^{n-1}\dot x,
$$

以及 $\dot t=1/(2t)$、$\dot{\sin t}=\cos t\,\dot t$、$\dot{\cos t}=-\sin t\,\dot t$。原每个表达式的乘除分组保留。

作代数核对，后两项在实数算术下也可以化为

$$
\dot A_{zz}
 =\frac{-t^3\cos t+6t^2\sin t+15t\cos t-15\sin t}{8t^7},
$$

$$
\dot B_{zz}
 =\frac{-t^3\sin t-9t^2\cos t+33t\sin t-48(1-\cos t)}{8t^8}.
$$

实现采用前述完整乘除链，不用化简式来暗改原独立系数函数的来源。

正的 safe 参数同时保护未选中的大分支；$q=0$ 使用小分支，无除零。该实现保原 `where/clamp` 分支规则。在 $q=1/4$ 选择大分支的工作导数，不据此证明两个独立 working 分支在接缝处准确全阶相等；接缝、截断和舍入费用仍是后续连续误差账的责任。

## 5. 全部叉积 jets 及六方向偏导

写 $V,V_\phi,V_{\phi\phi}$ 为当前未纠正 meridian 的完整实际 jets。定义

$$
C_0=w\times V,
$$

$$
C_1=w_\phi\times V+w\times V_\phi,
$$

$$
C_2=w_{\phi\phi}\times V
       +2w_\phi\times V_\phi+w\times V_{\phi\phi}.
$$

它们对第 $\ell$ 个局部控制方向的偏导为

$$
\delta C_0=e\times V,
$$

$$
\delta C_1=e_\phi\times V+e\times V_\phi,
$$

$$
\delta C_2=e_{\phi\phi}\times V
       +2e_\phi\times V_\phi+e\times V_{\phi\phi}.
$$

再定义二重叉积

$$
D_0=w\times C_0,
$$

$$
D_1=w_\phi\times C_0+w\times C_1,
$$

$$
D_2=w_{\phi\phi}\times C_0
       +2w_\phi\times C_1+w\times C_2.
$$

其完整偏导为

$$
\delta D_0=e\times C_0+w\times\delta C_0,
$$

$$
\delta D_1
 =e_\phi\times C_0+w_\phi\times\delta C_0
   +e\times C_1+w\times\delta C_1,
$$

$$
\boxed{\quad
\begin{aligned}
\delta D_2={}&e_{\phi\phi}\times C_0+w_{\phi\phi}\times\delta C_0\\
 &+2(e_\phi\times C_1+w_\phi\times\delta C_1)\\
 &+e\times C_2+w\times\delta C_2 .
\end{aligned}
\quad}
$$

$V$ 在这次局部控制偏导中固定，但新实现中的 $V$、$V_\phi$、$V_{\phi\phi}$ 都保留原活动外参数图，不能在代码中以“局部固定”为由 detach。

## 6. 原三个 corrected jets 的完整微分

定义原表达式实际使用的组合系数

$$
a_1=A_zq_\phi,\qquad b_1=B_zq_\phi,
$$

$$
a_2=A_{zz}q_\phi^2+A_zq_{\phi\phi},\qquad
b_2=B_{zz}q_\phi^2+B_zq_{\phi\phi}.
$$

相应六方向变化是

$$
\delta A=\dot A\,\delta q,\qquad
\delta B=\dot B\,\delta q,
$$

$$
\delta a_1=\dot A_z\,\delta q\,q_\phi+A_z\delta q_\phi,
$$

$$
\delta b_1=\dot B_z\,\delta q\,q_\phi+B_z\delta q_\phi,
$$

$$
\boxed{\quad
\delta a_2
 =\dot A_{zz}\delta q\,q_\phi^2
  +2A_{zz}q_\phi\delta q_\phi
  +\dot A_z\delta q\,q_{\phi\phi}
  +A_z\delta q_{\phi\phi}.
\quad}
$$

$\delta b_2$ 同样将 $A$ 全部换为 $B$。这里使用 $\dot A_z,\dot A_{zz}$，不是偷换成相邻舍入表。

原 corrected jets 是

$$
T_0=V+AC_0+BD_0,
$$

$$
T_1=V_\phi+a_1C_0+AC_1+b_1D_0+BD_1,
$$

$$
T_2
 =V_{\phi\phi}+a_2C_0+2a_1C_1+AC_2
                +b_2D_0+2b_1D_1+BD_2.
$$

因此完整六方向偏导为

$$
\delta T_0
 =\delta A\,C_0+A\delta C_0
  +\delta B\,D_0+B\delta D_0,
$$

$$
\begin{aligned}
\delta T_1={}&
 \delta a_1C_0+a_1\delta C_0+\delta A C_1+A\delta C_1\\
 &+\delta b_1D_0+b_1\delta D_0+\delta B D_1+B\delta D_1,
\end{aligned}
$$

$$
\boxed{\quad
\begin{aligned}
\delta T_2={}&
 \delta a_2C_0+a_2\delta C_0
 +2(\delta a_1C_1+a_1\delta C_1)
 +\delta A C_2+A\delta C_2\\
 &+\delta b_2D_0+b_2\delta D_0
 +2(\delta b_1D_1+b_1\delta D_1)
 +\delta B D_2+B\delta D_2 .
\end{aligned}
\quad}
$$

以上各项与 helper 的 `_analytic` 一一对应。六列独立完整生成；每个所需 $j$ 都将 $\delta T_j$ 送入原 `_total`，随后除原正的 $S$。返回 shape 为 $(A,j+1,3,6)$，不做秩裁剪、对称化、列删减或伪逆截断。

## 7. 完整外参数 J/J* 为什么仍保留

令 $x$ 是全部原自由变量，包含原所有自由 core、所有 Fourier/quintic 系数和 H。原隐式链需要

$$
x\longmapsto
\mathcal A_j\bigl(U_0(x),U_1(x),U_2(x),\mathcal D(x)\bigr).
$$

新解析式显式保留 $U_0,U_1,U_2$、$W$、完整未纠正 meridian jets 及所有系数函数的 tensor 图。因此活动上下文中，后续 Torch 对它微分时，链式法则包含所有这些依赖，不只某一个局部控制方向。

当原 previous 已有活动图时，helper 从不 detach 它。当 previous 本来没有 `requires_grad` 而当前开启 grad 时，保原局部叶约定，只为这个本来独立的局部控制创建叶；活动 data 完全保留。no-grad 调用的返回为 detached 数值，与原函数的调用范围相同。

新解析支不调用 `autograd.grad` 来重新求 frame 的第一层偏导。它直接构建这个完整偏导函数的前向算式；活动外层仍能继续微分该算式。原 AD fallback 仍使用完整 closure 和全部 $3(j+1)$ 个反向积，并在 active 情形保 `create_graph=True`。

原 normal 链的以下部分不变：

- 所有原 32 个共同分区节点及其实际 carrier；
- 每一段完整 residual、全角 Newton/Armijo、控制域和实际失败记录；
- 原 $3/6/9$ 矩阵及两角 jet 的下三角隐式链；
- 真实 previous、frame、zero 及目标对外参数的全部依赖；
- 完整 `_stage_control_jets`、`_stage_constraints` 和 `_implicit_jet_value`；
- 原物理六jet中的完整 current closure lift 以及三个实际 Gram 行；
- 原所有几何、幅度、永久地点和真实非线性验收。

特别地，新 helper 不会把 Newton 迭代过程冒作准确隐式微分，也不把 root cache 的 detached 值直接拿来替活动图。

## 8. 数值 fallback、来源与计数

### 8.1 真正独立的完整源

新 normal 的唯一科学 wrapper 为：

```python
def _normal_frame_jets(self, previous, data, order):
    return self.analytic_normal_frame.frame(previous, data, order)
```

新 helper 构造器核：

- 完整 normal schema/model canonical 及实际整文件 SHA；
- 全 base 对象及 `6a803...` 实际 source；
- 所有六控制、三增量、完整共同分区；
- 原 `_W/_total/_corrected_jets/_closure_jets/_run_chain/_get_roots/_implicit_jet_value/_meridian_data` 等完整 AST；
- 唯一新 wrapper 的精确 AST；
- 实际 `rotation_coefficients` 的函数名与 code file 全 SHA；
- 实际当前点、完整 data order、CPU float64、所有角/径向维度及有限输入。

完整来源、模型或 shape 错误在解析尝试之前直接报出，不用 fallback 掩盖它们。新上层全部调用方与四 cache/helper 的 schema、method AST 和完整 source pins 必须独立闭合；不能把旧 guard 删除或仅换报告标签。

### 8.2 完整原 AD fallback

在已通过输入/source 合同后，解析支若遇到算术、内存或数值运行不可用，可回到同一实际点、同一完整角块、同一 order 的原 AD frame。它不缩角、不删控制列、不选少量节点，不修改任何原 root 容差或 normal 分区。fallback 仍失败时诚实传播失败，不能把它解释成全域几何不可行。

新算术允许与旧反向积产生不同的 binary64 frame 字；原 true residual 和所有验收仍要真实重读。不存在由“解析公式正确”自动得到同一 working root、同一 accepted field、同一 continuous branch 或严格误差费用的结论。

### 8.3 不伪造旧成本计数

原 `frame_reverse_angle_products` 只累计真正执行的原反向积。解析成功时不把这些没有执行的反向积记成已执行，也不伪增原 `closure_jet_angle_evaluations`。

新 helper 分开记录：

- request/return/failure、order、角数、活动图/数值范围；
- 解析尝试、失败与原 AD fallback；
- 实际六列开始/返回；
- 实际 `_total` 调用与完成的角向量数；
- 原六系数取值和六函数导数的实际调用；
- fallback 的每个真实反向积尝试/返回；
- 原 normal counters 的实际差值；
- 同点 previous 全字摘要、结果全字摘要、实际耗时（对通过输入合同的调用，包含 shape/有限性和字节记录费用）及 last-call 来源。

纯 validator 只核这些已有字段及完整 source/model/point 关系，不重新运行 frame、root、F、J 或数组运算。初始零调用时 last-call 为 null；失败不得借上一帧的结果摘要。捕获 current point 不等于它一定是最终已接受点，报告中保留真实点等号。

## 9. 解析 J3 之后仍存在的完整调用链与成本

以下是源代码结论，不是本次 run07 的实测 profile。

### 9.1 首次 residual 与几何读

`residual` 按完整角块调用 `fields_torch(order1)`。后者先建立完整 meridian data、core/cap/reference 和积分 W，然后才查询 root cache；cache hit 并不消除先前的 meridian data 构造。

缺少 root 时，`_run_chain` 仍完整走所有 normal 段。原完整 frame 在每段读取 preceding control 的零/一阶角 jets，之后有 Newton、当前矩阵、两角 jet 中已要求的求解、实际 residual 与 endpoint 重读。局部解析 J3 只改善其中的 `_stage_jacobian`；它未替换 frame。

随后的完整几何读需要 order2。已有 order1 root 可保原已计算低阶字，但 order 升级仍要经过全部段的完整高阶 frame、角方程、相应 solve 和真实 checks。它不是免费读取，更不能凭 order1 的已有成功填 order2。

### 9.2 活动 J/J* 的全部 normal 图

活动 `_implicit_jet_value` 用数值缓存选择的全部实际 root，但重新建立每段 previous/frame/zero 的完整活动图，再用当前矩阵构造零值 implicit surrogate。所有 32 段仍在，最终原参数 J/J* 不能只保最后段。

C1 原 scope 只在同点、同图、同 order、同全部控制字和原 eligibility 条件下复用。generic template 的完整局部 partial 本身还需要对 frame 的全部 $18(j+1)$ 个分量做相应反向偏导；这些实际工作没有被本 helper 偷删。新 helper 先避免每次 frame 内的第一层 $3(j+1)$ 次反向构图；不能据此声称所有高阶 AD 或整条图已经消失。

### 9.3 adjacent 6/9 矩阵与真实回退

当前 adjacent helper 在真实 provenance/全字条件成立时，使用相邻已有 frame 和一个实际新 final frame 装配完整 $6/9$ 矩阵；因此不能把它一概描述成每段仍独立 full-AD 6/9。不满足条件时它回到完整原矩阵路径。新 frame 改善那个必要 final frame 以及其他真实 frame 请求，但不删任何矩阵或隐式行。

### 9.4 永久点已有缓存与仍可能重复的前缀

完整 geometry 已在同点全 grid 中保存所需 explicit/candidate 的物理六jet，许多 P0/grid 地点可以命中这个真实 cache。不能声称每个永久点都重新跑完整场。

非 grid 地点或某些逐行 point-VJP 仍可能重复同角的完整 integration 前缀。严格同当前完整点、字面角顺序、order、source 和 query 的 no-grad integration cache 可作为另一个独立后继，但不能直接借给活动 J/J*。它不取代本次对首次全 normal 帧成本的处理。

本次新实现只针对上述真实存在的一层计算；没有科学实测前，不声称它就是运行耗时的唯一来源或有任何确定加速比。

## 10. 严格数学与数值结论的范围

在固定分支、固定实际系数常数的实数算术表达式中，§3–6 是完整链式法则和乘积法则，由此得到原 working closure 对六个零阶控制槽的完整偏导。沿活动输入继续微分时，所有外参数依赖都保留。

浮点实现仍有新乘加与归约路径；准确 Rodrigues、截断多项式、working jets 的独立舍入表、branch seam、normal root、隐式逆与物理六jet之间的误差责任没有消失。尤其：

- 不将独立 working $A_z/A_{zz}$ 表的名字当作精确导数证明；
- 不将原 working $T_\phi/T_{\phi\phi}$ 自动当作同一个 binary64 值函数的准确经典角导数；
- 不由普通 frame finite 或局部矩阵可解推出全角连续分支；
- 不由解析替换自动声明整面度量、全 t 几何、幅度或 refinement 标准完成；
- 不因本 source 的数学等式重新归类 run07 的未返回结果。

完整后继只在 public Actions 运行，按实际 full report、counter、packet、true residual 和原验收逐项登记。原未返回历史与已知完整有限材料包络责任继续保留。

