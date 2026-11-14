# 同wc01真实M8加密、节点两jet差与native零符号恢复

2026-11-12，numerical_recovery。固定物理wc01与REAL h2=−8e−9，仅将M4/N64改为M8/N128；160实际修改格、far196、P2/S32、原floor .05和tol2e−9不变。

## 完整响应

05 session74866，launcheee69d，completion2ebb21，工具exit0、Node0，992.592656秒。原始JSON1,486,592字节，SHA `8d25507e0b65de103afaee0109f97aef2eeb8313fd2eded486a3561447036502`；仓库gzip249248字节，SHA `c082a4aab7fcca806c47b977469412c8e09d3b19f0954f6765a97e714d56017b`。

真实完整F/J残差3.836142665793242e−7；一次λ=1试步全域接受后，末次完整F/J为1.6067532721703842e−14。全部2881节点、208项heightJetJacobian、实际finite meanHeightToCut=.016564199294891568与完整采样audit均已返回。minA=.9601336639368594、minD=.9999999871918863、formal κ6.99660503，采样actualMetric3.1152315e−15。

同一h的采样normalizedFullDefect由M4的2.573505551e−9降至M8的1.592476151e−14。这是真实不同有限谱方程的解间比较，不是把M4初猜补零冒作M8收敛；实际UR保持的Q/L延拓之后确实重新求了非线性F。

## 共同节点两jet比较

独立6301/c48f79→8c03b4真实exit0，8.292秒。两份完整同g响应、原2880个实际stage均值（逐块SHA与原packed-input SHA绑定）、相同2881径向节点及64共同角，共184384点。只重新求局部root和物理height两jet，没有径向重积分。

最大差：height3.17685125e−19、H_r3.91027254e−16、H_u3.05623973e−18、H_rr2.63783187e−13、H_ru3.76045579e−15、H_uu3.18211278e−17。最大值均在raw1附近；无量纲L最大改变量1.09114396e−10。保留的每stage总mean积分在两份二进制数据中给出相同均值差0。

这只是在实际共同节点/共同角的有限比较，不是径向区间误差或真正Cartesian全C²包围。报告另外保留若干较深节点相对旋转背景的有限两jet读数；极小差受舍入相消影响，不能把浮点零当严格零。

## 原native输入的706个负零

实际完整F/J cache的packed-input SHA为`aea57a9e0dd527663051693eb3ed68dc8741a67370cb04ac3bfcd5b9643e7366`，而JSON反解后为`884e60fbd32e1c13c550e8e9c24131d3cb53a0ea2ea9186a480b1cf6fb87fe85`。不是数学状态失败：JSON把负零写为零。

冻结原线性graph bootstrap/局部root重新构造后，使用已保存的首F/J、试步F与末F/J做同源Newton代数重放，所有非线性stage均从准确输入键的实际缓存读取，遇未保存输入立即拒绝。02 replay session29943/c4a8ac→8ace97真实exit0，52.649秒，最终native SHA逐字节回到原值，全部非零坐标一致，差异确为706个负零。恢复mask2027字节，SHA `8ff35840f7d909508d25ae5366067dea9d25e5139f896ddbf8dadeba6c3b5361`。

01 replay入口先在Array.map直接传typed-array静态方法时实际exit1，未进入缓存残差；保源与回执，另名v2修复。节点比较01也在把runtime日志路径误纳入物理身份时实际exit1，尚未求jet；另名v2仅排除明确runtime路径和本来要改变的M/N，其他物理/径向参数仍逐值相等。

v3均值提取器先用已核mask恢复负零、再比对原packed-input SHA，最后按原序读取90块、2880个已算stage meanHeight。没有为保存格式问题重跑一条非线性尾。

## 当前范围

这些结果闭合了当前小幅wc01同g谱加密的实际证据，强曲面仍未完成。此处不称无限非线性尾、连续metric/曲率界或全局reach已付。按root安排停止旧g继续加幅；等待真正改进的新物理尾入口。三图册只读带宽任务另见coordinate-bandwidth-02.json和three-charts.md，没有新BVP。
