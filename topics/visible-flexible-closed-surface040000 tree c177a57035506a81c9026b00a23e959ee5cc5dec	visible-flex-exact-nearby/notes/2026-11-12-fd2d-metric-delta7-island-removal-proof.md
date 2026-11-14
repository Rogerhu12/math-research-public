# 只增大第七个 bump 系数以消去晚段正 K 岛

状态：**充分条件的完整证明已得；精确 89 盒最大值尚待执行已保存脚本。**
本说明不声称阈值数值已算出。它只复用 R182 已证明的连续盒，不重跑 F/J、
BVP、body、ODE 或 profile 区间。

## 准确输入与问题

固定 34 接受态 b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f
的准确 base 以及前六个实际 profile 系数。把第七个系数 $\delta_7$ 增大，
仍要求不超过原 binary64 参数上限 0.08。

目标区间是 R182 已保存的准确 dyadic 闭支撑 $I=[A,D]$，显示端点
$1.423,1.445$：

$$
A=\frac{801077783718527}{562949953421312},\qquad
D=\frac{6507701461550367}{4503599627370496}.
$$

这明确了十进制标签的含义，没有把标签偷偷改成另一对准确十进制有理端点。

区间数据为
notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-rows.json.gz，
SHA256 d7f990bcef75ec30311e23d3cf92dadf5736f871f141dd3f7fa62071f7793095；
配套报告 SHA256 44d3d9318ffa7b70f7bcc59cebf81df09e72b9c37562c05e1410cdb65b627a68。

## 单系数连续充分条件

准确 profile 为

$$
a(s;\delta)=a_{\rm base}(s)+\sum_{j=1}^7\delta_j\psi_j(s).
$$

在 $I$ 上，前六个 bump 已超出各自紧支撑，故其二导恒零。
R182 的 89 个连续盒覆盖整个 $I$。对每盒 $I_b$，从已保存准确 dyadic
端点取

$$
b_b\le a_{{\rm base},ss}(s),\qquad
0<B_b\le\psi_7''(s)\qquad(s\in I_b).
$$

如果 $\delta_7\ge0$，则逐点有

$$
a_{ss}(s;\delta_7)\ge b_b+\delta_7 B_b.
$$

因此定义准确有理数

$$
T=\max\!\left(0,\max_b\frac{-b_b}{B_b}\right),
$$

任何满足

$$
\max(T,\delta_{7,\rm old})\le\delta_{7,\rm new}
\le {\rm binary64}(0.08)
$$

的系数都在整个 $I$ 上保证 $a_{ss}\ge0$。
只要半径保持正，即有 $K=-a_{ss}/a\le0$，所以原正 K 岛消失。
这是充分阈值；各盒 base 与 bump 下界分别包围，故不声称它是最优阈值。

所有上式只涉及整数和有理数运算。脚本逐行验证连续盒无缝相邻、
前六个二导基确为零、第七个严格正、端点与报告一致，再计算最大值。
如果原上限允许，脚本取一个在该阈值之上的百万分数作为显式 witness，
并给出所有盒上 $b_b+\delta_{7,\rm new}B_b$ 的最小准确下界。
若上限不足，脚本如实输出本充分条件未给出可行 witness，不将其等同于数学不可能。

## 正半径和原 protected 末窗

第七个紧支撑 bump 为

$$
\psi_7(s)=1024t^5(1-t)^5,\qquad
t=(s-L_7)/(R_7-L_7),\quad 0\le t\le1,
$$

区间外为零。因此 $\psi_7\ge0$。只增加 $\delta_7$ 时

$$
a_{\rm new}-a_{\rm old}
=(\delta_{7,\rm new}-\delta_{7,\rm old})\psi_7\ge0.
$$

原已证全域半径下界
$18103121383342981011/23058430092136939520>0$
直接保留，不需要另加小扰动半径门。

准确右支撑端点为

$$
R_7=\frac{3307833529335461}{2251799813685248},
$$

恰等于旧 protected terminal start，显示值 1.4689731783581288。
该 bump 的值和一至四导数在右端都为零，且之后恒零。
故原 protected 末窗上的 $a$、度量、$K$ 及其已声明导数保持完全相同。
新增设计在左侧确实改变物理 g，不能将旧完整 F/J/几何结果当成新 g 的结果。

## 可执行消费者

scripts/fd2d-metric-delta7-island-removal-threshold.py 是独立 stdlib/Fraction
消费者。它在 executor unavailable 时写成，目前没有真实执行记录。
在本课题 cwd 的命令为：

    python scripts/fd2d-metric-delta7-island-removal-threshold.py \
      --output notes/2026-11-12-fd2d-metric-delta7-island-removal-01-report.json

默认读取上面已推的两份输入，核其完整 SHA256；不需要 flint 或 NumPy。
运行结果将给出准确 T、原上限比较、witness 和连续 a_ss 下界。
当前说明没有据首盒或某节点推断全域阈值。

消去这一个标量正 K 岛只提供新的 g 设计方向，不证明新的完整闭曲面已满足
等距、曲率、reach 或形状幅度条件。它也不要求继续使用 R182 late signed 窗。
