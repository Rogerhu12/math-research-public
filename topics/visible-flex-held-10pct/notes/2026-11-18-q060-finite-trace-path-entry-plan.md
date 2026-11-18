# q060：有限七列路径与同步 lift 的唯一初始入口计划

## 当前完成范围

本条冻结新源码、全部旧锚身份和一次最小模型入口计划。
**尚未构造新核心或 Flow，尚未评价新初猜，没有 BVP、实际尾或完整 metric 结果。**
它接在[八参数有限差分终态](2026-11-18-q060-trace-parameter-jacobian-terminal.md)之后，
不修改已审的旧 Jacobian，不重试此前失败的 $\lambda=1$ 大跨步。
有限空间独立性、主矩规范及同步 lift 代数由 R45 单独记录，本条只说明实际接口和身份。

源码准备实际 chunk `2abe74`、退出码 0，只读核 80 项源或输入及 9 个引用。
计划文件为 scratch 中
`m3_work/q060-circle-trace-path-entry-v1/launch-plan.json`，SHA256
`945259b830d5d4a129cbe86068a6f72a2940f5cba2265224584cc8ac192a785f`。
已存在的 `launch-command.json` 是未来独立模型诊断的命令，**尚未执行**。

## 固定的物理与表示选择

旧锚是原 $q=.06$、M8 的完整已接受余弦前缀：
`q060-saved-inner-resume-v1/seed.json.gz`，SHA256
`4755143bb3c02c28669eebaa2db53ad97142acec799afd4136125db4277350d9`。
使用原完整 $6\times1933\times25$ 物理 quintic 块、全部 7 个真实系数，
原最终 frozen profile、原材料 chart 和原 `.06` warp。
没有把原历史 $p_0$ 再加到已经冻结的 $\delta=.06104275721220832$。
新入口 $p_0=0$，其后第零参数仍只控制 $\delta$。

全路径明确保持**数值 gauge `.06` 和原七个 `pscale`**。
定义核心的 `seed_support_amplitude` 独立设为 $q_\lambda=.06/P_\lambda$。
这使用现有 `initial` 已区分 gauge 与 support seed 的语义，
不改变残差中的 gauge 或原参数链式法则，不是隐式地重标参数列。

新七列为

$$
C_j(\lambda)=(1-\lambda)\cos(3j\phi)+\lambda E_j(\phi),\qquad
(E_2,\ldots,E_8)=(B_2,\ldots,B_6,T,U).
$$

所有旧系数直接保留在相应七个坐标中，包括旧 $\cos21\phi$、$\cos24\phi$
两项；没有丢弃它们、再做两 jet 匹配、套用旧 $q^j$ 放大或借失败端点系数。
这是新的有限物理空间路径，不是固定 $g$ 精化或旧 raw 无限维空间的换坐标。

只选择首个非零值 **$\lambda=.02$**。
复用已经登记的 $P_1$ 严格区间，用精确 Fraction 算术计算
$P_\lambda=1+\lambda(P_1-1)$，没有重新积分求矩或扫主幅值。
$q$ 和 $\lambda$ 按所记录 binary64 代表的精确实数解释；
宽度仍用既有定义积分的十进制参数约定。
所得唯一最近 binary64 是

$$
q_{.02}=0.059818741459951905,
$$

其定义主矩残差约为 $-6.24908\times10^{-19}$，完整包围留在记录。
$\lambda=1$ 的 $q=.05210565550627671$ 只作为既有物理目标规范，
本计划不实例化该端点，也不把旧失败端点的 gauge、Jacobian 或状态当成本路径身份。

## 五份独立源码

| 源码 | 实际作用 |
|---|---|
| `circle_trace_homotopy_basis.py` | 完整七列的支撑及原函数 jets；全域曲率 jets 上界是旧 cosine 界与已合成的 R44 界的同 $\lambda$ 组合，保留 $T/U$ 抵消 |
| `circle_trace_homotopy_core.py` | 原积分核心及数值域守卫不换方程；$\lambda=0$ 返回字面原余弦类，$\lambda=1$ 用原 R44 类 |
| `synchronous_core_lift.py` | 对原 lift 的七个几何 jets 和控制变分同步乘固定外部 $\lambda$；两个端点直接分支 |
| `m3_circle_trace_path_model.py` | 每个 $\lambda$ 新建 Flow/BVP 类和冻结工厂，固定 gauge/pscale，独立设置定义主幅值 |
| `prepare_q060_trace_path_entry.py` | 元数据绑定与未来唯一的零点身份、`.02` 初始入口诊断；禁止 BVP/native 尾 |

每个模型独立捕获其工厂和 lift 强度。旧实例及其缓存不随之后的全局工厂赋值改变；
不同 $\lambda$ 不共用 Flow/core 的参数缓存。
原生产源没有热修改。

正 $\lambda$ 核保留原 triangle、一阶及 C² 插值数值守卫、$\rho>10^{-5}$ floor
和 32768 网格上限；全域导数界没有以采样峰替代。
零点的原余弦构造器仍是原 $10^{-8}$ guard，路径包装器在它返回后
**额外要求同一个 $10^{-5}$ floor**。这是明确更强的入口过滤，
不笼统称零点全部 guard 字面不变。原 Frenet 域、残差、RMS、BC 与尾停止门不放宽。

## 原有限图与真圆弧 lift 的衔接

令 $I_\lambda$ 为原有限入口投影，
$H_\lambda=\Gamma_\lambda-b-.06\,B I_\lambda$。
参考图采用原 background 加 $\lambda a(s)\chi(s)H_\lambda$；
BC 仍要求 $Y(0)=I_\lambda$。
因此中间实际有限入口是

$$
(1-\lambda)\bigl(b+.06\,B I_\lambda\bigr)+\lambda\Gamma_\lambda.
$$

它一般不是严格的弧长曲线 $\Gamma_\lambda$。
定义核的 $\rho$ 和主矩关系不能直接充当这个有限入口的几何证书。
原 installer 在完整 lift 后写零的 `_inlet_metrics` 不能搬到中间态；
派生入口仅保留原未 lift 的投影诊断并明确 partial lift，不宣称零 metric。

$\lambda=0$ 完全不安装 lift 或积分核心参数包装器，
用原余弦构造器及原未 lift 的 `geo` 路径。
$\lambda=1$ 则调用既有完整 R44 lift。
中间所有 $h\,\delta H_\psi$、$h\,\delta H_{\psi\psi}$、对流项及
$-h'\delta H$ 都乘 $\lambda$，包括其中有限入口投影的 subtraction；
入口 `_initial_jac` 本身不乘 $\lambda$。
$p_0$ 继续对实际 partial-lift 函数作原中心差分。

平面 lift 没有补入垂直均值轨迹。
零点 mean-height 保留原 `height_integral` 定义与原完整物理多项式；
本次不重新积分该已有轨迹。
正 $\lambda$ 的 Frenet 速度均值会改变，之后必须按实际模型重新积分，
不能拷贝旧高度均值。当前诊断明确 `mean_height_reconstructed=false`，
普通 C² 入口修补也不等于完整 metric 审计。

## 唯一后续模型入口检查

零点身份先复用完整原物理多项式，保留所有 25 态及原系数。
在预声明原物理节点索引
`0,1,17,67,129,257,513,1025,1537,1933` 和 256 角上，
比较原 `geo` 加相同有限状态后的 `pos,p1,p2,s1,s2,sp,spp` 七组 jets。
检查完整 8 个 H，同时**另记**物理多项式末端再评价的 H 与保存的原 actual-tail H 的差；
不把两种末端浮点表示默认混为一物。
原 reader 的 Jacobian 是 dense JVP，而正式模型用既有 Fourier backend，
所以此处不要求两种 state-Jac 浮点路径逐位相同，也不重跑已登记 Jacobian 诊断。

随后只构造 `.02` 一个模型：按原 257 点加 profile breaks，
4096 角回投原完整 represented field，应用既有共享 C² inlet 修补，
显式重编码完整原实际 H，实际形成后才记录 8 分量差和哈希。
仍用原 collocation 节点/中点及原 RMS Lobatto 点域检查；
初始 BC 只用原真实 full-Jac response 的既有 affine slope 近似。
这不调用新的 native 尾，也不声称新 H 已被实际尾接受。

初始数组和已算 RHS/cubic 会保存在 scratch，失败阶段、原域异常和真实退出状态保留；
不自适应换 $\lambda$、步长、宽度或初猜。
下一次完整 BVP 必须另有明确入口及原所有终态门，本条尚未执行任何一项新模型检查。
