# q=.045/M16 的实际 λ0 设计前缀

依赖相邻 `complement_prefix_batch1/prepare_runtime.py`、`complementary_controls/` 和先前 q04 checkpoint 的实际再生。将本包两个 driver 复制入该 scratch runtime 后执行 `completed.json` 的完整 runtime_argv；source_topic 指向新恢复路径。所有输入输出 hash 与真正启动时 source hash 已保存。所有生成数组只留在 scratch。

recorded driver 对此前 scaled-check 版本只增加启动 argv/source 来源记录；scaled-check 改变差分审计的方向归一化与步长，不改变 BVP Jacobian、方程或接受门。先前高 M 的任意大差分方向会触核心正性守卫，现按真实 rho-control bound 归一化，未将门降级。

本次 q 与 δ 是设计参数变化，λ0 仍无精确保护圆弧，仅使用原真实线性端口。完整曲面与固定 g 收敛未获证。
