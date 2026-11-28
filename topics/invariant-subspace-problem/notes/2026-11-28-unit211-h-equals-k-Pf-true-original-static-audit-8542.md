# h=k 原 Pf 单位链：纠正后四直接源与完整等权前置链静审

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**性质：静态来源审计，未执行任何旧数学源、结式、Bézout 或资源门。**
本记录恢复既有原定理在当前正确碰撞图中的应用；不将旧排除重登记为新计算。

结论是当前原 unit211 的整个 $h_U=k_U$ 图可支付
$$
P_f=T_0(J-Q)\ne0.
$$
四份直接源码均使用真双点乘法，完整前置等权链也已核清。
因此正确的 $\Delta=0$ 十七阶覆盖不再留下未付的 $P_f=0$ 面。
这不关闭 $h_U=k_U$，不处理其一般 $\Delta\ne0$ 余图，也不恢复错误旧第二曲线或旧全局覆盖。

## 1. 当前同一点原参数与真正均值

写
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,
$$
$$
h_U=k_U=1+\xi,\quad
w=\lambda-1-T,\quad
S=2\xi+3-2\lambda,\quad \eta=\xi+3-2\lambda,
$$
$$
p=1+\rho,\quad q=1-\rho,\quad Q=1-\rho^2,\quad
u=bp+cq,\quad b+c=\ell.
$$
这些是原二、三值矩的碰撞参数；$h_U=k_U=1$ 的独立原排除保留。
原 $A,B,Q,1-Q,bc,P_{02},\lambda$ 及已审的 $S$ 单位按各自原范围使用。
$u=0$ 使用已审原归一化传回；对称 $u=1$ 使用后来真正独立的整支原证明，
不把旧非对称坐标 $u'=1$ 当作这一点。

四直接源都明写
$$
\operatorname{vm}(v,z)_1=v_0z_1+v_1z_0,
\qquad
-2\operatorname{vm}(d,d)_1=-4d_0d_1.
$$
完整 $N_4,P_2$、原极化、两个 singleton 值目标与八个原行都由同一 Gram 构造。
未借用错误 compact 均值的 $-2d_1^2$。

准确两仿射行是
$$
P_c+P_ff+bcQ\Phi t=0,\qquad
N_C+N_Ff+bcQS\xi t=0,
$$
其中
$$
T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,
$$
$$
G_0=\lambda P_{02}+(u-1)T_0,\quad
P_c=QP_{02}(\ell+T)-G_0T_0,
$$
$$
N_F=(3-4\lambda)Q+J\xi\eta,\quad
N_C=\eta(-G_0\xi+Qwu),\quad
\Delta=\Phi N_F-S\xi P_f.
$$
这两行来源不依赖错误 compact 行；本次只核其已成原来源。

## 2. 前置等权整支必须是四源链

[完整等权四源静审](2026-11-28-unit211-h-equals-k-equal-weight-four-source-static-audit-8542.md)
由 r150_open_geometry 全文核四份原代码、结果和既有实际回执，root 再核其完整覆盖说明。
先前把三源说成整支完成的简短描述已在该记录明确更正：

- $\Delta=0$：6f3b 的原相容二十次覆盖，加 3f51 在整个常数代数中的原 $Q$ 恢复和自由 $f$ 八行返回；
- $\Delta\ne0$：8d6c 只给 F96 必要覆盖，必须再接 b84e/f5e 的四个完整常数域返回。

后者既有 run46005327745/job140526939140 返回四域：
两域的原 gcd 为 $Q-1$，第三域直接为 $1$，
第四域的二次 gcd 两层都实际整除该域原 $\Delta$ 分子，再由该图 $\Delta\ne0$ 排除。
全部 141 次常数逆、94 次 $Q$ 除法和原标签乘回已在旧成功中完成；
没有把 F96 的必要覆盖本身当排空。

四源既没有倒待证 $u-\ell$，也不引用后继 $T_0/J=Q$ 排除。
它们由碰撞自己的原系统支付整个等权支，故 $u-\ell\ne0$ 的前置使用不循环。
独立 $S=0$ 原链参见
[此前完整来源审计](2026-11-28-hk-Szero-true-original-static-source-audit-8542.md)。
本段没有借不同值图 $D\ne0$ 上的等权结论。

## 3. T0 的两个完整 Delta 图

### T0=0、Delta=0

原 $T_0=0$ 给
$$
Q=\frac{2u(1-u)}{\ell},\quad
bc=\frac{u^2(2\ell-1)}{4(1-Q)},\quad
P_{02}=uQ(2\ell-1),\quad
\Phi=\frac{2(u-1)(2\ell-u)}{\ell}.
$$
这里 $Q\ell\ne0$ 直接付 $u(u-1)\ne0$。
原第一仿射行及
$$
\ell+T=\frac{A^2\lambda(2\lambda-1)^2}{B^2}
$$
付 $\Phi\ne0$；$\lambda=1/2$ 使用已成的真正原整支排除。
此后
$$
N_F=Q\frac{(3\lambda-1)(2\lambda-1)}B,\qquad
\Delta=\Phi N_F.
$$
所以该整零面迫 $\lambda=1/3$。原第二仿射行唯一迫
$u=125/123,\ Q=-784/15129$，实际 $\Phi=200/15129$。
仍保自由 Gram 参数 $f$，真原单点均值有
$$
E_{Be}=\frac{2605898}{4412625}-\frac{4406}{2583}f,\qquad
E_{Bo}=-\frac{29258}{35875}+\frac{50}{21}f,
$$
$$
E_{Be}+\frac{2203}{3075}E_{Bo}
=\frac{32956}{5253125}\ne0.
$$
这覆盖整个该面，没有倒 $\Delta$ 或 $N_F$。
原文是
[整个 T0/Delta 同零面](../results/R150-appendix-unit211-equal-singleton-T0-Delta-zero-complete-original-exclusion.md)。

### T0=0、Delta 非零

互补面由原两仿射行恢复 $f,t$；
$\Phi,N_F$ 的逆只在本 $\Delta=\Phi N_F\ne0$ 图内使用。
55898 源直接重建未缩放八原行。
其两个固定次数结式保所有参数首项零，实际 QQ 原余式次数为 28、12，
并已返回一元 Bézout 常数 $1$。
剥除中的 $u-\ell$ 由第 2 节四源完整链支付，其余分母仅为本图已付支持。

由此可恢复
[整个碰撞 T0 非零](../results/R150-appendix-unit211-equal-singleton-entire-T0-zero-original-exclusion.md)
的既有结论。没有把旧不同值图的 T0 定理运输过来。

## 4. J=Q 的两个完整 Delta 图

在 $J=Q$ 上，若 $\ell=1$ 则 $u=0$ 或 $u=1$；
前者由原 $u=0$ 链、后者由当前真正对称 $u=1$ 整支原证明排除。
所以本面可用 $\ell-1$，并有
$$
Q=\frac{2u(u-1)}{\ell-1},\quad
T_0=Q(1-2\ell),\quad
P_{02}=2(1-u)T_0,\quad
\Phi=-4(u-1)^2.
$$
这里 $P_{02}\ne0$ 也直接付 $u-1$ 与 $T_0$，
并非用待证 $J-Q$ 或在其零面倒 $P_f$。

又
$$
N_F=Q(1-2\lambda)(3\lambda^2-3\lambda+1)/A^2,\qquad
\Delta=\Phi N_F.
$$
$\Delta=0$ 时，去掉已独立关闭的半值，保整个
$K=\mathbb Q[\lambda]/(\lambda^2-\lambda+1/3)$。
原 $N_C=0$ 的 $u$ 系数在整个 K 中真正可逆，
其关键系数范数 $122-243\lambda$ 为 4921。
它给唯一
$$
u=(58-70\lambda)/19,\qquad
Q=-3872/1083+4188\lambda/361.
$$
c673 源保完整 K 和自由 $f$，真原 E1/EBe 的 Bézout 返回 $1$；
29 次常数逆、4 次多项式除法均为既有实际返回，未选单个嵌入。

$\Delta\ne0$ 时，d3d7 源从原两行恢复同一 $f,t$，
重建真八原行；两个固定 $u$ 结式的实际 QQ 核为 60、33 次，
完整 Bézout 返回 $1$。
其 $u-\ell$ 仍由第 2 节四源链支付；全部中间头零面保留。

这恢复
[整个碰撞 J=Q 排除](../results/R150-appendix-unit211-equal-singleton-entire-JQ-zero-original-exclusion.md)
的既有结论，并与第 3 节合成 $P_f\ne0$。

## 5. 四直接源的不可变身份和原运行

root 已全文读完以下四直接源；这里只记录旧成功，不给它们新运行时间或新完成标签。

| 整原面 | Git blob | UTF-8 SHA256 |
| --- | --- | --- |
| T0=0, Delta=0 | 6aee162135c5c7edace4e78a33a3af8c5eaac5c8 |402d5ce112bbd862d8eaedc5a2447f058bb097d229c6621d5daf04203108dd97|
| T0=0, Delta 非零 |55898c9cc67257b5e22fbd5fe0af851bfbaee0c3|031d1737a60b359ffd82231b374efec96232fdc64ceda551aa55d91fe39d1bba|
| J=Q, Delta=0 |c673e4e4e690a7ced602ef5d3f5f2ea9c1dc3f05|f7c64310689e077bfb2b6aaea57bdefd724a9f01ca9b38b5266a72935f80e08c|
| J=Q, Delta 非零 |d3d7a611e32c9074a32fc93c0238c81b3a3689d9|57a419da9e60bd135f1a41943604889f1e62e67a16239d87c0c9560f84a8a92e|

原文件：

- [T0 同零源](2026-11-27-unit211-equal-singleton-T0-Delta-zero-complete-original-rational-return-8542.py)；
- [T0 非零 Delta 源](2026-11-27-unit211-equal-singleton-T0-nonzero-Delta-original-two-parameter-return-8542.py)；
- [JQ 同零源](2026-11-27-unit211-equal-singleton-JQ-Delta-zero-complete-quadratic-original-return-8542.py)；
- [JQ 非零 Delta 源](2026-11-27-unit211-equal-singleton-JQ-nonzero-Delta-original-two-parameter-return-8542.py)。

| 原成功 run/job | 驱动秒 | RSS KiB | 退出 |
| --- | ---: | ---: | ---: |
|46010648548 / 140544983517|0.120085485|37448|0|
|46011596196 / 140548221367|0.222151756|41044|0|
|46013488114 / 140554634214|0.088397285|34568|0|
|46013953380 / 140556219747|0.349964772|41064|0|

原实现失败与各原回执继续保留，不重新运行。
静审只能恢复上述实际由真原式完成的定理，不能给任何冻结任务补成成功。

## 6. 当前正确 Delta 零覆盖的准确范围

现在
[正确五原行](../results/R150-appendix-unit211-h-equals-k-corrected-five-original-rows-and-three-physical-cofactor-conditions.md)
所用 $P_f$ 已在整个碰撞图支付。
所以
[正确十七阶与 5640 点界](../results/R150-appendix-unit211-h-equals-k-corrected-fixed-seventeen-lambda-cover-and-5640-points.md)
覆盖整个当前 $h_U=k_U,\Delta=0$ 的原点，而非只覆盖额外开的 $P_f\ne0$ 子图。

实际仍是 716 次固定行列式只剥已付支持后得 470 次，
不同 $\lambda$ 至多 406，保重数给至多 470 个 $(\lambda,u)$，
完整 $Q$ 至多 2、Loww 的 $z$ 至多 3、两 $\rho$ 给至多 5640 个不同有序规范点。
这只是有限原候选覆盖；候选排空仍待处理。

旧 848/578、错误七个 lambda 全覆盖、错误 compact 的其它结果和 dc888 冻结尾均不恢复。
各固定小 lambda 的正确原纤维可另作条件来源审计；
不能用旧错误覆盖断言它们已经穷尽本次候选。
