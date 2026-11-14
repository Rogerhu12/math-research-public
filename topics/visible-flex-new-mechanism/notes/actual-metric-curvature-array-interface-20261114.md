# 实际度量曲率PSD数组接口

记录：2026-11-14 21:19:43 UTC。依据[R103](../results/R103-actual-metric-curvature-semidefinite-gates.md)实现独立数组模块[frame_curvature_psd.py](../scripts/frame_curvature_psd.py)，SHA-256 `146f12fb56ac1a0b18a4d35ede1c171d68e72f7ae778e49fdff0b9bd1f9561bc`，12333 bytes。

## 准确接口

输入是同一物理状态的 Xs、Xt、Xss、Xst、Xtt，固定正 a 和固定 τ；逐点使用真实第一基本形式，保实际 G=|Xt/a|²。输出 qI±τK 两矩阵的迹和行列式四行。独立 q 正则门先检查，退化时拒绝而非用零矩阵通过。另提供R103的多项式矩阵和基于实际I的Cholesky主曲率诊断。

参数导数要求五个位置jet的全部真实参数列，保法向变化。接口只返回物理参数导数，附加epigraph辅助delta列应由调用者明确补0。固定a不随这些列变化。传入复用values时，调用者必须保证它属于同一个不可变state；本模块不管理研究候选缓存。

## 新人工检查的范围

[开发回执](curvature-psd-artificial-array-check-20261114.json)，SHA-256 `c15dc5c9a56952d0760f059acd02e421ad873e10c6a83be548a77d1ac3dd43fb`，6344 bytes，只使用小人工局部图jet，没有载入或评价研究候选、没有调用研究optimizer。

16个平面/球面局部jet/柱面局部jet/鞍面局部jet用两种材料坐标和两个τ交叉检查，主曲率与纸面值一致；非正交坐标下两PSD与多项式矩阵的通过/失败一致。R103真实I不等于目标I的明确反例被正确拒绝。完整五jet方向Jacobian相对误差 `8.303169162764031e-10`，环境反射准确交换正负两个PSD门（差0），零面积输入被先拒绝。全部新人工检查通过。

## 研究接入仍待实际需要

当前dense源与已经发布的接受记录保持原样，本模块尚未用于任何真实候选。后续若加入曲率约束，须使完整entry/Q等包装提供对应真实二阶列，并按批次控制内存；不能从第一阶缓存代取。工作/细网格上的曲率通过也仅是有限局部筛，不能支付全时全域reach或非局部点对。
