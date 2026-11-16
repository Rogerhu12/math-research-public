# 冻结 psi3 外 cap 的唯一新复积分区间观察设计

日期：2026-11-16。状态：**仅写源码及参数，未执行、未编译、未运行开发检查或旧科学。** Root 统一部署、读取真实规则并触发唯一公开 Actions。

入口：`scripts/frozen_psi3_complex_cap_interval_audit.py`。请求：
`computations/request-frozen-psi3-complex-cap-interval.json`。
工作流由 root 接到
`.github/workflows/visible-frozen-psi3-complex-cap-interval.yml`。

## 1. 唯一新问题与不重算范围

[R471](../results/R471-five-real-cap-conditions-and-the-complete-complex-second-moment-interface.md)
已给完整真实复余量

$$
E(z)=\frac32\int_\ell^T(x+z)^2w_z(x)^2a_z(x)^2q(x)\,dx.
\tag{1}
$$

原局部 primitive 与 self 端项已经在该身份中抵消，不能再次加减它们。
当前 [R455](../results/R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md)
的两外 cap 是下述固定函数的正幅、正仿射像：

$$
u(x)=\exp[-3/(1-x^2)],\qquad -1<x\le T.
\tag{2}
$$

本任务只对(1)在这个**固定 cap**的上半平面二矩根求一个严格复区间。
不恢复 XH/XY mixed 根，不运行原四 self 的85条记录，不重建响应，
不求任何旧秩，不构造或优化新 profile。下根值由实系数共轭性得到，
不是第二次计算。

既有四 self 科学钟 `15.69076311099991` 秒是关闭的来源账。本任务只加
一个新的不超过240秒入口段；旧四 self 本轮调用次数为0。

若一个分量的完整区间严格离0，即证明这个固定 cap 的 $E(z)\ne0$。
若预算内未分离，只输出 unresolved，不能称 $E=0$、MEMBER 或五门已付。
本观察亦不证明所有满足 $A_f>0$ 的 cap 都非零。

## 2. 从原 cap 得到准确有理密度

设 $d=1-x^2$，$P=3x^4+4x^2-1$。对(2)逐原式求导，

$$
\frac pu=-\frac{6x}{d^2},\qquad
\frac ru=\frac{6P}{d^4},\qquad
\frac qu=\frac{36x(1-2x^2)(x^4+4x^2+1)}{d^6}.
\tag{3}
$$

完整退化量为

$$
\frac{A_f}{u^2}
=\frac{72\,F(x^2)}{d^8},\qquad
F(t)=27t^4+102t^3-46t^2-10t-1.
\tag{4}
$$

$F$ 从最高项到常数只有一次符号改变，故恰有一个正根。原准确端点：

$$
F(11/20)=-155853/160000<0,\qquad
F(3/5)=1232/625>0.
\tag{5}
$$

以 $\alpha$ 表示该根，$T=-\sqrt\alpha$。因 $\alpha>11/20>1/2$，
左 cap 内 $q>0$；又 $F(x^2)>0$ 于 $x<T$，所以 $A_f>0$，
$T$ 是其实际根。程序只做这个新目标必需的精确有理根夹，
不从浮点 root 或旧 profile 样本取值。

令

$$
a=\sqrt\alpha,\quad d_*=1-\alpha,\quad
P_*=3\alpha^2+4\alpha-1,
$$

$$
s=\frac{a d_*^2}{P_*},\qquad
h=\frac{d_*^4}{6P_*},\qquad
\delta=\sqrt{2h-s^2}>0,\qquad
z=a+s+i\delta.
\tag{6}
$$

这里 $s=p(T)/r(T)$、$h=u(T)/r(T)$，所以
$z=-\operatorname{mean}(q)+i\sqrt{\operatorname{Var}(q)}$，
与原全 cap 的三个末端矩完全一致。不是在一个舍入后的 $T$ 上另求根。

记 $\zeta=x+z$，并定义

$$
B=x d^2+\zeta P,\qquad
A=d^4+6x\zeta d^2+3\zeta^2P.
$$

则 $w_z=-6uB/d^4$、$a_z=uA/d^4$。
式(1)的**完整**复密度是

$$
\boxed{
f(x,z)=1944\,e^{-15/d}
\,\frac{\zeta^2x(1-2x^2)(x^4+4x^2+1)B^2A^2}{d^{22}} .
}
\tag{7}
$$

程序直接消费(7)，没有只取一个 principal，也没有假定复被积式为正。

## 3. 平端没有被截掉：解析 tail 界

固定截点 $x_c=-19/20$，$d_c=39/400$。由(6)的根区间，
程序须严格包住并确认粗界 $|\operatorname{Re}z|+|\operatorname{Im}z|\le2$；
若不能确认，完整观察失败，不能继续使用该尾界。

对 $-1<x\le x_c$，

$$
|\zeta|\le3,\quad |P|\le6,\quad |B|\le19,\quad |A|\le181,
$$

以及
$|x(1-2x^2)(x^4+4x^2+1)|\le6$。因此

$$
|f(x,z)|
\le C_{\rm tail}e^{-15/d}d^{-22},\qquad
C_{\rm tail}=1944\cdot9\cdot6\cdot19^2\cdot181^2.
\tag{8}
$$

函数 $e^{-15/d}d^{-22}$ 在 $0<d\le39/400$ 上严格递增，因为其
对数导数的符号为 $15-22d>0$。原遗漏段长度为 $1/20$，故

$$
\boxed{
\left|\int_{-1}^{x_c}f(x,z)\,dx\right|
\le B_{\rm tail}
:=\frac{C_{\rm tail}}{20}
 e^{-15/d_c}d_c^{-22}.
}
\tag{9}
$$

程序以有向区间求(9)的上界，分别给实部和虚部都加
$[-B_{\rm tail},B_{\rm tail}]$。这是实际平端积分的完整包络，
不是把小值当零，也没有用一个数值积分样本估计尾部。

## 4. 所有数值是有向 dyadic 有理区间

固定 $Q=2^{256}$。每个区间储存两个整数
$[l/Q,u/Q]$。加减是精确整数运算；乘法取四个端点积的最小、最大，
再分别向下、向上除以 $Q$。倒数在确认不跨零后用单调性与精确整除。
不使用二进制浮点做任何数学门判定。

$\alpha$ 由(5)开始，至多160次精确 `Fraction` 二分；每次原多项式
值精确取号，最后再向外转入 dyadic 区间。平方根通过整数
`isqrt` 对 $lQ,uQ$ 取下根/上根。所有端参数(6)都由同一个
$\alpha$ 包络计算，而非各自用一个独立 nominal 样本。

### 指数的完整严格界

只需要 $\exp(t)$，其中 $-256\le t\le0$。把 $v=-t/512$ 包在
$[0,1/2]$ 内。对固定真实 $v$，

$$
\sum_{k=0}^{47}\frac{(-v)^k}{k!}
\le e^{-v}\le
\sum_{k=0}^{48}\frac{(-v)^k}{k!}.
\tag{10}
$$

程序用有向区间计算两有限和，取47项和的下端与48项和的上端。
由 $0<e^{-v}\le1$ 合法裁切到 $[0,1]$，再作9次有向平方。
对一个指数区间的两端分别求界，并用指数单调性包住整个区间。
这是严格交错级数界，不是固定阶 Taylor 近似值或经验误差。

每次倒数、平方根与指数的适用域都由当前新目标的区间确认；
域未确认时保存失败和已有有限状态，不加 jitter、不改公式、
不切换到旧计算器。

## 5. 可变上限与复参数依赖同时入账

有限段换元为

$$
x=x_c+(T-x_c)y,\qquad0\le y\le1.
\tag{11}
$$

程序积的是

$$
F(y)=(T-x_c)f(x_c+(T-x_c)y,z).
\tag{12}
$$

区间中的 $T,z$ 在全部操作中作为同一个真实未知参数的外包；
依赖重复会使界变宽，但不会漏掉误差。式(11)同时处理上限的
不确定性，不把它偷换为固定舍入端点。

没有在 $\alpha,T,z$ 的中点作一次点积分再追加猜测误差。
真实端点误差、平方根误差、指数界和所有有理舍入都已经进入(12)。

## 6. 六阶 Taylor 区间积分及有限细分

每个 dyadic panel 为 $[m-h,m+h]\subset[0,1]$。
自动微分 jet 的第 $j$ 项准确表示 $F^{(j)}/j!$ 的区间，
通过加乘、倒数、整数幂与指数的原链式递推求得。指数递推是

$$
b_0=e^{a_0},\qquad
b_n=\frac1n\sum_{k=1}^n k a_k b_{n-k}.
\tag{13}
$$

在中心 $m$ 求点 jet，在整个 panel 上另求一个区间 jet。
后者包住该 panel 中每个真实点的六阶导数系数，并非两个点值的差。

Taylor 定理给每个实分量

$$
\boxed{
\int_{m-h}^{m+h}F(y)\,dy
\in
\sum_{j=0,2,4}\frac{2h^{j+1}}{j+1}\,[F_j(m)]
+\frac{2h^7}{7}\,[F_6([m-h,m+h])].
}
\tag{14}
$$

奇数中心项准确积分为零；六阶余项的乘子非负，
所以(14)直接使用完整导数区间。实、虚部各自应用同一个公式。
区间 Taylor 运算只是这个唯一新标量复积分的求界，不是旧几何 JVP、
旧 self 观察或 profile 的另一次检查。

固定先放8个等长 panel。之后每次只分裂当前界宽最大的可分 panel，
不在中点重用经验 quadrature 差。两个子界都完成以前，保留旧完整
partition；若第二子界失败，旧完整区间仍有效，并输出已经完成但未
提交的子界，不能把半个积分称为完整。

硬上限如下，不因结果不利而增加：

| 项目 | 固定上限 |
|---|---:|
| 新复目标 | 1 |
| 精度 | 256 bits |
| 根二分 | 160 |
| Taylor 余项阶 | 6 |
| 最终叶 panel | 1024 |
| dyadic 深度 | 20 |
| 新 integrand jet 评价 | 4096 |
| 新入口总钟 | 240 秒 |
| 计算停止到封账的预留 | 10 秒 |
| 数学 stdout | 900,000 bytes |

1024叶最多需要 $4\times1024-16=4080$ 次 jet 评价，低于固定4096额度。
没有额外重复检查额度。若达到叶数、深度、时钟或其它有限门，
原样保留最后完整区间，并标 unresolved；若初始8 panel 尚未完成，
明确标记尚无完整积分区间，不凭已有部分判号。

## 7. 唯一结果门与其数学含义

对当前完整 partition 求和，再加入(9)。
如果最终实部下端 $>0$、实部上端 $<0$、虚部下端 $>0$、
或虚部上端 $<0$ 中任何一个成立，即可输出
`certified-nonzero`。不要求全部四个不等式都成立。

真实下根值是上根值的复共轭，所以同一证明覆盖两根。
接 R471 的必要条件，这会排除**当前固定 cap 与该同一共同商**
的相应 self 成员关系；不会排除换 cap 的整个主课题。

区间包含0只能输出 `unresolved-at-finite-limits`。
它不是零证明，也不授权修改源、延长本次预算或重跑旧四 self。
所有输入失败、域失败、时钟失败及已完成的有限状态进入原 stdout。

## 8. 入口、原输出与 clock

CLI 固定为

```text
python scripts/frozen_psi3_complex_cap_interval_audit.py \
  --request computations/request-frozen-psi3-complex-cap-interval.json \
  --out "$RUNNER_TEMP/visible-frozen-psi3-cap"
```

`--out` 是目录，必须位于 `RUNNER_TEMP`。仅保存一份小的临时 JSON，
不上传 artifact、不缓存数学数组。数学来源和全部结果以原 stdout 为准。

每条 stdout 的前缀为 `FROZEN_PSI3_COMPLEX_CAP_RECORD`，后接封包：

```text
{sequence, kind, payload_bytes_including_lf,
 payload_sha256_including_lf, payload}
```

类型为 INPUT、ROOT、少量 PROGRESS、COMPLETE、FINAL_CLOCK。
COMPLETE 包括全部最终叶的整数界、真实参数、tail界、所有失败、
判据和临时 JSON 的准确 bytes/SHA；没有仅输出一个成功标签。
十进制显示由 Decimal 定向舍入，门判定仍只用整数端点。

进程在所有科学 imports 前启动唯一时钟；输入、源 SHA、参数解析、
求界、输出和临时 JSON 写入都在本次钟内。
FINAL_CLOCK 在完整 COMPLETE 数学输出及临时文件写完后采样，
保原 `15.69076311099991` 秒四 self 账并加本段实际用时。
该关闭旧账的85记录在本轮读取/恢复/计算次数都为0。

工作流由 root 负责：先实际 public/private pull，展示规则 diff、身份和
QUEUE，删除 MR_TOKEN，再 detach 到源提交并运行唯一入口。
报告只需读取这个小 research stdout，无需新的大日志 semantic job。
请求的 `source_sha256` 是入口文件的 SHA 字符串；
工作流其它绑定应另用其自己的字段，不覆盖该字符串。

本源码与参数没有被执行、编译、import、开发测试或本地检查。
首次实际观察不论成功、部分或失败，均完整消费原 stdout；
任何后续新问题必须另立范围和账，不能隐藏在本次未分离结果之后。


原四self首次前置元数据失败0.005253693000000226秒另在request来源回执保留，不冒科学执行；本设计使用的15.69076311099991是原FINAL_CLOCK精确显示值，较早摘要15.690763111仅为舍入。原85记录仍0读取/0重算。
