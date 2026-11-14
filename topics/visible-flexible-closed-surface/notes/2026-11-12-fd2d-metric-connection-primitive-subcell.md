# R180 原 P1 cell 内的准确验证子区间

这是 [R180](../results/R180-full-function-endpoint-primitive-and-material-drift.md) 一般 $[a,b]$ 结论的直接实现，不是新的字段表示或求解器离散。

新消费者 [fd2d_gc_connection_primitive_subcell.py](../scripts/fd2d_gc_connection_primitive_subcell.py) 提供 RestrictedConnectionEndpointPrimitive(field, cell, ta, tb)，其中 $0\le t_a<t_b\le1$ 是原实际 cell 内的准确归一化标签。验证局部标签 $r$ 与原标签满足

$$
t=t_a+(t_b-t_a)r,\qquad 0\le r\le1.
$$

物理子区间长是 $(t_b-t_a)$ 乘原准确物理 cell 长；原最后一格仍使用 $S-b_{\rm saved}$，而不使用 endpoint enclosure 中点。所有字段/角/物理径向导数依旧在原完整消费者中定义。改变的是 primitive 的两端函数与积分分段，不改变保存 mesh、54 参数、atlas、目标 $g$ 或实际场。

完整原 cell 索引始终保留。因此不会把一个只含 coast 的验证视图伪称为“最后 cell”，误用 terminal Gauss 恒等式。实际调用原领域消费者时，只映射查询标签；不构造另一个字段或替换其 last_cell 属性。

准确原生端值、$q=v-L_v$、负漂移项和第三分量仍由 R180 的证明支付。该证明适用于任意此类准确子区间，两端 $q,q_\xi$ 逐角恒零；不要求两端是 solver 节点。

## 已发生的唯一实际小核

输入仍是 dyadic30 archive 3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981、同准确新 $\delta$ packet 和同 R170 完整 native definition。原 cell 69 内选择 $[t_a,t_b]=[1/4,3/4]$，局部 $r=1/2$ 准确对应原 $t=1/2$；实际原 cell 索引仍为 69。

该次程序作为真实 here-document 执行：session 54216，首块 69f13e、末块 d8d1fd，exit 0；内部耗时 0.5006752100016456 秒。原程序核完整实例、准确标签映射、非零内部 $q$ 和两端准确 $q=q_\xi=0$，并消费一个正宽连续矩形。[实际报告](2026-11-12-fd2d-metric-dyadic30-connection-subcell-R180-01-report.json) 保持原字节。

与已经闭存的整 cell primitive 在同一个物理中心点比较：

| 准确 primitive 端点 | 中心点 $E$ 范数上界 | 各自小盒 $E$ 上界 | 各自小盒 $q$ 上界 |
| --- | ---: | ---: | ---: |
| 原 $t\in[0,1]$ | 0.38339241397 | 0.38483340326 | 0.006779743504 |
| 原 $t\in[1/4,3/4]$ | 0.36714194798 | 0.36915467471 | 0.001747002961 |

两条小盒各自使用局部标签 $1/2\pm2^{-16}$ 和同角半宽 $2^{-22}$，所以第二条对应的原径向半宽也缩小一半。表中没有将盒宽变化和 primitive 变化的作用混成单独的普适因果结论。当前场本来有较大的真实缺陷；本次不宣称其全域 posterior 通过。

## 可复现入口

[fd2d-metric-connection-subcell-check.py](../scripts/fd2d-metric-connection-subcell-check.py) 是保存原算法后的可配置 replay 入口。本次首次真实运行发生在 here-document 中，清单不会冒称后来保存的 CLI 文件就是首次执行源。重做命令如下，输出 stem 必须未存在：

~~~sh
PYTHONPATH=/workspace/scratch/fd2d-recovered-deps/python-flint-0.9.0 \
python scripts/fd2d-metric-connection-subcell-check.py \
  --native-definition notes/2026-11-12-fd2d-dyadic-tail-accurate-last-cell-30-01-native-definition.json \
  --profile-packet notes/2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-02-packet.json.gz \
  --out-prefix notes/2026-11-12-fd2d-metric-connection-subcell-replay
~~~

仅保存并作语法检查的 replay 入口与真实已执行的数学消费者分别记账。没有重跑旧 F/J、BVP、whole-body 或 whole-domain 证书。

