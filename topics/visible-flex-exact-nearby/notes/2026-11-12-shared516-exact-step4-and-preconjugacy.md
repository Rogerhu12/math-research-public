# 共享 516 图、准确 H 更新和预共轭费用

状态：实际射线、有限 Newton 和预共轭范数代理是**浮点数值证据**；新 dyadic $H$ 的逆导数预算是 R48 方法的**准确有限多项式证书**。这里未证明真实共轭、PDE 逆或闭曲面。

## 同一第三点的两个完整网格

固定准确 $\delta_3$ 对象 e6ff2d46...、自己的根 afdc964a...、同一 dyadic $H_{129}$ 028a9567...、Q=256、rtol $2\cdot10^{-12}$：

| 积分方式 | RHS | 归一角最大共轭误差 |
|---|---:|---:|
| 12 组，每组 43 条，knot 分段 | 204003 | $2.101803566745275\cdot10^{-7}$ |
| 全部 516 条共享时间网格，knot 分段 | 21540 | $2.1017385876120898\cdot10^{-7}$ |

共享计算两支各 550 accepted steps，记录约 1498 秒。两图逐节点最大差：物理返回角 $7.400302592941443\cdot10^{-12}$，$J$ 为 $1.4764456324201092\cdot10^{-10}$，物理参数列 $7.670573161019933\cdot10^{-14}$。这些差值不是有向 ODE 误差。

完整 endpoint 报告分别为 2026-11-12-D5-exact-affine-step3-knot-Hnodes516.json（SHA256 118239ce6fa60c1363e65ae15759dc5c2aee11115ecea43349c4ec9476f40791）和 2026-11-12-D5-exact-affine-step3-shared-knot-Hnodes516.json（SHA256 3ba4ca28b138a63ca9fe3ce6202e393ab33cc7d5b15063a7580902458085278b）。shared 加权误差均值为 $-2.151392554507342\cdot10^{-8}$，加权参数列均值为 $0.002307172234745314$。

大 dense 文件保留本地，并在冻结 manifest 中保存每件 SHA、大小，默认不提交这些可重做的中间轨道。R61 若使用新定义的准确参考，只需保存那份参考自身的准确系数与验证输入。

## 第四个准确参数点与整数 H 更新

从 shared516 同一张实际图的值、$J$、参数列作 finite Newton，得到
$$
\Delta\delta=9.324830882778994\cdot10^{-6},\qquad
\delta_4=-\frac{7789866024620307}{4611686018427387904}.
$$
其 decimal 为 $-0.0016891579334528714$。新 step4_object.json 的 SHA256 为 87566dee6e119bb4127200c2dae38f9cdf692a18475c1cde23961a56605919b5；仍是同 origin 0d17500a...、同 direction 8db5d57d... 的准确 affine 族，没有新 rounded 控制点图。

有限矩阵条件数约 1999.07、线性残差 $2.3227231600489017\cdot10^{-21}$。$H$ 校正采样最大值 $5.215166907141349\cdot10^{-7}$、$H'$ 校正采样最大值 $3.0144100960372862\cdot10^{-5}$。这些不是非线性接受条件。

新 exporter 直接读取旧 $H$ 的准确整数，把每个 binary64 小校正作为准确 Fraction 相加。实 Fourier 校正 $c_k\cos kx+s_k\sin kx$ 给正频率加入 $(c_k-is_k)/2$。旧常数保留；不再经过 sample FFT 重定义 H。最后按 $2^{-120}$ 量化，本次所有和恰能被该分母表示，所以 $C^0,C^1,C^2$ 系数舍入预算的准确分子全为零。这不消除有限 Newton 或 ODE 误差。

再以浮点采样选择 $q$，用 R48 的准确整数卷积、有理指数主项和 Neumann 级数证明：

| 归一角带宽 | $\|H'\|$ 上界 | $\|1/H'\|$ 上界 |
|---|---:|---:|
| $1/512$ | 2.359265552697352 | 3.4241573460179358 |
| $1/128$ | 2.4463265090932262 | 3.5200103211557954 |
| $1/32$ | 2.972904244730295 | 4.026242499406976 |

所有五个测试带宽都通过，实圆上 $H'>0$。物理角带宽除以 4，导数范数不变。实际新 H 是 type_fixed_step02_d5_exact_affine_step4_dyadic_H.json（SHA256 8bd6078f8c442b48bab2b15850b99e2455d616ab48e687abb22114a1f1bfe39b），**不是**同前缀 H_float_export.npz。预算 SHA256 为 4129939803e93cef2c26ec1817540d258bb7953d0ea21313e2b51eaafe070ba0。

生成次序：先用 frozen fourfold_circle_exact_affine_newton.py 输入 shared516 report、step3 object、step3 dyadic H，输出 Newton516-step4 report、step4 object 和辅助 H_float_export.npz；再运行：

    python scripts/fourfold_circle_exact_correction_budget.py \
      --newton-report notes/2026-11-12-D5-exact-affine-Newton516-step4.json \
      --base-polynomials data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_dyadic_H.json \
      --polynomials data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_dyadic_H.json \
      --out notes/2026-11-12-D5-exact-affine-step4-H-Wiener-budget.json \
      --bits 120 --inverse-degree 512 --width-denominators 512 256 128 64 32

## 固定 H 预共轭费用

本比较仍在已完成的 $\delta_3,H_{129}$ 点，令 $G_p=H^{-1}R_pH$。实轴浮点逆方程残差至多 $1.78\cdot10^{-15}$；复域局部逆由 root 的 R63 单独支付。实际公式为
$$
G_p=\frac{R_p(H)}{H'(G)},\quad
G_{xp}=\frac{R_{xp}(H)H'(x)-H''(G)G_pG_x}{H'(G)},\quad
G_{pp}=\frac{R_{pp}(H)-H''(G)G_p^2}{H'(G)}.
$$
八条实际二阶射线给采样最大值 $|G_p|\simeq.004364721$、$|G_{xp}|\simeq.011292903$、$|G_{pp}|\simeq.000137263433$。八点实际 $G_{xp}$ 与完整参数列的 Fourier 导数差约 $7.78\cdot10^{-10}$，实际 $G_p$ 与 shared516 相同节点差约 $1.07\cdot10^{-12}$。

下表是宽度 $S=1/128$ 的**有限三角插值多项式范数**，没有 alias/ODE 误差保证：

| 坐标 | $P$ 代理 | $Q$ 代理 | $B$ 代理 |
|---|---:|---:|---:|
| 原返回图 | .0104980 | .141119 | 106.702 |
| 固定 H 预共轭 | .00728053 | .0323316 | .00959456 |

取 R31 的 $s_0=1/512$、$\delta_0=s_0/8$。原坐标使用已证 $M_0,R_0$；预共轭从 id 起步，$M_0=R_0=1$。$T$ 尚无连续界，只作假设场景：

| 假设 T 是相应八点最大值的倍数 | 原坐标 epsilon 门 | 预共轭 epsilon 门 |
|---|---:|---:|
| 1 | $7.2594\cdot10^{-18}$ | $3.8320\cdot10^{-13}$ |
| 10 | $7.2587\cdot10^{-18}$ | $2.7729\cdot10^{-13}$ |
| 100 | $7.2522\cdot10^{-18}$ | $7.3670\cdot10^{-14}$ |

这是费用比较，**不是通过的 KAM 门**；八点最大值乘 10 或 100 也不会自动成为连续上界。完整来源、插值和假设在 2026-11-12-D5-exact-affine-step3-preconjugacy-cost.json；重做用同名 fourfold_circle_preconjugacy_probe.py，输入 shared516 report、second-parameter-rays8、step3 dyadic H 及其 H-Wiener-budget。

## 第四点的实际验证正在运行

numerical 已给 $\delta_4$ 自身的 tight root：step4_root_tight.json，SHA256 03a0863733b25b6c4058a39590648dda2292a2943e783021747e3bc3f27c86f4，中心 $0.2383968742995617$，未移用第三点的根。新的 1032 条共享图已启动，live 输出不属本次冻结包：

    python scripts/fourfold_phase_shared_grid_adaptive_chunks.py \
      --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json \
      --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_root_tight.json \
      --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_dyadic_H.json \
      --out notes/2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032.json \
      --trace-dir data/phase_ring_continuation/exact_affine_step4_shared_knot_dense1032 \
      --rays 1032 --block-size 1032 --tolerance 2e-12 --resume

新入口按至多 16512 个 step-times-ray 单元分片，1032 射线时每片 16 accepted steps，且逐件检查小于 5 MB。仍须实际新图、连续残差、参数小盒和 R63/R31 的完整费用，不能把这次预测当最终共轭。
