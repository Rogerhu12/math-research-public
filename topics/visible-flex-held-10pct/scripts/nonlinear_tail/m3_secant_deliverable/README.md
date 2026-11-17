# m3 fast45 小 cut：q=.02、.04、.06 的已完成开放前缀

结果是有限线性 DN 端口的真实 Cartesian BVP 解，尚不是闭合候选。真实尾的联合计算由另一个闭包记录。三个 q 点之间设计参数 delta 可变，不能称为同 g 加密序列；每一固定 q 的相位族才使用该点冻结的 g。

q=.04 从 q=.02 成功；q=.06 的普通单态缩放两次遇 Frenet 域错误，均保留。随后以两个成功点作 secant 初值，q=.06 在原方程、原 guard 和原 tol 下通过，采样 metric=1.14360068896e−7、κ=9.41069833、高度=.7826757293。失败不是幅度上界；secant 只改变初值，也未将成功当作严格存在性证明。

## 源与输入

70 项 `m3_source_recovery_manifest.json` 是 hash 核验的 source-only 闭包，含原 db6f coupled wrappers、原950f worker/client 和全部 CJS 工厂依赖、ShortBridge。另一代理已在新空目录实际恢复并真实启动原 worker，canonical8 端口字节 SHA 完全重现历史值。当前包不包含生成端口、H、chart、checkpoint 或网格数组。

```sh
python recover_m3_source.py --repo REPO --dest SCRATCH_RECOVERY
```

真实尾配置由 `m3-tail-input.json` 先删除 `valleyControlsPadTo`，再将 `valleyControls` 补零到160项后写到运行目录。用 `export_original_worker_port.py --source-topic SOURCE --config CONFIG --out PORT8` 从原 worker 启动再生。M16只将 modes 改16、quadrature改256，再生成 PORT16；完整物理参数不变。已执行的两个启动中前8列和 cut 字面相同。

先用 `linear_design_m3.py --source-topic SOURCE --port PORT8 --out CASE --vu .45 --vd .5 --short-bridge SHORT_SOURCE --curvature 4 --peak-fraction .2` 再生初始 profile/chart。然后复制端口为运行期 port.json / port-m16.json，并只在 `cut['_prefix_bridge']` 记录 profile 的 prefix_bridge 字典。该字段是前缀分派元数据。

`m3_secant_completed.json` 包含三次实际终态的完整原 argv、容差、输入/输出 SHA 和必要标量；可将路径映射到新 scratch 后逐条执行。q02、q04 用原 `linear_prefix_m3.py`，q06 用 `linear_prefix_m3_v2.py`，并分别将 q04/q02 成功 checkpoint 传给 `--restart` / `--secant-low`。最后由 `extract_m3_height.py` 再生完整有符号 upper H；原正 zr 尾 worker 应消费完整 −H，并在空间重建时反射完整 z（含均值）。

新目录、元数据路径、平台版本或求解器舍入可改变生成文件字节，历史 SHA 是已执行对象的标识；再生成应同时核物理参数、实际残差和同 g 加密。不存在旧历史 argv 的地方不得编造；本包三个主线点都有原 run.json。
