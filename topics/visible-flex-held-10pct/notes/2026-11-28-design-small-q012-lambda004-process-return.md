# 小 q 原 λ=.004/M24 的真实进程终态

从真全门 λ=.002/M24 场续入原 λ=.004。原 pre-J 资源门先等 45 秒，随后真实 MemAvailable=1945116672 B 大于原需求1883198500 B，才进入原完整 J；预算与数学门均未改。原完整 QR factor 1、solve_calls 6 已返回，但在 BVP 的最终 RMS/raw/metric 返回以前数值子进程被 −9 终止。顶层控制器返回3，2026-11-28 14:21:24 UTC observer 已真实 join 所有自有子进程，无残余。

此次首次具有该中断的完整 kernel RUSAGE_CHILDREN：最大 RSS 为524404 KiB，CPU user83.555034秒、system1.319382秒；不是从末条日志推测的峰。这个数接近512 MiB，而此前成功的同 M24 恢复为518732 KiB。这仅是需读执行容器实际 cgroup/rlimit 的线索，不是已经证实的内存限额或 OOM 归因；先前主机 MemAvailable 也不能充当容器限额。

完整615×73节点与24个参数、23个scale已在原full-J前保存：`0fdf914d92a9dc84b45cb8ab3e3f7d92ec66c4b0faa908fbad88b161fc5add37`。没有更后的完整节点保存；原同factor下的 chord 步不能假称已保存。后继需保此真状态，并在原每个已接受Newton步之后保存完整节点，避免工程中断重付该段。M8/M16不重算。

没有原数学失败判断，也没有λ二分，真 accepted 仍为q=.012、λ=.002/M24。此轮释放大前缀 J 窗口给真q=.06/λ=.002的原generic8outer任务；设计仅准备后继，不并开J。相邻JSON绑定实际命令、原运行、节点、QR和真实终态。
