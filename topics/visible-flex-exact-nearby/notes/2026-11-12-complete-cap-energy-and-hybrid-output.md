# 同一 r=1/4 帽的完整能量、有限 DN 与全部输出

2026-11-12，R88/R95 实际闭合补充。

准确对象为 \(\delta_5=-7789843107295549/4611686018427387904\)。
物理入口保留 \(k=-4,\ldots,4\) 及 regular 均值 \(\xi\)，
共十个复输入。这里已经完成的是完整未压缩正帽对于这些输入的
DN 包络和全部角输出；它仍不是任意无限输入上的完整低高反馈逆。

## 1. 原始远端结果接回与完整径向覆盖

GitHub Actions run `43286203435` 的九个 FE 块均实际完成，触发
commit 为 `dd8fc199d78c76379502b3be9f2c369e0147ce2d`。
原始完整科学文件保持在
`data/cap_physical4_energy/native_ci_43286203435/block_first_last/`。
这些就是 worker 写入 manifest 的原路径，未将其改成较早建议的
另一套独立目录名称。

接回入口 `fourfold_phase_cap_ci_intake.py` 对每个 archive 核对
GitHub 给出的 SHA256，再核对 42 个原输入文件、原 worker/kernel、
完整 FE manifest、每个元素的 SHA、准确径向区间和原始 identity。
API 请求禁止自动重定向；下载签名地址时使用不含 Authorization
的新请求，地址没有打印或保存。原日志和 archive/file 哈希分别
保存在 `notes/2026-11-12-cap-ci-outcomes/43286203435/`。
本次未保存重复 ZIP 缓存。接回本身不替代数学 collector。

冻结 collector 实际使用：本地 FE0、FE1；远端 FE2–FE19；此前
已付 FE20–FE63；以及自然 C4 graft 和真正无限外尾。完整闭区间
覆盖为 \([1/4,25/8]\)，没有重复、缺失或用零补齐的元素。
未完成的旧本地 FE2 仍独立保存，未进入此次完整积分。

## 2. 完整互补能量矩阵

准确 trial 的内部物理模为 \(|k|\le16\)，径向 P2；准确 dual
通量满足完整散度零恒等式。全部 body、graft、真无限 Robin 尾
经原有 native/全角误差门后，汇总给出
\[
 \|E-\widehat E\|<7.973176493\,10^{-5},\qquad
 \|D-\widehat D\|<7.984482290\,10^{-5}.
 \tag{1}
\]
令准确边界配对为 \(L(j_g,h)=g^*Th\)。R88 配方给
\[
 T+T^*-D\le S_{LL}\le E.
\]
因此以 \((\widehat E+T+T^*-\widehat D)/2\) 为中心，并支付
精确常数核投影及 dyadic 中心选择误差，可得
\[
 \boxed{\ \|S_{LL}-C\|_2<0.000757829736.\ }
 \tag{2}
\]
这里 \(S_{LL}\) 是同一完整未压缩帽在十维输入/输出上的压缩，
不是仅内部十六模解的 DN。完整能量最小值与任意 admissible
trial/dual 的上下界正是消除这一区别的理由。

保存的 \(C\) 对共同常数向量
\(v=e_{k=0}+e_\xi\) 准确为零。实际完整帽同样有 \(Sv=0\)。
投影不是将一个一般小特征值人为删去；其数学依据是准确常数解。
旧 primal trial 的内部均值并未被宣称逐位满足常数分解，相关
能量和选择费用仍全部保留。

对全部输入同时成立的完整 primal/dual gap 为
\[
 \boxed{\ \Delta<0.001515546414.\ }
 \tag{3}
\]
它由
\(\|\widehat E-T-T^*+\widehat D\|+\epsilon_E+\epsilon_D\)
给出；中心矩阵 norm 用 Arb 中准确 Hermitian 幂和绝对行和
支付，不使用浮点特征值作为严格上界。(2) 和 (3) 是两个不同量。

完整 \(\xi\) trial 列本身又是 R95 regular 延拓的合法竞争函数。
使用 \(\widehat E_{\xi\xi}+\epsilon_E\) 得
\[
 E_\xi<0.015002093200,
 \tag{4}
\]
将此前局部均值 ramp 的 \(6.745394\) 上界收紧。这个改进只有在
本次全部能量完成后才使用。

## 3. 全部输出的 34×10 准确中心

R95 的完整 dual 边界输出为
\[
 Jg=(-p_{g,L},p_{g,0}).
\]
其物理输出模式 \(-16,\ldots,16\) 加 regular 通量共 34 行；
更高输出准确为零。保留的十行等于 \(T^*\)，不是 \(T\)。
实际装配逐位核对这一配对，以及原准确 flux 给出的全部 34 行。

令 \(\Pi_L\) 为 \(|k|\le4\) 和 regular 输出，定义有限中心
\[
 J_{\rm hyb}=\Pi_L C+(I-\Pi_L)J.
 \tag{5}
\]
高于 16 的行由这个有限中心定义为零。输出范数严格采用 R95 的
\[
 \|(p,\lambda)\|_{\mathcal X_c^*}^2
 =|p_0|^2+\sum_{k\ne0}\frac{|p_k|^2}{|4k|}+|\lambda|^2.
\]
低行 Euclidean 误差 (2) 也控制其此范数；高行由 R95 真完整
contact 控制，且两个输出空间正交。因此
\[
 \|(S-J_{\rm hyb})g\|_{\mathcal X_c^*}
 \le\sqrt{\rho_L^2+E_4\Delta}\,\|g\|_2
 <0.033369005744\|g\|_2.
 \tag{6}
\]
这包括全部未保留角输出，不仅是 34×10 数组之间的误差。
若十维输入改用更大的有限物理 \(H^{1/2}\oplus\mathbb C\) 范数，
同一常数仍成立。该 statement 没有把任意高频输入置零。

用准确有限 weighted Gram 的 trace/绝对行和，实际得到
\[
 \|J_{\rm hyb}\|<.328139602363,\qquad
 \|S|_{\mathbb C^{10}}\|<.361508609.
 \tag{7}
\]
中心保留了准确共同常数输入核。直接使用全部 dual 而不替换低行
时，本次收紧 (4) 后的完整误差为 \(<.072730081972\)。

| 输出物理指标切口 | 准确 dual 高输出 norm 上界 | 真 DN 高输出 norm 上界 |
|---:|---:|---:|
| \(|k|>4\) | .024417725968 | .057778125222 |
| \(|k|>16\) | 0 | .024703541509 |
| \(|k|>N,\ N\ge16\) 的本报告表项 | 0 | .024703541509 |

这里 regular 输出保留在低行，不混进高角范数。后一行上界不会
仅因提高切口而自动变小：R95 当前短窗 ramp 给的是统一 contact，
不是一个额外的解析高输出衰减定理。

## 4. 保存、准确重放及接线范围

完整能量文件为 `notes/2026-11-12-actual-cap-compression-energy.json`
及同名 NPZ；全部输出文件为
`notes/2026-11-12-actual-cap-full-hybrid-output.json` 及同名 NPZ。
每个报告包含实际对象、源、所有完整积分输入和数组 SHA。

从 topic 目录重放完整汇总：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_energy_collect.py \
 --body-manifest data/cap_physical4_energy/native_local_manifest_at_interruption.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_2_4/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_4_6/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_6_8/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_8_10/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_10_12/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_12_14/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_14_16/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_16_18/manifest.json \
 --body-manifest data/cap_physical4_energy/native_ci_43286203435/block_18_20/manifest.json \
 --body-manifest data/cap_physical4_energy/body_wiener_0800_3000/manifest.json \
 --body-manifest data/cap_physical4_energy/body_wiener_0900_3000_vector/manifest.json \
 --out notes/2026-11-12-actual-cap-compression-energy.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_contact_assemble.py \
 --out notes/2026-11-12-actual-cap-full-hybrid-output.json
~~~

本次 complete 只授予同一完整帽与所列输入列。R88 真核心径向
传播、完整 \(Y,Y^{-1},Yp_Y\) 接口、高低耦合与最后 Schur 逆仍须
按各自真实 norm 支付。新的接口 Fourier 包已提供完整乘子，
但不能用它免费地把十维 grounded 输入列改成另一个无限输入族。
