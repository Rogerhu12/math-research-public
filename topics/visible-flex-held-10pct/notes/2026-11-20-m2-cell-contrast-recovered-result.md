# m2 平衡 cell 对比：恢复的八条实际有限诊断

维护：Astra-held10-1b6d88ec-20261120。**可信度：实际有限线性传播与背景采样；不是非线性容量或闭族证明。**

本地环境恢复后，原作业57647的 record.json 与日志仍在。记录完整包含七个 contrast 设计及选中设计的细传播，共八行；没有重新执行。原执行器终态/exit code没有恢复，不能为它补写，但以下文件与各行数据可以实际读取。m3 82514、n4 18524/2919的文件仍无terminal，当前进程表也未发现相应进程，不改判其数学成败。

## 固定和改变的量

源码 mode2_cell_contrast_design.mjs 读取 mode2_valley_parameters.json，只逐次改变 prefixR 为1.125、1.25、1.5、3、4、8、16；每次重算真实tail装配、物理传播与径向warp校准。rCut=.3、wCut=.08、width=.25、背景curvatureBound=8，原valley/warp/cap参数不改。七个contrast是七个不同物理度量，不能当固定g精化。

每个设计用 diagnosePhysicalMode(tail,2,96,48,0)；背景几何只sampleTailGeometry(tail,32)。再对原96步选中contrast=16做384步传播。所报threshold是源码定义的采样线性化角支正性量，不是非线性允许振幅上限。

| contrast | propagation steps | linear threshold | cut slope |
|---:|---:|---:|---:|
| 1.125 | 96 | 5.58879354960774e-05 | 11.7428792013584 |
| 1.25 | 96 | 5.8399712303216e-05 | 11.745056702101 |
| 1.5 | 96 | 6.26079013020277e-05 | 11.7492308709822 |
| 3 | 96 | 7.60165670441237e-05 | 11.7660988284181 |
| 4 | 96 | 8.00742112720279e-05 | 11.7734210839756 |
| 8 | 96 | 8.62297882365171e-05 | 11.7910264307766 |
| 16 | 96 | 8.83747579181992e-05 | 11.8072121833712 |
| 16 | 384 | 8.83705810473522e-05 | 11.8069195932694 |

## 解释和边界

contrast=16的384步值为8.837058104735218e-5，较96步低约4.73e-5的相对量；这是同一个背景的传播分辨率对照，不是完整曲面等距误差的精化。更细结果的瓶颈仍在首cell第三段，x=.9921875、r=.2391649712203156、w=.0016519376827715511；不是深端。背景采样经向曲率最大7.999442965266091，仍没有截面间的连续余项证书。

本轮改善了这个有限线性指标，但没有得到新的非线性tail、真实DN、闭合曲面或固定g收敛。不得把另一物理profile的旧H/q直接与此阈值拼成严格q上限；也不因此排除其他cell设计或非线性支。停止对本七点结果的重复扫描，主线继续材料圆弧与完整前缀—尾匹配。

## 复现与来源

先按既有 portable_bootstrap.py 恢复原source bundle，再运行：

~~~bash
node topics/visible-flex-held-10pct/scripts/resume_transfer/mode2_cell_contrast_design.mjs \
  "$SOURCE_TOPIC" \
  topics/visible-flex-held-10pct/scripts/resume_transfer/mode2_valley_parameters.json \
  /tmp/held10-m2-cell-contrast
~~~

只保存源、参数与散列；可再生record/best-config及内部数组不入Git/Release/CI artifacts。

- 源 SHA256：d898bf2af4dac3b8482a8cf611ab48a5e43103dbfdd634180f49f4d4b86c81cd
- 输入参数 SHA256：c730178ed3830a33ecb85136ac09482cade9f0feb2dcffc5822c23a5a3db663b
- 原record SHA256：d697d837a72227826d1b80a5d001ce4485ddadfc95b55fa17fc90cf98248345b
- 原best-config SHA256：dd4219af9aa581ea8fc44daeba7b8df1b689bb40a322514af44e29ff223f8d66
