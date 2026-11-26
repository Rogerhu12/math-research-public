# R239 同一 LM 方程的独立块预条件实现与非零有限核

**可信度：R239 的完整有限维代数实现，加一次真正执行的 91 列有限算子核。没有完成 Cauchy/7760 列实解，没有新的完整非线性接受，没有连续证明或强几何达标。**

## 冻结源码与入口

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `scripts/6a65-cartesian-exact-channel-blocks.py` | 12696 | `d292b35b6121598470968937dab983724aa5250e24ba87942cc50e2e2ec90892` |
| `scripts/6a65-cartesian-channel-blocks-finite-fixture.py` | 9501 | `48b05a801b07dbff80474f4d0e95d0f6341d61287e4783a0c19a1aa69eaa1935` |

固定依赖仍是原完整 stream `b8cfd595b535cc33d47e2c0bc3e2b8d6a79c8163a235415115ca42c53416e4a9` 与原 point `cf475476fb2b5e3a91d4438dd9dd67e54652bfd9594cc577b038ee2fd5e6f08f`。原 v4/long 冻结入口均未修改。

生产用导入 API 是 `SameSobolevAugmented(linear, damping, eta=...)`。`linear` 必须是已有完整 13 行、quintic 两端两 jet 固定的真实线性化。返回的 `.operator` 与 `.rhs` 用于 `lsmr(..., damp=0)`；`.unpack()` 将新坐标转回实际 Cartesian 系数方向，`.physical_normal_residual()` 在原物理系数中计算完整旧正则方程残差。原背景、g、A/Z、训练点、行权重和系数由上层真实状态消费者继续核验，本 helper 不建立或冒充新的状态身份。

本次仅建立上述独立 helper 及可执行有限核，尚未连接任何正在运行的 CI 后继配方。`.receipt` 给出真实局部组装、角收缩、径向累加、带 Cholesky 成本以及显式数组字节数；这些数组字节数不冒充进程 RSS。

## 组装如何保留真实全部行

[R239](../results/R239-complete-cartesian-radial-block-preconditioning.md) 已证明物理系数 normal 的精确径向带宽 5、各角通道的主块公式及旧 Sobolev 正则的增广等价式。

实现逐 radial block 调用原 point 的全部 13 个行 cotangent，取各 Cartesian 分量的局部 jet Gram

$$
C_{c,jk}(s,u)=\sum_{r=1}^{13} L_{r,j,c}(s,u)L_{r,k,c}(s,u).
$$

它是局部 6×6 协方差，未存全局 Jacobian。真实全部 weights 已在 $L$ 中，不再重复乘 quadrature weight。三种 group 的导数都在其中。只有整个 radial block 的全部基两 jet 严格为零时，预条件累加可直接记零；这些点的原残差和原 J/JT 仍保留，未从目标删掉。

对于 $\psi=\cos ku$ 或 $\sin ku$，通道二次乘积只需角离散矩的频率 0 和 $2k$：

$$
\cos^2ku=(1+\cos2ku)/2,\quad
\sin^2ku=(1-\cos2ku)/2,\quad
\sin ku\cos ku=\sin2ku/2.
$$

这是对当前实际离散角网格的恒等计算，不是把非线性系数投影到低模后丢弃高模。当 $2k$ 超过 rFFT 半网格但仍小于完整 $N$ 时，取相应共轭频率；本次有限核特意实际覆盖这个分支。对得到的 $Q_{m,de}$ 只做浮点对称化并记录对称前差值。然后用真实 $B,B',B''$ 全部相乘累积六条径向带。预条件只取主块；每次真实迭代的原 J/JT 仍保留全部跨通道耦合。

旧 Sobolev 正则直接从原 `BandedSobolev` 的真实 lower factor 取得，保留同一 $L_S$。新预条件用 $H_m+\eta S_m$，但求解矩阵是 `[J T; sqrt(lambda) L_S^T T]`，外加 LSMR damp 必须为 0。既没有改成 $\lambda P$ 正则，也没有增加物理 residual 行。

## 本次实际命令和输入

在 NumPy 2.3.5 / SciPy 1.17.0 环境，于 topic scripts 可复算同一数学核：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/6a65-cartesian-channel-blocks-finite-fixture.py --output /tmp/channel-blocks-finite-report.json
```

本次实际输出路径为 Git 外 `solver-work/channel-blocks-finite-fixture01-report.json`，4770 字节，SHA-256 `ceb0a8cd4aadc0d8ce4ede85e5c35f44a91f5a39601fec14b7a2a7f9a2eede8d`。进程真实自然 exit 0；内部总用时 1.4122553100023651 秒。输出有时钟字段，重跑数值核相同而输出文件哈希不承诺相同；新 run 必须记录自己真实 SHA。可重算 raw/report 不入 Git。

输入是源码明确给出的旋转曲面完整六 jet，加 seed `202611261339` 的 91 个非零 Cartesian 系数，非 Cauchy checkpoint、非 probe 标签转换、非云端已接受状态。实际 $J=7,M=4,N=12$，30 个径向点，共 360 点/4680 行/91 列。全部三个 residual group 均非零。原系数 little-endian float64 SHA-256 `34496fac26ca71c1c7977e5294396b04a77a7e8cbd5a0dc603e8bbf29dc252a7`，完整定义和 seed 留在源码。

该小核为独立比较才形成 91 列 dense J；生产 helper 没有这个路径。旧物理增广方程和新预条件增广方程各自用 dense least-squares 比较，并另运行真正的 matrix-free LSMR。

## 实际返回

| 核查量 | 实际值 |
|---|---:|
| 逐通道主块相对完整小 JᵀJ 的最大相对差 | 5.864233030433034e−16 |
| 旧 Sobolev 下带相对真实 $L_S L_S^T$ 的差 | 1.9884041648964861e−16 |
| 完整 physical normal 径向 off-band 最大项 | 0 |
| 新实际增广算子相对旧方程乘 $T$ 的差 | 2.3996200432671387e−16 |
| 完整增广伴随双线性相对差 | 1.4187784990134823e−15 |
| 两个 dense 同一二次问题的物理方向相对差 | 1.6667816404368766e−15 |
| 原二次最小值 / 新二次最小值 | 70.6393109434054 / 70.6393109434054 |
| 返回方向的相对原物理法方程残差 | 2.2385844277799046e−15 |

独立 matrix-free LSMR 真返回 `istop=2`、42 次迭代，用时 .3990167529991595 秒；相对 dense 同方程方向差 3.894934917146806e−10，相对物理法方程残差 4.653226516981372e−11。这里可以报告这个有限线性问题的求解器收敛；不能移借到 7760 列、真实 Cauchy 场或非线性问题。

实际组装 .04822705998958554 秒：point covariance .021219599002506584 秒，角收缩 .022335168003337458 秒，径向带累加 .0029502139950636774 秒，带 Cholesky .0002706749946810305 秒。主带存储 4368 字节，最大显式 covariance 临时数组合计 128040 字节；未测 RSS，未声称生产总成本。局部 Q 对称化前最大反对称差 2.220446049250313e−16。

没有追加非线性接受，没有改进曲面指标的结论。下一次真实消费需要新的显式入口身份、同一完整目标和真实实际非零源；其 Armijo、dense observer、minImmersion（归一化 Gram 行列式）及全部几何约束照旧支付，不能只用有限核成功替代它们。
