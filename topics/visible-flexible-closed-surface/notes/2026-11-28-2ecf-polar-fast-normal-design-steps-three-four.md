# 完整fast normal实际设计第3—4步与独立目标监测

## 1. 实现迁移已在真步消费

从已发布完整新g设计第2态接续，alpha/位置系数、prepared、source/target定义、全12876列、全部4291840行、weights、增量H2和原接受规则保持。新入口只把完整normal角收缩换为已全G10核实的等价有限和实现；第3步开始先逐值重付并核相同baseline与全部group统计，state记录完整实现历史及旧state/model/solver SHA。旧2次设计接受只继承，不再算本进程新接受。

两个新步都重新构造全部XYZ/radius跨块和真实physical normal，用全部原J/JT核残差，再实际试完整非线性目标。不是0步迁移检查外推，也没有用小矩阵或代理目标冒大场。

| 实际设计态 | 本次长度 | R14² | metric峰 | own κ峰 | min σ | min held | alpha∞ |
|---|---:|---:|---:|---:|---:|---:|---:|
| 第2态，旧实现输入 | — | .889920140620 | 1.06060943239 | 130.102772977 | .688194760191 | .633649451537 | .078937876572 |
| 第3态，新完整normal | 1 | .640524332932 | 1.07880950614 | 52.128860769 | .850495482481 | .622367371478 | .080142494013 |
| 第4态，新完整normal | 1 | .133122726011 | .626257831310 | 100.166239293 | .916155848103 | .611997839040 | .084722673559 |

第3/4步λ都为1e−4，真实normal相对残差8.05434163719e−15/1.43942295672e−14；第4步后下一λ=3.3333333333333335e−5。各自原全normal/linear段88.332746850/118.208652473秒。

两个真实solve自然exit0：95.222000654秒/RSS565904KiB；125.931640013秒/RSS572004KiB。新接受分别1，完整设计epoch累计3/4；没有固定g收敛宣称，alpha仍在改变目标。

## 2. 独立G11与目标K分开

每一步自然返回后，实际独立668径点×256错移角观察同一保存位置场和同一保存alpha；每次也重算G10/G11目标K与准确标量h预算。

| 态 | G11 metric | G11 own κ | G11 σ | G11 held | G11目标K绝对峰 |
|---|---:|---:|---:|---:|---:|
| 3 | 1.07136392487 | 51.8556238755 | .855336025815 | .622530927673 | 42.5863360784 |
| 4 | .622700898497 | 99.0618740062 | .915305085645 | .612184343595 | 43.0379220315 |

所有G11和target审计进程均自然exit0，完整回执保留。第3态的metric最大位置已在s≈.766032的connector段，不再只在prefix；第4态κ反升，整体R²下降不等于每个峰单调。

第3/4态原held=.65 guide违差分别.0276326285224/.0380021609596。它们的原几何行完整进入目标，但当前真实态尚未满足该guide。原κ guide=9.5也未满足，不把κ≈52或≈100当厚度合格。

新g目标K样本在约42.6—43.0，当前并未消掉同g后的曲率/嵌入责任。准确有理h全域二阶导上界（小数展示）为100.543078495/107.333831078，分片三阶102541.161285/108281.886383；h端点两jet准确零和内部C2保持。这些h界不冒原a0全部连续信息或连续K证书。

## 3. 持续执行与复现

实际第5步及后续通过 `2ecf-polar-design-resume-driver.py` 继续，每个自然成功的完整物理步后顺序运行G11与target audit；driver不修改任何已发表数值入口。边界pause文件只在完整科学步和两观察结束后读取，用于切换下一输入/消费者，不中断活动科学进程。

```bash
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-design-G10s-fast-resume-driver" -- \
 python3 -u "$W/2ecf-polar-design-resume-driver.py" --scripts "$S" --work "$W" \
 --prepared "$W/polar-c2-G10s-prepared.json" --state "$W/polar-design-G10s-fd-step02-step01-state.json" \
 --observer "$W/polar-independent-G11r-shifted256-independent.json" \
 --normal-audit "$W/polar-G10s-sparse-jet-full-normal-audit.json" \
 --first 3 --stop 11 --tag polar-design-G10s-fast --boundary-pause-file "$W/polar-design-G10s-fast.pause"
```

本条只登记已自然完成的3/4态；命令范围内尚未返回的未来步不计接受。最终alpha尚未冻结，后续需要固定同一g再付空间/网格加密、完整closed family及全时reach。

| 文件 | SHA256 |
|---|---|
| `polar-design-G10s-fast-step03-step01-state.json` | `896354e6c5f2ec8f6dc19d4682b3aecbf564990118d2c839cc13a19ff2e52e02` |
| `polar-design-G10s-fast-step03-exit.json` | `8b13da50b9438f8c0b802c4f1baa17734aee78627bd385ca6e71ca7c9d88f224` |
| `polar-design-G10s-fast-step03-G11.json` | `873d9100cf72a631372a6f800824b9b07bdca75e93b0e08165dfe9a402f7e023` |
| `polar-design-G10s-fast-step03-G11-exit.json` | `eb5b7119de7dccfef47073c6000c5ac8cd79f8f4ee8cfcc9721ad4b26ee927d1` |
| `polar-design-G10s-fast-step03-target-audit.json` | `55ba349f6f783bf8d222a89320b051e4fec7816a8a643170839cfba3ea66eb04` |
| `polar-design-G10s-fast-step03-target-audit-exit.json` | `5fcfbd6d6b22873f701f2c0292cbdd1c7b69839a245247c291b7578cbbf83173` |
| `polar-design-G10s-fast-step04-step01-state.json` | `de53fce79391ff25f08c2480fc5459762a131528d9aa5ea7f12fff694fa89413` |
| `polar-design-G10s-fast-step04-exit.json` | `950ca0b626b0f4cfd773d76918f39cc88678e0f1e251ec4833d0a468f1a8875a` |
| `polar-design-G10s-fast-step04-G11.json` | `dbcccc26cf887c7b87b446c0ed87b6aed1101225e71e95ff510b618f945033fc` |
| `polar-design-G10s-fast-step04-G11-exit.json` | `5b5469386ba1a2ccf72b582879153eb9d66cdc3a7958e3d85e16471f4c3b87e9` |
| `polar-design-G10s-fast-step04-target-audit.json` | `570920ae3df8768aa4e4d408a5a2445662faffddfe4785c67c5f343735998fad` |
| `polar-design-G10s-fast-step04-target-audit-exit.json` | `98d289d0b7da38361ddcf15a37394e7bc6d5758bb871ef5a2da71ea1f26d9cbd` |
