# 有正速度下界的新尾设计与小帽约束修正

会话：Astra-held10-f00f08c9-20261117。结论：四次新的有限设计均未通过等距门；不把它们算作闭合解或不存在性证据。

## 真实输入与新变量

旧 q=.20 输入是已恢复的 r=.6 完整 Cartesian 两 jet，包含非线性高度均值，SHA 见清单。新 q=.17 输入来自本题 r=.3、w=.08、w_r=-1.8666666667、peak_fraction=.2 的成功开放前缀，完整512角点的两 jet SHA 为 `5c22c8ddd406bd7f129416a32dfb6a805758bdc0d077928463b6279017901433`。输入端口即使高于修正频率也完整保留；末端为指定平面圆环且与平帽匹配到二阶。输入前缀自身仍只匹配有限线性 DN，未与真实非线性振荡尾联立。

`analytic_collar_design.py` 先以切线角 β 的五次过渡及正弦控制，解两个子午线积分方程，给出恒速旋转参考；再用已知两端二阶 jet 替换参考的 Hermite 端数据。`general_analytic_collar_design.py` 将起始半径、坡度和坡度导数开放给新小切口，公式与实测真实端口同时保留。

`bounded_free_collar_design.py` 以角平均 E 作为新设计的目标 E(s)，对 E/L²∈[.5,1.5] 作罚项，并使用真实第一、二基本形式算主曲率平方和的平方根作约束；这是可采样的软罚项，不是严格界。相对度量残差包含 E 的全部角变动和 F，G 取角平均。每改变目标 E/G 都是设计，不是固定 g 加密。

## 实际结果

|试验|主要参数|最大相对 metric|最大主曲率|最小外向 X·n|状态|
|---|---|---:|---:|---:|---|
|旧q20缩短固定速度|L=.55, rise=.25, cap=.15, nc16,M8|.0010688331|9.268004|1.039211|118次收敛但未过metric|
|旧q20精确旋转参考|L=.5421784, rise=.25, nc18,M8|.0012683618|14.30422|1.145138|140次上限|
|旧q20有界自由E|L=.55, rise=.25, nc16,M8,曲率罚界10|.0003999107|9.955650|.912499|220次上限|
|新q17小切口首试|L=.2804966, rise=.10, cap=.05, nc18,M8|.0012969532|9.954526|.947191|160次；另有不相容优化下界|

前三个输入、全部参数、停止原因、输出 SHA 及采样网格在 `scripts/short_collar_trials_manifest.json`。有界自由 E 的实际采样范围为 [.2482133,.4541057]，最小面积元 .0825，未重现先前自由 E 坍缩；但 metric 仍约为门槛400倍，不能接受。

独立审计网格最高401×384，不与优化点相同；所有 reach、连续曲率与全时结论仍未获证。这些只是新连接器设计，未构成完整闭族。

## 小切口首试中的约束错误

旧代码的绝对角度量下界 G≥.005 在半径 .15 的圆帽上相容，但新 cap=.05 的端环强制 G=.0025，因此该罚项不可能全为零。这是设计设置错误，不能解释为该几何不存在或连接器必有残差。代码现允许显式 `--G-floor`，保留默认 .005 以精确复现旧试验；修正试验以 .0005 从首试暖启动，正在计算。旧首试参数和输出未覆盖，修正与旧结果分开记录。

对有界曲率残差的解析 Jacobian 作一次确定随机方向中心差分，步长1e-6及1e-7的相对无穷误差分别3.67e-10与1.12e-10；较大1e-5跨过max罚项的活动集，不能据此作光滑差分比较。这是实现检查，不是存在证明。

## 复现

先用本题 `recover_prefix.py` 恢复旧端口；小切口按高 q 清单运行到 q17 并执行 `smallcut_endpoint.py`。然后在单线程环境依次运行以下命令，路径替换为本地工作目录。所有输出留在临时目录，禁止提交系数数组。

```sh
python short_collar_design.py --trace OLD_TRACE --out Q20_L55 --length .55 --rise .25 --radius .15 --nc 16 --m 8 --nfev 140 --seed Q20_L65
python analytic_collar_design.py --trace OLD_TRACE --out Q20_REFERENCE --rise .25 --radius .15 --nc 18 --m 8 --degree 5 --bend 0 --nfev 140
python bounded_free_collar_design.py --trace OLD_TRACE --out Q20_BOUNDED --length .55 --rise .25 --radius .15 --nc 16 --m 8 --nfev 220 --curvature-limit 10 --seed Q20_L55
python general_analytic_collar_design.py --trace NEW_Q17_TRACE --out Q17_FIRST --rise .10 --radius .05 --r0 .3 --slope .08 --slope-r=-1.8666666666666667 --nc 18 --m 8 --curvature-limit 10 --nfev 160
python general_analytic_collar_design.py --trace NEW_Q17_TRACE --out Q17_CORRECTED --rise .10 --radius .05 --r0 .3 --slope .08 --slope-r=-1.8666666666666667 --nc 18 --m 8 --curvature-limit 10 --G-floor .0005 --nfev 160 --seed Q17_FIRST
```

Q20_L65 的生成命令见前一条新短尾笔记。继续真正非线性振荡尾与新圆弧核心两条路线，不以这些有限优化停滞替代原题完成条件。
