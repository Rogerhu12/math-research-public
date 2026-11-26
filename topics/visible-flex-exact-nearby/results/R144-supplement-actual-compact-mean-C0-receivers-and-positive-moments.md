# R144 补篇：紧支撑正矩与完整 C0 接收量的实际结果

2026-11-26，visible-exact-astra-198c63d-20261126。

**公开 Actions [45787608966/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45787608966) 已完整完成52个声明量，并证明紧支撑正矩的下界严格为正。** 科学与执行记录的 complete 均为 true，科学 proved=true、failure=null，唯一 child 返回0。这里 proved 的精确含义仅为完整52量及正矩门；小根、非线性均值小球、非均值方程和最终闭等距族没有被这个标志证明。

[完整科学原件](../notes/compact_mean_c0_receivers_ci/run-45787608966-1/compact-mean-c0-receivers.json)与[完整执行原件](../notes/compact_mean_c0_receivers_ci/run-45787608966-1/execution.json)已整件读取并由两名审查者独立核对。对应解析定义为[CR](R144-supplement-complete-C0-mean-receiver-and-compact-moments.md)、[CP11](R144-supplement-profile-weighted-mean-feedback-polynomial.md)及[固定执行合同](../notes/2026-11-26-R144-compact-mean-c0-receivers-contract.md)。

## CA1. 同一原对象与完整覆盖

本对象仍是原 raw candidate `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413` 在固定参数

$$
\alpha=\frac{6890507429876859}{9007199254740992},\qquad
\nu_0=-\frac{2572625729470897}{72057594037927936},\qquad
\eta_0=-\frac{7789843107295549}{4611686018427387904}.
$$

原完整 mean native 的 SHA256 为 `e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b`。五个原 parts 从固定历史提交46f127c7153f5393dcd2a00f42d4c1d3662c294d逐字恢复，当前15件输入全部按bytes、Git blob和SHA256准入。原 intrinsic object身份及原半宽10^-9整盒保留；此盒在这里仅包围原固定η₀中心。没有将它改名为Qrepair或selected δ*。

| 实际范围 | 已接受完整数量 |
|---|---:|
| 正向原共同闭格 | 7721 / 7721 |
| 原均值接口 | 6143 / 6143 |
| 新加权核的反向闭格 | 7721 / 7721 |
| H前缀闭格 | 1753 |
| 真紧支撑闭格 | 1156 |
| 公开完整标量字段 | 52 / 52 |
| 原已成 whole scalar 仅读次数 | 4 |

终态径向右端是25/8，H前缀右端是9/50，反向cursor为−1，`scalar_scope=complete_whole_target`。原首轮执行没有未提交的private trace尾部。

## CA2. 实际得到的量及它们的用途

四个旧标量是已保存的Γ、mean row sum、nonmean row sum和全部mean interface log。原Γ、旧row maximum、旧Green、残差、primitive、DFT、forward W均没有重算。新的完整量包括：

- CR的ordinary、nonmean、全部mean-jump和加权ordinary C0接收界；原L²→L²数不当作C0界。
- 全域mean上下界、variance、密度比、βK等原系数的本次所需完整界。
- 在[1/20,9/50]上的两个归一化正矩 ā、b̄，以及H前缀。
- CP11的全部11个完整profile source kernels，及与真反向cursor一致的11个suffix和11个maximum。

KJ按CR10保留右侧τ注入和终端跨越的T^-1；连续新mean仍须补原−[m]跳。11个反馈核使用原逐格系数与χ、χ²的准确有理积分；没有把其支撑扩为全域，没有重复原Green目标。

实际保存并读回的严格门为：

| 门 | 实际结果 |
|---|---|
| compact_leverage_positive | true |
| actual_forward_endpoint_consumed | false |
| actual_small_root | unknown |
| actual_nonlinear_mean_small_ball | unknown |

因此CD中的正矩分母已得到实际严格资格。未来小根仍须一个独立合格的D_R/H_R界；随后CP11的完整S/L门还须实际通过。直接对完整forward求值或从同一terminal方程导出上界，必须各自说明其同对象证明，不能由本文件的complete代替。

以下六件记录逐字抄自完整52量，表示球 (midpoint_integer ± radius_integer) × 10^decimal_exponent；它们不是省略半径的点值。其余46件与所有scope/身份仍在上面的整件科学原件中。

~~~json
{
  "K0_ordinary_mean_C0_upper": {
    "decimal_exponent": "-80",
    "kind": "complete_decimal_ball_v1",
    "mathematical_direction": "upper",
    "midpoint_integer": "59525433897736093953566020263146413064442597196990169108742673212396883025311183",
    "radius_integer": "2"
  },
  "KJ_all_common_jumps_C0_upper": {
    "decimal_exponent": "-79",
    "kind": "complete_decimal_ball_v1",
    "mathematical_direction": "upper",
    "midpoint_integer": "14953841848107665259325079226656420630438489849516826520475310721533468709899520",
    "radius_integer": "2"
  },
  "K_betaK_weighted_ordinary_C0_upper": {
    "decimal_exponent": "-80",
    "kind": "complete_decimal_ball_v1",
    "mathematical_direction": "upper",
    "midpoint_integer": "23334770816663150008955519628220628530658185720442857929767830748025091437994945",
    "radius_integer": "2"
  },
  "C10_profile_kernel_upper": {
    "decimal_exponent": "-81",
    "kind": "complete_decimal_ball_v1",
    "mathematical_direction": "upper",
    "midpoint_integer": "14235287688159617935251199229424017472537717606393623433586206500221651583176772",
    "radius_integer": "2"
  },
  "abar": {
    "decimal_exponent": "-82",
    "kind": "complete_decimal_ball_v1",
    "mathematical_direction": "enclosure",
    "midpoint_integer": "45695933063269516579873097104402364250175198365218362044496000381156616531864781",
    "radius_integer": "456218369552305885238026198802358496514286650329647952403893024251817685417985"
  },
  "bbar": {
    "decimal_exponent": "-82",
    "kind": "complete_decimal_ball_v1",
    "mathematical_direction": "enclosure",
    "midpoint_integer": "16967924621484206601552445831187075666980142221962502239115287569596518011272895",
    "radius_integer": "167700007260237996915308989244704361052507310521967291325886390176340240236545"
  }
}
~~~

## CA3. 保存、读回与实际身份

每个已接受正向格和反向格均原子保存其完整标量状态。private trace共有15442条、24578707B，SHA256为`c0df9de3396e07568d50713558d2ac85967f4b1e7028897bebd96ec9e3c0da3b`；worker独立重读真实文件核hash，未提交尾部为0。其数组未入库、未上传artifact或Release。所有声明old-call counters为0。

完整球先写盘并实际parse，之后才置complete与正矩门。执行没有把前缀的零weighted state解释为完整上界。若失败，其代码只恢复最后atomic状态并截断private尾部；本次实际全两遍均完成。

| 原件 | Git blob | bytes | SHA256 |
|---|---|---:|---|
| science | d6ab32745806327b1afa5c0be38c41050c7e6046 | 16007 | 0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641 |
| execution | 403e562f321d9059778d637a8049315c725b1176 | 12471 | 9e21d438e609b207274e6a510d7e7b3ce87522e19a3547635206ab609a91bedc |
| manifest | d4f30ca95d1a1accb31ddf9b1f8d1a1c87ed5f24 | 10945 | 9f2ae6850b56799356a8fd5aac2b2cdb2de62efb077f76e05327851ba88d8aff |
| science source | 37e46058c88514507e26dea0c1be8d5a0bc16357 | 27706 | 2f94b9a223fa99e63b2971c22f37796123b601565feb403ab81d2704438661a8 |
| worker | b075a2044e9b42882040dfb347a5f5c5f5aa4549 | 36216 | 0b4b13b17f349b17d49d22d8bcdfd8a707c25712c6755e1cd79d581b5b28c173 |

事件提交6a651d271e5c5b8f7f42e7f2918568720318db8c；实际科学checkout为`084f0740bb673c1684e7c11b42792dd44c344336`。runtime为Python3.12.14、python-flint0.9.0、numpy2.3.5、320bits。执行始于2026-11-26T08:58:03.426168+00:00，结束于2026-11-26T08:58:40.363990+00:00，child0；5次真实pull/README核对均无规则差异。

此完整目标现在锁定只读。后继应使用这些正式whole球，先证明同原初值的小根和统一mean球，再处理新中心的完整ordinary/divergence残差、所有raw接口和物理同角C0。原selected相位、逆、far height与cap匹配都不能直接继承。
