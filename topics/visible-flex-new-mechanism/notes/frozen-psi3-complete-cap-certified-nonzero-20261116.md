# 冻结 ψ3 的完整复帽积分：一次严格区间观察为非零

## 已得到的结论及准确范围

公开仓库自己的 [run 43827984553](https://github.com/Rogerhu12/math-research-public/actions/runs/43827984553)、research job 133166230952，在 source **5104179cb2ce1131f849ce0b2a224a021691d91c** 完成唯一新目标。原 COMPLETE 的状态是 **certified-nonzero**。包括真实左平端尾、Af 根位置、复参数和可变上限的完整区间为

\[
\begin{aligned}
\operatorname{Im} E(z_+)&\in[
1.7333041007120258150943981724950880627810814679655\,10^{-16},
3.5283382087782635540047858686117238247059736454616\,10^{-16}],\\
\operatorname{Re} E(z_+)&\in[
-2.7770312685826872205565755267638598437636506046815\,10^{-16},
4.2866225832793890132114275253521726176985468184299\,10^{-18}].
\end{aligned}
\]

虚部的严格正号已经足够；实部区间仍跨零，不另声称实部的号。下根值为共轭，故也非零。这里是 [R455](../results/R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) 冻结的正幅、正仿射 ψ3 单侧 cap，不是任取的新 cap；原相应协变因子为正 \(A_{\rm amp}^5H^{-2}\)，因此该非零性传到 R455 的实际幅宽。

[R471](../results/R471-five-real-cap-conditions-and-the-complete-complex-second-moment-interface.md) 的四局部列共同含原二矩多项式因子，因此这个完整 \(E\ne0\) 排除了**该冻结母库**的 \(\mathfrak h\in\operatorname{span}\mathfrak y\)。[R466](../results/R466-complete-mirror-anchor-identity-and-enhanced-minus6-minus4-cone-reduction.md) 的准确推论须保同一个完整 \(J_{\rm aff}\) 和 canonical 正时长、同端口、\(M=0\) 成本条件：在其假设下存在正字符分离，不能实现该 \(J_{\rm aff}=0\) 的 actual 正时长成本。不能把它扩大为只固定宽 \(F=0\) 的所有成本障碍，不能排另一新帽区、另一完整母库或未列的新机制，也不证明主课题的一般刚性。

这条观察关闭“当前冻结 ψ3 的完整复积分是否为零”子问题。后续继续真实允许 cap 的五门共同零目标和新的完整路径接口；不重新执行这一已判非零的目标。

## 唯一执行所用的原数学对象

令
\[
u(x)=e^{-3/(1-x^2)},\quad d=1-x^2,\quad
P(x)=3x^4+4x^2-1.
\]
原 \(A_f=6u'u'''-2(u'')^2\) 的唯一相关负根是
\(T=-a\)，其中 \(a=\sqrt\alpha\)，而 \(\alpha\) 是
\[
27t^4+102t^3-46t^2-10t-1=0
\]
的唯一正根。原有理夹为 \([11/20,3/5]\)，Descartes 一次号变和端点严格异号给唯一性，执行做了 160 次准确有理二分。

在末根使用原归一比
\[
s=\frac{a(1-\alpha)^2}{3\alpha^2+4\alpha-1},\qquad
h=\frac{(1-\alpha)^4}{6(3\alpha^2+4\alpha-1)},\qquad
\delta=\sqrt{2h-s^2}>0.
\]
计算包入的近似位置是 \(a\approx0.7538795482888717589\)，
\(s\approx0.06264603905377009323\)，
\(h\approx0.002580687032573252132\)，
\(\delta\approx0.03516884780626195814\)；这些打印近似不充当误差界，原 ROOT 保存有向定点整数端点。

置 \(z=a+s+i\delta\)、\(\zeta=x+z\)，并记
\[
B=xd^2+\zeta P(x),\qquad
C=d^4+6x\zeta d^2+3\zeta^2P(x).
\]
原完整 E 的积分密度准确为
\[
1944\,e^{-15/d}\,
 \frac{\zeta^2x(1-2x^2)(x^4+4x^2+1)B^2C^2}{d^{22}},
 \qquad -1<x<T .
\]
它来自 R471 的完整单侧 primitive，末端局部项已由原二矩根关系准确抵消；没有另删 cap 常数、整包尾或有序历史。

## 为什么输出是包含完整积分的界

预先公开的 [设计](frozen-psi3-complex-cap-interval-design-20261116.md) 与源码完整规定以下有限过程。此次没有增加参数、细化额度或重试。

在 \([-1,-19/20]\) 上，原解析单调界把每个实分量的未求积尾包入 \(\pm\varepsilon_{\rm tail}\)，其中此次
\[
0\le\varepsilon_{\rm tail}\le
1.6606845818682220665123793393325407702132629803537\,10^{-34}.
\]
该界使用 \(d_c=39/400\)、长度 \(1/20\) 和
\(e^{-15/d}d^{-22}\) 的单调性 \(15-22d>0\)。平端未被当成准确零而截去。

剩余区间通过 \(x=-19/20+(T+19/20)y\)、\(0\le y\le1\) 处理，根和复参数的不确定性进入同一全部区间运算。所有标量端点是分母 \(2^{256}\) 的有向整数；乘除向外取整，平方根用整数平方根向外包入。负指数先缩小 512 倍，以 47/48 阶交错式包入后做九次区间平方。每个求积面板保留中点 jet 的 0、2、4 次积分，并用**整个面板**上六阶 jet 区间乘 \(2r^7/7\) 包住余项；没有把点采样差当作误差估计。

此次完整分割使用 **25 个叶面板**，共完成 42 个面板包含计算、84 次 integrand jet、17 次拆分和 170 个指数端点界；其中 8 个初始面板与 17 次实际拆分组成完整叶覆盖。原 COMPLETE 保存全部小叶证书，尚未提交子区间为空，最终包含上述两完整分量区间。根与复参数统一包入标记为真，tail 已加到两分量。

该精度已足够判虚部正，无须用剩余额度再计算。任务额度仍是预定新 240 秒、至多 1024 叶、4096 jet、最大深度 20、stdout 900000 字节，均未扩充。

## 来源、身份及实际费用

原研究 stdout 的原始 UTF-8 job log 为 **116962 B**，SHA256
**c5de2447d0304ffb1d5d3d27923b7800c88e84ad82644a6ffe65f9277a90ebac**。
原 envelope 各 payload 的 JSON 加 LF 身份如下；不在 Git、artifact、Release 或 cache 复制机器证书。

| 原记录 | sequence | B | SHA256 |
|---|---:|---:|---|
| INPUT | 0 | 1555 | 0f8e2984b375db746c74564428b0a5ed5c3be0c48959deb53c14e7dbebbd43f3 |
| ROOT | 1 | 3847 | 373cd16e7aa1e7ff509d74a115376a22388e70404cef15ce6d2ee77c17191dd4 |
| COMPLETE | 2 | 17398 | a3606eae0f9294f478a41cb70265aa27229d1deb9c17c1695480073dd293f741 |
| FINAL_CLOCK | 3 | 830 | 4bc0f79e76606dc667fd1c0fe98bfb2f064ad2823c7d7d829a99e4486b427c8a |

runner 临时 result JSON 为 17112 B / 92575191f8ce7e988add95a404bcc856272a732f1a460bc2744c3e94e4d5c127，只作为同次原输出对象，未上传。原 source script 30193 B / e8bd874e3a88ec8b311d7f2ae488f2aa8bdcbdd8e008034766b24272f0ad3baf；request 3934 B / e6ce88a7e9f086e8dff280ebbab17cf6485c26605de22fd018509031f6acd4ee；完整设计 11186 B / 4f4e88904a75462f3bb0d9c1156a183dacec42ec793a4f2dc09f95663c66b0a0。

最终时钟在 COMPLETE 输出之后取样，**本新科学 0.3593075210000052 秒**，1 个新复帽目标，失败 0、开发执行 0、旧 self 重算 0、旧 response/rank 0。保留旧四 self 的精确已付科学 15.69076311099991 秒后，总计 **16.0500706319999152 秒**。旧前置 metadata 失败 0.005253693000000226 秒仍在旧来源中单列，不冒充本次科学或丢弃。没有重读旧 85 条科学记录。

此次 Actions 在研究前做真实双 pull：

- 公开 08:01:54.946053→08:01:55.380782 UTC，before=after 5104179cb2ce1131f849ce0b2a224a021691d91c；根 README blob 21bd547f56590b7f2dd279d0297efb289a9b2783、课题 README blob d0432faff569c8e9af7ed4809847e12880976c11 均空 diff，返回码 0。
- 私有 08:01:57.690578→08:01:58.282958 UTC，before=after d1f36084ccf101b5221045bf61ec36eaca405d39；根 README 不变、该私有目录无课题 README，QUEUE 中会话 Astra-new-mechanism-9974ea84 唯一进行中。私有正文不发表。

## 接续的实际问题

[R481](../results/R481-polynomial-flat-tail-regularity-for-all-five-cap-conditions.md) 已付每个允许精确平端 cap 的五门处处满秩与一次有限径向下降，但还未付达到零的全局边界控制。当前继续该真允许类中的完整零目标；R479 的多 cap 共同系数条件仍保留。R480 所选全第三外矩的新库仍须与最终 actual 成本、单份内部 ruling、同一个 13 核规范相容，旧冻结库结果不跨库移植。

主几何分支仍在同一 g/b0 和点53上继续新的增广交换主问题。以上严格区间只关闭一个具体 cap 子问题，没有支付固定 g 的 C² 连续嵌入族、全时 reach、握持直径、宏观位移或 \(10^{-6}\) 度量精化门；不据此收尾主课题。
