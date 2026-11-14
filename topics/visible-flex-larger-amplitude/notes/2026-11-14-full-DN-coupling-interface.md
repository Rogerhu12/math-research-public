# 大核完整材料角尾接口：实际 profile、计数及可执行响应检查

可信度：**接口推导与待执行数值设计；没有新的完整延拓解或闭曲面结论。**

本条使用已经接受的 M96、$s=0.984$ 完整场，或公开 Actions 真正接受后的
后继场。没有把 $s=0.984/0.99$ 的正 $a'$ 端点称作物理尾切口。

## 1. 已有可运行的完整 scalar 对象

`geometry_20261114_full_scalar_profile.py` 从所给 accepted 文件恢复原
`FixedProfile`，接原 `strong_20261114_scaled_core_tail_connector.py` 的
`AngleConnector`、$a'=-0.985$ coast 和原 `NeckTerminalBridge`。
默认峰值角曲率为 $2.5$，末端是原物理 $r=0.3$ cut；原尾 $E,E'$ 及其余
参数不变。三个内支控制为

$$
a(s;p)=a_*(s)+\sum_jp_jb_j(s),\qquad
b_j(s)=64\ell_j^2x^3(1-x)^3,\quad
x=(s-l_j)/\ell_j\in(0,1),
$$

支集外 $b_j=0$。三个支集分别在已接受前缀内部、turn 内部、coast 内部。
它们的 $0/1/2$ jets 在支集端点为零，故 inlet 和真正 cut 的 scalar jets
不随 $p$ 移动。程序逐一检查新接缝的三个 scalar jets。控制的线性无关或
全 BVP 响应满秩尚未由支集不交自动得到；必须实际算。

原 `AngleConnector` 对 $a$ 使用既有 48 点分段 Gauss 积分；不能把这个
浮点调用宣称为全区间区间证书。完整非轴对称场还没有在这些新增段上求出。

## 2. 全非均值 DN 行与准确维数

物理场为

$$
y=(r_0,\ldots,r_M,t_1,\ldots,t_M,z_0,\ldots,z_M),
\qquad n=3M+2.
$$

固定前 $K$ 个 core 系数时，左边界包含 $r_0=1$、这 $K$ 个系数、
$t_m+2mr_m=0$ 和所有 $z_m=0$，共 $2M+K+2$ 行。若匹配材料角中全部
$T$ 个非均值 DN 行，所需 scalar 设计控制数量为

$$k=T-M+K.$$

| 用途 | $M$ | $T$ | $K$ | scalar 未知量 | 左 / 右行数 |
|---|---:|---:|---:|---:|---:|
| 初次完整 profile 设计 | 96 | 96 | 3 | 3 | 197 / 96 |
| 冻结实际 scalar 设计后的材料角精化接口 | 96 | 96 | 0 | 0 | 194 / 96 |

第一行共有 $n+3=293$ 个边界条件，第二行有 $n=290$ 个。
不能在 $T>M$ 时仍只加三个控制，也不能用旧 64 行 principal normal
projector 代替实际 96 行材料角 DN。

`FrozenCompleteProfile(designed, p_star, field_modes=...)` 用同一个公式和
全部已求出的 $p_*$ 冻结 $a(s;p_*)$，不再留下 scalar 参数。后续令 $T=M$
一起增加，`FullDNBoundary(..., target_core=[])` 释放全部 core 系数。共同
材料角下 target metric 的识别与固定度量精化的条件另见根会话登记的
材料坐标结论；本接口没有把“重新设计 scalar profile”计为同度量精化。

## 3. 材料角变换必须进入边界 Jacobian

令

$$
\theta=\phi+\sum_{m=1}^M\frac{1-4m^2}{2m}c_m\sin(2m\phi),
\qquad \rho=\partial_\phi\theta>0.
$$

`MaterialTrace` 使用原 `material_angles` 反解器和全部 $M$ 个 core 系数，
构造有限角网格投影 $P_c$。虽然原场在 $\phi$ 中只有 $M$ 模，换成
$\theta$ 通常有无限谱，因此 $P_c$ 的网格和 $T$ 截断误差都仍须精化。

固定原 $\phi$ 场时，换角导数是

$$
\partial_{c_j}\phi
=-\frac{1-4j^2}{2j\rho(\phi)}\sin(2j\phi).
$$

设实际尾高度和径向方向符号分别为 $\epsilon_h,\epsilon_r$，且

$$
a=r_{\rm cut},\quad a'=\epsilon_r/\sqrt E,
\quad a''=-E'/(2E^2).
$$

全部非均值边界为

$$
R=P_c f_z(s_b,y_b,p)
-\frac{\epsilon_h\epsilon_r}{\sqrt E}
\mathcal D(\epsilon_hP_c z_b)=0.
$$

默认上半片采用 $\epsilon_h=\epsilon_r=-1$。
`geometry_20261114_full_dn_boundary.py` 保留
$\partial_cP_cz$、$\partial_cP_cf_z$、完整有限 ODE Jacobian 和全部
$T\times T$ DN Jacobian。特别是右边界对 inlet $y_a$ 的 core 列不为零，
不能把它装成只依赖 $y_b$ 的旧 normal BC。

`tail_map(H)` 必须返回完整 `slope`、`jacobian` 和
`actual_nonlinear_solve` 标记。允许 outer Newton 内部明确标记的完整 affine
DN 线性化；最终必须重新请求原非线性尾及 audit。`directional_check` 对
全部 $y_a,y_b,p$ 方向作两级中心差分，返回实测误差，不自行授予闭合接受。

这里 $T$ 行是全部**非均值**行。均值 $H_r,H_{rr}$、完整高度六 jet、平面
配准和 branch 一致性仍须实测。连续层面在原正分支、完整 cut 数据和周期
条件下的均值与六 jet 唯一性由 **R239** 给出；有限 DFT 不自动满足该定理
的全部连续假设，也不能把均值误差从报告中删掉。

## 4. 不改原 QR 的常值状态增广

原 `geometry_20261114_separated_qr_bvp.py` 明确要求无外部参数且左右边界
分离。新 `geometry_20261114_full_dn_augmented.py` 追加

$$c'=0,\qquad p'=0,$$

并在左边界加 $c-y_{a,r[1:M+1]}=0$。右边界中的 core 使用 $c_b$，
scalar 控制使用 $p_b$。这与原非局部边界代数等价，不增加物理自由度。

初设计有 $n_{\rm aug}=290+96+3=389$ 个状态，左 293 行、右 96 行；
冻结 scalar 的 $K=0$ 精化有 386 个状态，左 290 行、右 96 行。
两种情形都能交给原 separated QR，而不削掉任何高度或 core 模。

`AugmentedFlow` 调用原 `BatchedFFTFlow` 的同一方程。每次调用注入该次
实际 $a,a',a''$，避免旧的“仅按 $s$ 缓存 profile”在不同参数迭代间沿用
陈旧数值。导数用原 $10^{-25}$ complex step；新 core 常值列和常值状态
导数为严格零。没有谱过滤、截根、人工修改不合格 trial 或替换尾方程。

## 5. 本公开仓库 Actions 的短响应命令

以下先验证具体完整 scalar 及控制 RHS 实现，不启动全局 Newton：

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_dn_augmented.py \
  --accepted topics/visible-flex-larger-amplitude/notes/2026-11-14-geometry-resume-scaled-sphere-M96-normal-BVP-r1.json.gz \
  --port topics/visible-flex-larger-amplitude/computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --out "$RUNNER_TEMP/full-DN-interface-response.json"
```

输出包含真实已接受前缀上零控制 RHS 与原实现的差、参数导数的两级
CS/FD 对比，以及明确标记的 turn/coast 圆形**局部校准状态**。后者不是
沿完整新 profile 的非轴对称解。实际 full-DN 边界 FD 检查还需接入真正
T96 原尾 client，不能用这个 RHS 检查代替。

## 6. 可以同时执行的 fixed3 normal 第三线

`geometry_20261114_public_free3.py` 从完整 accepted M96/N1024 文件出发，
调用原 continuation 的 `--fixed-modes 3`，重建 first_mode=4 的 93 行
principal normal projector。原 290 个状态、完整 Fourier RHS、
RMS $10^{-6}$ 和 BC $10^{-11}$ 门均不变。每次实际接受后执行全 core
有理界证书及材料角 C² 场读出，再推进下一段：

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_public_free3.py \
  --out "$RUNNER_TEMP/free3-out" --work "$RUNNER_TEMP/free3-qr" \
  --durations .006 .012 .024 --budget-seconds 18000
```

本地只完成 AST 与只读 `--plan-only` 校验，未在本地执行数值求解。
normal 第三线仍然是带边前缀；它的意义是提前释放最终全 DN 所需的
core 4..96 响应，不是绕开真正尾与全曲面完成标准。
