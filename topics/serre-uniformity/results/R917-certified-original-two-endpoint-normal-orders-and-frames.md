# R917：原两端完整八维正规阶与原参数行列式帧的实际认证

日期：2026-11-16。状态：**本公开仓库 Actions 已实际完成原两个标记端点的完整八维正规阶、含幂零的完整特纤维，以及相对于原 primitive 与 $t$ 参数的 determinant 帧。** 本次辅助素点计算不展开特征零正规阶基；五目标理想、原目标 272 正规函数端点坐标、九范数完整端点标定仍不是本次完成项。

## 1. 实际运行与原来源

[公开运行 43904492746](https://github.com/Rogerhu12/math-research-public/actions/runs/43904492746) 的真实 source commit 为

`64228da6693769dcf70fb8bcaec4a72ad0faa445`。

规则 job 为 `133429574758`，构造 job 为 `133429673237`。两 job 及来源准备、数学计算、输出 IO 审读、一日 artifact 上传均已实际成功；不是 pending 请求或仅完成语法解析。核心回执记录退出码 **0**、`error=null`、总算术核运行时间 **3.290035527999976 秒**；数学 FINAL 的内部计时为 3.2893059340000264 秒。共有 **173 个完整数学 stage**、两个完整端点证书。

数学依据是 [R917 原两端正规阶证明](R917-original-two-endpoint-normal-orders-and-source-contract.md)、[R912 原八维端点格](R912-original-eight-dimensional-endpoint-lattices-and-norm-frames.md)，执行依 [R917 冻结执行契约](../notes/R917-original-two-endpoint-normal-orders-method.md)。原局部展开及几何对合来自 [R914 实际全 146 作用与 $P_1$ jets](R914-certified-original-full-V1-involution-and-P1-jets.md)，原对应及同素点十七系数保持 R873/R882，原 $t$ 首项保持 R883。

原曲线、level 82 整数尺度、$-3$ 下降、几何 $\iota$ 以及两个投影的方向全部保留。辅助素数和原嵌入为

$$
\ell=1000000753,\qquad \zeta\longmapsto549966761,\qquad
s\longmapsto99932770.
\tag{917R.1}
$$

原局部参数严格为

$$
\rho_0=z-z_0,\qquad
\rho_1=\iota^*\rho_0=z-2\beta_{72}-z_0.
\tag{917R.2}
$$

第二个参数没有替换成 $z-z(P_1)$，也没有用算术共轭取代几何 $\iota$。

## 2. 两端实际数值与正规化出口

以下每项均直接来自实际完整 stage，而非按方法中的预期填入。

| 实际量 | 原 $P_0$ | 原 $P_1$ |
|---|---:|---:|
| $v_{\rho}(\widetilde P_8)$ | 0 | 0 |
| primitive 缩放 $\Theta=\rho^hU$ 的 $h$ | 0 | 0 |
| primitive 表的系数数目 | 273 | 273 |
| primitive 判别式阶 | 6 | 6 |
| primitive 判别式首项 | 425050525 | 312352727 |
| 实际 idealizer 扩大次数 | 1 | 1 |
| 实际累计 index 长 | 1 | 1 |
| 最终判别式阶 | 4 | 4 |
| 最终判别式首项 | 425050525 | 312352727 |
| 最终统一系数精度 | $\bmod\rho_0^{271}$ | $\bmod\rho_1^{271}$ |
| 最终表的秩 | 8 | 8 |

因此此次两个端点都没有发生初始首一化的精度损失：$\widetilde P_8$ 已是实际单位，$\Theta=U$。一个真正 index 长 1 的扩大把判别式阶从 6 降到原正规阶的阶 4；该扩大消耗两个统一 $\rho$ 阶，273 项输入给出最终 271 项完整乘法表。

实际 idealizer 线性核在两端均为维数 1，选原第 7 个自由坐标为 1；其余标准补列为原幂基下标 $0,1,\ldots,6$。若 $v_\epsilon(U)$ 表示该已保存的完整八坐标核向量，则输出的实际正规基顺序为

$$
\left(\frac{v_\epsilon(U)}{\rho_\epsilon},
1,U,U^2,U^3,U^4,U^5,U^6\right).
\tag{917R.3}
$$

这里 $v_\epsilon$ 的全部八个系数、完整原方程矩阵、单位自由坐标及全部乘回均在实际 `idealizer-kernel` stage；不是一个尚待求解的余子式占位。正规基、相对原幂基的完整 Laurent 矩阵及其双向逆也都已经实际保存。

每次基变换保完整 $8^3=512$ 个结构常数。所有可能负阶系数逐项确认为零，原首一关系在新表中完整乘回，全部八个左右单位乘积通过。实际判别式阶及首项同时满足原累计 determinant 变换式。由 [R917 正规化证明](R917-original-two-endpoint-normal-orders-and-source-contract.md) 的 index/discriminant 判据，这两个完整整数阶均为原对应在指定辅助素点的两端正规阶。

## 3. 完整长度 8 特纤维

两端实际输出均保完整八维乘法常数及单位坐标，另有如下已成核验：

| 特纤维量 | $P_0$ | $P_1$ |
|---|---:|---:|
| 完整代数维数 | 8 | 8 |
| trace radical 维数 | 4 | 4 |
| radical 平方维数 | 2 | 2 |
| radical 立方所有乘积为零 | true | true |
| 删除因子或替换成约化商 | false | false |

原几何长度型 $1+1+3+3$ 来自同一个 R873/R912 对应来源；本次保存和验证的是其整个长度 8 代数，包括两个长度 3 部分的幂零。没有只挑两个固定点、只保半单商，或把八维表换成四个几何点的数值。

## 4. 原 primitive 与 $t$ 帧的实际首项

原基变换相对于 $1,U,\ldots,U^7$ 的 determinant 单位在两端都为

$$
u_\epsilon=1000000752=-1\pmod\ell,
\qquad 28h-I=-1.
\tag{917R.4}
$$

式中 $u_\epsilon$ 是普通 determinant 单位，不是固定微分 $\nu$。因而两个已保存基变换 determinant 均为 $-\rho_\epsilon^{-1}$。

保持原 $t_0=t$、$t_1=t-1$ 及原首项

$$
t_\epsilon=c_\epsilon\rho_\epsilon+\cdots,
\qquad
c_0=354813668,\quad c_1=645187085.
\tag{917R.5}
$$

这两个 $c$ 来自 R883/R914 原字节；R917 不重算原 $t$ 级数。其实际行列式帧为：

| 端点 | 原 $\rho$ 阶 | 原 $\rho$ 首项 | 原 $t_\epsilon$ 首项 |
|---|---:|---:|---:|
| $P_0$ | $-1$ | 1000000752 | 645187085 |
| $P_1$ | $-1$ | 1000000752 | 354813668 |

每个 frame stage 同时保存原 $U$ 在完整正规基中的八个 Laurent 坐标，原目标 $w=K/P_U=\widetilde K/\widetilde P_U$ 的准确来源表达式，以及 R873 的 canonical dual7 输运。dual7 的分子和分母两个 determinant 因子都仍在场。

原固定微分保持

$$
\nu=82\tau\,dq_Y/q_Y,\qquad \iota^*\nu=\nu.
\tag{917R.6}
$$

本次没有声称算出了 $\nu/d\rho_\epsilon$ 的新数值。特别地，上表是正规阶相对原 primitive/t 的 determinant 帧，不是目标线丛的 $\operatorname{Nm}(\Phi)\det U$ 或九范数截面的完成标定。

## 5. 来源与尺度的实际闭包

新载体只含五组原来源，共 **40 个成员**：R873 7、R882 8、R807 7、R883 7、R914 11。原 result、run、source commit、core SHA、manifest SHA、配置指纹及各成员字节均保持。

R807 的 $\theta,N_{692}$ 沿 R883 已续存的原 11 件 tar 逐 SHA 核验后只选七件，不访问更换身份的生产者。R873 的 2050 个 V8 原配方和八个补列、R882 的十七个真实坐标右端均直接消费；原 2058 阶系统和逆没有重算。$P_0$ 的 $\theta,N_{692}$ 前三项直接引用 R883，只有更高项及 $P_1$ 项属于本次必要新线性组合。

原 $e_i=82^2T_{1,i}$ 的尺度已经在原叶和配方中，本次没有再次乘 $82^2$。原有理分母的模逆也直接引用已成 R883；共同正则化使用

$$
\widetilde c=\theta_0^2 V_{8,c}+A^2V_{2,c},
\qquad \theta_0=\theta/\tau,\quad A=N_{692}/\tau^4.
\tag{917R.7}
$$

整个计算没有将 $\theta_0$ 的端点零当单位去逆。准确特征零 $P,K$ 定义仍绑定原 R873 unit-solve；本次正常表的有限域数组不更名为特征零展开系数。

## 6. 完整文件身份

数学 RESULT 为 `R917-original-two-endpoint-normal-orders`。核心实际配置 SHA 为

`1d1e0b7e6cd16ad4108e0674c2a9cca73ff1eadf35902269f1673a2199b5fb4b`。

固定实现 SHA：

- 算术 core `f0e321a19ef6dbd259e88de1b670f514b0f9ed0df5b24659a9f787978b8fd743`。
- 小阶算术 helper `c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d`。
- stdlib public wrapper `f4a5e2a1d1a5405c52b7a602c215e8cad734a4d613c964c197a69c5a28ca7d29`。
- 执行 method `fafa85a5ad5e2758f3e866000a34d3a1849825602b616e0067784077b8171941`。
- 实际激活 request `4354fff045dd08b3682b73c633853722cdc67b067877c5ae9173dc2200d32e07`。

请求的最终 session/规则读取 commit 更新没有改数学 core/helper、40 个原数学来源或固定策略。

| 原文件 | 字节 | SHA256 |
|---|---:|---|
| `p41-original-two-endpoint-normal-orders-certificate.json` | 13981 | `cf539a58a7ab8212bb0e0d56c9621c2c6916ca25c2cbc3b50ce7be3890c15349` |
| `full-outputs-manifest.json` | 32468 | `d8bac1cf2d29e385afd7222d87805506732e2dfecc440980b187e6112bb2af2b` |
| `R917-endpoint-stage-manifest.json.gz` | 13868 | `2da48780e4b10302720c07701e4cfff368631e7cb142a60bed044dcdbcadb9eb` |
| `R917-retained-original-inputs.tar.gz` | 1726328 | `2cc0f16ce61785304c90c2f6f43d1e594743313dac76eeed4215ad27ca039b24` |
| `R917-original-source-inventory.json` | 10700 | `15221ebe5e4fb2321c6b26393eb460e1a9399a9800cfc4e6eacf220e7b9689c1` |
| `core-receipt.json` | 703 | `b8e2f7a44590f7697d4cb47915689babfbd41ed40c021c98b4f61cf2260b326c` |
| `run-receipt.json` | 438 | `f73c00b92766fcfadb7694f9c7594b3041494aff3238a821245a3d61e03829d2` |

### 6.1 两端可直接消费的数学文件

| 端点与阶段 | 原文件 | 字节 | SHA256 |
|---|---|---:|---|
| P0 / certificate | `R917-endpoint-P0-normal-order-certificate.json.gz` | 5180 | `10e3993574969779d07eb99234f069fd220ec42a4aa95d61e855dc6090d4d16b` |
| P0 / common_cleared | `R917-endpoint-P0-common-cleared-seventeen-jets.json.gz` | 30888 | `11297c7a80c89c8d8e2d260bb1d1bcca1f53239a78934851281afa0c00c80d24` |
| P0 / primitive | `R917-endpoint-P0-primitive-order.json.gz` | 334193 | `433c346fe6e1e58a5889648a227cf6254d082002429fc9d1bb02bc8f0f6803da` |
| P0 / normal_order | `R917-endpoint-P0-order-001-complete-table.json.gz` | 319719 | `1d168ccd20d9697805293e185d6def489690717e24410ef771ddb2c62c41561c` |
| P0 / discriminant | `R917-endpoint-P0-order-001-discriminant.json.gz` | 68172 | `98ba374851febd0cfc98f0ca9a8827ea016ff085c5dd28cc3f3ccfafc2bf7ad8` |
| P0 / special_fibre | `R917-endpoint-P0-complete-length8-special-fibre.json.gz` | 6442 | `71d33efa4f41996f3ea1f1d54c11512af9c9998dc4f224a64b63317a090970e8` |
| P0 / frames | `R917-endpoint-P0-primitive-and-original-t-determinant-frames.json.gz` | 5242 | `af8612924918b42091891f979cf91f2d9d9a7e2ec08dec2d407e8f7e1e599f0f` |
| P1 / certificate | `R917-endpoint-P1-normal-order-certificate.json.gz` | 5174 | `ec5cc3e3245e9f4b962283699f9888338c4a5704c8d9ae7fb2717f338f8920c1` |
| P1 / common_cleared | `R917-endpoint-P1-common-cleared-seventeen-jets.json.gz` | 30843 | `63b7cf58f56344ecb8a86e3dedee66e5ea278c68871456edd93234b5b0c1ed5e` |
| P1 / primitive | `R917-endpoint-P1-primitive-order.json.gz` | 334720 | `1756e166d0f57696aef12db04fa036ecb82d9644a3f4fccbb128a6ea42a4b76f` |
| P1 / normal_order | `R917-endpoint-P1-order-001-complete-table.json.gz` | 319940 | `68d2d6d00f6fdf95b83826a46b098b5791d8265652e16a59c3ef30da1f14a345` |
| P1 / discriminant | `R917-endpoint-P1-order-001-discriminant.json.gz` | 69520 | `d5fd303919dccfadb201ac1eceafe6de189c2a013e2c5eb2a478d7d62626ff1a` |
| P1 / special_fibre | `R917-endpoint-P1-complete-length8-special-fibre.json.gz` | 6443 | `1ff4ea1a08787ee806ac74f6981334060a6d23b25cc02fdfdb1f8182a2580e8a` |
| P1 / frames | `R917-endpoint-P1-primitive-and-original-t-determinant-frames.json.gz` | 5244 | `7a20c3244907866e2c0033a8eb82c2d08234802654711896f787b70d2efef1cf` |

每个完整端点证书还引用同一 run 中的 primitive 判别式、idealizer 小核和全部新表；后继只按实际引用取件，无须重跑正规化。

## 7. Artifact 与已完成的纯 IO

真实一日 artifact 为 `14244312360`，名 `serre-R917-two-endpoint-normal-orders-43904492746-1`；平台长度 **13739001 字节**、完整 ZIP SHA256

`4ae6c58082f591a195978646039658a40c850df5c8c66803de234f29b7eb3056`，

到期时间 `2026-11-17T16:10:56Z`。

结束后只执行纯 IO：下载该完整小 ZIP、核其完整长度/SHA、核 manifest 的 184 个上传产物，再核选源 tar 的全部 40 个原成员。ZIP 另有 manifest/reference 两文件。没有在本地重新执行任何算术、正规化、判别式、核或帧计算。原产物保留于一日 artifact；Git 仅保存源码、方法、请求和本篇实证文字。

## 8. 现在可消费与仍未完成的接口

本次三个实际正面旗标均为 true：两端原正规阶、完整长度 8 代数、原 primitive/t determinant 帧。接下来可以直接在这些真实表和准确原基变换上处理 $K/P_U$ 的分母与目标正规函数，无需重做十七系数、对合、273 jets 或本次 idealizer。

以下实际旗标均为 false：特征零正规阶基展开、原目标 272 个端点坐标、五目标端点理想格、$P_0/P_1$ 的数值 Norm 校准、$\operatorname{Nm}(\Phi)\det U$ 与参考原帧的完整求值，以及 Hecke Picard 活跃支持或高度。未来 R903/R907 输入仍为空，不能由本次正规阶帧将其补成已完成。
