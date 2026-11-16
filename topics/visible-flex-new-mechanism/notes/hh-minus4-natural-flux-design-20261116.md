# 两个完整负四 hh 自然泛函的最小新观察

日期：2026-11-16。当前为源码和请求设计，尚未执行。依据 [R422](../results/R422-two-term-all-curvature-structure-of-the-minus4-hh-natural-function.md)，只新增两个必要自然泛函，不重做原 pure、响应空间、秩或 forcing。

## 1. 原目标与新工作边界

令 $S=1+k^2$，沿原 $\omega=0$，取完整正规速度二次系数 $\widehat Q_{hh}=Q2_2$。本次两个原 $U_{-4}$ 元素是

$$
V_0=[h^{-6}k^0\omega^0(\log h)^0]\widehat Q_{hh},
\qquad
W=[h^{-6}k^6\omega^0(\log h)^0]\widehat Q_{hh}.
$$

R422 已在人类证明中给出

$$
\mathcal N([h^{-6}]\widehat Q_{hh}(h,k,0))
=S^2\{\mathcal N(V_0)+k^2\mathcal N(W)\}.
$$

这是自然函数层的准确恒等，不是说原 $U$ 元素只有两个系数。此前原 R210 已付这两个元素的完整 pure 坐标，但没有在本轮确认可直接读取其完整正规 mixed 根。原可读输入是 $v^{[2]},N^{[0]},N^{[2]}$ 的全原因子、原 $m_0,m_2$ 矩阵及旧响应根。因此必须新增这两个目标所需的完整 self 自槽装配，并如实计入新工作。

本次不求完整任意角 mixed 公式，不求新的 pure 映射，不求秩；只在原 mixed 公式的真实 self 对角上精确装配，随后做两次完整 $\Omega$。

## 2. 不能省略的正规势项

原完整 normal 是

$$
\widehat Q_{hh}
=[\gamma^2]\{v^{[2]}-B_{m_0}(N^{[2]})
-B_{m_2}(N^{[0]})-\Gamma(m_2)\}
-\partial_h[\alpha]v^{[2]}.
$$

这里 $\gamma=h_s,\alpha=h_{ss}$，$X=\partial_h$。程序扫描原完整几何键；$\gamma^2$ 行按目标状态直接取值，$\alpha$ 行先做原 $h$ 导数后取目标。若原 $\alpha$ 行有 $\log h$，同时保留 $\partial_h\log h=1/h$ 分支。输入已由原 producer 先作真实导数、再取局部历史初值。

R78 原 $K/L$ 公式在 $q=\bar q=u$ 给出

$$
(B_E N)_{-2}(u,u)=-\frac12N(\Phi_E(u,u);u,u).
$$

所以两个正规负势项在 $M_{-2}$ 的 self 中都加上

$$
+\frac12\,m_E\,N(\Phi_E(u,u);u,u).
$$

外槽仍是原非紧 $\Phi_E(u,u)$；其所有左二次尾由保存的实际右锚原积分保留。新代码只代入原 typed 三色表达式的 $a$ 槽，不能用 $N(u;u,u)$ 反猜其外槽，也不能删去单包边项。

R367 的 $C_A/N_2$ 配对只在完整自然泛函加真尾后抵消。**本次不使用该恒等删除任何 raw self 或 pure 项**，再套旧 pure 坐标会错。两条原势都准确进入 self 装配。

## 3. $\Gamma$ 与参考常数的准确缺席

程序从已绑定的原完整 $m_2$ 八坐标矩阵读取所有 scalar 状态，并核其 $h$ 次数均不低于 $-4$。$\Gamma(m_2)$ 是这组 scalar 的固定线性组合，因此没有目标 $h^{-6}$ 项。

对原 $N_0$ 的基准参考值减项，新增的 profile 算子不含 $h,k,\omega,\log h$；乘 $m_2$ 后也只有相同的原 scalar 支撑，所以同样不含 $h^{-6}$。这项缺席是逐几何键的完整证明，不能写成“$N_0$ 左紧”或“尾为零”。程序输出原 $m_2$ 全状态列表和此断言；若支撑发生变化即停止。

## 4. 两条已付 pure 坐标

唯一既付计算入口为 R210：

- run：43688302217；job：132733352458；
- source：1b032593b46210e7a0599a224d5c2110fe1d1606；
- 完整原 stdout：127473 bytes，SHA256 0cdf6ffa15b97cf926dad70b869945a782ee153dac317ec080d1b9d15c9030d6；
- 原 main JSON：53292 bytes，SHA256 aeea36d3c46f934ec784460367813ef7902f85f1c3492e575152fd6906e7a76a；
- 原 metadata receipt：47378 bytes，SHA256 f739e4a0ccdcf5ea102a9deb5794486b8f9f022975764e23fd14b16ec6d722c4。

原 family 下标 $3$ 是 Q2_2。以下坐标对原独立 global 列成立：

| 目标 | normalized 列 | global 列 | 原 scale | 归一 pure SHA256 |
|---|---:|---:|---:|---|
| $V_0$ | 60 | 100 | $-1/512$ | c78a807cad73491058fad4fa02d90b6e39cde3b9e67956dffba5746822adc54d |
| $W$ | 63 | 103 | $-5/512$ | ded90de054ec9adad817d6c189b0c0247a53aee3210884e143e9d3fbacdd38ea |

两条原 MATHEMATICAL_COLUMN 含 LF 的准确 framing 分别为：

- 345 bytes，SHA256 925fb9b481effb95b2ce71bfd50ecf1f2b308d5a2aa80f1c12fa364f6877178e；
- 372 bytes，SHA256 04c01596d395d85a8614341f28533f655971f11c38641cc325470e21d5a92c00。

$V_0$ 的归一坐标依次为

$$
(1,-24),(2,-56),(3,-8),(8,40),(9,8),(12,-14),(14,10),(16,-10).
$$

$W$ 的归一坐标依次为

$$
(0,4),(1,12/5),(2,-156/5),(3,-12/5),(8,192/5),
(9,36/5),(12,-78/5),(14,23/5),(16,-32/5).
$$

各行再乘其原 scale。原 retained-order 把 global $14,16$ 映到旧 R139 下标 $15,17$，其余本次下标不变。合并两目标只需旧列

$$
0,1,2,3,8,9,12,15,17.
$$

程序只读取上述 paid 行及原完成状态；不重运行 R210 或重新正规化旧 pure 差。原 MATHEMATICAL_RESULT 的 family 顺序、retained-order、完成标志和原行 hash 一并绑定。

## 5. 原因子输入与源码

原完整 factor input：

- run 43651096112，source 2259b57065cfad67682f4c4319885fd5334c4f76；
- 目录 notes/actions-43651096112-1-local_fourth_derivative_factors/；
- main local-fourth-derivative-factors.json：5477 bytes，SHA256 42289590f4e8319d2bd4b138497702b701a11c4bcf39ba4c7ed0c2616f3aa927；
- receipt：33580 bytes，SHA256 6857ea6edb3b8132147e3c0c698f79aa6f29e3b59272850267875f45a07fe95e；
- 既有 gzip local-fourth-derivative-factors-original-expressions.json.gz：2132064 bytes，SHA256 9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a；
- 原解压 JSON：11864540 bytes，SHA256 58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。

该输入包含 172 个原 potential 记录及 3802 个原 local 记录，共 3974 个有原 hash 的根。此次只扫描 metadata 来选两目标的必要依赖；逐根名称、原 hash、几何键、角色及有理系数会完整输出。其余根不解码，所有原 forcing/compiler 均不调用。

旧九响应取 R139：

- run 43654534244，source 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b；
- 目录 notes/actions-43654534244-1-g_translation_successor/；
- 既有 gzip G-fifth-translation-original-expressions.json.gz：76352 bytes，SHA256 b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b；
- 原解压 JSON：427950 bytes，SHA256 6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4。

实际读取沿已付 W4 reader，selected-DAG importer 沿原 literature_complete_pure_minus6_projection.py 的独立只读函数；该函数只注册所选根可达的原 atoms，并逐根核原 digest。不调用其研究入口。

新势项收缩先按实际 $E$ 的真实权选 typed 输入，再一次代入 $a=\Phi_E(u,u),b=c=u$。相同 typed hash 与 $E$ 跨两目标共用缓存。这里的必要 input extraction 和新自槽收缩单列计数，不能假记为已保存的完整 mixed 根恢复。

## 6. 新 $\Omega$ 的完整性与判据

给目标减去其已付 pure 响应，得到 $\pi\widehat V=0$，且自然泛函不因响应改变。程序完整装配的 self 正是

$$
\widehat V(u^2,0)=-4\,M_{-2}^{\widehat V}(u,u).
$$

只在 complete self 之后调用 frozen R406 mapper：

$$
\Omega_u(\widehat V)
=-4\int u'''M_{-2}^{\widehat V}(u,u)
=4\left[I_r^x\!\left(u'''M_{-2}^{\widehat V}(u,u)\right)\right]_{\rm left}.
$$

每个原 $I_r^x$ 保持同一个真实右锚，不改为支撑端，不删除 nested primitives。完整新积分之后才把左 collar 的外部 compact jets 置零；所有字、左多项式及真实常数仍保。

若全左式只余单字常数，则原 single word 的负号给完整局部五次密度 $L$。程序逐项输出 $L$ 和 Euler 多项式；紧 $u$ 的同锚边界给

$$
5\int L=\int u\,\mathrm{Euler}(L).
$$

因而字面 Euler 零严格等价该完整局部泛函恒零。若仍有多字或非恒左多项式，则输出完整余式并标 unresolved；不能把一个非零重写式当作非零泛函。两目标分别报告，不额外求新空间秩或用有限 profile 代替普遍恒等。

## 7. 执行与费用

新入口为 scripts/literature_hh_minus4_natural_flux.py，参数为 --request PATH --out PATH。

请求为 computations/request-hh-minus4-natural-flux.json，薄 workflow 为 .github/workflows/visible-hh-minus4-natural-flux.yml。Python 3.12.14，纯标准库；不装新的数值或符号依赖。

workflow 复用已付规则 reader：先真实 pull public 和 private、读取双 README 并准确核差；随后 detach 请求触发的精确 source commit，逐条核包含新 entry/workflow 在内的全部 source SHA。只有这些完成后才运行新入口一次。凭据不输出，private 凭据在规则读取后立即从环境删除。

资源沿 frozen mapper：120 秒、512 MiB、8192-bit 有理数、100000 terms、300000 IBP calls、250000 cache entries。未预设两函数为零。若预算或实现接口失败，输出有限失败和已完成阶段，不把未计算项当零。

本次新增：

- 两个完整 self 的必要 raw 因子装配与 self-slot 势项收缩；
- 两次新的完整五次总通量映射；
- 仅在全局部时的忠实 Euler 判定。

本次不执行旧 8 checks，不新增重复人工套件，不求旧 pure/self/rank，不重建原 forcing、$N_0/N_2$ producer 或任何旧响应。新开发执行次数为零；源码由静态读审后交唯一公开 Actions。

输出 JSON、完整公式和失败信息只留临时文件并完整打印原公开日志；不上传 artifact、Release 或 payload，不把可重算输出提交 Git，也不创建原输出 blob。只有源码、请求、设计、必要元数据和人类数学结论可进入树。

## 8. 当前结论边界

本设计尚未执行，不能声明 $V_0$ 或 $W$ 自然为零，也不能声明负四 hh 的下降字符已经排除。即使两函数字面非零，还须在已选共同自然查询商中判断其作用，不能从 universal 非零直接推出正字符。

两项若在共同查询中均零，R422 才把该消失传到所有 $k$ 的 hh 槽；随后原 PSD 可消混合槽。完整负四 kk 仍由独立原式工作承担。这里不授实际 joint 截面、全部 period 或主问题完成。
