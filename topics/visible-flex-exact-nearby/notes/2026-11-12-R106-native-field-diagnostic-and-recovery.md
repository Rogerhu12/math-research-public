# R106 首次原生真实字段执行记录与中断

2026-11-12，constructive-route。此 note 是实际 terminal 显示输出的恢复记录，
不是重新生成的原始有向报告。

## 准确对象与命令

在独立工作区 /home/agent/visible-exact-constructive-2256-f6a2，
固定 Python /home/agent/visible-exact-py2256/bin/python，设置
PYTHONDONTWRITEBYTECODE=1、OPENBLAS_NUM_THREADS=1 后，实际执行：

1. ParameterGermBulkTarget(object, Fraction(1,10**9), 512,512,
   arb(".002"),arb(".0015"),arb(".32"))，ctx.prec=192、ctx.cap=5；
2. r=Fraction(1,8)，取所有实际 scalar/反射 knots 的共同右侧区间；
3. complete_data(r) 与 physical_fields，再在索引
   0,64,128,192,256,320,384,448 调用 fields_from_true_geometry。

object 为 data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json，
SHA256 91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848。
origin SHA0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b、
direction SHA8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab
在复制前逐字验证。参数为完整准确 δ5±1/10^9，未改用中心对象。

实际共同 span：
[1/8, 2296835809958953/18014398509481984]。
显示曲率：
K0=[−0.5317995669 ±1.18e−11]；
K0r=[5.387894764 ±8.20e−10]。
执行器打印 total seconds=0.4685116580003523，exit_code=0。

## 保存的原始显示球

下表按 θ=πj/16。列 D、S、Vr、Vθ 均为 R106 的原 R37 height 字段。
只保留工具确实打印的显示包络；没有用小数中点另造严格输入。

| j | D | S | Vr | Vθ |
|---|---|---|---|---|
|0|−28.10758 ±1.87e−6|0 ±9.34e−12|−28.494214 ±8.45e−7|0 ±4.76e−8|
|1|−5.10646 ±2.27e−6|−.0018500 ±7.10e−8|−5.24206 ±4.11e−6|−1.571572 ±6.75e−7|
|2|−3.24585 ±5.41e−6|−.0028151 ±7.83e−8|−2.977409 ±8.44e−7|−.367368 ±6.40e−7|
|3|−2.95771 ±5.18e−6|−.0004580 ±4.72e−8|−2.58253 ±3.12e−6|.203955 ±2.94e−7|
|4|−2.906007 ±8.94e−7|0 ±2.07e−12|−2.477327 ±6.93e−7|0 ±1.49e−7|
|5|−2.95771 ±5.18e−6|.0004580 ±4.72e−8|−2.58253 ±3.12e−6|−.203955 ±2.94e−7|
|6|−3.24585 ±5.41e−6|.0028151 ±7.83e−8|−2.977409 ±8.44e−7|.367368 ±6.40e−7|
|7|−5.10646 ±2.27e−6|.0018500 ±7.10e−8|−5.24206 ±4.11e−6|1.571572 ±6.75e−7|

## 中断及明确限制

随后一条只读 sed/rg 命令在创建进程时返回
exec-server transport disconnected / recovery timed out after 45s；
environment 状态明确 unavailable。没有给尚未运行的射线积分编造退出码。

此次实际八点计算没有落成原始 JSON；上表只作真实执行诊断。
恢复的代码源 SHA256
0e5b12ddcd259d24c4e004d7353e2ce13375adee12de050551d423ff3e1874aa
与执行时相同。

新永久重放入口 scripts/fourfold_subprincipal_actual_points.py 已保存，
它增加原冻结 beta 密度重算/两支 flux 恒等式检查并写完整球 JSON。
这个新 CLI 在此次中断之前尚未执行，不能把新增检查声称成已经运行。

从课题根运行：

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 \
python scripts/fourfold_subprincipal_actual_points.py \
 --out notes/2026-11-12-R106-actual-points.json
~~~

它仍明确只输出有限角点、完整参数盒的字段。
不把此输出当成连续角覆盖、真实 J、积分、全相位、PDE 强逆或闭族。
