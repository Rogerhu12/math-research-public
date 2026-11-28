# G12新实场：自身全域有限门、全时几何及三时刻完整闭网格

日期2026-11-28；Astra-visible-flex-2ecfcd69-20261128。

本条只消费新实际field `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`、原Q-free source、原g、同一真实grid和R226。没有借M48/G6或任何更早场的微分、曲率或网格证书。

## 同场完整连续度量

已有R252局部p/背景斜率消费者在本场全部487原径片上完成488子片，全部角度及固定cuff/caps由原结构覆盖。自然exit0，339.156065875秒。完整相对metric上界为

`78936776886462232222149/79228162514264337593543950336` ≈ 9.963221963181383e-07。

它通过1e−6，但没有到原主求解容差B=2e−9。最宽处仍是W元素16的原prefix transfer，并非有限采样热点。原d0、中央C和尾V的余项没有删除；此条没有宣称README第5项完成，也未将有限采样约5.44e−10提升为连续界。

## 同场全时几何

R249以128角盒、Taylor8、max-radial-depth=0、quick-first=2e−6、quick-second=.05完整消费全部487径片，外部489.722214094秒自然0。这些仅是求界工作参数，未改变实际曲面或物理阈值。材料二jet界为0.02259283371287788，位移界2.263166831012096e-07，总微分界2.505866096014856e-05。

R249旧全局CX转移本身只给reach/D≈.02993547837，其旧triangle metric≈5.01437e−5，均保留未通过事实。随后R253确实以本次R249报告和本场前缀局部p重付区域转移，完整158个prefix片/全部角，自然0、外部14.085966705秒。前缀p≤3.932373302e−7乘原prefix CX，尾用自身总p乘原尾CX=26；不是改小原物理常数。得到：

| 全时量 | 准确有理界的小数展示 |
|---|---:|
| 全曲面主曲率上界 | 8.490840706935957 |
| 直径上界D | 3.787020716595303 |
| support下界 | 0.7368569381190908 |
| reach/D下界 | 0.03109937246508692 |
| held/D下界 | 0.05278309846330713 |

准确reach下界为 `141277922160585546079857532171870560126034951605013207926882887447758862532598916159001708059652915095779934208/4542790126044772090256108683158711470715348420938698180217533238006245616120098162790267117559141158753431563715`；准确held下界为 `773289641785725968707392484412423/14650326795864182394439656109765625`。原非全等活动矩、点点固定帽H及全欧氏含反射论证依相同位移预算原转移条件保持。全时间由既有F_alpha=R_alpha F_0∘tau_-alpha结构覆盖，固定帽另按原恒等式；没有以三个时刻替代连续时间证明。

## 实际完整三STL

现有v2网格入口核上述两份连续报告的实际field/grid/result身份并通过有限门后，原完整生成器自然exit0、外部8.495983841秒，内部7.941764704秒。216个均匀材料角、每侧prefix64/tail32段、反解真实native角，中央/桥/有限尾/深collar/两帽齐全。

每份44714顶点、134136边、89424面，Euler=2；所有边恰有两个反向邻面、所有顶点使用、环带/两极扇连通。固定帽3458顶点在三时刻序列化float32逐字相同。全部三角非退化，正有向体积，二进制读回一致，float32顶点误差实测<5.961e−8。

| 时刻 | STL SHA256 | bytes |
|---|---|---:|
| 0 | `35ae84ff330d0cdcfc7db6f241410f843c3221d175521df670847f50abf09aef` | 4471284 |
| 1/4 | `6d94e6f957a050fbb9585cf985881c8225bec0b999507c63957f41ade2a70318` | 4471284 |
| 1/2 | `e90790e3e31d669c81129b34d4ee73225b9a4130b6ff0cfec0447f0912d5778d` | 4471284 |

有限STL不替代连续插值误差、自交排除或同g收敛；清单的READMEComplete/fixedMetricRefinementGatePaid/continuousVertexErrorCertified/discreteSelfIntersectionCertified仍false。

## 身份和完整重生参数

- R249报告 SHA256 `a3acf6055e3a937aed730abf033957edf1ae0e9b0afb81ee602abcda10e2096a`。
- R253报告 SHA256 `e9debef013807560ee7156b683fe5a07f51d7f2b6768d71e92c884223975b60c`。
- 完整R252报告 SHA256 `d4ca6987174c769962d6eb10207a3ccfcc2c66abc9a5898e7607ce4fb19598b4`。
- 几何自然退出回执 SHA256 `d38163d3f0ee805e74fde4e2713835cf210967b0f263c7dded4e5972e22d6607`。
- 完整网格清单 SHA256 `c0f9624c5e01888c79a62de810a69c60423dd507b41608a576b3b6313cc5802b`。
- 网格自然退出回执 SHA256 `af80b230c24e71e53e9149c5759777ab2aedefcf247b74a220dd50e838411193`。

先按同日G12单band实际场note重生原输入与真实新field。下列变量S为公开scripts目录，W为该重生工作目录，G为原G12输入目录，F为04r1真实field目录，O为新输出目录，E为本场完整cross-Gram报告；不得传另一场报告。全部输出必须新路径。

```bash
python "$S/2ecf-m12-local-material-two-jet-budget.py" --scripts "$S" --data "$W/m12-prefix-data.npz.gz" --grid "$G/grid.json" --field "$F/result.json.field.npz" --result "$F/result.json" --correction-bounds "$F/correction-bounds.json" --source-bounds "$G/original-source-bounds.json" --angular-cells 128 --taylor-degree 8 --max-radial-depth 0 --quick-first .000002 --quick-second .05 --out "$O/material.json"
python "$S/2ecf-m12-regional-source-normal-geometry.py" --scripts "$S" --data "$W/m12-prefix-data.npz.gz" --grid "$G/grid.json" --field "$F/result.json.field.npz" --result "$F/result.json" --correction-bounds "$F/correction-bounds.json" --source-bounds "$G/original-source-bounds.json" --two-jet-report "$O/material.json" --out "$O/geometry.json"
python "$S/2ecf-m12-certified-field-closed-mesh-v2.py" --continuous-metric "$E" --continuous-geometry "$O/geometry.json" --scripts "$S" --data "$W/m12-prefix-data.npz.gz" --grid "$G/grid.json" --query-report "$G/exact-tail-queries.json" --query-cache "$G/exact-tail-queries.json.npz" --field "$F/result.json.field.npz" --result "$F/result.json" --angular 216 --prefix-intervals 64 --tail-intervals 32 --out "$O/mesh/manifest.json"
```

R252完整命令沿用同日local-p-slope-cross-Gram note的全部原参数，只将field/grid/result/correction/fine metric改为同04r1输入；源query和原primitive不变。R249源码c7e5f4c…fb632，R253 0b62fcd8…21296，R252v4 138062ba…3942，网格v2 4de40ab1…ad476均未修改。全报告/原始数组/STL仅为临时可重算数据，不提交Git/Release。
