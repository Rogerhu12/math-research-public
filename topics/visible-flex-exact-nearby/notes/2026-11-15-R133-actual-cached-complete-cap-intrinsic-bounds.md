# 实际完成：从既成闭行取得完整帽区本征常数

公开 Actions run 43674917925 / attempt 1 已实际完成。数学子进程返回 0，9 个门全部通过。消费者只恢复原 4650 行完整证书并取其真实帽区交段上的原球上端；旧 target、intrinsic 网格、ODE、FFT、连续修补和帽残差均未重算。

## 1. 完整帽区结论

对准确闭区间 $[9/10,25/8]$，同固定物理 $\eta_0$、同原本征对象有

$$
|\beta(r)|\le b_*<5.639200000174,\qquad
0<\gamma(r)\le g_*<5.639200000174,
$$

$$
0<K(r)\le K_*<0.254600000149,\qquad
k_*=\max(1,K_*)=1.
$$

完整有向球保存在实际 native。这里 $b_*,g_*,K_*$ 是原闭行给出的合法统一上界，不是实际系数范数的下界或抽样最大值。被选出的最大球上端分别来自原全表行 4620、4620、3310。

原 4650 行完整覆盖首先核验；与帽区有正长度交集的 1346 行再按准确有理交段无缝覆盖 $[9/10,25/8]$。这些行全部保有 same_intrinsic_cap_v2 来源、合法原缓存行号、完整 actual_scalar_germ 和原 beta/gamma/K 闭球。真实 $9/10$ 没有替换成最近浮点节点；跨该左端的原完整球合法包围交段。

原 affine 参数中心为 $-7789843107295549/4611686018427387904$，原闭参数半宽为 $10^{-9}$，因此包括同固定物理 $\eta_0$。原 compact 参数 $\nu_0=-2572625729470897/72057594037927936$、原 M32 candidate、alpha、intrinsic object 和 cap-cache 身份全部匹配。此处的常数不依赖对 moving 场所作的已成连续修补；没有将改变本征对象的参数域纳入范围。

## 2. 原输入完整复用

原完整 native 为 6223338 字节，SHA256：

ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d

它仅按 notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json 恢复原四个完整 byte parts。原 manifest SHA256：

32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3

恢复保持原 gzip 容器和所有数值记录原字节相同；没有新拆分或改写。原 producer SHA256：

1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c

此前 run 43674204314 / 1 已完成的 660 片 $Z$ 联合界仅通过其原 summary 和实际 child0 process 核验后作为输入身份保留。新 Bernstein/联合范数格数准确为 0。该原联合界 native 为 dd236bb30e17ed457a45bd38a24ff3188d896562e5e2e4189d5f3a5579cdc39c。

## 3. 实际过程和输出身份

公开运行：

https://github.com/Rogerhu12/math-research-public/actions/runs/43674917925

工作流提交 6194930c5eaceb40650d51c948a6f1379bfbe368。新科学 source、worker 和 18 项 input manifest 的 SHA256 依次为：

- b0e930d6ba184b4f5d13966e3bba723c101102b751876fd070ec19136a5260af
- 79ccf028728bc13935d68d965dc40e25d85a238bd8e9cb4eda8455b64b0a68da
- f1ddde2aabc4dac44a5b8158de8b874757c598a4610f0984e723ec62931177a6

数学实际用时 1.8337089459999945 秒，子进程包装层观测 5.000526768 秒。新增消费 1346 个旧闭行交段；没有新增 intrinsic enclosure。完整原 4650 行和此前 660 个联合格的数学均未重做。

目录为 notes/cached_cap_intrinsic_ci/run-43674917925-1-complete-cap-cached-intrinsic/。下表路径相对该目录：

| 输出 | 字节数 | SHA256 |
| --- | ---: | --- |
| native/complete-cap-cached-intrinsic-beta-gamma-K.json.gz | 306998 | 145d6e558f8348bf2b29febc8700aa43cba2a507b3ba2d7fc7da5ea1db22cd2d |
| process.json | 6912 | 02ad407e992974d6c5505e2d2a6774f34692731091fb375ec6ef00d0d26769d4 |
| evidence/complete-cap-intrinsic-summary.json | 5275 | 7a08e94850d66de1d9dba184df205a5a288436fbb0cc005edaa462261976a17f |

本记录只经连接器读上述小文本和 artifact 元数据，没有读取 gzip 或原 byte parts。新 artifact visible-exact-cached-complete-cap-intrinsic-43674917925-1 的 ID 为 14146575124，大小 6432157 字节，digest 为：

80a716b0a6693af822fdff7a972be1a4538a8c70ed0499148bb13a46417cf5dd

该 artifact 保留恢复后的完整原 native，以及本次输出和真实过程。

四次真实 pull 的两份 README 差异均为空。末次为 2026-11-15 04:02:14.082719 UTC，从 807a2f223abe36002ced38edeecfe3b3eb5a0aac 拉到 69d9ce86c573a5b2e4262f1336432c52bee96c81。根 README SHA256 仍为 8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2，本题 README 仍为 81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220；先前已读规则变更提交 ee26c0a65a2e63c15f2ccfba6714181584416542 仍完整记录。

## 4. 后续可用范围

本条提供同一本征对象在完整帽区的三个系数上界，可与已成完整 $Z$ 联合界一起交给固定 gauge 的帽算子扰动合同。后续组合小量、改变外边界、未知全频反馈或非线性同域条件仍须按相应合同单独核验；本次 9 门没有宣称这些后续门已付。

没有重算 5970 同 F 矩阵格、7908 adjoint 格、真实帽边界、Green 或 Poisson。完整无限 BVP 逆、真正参数响应及最终 Schur 结论仍不由本条授予。
