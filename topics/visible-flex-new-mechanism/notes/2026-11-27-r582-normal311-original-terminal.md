# 97q normal311原终态：新0d材料上的3bc1真接受

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
可信度：唯一原Actions自然终态的数值观察；只解析原日志，没有本地科学重算。

本段8次真正metric接受，把源59a4推进到97q
`3bc11a9c80696ad3ec54066a9bf0d5cee4436081dee79b9e22b61757fe507aa1`，
完整16189×3072上的eta为 **`3.722676721935829e-5`**。
材料实际是新构造的 `0d222bd1…`，并非其source的f60；新材料及新fine的入口资格确已支付。
这是原完整有限物理门上的进展，不把59a4的连续reach证书转授给这个新q。

## 1. 原source和唯一收据

- run [45909167191](https://github.com/Rogerhu12/math-research-public/actions/runs/45909167191)，
  job `140213091600`，source `181de62c735dfa087cd62e842c191c7d226f4e0a`。
- runtime public实际pull到 `08e0b93016a795fd312f83db96ff07f444810bbd`，根与课题README
  diff均空；private实际pull到 `ebd31244c69fb695b007ec72eee5183f5edda493`，规则匹配且QUEUE仍本会话。
- entry `scripts/r582_physical_normal311_resume_20261127.py`，11793 B，SHA-256
  `2fc530a00a2a560ea2a85f33aa057ea3085c7850a568d855cc2271494b730c91`。
- request `computations/request-r582-physical-normal311-resume-20261127.json`，498680 B，SHA-256
  `28f8beb6c034ba934fb9e57b95aa7da516800d177255a43263027e6a33a1bb6a`。
- lane `actual-59a4-f60-normal311`，原stdin 482797 B，SHA-256
  `95f9118e0e196b7a5d8a992ffaba1ff335b73f329245b128543ad3c372dc82cd`。
- job `2026-11-26 23:08:58–23:49:59 UTC`，Actions `success`；子进程
  `23:09:25.980855–23:49:54.345034 UTC`，returncode0。
- 新科学 **`2427.43645062` 秒**；原时钟在下一个exact block前退出，
  `termination=scientific_clock_checkpoint_not_complete`。该实际elapsed照付，不能截成2400秒。
- 原stdout 7220660 B，SHA-256
  `9726268200ac107dbd7c7c411e13b33cba913522bb1663b7930f66c0a4985d0a`。
- 唯一原FINAL 506334 B，SHA-256
  `23bef2fbc32807204c2ee2c3bebbb646ccd740642c95de117289809504b282d7`。
- 唯一原FIELD 116368 B，SHA-256
  `00bb259bcb8c20933379ed0e0776fcca71639e85ec4db8d05012f967ffaa1b02`。

原日志只在自然结束后下载一次；FINAL/FIELD为原行逐字截取，未重序列化冒充原字节。
源字段、完整数组和费用的必要后继输入从该唯一FINAL取得；可重算原log不入库。

## 2. 新材料和入口完整资格

新FIELD实际mesh为
`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`，
62878端点，62877稳定Hermite cells；旧source实际mesh为f60。
新dense transfer付960944 RHS，weight1023386；精确core forward2510 RHS、
short-tail backward206 RHS；高度QUADPACK235893 RHS。全部属于本段新费用。
原端点阈值筛选观测2956点，未选端点jet最大 `7.838393053637985e-13`，
只是一份端点观察，不成为连续径向误差界。

入口59a4的原资格是source f60上的16149点，实际新required为16167点，
因此原START0准确写 `initial_scan_reused_at_identical_p_q_and_complete_fine_grid=false`。
新单一构造对象上完整支付16167×3072，40.659935475秒，eta
`3.838285782598227e-5`，物理和工作margin违反均0；没有把旧16149贴成新16167。
新fine SHA为 `4240c3ba1d2959ea4c5f81139ead8a1a6e1f218f6b903df1eca94156361c71fd`。

本段三个实际交换后，原START1/2/3分别在扩大到16177、16182、16189的永久fine上
完整支付同q新网资格；其eta分别为
`3.7587771584801644e-5`、`3.733793927323609e-5`、`3.731651009755743e-5`。
这些资格更新本身不算metric接受。全run只有这一个实际材料对象用于所有fine和backend；
没有另造近似场只供物理门。

## 3. 全部8次真正接受与失败候选

接受要求同候选在原全部组、fine及当前行上真实合格并严格降低eta。
下表fraction是独立物理评估副本从当时真best向原raw候选的比例，原backend数组不改。

| outer / callback | 真q SHA前12位 | 完整eta | fine径向数 | fraction | 独立e lift |
|---|---|---:|---:|---:|---:|
| 0 / 1 | `f360135ab727` | `3.7587771584801644e-05` | 16167 | `0.5` | `4.920506569959266e-07` |
| 1 / 1 | `0ccc2a0d8773` | `3.754180753912095e-05` | 16177 | `0.5` | `5.298672531243168e-08` |
| 1 / 2 | `d4e21ade7eb0` | `3.7516620393196476e-05` | 16177 | `0.5` | `4.390890826069327e-08` |
| 1 / 3 | `cea0b86028c0` | `3.748398167956271e-05` | 16177 | `0.5` | `7.057474484968552e-08` |
| 1 / 4 | `1a2d396bc2c9` | `3.7361435613595336e-05` | 16177 | `0.5` | `1.0737784347712541e-07` |
| 1 / 5 | `1faaeed68f64` | `3.733793927323609e-05` | 16177 | `0.125` | `4.849851079629129e-07` |
| 2 / 1 | `0bda03f8a3cc` | `3.731651009755743e-05` | 16182 | `0.5` | `5.7982938965691103e-08` |
| 3 / 2 | `3bc11a9c8069` | `3.722676721935829e-05` | 16189 | `0.5` | `5.583251865624552e-08` |

原其余完整fine候选没有偷用较小raw e获得接受：

- outer0 callback2：`f6d205cb4027…`，eta `3.7206832165533906e-5`，
  fine工作物理违反 `2.3884473043713633e-7`，未接受。
- outer0 callback3：`693eb8f7654a…`，eta `3.7116189564402344e-5`，
  fine工作物理违反 `2.1449588636359915e-6`，未接受。
- outer1 callback6：独立half-step `76dfd838cdef…`，eta `3.6840940227045316e-5`，
  fine工作物理违反 `.001896927452205043`，未接受。
- outer2 callback2：独立half-step `595dbcee2137…`，eta `3.7303373930489374e-5`，
  fine工作物理违反 `7.928791305399606e-6`，未接受。
- outer3 callback1：`067d51cec98b…`，fine工作违反只有 `6.88115363300934e-13`，
  但eta `3.7463245821101054e-5` 没有改善，未接受。

三次完整outer退出原因为 `uncovered fine peak exceeds current actual row coverage`，
其新径向证据和全部永久fine均保留，原工作margin不因epigraph升高而放松。

## 4. 准确终态：327实际、330仅拟定

| 终态数组/状态 | 长度或数值 | SHA-256或解释 |
|---|---:|---|
| 当前实际coarse | 327 | `6c55a5e61e09146bd8972348a3176db35ee585985b46667128b041ef0e05b440` |
| 当前永久fine | 16189 | `d6a0d6e71af4341f2ce4c64723c124835071ca1f7148fda7278c3dd053f17ccb` |
| 真保留q资格fine | 16189 | 与当前fine相同，完整3072角 |
| 尚未采用pending径向 | 3 | `.230712890625`, `.249609375`, `.25532226562500004` |
| 原拟定下一coarse | 330 | `d67124b1f5d7e01959036ff617ba269dd1189373cc89c663cc87c3af88f3a0da` |
| 实际/拟定角数 | 1536 / 1536 | 没有pending角升级 |
| 实际/拟定trust | 2 / 2 | 未伪称下一330已经优化 |
| p / epsilon | `.181` / `.0010000000000000009` | 同原固定有限问题 |

新3bc1在自身16189×3072上的physical violation为0，working violation
`2.3094850684635126e-12`，来自curvature-plus的原容差量级。
其他七组working violation均0。实际曲率最大 `16.452569169998508`，
在 `s=.8715482369363079, theta=4.71238898038469`；eta峰在
`s=.45615234375, theta=6.033657765683522`。
原mean-E范围 `.620610758052325–1.1741521871842158`，
det最小 `.6205935583977046`，ball最大 `.775759261458187`，
abs(y)最大 `.39253405092474974`，z最小 `.02`。

最后raw q是
`135e3bccf8ee50fc816c3acad03a9928b67cfcc0323ea20035a4591dff064e72`，
raw e `3.7088351809257116e-5`，原当前完整行违反
`1.428317347522942e-6`。callback明确 `complete_fine_assessment=false`，不替代3bc1。
独立回溯已到fraction `1.52587890625e-5`（16次减半），
物理组违反降到 `1.4528369826627419e-12`，但没有原要求的严格metric promise，
正确跳过新fine；没有把较低raw epigraph当作真实改善。

最后完整合格trial就是3bc1，来自raw `746bf69b4abb…` 的half-step；
独立e为 `3.7226767222911544e-5`。raw、独立物理副本、真best三者身份都保持原样。

## 5. 真实后端形态和新增费用

这里与B030“每次只有一份J即交换”不同。四个backend分别支付 **2 / 6 / 2 / 4** 份J；
前三个完成outer，第四个自然时钟退出。因此原native有机会消费MODEM1学习曲率。
当前没有H/乘子输出可恢复，但没有证据把它描述成整段BFGS学习饥饿。
下一正常物理续算无需为了复用B030的82维helper而改成一个未经审查的98维接口。

前10份J/130方向块/53 value属于已折入completed outer的counts；
当前第四backend另有4份完整J/52块/44 value，必须另计，共 **14份J / 182块 / 97 value**。
原14条J时间合计 `583.8261914330001` 秒；0次自然OptimizeResult，0次旧方向诊断重放。

| 原counts字段 | 本段值 |
|---|---:|
| `accepted_metric` | `8` |
| `backend_callback_invocations_including_explicit_terminal_read` | `14` |
| `coarse_feasible_assessments_without_metric_promise` | `28` |
| `complete_fine_radial_blocks` | `2159` |
| `complete_fine_scans` | `17` |
| `completed_backend_Jacobians` | `10` |
| `completed_backend_direction_blocks` | `130` |
| `completed_backend_value_evaluations` | `53` |
| `completed_callback_current_complete_row_checks` | `14` |
| `completed_optimizer_callback_scans` | `13` |
| `completed_outers` | `3` |
| `exact_epigraph_lifted_physical_candidates` | `13` |
| `fine_radial_points_evaluated` | `275020` |
| `fine_scans_skipped_for_current_backend_infeasibility` | `1` |
| `natural_backend_returns` | `0` |
| `new_physical_backtrack_row_assessments` | `42` |
| `physical_backtrack_halvings_taken` | `12` |
| `source_unqualified_warm_trial_entries` | `1` |

`completed_backend_*`只含前三个完成outer；不能把当前4J/52块/44 value漏掉。
17份完整fine包括4份新网入口资格和13次callback完整scan；共2159 blocks、275020径向点。
全部R604附带观察复用原geometry blocks，观察844861440个径向角点，
不额外产生AD或geometry calls，也不授连续norm或reach。

| 新模型费用 | 本段值 |
|---|---:|
| `attempted_geometry_AD_blocks` | `182` |
| `attempted_geometry_value_calls` | `2214` |
| `attempted_model_grid_constructions` | `8` |
| `geometry_cache_hits` | `59` |
| `geometry_parameter_direction_points_requested` | `665696256` |
| `geometry_spatial_points_requested` | `961162752` |
| `model_radial_points_prepared` | `65990` |

| Resonant/材料费用 | 本段值 |
|---|---:|
| `continuous_profile_radial_values` | `3166` |
| `dense_tail_radial_queries` | `62443` |
| `height_QUADPACK_RHS` | `235893` |
| `height_cache_hits` | `375` |
| `height_queries` | `3166` |
| `material_Hermite_radial_queries` | `65990` |
| `material_raw_knot_candidates` | `63045` |
| `new_dense_tail_RHS` | `960944` |
| `new_dense_tail_segments` | `160` |
| `new_dense_tail_transfers` | `1` |
| `new_exact_core_forward_RHS` | `2510` |
| `new_exact_core_forward_calls` | `1` |
| `new_material_Hermite_endpoints` | `62878` |
| `new_short_tail_backward_RHS` | `206` |
| `new_short_tail_backward_calls` | `1` |
| `radius_only_reference_queries` | `65990` |
| `resonant_field_queries` | `436` |
| `uncomputed_inner_tail_query_points` | `0` |
| `underflowed_nonzero_jet_components` | `274689` |

稳定求值另有62877 residual preparation cells和65990径向查询。
原model计数保持weight1023386、outer RHS960944，inner RHS/linear least squares/
background constructions/mean-control candidates均0，旧24/48/96拟合未回放。
所有旧primitive、core、先前真实失败及各97q正常段的原成本账完整继承；
新elapsed与其中包含的J/fine/准备时间不重复相加。

## 6. 后继输入和连续证书边界

下一正常scope准确采用原拟定330库和全部16189永久fine、原3bc1真best，
最后未合格raw仅保持原warm候选地位。新增330资格或新材料所需的完整fine仍按原规则支付；
未发生变动的既付资格不为新算法或新日志而重放。

原3bc1的mean坐标仍是q[64:80]和q[96]；q[80]属于新增tail列，不能误算进mean。
与已有59a4连续reach输入相比，这16个mean控制均发生实际改变，最大坐标改变量
`.0030383095788611425`；帽高现 `.6975711972395291`，比59a4增加
`.0007781786957408166`。所以旧59a4的完整mean参考及其连续C0/C1/K/reach均不自动属于3bc1。
本段未付新连续全域证书，不借旧证书宣称完成。
