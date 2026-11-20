# R141 完整正区 Newton 普通源：首次公共消费合同

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**状态：新科学尚未执行。** 本合同只安排 [同成员与正区源证明](../results/R141-supplement-selected-member-and-complete-positive-Newton-source.md) 的七个新标量。已成的7296残差生产器、CRA核心限制、4650系数生产器、7721完整方向源、full-delta方向包络、所有 Green 与逆目标均只读，禁止重算。

## 1. 同一成员和准确新范围

固定原物理 $\eta_0$，$Q_\delta=Q_0+\delta Z$、$\nu_\delta=\nu_0+\delta$，centre 和 direction 定义分别为
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47、
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04。

新源界覆盖 $|\delta|\le10^{-10}$。原 NIF 的选定同一对来自 run43588332723/1、loss $1/250$，满足 $|\delta_*|<9.368259853002\,10^{-11}$，所以可限制到它；不把 $\delta_*$ 换成零或半径端点。R141/低族差/真实高图的 $10^{-8}$ 范围也只作同样限制；WOBSA 保持原 selected-member 资格。

使用 ordinary $dr$、原归一化 moving circle 与物理幅度 pair $L^2$。完整独立 even mean、真实根、原 angular frequency4、所有物理外行仍在。新的积分域只为 $[9/10,25/8]$；$[r_*,9/10]$ 连同真根 germ 直接由 CRA 已成全核心 bound 限制得到。

## 2. 全部只读输入

仅恢复原两个完整 gzip native 的原字节：

| 原完整对象 | Bytes | SHA256 | 原 lossless parts |
|---|---:|---|---:|
| 全7296 raw moving residual | 4592623 | 6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1 | 3 |
| 全4650 positive coefficient rows | 6223338 | ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d | 4 |

三份 raw 历史记录来自原 CRA inputs 的 historical_native_receipts，immutable commit 为 7c130fb94528de8f003a43e7049fb42768a64eec。四份 positive 历史记录原样取自已发布 X inputs。新清单只将 raw roles 改成 original_raw_part_0 至2；保全部原 path、commit、bytes、SHA，并附精确 Git blob SHA。positive roles 保持 original_positive_part_0 至3。

worker 恢复每个 part、核压缩及 payload 身份、按原 offset 拼接原容器，再核整原 native。完整 temporary native 不发布。无需恢复7722 angular、root germ、candidate 数组或7721方向行；本次用不到新的这些行积分。

以下完整小报告连同其原 execution/process 只读：

- CRA43757468943：原 new_core_restriction 的 full、low 与完整 quadratic contribution，保持同一 choice，不与 fallback 拼接；
- Z43613560173 finish：同一 full_body 的 full_through160、low193、high97_through160，全部 raw mean 与 repair 已付；
- full-delta body43615531666：完整 A0、angular_A0 方向增量包络；原源码明示 $10^{-8}(H+E_Z)$，所以精确乘 $1/100$，只缩方向，不缩 centre repair；
- NIF43795909913 与 WOBSA43844596176：同成员、原固定物理参数与范围资格。

所有 current pins 在 runner 中按原相对路径物化到 private snapshot repo。science 的 --repo 和 --manifest 指向该快照；后台 pull 不改变正在读取的数学输入。

## 3. 七个新标量与顺序依赖

令 $F_{\rm raw}^+,E_{\rm rep}^+,N^+$ 分别是证明 N6、N11、N15 的三个新完整尾端量；令 $C_{\rm full},C_{\rm low},C_{\rm quad}$ 是 CRA 三个原球，$S_{\rm full},S_{\rm low},S_{\rm high}$ 是 Z 三个 whole source 球，$d=10^{-10}$。

| 顺序 | 新保存名 | 准确新公式 |
|---:|---|---|
| 1 | new_outer_tail_raw_physical_residual_L2_upper | $F_{\rm raw}^+$ |
| 2 | new_outer_tail_continuous_centre_repair_L2_upper | $E_{\rm rep}^+$ |
| 3 | new_outer_tail_selected_nonlinear_remainder_L2_upper | $N^+$ |
| 4 | complete_outer_tail_selected_Newton_full_L2_upper | $F_{\rm raw}^++E_{\rm rep}^++dS_{\rm full}+N^+$ |
| 5 | complete_positive_selected_Newton_full_L2_upper | $\sqrt{C_{\rm full}^2+(\text{saved4})^2}$ |
| 6 | complete_positive_selected_Newton_low193_L2_upper | $\sqrt{C_{\rm low}^2+(F_{\rm raw}^++E_{\rm rep}^++dS_{\rm low}+N^+)^2}$ |
| 7 | complete_positive_selected_Newton_high97_through288_L2_upper | $dS_{\rm high}+\sqrt{C_{\rm quad}^2+(N^+)^2}$ |

第一至第三条分别全尾完成后保存；第四条只消费其读回 upper；第五条消费第四条读回 upper。第六、七条也只读前三条已保存 upper。三个 Z 球来自同一个完整 source，两个 CRA 最终界来自同一个核心 choice，余项来自其原全核心 remainder；不使用上下界相减，也不把一个 family enclosure 解释成参数点值。

原 $f_0$ 的完整支集只到96，故第七条无需低背景项；完整 $s_0$、二次及三次余项仍分别到160、224、288。这不是未知解的截断。

## 4. 固定 owner 接口和保存

新 owner 为 fourfold_codazzi_positive_Newton_ordinary_source_owner.py，纯核心为 fourfold_codazzi_positive_Newton_ordinary_source_math.py。CLI：

    --repo SNAPSHOT --manifest SNAPSHOT_MANIFEST --manifest-sha SHA
    --raw ORIGINAL_GZIP_NATIVE --positive ORIGINAL_GZIP_NATIVE
    --restoration-receipts RESTORATION_JSON --out NEW_RESULT

restoration JSON 含 original_parts 的完整7条回执与 restored_natives.raw、.positive 的 bytes、sha256、parts；可附原 index SHA 和 observed blob，owner 完整保留。manifest 中 pure core 角色为 math_core，science 角色为 science。owner 不运行 git，不调用旧科学模块。

owner 定义的 PARAMETERS、TARGETS、GATES、SCIENTIFIC_FIELDS、REQUIRED_ROLES、RETAINED_SCOPE 与 runtime 由 stdlib AST literal 读取进清单，不导入 owner 或科学库。固定 Python3.12.14、python-flint0.9.0、320bits，三项 BLAS/OMP 线程环境均显式为1。whole current/native/process/partition admission 完成后才导入 flint。

每条新球以完整80位 Arb 文本原子保存，读回并证明 contains(original directed upper)，再供后继使用。完整成功要求18门全过、7条记录原顺序齐全、36个外字段匹配，且所有旧目标、旧导入、新数组/artifact/Release计数均为零。

任何失败保存已经完成的整条 scalar prefix、真实未完成积累量及其覆盖端点、目标、actual returncode 和失败原因。未完成积累量不称 whole bound，不默认补零，不创建 dummy future 输入，也不自动重启科学。science wall cap900秒、worker child timeout1200秒；当前消耗 marker 是首次目标的唯一标记。

## 5. 公共运维与范围

worker 先发布 consumed marker，然后运行唯一 science child。每次真实 pull 立即核根与课题 README，30分钟至少 pull 一次，变更按已审规则处理并保完整回执链。marker 与结果 publication 的 non-fast-forward 立即 pull --rebase 再 push，循环直至实际成功；empty index 不得误判未推 commit 已存在。

容量界仍为200000000字节，reserve120000；science最多60000、execution最多70000，总publication最多140000。只发布完整小 scalar outcome 或真实失败 prefix、执行元数据及哈希。暂存原 native、逐格数组和私有输入快照都不发布。

即使七量成功，它们也只给同 $\delta_*$ 的 ordinary Newton 源 $-f_{\delta_*}$ 大小。N21 的真实外端物理 mean 残差准确为

$$
r_C=-\{m_\delta(R)^{-1}-C_{\rm ref}
-c_0(\mathcal Z_\delta,f_B)\},
$$

其中 $1/m_\delta$ 才是 physical mean。该数值、真实 Robin 残差、height/gauge、negative/root/interface输入、全低高逆与两 WPN RHS 均没有在这七条里免费完成。
