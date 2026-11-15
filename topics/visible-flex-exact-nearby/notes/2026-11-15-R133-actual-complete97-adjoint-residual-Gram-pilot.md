# R133：普通伴随残差完整97维Gram四格的实际认证

公开 Actions [43664278200](https://github.com/Rogerhu12/math-research-public/actions/runs/43664278200)
已真实完成数学child（返回0），九门全部通过。producer用时42.430547201秒，
wrapper实际child用时45.001444911秒。四个新闭quarter各约5.3秒。

## 实际对象和已付范围

本次直接验证完整257状态、97输入的固定Hermite试件，原提案native为
`acb2151b60f24ad88b30e6f7d1d966851abc53c15e45df19df2bfca27c2393c7`。
全部7908原whole标量域与7908原生点包围、原真实257×97节点值/两侧导数均按原字节复用。
新intrinsic target调用数为0，原forward帽列没有被转置或重算。

本次对quarter索引0、64、4096、7907分别算出完整signed97维普通形式伴随残差、
系数无限Fourier/径向余项、以及同一实际修补中心的完整Hessian伴随Gram。
真实Hermite节点与1341个Hessian原格按闭交段消费，入口准确为 $9/10$。
非mean Parseval权 $1/2$、独立mean权 $1$、物理角频 $4j$、
原有限多项式仿射限制、真实径向Legendre积分均通过实际代数门。

下表是每个独立Gram的 **trace上界**，不是源误差下界；
完整矩阵的符号非对角项和有向Loewner slack另存原数组：

| quarter索引 | finite ordinary | 全系数余项 | 完整Hessian伴随 | 合并后的真普通伴随 |
| ---: | ---: | ---: | ---: | ---: |
| 0 | $<1.660756\,10^{-29}$ | $<1.957084\,10^{-34}$ | $<4.460174\,10^{-30}$ | $<1.244641\,10^{-28}$ |
| 64 | $<9.983047\,10^{-9}$ | $<8.651290\,10^{-23}$ | $<2.639119\,10^{-18}$ | $<9.983373\,10^{-9}$ |
| 4096 | $<5.028220\,10^{-27}$ | $<2.429306\,10^{-32}$ | $<3.902023\,10^{-25}$ | $<4.844180\,10^{-25}$ |
| 7907 | $<7.706899\,10^{-33}$ | $<1.034688\,10^{-36}$ | $<4.694440\,10^{-45}$ | $<7.886543\,10^{-33}$ |

quarter64的当前界由有限Hermite残差主导；不能仅因uniform系数误差很小，
便把该有限残差省去。其余范围尚未由本pilot计算或推断。

## 完整原始身份

目录：

`notes/cap_adjoint_residual_Gram_pilot_ci/run-43664278200-1-cap-adjoint-residual-Gram-pilot/`

| 原件 | SHA256 | 字节数 |
| --- | --- | ---: |
| native/complete97-ordinary-cap-adjoint-residual-Gram-pilot.json.gz | eb58b97ae182cedf621c4ff122b421ffb844e3839266a6a7d6df86b9134d8cfb | 30674 |
| process.json（仓库最终快照） | b349e709a9e130c59819218bdb244ba42447a5ffb6e1881058316f7b285912a3 | 18571 |
| evidence/complete97-adjoint-residual-Gram-pilot-summary.json | de1fc5db39f2a782df94225a62cf2b41899d0d2474dc8c6da74c564decaf4138 | 19515 |

core SHA256 `689bf2c54350d832cffa7ca8f46dc424509fb221e3d73cb228a1f9a18130c0dc`，
producer `ae3b90c15e65343a0d5bdeb80cba4d6eb2a6f519155bff9a175b0f48a2f72310`，
worker `3f7c1f5862530cf13bda0a30466fc16998ef2a1f0f60ab97a8e5bc9506d81222`，
manifest `467cd31f6d62b834d3a0cf07a1ef92efe1a2ef218e27d862140122c37a9ce71f`。

公开artifact为 `visible-exact-cap-adjoint-Gram-pilot-43664278200-1`，
ID `14141059620`、API大小1459303B，
归档digest `8257f3eedc7c628cb72977575748b1e956918b9d96a400bb23bf08ff583df2df`。
四个实际NPZ分别326760、338894、344644、345611B，含完整97维signed三角、
对应dyadic对角slack及此次新的物理系数多项式；只由公开Actions保存/消费，
没有通过connector读二进制。

## 真pull和未授予的范围

最后真pull为2026-11-15 01:44:00.594123 UTC，
从 `319a16675aa5d562a4279e0e55e29ecb90c93c2f`
到 `1a973e6ab0306b0fc63eb19829e4fc094ab79f21`。
两README准确diff均为空，已读规则commit仍为
`ee26c0a65a2e63c15f2ccfba6714181584416542`。

本结论只授上述四个真实闭quarter。下一完整覆盖须原样复用这四份结果，
只补其余7904格；真左97输入误差、全外Robin/mean、高输出完整Gram、
与97右Poisson的方向合成仍须单独消费。
当前未证明全7908伴随误差、完整无限帽high-to-low新界、全身无限BVP逆或真实参数Schur。
