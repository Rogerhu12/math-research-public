# 仅在 2、17 处分歧的四次扭曲候选清点

日期：2026-11-13。**状态：同源类的有限归约是直接证明；表中其余曲线的秩是当天官方 LMFDB API 返回的数据，仅用于选题，不作为本课题的新秩证明或 Sha 证明。** 三个已采用的秩二类已有仓库内的完整下降证明。

## 1. 固定支撑的完整归约

本笔记统一写 $E_D:y^2=x^3-Dx$。这与课题按 congruent-number 参数称呼的 $E_{34}:y^2=x^3-1156x$ 不同；后者在本笔记是 $D=1156$。

任意 $j=1728$ 的有理椭圆曲线可写成这个形式，且 $D$ 按非零有理数的四次幂取类。把它取为四次幂自由整数后，若坏素数只可能是 $2,17$，便有
$$
D=\epsilon 2^a17^b,\qquad \epsilon\in\{1,-1\},\quad 0\le a,b\le3.
$$
这是因为在奇素数处，四次幂自由模型 $y^2=x^3-Dx$ 的好约化要求该素数不整除 $D$。

标准二同源把 $E_D$ 送到 $E_{-4D}$；再按四次幂缩放，$a=2,3$ 分别与相反符号的 $a=0,1$ 配对。因此上述 32 个四次扭曲类至多只需查 16 个有理二同源类，代表可取
$$
D=\pm17^b,\quad \pm2\cdot17^b,\qquad 0\le b\le3.
$$
这里的二同源保持 Mordell–Weil 秩。没有把同源模型当作新的固定候选方向。

## 2. 官方数据库的固定候选表

以下所有条目的 `rank` 与 `analytic_rank` 返回值一致。链接指向相应的实际官方曲线记录。

| $D$ | LMFDB 标签 | 返回的秩 | 本课题用途 |
|---:|---|---:|---|
| $1$ | [32.a3](https://www.lmfdb.org/EllipticCurve/Q/32/a/3) | 0 | 原 CM 基曲线 |
| $-1$ | [64.a4](https://www.lmfdb.org/EllipticCurve/Q/64/a/4) | 0 | 没有新增秩二候选 |
| $2$ | [256.b1](https://www.lmfdb.org/EllipticCurve/Q/256/b/1) | 1 | 没有新增秩二候选 |
| $-2$ | [256.c2](https://www.lmfdb.org/EllipticCurve/Q/256/c/2) | 0 | 与新 E8 参考同源 |
| $17$ | [9248.c1](https://www.lmfdb.org/EllipticCurve/Q/9248/c/1) | 2 | 原 E17，R4 已给完整证明 |
| $-17$ | [18496.n2](https://www.lmfdb.org/EllipticCurve/Q/18496/n/2) | 0 | 与 R231 的 $D=68$ 同源 |
| $34$ | [73984.m1](https://www.lmfdb.org/EllipticCurve/Q/73984/m/1) | 1 | 不能加入当前秩二池 |
| $-34$ | [73984.d2](https://www.lmfdb.org/EllipticCurve/Q/73984/d/2) | 2 | 与 R239 的 $D=136$ 同源 |
| $289$ | [9248.f3](https://www.lmfdb.org/EllipticCurve/Q/9248/f/3) | 0 | 没有新增秩二候选 |
| $-289$ | [18496.j4](https://www.lmfdb.org/EllipticCurve/Q/18496/j/4) | 2 | 与原 $D=1156$ 同源 |
| $578$ | [73984.o1](https://www.lmfdb.org/EllipticCurve/Q/73984/o/1) | 1 | 没有新增秩二候选 |
| $-578$ | [73984.b2](https://www.lmfdb.org/EllipticCurve/Q/73984/b/2) | 0 | 与 $D=2312$ 同源 |
| $4913$ | [9248.g1](https://www.lmfdb.org/EllipticCurve/Q/9248/g/1) | 0 | 原 tame 三次角色未给新秩二类 |
| $-4913$ | [18496.h2](https://www.lmfdb.org/EllipticCurve/Q/18496/h/2) | 0 | 与 R231 的 $D=19652$ 同源 |
| $9826$ | [73984.e1](https://www.lmfdb.org/EllipticCurve/Q/73984/e/1) | 1 | 没有新增秩二候选 |
| $-9826$ | [73984.l2](https://www.lmfdb.org/EllipticCurve/Q/73984/l/2) | 0 | 与 $D=39304$ 同源 |

查询使用公开表 `ec_curvedata`，例如参数
`?ainvs=li0;0;0;-9826;0&_format=json&_delim=;`，读取 `lmfdb_label`、`Clabel`、`rank`、`analytic_rank` 字段。少数初次请求没有返回可解析的 JSON；在得到实际合法记录后才填表，没有从失败请求猜测标签或秩。

因此这次固定支撑清点没有提示第四个应当追踪的秩至少二同源类。当前三个已严格构造的来源并非漏查同一支撑中显然可用的另一条曲线。表格自身不是其余十三类的独立下降证明；若以后需要把排除结论作为定理输入，须另付下降或严格解析证书。

## 3. 保持原问题的范围

这次计算没有变化目标素数 $p$，也没有把数据库的解析 Sha 阶当作实际 Sha 有限性。它只关闭一次固定候选搜寻，并将研究返回 R243–R245 的三个实际中央行及其完整伴随比较。
