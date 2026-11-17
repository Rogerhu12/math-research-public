# Pr602 失败终态的共同 C² 五次式：真实二 jet 转换成本

2026-11-17，geometry_amplification。**完整有限数值读出，非连续证书、非接受父。** [固定 Pr602 尝试](2026-11-17-parallel-model-implicit-frenet-newton-preparation.md)的唯一真实终态，在原8次 fresh Jacobian 预算下未接受。本条实际读保存 Y/U/a 定义的**新共同五次式**全部601胞、每胞4等分、8192角，共24,616,960个含重复端点样点。

## 输入与新场

输入 `parallel-model-implicit-frenet-602-once.field.json.gz` SHA256：
`3a7f49623d03a1534a620e3c3d69d7a64c122fc01074b197002bf08de67c294c`；生产源为已刊 `5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac`。不读 checkpoint/e313，不制造接受父。

M160/N2048、602节点、s=0→binary1.03，保存的全部 Y、独立 U、`common_accelerations` 均 finite，无缺失。最小胞宽8.251835513606309e−5；未删胞或改 jet。依[R227](../results/R227-hermite-seam-general-reference-hessian.md)/[R230](../results/R230-actual-A-finite-Hermite-cardinal-sameg-bridge.md)，每胞取唯一匹配两端0/1/2 jet的五次式，因共用节点而准确 C²。

[R647](../results/R647-polynomial-Frenet-constraints-and-complete-collocation-condensation.md)的节点 a=−CU⁻¹(CY U+CK k′)在 C≠0时仅是水平集 C=c 的切向加速度选择。读者只消费保存 a，内部求同一五次式的真实一／二导，端点直接用定义 jet；不重算旧 RHS/jvp，不把 solver cubic 的导数混入。

## 实际核心与同一标量

所有核心 Z、U水平槽、a_Z **逐字为0**，且 U_Z逐槽恰为常数1；故新映射的镜像准确 C²接合，未构造补丁。这个正则性事实不替代浸入/嵌入/reach。R0=1，首标量为1/0/.2，core metadata与实际R系数逐字相同。156个 binary support关系误差 Tj+2jRj逐项保留，未删除。

目标 rho 用本次 core 的 `1+Σ(1−4j²)Rj cos(2jφ)`，不照抄旧值。其8192角采样最小值为 **.14826804579209685**。相对 aa1 core，最大系数变化1.4271917252078382e−6，但 rho 系数 l1差准确为
`2013738415119682057037042975/9903520314283042199192993792`≈.20333561715579368，超过旧[R638](../results/R638-global-positive-arclength-coordinates-for-two-prefixes.md)下界 .159；因此本比较不能转出新 rho 连续正性，亦不表示观察到负 rho。不追加正性扫描；共同材料规范仍按 R240。

标量仍为原冻结 HoldProfile；所有节点的 a/a′/a″重新评价与保存字词差0。`scalar_nodes`只是数值评价记录，不另定义新准确g；本条未用普通浮点评价冒严格 oracle。

## 完整读出

| 量 | 实际读数 |
|---|---:|
| 最大 relative Gram operator | **5.285539583424713** |
| 所在cell/u/s/φ | 573/.25/1.0251188872103523/.7416797109427075 |
| 该点rr/mixed/angular误差 | 5.28548238881494/−.017387421678782333/−.00031574165401948573 |
| 最大主曲率绝对值 | **104463.15838500897** |
| 最大实际加速度模 | 104469.09054809148 |
| 曲率及加速度峰 | node573，s=1.0250146696075482，φ=.7416797109427075 |
| H最小值 | −.0002062693828627617，cell572/u=.5 |
| V·(d×e)最小值 | −3.6109121580377224，cell573/u=.5 |
| Gram determinant样点最小值 | .021983413403008644 |
| 首胞最大Gram误差 | 7.357895938791838e−12 |

峰值节点直接合成保存的a573，非幂基端点抵消假峰；该节点原 CU cond1估计2.5372739756063848e9、线性解余项2.0364e−11。小线性余项不控制解的幅度。原 cubic 节点/中点Gram .003089052225749451仅引用已刊终态，未重扫，也不能移作五次场界。

对同一报告汇总，除572/573外仍有Gram **.09712594144199398**（cell526）及曲率 **28678.015093558308**（cell582），不是改一个节点即可合格。全未投影点残差r0/r1/r2样点最大为 `.04857608646,19.3412016490,5.2854823888`；未保留模161–320最大系数为 `.0009984938805,.171607491898,.043588718705`。

所有样点 finite，面积和 Gram行列式样点值均正；H≤0与法向速度≤0的含重复端点样点分别20,522及285,460。新读者在全部节点把真实残差投回原Pr槽，与原保存C最大差 **2.3438711904616774e−16**，确认角规范/独立U/标量的绑定。未由样点正面积推出全域浸入，未建立连续上界。

## 冻结源与复现

[读出源](2026-11-17-parallel-geometry-implicit-frenet-quintic-readout.py)，12212 B，SHA256
`5f0528852ffec655c62f9554320118f1bafce0aaa3f84f2c33b3b74c2ad5930f`；沿用 ed0de 的共同五次定义，增加同次真实 Pr/遗漏模/正支。所有依赖入口及出口核身份。外部报告 `parallel-geometry-implicit-frenet-602-quintic.json.gz`（35258 B）SHA256
`323d8ecb5d75bfc9aa7dceda41cb5bf71f317b3d78b234eca004bedcd4fec5ae`，保全部601胞及完整最坏地址，约19.838554秒。计时字段不承诺重跑整文件同SHA。

仓库根运行，WORK为保存输入及aa1参照的仓库外目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-implicit-frenet-quintic-readout.py \
  --topic topics/visible-flex-larger-amplitude \
  --input "$WORK/parallel-model-implicit-frenet-602-once.field.json.gz" \
  --reference "$WORK/parallel-negative-hold-complete-base.json.gz" \
  --out "$WORK/parallel-geometry-implicit-frenet-602-quintic.json.gz"
```

raw/报告保仓库外。结论只否定本次保存二jet的合格几何标签，不否定该固定g、隐式方法或题目。既有 aa1/pulse 成果保持；无新接受父、闭面、全t、reach、held/D或完成声明。
