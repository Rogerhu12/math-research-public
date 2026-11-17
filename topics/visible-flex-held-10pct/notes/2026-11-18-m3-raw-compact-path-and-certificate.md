# m3 原始补弧控制路径与低维系数证书

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：精确定义、系数包围及初值数值接口；actual λ=.02 已启动，
此笔没有预先申领完整联立、metric、闭族或10%完成。

## 新路径的定义与旧路径的区别

令 n=3、T=2π/3、中心 φ₀=π/3，W 是原 C4 补弧 cutoff：
保护区 |φ−φ₀|≤a 上为0，宽度 ε 的转接之后为1。
记 e_j(φ)=cos(jnφ)，加权 Gram G_ij=avg(W e_i e_j)，e₀=1。
取 L=G_{0:2,0:2}，每个 j=2,…,M 定义

\[
(C_{0j},C_{1j})^\top=L^{-1}(G_{0j},G_{1j})^\top,\qquad
B_j=W(e_j-C_{0j}-C_{1j}e_1).
\]

新控制路径是

\[
b_j^\lambda=(1-\lambda)e_j+\lambda B_j.
\]

它在 λ=0 准确等于旧 cosine；每个 λ 都有均值零及主频零。
λ=1 时控制在保护弧恒零。高 support 矩在 λ>0 不再保持恒等，
而是随物理同伦变化；保持旧 c 数值不是保持旧完整物理曲线。

原 canonical 族是对 B_j 再乘高矩 Schur 矩阵 A 的逆，其中
A=2(G_high,high−G_high,low L^{-1}G_low,high)。W 在开区间严格
为正，非零有限三角多项式不能在那里恒零，故完整 Gram 与
Schur 补正定。A 可逆，所以 λ=1 的两族自由控制空间相同。
这里仅解释控制空间，不推断 BVP 或完整圆弧解存在。

每列的 C_0j,C_1j 只依赖 j 及低2×2块，不依赖最终截断 M。
因此增大 M 并追加零控制，在数学定义上精确保留完整原核心，
可以服务于后续真正固定 g 的加密；当前启动本身仍是新物理路径。

## 系数证书和原正性门

独立 `round_raw_lib/` 保留原 integral core、材料弧长反演、
参数 jets 与 exact lift。原库与 canonical source 未改动。
`complementary_moment_basis.py` 的 H_j 行为
[−C_0j,−C_1j,0,…,1_j,…,0]，没有高矩 A⁻¹。

`moment_interval_bounds.py` 用原有理矩区间（sin/cos Taylor、
π 区间）只包围 L。100位计算提供一个有理 inverse 候选 R，
精确有理残差 β=‖I−RL‖∞<1 给出
‖L⁻¹−R‖∞≤β‖R‖∞/(1−β)。再以区间乘法包围 C 两项。
所有原系数误差、完整 rho 导数界、rho>1e-5、最大32768点门
均保留；degree180 的矩余项强化也保留。该系数证书不是曲面
存在、连续完整 metric 或全相位 reach 的证书。

## 同一旧锚点的完整初值检查

固定 β₀=4.625/q=.040 旧接受核心的全部七个 c，a=.21、b=.08、
ε=.16。每 sector 32768 点检查完整合成控制，原 core 正性门
另按其自身三角/导数界运行。

| λ | 完整 core rho 下界 | 合成控制 rho sampled 最大绝对值 |
|---:|---:|---:|
| 0 | .671963970965 | .008030984087 |
| .02 | .670840560800 | .007870364405 |
| .1 | .667518965239 | .007368090410 |
| .25 | .661290973562 | .020870399465 |
| .5 | .650910987435 | .044572788025 |
| 1 | .630151015179 | .091991231309 |

这里全部只需512点便通过原完整 core 正性门；2×2逆证书的有理
Neumann residual 上界约4.78020269e-60。λ=0 与原解析核心的
F/F_u/F_uu/κ 最大差分别为1.48e-13/2.01e-13/3.44e-13/2.30e-13，
参数位置导数差4.68e-12。λ=1 保护弧内部 rho 与1+8q=1.32的
数值差为0，精确恒定来自控制的定义，不来自该采样零值。

这些初值比 canonical 路径的合成 rho 峰88显著温和，但不是
联立结果，.09199 也未满足 R32 的充分控制预算 .08。最终需看
实际求出的完整控制和 metric，不能只凭初始 rho 余量增大 λ。

## 实际入口与来源

`continue_round_core_raw.py` → `couple_m3_round_core_raw.py` →
原 actual TailMixin/原真实外层边界/最终 audit。原2e-9尾门保留。
本次从原 metric 良好的 q=.040 cosine prefix 出发，λ=.02、
M8/N128/depth8、parts16/steps16；尾初值是此前 parts16 已接受
的旧 H warmup，未借用 metric 失败 canonical 圆化态作锚。

输出显式保存 `core_control_path=raw-mean-primary-compact-v1`
和 `core_kind=exact_m3_raw_local_circle_integral_lift`；旧 canonical
loader 因而不能默默解释这些新系数。实际材料原点仍 u(φ=0)=0，
exact lift 仍是 (.5,.9)*prefix_end 上转接的 a(s)χ(s)H(ψ)。

源码/字面来源和变更在 `round_raw_lib/manifest.json`。可复现
screen 用 `screen_raw_round_core.py`；完整输入/来源hash、控制
参数和命令在 `raw_round_core_start_record.json`。actual终态另记。
