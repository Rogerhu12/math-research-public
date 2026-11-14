# R133：全部网格凸包与连续双线性几何包络

2026-11-14，visible-exact-astra-ac0d。

**已证明并完成网格消费者。** 原 `ac1d5b98…` 模型的全部 8,966 个径向单元、每象限 512 个角单元和全部四次旋转、上下反射已经消费。它们共有 4,590,592 个基本四边形；对八个反向见证像，共认证 36,724,736 个分离向量。实际网格结论是

$$
R_{\rm mesh}<1.275559740657,
\qquad A_{\rm mesh}>.901284727159,
\qquad d_{\rm hull}>.129668021172. \tag{T.1}
$$

这里 $d_{\rm hull}$ 已是到**每个完整四顶点凸包**的下界，$A_{\rm mesh}$ 已包含双线性位置和框架法向的全部交叉顶点项；均不只是最邻近采样值。连续模型还须合并下面的径向和角向误差。完整径向 directed 消费者仍在继续，因此 (T.1) 目前不单独授予连续模型、精确曲面或最终 held/reach 条件。

## 1. 精确的网格对象与分离向量

全部浮点几何块已由[原完整模型消费者](../notes/2026-11-13-R133-moving-connection-checkpoint-consumer.md)产生。这一页将其中每个保存的 binary64 数准确解释为二进制有理数，保留整个原不可变 block chain。共同世界高度平移取原报告中 `0.9654154298482165` 的**准确 binary64 有理值**，不把它换成截断十进制。

设平移后保存顶点为 $\widehat F_{ik},\widehat N_{ik}$。最后一个角点的下一邻点取

$$
\widehat F_{i,512}=R_z(\pi/2)\widehat F_{i,0},\qquad
\widehat N_{i,512}=R_z(\pi/2)\widehat N_{i,0}; \tag{T.2}
$$

这个四次旋转是坐标的准确置换与变号，不能把它当作同一个未旋转顶点。对每个径向—角单元取四顶点凸包 $C_{ik}$，以及相同权重的双线性场 $B_F,B_N$。

见证取保存腰顶点的准确旋转

$$
\widehat w=R_z(\pi/4)\widehat F_{0,0}. \tag{T.3}
$$

其中 $\sqrt2/2$ 由 Arb 向外包围。四次旋转和上下反射作用于整个模型，因此比较到基本象限上的八个逆像 $T^{-1}\widehat w$ 即准确覆盖全部八个像。

对每个 $C_{ik}$ 和每个逆像，先用浮点重心选一个方向向量 $v$，然后把所得数准确视为 dyadic。选正 dyadic $b$，用完整 directed 平方与求和证明

$$
b^2\ge\sum_{l=1}^3v_l^2. \tag{T.4}
$$

故 $n=v/b$ 真正满足 $|n|\le1$。初始平方根只是选取 $b$ 的提案，(T.4) 独立认证其范数，不假设库函数的误差为零。完整 directed 点积给

$$
\ell_{ik,T}\le
\min_{a\text{ 为四顶点}} n\cdot(T^{-1}\widehat w-a).
$$

线性泛函在凸包上的最小值就在顶点，故只要该下界为正，

$$
\operatorname{dist}(T^{-1}\widehat w,C_{ik})\ge\ell_{ik,T}. \tag{T.5}
$$

实际全部下界均为正。记录逐径向格保存各角格、各逆像的共同下界；全局取最小得到 (T.1) 的 $d_{\rm hull}$。这个方法没有把网格填充距离从最近采样距离中粗减掉。

凸性还给 $|B_F|\le R_i$，其中 $R_i$ 是本径向格全部角顶点的最大范数。位置和框架法向分别的坐标区间凸包包含 $B_F,B_N$，对这两个区间作完整 directed 点积即得到

$$
B_F\cdot B_N\ge A_i. \tag{T.6}
$$

这里确实包括不同顶点的交叉积；不能仅用四个 $\widehat F_a\cdot\widehat N_a$ 的最小值代替。

## 2. 连续模型的径向二阶界

原模型准确满足 $Q_r=Q\Omega_r$、$F_r=Qf_r$，$Q$ 为正交框架。令一个径向格宽为 $h_i$，其内部的真实 scalar germs 已分开。对每个准确角网格点，记实际 directed jets 给出的上界为

$$
A_0\ge\|\Omega_r\|,\quad A_1\ge\|\partial_r\Omega_r\|,
\qquad f_0\ge|f_r|,\quad f_1\ge|\partial_r f_r|.
$$

它们是原 3×3 skew 连接的 operator norm 和完整两分量径向速度 norm，保全部原模式。准确微分给

$$
|F_{rr}|\le A_0f_0+f_1=:M_{F,r},\qquad
|N_{rr}|\le A_0^2+A_1=:M_{N,r}. \tag{T.7}
$$

每格取其所有真实 germs 的最大值。原径向网格包含每一个 candidate cubic 的接点；所以原候选值跳都在格端，不被跨越。内部 scalar germ 接点的连接及速度由同一连续内蕴定义给出相同两侧值，因而 $F_r,N_r$ 连续；二阶径向导数只需分片有界，(T.7) 仍给整个格的 Lipschitz 一阶导数界。没有要求不匹配的第三阶 scalar jets 相等。

设实际径向积分消费者在两端全部准确角点给位置误差 $e_{F,i},e_{F,i+1}$、框架误差 $e_{Q,i},e_{Q,i+1}$。取

$$
\epsilon_{F,i}^{\rm node}=\max(e_{F,i},e_{F,i+1}),\qquad
\epsilon_{N,i}^{\rm node}=\max(e_{Q,i},e_{Q,i+1}). \tag{T.8}
$$

其完整框架 Frobenius 误差当然控制单列法向误差。模型锚的初始误差、每个实际单侧 Taylor remainder 和回接原浮点整步的误差都必须已在这两个数中；不能只代入浮点 frame Gram 缺陷。

## 3. 连续角界与不丢混合项的双线性误差

设 $\Delta\phi=\pi/(2\cdot512)$。在同一径向格相交的全部角缺陷 native 行上，取

$$
M_{F,\phi}\ge\sup|F_{\phi\phi}|,\qquad
M_{N,\phi}\ge\sup|N_{\phi\phi}|. \tag{T.9}
$$

[已完整消费的角向证书](../notes/2026-11-14-R133-final-complete-angular-defect.md)确实给出这些全圆周界，保全部残差、均值、接口和 model anchor。其全局宽放可用 $5.970523$ 与 $4.646383$，也可消费更紧的逐行数据。

令 $I_r,I_\phi$ 为线性插值算子。准确恒等式

$$
F-I_\phi I_rF=(F-I_\phi F)+I_\phi(F-I_rF) \tag{T.10}
$$

及线性插值的正权重给

$$
\boxed{\quad
\epsilon_{F,i}=\epsilon_{F,i}^{\rm node}
  +\frac{h_i^2}{8}M_{F,r}
  +\frac{\Delta\phi^2}{8}M_{F,\phi},\qquad
\epsilon_{N,i}=\epsilon_{N,i}^{\rm node}
  +\frac{h_i^2}{8}M_{N,r}
  +\frac{\Delta\phi^2}{8}M_{N,\phi}.
\quad} \tag{T.11}
$$

则整个单元上 $|F-B_F|\le\epsilon_{F,i}$、$|N-B_N|\le\epsilon_{N,i}$。第二项只需要角网格点上的径向二阶界；第一项需要全连续径向的角二阶界，二者均已明确区分。由于使用 (T.10)，不需要额外的混合导数假设，也没有遗漏某个 $h_i\Delta\phi$ 项。

这一结论对格端的一侧径向导数不匹配仍成立，因为 $F,N$ 本身由同一 ODE 连续通过该格端，且每格分别插值。

## 4. 从 mesh 到整个连续模型

令 $d_i$ 为本径向格的全部八像凸包距离下界。连续模型的准确见证为 $w=R_z(\pi/4)F(0,0)$，故由准确角点上的径向积分误差

$$
|w-\widehat w|\le e_{F,0}. \tag{T.12}
$$

它不需要再付角插值，因为 $\phi=0$ 本就是准确节点。结合 (T.5)、(T.11)，到四次旋转及上下反射后整个模型像的距离满足

$$
\boxed{\quad
\operatorname{dist}(w,\mathcal M_{\rm model})
\ge\min_i(d_i-\epsilon_{F,i})-e_{F,0}.
\quad} \tag{T.13}
$$

同样，整个模型的范数与框架支撑量满足

$$
|F|\le\max_i(R_i+\epsilon_{F,i}),\qquad
F\cdot N\ge\min_i(A_i-\epsilon_{F,i}-R_i\epsilon_{N,i}). \tag{T.14}
$$

支撑公式使用准确 $|N|=1$ 以及
$F\cdot N-B_F\cdot B_N=(F-B_F)\cdot N+B_F\cdot(N-B_N)$。
这里 $N$ 是准确模型框架列；在未解 Codazzi 中心上不自动等于该位置图的几何单位法向。

若后续同对象精确解与模型的完整位置、真实单位法向比较误差分别为 $\delta_F,\delta_N$，则在 (T.11)、(T.14) 中分别再加它们，直接得到精确解的支撑界。见证也加其真实比较误差。外帽锚、连续修复中心、最终选定 $\eta,\nu$、完整高尾及非线性校正都必须进入这些费用，不能预设为零。

模型范围以外的真正帽和固定标记也必须分别覆盖。只要其准确高度离腰见证至少 $.9$，它们的距离比较很宽裕；该高度条件本身仍须按已发表同族帽/marker 定理落实，不能从本页有限模型直接推定。

## 5. 实际消费者、身份和当前完成边界

[完整凸包源码](../scripts/fourfold_codazzi_complete_geometry_mesh_hulls.py)只读取原中心、原 geometry report 和全部 141 个不可变块，不重算 primitive 或原浮点 ODE。
实际运行正常返回 0，耗时 198.985065 秒；每个径向单元的 $R_i,A_i,d_i$、最小高度、达到距离界的角/逆像位置以及全部 block SHA 都保存在
[完整原生记录](../notes/2026-11-14-R133-complete-geometry-mesh-hulls-native.json.gz)。

它逐项验证原报告 SHA `49870375…`、原 candidate SHA、完整 8,967 点径向网格和全部 block chain 的身份；最后链 SHA仍为 `4d87057a72944913d013636f57c1b90688a5df95264825f86241e47535e5ffa1`。完整原始顶点、均值高度平移、真四次 wrap 和反射全部保留。

(T.11)–(T.14) 是下一消费者的准确公式。原径向 directed native 尚未覆盖全部 8,966 个单元，故目前不能给这些公式填入一个虚构的全域积分误差。本篇保留所有模型/精确解、body/帽和源/几何差别，继续实际完成它们后再判断最终比例。
