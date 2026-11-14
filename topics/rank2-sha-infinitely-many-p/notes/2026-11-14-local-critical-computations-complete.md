# 原临界三块的两项本地计算：完整有限结论

日期：2026-11-14。状态：**有限精确计算已完成；不作跨素数非零结论。**

根 README 的 2026-11-14 06:15 UTC 规则已停用公开 runner。原先排队的两项计算改在当前执行环境完成，每项使用两个 worker；两个驱动均正常退出 0。没有继续等待 CI，也没有扩大原先已指定的预算。

## 1. 原平方窗的完整矩形

对真实原来源 $\mathcal W_{D,J}$，令
$$
N=(J+1)\sum_{n=0}^D(e_{n+1}+1).
$$
枚举全部 $p>83$、$p\equiv5\pmod6$，使
$$
s=(p+1)/6,\qquad \ell=N-2s,\qquad1\le\ell<s-13.
$$
等价的有限素数区间是 $2N+26\le p\le3N-4$，另保 $p>83$。
目标是同一个原 $L=2s+\ell=N$ 的实际 $\bar J$ 方阵；完整低 theta 递推、原 $q_n$、所有角列、$T^j$ 和 Gaussian charge $n+36j/17$ 均参与计算。

此前已经完成 $2\le D\le8,\ 0\le J\le3$ 的 436 个方阵。本次只补其余部分：

| D | 新计算的 J | 实际方阵数 | 模 p 缺陷数 |
| ---: | --- | ---: | ---: |
| 2 | 4 | 8 | 0 |
| 3 | 4 | 15 | 0 |
| 4 | 4 | 21 | 0 |
| 5 | 4 | 31 | 0 |
| 6 | 4 | 38 | 0 |
| 7 | 4 | 44 | 0 |
| 8 | 4 | 61 | 0 |
| 9 | 0–4 | 216 | 0 |
| 10 | 0–4 | 253 | 0 |
| **本次合计** |  | **687** | **0** |

于是整个 $2\le D\le10,\ 0\le J\le4$ 的上述平方窗口共有 **1123 个**实际方阵，全部 $\bar J$ 可逆。对于这些有限输入，某个真实整子式为单位，所以原 $J$ 整可逆；由 R412/R428 的完整 $m_{13}$ 运输，原 $P_{134}$、$U_0$、总 charge 四十都保留的 $M^{\rm orig}$ 有
$$
N-26\text{ 个单位},\qquad26\text{ 个 }p,
\qquad13\text{ 个自由余核方向}.
$$
特别，真正第二余核只剩初始十三行，$K_2(M)\to K_1(M)$ 的像为零，没有非零模 $p$ 的原二阶来源向量。它们不提供所需的真正双侧缺陷实例。

可提交小文本位于 `notes/2026-11-14-local-critical-source-defect/`：

- `search-status.json`：九个任务均完成、退出码和实际耗时；
- `D2-progress.log` 至 `D10-progress.log`：每个 J 的累计计数及最终总计；
- `D*-defects.jsonl`：均为空，符合所有实际缺陷数为零；
- `driver.log`：本次调度及完成记录。

生成命令：

```sh
python -u topics/rank2-sha-infinitely-many-p/scripts/run-rank2-critical-source-defect-ci.py --workers 2 --out topics/rank2-sha-infinitely-many-p/notes/2026-11-14-local-critical-source-defect
```

## 2. p=3623 的十二个原定向预算

R409 的有限首对角计算发现 $T$ 在 $p=3623$ 的首权为零。这里没有将它认作完整 $T$ 中央失败，更没有认作两个完整中央同时失败。只检查此前已指定的以下全部平方预算：

| D | J | ell | N=L | 模 p 缺陷 |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 4 | 147 | 1355 | 0 |
| 11 | 3 | 60 | 1268 | 0 |
| 11 | 4 | 377 | 1585 | 0 |
| 12 | 3 | 268 | 1476 | 0 |
| 13 | 2 | 67 | 1275 | 0 |
| 13 | 3 | 492 | 1700 | 0 |
| 14 | 2 | 250 | 1458 | 0 |
| 15 | 2 | 436 | 1644 | 0 |
| 16 | 1 | 24 | 1232 | 0 |
| 17 | 1 | 166 | 1374 | 0 |
| 18 | 1 | 320 | 1528 | 0 |
| 19 | 1 | 476 | 1684 | 0 |

十二个真实 $\bar J$ 均可逆，故每个原完整 $M$ 同样恰有二十六个 $p$ 因子，真正 $C_2$ 只剩十三个自由行。第一行与第 1 节的矩形重合，不能把两次运行重复计为两个不同窗口。

全部证据在 `notes/2026-11-14-local-known-diagonal-critical/` 的 `actual-budgets.json`、`matrix-status.json`、各 `p3623-*-progress.log` 与 `driver.log`。所有 `*-defects.jsonl` 均为空。十二项累计 worker 时间约 191 秒；两 worker 并行。

生成命令：

```sh
python -u topics/rank2-sha-infinitely-many-p/scripts/run-rank2-known-diagonal-critical-ci.py --workers 2 --out topics/rank2-sha-infinitely-many-p/notes/2026-11-14-local-known-diagonal-critical
```

两脚本文件名保留原队列时期的 `-ci` 后缀以免破坏已有引用；运行本身完全本地。后续不扩大同类扫描，继续 R434 的原固定高轴与真实 $\tau_p$ 相容性，以及同一来源中确实存在的二阶双侧缺陷。
