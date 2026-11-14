# 实际 M14 导出有限图的轴点下界：全文独审与真实重放

日期：2026-11-10。审者：Astra-visible-flex-78718bd0 / independent_audit。

## 0. 结论与对象

**全文数学、全部新源码和实际独立重放通过。** 结论只排除这一个保存的有限 prefix 对其 frozen target 达到原 $2\cdot10^{-9}$ 预算。它不自动成为主精确目标／完整 common-cut 闭图的下界，也不排除其它候选或任何无限维存在结论。

被审原稿：[numerical-prefix-axis-lower-v1](2026-11-10-78718-numerical-prefix-axis-lower-v1.md)，8767 字节，SHA256 `989f3109bb4bd7af752b7e81044f4b8bbc431f59be8a8008b668c6facee9cbe3`。全部新脚本 `78718-prefix-nodal-axis-lower-v1.py`，9205 字节，SHA256 `661bc0daf17b303cfc3c093b9f913b9f003f68f0463b24bda0557ad72c48cbf8`，已完整读取；作者稿、源码和输入不作修改。

审者未参与该有限候选构造、参数调整、节点预算选择或此轴点见证的发现。此次执行固定已冻脚本，是对确定图与确定扫描的独立复核；没有选择新候选，也未读取或输出候选参数数组。主独立 BVP 仍另由自身观察单元持有，不能与本次小检查混淆。

冻结对象是 `2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json`，9865 字节，SHA256 `11cd5569b3c2218591a757aea966f9aa25963fa1a3ec69fbb0b6729cb141a42d`。它的 Cartesian 有限表示 M=24、原生节点 N=6599。原 BVP 的 M14／N512 与此表示维数是不同对象，本检查没有执行源方程频率加密。

目标 metadata `prefix-target.json`，5695 字节，SHA256 `dbfb5c348a6921b078c1ee25c9aa5874856de303afd11b1e6277ac1eebdbbd8c`；原全域 metric 报告 `prefix-base-metric.json`，4110 字节，SHA256 `b076c6c052a00d72d201ca9c76a3a5a724e9dc70350437cb14fa90d430f0c48a`。三者及原稿、程序在 **a73b4e exit 0** 全部逐字核 SHA 后才开始复跑。

## 1. 新程序与原定义的完整阅读范围

实际回执：原稿全文 `ea8fdf`；全部新代码 `a8804d`、`0265c8`。另核如下定义：

- storage helper 全文 `e4c81a`，包括 exact logical bytes 的读取和数组 dtype／shape 检验；
- `ExactHermite.__init__`、`ranges` 与 `cylindrical` 全相关函数，`f094a8`；
- common-cut 的完整 `install`／`CommonCutPrefix` 与 `make`，`e2d48b`；
- mirror wrapper 全文，`5355cc`；
- metric polynomial 的完整 `run` 目标式与正性门，`3444ff`；
- 原 [exact-bridge-and-metric-transfer](2026-11-09-db6f-exact-bridge-and-metric-transfer.md) 全四节，`bfc2df`，特别 §3 的真实域重参数化。

此 storage 家族的纯字节 codec、原 reader 的数学不变性及整族来源闭包已有本会话全文独审；本次硬钉以下六份不变源，并再次实际核其身份：

| 文件 | SHA256 |
| --- | --- |
| `78718-prefix-storage-v1.py` | `83cf59cfe5ab373421e53d0c0d8d2274edfc6a6b266fc2ab6161274b474a4329` |
| `78718-prefix-byte-shards-v1.py` | `e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39` |
| `78718-prefix-continuous-hermite-storage-v1.py` | `09e8c748c7cc49347876d849029e835a8cd0e5f097d36eaf6cf2fd7c0f2ddc18` |
| `78718-prefix-common-cut-storage-v1.py` | `34b0b92c6f4d92bd497f3d84d28cbd73cb29271e36b240d3a19795987f057d43` |
| `78718-prefix-metric-polynomial-storage-v1.py` | `d290543f75224509fef8287db838265540a74b7caec38d7b9f34cea563d8359e` |
| `78718-prefix-metric-supplier-storage-v1.py` | `f2d8e79504a2a3895ec8705457eabe46321e80b68b8e7c7de11f13015d160ff3` |

另已核 base 的 `wrapper_sha256` 确为当前完整读过的 mirror 源 SHA256 `f975ab40ca05f5237954398533934eda2365ceda38cb0ba4dfe8d9e3287f6957`。其对应修改也在下文具体检查。

## 2. 为什么保存 nodal jet 是一个精确点值

有限图的定义是共享二 jet 的精确分段五次 Hermite 图，数据的每个有限 binary64 数被解释为精确二进有理数。interval `power` 是该图的系数包围，不是任意选取一个 interval 系数来另定义图。mean 的节点位置按保存 increments 的精确有理部分和确定，原存储的 mean 一阶／二阶 jet 保留。

为不以程序注释代替数学，考虑任意一跨 $h=s_1-s_0>0$，置 $\tau=(s-s_0)/h$，左右数据 $Y_0,D_0,Q_0$ 与 $Y_1,D_1,Q_1$。令
\[
e_0=Y_1-Y_0-hD_0-h^2Q_0/2,
\quad e_1=h(D_1-D_0)-h^2Q_0,
\quad e_2=h^2(Q_1-Q_0).
\]
代码的精确多项式为
\[
P(\tau)=Y_0+hD_0\tau+(h^2Q_0/2)\tau^2
 +(10e_0-4e_1+e_2/2)\tau^3
 +(-15e_0+7e_1-e_2)\tau^4
 +(6e_0-3e_1+e_2/2)\tau^5.
\]
后三项系数的和为 $e_0$，所以 $P(1)=Y_1$。其一阶加权和 $3c_3+4c_4+5c_5=e_1$，二阶和 $6c_3+12c_4+20c_5=e_2$；因此
\[
P_\tau'(1)=hD_1,\quad P_\tau''(1)=h^2Q_1,
\quad P_\tau'(0)=hD_0,\quad P_\tau''(0)=h^2Q_0.
\]
转回 $s$，左右跨在公共原生节点给出完全相同的保存一阶／二阶 jet。mean increments 只改变 $Y$，这个端点恒等仍成立，不能因此改变 $D$。

代码只读 `jets[1,node]`。通过 storage 的 `verify_arrays=True`，三个数组都实际为 `<f8`，shape 分别是 `(N,)`、`(3,N,3M+2)`、`(N-1,)`；因此 `float` 转换不引入额外有效位损失。`Fraction.from_float` 随后精确取出所存二进值。所有系数有限、mesh 严格增加均检查，未把 NaN／Inf 或非法跨交给算术。

## 3. 两条轴上的完整一阶导数

按 `cylindrical` 的实际布局，保存槽位依次为：$r_0$，$r_1,\ldots,r_M$，$t_1,\ldots,t_M$，$z_1,\ldots,z_M$，$z_0$。新程序索引 0、1…M、2M+1…3M、最后一槽与它逐项相同，没有把 tangential 或 mean 槽误读成 height mode。

固定 $\psi$ 的经线导数不微分转动基，故
\[
F_s=R_s e_r+T_s e_\theta+Z_s e_z.
\]
在 $\psi=0$ 与 $\pi/3$，$\sin(3j\psi)=0$、$\cos(3j\psi)=\sigma_j$，其中 $\sigma_j=1$ 或 $(-1)^j$。因此
\[
R_s=r'_0+\sum_{j=1}^M\sigma_jr'_j,
\quad T_s=0,
\quad Z_s=z'_0+\sum_{j=1}^M\sigma_jz'_j,
\quad h_{ss}=R_s^2+Z_s^2.
\]
这是任意保存有限模式的一阶精确身份。源码从不计算近似 $\pi$、sin、cos，而以奇偶整数给符号。所有和、平方、减一与绝对值均在 `Fraction` 中进行，未使用舍入区间上界代替下界。

在普通显示步骤，先取 `float(value)`，再用该 binary64 的精确 Fraction 与原值比较；若中点偏高只将 lower 向负无穷移一个 `nextafter`，若偏低则将 upper 向正无穷移一格。随后再次要求精确有理包含，浮点溢出亦会拒绝。因此显示的 lower 确为向下端点，精确比较本身仍直接用 Fraction。

## 4. 冻结目标的 Rayleigh 商：为什么是下界

目标材料角为
\[
\theta(s,\psi)=\psi-e(s)\sin(3\psi)/3,
\quad g_0=ds^2+a_0(s)^2d\theta^2.
\]
在两条轴上 $\theta_s=0$，所以 $(g_0)_{ss}=1$，不需要代入或近似任何 $a_0,e,e'$。实际 full metric 源的 `targetE=1+a^2 theta_s^2` 与此完全相符；该源还拒绝非正半径／角 Jacobian。**6a3722** 实际核 frozen 全域报告的两个正性下界都为正。这与已审目标定义相容。

给任意正定 $g_0$ 和对称误差形式 $h-g_0$，令 $B=g_0^{-1/2}(h-g_0)g_0^{-1/2}$。对非零方向 $v$，以 $w=g_0^{1/2}v$，有
\[
\|B\|_{op}\ge\frac{|w^TBw|}{w^Tw}
=\frac{|(h-g_0)(v,v)|}{g_0(v,v)}.
\]
取 $v=\partial_s$ 即得 $\|B\|_{op}\ge|R_s^2+Z_s^2-1|$。这里不要求把所有方向都采样；一个方向便给严格下界。原全域上界只用于对象连接与已知正性，完全没有进入这个下界的有理算式。

实际见证是原生节点 1518、$\psi=\pi/3$，保存径向坐标
\[
s_i=2474546589463719/9007199254740992.
\]
其 $E_i=h_{ss}$ 的精确值与 $E_i-1>0$ 保存在独立报告的 Fraction 字段；本审再次核 $E_i-1$ 与报告 signed 项完全一致，且严格超过 $1/500000000$。向下显示值为
\[
|E_i-1|\ge 7.7414749922943985\times10^{-8}>2\times10^{-9}.
\]
终端短 JSON 的十进显示 `7.741474992294399e-08` 是同一 binary64 lower 的规范短表示，不是另一次重新向内舍入。

这排除的是这个图相对于这个 frozen target 的原全域预算。原 BVP 的 RMS、程序自然成功、其它包围上界或有限模式收敛状态都不推翻这一单点数学事实；本审不由它推其它图不合格。

## 5. common-cut 和 mirror 的局部支持关系

新脚本对原 `make` 使用完全相同的 binary64 表达式
`int(np.searchsorted(mesh,mesh[-1]-.15))`，得到 start=6124。其节点下端显示 1.8720381178742067；见证 $s_i$ 下端显示 0.27472985991302756，且索引 1518 严格小于 start。循环检查了节点 1…6123 的两轴，确为 $2\cdot6123=12246$ 个点。

common-cut reader 先把原 M=24 的各轴系数按真实布局嵌入更大的尾基，其余补零；这是同一个函数。随后仅在 `range(start,len(mesh)-1)` 的跨上加五次修正，所有更早跨的系数未动。见证及其两侧邻域都在此区间之前，故任何按该已冻定义从这个 base 构造的 common-cut 图在此处与 base 精确相同。这个支持结论不使用未来末 jet 的具体数值，也不替未来产品伪造 SHA。

mirror wrapper 的额外 mutation 仅为 `jets[2,0,2*M+1:]=0`，其余入口奇偶是已满足后的断言。它只改变初节点 height 二阶 jet，影响首跨；原生节点 1518 及邻跨不受影响。当前 base 已经是实际生成的 mirror 图，本点下界直接消费该 base，无需从旧未镜像图转抄导数。

因此可以陈述“若按指定定义生成 common-cut，则该点未被局部修正改变”。当前脚本本身没有生成 common-cut、尾、桥或全闭图，不能删掉这个条件。

## 6. exact-target 转移必须保留的 λ²

原 exact-bridge 稿 §3 的真实记号是：保存图的域终点 $S_0$，精确目标终点 $S_*$，先将保存图还原为物理材料角，再以
\[
u=\lambda s,\qquad \lambda=S_0/S_*>0
\]
把精确目标参数 $s$ 送到保存径向参数 $u$。这里的 $u$ 是该旧稿的径向变量，与其它稿的物理角字母须区分。

在轴上固定材料角对应固定辅助轴角，因为 $\theta_u=-e'(u)\sin(3\psi)/3=0$ 且角 Jacobian 非零，隐函数求导给 $\partial\psi/\partial u|_\theta=0$。所以该点原保存的 $E_i$ 也是固定材料角下的径向速度平方。

重参数化后的同一点位于 $s_i=u_i/\lambda$，并有
\[
|\partial_s\widetilde F|^2=\lambda^2E_i,
\quad (g_*)_{ss}=1,
\quad \|g_*^{-1/2}(\widetilde h-g_*)g_*^{-1/2}\|_{op}
\ge|\lambda^2E_i-1|.
\]
所以不能原样把 $E_i-1$ 当作 exact-target 下界。若有这个新图实际绑定的正区间 $0<\lambda_-\le\lambda\le\lambda_+$，单调性给
\[
\lambda^2E_i-1\in[\lambda_-^2E_i-1,\lambda_+^2E_i-1].
\]
若左端正即以它为严格下界；若右端负取其相反数；若区间含零只能先给下界零。该结论只需实际缩放区间和点证据，无需重跑整域上界，也不能借旧 M12 的邻近缩放冒充新图的绑定。

这不重开主 g 唯一精确桥的存在性。R21 已审唯一根仍接受；现在缺的是对本轮实际 base、target、own tail／common-cut 及相应缩放的身份接线。当前报告 `new_exact_bridge_target_transfer=false`、`complete_closed_graph_rejection=false` 正确保留这一范围。

## 7. 全部新程序的门、实际执行和逐字段核对

程序先拒绝覆盖输出，逐字硬钉六份源；以已审 storage helper 核 descriptor、每片、完整原 gzip／NPZ 逻辑字节、三个数组 dtype／shape。然后核 geometry 的 mirror／ell 状态、target→geometry 和 metric→geometry／target 的 SHA、supplier／metric 源身份及整域覆盖标记。它只加载数据，没有导入 BVP／RHS／tail evaluator，也未调用 SciPy 求解器。

有限性、维数、mesh 单调性检验后，按冻结 scan 顺序取 exact Fraction 最大轴点；选择顺序也是确定的，等值不替换第一次见证。原预算比较在 Fraction 中做，而不是对 lower 显示值做。写报告前再次核程序、六源及去重的八份实际输入闭包，变化则拒绝。报告包含真实 scope flag，没有以 source hash 替代数学证明。

本审实际完整重放命令：

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
scripts/78718-prefix-nodal-axis-lower-v1.py
--geometry notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json
--target notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-target.json
--metric-certificate notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base-metric.json
--out notes/2026-11-10-78718-audit-prefix-axis-lower-01.json
```

cwd 为本题目录。真实启动 **b1bd09 / session 43214**，真实续读 **e22b4c，自然 exit 0**。输出 [audit-prefix-axis-lower-01.json](2026-11-10-78718-audit-prefix-axis-lower-01.json)，7601 字节，SHA256 `97e229ad32c4b1efc0d305ed5c1ff9734e6304e1e8f3dcd326b842c938634083`。0 BVP、0 ODE、0 geometry producer。

随后 **6a3722 exit 0** 独立核：作者原报告 SHA `ccce95078e16f2b503dc3df1f19503c8e15b8362647007db5f9ea243f1c746cf` 仍正确；两报告除不可期待一致的运行秒数 `seconds` 外，全部字段完全相等。又重算了 signed Fraction 与 $E_i-1$ 的恒等、正号、原预算严格比较、节点坐标、1518／π3／6124／12246 四项，以及六源／八输入的当前字节身份。未把任何原始数组输出到对话。

本审核查完成，没有发现实质错误。可登记上述 frozen-target 单点拒绝中间结论；未来 exact-target 或闭图判定须另行使用本轮实际绑定，不能用本审报告提前盖过缺口。
