# 前缀到实际尾的高度符号：撤回额外 π/2 相位建议

## 实际代码约定

`root_actual_neck_bvp.py` 的实际函数是

```python
def tail_height(self,y):
    return self.bridge.sigma*self.q*np.asarray(y[self.iz:],float)
```

当前 `alternative-neck-provider.py::NeckTerminalBridge` 明确设置
`sigma=-1`，所以待求尾的完整 Dirichlet 向量为 **H=−q y[iz:]**。
`db6f-prefix-tail-trial-client.py::WeightedTailPort.solve` 仅转成 float，
检查 shape/finite 后原样写入 request.height，没有再反射或转相位。
`tail_stored_client.py` 直接复用该 solve 方法。联解文件也明确写有
`Z_prefix = sigma Z_tail + constant`。

此前聊天中的比较直接取了前缀 `q y[iz:]`，漏掉已有的高度反射，再根据
H₂ 正负建议对旧尾数据旋转 π/2。**该建议撤回。** 坐标平移与上下片高度
反射已经包含在联解约定中，不应再据此对 warm 施加 π/2 变换。

## 实际保存包的逐模读取

`strong_tail_trace_check.py` 验证各 coeff 块 SHA，使用原物理五次多项式
最后区间的 Horner 值取得完整端点，实例化实际 bridge，并从联解文件
AST 取出原 `tail_height` 函数执行。没有启动 worker、没有 Newton，
也没有生成任何变换后的初值或新的成功响应。

| 保存对象 | H₂ | H₄ | H₆ |
|---|---:|---:|---:|
| 旧真实 q040/M14 warm 的 request.height | −1.3255890659493767e−5 | −4.4314567155666715e−9 | +1.1360945221954465e−11 |
| 恢复的 first675 q085/M20，按实际尾约定 | −2.280325086533358e−5 | +1.5841039043170376e−8 | −4.8102183560904645e−12 |
| angle vu032 q085/M20，按实际尾约定 | −2.166791494264275e−5 | +1.3906395882015728e−8 | −4.1370435279040695e−12 |

旧 warm 文件是
`root-neck-k7-v098-q040-actual-m14-tail-response_0003.json.gz`。
其 request.height 与完整 checkpoint.cutHeight 逐字相等，finite response
converged=true、记录 residual=1.6420129765077173e−9。两个前缀中保存的
physical_tail_parameters 与该 checkpoint 的对应参数全部相等。

旧 worker 的 amplitude warm 按首模比值整体缩放非恒定高度，然后对**完整**
新 Dirichlet 差施加有限线性响应修正，最终仍由真实非线性 DN 求解决定
成功。这里 first675 的首模比为 1.7202352864160106，angle vu032 为
1.6345876334702836，均在原代码允许的 (.25,4) 内。整体缩放后必须补的
H₄ 分别为 +2.3464187255513362e−8、+2.115000022753985e−8；因此旧 warm
只是初猜，不能把这条边界变化称成同一完整向量射线。

若额外对 warm 旋转 π/2，则 H₂ 被反号，以上首模比会变负，反而无法
走原正比值 amplitude warm 路径。当前没有转换包的需求，因此没有添加
`strong_tail_phase_warm.py`，也没有动当前 tail worker。

完整 M14/M20 向量、逐模差、原 q070 尾射线对照以及代码/数据 SHA 在
`2026-11-12-strong-tail-height-convention.json`。比较旧 M14 与 M20 时的
高模补零仅遵循原 warm 嵌入约定，不宣称旧 M14 解的未计算高模为零。

## 复算

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python computations/strong_tail_trace_check.py \
  --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
  --prefix notes/2026-11-12-strong-first675-q085-m20.json.gz \
  --prefix notes/2026-11-12-strong-angle-vu032-q085-m20.json.gz \
  --warm notes/root-neck-k7-v098-q040-actual-m14-tail-response_0003.json.gz \
  --ray-response notes/numerical-neck-q070-tail24-base-response_0001.json.gz \
  --out notes/2026-11-12-strong-tail-height-convention.json
```

这些结果只校正符号约定和初值比较；没有增加尾容量、前缀闭合或连续
几何结论。
