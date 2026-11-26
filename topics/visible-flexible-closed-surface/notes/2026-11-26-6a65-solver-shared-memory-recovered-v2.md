# R206 完整矩阵准备的共享存储恢复版与实际小对照

**可信度：结构等价推导 + 可复算有限浮点核验。** 这不是新的曲面解、完整 1788 维实际 normal 对照或 LM 接受；不支付连续 metric/reach 目标。

## 身份与范围

2026-11-26 执行环境再次失联，旧 `/tmp` 盘随后确认消失。旧共享 kernel SHA `d387e07ffb6d0e2a2a49b4153f1e03b841248263accba9f6e86a5bf5f3455ad9` 和 capture 工具 SHA `62ea9fe49e0dc595aa1e3b031e6485b2c1a935e445e6e829fe2847c6e9a24fff` 不由这里的恢复源码冒充。旧临时 51 维 heredoc 没有保留完整源码/报告，不能给它补造报告 SHA。以下为另名新源码和新实例。

支持的 base kernel 是仓库 `fd2d-R201-R205-band-border-layout.cjs`。新入口 `createSharedBandR206Kernel(baseKernel)` 只替换 R206 的准备阶段，`solvePreparedBandBorder` 直接保留原 R206 函数；不更换目标、法方程、参数列、行、阻尼、Armijo 或实际 value。

## 为什么允许共享

原 R206 准备先复制完整 H，再把左上块 H0 抽到另一稠密数组；同一个 H0 用同一 R201/R205 base prepare 调用两次，第二次只把 gradient 换为 auxG、squaredNorm 换为 0。

恢复版按相同顺序检查完整 H 的每个有限标量，但借只读 H；H0 用有原行跨度的只读 view。随后仍调用原 base prepare，完整扫描两种方向的矩阵元素并按原规矩拒绝任何非零越带项。第一次 prepare 已计算所有仅依赖 H0 的矩阵、scale、permutation 和诊断，第二份 aux 可以共享这些数组。aux 的 gradient 与 scaledGradient 单独分配。

尤其保留原 `auxG[i]=b[i]/scale[i]` 后再乘 scale 的两次浮点操作，不能用 b 直接替换以省略一次舍入。aux 的 suppliedDiagonalDifference 和 relativeDifference 设为 0，因为原第二次 prepare 没有传入 supplied diagonal；它自己的 gradient infinity 重新计算。原两次 Cholesky 和最终 working/original 非对称全方程残差继续由旧 solve 计算。

约定：准备/求解结束前，调用方不能改写借用的 `normal.H`。实际旧 solve 不改写 H；测试另核全部输入 H/g/diagonal 的字节哈希不变。

若 N=1788、旧块 n=1787，则避免 fullH clone 25,575,552 B 和 H0 copy 25,546,952 B，共 51,122,504 B。J38、每块47、width4 时 aux 的三 band 共10,073,040 B，三 border42,864 B、diagonal/scale28,592 B、两 permutation14,296 B 可共享。以上只计避免的数值数组分配，另有 O(n) 行 view；不能据此宣称实际 RSS 降了同一数额，也不能据此认定此前 SIGKILL 原因。

## 确切可复算命令

把以下两个新源码放在课题 scripts 中，与两个旧 algebra 文件同目录：

- `6a65-r206-shared-band-memory-kernel-recovered-v2.cjs`
- `6a65-r206-memory-small-fixture-recovered-v2.cjs`

从仓库根运行（输出路径须未存在，且放仓库外）：

```bash
node --expose-gc --max-old-space-size=64 topics/visible-flexible-closed-surface/scripts/6a65-r206-memory-small-fixture-recovered-v2.cjs /tmp/r206-shared-small.json
```

本次实际用 `/tmp/visible-flex-6a65e705/solver-work/recovered-sources/` 的同名源码，输出 `/tmp/visible-flex-6a65e705/solver-work/recovered-r206-small-01.json`。外部真实 OS exit=0，工具等待0.109086081秒；程序计时0.06秒，Node v24.22.3，process.resourceUsage().maxRSS=48896 KiB。这里只跑51维线性实例，没有 surface provider、完整曲面 normal 或 LM。

实例由脚本完整定义：7个径向块，每块7列，原 cut border 在物理列17，另附全局列50；非平凡完整置换，带宽2，物理对角乘子跨度1e−4至1e4；明确非对称浮点扰动和一项故意 supplied-diagonal mismatch。对 Float64Array 和普通数组两种 H 输入各验证4档 λ：1e−6、.001、1、10。

## 实际返回

两个输入各10035个 prepared 标量比较，加上全部方向/缩放方向/scale、模型与原式/工作式诊断，合计22342个 Object.is 比较全部通过。aux 规定矩阵数组实际为同一对象，两个 gradient 数组实际独立。两输入的 H/g/diagonal 字节哈希始终未变。越声明带宽加入1e−300后，旧/新均抛 `NONZERO_OUTSIDE_RADIAL_BAND`，offBandCount=1、offBandMaximum=1e−300。

| λ | working scaled 方程残差 max | original scaled 方程残差 max |
|---:|---:|---:|
| 1e−6 | 1.734723475976807e−18 | 2.0252896582029223e−16 |
| .001 | 2.168404344971009e−18 | 2.0339632755828063e−16 |
| 1 | 1.734723475976807e−18 | 1.0148132334464322e−16 |
| 10 | 8.673617379884035e−19 | 1.8214596497756474e−17 |

两类 H 输入和旧/新 solve 的上表数值逐位相同。原非对称残差没有被对称化后的较小残差掩盖。第一次运行在普通数组实例的比较器中因旧输出H为typed array、新输出借普通数组而拒绝；此为比较器对存储类型的过强断言，改为逐标量检查后以上实际运行通过，kernel源码未变。第一次失败不登记为通过。

## 本次文件 SHA-256

- `6a65-r206-memory-small-fixture-recovered-v2.cjs`：`f7a3a1163e76f0752fd8d35498fdc695e5a5e7d1c4b6cb3411465cb2a2004ed1`。
- `6a65-r206-shared-band-memory-kernel-recovered-v2.cjs`：`3e60ada0f3cb64a548c21995b1b4dba820a05ce8376d2fe39d66e9560697715e`。
- `fd2d_appended_global_schur_R206.cjs`：`b28febaee12d2bad62457ba6b2371a34cd273b2cee9eebc006fc9e961e1c36ba`。
- `fd2d-R201-R205-band-border-layout.cjs`：`636bdea5b19c8334a69ae3ad5adc1cfacd5370d7321905bc1ff5ad32829be82b`。
- 本次实际小报告：`fd201c48f7892fc7a02ea15ebae5a3ce543d210102f542ceb682f9c462d3a520`。报告只在scratch；可复算数组不发布。

## 尚待完成的实际核验

恢复版尚未消费完整1788维实际 normal；没有完整旧/新 direction 对照或采用此 kernel 的实际 LM。此前新 clock 输入 SHA `01725d3b221e5d0f8d0580ac332f957e8183edc6bcacd3b664743197a4ee46e2` 的 capture 在160.282155858秒以−9退出，stdout仅开始事件、没有normal；末采样RSS/HWM134576 KiB，原因未证。因此本条只登记小线性核验与存储等价理由，不把 capture 失败补算成功。当前同 job Cauchy 消费仍可使用原 R206 完整求解器。
