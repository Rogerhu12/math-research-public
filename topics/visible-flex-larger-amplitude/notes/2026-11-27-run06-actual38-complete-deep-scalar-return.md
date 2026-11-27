# Run06 actual38：完整固定 deep scalar 的两个真实方向与未驻点边界

本条记录公开 run **45904402595/1** 的第38步 `complete-fixed-deep-scalar-amplitude-first-20261126-rebuild06` 实际返回：completed，exit=0，791.6168632489998秒。它是本次完整父链的必要重建；不把旧run04的结论或字节直接转给新run06，也不重复宣称原课题已完成。

## 1. 实际来源与整输入身份

原完整小卷为 [run06 part003](2026-11-26-public-actions-45904402595-1-part-003.md)，本次完整读取的固定 Git blob 为 `a81afbe128abe6d11ff76db14a7309654d30e484`，**56787 bytes**，完整 SHA256 `b9e67fd697fef3fa576836eb16304bf14d022bce7fe9ef5e771ef39b9903744d`。root先核实际size再读完整小卷，并逐值比较其完整actual38 record；代理临时文本多一个尾换行的56788-byte版本不被冒称此原公开对象。

| 角色 | 实际完整身份 |
|---|---|
| source commit | `3043e5ac4c0e740a786f40b940c02b3980e24c3b` |
| launcher | `b458ee7656bd44b82ffa996b9be4d32ecf71d1ad6fa75e181e1c4dc4bc4a0d88` |
| driver | `d3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95` |
| 实际 profile | `364e73ce2ed258b923c0dff10a1c4dfdc846e143930d4c56b55944d0d2c18853` |
| 真实父 bundle | `aebb8bd5f8158e9158e552509a6ddd240ae12cd814d31bf5e18b1bc450e3816a` |
| 真实 final bundle | `d466ef7605281dcb951f821fe2de08953c53eb3a021a08a436f9529c6af4de04` |

该步骤真实取到的queue仍为原76950-byte版本，path commit `7a771e602bbdb8ee25a845d8d690b27e2e4896bd`、checkout `9d158091ba660d7b9fc679fd90057c572a9c5e6d`、SHA `88681682ff4865d4f15d6585f312314a4d48acf044b970b9c6d768c258e9a8c9`。后来已刊的[29–35完整归档和current-PCG准入](2026-11-27-run06-returned-parameter-archives-and-complete-current-PCG-admission.md)逐值保持本38及36–40全部对象；不能将该后继queue时间倒填到本次actual input。

## 2. 新run内的完整实际进展

| 读数 | initial | final |
|---|---:|---:|
| 此入口有限 max-relative-Gram 读数 | 0.016536480593973855 | 0.01426432970666691 |
| 原 Phi | 0.0008446466076168624 | 0.00032735551888962906 |
| 原 centered merit | 0.0008443266076168626 | 0.00032703551888962917 |
| 有限 K 必要筛 | true | true |
| 原 amplitude 必要筛 | true | true |
| amplitude physical g | −0.047989034643628914 | −0.04784623969218671 |
| 完整已知 curvature 地址数 | 2733 | 2737 |
| 完整已知 radius 地址数 | 2728 | 2731 |

`complete=true`，两方向均实际接受，最后mu=.01；`known_set_complete=true`只指该入口的全部已知材料地址责任。完整原报告及其来源仍是集合身份证据，计数自身不证明两个集合相等。末有限曲率乘积为0.9919954367406946，H=1.8784180371944992，直径点对下界4.096339824437384，点曲率读数8.072209820278939；最坏点(s,phi)=(1.0282499999999999,1.2946797849754812)。这些有限读数不成为全连续reach、整面operator norm或最终幅度证书。

## 3. 两个完整线性子问题尚未驻点

| 实际方向 | alpha | QP advances/status | projected gradient | tolerance | J / J* 次数 | 实际方向秒 |
|---|---:|---|---:|---:|---|---:|
| 0 | .5 | 64 / iteration_limit | 0.005880969293001908 | 1.4545134006167126e−7 | 67 / 68 | 230.1672809189995 |
| 1 | .5 | 64 / iteration_limit | 0.0037113809337059257 | 8.323066550187895e−8 | 67 / 68 | 230.86176768800033 |

方向0的原centered merit从0.0008443266076168626降到0.0004908883617140412；方向1再降到0.00032703551888962917。acceptance和停止原因分别记录，不能用已接受推出QP驻点。原192行与5个追加幅度行均保，行cache记录4156832216 bytes，峰值RSS 2738456 KiB。实际参考误差字段为a:2.41717124027056e−13、I:6.568544714666212e−11；不迁为完整表面六jet费用。

唯一summary_error是旧模板索取不存在的 `stopped_before_linear_iteration` 键；missing_outputs为空。它是已返回完整报告的摘要路径缺项，不是新科学失败，也不填一个假false覆盖缺项。清理记录只针对已返child的四个生成cache，8313664432 recorded bytes；原父/输入/实际报告和最终场不在其清理范围。

## 4. 实际输出，不转存原raw

| 实际相对输出 | bytes | SHA256 |
|---|---:|---|
| `deep-fixed-scalar-amplitude-first/report.json` | 29175711 | `3c73dcf93d2ba758051f405f4c2524689cf50fd3ce7fd8edf91f3ebb23d533be` |
| `deep-fixed-scalar-amplitude-first/final.npz` | 10380030 | `d466ef7605281dcb951f821fe2de08953c53eb3a021a08a436f9529c6af4de04` |
| `deep-fixed-scalar-amplitude-first/exact-tail-lift-profiles.json` | 20580 | `f5c4f6ae4c39e7b60322d84460c3e85d56930c6e6aade3c09df17051e7d0bfcd` |
| `deep-fixed-scalar-amplitude-first/exact-tail-lift-profiles.npz` | 150630 | `35087b80560f0d16ad73fb2c0bfbc7ad1dc9a54602afc04b4b546d8a8944256b` |
| `deep-fixed-scalar-amplitude-first-command.json` | 29282 | `761b61d76916cf423e286f8414760abaabe98000a3a95632cf527343fbc2c858` |
| `deep-fixed-scalar-amplitude-first-inputs/complete-current-positions.json` | 175557 | `1964e53a7559a8e56b081a00c55f13acca79f66e84f4221d21d5ad8a8114be6a` |

29,175,711-byte原报告、10,380,030-byte最终场及其他生成raw均未下载或整读；这里只使用正式公开小记录的实际SHA/size。完整source/参数/实际command、input/output/parent/summary/cleanup证据已在上述小卷保留。

## 5. 原实际完整调用与继续责任

以下是原record的完整argv，每行一项，不删除任何参数：

```text
/opt/hostedtoolcache/Python/3.12.14/x64/bin/python
-u
/home/runner/work/_temp/visible-larger-research-45904402595-1/followup-sources/0010-a9179ae50e40-3043e5ac4c0e/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_deep_scalar_amplitude_actions.py
--repo
/home/runner/work/_temp/visible-larger-research-45904402595-1/followup-sources/0010-a9179ae50e40-3043e5ac4c0e
--work
/home/runner/work/_temp/visible-larger-research-45904402595-1/research
--bundle
/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/seed.npz
--preparation-report
/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/report.json
--carrier
/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/observations.npz
--node-report
/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/nodes.json
--scalar-input
/home/runner/work/_temp/visible-larger-research-45904402595-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz
--manifest
/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/locations.json
--eta-start-node
885
--angles
2048
--stage-block
64
--marked-diameter-budget
4.2
--witness-lower-budget
.9
--amplitude-height-floor
1.01
--damping
.01
--directions
2
--maxiter
64
--active-rows
192
--qp-atol
0
--qp-rtol
1e-6
--reach-safety-factor
.992
--active-band
.025
--spectral-p
4
--spectral-epsilon
.001
--spectral-scale
.05
--target
1e-9
--scalar-admission-seconds
300
--scalar-integral-tolerance
1e-18
--scalar-tail-cutoff
1/8
--outdir
/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-amplitude-first
```

06继续原39–40、已准入的四个normalized-history步骤及完整current-PCG单次入口。后继父/模型/位置/μ必须来自本run真实输出；后继新表示要重读自身初场和Phi，不按本次更小的finite读数预先宣称优于另一表示。07的完整独立新包络入口保持运行责任。课题全部连续条件、同g真实mesh/频率精化至原容差、可复现多t网格与严格存在缺口仍未完成。
