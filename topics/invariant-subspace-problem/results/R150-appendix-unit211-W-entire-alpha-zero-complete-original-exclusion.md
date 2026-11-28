# R150：整个当前 W 的 $\alpha=0$ 原支排除

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。AI-assisted，GPT-6 Astra Pro。

## 1. 完整结论与适用域

沿当前 W 的原权单位图，记
$$
\eta=f-u,\qquad
\delta=1-Q,\qquad \widehat U=u-\ell Q,\qquad
\alpha=4\delta\eta-\widehat U t.
$$
整个 $t=0$ 和整个 $f=u$ 已分别由 [原 $t=0$ 定理](R150-appendix-unit211-W-entire-t-zero-complete-original-exclusion.md) 与 [原 $f=u$ 定理](R150-appendix-unit211-W-entire-f-equals-u-complete-original-exclusion.md) 排除。

**定理。整个当前 W 的 $\alpha=0$ 原支为空。**

证明保留所有原 $e$ 首项退化、完整 QQ 二次权域的两个嵌入以及此前覆盖的全部四重幂零层。没有使用数值根、有限域判空或额外物理 $D$ 的逆。

因此在整个当前 W 原物理商中可以支付 $\alpha$。取已付
$$
s=t/\eta,\qquad \gamma=4\delta-\widehat U s,
$$
便有 $\alpha=\eta\gamma$，所以整个剩余 W 都落在 $s\gamma\ne0$ 图。既有全 $\gamma$ 首一 $f^2$ 结论由此覆盖全部当前剩余 W；这仍不是整个 W 排空，也不扩大先前关于一般几何局部化的有限自由结论。

本定理仅用于已经列明原单位的当前 W、原两 singleton 值互异的 $D\ne0$ 图，不移植到一般 $h=k$ 碰撞图。

## 2. 已刊四重权覆盖与原恢复

当前 W 权坐标为
$$
u=e+1,\quad Q=ek,\quad V_b=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV_b}.
$$
另记
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
M=\ell V_2-u^2,\quad m=u-\ell.
$$
在 $\alpha=0$ 上，已刊原均值恒等式给出整支恢复
$$
t=-\frac{2(1-Q)((k+2)^2-2Q)}{(k+2)(Q-2)},\qquad
f=u+\frac{\widehat U t}{4(1-Q)},
$$
$$
W_1=(T_0+4uf)/2,\quad V=bX+cY,
$$
$$
x=\frac{\widehat U V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
\tag{1}
$$
全部分母已经支付，唯一剩余 Gram 参数是同一个 $V$。$\widehat U$ 在本支由 $\widehat Ut=4\delta\eta$ 及 $t\eta\delta$ 已付而为单位；不向整个 W 无条件外推这个单位。

[整个 $\alpha=0$ 的 F8 原覆盖](R150-appendix-unit211-W-alpha-zero-F8-whole-original-cover.md) 已由四个固定原 $V$ 结式、两个固定原 $e$ 结式和完整 QQ Bézout 证明
$$
\phi(k)^4\in I_\alpha,\qquad \phi(k)=k^2+8k+8.
\tag{2}
$$
这里 $I_\alpha$ 是原权局部化后的同点原条件理想。固定 Sylvester 的 adjugate 身份保留各次首项零面，已付因子剥除和最后 QQ Bézout 保留理想来源。式 (2) 不只是一个数值候选列表。

本次没有重算这些结式或因式分解，只使用准确的小参数 $[8,8,1]$；其规范 SHA256 为 9526e32c263849d71edfb1f466d3871c3b56b7484047221b42480bb470bf279b。

## 3. 整个 QQ 二次域与原八行二列

取
$$
K=\mathbb Q[k]/(k^2+8k+8),\qquad A=K[e].
$$
判别式 $32$ 非平方，故 $K$ 是完整二次域。每次逆使用
$$
(a+bk)^{-1}=\frac{a-8b-bk}{a^2-8ab+8b^2},
$$
并实际检查左右乘回 $1$。不选择一个嵌入，不对任意 $e$ 多项式取域逆。

同点真实 Gram 的五原式取
$$
Q_0=EW,\quad Q_1=E_B^{\rm odd},\quad Q_2=N_1,\quad
Q_3=Low_w,\quad Q_4=NS.
\tag{3}
$$
其来源保留完整真 dual 乘法，且已有
$$
E_1=EW,\qquad Low_w=NS-PS+E_{W2}.
$$
所以原均值和 (3) 保留两个完整原加权 N/P 条件。

原二次首项是
$$
[V^2]E_B^{\rm odd}=-4x_Vy_V=\frac{4u\widehat U}{M^2}.
\tag{4}
$$
新源从完整原式抽出并返回 (4)，同时把所有分母及付清原单位后的二次首项逐项支付。实际专门化后的五个 $V$ 次数为 $2,2,2,2,3$，$e$ 次数为 $12,14,15,14,21$。原二次 $Q_1$ 的多项式 $V^2$ 首项对 $e$ 八次，其支持由 $V_b,Q-2,\widehat U$ 的已付原因子排尽。

记 $q=Q_1=aV^2+bV+c$，其中 $a$ 只在已说明的原权局部化中为单位。源码在 $A[V]$ 中使用正幂伪除法：
$$
a^{n_i}Q_i-H_iq=r_{i0}+r_{i1}V\qquad(i\ne1),
$$
$$
aV(r_{i0}+r_{i1}V)-r_{i1}q.
\tag{5}
$$
式 (5) 共八个一次行，全部携带五原式的多项式组合并实际回乘。没有倒任何 $e$ 首项，也没有依赖泛型次数。

八行的实际 $e$ 列次数为
$$
(21,18),(32,29),(24,21),(35,32),
(23,20),(34,31),(38,35),(49,46).
$$
其完整形成只用 0.372715989 秒。

## 4. 两个真正原标量与 $U^{13}$ 返回

对两行 $(r_0,r_1),(s_0,s_1)$，在 $K[e]$ 计算
$$
h=\gcd(r_1,s_1),\qquad
\mu=s_1/h,\quad \nu=-r_1/h.
$$
实际返回全部两列及五原来源：
$$
\mu(r_0,r_1)+\nu(s_0,s_1)=(C,0).
\tag{6}
$$
被约去的只是两个实际乘子的公因子；任何 $h=0$ 的特殊点仍由最终多项式身份 (6) 覆盖。

第一次取行 $(0,1)$，得到 $e$ 三十四次的原标量；只按已付支持处理后仍余十六次，故没有在这里宣称排空。第二次取行 $(0,2)$，得到 $e$ 二十七次原标量。完整 $K[e]$ 扩展 Euclid 及原五源乘回给
$$
g(e)=\sum_{i=0}^4 A_i(e,V)Q_i(e,V),\qquad \deg g=13.
\tag{7}
$$
$g$ 的精确定义 SHA256 为 a05d58e596816954a31d03c7df5bbb19ee24bc1ffc07bbc62c462cf6148eb2ad。

整个 $g$ 的支持只来自下列已付原单位的实际专门化像：
$$
e,\quad u,\quad V_b,\quad \operatorname{num}(M),\quad
\operatorname{num}(\ell),\quad \operatorname{num}(Q-2).
\tag{8}
$$
这不是把 (8) 的乘积错误地写成 $g$ 的完整因式分解。实际记录的是逐项 gcd/精除；各因子可能有公共支持。

令 $U(e)$ 是 (8) 每项取一次的实际乘积，$\deg U=11$。源码还用完整模乘法与除法乘回确认
$$
U(e)^{13}\equiv0\pmod {g(e)}.
\tag{9}
$$
所以 (7)、(9) 给 $U^{13}\in I_\alpha+(\phi)$。$U$ 是原单位，故
$$
1\in I_\alpha+(\phi).
\tag{10}
$$
这个最后步骤没有靠“已经剥完支持”的口头判断，也没有把有限域中的 $D$ 幂零提升到 QQ。全部返回就在完整 QQ 二次域上完成。完整五原组合证书只保定义与 SHA：21056 字节，SHA256 bb4ef2fa31e00e102d05ff96f818ca038666fdd0e8b55d80a061b8eabcdc26ea；可重算大系数不入库。

## 5. 保留原四个幂零层

由 (10)，在原商中可写 $1=i+\phi h$，$i\in I_\alpha$。已有 $\phi^4\in I_\alpha$。因此
$$
1=(1-\phi h)(1+\phi h+(\phi h)^2+(\phi h)^3)+(\phi h)^4
\in I_\alpha.
$$
这完整恢复 (2) 的四重覆盖。没有把 $\phi^4$ 先替换成根式理想，也不需要新增一个有限自由 $e$ 环境。于是整个原 $\alpha=0$ 支被排除，定理成立。

## 6. 实际回执、来源与后续边界

唯一运行：run46113632943，job140882456944。驱动墙钟 0.514844278 秒，峰值 RSS 41612 KiB，内层退出码 $0$。数学末项为 0.448020930 秒。

实际计数为：292 次二次域左右真逆、212 次完整 $K[e]$ 除法乘回、80 次 Bézout、4 次正幂 $V$ 伪除返回、12 次完整五原组合返回、6 次原单位积模幂乘积返回。没有剩余 $e$ 因子、未付头分支或候选根。

源 blob 6ebcbefbb75cc5147209368b4f275b2ef54dc19f；14424 字节，SHA256 98c0618c324db0ba07acf2477857b78b36d8790445b64626ed7f81313d4f85f7。源 basename 为 2026-11-28-unit211-W-alpha-zero-F8-complete-quadratic-original-eight-two-8542.py。

源提交 25278e10a39ec1b589c597de1858151d49a525b3。05:47:04.358836 UTC 真 pull 到 dd9bb4f0adc7acaf52f2098fd5a9027ac9c92ec3，两 README 无变化。stdout 5360 字节，SHA256 bfd2379edf54473388bd2afb5def3cec3029951952a33da9652fa1afcaf9f9c6。

唯一重建依赖是已刊 $\alpha=0$ 同点 Gram/五行源的 8836 字节必要前缀，SHA256 a94137db3b117087205325533fb64cfda913d3dcf1bf1a3485989680b923968e；全部旧四个 $V$ 结式、两个 $e$ 投影及因式分解尾均未执行。

本定理使当前 W 的 $\gamma$ 开图覆盖成为完整覆盖；全 W 其余原条件继续通过新九个二次原系统处理。既有整个 W 的有限性/上界不在本篇重复计为新结论，也不把此分支关闭当作普通 ISP 完成。
