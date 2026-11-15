# R837：原 P0 评价与固定21点铅笔的实际准确证书

日期：2026-11-15。状态：**公开 Actions 已完成原 $P_0$ 的146个 M2 评价、完整397维固定21点空间以及两锚的1213阶非零子式。** 本文登记真实输出；不把锚点计算当成原 $D$、$\eta$ 或高度已经求得。

## 1. 已完成的数学对象

沿用 [R836](R836-original-reduced-D-fixed-branch-pencil-and-short-RR-kernels.md) 的原 $Y$、$H$，以及
$$
\mathcal B=\mathcal D_{\rm cusp}+P_0,
\qquad P_0=\phi(c_0),
\qquad \deg\mathcal B=21.
\tag{837R.1}
$$
这里 $P_0$ 是原分歧点；它与用于原高度及 CM 切向量的 $P_1=\phi(c_1)$ 不同。实际计算取得
$$
U=H^0(Y_K,2H-\mathcal B),\qquad \dim_KU=397,
\tag{837R.2}
$$
以及两个有准确原 $V_2$ 坐标和尺度的截面 $u,v\in U$，满足
$$
\boxed{\quad \gcd\bigl(\operatorname{div}_{2H}(u),
\operatorname{div}_{2H}(v)\bigr)=\mathcal B.\quad}
\tag{837R.3}
$$
这给 R836 的短 RR 整商一个实际可消费的固定铅笔。原 $82^{2m}$ 尺度、$K=\mathbf Q(\zeta_3)$ 的坐标以及两个锚的清分母标量都保存在来源绑定的阶段文件中。

## 2. 真实公开运行与最终状态

| 项目 | 实际值 |
|---|---|
| 数学 RESULT | `R837-original-fixed-branch-pencil` |
| 公开 run | `43770995901` |
| 数学 job | `132986722252` |
| source commit | `fa17c77fe36fddd9df06677569984d1ea71a6b41` |
| run/job conclusion | `success` |
| 最终证书记录的数学时间 | `14.224433011999999` 秒 |
| core receipt 的总核心时间 | `14.226702526999993` 秒 |
| 已完成数学阶段 | `141` |
| 原输入文件 | `1413` |
| full manifest 项数 / ZIP 成员数 | `151 / 153` |
| 已尝试的铅笔参数 | `a=0,1` |
| 最终实际铅笔秩 | `1213` |

原 run 链接：<https://github.com/Rogerhu12/math-research-public/actions/runs/43770995901>。

最终证书中的三个数学旗标均为真：`original_P0_evaluation_certified`、`complete_fixed_branch_space_certified`、`fixed_branch_pencil_certified`。同时 `actual_D_or_eta_or_height_computed=false`，`old_CM_torsion_trace_or_Fourier_arithmetic_recomputed=false`。

本次冻结源码与方法身份为：

| 来源 | SHA256 |
|---|---|
| `R837_original_branch_pencil.py` | `5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924` |
| public wrapper | `eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae` |
| active request | `f23f455ad45cbcf53924986b2e2ecf675bb8704bf96d7067a8db7b5bc98161a3` |
| workflow | `9751c619914a5b10c07adefdc1460a1796b77f3aa5d16f27e53b21b9d961bc0f` |
| [执行方法](../notes/R837-original-fixed-branch-pencil-method.md) | `3fdfec25ee15721f62312547f18f1c2bd053d7976a2005f10dbd2c77b73b3043` |
| R836 原证明 | `0febe81e24ec578605383fcfb5eca900ad7c8176fa438649b1bc779ddf694fd7` |
| R802 原半线性下降证明 | `2e8a3b19685d6f607d4f1b000c98e34a98370aa54a98ffeeb2c59e892ba393ca` |
| R790 原 CM 证明 | `83303dcd6abc65875d8c67eb8977126db1c85cf3e9dafb3fbd2881163aadfc39` |
| 实际数学 configuration | `1fbdd4c7173879f69cac92f39b2c485a583deb1cada140b4ac9afadc7d2622f9` |

## 3. 原 P1 到 P0 的评价运输已准确完成

本次直接消费 [R790](R790-certified-original-CM-fiber-jets.md) 的146个原 M2 CM 值以及 R786 的原 $V_1$ 前缀。按 [R802](R802-original-semilinear-parity-and-degree-seven-relations.md)，原反射把 $q_Y$ 变为 $-q_Y$，把 $t_Y$ 变为 $1-t_Y$，并把 $P_1$ 运到 $P_0$。原偶权线丛的运输因子为1；$E_4,E_6$ 保持不变。这里没有再插入 $g_\star$、$\eta^{12}$ 的符号或新的 CM 周期。

原 $V_1$ 的 $q_Y^0,\ldots,q_Y^{13}$、40个 $\xi_{41}$ 坐标给 $560\times146$ 有理矩阵 $S$。实际选行块 $A=S[I,:]$ 的146阶子式为
$$
\ell=1000000009,\qquad \det\overline A=780670146\ne0.
\tag{837R.4}
$$
对 $P_1$ 评价的两个原 $1,\zeta_3$ 坐标分别准确解转置方程；原反射在选定 Fourier 行上只作用 $(-1)^n$。得到全部146个 $P_0$ 原评价，并对原转置方程完整准确乘回。评价所带的原整数尺度仍为
$$
82^2=6724.
\tag{837R.5}
$$
本次没有重算任何旧 CM 挠点、域迹或 Fourier 系数，也没有生成完整的146阶反射逆矩阵。

| 输出 | bytes | SHA256 |
|---|---:|---|
| `R837-original-V1-reflection-minor.json.gz` | 2567 | `237ec9c58cc86956be7e999d13fdf4e7672e1d8969b23e7a5e3e1729be5a9cf8` |
| `R837-original-P0-evaluation.json.gz` | 21063 | `2e41a7ec7a73401fd2f5d770c5ef6c4d8d722c38312026a5c6a0f906aedf58c7` |
| `R837-original-V2-P0-evaluation.json.gz` | 28665 | `0671c2bc0dfd8942dfdf90c21039e658df29f3c3e8b91292d833e7659a302421` |

第三项由原 $V_2$ 的已认证乘积 recipe 与上述原 $V_1$ 值相乘得到，保留 $82^4$ 尺度。它没有将原有限域 M2 recipe 的系数冒充准确 Fourier 系数。

## 4. 完整固定21点空间及实际锚

原 $V_2$ 的尖点常数项评价秩实际为20。其非零20阶子式为
$$
\ell=1000000009,\qquad \det=756065994\ne0.
\tag{837R.6}
$$
准确求出全部398维尖点核，并在全部40个原 $\xi_{41}$ 坐标中乘回。随后在该核中加入准确 $P_0$ 评价，实际约束主元为原核坐标0，得到完整397维 $U$，没有将一个子空间称作完整 RR 空间。

| 输出 | bytes | SHA256 |
|---|---:|---|
| `R837-original-V2-cusp-minor.json.gz` | 2128 | `52d5b002e00525e08e0cfb6bd8017e21a1c4e6ffe67fb5c0f6dd3665aa7f1575` |
| `R837-original-V2-cusp-kernel.json.gz` | 233915 | `4e7ccc514761099f7f1750bd29776fd121799233b00d9fcf2cc5108e26a04f08` |
| `R837-original-fixed-twenty-one-point-space.json.gz` | 469328 | `f13254045b0a019c36c9380f6404b5f2c3d185e266a0f2d3251328cb951b5ef4` |

记这个原有序基为 $U_0,\ldots,U_{396}$。第一锚由 $U_0+U_1$ 按原清分母规则取准确整数 primitive 坐标，含22个原 $V_2$ 非零项。第二锚由
$$
\sum_{j=0}^{396}a^jU_j
\tag{837R.7}
$$
同样准确规范化。成功参数为 $a=1$；其原 $V_2$ 支撑含418项。

这里的实际 $u,v$ 是上述规范化后的原截面；`primitive_normalization_scale` 和未规范化坐标都同时保存在输出。后继若比较主函数常数，必须按该标量运输，不能只保除子类或把两个锚无声地重标。

| 实际锚 | bytes | SHA256 |
|---|---:|---|
| `R837-fixed-first-anchor.json.gz` | 3453 | `d57929a0075dde31513dbf586c00eabc01619448753578e2363076b21259b01c` |
| `R837-second-anchor-parameter-00001.json.gz` | 9574 | `c827059c209e1b5a80c57e7126b94a182483a83fd511389738ceb38e03959ecd` |

## 5. 1213阶真子式证明没有额外共同零

实际计算原乘法
$$
V_3\oplus V_3\longrightarrow V_5,\qquad (s,t)\longmapsto us+vt.
\tag{837R.8}
$$
使用 $q_Y^0,\ldots,q_Y^{68}$ 的全部40个原 $\xi_{41}$ 坐标，形成 $2760\times1380$ 矩阵。这里保留完整尖点轨道的准确坐标；没有把40个坐标替换为一次 $\xi_{41}$ 数值代入。R786 原 $V_3$ 前缀直接复用，只计算此前不存在的锚乘积。

本次的两次实际结果为：

| trial | 参数 a | 素数 | 原 ζ3 的模像 | 实际秩 | 固定21点铅笔认证 |
|---:|---:|---:|---:|---:|---|
| 0 | 0 | 1000000009 | 115381398 | 900 | false |
| 1 | 1 | 1000000009 | 115381398 | 1213 | true |

第二次使用的1213个真实坐标行及1213个真实乘积列均已保存，其子式满足
$$
\det=665846025\pmod {1000000009},\qquad \det\ne0.
\tag{837R.9}
$$
第一锚在同一素数上的全部乘积块由两次 trial 共享；没有因改变参数 $a$ 重算已成 $uV_3$。成功 trial 引用82个完整乘积块。

R836 的原 RR 计算给：若两锚的共同零为 $\mathcal B+Z$，则(837R.8)的特征零秩为
$$
1213-\deg Z\le1213.
\tag{837R.10}
$$
实际非零1213阶模子式给特征零秩至少1213，因此 $\deg Z=0$，准确得到(837R.3)。这是完整共同零除子的结论，包括闭点及其重数。trial0 的秩900只记录该模试次的结果；它不被当作一般特征零失败的证明。

| trial 输出 | bytes | SHA256 |
|---|---:|---|
| `R837-trial-00000-result.json.gz` | 8976 | `ea4a7337715cc81f72050442461e529a2a5ea3838d20d718a24b8b56bbd1ad83` |
| `R837-trial-00001-result.json.gz` | 11471 | `6e86cee4f02ef5c7055f5c55038215b8eae2f7ca13b78966b7f2c847c70278cf` |

## 6. 原输入与完整输出绑定

本次消费的两组旧源为：

| producer | run / source | 原 full manifest SHA256 |
|---|---|---|
| R790 | `43688215703` / `9e4074fd9c99ab3af6bfad363b674e57f938800f` | `49b5ccda0bbe3bc9d06a263fa3b15632f34b97ce518bc3825002583fb74afa60` |
| R786 | `43682100611` / `dd262672a8b1e2af82277b15e0fa766038609670` | `e3c29e85236c8cc665bdf88e9ffd2bbab9180b6f977f0b2b22f54266762f405a` |

实际选择146个 R790 CM 行、R786 的146/418/690个原 power1/2/3 行以及必要原 metadata/index，共1413文件。完整逐文件身份在本次 source inventory 中。没有携带与本次消费无关的原 R775 大 carrier。

| 本次总接口 | bytes | SHA256 |
|---|---:|---|
| `full-outputs-manifest.json` | 26808 | `fe2aee5e584b5e6e8800d2ef30ff17ed76fdfb349d5f783880c1e08cf7a64e43` |
| `full-outputs-manifest-reference.json` | 217 | `ff1da93e938c2b64a2dc1d7f4ad101736d1808809b324db8984a888ba843d636` |
| `p41-original-fixed-branch-pencil-certificate.json` | 5040 | `83234905bd30dd774ec4fd4ed6bfaef46f7bcacc1ff8fe0f5b00e4119ca31eb1` |
| `R837-stage-manifest.json.gz` | 9664 | `4cae97c2b31a9a1fd024849d84580c289c6b1ee26649766e51c7938345236a71` |
| `R837-original-source-inventory.json` | 246426 | `eba630491f6306e7f95a322a05eaf71c0bd11bb7c80226919879a5bb879c053c` |
| `R837-retained-original-inputs.tar.gz` | 29497132 | `c17f51a91c2bc2a93ac7184fa0876998d766218f99790e700daff945687cea6d` |
| `public-actions-input.json` | 5303 | `db7aadcd9ea5108ed65032654eb868e5ffcc3b77040158b3222c03d866efe245` |
| `core-receipt.json` | 644 | `04b78eca25723b25ee4401b7033e67c1c0e754bda370b2aa0c021c389aeb0b1d` |
| `run-receipt.json` | 442 | `f2a72e5ea61e5ea1622a3a78d79a0490d135a1774179121389873a918b3855b5` |

实际 artifact 为 `14184475817`，名称 `serre-global-R837-original-fixed-branch-pencil-43770995901-1`，48599362字节，平台 ZIP SHA256 为 `ea610ed2142ca7ad563d49803002aaccd6b81b0888173265e826caabc68d0864`，到期时间 `2026-11-16T22:45:47Z`。原矩阵、坐标和 carrier 仅作活跃接续用的一日临时输出，不提交到 Git 或 Release。

本地纯 IO 读回使用11次 Range、共19129315字节，逐一验证152个非 carrier 文件以及141个完成阶段的原配置与 SHA，并以冻结 public wrapper 对已缓存的1413个原输入重新做来源/字节/schema 检查。它没有导入数学 core/flint，没有重算评价、域运算、秩或子式，也没有再次下载29.5 MB carrier。ZIP 的整体身份沿平台 digest 绑定；此次局部 Range 传输未冒称重新哈希完整 ZIP。

## 7. 下一消费的准确边界

现在 R836 的 $u,v$ 已经是实际原截面，后继可直接用其原坐标计算短 RR 整商。尚需从真正完整的 $T_m=H^0(mH-E_2)$ 来源构造相应乘法核；单个 B 的若干导数列不能未经完整性证明就代替该 RR 空间。实际固定锚不改变原 $\eta$ 的三同源主函数修正、全局常数、$\beta$ 或规范高度。

本文不登记 $D$ 的准确坐标、原 $\eta$、原函数 $y$、CM 点 $\beta$ 或指定高度多项式 $T_p$ 已经完成。它完成的是原 $P_0$ 评价、完整固定21点空间以及 R836 所需的确切两锚。
