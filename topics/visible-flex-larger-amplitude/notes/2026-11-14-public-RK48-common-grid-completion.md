# 公开 Actions 补齐旧 A 的 RK48 全共同网格和闭组装

2026-11-14，exact_refinement，AI 辅助。**原来中断的有限计算已补齐；同度量全过程收敛和目标幅度仍未完成。**

来源：[公开 run 43579782197](https://github.com/Rogerhu12/math-research-public/actions/runs/43579782197)。本次直接复用已经真实求解并保全的同 $g$、同完整 32H 的 RK24/RK48 shooting 响应，重建真实径向读出，插入全部 source breakpoints，完成两次原来中断的共同网格比较、固定 collar 界和闭组装。没有重复已经成功的非线性求解，也没有把旧 RK12 endpoint 冒充新解。

[pipeline terminal](public-actions-43579782197-1-rk48/reports/terminal.json) 明确 `finished=true, success=true`，所有子命令 exit 0；本段实际运行约 707.42 秒。terminal SHA-256 为 `de24a8d3c29f0195ff966c2431de3d656c9ef1443f9c98195783f77af2b39e25`。

## 两种加密的不同结果

以下是同 $r,\theta$ 网格和同均值锚下的完整表示域有限样本。保留所有 source knots，角数为 1024；第一项覆盖 4638 个共同径向区间、78846 个径向样本，第二项覆盖 9244 个区间、157148 个径向样本。

| 比较 | position 最大差 | radial first 最大差 | radial second 最大差 | metric 标量差 | curvature 标量差 |
| --- | --- | --- | --- | --- | --- |
| 新 RK24 → 新 RK48，同 f8 读出 | $9.30524\cdot10^{-15}$ | $2.42553\cdot10^{-11}$ | $7.02742\cdot10^{-6}$ | $4.78926\cdot10^{-11}$ | $1.85198\cdot10^{-6}$ |
| 同新 RK48，f8 → f16 读出 | $2.66413\cdot10^{-13}$ | $1.12479\cdot10^{-8}$ | $.0029137968004$ | $2.16149\cdot10^{-8}$ | $.0007092930646$ |

两个报告分别是 [common-RK24-to48-eight.json](public-actions-43579782197-1-rk48/reports/common-RK24-to48-eight.json) 和 [common-RK48-eight-to-sixteen.json](public-actions-43579782197-1-rk48/reports/common-RK48-eight-to-sixteen.json)。其 SHA-256 依次为 `0b054f17d58a6992cc60bd539125cb877385ebd432fd41770613ee105e9aee0a`、`a72d76296ef0e8e99b1bc22634a137c366717d973127ed98ac3d38288d8ebef0`。

径向射击的 RK24→48 差已经很小，但物理五次读出的 f8→f16 二阶差仍约 $.0029$。因此不能只根据 position 接近浮点精度就宣称完整 $C^2$ 或首二阶 jet 达到求解器/机器精度。

进一步按相同外接缝宽度 $.01$ 分区：

- RK48 f8→f16 时，外接缝区外最大 metric 样本从 $2.1614936937\cdot10^{-8}$ 降到 $2.0760835767\cdot10^{-9}$。
- 整个尾/外接缝表示的最大值仍为 $4.7703317350\cdot10^{-8}$；最大点在使用原前缀 target 的切口。
- 原前缀、其完整均值锚和所有原系数在本次比较中完全未变，也未用新 DN 重新求解前缀。这个平台不能用继续只细化旧尾来冒充前缀加密收敛。

本次两份完整输出替代以前只有 3456/4638 和 3648/9244 进度的中断 checkpoint；原中断与磁盘空间有关。本次没有遗留该两项消费者的未完成部分。

## 固定有限 collar 的连续界与闭网格

[finite-collar-bound.json](public-actions-43579782197-1-rk48/reports/finite-collar-bound.json) 对已导出的准确 binary64 Fourier jet 定义的固定有限 collar，使用准确有理 Bernstein/角系数三角界，给出全半径、全角度的相对 metric operator defect 上界

$$1.0013852491260307\cdot10^{-18}.$$

宽度仍为 $.0005615866909020606$，没有通过收缩 collar 掩盖误差。该上界严格属于这个有限 collar；它是非零界，不是无限非线性尾的精确等距证明。对应报告 SHA-256 为 `0380ac618559ac9a2c854b00b2a58f7971bc88957b7f379aee953534dccdb7bd`。

[closed/summary.json](public-actions-43579782197-1-rk48/reports/closed/summary.json) 和同目录三份 mesh 确认：

- 73442 个顶点、146880 个三角面，Euler 数 2；每条边恰属两个面，零面积面数为 0。
- 三个压缩 mesh 都小于 5 MB；对应 $t=0,.5,1$。
- 点云直径为 $3.977459266677549$，固定帽点云直径比为 $.9980148410$；全部固定帽在每个 phase 保持不动。
- 九个 phase 的最大顶点云 Hausdorff 为 $.25063813746459784$，归一化仅 $.0630146333777444D$，明显低于所需 $.2D$。这些点云数值本身也不是连续整面 Hausdorff 证书。
- moving/fixed 的全部连续 phase 法向弦最小化，在保存的空间点对上无负数；moving/moving 和 fixed/fixed 的空间样本同样无负数。三类仍是有限空间样本，不是连续 reach 界。

闭组装 summary SHA-256 为 `751e0695fc152d641ae217cd6872b9e888fb687850e7f38df7d747235d7bc142`。当前旧 A 完整样本的幅度不足；这次恢复支付了明确中断的有限计算，不改变其限制，也不替代新的大核心整段 BVP 主线。课题未完成。
