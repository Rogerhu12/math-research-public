# 第一下降转弯 ramp：独立实际求解/响应入口准备

已完成的背景 C² 接口计算见 [前条 ramp 结论](2026-11-14-strong-resume-descending-turn-ramp.md)。本条只是把同一个 `descending_turn_ramp` 参数接入真正的 production 和完整响应入口，供当前同半步实际结果之后使用。

三个新源为 `strong_20261114_ramp_actual_bvp.py`、`strong_20261114_ramp_augmented_core.py`、`strong_20261114_ramp_control_response.py`。生产入口沿用全部 32 个核未知量和 delta/LB/vp 三个几何未知量；ramp 为显式外部物理控制，缺省 .08。响应入口同时安装同一个 provider，保留原 full/half forcing、完整 H Jacobian 和原 backward checks。所有旧源、当前在跑的同半步和 MJS 都没改。

实际执行了两条原 source-only 准备命令，以及新 augmented factory 的加载与布局检查，均成功。两条完整生产/响应变换的 SHA256 分别为 `1c7135d0acc9f815c91e6a792395ee954593841a85cd64a60d29a91756be7ebf`、`f8e3dc732ffe44c5cda168074cfb53797bca5d47fdea6315541188d68d0c32d0`。结果在 [准备记录目录](2026-11-14-strong-resume-descending-ramp-entry-preparation-r1/archive.json)。

尚未计算新 ramp 的完整方向，也未运行非默认 ramp 的实际场或 BVP。当前 13 方向包没有这个方向，不能将它作为第 14 方向直接消费。非默认 ramp 改变前缀 scalar profile，故全局 g 是新设计；仅尾部 g/cut 与有限末端 bridge 不变。将来若接受非默认 ramp 的状态，其 fixed-view、完整 mean 审计和同 g 精化必须再显式安装同一 ramp provider；那些后续入口尚未在本条声明支持。
