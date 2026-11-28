# 混合 Gaussian 曲率的准确圆形继续种子

[R275](../results/R275-exact-mixed-gaussian-round-seed-with-two-true-ports-and-reach.md) 用显式分段多项式转角及两个真实积分定义整面。积分对称性决定中央半径和柱长，两端六 jets、准确等距、全核及真实 R210 帽的 reach 都由解析估计给出。相位在圆形增长参数为零时恒定。非零间隙步使用各自的中央、尾及 $g$，另行记录其真实误差。

令 `S` 为公开课题 scripts 目录，`OUT` 为新的可写文件。以下检查只需 Python 标准库。

```bash
python "$S/2ecf-round-mixed-K-exact-seed-budgets.py" --output "$OUT"
```

实际进程自然退出 0。源码的上下界用 $333/106<\pi<355/113$ 和有理平方比较，包含 $t=1/16$ 的严格负 Gaussian 曲率、整个转角曲率、meridian 锥、真实超高与帽输入。零间隙指定 $r_*=4/5,L=2/5$，$Z$ 是存储的 $.51$；程序不把这些积分替成浮点定义。

| 输入或输出 | SHA-256 |
|---|---|
| `2ecf-round-mixed-K-exact-seed-budgets.py` | `4d2814abdb8003fd9bcb5c3344a87f90fda438e5a874cd4446ee0b8d04171bda` |
| `round-mixedK-exact-seed.json` | `557a14b3917c6ee979b95387f92a2ab0812cd0447c29acb7ad9ab1c7f53d4e37` |
