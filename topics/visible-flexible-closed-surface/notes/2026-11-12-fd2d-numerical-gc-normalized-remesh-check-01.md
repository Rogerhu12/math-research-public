# 全160真实节点的无量纲谱延拓核对

2026-11-12，numerical_recovery。此次只将一份完整真实 M4/N64 尾响应转换为 M8/N128 初猜，没有求新的 ODE、DN 或边值问题。

## 真实输入与转换

输入为 `2026-11-12-fd2d-numerical-gc-layered64-full160-04-response-0001.json`，REAL cosine cut height为−2e−9，SHA256 `d8a78ef41bed1c7d98af6f887e30e6ddbe2b88208fe5abc9ca8d26da24f58248`。其原物理wc01配置、160格、每原profile两段射击、全部2,881节点保持。

谱延拓保留低模Q与无量纲非均值L，高模Q和L置零，再按新M/N的原完整均值方程重新求均值，转回真实momentum。新高阶momentum一般不为零；不能把原momentum向量简单补零来代替这一操作。所有正常/深层求值沿已闭存的同式稳定算术，既不形成先下溢的w²，也不形成次正规physical raw试步。

原模态均值/低模与新模态的差异只属于初猜转换，后续必须求新有限方程的完整残差。M8不是M4的相同离散方程；物理g相同。

## 实际检查

独立session41341，启动chunk286f62，工具结束chunk638bc4，exit0，报告耗时11.044秒。
初次启动chunkb2900d为真实exit1：环境变量误传成archive scripts目录，导入路径重复，数值fixture尚未执行；随后改为独立runtime根路径，源码未改。错误回执单独保存。

全部节点结果：Q/非均值高度的变化严格为0；重求root后的无量纲非均值L最大差1.63665584e−18；共同角节点上的physical UR差2.64887837e−23，Fourier L1差2.64928166e−23；均值斜率变化0。低模momentum相对变化7.65643e−14，新高模momentum相对原尺度最大1.48495e−11。新root最大relative residual7.65643e−14，minLeading=.9901038631668481，minD=.9999999967980512。

完整初猜gzip185270B，SHA `142d7a05673cb7d5836de8d5b87c5cef8f9c93713c0fac0fb887bdbeed03239b`。它明确标注为初猜，不是实际M8收敛状态。

## 下一实际计算使用范围

`fd2d-gc-tail-partition-worker-v9.mjs`只将v8的谱延拓入口替换为本次已实际执行的无量纲Q/L实现；原F、Jacobian、projection floor、接受条件及物理配置仍在。当前运行04仍用冻结v8；只有04闭边界后的新独立入口才使用v9。这里没有预写未来的M8收敛结果。

原M4的连续角缺陷有实际增长依据：h=1e−9/2e−9/4e−9时，有限采样的normalizedFullDefect分别约7.83423e−14/2.50711e−12/8.02665e−11。每次加倍约放大32倍，提示未留高模项开始主导；这组数是完整有限audit的观察，不是对整个连续域的严格上界，也不代表实际metric等于该归一缺陷。
