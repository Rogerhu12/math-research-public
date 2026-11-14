# 固定旋转背景的全尾高度总变差粗界

2026-11-09，`/root/tail_theory`。状态：完整条件证明，待独审。与已审背景曲率证明相同，径向 warp 解释为精确积分定义，取使物理宽度归一的精确正参数 $\alpha>0$；这里不从一个浮点正值断言该精确假设已经完成验证。

## 1. 参数条件

考虑当前 `closing_weighted_tail` 固定物理背景，orientation $+1$，无 literal-R20 rejoin，未启用 `flatOuterThroughCell` 覆盖。写 $a_c$ 为 cuff 半径，以免与源指数混淆。`oldCut` 与 `epsilonScale` 按源的精确解析归一化公式派生；这里不把两个独立舍入的派生浮点值之间的等式当作严格解析恒等式。要求

$$0<r_{\rm cut}-a_c<\tfrac12,\quad w_{\rm cut}=\tfrac12,
\quad \tfrac1{200}\le\delta_0\le\tfrac1{160},
\quad0<c_0\le\tfrac1{16}.$$

源指数 $a=11/4$，$\eta$ 指数 $3/2$，$\eta_0=c_0\delta_0$。有限段所有 slope/pulse/valley cap 严格为正且不超过 $1/2$。第 0 cell 的最后过渡段两端 cap 均不超过 $1/49$；最后一平段按 cut-preserving 恢复 raw source。当前二进制参数满足这些有理条件。

从 protectCell 160 起的未修改无限源，采用已审背景证明的全源界 $w_n\le1280\,2^{-7n/4}$，特别是该部分 $w<1/2$。有限部分的 valley 修改只出现在 segments 3、4、5，因此不影响第 0 cell 最后的 segments 7、8 的 raw 公式。

固定背景高度 $h$ 以 $h(a_c)=0$ 归一，且 $h'(r)=w(r)>0$。换成上下镜像或加入整体竖直常数不会改变下面的总变差界。

## 2. 最后 raw 平段的坡度界

设原始源的 cut 半径为 $r_{\rm old}$。其总对数长度满足

$$T=6\delta_0+\frac{6c_0\delta_0}{1-2^{-3/2}}
<\frac6{160}+\frac{12}{16\cdot160}
=\frac{27}{640}.$$

因 $\sqrt{12}>3$，

$$7\log(r_{\rm old}/a_c)=\frac{7T}{\sqrt{12}}
<\frac{63}{640}<\frac1{10}.$$

在第 0 cell 最后 raw 平段，源公式精确给

$$w=\tfrac12(r_{\rm old}/r_{\rm source})^7,
\qquad r_{\rm source}\ge a_c.$$

所以

$$w\le W:=\tfrac12(r_{\rm old}/a_c)^7
<\tfrac12 e^{1/10}\le\frac59<1.$$

最后一步用 $e^x\le(1-x)^{-1}$，$0\le x<1$，可逐项比较指数级数与几何级数得到。

## 3. Cut-preserving 恢复过渡段

令 $t=S(x)\in[0,1]$ 为原五次 smoothstep。源 `cellSegments` 的倒数第二段，其对数平台从 $0$ 到 $\log\delta_0+a\log2$ 线性插值于 $t$。因此它的未 capped 坡度精确满足

$$\log w_{\rm raw}
=\log\left[\tfrac12(r_{\rm old}/r_{\rm source})^7\right]
 +(1-t)B,\qquad B=-\log(\delta_0 2^a).$$

由 $4<2^a<8$ 和 $\delta_0\in[1/200,1/160]$，有 $0<B<4$。其中 $e^4>50$ 可直接用前八个正项 $\sum_{k=0}^7 4^k/k!>50$ 验证，而 $\delta_0 2^a>1/50$。

源 `cap` 函数的输出始终不超过其 cap level：其过渡导数位于 $[0,1]$，并单调从 $c-L$ 到 $c$；超出过渡则等于 raw 或 cap。这是该显式 cap 多项式的直接微分性质。该段的局部 cap 不超过 $1/49$，故

$$\log w_{\rm capped}\le-\log49<-3.$$

Cut-preserving 恢复在对数中恰为

$$\log w=t\log w_{\rm raw}+(1-t)\log w_{\rm capped}.$$

用 $W<1$，得到

$$\log w\le 4t(1-t)-3(1-t)
=-3+7t-4t^2\le\frac1{16}.$$

二次式最大值在 $t=7/8$，因此

$$w\le e^{1/16}\le\frac{16}{15}.$$

这是对该整段的界，不取决于离散采样点。它也说明不能直接用 raw 坡度不超过 cut 坡度来论证：过渡开始的 raw 坡度确实可能较大，必须利用恢复权重与 raw 衰减的同一个 $t$。

## 4. 全尾高度和总变差

其余有限段在 cap 下不超过 $1/2$；最后 raw 平段不超过 $5/9$；未修改无限源不超过 $1/2$。故全部物理尾上

$$0<w(r)\le\frac{16}{15}.$$

因为物理宽度小于 $1/2$，

$$0\le h(r)\le h(r_{\rm cut})
=\int_{a_c}^{r_{\rm cut}}w(r)\,dr
<\frac8{15}<1,$$

$$\int_{a_c}^{r_{\rm cut}}|h'(r)|\,dr<\frac8{15}.$$

若背景另加竖直常数 $z_*$，则只能得到 $|H(r)|\le|z_*|+8/15$；本稿没有从内禀尾参数推断任意外部定位的 $|H_{\rm cut}|\le2$。该绝对高度须由真正前缀接口或单独的竖直锚点界提供。

本证明不使用有限非线性尾的 C² 插值或其误差。它也不证明全候选精确闭合、等距、reach 或 README 完成。
