# R133：97 输入物理伴随 Hermite 提案 v2 的实际成功

## 实际结果及严格范围

公开 Actions [run 43662865692](https://github.com/Rogerhu12/math-research-public/actions/runs/43662865692)
已完成新的完整物理伴随浮点提案。数学 child 返回0，五门全部通过；
原生 producer 用时286.218807219秒，wrapper记录的实际 child 时间290.007529474秒。
这是真正完成的新伴随 QR、全部97右端列恢复和独立动作检查，不是只跑 eligibility。

完整对象包含1977个实际节点、1976个 collocation 区间、257物理状态
（128个odd、128个非mean even和独立even mean）、97个独立输入。
保存的 shared binary64 节点值与每片两侧导数定义准确连续的分片有理 Hermite 试件。
原始输入 Gram 是归一化 moving odd96加独立mean；
输出非mean Parseval权为 $1/2$、mean权为 $1$。

独立有限动作及两端残差的相对量实际为
$6.968799796965097\times10^{-15}$，通过预先固定的 $5\times10^{-8}$ 门；
最大节点动作残差 $9.631184738623233\times10^{-15}$，
最大有限边界残差 $5.329070518200751\times10^{-15}$。
这些数字属于浮点有限提案检查，**不是连续残差或真实无限帽图的误差界**。
输出明确保留 `mathematical_certificate=false`、
`complete_continuous_adjoint_bound_proved=false`、
`complete_full_cap_high_to_low_bound_proved=false`。

## 原始输入与恢复

全部7908个原 whole scalar 域和全部7908个原生 midpoint 包围都复用；
其中64个原生点来自既成补点计算。本次没有任何 intrinsic target 调用，
没有重算原7908域/原64点，也没有将原 forward 帽列转置冒称伴随证书。
原 v1 的准确已选 scalar NPZ 和 receipt 从其实际失败 artifact 原样恢复。
v1 的零QR失败 native仍为
`f6cdd51f5776ea66435212188cd5db2518f225c24c240823ee7f726e389757d0`。

v2只把每个 collocation 区间的候选 cubic 选择改为准确左端节点的
`side='right'` 分支；完整两端 containment 门不变。
全部原247输入pin保持不变，新253清单增加明确迁移身份。
固定中心仍是原ac1候选的完整连续M32修补对象，物理参数仍是固定 $\eta_0$。
首实际节点是binary64的 $0.9$；后继连续消费者必须在准确 $9/10$
使用原首Hermite多项式延拓，不能直接state[0]代替真入口。

## 完整实际身份

原生目录：

`notes/cached_cap_adjoint_proposal_v2_ci/run-43662865692-1-cached-cap-adjoint-proposal-v2/`

| 文件或对象 | SHA256 | 字节数 |
| --- | --- | ---: |
| native/complete97-cached-physical-adjoint-proposal-v2.json.gz | acb2151b60f24ad88b30e6f7d1d966851abc53c15e45df19df2bfca27c2393c7 | 4425 |
| process.json（仓库最终快照） | abe7652b659c9f2e70571f900239999f2d3cb34ca0fdd37821290b4502f139c6 | 20571 |
| evidence/complete97-cached-adjoint-proposal-summary.json | 292a4bbb3d7b036b685c7fd6d3652aed87f5dc32f3bcd31d66eb98d95d093eb6 | 5823 |
| evidence/proposal-state-inventory-index.json | 81ff1b0f80c9a3f49da8566420659cd18ed64612b6788538d72083978dcaf350 | 4041 |

科学源 SHA256：
`0bc067d92254b78e00b022beb455a30595b9713fba686639be78480c69685721`；
worker：
`de387aaf02696fb1794cb0843028d898b0f3cde21bb3816e4e67199c0ca32368`；
manifest：
`af838e4127505e8744e140833f30037f8c4103dad08f2a11dc229932666045f3`。

完整515个提案/QR/检查文件仅保存在公开 Actions artifact
`visible-exact-cached-cap-adjoint-proposal-v2-43662865692-1`，
artifact ID `14140199819`，API实际大小1125474991B，
归档digest `3878f761f55d21535ca2d99cd0a5e369c842ed6bedceb04544e2eefa6b88aa5f`。
本次仅通过connector读取小process/summary和artifact元信息，没有搬运二进制。

## 真 pull 与后继义务

实际process保存五次pull/README核验。
最后一次为2026-11-15 01:31:19.648685 UTC，
从 `4b399fc43313e73bf247cb20776653efe6e948c1`
推进到 `e6c81ee7fde76361a177ea467829cae967d5a793`，
两README的准确diff均为空；另四次同样无差异。
已读规则提交仍为 `ee26c0a65a2e63c15f2ccfba6714181584416542`。

后继须对该同一Hermite试件支付完整ordinary伴随残差、Hessian转置、
真左端97输入误差、全外Robin与独立mean、真高输出Gram，
再以完整同源矩阵费用接已安装的97右Poisson消费者。
本结果不授完整无限高逆、真实参数Schur、非零参数族转移或课题最终完成。
