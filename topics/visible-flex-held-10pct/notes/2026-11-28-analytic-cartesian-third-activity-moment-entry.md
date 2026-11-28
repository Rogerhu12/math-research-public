# 同一真实 Cartesian 图的三阶活动矩：连续区间入口

日期：2026-11-28。状态：**推导与独立入口准备完成；尚未执行实际矩积分。** 沿用 [R6](../results/R6-threefold-markers-and-strict-noncongruence.md) 与 [R67](../results/R67-universal-threefold-marker-and-euclidean-noncongruence.md) 的已证判据。本条补的是当前真实 R53 Cartesian 图的数值系数入口，没有重证非全等引理、没有构造未返回的尾，也不以准备源代替完成结果。

已查旧 `resume_closed/certify_moments_and_hold.py` 与 `finite_core_moment_exact.py`：前者认证旧有限图的二阶轴矩与双重标记，后者针对有限 cosine-support 核的四极矩；它们不包含本次实际 R53 核、完整 core lift/center repair 和三阶活动矩的这个入口。

## 1. 精确待积量及方向

取未插柱、未加固定帽的同一上半 Cartesian 图

\[
X(s,\psi)=(x,y,z),\qquad 0\le s\le s_c,
\]

外法向有向面积采用现几何证书相同的 \(X_\psi\times X_s\)。令 \(w=x+iy\)。上、下反射前缀的实三阶活动通量为

\[
A_{3,p}=\int_0^{s_c}\!\int_0^{2\pi}F(s,\psi)\,d\psi\,ds,
\quad
F=2z\,(x^3-3xy^2)\,(x_\psi y_s-y_\psi x_s).
\tag{1}
\]

这里的 2 来自下半反射片；与后面的三重扇区因子 3 分开计算。式 (1) 在闭图尚未成立时仅称为该真实前缀的有向通量，不称完整区域的体积矩。相应全图解释仍须同图闭合、方向及嵌入条件。

同一完整图在 \(s=0\) 的实际核边界给

\[
\Re m_3=\int_0^{2\pi}G(\psi)\,d\psi,
\qquad
G=\frac15(x^3-3xy^2)(xy_\psi-yx_\psi)\big|_{s=0}.
\tag{2}
\]

这是 R6 的平面边界公式，用当前核的真实材料角参数表达。入口同时报告原点有向面积行列式的全角下界，但不重证 R53 核的闭合/凸性。只认证实部；没有假定虚部为零。实部区间排除 0 已足以证明相应复系数非零。

## 2. 完整三 jet 足以支付两个误差项

记 \(L=2\pi/3\)，扇区均分宽度 \(d=L/N\)。完整字段有精确三重协变关系 \(X(s,\psi+L)=R_LX(s,\psi)\)。因此 \(z\)、\(\Re(w^3)\) 和水平行列式都为 \(L\) 周期标量，式 (1)、(2) 可以在一个扇区积分后乘 3。

每个径向叶 \([a,b]\) 必须位于一个真实公共 Hermite 区间，并在中心修补、cut 修补与原 profile 的各接点分开。令 \(h=b-a\)、\(c=(a+b)/2\)，定义

\[
T_{a,b}=h\,d\sum_{j=0}^{N-1}F(c,jd).
\]

取完整闭盒上的真实区间界

\[
R\ge\sup_{[a,b]\times[0,L]}|F_{ss}|,
\qquad
B\ge\sup_{[a,b]\times[0,L]}|F_{\psi\psi}|.
\]

逐角应用径向中点余项，及在 \(s=c\) 应用周期复合梯形余项，给

\[
\left|\int_a^b\!\int_0^L F-T_{a,b}\right|
\le \frac{Lh^3R}{24}+\frac{hLd^2B}{12}.
\tag{3}
\]

第一项可由 \(F\) 在中点的一阶 Taylor 式与二阶积分余项直接积分得出。第二项是每个角盒的线性插值余项积分 \(d^3\sup|F_{\psi\psi}|/12\) 相加；周期性使首、末半权合成同一个节点值。没有新 Gauss 节点、有限差分导数或采样最大值。

式 (1) 只含 \(X,X_s,X_\psi\)，所以其任一纯方向二阶导数只需总阶至三的场导数。原 `D2` 乘法法则计算全部项，包括混合项；使用真实完整 box 三 jet 求上界。对分片 \(C^2\) 图，只需每片二阶 integrand 导数有界、一次导数绝对连续。公共两 jet 与逐片拆分保证接点无额外跳跃项；不假设整个图跨所有接点为 \(C^3\)。

核矩同样有

\[
\left|\int_0^L G-d\sum_{j=0}^{N-1}G(jd)\right|
\le \frac{Ld^2}{12}\sup_{[0,L]}|G''|.
\tag{4}
\]

所有节点值本身也用原向外区间包围，权重 \(h,d,L\)、求和和余项均用同一已核区间内核。真实 \(\pi\) 不替换为浮点中点。公式中的全部扇区误差最后乘 3。

## 3. 字段复用与完整覆盖

独立入口为 `scripts/resume_20261128/analytic/cartesian_third_activity_moment.py`。它从已审的 `NewMetric.evaluate` 或 `CutMetric.evaluate` 原样取出 field 闭包，保留其全部系数、core lift、center 修补、真实有限均值与可选完整 cut；只把最后的 Gram 输出改为返回 \(X,X_s,X_\psi\)。在独立 namespace 编译，不修改旧模块或任何接受门。原函数源码和生成函数源码 SHA 都进入报告。

原 `CutMetric` 的自身证书只扫描末端 cut 条带，其 `grid` 因而被截短。新积分入口明确重新取**整个** `field.x + target.grid + center_width + cut_start`，并在结束时检查真实 \([0,s_c]\) 无缝且恰覆盖一次。不能把只积末端条带的结果误称整个前缀。

没有 bundle 时只使用原真实前缀。附 bundle 时沿原完整 cut 合同保留尾的全部 planar/height 高模及均值零模处理，不用原前缀谱截断尾。原设计与真正耦合来源分别调用原 `NewMetric/CutMetric` 和已审 `CoupledNewMetric/CoupledCutMetric`；不替换 `accepted_original`。耦合输入必须用最终 physical endpoint 的完整 H 绑定，不偷换 raw candidate。当前 physical 文件 SHA 从当前已验文件读取，并与实际来源再核一致。

报告绑定完整源 run、物理文件、定义两 jet、三 jet 角表、所有构造源和目标度量。原 finite mean 始终取该图自身的 mean。不同图须重新计算自己的矩，不能搬已有场的系数。

## 4. 与短柱及未来真实尾的接口

R67 的 \(\ell\) 是**总柱长**，与 R6 中上下各移 \(\ell\) 的半长记法不同。已有公式为

\[
A_3(\ell)=A_3(0)+\ell m_3.
\]

当前入口仅报告 \(A_{3,p}+\ell\Re m_3\) 在 \(\ell=1/200,1/100\) 的两个区间；尾贡献仍缺，不选择完整图的实际柱长，不声称 \(\delta_E>0\)。若真实 \(m_3\) 的认证区间包含 0，这不排除 R67 的某个更高 \(3j\) 阶矩非零；本入口不虚报一个已认证阶数。

未来若同一完整尾已经支付正的投影 Jacobian、全局投影单射、实际半径图身份 \(r=R\)、\(|z|\le Z\)、\(r_{xy}\le r_*\)，则两个反射尾的粗界可用

\[
|A_{3,\mathrm{tail}}|
\le 2Z\int_{r\le r_*}r^3\,dA
=\frac{4\pi Zr_*^5}{5}.
\tag{5}
\]

投影单射不能只由局部正 Jacobian 代替；否则可能重复覆盖，圆盘面积粗界不足。\(r=R\) 是复用当前真实尾证书的图身份合同，不能用只读预检取代完整 bundle 验证。式 (5) 的函数已保留为显式条件接口，但本命令不会在没有这些实际证据时调用它或输出伪造尾数值。

## 5. 当前可复核范围

两个原 field 返回版本已实际完成源码提取及编译，旧区间代数 SHA 门通过。没有构造任何实际 source 模型、没有读取角表数组、没有执行矩积分，也没有 J 或 BVP。

入口 SHA256：`fef214b4b49efb77e4493886431ec125553f842be7a13c3dadd357c0a9a9002e`。配套 JSON 保存完整编译记录。将来真实运行命令形式为：

```text
python scripts/resume_20261128/analytic/cartesian_third_activity_moment.py \
  --tables ACTUAL_SAME_FIELD_ANGULAR_REPORT \
  --outdir FRESH_EXTERNAL_DIRECTORY
```

真正耦合来源另加实际 `--coupling-summary`；只有真实完整 H 的 bundle 才可另加 `--bundle`。这些占位命令没有被冒称执行。全部闭图、全活动系数、欧氏非全等和完成标记保持 false。
