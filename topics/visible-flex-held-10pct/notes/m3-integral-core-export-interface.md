# m3 积分中心的单次 reference lift 导出接口

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

## 1. 结论范围与输入

这里补齐 `resume_m3/couple_m3_round_core.py` 到闭图导出的表示接口。
新生产读取器只接受原 `accepted_anchor` 全部门槛通过、带
`core_round_settings`、`core_round_sources` 与
`config.core_kind=exact_m3_local_circle_integral_lift` 的 checkpoint。
它逐项保留实际 `parameters[1:]*central_correction_scales`，核对原 source hash、
物理前缀/尾部参数和材料区间，并重新安装同一个积分 core 与同一个
`exact_core_lift`。没有运行 BVP 或实际尾 shooting，也没有降低任何接受门槛。

**这不是新的 accepted 圆化解、全闭面或连续误差证书。**
本次执行只使用明确标为非解的代数探针：有限未知量取常数 inlet projection，
平均高度取 `s`。它不满足完整 Frenet 或尾边界方程，不冒充某个失败 checkpoint
的修复。实际生产读取器在本条登记时尚待第一个 accepted 圆化 checkpoint。

相关文件：

- `scripts/resume_closed/m3_integral_prefix.py`：读取及有限表示；
- `scripts/resume_closed/audit_integral_prefix.py`：只接受实际 accepted 输入的导出/数值审计；
- `scripts/resume_closed/probe_integral_prefix_interface.py`：非解的接口探针；
- `scripts/resume_closed/integral_prefix_interface_execution.json`：执行命令、来源与输出 hash。

## 2. 为什么旧有限 Fourier core 读取器不能直接复用

新的 source `Flow.geo` 已加入

\[
 f(s)H(\psi),\qquad f(s)=a(s)\chi(s),
 \quad H=\Gamma(\theta_0(\psi))-e_r(\theta_0(\psi))-qV_{\rm init}(\psi).
 \tag{1}
\]

它同时给出 `pos,p1,p2,s1,s2,sp,spp` 中相应的全部导数。
`theta0` 来自原 `Flow.angular`，不是把随 `s` 变化的角图重新带入 `H`。
`chi` 的窗口为 `(.5,.9)*Flow.prefix_end`；这里的 `prefix_end` 是物理
循环前缀末端，不能换成完整 bridge 末端 `Flow.end`。

旧 `M3CartesianPrefix` 是从圆背景的 Bessel 系数和有限未知量显式构造 Cartesian
系数，不调用 `Flow.geo`。若直接把它套在新 checkpoint 上，(1) 会整项遗漏。
另一方面，在原 `Flow.geo` 导出值上再次加 (1) 则会重复加入。
新 integral core 的 `coefficients` 与 `frequencies` 只是参数标签，不能用旧
有限 Fourier support 公式计算它的真实 `rho_phi` 或第三角导数。

## 3. 新表示和接缝恒等式

令 `C(s,psi)` 为旧构造给出的有限 Cartesian Fourier / 共享二阶 jet 五次式，
其中不含 (1)。将 source 的 `f,f',f''` 在同一组径向节点取值，定义唯一共享
二阶 jet 五次式 `f_*`，并加入两个 source cutoff 端点。新代表元为

\[
 X_*(s,\psi)=C(s,\psi)+f_*(s)H(\psi)
       +\sum_{j=0}^2 h_j^L(s)\Delta_j(\psi)
       +\text{cut lift}.
 \tag{2}
\]

`H` 在 (2) 中出现一次。源数值表达的乘法次序也保留：
`span=(.9-.5)*prefix_end`，而不是先算两个端点再相减。
右端共享节点取 `nextafter(.5*prefix_end+span,+inf)`，因此 source 的
`clip` 在该点已经严格输出 `1`，三个 cutoff jet 都为字面零。
这里增加一个向外 ulp 的节点只决定有限代表元；它不是新物理 metric 参数。
`f_*` 与 source 的 `f` 之间仍须纳入后续近似误差预算。

中心目标函数使用同一个真实积分曲线 `Gamma`。写

\[
 \rho_\theta=1-E_0\cos3\psi,\qquad
 b=-E_{ss}(0)\sin(3\psi)/3.
\]

中心的径向目标二阶 jet 是

\[
 J_0=\Gamma(\theta(0,\psi)),\quad J_1=e_z,\quad J_2=b\Gamma'(\theta(0,\psi)).
 \tag{3}
\]

关键扣除项为

\[
 \Delta_j=J_j-\partial_s^j C(0,\psi)-f_*^{(j)}(0)H(\psi).
 \tag{4}
\]

(4) 对 **已经包含一次 reference lift 的完整 raw 表示** 做补缝，因此不会把
`Gamma-circle-projection` 再加一次。它对整角函数而非有限角网格定义。
`h_j^L` 是原共享 Hermite 端点基，故中心二阶 jet 恰为 (3)，同时中心条带右端
全部二阶 jet 为零。尾部目标仍可用原 `TailCutTarget/CartesianCutLift`，因为
`f_*` 和中心条带在完整前缀末端都带二阶零 jet；此处没有把旧尾数组移给新 checkpoint。

若 `rho=du/dphi`，弧长曲线满足

\[
 \Gamma'=T,\qquad\Gamma''=-n/\rho,\qquad
 \Gamma'''=-T/\rho^2+n\rho_\phi/\rho^3.
 \tag{5}
\]

新接口的中心角二阶导数由 (3)–(5) 计算，其中 `rho_phi` 来自实际
`Core.rho_material_jets`；没有将 nominal support 参数解释成真实 Fourier 系数。
例如

\[
 \partial_\psi^2(b\Gamma')
 =b''\Gamma'+(2b'\rho_\theta+b\rho_\theta')\Gamma''
      +b\rho_\theta^2\Gamma'''.
\]

对于数学上精确定义的 `Gamma`，(2) 的共享径向五次式和完整角函数 Hermite
恒等式给出字面的 `C^2` 代表元。若 `Gamma` 三重协变，则 finite Cartesian
频率 `1 mod 3`、三重高度频率、`H`、(3)–(4) 和两种径向 lift 都保持同一协变。

必须区分这个代数声明与运行中的浮点评估：曲线的数学定义使用
`core_round_settings` 指定的真实积分、均值修正和 canonical moment 系数；
source 用 Gauss 求积、高精度系数转 binary64 和弧长反函数迭代近似它们。
这些误差尚未由本接口认证，不能把 source 的数值函数直接等同于精确曲线。
R31 的旧 cos3 小幅 core 证书没有迁移到这里。

## 4. 本次非解探针实际检查了什么

探针使用 `q=.085,lambda=1,M=8,N=256`，完整 complementary controls 为零，
采用已登记 source 的真实 `Flow.geo` 安装链；有限径向代表元有 148 个共享节点。
所有比较都是浮点接口诊断。结束码为 `0`。

直接比较 source 已加项与 (1) 独立展开的七种 jet，最大差分别为：

| source 字段 | 最大数值差 |
|---|---:|
| `pos` | `1.3985106024881918e-16` |
| `s1` | `3.5261066962547e-16` |
| `s2` | `6.333464698866285e-15` |
| `p1` | `2.4610717239706577e-16` |
| `p2` | `1.009880263425834e-15` |
| `sp` | `1.6049767423942351e-15` |
| `spp` | `9.405506235314741e-15` |

这次 reference 本身不是近零探针：它的 `pos` 大小约 `4.190109e-5`，
`p2` 大小约 `.0614745`，`spp` 大小约 `.673127`。
因此整项遗漏或重复加入会被这个检查识别。
完整 raw finite/source 共享节点六 jet 比较的最大差为 `2.006281e-14`。
中心 `X=Gamma,Fs=e_z,Fss=0` 三个恒等式数值差分别为
`6.662784e-16,0,4.720733e-15`。
右 cutoff 及其后全部共享节点的 reference 二阶 jet 均为字面零。

另外，探针观察到 source `Flow.angular` 的 inlet 参数为 `.68`，而随 `s` 的
数值 spline 在中心给出 `E0=.6800000000000002`。新接口分别保留它们：
前者定义原 source `H`，后者定义有限闭图的中心材料图和 (3)。没有静默把两个
浮点值认成同一个参数；(4) 也支付这个中心接缝差。

## 5. 实际 accepted 输入后的使用

`audit_integral_prefix.py` 保留原接受门槛，核来源后导出完整共享数组和 core 参数，
比较 source reference 只出现一次、raw/完整有限代表元差、中心及可选尾接缝、
新代表元自身的 metric/曲率等有限采样。
可选尾输入必须同时给出 `--tail-manifest --tail-reader --cap-source`，并来自
同一实际 accepted 尾。没有尾输入时只导出前缀。

后续仍须完成同一物理输入的真积分 core/反函数误差、真积分全局 `g` 口径、
完整尾的共同二阶 jet、全角/全相位连续 metric 及全闭几何界。
本接口既不将 R32 的条件预算当作存在证明，也不将新的设计延拓当作固定 `g` 收敛。

## 6. 主会话读取器复核

实际 checkpoint 的系数可能存于原 `pp_coefficient_chunks`。生产 loader 经只读代码审查改为在全部来源/物理身份核对之后调用原 `curve_stable_prefix_bvp.load_checkpoint` 解码，再构造 PPoly；不把 gzip 元数据当成完整场数组。上述非解 probe 没有走生产 loader，执行时与修订后的 source hash 在 execution record 中分列。此修改不触及 probe 使用的参考项/中心两jet公式，未重复运行 probe；第一个 accepted 积分核心 checkpoint 出现后仍须端到端验证，当前不提前认领。
