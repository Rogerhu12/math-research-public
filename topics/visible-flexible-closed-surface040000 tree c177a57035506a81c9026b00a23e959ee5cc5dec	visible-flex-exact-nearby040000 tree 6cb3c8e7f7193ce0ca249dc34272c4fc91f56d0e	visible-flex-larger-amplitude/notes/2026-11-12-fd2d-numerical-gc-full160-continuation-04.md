# 同一wc01全160格真实非线性幅度续算04

2026-11-12，numerical_recovery。此运行在三个明确REAL cosine cut height上实际求解同一物理g的有限非线性尾方程。每个响应都已包含2881节点末态、cut两jet、56项heightJacobian、完整有限采样audit及原序累计的finite meanHeightToCut。

## 固定物理与数值输入

物理cfg为`2026-11-12-fd2d-layered64-wc01-recovery02-config.json`，SHA256 `d4d41047c5afa1df90e17e3814e896a7cd91f64c79d0e11116e071cb97e17994`。全部修改0…159非线性消费；≥160不改原source；linear far196只给明示有限深度的边界图。M4/N64、每原profile两段射击、每段RK32、audit32、projection floor .05、原tol2e−9保持。

新v8仅将幅度warm放在原Q/L物理坐标的无量纲实现，并输出已经实际计算的meanHeightToCut。第一个请求用scale2的几何初猜；之后两个用真实已算完整射击切线作warm。所有初猜之后均以原完整非线性F/J和原接受条件实际校正。

## 真实结束与响应

独立session59895，launchfb5476，最终chunk7256f5返回工具exit0。Node returncode0；总1359.506570622秒。没有主动停止或推测退出原因。

| REAL h2 | shooting residual | minLeading | normalized full defect（采样） | actual metric（采样） | finite meanHeightToCut |
|---:|---:|---:|---:|---:|---:|
| -2.0e-09 | 1.606753272e-14 | 0.990103863167 | 2.507109104e-12 | 1.795644201e-15 | 0.016564199301009993 |
| -4.0e-09 | 3.581202630e-14 | 0.980160752619 | 8.026650351e-11 | 2.002105512e-15 | 0.016564199299786388 |
| -8.0e-09 | 2.446425032e-14 | 0.960133663816 | 2.573505551e-09 | 2.003034592e-15 | 0.016564199294891568 |

三个响应分别536.482/433.534/317.811秒。每个实际history有三次完整F/J事件：第一请求 .15409→2.49038e−8→1.60675e−14；第二 .00760718→1.00924e−6→3.58120e−14；第三 .01523274→8.12908e−6→2.44643e−14。末态接受立即另存，返回后保完整响应。

完整响应SHA、每个文件字节数、原runtime路径及真实结束回执在`full160-04-completion-and-closed-manifest.json`。19份关闭输出共4,071,422字节，每件小于1MB。中间阶段cache仍只在独立runtime，未把可再生块全量加入仓库。

## 结果含义与继续计算

这些是同g完整有限DN响应，不能从shooting residual或采样metric反推出连续全域界，也不是无限非线性深尾存在证明。meanHeightToCut从finite node160的零均值锚到cut累加；原无限source的剩余非线性均值未由本次数据证明为零。heightJacobian使用完整真实变分射击图和现有cutjet中心差分消费者，不冒称精确解析矩阵。

M4采样的归一全角缺陷随高度每加倍约×32，最后达到2.5735e−9；实际metric采样仍约2e−15，因为它的量纲权重不同。因此继续原M4加幅会掩盖实际谱截断风险。下一独立05固定末实际h2=−8e−9和同一物理g，改M8/N128，其余网格/容差不变。05已实际启动session74866（eee69d），初始2881节点来自此第三响应；不是复用一个已解的M8实体。

05的ready已观察实际heap268435456字节。此次实际M4→M8初猜Q/height变化0，非均值L差3.47e−18、physicalUR差1.064e−22，新增高模momentum不可简单置零。这仅支付输入转换，没有提前支付M8有限残差或后验几何。
