# 第三独立观察揭示完整 C2 前缀的严重径向漏峰

日期：2026-11-28。状态：**有限数值证据与已见反例**。原完整前缀205径向×(128+192)角双训练组的曲率/面积峰不是连续域界。对同一非零第15步场的第三观察得到 **metric=1.2189606249507947、曲率=52181.53785185456、最小面积比σ=.13926034542480406**；相应训练峰仅 .18063669887432332、19.560625229639882、.888195756770479。不能以训练数值通过厚度或等距要求。

## 观察身份与实际源

入口 `2ecf-polar-c2-prefix-observe.py`；直接调用冻结的 polar-v2实际背景和原固定 target g。径向在54个非空 quintic span各取3点Gauss，加入全部55个break、中心0/c/2和真尾段18节点，合并共236径向点。角为 `2π(j+1/2)/256`，共60,416点。其背景六jet在这些实际角直接生成，修正六jet用实际cos/sin直接求和；没有把未错移FFT的值改标签冒作错移观察。源缓存自然退出0、618.730059928秒、峰值子进程RSS212500 KiB；底层target-definition oracle也自然退出0。该观察未参与已完成的205节点优化。

两组原128/192都已进入训练，不能把其中名为 `observer` 的组当第三观察。此处明确是不同径向、不同256半格错移角的实际第三观察。源和角均未插值、未投影，目标仍冻结原 `target-zero`；未把polar周长重新定义为g。

## 同一固定状态在训练与独立观察上的比较

| 状态 | 样本 | metric峰 | 自身曲率绝对峰 | 最小面积比σ |
| --- | --- | ---: | ---: | ---: |
| 暖15 | 205×(128+192)训练 | 0.18063669887432332 | 19.560625229639882 | 0.88819575677047902 |
| 暖15 | 独立236×256错移角 | 1.2189606249507947 | 52181.537851854562 | 0.13926034542480406 |
| 独立零起点6 | 205×(128+192)训练 | 1.2072129703972876 | 473.88912419137876 | 0.75130817134091366 |
| 独立零起点6 | 独立236×256错移角 | 1.324513281402526 | 2080.4894597110952 | 0.47118349600596643 |

暖15观察进程自然退出0/.913682981秒；零6观察进程自然退出0/.609801993秒。观察报告删除了任意观察权重下的成本，未把不同quadrature的成本冒作优化下降；只比较同一场在实际已见点的峰/谷。

| 状态 | 最坏metric位置 (s,u) | 最坏曲率位置 (s,u) |
| --- | --- | --- |
| warm15 | (0.14093749999999999, 0.012271846303085129) | (0.13718750000000002, 5.9518454569962884) |
| zero6 | (0.12593749999999998, 0.50314569842649026) | (0.1071875, 0.33133985018329853) |

这些新峰均在 [c,b]=[.1015625,.1815625] 的释放前缀。六个修正jet (X,Xs,Xu,Xss,Xsu,Xuu) 在9径向×128个未错移角上与生产FFT的同场比较：

| 场 | 六个最大绝对差 |
| --- | --- |
| warm15 | 4.71844785e-16, 3.85802501e-15, 2.59514632e-15, 6.48370246e-14, 2.93098879e-14, 4.9904525e-14 |
| zero6 | 4.78783679e-16, 4.20496971e-15, 2.83106871e-15, 6.61692923e-14, 3.28626015e-14, 5.57331958e-14 |

这是有限舍入一致性检查，不是所有连续角的严格浮点误差界。

## 极值原位重取样与独立两基本形式核验

另入口 `2ecf-polar-independent-extreme-audit.py` 打开新的实际背景/target进程，在暖15两个极值的同一(s,u)重新直接求六jet，不消费缓存作新值。两处背景六jet与radius三jet同原缓存的最大差都恰为0。曲率位置报告标签的角加法舍入差为8.881784197001252e-16，复核使用缓存的原实际物理角5.9518454569962875，未混淆标签舍入。

直接用 `I=[[Xs·Xs,Xs·Xu],[Xs·Xu,Xu·Xu]]` 和 `II=[[n·Xss,n·Xsu],[n·Xsu,n·Xuu]]` 的对称广义特征值核验曲率；独立用归一Gram减I的谱范数核验metric。极值审计进程自然退出0/1.638388060秒，其target子进程自然退出0。

| 位置种类 | 自算metric谱误差 | 自算曲率 | σ | 背景Xs范数 | 修正Xs范数 | 实际Xs范数 | 修正Xss范数 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| worstMetric | 1.2189606249507943 | 10.684869843804911 | 1.4237353447022725 | 1.0000000000033384 | 0.52790269895109665 | 1.4894097992136226 | 19.172013778857021 |
| worstCurvature | 0.98027028118957271 | 52181.537851854693 | 0.13926034542480389 | 0.99999999999515043 | 0.9145905360508787 | 0.14968109852419201 | 1034.8480988061799 |

这定位了当前误差：峰值位置背景本身Xs范数约1，修正Xs大幅抵消，修正Xss范数约1034.85，导致局部接近退化并放大曲率。它不是把背景曲率误写成修正后曲率，也不是通过观察角标签制造的峰。不能从两个已见点推出全局最大；52181.54只是一个实际已见曲率值。

## 已启动的同g补救输入

G2点在每个quintic span对导数与非线性Gram/曲率严重欠采样；它不能证明离散零解的连续行为。新 `2ecf-polar-c2-g10-prepare.py` 保留原205全部节点、第三观察236全部径向节点和全部break，逐span加入G10，共958节点、每span至少15内部点。仍使用原128/192实际角，新增源点直接重算；所有旧源行与完整12789维父态保留，目标g与原13+q2行不变，有限quadrature有变化，必须单列新基线与新接受计数。该补源正在实际运行，这里不登记尚未完成的基线或步数。未来真实观察仍需径向再加密；这次G3径向点既进入新训练，之后必须明确它在新模型上只剩角独立性，不能继续称完全独立的空间观察。

## 实际重现入口

变量 `SCRIPTS` 指课题scripts目录，`WORK` 指临时区。先完成已登记的旧源恢复及完整前缀准备。独立源命令：

```sh
python3 "$WORK/2ecf-polar-c2-prefix-observe.py" cache \
  --scripts "$SCRIPTS" --prepared "$WORK/polar-c2-extended-prepared.json" \
  --candidate "$TOPIC/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json" \
  --target-definition "$WORK/target-zero.json" \
  --ramp-master "$WORK/gap105-prefix-ramp-master.npz" \
  --coast-master "$WORK/gap105-prefix-coast-master.npz" \
  --prefix "$WORK/polar-independent-G3-shifted256"
python3 "$WORK/2ecf-polar-c2-prefix-observe.py" observe \
  --scripts "$SCRIPTS" --prepared "$WORK/polar-c2-extended-prepared.json" \
  --observer "$WORK/polar-independent-G3-shifted256-independent.json" \
  --state "$WORK/polar-c2-step15-step01-state.json" \
  --output "$WORK/polar-independent-warm15.json"
```

极值重取样同传source输入，另加 `--observation "$WORK/polar-independent-warm15.json"`；其实际退出receipt保留完整命令。所有原始源/状态/观察数组留临时区，Git只存脚本与解释。

| 输出/源码 | SHA-256 |
| --- | --- |
| `2ecf-polar-c2-prefix-observe.py` | `6390a1e038bc6c8d17459cf8dda37182297b985f1378ca456fda064a572d4353` |
| `2ecf-polar-independent-extreme-audit.py` | `2960c2eb9520d8ad08188490ea11e71a5732614ed0880dc47b8dc27792b98054` |
| `polar-independent-G3-shifted256-independent.json` | `a0f45b5032b0eec200174cbbba864355eff629f22a30ef289b75787fc56d563a` |
| `polar-independent-G3-shifted256-jets.npy` | `5a9a5ec18dd1f7ebffcdbea13f6420c8faceb36629a642864ff59dac5f4d8bfa` |
| `polar-independent-G3-shifted256-radius.npy` | `dbc2b7a47c2a384b3a8cfa74f499ffb3f70d2318b3f2efdeb8050945fdeef914` |
| `polar-independent-G3-shifted256-cache.json` | `76f467bb264d8da21b9872cea66d607578a00a9e961f40a12724ad622f847ddd` |
| `polar-independent-cache-exit.json` | `5b37e5378a0e224f41253cb101f8bdb8f58fbd844cb64474fba4f6a99bb88ee4` |
| `polar-c2-step15-step01-state.json` | `82955a105138a27ef786d6991a2f849018b496bb1737cd5adf64550ac7916b5e` |
| `polar-c2-zero-step06-step01-state.json` | `3faa387496334e0561982c1fc1e8723e889bdbef0fc88250847d460aff08868b` |
| `polar-independent-warm15.json` | `ecfe57d54154babc2c5989ffbb4848873a5b71ae5ceb0970a1498b2075190c78` |
| `polar-independent-warm15-exit.json` | `69755e413707fd1d43abd633b45a5d3344338b92dfa41ce77cd2f667ea9a1059` |
| `polar-independent-zero06.json` | `b3f41e240f664ec181e1d275d1ea7f0a7670251bad9632e792d897c192658046` |
| `polar-independent-zero06-exit.json` | `ad51502f61fe4c361d1b4d55ac73f1b3d76cc50581646792d2f803c337d1eacf` |
| `polar-independent-warm15-extreme-audit.json` | `a94a189df81a2e1d0cbf56040d0941f90a8eb87522f56679756076fafa3a1738` |
| `polar-independent-warm15-extreme-audit-exit.json` | `089568fadc656aa95049e2c763b8e88f9afd9179804cec3baaa1244c88281370` |
