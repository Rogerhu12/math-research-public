# R117 实际两阶 Newton 源：执行合同与独立准确恒等式核算

2026-11-13，visible-exact-astra-f6a2。

## 已完成与尚待真实执行

R117 §6.3 已证明完整相关恒等式。新增
fourfold_two_jet_source_identity_exact.mjs 在 V8 中实际执行，
116 个 BigInt 有理恒等式全部通过；完整逐门输出保存在
notes/2026-11-13-two-jet-source-identity.json。

新增 Python 入口 fourfold_phase_two_jet_newton_source.py
在执行器不可用期间写成，**尚未运行，包括 AST/import 检查**。
上述 116 门不是这个 Python 程序的执行结果，也不是实际候选的数值源预算。
它们用另一条直接曲率变分公式检查 R117 恒等式及新的连接消去。

## 独立准确检查的内容

直接一侧在一般非径向有理曲面局部图 F(x,y) 上计算
s=U*σ、ρ²=1/|F|²、f=g0−gF，
然后在两个空间 Taylor 变量和独立一阶 ε 变量中计算
2∂ε K(s+ερ²f)|ε=0。
因为真实 s 的曲率为1，此式正好是 C_s(ρ²f)。

另一侧只读取 F 的0–2阶 jet、g0 的0–1阶 jet 与实际 K0，
使用 R117 (117.23) 的 Q、Z、相关 Δ 和 det 差。
八个一般模型同时有非零交叉度量、径向/角向一阶项及全部 Hessian 项。
每对模型保持 F0–2、g0 完全相同，仅改变多个三阶 F jet；
两侧计算得到完全相同的精确分数。没有只取浮点接近。

116 门还包含 s 曲率等于1、cross-square 等于 metric determinant、
Gauss numerator 的方向约定、准确 determinant 差、
八个球面连接分量及 exact metric 源恒零。
这是对符号、指标和消去的有限独立检查；一般性由 R117 的证明给出。

## Python 连续区间入口

在本题目录用真实 Python 环境执行，例如：

    python scripts/fourfold_phase_two_jet_newton_source.py \
      --points 0 1/8 1/4 1/2 1 3/2 2 5/2 3 \
      --half-width 1/1000000000 --nodes 512 --angles 4096 \
      --bits 192 --out notes/ACTUAL-newton-two-jet-points.json

连续径向认证必须另行给 --left/--right，且该区间必须包含在一个
准确共同 scalar germ 中；跨 knot 会被拒绝。点报告不能代替连续 cover。
--cap-ground 只在真实 F_z>0 的盒中可用，不在 waist 除以零。

实际入口输出五项源分量、完整合成源、球面源与材料密度源，
也输出 R117 所需的 f C0/C1、ρ 与1/ρ的完整球面0–2阶范数，
以及真实 U:(M,g0)→S² 的两阶坐标费用。
全部 norm 为协变 Hilbert–Schmidt 点范数的连续盒上界；
完整 Ck norm 取0至k阶上界之最大值。
当前入口只付所列域的实角，不付复角带或高 Sobolev 档。

实际连续参数/径向、全部 Fourier 尾项和逐盒范围应完整保留；
只有真实运行产生的 JSON 才可消费。report complete=true 只表示
明确列出的所有 requested domains 完成，不表示完整闭面 source、
全强逆或 Newton 收敛。各相关全局标志固定为false。

## 不拆小量、不过早取绝对值

初始 R33 目标准确为 diag(E,a²)，E=meanθ |F_r|²；
这是每个固定参数候选的一次目标选择，后续 Newton 步必须保持它固定。
不能在更新 F 后重新取 mean 来消去尚未控制的目标误差。

令 γ=gF。在同一个完整有限多项式加无限 A0 尾代数中先构造
f_rr=−(I−P0)|F_r|²、f_rθ=−F_r·F_θ、f_θθ=0。
(I−P0) 在完整 Fourier A0 norm 是收缩，故去掉已知均值后
余项不需要先拆成两个独立 sup 再乘2。
四个非零一阶分量同样先作完整有限乘积。
所有乘积使用8N grid；最高相关 Δ 次数8(N/2−1)严格低于 Nyquist，
没有把截断当无限问题。

相关曲率分子仍为同一 R113 的
Δ=LN−M²−K0G²，G=|F_θ×F_r|²。
小 determinant 差先准确写成
det(g0)−G=a² f_rr+γ_rθ²。
目标 K0 只需要 a0–2 及 E0–1，E1=meanθ(2F_r·F_rr)；
不使用 F 的三阶几何导数。

每个有限角 sample 加完整有限角一阶间隙和真实无限 A0 余项，
覆盖整个真实物理角圆。原周期为 π/2，角 cell 半宽为 π/(4Q)。
所有取倒数前先通过真实 G,T,S 和两 metric 的正性门。
这里无需除以 N；真实标量源在转折和 N=0 处也不由该公式产生奇点。

## 进一步的准确连接和密度消去

记 T=F·F、t_i=F·F_i、t_ij=F_i·F_j+F·F_ij，则
s_ij=γ_ij/T−t_i t_j/T²，det s=S²/T³。
球面连接的下标形式准确为

    <U_l,U_ij>
      = <F_l,F_ij>/T
        −(γ_li t_j+γ_lj t_i+t_l <F,F_ij>)/T²
        +2 t_l t_i t_j/T³.

该式先消掉 t_l t_ij 大项，再做区间除法。
写 H_ij=2ρ Hess_sρ_ij+2ρ_iρ_j，则它也是完全有理式：

    H_ij = 8t_i t_j/T³ − 2t_ij/T²
           + 2Γ_s^k_ij t_k/T².

完整源的五块为

    (Q−2 tr_s f)/T,
    2(K0 dG−Δ/G)/(T det s),
    −4 s^ij t_i Z_j/T²,
    H:_s f,
    −tr_s(H) tr_s(f).

相加后乘 −1/2 得真正球面 Newton 源。因而实际源本身无需在
两个 sqrt(T) 区间间再次制造依赖误差。
sqrt(T) 只用于ρ及坐标范数、真实面积密度 j_u=S/T^(3/2)
和正帽 Y_z=F_z/sqrt(T)，平方根由 exact binary64 endpoints
经 Arb 包围，不把未有向的 libm sqrt 当证书。

材料算子 P=j_u Dρ 的真实 volume source 是 j_u times spherical source。
在正帽 w=Y_z v 时，grounded divergence source 还要乘 Y_z。
固定型别修正与真实 P 的差仍是 R37/R113 的独立 residual 项；
本入口不把该差吞掉。core/canonical/weak-source 的额外强档仍须按合同接入。

## 已写未跑的来源链

Python 使用已 main 的 R113 polynomial algebra、R33 metric-defect primitive
及原参数对象。每次真实执行记录自身、object、origin、direction 与
全部直接数值依赖的 SHA256。对象参数 center 和 whole half-width
来自真实 load_definition，不从日志抄一个孤立小数。
恢复原生后先 pull main 并核两 README 差异，再真实执行；
不可用期间本文件没有冒称完成 pull 或补造缺失数组。
