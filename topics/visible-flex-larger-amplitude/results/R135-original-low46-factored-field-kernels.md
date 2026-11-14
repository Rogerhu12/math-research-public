# R135：保留真实 low46 Green 的逐模因子并转入 R100 规范

作者：/root（GPT-6 Astra Pro，AI 辅助），2026-11-13。状态：已证明下述算子界；尚非新的非线性闭合。

## 原聚合之前保留46模

原 low46 Green 生产器在每个模上分别构造两支齐次解和完整正源积分，再对46模逐元素取最大。这里在取最大之前保留每模的正因子：213个目标 Φ、Ψ 强范数，213个来源 μ 比值、IΦ、IΨ，以及213个完整有序对角项。原计算表达式、流程、192bit Arb 精度、全部46模、12份浅胞元面板和全213范围均未改变。只增加观察输出；没有新 ODE 或径向积分。

原代码SHA9e420455ef59285219422bdbd1fc82d7d3f15a2af9178a25fd89a2c86faee809，原聚合包31c65d6c8053325502542c008720f880d7386cd39168be79ca466851e76bb7ee。实际重放逐字段要求 gamma_upper、far_z_source_upper、rows、source_profiles、E_B_low 与该原包完全逐位相同，全部通过。原四材料全部按旧算法保留，因此不是以另一个径向范数替换旧问题。

对每模 m，源cell n到目标cell k的基材料核为：对角使用保存的完整有序项；k>n使用 μ_n Φ_k IΨ_n；k<n使用 μ_n Ψ_k IΦ_n。各分支的 P 与 κ 已在强目标因子内相加，保留原连续角宽；不能交换两支或以端点核代替整cell核。

## 精确重标及独立共同界

令 σ_j 为 R42 原 q 包络到真实强包络 Vs 的比，S=257/256，Vprime=S Vs。使用原强包已付 source_factor_base 的上端（界 σ_n²），目标用原 σ_k 的正下端。因此源 dprime=Vprime²/(r w)+|w_r/w|Vprime²/w 到输出 strong(P+κ)/Vprime 的核，额外乘 S σ_n²/σ_k；具体分配在源和目标因子上，两个分支与对角完全一致。

每个核还与 S乘原 strong gamma_upper.base 取最小，两个独立有效界取交合法。实际2,086,974个模×目标×来源顶点逐个有理检查为正，并且新因子在全部顶点已不大于旧共同界，交之前超出次数为零。总2,087,084门全部为真。第2模cell12对角是旧共同界的2.261797e-10，第46模约8.387629e-6，第92模约0.999999892；不能对第92模冒称相同的大改善率。主要用途是完整保留不同源频率的传播。

源到 far consistency 的各模列按 S² σ_n²/Z，Z=2^-2200重标。齐次 far 场列按1/(S σ_k)重标；它本身不含完整非线性 far 图的系数/导数。共同 far 比较仍独立保留。所有 N 中的均值、逆、二次及完整 Taylor 余项都必须由消费者支付；这里的基核没有预先塞入1.5或23/18等非线性常数。

## 实际运行及失败保留

观察器r1实际exit=1，31.871171s/306856KiB：原聚合逐位检查已过，但把全部高精度因子与显示字符串写进单件后超过5MB文件门，故没有保存成一个超限正式产物。失败源4ba8d1188141f5cd54bfea46e8cafa2d930412b3c5cd7e906cf58ed88015d936及真实资源完整保留。

r2只将观察值改为准确160bit向上二进制数并分六件，原算法不改；formal exit=0，32.211743s/185992KiB。源c6a07b4e72806f921af0302bbe2f759fff61e627c75d898e464a3b454ab0e589，主a12b730f9f78ed74a8d8425f0ce5b6b3a706e92733b3d153e278d17e19e51eca。

R100重标实际formal exit=0，118.850003s/143048KiB。源d1cfd155f667503ee934a4715f3434228bb27e40c96c0656154010455ab1d38c，主515def084db566b4b484bd72c4f0a5405f569a2f4daca70374e4e2b8814c19ab。其六个模分块合计约1.98MB，主约1.23MB；所有可再生块留scratch，compact包保存完整路径/SHA/大小/规范/复现pins。

## 使用与复现

先按 observer-input-manifest-v2 的27份原数据pins在新目录恢复同名notes，使用 computations/root_inner_low46_factored_green.py 加原三helper运行原命令并换新out-prefix。它会核原聚合逐位相同，再输出六组因子。随后将这些新路径和SHA置入 rescale-input-manifest，运行 computations/root_inner_low46_rescale_factored_green.py --inputs <manifest> --out-prefix <fresh>。两次均用原strong_resource_run.py记录实际退出。

重标primary.mode_kernel_parts逐件rows里：phi_target、psi_target、mu_ratio、phi_source、psi_source、ordered_diagonal均是213项；准确kernel规则随记录保存。对每模完整源向量应用该两支公式（可用前后缀和），再另加已付的真实far项。源输入是该模的弱成对质量、径向sup先于频率和；输出是同一连续strip下strong(P+κ)/Vprime。若同时使用各模帽和共同质量，还需做对应support，不能给每个模重复一份共同质量。

该结论不改变已存在场、参数域或g，不新增固定点；供R134受限域的低误差逐模传播使用，后者再反馈到高模和完整外cut。所有闭面、同g精化和全相位reach门仍独立未完成。
