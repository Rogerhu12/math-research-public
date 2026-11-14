# 新网格基准的监测范围

root session50791按已冻结r2计划运行单个3178×384 baseline，原数学入口、全部raw/modes/mean未变。外层运行器尝试通过/proc/<wrapper-pid>/task/<wrapper-pid>/children读取其字段子进程以实施220MiB cap，但实际逐次记录的子PID列表为空；因此没有证据表明该cap生效，不将peak_observed=0当作真实内存值。最终资源以原strong_resource_run.py的正式wait4结果为准。无第二个几何场、新BVP、Jacobian或Node启动。

此限制不改变已完成的数学计算；也不将本次外监测的0值复制为正式峰值。后续若需要自有限制，应在字段执行进程内部读取自身资源，避免依赖跨命名空间的PID路径。
