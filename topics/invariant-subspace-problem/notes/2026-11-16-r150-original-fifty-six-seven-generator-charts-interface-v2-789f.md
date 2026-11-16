# 原56个7×54临界图册：执行与消费接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

~~~sh
python 2026-11-16-r150-original-complete-fifty-six-seven-generator-charts-v2-789f.py \
  --presentation-out PRESENTATION_OUT --minor-out MINOR_OUT --six-out SIX_OUT \
  --out OUT --seconds 90 --memory-mib 512
~~~

只依标准Python；不重新求解16 RHS，不读大六mean多项式。完整固定输入与两个SHA见同目录inputs-v2。
实际v2已经7.132909848005511秒/exit0；首版错误是实际旧标签schema未对应，独立失败身份保留。

## 三个索引域

母68列中保留0…49及61…67为准确57列子集。
选中的56个是80原minor中原系数unit所选列，不是任意56个。
每个degree3来源标签先核minorIndex及六维全零multiplier，再取同一个原minor的rows/columns。

若原minor rows=R、columns=C，则原模行E=6+C、原关系主列=61+R；
其他七行K、54列rest按原顺序保存。不得把minor的row/column解释交换。

## 全部图册与精确来源

原矩阵按E/K与pivot/rest分为A,B,C,D，A是原mean minor的转置。
每chart保存：

- $\delta=\det A$、$\operatorname{adj}(A)$；
- 完整7×54列 $\delta D-C\operatorname{adj}(A)B$；
- 完整18×54源 $\delta S_R-S_P\operatorname{adj}(A)B$；
- 三条消去graph $\,\delta m_E+m_K C\operatorname{adj}(A)=\mathcal G S_P\operatorname{adj}(A)$；
- 全部原行、原列、源标签与两方向映射。

数据中没有参数逆节点。数学意义是仅在该原$\delta$可逆时，上述多项式矩阵给完整原商。
56个$\delta$已生成$(y)^3$，故这些图册完整覆盖Bell=1。rank3仍在覆盖内。

每chart仅存对共享baseArithmeticDag的扩展，baseNodeCount=105774；
节点编号小于该数者来自母图，以上者来自该chart的extensionNodes。
禁止把不同chart的扩展节点混用。全部原leaf继续按母图完整文件/SHA解析。

完成索引名：complete-original56-seven-generator-critical-cover.json.gz。
逐chart名：complete-original-seven-generator-chart-01.json.gz，依次到56。
每chart的完整压缩与逻辑SHA在最终索引中；checkpoint只表示已完成前缀。

有限域127只用于核原E常数系数unit和原标签。
3×3伴随的18个左右恒等式在九个独立整变量上核，不是有限域近似。
原parameter/source Schur恒等式用精确通用代入，未宣巨大展开多项式重乘。
本次仍没有判任何chart为空，也没有自由七元基或rank4的假设。
