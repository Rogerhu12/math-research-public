# 原 support 固定 g 的 M32：独立 CSR / streaming-QR 恢复入口已准备

这是一条**尚未执行新 BVP 的入口记录**。唯一目标仍是此前 M24 已接受解在原线性 Robin 前缀、同一固定 g 下的 M32 谱精化；不涉及 fullDN、闭图或完成标准的晋级。

## 保留的真实状态

输入仍为第二次被中断 M32 的完整 1497 个 nodal 点、97 个状态分量、32 个参数与 31 个参数尺度，使用已实际生成并核验的 `fixed-lambda002-m32-nodal-recovery-v1/initial-recovery.json`。全部 x/y/p/pscale 在 v3.prepare 中逐位核对过；本次不重新运行 helper，也不为存储组件更换重复 prepare-only 求值。

冻结的 v3 源 SHA-256 为 `8ebbda010585c88c828d09bb53096a229c960672f25ea959964185c871370ff5`。新的独立 `fixed_support_literal_driver_v4.py` SHA-256 为 `c678f8c9fc3f5b878ee389e7cf36353f7267b2bd071184cb49c43d9c5ad77553`；原 v1/v2/v3 均不修改。

## 唯一资源实现变化

v4 使用设计链已在完整真实 M24 矩阵及方向上验证过的 `design/direct_csr_collocation.py` 与 `block_qr_v2.py`。原 collocation 的全部非零项、显式零、参数列和端点方程保留。CSR 避免装配 COO 行列索引和随后格式转换的大临时数组；QR 的矩阵绝对值诊断按块进行。旧 factor 在构造下一个完整 J 前释放，solve 包装无反向引用环；每次方向仍针对同一个完整原 J 检查 residual。没有新的降维、投影或门槛放宽。

固定 gauge q=.06、warp_reference_q=.06（实际 warp_e=.48）、lambda=.002、原物理 delta、mean_N=1168 与字面 chart 全部保留；M32 / angular1024 / audit2048,4096、tol=2e-7、bc_tol=1e-7、physical_bc_tol=2e-9、原 q 分支和 max_nodes 也保持已准备合同。

## 当前执行边界

源码已编译，v3→v4 差异已逐段核对。完整未启动命令、输入 SHA 和两个存储组件 SHA 见同名 JSON。它等待设计链实际 lambda=.128/M48 结束及下一尝试目录屏障确认，然后在独占前缀大 J 窗口运行原完整 BVP。本记录时无新大 J、无新 M32 返回，也无 M32 接受结论。两次此前 exit137 记录不因本入口存在而改变。
