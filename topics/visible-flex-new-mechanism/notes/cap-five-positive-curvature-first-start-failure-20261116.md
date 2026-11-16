# 真正正曲率 cap 五门首执行：启动积分失败，保原费用后修复

日期：2026-11-16。主课题进行中，未满足 README 完成门。本条是一次真实失败记录；没有完整新 cap 的五门观察，更不能据此称不存在。

## 原执行与已完成的输入

- 公开 [run 43831664308](https://github.com/Rogerhu12/math-research-public/actions/runs/43831664308)，research job 133178210211。
- source commit `03bfffd120026aa5f25187dc0c0ec5c01705e709`，workflow `.github/workflows/visible-cap-five-positive-curvature-search.yml`。
- 原 stdout 106370 B，SHA256 `0e78611cfb99dc2e6a9158991d920a3740185919bb25924c5a4865333fce2520`。
- 入口源码31582 B / SHA256 `ab19482e582c93a552b915d8d813cc6f4d36c94f88f2b2ed4eb266179b892c38`。完整数学定义和预算见[设计](cap-five-positive-curvature-search-design-20261116.md)。

真实公共 pull：08:30:10.280694→08:30:13.960397 UTC，从本 source 到已读
`0620f8d68bb4b06637ee3cdba916cce5e11906d1`，returncode0，根/课题 README 均空 diff。
私有实际 pull：08:30:17.979083→08:30:18.931957，before=after
`ef9137d638db4223eb669caa01d95781f99f7a54`；根 README 不变、课题 README 仍无，本会话 QUEUE 唯一进行中。
读过的根/题 blob 仍为21bd547f56590b7f2dd279d0297efb289a9b2783 /
d0432faff569c8e9af7ed4809847e12880976c11。下一实际 pull 不晚于09:30:10 UTC。

## 真实停止点

科学入口成功导入固定 Python3.12.14 / numpy2.3.5 / scipy1.17.0。
公共左 germ 的完整区间[0,1/32]八系数积分已完成：63个quad回调，
其浮点误差估计约2.455898075778704e−78（不是严格包含）。
这份原 prefix 已付，后续只读原日志恢复，不为修复重做。

随后第一次全零15参数的完整 cap 积分启动，DOP853第14个真实 RHS
在指数恢复正状态时抛出 `OverflowError('math range error')`。
原日志末个已记 RHS 坐标为0.0390625，即1/32+1/128；
其中v约9.2807785827e−8、v′约2.2164205103e−7、U约1.8000987089e−28。
这些是未接受的积分内部 stage，**不是实际 cap 端点，也不是可用五门值**。

从公式看，靠近平端的log状态导数很大，而入口未显式指定足够小的首步；
这个实际错误需要修复初始步控制。没有完成的目标、Jacobian预条件、优化起点或候选，
没有许可将其当作参数盒失败、局部驻点或全局非存在。

## 不重置的费用

权威 CAP5_FINAL_CLOCK：**0.5630522320000182 秒**，含imports、请求读取、
失败和最终输出；started积分2、completed1、failed1，RHS14，prefix回调63。
所有旧ψ3完整E、self/rank/forcing与独立开发执行均0。

修复仍属于原同一个120秒/400started分配；必须把上述费用及次数带入，
并从这份原stdout恢复已经完成的prefix，只完成此前未完成的真正cap观察。
不延长、重开或剪掉失败费用。原输入/失败/final记录均仍在公开stdout，
不把机器payload提交Git、artifact、Release或cache。

## 接着处理的工作

修复对象仅是这次真实启动错误。数学族、六固定起点、完整十二项L/八Aj/
五Δ、解析敏感度、原正性及端点条件保留。若完成有限搜索仍没有小残差，
只能记录该有限观察；R481可通过真实logρ lift提供该固定15列外的新方向，
而实际全局零、严格包含、母库安装、全s同规范和主几何门都还欠着。
