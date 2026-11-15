# R787：518 位新全格的实际结束与固定基行边界

本条登记公开 run **43766834526**、job **132973884134**、source **0084d2e067710af828ae071e7850764791e41300** 的真实输出。方法为[原精度增量完整核格](R787-original-precision-increment-kernel-lattice-method.md)；原 518 位输入与双入口已在[断点记录](R787-518-digit-checkpoint-and-precision-increment-activation.md)登记。不得重做已成 430 位格、旧 98 条候选或旧固定分母向量的 \(\Omega\) 结论。

## 1. 完整格已经准确取得

本次直接消费旧完整 430 位三 probe 基与已结束的原 518 位 current。实际辅助素数为 \(\ell=1000000753\)，增量为 88 位；没有计算新的 Dixon 位或重建原 Schur/大逆矩阵。

真实证书包含：

1. 全部 \(A\) 的 \(1234\times14\) 与 \(C\) 的 \(1214\times14\) 原坐标约化，原 chart、完整自由列模式及三个 probe 的兼容性。
2. 全部56个旧格行产生的 \(56\times42\) 增量残差；2352 次整除原模数均准确通过，全部168个数域 probe 同余保留。
3. 一个真实42阶单位子式，其模 \(\ell\) 行列式为 **740671961**。小42阶逆提升到 \(\ell^{88}\)，每个完整阶段保留双向乘回。
4. 显式自由参数化给完整整数核 \(K\)，新格是准确的 \(KH_{\rm old}\)，新全格指数为 \((\ell^{518})^{42}\)。没有把真子格冒作完整格。
5. 对此新56维格仅调用一次 LLL；全部56行保存，准确整数基变换 \(U\) 满足 \(\det U=1\) 及完整基等式。所有非零不同分母均保留。

## 2. 所有56个预定基行候选均未通过

run 完成于 **2026-11-15T22:31:02.655150+00:00**。core receipt 用时 **1742.313128262 秒**；最终数学证书的计时为 1742.310489445 秒。process exit 为 **2**，wrapper error 为 null。

全部56个实际新候选都执行了原准确关系评价，且其完成的否定记录均在**首个非零关系阶 \(m=1\)** 给出准确非零残差。这是完整原129阶/280坐标判据的一部分，故足以否定相应候选，无须再计算该候选后面的阶。

实际 counters 为：

| 字段 | 实际值 |
|---|---:|
| consumed_LLL_candidate_rows | 56 |
| completed_search_nodes | 56 |
| new_exact_candidate_evaluations | 56 |
| previous_exact_candidate_rejections_referenced | 0 |
| complete_new_precision_lattice_basis_certified | true |
| candidate_search_exhausted | true |
| search_time_budget_reached | false |
| search_node_budget_reached | false |
| search_lattice_budget_reached | false |
| additional_Dixon_digits_computed | 0 |

原 430 位旧否定默认没有借用到新精度；实际旧拒复用数确为零。原 \(\Omega(C)\) 结论也没有代替本次准确候选评价。源兼容记录中 old_exact_or_Omega_rejections_reused 为 false。

**数学边界。** exhausted 只指本次一个真实精度增量格的56个预定基行，不是全部整数线性组合、全部 \(D\)、全部重构窗口或原函数关系空间。LLL 是候选生成，没有成功保证。不能由上述56个否定反推518位不足、原 normalized 方向不存在或原 \(A=yB\) 不存在。没有准确展开的函数 recipe、原点坐标、\(\beta\) 或高度；相关 success flags 均为 false。

## 3. 固定来源与小回执

本次 core **414fef537020ed2acbb98e4632c6132bb5f5e5fd4561c82bfe569a7381e0a7be**，wrapper **889cdf5e646759f1ffb79d5063ca604683668f8cc6bf77ac186134eedc635c88**，method **bc91a89140d912b1e3f7da9ec9c12b742884084e60860cc408cbacb9d7b54f0f**。原完整 current 仍为 73180954 B / **4997a05b79ab9e7c7f9286fc483b1f459ff6e23fa18df5344bd8ef0eb80f10f5**。

| 实际阶段 | 字节 | SHA256 |
|---|---:|---|
| 全原源精度兼容 | 12376 | 574bccc151f16ddc883eb4ae14c0387f73fc13f2d77b27cd7b3fcc9a6da41b51 |
| 56×42 残差 | 940368 | 3e4cce9c092d038b0444722a035072d38bbd6b95cbcbbbb2c0ffd649a5340fcf |
| 42 阶单位子式 | 28744 | 93d43a6a7c12db8160bcdc5d40f2c48969e26bbcd41bf5f27d9084e48b3527bc |
| 88 位小逆 | 705746 | 5f19834f96cf1190728ab83018e4501c8bee38894d8206d39bafab350fb57290 |
| 完整核格 | 6263578 | f8f9aa315a5f506291fa271642469af060375fd1dfb612da188f807d7bc3790e |
| 完整新 reduced basis | 5453988 | 84306d1447fab845f96b8f4e78fc6ffa2170fb07d511cde7453df34f6e24f7c3 |
| LLL 全基认证 | 7126744 | 10d8676bd054e3284c82a8973ed8cdc33fe6502fe57ebddb73bf89b7868c74e2 |
| 固定调度 current | 9962 | 84e07b68ef1565d9404130813b8745e358734f962d5875af10cf10d3900e691b |
| 数学阶段 manifest | 22601 | d011c6223b05d5f728e3fa0d0e1a160245fe467666140898e7dc96e78501513c |
| 最终证书（complete=false） | 28473 | 25631ecfb4ba05b4a9a2b3c44cb9e16a96ba46f1967de2c5e9f6f6a5470f3f2f |
| core receipt | 1254 | d7e75c717abe3c9a3d71c821843adaa940dbb23ba753bdb9914780b6000429ac |
| run receipt | 421 | bf41c6957922472f2135e3d8f6f68ea90a3e4f5467466aaebf4a1be5b2138537 |
| public input | 30091 | b5846a73ae87667332348835f212e393950a941e845bca41cb9ef21bf075fee7 |
| 全输出 manifest，253项 | 75013 | 8f886d19d695c71214d979caf7e6ffae89c94c77022d8c31557070f7447ba4b1 |
| manifest ref | 382 | 2f9019bf918c1c8e25135d342413c267903e2aaee6115970e99ac30d8903d27d |

56条精确否定记录及其原候选身份由上述 current、数学阶段清单和全 manifest 完整绑定。它们均为 complete=true、not_a_characteristic_zero_relation=true，并保实际 \(m=1\) 的准确残差；原大 rejected payload 只按既定已闭记录规则退役，完成的决定及 SHA 不删除。

## 4. 活跃载体与继续方向

artifact **14183618203**，名 serre-global-R787-original-power5-function-relation-43766834526-1，大小 **318998777 B**，ZIP SHA **d259343bcc7f4bbcd6f8f05508843a1be49d2df3b3aef597317b4aa4edcbc539**，到期 **2026-11-16 22:31:03 UTC**。ZIP 共255项。

| 必要继承载体 | 字节 | SHA256 |
|---|---:|---|
| 当前518输入 | 73285192 | 666a52db1d10a5aa0b2c1eaa377e480237cb9056be337e6fd4fa54adcca0066e |
| 已成三 probe 源 | 20914740 | af211f73448cb764f3e6e2340994db63bdf5d9b778bb02b229411fc16ad85395 |
| 原 producer 输入 | 189156436 | ad0c9493b6dc6f6ed99b37c58941000c638fcad683992e9b538a81a2123ed6e4 |
| 已成二 probe 源 | 6594510 | 7d3ca58e7bb6103084d6fbf9783cbd417978a376b7d4627d19e9814511f4dd5f |

本地仅读取251个小文件（含 manifest/ref）并逐字节/SHA核对，11次 range、29123085 B 传输；没有执行新数学或重做上述格/候选。raw/向量/矩阵仅在一日 artifact，不进 Git 或 Release。

本56行入口已经完成，不原样再跑。原518位同核续算 run **43766834509** 保持进行；下一批新消费优先使用真实单位选行块的隐式特征零函数/CM响应，以及 R835–R837 的原约化除子与短 RR 核，不以失败样本取代准确包含、完整维数或原点身份。主目标 OPEN。
