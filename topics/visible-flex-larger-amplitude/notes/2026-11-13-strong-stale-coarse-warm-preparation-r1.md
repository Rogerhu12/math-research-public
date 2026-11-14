# 已接受当前点与陈旧方向的初猜转接准备

AI-assisted research workflow：strong_recovery，2026-11-13。

新的 `strong_stale_coarse_response_warm_actual_bvp.py` 仅扩展初猜存储/坐标传递。旧 q122 M28 响应仍逐文件绑定旧基线；不会被重标成 A 的导数或 M32 Jacobian。当前 M32 主包必须已有原 owned exit 0、真实完整 H/J/audit；若使用 fixed view，还要逐项核原物理字段不变、所有原 raw x/y 及 p[:32] 二进位相同。当前 A 的正在运行数据没有当作已接受输入使用。

两点仍须具有相同 gauge、角 chart、参考 Fourier 系数/频率、原数值 t 锚点、物理尾与端口。只有原 PRIMARY/EXTERNAL 控制列对应的前缀 profile 键允许不同，并逐项记录差异。若原 raw 网格改变，全部85个旧场分量在同一材料 t 上用明确标记的 CubicSpline 作初猜插值；原当前97个场分量、完整32模基线和当前 raw 网格本身保持。新增4模只有零增量，不是清零基线。参数方向先用旧单位得到物理 dc，再转当前 log-c2/高模尺度；前三个目标仍由原入口精确回代。

原 ODE、MJS、Newton、线搜索、RMS、坐标/正性条件、新 H 的完整真尾/J、最终物理审计均未改变。旧六组合 half 数组缺失、两新增组合只保存数值误差上界的事实也没有升级。任何未来候选仍须先用真正当前点完整均值暖场检查，再走原实际求解。

本次四个实际准备过程均 owned exit 0：源码接口、真实 q122 M32 零步、同真实 q122 M32 加原 A 的六个控制、以及原完整生产入口的 prepare-only。它们都没有启动 ODE、Node、大 J 或新的几何场。当前测试数据是已接受 q122 M32；不同 g 的 A fixed-view 分支及不同 raw 网格的插值分支尚未在一个新接受点实跑，必须等真实 A 完成后再进行其具体身份核验。原 A 同时继续唯一生产求解，没有重新启动。

几何读端不能把原专门绑定 q122 的网格桥直接用于 A；需同一真实当前点的新网格/见证身份。新增 `--current-original-accepted` 与 `--current-owned-resource` 必须与将来的几何 warm 入口一同透传。
