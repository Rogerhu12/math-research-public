# 只用实时间参考门支付真实相邻 germ cap

本结论放松旧 `2026-11-12-exact-germ-matching-and-cubic-caps.md` 的一项
充分条件。旧文先复合 Y 再在复时间盘取界，因此要求整个复时间像落进
物理场域；那个结论仍正确。本页先固定物理角取统一商界，再只在实时间
代入 Y，于是无需这项额外的复时间像门。

## 1. 固定物理角的三重零商界

固定同一个准确目标参数、真实根 t、时间坐标 \(\tau=c+hu\)、分支
及物理角。设相邻真实 scalar germ 的场 \(f_-,f_+\) 均在

\[
|u|<R,\qquad |\Im\theta|<S_\theta
\]

上联合解析，且对全部实部有 \(|f_\pm|\le M_\pm\)。两者在同一非转折
公共 knot 的真实 crossing \(u_*\in\mathbf R\) 有准确0、1、2阶
u-jet匹配。当前图的该性质来自：base/raw/shift/mean的 C⁴、height
primitive的 C⁵，以及带固定base权重和显式对称化的真实无限 R33 图；
从而 \(F\in C^4\)、\(E\in C^3\)、\(K_0\in C^2\)，完整真实物理场
在严格负曲率非转折接缝处为 C²。此处匹配对整个共同复角带成立。

因此

\[
f_+(u,\theta)-f_-(u,\theta)=(u-u_*)^3A(u,\theta).
\tag{1}
\]

令 \(\rho=R-|u_*|>0\)。**固定任意一个允许的复物理角**，在
\(|u-u_*|<\rho\) 对 A 用最大模原理。圆周半径趋近ρ时得到

\[
|A(u,\theta)|\le\frac{M_++M_-}{\rho^3},\qquad
|f_+-f_-|\le(M_++M_-)\left(\frac{|u-u_*|}{\rho}\right)^3.
\tag{2}
\]

因为最初的 M 对整角带统一，(2) 也对整个角带统一。这里没有出现 Y。

## 2. 仅在实 cap 代入同一参考

现在只要求：对所需的**实时间 cap**及完整初值标签带
\(|\Im x|\le S_x\)，同一有限参考满足

\[
|\Im Y(u,x)|\le I<S_\theta,\qquad
|q(u,x)|=|Y_x(u,x)|\ge m>0.
\tag{3}
\]

无需控制 Y 在其他非实时间点的像。将 \(\theta=Y(u,x)\) 代入统一
的 (2)，再用两小场

\[
g_\pm=(h f_\pm(u,Y)-Y_u)/q
\]

的共同 \(Y_u\) 准确相消，得到

\[
|g_+-g_-|\le
\frac{|h|(M_++M_-)}{m\rho^3}|u-u_*|^3.
\tag{4}
\]

若实际单侧 cap 长度不超过 \(d<\rho\)，则

\[
\boxed{E_{\rm cap}\le
  \frac{|h|(M_++M_-)}{4m\rho^3}d^4.}
\tag{5}
\]

同理一致点态误差为 \(|h|(M_++M_-)d^3/(m\rho^3)\)。若跨过多个
公共 knot，逐**相邻** germ telescoping 后把 (5) 相加，不能跳过
近邻 binary knots 形成的极短中间 span。时间 h 的正负保留在定义中，
费用里使用 \(|h|\)。不可再次乘 h，亦不可再次除 q。

该 cap 费用同时进入 R72 的误差积分 E 和共同大小积分 A 的预算。
它不支付 main-germ 的有限场截断误差、密度误差或真实流误差。
真转折只用同一根芽的 Q 消根表示；本页没有把 ordinary C² 接缝论证
外推到退化根。

## 3. 从已有整段 q 模界直接取得实时间像

若已证明对全部实时间、全部标签带 \(|q|\le Q\)，而 Y 对实标签实，
则沿竖线积分给出

\[
Y(u,x+iy)-Y(u,x)=\int_0^y iY_x(u,x+it)\,dt,
\qquad |\Im Y(u,x+iy)|\le |y|Q.
\tag{6}
\]

因此 \(S_xQ<S_\theta\) 即足够支付 (3) 的像门。更紧的实际
`real_time_image` 也可直接代入，不需要把复时间 Taylor 单项式系数的
总模加到实时间像上。

## 4. 完成的 prefix203 实际误差

输入固定为准确 δ₅、descriptor
`097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052`。
已冻结的 domain snapshot覆盖前腿0–202，共203段、203个完整leaf，
有119个真正相邻 ordinary crossing 对。其字节闭包已独立检查：
278个direct germ证书、48条继承边、227个依赖文件，无缺失时间分区。
这不是完整前腿550段，也不是两腿证书。

独立完成的全前腿 q 报告
`notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz`
SHA
`87aeff7e8824c7d6301c6f33cbeea506e584004c5bee1591512a556348cbfd8c`
覆盖全部550段的实时间及标签带1/512。新源码逐段重聚合保存的有向
q界，核对所有时间、manifest、source、准确 coefficient shard 哈希，
并采用简单严格常数

\[
m=3/100,\qquad Q=21/20,\qquad
I=S_xQ=21/10240<1/64.
\]

已实际计算得到这203段的总 raw field cap 积分小于
\(2.110408087081\times10^{-36}\)。代入同对象已证 m 后，新的实际
small-field cap 报告给出

\[
\boxed{\sum E_{\rm cap}
 <7.034693624\times10^{-35}}
\quad(S_x=1/512).
\tag{7}
\]

这是已付清参考门后的实际 cap 误差，不再只是“以后除 q”的条件数。
报告是
`data/phase_ring_continuation/type_fixed_step02_d5_step5_real_time_actual_cap_prefix_0002.json.gz`。
S=1/256的更宽实时门正另行完整扫描；不能把 (7) 的带宽直接翻倍。

## 5. 主流水线接口

新源 `scripts/fourfold_phase_real_time_cap_budget.py` 提供：

```python
ledger = real_time_reference_cap(field, reference, image_gate, q_gate)
```

field为实际 `UnifiedScalarTimeCircleField`，reference为准确
`CompleteReferenceSegment`。函数核对同descriptor、目标、真根、分支、
准确PiTime端点及subspan；两个参考门须同标签带且覆盖该准确参考段。
随后检查实际根包的 C⁴/C⁵ 输入和 main germ 等于实际时间中心所属芽，
输出：

- `integrated_density_cap_error_upper`：已含 \(|h|/m\) 的 (5) 总和；
- `uniform_density_cap_error_upper`：同一完整域上的点态误差总界；
- 全部真实 crossing、相邻芽、cap长度、公共解析半径与输入身份。

旧条件 cap report、旧较强充分条件的证明和所有冻结哈希保持原样。
新接口只免去不必要的参考复时间像条件；真实场的共同复时间域仍是
(2) 的必要输入，不能因此省掉R65全域。
