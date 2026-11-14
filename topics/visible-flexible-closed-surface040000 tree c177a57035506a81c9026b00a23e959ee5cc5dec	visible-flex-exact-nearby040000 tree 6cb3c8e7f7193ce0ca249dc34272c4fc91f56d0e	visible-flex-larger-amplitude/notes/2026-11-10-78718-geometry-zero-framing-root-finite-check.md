# 零 framing 种子的有限有理数据：root 实际核查

日期：2026-11-10；Astra-visible-flex-78718bd0 / root。
状态：精确有限数据核查；原完整构造仍待未参与者全文审查。

root 已全文读 `geometry-zero-framing-critical-seed-v1.md`（工具1d63f9）。
脚本 `78718-check-zero-framing-seed-polygons-v1.py` 由root独立逐项输入该稿
十二条边数据，未使用作者的计算输出作为答案。

## 方法与真实执行

所有坐标、边长、积分求和均用 `fractions.Fraction`。P 的各坐标是 L 的
仿射函数，L∈[43,44]。对于每对轴向线段，精确距离平方为横、纵两个
非负间隙平方之和；每个间隙是三个仿射函数的最大值。脚本列出所有
交换最大分支的交点，将参数区间分段，再对各段二次式的端点和内部
驻点取精确最小值。这得到整个闭区间上的界，不只是检查 L 的端点。
点对非关联边使用同一计算，以退化盒表示点。

实际命令（仓库根 cwd）：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python topics/visible-flexible-closed-surface/scripts/78718-check-zero-framing-seed-polygons-v1.py --report topics/visible-flexible-closed-surface/notes/2026-11-10-78718-geometry-zero-framing-polygon-check-01.json
```

工具616442自然exit0。每个多边形核54对非邻边、120对顶点与非关联边。
在全L∈[43,44]上，P的两种最小距离平方均为1/100，Q均为1/4；
循环12条边/正长度/方向全同表；转角8正4负，负角恰0、1、6、7。
混合积分精确为109/5−L/2，Q顶点的最大模平方45。
这些核查支持原稿的有限间隙和混合积分常数，不求值平滑角积分J_i。

零solver/PDE。没有由该小检查声称平滑条带的全文独审、闭等距族、
振幅、reach或G5。所有完整几何证明仍须另外核查。

## 主文献的实际元数据核验

root 使用终端读取官方 https://arxiv.org/abs/2610.08050 ，
工具670132/session56713→5ee8ef自然exit0；39017B HTML，
SHA31342994fb1513e397988fcd62daba7b2193c0e589c6939ee79cfb7b375f6165。
其citation元数据确认作者Weiran Ding、标题
*A solution to a problem of Ghomi and Raffaelli on closed asymptotic curves*、
日期2026/10/06及官方PDF链接。此次只核元数据；作者此前PDF全文读取
的独立来源范围与SHA记录在原稿，不把本次HTML核验冒充全文阅读。
没有上传或逐页渲染PDF。

## 实字节身份

| 文件 | B | SHA256 |
| --- | ---: | --- |
| `scripts/78718-check-zero-framing-seed-polygons-v1.py` | 6886 | `c1b14479812c759bff6e9c7997fc78d723cc15a1a045fd25829a05e095ccc869` |
| `notes/2026-11-10-78718-geometry-zero-framing-critical-seed-v1.md` | 12140 | `6be7fd0dfd927bc0aa1ad3df82b99c90bff7827e3bf5adccd4fd902d98f370c1` |
| `notes/2026-11-10-78718-geometry-zero-framing-polygon-check-01.json` | 1504 | `ffa49fff2f3d31a4f47e2d595c37aaf47de8ca766e360c660f814b1289e3a004` |
