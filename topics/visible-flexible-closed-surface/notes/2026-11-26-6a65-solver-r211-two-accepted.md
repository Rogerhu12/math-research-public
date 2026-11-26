# R211 已保存分支的两次真实接受与当前度量瓶颈

2026-11-26，Astra-visible-flex-6a65e705-20261126 / resume_solver。

**可信度：可复现的有限数值证据；不是完整闭曲面或精确等距存在结论。**

本次接续公开仓库已保存的 `R211-full-half-01-initial`。它继承 R208 第8态的1025个完整参数，原来只是准备输入，没有已保存的真实R211接受回执。本次不重做R208八步。

## 真实运行

首个原入口的终端Node进程返回 **exit 137**，没有产生接受态或checkpoint；具体杀死原因没有取得证据，不把它冒充方程不收敛。随后仅把精确切片缓存容量由 value=512、derivative=320 改为8和4，使用Node v24.22.3、`--max-old-space-size=768`。缓存改变不改函数、样本、权重、参数列、normal或Armijo规则。

新入口 `scripts/6a65-continue-r211.cjs` 的完整两步真实自然退出 **0**，总耗时58.7071秒，子进程峰值RSS 560344 KiB。每步均重算完整normal（18.609秒和18.653秒），未复用旧normal。原完整106920条行及1025列保留。

| 量 | 同R211新目标的实际基线 | 第1次接受 | 第2次接受 |
|---|---:|---:|---:|
| 总平方残差 | 0.012140203833724286 | 0.011975394130972490 | 0.011856666403765490 |
| 最大采样相对metric | 0.4448327457513894 | 0.45043075522038845 | 0.4520835305122641 |
| 最大采样主曲率 | 12.037909108136335 | 11.547727519212682 | 11.368804706665058 |
| Armijo实际步长 | — | 1/2 | 1/2 |
| 实际尾幅参数 | 0.3474631034（父态记录） | 0.35683665371098383 | 0.36571042144986887 |
| 实际内cuff高度 | 0.5868115567（父态记录） | 0.5881871142083718 | 0.5894200898374754 |

最后状态仍有宽度超额0.04805506543、高度超额0.00638137924、held距离不足0.07527365116。总目标下降伴随metric峰值上升，故这两步只表明原R211迭代可实际续算，**不能解释成更接近完成标准**。当前最大metric仍比1e−6要求大五个数量级以上；未支付非局部reach或全域区间余项。

## 复现

在仓库根目录执行（输出目录仅为本地可重算中间数据，不提交）：

```sh
node --max-old-space-size=768 topics/visible-flexible-closed-surface/scripts/6a65-continue-r211.cjs \
  topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
  topics/visible-flexible-closed-surface/notes/2026-11-13-fd2d-R211-full-half-01-initial.json \
  /tmp/visible-flex-r211-replay 2 8 4
```

这些输入均为公开仓库已有小文件；不需要旧环境未推送数据。输出checkpoint可用于继续实际步骤。准确目标仍为原R211四次曲率罚，原height/geometry规则保持；不是R210升喉目标，也不把原R208目标值当成R211基线。

## 输入与输出身份

| 输入 | SHA-256 |
|---|---|
| `scripts/6a65-continue-r211.cjs` | `a1232599a9c2f65a69405755d46a97af19777299d6da6cba3a2a1705c0f9a8c4` |
| `scripts/fd2d-run-full-half-quartic-R211.cjs` | `7c3b7d384c3fa3fc90294e5545e0500595edd0ec9d044695fb14cee67af6ab8b` |
| `notes/2026-11-13-fd2d-R211-full-half-01-initial.json` | `f0ef3eb228a74a7987b0028285e113a15b25f0b32828a25fced1aabec5c35379` |
| `notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json` | `9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d` |

以下输出仅保存在本轮临时目录；依根README第15条只保存哈希和脚本，不把可复算数据入库。

| 输出文件 | SHA-256 |
|---|---|
| `r211-lowcache-1.json` | `f129a383cd9b587554f6f57e7b3ec00c053c9eb05a1932dbe0834c24f606750c` |
| `r211-lowcache-2.json` | `777760e5f10d7fd6df817c4c767b1264fac3bb7f8e5d55cd365fe5597328b8fa` |
| `r211-lowcache-exit.json` | `8f4a07757f148885dee4035050a9885cff813a3f070a0c550c7a62dafd85780e` |
| `r211-lowcache-final.json` | `4492e5863f479084b2f0f6acb2d03c48f52fde7e7aac437ba63f082d31ad25fa` |

## 接续方向

原`R208`至`R211`反复在降低平均平方罚项的同时容许中央附近的metric峰增长。下一实际设计需处理这一几何瓶颈：完整高峰权重或改变非中央外段可用经线长度；任何新目标、g或参数域须自己的基线，最后冻结后再做同g加密。没有将本次有限迭代登记为完成。
