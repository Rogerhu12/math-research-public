# 真正负全局控制状态的准确末格入口

本组使用已实际接受的第 30 轮 `dyadic30-trial-back01-a01-accepted.npz`，SHA `3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981`。它的全局 tail 控制有负值，R170 八段准确子盒仍通过。没有使用早期未求解的 witness fixture 冒充该状态。

## 新类与完整定义

入口为 `fd2d_gc_dyadic_tail_accurate_last_cell.DyadicTailAccurateLastCell(field_arrays, profile_packet, *, profile_sha256=None)`，新 schema 是 `fd2d-R170-accurate-last-P1-cell-physical-tail-v1`。

它显式读取并核 R170 domain kind、完整 domain definition 与真实参数重算的准确 certificate；读取实际 K31/tail16/profile7、131 节点 P1 场、零 cut raw 行及全部保护窗。R171 profile packet 必须绑定**同一 actual NPZ SHA**，因此不能借第 27 轮的旧 $\delta$。本次使用 metric 侧真实重绑的 packet `a6215af63b98cc8409faf9dbb46c039f86c1ef9e9bc6fedacdd62514ba3dcb5a`。

此构造器不调用原正控制构造器，也不改名伪装旧类。准确坐标、raw、weight、profile、tail polynomial 和完整 box 求值全部继承冻结的 R172 方法，父源 SHA 为 `8c8b8fefd5a3d459833e2b20b472710c54aebbf3ed00028e9740ef0843f6f435`。原方法对整个有限多项式作区间运算；其算式本身不要求每个全局控制非负。所需函数条件 $\kappa\ge0$ 和统一曲率上界已由新准确子盒证明，所以构造器的域替换有完整数学依据，不是绕过旧 guard。

沿 R172，物理半径和 $K$ 在准确 $s$ 求值，raw/weight 只在明确 $\sigma$ 复合。cut 仍返回准确尾的角向 jet，径向 II 导数保持缺失。`angular_majorant()` 直接消费 R174 的有限系数常数，给可积端部角二导界；没有把 $II_{uu}$ 或径向导数填零。

## 实际小核与范围

最终执行真实退出 0：chunk `49596d`，内部 0.211 s。使用显式独立依赖目录的 python-flint 0.9.0，没有改全局 numpy/scipy。

只核三个 cut 角 $0,\pi/6,\pi/2$ 和一个内部点 $(t,u)=(1/2,\pi/6)$：cut 全部不含径向 jet；两个零角的值/角两导包围准确零；$\pi/6$ 与独立准确有理多项式公式相交；内部 $K>0$ 且完整 R155 Gauss 恒等式的区间包含零。另生成 R174 全末格有限系数常数。

同次用现成 `bind_dyadic_tail_archive_native` 给出该 **actual 30** 的完整 native definition，SHA `5853eda23c948549b871777ac3aabbb298c8f76808267ab45c114432b9f6d8db`。固定 foundation 只提供 candidate/seed/reference 输入；所有实际系数、mesh、atlas、windows、lifting 和新域 packet 来自当前 NPZ。

这些小核不等于全域 metric、Codazzi、body、seam 或 reach 通过。没有运行 F/J、whole normal 或 BVP，未改变任何输入、物理 $g$ 或已闭源码。完整 interval 层由 metric 侧独立接入这份新 native 和新 profile packet，不重复本小核。

此前一次执行在所有小点计算后，仅报告路径的相对/绝对转换处真实退出 1；修复为 `Path.resolve()` 后，又因恢复环境缺 `flint` 在 import 阶段真实退出 1。依赖按原版本恢复后取得上述真 0。另一次恢复期间调用从未创建进程，不当成检查执行。所有阶段在 receipt 中分清。
