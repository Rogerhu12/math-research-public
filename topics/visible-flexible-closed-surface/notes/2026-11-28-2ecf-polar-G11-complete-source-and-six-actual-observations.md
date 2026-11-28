# 完整G11错移观察源、六个真实旧场观察与新增metric漏峰

原G11 source失败后，独立新consumer按433行正式回执恢复、余107行重付，现实际完成；它没有更换原数学位置source/固定g。此条的六个旧场观察是固定场的新增空间证据，不是任何新优化接受；G10两训练组的新有限baseline仍单独付款。

## 1. 实际完整源

`polar-independent-G11r-shifted256-independent.json` 给668个实际径点、256个真实角 `2*pi*(j+.5)/256`，171008个全半域物理点。全部54个非空quintic span各含11个Gauss点，另含各break及完整尾部节点。540个新增source径点中，前433正式完成行恢复并字节比对，107重新实际求值；另128个与原G3共享径点完整六jet/radius字节保持。

新进程自然OS exit=0，外部480.634237537秒、peak child RSS259624KiB，内部480.152041291秒；目标metric oracle也自然exit=0。原失败1730.6406秒/exit1仍另记，不能删除或合成“一个成功耗时”。所有保存源行均有明确来源，恢复时还实际重采索引0、216、432要求六jet/radius逐字一致。

唯一实际fallback位于新增源行437，s=.7328699344622418，原外层失败角170。收紧内层material tolerance到2e−15，外层仍5e−14；真实返回根独立longdouble primitive：G16最大角残差6.8074886006e−15，G32为6.8087896432e−15。相同根处polar rho/logrho/z全两jet差分别不超过8.2601e−13、7.4252e−13、6.1507e−14；local arc residual4.34e−19。有限精度审计，不是连续source证界。

与新G10训练958径点比较，G11有 **540个不在训练中的实际径点**，其256角亦全部错移；与旧G2的205点比较有645个新径点。这里G11与G3并非嵌套网格；不能由某个G11峰比G3低就推断场已改善或峰已收敛。

## 2. 六个不变的实际系数字段

只读取保存z；直接三角函数求和产生 W 的全部六jet，再加该实际(s,u)处direct source六jet。没有把无错移FFT标签重写为错移。每个实际非零场另在9个物理s×128无错移角将direct三角六jet与production FFT对照，最大全六jet差<=2.2383e−13；zero0差严格为0。

| 不变场 | G11 metric峰 | G11 own-curvature峰 | G11 min sigma | 原新空间自身接受数 |
|---|---:|---:|---:|---:|
| warm3 | 2.877970923552 | 724.317697701 | .466756986984 | 3 |
| warm2 | 1.795132394309 | 2032.684042420 | .298265735058 | 2 |
| zero6 | 1.324513281403 | 2080.489459711 | .471183496006 | 6 |
| literal zero0 | .939628853190 | 106.031080317 | .246123643196 | 0 |
| warm20 | 1.205479530725 | 69268.251668145 | .121675356671 | 20 |
| zero10 | 1.272208682452 | 3631.673766875 | .423327156851 | 10 |

这里所有数为有限样本观测，不是连续上/下界。保持场不变的warm3在G3 metric峰2.730900998之后，G11找到2.877970923552，位于s=.11894289341741064、u=3.718369429834794。这个新点属于早期prefix，完全不涉及后段polar inverse恢复点；新峰来自更密径向观察，而非修改优化系数。

warm20在G2训练上的κ13.95336833，与G11真实有限κ69268.251668145仍直接冲突。独立新径点没有拯救该终态；这支持关闭原欠积分训练链、用G10全span新baseline后继续同g求解的已执行方向，不把G2训练值当连续reach依据。

## 3. 六次实际观察的进程回执

| 场 | 观察外部秒 | OS exit | 报告SHA256 |
|---|---:|---:|---|
| warm03 | 2.494524104 | 0 | `bdd2be45a0dc96c0e2ac1132fb014324c84755fa5eef88308592d6b9f8f50818` |
| warm02 | 2.321110016 | 0 | `7b4c53b9da820401df71bd6a952c24f4a279e8149c1009bcaa66c6f1eed31f5a` |
| zero06 | 2.459888920 | 0 | `110dcaebc445209e82988d5af6a38dfbf51efb722f2257ea4e99e4ecd780c01a` |
| zero00 | 2.628057106 | 0 | `d38dbd7242d87509612ec6eb31ff08dd81edfc34dc64eda74165d7e78f9d6e8f` |
| warm20 | 2.966496900 | 0 | `4a2d8cd74f4bdc6d96c89900141a7884fe861af465c3c692224f763c86afa4e5` |
| zero10 | 2.284069462 | 0 | `8582a90a41e5a6748b4c60bea5a04f258bd2157bbdc04f9d8feea1ca8ce79a45` |

各进程只观察固定状态，没有nonlinear trial、线性求解或新接受。原恢复source的live/hash消费通过全部来源检查；G10新生产父态选择将比较其自己的完整4291840行原目标成本，不使用本表或G3成本替代它。

## 4. 原位复现命令与身份

原source恢复的完整命令保存在`polar-independent-G11r-cache-exit.json`。观察例：

```bash
python3 -u "$W/2ecf-polar-c2-independent-g11-resume-observe.py" observe --scripts "$S" --prepare-entry "$W/2ecf-polar-c2-prefix-prepare.py" --prepared "$W/polar-c2-extended-prepared.json" --state "$W/polar-c2-step03-step01-state.json" --observer "$W/polar-independent-G11r-shifted256-independent.json" --output "$W/polar-G11r-G2-warm03.json"
```

W原始数组不进主仓库；公开入口、源/旧态生成方法和SHA完整保留，后续会话需实际重建而不假定临时目录存在。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-c2-independent-g11-resume-observe.py` | `13510aae185c0840293fb1957206be30cb27a285271ff82b66fac37f5682f4f9` |
| `2ecf-polar-tight-source-evaluator.py` | `5d91140712ca78df5bf8e62392ad9ddb86915a0b0197d7f3804d4d4a9fe4435a` |
| `polar-independent-G11r-shifted256-independent.json` | `9681d300b461ca13cd0f357a568d487c98ef3d15fbd45917221dd861ed254ed6` |
| `polar-independent-G11r-shifted256-jets.npy` | `75ec3f21e6eb6f3b2c17887aac7098a68e5ab897439225ef145db970124045c8` |
| `polar-independent-G11r-shifted256-radius.npy` | `f8d5110a1d53d03fc3ea2e2dce5bc47a7d64cb0ac19169a792ba93ea8a61cba9` |
| `polar-independent-G11r-shifted256-cache.json` | `4c5303828a191b401bc6e8644441f4be8ff9cb9554863c5db22ad5d7c690fb4f` |
| `polar-independent-G11r-shifted256-new-cache.json` | `c5878dfaaa00be8cbe6c73aae3418b9ea169e9fc8fd16fdad39dc1bf3add9080` |
| `polar-independent-G11r-cache-exit.json` | `25c1a2ee68c4b316ae549ee3105c3e4e89d3c04f1d64e3be8c0c28570646fd85` |
| `polar-independent-G11r-cache.log` | `3b3f98f06ea216d8128291e74bcf0d176a6105d5230e05b4113b2cc50f07a6d4` |

全时、whole closed、全域metric、连续reach与固定g加密趋解均未由这些有限观察完成。实际G10新基线/真实续步继续。
