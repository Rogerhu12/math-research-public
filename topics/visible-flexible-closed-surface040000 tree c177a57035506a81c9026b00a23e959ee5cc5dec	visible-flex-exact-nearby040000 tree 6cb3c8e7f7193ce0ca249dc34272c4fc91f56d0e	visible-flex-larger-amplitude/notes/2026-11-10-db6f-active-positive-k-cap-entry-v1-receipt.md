# 活动正 K 解析/双曲帽入口 v1：真实纯代数执行回执

2026-11-10，作者回执。仅记录本版来源和实际小程序；不是独立全文审查。

## 固定来源

[完整正文及附录 A](https://github.com/Rogerhu12/math-research/blob/34430a86495804875207cfce743b173e490ec63c/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-active-positive-k-analytic-hyperbolic-cap-entry-v1.md)

- commit：34430a86495804875207cfce743b173e490ec63c
- Git blob：370075742e2d4bfe54cfa477013813ec8df185f9
- SHA-256：1d1bd51ecef41d31be633904dfee7c4ac3a461ea08f32d763931cf4a32109aab
- UTF-8 字节：30869
- 保存后从固定 commit 全文回读，逐字等于冻结文本。

从这次固定回读的唯一 javascript 代码块提取完整源，
并在执行前逐字核对冻结原字符串：

- 源字节：2964（ASCII）
- 源 SHA-256：3e0e27c923276be97da6f6137eea8465b58db2769a46f84ce762dc4911bc121b
- 执行环境：functions.exec 的 V8 JavaScript
- 开始：2026-11-10 01:21:35 UTC
- 完成：2026-11-10 01:21:35 UTC

## 实际返回

```json
{
  "pass": 24,
  "fail": 0,
  "exact_field": "Q(sqrt(2),i)",
  "pde_runs": 0,
  "geometry_arrays": 0
}
```

24 项实际通过，0 失败。它包括 Q(sqrt(2),i) 上的 Laurent 多项式乘法，
核 P 的平均系数及 P(0)，以及正文的有理常数门。

没有终端进程，故不编造 shell exit 0。
没有 PDE、BVP、tail、RK、曲面数组、网格或优化数据运行；
本程序不证明解析/双曲存在、有限传播、真实位置闭合或完整帽的存在。
新的证明仍须由未参与者全文独审；root 参与的方程复算在正文已署明。

本次来源与旧的固定正 K 短桥 24 门不同，不冒用旧回执。
所有既有冻结文件保持不变。
