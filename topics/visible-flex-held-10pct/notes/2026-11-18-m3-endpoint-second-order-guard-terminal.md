# 二阶核心正性界入口的完整失败终态

状态：**完整数值失败记录**。原二阶充分界入口已结束，没有 $\lambda=1$ 的接受前缀。原前缀内解先触及拟增网格点数上限；保存其有限物理五次表示后，后续 prefix/seam 审计阶段又触原 Frenet 域门，具体子调用未记录。不能把 shell 退出 0、两次起始尾门通过或已保存 CP 称为联合解成功。

## 1. 原门实际结果

执行句柄 **14903** 已直接观察到退出码 0；launcher 和尾 worker 的终态记录也均为 0。这里 wrapper 原本会捕获异常并写入 summary，所以退出码不代表数学接受。尾 worker 于 `2026-11-18 00:09:26 UTC` 正常关闭，stderr 为空；实际 coupler 计时 $1363.078177$ 秒，外包装计时 $1365.869347$ 秒。

相对已登记的 C² 初猜入口，本轮只新增已独审的解析二阶 $\rho$ 插值充分界；仍用 $q=.03991248545080898$、$\lambda=1$、$a=.21$、$b_p=.32$、$b_c=.4$、M16、prefix 512 角节点、tail parts16 及原所有门。完整来源见入口记录 `circle_endpoint_second_order_guard_entry_record.json`。

| 项目 | 实际终态 |
|---|---:|
| 内层 `solver_success` | false |
| 原停止消息 | The maximum number of mesh nodes is exceeded. |
| 当前径向节点 | 3469；下一次拟增超过原上限 6000 |
| 最大 collocation RMS | 3.70554950990657 |
| 拒绝的 domain / merit 试步 | 165 / 34 |
| 已取 Newton 步 / `no_step` | 16 / 0 |
| 最小步长 | $2^{-19}$ |
| 最终参数 $\delta$ | .06068237630000981 |
| 审计异常 | `Adaptive Frenet domain failure: -6.346191867567796e-07` |

本轮统计没有逐条记载 165 次域拒绝的类型，不能把它们一概说成核心正性或 Frenet 失败。这里也不据旧、新不同迭代路径的 RMS 或步数推导收敛结论。

尾只发生两次实际调用：起始 $H$ 的 warmup/audit，以及同一个 $H$ 的 affine 内层 DN/Jacobian。二者原停止残差均为

$$1.3784657706205187\times10^{-9}<2\times10^{-9}.$$

Call 1 返回完整有限尾审计，call 2 返回 800 个有限 Jacobian 数值。内层失败后没有 call 3，因此没有检查这个失败前缀的新末端 $H$。不能把起始尾接受移给最终失败前缀。

## 2. 已保存什么，尚未得到什么

原控制流先完成 `physical.sol=f.c2_interpolant(physical)` 并保存 CP，然后依次调用 `adaptive.audit` 和 `seam_audit`，两者都返回后才再次保存 CP。`seam_audit` 在查询新尾之前调用的 `f.velocity_s` 也可能抛出同名 Frenet 异常。因此，已落盘 CP 和仅两次尾调用只能把本次异常定位到后续 **prefix/seam 审计阶段**；没有原 traceback，不能唯一归因于 `adaptive.audit`。没有保存可供复核的完整 metric 或接缝报告，也没有已接受的实际外层检查；这不证明 metric 审计一定尚未返回。

保存的是**失败内层态的物理五次表示**，不是原 raw cubic 的逐位快照。后续若从它重建原 chart/节点，必须明确此区别。

- CP：`m3_work/beta4625-q039912-raw-lam1-b032-w040-m16-c2guard/seed.json.gz`。
- SHA-256：`d95ed7f6888fe9ad35447fb5b1e477cddfe047f3923fc2eed1eb5ed67b7f407e`。
- 两块有限 float64 五次系数均完整覆盖 49 个状态，哈希分别为 `653d4c68ed7fc8b04cd9a296bb981e22768a427b0c09e78e023a7bb6a00e7953`、`8b8ec30d268ac8f38bc3a2ee902f537432a08c5863ced6a64353329104e5312d`；数组只留 scratch。

全部 15 个最终物理控制保留在终态记录。首个已从初始约 $.00021128$ 变为 $2.245797491590578$，后续呈交替抵消；单个参数大不等于完整核心 $\rho$ 负，也不能代替真正完整控制函数检查。

## 3. 记录与继续方向

`collect_endpoint_second_order_guard_terminal.py` 只读取终态、输入和源码哈希，核原两次尾门、有限 Jacobian 及物理系数分块覆盖，不重跑 BVP 或审计。复现记录为
`scripts/resume_m3/circle_endpoint_second_order_guard_terminal_record.json`。

二阶充分界保留了原 $10^{-5}$ 核心门与 32768 网格上限，并允许原诊断中被保守下界拒绝的部分初猜进入；本完整实解仍没有得到圆弧前缀。本条不把这种数值失败升级成不存在性，也不为接受而改门。

已有独立五半宽初猜探针显示，同一控制/C² 初始化的 $\lambda=1,a=.01$ 原 RMS 约 $.423$，较同离散 $a=.21$ 的 $3.001$ 小。下一具体路径从原有限接受的 raw $\lambda=.02$/M16 重新初始化较短的精确圆弧，保持原方程与门，若得到合格锚点再向目标半宽 $.21$ 续接；不从本次大控制失败态冒充接受重启。小半宽不继承最终 10% 几何窗。
