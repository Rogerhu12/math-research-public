# R149 自然母线图中的实际 P1 场读入与解析二阶角导数

本说明封存实际读入器与一次小范围真实检查。数学图册及整函数接口证明见
[R149](../results/R149-frozen-ruling-atlas-with-full-functional-traces.md)，
冻结参考函数的原定义见 R139、R144 及
[原参考二阶导数说明](2026-11-12-fd2d-metric-coast-native-second-jets.md)。
本组不重新求解 BVP，不把有限抽样提升为连续证书，也不改变保存场的网格、
参数、中央种子、尾函数或参考函数。

## 1. 实际输入与计算对象

实际输入是 `2026-11-12-fd2d-ruling-atlas-warm01-warm.npz`，
SHA256 `d705b2e328873b37f541b524800d09d7261e579c71f75b33fc6178d23d014b69`。
它有 123 个保存径向节点；原 122 节点全部保留，另增加图册端点 `1.40`。
保存的逐节点 correction 作分片线性函数，角方向保留其完整有限 Fourier
表示，三场顺序始终为 `(n,m,l)`，其中 `l` 是独立场，绝不由未知 `n` 消元。

该 warm 是明确的新有限场。原生成器记录的同材料角投影误差
`max(n,m,l)=(0.08931556,0.10001922,0.27467357)` 不被读入器重新解释为
准确重表达。本文检查保存后的新定义，而不宣称它等于旧 mixed-chart 场。

实际物理 profile 输入为
`2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json`，
SHA256 `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
冻结入口 `2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz`
SHA256 为 `ed69b9a6599ef75f36f2d5bc094d152d993baeb078f4852a392648b85f6c9c3a`。
旧参考首导缓存 SHA256 为
`a300860b15e993f4272dff55d9068723664d84240d643a195b2c955ab15fd6c8`；
它仍只代表旧保存点。本次新母线标签求值直接使用解析公式，不借用不同
材料角列的旧缓存。

## 2. 全局角图与单侧约定

计算径向变量为物理弧长 `s`。母线标签 `xi` 是冻结入口的 seed-normal
角；入口材料角为 `t=U_seed(xi)`，不是 `xi` 本身。图册为

* `[0.55,e]` 上从旧图以五次平滑阶梯凸组合到 `U_seed`；
* `[e,f]` 上采用冻结母线图 `U(s,xi)`；
* `[f,1.40]` 上从冻结的完整出口角函数凸组合回旧图；
* 其余区间保持旧图。

这里保存的二进制端点为
`e=0.5919999999999992`、`f=0.8675434451024153`。
R149 证明 `U,U_xi,U_xixi` 在接口有共同整函数迹且 `U_xi>0`。
`U_s,U_sxi,U_ss` 可有真实侧限跳变。读入器不把它们平均，也不通过径向
微小偏移猜测侧限：在同一保存节点调用相应解析片公式。

`evaluate_native(s,xi,side='left'|'right')` 同时把指定侧用于实际 P1
correction 的径向斜率和角图的径向导数。单独查询
`chart(s,xi,side='coast')` 的默认约定与有限求解器一致；用于微分的场查询
必须选同一个 `left` 或 `right`。这样不会将左侧 P1 斜率与右侧图册漂移
错误地混合。

## 3. 实际场的值与链式导数

令 `B y` 为保存 P1 correction，`L_old` 为完整 seed/tail lifting，`R` 为
同一个冻结物理参考函数，`w(s)` 为原 coast 窗。实际场定义为

\[
 f(s,\xi)=B y(s,\xi)+(1-w(s))L_{old}(s,\xi)
                  +w(s)R(s,U(s,\xi)).
\]

其中 correction 只加一次，不再乘 `1-w`。读入器先在一个零 correction
浅复制视图求 `L_old`，再加实际 correction 与参考函数。它逐点返回值、
`x`、`xi`、`xixi`、`x_xi` 五种真导数；这里 `x=s`。

对任一物理参考标量 `R(s,u)`，链式公式为

\[
 R_x=R_s+U_sR_u,\qquad R_\xi=U_\xi R_u,
\]
\[
 R_{\xi\xi}=U_\xi^2R_{uu}+U_{\xi\xi}R_u,
\]
\[
 R_{x\xi}=U_\xi R_{su}+U_sU_\xi R_{uu}+U_{s\xi}R_u.
\]

窗函数还准确贡献 `w_s(R-L_old)` 和
`w_s(R_xi-(L_old)_xi)`。计算整张接口数组时，原图册 API 的输入是径向与
标签的张量积；读入器按实际相同 `s` 分组调用，避免把扁平的配对点误作
巨大外积。该分组不改变求值点。

`physical(s,u,side=...)` 使用同一新图册反解材料角，再按
`partial_s|u=partial_x-(U_s/U_xi)partial_xi` 及对应角导数公式给出物理
导数。其用途是 R141 固定材料角的 frame/position 重建，而不是把不同
计算角下的 Fourier 系数直接等同。

## 4. 已知母线标签下的解析参考二阶导数

新模块 `fd2d_gc_ruling_reference_second_jets.py` 在已知标签 `xi` 下直接
调用同一 `atlas.ruling_jet(...,include_native=True)`。因此数值第一导数
与主 provider 使用同一公式；只有二阶物理角导数及混合导数是新增输出。
这里不调用可能迭代停滞的材料角逆解，也不修改旧 `SavedNativeCoast`。

设入口材料变量为 `t`，冻结入口二场为 `n_c(t),m_c(t)`，
`k=m_c/n_c`。R139 已支付该冻结入口的严格正性，以下分母中的 `n_c,n`
均属于这个冻结参考，绝不是待解 raw 场。记入口半径 `a_c`、正斜率 `v`、
`sigma=s-e`、`rho_c=a_c/v`、`rho=rho_c+sigma`，并设

\[
 \Delta=\sigma(2\rho_c+\sigma),\quad
 Q=\sqrt{\rho_c^2+(1+k^2)\Delta},\quad
 z=\frac{\Delta}{\rho_c+Q},
\]
\[
 B=v(1+k^2)-k_t,\quad D=a_c+zB,\quad
 n=\frac{a_cn_cQ^2}{D\rho^2},\quad q=\frac{k\rho_c}{Q},
 \quad m=nq,\quad l=nq^2.
\]

这里 `z` 只是本段代数中稳定的根式差商，与三维高度无关。
固定 `sigma` 求入口角导数：

\[
 Q_t=\Delta kk_t/Q,\qquad
 Q_{tt}=\Delta(k_t^2+kk_{tt})/Q-\Delta^2k^2k_t^2/Q^3,
\]
\[
 z_t=-\Delta Q_t/(\rho_c+Q)^2,
\quad z_{tt}=-\Delta Q_{tt}/(\rho_c+Q)^2
                  +2\Delta Q_t^2/(\rho_c+Q)^3,
\]
\[
 B_t=2vkk_t-k_{tt},\quad
 B_{tt}=2v(k_t^2+kk_{tt})-k_{ttt},\quad
 D_{tt}=z_{tt}B+2z_tB_t+zB_{tt}.
\]

以 `log n=log a_c+log n_c+2 log Q-log D-2 log rho` 求 `n_t,n_tt`，
再用乘积法求 `m_t,m_tt,l_t,l_tt`。母线图提供

\[
 U_t=D/(vQ),\qquad U_{tt}=U_t(D_t/D-Q_t/Q),
\]

因此任一三场分量都满足

\[
 f_{uu}=\frac{f_{tt}U_t-f_tU_{tt}}{U_t^3}.
\]

实际有限入口 Fourier 系数的前三个 `xi` 导数都可逐模解析求得。
若 `h=dt/dxi`，则

\[
 f_{ttt}=\frac{f_{\xi\xi\xi}}{h^3}
 -\frac{3f_{\xi\xi}h_\xi}{h^4}
 -\frac{f_\xi h_{\xi\xi}}{h^4}
 +\frac{3f_\xi h_\xi^2}{h^5}.
\]

入口 `h,h_xi,h_xixi` 由冻结 seed 的同一解析函数给出。
再由 `m_c=k n_c` 的三次乘积公式得到 `k_ttt`，没有数值差分。

混合物理导数使用同一准确 R139 Codazzi 恒等式，实际参考半径
`a=a_c+v sigma`：

\[
 n_{su}=m_{uu}/a+(v/a)(l_u-n_u),\qquad
 m_{su}=l_{uu}/a-2(v/a)m_u.
\]

由 `l=nq^2`、`l_s=2q m_s-q^2n_s` 再求 `l_su`。这些公式仅用于解析
冻结参考；对一般 raw 场，读入器保留其独立 `l` 和全部实际残差。

## 5. 接口共同迹、允许的跳变与身份检查

新场使用同一共享节点 correction 值及完整有限角函数，因此 correction
的值和任意有限阶角导数有共同迹。图册的完整 `U,U_xi,U_xixi` 共同迹、
原 lifting 的共同物理迹，以及 coast 窗端 `w=w_s=0`，合起来给出本
实际场的 `f,f_xi,f_xixi` 共同迹；由于 `U_xi>0`，物理的 `f,f_u,f_uu`
共同迹亦成立。这是整函数条件，不以八个样本的零差代替证明。

P1 径向斜率以及图册径向导数可以跳。于是三场的 `f_s` 也可跳；这不
等于位置图的二阶导数不连续。R141/R149 的固定材料角 ODE 重建依据连续
的 `l,m` 和所需共同角迹得到位置图的实际 C2 正则性，不增加全局 C1-II
或 C3 的条件。

读入器要求 NPZ 显式保存并核对 `angular_atlas_definition`、
`atlas_mesh_definition`、`reference_evaluation_definition`；其中完整
保存节点必须逐值等于 `actual_nodes`。它还核对旧 coast binding、实际
candidate、profile 支撑、seed 权重、tail/base kind 与源 SHA。
不同源/不同参数不以同名路径代替。定义 JSON 保存原有限径向 scheme
文字，注明实际重投影与新增节点，不自行清网格或改场。

## 6. 可调用接口

```python
from fd2d_gc_ruling_atlas_native_field import RulingAtlasRawBumpNativeField

field = RulingAtlasRawBumpNativeField(
    field_npz, candidate_json,
    reference_inlet=inlet_npz,
    reference_cache=old_cache_npz,  # 可省；新标签求值不依赖此缓存
)
native = field.evaluate_native(s, xi, side='right')
material = field.physical(s, u, side='right')
chart = field.chart(s, xi, side='left')
definition = field.definition()
# definition 写成 JSON 后可使用 from_definition(path) 精确重新绑定。
```

解析参考接口为
`ruling_reference_second_jets(atlas,s,labels)`，输出 `values`、
`physical_s`、`physical_u`、`physical_uu`、`physical_su`，末轴顺序
均 `(n,m,l)`；同时返回实际材料角和第一导数公式的浮点差诊断。

## 7. 已实际完成的小范围检查

命令与全部输入身份保存于报告及 exit receipt。本次 unified-exec
session `62999`、completion chunk `ff5ed7`，真实 exit `0`；报告实际
耗时 `3.674103093` 秒、峰 RSS `76172 KiB`。只读两个保存 cell 中点及
两个接口；未装配 BVP/Jacobian，未积位置图，未求非线性方程。

两个内部点为 cell 68 的 `s=0.7691350718515524` 和 cell 97 的
`s=1.1343214557869101`。角样本恰为实际 atlas `theta` 数组索引
`[5,17,31,53,71,89,107,123]`；并非全 256 角，也非连续全角包围。
差分步长为 `2e-5` 及 `1e-5`，细步最大 scaled error 为
`5.785685988162947e-8`，误差随步长减半约按二阶下降。
新参考的 `values/x/xi` 与实际主 provider 的 direct-label 第一导数
逐值相同，最大差 `0`；保存定义重载五种 jet 的差也为 `0`。
固定材料角反解的最大残差为 `5.995204332975845e-15`。

接口查询恰在保存的 `e,f` 节点上，直接调用解析 `side='left'/'right'`，
**不使用径向 epsilon 偏移**。上述八角上的完整值/角一二导及物理角
一二导左右差均为 `0`。同一八角集合的 `max |U_s^- - U_s^+|`
分别为 `1.8791182738859815`、`1.3560483657500495`。
主 warm 检查所报约 `1.88177`、`1.35735` 来自其更大的角采样集合；
二者不是同一个离散最大值，不作全角界比较，也无需重复求值来抹平差异。
实际三场物理径向导数的跳分别可达 `446.08687583444873`、
`320.6864259164658`；它们被如实保留而非宣称为零。

所有 input/source 文件在检查前后 SHA 未变。完整样本数组、来源绑定及
定义 JSON 都与报告一起封存。本组只证明实现读的是明确的新场并通过上述
有限核验；后续原始全 Gauss/Codazzi 残差、连续误差、真实几何与尾缝仍须
消费合适的实际主求解结果，不能由本组接口核验代替。
