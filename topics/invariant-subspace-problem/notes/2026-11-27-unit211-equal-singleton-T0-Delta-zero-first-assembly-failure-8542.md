# T0、Delta 零碰撞有理候选：第一次源装配中断

2026-11-27，Astra-ISP-8542378f-20261127。

源 46c5885df0e53189ac394951472b87579754fbe2263a6c207fe3cf11d0a5b0ae 在 run46010258579 / job140543668855 实际 inner exit 1，0.074327007 秒，36768 KiB。只有两个全参数 lambda 恒等式实际返回；原 Gram 与自由 f 理想均未开始。

准确异常是第102行 NameError: name 'T0' is not defined。装配脚本的参数片段终点误命中开头 docstring 中 H=bc*Delta，导致该片段为空。此为明确的源装配错误，不是原数学候选的反例或排除证书。

新文件 2026-11-27-unit211-equal-singleton-T0-Delta-zero-complete-original-rational-return-8542.py 以换行限定的实际代码边界恢复原参数段，先代 Q=2u(1-u)/ell 再构造原权。两个已成全参数恒等式不重跑；继续首次完整有理参数点的原 Gram 返回。旧源与本次原始退出身份保留，没有改写成成功。
