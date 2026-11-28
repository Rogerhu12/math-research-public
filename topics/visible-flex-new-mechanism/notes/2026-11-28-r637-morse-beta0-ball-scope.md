# R637：Morse 参考端口的首次严格球积分范围

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

本次只支付 R630 左正规全线参考中一个尚未支付的严格输入：
在统一归一化 r(X=0)=w(r(X=0))=f2(X=0)=f3(X=0)=1 下，
以显式球包围和已经写出的两端解析余项，判断 1/3 < beta0 < 3/8。
不重新执行小 nu 分支扫描，也不把此前普通高精度值直接标成认证。

## 固定输入和成功条件

source 为 scripts/morse_beta0_ball_integral_20261128.py；
解析余项证明为 notes/2026-11-28-morse-beta0-rigorous-tail-bounds.md。
固定 t 区间 [1/1024,12]，左遗漏尾严格上界 1/10000，
右遗漏尾严格上界 1/100000000。球值还必须证归一常数 |C*|<10000。
只有全部有限段给出有限包围，并在加入两项有理尾界后通过准确有理数比较，
才输出 certified_1_over_3_lt_beta0_lt_3_over_8=true。

使用 python-flint==0.9.0，128 bit，source 总计 300 秒显式预算，
每积分段 eval_limit=50000；一个 lane，一个 15 分钟 job。
source 对复球强制正半平面并传递幂的 analytic flag，
记录真实 callback、hyperu、公式求值、拒绝解析邻域的调用次数与每段时间。
未收敛、非有限包围、预算到期和最终严格比较未通过都作为失败输出。

沿用现有真实 pull runner：先 pull 两库、检查根/课题规则 blob 与本会话 QUEUE，
再移除凭证，核对全部源/解析证明绑定，最后执行数学程序。
source 本身还检查准确公开仓库、GITHUB_ACTIONS 和真实 RUN_ID。

## 保留前一次探索费用

前一次 run 46121291838 / job 140906179922 是普通 50 位探索，
source commit 1d1ec944b457eeb38a85423e305a43f457688394。
全程序真实数值墙钟 5.675849416999995 秒；参考积分 5.48510230200003 秒，
hyperu 4160 次、半径公式 2080 次、端口公式 2079 次、callback 4065 次。
run API duration 43000 ms、job 40 秒、billable.UBUNTU.total_ms=0。
四个小 nu 分支的调用记录保留在
notes/2026-11-28-r630-morse-port-actions.md，不在新运行重做。

## 结论边界

本次成功只给 R630 全线参考 beta0 的严格符号与有理区间；
R635 的通用边界消去单独说明这里 beta=beta0。
R633 的真实全平尾端口还须使用 R637 已写的尺度、缓冲和全积分连续性证明，
不能由球程序自行宣布真尾或非线性嵌入完成。
任何有限宏观角、Hausdorff 位移、reach 或 README 完成资格都不属于本次计算。
