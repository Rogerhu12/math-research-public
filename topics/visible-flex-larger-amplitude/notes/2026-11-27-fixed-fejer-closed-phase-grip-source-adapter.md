# Fixed Fejér：完整闭面、物理相位、握持与整像幅度的来源适配

## 1. 本文件的对象和实际范围

本文件实例化原完整端口与相位证明，供独立命名的 `fixed_fejer_complete_closed_phase_grip_evidence.py` 使用。算法父体是完整 `run10_complete_closed_phase_grip_evidence.py`，70,086 B，SHA256 `f7a10d7d6050cd57b5aea72d374c33662bf0c88e4175b6f7b738d6331d0976be`。原父体、原输入、旧结论和未完成责任均保留。

实际新目标由 [R717](../results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 的预定 Fejér 配方与原完整 R690 标量法则定义。七项有理配方各经 RN-even binary64 后作为准确 dyadic 系数；其余153初始项为正零。只有前三个当前 core 词固定，其余157个及全部 SO3/H 自由量保留。新图不是旧优化 core 的复制。

[实际12输入记录](2026-11-27-run12-actual-fixed-fejer-input-and-reference.md) 已确认 maker/reference 两步返回0。纯数学目标为 `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`；本次工作参考模型为 `ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac`，完整参考定义为 `50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319`。这些不同层次的身份不混用。原2218叶完整尾的请求精度仍为false。

本文件不提供未来场点、snapshot、全域误差或几何数值。下述结论均须完整新场的准确消费者实际付清前提。源码、准备完成和某个小进度记录都不等于闭面、reach或幅度已经完成。

## 2. 完整当代来源

| 角色 | 完整来源 | SHA256 |
|---|---|---|
| 固定输入 maker | fixed_fejer_r690_reference_inputs.py | 89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60 |
| 固定参考 | fixed_fejer_axisymmetric_reference.py | e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb |
| 支撑内参考 | fixed_fejer_supported_meridian_reference.py | ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a |
| 完整 base | fixed_fejer_supported_so3_meridian_operator.py | 552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3 |
| literal Q | fixed_fejer_literal_zero_moment_input.py | ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3 |
| 完整 normal | fixed_fejer_normal_lift_operator.py | 1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778 |
| 实际 packet | fixed_fejer_immutable_normal_root_packets.py | 1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468 |
| 完整科学 | fullclosed_fixed_fejer_immutable_point_so3_qp.py | 477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd |
| 完整 pure | read_fixed_fejer_immutable_point_so3_report.py | 274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b |
| 六文件/recipe 绑定 | fixed_fejer_reference_input_binding.py | 3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f |

新的完整准确费用来源如下，均绑定同一实际模型、全点、全部原根盒/分支和准确物理六 jet：

| 角色 | 完整准确源 | 字节数 | SHA256 |
|---|---|---:|---|
| input | fixed_fejer_normal_packet_accurate_field_input.py | 32991 | 1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f |
| radial | fixed_fejer_accurate_reference_control_radial_boxes.py | 45317 | c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4 |
| normal | fixed_fejer_complete_normal_root_and_sixjet_fees.py | 40294 | 1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35 |
| leaf | fixed_fejer_complete_physical_leaf_binding.py | 47321 | ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c |
| geometry | fixed_fejer_continuous_gram_curvature_support.py | 46689 | fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b |
| bridge | fixed_fejer_complete_geometry_support_beta_bridge.py | 20810 | ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15 |

共享准确算术完整源 `29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b` 与原 R650 消费者 `e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991` 不变。新的六个准确入口只在本次完整新来源、全对象一致性与明确的 R717 直径改进处变化；其完整交付说明保留实际派生范围。

新 normal 的源变化已由[完整九下层交付](2026-11-27-fixed-fejer-immutable-normal-lower-family.md)记录：53个缩进方法中只改构造器的支撑种子 schema 字面量，其余52个完整方法原字保留。不可写点存储、绑定键和同链复用保持原准确方程与末次完整原式重读。这里不重做原已登记的算法比较，也不从缓存或工作根推导准确分支证明。

## 3. 参数端口与闭 C2 拼接

原[完整端口和相位审计](2026-11-27-complete-normal-closed-phase-and-grip-source-interface-audit.md)、[原run10来源适配](2026-11-27-run10-closed-phase-grip-source-adapter.md)及 R715 的物理公式按参数适用于实际新模型。需要核对的对象仍包括完整 source、完整 base/reference 对象、全部157个自由 core 词、整个1,333,370维点、当前高度、全支撑参数与全部32阶段。

准确物理公式仍为
```text
U(s,phi) = (1-h(s)) P(phi) + h(s) Gamma(phi)
           + integral_0^s T(q,phi)dq - (1-h(s)) integral_0^S T(q,phi)dq,
h(s) = 1 - 10(s/S)^3 + 15(s/S)^4 - 6(s/S)^5.
```
完整 raw closure lift 仍在；没有把工作 Fs 直接当作单位向量，也没有设 raw defect 为零。

固定零 SO3 径向行仍严格为0、2766、2767。core 的一、二阶与cap的二阶 SO3 jet保留原自由度。两个 Q 支撑、gamma 支撑及种子修改支撑都必须严格位于(0,S)。准确标量的端点单位支和非负竖直分量来源必须来自真实新参考。消费者仍核全部系数的固定/current rho正性、完整[0,2pi]准确分支及真实连续物理叶。

core六jet为 Gamma、ez、Gamma_phi、horizontal U_ss、0、Gamma_phiphi。下片采用 Jz U(-u,phi)，Jz=diag(1,1,-1)。在u=0，函数值、两一阶导数和三个二阶导数逐项相等；这是原完整带符号反射，不删 mixed jet。

cap六jet为
```text
U = R er(Theta0) + H ez
Us = -er(Theta0),  Uss = 0
Uphi = R rho0 et(Theta0)
Usphi = -rho0 et(Theta0)
Uphiphi = R (rho0_prime et(Theta0) - rho0^2 er(Theta0)).
```
通过 r=R+S-s 与固定 Cartesian 帽拼接。完整 p4 支撑处于严格帽内圈，帽边缘为平坦 collar；所有原控制、scalar、共享Hermite节点与参考转换仍由准确完整物理流负责。

参数域是[-S,S]×S1再附两张Cartesian闭盘，拓扑为连通闭S2。完整准确上片浸入、分支粘合及严格帽collar付清后才得到C2闭浸入。此时尚未先验假设嵌入或向外定向；这些随后由全域 R650 正支撑证明。

## 4. 全物理时间与同一固定度量

物理相位保留 R248 的准确材料角共轭：
```text
alpha = pi*t/2, t in [0,1],
zeta = Theta0^{-1}(Theta0(phi)-alpha),
upper = R_alpha U(s,zeta),
lower = Jz R_alpha U(s,zeta),
caps = fixed Cartesian p4 graphs.
```
固定rho0全正后，Theta0为全圈光滑可逆图。其两材料导数
```text
zeta_phi = rho0(phi)/rho0(zeta),
zeta_phiphi = rho0_prime(phi)/rho0(zeta)
             - rho0(phi)^2 rho0_prime(zeta)/rho0(zeta)^3
```
全部保留。不能仅旋转一个旧fixed-phi网格来拼帽。

对已经完整C2的U，紧参数域上的组合连续性给出整个t区间的强C2连续；不声称t在C2 Banach空间可微。活动度量固定为 ds^2+(a_R690(s)rho0(phi))^2dphi^2，材料共轭正好保持这一固定度量；全域relative Gram算子误差由原归一化坐标变换保持。下片反射保持主曲率大小；固定帽的目标就是其固定诱导度量。因此实际活动全域metric界与完整端口责任均已支付时，才可推广到全闭面和全t。

R248仅自动处理活动像，不自动处理固定不对称p4帽的all-phase reach。所有活动—活动、活动—帽、帽—帽 mixed pair 必须由下节共同正矩阵或另一条完整证明覆盖。真实mesh、频率和t精化仍是独立实际任务，不能以相位公式替代 README 的精化证据。

## 5. 全域共同支撑、向外性与 reach

原九个证据角色保持：当前场、物理六jet、全部活动域/接缝、闭球面浸入、全物理相位、完整D、活动曲率、固定帽参数，加原带符号径向扩张。完整支撑stream逐叶实际复读；每行必须来自同一全点和准确位置/法向盒。

共同矩阵严格为 A_beta=diag(1,1,beta)，beta>0。它与所有z轴物理旋转交换，因此同一个参数同时用于全部活动相位、反射和固定帽。原 R650 给出全闭面嵌入、向外性以及
```text
reach >= min(sigma/max(1,beta), 1/K)
```
的充分条件；K=0按原无曲率限制分支处理。不从已经假定的嵌入反推正支撑。

原选择保留：先求达到0.03D的参数区间；不足时仍保留真实严格正支撑候选，用于如实区分“正reach已证”和“README比例未付”。不改任何阈值或只选择一部分叶。完整field/cover/source/claims与全部support chunk仍由原 beta consumer实际消费，独立参数不充作新g上的仿射变换。

## 6. 同一完整场的D与整像幅度

新准确geometry使用原完整圆柱上界，并另外从每个同一三维位置叶取得范数上界。若全部上片叶的范数最大上界为L，准确R上界为Rplus，则
```text
Dplus = min(Dplus_original,
            2 max(L, sqrt(max(Rplus,1/5)^2+(abs(H)+1/1000)^2))).
```
反射和z轴旋转保持范数，固定p4两帽包含在所写帽范数界；所以这是整个形式并集、所有mixed pair的直径上界。没有把一个点的最宽水平位置与另一个点的最高帽位置错误拼成更大半径，也没有省略某个帽或相位。闭面前提未付时它仍只称形式集合界。实际输出保留原 `formal_reflection_fixed_caps_all_rotation_set_diameter_upper` 键及新增完整范数来源，旧消费者可完整复读统计。

完整当前core必须从实际全点恢复所有160系数，而非继承R717初始X/Y。用其准确有理词求
```text
X = 1 + sum c_m,
Y = 1 + sum (-1)^m c_m.
```
t=1时四个真实core像点为(0,±X,0)、(±Y,0,0)。对每个点，求它到每个上片完整三维位置盒、每个反射下片盒以及两张完整固定帽盒的距离下界。先对所有目标盒取最小，再对四个源像点取最大。独立全水平hull的合法下界也保留。z坐标、所有帽和完整目标域都参与，不能用core-to-core、材料点位移或仅活动像替代。

该数是整体Hausdorff距离的合法单向见证下界，不作任何刚体对齐。宽盒给零只表示当前包围未分离，不能声称曲面全等或真实Hausdorff为零。完整闭面前提未付时，主报告清除可用的几何幅度结论；原形式集合计算另存。

强目标仍为 delta_hold>=D/5；旧D/20字段保留其原含义，不能用它完成本题。实际初始Fejér设计约束不能代替当前自由core、真实整像距离或完整D。

## 7. 固定握持和包含反射的非全等

握持域是固定上帽半径9/20的闭材料graph盘。实际帽半径必须允许该盘且保全部原p4支撑。投影直径给出diam(H)>=9/10，故0.2D条件需要真实Dplus<=9/2。这个必要的实际比例检查没有被强制写入求解器为额外变量限制。原具有内点、逐点固定以及仿射张成空间的证明按完整p4配方保留，包含反射的逐点稳定子仍按原证据判断。

delta_E的证明另交完整 R716 消费。闭面源只输出同场、完整主报告绑定的未标记外管副件。未标记闭族必须先用自身活动支撑、平帽和曲率求正reach tau0，再严格证明1/1000<tau0，才能用四个固定柱体作实际体积矩加法。不能用标记面的reach循环证明未标记面。

本消费者不声称十二个矩通道、正体积或非零中心化不变量已付。后继 R716 要真实读全部角域/径向域和十二通道，完整same-point/model/snapshot/target相等，方可使用包含反射的Euclidean非全等不变量。

## 8. 真实输入文件和稀疏源码

本入口通过新完整准确reader消费实际 normal/source/input 对象。固定图身份从 `context['actual']['fixed_chart_core_sha256']` 读取；完整target、纯math recipe和reference model各有独立字段且由3da复读全文件和全模型。旧90e6 chart与旧e711 target不再是此消费者的常量。

完整当代110个科学角色和准确源全部保留实际路径/字节/SHA。原算法父proof继续以原名和原散列保存，不能将原run10实际输入记录改标为新结果。当前proof单独命名并由完整代码固定散列。

controller只稀疏检出本topic。原题完整README位于另一个公共topic，因此若缺少该文件，proof loader只用当前冻结提交的 `git show HEAD:topics/visible-flexible-closed-surface/README.md` 取回完整原文，先核其既定SHA `d0119679e6c4d855f1f322fa6daa68cd2a30c795b14d0b124e6674459855fc23` 再放入同一detached源树。没有下载新科学输入、改变原题内容或另作数值检查。其余完整proof均按原路径核验。

## 9. 完整主报告、晚失败和后继合同

实际输入为 `{work}/fixed-fejer-continuous-gram-curvature-support-v1/report.json`，输出为 `{work}/fixed-fejer-complete-closed-phase-grip-v1`。完整8 argv保留原4096 support-chunk行数；全部57原scalar selectors保留其意义。分chunk仅是持久化划分，不截域。

R716必须从实际主报告开始：complete严格true、status为complete-same-field-consumption、all_bound_input_and_generated_evidence_bytes_rechecked严格true，且当前完整producer SHA相符。再使用主报告 `R716_outward_tube_evidence` 唯一列在 `generated_evidence_records` 的完整file record。副件须指回真实主报告路径，并与完整point/model/snapshot/target/geometry/normal binding逐项一致；孤立副件不构成证书。

不同后继step的源worktree绝对路径可能不同。保留原source/proof记录并实际复读，当前副本另记完整字节/SHA等号，不改写原路径来蒙混缺文件。晚失败清除所有已提升标志，complete/recheck改false，原中间副件不得再被当作已完成证据。

## 10. 本次源码构造的范围

完整派生器保留原70,086B父体身份、每处精确文字替换、全部后继身份和严格逆向还原。变化只涉及新完整来源与schema、动态完整图/目标绑定、原题源的必要材料化及明确实例说明；所有原端口、完整target距离、支撑选择、所有phase、握持、原beta证据和R716主副件算法保留。

没有执行本地Python AST、编译、Fraction科学算例、field/root/jet或数值fixture；这些也不是实际科学运行的新增前置门。本说明是源专属证明接口，实际未知场和所有未付误差仍未知。课题须继续到README全部标准真正完成。
