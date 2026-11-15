# R813：两个原 Wronskian 正规坐标的准确完成

日期：2026-11-15。状态：**本篇记录已完成的真实原 S3 计算及完整文件认证。**
它完成原 g、h 两个正规向量；Mg、Mh、Γ、极理想、η与高度不在本次范围。

## 1. 实际运行与固定源

- 公开 run：[43715253991](https://github.com/Rogerhu12/math-research-public/actions/runs/43715253991)。
- source commit：74f5296a6aa06539580ecbd9591a1284e1984a4e。
- 数学 job：132815271738；2026-11-15 12:58 UTC 完成，原 compute 与冻结 verify 均成功。
- 核心计时：67.613511668 秒；这不是含下载、安装和上传的整个 job 用时。
- 核心目标仅两个Q右端，同一原690维S3、41个qY项、820个实坐标。

| 固定源 | 字节数 | SHA256 |
|---|---:|---|
| serre-p41-original-Wronskian-derivation-inputs.yml | 3190 | 13fb4bb39f0a4f34fc3a188ce563c7baf482d876e8c8bb1a8ed4be142de287f4 |
| R813-original-two-S3-Wronskian-derivation-input-method.md | 8667 | 00c21c72eee29f4ef9c2d643f4c03d0b98abd45c775f7c7328b5b6782ec29b27 |
| R813-public-original-Wronskian-derivation-inputs-request.json | 5750 | dec2573f4641b3a577c49fd4a5466f69799fb49ca97098cdb5009519040ccef7 |
| R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md | 14121 | 3cf42cc8b6018e6e171feccdf77340f386d38051812a0bf5037851cad0ab0f25 |
| R786_public_exact_power5_short_basis.py | 17041 | 7fbfe97b21ff9f58de4f1d2891b9f4a8cec4712e1b1c6d26d6d1ab9c336b81ec |
| R813_original_Wronskian_derivation_inputs.py | 48020 | 830ae652ebb08a035c6636c7738ab4823322111944932ffc77b1136caf7a07bc |
| R813_public_original_Wronskian_derivation_inputs.py | 45422 | e838f3abfae569b2638114fbc75ae8a22c03a90b1bfb1718c88d3d8d86197e78 |
| p41_public_actions_recovery.py | 10548 | 39de279d30ad1493f1727c2e3c650b47b2bb0191765770b32a17ae2adb97c49e |

理论依据为 [原 R813 证明](R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md)；
执行契约为 [两个 S3 右端的方法](../notes/R813-original-two-S3-Wronskian-derivation-input-method.md)。
所有数学均由本公开仓库 Actions 执行；本地恢复后只读源、数据、哈希、schema及原wrapper.verify，
没有导入或执行数学核心，也未导入flint。

## 2. 原函数、真实基与尺度

保原 τ=e0、σ=e1+e73、实际 primitive w0=e2，令
$$
D_0=\frac{q_Y}{82}\frac{d}{dq_Y},\qquad
G=\tau D_0\sigma-\sigma D_0\tau,\qquad
J=\tau D_0w_0-w_0D_0\tau.
$$
实际输出给
$$
g=\frac G{\tau^3}=\delta z,\qquad
h=\frac J{\tau^3}=\delta w,\qquad \delta=\tau^{-1}D_0.
$$
使用R805已完成的原S3基，不能换成同维度的旧R786 V3基。
690个坐标按已认证的原(S_row,normal_basis_row,power_of_z)表
放回权(0,1^144,2^127)的272维正规基；各向量的weighted次数为3。

| 原尺度 | 实际证书值 |
|---|---:|
| D0 的 qY 系数 | 1/82 |
| M2 整尺度 | 6724 |
| 旧 V2 整尺度 | 45212176 |
| S3 整尺度 | 304006671424 |

准确坐标读取规则始终是
$$
\frac{\text{coordinate numerator}}{\text{column denominator}}
\cdot\text{original target rational scale}.
$$
真实两个target scale都为6724/1，必须各乘一次。
不能按次数猜补1/82、82²或82⁶，也不能把已除content再插回。

## 3. 实际恢复与全行终验

两列使用原R806已成的 p=1000000007 固定690阶逆；
真实 Dixon digits 为 **432**，未重做旧选行、旧秩或模逆。

| 原目标 | column denominator 十进制位数 | 实际非零S3分子数 | 原target scale |
|---|---:|---:|---:|
| g | 828 | 690 | 6724/1 |
| h | 1931 | 690 | 6724/1 |

两原Wronskian均非零；两种qY/ξ与v/t表示完全一致，cusp常数项准确为零。
每一列均已在全部820个原坐标中乘回核验；严格有理重构只提出候选，
最终结论来自这个特征零完整恒等式。
原τe_i乘积全部复用旧V2别名；只新增每个右端所需的一次weighted卷积。
R806的34组Mw数值没有在本首scope中重求或消费。

## 4. 原产物身份与完整纯IO核验

- artifact：14162633303，serre-global-R813-original-Wronskian-derivation-inputs-43715253991-1。
- ZIP：20102979 B；SHA256 0850402e283b5b16454aeba4c0967d06cad65951d09a8972aba9b34007b3c812。
- 到期：2026-11-16T12:58:33Z；仅用于直接消费者的一日活跃传输。
- 实际ZIP成员451，完整manifest列449；所有文件大小和SHA均已核。
- 原stage manifest含441个stage；所有配置与原source身份相符。

| 产物 | 字节数 | SHA256 |
|---|---:|---|
| p41-original-Wronskian-derivation-inputs-certificate.json | 10654 | e3c2e041490d918bfec45c08dea337eb44a17548788ad8ce5f01cd14877d0a64 |
| R813-stage-manifest-18457338f91f4aa2c9541979.json.gz | 25162 | ee8a07765edff4a1349ded569085330521998ec296d14020c5ff49400e6a1366 |
| R813-original-S3-coordinate-interface.json.gz | 50237 | c853f0e2b2db2ab82f7f50abda80fb801234b4fa408c1e5dea5c71ccfc51a882 |
| R813-two-exact-S3-Wronskian-coordinates.json.gz | 950296 | 29bedd339da16b4fee3dfd412f1d599343a25231fa3b360f5b7b6be4404e9085 |
| R813-original-g-h-normal-vector-interface.json.gz | 8761 | ef9d09186098bd8cc2144c16bf7797234ac176b7d1faac3fd50b74564c6f32a6 |
| R813-retained-producer-inputs.tar.gz | 17558153 | 56e26ff7e54d4bdea44dd86050ebd0e86c59ed988d30c3d2628ab2a0fbc3e108 |
| full-outputs-manifest.json | 163532 | 0b54cf2ebb843fb789058d6c40c766428a2d79d1a9b0f705ce4094d4aee1acf8 |

原输入carrier共726个文件：

| 原producer | 已携原文件数 | 原数学run | 原source commit |
|---|---:|---:|---|
| R786 | 14 | 43682100611 | dd262672a8b1e2af82277b15e0fa766038609670 |
| R805 | 701 | 43705580592 | 9f960b8e0b2fa825ab1391e86db4e1383ffdd700 |
| R806 | 11 | 43707290840 | 75b1d56c821abe34660477ba8b4c7f7b75a4382b |

全部carrier成员按各自原完整manifest逐字节数/SHA验证，
再以冻结R813 wrapper的Producer与select_original_inputs核完整源闭包、
146条旧τe_i别名、原690基、真实e2和原固定逆。
随后原样运行冻结wrapper.verify，返回0。
此核验只读原数据与认证字段，未重新执行其中任何数学。

纯IO摘要15678 B，SHA256
55086bf25e4d83e0ebba671af1c8ab33b07653182e43a69eedd5f889636fb8d6；
执行审读脚本SHA256 c8f5f0516cd78a0ed51fcf4bb4eeb608558ce3e2e6b1957b1b195c0f1b80517e。
摘要、raw、坐标与证书不入Git或Release；本篇保原source/run、准确结论与复现身份。

## 5. 真正后继

R815消费这两个原向量和R806已成Mw；
按 [R817](R817-original-normal-derivation-without-separate-h-multiplier.md)
只恢复Mg与Γ，h仍是必要原向量，独立Mh表不重构。
七个固定准确点的嵌套交换子与原两列约束识别Γ；
下游 [R814](R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md)
再处理原cusp零理想与重数剥离。

本次不声称这些后继矩阵、理想、η、规范高度或主Serre一致性定理已经完成。
