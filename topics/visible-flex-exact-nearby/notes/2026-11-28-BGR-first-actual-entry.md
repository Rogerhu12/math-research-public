# BGR3：完整原行的三个新 Gram 目标首次入口

2026-11-28，`visible-exact-astra-b0d5a16-20261128`。

本次将已完成的 [BGR 证明](../results/R149-supplement-complete-target-B-trial-Gram-and-joint-row-error.md)
及其原 pure 模块接到实际执行。尚未宣称三个新数值目标成功。

唯一新 manifest 为 `2026-11-28-target-B-Gram-inputs.json`，
75,836 bytes，SHA256
`0205e488d6932e2348725306f7be7e13d9829461b84cdedfe170e3cadeab24d3`，
含 185 个 current、51 个原 historical inputs。完整原 DWTB9
run45935081577/1 的所有已成记录不变。新工作依次是：

1. 用同一完整 96×192 试探行形成全 96×96 有符号 Gram，再给 operator upper；
2. 同一原系数误差的新 $L^\infty$ product；
3. 保留全部原误差项的完整 inverse96 row error。

原 grid、target w 与完整行仅作为必要输入按原全 SHA 恢复；旧 DWTB
系数/残差/范数、BNC 的观察和 BFP 的 forward 目标均不重新计算。
新结果不会以新 upper 减去旧 upper，也不会删除相位或两个 mean。

本地已对全 236 个输入做完整原 admission；51 个历史文件按原路径
及 sibling basename 恢复，字节数与 SHA 全部核对。此步未导入
numpy/flint/scipy，没有科学计算。实际三个目标在公开 Actions
运行，唯一路径 `.github/workflows/fourfold-codazzi-target-B-Gram-public.yml`。
新 consumed marker 与独立 group 只启动这三个此前未成目标。

完整输出须读取 actual 与 execution 后才能登记数值；全 Schur、
真正 homogeneous PDE 列和最终闭曲面族仍保留其全部独立义务。
