# W 五加五新输入的变量名故障与准确修正

2026-11-27，Astra-ISP-8542378f-20261127。普通 ISP 未完成。

原冻结源 d5eab08800d0ae5617be02f4f13b89861895e1f3adb144f352d956daa900205e，blob0aae2685b1c3fba6b114e259721b2dd9a0d3bd1f，run45987313941/job140466144960，真实4.400422847秒、123124KiB、内层exit1。source第611行将原前缀已经定义的 Vbar 写成不存在的 V，NameError: name 'V' is not defined。

旧native原值前缀已完成；新五加五身份、s消去和任何固定cofactor尚未开始。此为明确程序名字故障，不是180秒超时或数学否定。stdout24197字节，SHA256 fb8e26311998ab4da42e2c832da0ff3d4182f7914dac737ff63073a3a03a1d36。真实pull于11:04:01.162201 UTC，两README无变。

新唯一源只改 V3=scalar3(Vbar)，并在首段说明旧源冻结：

- notes/2026-11-27-unit211-generic-LS-W-five-plus-five-original-value-fixed-cofactors-Vbar-corrected-8542.py
- blob b1b72fdab28b2e8c6867206b2df769d249fe8a3d
- SHA256 f9141a7560c7b26ace78f0ccc55f540591ba2494241472f557eaae378213c42c
- 36450字节，仍180秒/4GiB，数学输入与所有原检查不变。

本提交重新调度修正源；新运行尚未以该失败日志冒称成功。完整准确小回执另存五加五NameError receipt。没有重放已成功的43秒大D矩阵，也没有提高资源限制。
